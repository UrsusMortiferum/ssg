#!/usr/bin/env bash

run_python() {
  if [ -n "$VIRTUAL_ENV" ] && command -v python &>/dev/null; then
    python "$@"
  elif command -v uv &>/dev/null; then
    uv run python "$@"
  elif command -v python3 &>/dev/null; then
    python3 "$@"
  else
    echo "Error: No Python runtime found"
    echo "Please activate a virtual environment, install uv or python."
    exit 1
  fi
}
