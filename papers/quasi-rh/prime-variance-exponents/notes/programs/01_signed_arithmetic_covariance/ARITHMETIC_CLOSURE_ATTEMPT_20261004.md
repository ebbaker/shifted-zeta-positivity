# Product-coordinate arithmetic closure of the signed covariance

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant
and configured reasoning effort are not exposed and are not inferred.
Same-model internal analysis and review are not independent specialist
refereeing. This is a continuation of the [mixed-discrepancy feedback](MIXED_DISCREPANCY_FEEDBACK_20261004.md),
not a new global variance bound or zero-free strip.

## 1. The actual two-factor correlation in one product coordinate

Keep the inherited fixed kernel \(\mathscr F\), support endpoint \(C\),
normalization \(q\), real cutoff \(U\ge1\), and density remainder
\(R=O_w((U^2/X)^8)\). Assume \(U^2\le AX\).
Let \(W(n)\) be either the prime-only weight
\(P(p)=\log p\), \(P(n)=0\) otherwise, or \(\Lambda(n)\). Put

\[
\Psi_W(t)=\sum_{n\le t}W(n),\qquad
E_{W,U}(t)=\Psi_W(t)-\Psi_W(U)-(t-U),\qquad
M_U(s)=M(s)-M(U).
\]

For \(r\ge U^2\), define the fully capped product-coordinate correlation

\[
\mathcal C_U^W(r)=
\int_U^{r/U}M_U(s)E_{W,U}(r/s)\frac{ds}{s};
\tag{1}
\]

set it to zero for \(r<U^2\). The lower values at \(U\) are
right-continuous, so the arithmetic atoms at \(U\) are excluded.
Changing variables \(v=st/X\) in the mixed-discrepancy formula gives
exactly, for the actual prime-only target,

\[
\boxed{
J_0(X;U)-R
=\frac1{qX}\int_{U^2/X}^{C}
\mathscr F(v)\mathcal C_U^P(Xv)\,dv.
}
\tag{2}
\]

The von Mangoldt variant has the identical formula with \(P\) replaced
by \(\Lambda\). Equation (2) preserves both terminal factor intervals
through the integration interval in (1); it has not enlarged the
arithmetic region. It is an exact single product-coordinate form of the
joint correlation, not a separated envelope estimate.

## 2. A finite logarithmic Riesz formula

Expanding both increments in (1), then integrating over
\(d\le s\le r/n\), proves

\[
\mathcal C_U^W(r)=\mathcal H_U^W(r)-\mathcal D_U(r),
\tag{3}
\]

where

\[
\mathcal H_U^W(r)=
\sum_{\substack{d>U,\ n>U\\dn\le r}}
\mu(d)W(n)\log\frac r{dn},
\tag{4}
\]

and the exact continuum correction is

\[
\mathcal D_U(r)=
\sum_{U<d\le r/U}\mu(d)
\left\{\frac rd-U-U\log\frac r{Ud}\right\}.
\tag{5}
\]

Indeed the continuous contribution of a fixed \(d\) is

\[
\int_d^{r/U}\left(\frac rs-U\right)\frac{ds}{s}
=\frac rd-U-U\log\frac r{Ud}.
\]

All sums are finite. At \(dn=r\), the logarithmic weight in (4) is zero;
at \(d=r/U\), the bracket in (5) is zero. Thus the displayed weak
product caps and strict lower cutoffs handle equality without any
half-weight convention. At \(r=U^2\), both sides of (3) vanish.

## 3. Exact low/high edges of the logarithmic derivative identity

For an arithmetic sequence \(a\), write

\[
\mathcal L_a(y)=\sum_{n\le y}a(n)\log(y/n)
\quad(y\ge1).
\]

For every real \(r\ge U^2\), inclusion-exclusion gives

\[
\begin{aligned}
\mathcal H_U^W(r)
={}&\mathcal L_{\mu*W}(r)
-\sum_{d\le U}\mu(d)\mathcal L_W(r/d)
-\sum_{n\le U}W(n)\mathcal L_\mu(r/n)\\
&+\sum_{d\le U}\sum_{n\le U}
\mu(d)W(n)\log\frac r{dn}.
\end{aligned}
\tag{6}
\]

