# Heat-flow applications to RH and zero geometry

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded reasoning
effort max**. Configuration is verified from this chat's turn metadata.

**Status: exploratory investigation.** Study what the new canonical
heat-flow bounds can contribute to RH-related problems, starting with
Rodgers–Tao's zero dynamics while retaining Newman upper bounds,
RH-conditional simplicity, and other quantitative applications. A coequal
goal is to work backward from these applications to identify aspirational
bounds that could guide the still-developing intermediate estimates. No route
is selected as the exclusive program, and no new bound on the Newman
constant or zero-exclusion theorem is claimed.

Start with the maintained [current summary](summary/CURRENT_SUMMARY.md).
It preserves the [opening brainstorm](notes/01_HEAT_FLOW_RH_APPLICATIONS_BRAINSTORM_20261026.md)
and tracks the follow-up [positive-threshold Rodgers–Tao analysis](notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md).
The dedicated [Rodgers–Tao program](rodgers_tao/README.md) now has its own
initial-results note, [research overview](rodgers_tao/research-overview/01_RODGERS_TAO_RESEARCH_OVERVIEW_20261026.md),
and [progress register](rodgers_tao/research-progress/01_RODGERS_TAO_RESEARCH_PROGRESS_20261026.md).
The [Book application review](reviews/01_BOOK_APPLICATION_REVIEW_20261026.md)
records the original approximation baseline.
The [Book](../01_heat_density_asymptotics/book/main.tex) and its technical
companions remain the homes of the approximation proofs. This investigation
owns their proposed consumers and comparisons, without changing the parent
program's task statuses.

| Direction | First useful question |
| --- | --- |
| Bounds needed for progress | What domain, norm, accuracy, and parameter dependence would make an estimate useful for a named application? |
| Rodgers–Tao dynamics and energy | Can a complete field/jet estimate improve a localized energy or exterior-interaction bound, with every boundary term retained? |
| Positive-threshold contradiction | What theta-specific estimate could exclude a finite collision under the hypothetical positive threshold, or improve a fixed positive upper bound? |
| Newman upper bounds | Can a small-positive-time estimate improve a complete barrier/exterior certificate or its cost? |
| RH implies simple zeros | What source-specific arithmetic estimate distinguishes theta from the existing multiple-endpoint controls? |
| Other quantitative applications | Can the bounds yield effective negative-time witnesses, finer counts, or useful moving-time zero asymptotics? |

The [summary folder](summary/README.md) tracks ideas and priorities in place.
Research goes in [notes](notes/README.md), computation in
[numerics](numerics/README.md), and assessments in [reviews](reviews/README.md).
[References](references/README.md) retain checked versions and external PDF
receipts. [Chat histories](chat-histories/README.md) contain this conversation's
unique registration. [DRAFT_HISTORY.md](DRAFT_HISTORY.md) records milestones;
no manuscript snapshot folder is created.

The [result summaries](../../../result-summaries/README.md) and
[patterns to avoid](../../../avoid/README.md) apply. In particular, read
[heat-flow results](../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[collision controls](../../../result-summaries/12_collision_controls_and_screening.md),
[local geometry](../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[target classification](../../../avoid/01_restating_the_target.md), and
[control screening](../../../avoid/02_shape_only_arguments_and_the_controls.md).

Recommended opening work: a concrete specification of bounds needed by
one Rodgers–Tao consumer, compared with what the Book already provides.
The present focus is the positive-threshold question: distinguish forward
relaxation from the missing local endpoint control, and compare a complete
energy estimate with a direct first-jet certificate on a fixed positive slab.
An informative gap analysis is a valid planning output before the missing
estimate is proved. Keep a small-positive-time certificate comparison
alongside it if its hypotheses can be met.
This recommendation is a research judgment, not a claim that the other
directions cannot succeed.
