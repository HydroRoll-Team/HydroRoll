package fs

import (
	"os"
	"reflect"
	"sort"
	"strings"
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/vercel/turbo/cli/internal/turbopath"
	"github.com/vercel/turbo/cli/internal/util"
	"gotest.tools/v3/assert/cmp"
)

func assertIsSorted(t *testing.T, arr []string, msg string) {
	t.Helper()
	if arr == nil {
		return
	}

	copied := make([]string, len(arr))
	copy(copied, arr)
	sort.Strings(copied)
	if !reflect.DeepEqual(arr, copied) {
		t.Errorf("Expected sorted, got %v: %v", arr, msg)
	}
}

func Test_ReadTurboConfig(t *testing.T) {
	testDir := getTestDir(t, "correct")
	turboJSON, turboJSONReadErr := readTurboConfig(testDir.UntypedJoin("turbo.json"))

	if turboJSONReadErr != nil {
		t.Fatalf("invalid parse: %#v", turboJSONReadErr)
	}

	assert.EqualValues(t, []string{"AWS_SECRET_KEY"}, turboJSON.GlobalPassthroughEnv)

	pipelineExpected := map[string]BookkeepingTaskDefinition{
		"build": {
			definedFields:      util.SetFromStrings([]string{"Outputs", "OutputMode", "DependsOn"}),
			experimentalFields: util.SetFromStrings([]string{"PassthroughEnv"}),
			experimental: taskDefinitionExperiments{
				PassthroughEnv: []string{"GITHUB_TOKEN"},
			},
			TaskDefinition: taskDefinitionHashable{
				Outputs:                 TaskOutputs{Inclusions: []string{".next/**", "dist/**"}, Exclusions: []string{"dist/assets/**"}},
				TopologicalDependencies: []string{"build"},
				EnvVarDependencies:      []string{},
				TaskDependencies:        []string{},
				ShouldCache:             true,
				OutputMode:              util.NewTaskOutput,
			},
		},
		"lint": {
			definedFields:      util.SetFromStrings([]string{"Outputs", "OutputMode", "ShouldCache", "DependsOn"}),
			experimentalFields: util.SetFromStrings([]string{}),
			experimental: taskDefinitionExperiments{
				PassthroughEnv: []string{},
			},
			TaskDefinition: taskDefinitionHashable{
				Outputs:                 TaskOutputs{},
				TopologicalDependencies: []string{},
				EnvVarDependencies:      []string{"MY_VAR"},
				TaskDependencies:        []string{},
				ShouldCache:             true,
				OutputMode:              util.NewTaskOutput,
			},
		},
		"dev": {
			definedFields:      util.SetFromStrings([]string{"OutputMode", "ShouldCache"}),
			experimentalFields: util.SetFromStrings([]string{}),
			experimental: taskDefinitionExperiments{
				PassthroughEnv: []string{},
			},
			TaskDefinition: taskDefinitionHashable{
				Outputs:                 TaskOutputs{},
				TopologicalDependencies: []string{},
				EnvVarDependencies:      []string{},
				TaskDependencies:        []string{},
				ShouldCache:             false,
				OutputMode:              util.FullTaskOutput,
			},
		},
		"publish": {
			definedFields:      util.SetFromStrings([]string{"Inputs", "Outputs", "DependsOn", "ShouldCache"}),
			experimentalFields: util.SetFromStrings([]string{}),
			experimental: taskDefinitionExperiments{
				PassthroughEnv: []string{},
			},
			TaskDefinition: taskDefinitionHashable{
				Outputs:                 TaskOutputs{Inclusions: []string{"dist/**"}},
				TopologicalDependencies: []string{"build", "publish"},
				EnvVarDependencies:      []string{},
				TaskDependencies:        []string{"admin#lint", "build"},
				ShouldCache:             false,
				Inputs:                  []string{"build/**/*"},
				OutputMode:              util.FullTaskOutput,
			},
		},
	}

	validateOutput(t, turboJSON, pipelineExpected)
	remoteCacheOptionsExpected := RemoteCacheOptions{"team_id", true}
	assert.EqualValues(t, remoteCacheOptionsExpected, turboJSON.RemoteCacheOptions)
}

func Test_LoadTurboConfig_Legacy(t *testing.T) {
	testDir := getTestDir(t, "legacy-only")
	packageJSONPath := testDir.UntypedJoin("package.json")
	rootPackageJSON, pkgJSONReadErr := ReadPackageJSON(packageJSONPath)

	if pkgJSONReadErr != nil {
		t.Fatalf("invalid parse: %#v", pkgJSONReadErr)
	}

	_, turboJSONReadErr := LoadTurboConfig(testDir, rootPackageJSON, false)
	expectedErrorMsg := "Could not find turbo.json. Follow directions at https://turbo.build/repo/docs to create one: file does not exist"
	assert.EqualErrorf(t, turboJSONReadErr, expectedErrorMsg, "Error should be: %v, got: %v", expectedErrorMsg, turboJSONReadErr)
}

