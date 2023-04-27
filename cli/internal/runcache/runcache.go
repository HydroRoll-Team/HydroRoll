package runcache

import (
	"bufio"
	"context"
	"fmt"
	"io"
	"os"
	"path/filepath"
	"strings"

	"github.com/fatih/color"
	"github.com/hashicorp/go-hclog"
	"github.com/mitchellh/cli"
	"github.com/vercel/turbo/cli/internal/cache"
	"github.com/vercel/turbo/cli/internal/colorcache"
	"github.com/vercel/turbo/cli/internal/fs"
	"github.com/vercel/turbo/cli/internal/globby"
	"github.com/vercel/turbo/cli/internal/logstreamer"
	"github.com/vercel/turbo/cli/internal/nodes"
	"github.com/vercel/turbo/cli/internal/turbopath"
	"github.com/vercel/turbo/cli/internal/ui"
	"github.com/vercel/turbo/cli/internal/util"
)

// LogReplayer is a function that is responsible for replaying the contents of a given log file
type LogReplayer = func(logger hclog.Logger, output *cli.PrefixedUi, logFile turbopath.AbsoluteSystemPath)

// Opts holds the configurable options for a RunCache instance
type Opts struct {
	SkipReads              bool
	SkipWrites             bool
	TaskOutputModeOverride *util.TaskOutputMode
	LogReplayer            LogReplayer
	OutputWatcher          OutputWatcher
}

// SetTaskOutputMode parses the task output mode from string and then sets it in opts
func (opts *Opts) SetTaskOutputMode(value string) error {
	outputMode, err := util.FromTaskOutputModeString(value)
	if err != nil {
		return fmt.Errorf("must be one of \"%v\"", TaskOutputModes())
	}
	opts.TaskOutputModeOverride = &outputMode
	return nil
}

// TaskOutputModes creates the description string for task outputs
func TaskOutputModes() string {
	var builder strings.Builder

	first := true
	for _, mode := range util.TaskOutputModeStrings {
		if !first {
			builder.WriteString("|")
		}
		first = false
		builder.WriteString(string(mode))
	}
	return builder.String()
}

// RunCache represents the interface to the cache for a single `turbo run`
type RunCache struct {
	taskOutputModeOverride *util.TaskOutputMode
	cache                  cache.Cache
	readsDisabled          bool
	writesDisabled         bool
	repoRoot               turbopath.AbsoluteSystemPath
	logReplayer            LogReplayer
	outputWatcher          OutputWatcher
	colorCache             *colorcache.ColorCache
}

// New returns a new instance of RunCache, wrapping the given cache
func New(cache cache.Cache, repoRoot turbopath.AbsoluteSystemPath, opts Opts, colorCache *colorcache.ColorCache) *RunCache {
	rc := &RunCache{
		taskOutputModeOverride: opts.TaskOutputModeOverride,
		cache:                  cache,
		readsDisabled:          opts.SkipReads,
		writesDisabled:         opts.SkipWrites,
		repoRoot:               repoRoot,
		logReplayer:            opts.LogReplayer,
		outputWatcher:          opts.OutputWatcher,
		colorCache:             colorCache,
	}

	if rc.logReplayer == nil {
		rc.logReplayer = defaultLogReplayer
	}
	if rc.outputWatcher == nil {
		rc.outputWatcher = &NoOpOutputWatcher{}
	}
	return rc
}

// TaskCache represents a single task's (package-task?) interface to the RunCache
// and controls access to the task's outputs
type TaskCache struct {
	ExpandedOutputs   []turbopath.AnchoredSystemPath
	rc                *RunCache
	repoRelativeGlobs fs.TaskOutputs
	hash              string
	pt                *nodes.PackageTask
	taskOutputMode    util.TaskOutputMode
	cachingDisabled   bool
	LogFileName       turbopath.AbsoluteSystemPath
}

