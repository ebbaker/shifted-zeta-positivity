# Explicit heat zero counts: revised manuscript

17 October 2026, America/New_York. Drafted for Edward Baker with substantial
LLM assistance: **gpt-6.1-sol (Codex)**, effort **ultra**.

**Status: round-2 result integrated; new proof and revision have same-model
checks only.** The [earlier version](https://github.com/ebbaker/shifted-zeta-positivity/tree/146b3f9/papers/investigations-3/06_explicit_heat_zero_counts/manuscript)
received [Claude Review 02](../reviews/02_CROSS_MODEL_REVIEW_NOTES_01_02_AND_MANUSCRIPT_CLAUDE_20261017.md).
That review covers its original source identity, not the changed cutoff or
paired extraction. The [round-2 assessment](../reviews/03_ROUND_TWO_CUTOFF_AND_EXTRACTION_REVIEW_CODEX_20261017.md)
and manuscript transcription checks are same-model work. Specialist human
review has not occurred; cross-model review of the extension remains pending.

- [Compiled manuscript](explicit_heat_zero_counts.pdf): 13 pages.
- [Editable source](explicit_heat_zero_counts.tex): current manuscript.
- [Build record](BUILD_RECORD.json): current source/PDF and input hashes,
  earlier-version identities, review scopes, compiler and layout checks.
- [Round-2 derivation](../notes/round-2/01_LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CODEX_20261017.md)
  and [arithmetic package](../numerics/round-2/README.md).

The main theorem is `K_t(X)<=0.9 log(X+2)+6` for `0<t<=1/2`,
`X>=100000`, with additive `11/2` for `X>=2000000`. The unified proof
retains both comparison budgets, ordinary error regimes and remainder
prefactors. It includes the Schwarz–Pick and conjugate-pair extraction,
full multiplicity and endpoint conventions, and the review's editorial
corrections: explicit source slips, indirect Arias de Reyna/Boyd imports,
mean-density/loss context and the primary-source-checked time-zero benchmark.

The author field names the intended recipient and the acknowledgment
records LLM assistance. No new application gain or collision exclusion is
claimed. Coverage below X=100000, cumulative constants and a consumer
budget remain open.

Rebuild from this directory, keeping auxiliary files outside the repository:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -pdflatex='pdflatex -no-shell-escape %O %S' -outdir=/tmp/explicit-heat-counts-build explicit_heat_zero_counts.tex
```

The saved build uses TeX Live 2023 and latexmk 4.79, with shell escape disabled.
All 13 rendered pages were visually inspected; there are no undefined
references/citations, overfull/underfull boxes, duplicate labels or text
outside page bounds. Compilation and visual QA are not mathematical review.
All saved files remain below 1 MiB. No snapshot folder was created; the old
version is recoverable from commit `146b3f9`. See [draft history](../DRAFT_HISTORY.md).

Baseline Note 01's current hash differs from its historical reviewed hash
only because of a pre-existing hyperlink repair in commit `452eee4`. The
[round-2 record](../numerics/round-2/LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CHECKS_20261017.json)
verifies that reversing that single repair recovers the reviewed bytes.
The current build records both identities; the research notes are unchanged.
