#!/bin/sh
set -eu
paper_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(git -C "$paper_dir" rev-parse --show-toplevel)
output_dir=${1:-"$repo_root/output/pdf/mc08-open-quantum-dynamics"}
mkdir -p "$output_dir"
output_dir=$(CDPATH= cd -- "$output_dir" && pwd)
cd "$paper_dir"
python3 "$paper_dir/../../manuscript/prepare_bibliography.py" "$output_dir"
BIBINPUTS="$output_dir:${BIBINPUTS-}"
export BIBINPUTS
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -jobname=fermionic_theta_open_dynamics_energy -outdir="$output_dir" main.tex
