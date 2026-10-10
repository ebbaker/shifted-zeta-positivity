# Radial Bessel geometry of the genuine theta state

10 October 2026. Model: GPT-6 (Codex); exact serving variant and configured reasoning effort unavailable and not inferred. Checks are internal, not independent mathematical review.

This folder implements program 12 in [Heat Note 14](../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md), beside the existing `01_analytic_gaussian` project.

The full genuine theta density has a smooth strictly positive three-dimensional radial inverse marginal for every 0<=t<=1/20, including the center. Its exact heat generator is multiplication by r squared minus a Volterra term. The correction fails positivity on the general cone. A separate nonnegative smooth compactly supported radial control has a prescribed positive-time double zero.

[Initial result](notes/1_POSITIVE_THREE_DIMENSIONAL_THETA_LIFT_AND_NONLOCAL_GENERATOR_20261010.md) gives the genuine state, reduction map, domains, backward-heat sign, derivative and normalizer dictionary, and the remaining obstruction. [Internal review](reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md) records scope and checks; [numerics](numerics/README.md) supplies a small reproducible replay.

[Continuation](notes/2_SINE_COLLISION_JETS_AND_HIGH_DIMENSION_THETA_OBSTRUCTIONS_20261010.md) gives the exact sine collision expression with mirror coefficient 27, an enclosed obstruction to positive Gaussian mixtures of the genuine density, and a uniformly negative central radial inverse in dimension 11. Hence no exact positive rotation-invariant realization exists in integer dimensions at least 11. [Continuation review](reviews/2_RADIAL_CONTINUATION_INTERNAL_REVIEW_20261010.md).

Next bounded task: Control the candidate-conditioned signed sine moments in dimension three with the Volterra and cutoff terms paid. Dimensions 5, 7 and 9 are separate unclassified geometry tests; positive Gaussian mixing and unlimited positive radial dimension are now excluded as mechanisms.

No collision exclusion or RH conclusion is claimed. Follow [LARGE_FILES.md](../../../../LARGE_FILES.md); the present source and small check record need no external archive.
