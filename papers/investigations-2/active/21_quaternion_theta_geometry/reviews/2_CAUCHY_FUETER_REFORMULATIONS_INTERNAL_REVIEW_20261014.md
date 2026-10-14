# Internal review of Fueter boundary reformulations

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

Scope: internal LLM derivation with two subagent cross-checks of
[Note 4](../notes/4_CAUCHY_FUETER_BOUNDARY_AND_CURRENT_REFORMULATIONS_20261014.md).
This is not independent specialist validation or formal verification.

## Classical source checks

[Frenkel and Libine, Theorem 9](https://arxiv.org/pdf/0711.2699)
fixes the Cauchy--Fueter kernel, constant, and order kernel--normal--field.
The use of half-normalized operators was separated from the boundary
kernel's normalization. Their harmonic Poisson formula was differentiated
to obtain the center moments. [Sudbery](https://dougsweetser.github.io/Q/Stuff/pdfs/Quaternionic-analysis.pdf)
supplies the harmonicity and operator conventions, and identifies the
failure of general product closure and isolated-zero behavior.
Perotti's [boundary characterization](https://arxiv.org/pdf/math/0612092)
was reviewed as a possible alternative, with its complex-coordinate
conversion left explicit rather than silently identifying N and T.

## Direct derivations checked

- Conjugate Fueter differentiation agrees with q_0 differentiation on
  regular fields; the full spatial jet hierarchy remains regular.
- External heat becomes \(\partial_tF=-\partial_q^2F\), and translation
  equivariance yields the single-field positive-j-half-plane criterion.
- Derivatives of boundary reproduction give the signed double-boundary
  forms, with conjugation reversing the correct factor order.
- Harmonic Poisson differentiation gives constants 4 and 6 in the first
  three sphere moments in real dimension four.
- The two stationary signs combine as \(\partial_t|F|^2\ge0\) on
  the physical union \(H_xH_{xx}=0\), with the analogous bounded loss.
- The imaginary harmonic current is divergence-free and has physical
  j component \(-\mathscr L_j\). Harmonic and logarithmic norm identities
  retain squares, not the needed oriented sign.
- The nonregular reciprocal example and the negative real Jacobian
  orientation were checked directly.
- The polynomial control reproduces the wrong first stationary sign,
  a nondegenerate quaternion zero, and the physical collision.

The [exact polynomial checker](../numerics/check_fueter_boundary_identities.py)
and [execution record](../numerics/FUETER_BOUNDARY_IDENTITY_CHECKS_20261014.json)
provide a separate reproducible algebra check of the lift and spherical
moments. They do not validate source-specific theta signs or all analytic
theorems.

## Remaining obligation

Boundary values include complex heat-time displacements; real-time theta
signs do not already control them. A useful continuation needs a complete
theta constraint on the signed boundary correlations or transverse
current, with locally bounded loss through candidate joint zeros and
predecessor coverage. No positivity, lower norm bound, or RH proof follows
from the reproduction formulas alone.
