#!/bin/sh
set -eu
paper_dir="$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)"
repo_root="$(git -C "$paper_dir" rev-parse --show-toplevel)"
build_dir="$repo_root/output/pdf/08_theta_observables_newman_dynamics/localized_zero_correlations"
mkdir -p "$build_dir"
python3 "$paper_dir/prepare_bibliography.py" "$build_dir/localized_zero_correlations_sources.bib"
cd "$paper_dir"
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$build_dir" -jobname=localized_zero_correlations main.tex
