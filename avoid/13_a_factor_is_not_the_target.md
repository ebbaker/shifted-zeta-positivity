# Realizing one factor, a boundary phase or a positive state space, and calling it the target

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

A physical or geometric construction reproduces one ingredient of the
complete form (the gamma kernel, a unit-modulus boundary multiplier, a
positive Hilbert space, a Ward identity) and the match is described as a
realization of the arithmetic target. The missing ingredient (the prime
comb, causality, an actual inequality) is exactly the RH-equivalent part.

## What it looks like here

A YM state space that reproduces a sentence true of \(\ell^2(\mathbb N)\)
with no group; the Robin Gaussian with the prime comb "outside"; an
all-pass boundary phase that follows from the functional equation; a
positive state space mistaken for a causal contraction; a symmetry of the
action mistaken for Osterwalder–Schrader reflection.

## Evidence

- [YM cross-model verification](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/YM/reviews/REVIEW_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md) §3.1: "the same sentence holds for the Haar measure on one copy of SU(2) … or for ℓ²(ℕ) with no group at all."
- [Wilson–Loewner free kernel](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/sections/03_free_kernel.tex): "The supplied factor \(\pi^\omega\), the prime comb, and the rational pole correction remain outside this Gaussian mechanism."
- [Brownian readout review](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/WZW/reviews/review_codex_brownian_readout_20260923.md): "The exact unit-modulus boundary multiplier follows from the functional equation without RH. Causality … is the missing RH-equivalent assertion."; the [fractional-dimension trap list](../papers/weil-positivity/susy-positivity/investigations/fractional-dimension/notes/NEW_SESSION_PROMPT.md): "CONTRACTION AT omega >= 1/2 IS NOT EVIDENCE."
- [Wilson-lines cross-model review](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/reviews/review_claude-fable-5-1_2026-09-17.md) §2.2: the step from boundary values to innerness was "false in the strip" and had to be repaired.
- [Lessons from WZW](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/notes/LESSONS_FROM_WZW_FOR_YM_AND_N4SYM_20260923.md): a positive state space is not a causal contraction; the [Codex review](../papers/weil-positivity/susy-positivity/investigations/wilson-lines/reviews/review_codex_2026-09-18.md) §3: "Positivity is an inequality; nonrenormalization needs an actual Ward identity or cohomological argument".
- The all-pass dichotomy itself ([result-summaries 05](../result-summaries/05_transfer_loewner_and_fractional_dimension.md)): the contraction margin "carries essentially no arithmetic information".

## What it cost

The YM manuscript was reframed as a negative-result record with errata;
the Brownian readout left causality open; the odd-\(H\) reflection was
disproved after a correction notice; the WZW branch was parked after its
four sibling results were found to cover it.

## Instead

Name the target first (the collar theorem's lesson: the transfer \(V\),
the form \(Q\) and the discrepancy \(D\) are different objects, [cross-program priorities](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/notes/CROSS_PROGRAM_PRIORITIES_AFTER_WZW_AND_N4SYM_REVIEWS_20260924.md) §3); list which of gamma, pole and prime terms the construction carries, as the top-level [README](../README.md) requires ("The gamma, pole, and prime terms must be retained together"); and apply the YM four-question filter ([structural requirements](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/YM/notes/STRUCTURAL_REQUIREMENTS_AND_NEXT_STEPS_20260925.md)) before writing a physical channel up.

**A changed integral needs a paid transfer, 22 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**. [RHE Note 08](../papers/investigations-4/09_reciprocal_hodge_energy/notes/08_DERIVATIVE_WEIGHTED_ENERGY_AND_GLOBAL_STRIP_BOUND_20261022.md) obtains useful derivative-weighted reciprocal disk/strip bounds, while stating: “A comparison that divides by |H_z|^2 to recover the original reciprocal energy restores exactly the dangerous critical-point payment.” Its positive mass and collision-stable cutoff error are valid independent outputs; an unproved numerator/denominator comparison would not make them the missing BW09 signed surplus or BW10 trace bound. The cubic cutoff was already present in I4/07 with a different potential. [Review 05](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/05_FINITE_PART_AND_WEIGHTED_INTEGRAL_REVIEW_20261022.md) checks those distinctions.

