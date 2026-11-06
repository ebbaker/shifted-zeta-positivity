#!/usr/bin/env bash
set -euo pipefail
paper_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
repo_root="$(git -C "$paper_dir" rev-parse --show-toplevel)"
build_dir="$repo_root/output/pdf/08_theta_observables_newman_dynamics/direct_newman_realization"
mkdir -p "$build_dir"
cat "$paper_dir/../references/manuscript_internal_sources.bib" \
 "$paper_dir/../../references/internal_sources.bib" \
 "$paper_dir/../../../07_positive_theta_primitives/01_jensen/01_mellin_curvature/11_energy_filtered_theta_overlaps/references/references.bib" \
 "$paper_dir/../references/references.bib" > "$build_dir/direct_newman_sources.bib"
cd "$paper_dir"
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
 -outdir="$build_dir" -jobname=conditional_newman_dynamics main.tex
