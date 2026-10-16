# Internal scout review: 09_prime_phase_torus

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are unavailable and are not inferred. Internal LLM checks are not
independent mathematical validation.

Scope: review of [Note 1](../notes/1_ACTUAL_ORBIT_JETS_AND_EXACT_FINITE_HEAT_RESIDUAL_20261010.md) and the associated
[exact checker](../numerics/check_prime_torus_scout.py). This review was performed by
the same LLM research scout. It is an internal audit and must not be
represented as independent validation or specialist mathematical review.

## Findings

The torus encoding retains all composite monomials, actual nonmultiplicative weights, carrier, and amplitude drift. Physical height has `Tprime=c`, and the coefficient derivative is `-d log n`; the first and second derivatives agree with the manuscript vector. The candidate implies vanishing of two projected quadratures, not two complex channels. Its curvature expression leaves signed second log moments unconstrained.

The finite branch is written as `exp(m_0-s log n+t(alpha-log n)^2/4)` before computing its heat residual. This uses `m_0prime=alpha` and retains `alpha'` and `alpha''`. After normalization, the residual enters as `R_G/A` in addition to the same drift and multiplication present in the genuine normalized heat equation. The spatial Cauchy error is not represented as a time-derivative error bound.

The relative block and core recombine exactly at one physical height; their cross correlation is potentially adverse. Haar norm positivity cannot control this pointwise cross term. The two paid candidate tolerances are correctly propagated to the curvature identity, including the residual `Omega^2 eta_N/2` from `C_0`. An actual signed relation, its quadratic payment, higher multiplicity, and coverage remain open. The known twisted zeros are not promoted to actual heat collisions.

## Reproducible checks and limitations

The retained checker run passed 510 exact assertions and a fresh
repeat reproduced its small record byte for byte. The record binds its
source SHA-256. Drift-containing orbit curvature, finite heat residual, complete block cross correlation, monomial factorization through 256, and raw jets through order four.

No huge-height heat evaluation, actual-phase sign estimate, time-remainder bound, or density-to-collision transfer is certified. An unrestricted torus bound remains ruled out by the prior complete twist construction.
The formal checks do not certify the imported analytic theorems, limiting
interchanges, uniform asymptotics, actual collision signs, or RH. Their
counts are not a measure of the depth or likelihood of the proposed route.
All files obey the source/small-record convention in `LARGE_FILES.md`.

## Milestones and disposition

| Milestone | Status |
| --- | --- |
| Exact representation | Established in the stated finite or full-kernel domain |
| Additional identity or scoped obstruction | Established as printed in Note 1 |
| Paid signed collision exclusion | Not established |
| Coverage sufficient for an endpoint conclusion | Not established |

Use the exact candidate curvature identity and higher Bell jets to test one signed relation on a closed kappa interval; combine theta Ward or global-character information only when it constrains actual moments.
No theorem beyond the stated scopes or literature-priority claim is approved
by this internal audit. Independent specialist and literature review remain
necessary before treating these results as independently validated.
