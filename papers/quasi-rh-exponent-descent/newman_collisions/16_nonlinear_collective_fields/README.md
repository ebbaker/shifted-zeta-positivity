# Nonlinear theta selection and collective moment fields

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Reviews are internal LLM checks.

Program 16 of [Heat Note 14](../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md)
is instantiated directly in `newman_collisions`.

The scout derives the complete normalized moment and spatial-jet hierarchies,
proves that no universal finite moment closure works on a neighborhood of
positive densities, and shows that an even density interaction invisible
to the full cosine observable must vanish. This restricts a particular
collective architecture; it leaves possible theta-specific constraints open.

| Obligation | Initial realization |
| --- | --- |
| State | Positive theta density rho_t and partition scalar Z_t |
| Generator | Nonlinear selection `(u^2-m_2)rho_t`; `Z_t'=m_2 Z_t` |
| Reduction | `H_t(x)=Z_t integral rho_t(u) cos(xu) du` |
| Arithmetic initial data | Full theta kernel divided by its integral |
| Domain | Densities with all required Gaussian/exponential moments; theta has them |
| Desired extra property | A signed theta-specific constraint surviving the full hierarchy |

Read [Note 1](notes/1_MOMENT_HIERARCHY_AND_INVISIBLE_INTERACTION_OBSTRUCTION_20261010.md),
[review](reviews/1_SCOUT_INTERNAL_REVIEW_20261010.md), and
[numerics](numerics/README.md). No collision exclusion is proved.
Follow [LARGE_FILES.md](../../../../LARGE_FILES.md).
