# Investigation summary and notes index

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

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

Start with the [latest signed fourth reduction](../mixed_character_families/notes/14_SIGNED_HIGH_GCD_REDUCTION_20261009.md),
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

The [standalone manuscript](../short_families/short_family_reductions.tex)
organizes the useful results below, with proofs and explicit imported inputs.
The [manuscript review](../reviews/SHORT_FAMILY_MANUSCRIPT_REVIEW_20261008.md)
maps its initial coverage to notes 1–13. The
[cancellation addition review](../reviews/SHORT_FAMILY_CANCELLATION_MANUSCRIPT_REVIEW_20261008.md)
records the incorporation of note 15 with complete proofs and successful
native compilation. The
[squarefree addition review](../reviews/SHORT_FAMILY_SQUAREFREE_AND_COFACTOR_REVIEW_20261008.md)
records the new whole-nonsquarefree bound and its manuscript incorporation.
The full arithmetic moment remains open.

Finite reuse of one hypothetical short-family moment removes the prime-mask
error. Diagonal subtraction, second Poisson summation, and overlap bounds
reduce the residual region, but the low-overlap signed core remains open.
The prime-selected obstruction and generic sieve and replication limits
constrain which estimates could close that gap. Exact Möbius factorization
removes a centered small-product sector. Zero-integral profiles now
remove the principal correction exactly while preserving Mellin detection;
a radical-dependent row cutoff makes the actual small sector negligible.
A growing family with a small nonunit cofactor now cancels exactly within
each total product, with negligible full weighted energy. The surviving
semiprime sector requires cancellation across total products for every
fixed nonzero profile. The ideal mixed-discrepancy bridge retains the
density and both low/high edges for this unresolved estimate.
The whole nonsquarefree total-product sector is now affordable at
\(H=D^{2/5}\) with cutoff \(\theta=11/20\), leaving a squarefree
signed residual. This is a component bound, not an improved full moment.
At the same cutoff, complete small-prime cofactors now cancel odd rough
cores, giving a growing three-prime signed zero sector on a specified
large-conductor range. Even rough cores and coherent low-conductor triples
remain. The masked squarefree discrepancy identity retains all edges and
the enlarged deletion modulus; the full moment remains open. The
[rough-parity audit](../reviews/SHORT_FAMILY_ROUGH_PARITY_REVIEW_20261008.md)
records these proofs and their validation limits.

1. [Descent refinement](../short_families/notes/1_SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md): conditional extraction and finite reuse of a fixed moment.
2. [Small-cofactor reduction](../short_families/notes/2_SHORT_FAMILY_SMALL_COFACTOR_20261008.md): diagonal subtraction and second-Poisson decay.
3. [Core involution](../short_families/notes/3_SHORT_FAMILY_CORE_INVOLUTION_20261008.md): corrected conjugations, exact involution, and the prime-column obstruction.
4. [High-overlap bound](../short_families/notes/4_SHORT_FAMILY_HIGH_OVERLAP_20261008.md): uniform primitive-kernel estimate and the enlarged controlled sector.
5. [Replication limits](../short_families/notes/5_SHORT_FAMILY_REPLICATION_LIMITS_20261008.md): composite rows, weights, and inherited lower-order families.
6. [Sextic sieve barrier](../short_families/notes/6_SHORT_FAMILY_SEXTIC_SIEVE_BARRIER_20261008.md): imported generic sixth-order sieve and its extraction floor.
7. [Overlap and sieve continuation](../short_families/notes/7_SHORT_FAMILY_CONTINUATION_20261008.md): overlap results, remaining transformed region, and analytic targets.
8. [Centered factorization](../short_families/notes/8_SHORT_FAMILY_CENTERED_FACTORIZATION_20261008.md): exact Möbius convolution and a negligible centered small-product sector, with the principal main term retained.
9. [Signed gcd recombination](../short_families/notes/9_SHORT_FAMILY_SIGNED_GCD_RECOMBINATION_20261008.md): exact original-core identity, truncated diagonal and the correct original gcd cutoff.
10. [Factorization continuation](../short_families/notes/10_SHORT_FAMILY_FACTORIZATION_CONTINUATION_20261008.md): recombined convolution target and quantitative coherent-core cutoff limits.
11. [Zero-integral adaptive reduction](../short_families/notes/11_SHORT_FAMILY_MEAN_ZERO_ADAPTIVE_REDUCTION_20261008.md): sufficient detector profiles, sharp moment recovery and a negligible radical-dependent small sector.
12. [Factor selection barrier](../short_families/notes/12_SHORT_FAMILY_FACTOR_SELECTION_BARRIER_20261008.md): an actual prime-by-prime tail piece and the generic grouped sieve retain the coherent power barrier.
13. [Adaptive continuation](../short_families/notes/13_SHORT_FAMILY_ADAPTIVE_CONTINUATION_20261008.md): the correction-free adaptive tail target, shorter coherent free factor and remaining signed estimate.

