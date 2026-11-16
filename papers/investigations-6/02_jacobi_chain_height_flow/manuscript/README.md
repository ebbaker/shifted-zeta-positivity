# The Fixed Jacobi Chain for Newman Flow

Analytical draft for **Edward Baker**, 14 November 2026, with substantial
OpenAI Codex LLM assistance. The execution dispatch selected
**GPT-6.1 Sol / Ultra**. Backend and runtime effort attestation is unavailable.

[Editable manuscript](main.tex) · [Source and proof map](../notes/03_JCH_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md) ·
[Internal assessment](../reviews/02_JCH_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md) ·
[Build record](../numerics/02_JCH_E03_MANUSCRIPT_BUILD_20261114.json)

The draft derives the fixed-basis Jacobi realization and single-excitation
encoding, proves the finite scalar quadrature error and sufficient depth,
and illustrates uncertainty transfer with the existing 16-site interval
certificate. The last section discusses state-prefix transport, growing
height, coefficient conditioning and signed readout.

## Build a reading copy

Run from this manuscript directory with the TeX distribution on PATH.
Keep the reading PDF and all generated files outside the repository.

```sh
jch_output=/private/tmp/investigations-6-manuscripts-20261114/jch
mkdir -p "$jch_output"
latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error \
  -outdir="$jch_output" -jobname=jacobi_chain_height_flow main.tex \
  > "$jch_output/latexmk.log" 2>&1
```

The reading copy is `/private/tmp/investigations-6-manuscripts-20261114/jch/jacobi_chain_height_flow.pdf`.
Use another external directory if needed. The LaTeX source includes the
bibliography and builds with pdfLaTeX. The small record identifies the
source and the local output.

The parent [combined build record](../../numerics/15_TN6_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json)
identifies the latest external reading-copy bytes after the final common
build. Branch build records retain their earlier compilation identities;
PDF metadata may differ on recompilation of unchanged TeX. The
[parent document check](../../numerics/18_TN6_MANUSCRIPT_FINAL_CHECK_20261114.json)
records final source matching and page inspection.
