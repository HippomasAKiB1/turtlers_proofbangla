#!/usr/bin/env bash
# Builds work/ with the folder layout the notebooks expect, from the files in this repository.
# Run from anywhere; works on Linux, macOS, WSL and Git Bash on Windows.
# The notebooks overwrite files in their working folder (Stage 1.5 of the original notebook deletes and
# recomputes predictions/F_olik_*.jsonl), so always run them inside work/, never in the repository folders.
set -euo pipefail
cd "$(dirname "$0")/.."
if [ -e work ]; then
  echo "work/ already exists. Remove or rename it first." >&2
  exit 1
fi
mkdir -p work/data/raw work/checkpoints work/cache work/results work/results2
cp -r predictions work/predictions
cp results/original_run/*.json work/results/
cp -r results/original_run/tables work/tables
cp -r results/original_run/figures work/figures
cp -r results/posthoc/. work/results2/
echo "work/ is ready. Put the downloaded datasets in work/data/raw/ and start the notebooks with work/ as the working directory."
