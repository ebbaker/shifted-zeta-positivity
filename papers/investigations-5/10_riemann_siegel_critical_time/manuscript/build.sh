#!/bin/sh
# Drafted for Edward Baker with OpenAI Codex assistance, 2026-11-12.
# Actual backend model and reasoning effort were not recorded.
set -eu
manuscript_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd -P)
repo_dir=$(CDPATH= cd -- "$manuscript_dir/../../../.." && pwd -P)
requested_output=${1:-/private/tmp/rsct-manuscript-20261112}
# Resolve existing symlinks and reject repository destinations before writing.
output_dir=$(python3 - "$requested_output" "$repo_dir" <<'PY'
import pathlib, sys
out = pathlib.Path(sys.argv[1]).expanduser().resolve()
repo = pathlib.Path(sys.argv[2]).resolve()
if out == repo or repo in out.parents:
    raise SystemExit("Choose an output directory outside the repository.")
print(out)
PY
)
mkdir -p "$output_dir"
cd "$manuscript_dir"
if command -v latexmk >/dev/null 2>&1; then
    tex_builder=latexmk
elif [ -x /Library/TeX/texbin/latexmk ]; then
    PATH="/Library/TeX/texbin:$PATH"
    export PATH
    tex_builder=/Library/TeX/texbin/latexmk
else
    echo "latexmk and a pdfLaTeX installation are required." >&2
    exit 1
fi
"$tex_builder" -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
    -outdir="$output_dir" -jobname=riemann_siegel_critical_time main.tex
printf '%s\n' "$output_dir/riemann_siegel_critical_time.pdf"
