# Separate same-model review: coherent remote-gap saturation

20 October 2026. Prepared for **Edward Baker** with LLM assistance by **gpt-6-astra, reasoning effort ultra**. Three separate same-model analytic work streams checked the construction, the spline/leakage estimates, and the full completion and scope; the integrating agent rechecked the final text. This is internal LLM review, not specialist review or a novelty claim. Starting checkout: `1020b3e`.

Review target: [Note 13 §9](../notes/13_CERTIFIED_GAP_SIGNED_POLYNOMIAL_KERNELS_20261020.md).

**Verdict: the proposed fixed-base construction is valid.** It can reduce a complete absolute-prime envelope to the base test's exact signed zero sum with a quantitative error. It supplies no upper bound for that signed sum below two, and does not improve on directly retaining the base test's signed prime coefficients. The former separate-payment obstruction does not cover this coherent construction.

The [result index](../../../../../../../result-summaries/README.md), [avoid index](../../../../../../../avoid/README.md), and specifically [avoid01](../../../../../../../avoid/01_restating_the_target.md), [avoid07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [avoid12](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) determine the interpretation below.

## 1. Uniform Fourier sign and all-zero leakage

Fix `gamma>g=1/8`, an integer `q>=2`, and `D=gamma²−g²`. The gap `|lambda|<=g` is established by Note13's elementary floor-integral proof. Assume RH for zero-side positivity. Let

\[
\ell_\delta(u)=\left(\frac{\sin(\pi\delta u)}{\pi\delta u}\right)^{2q},
\quad
r_\delta(x)=\frac{(x+\gamma)^2-g^2}{D}\ell_\delta(x+\gamma),
\quad \delta\gamma\in\mathbb Z_{>0}.
\tag{V1}
\]

The integer restriction gives `r_delta(0)=0`. Every actual zero offset has nonnegative `r_delta`, and its strip decay is at least quadratic.

Write `F_q` for the convolution density of `2q` copies of the indicator of `[-1/2,1/2]`; thus `hat ell_delta(v)=delta^-1 F_q(v/delta)`. The ratio `F_q''/F_q` is bounded below on its positive support. Indeed the outer unit intervals have positive second derivative, while the complementary compact core has a positive minimum of `F_q` and bounded continuous second derivative. Choose `K_q>=0` with `F_q''>=−K_q F_q`. Then

\[
\mathcal B_\delta(v)
=-\frac{\widehat\ell_\delta''(v)}{4\pi^2}
-g^2\widehat\ell_\delta(v)
\le-\frac{g^2}{2\delta}F_q(v/\delta)\le0
\tag{V2}
\]

once `delta²>=K_q/(2pi²g²)`. Support endpoints are included by continuity. On every fixed compact Fourier interval, `−B_delta(v)>=kappa/delta` for a positive constant `kappa` and all sufficiently large `delta`.

The transform is `hat r_delta(v)=D^-1 e^(2pi i gamma v) B_delta(v)`. Its height phase cancels exactly in the signed prime term, giving `Q_gamma(r_delta)=−C(r_delta)`, with every prime power retained. Its full zero sum obeys

\[
0\le S_\gamma(r_\delta)
\le\frac{Z_{q,g}}{D\delta^{2q}},\qquad
Z_{q,g}=\pi^{-2q}\sum_\lambda
 \frac{m_\lambda(\lambda^2-g^2)}{|\lambda|^{2q}}<\infty.
\tag{V3}
\]

The known gap bounds the denominator away from zero; the complete zero count gives convergence for `q>=2`. All multiplicities are present, including a hypothetical target multiple zero, whose contribution here vanishes.

## 2. Exact coherent residual

Let `f` be fixed, real, admissible and bandlimited, with `f(0)=1`. For the multiplicity interpretation require `f` nonnegative at every actual zero offset; a globally nonnegative base suffices. Define `U=G+P+C` with exact signed poles and `S=G+P−Q`, as in Note13 and [Goldston--Gonek, Lemma 1](https://arxiv.org/pdf/math/0511092).

For `h=f+a r_delta`, `a>0`, put at each prime-power frequency

\[
z_n=n^{-i\gamma}\widehat f(\log n/(2\pi)),\qquad
t_n=-\frac aD\mathcal B_\delta(\log n/(2\pi))\ge0.
\]

Outside the fixed Fourier support of `f` the modulus is exactly `t_n`. On its support `t_n>=a kappa/(D delta)`, and for `t_n>=2|z_n|`,

\[
0\le |z_n-t_n|-t_n+\Re z_n
=\frac{(\Im z_n)^2}{|z_n-t_n|+t_n-\Re z_n}
\le\frac{|z_n|^2}{t_n}.
\tag{V4}
\]

There are only finitely many relevant prime powers. Summing (V4), and combining the exact remote gamma, pole and prime terms before estimation, yields

\[
\boxed{
U_\gamma(f+a r_\delta)=S_\gamma(f)
 +aS_\gamma(r_\delta)+E_{\delta,a},\qquad
0\le E_{\delta,a}\le K_f\frac{D\delta}{a}.}
\tag{V5}
\]

Here one may take `K_f=kappa^-1 pi^-1 sum_(n<=X_f) Lambda(n)n^-1/2 |hat f(log n/(2pi))|²`, with the fixed base cutoff `X_f`. The condition `t_n>=2|z_n|` holds eventually for the choice below. Taking `a=D delta^(q+1/2)` along `delta gamma` integral gives

\[
0\le U_\gamma(f+a r_\delta)-S_\gamma(f)
\ll_{f,q,g,\gamma}\delta^{1/2-q}.
\tag{V6}
\]

The constants are for a fixed target and base. No uniform high-height or varying-base statement follows without additional bounds.

## 3. What is improved, and what is merely encoded

If the base has positive slack `C(f)+Q_gamma(f)>0`, (V6) gives a strict improvement over `U_gamma(f)` for sufficiently large `delta`. This is a genuine comparison of the stated complete envelopes. It does not produce a stronger zero-side majorant: `S(f+a r_delta)>=S(f)`. The coherent modulus asymptotically extracts `−Re z_n` for each original coefficient. Thus it recovers exactly the base's finite signed prime sum, rather than proving a new sign for that sum.

An explicit strict slack is available when `hat f>=0` and both its samples at `p` and `p²` are positive. Put `c1=(log p)/(pi sqrt p) hat f(log p/(2pi))` and `c2=(log p)/(pi p) hat f(log p/pi)`. With `x=cos(gamma log p)`, all remaining slack terms are nonnegative, so

\[
U_\gamma(f)-S_\gamma(f)\ge c_1(1+x)+2c_2x^2\ge\kappa,
\quad
\kappa=\begin{cases}
c_1-c_1^2/(8c_2),&c_1\le4c_2,\\
2c_2,&c_1>4c_2.
\end{cases}
\tag{V6a}
\]

Both values are positive. Taking the saturation error at most `kappa/2` proves `U_gamma(h)<=U_gamma(f)−kappa/2`. This prime-power relation is already among those retained in Note06's universal phase class; the displayed strict comparison is against the original absolute envelope, not a new arithmetic correlation bound or leading-height improvement. A full saturation may be numerically below a universal-phase envelope because it recovers the actual signed sum; the direct actual signed consumer still remains at least as strong.

The complete cancellation is quantitatively large. Exactly,

\[
P_\gamma(r_\delta)
=-\frac{2(g^2+1/4)}D
 \left[\frac{2\sinh(\pi\delta/2)}{\pi\delta}\right]^{2q}.
\tag{V7}
\]

Scaling the gamma integral gives `G_gamma(r_delta)=O_(q,g)(D^-1 delta^-1)`. From `Q(r)=−C(r)` and the complete formula,

\[
C(r_\delta)=-P_\gamma(r_\delta)-G_\gamma(r_\delta)+S_\gamma(r_\delta)
\sim\frac{2(g^2+1/4)}{D(\pi\delta)^{2q}}e^{q\pi\delta}.
\tag{V8}
\]

After multiplication by `a`, the opposing pole/prime terms have size `e^(q pi delta) delta^(1/2−q)`, while the final excess in (V6) is polynomially small. A literal evaluation has prime cutoff `exp(2pi q delta)` and must preserve that cancellation. This is not a lower bound on every evaluation algorithm: the known gap and exact formula permit symbolic cancellation. But that simplification leaves precisely `S(f)`, already available from the original fixed finite signed expression. No computational advantage is proved.

These kernels have negative real values in the known remote gap and a large negative exact pole contribution. They fall outside Note11's nonnegative-kernel and pole-budget hypotheses. They also fall outside Note13's separate-payment comparison. There is no conflict with either theorem.

One short scope consequence is exact: at a fixed actual ordinate of multiplicity `m`, the infimum of these envelopes over unbounded auxiliary bandwidth and pole magnitude is `m`. Indeed the bases `f_T(x)=sinc²(pi T x)` have `S_gamma(f_T)->m`, by dominated convergence with the complete all-zero majorant `min(1,1/(pi²x²))` for `T>=1`. For each fixed `T`, (V6) approximates that sum arbitrarily closely; conversely every admissible member has `U>=S>=m`. This limit estimates neither `m` nor a sufficient bandwidth, and is recorded only to delimit extension of Note11 to this signed class, not as a simplicity criterion.

## 4. Controls and goal relevance

The proof uses unchanged nonnegative von Mangoldt weights to turn (V2) into exact equality `Q(r)=−C(r)`, as well as the original complete zeta formula. The normalized positive-source control does not preserve that arithmetic; the ordinary-Dirichlet control does not preserve the reflected entire completion. Neither can be assigned both premises. Where a changed field has its own valid positive-weight explicit formula, the corresponding saturation argument must use that formula and its actual zero gap. It does not exclude a surviving double zero: the base zero sum still contains its mass two.

No bound `S_gamma(f)<2`, endpoint exclusion, or boundary-winding surplus has been obtained. The result is a quantitative fixed-base conversion of a coherent absolute envelope into the existing signed consumer, not a new simplicity criterion. Its useful conclusion is the exact separation between the earlier failed separate payment and this successful saturation of the already retained signed consumer.


## 5. Primary inputs and explicit quartic specialization

The stated strip-decay explicit formula and its Fourier normalization
were checked directly in [Goldston–Gonek, Lemma 1](https://arxiv.org/pdf/math/0511092).
The full zero count was checked in [Simonič, equation (1)](https://arxiv.org/pdf/1910.08274),
and the gamma-growth input in [DLMF 5.11.2](https://dlmf.nist.gov/5.11.E2).
No new estimate for zeta, prime phases or zero multiplicities is imported.

### Explicit quartic saturation constants: checked

The requested \(q=2\) constants and CS14a–CS14d pass, with the following derivations and scope.

#### Reciprocal-zero sum

The complete genus-one product, with the two logarithmic derivatives subtracted before summing, gives the absolutely convergent identity
\[
\frac{\xi'}{\xi}(1)-\frac{\xi'}{\xi}(0)
=\sum_\rho m_\rho\left(\frac1{1-\rho}+\frac1\rho\right)
=\sum_\rho\frac{m_\rho}{\rho(1-\rho)}.
\]
Functional symmetry makes the left side \(2\xi'(1)/\xi(1)\). Under RH, \(\rho=1/2+i\lambda\), so \(\rho(1-\rho)=\lambda^2+1/4\). Thus every positive and negative ordinate, with its full multiplicity, is counted in
\[
Z:=\sum_\lambda\frac{m_\lambda}{\lambda^2+1/4}
=2\frac{\xi'(1)}{\xi(1)}
=2+\gamma_E-\log(4\pi).
\tag{E1}
\]
For the last equality, logarithmic differentiation of the completion at \(1\), with its removable singularity combined, yields
\[
\frac{\xi'(1)}{\xi(1)}
=1+\gamma_E-\tfrac12\log\pi+\tfrac12\psi(1/2)
=1+\tfrac12\gamma_E-\tfrac12\log(4\pi).
\]
The completion and symmetry, Laurent constant at \(1\), and half-integer digamma value were directly checked in [DLMF 25.4.3–4](https://dlmf.nist.gov/25.4.E4), [25.2.4–5](https://dlmf.nist.gov/25.2.E4), and [5.4.13](https://dlmf.nist.gov/5.4.E13). There is no missing factor of two and no simplicity assumption.

#### Exact leakage constant

Set \(g=1/8\). For every \(t>0\),
\[
\frac{289}{64}-\frac{(t-1/64)(t+1/4)}{t^2}
=\frac{(1/t-30)^2}{256}\ge0.
\]
Consequently the tighter leakage constant, retaining its numerator, satisfies
\[
A:=\pi^{-4}\sum_\lambda
 m_\lambda\frac{\lambda^2-g^2}{\lambda^4}
\le\frac{289}{64\pi^4}Z.
\tag{E2}
\]
All summands of \(A\) are nonnegative under the stated zero-free gap. This bound is for that exact \(A\), not for the earlier coarser sum with numerator \(\lambda^2\).

#### Fixed-support lower bound and explicit error

For \(0\le s\le1\),
\[
F_2(s)=\frac23-s^2+\frac{s^3}{2},\qquad
F_2''(s)+3F_2(s)=\frac32s\{(s-1)^2+1\}\ge0.
\]
The outer pieces have nonnegative second derivative. At zero the ratio \(F_2''/F_2=-3\), so \(K_2=3\) is exact. Moreover \(F_2\) decreases on \([0,1/2]\), and \(F_2(1/2)=23/48\). Hence if
\[
\delta\ge2V,\qquad \delta^2\ge\frac3{2\pi^2g^2},
\]
then on the whole fixed support \(|v|\le V\),
\[
b_\delta(v)\ge\frac{g^2}{2D\delta}F_2(v/\delta)
\ge\frac{23g^2}{96D\delta}.
\tag{E3}
\]

Write \(c=23g^2/96\), \(M=\sup|\widehat f|\), and
\[
R_f=\sum_{\substack{n\ge2\\v_n\le V}}
\frac{\Lambda(n)}{\pi\sqrt n}|\widehat f(v_n)|^2.
\]
For \(a=D\delta^{5/2}\), the condition \(c\delta^{3/2}\ge2M\) is exactly the sufficient condition for the residual inequality on the active finite prime-power set. The leakage is at most \(A\delta^{-3/2}\), and the coherent residual is at most \(c^{-1}R_f\delta^{-3/2}\). Therefore
\[
0\le U_\gamma(f+a r_\delta)-S_\gamma(f)
\le
\left[A+\frac{96}{23g^2}R_f\right]\delta^{-3/2}
\le
\left[\frac{289Z}{64\pi^4}+\frac{96R_f}{23g^2}\right]\delta^{-3/2}.
\tag{E4}
\]
The target-normalization condition \(\delta\gamma\in\mathbb N\) remains necessary for the stated construction. All displayed constants are explicit, and the estimate retains every prime power in \(R_f\).

The additional prime-and-square strict margin CS14d also checks: minimizing \(c_1(1+x)+2c_2x^2\) on \([-1,1]\) gives \(c_1-c_1^2/(8c_2)\) if \(c_1\le4c_2\), and \(2c_2\) otherwise. Both are positive. This proves a strict improvement over the base absolute envelope once (E4) is below half that margin; it does not improve on or bound the exact signed zero sum.

The final CS12 statement requires t>0 and handles t=z=0 separately; the active finite-set application has t>0. No numerical sign scan or new certificate was used.
