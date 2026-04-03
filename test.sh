#!/usr/bin/env bash

source "$(dirname "$0")/runPython.sh"

run_python -m unittest discover -s src --failfast
