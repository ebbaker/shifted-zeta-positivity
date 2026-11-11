# Green Potentials and Boundary Logarithms for the Newman Family

10 November 2026, America/New_York. Working draft updated through E08, prepared for
**Edward Baker**, with substantial OpenAI Codex LLM assistance. The actual
model and reasoning effort are not recorded in this chat's capture
metadata; no recommended setting is substituted.

[Editable manuscript](main.tex) ·
[26-page reading PDF](../../../../../../output/pdf/08_theta_observables_newman_dynamics/green_potential_resolvent/green_potential_resolvent.pdf) ·
[Current editorial check](../reviews/14_TND_OG_POST_E08_MANUSCRIPT_RECONCILIATION_CHECK_20261110.md) ·
[Current build record](../numerics/10_TND_OG_POST_E08_MANUSCRIPT_BUILD_20261110.json)

## Development and scope

This is the branch's single evolving manuscript source tree. It develops
the canonical theta source and logarithmic resolvent, the complete strip
Green identity, the exact prime baseline, the uniform square-root
conditioning obstruction, the short-mollifier residual floor and complete
quadratic acquisition ledger, and the local one-sided logarithmic theorem.
The E02 real mixed-term correction is incorporated explicitly. Section 9
now includes the completed E03/E05 signed-log assembly, the E06 recipe
failure, assessed B05 r1 deflation, conditional B05 r2 contour design,
E08's four finite certificates and the inherited OC-census Green bound.
It separates the remaining signed-value, uniformity and total-cost questions.

The parent manuscript is background and remains unchanged. Classical
inputs and the external short-mollifier moment theorem are attributed;
the latter is imported, not reproved. Existing internal assessment and
proof-author-checking levels are preserved. E08 excludes its known-region
rectangle directly; it does not supply the complete signed J(30) value.
The finite J(1500) consequence uses a stronger inherited zero census.
No new numerical research was performed by this editorial update.
The [8 November integration check](../reviews/03_TND_OG_E04_MANUSCRIPT_INTEGRATION_CHECK_20261108.md)
and [original build record](../numerics/01_TND_OG_E04_MANUSCRIPT_BUILD_20261108.json)
remain historical, superseded for current manuscript coverage only.

## Build

From this directory, run:

```sh
bash build.sh
```

The build needs Python 3.9 or later, latexmk, pdfLaTeX and BibTeX, with
the ordinary LaTeX packages named in main.tex. The build was checked
with TeX Live 2023. [prepare_bibliography.py](prepare_bibliography.py)
selects the 28 cited records from their canonical repository
bibliographies and writes a combined build-only bibliography. External
reference ownership is unchanged; the branch's new
[internal manuscript records](../references/manuscript_sources.bib) are
kept separately.

All generated PDF, bibliography, log and auxiliary files go to the ignored
repository-root output/pdf location linked above. Rebuild the reading copy
if that generated file is absent. Do not create manuscript snapshot
folders or place generated PDFs here; follow
[LARGE_FILES](../../../../../../LARGE_FILES.md).

The [source-use record](../references/05_TND_OG_E04_MANUSCRIPT_SOURCE_USE_20261108.md)
identifies actual primary passages checked. The
[session note](../brainstorm/notes/04_TND_OG_E04_MANUSCRIPT_DEVELOPMENT_20261108.md)
records the original editorial decisions; the
[post-E08 discussion](../brainstorm/notes/12_TND_OG_POST_E08_STATE_AND_PATHS_20261110.md)
records the present reconciliation and research ranking. The
[sole branch register](../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md)
owns current task status.
