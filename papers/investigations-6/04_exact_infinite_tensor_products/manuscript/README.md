# Exact Dyadic Tensor Products for the Newman Source

Analytical draft by Edward Baker, 14 November 2026, with substantial
OpenAI Codex assistance. Recorded worker dispatch GPT-6.1 Sol / Ultra.
Independent backend metadata are unavailable.

[Editable LaTeX](main.tex) contains the proofs, normalization, and
bibliography for the dyadic construction and its uniform absolute strip
estimate. See the [integration note](../notes/03_ITP_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md),
[internal analytical assessment](../reviews/02_ITP_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md)
and [build record](../numerics/02_ITP_E03_MANUSCRIPT_BUILD_20261114.json).

From this directory, build with TeX Live and latexmk. Set the absolute
output directory outside the repository. The command produces the PDF,
log, and auxiliary files there and repeats LaTeX until the references
settle.

```sh
itp_manuscript_output_dir="/private/tmp/investigations-6-manuscripts-20261114/itp"
mkdir -p "$itp_manuscript_output_dir"
latexmk -pdf -halt-on-error -interaction=nonstopmode \
  -outdir="$itp_manuscript_output_dir" \
  -jobname=exact_infinite_tensor_products main.tex
```

The 14 November working reading copy is at
`/private/tmp/investigations-6-manuscripts-20261114/itp/exact_infinite_tensor_products.pdf`.
A fresh build from source is sufficient to reproduce its mathematical
content. PDF metadata can vary between builds.

The parent [combined build record](../../numerics/15_TN6_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json)
identifies the latest external reading-copy bytes after the final common
build. Branch build records retain their earlier compilation identities;
PDF metadata may differ on recompilation of unchanged TeX. The
[parent document check](../../numerics/18_TN6_MANUSCRIPT_FINAL_CHECK_20261114.json)
records final source matching and page inspection.
