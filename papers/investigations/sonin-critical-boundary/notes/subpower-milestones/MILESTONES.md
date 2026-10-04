# Subpower milestone ledger

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal same-model research record, not independent specialist review.

This ledger records established statements and open milestones for the
[subpower program](README.md). A proof of a global exponent reduction
has not yet been obtained.

| Date | Statement | Status and scope | Evidence |
| --- | --- | --- | --- |
| 2026-10-03 | Fixed delta variance bound iff every zero has real part at most 1/2+delta/2 | Established transfer for the fixed probe, delta in [0,1]; no new zero location information | [Baseline note](01_baseline_and_exponent_budget_20261003.md) |
| 2026-10-03 | Global variance O(X cubed) | Established baseline delta=1 | Existing effective PNT and [baseline transfer](01_baseline_and_exponent_budget_20261003.md) |
| 2026-10-03 | Stronger Vinogradov–Korobov decaying factor multiplying X cubed | Established application of Johnston–Yang; same global delta=1; explicit supremum retained, numerical constants not enclosed | [Baseline proof](01_baseline_and_exponent_budget_20261003.md) |
| 2026-10-03 | One fixed global delta below 1 | Open first power-saving milestone; no attained value recorded | [Candidate exponent budget](01_baseline_and_exponent_budget_20261003.md) |
| 2026-10-03 | Rule improving a proved delta to a smaller delta | Open for actual primes; retained generic structural hypotheses alone cannot imply such a rule | [Finite-prefix obstruction](04_structural_nonbootstrap_20261003.md) |
| 2026-10-03 | Complete-cap short-interval transfer Vcal_g(X) << X^2 S(X,h)/h^2+h^4/X | Established unconditional transfer; at h=X^(3/4), approximation cost is O(X^2); power-saving arithmetic input remains open | [Proof and exponent budget](02_short_interval_transfer_and_gate_20261003.md) |
| 2026-10-03 | Saffari–Vaughan input through the short-interval gate | Audited unconditional input, complete bands; gives only a subpower saving on X cubed, retaining delta=1; does not strengthen the existing PNT baseline | [Primary-source audit](02_short_interval_transfer_and_gate_20261003.md) |
| 2026-10-03 | Vcal_g(X)<38 X^2 on e<=X<=10^99; <40 X^2 through 10^100; <72 X^2 through 10^102 | Established finite continuous ranges using published verification through height 3e12 and existing outward records; no global delta reduction | [Finite-range proof](03_finite_range_variance_20261003.md), [rational record](../../numerics/subpower_finite_variance_20261003/record.json) |
| 2026-10-03 | Certified finite quadratic range scales as H^10/(log H)^2 | Established transfer for a family of verified heights with fixed low cutoff and variance ceiling; fixed H still leaves a cubic allowance globally | [Range law](03_finite_range_variance_20261003.md) |
| 2026-10-03 | Finite-prefix models with variance of exact order X^(2+delta), 0<delta<1 | Established generic obstruction for every sufficiently large real X; not an actual-prime counterexample | [Construction and phase bound](04_structural_nonbootstrap_20261003.md) |

For subsequent entries, record the exact inequality and quantifiers,
all-real-X range or finite range, delta and any extra factors, proof
source, hypotheses, constants and thresholds where established,
complete-cap and exceptional-set accounting, and review link.
Conditional estimates and finite diagnostics must be marked in their
status. Record both successes and precise limitations. Numerical fitted
exponents must never be entered as proved global deltas.
