# Lee–Yang spin realizations and theta moment screening

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Reviews are internal LLM checks.

This is program 15 of [Heat Note 14](../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
The initial result is a rigorous low-moment exclusion of two elementary
spin families: equal-weight independent Rademacher spins, and two
equal-weight ferromagnetically coupled spins. A ten-spin Curie–Weiss model
fits the second and fourth moments numerically but misses the sixth by
about 1.40 percent. That fit and sixth-moment mismatch are exploratory.

| Obligation | Initial realization |
| --- | --- |
| Genuine state | Even theta spin density, with unnormalized partition function Z_t(h) |
| Generator | `partial_t Z=partial_h^2 Z`; normalized growth-selection density |
| Reduction | `H_t(z)=Z_t(iz)/2` with the full even theta kernel |
| Finite comparison | Ten equal spins with positive pair coupling and one amplitude |
| Time evolution in comparison | Coupling changes by `2t a^2`; amplitude is fixed |
| Intended implication | Constructive spin realization with certified complex convergence; presently absent |

Read [Note 1](notes/1_THETA_MOMENT_ENCLOSURE_AND_FERROMAGNETIC_SPIN_SCREEN_20261010.md),
[review](reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md), and
[numerics](numerics/README.md). Positivity of the genuine density is not a
Lee–Yang certificate. No collision exclusion is proved.
Follow [LARGE_FILES.md](../../../../LARGE_FILES.md).
