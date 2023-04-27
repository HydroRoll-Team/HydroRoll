// Package cmdutil holds functionality to run turbo via cobra. That includes flag parsing and configuration
// of components common to all subcommands
package cmdutil

import (
	"fmt"
	"io"
	"io/ioutil"
	"os"
	"strconv"
	"sync"

	"github.com/hashicorp/go-hclog"

	"github.com/fatih/color"
	"github.com/mitchellh/cli"
	"github.com/vercel/turbo/cli/internal/client"
	"github.com/vercel/turbo/cli/internal/config"
	"github.com/vercel/turbo/cli/internal/fs"
	"github.com/vercel/turbo/cli/internal/turbopath"
	"github.com/vercel/turbo/cli/internal/turbostate"
	"github.com/vercel/turbo/cli/internal/ui"
)

const (
	// _envLogLevel is the environment log level
	_envLogLevel = "TURBO_LOG_LEVEL"
)

// Helper is a struct used to hold configuration values passed via flag, env vars,
// config files, etc. It is not intended for direct use by turbo commands, it drives
// the creation of CmdBase, which is then used by the commands themselves.
type Helper struct {
	// TurboVersion is the version of turbo that is currently executing
	TurboVersion string

	// for logging
	verbosity int

	rawRepoRoot string

	clientOpts client.Opts

	// UserConfigPath is the path to where we expect to find
	// a user-specific config file, if one is present. Public
	// to allow overrides in tests
	UserConfigPath turbopath.AbsoluteSystemPath

	cleanupsMu sync.Mutex
	cleanups   []io.Closer
}

// RegisterCleanup saves a function to be run after turbo execution,
// even if the command that runs returns an error
func (h *Helper) RegisterCleanup(cleanup io.Closer) {
	h.cleanupsMu.Lock()
	defer h.cleanupsMu.Unlock()
	h.cleanups = append(h.cleanups, cleanup)
}

// Cleanup runs the register cleanup handlers. It requires the flags
// to the root command so that it can construct a UI if necessary
func (h *Helper) Cleanup(cliConfig *turbostate.ParsedArgsFromRust) {
	h.cleanupsMu.Lock()
	defer h.cleanupsMu.Unlock()
	var ui cli.Ui
	for _, cleanup := range h.cleanups {
		if err := cleanup.Close(); err != nil {
			if ui == nil {
				ui = h.getUI(cliConfig)
			}
			ui.Warn(fmt.Sprintf("failed cleanup: %v", err))
		}
	}
}

func (h *Helper) getUI(cliConfig *turbostate.ParsedArgsFromRust) cli.Ui {
	colorMode := ui.GetColorModeFromEnv()
	if cliConfig.GetNoColor() {
		colorMode = ui.ColorModeSuppressed
	}
	if cliConfig.GetColor() {
		colorMode = ui.ColorModeForced
	}
	return ui.BuildColoredUi(colorMode)
}

func (h *Helper) getLogger() (hclog.Logger, error) {
	var level hclog.Level
	switch h.verbosity {
	case 0:
		if v := os.Getenv(_envLogLevel); v != "" {
			level = hclog.LevelFromString(v)
			if level == hclog.NoLevel {
				return nil, fmt.Errorf("%s value %q is not a valid log level", _envLogLevel, v)
			}
		} else {
			level = hclog.NoLevel
		}
	case 1:
		level = hclog.Info
	case 2:
		level = hclog.Debug
	case 3:
		level = hclog.Trace
	default:
		level = hclog.Trace
	}
	// Default output is nowhere unless we enable logging.
	output := ioutil.Discard
	color := hclog.ColorOff
	if level != hclog.NoLevel {
		output = os.Stderr
		color = hclog.AutoColor
	}

	return hclog.New(&hclog.LoggerOptions{
		Name:   "turbo",
		Level:  level,
		Color:  color,
		Output: output,
	}), nil
}

// NewHelper returns a new helper instance to hold configuration values for the root
// turbo command.
func NewHelper(turboVersion string, args *turbostate.ParsedArgsFromRust) *Helper {
	return &Helper{
		TurboVersion:   turboVersion,
		UserConfigPath: config.DefaultUserConfigPath(),
		verbosity:      args.Verbosity,
	}
}

