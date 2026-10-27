# Three regime heat flow dynamics

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

Study how three hypotheses about the canonical heat flow constrain its
solutions across time, height and observation scale: a positive Newman
constant; a zero Newman constant with multiple endpoint zeros; and a zero
Newman constant with only simple endpoint zeros. The first objective is a
quantitative comparison of these conditional dynamics, including what an
average can detect and what it loses.

The [parent overview](research-overview/01_THREE_REGIME_DYNAMICS_RESEARCH_OVERVIEW_20261026.md)
and [TRD progress register](research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md)
track the broader investigation.

**Parameter based collision energy program, 27 October 2026:** the author
has selected an analytical continuation keeping the collision time, height,
positive target and multiplicity general. Start with its
[research overview](research-overview/02_COLLISION_ENERGY_RESEARCH_OVERVIEW_20261027.md),
[CE progress register](research-progress/02_COLLISION_ENERGY_RESEARCH_PROGRESS_20261027.md)
and [multi-goal continuation](notes/08_COLLISION_ENERGY_CONTINUATION_20261027.md).
These define eight subtasks for source estimates, hierarchy errors, energy
transfer, strict canonical bounds and the limit toward zero.
The first research return is now saved in
[Note09](notes/09_COMPLETE_SOURCE_AND_SCALED_ENERGY_TRANSFER_20261027.md) and
[Note10](notes/10_COUPLED_CURVATURE_AND_ENERGY_BUDGET_20261027.md): complete
conditional source/energy interfaces, a paid finite source tail, and the
first coupled exterior correction. The sharper local energy remainder
does not reduce its logarithmic coefficient. The bounded-exterior attempt
has a scoped failure; the independent excluding theta bound remains open.
[Review05](reviews/05_COLLISION_ENERGY_FIRST_RETURN_SELF_ASSESSMENT_20261027.md)
and [the continuation](notes/11_COLLISION_ENERGY_FIRST_RETURN_CONTINUATION_20261027.md)
record the evidence and next decision. Prepared for Edward Baker with substantial
LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

The [founding note](brainstorm/01_FOUNDING_DIRECTION_AND_FIRST_COMPARISONS_20261026.md)
records the change of direction. [Dobner's functional approximation](references/01_DOBNER_FUNCTIONAL_APPROXIMATION_20261026.md)
is an initial methodological input.

**Dobner status, 27 October 2026:** the requested [chat0001 research
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
remain available. Chat0001 owns the Dobner continuation and chat0002 owns
the response/growing-window continuation; the new CE program originated
in chat0003.
Research updates prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), actual recorded effort ultra**.

| Folder | Use |
| --- | --- |
| `research-overview/` | Scope, mathematical framework and strategy |
| `research-progress/` | Separate authoritative registers for TRD tasks and CE subtasks |
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

**Second collision-energy return, chat0005, 27 October 2026:**
[Note12](notes/12_FINITE_TIME_CLUSTER_ENERGY_COMPARISON_20261027.md) proves
a finite-time cluster energy lower comparison with the full real exterior.
[Note13](notes/13_UNCONDITIONED_SOURCE_ACQUISITION_AT_COLLISION_SCALE_20261027.md)
constructs a finite canonical source approximation with explicit tails and
analytic quadrature, without exact low-moment inputs. These strengthen
geometry and acquisition; the universal logarithmic coefficient and missing
theta exclusion remain unchanged. [Review06](reviews/06_FINITE_TIME_COMPARISON_AND_SOURCE_ACQUISITION_REVIEW_20261027.md)
records same-model checks; [Note14](notes/14_SECOND_RETURN_AND_NEXT_CANONICAL_CALCULATION_20261027.md)
gives the next matched comparison. 27 October 2026, chat0005. Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.

**Raw-versus-shifted source comparison, third return, 27 October 2026:**
[Note15](notes/15_MATCHED_RAW_AND_SHIFTED_SOURCE_ERROR_BUDGET_20261027.md)
completes the same-target physical first-jet error budget with fullreflection
before truncation. [Note16](notes/16_STRIP_RADIUS_AND_POSITIVE_SLAB_COMPARISON_20261027.md)
pays the strip-radius cost and proves a positive-slab moving-contour schedule
with a logarithmic gain in the declared source-data ledger. This does not
measure runtime or acquire a lower theta margin. [Review07](reviews/07_RAW_SHIFTED_SOURCE_COMPARISON_REVIEW_20261027.md)
records same-model checks; [Note17](notes/17_RAW_SHIFTED_RETURN_AND_IMPLEMENTATION_CONTRACT_20261027.md)
states the remaining implementation contract. 27 October 2026, chat0005 continuation. Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.

[Consolidated chat0005 handoff](notes/18_CHAT0005_RESEARCH_HANDOFF_20261027.md),
27 October 2026: results from Notes12-17, inherited inputs, exact limits,
verification record and the next bounded source implementation comparison.
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), actual recorded effort ultra**.

**Radial structural continuation, 27 October 2026:** Edward Baker requested a separate investigation following [Note20](notes/20_THREE_DIMENSIONAL_RADIAL_THETA_AND_KELVIN_REDUCTION_20261027.md) and [Note21](notes/21_COLLISION_MECHANISMS_IN_THE_RADIAL_REPRESENTATION_20261027.md). The new [Investigation05](../05_radial_theta_collision_geometry/README.md) develops the radial/Kelvin source, exact forced-boundary dynamics and possible changes to the collision argument. Its [RTC register](../05_radial_theta_collision_geometry/research-progress/01_RADIAL_THETA_COLLISION_RESEARCH_PROGRESS_20261027.md) owns that work; existing TRD/CE ownership is unchanged. Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, chat0006.
