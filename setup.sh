#!/usr/bin/env bash
set -euxo pipefail
cd "$(dirname "$0")"

python -m venv .venv
source .venv/Scripts/activate

pip install --require-virtualenv -r requirements.txt
