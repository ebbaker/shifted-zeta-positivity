# Modular Hodge scattering and a bounded cusp-coupling test

23 September 2026. Prepared for Edward Baker with LLM assistance.

**Model:** GPT-6 (Codex; developer-provided identity).  
**Effort:** not exposed; not inferred.  
**Status:** a geometric realization of the fixed half-shift response in an exact one-form radiation channel, and an analytical exclusion of one real cusp-coupling family as the arithmetic shift evolution. No variable-shift realization, RH result, novelty claim for Hodge scattering, or independent specialist review.

This continues the [independent-source search](INDEPENDENT_ARITHMETIC_SOURCE_SEARCH_20260923.md) and [Brownian test](BROWNIAN_BRIDGE_READOUT_TEST_20260923.md). The [program](../numerics/check_modular_scattering.py), [65-case record](../numerics/records/modular-scattering-20260923.json), and [same-assistant audit](../reviews/review_codex_modular_scattering_20260923.md) accompany the derivation. Section 8 documents a correction to two earlier numerical implementations and their complete replays.

## 1. What this resolves

At arithmetic shift one half, the rational completion of scalar modular scattering is supplied by a native differential operation: pass from scalar waves to their exterior derivatives. In the exact one-form channel, the ordinary incoming/outgoing amplitude ratio is minus the desired transfer. A fixed output orientation removes the minus sign. Its positive norm follows from the Hodge Hilbert space and the normalized gradient isometry; causality uses the known unconditional half-shift innerness theorem.

The arithmetic weights already come from the modular quotient. They are not added as a prime-dependent filter. This gives a stronger fixed-shift physical benchmark than a scalar moment identity or an unverified boundary phase.

A real, frequency-independent delta load in the open cusp channel remains lossless and causal, but its infinitesimal response is not the arithmetic shift derivative. The mismatch is analytical, both at high positive Laplace frequency and at the first delayed singularity. The remaining task is a physical deformation of the system, not a further normalization of this fixed-shift channel.

## 2. Scalar geometry and the native completion

Write

\[
\Lambda_R(s)=\pi^{-s/2}\Gamma(s/2)\zeta(s),\qquad
\xi(s)=\tfrac12s(s-1)\Lambda_R(s),\qquad H(p)=\xi(\tfrac12+p).
\]

The target family and its source are

\[
K_\omega(p)=\frac{H(p-\omega)}{H(p+\omega)},\qquad
\partial_\omega\log K_\omega(p)=-a_\omega(p).
\]

In particular,

\[
K(p):=K_{1/2}(p)=\frac{\xi(p)}{\xi(p+1)},\qquad
a_{1/2}(p)=\frac{\xi'(p)}{\xi(p)}+\frac{\xi'(p+1)}{\xi(p+1)}.
\]

On the modular surface (orbifold) \(M=\mathrm{PSL}_2(\mathbb Z)\backslash\mathbb H\), use its hyperbolic metric and positive scalar Laplacian

\[
\Delta_0=-y^2(\partial_x^2+\partial_y^2),\qquad
L^2(M,dx\,dy/y^2).
\]

The Eisenstein wave has constant term

\[
E_\sigma=y^\sigma+\phi(\sigma)y^{1-\sigma}+\text{nonconstant modes},\qquad
\phi(\sigma)=\frac{\Lambda_R(2\sigma-1)}{\Lambda_R(2\sigma)}.
\]