func Test_LoadTurboConfig_BothCorrectAndLegacy(t *testing.T) {
	testDir := getTestDir(t, "both")

	packageJSONPath := testDir.UntypedJoin("package.json")
	rootPackageJSON, pkgJSONReadErr := ReadPackageJSON(packageJSONPath)

	if pkgJSONReadErr != nil {
		t.Fatalf("invalid parse: %#v", pkgJSONReadErr)
	}

	turboJSON, turboJSONReadErr := LoadTurboConfig(testDir, rootPackageJSON, false)

	if turboJSONReadErr != nil {
		t.Fatalf("invalid parse: %#v", turboJSONReadErr)
	}

	pipelineExpected := map[string]BookkeepingTaskDefinition{
		"build": {
			definedFields:      util.SetFromStrings([]string{"Outputs", "OutputMode", "DependsOn"}),
			experimentalFields: util.SetFromStrings([]string{}),
			experimental: taskDefinitionExperiments{
				PassthroughEnv: []string{},
			},
			TaskDefinition: taskDefinitionHashable{
				Outputs:                 TaskOutputs{Inclusions: []string{".next/**", "dist/**"}, Exclusions: []string{"dist/assets/**"}},
				TopologicalDependencies: []string{"build"},
				EnvVarDependencies:      []string{},
				TaskDependencies:        []string{},
				ShouldCache:             true,
				OutputMode:              util.NewTaskOutput,
			},
		},
	}

	validateOutput(t, turboJSON, pipelineExpected)

	remoteCacheOptionsExpected := RemoteCacheOptions{"team_id", true}
	assert.EqualValues(t, remoteCacheOptionsExpected, turboJSON.RemoteCacheOptions)
	assert.Equal(t, rootPackageJSON.LegacyTurboConfig == nil, true)
}

func Test_ReadTurboConfig_InvalidEnvDeclarations1(t *testing.T) {
	testDir := getTestDir(t, "invalid-env-1")
	_, turboJSONReadErr := readTurboConfig(testDir.UntypedJoin("turbo.json"))

	expectedErrorMsg := "turbo.json: You specified \"$A\" in the \"env\" key. You should not prefix your environment variables with \"$\""
	assert.EqualErrorf(t, turboJSONReadErr, expectedErrorMsg, "Error should be: %v, got: %v", expectedErrorMsg, turboJSONReadErr)
}

func Test_ReadTurboConfig_InvalidEnvDeclarations2(t *testing.T) {
	testDir := getTestDir(t, "invalid-env-2")
	_, turboJSONReadErr := readTurboConfig(testDir.UntypedJoin("turbo.json"))
	expectedErrorMsg := "turbo.json: You specified \"$A\" in the \"env\" key. You should not prefix your environment variables with \"$\""
	assert.EqualErrorf(t, turboJSONReadErr, expectedErrorMsg, "Error should be: %v, got: %v", expectedErrorMsg, turboJSONReadErr)
}

func Test_ReadTurboConfig_InvalidGlobalEnvDeclarations(t *testing.T) {
	testDir := getTestDir(t, "invalid-global-env")
	_, turboJSONReadErr := readTurboConfig(testDir.UntypedJoin("turbo.json"))
	expectedErrorMsg := "turbo.json: You specified \"$QUX\" in the \"globalEnv\" key. You should not prefix your environment variables with \"$\""
	assert.EqualErrorf(t, turboJSONReadErr, expectedErrorMsg, "Error should be: %v, got: %v", expectedErrorMsg, turboJSONReadErr)
}

