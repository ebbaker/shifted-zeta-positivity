#!/bin/sh
set -eu
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_dir=$(git -C "$script_dir" rev-parse --show-toplevel)
out_dir="$repo_dir/output/pdf/vcd-conservation-laws"
mkdir -p "$out_dir"
cd "$script_dir"
BIBINPUTS="$script_dir/../references:$script_dir/../../brainstorm/references:${BIBINPUTS-}"
export BIBINPUTS
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -jobname=conservation_laws -outdir="$out_dir" main.tex
