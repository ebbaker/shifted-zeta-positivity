# Integrable matrix lifts of the Newman heat flow

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning
effort are not exposed and are not inferred. Reviews are internal LLM checks.

This is program 14 of [Heat Note 14](../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md),
instantiated directly beside the existing Gaussian project.

The initial result is an exact finite matrix dictionary with the Newman
time sign, an explicit matrix collision at an arbitrary positive threshold,
and a joint time/spatial Taylor-remainder bound for a genuine theta-moment
polynomial. The rank-one Calogero–Moser commutator is shared by the collision
control; it is not an additional arithmetic exclusion condition.

| Obligation | Initial realization |
| --- | --- |
| Enlarged state | Polynomial coefficients, or an affine matrix pencil for a squarefree reference polynomial |
| Generator | Nilpotent `-D_z^2` on finite polynomial space; the pencil uses rescaled Newman time |
| Reduction | Characteristic polynomial, multiplied by its original leading coefficient |
| Arithmetic preparation | Initial Taylor coefficients from the full positive theta moments |
| Domain | Finite polynomial space; genuine approximation on a specified compact time/spatial set |
| Collision implication | Still needs a theta-specific invariant beyond the universal rank-one condition |

Read [Note 1](notes/1_MATRIX_HEAT_LIFT_AND_COMPACT_THETA_REMAINDER_20261010.md),
[the internal review](reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md), and
[numerics](numerics/README.md). No genuine collision exclusion is proved.
Follow [LARGE_FILES.md](../../../../LARGE_FILES.md).
