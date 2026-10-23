# Complete-source coefficient transport manuscript

23 October 2026. Drafted for **Edward Baker** with substantial LLM assistance.
Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**.

The [current PDF](main.pdf) is a 19-page working research draft. Its
[main source](main.tex) includes the five section files in this directory.
Open this directory in the desktop LaTeX editor for source editing and a
live preview. The [review](../reviews/14_MANUSCRIPT_AND_RESEARCH_RESET_REVIEW_20261023.md)
records mathematical cross-checks, scope and rendering checks; the
[next-step assessment](../notes/16_RESEARCH_RESET_AND_NEXT_STEPS_20261023.md)
separates the recommended diagnostic from the missing global estimate.

From this directory, a local TeX installation can rebuild using:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/hdc-manuscript-build main.tex
```

Create the chosen output directory first if needed. Intermediate files are
not part of the manuscript deliverable. The
[build record](BUILD_RECORD_20261023.json) identifies this source and PDF;
byte-identical PDF regeneration is not promised because PDF metadata includes
build time. Research derivations, executable checks and receipts remain in
the parent investigation's notes, numerics and reviews folders.

This is the current editable manuscript, with milestones indexed in
[DRAFT_HISTORY.md](../DRAFT_HISTORY.md). No new snapshot folder, Git commit
or tag was created. The manuscript establishes no RH theorem or new global
simplicity proportion and remains subject to specialist mathematical review.
