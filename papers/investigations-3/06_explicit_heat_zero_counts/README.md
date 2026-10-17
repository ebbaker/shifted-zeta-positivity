# Explicit heat zero counts

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

**Status: unreviewed working manuscript drafted; review remains deferred.**
The [11-page manuscript](manuscript/explicit_heat_zero_counts.pdf),
[editable source](manuscript/explicit_heat_zero_counts.tex) and
[build record](manuscript/BUILD_RECORD.json) assemble the first two rounds
at the user's request. No accepted review milestone is asserted.
The [second research note](notes/02_EXPLICIT_OFF_AXIS_COMPARISON_AND_HIGH_HEIGHT_COUNT_20261017.md)
derives a uniform off-axis comparison and the local bound
`K_t(X) <= (6/5) log(X+2) + 22` for `0<t<=1/2`, `X>=2,000,000`.
This is an unreviewed analytic derivation from named classical inputs;
the [exact arithmetic record](numerics/OFF_AXIS_COMPARISON_CHECKS_20261017.json)
checks its finite constants. The range `200<=X<2,000,000`, cumulative
counts and an active consumer budget remain open. The user requested
continued work and postponed review for further rounds on 17 October.

The [opening ledger](notes/01_CONSUMER_AUDIT_AND_CONSTANT_LEDGER_20261017.md)
and its [same-model review](reviews/01_OPENING_LEDGER_REVIEW_CODEX_20261017.md)
remain the frozen first-round record; that review does not cover Note 02.
Both rounds: **gpt-6.1-sol (Codex), ultra**, with substantial LLM assistance.

Start with the [initial research proposal](research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
and the [portfolio plan](../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md).
Codex extracts constants and the consumer budget; Claude audits the analytic proof and uniformity. These are future model-family responsibilities; record the actual
model and effort when work is performed.

| Folder | Purpose |
| --- | --- |
| [research-overview](research-overview/README.md) | Numbered research proposals and decisions about priorities |
| [notes](notes/README.md) | Incremental derivations and one coordination note per phase |
| [numerics](numerics/README.md) | Reproducible code, parameters and small execution records |
| [reviews](reviews/README.md) | Separate assessments of claims, computations and scope |
| [source-documents](source-documents/README.md) | Reference provenance and links to canonical sources |
| [brainstorm](brainstorm/README.md) | Undeveloped candidate mechanisms with a decision question |
| [manuscript](manuscript/README.md) | Current unreviewed working manuscript and build record |
| [chat-histories](chat-histories/README.md) | Canonical records of new project-specific conversations |

The proposal states the opening deliverable, controls, dependencies and
stopping criteria. Its linked earlier results retain their canonical homes;
this project owns only the new work specified there.
Keep this status current at each accepted gate. See [draft history](DRAFT_HISTORY.md),
the [result summaries](../../../result-summaries/README.md) and
[patterns to avoid](../../../avoid/README.md).
