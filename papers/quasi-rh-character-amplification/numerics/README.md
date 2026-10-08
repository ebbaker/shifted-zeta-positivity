# Exact parameter and geometry checks

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and configured reasoning effort were
not exposed.

The certificate scripts use only the Python standard library and exact
rational arithmetic. Decimal values are explanatory conversions. Run each script
from this directory to print its small retained JSON record.

| Command | Record | Scope |
| --- | --- | --- |
| `python3 check_geometry_optimization.py` | [Current geometry record](geometry_optimization_check.json) | Exact scale identities, complete low subset inequality, continuous quadratic positivity certificate, all range margins, and a rational interval for the fixed-geometry endpoint limit. |
| `python3 check_parameter_extension.py` | [First extension record](parameter_extension_check.json) | Original source polynomial, ratio factorization, first displacement, Euler-region exponents, and conditional amplification examples. |
| `python3 check_localized_target.py` | [Conditional next-target record](localized_target_check.json) | Exact Bernstein certificate outside the hard box and inside it **assuming a new row gain**; geometry and remaining margins. |
| `python3 check_amplitude_profile.py` | [Profile reduction checks](amplitude_profile_check.json) | Rational retuning constants and two exact profile examples, including zero gain at full saturation. |
| `python3 check_joint_witness_payoff.py` | [Mixed-moment payoff checks](joint_witness_payoff_check.json) | Exact two-stage rebalancing, minimum gain factor, witness-band coverage, and loss allowance; the mixed moment itself is unproved. |
| `python3 check_mixed_kernel.py` | [Mixed-kernel algebra and margins](mixed_kernel_check.json) | Exact local valuation/mask checks, conductor-reduction margins, and formal transfer-width deficits; no cancellation estimate is proved by the finite checks. |
| `python3 check_selector_feasibility.py` | [Selector and divisor budgets](selector_feasibility_check.json) | Continuous principal-row budget extrema, mean-zero subcase margin, and exact live-label width and normalization identities; no main-mass or cancellation assertion. |
| `python3 check_selector_preserving.py` | [Two-conductor and subcase checks](selector_preserving_check.json) | Exact adaptive conductor thresholds and zero masks, positive interpolation identity, and upper plain-band selection-loss margin. |
| `python3 check_selector_energy.py` | [Energy and application-domain checks](selector_energy_check.json) | Exact count-sensitive strip, rebalance/taper identities, continuous monotonicity bounds, and buffered triangle constants. |

The current certificate proves positivity by comparing polynomial
coefficients and completing a square over the entire parameter rectangle.
It is not a grid search. The root interval for the endpoint limit uses
exact rational signs. Those two complete records are under 5 KB; these scripts generate no
large data.

The checks establish algebra and exponent feasibility. They do not prove
analytic continuation, reflection identities, detector construction,
external moments, or a Lean theorem. The applicability and limits of
those inputs are recorded in the [current derivation](../notes/GEOMETRY_OPTIMIZATION_20261008.md),
[low audit](../reviews/LOW_STRUCTURAL_AUDIT_20261008.md),
[moment audit](../reviews/MOMENT_STRUCTURAL_AUDIT_20261008.md), and
[contour audit](../reviews/CONTOUR_TRANSFER_AUDIT_20261008.md).

The [first derivation](../notes/PARAMETER_EXTENSION_20261008.md) and
[first review](../reviews/PARAMETER_EXTENSION_REVIEW_20261008.md) retain
the preceding calculation. No numerical prime-data sweep is represented
by these records.

## Exploratory bottleneck sensitivity

Run `python3 bottleneck_sensitivity.py` for the [diagnostic record](bottleneck_sensitivity.json).
This separate script uses floating arithmetic to evaluate witness lengths,
prime capacities, and local derivatives at the previously certified fixed
geometry limit. Its decimals are sensitivity guidance, not outward
enclosures, a new continuous certificate, or a new zero-free bound. See
the [research directions](../notes/RESEARCH_DIRECTIONS_20261008.md) for
the proposed estimates and their missing hypotheses.

## Localized next-target certificate

The proposed boundary `17499/20000` is **not established** by these checks.
It requires the additional restricted count or mixed estimate in the
[localized target](../notes/LOCALIZED_JOINT_WITNESS_TARGET_20261008.md).
The Bernstein calculation uses seven rational rectangles to cover the
continuous active domain; the hard rectangle is shifted by the assumed
count gain. The profile and mixed-payoff scripts check derived constants
and implications, not the external analytic theorems. See the
[scoped review](../reviews/LOCALIZED_TARGET_PROFILE_REVIEW_20261008.md).

## Mixed-kernel reduction

The [combined derivation](../notes/MIXED_MOMENT_REDUCTION_20261008.md)
proves the ideal-pair estimate and the source-dependent removal of lower
row conductors and the plain-variable diagonal. The checker enumerates
local valuations at two formal good primes, checks the retained zero masks,
and verifies the exact margins `23/1250`, `1/6250`, and `647/5000`.
These finite checks support the displayed identities; they neither estimate
actual exceptional character sums nor prove the remaining signed saving.
The [scoped review](../reviews/MIXED_REDUCTION_REVIEW_20261008.md) records
what was independently checked.

## Selector and live-divisor continuation

The [selector note](../notes/SELECTOR_FEASIBILITY_20261008.md) extracts
the exact sixth-power norm with the actual profiles. Its near-capacity
inverse-budget shortfall is at least `19/375-rho`, using the imported
seven-eighths bound; this is an upper-bound deficit, not a lower bound on
the norm. The mean-zero plain-profile subcase has margin `6791/15000`.
The [live-divisor note](../notes/LIVE_DIVISOR_TRANSFORM_20261008.md)
retains the first canonical width at most `-3/50` after label reindexing.
The new script checks these extrema using monotonicity and exact fractions,
and compares polynomial coefficients for the width and normalization
identities. It does not activate the conditional two-rebalance payoff.

The subsequent [plain-ratio reduction](../notes/SELECTOR_PRESERVING_PLAIN_CONDUCTOR_20261008.md)
uses the new thresholds `2*delta*m-9/12500` and
`2*delta*(m+23/20)-1/4-9/12500`. Their positive-norm and pair-count proofs
are in the note; the checker verifies algebra and local zero masks.
The [mixed subcase](../notes/SELECTOR_PRESERVING_SUBCASES_20261008.md)
has upper-band margin `59/100000` after the stated whole-slot loss.
The [energy note](../notes/SELECTOR_ENERGY_LOCALIZATION_20261008.md)
proves continuous derivative signs before evaluating corner extrema;
its application triangle has ideal width at most `1/900`. These records
do not estimate the remaining correlation within that triangle.
