# Subpower milestones program

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal same-model research and checks, not independent specialist review.

This investigation develops the manuscript's second proposed path,
“Allow subpower losses and identify partial milestones.” Its organizing
goal is to prove successively smaller global exponents for the existing
prepared prime-response variance. A decreasing exponent would have a
precise consequence for zeta zeros. No mechanism for repeated exponent
improvement has yet been established, and the first fixed improvement
below the present exponent would itself be a major theorem.

## The quantity and its meaning

Keep the existing normalized prepared probe, with zero extensions,

\[
h(v)=(1-16v^2)^8\mathbf1_{|v|<1/4},\qquad
g=\frac{-h'''+h'/4}{\|-h'''+h'/4\|_2}.
\]

Retain its complete smoothing window and

\[
V_g(x)=\sum_{n\ge2}\Lambda(n)w(n/x),\qquad
w(t)=t^{-1/2}g(-\log t),\qquad
\mathcal V_g(X)=\int_X^{2X}|V_g(x)|^2dx.
\]

The target at exponent delta is a proof that

\[
\mathcal V_g(X)\le C_\delta X^{2+\delta}
\quad\text{for every sufficiently large real }X.
\]

For this fixed probe and each delta in [0,1], this is equivalent to the
global assertion that every nontrivial zero satisfies
\(\Re\rho\le1/2+\delta/2\). The converse as well as the implication is
proved in the [baseline note](01_baseline_and_exponent_budget_20261003.md).
Boundary zeros are permitted for positive delta. Illustrative exponents
below one are goals, not achieved bounds:

| Global delta | Consequence for zeros | Present status |
| --- | --- | --- |
| 1 | No nontrivial zero has real part above 1 | Established baseline |
| 0.99 | None has real part above 0.995 | Open illustration of a first improvement |
| 0.9 | None has real part above 0.95 | Open illustrative milestone |
| 0.5 | None has real part above 0.75 | Open illustrative milestone |
| Every positive delta | RH | Open ultimate goal |

The central signed projection from the first proposed investigation is
one possible method for proving these bounds. It is part of this exponent
program, rather than a separate goal that must be completed first.
Every technical calculation should state which exponent, saving, or
limitation it establishes.

## Initial results and next task

The [first note](01_baseline_and_exponent_budget_20261003.md) records the
fixed-exponent equivalence, an exact transfer from any unconditional
Chebyshev-error envelope, and a stronger unconditional baseline using
Johnston–Yang's Vinogradov–Korobov PNT estimate. That transfer improves
the decaying factor multiplying X cubed. It leaves the fixed global
exponent at delta=1.

The [first arithmetic investigation](02_short_interval_transfer_and_gate_20261003.md)
now proves a complete-cap transfer from short-interval prime mean squares:
Vcal_g(X) is bounded by a constant times X^2 S(X,h)/h^2+h^4/X.
At h=X^(3/4), the approximation is already O(X^2). A genuine relative
saving X^(-kappa) in S would deliver every delta>max(0,1-kappa).
The tested unconditional Saffari–Vaughan input gives only a subpower
saving on X cubed and retains delta=1. This gate exposes exactly what
must improve; changing interval ranges or logarithmic factors alone is
insufficient for this transfer.

There is also a [certified finite-range milestone](03_finite_range_variance_20261003.md):
Vcal_g(X)<38 X^2 for every real e<=X<=10^99, with further bounds
40 X^2 through 10^100 and 72 X^2 through 10^102. The constants are
checked by a small rational transfer of the existing outward records.
For fixed low-zero allowance, the certified range grows as H^10/(log H)^2
with a rigorously verified height H. These are finite results, not smaller
fixed global deltas.

The [structural non-bootstrap theorem](04_structural_nonbootstrap_20261003.md)
constructs models agreeing with any finite actual-prime prefix, retaining
PNT, the diagonal and current structural controls, yet having variance
of exact order X^(2+delta) for all sufficiently large real X. Those
properties cannot provide a universal exponent-descent rule. The result
does not concern the actual Euler-prime sequence.

The next global task is one actual-prime estimate with a genuine fixed
power saving after all caps and exceptional contributions. Use the new
short-interval gate to test an input, or retain the signed covariance
rather than taking its absolute mean-square norm. State the proposed
lemma and the exponent budget before a long calculation. Stop this
candidate route if it assumes an equivalent fixed zero strip or supplies
only a subpower saving. No repeated-improvement mechanism is established.

Keep useful results that improve constants, logarithmic or other subpower
factors, finite certified ranges, or the understanding of an obstruction.
Label their scope explicitly. Finite-range fitted slopes do not prove a
global exponent. Smaller constants and stronger smoothing alone do not
eliminate a hypothetical off-critical zero that the probe does not cancel.

## Records and related work

- [Milestone ledger](MILESTONES.md) records the statement, status, proof,
  and scope of each result.
- [Baseline and exponent budget](01_baseline_and_exponent_budget_20261003.md)
  supplies the initial proofs and the next candidate test.
- [Physical weighted-energy analysis](../selective-loss-program/07_weighted_energy_abscissa_20261003.md)
  identifies the convergence abscissa.
- [Actual central projection](../selective-loss-program/09_actual_error_projection_and_frequency_20261003.md)
  contains the technical reduction and complete caps.
- [Subpower transfer theorem](../selective-loss-program/10_subpower_growth_and_investigation_paths_20261003.md)
  supplies the all-exponent implication used in the manuscript.
- [Program review](../../reviews/SUBPOWER_MILESTONES_PROGRAM_REVIEW_20261003.md)
  records the internal mathematical and source checks.

Save subsequent derivations in this folder, numerical sources and small
records under the investigation's numerics folder, and reviews under its
reviews folder. Preserve existing research files and follow the repository's
large-files policy. The current manuscript remains the same editable file;
this folder establishes the research program without revising its source.
