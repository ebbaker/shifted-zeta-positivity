# A quantics tensor train for the Newman heat flow

**Analytical draft, 14 November 2026.** Edward Baker, with substantial
OpenAI Codex LLM assistance. Recorded drafting dispatch gpt-6.1-sol /
ultra. Independent backend attestation is unavailable.

[Editable LaTeX](main.tex) includes the full fixed-box proof, the matched
scalar polynomial comparison and the outstanding challenges.
See the [integration note](../notes/05_QTT_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md),
[internal assessment](../reviews/02_QTT_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md)
and [build record](../numerics/03_QTT_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json).

## Build a reading copy

From this manuscript directory, with pdfLaTeX and the standard packages
listed in the TeX preamble, run the following twice. Use an absolute
output directory outside the repository.

~~~sh
qtt_output_dir=/private/tmp/investigations-6-manuscripts-20261114/qtt
mkdir -p "$qtt_output_dir"
pdflatex -interaction=nonstopmode -halt-on-error -file-line-error \
  -output-directory="$qtt_output_dir" -jobname=qtt_newman_flow main.tex
~~~

The PDF and all generated files go to that directory. The source has no
data file, bibliography processor or numerical runtime dependency.

The parent [combined build record](../../numerics/15_TN6_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json)
identifies the latest external reading-copy bytes after the final common
build. Branch build records retain their earlier compilation identities;
PDF metadata may differ on recompilation of unchanged TeX. The
[parent document check](../../numerics/18_TN6_MANUSCRIPT_FINAL_CHECK_20261114.json)
records final source matching and page inspection.