14. [Ideal mixed discrepancy](../short_families/notes/14_SHORT_FAMILY_IDEAL_MIXED_DISCREPANCY_20261008.md): exact logarithmic bridge, principal density, Stieltjes endpoints and capped Riesz edges.
15. [Signed packet milestone](../short_families/notes/15_SHORT_FAMILY_DIVISOR_PACKET_CANCELLATION_20261008.md): exact divisor cancellation, a growing negligible full-weight sector, and two oversized compensating branches.
16. [Product barrier](../short_families/notes/16_SHORT_FAMILY_PRODUCT_BARRIER_20261008.md): the obstruction survives complete productwise recombination and every fixed nonzero profile; pure prime powers are affordable.
17. [Squarefree tail reduction](../short_families/notes/17_SHORT_FAMILY_SQUAREFREE_TAIL_REDUCTION_20261008.md): the entire nonsquarefree sector has bound \(D^{19/24+\varepsilon}\) at the proposed test point; the squarefree moment remains open.
18. [Cofactor compensation](../short_families/notes/18_SHORT_FAMILY_COFACTOR_COMPENSATION_20261008.md): an actual selected-factor block is negligible by complete cofactor inversion and free completion; its range has constant relative width.
19. [Opposing edge compensation](../short_families/notes/19_SHORT_FAMILY_EDGE_COMPENSATION_20261008.md): exact low/high cancellation and a positive packet integral, with selected-edge barriers and the unit exception retained.
20. [Squarefree-reduction continuation](../short_families/notes/20_SHORT_FAMILY_SESSION_CONTINUATION_20261008.md): preceding proof status, exact squarefree target, cutoff safeguards and research tasks.
21. [Rough-core parity](../short_families/notes/21_SHORT_FAMILY_ROUGH_PARITY_20261008.md): complete small-prime cofactors, a growing signed zero sector at large conductor, and the retained generic budget.
22. [Squarefree discrepancy](../short_families/notes/22_SHORT_FAMILY_SQUAREFREE_DISCREPANCY_20261008.md): complete masked convolution, both edges, low/low, density, prime powers, endpoints and added modulus cost.
23. [Parity continuation](../short_families/notes/23_SHORT_FAMILY_PARITY_CONTINUATION_20261008.md): the signed sector, surviving nonzero response, validation scope and cofactor test.
24. [Complete-cofactor obstruction](../short_families/notes/24_SHORT_FAMILY_FINITE_COFACTOR_PAIRING_20261008.md): for the permitted trivial twist, a genuine semiprime/odd-product pairing retains coherent power 16/15 uniformly for growing cofactor norm below D^(1/20); no full-tail lower bound follows.
25. [Pairing remainder](../short_families/notes/25_SHORT_FAMILY_PAIRING_REMAINDER_20261008.md): exact finite-prime resummation, negligible auxiliary free response with both norm costs paid, and an unbounded signed arithmetic complement.
26. [Cofactor continuation](../short_families/notes/26_SHORT_FAMILY_COFACTOR_CONTINUATION_20261008.md): completed cofactor test, mixed actual-probe reassessment, reproducible checks and the distinct-character open-chain task.

The [signed packet review](../reviews/SHORT_FAMILY_SIGNED_PACKET_REVIEW_20261008.md)
records the proof audits and finite checks. The full tail moment remains open.

## Mixed character families

Conditional conductor cutoffs and selected inverse-mass bounds remove more
sectors while preserving selectors and masks. Frame transposition and bounded
primitive-character fibers control repeated-character terms; the signed cycle
over three inequivalent primitive characters, or a weaker fixed-vector
estimate, remains unproved.

