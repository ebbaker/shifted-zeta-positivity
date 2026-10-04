# Priorities for height adapted zero detection

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. The exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model analysis and internal cross-review are not independent
specialist refereeing.

Status: research assessment with elementary deductions, one application of an
existing exponential-polynomial inequality, and proposed next theorems.
No new arithmetic saving, complete finite detector, or zero-free region is
proved. Broader novelty of the deductions has not been established.

The best next investigation is a quantitative detector with Gaussian
localization, developed alongside an arithmetic formula centered at the
carrier frequency. The existing unit-box coefficient bound can be strengthened
to a common-sector bound, which gives a useful finite-cluster baseline.
The main unresolved costs are the other zeros, physical convolution tails,
and the complete signed arithmetic estimate. These should determine the
target height and prime scale before substantial numerical work begins.

This assessment reads all three files in this investigation and the linked
natural-bound assessment, arithmetic closure, finite cross-spectrum,
approximation, short-interval, large-value, and certificate programs. The
existing [overview](README.md), [detector lemmas](DETECTOR_LEMMAS_20261004.md),
and [research map](RESEARCH_DIRECTIONS_20261004.md) remain the starting records.

## Recommended order of work

| Priority | Investigation | Concrete next output | Decision criterion |
| --- | --- | --- | --- |
| 1 | Gaussian localization and cluster detection | A conditional exclusion theorem with a continuous log-prime-scale interval, explicit threshold, guard band, multiplicities, and every remainder | The full detection budget remains smaller than the candidate zero response |
| 1 in parallel | Arithmetic reduction centered at the carrier | One exact complex signed correlation with uniform spectral truncation, continuum, endpoint, and comparison costs | The arithmetic parameter range overlaps the detector interval |
| 2 | Classical calibration | A moving-carrier comparison using current finite zero-free regions and certified zero heights | A proposed saving improves exclusion beyond its actual inputs |
| 3 | Several probes or local energy | A cluster lower bound that explicitly charges interval location and length | It survives positive-multiplicity cancellation tests without a hidden separation assumption |
| Bounded alternative | Hardy approximation with real dilations | An explicit local norm criterion with an approximation dictionary that resolves the oscillation | The dictionary passes the approximation-floor test below |
| Defer pending a new mechanism | Large values and zero proportions | An amplification or observable-transfer theorem | It produces more than an allowed isolated exception or bridges the distinct correlations |

The first two items should proceed together. A detector whose physical norm
requires an unavailable arithmetic estimate is not a useful interface.
Classical calibration is a control for both, and is not a source of a new
arithmetic saving.

## The coefficients occupy a common sector

**Elementary deduction.** In the existing rectangle, a fixed rotation makes
the real part of every coefficient positive:

\[
\operatorname{Re}\{-i\operatorname{sgn}(t)D_t(\beta+i\gamma)\}>1/8,
\qquad |t|\ge100,\quad 3/4\le\beta\le1,\quad |\gamma-t|\le1.
\tag{1}
\]

Here and below use the existing normalization of \(D_t\). Put
\(a=\beta-1/2\), \(\nu=\gamma-t\), and \(z=-a-i\gamma\).
The three factors of \(z(z^2-1/4)\) have real parts
\(-a,-a-1/2,1/2-a\). Their product lies within angle
\(3/(2|\gamma|)\le1/66\) of \(i\operatorname{sgn}(t)\), since
\(|\gamma|\ge99\) and \(\operatorname{sgn}(\gamma)=\operatorname{sgn}(t)\).
The positive-weight integral \(H(-a-i\nu)\) lies within angle \(1/4\)
of the positive real axis. The shell integral
\(K(\beta+i\nu)=\int_1^2 y^{\beta+1}e^{i\nu\log y}\,dy\)
lies within angle \(\log2\). Thus the rotated coefficient has argument
of modulus at most \(1/4+\log2+1/66<1\). The proved modulus bound
\(|D_t|>1/4\), together with \(\cos1>1/2\), proves (1).

