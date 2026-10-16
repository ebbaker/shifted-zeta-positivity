# Build the N4SYM manuscript

The entry point is [manuscript.tex](manuscript.tex); it inputs `preamble.tex`, `sections/*.tex` and
`references.tex` and nothing outside this directory. A usual TeX Live installation with latexmk, pdfLaTeX,
Latin Modern, AMS packages, microtype and hyperref suffices.

From this directory:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex
    cp build/manuscript.pdf manuscript.pdf

The build directory is not tracked. Inspect every rendered page before recording a milestone:

    pdftoppm -r 110 -png build/manuscript.pdf build/page

There is no `validation/drafts.py` record for this manuscript yet. Manuscript milestones are recorded in
[DRAFT_HISTORY.md](DRAFT_HISTORY.md) by commit or tag, without dated snapshots. The seven diagnostic programs
under [numerics](numerics/README.md) replay independently of the manuscript; register them in a validation
replay in the same pass that records the first reviewed build. A matching hash or a visual-review note is not
evidence of mathematical correctness.
