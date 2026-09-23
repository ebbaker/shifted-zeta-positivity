# The arithmetic source and an actual generalized Loewner evolution

22 September 2026. Prepared for Edward Baker.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed in this session; not inferred.  
**Status:** internal analytical research with exact model controls and floating
diagnostics; specialist review outstanding. Prepared with LLM assistance.
The constructions below apply classical positive-real and Loewner theory;
no new RH criterion or independent physical realization is claimed.

## 1. Decision and what has been accomplished

Edward Baker asked whether the *source* of the arithmetic differential
equation can be related directly to Loewner evolution. Yes. The source is the
logarithmic derivative of the completed xi function. A sufficiently shifted
version is a positive-real function, hence supplies an actual generalized
Loewner vector field. Its arithmetic content includes the gamma factor,
rational terms, and every prime-power coefficient. There is also a genuine
Loewner semigroup whose evolution is linearized by the logarithm of xi.

This is a more direct **next investigation of arithmetic matching** than
extending WZW sewing without an arithmetic specification. The
[completed SU(2)_2 pilot](SU2_LEVEL2_DETERMINISTIC_LOEWNER_PILOT_20260922.md)
remains a useful physical benchmark. Its proposed sewing calculation is
deferred in priority, not invalidated. This note carries out the bounded
source calculation, the normalization and continuation tests, and two
obstruction controls before recommending further work.

The outcome has a precise limit: the safe shifted source gives a Loewner
evolution unconditionally, but obtaining this positive-real source at zero
shift is already equivalent to RH. Moreover, the logarithmic generator of
the *arithmetic transfer* has interior poles even under RH, so it cannot
itself be the positive-real Loewner driver. These observations distinguish
an exact connection at the level of the source from a completed realization
of the arithmetic operator and its norm.

The source identity and commuting arithmetic deformation were already
recognized in [the earlier shift-flow note](../../wilson-lines/notes/DEFORMATION_FLOW_AND_THE_SHIFT_20260917.md).
The cumulative Cayley alternative is also already in
[the earlier critical-path assessment](../../wilson-lines/notes/CRITICAL_PATH_20260917.md).
The contribution here is the explicit normalized Loewner construction,
its relation to the full arithmetic source, and the tests separating its
geometric time, regularizing shift, and arithmetic shift.

## 2. Begin with the arithmetic source

Use the manuscript conventions

