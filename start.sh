#!/usr/bin/env bash
set -euxo pipefail
cd "$(dirname "$0")"

source .venv/Scripts/activate

flask run --host=0.0.0.0
