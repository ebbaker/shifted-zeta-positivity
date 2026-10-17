# Constructive stable models: working manuscript

17 October 2026. Drafted for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

**Status: unreviewed working draft created at the user's explicit request
before formal round review.** No review gate or accepted manuscript
milestone is asserted.

- [Compiled manuscript](constructive_stable_models.pdf): 11 pages.
- [Editable LaTeX source](constructive_stable_models.tex): the sole current manuscript source.
- [Build record](BUILD_RECORD.json): source/PDF hashes, compiler, scope and layout checks.
- [Round-one research](../notes/round-1/README.md) and [bounded replays](../numerics/round-1/README.md).

The draft proves scoped construction obstructions. Its additional
results exclude independent pure-quartic arrays with a Gaussian component,
even under weak convergence, and require every interacting quartic-network
theta approximation to lose its persistent diffuse sites at readout scale.
The independent-array proof is analytic and needs no numerical theta
moment premise. Infinitesimal interacting and degenerating-site regimes
remain open; there is no theta approximation or RH conclusion.

Classical stability inputs are credited. Same-model authoring checks
do not replace the pending round review. The author field says
“Drafted for Edward Baker,” and the manuscript acknowledges LLM use.
Its existence does not imply the intended author's endorsement.

To rebuild, use a TeX installation with latexmk and pdfLaTeX, from this
directory, directing auxiliary files outside the repository:

    latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/constructive-stable-build constructive_stable_models.tex

The retained build used TeX Live 2023 and latexmk 4.79. All 11 rendered
pages were inspected; there are no undefined references/citations or
overfull boxes. Compiler and visual checks do not certify mathematics.
Keep this single source/PDF pair and record future versions through
Git commits/tags in [DRAFT_HISTORY.md](../DRAFT_HISTORY.md). No new
manuscript snapshot folder is created.
