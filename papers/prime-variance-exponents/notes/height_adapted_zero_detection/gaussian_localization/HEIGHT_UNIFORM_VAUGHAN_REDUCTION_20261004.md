# An explicit height-uniform full-Lambda Vaughan reduction

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration. Exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model cross-review is an internal check, not independent
specialist refereeing.

Status: effective derivative, lattice, and cutoff estimates for the
original prepared scalar. The signed arithmetic bound remains open. No
new zero exclusion or independent arithmetic power saving is claimed.

This complements the [direct Gaussian divisor reduction](FINITE_GAUSSIAN_MOBIUS_REDUCTION_20261004.md).
It makes the original continuous scalar gate effective, preserving the
Type-I continuum term, full von Mangoldt coefficients, and all product
endpoints. The direct Gaussian criterion remains the narrower first
arithmetic target.

## Definitions and regularity

Use the zero extension of \(h(v)=(1-16v^2)^8\) on \([-1/4,1/4]\),
\(T=|t|\ge100\), \(h_t(v)=e^{itv}h(v)\), and
\(N_t=\|-h_t'''+h_t'/4\|_2\). Put \(q=7/3\),
\(g_t=(-h_t'''+h_t'/4)/N_t\), and

\[
w_t(u)=u^{-1/2}g_t(-\log u),\qquad
\ell_t(u)=\int_1^2 y^{1-it}w_t(u/y)\,dy,\qquad
\lambda_t(X)=\frac1{qX}\sum_n\Lambda(n)\ell_t(n/X).
\tag{1}
\]

Their supports are \([A,B]\) and \([A,C]\), where
\(A=e^{-1/4}\), \(B=e^{1/4}\), and \(C=2B\).
The exact factorization is

\[
w_t(u)=u^{-1/2-it}A_t(-\log u),\quad
A_t(v)=\frac{-h'''-3it h''+(3t^2+1/4)h'+i(t^3+t/4)h}{N_t}.
\tag{2}
\]

Writing \(a_j=\|h^{(j)}\|_2^2\), expansion of the Fourier multiplier
gives

\[
N_t^2=T^6a_0+T^4(15a_1+a_0/2)
 +T^2(15a_2+3a_1+a_0/16)+a_3+a_2/2+a_1/16.
\]

The [preceding exact norm calculation](EXPLICIT_CONSTANTS_AND_FINITE_WINDOW_20261004.md)
gives \(\sqrt{a_0}>13/40\). Hence \(N_t>13T^3/40\), and the
sum of the absolute four coefficients in (2) is below four for \(T\ge100\).

For \(0\le m\le9\), the interior polynomial derivative satisfies

\[
\sup_{|v|<1/4}|h^{(m)}(v)|\le256\,64^m.
\]

Indeed expand \(h\) into its nine monomials and use
\((2j)_m\le16^m\), with terms of degree below \(m\) zero.
The zero extension has finite-measure derivatives through order nine.
Its ninth derivative has endpoint atoms from \(h^{(8)}\), each of
magnitude \(8^8 8!=676457349120\). For \(m\le8\), multiply the
interior bound by the interval length \(1/2\); for \(m=9\) its
interior mass is at most \(2^{61}\), and the atom pair is below
\(2^{41}\). Thus

\[
\|D^m h\|_{\rm TV}\le2^{62}\quad(0\le m\le9),\qquad
\|D^j A_t\|_{\rm TV}\le2^{64}\quad(0\le j\le6).
\]

The ordinary derivatives, interpreted as zero-extension measures at
the highest order, obey the Euler formula

\[
D_u^j w_t(u)=(-1)^j u^{-j-1/2-it}
 \prod_{l=0}^{j-1}(D_v+it+l+1/2)A_t(v),\qquad v=-\log u.
\]

Converting the norm to \(v\) contributes at most
\(e^{|j-1/2|/4}<4\) for \(j\le6\). The polynomial coefficient
sum is at most \(\prod_l(1+T+l+1/2)<2T^j\); the additional one
accounts for the coefficient of \(D_v\). Consequently

\[
\|D^j w_t\|_{\rm TV}\le2^{67}T^j,\qquad
\|D^j\ell_t\|_{\rm TV}\le3\,2^{67}T^j
\quad(0\le j\le6).
\tag{3}
\]

The shell bound uses \(\int_1^2y^{2-j}\,dy\le7/3<3\).
An additional derivative follows from the exact endpoint identity

\[
\ell_t'(u)=\frac{(2-it)\ell_t(u)}u
             +\frac{w_t(u)-2^{2-it}w_t(u/2)}u.
\]

Differentiate six more times. Using \(A>3/4\), \(A^{-7}<8\),
\(|2-it|<2T\), and \(\sum_{j=0}^6(6!/j!)T^j<2T^6\),
the two terms have norms at most \(96\,2^{67}T^7\) and
\(144\,2^{67}T^6\). Their sum is below \(2^{74}T^7\).
Since \(|\log u|<1\) on \([A,C]\), the remaining logarithmic
product-rule terms are at most \(336\,2^{67}T^6\). Therefore

\[
\boxed{\|D^7\ell_t\|_{\rm TV}\le2^{74}T^7,\qquad
\|D^7(\ell_t\log u)\|_{\rm TV}\le2^{75}T^7.}
\tag{4}
\]

## Two effective lattice estimates

Order-seven Poisson summation gives, for \(y>0\),

\[
\left|\sum_{j\ge1}F(j/y)-y\int F\right|
 \le\kappa_7\|D^7F\|_{\rm TV}y^{-6},\qquad
\kappa_7=\frac{2\zeta(7)}{(2\pi)^7}<2^{-16}.
\]

The constant follows from \(\zeta(7)<2\) and \(\pi>3\).
Preparation gives \(\int\ell_t=0\). Define
\(D_t(s)=q^{-1}\int\ell_t(u)u^{s-1}\,du\), matching the
zero coefficient in the [parent notes](../README.md). Then
\(qD_t'(1)=\int\ell_t(u)\log u\,du\), and (4) gives

\[
\left|\sum_j\ell_t(j/y)\right|\le2^{58}T^7y^{-6},
\]
\[
\left|\sum_j(\log j)\ell_t(j/y)-qD_t'(1)y\right|
 \le2^{59}T^7(1+|\log y|)y^{-6}.
\tag{5}
\]

The logarithmic continuum survives preparation and stays explicit.

## Full-Lambda decomposition

For real \(U,V\ge1\), the exact Vaughan convolution identity is

\[
\Lambda=\mu_{\le U}*\log-\mu_{\le U}*1*\Lambda_{\le V}
           +\Lambda_{\le V}+\mu_{>U}*1*\Lambda_{>V}.
\]

Put

\[
M_1(U)=\sum_{d\le U}\frac{\mu(d)}d,\qquad
A_U(m)=\sum_{d\mid m,\ d>U}\mu(d),
\]
\[
\mathcal J_{U,V;t}(X)=D_t'(1)M_1(U)
  +\frac1{qX}\sum_{m>U,\ n>V}A_U(m)\Lambda(n)\ell_t(mn/X).
\tag{6}
\]

Assume \(1\le U\le X\) and \(V<AX\). The direct
\(\Lambda_{\le V}\) term vanishes by support. Applying (5) and
the elementary Chebyshev bound \(\psi(V)<3V\) proves

\[
\boxed{|\lambda_t(X)-\mathcal J_{U,V;t}(X)|
 \le2^{59}T^7X^{-7}\big[(1+\log X)U^7+(UV)^7\big].}
\tag{7}
\]

For the first Type-I term, \(1\le X/d\le X\) and
\(\sum_{d\le U}d^6\le U^7\). For the second,
\(\sum_{n\le V}\Lambda(n)n^6\le3V^7\); the factor \(q=7/3\)
fits the constant in (7). The [source arithmetic assessment](../../programs/01_signed_arithmetic_covariance/NATURAL_BOUND_ASSESSMENT_20261004.md)
already proves \(\psi(V)\le4(\log2)V<3V\).

The full support constraint \(AX\le mn\le CX\), strict cutoff
conditions, and every terminal partial product band are part of (6).
The inner coefficient is full \(\Lambda\), including every prime power.

## A feasible cutoff for the saved finite gate

Let \(N\ge10\), \(T+1<e^N\), \(\eta_N=(8e)^{-N}\),
\(a_N=\eta_N/256\), and

\[
24(N+1)\le\log X\le208N,\qquad r=a_N X^{-1/4},
\qquad U=V=2^{-5}\sqrt{X/T}\,r^{1/14}.
\tag{8}
\]

These are the scales required by the
[original scalar gate](EXPLICIT_CONSTANTS_AND_FINITE_WINDOW_20261004.md).
The cutoff satisfies \(U>e^{10N}\), \(U^2<AX\), and
\(U^7>1+\log X\). Indeed, with \(y=\log X\),

\[
\log U=\frac{27y}{56}-\frac{\log T}{2}
 -\frac{N\log(8e)}{14}-\frac{39\log2}{7}
 >\frac{217}{20}N+\frac{537}{70}>10N.
\]

Here \(y\ge24(N+1)\), \(\log T<N\), \(\log(8e)<31/10\),
and \(\log2<7/10\). Also \(r<1\) gives
\(U^2/X=2^{-10}T^{-1}r^{1/7}<A\), and
\(U/X\le1/(32\sqrt{XT})<1/320<A\). Thus \(U\le X\) and
\(V<AX\) separately. Finally \(e^{70N}>1+208N\) for
\(N\ge10\), proving the required bound on \(U^7\).

Since \(U^{14}=2^{-70}(X/T)^7r\), the two errors in (7)
each cost at most \(2^{-11}r\). Hence

\[
\boxed{|\lambda_t(X)-\mathcal J_{U,U;t}(X)|\le2^{-10}r.}
\tag{9}
\]

An independent signed estimate

\[
|\mathcal J_{U,U;t}(X)|\le(1-2^{-10})a_NX^{-1/4}
\tag{10}
\]

uniformly over the saved carrier and physical-scale intervals suffices
for the original scalar gate. It concerns the complete Type-II sum
together with \(D_t'(1)M_1(U)\); (9) discards neither component.
The factor region is explicitly

\[
U<m,n\le CX/U,\qquad
U=2^{-5}T^{-1/2}a_N^{1/14}X^{27/56},\qquad AX\le mn\le CX.
\]

This is arithmetic localization with an effective error. In particular,
deleting inner prime powers by an absolute \(U^{-1/2}\) envelope
would cost \(X^{-27/112}\), larger than the demanded
\(X^{-1/4}=X^{-28/112}\), even before height and \(a_N\) losses.
Full \(\Lambda\) must remain in the first proposed Type-II estimate.

The [exact replay checks](../../../numerics/height_adapted_zero_detection/gaussian_localization/README.md)
certify the polynomial and rational constant arithmetic. The
[internal review](../../../reviews/height_adapted_zero_detection/gaussian_localization/ARITHMETIC_REDUCTION_REVIEW_20261004.md)
records the scope and proof corrections. Neither supplies (10).
