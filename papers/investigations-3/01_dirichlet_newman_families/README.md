# Dirichlet Newman families

17 October 2026 continuation. Prepared for Edward Baker with substantial LLM assistance.
Recorded model for this update: **gpt-6-astra (Codex), reasoning effort max**.

**Current status: comparison proved in-note without H12; research manuscript
expanded after review.** The [manuscript](manuscript/main.tex)
([PDF](manuscript/main.pdf)) proves the initial-floor comparison and gives
**Lambda_chi <= 0.27 for every primitive character with q >= 10^12**, and
**Lambda_chi = O((log q)^(-4/7)) -> 0** in the conductor aspect.
The [round-3 proof](notes/round-3/03_SINE_TAIL_LIMIT_AND_COMPARISON_CODEX_20261017.md)
uses a real sine tail to preserve the global initial floor, confines the
nonreal zeros of each approximant, and passes the heat comparison to the
original function. H12 for the original character flow remains open and
is not a premise of these two results. No GRH or quasi-RH assumption is used.

[Review 03](reviews/03_CROSS_MODEL_MATHEMATICAL_REVIEW_CODEX_20261017.md)
found no substantive mathematical defect in the reviewed version and
replayed its exact scalar certificate. It used gpt-6-astra, whereas the
round-2/3 derivation used gpt-6.1-sol: this is internal review using another
GPT model, following the [same-model checks in review 02](reviews/02_SINE_TAIL_AND_MANUSCRIPT_CHECK_CODEX_20261017.md).
Independent specialist review and a priority audit remain outstanding.
The [review response](notes/round-4/04_REVIEW_RESPONSE_AND_SIBLING_BENCHMARK_CODEX_20261017.md)
records the current edits, including analytic proof appendices and the
public provenance entry. Those new appendices have an authoring check,
not a separate independent review.

**Current finite benchmark: 0.215 at the same conductor threshold.**
Project 03's [uniform positive-time floor and restarted comparison](../03_effective_outer_remainders/notes/round-2/README.md)
give **Lambda_chi <= 43/200 = 0.215** for primitive q >= 10^12.
Its status remains proved in-note from named imports, with Arb/exact
certificates and internal same-model checks. A
[further audit](../03_effective_outer_remainders/reviews/03_FAMILY_FLOOR_AND_RESTART_AUDIT_CODEX_20261017.md)
checked the analytic domination and restart and reproduced both certificate
outputs byte for byte; it is also same-model review of that work.
Retain 0.27 as the simpler initial-floor application. Compare future finite
bounds with 0.215; the general comparison and conductor exponent are
separate contributions. The [original scalar record](numerics/DIRICHLET_SCALAR_CONDITIONAL_CERTIFICATE_20261017.json)
is unchanged.

The historical [round-1 contract](notes/round-1/01_NORMALIZATION_AND_TRANSFER_CONTRACT_CLAUDE_20261017.md)
was assessed in [review 01](reviews/01_NORMALIZATION_AND_TRANSFER_CONTRACT_REVIEW_CODEX_20261017.md).
It established the normalization, paired-zero algebra and time-zero floor;
its zero-loss planning tables and claimed-half-plane consequences retain
their stated assumptions. The [round-2 note](notes/round-2/02_BURGERS_FLOOR_AND_CONDITIONAL_COMPARISON_CODEX_20261017.md)
proved the Burgers floor and compact comparison. Its H12-dependent
quantitative conclusion was superseded by round 3. The former opening
status, “contract note filed; independent audit pending,” described that
earlier stage and is superseded by this update.

The [source ledger](source-documents/README.md) records Ki–Kim–Lee's earlier
qualitative result for real primitive characters and the incomplete public
discussion of the conductor limit. No priority claim is made.

The [initial research proposal](research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md)
and [portfolio plan](../research-overview/01_PORTFOLIO_RESEARCH_PLAN_20261016.md)
retain their historical planning context. Model suggestions in those plans
are not requirements. Edward Baker chooses models with latency and usage
in mind and generally tries to alternate GPT and Claude between derivation
and review. Each artifact records the model and effort actually used.

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
