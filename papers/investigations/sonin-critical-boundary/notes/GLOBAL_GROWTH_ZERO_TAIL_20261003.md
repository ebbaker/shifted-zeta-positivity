# A continuum bound for the fixed probe and the remaining global tail

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and reasoning effort not exposed.
Internal research draft, not independent specialist refereeing. No priority claim.

## 1. Result and scope

For the exact polynomial probe already used in the manuscript, one can prove

\[
 |M_g(r)|<1.48\qquad(2\le r\le500).
\]

This holds at every real separation in the interval, using a published
finite-height RH verification and a proved, absolutely convergent zero tail.
No new prime sieve or zero-ordinate computation is needed. It is substantially
stronger than five individual numerical tests as an absolute growth estimate.
It still does not give the exact pairwise threshold `|C_g(r)|<=q`, since
`q=Q[g]` is about 1.4669400310052846. It does not establish the global
subexponential bound, and the high-zero remainder explains the remaining gap.

## 2. Exact transform decay with elementary constants

Write `a=1/4`, `ell=1/2`,

\[
 h(x)=(1-16x^2)^8\mathbf1_{|x|<a},\quad
 g_0=-h'''+h'/4,\quad g=g_0/\sqrt\nu,
 \quad \nu=\|g_0\|_2^2.
\]

Let `g0^(6)` below mean the interior polynomial sixth derivative, and let
`D^6 g0` mean the derivative of the zero extension, a finite signed measure.
The polynomial and its first four derivatives vanish at both endpoints;
its fifth derivative has absolute value `8! 8^8` at each endpoint. Hence

\[
 \|D^6g_0\|_{\rm TV}
 \le 2\,8!8^8+\int_{-1/4}^{1/4}|g_0^{(6)}(x)|\,dx
 \le2\,8!8^8+\sqrt{\tfrac12\|g_0^{(6)}\|_2^2}.
\]

Direct rational polynomial integration gives

\[
 \nu=\frac{146640624550936576}{37921101075},\qquad
 \|g_0^{(6)}\|_2^2=
 \frac{2504085215525628254072340480}{19}.
\]

The integer `8117695446119` strictly exceeds the square root above. Thus set

\[
 B=9470610144359,\qquad
 K^2=\frac{B^2}{\nu}
 =\frac{3401236708845585730813202011474047075}{146640624550936576}.
\]

For `G(z)=integral g(x)e^(zx)dx`, integration by parts against the
sixth distributional derivative gives

\[
 |G(z)|\le K\,e^{|\Re z|/4}|z|^{-6}\quad(z\ne0).
\]

Consequently, for `Phi(z)=G(z)G(-z)` and `|sigma|<=1/2`,

\[
 |\Phi(\sigma+it)|\le e^{1/4}K^2|t|^{-12}\quad(t\ne0).       \tag{1}
\]

All norms and the integer square-root bracket are checked by exact rational
arithmetic in [`certify_zero_tail.py`](../numerics/global_growth_20261003/certify_zero_tail.py). This conservative estimate does not
use cancellation between polynomial coefficients in an absolute integral.

## 3. The unconditional zero expansion

Put `s_rho=rho-1/2`; sums run over distinct nontrivial zeros, with multiplicity `m_rho`. The
complete explicit formula already in the manuscript, followed by polarization,
gives

\[
 C_g(r)=\sum_\rho m_\rho\Phi(s_\rho)e^{s_\rho r}
 \quad(r\in\mathbb R),\qquad
 q=\sum_\rho m_\rho\Phi(s_\rho).                           \tag{2}
\]

No zero location is being assumed. Reflection of zeros makes these expressions
real and even in `r`. The series converges absolutely, locally uniformly in
`r`, by (1), `|Re s_rho|<1/2`, and `N(T)=O(T log T)`. To extend the
manuscript's smooth-source formula to this polynomial source, mollify `g0`.
On the critical strip the mollifier's bilateral transform is uniformly bounded
for a fixed small support enlargement. It multiplies the `|t|^-6` estimate,
so (1) dominates all zero sums uniformly; the arithmetic form also converges
in the stated logarithmic form norm. This justifies the extension.

For `r>ell`, the existing covariance identity then gives the exact expansion

\[
 M_g(r)=-\sum_\rho m_\rho\Phi(s_\rho)e^{s_\rho r}
        +\epsilon_g(r),                                  \tag{3}
\]

where, writing `n(v)=e^(-v/2)/(1-e^(-2v))`,

\[
 \epsilon_g(r)=-\int_{-\ell}^{\ell}\varphi(u)n(r+u)\,du
 =-\sum_{k=1}^{\infty}\Phi(2k+1/2)e^{-(2k+1/2)r}.          \tag{4}
\]

The omitted `k=0` term vanishes because `Phi(1/2)=0`; all terms in (4)
converge absolutely for `r>ell`. In particular

\[
 |\epsilon_g(r)|\le b(r):=
 \frac{\ell e^{-5(r-\ell)/2}}{1-e^{-2(r-\ell)}}.            \tag{5}
\]

For this real odd probe `G(z)` is real and odd for real `z`, so
`Phi(z)=-G(z)^2<=0` there; consequently the exact remainder (4) is
nonnegative. We only need its absolute bound. Formula (3) agrees with the
residues of the Laplace identity: nontrivial zeros have residue
`-m_rho Phi(s_rho)`, the pole at 1 is canceled, and the trivial zeros yield
(4). This is a sign check, not a second assumption.

## 4. A tail bound without enumerating zeros

Let `N(t)` count zeros with `0<Im rho<=t`, with multiplicity. Corollary 1.2
of Hasanalizade, Shen and Wong, *Counting zeros of the Riemann zeta function*,
[primary paper](https://arxiv.org/pdf/2107.06506), states for `t>=e` that

\[
 \left|N(t)-\frac{t}{2\pi}\log\frac{t}{2\pi e}\right|
 \le0.1038\log t+0.2573\log\log t+9.3675.
\]

In particular `N(t)<=t log t` for `t>=100`. For an elementary check, the
main term is at most `(t/6)log t`; using `log t>=4` and
`log log t<=log t`, the error is at most `3log t`, which is at most
`(3t/100)log t`. Their sum is smaller than `t log t`.

Stieltjes integration by parts gives, for `T>=100`,

\[
 \sum_{|\Im\rho|>T}m_\rho|\Im\rho|^{-12}
 =-2N(T)T^{-12}+24\int_T^\infty N(t)t^{-13}\,dt
 \le24T^{-11}\left(\frac{\log T}{11}+\frac1{121}\right).
\]

Define

\[
 \delta_T=24e^{1/4}K^2T^{-11}
          \left(\frac{\log T}{11}+\frac1{121}\right).
                                                                    \tag{6}
\]

Then the high-zero part `R_T(r)` of (2) obeys

\[
 |R_T(r)|\le\delta_Te^{|r|/2}.                              \tag{7}
\]

Suppose RH has been verified through height `T`. The complementary low-zero
sum has nonnegative coefficients `Phi(i gamma)=|G(i gamma)|^2`. At zero,
(2) implies

\[
 S_T:=\sum_{|\Im\rho|\le T}m_\rho|G(i\Im\rho)|^2
      =q-R_T(0)\le q+\delta_T.
\]

Thus for every real `r`,

\[
 |C_g(r)|\le q+\delta_T(1+e^{|r|/2}),                      \tag{8}
\]

and for `r>ell`,

\[
 |M_g(r)|\le q+\delta_T(1+e^{r/2})+b(r).                  \tag{9}
\]

The diagonal controls the entire verified low-frequency mass. No list of its
individual ordinates is needed. Positivity is used only for the finite-height
zeros to which the published theorem applies; the unknown high zeros are
bounded by absolute values.

For completeness, (7) also gives an approximate Gram inequality. If finitely
many translation parameters lie in an interval of length `R`, then

\[
 \sum_{i,j}\overline{c_i}c_j C_g(r_j-r_i)
 \ge-\delta_Te^{R/2}\left(\sum_j|c_j|\right)^2.
\]

This is not nonnegativity. The number and conditioning of the sources matter
when using it as an operator estimate.

## 5. Published height and outward arithmetic

Platt and Trudgian, *The Riemann hypothesis is true up to 3*10^12*,
[primary publication](https://doi.org/10.1112/blms.12460),
[author preprint](https://arxiv.org/abs/2004.09765), rigorously verify that all
zeros with `0<gamma<=3*10^12` are on the critical line. We use only that
stated height; no claim that it is the latest possible height is needed.

At `T=3*10^12`, (6) gives

\[
 \delta_T<1.058\,10^{-116},\qquad
 \delta_T(1+e^{250})<3.961\,10^{-8}.
\]

The previously certified diagonal has `q<1.46694003100529`, and

\[
 b(2)<0.01237498726501953.
\]

Since `b` decreases and the tail cost increases, (9) proves throughout
`2<=r<=500` that

\[
 |M_g(r)|<1.47931505787654<1.48.                            \tag{10}
\]

The saved 192-bit and 256-bit Arb runs both certify these comparisons. They
recompute the polynomial norms exactly and hash-check the existing 256-bit
diagonal certificate before using its rational upper endpoint. Each run took
less than 0.01 seconds. The preflight was saved before either run. The
arithmetic certifies constants in (10); the published height theorem and the
analytic argument above remain external mathematical inputs.

## 6. What would have to change to obtain the global theorem

For a fixed `T`, (9)'s error still grows like `e^(r/2)`. To keep this explicit high-zero
majorant bounded as `r` grows, the height must grow on the scale
`exp(r/22) r^(1/11)`, up to constant factors; the assumption of critical-line
location through those indefinitely increasing heights is precisely the
unresolved obstruction. The smooth profile's twelfth-power transform decay
makes a fixed height remarkably useful but does not remove this dependence.

Known zero-free regions do improve the absolute zero majorant
unconditionally. Theorem 1.3 of Mossinghoff, Trudgian and Yang,
*Explicit zero-free regions for the Riemann zeta-function*,
[primary paper](https://arxiv.org/pdf/2212.06867), gives

\[
 \beta<1-\frac1{R\log|\gamma|},\qquad
 R=5.558691,\quad |\gamma|\ge2.
\]

Group high zeros into `e^k<|gamma|<=e^(k+1)`. By (1) and the counting
bound, their absolute contribution to (2) is at most a fixed constant times

\[
 e^{r/2}\sum_{k\ge k_0}(k+1)
 \exp\left(-11k-\frac{r}{R(k+1)}\right).                 \tag{11}
\]

For every `0<eta<11`, with `j=k+1`,

\[
 11j+\frac r{Rj}\ge\eta j+
           2\sqrt{\frac{(11-\eta)r}{R}}.
\]

The remaining `sum j exp(-eta j)` converges. The finitely many omitted
zeros can be taken within the published verified height, and so contribute
a bounded amount. Therefore for every

\[
 0<c<2\sqrt{11/5.558691}=2.813455638\ldots
\]

one obtains the unconditional asymptotic estimate

\[
 M_g(r)=O_c\bigl(e^{r/2-c\sqrt r}\bigr).                  \tag{12}
\]

This is a consequence of the known zero-free region applied to this smoothed
probe, not a new zero-free region. The exponent still has linear rate `1/2`.
Their stronger Vinogradov--Korobov region, with denominator
`55.241(log|gamma|)^(2/3)(loglog|gamma|)^(1/3)`, gives by the same grouping
and elementary optimization

\[
 M_g(r)=O\left(\exp\left\{\frac r2-
 c\,r^{3/5}(\log r)^{-1/5}\right\}\right)
\]

for some `c>0`. No numerical optimum for this latter constant is asserted.
Neither estimate is subexponential in `r`; neither proves the single-probe
criterion in the manuscript. A successful global approach must retain
substantial additional signed cancellation or prove a stronger zero-location
statement, rather than merely substitute a known zero-free region in an
absolute zero sum.
