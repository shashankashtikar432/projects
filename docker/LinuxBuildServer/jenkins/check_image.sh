#!/bin/bash
set -euo pipefail

# Prefer the virtualenv python if it exists, otherwise fall back to system python3
PY_VENV="/build/jenkins/pythonvenv/bin/python"
SCRIPT="/build/jenkins/check_image.py"

if [ -x "$PY_VENV" ]; then
	"$PY_VENV" "$SCRIPT"
else
	/usr/bin/env python3 "$SCRIPT"
fi

# Capture and return the Python script exit code
RC=$?
exit $RC