// GetCmdBase returns a CmdBase instance configured with values from this helper.
// It additionally returns a mechanism to set an error, so
func (h *Helper) GetCmdBase(cliConfig *turbostate.ParsedArgsFromRust) (*CmdBase, error) {
	// terminal is for color/no-color output
	terminal := h.getUI(cliConfig)
	// logger is configured with verbosity level using --verbosity flag from end users
	logger, err := h.getLogger()
	if err != nil {
		return nil, err
	}
	cwdRaw, err := cliConfig.GetCwd()
	if err != nil {
		return nil, err
	}
	cwd, err := fs.GetCwd(cwdRaw)
	if err != nil {
		return nil, err
	}
	repoRoot := fs.ResolveUnknownPath(cwd, h.rawRepoRoot)
	repoRoot, err = repoRoot.EvalSymlinks()
	if err != nil {
		return nil, err
	}
	repoConfig, err := config.ReadRepoConfigFile(config.GetRepoConfigPath(repoRoot), cliConfig)
	if err != nil {
		return nil, err
	}
	userConfig, err := config.ReadUserConfigFile(h.UserConfigPath, cliConfig)
	if err != nil {
		return nil, err
	}
	remoteConfig := repoConfig.GetRemoteConfig(userConfig.Token())
	if remoteConfig.Token == "" && ui.IsCI {
		vercelArtifactsToken := os.Getenv("VERCEL_ARTIFACTS_TOKEN")
		vercelArtifactsOwner := os.Getenv("VERCEL_ARTIFACTS_OWNER")
		if vercelArtifactsToken != "" {
			remoteConfig.Token = vercelArtifactsToken
		}
		if vercelArtifactsOwner != "" {
			remoteConfig.TeamID = vercelArtifactsOwner
		}
	}

	// Primacy: Arg > Env
	timeout, err := cliConfig.GetRemoteCacheTimeout()
	if err == nil {
		h.clientOpts.Timeout = timeout
	} else {
		val, ok := os.LookupEnv("TURBO_REMOTE_CACHE_TIMEOUT")
		if ok {
			number, err := strconv.ParseUint(val, 10, 64)
			if err == nil {
				h.clientOpts.Timeout = number
			}
		}
	}

	apiClient := client.NewClient(
		remoteConfig,
		logger,
		h.TurboVersion,
		h.clientOpts,
	)

	return &CmdBase{
		UI:           terminal,
		Logger:       logger,
		RepoRoot:     repoRoot,
		APIClient:    apiClient,
		RepoConfig:   repoConfig,
		UserConfig:   userConfig,
		RemoteConfig: remoteConfig,
		TurboVersion: h.TurboVersion,
	}, nil
}

// CmdBase encompasses configured components common to all turbo commands.
type CmdBase struct {
	UI           cli.Ui
	Logger       hclog.Logger
	RepoRoot     turbopath.AbsoluteSystemPath
	APIClient    *client.APIClient
	RepoConfig   *config.RepoConfig
	UserConfig   *config.UserConfig
	RemoteConfig client.RemoteConfig
	TurboVersion string
}

// LogError prints an error to the UI
func (b *CmdBase) LogError(format string, args ...interface{}) {
	err := fmt.Errorf(format, args...)
	b.Logger.Error("error", err)
	b.UI.Error(fmt.Sprintf("%s%s", ui.ERROR_PREFIX, color.RedString(" %v", err)))
}

// LogWarning logs an error and outputs it to the UI.
func (b *CmdBase) LogWarning(prefix string, err error) {
	b.Logger.Warn(prefix, "warning", err)

	if prefix != "" {
		prefix = " " + prefix + ": "
	}

	b.UI.Warn(fmt.Sprintf("%s%s%s", ui.WARNING_PREFIX, prefix, color.YellowString(" %v", err)))
}

// LogInfo logs an message and outputs it to the UI.
func (b *CmdBase) LogInfo(msg string) {
	b.Logger.Info(msg)
	b.UI.Info(fmt.Sprintf("%s%s", ui.InfoPrefix, color.WhiteString(" %v", msg)))
}
