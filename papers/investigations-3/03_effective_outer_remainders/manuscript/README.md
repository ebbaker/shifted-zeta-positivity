# Effective outer remainders: working manuscript

17 October 2026. Drafted for Edward Baker with substantial LLM assistance.
Recorded model: **Claude Opus 5.5** (`claude-opus-5-5`, Claude Cowork);
reasoning effort: **max**.

**Status: unreviewed working draft created at the user's explicit request
before formal round review.** No review gate or accepted manuscript
milestone is asserted.

- [Compiled manuscript](height_p_transport.pdf): 22 pages.
- [Editable LaTeX source](height_p_transport.tex): the sole current manuscript source.
- [Build record](BUILD_RECORD.json): source/PDF hashes, compiler, scope and layout checks.
- [Round-one research](../notes/round-1/README.md) and [code and records](../numerics/round-1/README.md).

The draft integrates round-one notes 01 and 02. It proves the height-p
transport identity with an explicit remainder (Theorem 4.6) and a bound
for the vertical derivative (Corollary 5.1). It reports their floating
evaluation, which is numerical and not certified, and compares the floor
with Hakimoglu-Brown's at p = 61/20. It checks a 34-row table that restarts
his derivative-kernel comparison from the classical strip, giving
Λ ≤ 0.18891 conditional on his unrefereed lemmas: a cross-check, not a
record. Planning values for the Dirichlet family are labelled as such.
There is no unconditional bound on Λ or Λ_χ and no RH conclusion.

Two same-model subagents checked the proofs and the numbers before
filing. They found no error in the proofs but several small errors that
the manuscript corrects relative to the notes; these are listed in the
[round-one README](../notes/round-1/README.md). Same-model checks do not
replace the pending round review. The author field says "Drafted for
Edward Baker", and the manuscript acknowledges LLM use. Its existence
does not imply the intended author's endorsement.

To rebuild, use a TeX installation with latexmk and pdfLaTeX, from this
directory, directing auxiliary files outside the repository:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/height-p-transport-build height_p_transport.tex

The retained build used TeX Live 2023 and latexmk 4.83; the source also
builds to the same 22 pages with latexmk 4.76 on this computer. All 22
rendered pages were inspected; there are no undefined references or
citations, no overfull boxes and no bitmap fonts. Compiler and visual
checks do not certify mathematics. Keep this single source/PDF pair and
record future versions through Git commits/tags in
[DRAFT_HISTORY.md](../DRAFT_HISTORY.md). No new manuscript snapshot folder
is created.
