# Explicit heat zero counts

Updated 17 October 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance: **gpt-6.1-sol (Codex)**, effort **ultra**.
Original setup: **gpt-6-astra (Codex), ultra**, 16 October 2026.

**Status: the original high-height theorem has cross-model LLM review;
the requested round-2 continuation has same-model checks only.**
[Claude Review 02](reviews/02_CROSS_MODEL_REVIEW_NOTES_01_02_AND_MANUSCRIPT_CLAUDE_20261017.md)
accepts Notes 01–02 and the manuscript as **proved from named imports**,
with editorial follow-ups and a recommendation to freeze until a consumer
states a tolerance. No specialist human review has occurred.

The user then requested continued work in [notes/round-2](notes/round-2/README.md).
That bounded continuation proves in-note
`K_t(X) <= (9/10) log(X+2) + 6` for `0<t<=1/2`, `X>=100000`,
and the additive `11/2` corollary for `X>=2000000`. It lowers the
comparison cutoff and improves the extraction using Schwarz–Pick and
conjugate zero pairs. Its [same-model assessment](reviews/03_ROUND_TWO_CUTOFF_AND_EXTRACTION_REVIEW_CODEX_20261017.md)
and [finite arithmetic package](numerics/round-2/README.md) do not extend
Claude's review to the new proof. The range `200<=X<100000`, cumulative
counts and a consumer gain remain open.

The [current manuscript](manuscript/README.md) now integrates the requested
round-2 result in a compiled 13-page source/PDF pair. It includes both
comparison regimes, the sharper extraction and Review 02's editorial
corrections, including a verified time-zero benchmark. Its new proof and
integrated revision have same-model checks only; the earlier cross-model
review is not extended to them. The prior source/PDF is recoverable from
commit `146b3f9`, without a new snapshot folder.

The original [Note 01](notes/01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md)
and [Note 02](notes/02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md)
remain unchanged. Their baseline result was `(6/5)log(X+2)+22` for
`0<t<=1/2`, `X>=2000000`. The old checker equality label and replay
record have been corrected; historical note/review statements retain
their creation-time scope.

This round stops at its proof and replay package. Cross-model analytic
review of the new cutoff and extraction is the next gate. A consumer must
state its kernel, domain, baseline and tolerance before an application
budget or further optimization; none was supplied in this round.

| Folder | Purpose |
| --- | --- |
| [research-overview](research-overview/README.md) | Proposal, gates and current execution status |
| [notes](notes/README.md) | Reviewed baseline and the requested round-2 continuation |
| [numerics](numerics/README.md) | Reproducible code and small execution records |
| [reviews](reviews/README.md) | Separate assessments with precise review scopes |
| [source-documents](source-documents/README.md) | Reference provenance and canonical links |
| [brainstorm](brainstorm/README.md) | Candidate mechanisms with a decision question |
| [manuscript](manuscript/README.md) | Current integrated source/PDF pair and build record |
| [chat-histories](chat-histories/README.md) | Canonical records of project-specific conversations |

Start with the [initial proposal](research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md),
[portfolio plan](../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md),
[draft history](DRAFT_HISTORY.md), [result summaries](../../../result-summaries/README.md)
and [patterns to avoid](../../../avoid/README.md).

Baseline identity qualification: Note 01 already received a hyperlink-only
repair in commit `452eee4`. The old review/build hash identifies the text
before that repair. The [round-2 execution record](numerics/round-2/LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CHECKS_20261017.json)
checks that reversing exactly the one repaired link recovers those reviewed
bytes; no mathematical text changed. This round leaves Note 01 unchanged.
