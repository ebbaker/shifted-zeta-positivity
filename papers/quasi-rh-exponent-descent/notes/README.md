# Investigation summary and notes index

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.

This project investigates arithmetic exponent descent toward RH and exclusion
of positive-time Newman collisions. Five investigation folders sit directly
under `papers/quasi-rh-exponent-descent/`, each with its own `notes/` folder.
Shared plans, results summaries, and the dependency ledger remain here.

Each investigation numbers its notes independently from `1_`, followed by
the existing title and date, for example
`1_FIXED_SCALE_DESCENT_CRITERION_20261008.md`. Numbers follow approximate
research progression where the original order is uncertain. For future
notes, use the next unused number in that investigation and retain the date;
keep existing numbers stable. Shared program records and this index retain
their filenames.

Start with the [latest short-family continuation](../short_families/notes/7_SHORT_FAMILY_CONTINUATION_20261008.md),
then the [dependency ledger](RESEARCH_LEDGER_20261008.md) and the
[broad continuation plan](CODEX_CONTINUATION_20261008.md).
The [project overview](../README.md) gives the common notation and motivation.

The notes establish reductions, conditional criteria, controlled sectors, and
obstructions. The necessary new signed arithmetic estimates remain open;
no new zero-free strip or implication from zeta-only quasi-RH to RH is proved.
Reviews and finite checks have the scope recorded in the dependency ledger.

## Project map

Paths below are relative to `papers/quasi-rh-exponent-descent/`.

| Project | Notes folder | Focus and remaining task |
| --- | --- | --- |
| Fixed-scale descent | [`fixed_scale_descent/notes/`](../fixed_scale_descent/notes/) | A fixed multiplicative-scale contraction would improve the variance exponent; prove the signed arithmetic contraction. |
| Short character families | [`short_families/notes/`](../short_families/notes/) | Extract a stronger strip from a new short-family moment; control the complete signed low-overlap remainder. |
| Mixed character families | [`mixed_character_families/notes/`](../mixed_character_families/notes/) | Refine conductor sectors while preserving selectors and masks; estimate the remaining signed cycle or fixed-vector energy. |
| Integer quadratic lift | [`integer_quadratic_lift/notes/`](../integer_quadratic_lift/notes/) | Lift the complete integer response into a quadratic family; prove the new weighted small-conductor moment. |
| Newman collisions | [`newman_collisions/notes/`](../newman_collisions/notes/) | Exclude positive-time real collisions; certify middle heights and control the limit as the positive time floor tends to zero. |

## Fixed-scale descent

A contraction at fixed multiplicative scales with a power-decaying error
would force strict variance-exponent improvement. The spectral and arithmetic
notes explain why logarithmic savings, factor-scale contraction, and pole
cancellation alone do not supply that improvement.

1. [Fixed-scale descent criterion](../fixed_scale_descent/notes/1_FIXED_SCALE_DESCENT_CRITERION_20261008.md): sufficient recurrence and its exact signed prime formulation.
2. [Spectral edge and logarithmic savings](../fixed_scale_descent/notes/2_SPECTRAL_EDGE_AND_LOG_SAVINGS_20261008.md): boundary-zero issues and a model separating logarithmic savings from power improvement.
3. [Arithmetic feedback and resonance](../fixed_scale_descent/notes/3_ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md): complete mixed remainder, moving-cutoff transform, and the unresolved signed delay defect.

## Short character families

Finite reuse of one hypothetical short-family moment removes the prime-mask
error. Diagonal subtraction, second Poisson summation, and overlap bounds
reduce the residual region, but the low-overlap signed core remains open.
The prime-selected obstruction and generic sieve and replication limits
constrain which estimates could close that gap.