// RestoreOutputs attempts to restore output for the corresponding task from the cache.
// Returns the cacheStatus, the timeSaved, and error values, so the consumer can understand
// what happened in here.
func (tc *TaskCache) RestoreOutputs(ctx context.Context, prefixedUI *cli.PrefixedUi, progressLogger hclog.Logger) (cache.ItemStatus, int, error) {
	if tc.cachingDisabled || tc.rc.readsDisabled {
		if tc.taskOutputMode != util.NoTaskOutput && tc.taskOutputMode != util.ErrorTaskOutput {
			prefixedUI.Output(fmt.Sprintf("cache bypass, force executing %s", ui.Dim(tc.hash)))
		}
		return cache.ItemStatus{Local: false, Remote: false}, 0, nil
	}

	changedOutputGlobs, err := tc.rc.outputWatcher.GetChangedOutputs(ctx, tc.hash, tc.repoRelativeGlobs.Inclusions)
	if err != nil {
		progressLogger.Warn(fmt.Sprintf("Failed to check if we can skip restoring outputs for %v: %v. Proceeding to check cache", tc.pt.TaskID, err))
		prefixedUI.Warn(ui.Dim(fmt.Sprintf("Failed to check if we can skip restoring outputs for %v: %v. Proceeding to check cache", tc.pt.TaskID, err)))
		changedOutputGlobs = tc.repoRelativeGlobs.Inclusions
	}

	hasChangedOutputs := len(changedOutputGlobs) > 0
	var cacheStatus cache.ItemStatus
	var timeSaved int
	if hasChangedOutputs {
		// Note that we currently don't use the output globs when restoring, but we could in the
		// future to avoid doing unnecessary file I/O. We also need to pass along the exclusion
		// globs as well.
		itemStatus, restoredFiles, duration, err := tc.rc.cache.Fetch(tc.rc.repoRoot, tc.hash, nil)
		hit := itemStatus.Local || itemStatus.Remote
		timeSaved = duration
		tc.ExpandedOutputs = restoredFiles
		// Assign to this variable outside this closure so we can return at the end of the function
		cacheStatus = itemStatus
		if err != nil {
			// If there was an error fetching from cache, we'll say there was no cache hit
			return cache.ItemStatus{Local: false, Remote: false}, 0, err
		} else if !hit {
			if tc.taskOutputMode != util.NoTaskOutput && tc.taskOutputMode != util.ErrorTaskOutput {
				prefixedUI.Output(fmt.Sprintf("cache miss, executing %s", ui.Dim(tc.hash)))
			}
			// If there was no hit, we can also say there was no hit
			return cache.ItemStatus{Local: false, Remote: false}, 0, nil
		}

		if err := tc.rc.outputWatcher.NotifyOutputsWritten(ctx, tc.hash, tc.repoRelativeGlobs); err != nil {
			// Don't fail the whole operation just because we failed to watch the outputs
			prefixedUI.Warn(ui.Dim(fmt.Sprintf("Failed to mark outputs as cached for %v: %v", tc.pt.TaskID, err)))
		}
	} else {
		// If no outputs have changed, that means we have a local cache hit.
		cacheStatus.Local = true
		prefixedUI.Warn(fmt.Sprintf("Skipping cache check for %v, outputs have not changed since previous run.", tc.pt.TaskID))
	}

	switch tc.taskOutputMode {
	// When only showing new task output, cached output should only show the computed hash
	case util.NewTaskOutput:
		fallthrough
	case util.HashTaskOutput:
		prefixedUI.Info(fmt.Sprintf("cache hit, suppressing output %s", ui.Dim(tc.hash)))
	case util.FullTaskOutput:
		progressLogger.Debug("log file", "path", tc.LogFileName)
		prefixedUI.Info(fmt.Sprintf("cache hit, replaying output %s", ui.Dim(tc.hash)))
		tc.ReplayLogFile(prefixedUI, progressLogger)
	case util.ErrorTaskOutput:
		// The task succeeded, so we don't output anything in this case
	default:
		// NoLogs, do not output anything
	}
	// TODO: timeSaved could be part of cacheStatus, so we don't have to make a new struct
	// downstream, but this would be a more invasive change right now.
	return cacheStatus, timeSaved, nil
}

// ReplayLogFile writes out the stored logfile to the terminal
func (tc TaskCache) ReplayLogFile(prefixedUI *cli.PrefixedUi, progressLogger hclog.Logger) {
	if tc.LogFileName.FileExists() {
		tc.rc.logReplayer(progressLogger, prefixedUI, tc.LogFileName)
	}
}

// OnError replays the logfile if --output-mode=errors-only.
// This is called if the task exited with an non-zero error code.
func (tc TaskCache) OnError(terminal *cli.PrefixedUi, logger hclog.Logger) {
	if tc.taskOutputMode == util.ErrorTaskOutput {
		tc.ReplayLogFile(terminal, logger)
	}
}

// nopWriteCloser is modeled after io.NopCloser, which is for Readers
type nopWriteCloser struct {
	io.Writer
}

func (nopWriteCloser) Close() error { return nil }

type fileWriterCloser struct {
	io.Writer
	file  *os.File
	bufio *bufio.Writer
}

func (fwc *fileWriterCloser) Close() error {
	if err := fwc.bufio.Flush(); err != nil {
		return err
	}
	return fwc.file.Close()
}

// OutputWriter creates a sink suitable for handling the output of the command associated
// with this task.
func (tc TaskCache) OutputWriter(prefix string) (io.WriteCloser, error) {
	// an os.Stdout wrapper that will add prefixes before printing to stdout
	stdoutWriter := logstreamer.NewPrettyStdoutWriter(prefix)

	if tc.cachingDisabled || tc.rc.writesDisabled {
		return nopWriteCloser{stdoutWriter}, nil
	}
	// Setup log file
	if err := tc.LogFileName.EnsureDir(); err != nil {
		return nil, err
	}

	output, err := tc.LogFileName.Create()
	if err != nil {
		return nil, err
	}

	bufWriter := bufio.NewWriter(output)
	fwc := &fileWriterCloser{
		file:  output,
		bufio: bufWriter,
	}
	if tc.taskOutputMode == util.NoTaskOutput || tc.taskOutputMode == util.HashTaskOutput || tc.taskOutputMode == util.ErrorTaskOutput {
		// only write to log file, not to stdout
		fwc.Writer = bufWriter
	} else {
		fwc.Writer = io.MultiWriter(stdoutWriter, bufWriter)
	}

	return fwc, nil
}

