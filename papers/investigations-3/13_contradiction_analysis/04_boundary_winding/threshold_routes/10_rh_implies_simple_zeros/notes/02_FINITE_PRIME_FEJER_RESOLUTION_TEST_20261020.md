# Bounded continuation: a finite-prime Fejér formula and its absolute-payment barrier

20 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra, reasoning effort ultra**, as recorded by the parent session. Separate same-model analytical derivation and [internal review](../reviews/02_FIRST_ANALYTICAL_ROUND_REVIEW_20261020.md); no specialist review.

**Status:** the exact finite-prime formula and the optimized asymptotic of the declared absolute-payment envelope are proved below. The envelope recovers the classical \(\log \gamma/\log \log \gamma\) multiplicity scale and does not yield simplicity. This supplies a valid finite-prime alternative to the inadmissible critical-strip continuation of an absolutely convergent Euler series. No novelty is claimed for the explicit-formula method or the classical multiplicity scale.

This bounded continuation follows [Note 01](01_FINITE_WALLS_ARITHMETIC_RESOLUTION_AND_GAUSSIAN_SCREEN_20261020.md), the [result index](../../../../../../../result-summaries/README.md), [collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md), and [avoid index](../../../../../../../avoid/README.md), especially its [reformulation](../../../../../../../avoid/01_restating_the_target.md), [control-premise](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scope](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [source-checking](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md) rules. It does not reopen a numerical campaign.

## 1. Exact formula, with complete gamma and pole terms

Use the Fourier convention \(\widehat h(v)=\int h(u)e^{-2\pi iuv}\,du\). For \(\Delta>0\), define
\[
 K_\Delta(v)=\left(\frac{\sin(\pi\Delta v)}{\pi\Delta v}\right)^2,
 \qquad h_{\Delta,\gamma}(u)=K_\Delta(u-\gamma).
\]
Then
\[
 \widehat h_{\Delta,\gamma}(v)
 =\frac1\Delta(1-|v|/\Delta)_+e^{-2\pi i\gamma v}.
\]
This entire function \(h\) is real and nonnegative on the real axis, has value one at \(\gamma\), and decays quadratically along each fixed horizontal strip. It satisfies the hypotheses of Goldston--Gonek, [*A note on S(t) and the zeros of the Riemann zeta-function*, Lemma 1](https://arxiv.org/pdf/math/0511092), the Guinand--Weil formula. Specialization gives, under RH,
\[
 S_\Delta(\gamma):=\sum_\lambda m_\lambda K_\Delta(\lambda-\gamma)
 =G_\Delta(\gamma)+P_\Delta(\gamma)-Q_\Delta(\gamma),          \tag{1}
\]
where every term is retained:
\[
 G_\Delta(\gamma)=\frac1{2\pi}\int_\mathbb R
 K_\Delta(u-\gamma)
 \left[\Re\psi(1/4+iu/2)-\log\pi\right]du,
\]
\[
 P_\Delta(\gamma)=h_{\Delta,\gamma}(i/2)
                  +h_{\Delta,\gamma}(-i/2),
\]
\[
 Q_\Delta(\gamma)=\frac1{\pi\Delta}
 \sum_{2\le n\le X}\frac{\Lambda(n)}{\sqrt n}
 \left(1-\frac{\log n}{\log X}\right)\cos(\gamma\log n),
 \qquad X=e^{2\pi\Delta}.                                  \tag{2}
\]
The summand at \(n=X\), if any, is zero. The sign of the prime sum is part of the identity. The formula is finite in the primes because the Fourier transform has compact support, not because the prime Dirichlet series is continued to the critical line.

At a zero ordinate, RH gives \(m(\gamma)\le S_\Delta(\gamma)\). Thus a proved strict bound
\[
 Q_\Delta(\gamma)>G_\Delta(\gamma)+P_\Delta(\gamma)-2          \tag{3}
\]
would exclude multiplicity at that ordinate. This is an unachieved signed estimate. Its existence without a scale rule is again only a simplicity reformulation: \(S_\Delta(\gamma)\to m(\gamma)\) as \(\Delta\to\infty\), by isolation and the summable reciprocal-square tail.

## 2. The declared absolute-payment class

Pay the prime sum by absolute values and the two pole terms by their moduli:
\[
 C_\Delta=\frac1{\pi\Delta}
 \sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
 \left(1-\frac{\log n}{\log X}\right),
\quad
 E_\Delta(\gamma)=|h(i/2)|+|h(-i/2)|,
\]
\[
 U_\Delta(\gamma)=G_\Delta(\gamma)+E_\Delta(\gamma)+C_\Delta.
                                                                    \tag{4}
\]
Then \(m(\gamma)\le S_\Delta(\gamma)\le U_\Delta(\gamma)\). No zero term or signed remainder has been suppressed; G is the exact complete gamma integral. We study this envelope for all \(\Delta\ge1\).

Three estimates determine its best possible asymptotic.

**Gamma term, uniformly in every \(\Delta\ge1\).** Set \(L_\gamma=\log(\gamma/(2 \pi))\). As \(\gamma\to\infty\),
\[
 G_\Delta(\gamma)=\frac{L_\gamma}{2\pi\Delta}
 +O\left(\frac{\log\gamma}{\Delta\sqrt\gamma}\right).        \tag{5}
\]
For a direct proof, put \(v=u-\gamma\) and split at \(|v|=\sqrt{\gamma}\). On the inner interval the digamma expansion gives
\(\Re\psi(1/4+iu/2)-\log \pi=L_\gamma+O(\gamma^{-1/2})\), and the total kernel mass is \(1/\Delta\). On the complement use
\[
 K_\Delta(v)\le(\pi\Delta v)^{-2},\qquad
 |\Re\psi(1/4+iu/2)-\log\pi|\ll\log(2+|u|).
\]
Integrating the tail, including the subtraction of the main constant, costs \(O(\log \gamma/(\Delta^2 \sqrt{\gamma}))\); the displayed estimate follows. The constants are absolute, and the argument is uniform even when \(\Delta\) depends on \(\gamma\). The elementary gamma bounds can also be obtained from the periodic-Bernoulli representation used in the Poisson note.

**Prime payment.** By the ordinary prime number theorem in the form \(\sum_{n\le x} \Lambda(n)\sim x\), partial summation yields
\[
 \sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}
 \left(1-\frac{\log n}{\log X}\right)
 \sim\frac{4\\sqrt X}{\log X}\qquad(X\to\infty).
\]
Indeed replacing the Chebyshev measure by \(du\) produces exactly
\[
 \int_1^X u^{-1/2}\left(1-\frac{\log u}{\log X}\right)du
 =\frac{4\\sqrt X}{\log X}-2-\frac4{\log X}.
\]
The weight is nonnegative and decreasing. Partial summation and the PNT make the error \(o(\sqrt X/\log X)\); split first at a fixed large lower cutoff to make the relative PNT error uniformly small. Hence
\[
 C_\Delta\sim\frac{2e^{\pi\Delta}}{\pi^2\Delta^2}
 \qquad(\Delta\to\infty).                                  \tag{6}
\]
The PNT is the only arithmetic asymptotic needed for this payment estimate; see [DLMF, distribution of primes](https://dlmf.nist.gov/25.16.i) for the named classical input.

**Pole payment.** Directly from the sine formula,
\[
 E_\Delta(\gamma)
 \le\frac{2\cosh^2(\pi\Delta/2)}
 {\pi^2\Delta^2(\gamma^2+1/4)}.                             \tag{7}
\]
No favorable sign is assumed.

## 3. The optimized envelope diverges

Equations (5)--(7) imply the quantitative scoped result
\[
 \boxed{\inf_{\Delta\ge1}U_\Delta(\gamma)
 =\left(\frac12+o(1)\right)
   \frac{\log\gamma}{\log\log\gamma}
 \quad(\gamma\to\infty).}                                 \tag{8}
\]
For the upper bound choose \(\Delta=(\log L_\gamma)/\pi\). The gamma term is \(L_\gamma/(2 \log L_\gamma)\), the prime payment is asymptotic to \(2 L_\gamma/(\log L_\gamma)^2\), and the pole payment is negligible. These are all complete payments for the declared envelope.

For the lower bound fix any \(\epsilon>0\). If
\(1\le\Delta\le(1+\epsilon)\log L_\gamma/\pi\), (5), together with the nonnegative payments, gives
\[
 U_\Delta(\gamma)\ge(1-o(1))
 \frac{L_\gamma}{2(1+\epsilon)\log L_\gamma}.
\]
If \(\Delta>(1+\epsilon)\log L_\gamma/\pi\), (6) bounds the prime payment below by a fixed positive multiple of
\(L_\gamma^{1+\epsilon}/(\log L_\gamma)^2\): the function \(\exp(\pi \Delta)/\Delta^2\) is increasing in this range, and the asymptotic lower bound in (6) is uniform once its argument exceeds a fixed threshold. This is much larger than \(L_\gamma/\log L_\gamma\). Formula (5) is positive uniformly for large \(\gamma\). Let \(\epsilon\) tend to zero after taking the asymptotic lower limit. This proves (8).

Thus this complete absolute-payment strategy cannot produce an all-height bound below two. Optimizing the bandwidth does not fix the loss. The leading scale agrees with the historical RH multiplicity estimate in Goldston--Gonek, Corollary 1; it is not a new multiplicity theorem or a claim about current best constants.

The conclusion is confined to (4), this squared-sinc kernel, and \(\Delta\ge1\). It does not exclude signed estimates of (2), other kernels, zero deflation, or use of additional event-conditioned information. In particular the **exact** quantity S can tend to one at a simple zero even though its absolute-payment upper envelope has the divergent optimum (8).

## 4. Exact arithmetic control test

Let \(\ell=\log p\) and use the endpoint Euler-factor control. Its added ordinates form the lattice \((2k+1)\pi/\ell\), each with multiplicity two. Center at one added ordinate \(\gamma_k\). On the control's own zero data, the added contribution is exactly
\[
 S_{\Delta,p}(\gamma_k)-S_\Delta(\gamma_k)
 =2\sum_{j\in\mathbb Z}K_\Delta(2\pi j/\ell)\ge2.           \tag{9}
\]
This admits a fully finite arithmetic check. Put \(N=2 \pi \Delta/\ell\). The conductor term contributes \(\ell/(\pi \Delta)\). The logarithmic coefficients at \(p^r\) change by
\(2 \ell (-1)^{r-1}p^{r/2}\); at \(\gamma_k\), the phase cosine is \((-1)^r\). Thus the minus-signed prime term contributes a positive amount and the exact total difference is
\[
 \frac{\ell}{\pi\Delta}
 \left[1+2\sum_{1\le r\le N}\left(1-\frac rN\right)\right]
 =2\left[1+\frac{\{N\}(1-\{N\})}{N^2}\right]\ge2.        \tag{10}
\]
The term at an integral endpoint is zero. This agrees with Poisson summation of (9), including the factor two for multiplicity. Equality holds when \(N\) is an integer; strictness is not inserted incorrectly. Unlike the desired strict upper bound below two, the control carries its required double mass at every bandwidth.

Equations (1)--(10) pay all prime, pole and gamma contributions. They close one further bounded estimating branch while leaving a precise signed task: obtain a genuine estimate of Q at a declared bandwidth which beats the actual gamma-and-pole allowance in (3), under the putative event, without assuming simplicity. Such a bound, a cap surplus, and a negative Gaussian deficit remain unproved.

A concrete scale comparison: choosing \(\Delta=c \log \gamma\) with fixed \(c>0\) makes the gamma term tend to \(1/(2 \pi c)\) and sets the finite prime horizon at \(X=\gamma^{2 \pi c}\). Its absolute prime payment is asymptotic to
\[
 \frac{2\gamma^{\pi c}}{\pi^2c^2(\log\gamma)^2},
\]
so an order-one bound requires substantial signed cancellation. Making the gamma term alone less than two corresponds to \(c>1/(4 \pi)\) and hence a horizon larger than \(\gamma^{1/2}\). This last comparison is not a necessary condition for every signed strategy: at smaller bandwidth a favorable Q might cancel a larger gamma term.
