# Explicit large-time zeros and backward transport of gaps in the Newman heat flow

20 November 2026. Working draft prepared for Edward Baker with substantial OpenAI Codex assistance. The recorded model and effort for this turn were gpt-6.2-astra/max.

[Read the PDF](../../../../../output/pdf/explicit-zero-gap-transport/explicit_zero_gap_transport.pdf) · [Editable LaTeX](main.tex) · [Source map](../references/README.md) · [Internal assessment](../reviews/01_EZ_OPENING_ASSESSMENT_20261120.md) · [Production record](../numerics/02_DRAFT_BUILD_AND_CHECK_20261120.json)

| Section | Subject | Source |
| --- | --- | --- |
| 1 | Literal half-line theta field, physical time and the parent discriminant | [Main file](main.tex) |
| 2 | Individual residues, inverse cumulants, all-order cubic sum and complete factors | [Explicit anchors](anchors.tex) |
| 3 | A common velocity field for the chain and complete exterior moment identities | [Current and exterior](current.tex) |
| 4 | Signed large-time drift, integrated transport and the mean-normalized gap | [Transport theorem](transport.tex) |
| 5 | Three upper-time zero checks and one finite backward interval for the first edge | [Interval calculation](finite.tex) |
| 6 | Fourth-cumulant cancellation, the parent's forcing barrier and collision controls | [Analytical continuation](frontier.tex) |

From this directory run the following command with Python 3, latexmk, pdfLaTeX and BibTeX installed.

~~~sh
python3 build.py
~~~

The [builder](build.py) uses the two local bibliographies, builds in temporary storage under the repository's ignored PDF output directory, and replaces the reading copy on success. Run the [numerical replay](../numerics/README.md) separately. [Large-file policy](../../../../../LARGE_FILES.md)
