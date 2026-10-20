# Internal review: the general nonnegative-kernel arithmetic barrier

20 October 2026. Prepared for **Edward Baker** with substantial LLM
assistance, **gpt-6-astra (Codex), reasoning effort ultra**, verified from
recorded metadata. Separate same-model internal checks of [Note 11][note];
no specialist review or novelty claim.

**Verdict: pass.** The full-tail argument extends from positive Fejér mixtures to every admissible kernel in Note 08: `h>=0`, `h(0)=1`, the declared quadratic strip decay, and compact Fourier support. No mixture representation, restriction on `I Delta`, or sign restriction on Fourier coefficients is required. The leading complete-envelope conclusion retains Note 08's explicit gamma and pole budgets. The unrestricted prime-payment counterexamples remain valid because the resulting lower bound jointly prices prime payment and a logarithmic moment.

## 1. Continuous Gram representation and the exact formula

Let `I=int h`, `phi(v)=int h(x)e^(-2pi ivx)dx`, and

\[
d\mu(x)=h(x)\,dx/I,\qquad
S(u)=\int e^{-iux}\,d\mu(x)=\phi(u/2\pi)/I.
\]

Then `mu` is a probability measure, `|S|<=1`, and `S(u)=0` for `|u|>B=2pi Delta`. Define the finite logarithmic pair moment

\[
\mathcal M=\iint\log(2+|x-y|)\,d\mu(x)d\mu(y).
\tag{R1}
\]

Its finiteness follows from the quadratic real-axis decay, since `log(2+|x-y|)<=log(2+|x|)+log(2+|y|)`.

For `A>=2`, `B>=A`, let `chi_A` vanish below `A-1` and equal one above `A`. Let `theta_B` equal one through `B` and vanish above `B+1`, using fixed smooth transition profiles with values in `[0,1]`. Put

\[
F(u)=\chi_A(u)e^{u/4}\theta_B(u),\qquad
J(u)=e^{-u/2}F(u).
\]

Both are smooth and compactly supported, and

\[
\|J\|_1+\|J''\|_1\ll e^{-A/4}
\tag{R2}
\]

uniformly in `B>=A`. The upper transition contributes `O(e^(-B/4))`; it introduces no bandwidth loss.

