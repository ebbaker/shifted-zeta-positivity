# Internal review of theta specific estimates

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

Scope: analytic derivations in [Note 5](../notes/5_COMPLETE_THETA_CENTRAL_ESTIMATE_20261014.md)
and [Note 6](../notes/6_IMAGINARY_GLUING_STABILITY_AND_HEIGHT_OBSTRUCTION_20261014.md),
with three subagent tasks and integrating-agent checks. This is internal
LLM validation, not independent specialist review or formal verification.

## Central source estimate

The complete theta series bound, first-summand core lower bound, and
uniform entire-tail envelope were checked analytically. The signed fourth
moment retains its negative tail with the correct inequality direction.
The constants in the exact rational remainder and its slope, curvature,
norm, and stationary consequences were checked separately.

The global sine lower bound makes the derivative estimate legitimate
despite the oscillatory source tail. The discarded interval in the scalar
bound is positive for the stated height range. The theorem proves
nonvanishing only for \(0\le t\le1,|x|\le8\), and covers the two
stationary sets only on \(|x|\le5\). It does not use or prove a full
imaginary-gluing sign estimate.

## Imaginary gluing defect estimate

The elliptic gauge and coefficient reindexing yield the exact Parseval
weights. The stated sequence class has bounded coefficients, ensuring
normal convergence on the angular lines. The physical observation is
explicitly a separate half-line cosine transform; its perturbed even
extension is not silently identified with a modular prepared-field
projection.

Summation by parts, the full-index moment majorant, and weighted
Cauchy--Schwarz give the four absolute derivative estimates. The closed
constant bounds, quadratic sign-error payments, and central robust norm
gap were checked with rational arithmetic. The defect is an infinite
angular observation at one theta scale, not a uniform error for all u.

The two-coefficient remote-control construction has an asymptotically
invertible value-slope matrix. Its determinant polynomial and positivity
at pi are checked exactly. Choosing an unbounded sequence with nonzero
genuine H makes the coefficient change and defect strictly nonzero.
The odd-jet determinant also verifies failure of smooth reflection.
Such controls break exact imaginary gluing and
modular smoothness, yet their defect norm tends to zero. They show the
scope limit of an all-height conclusion from a positive defect tolerance.

## Boundary and truncation scope

Full-source substitution into the Fueter boundary formula reproduces the
paired Laguerre integral exactly and removes the boundary radius. All
n,m cross terms remain. Separate fixed-index diagonal channels have
negative algebraic Laguerre tails; full odd-endpoint cancellations are
necessary at high height. Endpoint subtraction is a bounded certificate
improvement, not positivity of independent channels or a new heat family.

The [central checks](../numerics/THETA_CENTRAL_MOMENT_BOUND_20261014.json)
and [gluing checks](../numerics/THETA_GLUING_DEFECT_CHECKS_20261014.json)
verify their explicit constants and bind the checker sources by SHA-256.
They do not replace the analytic proofs or certify a global theta sign.

The remaining target is an actual signed off-diagonal estimate or locally
bounded loss on unknown-height predecessor neighborhoods. The current
results establish the declared bounded inequalities and identify why the
absolute boundary/gluing strategy cannot complete that target alone.