1. [Descent refinement](../short_families/notes/1_SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md): conditional extraction and finite reuse of a fixed moment.
2. [Small-cofactor reduction](../short_families/notes/2_SHORT_FAMILY_SMALL_COFACTOR_20261008.md): diagonal subtraction and second-Poisson decay.
3. [Core involution](../short_families/notes/3_SHORT_FAMILY_CORE_INVOLUTION_20261008.md): corrected conjugations, exact involution, and the prime-column obstruction.
4. [High-overlap bound](../short_families/notes/4_SHORT_FAMILY_HIGH_OVERLAP_20261008.md): uniform primitive-kernel estimate and the enlarged controlled sector.
5. [Replication limits](../short_families/notes/5_SHORT_FAMILY_REPLICATION_LIMITS_20261008.md): composite rows, weights, and inherited lower-order families.
6. [Sextic sieve barrier](../short_families/notes/6_SHORT_FAMILY_SEXTIC_SIEVE_BARRIER_20261008.md): imported generic sixth-order sieve and its extraction floor.
7. [Latest continuation](../short_families/notes/7_SHORT_FAMILY_CONTINUATION_20261008.md): current results, remaining region, and next analytic targets.

## Mixed character families

Conditional conductor cutoffs and selected inverse-mass bounds remove more
sectors while preserving selectors and masks. Frame transposition and bounded
primitive-character fibers control repeated-character terms; the signed cycle
over three inequivalent primitive characters, or a weaker fixed-vector
estimate, remains unproved.

1. [Mixed conductor refinement](../mixed_character_families/notes/1_MIXED_CONDUCTOR_REFINEMENT_20261008.md): buffered cutoff certificates and another removable plain-conductor sector.
2. [Selected inverse distribution](../mixed_character_families/notes/2_SELECTED_INVERSE_DISTRIBUTION_20261008.md): frame transposition, primitive-character fibers, and the remaining cyclic estimate.

## Integer quadratic lift

Odd square rows replicate the complete integer prime response with a
logarithmic deletion error. The resulting small-conductor moment remains
open and would improve the whole odd primitive quadratic family; its exact
absolute majorant and the classical large sieve do not give the required gain.

1. [Integer quadratic response lift](../integer_quadratic_lift/notes/1_INTEGER_QUADRATIC_RESPONSE_LIFT_20261008.md): exact replication, primitive grouping, and conductor localization.
2. [Moment strength and barrier](../integer_quadratic_lift/notes/2_QUADRATIC_MOMENT_STRENGTH_AND_BARRIER_20261008.md): stronger family consequences and the actual prime-pair absolute-majorant obstruction.

## Newman collisions

A positive transition time reduces to a finite real multiple-zero collision.
Theta identities and normalized derivative errors give compact conditional
criteria and explicit high-height exclusion at any fixed positive time floor.
Certified middle-height coverage and control as that floor tends to zero are
still missing; positivity and fixed finite theta cutoffs do not settle them.

1. [Newman flow and collision scout](../newman_collisions/notes/1_NEWMAN_FLOW_AND_COLLISION_SCOUT_20261008.md): collision reduction and limitations of general kernel properties.
2. [Zeta collision arithmetic](../newman_collisions/notes/2_ZETA_COLLISION_ARITHMETIC_20261008.md): theta identities, the finite-cutoff obstruction, and conditional compact certificates.
3. [Normalized heat collision criterion](../newman_collisions/notes/3_NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md): full-disk and derivative errors and explicit high-height real-collision exclusion.

## Shared program records

- [Broad continuation plan](CODEX_CONTINUATION_20261008.md): routes across the investigations and related papers.
- [Dependency ledger](RESEARCH_LEDGER_20261008.md): inherited inputs, conditional deductions, imported theorems, and unresolved estimates.
- [Second continuation results](SECOND_CONTINUATION_RESULTS_20261008.md): earlier extraction, conductor, lift, and theta-truncation results.
- [Third continuation results](THIRD_CONTINUATION_RESULTS_20261008.md): signed remainders and effective collision control across the four continuation lanes.

Add new investigation notes to the relevant project's `notes/` folder.
Keep shared coordination records here, reproducible calculations and small
records in [`numerics/`](../numerics/README.md), scoped reviews in
[`reviews/`](../reviews/), and milestones in
[DRAFT_HISTOR.md](../DRAFT_HISTOR.md).