This controls the sum at log scale zero for a finite cluster. It does not
control its phases at the large log scales where prime information is used.

**Application of an existing theorem.** Let \(\rho_j=\beta_j+i\gamma_j\)
be any finite nonempty set of distinct points in that rectangle, with positive
integer multiplicities \(m_j\), and define

\[
P(y)=\sum_{j=1}^n m_jD_t(\rho_j)
             e^{(\rho_j-1-it)y},\qquad M=\sum_jm_j.
\]

Suppose \(\beta_j\ge b\ge3/4\), put
\(w=\max_j\beta_j-\min_j\beta_j\), and take \(u\ge0,L>0\).
The Turan--Nazarov inequality gives, for an absolute constant \(C\ge1\),

\[
\sup_{u\le y\le u+L}e^{(1-b)y}|P(y)|
\ge \frac M8 e^{-wL/2}
       \left(\frac{L}{C(u+L)}\right)^{n-1}.
\tag{2}
\]

For verification, apply the inequality on \([0,u+L]\) and its subinterval
\([u,u+L]\) to \(e^{(1-a_*)y}P(y)\), where
\(a_*=(\min\beta_j+\max\beta_j)/2\). Its exponents have real parts
bounded in modulus by \(w/2\), and (1) gives \(|P(0)|>M/8\).
Multiplication by \(e^{(a_*-b)y}\), which on the subinterval is at least
\(e^{(a_*-b)u}\), cancels the \(u\) part of the exponential loss.
No simplicity, zero separation, or rightmost-zero assumption is used.