The primary exact formula is [Tao, *246B Notes 4*, Exercise 22(iii)](https://terrytao.wordpress.com/2021/02/12/246b-notes-4-the-riemann-zeta-function-and-the-prime-number-theorem/), applied at real frequency `t` to `eta_t(x)=x^(-1-it)F(log x)`. Under RH, the complete nontrivial-zero term is a sum of Fourier transforms of `J` at `tau-t`, with full multiplicities. Two integrations by parts and the complete local zero count give, for every real `t`,

\[
\sum_\rho\left|\int J(u)e^{i(\tau-t)u}du\right|
\ll e^{-A/4}\log(2+|t|).
\tag{R3}
\]

Integrate the exact identity at `t=x-y` against `mu(x)mu(y)`. Equation (R3) and (R1) justify exchanging the entire zero sum with the double integral by absolute convergence. The prime sum is finite; the main integral is compactly supported and bounded; and the complete trivial-zero integral has an absolute bound independent of `t`. These facts justify all other exchanges. No restriction on the support of `mu`, the number of mixture components, or the size of `t` is needed.

The resulting identity compares the positive quantities

\[
\sum_{n\ge2}\frac{\Lambda(n)}n F(\log n)|S(\log n)|^2
\quad\hbox{and}\quad
\int F(u)|S(u)|^2du
\]

with absolute error `O(e^(-A/4) M)`. The trivial term is absorbed because `M>=log 2`.

## 2. Full prime-power payment and the uniform tail bound

Let the standard universal absolute payment be

\[
C=\frac1\pi\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
       |\phi(\log n/2\pi)|.
\]

Since `|S|^2<=|S|`, the prime-power Gram sum is at most `pi(C/I)e^(-(A-1)/4)`. This retains every prime power. Since `S=0` beyond `B`, the upper cutoff equals one everywhere relevant. Consequently

\[
\int_A^B e^{u/4}|\phi(u/2\pi)|^2du
\ll e^{-A/4}(IC+I^2\mathcal M),
\]

and weighted Cauchy--Schwarz gives

\[
\boxed{\int_A^\infty|\phi(u/2\pi)|du
\ll e^{-A/4}\sqrt{IC+I^2\mathcal M}.}
\tag{R4}
\]

This estimate is independent of the bandwidth. If `B<A`, its left side vanishes and the separate Poisson mass bound handles that case.

## 3. Joint exponential cost

The pointwise Poisson inequality from Note 08 is

\[
\sum_{n\ge1}|\phi(nv)|\ge\frac{1/v-I}{2}.
\]

For `0<I<=1/4`, integrate on `a=1/I-1` to `b=1/I-1/2`. The lower integral is

\[
\frac12\left[\log\frac{1-I/2}{1-I}-\frac I2\right]
\ge\frac{3I^2}{16}.
\]

The overlap weight after changing variables is at most `1+log(b/a)`, so `int_a^infinity |phi(v)|dv` is bounded below by an absolute constant times `I^2`. In (R4) take `A=2pi a`. The ordinary mass-bandwidth inequality `I Delta>=1` ensures `B>A`. Squaring and rearranging proves, for an absolute positive constant `c`,

\[
\boxed{C+I\mathcal M\ge c I^3\exp(\pi/I).}
\tag{R5}
\]

The factor `exp(-pi)` from `A/2=pi/I-pi` is absorbed into `c`. This is a joint cost, not an unrestricted exponential lower bound on `C` alone.

## 4. Gamma budget and the complete leading constant

Let `L=log(gamma/(2pi))` and use Note 08's

\[
g_\gamma(x)=\Re\psi\!\left(\tfrac14+
                      \tfrac{i(\gamma+x)}2\right)-\log\pi.
\]

Uniformly in real `x`, `g_gamma(x)=log(2+|gamma+x|)+O(1)`. Hence

\[
\begin{aligned}
\log(2+|x-y|)
&\le\log2+\max\{\log(2+|\gamma+x|),\log(2+|\gamma+y|)\}\\
&\le L+O(1)+|g_\gamma(x)-L|+|g_\gamma(y)-L|.
\end{aligned}
\]

The explicit absolute gamma budget `int h|g_gamma-L|<=epsilon_gamma L I` therefore gives

\[
\boxed{\mathcal M\le(1+2\epsilon_\gamma)L+O(1).}
\tag{R6}
\]

For a competing complete envelope, the gamma and pole budgets imply `I=O(1/log L)` and `C=O(L/log L)`. In (R4), taking `A=2log L` then gives tail `O(1/log L)=o(1)`. Averaging Poisson over `[a,(1+epsilon)a]`, where `a=A/(2pi)`, yields `liminf aI>=1`. Equivalently, (R5)--(R6) exclude `I<=c/log L` for every fixed `c<pi` along a competing sequence. Thus

\[
U\ge\left(\frac12-o(1)\right)\frac L{\log L}.
\]

The already checked Fejér construction attains this leading value within the same complete-budget class. The barrier is therefore sharp at leading order for that class. It is an arithmetic cost of the universal absolute-payment method, not an opposing signed estimate, a zero exclusion, or a result assuming simple zeros.


## 5. Further checks and unchanged research gates

The coordinating agent derived the full-tail consumer and checked the
continuous-measure extension. A further same-model audit independently
verified the normalization, the stable Poisson factor two, the support
edge, all powers of I in the joint inequality, and compatibility with
the translated examples. No derivative of h or its transform enters
the absolute constant; its only distribution-dependent payment is the
displayed logarithmic pair moment.

The final note's sharper moment bound (G12) follows from the maximum of
the two shifted logarithms, rather than their sum. The lower bound is
sequential with the stated vanishing budgets. Sharpness uses the existing
centered Fejér sequence; a uniform infimum over varying kernels would
require uniform budgets. The power I^3 and the unspecified positive
constant in (G14) are not claimed optimal.

A separate check of continuing the short-log-zeta estimate toward the
critical line produced no useful opposing sign. At horizontal distance
c/log t its declared approximation allowance does not tend to zero.
No assertion that this defeats every analytic-continuation method is
made, and the failed attempt is not counted as a further research result.

The existing 265 exact-rational fixtures were unchanged and not rerun:
they do not test this infinite analytical argument. No numerical sign
scan, new zero certificate, manuscript or snapshot was created.
The [progress register][progress] keeps the positive signed estimate,
strict cap surplus and all-zero conclusion open.

[note]: ../notes/11_FULL_ABSOLUTE_PRIME_ENVELOPE_AND_LOGARITHMIC_SPREAD_20261020.md
[progress]: ../research-progress/01_RH_TO_SIMPLICITY_PROGRESS_20261020.md
