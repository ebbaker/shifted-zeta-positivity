#!/bin/sh
set -eu
cd "$(dirname "$0")"
repo="$(git rev-parse --show-toplevel)"
out="$repo/output/pdf/08_theta_observables_newman_dynamics/collision_constraints"
mkdir -p "$out"
latexmk -pdf -interaction=nonstopmode -halt-on-error \
    -jobname=regular_deflation_finite_pair_survival -outdir="$out" main.tex
