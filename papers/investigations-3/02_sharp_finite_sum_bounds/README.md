# Sharp finite-sum bounds

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

**Status: round one in progress (17 October 2026).** The
[contract and feasibility ledger](notes/round-1/01_SHARP_WEIGHT_CONTRACT_AND_FEASIBILITY_20261017.md)
derives the sharp binding, encloses one sharp row, and closes a revised
infinite-tail budget at t=0.157. The
[bounded gate implementation](notes/round-1/02_BOUNDED_ACTIVE_BRANCH_TRANSFER_IMPLEMENTATION_20261017.md)
now certifies strip transfer across all four finite legs. The complete
approximation allowance is below 3e-7. The other finite-row floors and their
coverage remain open; **no new Newman bound is established**.

Round-one work: prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex)**, reasoning effort **ultra**. Same-model internal
checks only. See the [small reproducible pilots](numerics/round-1/README.md).

A [14-page working manuscript](manuscript/README.md) now assembles these
results at the user’s request. It is explicitly unreviewed and retains the
remaining finite bridge and conditional Newman conclusion.

Start with the [initial research proposal](research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
and the [portfolio plan](../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md).
Claude leads binding, transfer and tail analysis; Codex leads numerical verification and coverage. These are future model-family responsibilities; record the actual
model and effort when work is performed.

| Folder | Purpose |
| --- | --- |
| [research-overview](research-overview/README.md) | Numbered research proposals and decisions about priorities |
| [notes](notes/README.md) | Incremental derivations and one coordination note per phase |
| [numerics](numerics/README.md) | Reproducible code, parameters and small execution records |
| [reviews](reviews/README.md) | Separate assessments of claims, computations and scope |
| [source-documents](source-documents/README.md) | Reference provenance and links to canonical sources |
| [brainstorm](brainstorm/README.md) | Undeveloped candidate mechanisms with a decision question |
| [manuscript](manuscript/README.md) | Unreviewed working draft, editable source and compiled PDF |
| [chat-histories](chat-histories/README.md) | Canonical records of new project-specific conversations |

The proposal states the opening deliverable, controls, dependencies and
stopping criteria. Its linked earlier results retain their canonical homes;
this project owns only the new work specified there.
Keep this status current at each accepted gate. See [draft history](DRAFT_HISTORY.md),
the [result summaries](../../../result-summaries/README.md) and
[patterns to avoid](../../../avoid/README.md).