var _emptyIgnore []string

// SaveOutputs is responsible for saving the outputs of task to the cache, after the task has completed
func (tc *TaskCache) SaveOutputs(ctx context.Context, logger hclog.Logger, terminal cli.Ui, duration int) error {
	if tc.cachingDisabled || tc.rc.writesDisabled {
		return nil
	}

	logger.Debug("caching output", "outputs", tc.repoRelativeGlobs)

	filesToBeCached, err := globby.GlobAll(tc.rc.repoRoot.ToStringDuringMigration(), tc.repoRelativeGlobs.Inclusions, tc.repoRelativeGlobs.Exclusions)
	if err != nil {
		return err
	}

	relativePaths := make([]turbopath.AnchoredSystemPath, len(filesToBeCached))

	for index, value := range filesToBeCached {
		relativePath, err := tc.rc.repoRoot.RelativePathString(value)
		if err != nil {
			logger.Error(fmt.Sprintf("error: %v", err))
			terminal.Error(fmt.Sprintf("%s%s", ui.ERROR_PREFIX, color.RedString(" %v", fmt.Errorf("File path cannot be made relative: %w", err))))
			continue
		}
		relativePaths[index] = fs.UnsafeToAnchoredSystemPath(relativePath)
	}

	if err = tc.rc.cache.Put(tc.rc.repoRoot, tc.hash, duration, relativePaths); err != nil {
		return err
	}
	err = tc.rc.outputWatcher.NotifyOutputsWritten(ctx, tc.hash, tc.repoRelativeGlobs)
	if err != nil {
		// Don't fail the cache write because we also failed to record it, we will just do
		// extra I/O in the future restoring files that haven't changed from cache
		logger.Warn(fmt.Sprintf("Failed to mark outputs as cached for %v: %v", tc.pt.TaskID, err))
		terminal.Warn(ui.Dim(fmt.Sprintf("Failed to mark outputs as cached for %v: %v", tc.pt.TaskID, err)))
	}

	tc.ExpandedOutputs = relativePaths

	return nil
}

// TaskCache returns a TaskCache instance, providing an interface to the underlying cache specific
// to this run and the given PackageTask
func (rc *RunCache) TaskCache(pt *nodes.PackageTask, hash string) TaskCache {
	logFileName := rc.repoRoot.UntypedJoin(pt.LogFile)
	hashableOutputs := pt.HashableOutputs()
	repoRelativeGlobs := fs.TaskOutputs{
		Inclusions: make([]string, len(hashableOutputs.Inclusions)),
		Exclusions: make([]string, len(hashableOutputs.Exclusions)),
	}

	for index, output := range hashableOutputs.Inclusions {
		repoRelativeGlobs.Inclusions[index] = filepath.Join(pt.Pkg.Dir.ToStringDuringMigration(), output)
	}
	for index, output := range hashableOutputs.Exclusions {
		repoRelativeGlobs.Exclusions[index] = filepath.Join(pt.Pkg.Dir.ToStringDuringMigration(), output)
	}

	taskOutputMode := pt.TaskDefinition.OutputMode
	if rc.taskOutputModeOverride != nil {
		taskOutputMode = *rc.taskOutputModeOverride
	}

	return TaskCache{
		ExpandedOutputs:   []turbopath.AnchoredSystemPath{},
		rc:                rc,
		repoRelativeGlobs: repoRelativeGlobs,
		hash:              hash,
		pt:                pt,
		taskOutputMode:    taskOutputMode,
		cachingDisabled:   !pt.TaskDefinition.ShouldCache,
		LogFileName:       logFileName,
	}
}

// defaultLogReplayer will try to replay logs back to the given Ui instance
func defaultLogReplayer(logger hclog.Logger, output *cli.PrefixedUi, logFileName turbopath.AbsoluteSystemPath) {
	logger.Debug("start replaying logs")
	f, err := logFileName.Open()
	if err != nil {
		output.Warn(fmt.Sprintf("error reading logs: %v", err))
		logger.Error(fmt.Sprintf("error reading logs: %v", err.Error()))
	}
	defer func() { _ = f.Close() }()
	scan := bufio.NewScanner(f)
	for scan.Scan() {
		str := string(scan.Bytes())
		// cli.PrefixedUi won't prefix empty strings (it'll just print them as empty strings).
		// So if we have a blank string, we'll just output the string here, instead of passing
		// it onto the PrefixedUi.
		if str == "" {
			// Just output the prefix if the current line is a blank string
			// Note: output.OutputPrefix is also a colored prefix already
			output.Ui.Output(output.OutputPrefix)
		} else {
			// Writing to Stdout
			output.Output(str)
		}

	}
	logger.Debug("finish replaying logs")
}
