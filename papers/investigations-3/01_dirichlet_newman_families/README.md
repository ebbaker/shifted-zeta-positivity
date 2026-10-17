# Dirichlet Newman families

16 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6-astra (Codex)**; reasoning effort: **ultra**.

**Status: contract note filed; independent audit pending.** On 17 October
2026 Claude Opus 5.5 (`claude-opus-5-5`, Claude Cowork, reasoning effort
max) added the
[normalization and transfer-contract note](notes/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md)
and its two [check programmes](numerics/README.md). Proved there: the
kernel and conjugate-pair normalization (Lemma 1.1), Hakimoglu-Brown's
paired-zero inequality for every primitive character (Proposition 3.3) and
the exact time-zero floor of its input (Lemma 3.4). Proof sketch: the
two-sided barrier criterion (Proposition 3.1). Conditional on claimed
zero-free half-planes: Λ_χ ≤ (2B − 1)²/2 for every primitive χ
(Corollary 3.2; 0.28119 from Liu's claimed B_new). Open: Lemma A_p and
H12, the inputs of the large-conductor Target A (for Lemma A_p see
Project 03's [note 01](../03_effective_outer_remainders/notes/01_HEIGHT_P_TRANSPORT_AND_LEMMA_AP_CLAUDE_20261017.md)
of 17 October: proved with an explicit remainder, no loss shown by
floating evaluation on a time grid above conductor about 10⁵,
certification pending; Project 03's
[note 02](../03_effective_outer_remainders/notes/02_HAKIMOGLU_BROWN_COMPARISON_AND_UNCONDITIONAL_TABLE_CLAUDE_20261017.md)
adds the derivative kernel of Hakimoglu-Brown's Theorem 12, which lowers
the Target A planning values by 5–13%). The first bounded test
demotes first-term dominance at existing verification heights (planning
value 0.30 against the conditional 0.2812) and proposes the strip
comparison for Target A. Section 4 values are floating diagnostics or
planning arithmetic, not bounds. The Codex audit the proposal requires has
not been done; conductor numerics remain gated. The 16 October setup
itself reported no result.

Start with the [initial research proposal](research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
and the [portfolio plan](../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md).
Claude leads the analytic contract; Codex audits normalization, finite-height logic and feasibility. These are future model-family responsibilities; record the actual
model and effort when work is performed.

| Folder | Purpose |
| --- | --- |
| [research-overview](research-overview/README.md) | Numbered research proposals and decisions about priorities |
| [notes](notes/README.md) | Incremental derivations and one coordination note per phase |
| [numerics](numerics/README.md) | Reproducible code, parameters and small execution records |
| [reviews](reviews/README.md) | Separate assessments of claims, computations and scope |
| [source-documents](source-documents/README.md) | Reference provenance and links to canonical sources |
| [brainstorm](brainstorm/README.md) | Undeveloped candidate mechanisms with a decision question |
| [manuscript](manuscript/README.md) | A future stable manuscript after a reviewed milestone |
| [chat-histories](chat-histories/README.md) | Canonical records of new project-specific conversations |

The proposal states the opening deliverable, controls, dependencies and
stopping criteria. Its linked earlier results retain their canonical homes;
this project owns only the new work specified there.
Keep this status current at each accepted gate. See [draft history](DRAFT_HISTORY.md),
the [result summaries](../../../result-summaries/README.md) and
[patterns to avoid](../../../avoid/README.md).
