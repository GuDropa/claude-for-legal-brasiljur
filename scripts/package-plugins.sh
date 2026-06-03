#!/usr/bin/env bash
# Wrapper: chama o empacotador Python que funciona em Windows, Mac e Linux
set -euo pipefail
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
python3 "$SCRIPT_DIR/package_plugins.py" "$@"
