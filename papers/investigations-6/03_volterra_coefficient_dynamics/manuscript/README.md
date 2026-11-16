# Volterra dynamics and logarithmic coefficient bounds for the Newman heat flow

**Analytical draft, 14 November 2026.** Edward Baker, with substantial
OpenAI Codex LLM assistance. Recorded drafting dispatch gpt-6.1-sol /
ultra. Independent backend attestation is unavailable.

[Editable LaTeX](main.tex) contains the complete-source bounds, the
moving-basis Jacobi dynamics and the coefficient and scalar estimates.
See the [integration note](../notes/02_VCD_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md),
[internal assessment](../reviews/02_VCD_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md)
and [build record](../numerics/02_VCD_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json).

## Build a reading copy

From this manuscript directory, use pdfLaTeX and the packages in the
preamble. Run the following twice, with an absolute output directory
outside the repository.

~~~sh
vcd_output_dir=/private/tmp/investigations-6-manuscripts-20261114/vcd
mkdir -p "$vcd_output_dir"
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory="$vcd_output_dir" -jobname=volterra_coefficient_dynamics main.tex
~~~

The PDF and all generated files go to that directory. The source has no
numerical or data-file dependency.

The parent [combined build record](../../numerics/15_TN6_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json)
identifies the latest external reading-copy bytes after the final common
build. Branch build records retain their earlier compilation identities;
PDF metadata may differ on recompilation of unchanged TeX. The
[parent document check](../../numerics/18_TN6_MANUSCRIPT_FINAL_CHECK_20261114.json)
records final source matching and page inspection.