\[
 H(p)=\xi(\tfrac12+p),\qquad m(p)=\frac{H'(p)}{H(p)},\qquad
 K_\omega(p)=\frac{H(p-\omega)}{H(p+\omega)}.
\]

On a right half-plane without zeros or poles,

\[
 \partial_\omega K_\omega(p)=-a_\omega(p)K_\omega(p),\qquad
 a_\omega(p)=m(p-\omega)+m(p+\omega),\qquad K_0(p)=1. \tag{2.1}
\]

These identities continue meromorphically. Products such as
\(a_\omega K_\omega\) can be regular where \(a_\omega\) has a pole.
The exact completion gives

\[
 m(p)=\frac1{p+1/2}+\frac1{p-1/2}-\frac12\log\pi
       +\frac12\psi(\tfrac14+\tfrac p2)
       +\frac{\zeta'}{\zeta}(\tfrac12+p). \tag{2.2}
\]

The apparent singularities at the completed function's removable points
must be treated together. In the absolutely convergent prime region
\(\Re p>1/2+\omega\), the prime part of (2.1) is

\[
 -2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       \cosh(\omega\log n)e^{-p\log n}. \tag{2.3}
\]

Thus the source already specifies the delays \(\log n\), their weights,
and the complete local and archimedean terms. In particular its first
prime delay is
\(-\sqrt2\log2\cosh(\omega\log2)e^{-p\log2}\).
Building the geometric source from (2.2) does not omit the primes or fit
them after the geometric calculation.

## 3. The positive-real source and its exact limitation

Write the xi zeros as \(\rho=1/2+\alpha_\rho+i\gamma_\rho\), with
multiplicity. The centered product and functional equation give, away
from zeros,

\[
 \Re m(x+iy)=\sum_\rho
 \frac{x-\alpha_\rho}
 {(x-\alpha_\rho)^2+(y-\gamma_\rho)^2}. \tag{3.1}
\]

The complex logarithmic-derivative series is symmetrically grouped; its
real-part series here converges absolutely. Centered functional symmetry
removes an additional real constant. This is not a sum over an assumed
list of critical zeros.

For \(\eta\ge0\), let

\[
 m_\eta(p)=m(p+\eta),\qquad \mathbb H_R=\{p:\Re p>0\}.
\]

Equation (3.1) gives the following exact equivalence:

\[
 \boxed{m_\eta\text{ is holomorphic and has positive real part on }
 \mathbb H_R
 \iff \xi\text{ has no zero with }\Re\rho>\tfrac12+\eta.} \tag{3.2}
\]

For the forward implication, a zero in that half-plane would give an
interior pole of \(m_\eta\), with positive integer residue. Conversely,
absence of such zeros makes every numerator in (3.1), evaluated at
\(p+\eta\), strictly positive. In particular:

- \(\eta\ge1/2\) is unconditional, using the known zero-free region
  \(\Re\rho\ge1\).
- \(\eta=0\) is equivalent to RH, using symmetry about the critical line.

The underlying positivity criterion is classical; see
[Lagarias, *On a positivity property of the Riemann xi-function*](https://matwbn.icm.edu.pl/ksiazki/aa/aa89/aa8932.pdf)
and its [published correction](https://www.impan.pl/shop/en/publication/transaction/download/product/81942).
The correction matters when importing auxiliary inequalities; this note
uses the centered product argument above and the positive sign of
\(1/(s-1)\) in the completed logarithmic derivative.

For every \(\eta\ge0\), the normalization constant
\(c_\eta=m(1+\eta)>0\) is already unconditional, since its argument lies
in the safe region. Positivity at that single point does not establish
positivity of the whole function.

## 4. A normalized radial Loewner evolution, with arithmetic source

Set

\[
 C(w)=\frac{1+w}{1-w},\qquad \chi(p)=\frac{p-1}{p+1},\qquad
 P_\eta(w)=\frac{m(\eta+C(w))}{c_\eta}. \tag{4.1}
\]

For \(\eta\ge1/2\), \(P_\eta\) is holomorphic on the disk,
\(\Re P_\eta>0\), and \(P_\eta(0)=1\). Hence

\[
 \partial_\tau\varphi_\tau(w)
 =-\varphi_\tau(w)P_\eta(\varphi_\tau(w)),\qquad
 \varphi_0(w)=w \tag{4.2}
\]

defines a global univalent disk self-map semigroup, with
\(\varphi_\tau'(0)=e^{-\tau}\). This is the inward evolution-family
convention for generalized radial Loewner evolution. The positive-real
criterion for the vector field is the classical Berkson--Porta framework;
see [Bracci--Contreras--Diaz-Madrigal, Theorems 1.1--1.2](https://arxiv.org/pdf/0807.1594).

Its Herglotz probability measure satisfies

\[
 P_\eta(w)=\int_{|\zeta|=1}\frac{\zeta+w}{\zeta-w}\,d\mu_\eta(\zeta).
 \tag{4.3}
\]

For the safe shifts the measure can be obtained directly from xi on a
zero-free vertical line:

\[
 d\mu_\eta(e^{i\theta})=
 \frac{\Re m(\eta+i\cot(\theta/2))}{2\pi c_\eta}\,d\theta.
 \tag{4.4}
\]

There is no atom at \(\zeta=1\): its mass is the limit of
\(m(\eta+x)/(c_\eta x)\) as \(x\to+\infty\), which is zero.
The remaining boundary points have analytic continuation across them,
so no additional singular measure is hidden in (4.4).

Under RH, but only then as a whole-half-plane construction at \(\eta=0\),
the limiting measure has the explicit atomic form

\[
 \zeta_\gamma=\frac{i\gamma-1}{i\gamma+1},\qquad
 \mu_0=\sum_{\gamma\text{ of either sign}}
       \frac{1}{c_0(1+\gamma^2)}\,\delta_{\zeta_\gamma}. \tag{4.5}
\]

Multiplicity is included. Indeed
\(m(p)=\sum_{\gamma>0}2p/(p^2+\gamma^2)\), and the paired Herglotz
kernels give (4.5); their weights sum to one by evaluating at \(p=1\).
The weights are summable. Assigning unit mass to every zero on the real
line would instead have infinite mass and would not be an ordinary
finite-capacity chordal driving probability measure.

Finally, for \(\Re p>\eta+\omega\), the *entire* arithmetic source is
recovered by

\[
 \boxed{a_\omega(p)=c_\eta\left[
 P_\eta\bigl(\chi(p-\omega-\eta)\bigr)
 +P_\eta\bigl(\chi(p+\omega-\eta)\bigr)\right].} \tag{4.6}
\]

This is an exact identity, not an asymptotic match or a comparison of
selected poles. Equations (2.2)--(2.3) supply its arithmetic coefficients.
It builds arithmetic data into geometry; it does not derive that data
from an independently specified field theory.

## 5. A second genuine flow, linearized by log xi

The same source has a geometric construction in which xi itself controls
the flow. Fix \(\eta\ge1/2\) and choose the analytic branch

\[
 L_\eta(p)=\log H(p+\eta)
\]

real on the positive real axis. It is univalent on \(\mathbb H_R\):

\[
 \frac{L_\eta(p)-L_\eta(q)}{p-q}
 =\int_0^1m_\eta(q+s(p-q))\,ds
\]

has positive real part for \(p\ne q\). Define

\[
 \partial_\tau\psi_\tau(p)
 =\frac{c_\eta}{m(\psi_\tau(p)+\eta)},\qquad \psi_0(p)=p. \tag{5.1}
\]

The reciprocal source also has positive real part. In disk coordinates
its vector field is

\[
 \dot w=\frac{(1-w)^2}{2P_\eta(w)}, \tag{5.2}
\]

a Berkson--Porta generator with boundary fixed point 1. Therefore (5.1)
is a global holomorphic self-map semigroup on \(\mathbb H_R\), not just
a local formal ODE. Along each trajectory,

\[
 \boxed{L_\eta(\psi_\tau(p))=L_\eta(p)+c_\eta\tau,
 \quad H(\psi_\tau(p)+\eta)=e^{c_\eta\tau}H(p+\eta).} \tag{5.3}
\]

Thus \(L_\eta\) is a Koenigs linearizing coordinate. Equation (5.1)
also has \(\partial_\tau\Re\psi_\tau>0\). It is generally neither a
single-slit chordal evolution nor the deterministic WZW evolution of the
earlier pilot. The coordinate \(p\) remains a spectral coordinate; no
identification with the physical boundary position has been derived.

On the domain of (4.6), the arithmetic transfer is exactly

\[
 K_\omega(p)=\exp\left[
 L_\eta(p-\omega-\eta)-L_\eta(p+\omega-\eta)\right]. \tag{5.4}
\]

The identity specifies a possible endpoint readout of the same analytic
potential. It is not the assertion that changing \(\omega\) follows
the trajectories (5.1).

## 6. What changing the regularization actually does

The three parameters have different meanings:

| Parameter | Role |
|---|---|
| \(\omega\) | Arithmetic shift defining \(K_\omega\) |
| \(\eta\) | Translation of the logarithmic-derivative source into a zero-free region |
| \(\tau\) | Geometric time in (4.2) or (5.1) |

Differentiating (4.1) gives an exact transport equation for the source:

\[
 \partial_\eta P_\eta(w)
 =\frac{(1-w)^2}{2}\partial_wP_\eta(w)
  -\kappa_\eta P_\eta(w),\qquad
 \kappa_\eta=\frac{m'(1+\eta)}{m(1+\eta)}. \tag{6.1}
\]

For \(h\ge0\), this integrates to

\[
 P_{\eta+h}(\chi(p))
 =\frac{c_\eta}{c_{\eta+h}}P_\eta(\chi(p+h)). \tag{6.2}
\]

Translation to the right is a half-plane self-map and preserves the
positive-real property. Where \(\eta\ge1/2\), let
\(u_\eta(y)=\Re m(\eta+iy)\). Its continuation farther right is
Poisson smoothing:

\[
 u_{\eta+h}(y)=\frac1\pi\int_{\mathbb R}
 \frac{h}{h^2+(y-t)^2}\,u_\eta(t)\,dt,\qquad h>0. \tag{6.3}
\]

The absence of a linear term at infinity follows from the xi asymptotic
used above. Reversing this smoothing is not positivity preserving.
Equations (6.1)--(6.3) therefore do not supply a continuation proof down
to \(\eta=0\).

An explicit control is the even, real entire polynomial

\[
 H_\delta(p)=((p-\delta)^2+\gamma^2)
            ((p+\delta)^2+\gamma^2),\qquad \delta>0. \tag{6.4}
\]

It has the same reflection and conjugation symmetries and a positive-real
shifted logarithmic derivative for \(\eta>\delta\). At
\(\eta<\delta\), poles enter the right half-plane. With
\(\delta=1/4,\gamma=2\), the shift \(\eta=1/2\) is safe, while at
\(\eta=1/10\) the disk pole has modulus approximately 0.941951 and a
sampled real part of the shifted logarithmic derivative is approximately
\(-17.7531\). This polynomial is a counterexample to a *general*
continuation argument based on symmetry and a safe positive shift, not a
model of the actual xi zero locations.

Even the RH-type polynomial \(H(p)=p^2+\gamma^2\) gives
\(m'(x)=2(\gamma^2-x^2)/(x^2+\gamma^2)^2\), of either sign on the
positive real axis. There is no general pointwise monotonicity in
\(\eta\) that substitutes for the missing continuation argument.

## 7. Why the arithmetic transfer is not yet a Loewner operator

### 7.1 The two endpoint paths have different velocities

For \(w_\pm(\omega)=\chi(p\pm\omega-\eta)\),

\[
 \partial_\omega w_\pm=\pm\tfrac12(1-w_\pm)^2. \tag{7.1}
\]

They are opposite translations in half-plane coordinates. They are not
trajectories of the single radial vector field \(-wP_\eta(w)\): at
\(w=0\) that field vanishes, whereas the velocities in (7.1) are
\(\pm1/2\). A scalar change of clock cannot identify these fields on
their whole domain. The reciprocal-source flow (5.1) likewise has a
position-dependent velocity in place of these fixed translations.
This excludes the proposed direct identification of these paths, not
every possible boundary observable or intertwiner.

### 7.2 Multiplication is not composition

In the Laplace representation the arithmetic operator acts as
\(F(p)\mapsto K_\omega(p)F(p)\). A geometric self-map acts by
composition. Even allowing a weight,

\[
 W(p)F(\psi(p))=K_\omega(p)F(p)\quad\text{for every analytic }F
\]

forces \(W=K_\omega\) and \(\psi(p)=p\), wherever the multiplier
is nonzero, by testing \(F=1,p\). This is an algebraic statement on
analytic functions; it does not assume these test functions belong to
the unweighted half-plane Hardy space. A physical construction still
needs a specified boundary readout, or a nontrivial intertwining map,
with the intended Hilbert norm.

### 7.3 The transfer generator itself is not a Herglotz driver

Even assuming RH, for every \(\omega>0\) the term \(m(p-\omega)\)
has poles at \(p=\omega+i\gamma\) inside \(\mathbb H_R\).
The second term in \(a_\omega\) does not cancel them. Thus
\(a_\omega\) is not a holomorphic positive-real function on that
half-plane, although \(K_\omega\) can be a contractive analytic
multiplier there. Its zeros cancel the logarithmic poles in (2.1).

This also fails away from the poles. For \(H(p)=p^2+4\), the transfer
is a finite half-plane Blaschke product for every \(\omega>0\). Yet
at \(p=1/4+2i\) and \(\omega=1/2\), exact rational arithmetic gives

\[
 |K_\omega(p)|^2=\frac{257}{2385}<1,\qquad
 \Re a_\omega(p)=-\frac{538768}{204315}<0. \tag{7.2}
\]

Consequently \(\partial_\omega|K_\omega(p)|^2>0\) there, despite
\(|K_\omega|<1\) throughout the half-plane. A cumulative contraction
does not imply contractive multiplicative increments. Requiring
\(\Re a_\omega\ge0\) on the whole half-plane would impose a false
condition even on this simplest RH-type control.

The appropriate cumulative positive-real candidate is instead

\[
 Z_\omega=\frac{1-K_\omega}{1+K_\omega},\qquad
 \Re Z_\omega=\frac{1-|K_\omega|^2}{|1+K_\omega|^2},\qquad
 \partial_\omega Z_\omega=\frac{a_\omega}{2}(1-Z_\omega^2). \tag{7.3}
\]

The last equality holds on regular regions and continues through
removable singularities. It is a useful exact Riccati identity, not an
independent positivity proof. It links this source investigation to the
existing cumulative Cayley and canonical-system program.

## 8. A direct operator consequence, and the cost of the safe shift

There is a rigorous operator result obtainable without a physical model.
Fix \(0\le\omega\le\Omega\) and a spectral translation
\(b\ge\Omega+1/2\). Then both terms of \(a_\omega(p+b)\) are
positive-real on \(\mathbb H_R\). Integrating (2.1) from \(\omega=0\)
therefore gives

\[
 |K_\omega(p+b)|\le1,\qquad \Re p>0. \tag{8.1}
\]

The shifted transfer is a contraction on the causal Hardy/Laplace space.
For its compression to \(L^2(0,L)\), let \(V_\omega\) be the
unshifted arithmetic convolution operator and
\((E_bf)(x)=e^{bx}f(x)\). The Laplace translation rule gives

\[
 V_{\omega,b}=E_{-b}V_\omega E_b,\qquad
 \|V_{\omega,b}\|\le1,
 \qquad \boxed{\|V_\omega\|\le e^{bL}.} \tag{8.2}
\]

One can equivalently define the finite-window unshifted operator by
this conjugation, consistent with its causal Laplace kernel. Its strong
identity limit at \(\omega=0\) follows from pointwise multiplier
convergence and dominated convergence; no operator-norm limit is asserted.
The estimate in (8.2) is an upper
bound, not a statement that the actual norm grows at that rate.

This is why safe-source positivity alone is insufficient: removing the
spectral weight costs a length-dependent factor. The unconditional
choice of \(b\) stays at least \(1/2\), so this estimate does not
approach a contraction as \(L\to\infty\). It is an explicit weighted
operator control, not the unweighted arithmetic norm identity sought
in the investigation.

## 9. Numerical controls and their scope

The separate [checker](../numerics/check_arithmetic_loewner_source.py) and
[record](../numerics/records/arithmetic-loewner-source-20260922.json) contain
**60 passing cases: four exact rational controls and 56 floating checks**.
The floating calculations use mpmath 1.3.0, normally at 40 decimal digits;
the time integrator uses double precision with 25-digit function
evaluations. They check:

- The completed logarithmic derivative against differentiation of xi,
  the shift equation, functional symmetry, the Cayley Riccati identity,
  and recovery of the source from \(P_\eta\).
- Prime-power reconstruction through \(n=1000\), including the gamma
  and rational terms, against an analytical tail bound.
- Source normalization, finite positivity samples, and the normalized
  transport equation and composition law (6.1)--(6.2).
- Evolution (5.1) at two initial points, step refinement, semigroup
  composition, half-plane motion, and the xi ratio in (5.3).
- A finite imaginary-zero Herglotz measure, the off-axis quartet control,
  and the exact distinction between cumulative and incremental contraction.

At \(p=5.5+0.7i\), \(\omega=0.2\), the prime reconstruction residual
is approximately \(8.81\times10^{-16}\), below the analytical tail
bound \(6.24\times10^{-15}\). The bound follows from
\(\Lambda(n)\le\log n\) and, for the sampled \(\sigma>1\),

\[
 \sum_{n>N}(\log n)n^{-\sigma}
 \le N^{1-\sigma}
 \left(\frac{\log N}{\sigma-1}+\frac1{(\sigma-1)^2}\right). \tag{9.1}
\]

The integral comparison is used where the summand is decreasing
for \(n\ge N\). Residual evaluations are floating values, not interval
certificates of their comparison to (9.1).

For \(\eta=1/2\), \(\tau=0.3\), the flow from \(1+0.7i\) ends
near \(1.2393712363+0.6045293214i\). The independently evaluated ratio
\(H(\psi_\tau(p)+\eta)/H(p+\eta)\) is approximately
\(1.0209360162\), agreeing with \(e^{c_\eta\tau}\). No xi-zero
table is used. The analytic positivity argument is (3.1)--(3.2), not
the finite sample grid.

Replay from the investigation directory with mpmath installed:

```sh
python3 -B numerics/check_arithmetic_loewner_source.py --output /tmp/arithmetic-loewner-source-replay.json
```

These cases are separate from the 72 WZW pilot controls and the original
299-case manuscript diagnostics. No manuscript or historical snapshot
is revised by this note. See the [same-assistant audit](../reviews/review_codex_arithmetic_loewner_source_20260922.md).

## 10. What should be pursued next

The result justifies working from the arithmetic source before expanding
the WZW construction. It also supplies a concrete rejection test: neither
an unproved positive measure at \(\eta=0\), nor
\(\Re a_\omega\ge0\), can be used as a shortcut.

The next bounded calculation should specify a **cumulative boundary or
canonical response** for \(K_\omega\) or \(Z_\omega\), starting from
the complete prime/gamma source on a safe line. Its deliverable is a
fixed-Hilbert-space operator dictionary and an explicit norm balance,
including the cost of removing the weight in (8.2). The tests are:

1. Identity initial operator; correct local and pole terms on
   \(0<L<\log2\), where the prime delays are absent.
2. The exact first delay coefficient from (2.3) as \(L\) passes
   \(\log2\), with a bound on all boundary or storage terms.
3. A cumulative positivity mechanism that permits the negative
   instantaneous generator in (7.2), rather than ruling it out by
   assumption.

For a canonical-system route, the distinction between spectral shift and
canonical depth must remain explicit. [Suzuki's construction](https://arxiv.org/html/1204.1827)
already relates the family
\(\xi(1/2-\omega-iz)/\xi(1/2+\omega-iz)=K_\omega(-iz)\)
to meromorphic inner functions and gives an explicit unconditional
canonical system for \(\omega>1\). Its criterion for innerness for
all positive shifts is RH-equivalent. The explicit construction's
\(\omega>1\) range must not be confused with unconditional innerness
for \(\omega\ge1/2\), or with the independent source shift \(\eta\).

Likewise the modular-surface scattering realization of the
\(\omega=1/2\) endpoint is already recorded in
[the parent realization analysis](../../loewner/sections/04_realizations.tex).
It is a comparison point, not a new result here or a continuous-shift
realization.

A new boundary or canonical response would count as progress toward an
independent realization only if its operator and positive norm are
specified without assuming the contractivity one hopes to prove. Merely
assigning (4.3) at zero shift, or calling the arithmetic multiplier a
geometric readout by definition, would leave that obligation untouched.
The present note provides an exact arithmetic source for that comparison
and establishes where the proposed direct identifications succeed and fail.
