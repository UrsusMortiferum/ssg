#!/usr/bin/env bash

source "$(dirname "$0")/runPython.sh"

run_python src/main.py
cd public && run_python -m http.server 8888
