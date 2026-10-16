# The Markov part of the transfer and what can realize it: opening note

**Author: Claude Fable 5.1 (Anthropic), model `claude-fable-5-1`.** 17 September
2026 (New York). Opening note of the Loewner investigation, written at Edward
Baker's direction after the
[Wilson-lines note of the same day](../../wilson-lines/notes/LOEWNER_AND_THE_MARKOV_DECOMPOSITION_20260917.md)
from which this folder was opened. That note is inherited whole and not
repeated; its Section 4 (the decomposition $K_\omega=R_\omega\widetilde K_\omega$
with $\widetilde K_\omega$ completely monotone) is the object this investigation
is about, and its Section 6 (the ranked first computation) is what this note
carries out, corrects in one place, and replaces.

**Nothing here is a construction. No positivity is proved, nothing assumes the
Riemann hypothesis, and no gauge theory or conformal system is matched.**

---

## 0. Summary

1. **The Beta part is Bessel additivity.** The archimedean transfer
   $K^\Gamma_\omega(p)=\pi^\omega\Gamma(\frac{s-\omega}2)/\Gamma(\frac{s+\omega}2)$
   is $\pi^\omega\frac{\Gamma(a/2)}{\Gamma(b/2)}\,\mathbb E\,U^{p/2}$ with
   $U\sim\mathrm{Beta}(\frac a2,\omega)$, $a=\frac12-\omega$, $b=\frac12+\omega$,
   and $U\stackrel d=Z_a/(Z_a+Z_{2\omega})$ for independent squared Bessel
   processes of dimensions $a$ and $2\omega$ started at $0$, whose sum is a
   squared Bessel process of dimension $b$ (Shiga--Watanabe). So the
   archimedean delay is the fraction of a dimension-$(\frac12+\omega)$ Bessel
   square carried by a dimension-$(\frac12-\omega)$ component, and the two
   exponents $a,b$ of the pole factor are the two Bessel dimensions
   (Proposition 1.1). This is a Bessel-process statement, not yet a Loewner one.

2. **A Loewner chain cannot produce the comb, in either reading of the
   variables.** If the arithmetic coordinate is Loewner time, the transfer is a
   linear time-invariant causal filter and the only such filter a
   rotation-invariant chain induces on analytic observables is the pure delay
   (Lemma 3.1 of the inherited note). If the arithmetic coordinate is the radial
   coordinate, the chain's transport of exterior points is a pure delay in the
   far field, $\log|g_t(z)|=\log|z|-t+O(|z|^{-1})$, so a translation-invariant
   induced kernel equals its far-field limit $\delta_{-t}$ (Proposition 2.1).
   Echoes at the fixed separations $\log n$ with $y$-independent weights are
   available in neither reading. **The comb is a semigroup structure**: the
   operator $\sum_n\widetilde c_n\,\mu_n$ with $\mu_n f(x)=f(x-\log n)$,
   $\mu_n\mu_m=\mu_{nm}$, a Dirichlet series in the multiplicative semigroup
   $\mathbb N^\times$ acting by dilations on the ray --- the Hecke/Bost--Connes
   structure the Wilson-lines manuscript's Section 10.4 already pointed at. What
   Loewner or Bessel processes can supply is the archimedean factor alone.

3. **The pole factor is forced by unimodularity; the "two marked-point
   coefficients" are not free, and the previous note's Section 6 is corrected
   accordingly.** $R_\omega$ is the unique rational function, unimodular on the
   imaginary axis and tending to $1$ at infinity, that cancels the two poles and
   two zeros of $\Lambda(s-\omega)/\Lambda(s+\omega)$ at the poles of $\Lambda$
   (Proposition 3.1). Its residues $-4\omega(\frac12\pm\omega)$ carry no
   information beyond the positions $s\mp\omega\in\{0,1\}$ of the poles of
   $\zeta$ and $\Gamma(u/2)$ and the shift. The arithmetic is where it always
   was, in the poles of $\widetilde K_\omega$ at the zeros of $\Lambda(s+\omega)$;
   the previous note's expectation that a realization would "fail at two
   numbers" was wrong, because those numbers are fixed by the functional
   equation once the Markov part is given.

