# Arithmetic covariance targets

[Investigation index](../../README.md)

12 October 2026. Prepared for Edward Baker. Model: GPT-6 Astra
(`gpt-6-astra`). Reasoning effort: ultra. Prepared with substantial LLM
assistance. Internal model reviews are not independent mathematical
validation or formal verification.

## Objective and current status

Identify one feasible signed arithmetic covariance estimate and an
independent source of cancellation that could improve it. Start by
consolidating the exact moment obligations for one short sextic family and
one integer quadratic lift. A universal moment formula that suppresses the
family size, coefficient energy, or diagonal is not an acceptable target.

**Status: scoped; research not started in this project.** Much of the
necessary bookkeeping already exists. The quadratic notes identify the
diagonal, signed prime-pair form, an obstruction to entrywise absolute
estimation, and a separated-prime checkpoint. The sextic notes establish
finite extraction and coherent-row equivalence, together with later
compensation barriers. This project should reuse and reconcile those
results, rather than repeat their reductions under new names.

## First bounded task

Write a short ledger for each selected family using its actual definitions:

- Row set, nonnegative row weights, fixed character, coefficient profile,
  conductor and length parameters, and every deletion mask.
- Exact character kernel, diagonal, exceptional congruences, coherent-row
  mass, and the remaining signed covariance.
- Whether the proposed bound concerns a positive whole moment, a centered
  moment, or an off-diagonal remainder; retain all subtractions and paid
  comparison errors when moving between them.
- The precise exponent target, constants, quantifiers, and independently
  proved inputs.

Classify each target as impossible by an exact lower bound, equivalent on
the restricted coherent rows, stronger than that restricted estimate, or
supplied by an independent theorem. Equivalence alone does not invalidate
a sufficient estimate. Conversely, assuming its coherent-row conclusion
does not prove the full moment. Random models may expose weaknesses but
cannot replace identities specific to the Möbius coefficients.

Then select one surviving covariance and test one named analytic source
against its actual coefficients, supports, masks, and parameter regime.
Begin with the existing separated-prime quadratic checkpoint or the
documented sextic remainder; do not add another decomposition unless it
creates a sector that the chosen source genuinely controls.

## Deliverables and decision tests

Deliver two compact ledgers, an explicit list of already settled sectors,
and one theorem-to-target comparison. A small checker may verify declared
exponent and mask arithmetic. It should not claim to decide equivalence of
arbitrary mathematical hypotheses.

Continue only when the remaining target is above all necessary lower bounds
and a candidate input supplies information beyond the existing scalar or
large-sieve envelopes. A bounded negative result is useful if it explains a
specific mismatch. Stop a target contradicted by an exact lower bound, or a
proposed proof that assumes its conclusion. If no applicable source emerges,
close the consolidation milestone and leave the estimate explicitly open;
do not manufacture an expanding series of conditional reductions.

## Starting references

- [Corrected moment-ledger proposal](../../../quasi-rh/quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CODEX_20261011.md#3-d2-and-d5-replace-the-universal-target-with-an-exact-moment-ledger)
- [Quadratic strength and barrier](../../../quasi-rh/quasi-rh-exponent-descent/integer_quadratic_lift/notes/2_QUADRATIC_MOMENT_STRENGTH_AND_BARRIER_20261008.md)
- [Separated-prime checkpoint](../../../quasi-rh/quasi-rh-exponent-descent/integer_quadratic_lift/notes/3_SEPARATED_PRIME_PAIR_CHECKPOINT_20261009.md)
- [Sextic extraction](../../../quasi-rh/quasi-rh-exponent-descent/short_families/notes/1_SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md)
- [Full sextic response ledger](../../../quasi-rh/quasi-rh-exponent-descent/short_families/notes/29_DELETION_MODE_COVARIANCE_AND_FULL_RESPONSE_LEDGER_20261009.md)

## Working records

Use `notes/` for ledgers and derivations, `numerics/` for reproducible checks
and small records, `reviews/` for scoped assessments, and `chat-histories/`
for selected discussion records. Follow the [large-file policy](../../../../LARGE_FILES.md).
Keep any manuscript at a stable path with author and LLM acknowledgement;
do not create manuscript snapshots. At notable milestones, add a concise
`DRAFT_HISTORY.md` entry with the date, significance, commit or tag, and links
to the detailed notes and reviews.