1. [Mixed conductor refinement](../mixed_character_families/notes/1_MIXED_CONDUCTOR_REFINEMENT_20261008.md): buffered cutoff certificates and another removable plain-conductor sector.
2. [Selected inverse distribution](../mixed_character_families/notes/2_SELECTED_INVERSE_DISTRIBUTION_20261008.md): frame transposition, primitive-character fibers, and the remaining cyclic estimate.
3. [Actual-probe cubic target](../mixed_character_families/notes/3_ACTUAL_PROBE_CUBIC_TARGET_20261008.md): a strictly weaker sufficient cubic criterion for the actual plain vector; conditional buffered endpoint input controls repeated characters, leaving a distinct-character open chain.
4. [Conductor-neighbor sectors](../mixed_character_families/notes/4_CONDUCTOR_NEIGHBOR_SECTORS_20261008.md): physical conductor-neighbor and coupled middle-row counts, hybrid masked Poisson kernels, and six controlled nonprincipal sectors with the exact remainder retained.
5. [Neighbor continuation](../mixed_character_families/notes/5_MIXED_NEIGHBOR_CONTINUATION_20261008.md): six controlled sectors, sharp raw-count example and the entrywise-method deficit.
6. [Weighted middle sieve and direct energy](../mixed_character_families/notes/6_WEIGHTED_MIDDLE_SIEVE_AND_DIRECT_ENERGY_20261009.md): seventh sector from the imported physical operator, the exact exterior-factor complement, and the optimized direct marginal budget with new correlation targets.
7. [Valuation factors and inverse-ratio fourth](../mixed_character_families/notes/7_VALUATION_FACTOR_SECTORS_AND_INVERSE_RATIO_FOURTH_20261009.md): eighth sector using grouped power-free exterior roots, control of the previous higher-valuation example, a surviving raw geometry, and an exact small-inverse-ratio removal for the direct fourth moment.
8. [Joint middle component conductors](../mixed_character_families/notes/8_JOINT_MIDDLE_COMPONENT_CONDUCTORS_20261009.md): coupled exterior-radical and quadratic/cubic column-conductor cut, exact expanded remainder, joint cubic operator scope and the retained sextic correlation.
9. [Operational fourth budget](../mixed_character_families/notes/9_OPERATIONAL_FOURTH_BUDGET_20261009.md): exact whole-slot optimization, continuous operational extrema, a sufficient uniform fourth saving 1/540, and the distinct tighter witness budget.
10. [Mobius ratio cores](../mixed_character_families/notes/10_MOBIUS_RATIO_CORE_FOURTH_20261009.md): exact squarefree gcd/core decomposition with all masks, annular balance, sharp absolute squarefree pair-count exponent, and the direct signed correlation.
11. [Parity-core joint correlation](../mixed_character_families/notes/11_PARITY_CORE_JOINT_CORRELATION_20261009.md): legal bounded-coefficient cubic power extraction, exact filtered cross-core identity, and a quantified failure of positive core recombination.
12. [Boundary reuse and input scope](../mixed_character_families/notes/12_BOUNDARY_REUSE_AND_INPUT_SCOPE_20261009.md): exact detector feedback obligations, present low/moment/contour ceilings, and conditional native comparison with the remaining dictionary stated.
13. [Fourth correlation continuation](../mixed_character_families/notes/13_MIXED_FOURTH_CONTINUATION_20261009.md): completed bounded tasks, uniform sufficient theorem, scoped evidence and the next signed ratio-core estimate.
14. [Signed high gcd reduction](../mixed_character_families/notes/14_SIGNED_HIGH_GCD_REDUCTION_20261009.md): shortened inverse deletion convolution and signed coprimality inversion control a new gcd sector; the near-coprime, near-maximal ratio correlation remains open.
15. [Finite prime completion](../mixed_character_families/notes/15_FINITE_PRIME_COMPLETION_20261009.md): complete prime states, controlled original ratio shell and a compatible completion with an affordable gcd boundary; isolated Euler factors supply no fixed power saving.

The [cofactor and mixed-probe review](../reviews/SHORT_FAMILY_COFACTOR_PAIRING_REVIEW_20261008.md)
records the scoped proof audits and finite checks. The remaining open-chain
bound has not been obtained.

The [conductor-neighbor review](../reviews/MIXED_CONDUCTOR_NEIGHBOR_REVIEW_20261008.md)
audits the new sector proofs, the native Poisson dependency and the retained
all-large-conductor obligation. Its finite checks do not validate an
unbounded mixed moment or the imported analytic inputs.

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