4. **A cleaner decomposition: one all-pass section at the pole of $\zeta$.**
   $K_\omega=B_b\,\widehat K_\omega$ with $B_b(p)=\frac{p-b}{p+b}$ a first-order
   Blaschke factor and
   $\widehat K_\omega=\frac{p+a}{p-a}\,\frac{\Lambda(s-\omega)}{\Lambda(s+\omega)}
   =\frac{s-\omega}{s+\omega-1}\frac{\Lambda(s-\omega)}{\Lambda(s+\omega)}$
   **completely monotone** on $p>b$ (Proposition 3.2). At the kernel level
   \[
    k_\omega=\widehat k_\omega-2\,\mathrm{EMA}_b[\widehat k_\omega],\qquad
    \mathrm{EMA}_b[g](x)=b\int_0^xe^{-b(x-y)}g(y)\,dy,\qquad \widehat k_\omega\geq0 :
   \]
   the transfer kernel is a positive measure minus twice its exponential
   moving average at rate $b=\frac12+\omega$. The subtraction removes the
   $e^{bx}$ growth of $\widehat k_\omega$ exactly and unconditionally (the pole
   of $\zeta(s-\omega)$ at $s-\omega=1$, the prime number theorem's main term),
   and what is left decays if and only if the zeros allow it: the dichotomy of
   the Wilson-lines manuscript's Proposition 7.2 at the level of the kernel.

5. **The endpoint $\omega=\frac12$ is the modular surface, exactly and in every
   piece.** There $a=0$, $\widehat K_{1/2}=\widetilde K_{1/2}=\Lambda(p)/\Lambda(p+1)$,
   which is the Eisenstein scattering matrix $\varphi(s')=\Lambda(2s'-1)/\Lambda(2s')$
   of $PSL(2,\mathbb Z)\backslash\mathbb H$ at $p=2s'-1$; the comb weights are
   Euler's totient, $\widetilde c_n=\varphi_{\rm Euler}(n)/n$, the coset count of
   the cusp's Fourier expansion; the Beta part degenerates; and
   $K_{1/2}=B_1\varphi=\frac{p-1}{p+1}\varphi$ is the scattering matrix with its
   pole at $s'=1$ removed by one Blaschke factor, which is the Lax--Phillips
   modification. So **the Markov part of the transfer is, at the endpoint, a
   classical geometric scattering system, and the comb is its coset sum.** For
   $\omega<\frac12$ no Eisenstein construction produces the offset $2\omega$
   (constant terms have unit offsets in $2s'$), so the interior of the family
   has no such realization from that source.

6. **What this investigation is, then.** Not a positivity mechanism: by the
   dichotomy, any structural positivity of $\widehat V_\omega$ says nothing
   about the contraction of $B_b(\partial)\widehat V_\omega$ compressed, which is
   the zero-free strip. It is three things. A **computational tool**: the
   transfer, its compression, its norm, its defect and its cumulative Cayley
   coordinate are now assembled exactly from elementary functions and the
   integers $n<e^L$ (Section 4 of the inherited note, §4.2(a)), and the
   contraction side of the programme can be measured as the form side has been.
   A **dictionary**: Bessel additivity for the archimedean factor, the Hecke
   semigroup for the comb, one Blaschke factor at the pole of $\zeta$ for the
   correction, and the modular surface at the endpoint. And a **statement of the
   criticality in filter language**: the shifted Weil transfer is a lossless
   filter whose impulse response is a positive measure minus twice its
   exponential moving average, and the Riemann hypothesis is the statement that
   this filter is stable at every $\omega>0$ --- passivity of every finite
   window. Section 5 ranks what to do with that.

---

## 1. The Beta part is Bessel additivity

Write $a=\frac12-\omega$, $b=\frac12+\omega$, $s=\frac12+p$.

> **Proposition 1.1.** Let $U\sim\mathrm{Beta}(\frac a2,\omega)$, equivalently
> $U=Z_a/(Z_a+Z_{2\omega})$ where $Z_\delta$ denotes an independent
> $\mathrm{Gamma}(\frac\delta2)$ variable --- the value at any fixed time, up to
> the common factor $2t$, of a squared Bessel process $\mathrm{BESQ}^{(\delta)}$
> started at $0$. Then
> \[
>  K^\Gamma_\omega(p)=\pi^\omega\,\frac{\Gamma(\frac a2)}{\Gamma(\frac b2)}\,\mathbb E\big[U^{p/2}\big],
>  \qquad\text{and}\qquad
>  Z_a+Z_{2\omega}\stackrel d=Z_b .
> \]
> The archimedean delay is $x=-\frac12\log U$, i.e. $(r_1/r_2)^2=U$.

*Proof.* $\mathbb E\,U^{p/2}=B(\frac a2+\frac p2,\omega)/B(\frac a2,\omega)
=\frac{\Gamma(\frac a2+\frac p2)\Gamma(\frac a2+\omega)}{\Gamma(\frac a2+\omega+\frac p2)\Gamma(\frac a2)}$,
and $\frac a2+\frac p2=\frac{s-\omega}2$, $\frac a2+\omega=\frac b2$,
$\frac a2+\omega+\frac p2=\frac{s+\omega}2$. The Gamma--Beta algebra
$G_\alpha/(G_\alpha+G_\beta)\sim\mathrm{Beta}(\alpha,\beta)$ and the additivity
$G_\alpha+G_\beta\sim G_{\alpha+\beta}$ are classical; for BESQ the additivity in
dimension is Shiga--Watanabe. The pull-back of the Beta density to $x$ is the
kernel $k^\Gamma_\omega$ of the inherited note (check 4 of
`decomposition_checks.py`). $\square$

Three remarks. The two Bessel dimensions $a$ and $b$ are the two exponents
$e^{ax}$, $e^{-bx}$ of the pole factor: one set of numbers, $\frac12\pm\omega$,
because both come from $s\pm\omega$ and the $\frac12$. The dimensions are
fractional and below one, so there is no sphere and no angle; the Beta variable
is the additivity fraction, and its "$\frac14$" at $\omega=0$ is half of the
dimension $\frac12$. And this is a statement about Bessel processes, which drive
radial Loewner chains but are not themselves Loewner chains; whether a
conformal-radius or hitting law of a radial chain has this Beta form is the one
question in this direction that remains open (Section 5, item 3).

## 2. A Loewner chain cannot produce the comb

The inherited note's Section 3 already showed (Lemma 3.1) that if the
arithmetic coordinate is Loewner time, the only linear time-invariant filter a
rotation-invariant chain induces on analytic observables is the pure delay. The
other reading takes the arithmetic coordinate to be the radial coordinate
$\log|z|$ and asks whether the chain's transport of points induces the kernel.

> **Proposition 2.1 (far-field transport is a pure delay).** Let $K_t$ be a
> whole-plane Loewner hull of logarithmic capacity $t$, deterministic or random,
> with any number of tips, and $g_t:\hat{\mathbb C}\setminus K_t\to\hat{\mathbb C}\setminus\overline{\mathbb D}$
> its normalized map, $g_t(z)=e^{-t}z+O(1)$. Then
> $\log|g_t(z)|=\log|z|-t+O(|z|^{-1})$ uniformly in the argument of $z$. Hence
> if the induced transition kernel $P_t(y,dy')$ from $y=\log|z|$ to
> $y'=\log|g_t(z)|$ (averaged over the argument of $z$ and over the chain's law)
> is translation-invariant in $y$, it is $\delta_{y'=y-t}$. In particular no
> Loewner chain induces a translation-invariant radial kernel with atoms at
> $y'=y-\log n$, $n\geq2$.

*Proof.* The normalization at infinity is the definition of the capacity
parametrization; translation invariance forces $P_t(y,\cdot)$ to equal its
$y\to\infty$ limit. $\square$

Away from the far field the kernel depends on the distance to the hull and is
not translation-invariant, and in either case $t\mapsto g_t(z)$ is continuous
for a càdlàg driving function (the Loewner equation is an ODE whose field is
smooth in $g$ away from the circle), so a jump of the driving process --- a
Lévy-driven chain --- moves the tip, not the transported points. The comb's
atoms at fixed separations $\log n$ with $y$-independent weights are not a
Loewner phenomenon in any reading.

**What the comb is.** On functions of the arithmetic coordinate let
$\mu_nf(x)=f(x-\log n)$. Then $\mu_n\mu_m=\mu_{nm}$, the $\mu_n$ are isometries,
and the comb operator is
\[
 C_\omega=\sum_{n\geq1}\widetilde c_n\,\mu_n,\qquad
 \widetilde c_n=n^{-1/2}\big(n^{\omega}*\mu(n)n^{-\omega}\big)
 =n^{\omega-\frac12}\prod_{p\mid n}(1-p^{-2\omega}),
\]
a Dirichlet series in the multiplicative semigroup $\mathbb N^\times$ with
completely multiplicative-convolution coefficients: the Hecke algebra of
$\mathbb N^\times$ acting on the ray by dilations, which is the Bost--Connes
structure. Section 10.4 of the Wilson-lines manuscript said the prime atoms
require "a structure invariant under $r\mapsto\lambda r$ but distinguishing the
ratios $p^m$" and named Bost--Connes; the decomposition says exactly which
element of that algebra the transfer contains, with which coefficients, at each
shift. Its local factor at $p$, $\frac{1-p^{-\omega}z_p}{1-p^{\omega}z_p}$ with
$z_p=e^{-s\log p}$, is a one-delay feedback loop of gain $p^{\omega}$, the
abelian monodromy of the inherited note's §4.2(e).

## 3. The pole factor is forced, and the cleaner decomposition

### 3.1 Forcedness

> **Proposition 3.1.** $\widetilde K_\omega=\Lambda(s-\omega)/\Lambda(s+\omega)$
> has, apart from its poles at the zeros of $\Lambda(s+\omega)$, exactly two
> poles, at $p=b$ and $p=-a$ (the poles of $\Lambda(s-\omega)$ at $s-\omega=1,0$),
> and exactly two zeros, at $p=a$ and $p=-b$ (the poles of $\Lambda(s+\omega)$).
> Among rational functions $\rho$ with $|\rho(i\tau)|=1$ and $\rho(\infty)=1$,
> the unique one of minimal degree such that $\rho\widetilde K_\omega$ is
> holomorphic and nonvanishing at these four points is
> $\rho=R_\omega=\frac{(p+a)(p-b)}{(p+b)(p-a)}$.

*Proof.* A rational function unimodular on the axis is a product of factors
$\frac{p-c}{p+\bar c}$; cancelling the pole at $b$ needs the factor
$\frac{p-b}{p+b}$, whose own pole at $-b$ is cancelled by the zero of
$\widetilde K_\omega$ there; cancelling the pole at $-a$ needs $\frac{p+a}{p-a}$,
whose pole at $a$ is cancelled by the zero there. Any further factor introduces
an uncancelled pole or zero. $\square$

So, given the Markov part, the correction is determined by the functional
equation. The residues $-4\omega(\frac12+\omega)$ and $-4\omega(\frac12-\omega)$
of the inherited note's §4.2(c) are not data a realization could get right or
wrong; a realization that produced $\widetilde V_\omega$ and respected
unimodularity would produce $V_\omega$, and the contraction of its compressions
would then be the zero-free strip by the dichotomy. The previous note's
Section 6 located the expected failure in "the two endpoint coefficients"; that
was wrong, and this note withdraws it. There is no small place where the
arithmetic hides. It is in the poles of $\widetilde K_\omega$ at the zeros, and
nowhere else.

### 3.2 One all-pass section

> **Proposition 3.2.** With $B_b(p)=\frac{p-b}{p+b}$ and
> $\widehat K_\omega(p)=\frac{p+a}{p-a}\,\widetilde K_\omega(p)
> =\frac{(s-\omega)\Lambda(s-\omega)}{(s+\omega-1)\Lambda(s+\omega)}$,
> one has $K_\omega=B_b\widehat K_\omega$, and $\widehat K_\omega$ is completely
> monotone on $p>b$. Hence $\widehat k_\omega\geq0$ and
> \[
>  k_\omega=\widehat k_\omega-2b\,\big(e^{-b\,\cdot}\mathbf 1_{>0}\big)*\widehat k_\omega
>  =\widehat k_\omega-2\,\mathrm{EMA}_b[\widehat k_\omega],
>  \qquad
>  \widehat k_\omega=\widetilde k_\omega+2a\,\big(e^{a\,\cdot}\mathbf 1_{>0}\big)*\widetilde k_\omega .
> \]

*Proof.* $\frac{p+a}{p-a}=1+\frac{2a}{p-a}$ is completely monotone on $p>a$, and
a product of completely monotone functions is completely monotone;
$\widetilde K_\omega$ is completely monotone on $p>b>a$ by the inherited note's
Proposition 4.2. $B_b=1-\frac{2b}{p+b}$ gives the kernel identity. $\square$

The reading. $\widehat k_\omega$ is a positive measure that grows like
$C_\omega e^{bx}$ with $C_\omega=\big(2\omega\Lambda(1+2\omega)\big)^{-1}\to1$
as $\omega\downarrow0$: the residue of the pole of $\zeta(s-\omega)$, which is the
prime number theorem's main term in the comb ($\sum_{n\leq N}\widetilde c_n\sim
N^{b}/(b\,\zeta(1+2\omega))$) smoothed by the Beta kernel. The exponential moving
average at rate $b$ maps $Ce^{bx}$ to $\frac C2(e^{bx}-e^{-bx})$, so
$g-2\,\mathrm{EMA}_b[g]$ sends $Ce^{bx}$ to $Ce^{-bx}$: the subtraction kills the
main term exactly and unconditionally and leaves a decaying piece, and what
remains of $k_\omega$ is the fluctuation of $\widehat k_\omega$ about its main
term --- the zeros. $k_\omega$ cannot be nonnegative, since that would make every
compression a contraction and prove a strip; the inherited note's Section 5 shows
the sign changes at every $\omega$ computed. $B_b$ itself is a lossless
first-order all-pass section, kernel $\delta_0-2be^{-bx}\mathbf 1_{>0}$, unitary
and causal on $L^2(\mathbb R)$, and its compression to $I_L$ is a contraction; by
multiplicativity of truncation $V_{\omega,L}=(P_LB_bP_L)(P_L\widehat V_\omega P_L)$,
which bounds $\lVert V_{\omega,L}\rVert$ by $\lVert\widehat V_{\omega,L}\rVert>1$
and is therefore useless for contraction --- the cancellation between the two
factors is the whole content, as it must be.

### 3.3 The endpoint $\omega=\frac12$

At $\omega=\frac12$: $a=0$, $b=1$, $\frac{p+a}{p-a}=1$, so
$\widehat K_{1/2}=\widetilde K_{1/2}=\Lambda(p)/\Lambda(p+1)$, and with $p=2s'-1$
this is the Eisenstein scattering matrix $\varphi(s')=\Lambda(2s'-1)/\Lambda(2s')$
of the modular surface, whose pole at $s'=1$ is $p=b=1$. The comb weights are
$\widetilde c_n=\prod_{p|n}(1-p^{-1})=\varphi_{\rm Euler}(n)/n$, the density of
reduced fractions with denominator $n$ --- the count of cosets in the cusp's
Fourier expansion that produces $\zeta(2s'-1)/\zeta(2s')$ in the first place.
The Beta part degenerates ($\mathrm{Beta}(0,\frac12)$; $k^\Gamma_{1/2}(x)=2(1-e^{-2x})^{-1/2}$
does not decay, the pole of $K^\Gamma_{1/2}$ at $p=0$). And
$K_{1/2}=B_1\varphi=\frac{p-1}{p+1}\varphi$: the transfer at the endpoint is the
Eisenstein scattering matrix with its pole at $s'=1$ removed by one Blaschke
factor, which is exactly what Lax--Phillips do when they pass to the
orthocomplement of the constant function. All of this is checked in
`decomposition_checks.py` (group 3). So the Markov part of the transfer has, at
the endpoint, a classical geometric realization in which the comb is a coset
sum and the correction is the removal of the residual spectrum; the Beta part
is absent there because $a=0$. For $\omega<\frac12$ Eisenstein constant terms
give only unit offsets in $2s'$, so the interior of the family is not realized
by any congruence-subgroup scattering matrix; that is the same statement the
review made and it is not changed here.

## 4. Numerics

`numerics/exploratory/decomposition_checks.py` (mpmath, 30 digits, record
`decomposition_checks_omega0.1.json`), at $\omega=0.1$:

| group | what | result |
|---|---|---|
| 1 | $(-1)^k\widehat K^{(k)}_\omega(p)>0$, $k\leq6$, $p\in\{0.8,1,2\}$ | all positive |
| 2 | $K_\omega=B_b\widehat K_\omega$ at five complex $p$ | rel. $2.0\times10^{-31}$ |
| 3 | $\widetilde K_{1/2}(p)=\varphi(\frac{p+1}2)$, $\widehat K_{1/2}=\widetilde K_{1/2}$, $K_{1/2}=B_1\varphi$; $\widetilde c_n|_{\omega=1/2}=\varphi_{\rm Euler}(n)/n$ for $n<200$ in exact rationals | rel. $1.0\times10^{-31}$; all equal |
| 4 | $K^\Gamma_\omega=\pi^\omega\frac{\Gamma(a/2)}{\Gamma(b/2)}\mathbb E\,U^{p/2}$ by Beta moments and by the Gamma-ratio form; the Beta density pulls back to $k^\Gamma_\omega$ at three $x$ | rel. $3.9\times10^{-31}$ |
| 5 | $k_\omega=\widehat k_\omega-2\,\mathrm{EMA}_b[\widehat k_\omega]$ against the $R_\omega$ assembly of `transfer_kernel.py`, at $x\in\{0.2,0.5,0.9,1.3\}$; $\widehat k_\omega>0$ there | abs. $2.0\times10^{-31}$; $\widehat k_\omega=1.52,1.45,1.78,2.23$ |
| 6 | $\widetilde c_n/(2\omega\Lambda(n)n^{-1/2})$ at $\omega=0.01$ for $n=2,3,5,7$; $\widetilde c_6/\omega^2$ | $1.00001$--$1.00006$; $1.2436$ against $4\log2\log3/\sqrt6=1.2436$ |

`transfer_kernel.py` and its record are the living copies of the inherited
note's programme (checks A--G, all passing at $\omega\in\{0.02,0.1,0.25\}$).

## 5. What to do, ranked

1. **Register the elementary assembly and measure the contraction side.**
   Port the kernel of the inherited note's §4.2(a) --- $k^\Gamma_\omega$, the comb
   for $n<e^L$, and $B_b$ --- to a registered, standard-library programme, and
   compute $\lVert V_{\omega,L}\rVert$, $\lambda_{\min}(D_{\omega,L})$ and the
   cumulative Cayley coordinate at the three recorded horizons
   $L\in\{\log3,\log5,\log7\}$ and a range of $\omega$. Two things to test:
   whether $\lambda_{\min}(D_{\omega,L})/(2\omega)\to m_L$ as $\omega\downarrow0$
   with the recorded margins, which validates the whole chain from kernel to
   form; and how the contraction margin $1-\lVert V_{\omega,L}\rVert$ behaves at
   finite $\omega$ --- the cumulative criterion's own margin, which the earlier
   shifted-zeta programme could only reach through an $\omega^2$ expansion on a
   far-right line. Run the phase-matched Gram control of the review on it. This
   is the one item that is purely computational and cannot fail to inform.
2. **Write the Lax--Phillips dictionary at $\omega=\frac12$ exactly**, object by
   object: which subspace the compression $P_L$ is, what the flux identity is in
   their energy form, and what their semigroup estimate says about the
   contraction margin of item 1 at the endpoint. Then say precisely which of
   their objects the $\omega$-deformation moves and which it cannot reach.
3. **The Beta law from a radial chain.** Determine whether a conformal-radius or
   hitting law of radial Loewner evolution driven by a Bessel process of
   dimension $b=\frac12+\omega$ has the additivity fraction of Proposition 1.1 as
   a squared radius ratio. If yes, the archimedean factor has a Loewner
   realization and its parameter $\frac14$ is a Bessel dimension; if no, the
   archimedean factor is a Bessel-process statement and not a Loewner one, and
   the folder's name is a misnomer to record rather than a direction to pursue.
4. **The Hecke comb as an operator.** Write $C_\omega=\sum\widetilde c_n\mu_n$ in
   the Bost--Connes algebra and identify it: it is the image of
   $\zeta(s-\omega)/\zeta(s+\omega)$ under the representation
   $n^{-s}\mapsto\mu_n$, with the $n^{-1/2}$ making the representation unitary
   on $L^2(dx)$. Ask what the KMS structure of that algebra says about the
   compression $P_LC_\omega P_L$, whose norm grows like $e^{bL}$, and whether the
   subtraction $2\,\mathrm{EMA}_b$ has a meaning there. This is a reading task
   with a small chance of a real statement.
5. **The criticality in filter terms.** The transfer is a lossless filter with
   impulse response $\widehat k_\omega-2\,\mathrm{EMA}_b[\widehat k_\omega]$,
   $\widehat k_\omega\geq0$; RH is its stability at every $\omega>0$. Ask
   whether any passivity theorem for filters of the form "positive measure minus
   twice its EMA" exists that does not go through the location of the poles.
   I expect not, by the dichotomy, and a clean statement of *why* not --- what
   property of $\widehat k_\omega$ beyond positivity would be needed --- would
   be the honest end of this line.

## 6. What not to redo

- Do not look for the comb in a Loewner chain, single- or multi-tip,
  deterministic or Lévy-driven, in either variable identification (Section 2).
- Do not treat the pole-factor residues as data (Section 3.1).
- Do not expect structural positivity of $\widehat V_\omega$ to bound
  $\lVert V_{\omega,L}\rVert$ (Section 3.2).
- Do not compute $V_{\omega,L}$ from $K_\omega$ on a far-right Laplace line; the
  elementary kernel is exact and cheaper.

## 7. Status of every statement

- **Written proof, unconditional:** Propositions 1.1, 2.1, 3.1, 3.2 and the
  identities of §3.3.
- **Labelled numerical computation (unregistered, mpmath):** Section 4.
- **Reading:** the Lax--Phillips remarks of §3.3 and item 2 of Section 5; the
  Bost--Connes identification of §2 beyond the algebra written out; the
  Shiga--Watanabe reference.
- **Corrected here:** the inherited note's Section 6, which expected a
  realization to fail "at two numbers"; those numbers are forced (§3.1).
- **Not claimed:** a realization of the transfer, a contraction, a positivity
  statement, or anything about the zeros.

See the [notes index](README.md) and the [investigation index](../README.md).