**The direction of a signed energy payment matters, 22 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**. [RHE Note 10](../papers/investigations-4/09_reciprocal_hodge_energy/notes/10_SIGNED_JET_FLUX_AND_PHASE_TRACE_OBSTACLES_20261022.md) writes the physical amplitude-weighted trace as T=P-M, with M>=0: “A complete upper on the bulk mass gives a *lower* bound on the signed trace.” A negative witness needs the other direction; its full half-domain trace also has logarithmic source sensitivity. [Note 11](../papers/investigations-4/09_reciprocal_hodge_energy/notes/11_WEIGHTED_TRACE_PAYMENT_AND_ENDPOINT_OBSTRUCTION_20261022.md) shows that a bounded or vanishing weighted area can coexist with the necessary eta^2/t tube payment. These are scoped transfer obstacles, not an exclusion of canonical-source estimates. [Review 06](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/06_DERIVATIVE_WEIGHTED_TRANSFER_REVIEW_20261022.md).

**A mass lower and a physical floor have different contracts, 22 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**. [RHE Note14](../papers/investigations-4/09_reciprocal_hodge_energy/notes/14_CANONICAL_BULK_MASS_LOWER_BOUND_20261022.md) certifies a positive lower for the bulk in T=P-M while warning: “This is not a pointwise lower for J or E in the target disk.” It improves an upper trace endpoint, without a signed potential value. [Note12](../papers/investigations-4/09_reciprocal_hodge_energy/notes/12_CANONICAL_ANCHORS_AND_ISOLATED_EVENT_FLOORS_20261022.md) derives physical floors only after explicit root isolation; [Note13](../papers/investigations-4/09_reciprocal_hodge_energy/notes/13_CRITICAL_AMPLITUDE_AND_PROPAGATED_LAGUERRE_FLOORS_20261022.md) propagates them under LP hypotheses. Keep these distinct inputs and their endpoint losses visible. Neither payment excludes the compatible quadratic or positive-source controls. [Review07](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/07_CANONICAL_AMPLITUDE_AND_BULK_LOWER_REVIEW_20261022.md) checks the scope and exact canonical replay.

**A completed finite sign can close the wrong window, 22 October 2026.** Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol, effort ultra**. [RHE Note15](../papers/investigations-4/09_reciprocal_hodge_energy/notes/15_SIGNED_CANONICAL_POTENTIAL_AND_COMPLETED_TRACE_20261022.md) pays the signed potential and stronger whole-cell bulk, but the complete trace is positive and direct Q is positive throughout the fixed window: “More precision on the same observable cannot turn its actual sign negative.” Its area-derived interval is valid; the direct interval is tighter. Stop only that specified negative-witness attempt, retain the finite estimate, and keep other regimes open. A mass interval inferred from P minus the direct trace is shared-data reuse, not independent trace improvement. [Review08](../papers/investigations-4/09_reciprocal_hodge_energy/reviews/08_SIGNED_POTENTIAL_AND_TRACE_REVIEW_20261022.md) checks these distinctions.


**An exact all-zero energy permits collisions, 22 October 2026.** For Edward Baker with substantial LLM assistance, **gpt-6-astra, ultra**. The [extensions note](../papers/investigations-4/notes/07_LOCALIZED_ROOT_COVER_ENERGY_AND_MANUSCRIPT_EXTENSIONS_20261022.md) states: “The localized energy permits every finite multiplicity; its exact count is not a collision exclusion.” The q-cover energy, conserved divisor, real birth current and complex event residue have distinct contracts. The [manuscript](../papers/investigations-4/manuscript/zero_count_heat_transport/README.md) identifies total boundary degrees while retaining separate formulas for individual physical faces. The identities are reusable analytic results; an exclusion needs additional signed information. [Internal review](../papers/investigations-4/reviews/01_ZERO_COUNT_HEAT_TRANSPORT_MANUSCRIPT_REVIEW_20261022.md).
