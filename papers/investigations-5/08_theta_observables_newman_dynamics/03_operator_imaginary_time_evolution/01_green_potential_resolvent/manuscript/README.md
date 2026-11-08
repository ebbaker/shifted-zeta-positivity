# Green Potentials and Boundary Logarithms for the Newman Family

8 November 2026, America/New_York. Working analytical draft prepared for
**Edward Baker**, with substantial OpenAI Codex LLM assistance. The actual
model and reasoning effort are not recorded in this chat's capture
metadata; no recommended setting is substituted.

[Editable manuscript](main.tex) ·
[23-page reading PDF](../../../../../../output/pdf/08_theta_observables_newman_dynamics/green_potential_resolvent/green_potential_resolvent.pdf) ·
[Production and claim check](../reviews/03_TND_OG_E04_MANUSCRIPT_INTEGRATION_CHECK_20261108.md) ·
[Build record](../numerics/01_TND_OG_E04_MANUSCRIPT_BUILD_20261108.json)

## Development and scope

This is the branch's single evolving manuscript source tree. It develops
the canonical theta source and logarithmic resolvent, the complete strip
Green identity, the exact prime baseline, the uniform square-root
conditioning obstruction, the short-mollifier residual floor and complete
quadratic acquisition ledger, and the local one-sided logarithmic theorem.
The E02 real mixed-term correction is incorporated explicitly. The final
section identifies the remaining assembly, assessment, canonical-value,
uniformity and finite-diagnostic tasks.

The parent manuscript is background and remains unchanged. Classical
inputs and the external short-mollifier moment theorem are attributed;
the latter is imported, not reproved. Existing internal assessment and
proof-author-checking levels are preserved. The full signed-log assembly
is still the E03 target; the manuscript does not execute it or obtain a
favorable canonical value. No numerical research is included.

## Build

From this directory, run:

```sh
bash build.sh
```

The build needs Python 3.9 or later, latexmk, pdfLaTeX and BibTeX, with
the ordinary LaTeX packages named in main.tex. The build was checked
with TeX Live 2023. [prepare_bibliography.py](prepare_bibliography.py)
selects the 18 cited records from their canonical repository
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
records the editorial decisions, and the
[sole branch register](../research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md)
owns current task status.