The primary theorem is Nazarov's
[Local estimates for exponential polynomials](https://www.mathnet.ru/eng/aa397).
The precise version used here is also stated in
[Bownik--Speegle, Theorem 2.1](https://pages.uoregon.edu/mbownik/papers/51.pdf).
The constant \(C\) has not been made numerical here. Equation (2) is a
finite-cluster statement. To use it for zeta, every other zero and the
trivial-zero remainder must be charged separately. This includes zeros
with \(\beta<b\) inside the same unit height band; proximity to the real
boundary does not give an automatic negligible remainder.

The dependence on \(u/L\) matters. Two formal zeros of the same real part
at ordinates \(t\pm\delta/2\), with \(\delta=\pi/u\), have opposite
phases at \(y=u\). Smoothness of the exact coefficients on the rectangle
then makes their combined response on \([u-L/2,u+L/2]\) only
\(O_h((1+L)/u)\) times their common exponential size for large \(u\).
This is a positive-multiplicity diagnostic, not an assertion about the actual
zeta zeros. Any fixed finite family of nearby carriers must charge this
interval-location cost as well. Identical points add multiplicity; they do
not create this cancellation by themselves.

## Why Gaussian localization deserves priority

**Elementary tail deduction with nonnumerical constants.** Write
\(T=1+|t|\). The coefficient upper bound in the detector note and the
standard unit-height zero count, with multiplicity, imply

\[
\sum_{|\gamma-t|>R}m_\rho|D_t(\rho)|
\ll_h
\begin{cases}
\log(2T)R^{-9}+T^{-9}\log(2T),&1\le R\le T,\\
T^{-3}R^{-6}\log(T+R),&R\ge T.
\end{cases}
\tag{3}
\]

Indeed the coefficient is bounded by
\(C_h(1+|\gamma-t|/T)^3(1+|\gamma-t|)^{-10}\).
Sum unit bins up to distance \(T\), then use the residual seventh-power
decay beyond that scale. The local zero count supplies the logarithms.

Without an additional real-part gap, normalizing on \([u,u+L]\) costs
\(e^{(1-b)(u+L)}\). A sufficient budget based on (3), in the range
\(R\le T\), therefore involves

\[
R\gtrsim
\left(\frac{\log(2T)e^{(1-b)(u+L)}}{A}\right)^{1/9},
\tag{4}
\]

where \(A\) is the desired normalized detection threshold; the far-tail
term must also be paid. This explains why the existing unit-box coefficient
lemma and an absolute tail estimate do not close the detector.
If \(u\) is a large multiple of \(\log T\), the sufficient guard band
can be much larger than one. This is a limitation of that estimate,
not an impossibility theorem for local detection.

**Promising inverse-multiplier scout.** Local inversion can plausibly retain
the central coefficient advantage. On a vertical line
\(\sigma\in[3/4,1-\epsilon_0]\), with fixed \(0<\epsilon_0\le1/4\),
the existing no-off-axis-zero property of \(H\), its endpoint expansion,
and the preparation polynomial give

\[
|D_t(\sigma+i(t+\nu))|^{-1}
\ll_{h,\epsilon_0}(1+|\nu|)^{13},\qquad |t|\ge100.
\tag{5}
\]

The factors are a ninth-power inverse bound for \(H\), a first-power
inverse shell bound, and at most a third-power loss from
\(T^3/(1+|t+\nu|)^3\). The last ratio is bounded by
\(C(1+|\nu|)^3\). Compactness controls the remaining finite frequency
range. Consequently a Gaussian-weighted vertical inverse norm is uniformly
bounded in the carrier for Gaussian parameter bounded below. The analytic
Gaussian \(e^{k(s-it)^2}\) also contributes \(e^{k\sigma^2}\) on this
line, so a complete test must keep its dependence on \(k\).

Equation (5) uses nonexplicit compactness constants and the inherited
transform property. It is not a physical inverse-test theorem. The next
scout should construct the physical kernel, bound its convolution tails,
and charge the finite initial cap. Division restores the known pole at one;
contour shifts must include it. Uniformity as \(\epsilon_0\to0\) is not
claimed. These checks decide whether an inverse Gaussian is better than
direct weighted cluster detection.

[Schlage-Puchta's finite-interval PNT detector](https://arxiv.org/html/1912.00853)
remains a useful model for the Gaussian and power-sum argument. Its prime
scale can be \(\gamma^{12000\epsilon^{-3}}\), and its exposed-zero
replacement can move the height substantially. Its constants and locality
cannot be imported into this prepared observable. Develop the finite-cluster
baseline (2), then compare a Gaussian inverse with a direct weighted version
before selecting the full detector architecture.

## Center the arithmetic spectrum at the carrier

**Exact deduction.** Factor out the oscillation before estimating derivatives.
Define

\[
A_t(v)=\frac{-h'''(v)-3it h''(v)+(3t^2+1/4)h'(v)
                     +i(t^3+t/4)h(v)}{N_t},
\qquad a_t(u)=u^{-1/2}A_t(-\log u).
\]

Then exactly

\[
w_t(u)=u^{-it}a_t(u),\qquad
\ell_t(u)=u^{-it}L_t(u),\qquad
L_t(u)=\int_1^2 y\,a_t(u/y)\,dy.
\tag{6}
\]

The carrier phases in the shell integration cancel. The coefficients of
\(h,h',h'',h'''\) in \(A_t\) are uniformly bounded because
\(N_t\gg_h(1+|t|)^3\). Thus the available amplitude derivative bounds,
including the sixth measure derivative of \(a_t\) and the seventh of the
shell amplitude, can be made uniform in \(t\).

Put \(B_t(z)=\int L_t(u)u^{z-1}\,du\). The cofactor spectral multiplier
corresponding to the [finite cross-spectrum](../programs/01_signed_arithmetic_covariance/FINITE_CROSS_SPECTRUM_20261004.md)
is

\[
W_t(\xi)=\zeta(1+i\xi)B_t(1+i(\xi-t)),\qquad
|B_t(1+i\nu)|\ll_h(1+|\nu|)^{-7}.
\tag{7}
\]

For \(|\xi|\ge1\), this gives
\(|W_t(\xi)|\ll_h\log(2+|\xi|)(1+|\xi-t|)^{-7}\).
At \(\xi=0\) the zeta pole is removable, since
\(B_t(1-it)=\int\ell_t=0\); the derivative of \(B_t\) controls the
continued value. The natural truncation is \(|\xi-t|\le B\).
After \(\xi=t+\nu\), both finite arithmetic factors carry the twists
\((n/U)^{-it}\) and \((p/U)^{-it}\). Mean-square bounds insensitive to
coefficient phases can then be applied in the centered variable.

This should be the first arithmetic deliverable. Equation (7) is a kernel
deduction, not the complete uniform reduction or a saving for its signed
integral. Poisson comparison still sees the physical oscillation, and the
complex integral has no automatic negative-frequency conjugacy. Retain
the exact continuum \(c_tK(1-it)\), every strict cutoff and terminal block,
and the signed product rather than replacing it by an absolute square.

**Conditional bookkeeping gates.** The inherited scalar comparison suggests
\(U_V=V_V\asymp\sqrt{X/T}\,r^{1/14}\), so even nontrivial cutoffs require
\(X\gtrsim T r^{-1/7}\). Extending the existing complementary-divisor
deletion naively suggests
\(D\asymp X^{1/2}T^{-3/2}r^{3/14}\); requiring \(D\ge1\) imposes
\(T\lesssim X^{1/3}r^{1/7}\). Dropping inner prime powers with the existing
\(U^{-1/2}\log X\) bound separately imposes

\[
T\lesssim X r^{29/7}(\log X)^{-4}.
\tag{8}
\]

These are proposed-extension budgets, not intrinsic detector barriers.
For \(r=X^{-\delta}e^{-\mathcal L_{\rm det}}\), the exponent of \(X\)
in (8) is \(1-29\delta/7\), already negative at \(\delta=1/4\).
Begin with the full von Mangoldt observable and full divisor band.
Deleting prime powers or divisors is useful only when its actual cost fits.
This avoids imposing optional bookkeeping losses on the first theorem.

## Update the classical comparison before choosing targets

The literature control needs a newer input. Theorem 1 of
[Bellotti--Trudgian--Yang, March 2026](https://arxiv.org/html/2603.21490v1)
proves zero exclusion for \(t\ge3\) and
\(\sigma>1-1/(4.896\log t)\). The same paper records the explicit
Littlewood width \(\log\log t/(21.233\log t)\) and the
Korobov--Vinogradov width with constant 53.989. Compare their union in
the actual target range. Its stronger 4.8594 statement invokes Yang's
thesis improvements; audit that input before adopting it in a finite budget.
This update does not invalidate the notes' separate asymptotic 48.0718 input.

[Platt--Trudgian](https://arxiv.org/abs/2004.09765) rigorously establish RH
through height \(3\cdot10^{12}\). This is a verified lower benchmark,
not a claim that no later extension exists. The 2026 source explicitly
uses this height. Boxes to the right of the critical line wholly below it
provide calibration cases rather than new exclusion.

A useful forward comparison to prove is

\[
|\lambda_t(X)|\ll_h
\log(2T)X^{-\eta(2T)}+T^{-9}\log(2T)
                +E_{\rm trivial}(X,t),
\tag{9}
\]

for a valid decreasing established zero-free width \(\eta\), with all
constants and starting ranges evaluated. Split the zeros into a central
band of width comparable to \(|t|\) and its complement; (3) controls
the latter. Equation (9) is a proposed complete calibration theorem here.
Any application needs the uniform explicit formula and the trivial-zero
budget. A candidate larger width \(\delta>\eta(t)\) produces a smaller
single-zero scale \(X^{-\delta}\), so the classical central estimate alone
does not rule it out.

The 2026 paper also offers a bounded structural scout: test whether a
combination or integral of the prepared probes has reflection-pair positivity
in its zero kernel. A positive answer could simplify cluster handling.
Preparation gives a signed kernel, so such positivity must be derived for
the actual observable and its restored pole. Keep the gamma background,
of order \(\log t\), in the budget. Kernel optimization by itself is a
classical comparison until a new arithmetic input is identified.

## Close the integer shifted Hardy scout before optimization

**Elementary obstruction for a specified dictionary.** Consider the local
target \(\phi_t(x)=x^{-it}\) and approximants in the original integer
dictionary spanned by \(\rho_{1/n}\). Every approximant is constant on
\(I_k=(1/(k+1),1/k)\). In \(L^2(x^{2b-1}dx)\), even the unrestricted
space of functions constant on those bins has approximation error

\[
Q_b(t)=\frac1{2b}-\sum_{k\ge1}\frac{|q_k(t)|^2}{m_k},\quad
m_k=\frac{k^{-2b}-(k+1)^{-2b}}{2b},\quad
q_k(t)=\frac{k^{-2b+it}-(k+1)^{-2b+it}}{2b-it}.
\tag{10}
\]

Consequently every finite integer-dictionary error is at least \(Q_b(t)\),
regardless of its coefficients or length. For fixed \(b>0\), dominated
convergence gives \(Q_b(t)\to1/(2b)\): each bin mean tends to zero, and
\(|q_k|^2/m_k\le m_k\), whose sum is finite.

The shifted Mellin error is
\(1/(s-it)-\zeta(s)P(s)/s\), with \(P(1)=0\). At a zero it equals
\(1/(\rho-it)\), so a sufficient certificate for
\(\beta\ge\beta_0\), \(|\gamma-t|\le\Delta\), is

\[
\|\phi_t-f\|_b^2<\frac{2(\beta_0-b)}{1+\Delta^2}.
\tag{11}
\]

For fixed \(0<b<\beta_0<1\), this threshold is strictly below
\(1/(2b)\), because \(4b(\beta_0-b)\le\beta_0^2<1\).
Thus this sufficient certificate cannot be attained by the integer
dictionary for sufficiently large carrier height, even with unbounded
coefficient count.

There is an explicit check in the present detector range. At \(b=1/2\),
for every integer \(K\ge1\),

\[
Q_{1/2}(t)\ge1-\frac1{K+1}
          -\frac{4K+K/(K+1)}{1+t^2}.
\tag{12}
\]

This follows by the triangle inequality on the first \(K\) bin integrals
and the projection bound \(|q_k|^2/m_k\le m_k\) on the tail.
Taking \(K=9\), \(|t|\ge100\) gives \(Q_{1/2}(t)>0.896\).
For \(\Delta=1\), the threshold in (11) is at most \(1/2\) for
\(\beta_0\le1\). The integer-only shifted-target route therefore fails
this sufficient norm test already throughout the unit-box carrier range.

This does not rule out real dilations, a different target, or a different
certificate. It makes real dilations the appropriate bounded alternative
scout, and prevents a large coefficient optimization from pursuing an
unattainable norm. The original unshifted finite certificate remains valid
with its existing height penalty.

## The first complete deliverable

The next theorem should state that any zero in a specified box forces one
of a specified family of observables to exceed a computable threshold on
a specified continuous interval. Its hypotheses should include an arithmetic
upper bound only for the exact full observable, with every comparison and
tail error already included. The theorem should allow multiplicities and
arbitrarily close zeros, and specify any enlarged height band.

Before extensive numerics, prove or disprove that the Gaussian inverse
has affordable physical tails and that the centered arithmetic formula has
a compatible range. Then state one independent arithmetic inequality that
beats the updated classical calibration. The arithmetic closure audit shows
that coherent zero modes survive the exact identities; separate Mertens
and prime-error estimates do not remove that obligation.

Small positive-multiplicity cluster tests and the existing capped arithmetic
harness can falsify candidate inequalities. A successful sample cannot
replace the continuous interval, remote-zero, continuum, or interpolation
budgets. No target height, power saving, or large sweep is selected here.