Here \(*\) means Dirichlet convolution. The final low/low sum has no
extra cap because \(dn\le U^2\le r\). It is added back once, and both
low/high edge sums are retained exactly. The two edge sums are
different arithmetic quantities and do not cancel merely because the
lower cutoffs agree.

The coefficient identity

\[
(\mu*\Lambda)(m)=-\mu(m)\log m
\tag{7}
\]

is exact for every integer \(m\ge1\). One elementary proof differentiates
\(\mu*1=\delta_1\) by the derivation
\(Da(n)=a(n)\log n\), obtaining
\(D\mu+\mu*\Lambda=0\) after convolution with \(\mu\).
Consequently the von Mangoldt version of the first term in (6) is

\[
\mathcal L_{\mu*\Lambda}(r)
=-\sum_{m\le r}\mu(m)\log m\log(r/m).
\tag{8}
\]

This explicitly couples the two arithmetic inputs before applying an
absolute value. It supplies information not present in a model of two
arbitrary functions satisfying separate size bounds.

To keep the actual prime-only correlation exact, define
\(\Pi=\Lambda-P\), supported on proper prime powers. Then

\[
\mathcal L_{\mu*P}(r)
=-\sum_{m\le r}\mu(m)\log m\log(r/m)
-\sum_{dk\le r}\mu(d)\Pi(k)\log\frac r{dk}.
\tag{9}
\]

The proper-prime-power correction in (9) must stay in this formula;
its full, untruncated convolution is not silently charged to a bound
proved only for the high/high prime-power range. Alternatively one can
apply the already-budgeted high/high prime-power comparison before
using the von Mangoldt form of (2).

## 4. What this attempt does and does not prove

Equations (2)--(9) turn the complete mixed discrepancy into a weighted
one-variable integral of an explicitly coupled arithmetic expression.
They give a concrete place to test a Selberg or renewal argument while
retaining both edge sums, the low/low correction, and the continuum.
The elementary identity (7) alone gives no sign to their combination.
Discarding any of those terms produces a different target.

In particular, a one-sided power estimate for the combined right side
of (3), after integration in (2), has not been proved. Bounding its
pieces independently by the available classical error envelopes gives
no fixed power. The required estimate for the full remaining divisor
band in the [aggregated-kernel continuation](AGGREGATED_KERNEL_CONTINUATION_20261004.md)
therefore remains the admissible analytic target. This reduction is
research progress in exact arithmetic structure; it is not a
contraction or an exponent improvement.

## Appendix. The deterministic lower-product cap is power-affordable

The mode calculation in the mixed-discrepancy note estimated its lower
product cap using only \(\mathscr F(v)=O(v^3)\). The already-proved
lattice primitive gives a stronger remainder. This is a bound for the
explicit deterministic test functions below, not for the arithmetic
correlation (1).

Write \(H=X/U^2\), and let

\[
H_\ell(v)=\int_v^\infty\ell(y)\,dy,\qquad
K_0(v)=\sum_{k\ge1}\ell(kv),\qquad
B_0(v)=\sum_{k\ge1}\frac{H_\ell(kv)}k.
\]

The centering calculation, applied to \(f(v)=H_\ell(v)/v\), proves

\[
B_0(v)=qc_w+R_\ell(v),\qquad R_\ell(v)=O_w(v^8).
\tag{10}
\]