func Test_ReadTurboConfig_EnvDeclarations(t *testing.T) {
	testDir := getTestDir(t, "legacy-env")
	turboJSON, turboJSONReadErr := readTurboConfig(testDir.UntypedJoin("turbo.json"))

	if turboJSONReadErr != nil {
		t.Fatalf("invalid parse: %#v", turboJSONReadErr)
	}

	pipeline := turboJSON.Pipeline
	assert.EqualValues(t, pipeline["task1"].TaskDefinition.EnvVarDependencies, sortedArray([]string{"A"}))
	assert.EqualValues(t, pipeline["task2"].TaskDefinition.EnvVarDependencies, sortedArray([]string{"A"}))
	assert.EqualValues(t, pipeline["task3"].TaskDefinition.EnvVarDependencies, sortedArray([]string{"A"}))
	assert.EqualValues(t, pipeline["task4"].TaskDefinition.EnvVarDependencies, sortedArray([]string{"A", "B"}))
	assert.EqualValues(t, pipeline["task6"].TaskDefinition.EnvVarDependencies, sortedArray([]string{"A", "B", "C", "D", "E", "F"}))
	assert.EqualValues(t, pipeline["task7"].TaskDefinition.EnvVarDependencies, sortedArray([]string{"A", "B", "C"}))
	assert.EqualValues(t, pipeline["task8"].TaskDefinition.EnvVarDependencies, sortedArray([]string{"A", "B", "C"}))
	assert.EqualValues(t, pipeline["task9"].TaskDefinition.EnvVarDependencies, sortedArray([]string{"A"}))
	assert.EqualValues(t, pipeline["task10"].TaskDefinition.EnvVarDependencies, sortedArray([]string{"A"}))
	assert.EqualValues(t, pipeline["task11"].TaskDefinition.EnvVarDependencies, sortedArray([]string{"A", "B"}))

	// check global env vars also
	assert.EqualValues(t, sortedArray([]string{"FOO", "BAR", "BAZ", "QUX"}), sortedArray(turboJSON.GlobalEnv))
	assert.EqualValues(t, sortedArray([]string{"somefile.txt"}), sortedArray(turboJSON.GlobalDeps))
}

func Test_TaskOutputsSort(t *testing.T) {
	inclusions := []string{"foo/**", "bar"}
	exclusions := []string{"special-file", ".hidden/**"}
	taskOutputs := TaskOutputs{Inclusions: inclusions, Exclusions: exclusions}
	sortedOutputs := taskOutputs.Sort()
	assertIsSorted(t, sortedOutputs.Inclusions, "Inclusions")
	assertIsSorted(t, sortedOutputs.Exclusions, "Exclusions")
	assert.False(t, cmp.DeepEqual(taskOutputs, sortedOutputs)().Success())
}

// Helpers
func validateOutput(t *testing.T, turboJSON *TurboJSON, expectedPipeline Pipeline) {
	t.Helper()
	assertIsSorted(t, turboJSON.GlobalDeps, "Global Deps")
	assertIsSorted(t, turboJSON.GlobalEnv, "Global Env")
	validatePipeline(t, turboJSON.Pipeline, expectedPipeline)
}

func validatePipeline(t *testing.T, actual Pipeline, expected Pipeline) {
	t.Helper()
	// check top level keys
	if len(actual) != len(expected) {
		expectedKeys := []string{}
		for k := range expected {
			expectedKeys = append(expectedKeys, k)
		}
		actualKeys := []string{}
		for k := range actual {
			actualKeys = append(actualKeys, k)
		}
		t.Errorf("pipeline tasks mismatch. got %v, want %v", strings.Join(actualKeys, ","), strings.Join(expectedKeys, ","))
	}

	// check individual task definitions
	for taskName, expectedTaskDefinition := range expected {
		bookkeepingTaskDef, ok := actual[taskName]
		if !ok {
			t.Errorf("missing expected task: %v", taskName)
		}
		actualTaskDefinition := bookkeepingTaskDef.GetTaskDefinition()
		assertIsSorted(t, actualTaskDefinition.Outputs.Inclusions, "Task output inclusions")
		assertIsSorted(t, actualTaskDefinition.Outputs.Exclusions, "Task output exclusions")
		assertIsSorted(t, actualTaskDefinition.EnvVarDependencies, "Task env vars")
		assertIsSorted(t, actualTaskDefinition.PassthroughEnv, "Task env vars")
		assertIsSorted(t, actualTaskDefinition.TopologicalDependencies, "Topo deps")
		assertIsSorted(t, actualTaskDefinition.TaskDependencies, "Task deps")
		assert.EqualValuesf(t, expectedTaskDefinition, bookkeepingTaskDef, "task definition mismatch for %v", taskName)
	}
}

func getTestDir(t *testing.T, testName string) turbopath.AbsoluteSystemPath {
	defaultCwd, err := os.Getwd()
	if err != nil {
		t.Errorf("failed to get cwd: %v", err)
	}
	cwd, err := CheckedToAbsoluteSystemPath(defaultCwd)
	if err != nil {
		t.Fatalf("cwd is not an absolute directory %v: %v", defaultCwd, err)
	}

	return cwd.UntypedJoin("testdata", testName)
}

func sortedArray(arr []string) []string {
	sort.Strings(arr)
	return arr
}
