package main

import (
	"os"
	"path/filepath"
	"time"
)

type Config struct {
	PythonExe     string
	ScriptPath    string
	MinConf       float64
	LocalCooldown time.Duration
}

func defaultConfig() Config {
	wd, _ := os.Getwd()
	repo := wd
	if filepath.Base(wd) == "go" {
		repo = filepath.Dir(wd)
	}

	pythonExe := "py"
	for _, dir := range []string{".venv", "venv"} {
		candidate := filepath.Join(repo, dir, "Scripts", "python.exe")
		if _, err := os.Stat(candidate); err == nil {
			pythonExe = candidate
			break
		}
	}
	pyScript := filepath.Join(repo, "py", "recognizer.py")

	return Config{
		PythonExe:     pythonExe,
		ScriptPath:    pyScript,
		MinConf:       0.60,
		LocalCooldown: 250 * time.Millisecond,
	}
}
