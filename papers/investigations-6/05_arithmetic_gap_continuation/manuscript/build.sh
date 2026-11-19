#!/bin/sh
# 19 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
set -eu
script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
repo_dir=$(git -C "$script_dir" rev-parse --show-toplevel)
out_dir="$repo_dir/output/pdf/arithmetic-gap-continuation"
mkdir -p "$out_dir"
cd "$script_dir"
BIBINPUTS="$script_dir/../references:${BIBINPUTS-}"
export BIBINPUTS
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -jobname=arithmetic_gap_continuation -outdir="$out_dir" main.tex
