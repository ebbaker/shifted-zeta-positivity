# Dirichlet Newman families

17 October 2026 update. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex), reasoning effort ultra**.

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
Project 03's [note 01](../03_effective_outer_remainders/notes/round-1/01_HEIGHT_P_TRANSPORT_AND_LEMMA_AP_CLAUDE_20261017.md)
of 17 October: proved with an explicit remainder, no loss shown by
floating evaluation on a time grid above conductor about 10⁵,
certification pending; Project 03's
[note 02](../03_effective_outer_remainders/notes/round-1/02_HAKIMOGLU_BROWN_COMPARISON_AND_UNCONDITIONAL_TABLE_CLAUDE_20261017.md)
adds the derivative kernel of Hakimoglu-Brown's Theorem 12, which lowers
the Target A planning values by 5–13%). The first bounded test
demotes first-term dominance at existing verification heights (planning
value 0.30 against the conditional 0.2812) and proposes the strip
comparison for Target A. Section 4 values are floating diagnostics or
planning arithmetic, not bounds. The Codex audit the proposal requires has
not been done; conductor numerics remain gated. The 16 October setup
itself reported no result.
**Status: comparison proved in-note without H12; initial manuscript drafted.**
The [round-3 proof](notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md)
adds a real sine tail to canonical-product truncations, preserves the
global initial logarithmic-derivative floor, proves confinement for each
approximant, and passes the heat comparison to the original function.
It bypasses H12 for the character flow; that separate assertion remains open.

The [manuscript](manuscript/main.tex) ([PDF](manuscript/main.pdf)) gives
**Lambda_chi <= 0.27 for every primitive character with q >= 10^12**, and
**Lambda_chi = O((log q)^(-4/7)) -> 0** in the conductor aspect.
These are proved in-note and in the draft, with internal same-model checks
recorded in [review 02](reviews/02_SINE_TAIL_AND_MANUSCRIPT_CHECK_CODEX_20261017.md).
Independent specialist review and a priority audit remain outstanding.
No GRH or quasi-RH assumption is used. The
[exact scalar record](numerics/DIRICHLET_SCALAR_CONDITIONAL_CERTIFICATE_20261017.json)
is unchanged; the new proof supplies its analytic consumer.

The [round-1 contract](notes/round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md)
was assessed in [review 01](reviews/01_NORMALIZATION_AND_TRANSFER_CONTRACT_REVIEW_CODEX_20261017.md).
The [round-2 note](notes/round-2/02_BURGERS_FLOOR_AND_CONDITIONAL_COMPARISON_CODEX_20261017.md)
proves the positive-time Burgers/Riccati floor and the compact comparison.
Its conditional quantitative conclusion is superseded by round 3. Round 1's
zero-loss planning tables retain their unproved assumptions. A dated
correction records Ki–Kim–Lee's earlier qualitative result for real
primitive characters; no novelty claim is made.

Start with the [initial research proposal](research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
and the [portfolio plan](../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md).
Future model-family assignments in the proposal are distinct from the
actual model and effort recorded in each artifact.

| Folder | Purpose |
| --- | --- |
| [research-overview](research-overview/README.md) | Numbered research proposals and decisions about priorities |
| [notes](notes/README.md) | Incremental derivations organized by research round |
| [numerics](numerics/README.md) | Reproducible code, parameters and small execution records |
| [reviews](reviews/README.md) | Separate assessments of claims, computations and scope |
| [source-documents](source-documents/README.md) | Reference provenance and links to canonical sources |
| [brainstorm](brainstorm/README.md) | Undeveloped candidate mechanisms with a decision question |
| [manuscript](manuscript/README.md) | One editable manuscript and its compiled PDF |
| [chat-histories](chat-histories/README.md) | Canonical records of project-specific conversations |

See [draft history](DRAFT_HISTORY.md), the
[result summaries](../../../result-summaries/README.md) and
[patterns to avoid](../../../avoid/README.md).
