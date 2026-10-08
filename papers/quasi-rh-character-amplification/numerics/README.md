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
