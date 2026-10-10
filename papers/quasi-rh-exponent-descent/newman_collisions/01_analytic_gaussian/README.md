# Gaussian analytic lift and joint collision observations

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex). Reasoning effort: ultra, verified from this
chat's recorded configuration. Parallel LLM checks are internal checks,
not independent mathematical review.

This investigation implements the first direction in
[Heat Note 14](../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
The question is whether the imaginary Gaussian representation of the genuine
Riemann heat function supplies an additional constraint on simultaneous
vanishing of its value and spatial derivative. The folder is directly within
`newman_collisions/`, as requested for this investigation.

The initial result is a precise obstruction to a lower bound obtained only
from Gaussian positivity or bulk norm: the joint observation sees Hermite
degrees zero and one, and its kernel contains nonzero analytic states with
positive bulk energy. An explicit positive smooth spectral kernel also
admits a positive-time double zero. These controls do not settle a possible
additional relation specific to the actual theta state.

| Item | Exact realization |
| --- | --- |
| Initial arithmetic field | `H_0(x+iy)`, with `H_0(z)=xi(1/2+iz/2)/8` and the full theta kernel |
| Moving reduction | Gaussian average `P_t`, of variance `2t`, of the fixed initial field |
| Moving reduction equation | `(partial_t P_t)f = -partial_x^2 P_t f` on the stated analytic class |
| Evolving field | `U(t,x,y)=H_t(x+iy)` |
| Generator and constraint | `partial_y^2`, with `U_y=i U_x` |
| Fixed reduction | Trace `U(t,x,0)` |
| Domain | Entire fields of sub-Gaussian growth on vertical lines; the theta field belongs to this class |
| Intended collision implication | A new restriction specific to theta on `P_t f` and `P_t(yf)`, or on their higher Hermite observations |

[Note 1](notes/1_GAUSSIAN_REDUCTION_JOINT_KERNEL_AND_POSITIVITY_OBSTRUCTION_20261010.md)
derives the two reductions, pays Gaussian truncation and normalization on a
closed rectangle, and proves a fixed Gaussian cutoff of radius 9 has error
below `exp(-84)` through the sixth normalized spatial derivative. It retains
the existing fixed-cutoff error and proves the observation obstruction.
[The internal review](reviews/1_GAUSSIAN_SCOUT_INTERNAL_REVIEW_20261010.md)
records its checks and scope.

The first scout reaches exact representation and a scoped obstruction. It
does not establish a new theta-specific signed inequality, collision
exclusion, or RH conclusion. A continuation should choose an explicit
arithmetic restriction on the remaining Hermite components before adding
numerical work.

Save derivations in `notes/`, numerical programs and small records in
[numerics/](numerics/README.md), and scoped checks in `reviews/`.
Follow [LARGE_FILES.md](../../../../LARGE_FILES.md). The stable manuscript
remains [newman_collision_reductions.tex](../newman_collision_reductions.tex);
milestone history belongs in [DRAFT_HISTOR.md](../../DRAFT_HISTOR.md).
