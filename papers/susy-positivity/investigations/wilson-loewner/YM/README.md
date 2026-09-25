# YM: positive norms and controlled hierarchies for growing Wilson loops

24 September 2026. Prepared for Edward Baker with substantial GPT-6 (Codex) assistance. Reasoning effort: not exposed; not inferred.

This investigation continues the parent's physical question in fixed pure SU(N) Yang–Mills theory: derive and control the Wilson observable on an actual growing Loewner trace with a specified return chord. The goal is an approximation with a positive norm and an explicit error estimate. Finite closure and an arithmetic match are not assumed.

The latest session gives an exact finite-slab reflection-boundary realization and the first interacting four-dimensional SU(2) test. Boundary-only unitary loop multiplication preserves the reflected null space. However, the tested one-, two- and three-observable families leave large residuals; their error estimates do not justify an accurate truncation at this coarse coupling. Adding the curvature observable worsens a statistically resolved intermediate loop estimate.

- [Finite-slab reflection and discrete hierarchy](notes/FINITE_SLAB_REFLECTION_AND_DISCRETE_HIERARCHY_20260924.md): boundary state, reflected color contraction, null-space descent, exact finite contour steps, Schur residuals, and a new forward/backward output bound. It also identifies slice-only smoothing as compatible with this construction.
- [First interacting test and continuation](notes/FIRST_INTERACTING_SLAB_TEST_AND_CONTINUATION_20260924.md): four chains on a 6³-by-5 open-time Wilson lattice, uncertainty estimates, the negative small-family result, and a concrete next experiment using local plaquette sectors and the backward readout hierarchy.
- [Preliminary analysis](notes/YM_POSITIVE_HIERARCHY_PRELIMINARY_ANALYSIS_20260924.md): regulated continuous storage and memory, a norm-preserving moving family, two-observable residual, and the OS interior-multiplier counterexample. Its 64 controls use prescribed backgrounds.
- [Opening research plan](notes/YM_REFLECTION_AND_HIERARCHY_RESEARCH_PLAN_20260924.md): historical starting plan with a completion update; the latest test note now supplies the next bounded task.
- [Numerics and reproduction](numerics/README.md): the earlier controls, interacting sampler, independent projection checks, and small records.

The continuous Galerkin approximation preserves its norm; the new discrete orthogonal compression loses norm according to its measured residual. These are different approximations. The finite open slab prepares a specified state, not an established infinite-time vacuum. No continuum theorem, efficient finite closure, Lorentzian input/output channel or arithmetic identity has been obtained.

Background: [original YM hierarchy](../notes/GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md), [N4SYM closure audit](../N4SYM/notes/NEAR_BPS_CORNER_ROUNDING_AND_CLOSURE_20260924.md), and [updated cross-program assessment](../notes/UPDATED_PATH_ASSESSMENT_REFLECTION_AND_HIERARCHIES_20260924.md).