Moreover \(B_0'=-K_0\), \(\mathscr F=(vK_0')'\), and the existing Poisson
bounds give \(K_0=O(v^6)\), \(K_0'=O(v^4)\). Therefore

\[
\mathscr F(v)=-(vR_\ell''(v))',\qquad
R_\ell'=O(v^6),\quad R_\ell''=O(v^4).
\tag{11}
\]

For fixed complex \(z,\xi\) with positive real parts, set

\[
\phi_{z,\xi}(u)=
\int_0^{\log u}(e^{za}-1)(e^{\xi(\log u-a)}-1)\,da,
\qquad u>0.
\tag{12}
\]

This includes \(z=\xi\) without a singular quotient. At \(u=1\),
\(\phi=\phi'=\phi''=0\). Near zero,
\(\phi^{(j)}(u)=O_{z,\xi}(u^{-j}(1+|\log u|))\), \(0\le j\le3\).
Three integrations by parts, using (11), give

\[
\begin{aligned}
\int_0^{1/H}\mathscr F(v)\phi_{z,\xi}(Hv)\,dv
=\int_0^{1/H}R_\ell(v)
\{2H^2\phi_{z,\xi}''(Hv)+vH^3\phi_{z,\xi}'''(Hv)\}\,dv
=O_{z,\xi,w}(H^{-7}).
\end{aligned}
\tag{13}
\]

All three upper endpoint terms vanish by the three zeros at one.
The lower endpoint terms vanish by the displayed bounds for
\(R_\ell,R_\ell',R_\ell''\). Substitution \(u=Hv\) in the last
integral gives an integrable majorant
\(H^{-7}u^8(2|\phi''(u)|+u|\phi'''(u)|)\).

Consequently the exact power-increment tests

\[
\mathcal B_{z,\xi}(X,U)=X^{-2}
\iint_{s,t>U}(s^z-U^z)(t^\xi-U^\xi)
\mathscr F(st/X)\,ds\,dt
\]

have the same main terms as in the mixed-discrepancy note, but with
stronger cap errors:

\[
\begin{aligned}
\mathcal B_{z,\xi}
&=\frac{(\xi/z)X^{z-1}U^{\xi-z}\mathscr A(z)
-(z/\xi)X^{\xi-1}U^{z-\xi}\mathscr A(\xi)}{z-\xi}\\
&\quad+O_{z,\xi,w}\left(U^{\Re z+\Re\xi}X^{-1}H^{-7}\right)
\qquad(z\ne\xi),
\end{aligned}
\tag{14}
\]

\[
\mathcal B_{z,z}
=X^{z-1}\{\mathscr A'(z)+(\log H-2/z)\mathscr A(z)\}
+O_{z,w}(X^{\Re z-1}H^{-\Re z-7}).
\tag{15}
\]

Here \(\mathscr A(z)=z^2\zeta(z)L(z)\) and
\(L(z)=\int\ell(v)v^{z-1}\,dv\). Indeed, the omitted lower integral
has prefactor \(U^{z+\xi}/X\) and integrand (12), so (13) applies
directly. No arithmetic terminal interval is removed in this argument.

The calculation also handles multiplicities. For a zeta zero \(\rho\)
of order \(r_\rho\), with \(\Re\rho>0\), define canonical finite test
functions

\[
m_\rho(s)=\operatorname{Res}_{z=\rho}
\frac{s^z}{z\zeta(z)},\qquad
e_\rho(t)=-\frac{r_\rho}{\rho}t^\rho.
\tag{16}
\]

These are explicit functions defined from local Laurent coefficients;
they are not asserted expansions of actual arithmetic errors. Insert
\(m_\rho(s)-m_\rho(U)\) and
\(e_\sigma(t)-e_\sigma(U)\) in the mixed integral normalized by
\(1/(qX^2)\). Its main term is zero for distinct zeros \(\rho\ne\sigma\)
and equals

\[
-\frac{r_\rho L(\rho)}qX^{\rho-1}
\tag{17}
\]

when \(\rho=\sigma\). To check this, take the residue in \(z\) of
(14) multiplied by \(1/(z\zeta(z))\), with \(\xi=\sigma\).
Because \(\mathscr A(\sigma)=0\), its remaining main term simplifies to

\[
\frac{\sigma L(z)X^{z-1}U^{\sigma-z}}{z-\sigma}.
\]

It is analytic at \(\rho\ne\sigma\); at \(\rho=\sigma\), the residue
is \(\rho L(\rho)X^{\rho-1}\). Multiplying by
\(-r_\sigma/(q\sigma)\) proves (17), with no simple-zero assumption.
Differentiating the lower-cap integral a finite number of times bounds
its residue error by

\[
O_{\rho,\sigma,w}\left(
U^{\Re\rho+\Re\sigma}X^{-1}H^{-7}
(1+\log U)^{r_\rho-1}\right).
\tag{18}
\]

For every fixed finite set of nontrivial zeros and
\(U=X^{1/2-\kappa/28}\), this error is
\(O(X^{-4\kappa/7}(1+\log X)^{r_*-1})
=o(X^{-\kappa/2})\), where \(r_*\) is its largest multiplicity.
Thus the complete finite deterministic test, including all cross terms
and its lower product cap, transmits each original zero coefficient at
the actual target's error budget. The new cap estimate removes an
unpaid remainder from that diagnostic. It supplies no expansion or
bound for an infinite zero sum, and does not prove the missing
one-sided arithmetic inequality.
