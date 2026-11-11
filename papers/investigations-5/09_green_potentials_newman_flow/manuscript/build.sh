#!/usr/bin/env bash
set -euo pipefail
paper_dir="$(cd -- "$(dirname -- "$0")" && pwd)"
repo_root="$(git -C "$paper_dir" rev-parse --show-toplevel)"
build_dir="$repo_root/output/pdf/09_green_potentials_newman_flow"
mkdir -p "$build_dir"
python3 "$paper_dir/prepare_bibliography.py" "$build_dir/green_newman_sources.bib"
cd "$paper_dir"
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$build_dir" -jobname=green_potentials_newman_flow main.tex

