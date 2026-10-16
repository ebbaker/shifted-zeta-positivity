# Fresh review of the exponent equivalence

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is a fresh internal same-model proof pass, not independent specialist
refereeing.

## Scope and finding

I reviewed Sections 1--3 of the actual new
[manuscript source](../manuscript.tex), through the remark on cumulative
energy, while the remaining sections were being drafted. The initial
350-line source inspected had SHA-256
`bda55d79f42088db8e16d5fd4b1be2248745429ee1e3b4a39f0ec6db9a52b18e`.
That identifies the initial review state, not the final whole manuscript.

**Mathematical pass:** I found no gap in the stated fixed-exponent
equivalence, its endpoints, the complete explicit formula, or the optimal
exponent assertion. The two initial unclosed `equation` environments at
`eq:probe` and `eq:response` were reported to the drafting agent. Whole-file
compilation and final bibliography verification belong to the main drafting
record, not this proof pass.

## Checks from the definitions

1. **Preparation and regularity.** The eighth-order endpoint zeros of
   \(h\) give \(g\in C_c^4\) with derivatives through order four zero
   at both endpoints. Three integrations by parts give
   \(G(z)=z(z^2-1/4)H(z)/\sqrt\nu\), with the plus-exponent convention
   used consistently. The substitution \(t=e^{-v}\) gives
   \(\int w=G(-1/2)=0\) and \(\int w^2=\int g^2=1\).
   The exact polynomial normalization and derivative constants were
   independently checked in the
   [certificate replay](CERTIFICATE_REPLAY_20261003.md).

