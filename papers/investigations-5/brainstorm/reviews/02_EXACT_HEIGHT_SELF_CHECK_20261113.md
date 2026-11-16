# Exact height brainstorm self check

13 November 2026, America/New_York. Prepared for Edward Baker with
substantial OpenAI Codex LLM assistance. Actual backend model and effort
are unavailable in recorded configurations. **Same-assistant analytical
check, not an independent review or numerical certificate.**

The subject is [Brainstorm 02](../02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md).
The following checks were made while deriving its formulas.

1. **Normalization and clocks.** The probability measure is
   \(W_{1/2}du/Z_*\), so multiplication of its expectation by \(Z_*/2\)
   restores the original full-line Fourier transform. Reversing
   \(\tau=1/2-\lambda\) gives \(\partial_\lambda H=-H_{zz}\).
   Renormalizing the evolving state would require an additional factor.
2. **Hilbert space and domains.** This is a fixed weighted-space
   realization, with its corresponding Lebesgue wavefunction stated
   explicitly. Complete theta tails justify polynomial density and the
   prepared-vector exponential domains. The self-adjoint Jacobi operator
   is defined by unitary transport of multiplication, not by silently
   selecting an extension of a formal matrix.
3. **Chain locality.** Squaring the tridiagonal zero-diagonal matrix gives
   diagonal entries \(a_n^2+a_{n+1}^2\) and next-nearest entries
   \(a_{n+1}a_{n+2}\). Thus equation (6) has the stated sign and range.
   A finite height propagator need not be banded. Only the single-particle
   sector is identified with the displayed chain wavefunction.
   Each fixed component is a Fourier transform of an integrable density,
   while total norm is conserved in real height, so the finite-prefix
   mass-escape statement holds. It gives no propagation rate and excludes
   only uniform all-height approximation by a fixed prefix in this basis.
4. **MPS identity.** The two boundary vectors annihilate the all-zero
   configuration; nilpotence of \(E_{12}\) removes configurations with
   multiple excitations. The coefficient of one excitation is exactly
   \(v_n\). Convergence is in state norm from \(v\in\ell^2\), not an
   asserted operator-norm convergence or QTT rank bound.
5. **Coefficient deformation.** Monicity makes
   \(\partial_\lambda P_n\) lower degree. Orthogonality removes its norm
   derivative term and yields \(h_n'/h_n=\beta_{n+1}+\beta_n\).
   The resulting Volterra sign agrees with the quadratic specialization
   in Van Assche. The moving basis is separated from the fixed basis in
   equation (5).
6. **Infinite products.** Equation (9) has a summable geometric norm
   bound at bounded height. Equation (10) telescopes and uses a strictly
   positive compact minimum. Full-line recovery uses an absolutely
   convergent sum of interval readouts; no uniform lower floor over the
   full real line or height-uniform near-identity norm is assumed.
7. **Scoped obstructions.** Full real spectral support gives norm
   distance two for any nonzero height increment. The finite constant
   matrix exclusion follows only for autonomous finite-dimensional
   linear realizations. Neither argument excludes infinite, moving or
   scale-dependent networks.
8. **Actual collision control.** For the three-atom control,
   \(\beta_1=p\), \(\beta_2=1-p\) and \(\beta_3=0\) satisfy the Volterra
   equations. At \(\lambda=T\), the regular chain coexists with
   \(F(\pi)=F'(\pi)=0\), \(F''(\pi)=2\) and \(F_\lambda(\pi)=-2\).
   The remaining catalog screen names absent theta premises and does
   not assign controls unproved quantitative coefficient estimates.

Disposition: usable as an exploratory exact-representation discussion with
these qualifications. No theta-specific coefficient asymptotic, favorable
transfer inequality, finite computational advantage or zero exclusion has
been established. An exact bond-two single-excitation encoding is an
information-preserving identity, not a complexity gain.

The [reference record](../references/EXACT_HEIGHT_REFERENCES_20261113.md)
states inspected versions and passages. Four local reading-copy attempts
failed with host name-resolution errors; web passage inspection succeeded
for the three used papers. The fourth paper remains abstract-only.
No numerical computation or source certificate was run for this check.
