# Exact theta identities and arithmetic bookkeeping

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## Summary

Correct, reusable, and sign-free: each identity below is exact and each is
shared by at least one collision control, so none is a lever by itself.

- **Covariant theta-source formula.**
  \(\Phi=\frac{y^{1/4}}{16\pi^2}(y^2\mathcal D^4\vartheta-3\pi^2\vartheta)(0,iy)\),
  which is the classical \(\Phi=(\partial_u^2-1)P/16\) written through the
  Hermite-weighted theta jets \(\mathcal D^k\vartheta(0,iq)\); their
  \(q\mapsto1/q\) law reproduces \(\Phi(-u)=\Phi(u)\). With it: the Hermitian
  metric \(h=e^{-2\pi(\operatorname{Im}z)^2/q}\), curvature
  \(-2\pi i\,dr\wedge ds\), the semi-flat hyperkähler metric and the
  base-rescaled ASD Chern connection, flat on the physical path.
- **Multiplicative dilations and sieve algebra (22 §12).**
  \(D_d\Phi=\sum_{d\mid n}\phi_n\) (dilation multiplies the square index,
  \(\phi_n(u+a)=p^{1/2}\phi_{np}(u)\)); exact sieve and Möbius identities with
  their lower-interval corrections; the uniform moment tail; and the
  divergence of the separated Möbius and Poisson series at every positive
  heat time, so "neither dropping the lower intervals nor moving the
  inversion to the whole real source line supplies the missing signed
  estimate". The heat-deformed dilation law
  \(H_{D_d\Phi}(t,x)=d^{-1/2}e^{ta^2-iax}H_\Phi(t,x+2ita)\) places the
  arithmetic at height \(\operatorname{Im}x=t\log d\) (Reply 18 §4; 19's
  exact flow theorem).
- **Two-coset reduction and the Hecke correspondence (09, 18, 06).**
  \(F_0=A\otimes A+B\otimes B\), \(F_1=A\otimes B+B\otimes A\) for both
  kernels with a tail ledger; the identity is the Hecke correspondence at
  2; the physical insertion annihilates the Eisenstein constant term so
  \(\mathcal L_0,\mathcal L_1\) are folded moments of a cusp kernel; and the
  folded same-parity responses are negative
  (\(C_0=-4c^2x^{-6}+\dots\)), so the cosets cannot be treated as separately
  positive channels.
- **Volterra recovery and positive correction (02).**
  \(R'+5R=-4\pi e^{-4u}\Phi\) with a stable inverse;
  \(P_t(x)>1/[3000(1+x^2)]\) for \(0\le t\le1\); and
  \((H^2+H'^2)/P^2\) decays faster than every power, so no polynomial
  relative margin exists.
- **Finite-time path theorem (20).** With \(r=u'+Au\) and
  \(d=\int_t^Tr-u(T)\), exact energy and norm identities for approximate
  imaginary-time paths; dropping the endpoint \(-u(T)\) is wrong; a certified
  Hubbard upper energy \(-0.50215\ldots<-\tfrac12\).
- **Recurrence core, absorption current, polynomial-source obstruction,
  recurrence boundary cokernel, signed observation quotient
  \(C_{\rm sign}=(a\cdot b+\|a\|\|b\|)/2\)** (22 §§9.3–11): exact, with
  replays.

## Status

Proved, with standard-library or python-flint replays whose receipts
describe polynomial germs and rational surrogates; reviewed internally and
hand-checked in the cross-model review.

## Caveats

"An exact identity that every control also satisfies is a rewriting, not a
constraint." Reindexing a sum does not change its value; the value of these
identities is bookkeeping (fewer integrals, exact tails) and the correct
form for future numerics.

## Reusable for

The source-side algebra of any arithmetic estimate on the heat flow; the
cusp-kernel representation; the Volterra anchor; the path corrections for
variational heat trajectories.

## Where

- Covariant jets and bundle: [22 manuscript §8](../papers/investigations-2/active/22_theta_manifold_geometry/manuscript/theta_manifold_geometry.tex); [theta jet bundle note (21)](../papers/investigations-2/active/21_quaternion_theta_geometry/notes/05_theta_correlation_kernels/62_THETA_JET_BUNDLE_AND_SEMIFLAT_HYPERKAHLER_GEOMETRY_20261015.md).
- Dilations: [multiplicative dilation and heat packets](../papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/11_MULTIPLICATIVE_DILATION_AND_COMPLETE_HEAT_PACKETS_20261015.md); [nonlocal multipliers audit](../papers/investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/12_NONLOCAL_ARITHMETIC_MULTIPLIERS_AND_BOUNDARY_OBSTRUCTIONS_20261015.md); [checker](../papers/investigations-2/active/22_theta_manifold_geometry/numerics/check_arithmetic_dilation.py).
- Cosets and Hecke: [09 reduction](../papers/investigations-2/inactive/09_rank_two_theta_addition/notes/1_COMPLETE_TWO_COSET_REDUCTION_20261013.md); [18 cusp formula](../papers/investigations-2/active/18_rank_two_automorphic_lift/notes/1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md); [06 obstruction](../papers/investigations-2/active/06_paired_kernel_factorization/notes/1_FOLDED_PARITY_CUSP_AND_FACTORISATION_OBSTRUCTION_20261013.md); [09-to-06 review](../papers/investigations-2/brainstorm/reviews/RANK_TWO_TO_PAIRED_KERNEL_REVIEW_CODEX_20261013.md).
- Volterra: [02 note](../papers/investigations-2/active/02_angular_jacobi_gluing/notes/2_VOLTERRA_RECOVERY_POSITIVE_ANCHOR_AND_TRANSFER_GAP_20261013.md).
- Path theorem: [20 note](../papers/investigations-2/active/20_constrained_operator_squares/notes/RESIDUAL_CORRECTED_HEAT_TRAJECTORY_IDENTITIES_20261014.md); [20 review](../papers/investigations-2/active/20_constrained_operator_squares/reviews/BOUNDED_PROGRAM_AND_DIRAC_CONTINUATION_REVIEW_20261014.md).
- The quoted rule: [19 initial program](../papers/investigations-2/active/19_euler_factor_controls/notes/INITIAL_RESEARCH_PROGRAM_20261013.md).
