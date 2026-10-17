# Explicit heat zero counts: working manuscript

17 October 2026. Drafted for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

**Status: unreviewed working draft created at the user's explicit request
while round review remains deferred.** No review gate or accepted manuscript
milestone is asserted.

- [Compiled manuscript](explicit_heat_zero_counts.pdf): 11 pages.
- [Editable LaTeX source](explicit_heat_zero_counts.tex): the sole current manuscript source.
- [Build record](BUILD_RECORD.json): source/PDF hashes, input-note identities, compiler and layout checks.
- [Opening ledger](../notes/01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md) and
  [explicit comparison derivation](../notes/02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md).

The draft assembles the time-uniform local multiplicity-count bound
`K_t(X) <= (6/5) log(X+2) + 22` for `0<t<=1/2`, `X>=2,000,000`.
It includes the off-axis comparison, general-real-part remainder proof,
fixed-index remainder term and the conditional count-extraction lemma.
The lower-height gap, cumulative constants and consumer feasibility remain
open. Classical analytic inputs are cited; finite checks do not formally
verify those inputs or the universal analytic arguments.

The author field says "Drafted for Edward Baker," and the manuscript
acknowledges LLM assistance with the recorded model and effort. The earlier
same-model review applies to Note 01 only. No new review was commissioned.

To rebuild from this directory with TeX Live, directing auxiliary files
outside the repository:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/explicit-heat-counts-build explicit_heat_zero_counts.tex
```

The saved build used pdfTeX from TeX Live 2023 and latexmk 4.79, with shell
escape disabled. All 11 rendered pages were inspected, with full-page
mathematical layout checks on pages 5, 6 and 9. There are no undefined
references/citations or overfull boxes. Compilation and layout checks do
not constitute mathematical review.

Keep this source/PDF pair and record later versions with Git commits or
tags in [DRAFT_HISTORY.md](../DRAFT_HISTORY.md), without snapshot folders.
