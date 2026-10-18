# Effective outer remainders working manuscript

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

**Status: round-one cross-model LLM review corrections incorporated;
round-two result proved in accompanying notes with same-model checks.**
Independent specialist review and an accepted manuscript milestone remain
outstanding. The original draft was prepared by Claude Opus 5.5
(`claude-opus-5-5`, Claude Cowork, effort max); this revision and the new
research used gpt-6-astra (Codex), effort ultra.

- [Compiled manuscript](height_p_transport.pdf): 24 pages.
- [Editable LaTeX source](height_p_transport.tex): the sole current source.
- [Build record](BUILD_RECORD.json): current hashes, compiler and layout checks.
- [Round-one review](../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CODEX_20261017.md).
- [Round-two proofs](../notes/round-2/README.md) and [review](../reviews/02_UNIFORM_FLOOR_AND_RESTARTED_COMPARISON_REVIEW_CODEX_20261017.md).

The manuscript proves the height-p transport identity and complete
remainder, reports the original floating evaluations with their proper
quantifiers, and retains the conditional zeta table Λ ≤ 0.18891. The
current source corrects real saddle uniqueness to [σ₀,∞), updates the
Project 01 links, and summarizes the new uniform regime: for primitive
q ≥ 10¹², Sχ(x,3,t) > 6 on every real x and 0 ≤ t ≤ 1/4, yielding
Λχ ≤ 0.215 by a restarted comparison. The full new proofs and certificates
are in round two. The old lower-conductor tables and derivative-circle
consumer are not thereby certified.

To rebuild with latexmk and pdfLaTeX, keeping auxiliaries outside the repo:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=/tmp/height-p-transport-build height_p_transport.tex
```

The retained revision uses TeX Live 2023 and latexmk 4.79 on macOS.
All 24 pages were rendered and visually checked; the build has no
undefined references or citations, overfull boxes, or bitmap fonts.
Compilation and layout checks do not validate mathematics. The author
field and LLM acknowledgement are present. Versions are recorded in
[DRAFT_HISTORY.md](../DRAFT_HISTORY.md); no new snapshot folder is created.
