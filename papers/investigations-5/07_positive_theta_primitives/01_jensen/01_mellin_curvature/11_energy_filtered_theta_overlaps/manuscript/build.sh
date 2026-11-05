#!/bin/sh
set -eu
paper_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_root=$(git -C "$paper_dir" rev-parse --show-toplevel)
if [ "$#" -gt 0 ]; then
  output_dir="$1"
else
  output_dir="$repo_root/output/pdf/mc11-energy-filtered-theta-overlaps"
fi
mkdir -p "$output_dir"
output_dir=$(CDPATH= cd -- "$output_dir" && pwd)
cd "$paper_dir"
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -jobname=angular_radial_theta_overlaps -outdir="$output_dir" main.tex
