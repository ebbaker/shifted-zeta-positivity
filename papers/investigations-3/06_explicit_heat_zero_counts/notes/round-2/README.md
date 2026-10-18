# Explicit heat zero counts: round-2 continuation

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance: **gpt-6.1-sol (Codex)**, reasoning effort **ultra**.

The user requested this continuation after [Claude Review 02](../../reviews/02_CROSS_MODEL_REVIEW_NOTES_01_02_AND_MANUSCRIPT_CLAUDE_20261017.md).
The original Notes 01–02 remain at their existing paths as the reviewed
baseline; this folder contains the subsequent work requested as round 2.

| Note | Result | Status |
| --- | --- | --- |
| [01: lower cutoff and conjugate-pair extraction](01_LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CODEX_20261017.md) | Comparison from x=100000; K_t(X)<=0.9 log(X+2)+6 for 0<t<=1/2, X>=100000; high-height corollary with additive 5.5 | Proved in-note from named imports; [same-model checks](../../reviews/03_ROUND_TWO_CUTOFF_AND_EXTRACTION_REVIEW_CODEX_20261017.md), no new cross-model review |

The finite [replay package](../../numerics/round-2/README.md) checks constants
and exact adversarial functions. The [current manuscript](../../manuscript/README.md) now integrates this
note and the editorial clarifications. Its prior baseline remains
recoverable from commit `146b3f9`; no research-note text was changed. No consumer gain, lower-height coverage
below 100000, cumulative constant or noncollision result is claimed.

This bounded round stops here. Cross-model review of the new proof is the
next mathematical gate; a consumer tolerance is needed before optimization
or an application budget. See the [result index](../../../../../result-summaries/README.md)
and [avoid index](../../../../../avoid/README.md).