2. **Elementary noncancellation.** The even-moment beta integrals yield
   \(H(z)/H(0)=\sum_{k\ge0}(z^2/64)^k/((19/2)_k k!)\).
   The coefficient recurrence is
   \((2k)(2k+17)c_k=c_{k-1}/16\), proving the stated radial equation
   \((t^{18}u')'=(z_0^2/16)t^{18}u\).
   The boundary term at zero vanishes because \(u,u'\) are bounded;
   that at one vanishes because \(u(1)=0\). Both energy integrals are
   strictly positive, since \(u(0)=1\) and \(u(1)=0\). Thus
   \(z_0^2\) is negative real, so every zero of \(H\) is nonzero and
   imaginary. The only additional zeros supplied by the preparation
   polynomial are \(0,\pm1/2\). Hence \(G(-s)\ne0\) for
   \(0<\Re s<1/2\), while its zero at \(s=1/2\) is simple because
   \(H(-1/2)>0\).

3. **Decay for the actual smoothness class.** The sixth distributional
   derivative of \(g\) is an interior polynomial plus two endpoint
   atoms, a finite signed measure. Since the derivative order is even,
   integration by parts gives \(z^6G(z)=\int e^{zv}\,d(D^6g)(v)\)
   with positive sign. The resulting \(|z|^{-6}\) estimate is adequate
   for absolute convergence and every contour step; no unstated
   infinitely differentiable test-function hypothesis is used.

4. **Initial inverse transform.** On \(\Re z=2\), Fourier inversion of
   \(e^{-3v/2}g(v)\) gives exactly the kernel
   \(e^{(z-1/2)y}G(1/2-z)n^{-z}\). Its inverse is
   \(n^{-1/2}g(y-\log n)\), confirming both the normalization and
   transform sign in the displayed contour integral. Absolute
   convergence follows from the Dirichlet series and sixth-power decay.

5. **Good heights and left contour.** The stated local zero count
   permits heights separated from all nearby ordinates by a constant
   times \(1/\log T\). Together with the logarithmic-derivative partial
   fraction formula this gives the stated \(O(\log^2T)\) estimate on
   each fixed bounded real strip. Horizontal integrals therefore tend
   to zero as \(T\to\infty\), with the left boundary fixed first.
   On \(z=-(2M+1)+it\), the logarithmic derivative of the functional
   equation reads
   \[
   \frac{\zeta'}{\zeta}(z)=\log(2\pi)
   +\frac\pi2\cot\frac{\pi z}{2}
   -\frac{\Gamma'}{\Gamma}(1-z)
   -\frac{\zeta'}{\zeta}(1-z).
   \]
   Here the cotangent is bounded uniformly in \(t,M\), the Dirichlet
   series on the right is uniformly bounded, and the digamma is
   \(O(\log(|z|+2))\) because \(\Re(1-z)\ge2\).
   More explicitly, the remaining vertical integral is
   \[
   O\!\left(e^{-(2M+3/2)(y-a)}
   (M+1)^{-5}\log(M+2)\right).
   \]
   It tends to zero locally uniformly for \(y>a\). Negative odd
   lines stay away from the trivial zeros, so no unrecorded indentation
   is required.

6. **Residues and complete formula.** The pole at one has positive
   residue before multiplication and contributes
   \(e^{y/2}G(-1/2)=0\). Each zero of multiplicity \(m_\rho\)
   contributes \(-m_\rho G(1/2-\rho)e^{(\rho-1/2)y}\).
   Every trivial zero contributes
   \(-G(2k+1/2)e^{-(2k+1/2)y}\); there is no zeta pole or zero at
   zero to add. Both ordinate signs and multiplicities are explicit.
   The zero count gives absolute summability of nontrivial coefficients;
   the trivial sum has the displayed geometric majorant for \(y>a\).
   Compact initial intervals are treated using the original locally
   finite arithmetic sum.

7. **True Laplace transform and pole exclusion.** The exact shell
   identity is
   \(\int|p_g(y)|^2dy=\int|V_g(x)|^2x^{-2}dx\).
   The assumed variance estimate gives shell energies
   \(O(2^{j\delta})\), and Cauchy--Schwarz gives the geometric factor
   \(2^{j(\delta/2-\Re s)}\). Locally uniform absolute convergence
   proves holomorphy only on the open half-plane
   \(\Re s>\delta/2\), exactly as needed.
   Since \(\log2>a\), the integral from zero includes every packet in
   full; termwise integration for \(\Re s>1/2\) yields
   \(-G(-s)\zeta'/\zeta(1/2+s)\) without an endpoint correction.
   The meromorphic identity theorem on the connected enlarged
   half-plane identifies this expression with the true transform.
   Every right-of-strip zero would then give a nonzero residue, contrary
   to holomorphy. Functional-equation symmetry supplies the left side.

8. **Converse and quantifiers.** On the closed strip the nontrivial
   exponential factors are at most \(e^{\delta y/2}\), including for
   zeros on either boundary. Absolute coefficient summability gives
   \(p_g(y)=O(e^{\delta y/2})\), hence the exact exponent
   \(\mathcal V_g(X)=O(X^{2+\delta})\), without logarithmic loss.
   At \(\delta=0\) this gives bounded \(p_g\), while cumulative
   energy is only asserted to be \(O(1+Y)\). At \(\delta=1\), the
   classical critical strip gives the unconditional baseline.
   The forward proof asserts no boundary convergence of the transform.

9. **RH limit and optimal exponent.** Intersecting the strips from any
   positive sequence \(\delta_j\to0\) gives RH without uniformity of
   variance constants or starting thresholds. A positive limiting
   exponent gives only its associated strip. The supremum
   \(d=2\sup_\rho(\Re\rho-1/2)\) lies in \([0,1]\) by symmetry
   and the critical strip. Every zero lies in the closed strip of width
   \(d\); the converse therefore proves the variance estimate at \(d\)
   itself. The stated infimum identity and attainment are justified,
   without determining its numerical value.

This review does not check the short-interval reduction or generic model
appendix, which were assigned separate proof passes. It does not verify
external numerical zero data. It also makes no claim of mathematical
priority or a newly proved global exponent improvement.
