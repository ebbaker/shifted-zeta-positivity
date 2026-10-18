# Constructive stable models

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

**Status: opening search closed after cross-model review; further construction gated.**
The [round-one review](reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md)
found no mathematical error in the scoped results, but showed that the main
obstructions also exclude a known stable Bessel control. They describe
family expressiveness, not theta stability. The review is internal LLM
review, not specialist human review.

The [round-two continuation](notes/round-2/README.md), dated 17 October 2026,
checks the review's extensions. Weak convergence suffices for the
interacting-quartic persistent-site obstruction. Fixed heat rollback
excludes the original independent-spin family at **all nonpositive
preparation times**, including times tending to minus infinity, for each
fixed nonnegative theta target time. A separate classical Newman-class
argument also excludes theta and the stable Bessel control as weak limits
of diverging heat tilts of general symmetric LP seeds. These round-two
proofs have same-model authoring checks; cross-model review is pending.
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), effort ultra**.

No qualifying theta approximation has been obtained. The completed opening
search is dormant pending a named new construction with a proved Bessel
(or Pólya stable-control) approximation and a theta-specific estimate.
General interacting infinitesimal arrays and fixed non-Gaussian Cardon
multipliers remain unresolved; independent-spin mean-field heat with
unbounded negative preparation times is no longer an open escape.

The [round-one manuscript](manuscript/README.md) remains a working record,
with no accepted manuscript milestone; it has not been revised to include
round two. Its original source, PDF and build record are retained.
Nomination, compatibility and diagnostics in round one preceded its first
cross-model review at the user's explicit request. Round-two notes now
supply the reconciliation; the original review remains unchanged.

Start with the [initial research proposal](research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
and the [portfolio plan](../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md).
Claude proposes the stable construction; Codex checks coefficient, heat and convergence compatibility. These are future model-family responsibilities; record the actual
model and effort when work is performed.

| Folder | Purpose |
| --- | --- |
| [research-overview](research-overview/README.md) | Numbered research proposals and decisions about priorities |
| [notes](notes/README.md) | Incremental derivations and one coordination note per phase |
| [numerics](numerics/README.md) | Reproducible code, parameters and small execution records |
| [reviews](reviews/README.md) | Separate assessments of claims, computations and scope |
| [source-documents](source-documents/README.md) | Reference provenance and links to canonical sources |
| [brainstorm](brainstorm/README.md) | Undeveloped candidate mechanisms with a decision question |
| [manuscript](manuscript/README.md) | Reviewed round-one working record and original build record |
| [chat-histories](chat-histories/README.md) | Canonical records of new project-specific conversations |

The proposal states the opening deliverable, controls, dependencies and
stopping criteria. Its linked earlier results retain their canonical homes;
this project owns only the new work specified there.
Keep this status current at each accepted gate. See [draft history](DRAFT_HISTORY.md),
the [result summaries](../../../result-summaries/README.md) and
[patterns to avoid](../../../avoid/README.md).
