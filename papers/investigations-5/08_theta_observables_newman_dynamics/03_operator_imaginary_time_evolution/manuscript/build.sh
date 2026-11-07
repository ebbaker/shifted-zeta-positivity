#!/usr/bin/env bash
set -euo pipefail

paper_dir="$(cd -- "$(dirname -- "$0")" && pwd)"
repo_root="$(git -C "$paper_dir" rev-parse --show-toplevel)"
build_dir="$repo_root/output/pdf/08_theta_observables_newman_dynamics/operator_imaginary_time_evolution"
mkdir -p "$build_dir"
python3 "$paper_dir/prepare_bibliography.py" "$build_dir/operator_newman_sources.bib"
cd "$paper_dir"
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$build_dir" -jobname=operator_newman_collision_geometry main.tex
