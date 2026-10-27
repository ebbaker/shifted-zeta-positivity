# Three regime heat flow dynamics

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

Study how three hypotheses about the canonical heat flow constrain its
solutions across time, height and observation scale: a positive Newman
constant; a zero Newman constant with multiple endpoint zeros; and a zero
Newman constant with only simple endpoint zeros. The first objective is a
quantitative comparison of these conditional dynamics, including what an
average can detect and what it loses.

Start with the [research overview](research-overview/01_THREE_REGIME_DYNAMICS_RESEARCH_OVERVIEW_20261026.md)
and the sole [research progress register](research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md).
The [founding note](brainstorm/01_FOUNDING_DIRECTION_AND_FIRST_COMPARISONS_20261026.md)
records the change of direction. [Dobner's functional approximation](references/01_DOBNER_FUNCTIONAL_APPROXIMATION_20261026.md)
is an initial methodological input.

**Current status, 27 October 2026:** the requested [chat0001 research
summary](notes/06_CHAT0001_RESEARCH_SUMMARY_20261027.md) records all five
analytical deliverables. The latest [narrow-seed result](notes/05_NARROW_SMALL_TIME_DOBNER_SEEDS_20261027.md)
improves the source-derived witness upper envelope to
R_*(tau)<=exp exp(C_d/sqrt(tau)) on0<tau<=1. The actual narrower seed
family is proved on0<tau<=2^{-30}; the earlier theorem covers the remaining
compact interval. [Review03](reviews/03_NARROW_SMALL_TIME_DOBNER_REVIEW_20261027.md)
records separate same-model internal checks. The published approximation
constants remain uninstantiated; no numerical first-zero bound, lower
escape rate or regime exclusion is supplied.

The [first small-time construction](notes/03_SMALL_TIME_CANONICAL_SEEDS_AND_WITNESS_ENVELOPE_20261026.md)
remains a proved baseline with its older tau^{-3} exponent. The
[direct lattice](notes/04_DIRECT_DOBNER_SEED_LATTICE_20261026.md) removes
recurrence on each declared fixed range32<=tau<=C.

The earlier [response note](notes/01_BUFFERED_RESPONSE_AND_RESOLUTION_20261026.md)
and [opening transport budget](notes/02_DOBNER_COMPLETE_CONDITIONAL_BUDGET_20261026.md)
remain available. At the user's request this chat now focuses on Dobner;
the response/growing-window continuation is left for a separate chat.
Research updates prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), actual recorded effort ultra**.

| Folder | Use |
| --- | --- |
| `research-overview/` | Scope, mathematical framework and strategy |
| `research-progress/` | Sole register of this investigation's TRD tasks |
| `brainstorm/` | Exploratory comparisons and discussion notes |
| `notes/` | Subsequent derivations and quantitative research results |
| `numerics/` | Bounded computation protocols and small execution records |
| `reviews/` | Assessments, with reviewer model and effort recorded |
| `references/` | Checked source records and bibliography |
| `chat-histories/` | Unique conversation registrations and founding pointers |

[Investigation 01](../01_heat_density_asymptotics/README.md) supplies the
canonical approximation and exact observable equations;
[02](../02_heat_flow_rh_applications/README.md) owns the application and
literature programs; [03](../03_heat_flow_collision_bounds/README.md) owns
collision-bound acquisition and transfer. This investigation has its own
questions and task IDs, and links to those inputs without duplicating their
live tasks. Positive-threshold contradictions remain within scope alongside
RH-conditional multiplicity questions.

The [founding chat](chat-histories/README.md) retains its existing unique
registration in 03. New chats primarily about this investigation should be
registered here. [DRAFT_HISTORY.md](DRAFT_HISTORY.md) records milestones.

Read the [result index](../../../result-summaries/README.md),
[collision controls](../../../result-summaries/12_collision_controls_and_screening.md)
and [patterns to avoid](../../../avoid/README.md). The repository
[reference workflow](../../../REFERENCE_WORKFLOW.md),
[large-file policy](../../../LARGE_FILES.md) and
[chat-history workflow](../../../tools/CHAT_HISTORY.md) apply.