These conventions follow the standard constant-term calculation; see [Lagarias–Suzuki](https://arxiv.org/pdf/math/0412039). The physical cusp coordinate and scalar scattering interpretation are explicit in [Savvidy–Savvidy, equations 1.1–1.10](https://arxiv.org/html/1809.09491).

Set \(p=2\sigma-1\), \(q=\log y\). On the physical axis take \(\sigma=1/2-ik\), so \(p=-2ik\). With scalar amplitude \(f=e^{q/2}v\), the constant channel is \(-\partial_q^2+1/4\), with eigenvalue \(k^2+1/4\). Then

\[
\phi=\sqrt\pi\frac{\Gamma(p/2)}{\Gamma((p+1)/2)}
\frac{\zeta(p)}{\zeta(p+1)},\qquad
K(p)=\frac{p-1}{p+1}\phi.
\]

The completion factor is not obtained merely by projecting away the constant scalar state: that projection leaves the scalar continuum coefficient unchanged. Instead take the exact one-form \(dE_\sigma\). In the unit vertical coframe \(dq\), its constant term is

\[
\sigma y^\sigma dq+(1-\sigma)\phi(\sigma)y^{1-\sigma}dq.
\]

Its raw outgoing/incoming ratio is therefore

\[
R_1(p)=\frac{1-\sigma}{\sigma}\phi(\sigma)
=-\frac{p-1}{p+1}\phi(\sigma)=-K(p).
\]

Choose measured outgoing amplitude to be minus the outgoing vertical coefficient. This is a single frequency-independent orientation convention, giving \(S_0=K\). The same convention must be retained when a load is added below. This mechanism is consistent with the standard weight-raising formula: the weight-two constant term acquires coefficients \(\sigma\) and \(1-\sigma\); see [O’Sullivan, equations 2.7 and 2.12](https://fsw01.bcc.cuny.edu/cormac.osullivan/Research/Eisenstein-series-Riemann-zeta3.pdf). We use this established structure, without claiming a new scattering theorem.

The scalar coefficient has residue \(6/\pi\) at \(p=1\), whereas the completed response is regular there:

\[
K(1)=\frac{3}{\pi}.
\]

The exterior derivative kills the scalar constant state responsible for this pole. Pole removal here has both a geometric explanation and the required exact coefficient.

## 3. State norm, radiation norm, and causality

Use the positive Hodge Laplacian \(\Delta_1=d\delta+\delta d\) on one-forms and its closed exact sector. The polar map

\[
J=d\Delta_0^{-1/2},\qquad
J^*J=I-P_{\rm const},\qquad JJ^*=P_{\rm exact},\qquad
\Delta_1J=J\Delta_0
\]

is defined by closure and functional calculus on the orthogonal complement of constants. These identities follow from \(d^*d=\Delta_0\). They identify an ordinary positive Hilbert norm, without defining a norm using xi.

On a continuum eigenwave, the incoming and outgoing normalization factors are

\[
\frac{1/2-ik}{\sqrt{1/4+k^2}},\qquad
\frac{1/2+ik}{\sqrt{1/4+k^2}},
\]

each of modulus one. For a constant one-form \(a(q)dq\), the state norm is \(\int e^{-q}|a(q)|^2dq\). Writing \(a=e^{q/2}v\) gives ordinary \(L^2(dq)\), with flux

\[
j=\operatorname{Im}(\bar v v')=k(|A_{\rm out}|^2-|A_{\rm in}|^2).
\]

For propagation one may use the shifted wave equation
\(\Psi_{tt}+(\Delta_1-1/4)\Psi=0\) on the exact absolutely continuous radiation sector. The shifted generator is nonnegative there. We do not assert its positivity on every one-form state. Wave frequency is \(k\); Schrödinger time, conjugate to \(k^2+1/4\), is not the arithmetic delay variable.

Because \(p=-2ik\), arithmetic delay \(u\) is half the physical wave delay. The map \(f(t)\mapsto\sqrt2 f(2u)\) preserves the unweighted radiation norm. The reference convention is the one used in the displayed Eisenstein constant term; a port at \(q=b\) adds the explicit delay \(e^{-bp}\).

Real-frequency unitarity alone does not imply causality. Here causality is supplied by the unconditional innerness of \(K_{1/2}\) in \(\Re p>0\), a known safe-shift result; see [Suzuki, Sections 1.2–1.4 and Theorem 2.2](https://arxiv.org/html/1204.1827). It implies that the boundary multiplier defines a causal isometry on radiation signals. This is a fixed-shift result and does not settle the RH-equivalent full positive-shift assertion.

Consequently, for \(f\) supported on \((0,L)\),

\[
\|f\|_2^2-\|1_{(0,L)}S_0f\|_2^2
=\|1_{(L,\infty)}S_0f\|_2^2\ge0.
\]

There is no earlier-than-zero term, because causality has been established, and no postulated arithmetic weight in this norm. This is a radiation input/output balance, not a claim that state norm, wave energy and arbitrary field-smearing norm are identical without their stated normalizations.

## 4. Arithmetic delays already in the geometry

In the scalar constant-term calculation, primitive residue classes \((c,d)\) contribute Euler’s totient \(\varphi_E(c)\); integration in the cusp supplies the gamma factor. Equivalently, for \(\Re p>1\),

\[
\frac{\zeta(p)}{\zeta(p+1)}
=\sum_{n\ge1}\frac{\varphi_E(n)}{n}e^{-p\log n}.
\]

Thus the first coefficient is \(c_2=1/2\). This arithmetic is part of the modular quotient, rather than an externally supplied sequence of delayed filters.

Let \(k_0\) denote the prime-free part of the half-shift kernel (subscript zero means no delayed arithmetic terms, not zero shift). It has the closed form

\[
k_0(u)=\frac{2(2e^{-2u}-1)}{\sqrt{1-e^{-2u}}},\qquad u>0.
\]

Writing \(z=\sqrt{1-e^{-2u}}\), its cumulative integral is

\[
G_0(u)=4z-2\operatorname{atanh}z
=4z-2u-2\log(1+z).
\]

The second expression is numerically stable for large \(u\). Locally \(k_0(u)\sim\sqrt2u^{-1/2}\); it changes sign at \(u=\tfrac12\log2\). Coherent scattering permits this sign change, unlike a positive delay average.

For \(\log2<u<\log3\),

\[
k(u)=k_0(u)+\tfrac12 k_0(u-\log2).
\]

For the unit indicator input on \((0,1)\), the output before time one is \(G_0(u)+\tfrac12G_0(u-\log2)\), where \(G_0=0\) at nonpositive arguments. Its computed squared norm is

\[
0.947244169601155008252987.
\]

The remaining energy, \(0.0527558303988449917470129\), follows from proved conservation. It was not separately evaluated by integrating the entire future arithmetic kernel. The finite-window quadrature was repeated at 15 extra decimal digits.

## 5. One explicit independent cusp coupling

Choose the regular cusp cross-section \(q=b=1\), i.e. \(y=e\). No prime length enters this choice. Add a real, frequency-independent delta load of strength \(\alpha\ge0\) to the constant vertical cusp mode only:

\[
v(b+)=v(b-),\qquad v'(b+)-v'(b-)=\alpha v(b).
\]

Other angular modes retain their original matching conditions. This is an angular-average channel load, not a local point scatterer on the two-dimensional surface. Its matching condition is self-adjoint; its quadratic-form addition is \(\alpha|v(b)|^2\). It may also be viewed as a point interaction on the free open lead attached to the geometric core.

At this port put \(d_b=e^{-bp}\), \(r_b=d_bK\). The raw vertical reflection is \(-r_b\). Solving the two matching equations with the same output orientation as above gives

\[
S_{\alpha,b}(p)=
\frac{p r_b+\alpha(1-r_b)}{p+\alpha(1-r_b)}.
\]

In particular \(S_{0,b}=d_bK\). The common reference delay must also appear in the arithmetic comparison \(d_bK_{\omega(\alpha)}\); moving the measurement port is not an arithmetic shift.

For numerator \(N\) and denominator \(D\), direct algebra gives

\[
|D|^2-|N|^2
=|p|^2(1-|r_b|^2)+2\alpha\Re(p)|1-r_b|^2\ge0.
\]

Moreover \(\Re D>0\) in the right half-plane, so there is no denominator zero there. The loaded response is contractive and analytic, with unit boundary modulus. The coupling therefore preserves the causal lossless properties relevant here. As \(\alpha\to\infty\), the normalized response tends to prompt reflection 1 almost everywhere on the boundary and hence strongly on radiation \(L^2\). At a nonzero port this endpoint is not the fixed-delay arithmetic identity.

## 6. The arithmetic tangent fails

The native logarithmic tangent is

\[
D_b(p):=\left.\partial_\alpha\log S_{\alpha,b}(p)\right|_0
=\frac{(1-e^{-bp}K(p))^2}{p e^{-bp}K(p)}.
\]

A differentiable arithmetic clock \(\omega(\alpha)=1/2+c\alpha+o(\alpha)\), with a real frequency-independent nonzero \(c\), would require

\[
D_b(p)=-c\,a_{1/2}(p).
\]

For large positive \(p\),

\[
K(p)\sim\sqrt{2\pi/p},\qquad a_{1/2}(p)\sim\log(p/(2\pi)),
\]

whereas

\[
D_b(p)\sim\frac{e^{bp}}{\sqrt{2\pi p}}\quad(b>0),\qquad
D_0(p)\sim\frac1{\sqrt{2\pi p}}.
\]

Neither can equal a nonzero constant multiple of the arithmetic source. The \(b=0\) case is a favorable algebraic zero-extra-lead control, not the selected regular cross-section. Even it fails. A zero clock derivative cannot help, since the native tangent is nonzero. Adding only a moving reference contributes a term proportional to \(p\), which cannot repair either asymptotic mismatch.

For illustration, fitting \(c=-D_b/a_{1/2}\) separately at three frequencies gives:

| \(p\) | control \(b=0\) | physical port \(b=1\) |
|---:|---:|---:|
| 2 | -0.0229835217 | -16.9602146 |
| 4 | -0.0226134038 | -43.9856043 |
| 8 | -0.0213918543 | -771.5444001 |

The analytical asymptotics, not these finite values, establish the exclusion. For finite \(\alpha\) the zero-extra-lead response still has leading order \(p^{-1/2}\), so it does not change the arithmetic front exponent to \(p^{-\omega}\).

### A bounded first-delay exclusion

The transfer tangent itself is

\[
\left.\partial_\alpha S_{\alpha,b}\right|_0
=\frac{(1-d_bK)^2}{p}.
\]

Let \(G(u)=\int_0^u k(v)dv\), \(Q(u)=\int_0^u(k*k)(v)dv\), and extend these by zero to negative arguments. Its inverse Laplace transform is

\[
\delta s_b(u)=1_{u>0}-2G(u-b)+Q(u-2b).
\]

For \(b>0\) it has an immediate step, before the target's fixed delay \(b\). At \(b=0\) its initial limit is 1, whereas

\[
\left.\partial_\omega k_\omega^<(u)\right|_{1/2}
\sim\sqrt2u^{-1/2}[\log u+C],\qquad
C=\log(2\pi)-\psi(1/2).
\]

There is also an independent first-prime mismatch. In the target family,
\(c_2(1/2)=1/2\) and \(c_2'(1/2)=\tfrac32\log2\). The new delayed contribution at \(b+\log2+\epsilon\) is

\[
J_{\rm target}(\epsilon)=c_2'k_0(\epsilon)
+\tfrac12\left.\partial_\omega k_\omega^<(\epsilon)\right|_{1/2}
\sim\sqrt2\epsilon^{-1/2}
\left[\tfrac12\log\epsilon+c_2'+\tfrac12 C\right].
\]

For the chosen \(b=1\), \(b+\log2<2b\), so the corresponding new native contribution is exactly \(-G_0(\epsilon)\sim-2\sqrt2\sqrt\epsilon\). In the favorable \(b=0\) control it is \(-G_0(\epsilon)+Q_0(\epsilon)\), where \(Q_0=\int_0^\epsilon k_0*k_0\sim2\pi\epsilon\). Both native increments vanish instead of diverging.

| \(\epsilon\) | load increment, \(b=1\) | arithmetic increment |
|---:|---:|---:|
| \(10^{-4}\) | -0.02828097153 | -235.34963438 |
| \(10^{-6}\) | -0.002828423825 | -5610.64775759 |

### Meromorphic pole diagnostic

At a simple xi zero \(\rho\), the load logarithmic tangent has residue

\[
\operatorname{Res}_{p=\rho}D_b(p)=\frac{e^{b\rho}}{\rho K'(\rho)},\qquad
K'(\rho)=\frac{\xi'(\rho)}{\xi(\rho+1)}.
\]

The arithmetic tangent would require the same real residue \(-c\) at every simple zero. Two locally solved approximate roots give incompatible, nonreal candidate clocks at \(b=1\): approximately \(-0.0987462-0.0691768i\) and \(-0.0162824-0.0823568i\). These are illustrative floating computations, not certified zero locations or evidence for RH. No external zero table is used. Simplicity is an explicit condition in the residue formula; multiple zeros would give a different, higher pole order for the native tangent. The exclusion already follows without any zero calculation.

## 7. Consequence for the broader program

The modular system supplies the exact arithmetic response at one independently meaningful shift, including a native completion and ordinary causal radiation norm. This resolves the fixed-shift normalization concern raised by the earlier source search. It does not supply the physical parameter whose variation yields \(-a_\omega\).

The real delta load is excluded as that parameter, even though it preserves causality and unitarity. This says nothing general against other geometric, distributed, or additional-channel deformations. In particular, fitting a frequency-dependent load to the target would move the unresolved arithmetic input into the coupling rather than derive it.

A next bounded investigation should first classify which independently specified changes of asymptotic geometry or field content can alter the high-frequency power continuously. Only candidates that pass that necessary condition should be tested against the first-prime tangent and pole residues. The exact one-form model is the reference system for those comparisons. No such deformation is constructed in this note.

## 8. Numerical correction and validation scope

While differentiating the prime-free kernel, we found a shared implementation error in the earlier WZW and Brownian diagnostic programs. The mathematical convolution formula stated in the notes was correct:

\[
q_\omega(u)=\frac{2\pi^\omega}{\Gamma(\omega)}
e^{-(5/2-\omega)u}(1-e^{-2u})^{\omega-1},\quad
k_\omega^<(u)=q_\omega(u)-2\omega\int_0^u
e^{(1/2-\omega)(u-v)}q_\omega(v)dv.
\]

After the substitution \(v=u z^{1/\omega}\), the exponential inside the correction integral must be \(e^{-(3-2\omega)v}\). Both programs had used \(e^{-2v}\), which is correct only at \(\omega=1/2\). We corrected both implementations and replayed their full suites: all 60 bounded-readout controls (13 exact rational) and all 51 Brownian floating controls still pass.

The corrected forward cell response in the WZW audit is 0.11571873508141131, replacing 0.11569708485331016. The Brownian note's scaled arithmetic first-delay values become 0.1071750107 and 0.1075136697. The Brownian native response, exact moment formulas, analytical smoothness exclusions, and leading arithmetic singularities are unaffected. The changed records and audits explicitly mark this correction.

An independent expression used for regression is

\[
k_\omega^<(u)=\frac{2\pi^\omega}{\Gamma(\omega)}
\left[e^{-(5/2-\omega)u}z^{\omega-1}
-\omega e^{(1/2-\omega)u}B_z(\omega,3/2-\omega)\right],
\qquad z=1-e^{-2u}.
\]

The new diagnostic compares both corrected sibling implementations against this incomplete-beta formula at shifts 1/4, 2/5 and 1/2, including points away from the singular origin. It also integrates the general kernel independently against its Laplace factor. These checks specifically address the shared error; earlier comparisons concentrated on leading singularities or half shift could not reliably detect it.

All 65 new controls pass: 5 exact rational primitive-residue counts and 60 floating controls. They cover constant terms, channel norm factors, pole cancellation, kernel transforms, finite-window energy, independently solved load matching equations, passivity, tangents, first-delay asymptotics, illustrative poles, and corrected-kernel regressions. Python 3.10.0, mpmath 1.3.0 and NumPy 1.25.1 were used, with 50 decimal digits for the mpmath calculations and 65 for the window refinement. NumPy regressions retain ordinary double precision.

These are finite diagnostics, not interval certificates or an independent mathematical review. Program and sibling hashes are stored in the record. The earlier parent WZW/arithmetic records and all manuscript TeX/PDF artifacts remain unchanged. This note is a research addendum, not a revised manuscript.
