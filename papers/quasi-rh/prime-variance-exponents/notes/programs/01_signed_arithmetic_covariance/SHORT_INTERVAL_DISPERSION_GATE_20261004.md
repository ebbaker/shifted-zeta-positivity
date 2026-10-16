# Additive smoothing and the coherent mean in the localized divisor target

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel analytical work and same-model cross-review are internal checks,
not independent specialist refereeing. No new global prime-variance exponent,
zero-free strip, or mathematical priority is claimed.

This continues the localized target (15)--(18) in the
[aggregated-kernel continuation](AGGREGATED_KERNEL_CONTINUATION_20261004.md)
and uses the probe regularity established in the
[mixed-discrepancy companion](MIXED_DISCREPANCY_FEEDBACK_20261004.md).
Set

\[
T=CX/U,\qquad
\epsilon_X=\sup_{U\le t\le T}|E(t)/t|.
\]

Chebyshev's bound gives \(\epsilon_X=O(1)\). All arithmetic sums use their
displayed real cutoff conventions. The additive window is denoted by \(h\),
reserving \(H=X/U^2\) for the product-scale parameter in companion notes.

## 1. Smooth the actual signed divisor sum at its natural scale

Write

\[
\mathcal I_{(D,U]}=\sum_n\mu(n)w_X(n),\qquad
W_X(d)=-\frac1X\int_U^T\frac{E(t)}t S(X/(dt))\,dt,
\qquad w_X(d)=\mathbf1_{(D,U]}(d)W_X(d).
\tag{1}
\]

Extend \(w_X\) by zero outside its band. The complete prime interval and
all prime-error signs are retained in this deterministic weight.

Put \(g(v)=v\ell'(v)\) and
\(g_1(v)=vg'(v)=v\ell'(v)+v^2\ell''(v)\). The mixed-discrepancy note
proves that \(\int g_1=0\) and \(D^5g_1\) is a finite measure.
Termwise differentiation of a locally finite sum and fifth-order Poisson give

\[
S'(y)=-\frac1y\sum_{k\ge1}g_1(k/y)=O_w(y^{-5}).
\tag{2}
\]

The already proved bound \(S(y)=O_w(y^{-5})\) also holds.
With \(d=Ur\) and \(\eta=U^2/X\), write

\[
\begin{aligned}
W_X(Ur)&=U^{-1}\Psi_X(r),\\
\Psi_X(r)&=-\int_\eta^C\epsilon((X/U)s)S(1/(rs))\,ds,
\qquad \epsilon(t)=E(t)/t.
\end{aligned}
\tag{3}
\]

Differentiation acts only on the smooth \(S\) factor, never on
\(\epsilon\). For \(0<r\le1\), these Poisson estimates imply

\[
|\Psi_X(r)|\ll_w\epsilon_Xr^5,\qquad
|\Psi_X'(r)|\ll_w\epsilon_Xr^3.
\tag{4}
\]

Consequently the continuous and discrete total variations satisfy

\[
\begin{aligned}
\operatorname{TV}(w_X)
&\le |W_X(D)|+|W_X(U)|+\int_D^U|W_X'(d)|\,dd
\ll_w\epsilon_X/U,\\
\sum_{n\in\mathbb Z}|w_X(n+1)-w_X(n)|
&\le\operatorname{TV}(w_X).
\end{aligned}
\tag{5}
\]

These estimates are independent of \(D\). Both band endpoint jumps are
included. A bound using only \(|W_X'(d)|\ll\epsilon_X/d^2\) would lose
the unnecessary factor \(U/D\).

For an integer \(h\ge1\), define

\[
a_h(n)=\frac1h\sum_{j=1}^h\mu(n+j),
\tag{6}
\]

with \(\mu(n)=0\) for \(n\le0\). There is the exact finite identity

\[
\begin{aligned}
\mathcal I_{(D,U]}&=\sum_n a_h(n)w_X(n)+R_h,\\
R_h&=\sum_m\mu(m)
\left[w_X(m)-\frac1h\sum_{j=1}^h w_X(m-j)\right].
\end{aligned}
\tag{7}
\]

Since \(|\mu|\le1\), translating a sequence through \(j\) places costs
at most \(j\) times its discrete total variation. Therefore

\[
|R_h|\le\frac{h+1}{2}
\sum_n|w_X(n+1)-w_X(n)|\ll_w\epsilon_Xh/U.
\tag{8}
\]

No assumption about Möbius cancellation enters (8). It preserves the signed
covariance while replacing individual Möbius values by short-interval means.
For the balanced cutoffs

\[
U=X^{1/2-\kappa/28},\qquad
D=X^{1/2-3\kappa/28},\qquad 0<\kappa<14/29,
\]

choose

\[
h=\left\lfloor UX^{-\kappa/2}\right\rfloor
=\left\lfloor X^{1/2-15\kappa/28}\right\rfloor.
\tag{9}
\]

Then

\[
\boxed{\quad
\mathcal I_{(D,U]}=
\sum_{D<n\le U}a_h(n)W_X(n)+O_w(X^{-\kappa/2}).
\quad}
\tag{10}
\]

The window tends to infinity throughout the stated range, and \(h<D\)
eventually. For \(\kappa=1/100\), its exponent is
\(277/560=0.494642857\ldots\). The means near \(U\) contain Möbius
values up to \(U+h\); those atoms are required. Formula (7) includes
all endpoint effects exactly.

## 2. The precise Cauchy criterion and the stronger strip it implies

Define the uncentered second moment

\[
V_h(D,U)=\frac1U\sum_{D<n\le U}|a_h(n)|^2.
\tag{11}
\]

The weight estimate gives \(\sum_n|w_X(n)|^2\ll_w\epsilon_X^2/U\).
Cauchy's inequality and (8) yield

\[
|\mathcal I_{(D,U]}|\ll_w
\epsilon_X\bigl(V_h(D,U)^{1/2}+h/U\bigr).
\tag{12}
\]

Thus \(V_h\ll X^{-\kappa}\), uniformly at all sufficiently large real
\(X\), would suffice. This factorwise criterion forces a stronger fixed
zero-free strip than the original target.

Indeed, let \(N=\lfloor U\rfloor-\lfloor D\rfloor\). For each \(j\),
the translated interval \((D+j,U+j]\) differs from \((D,U]\) in at
most \(2j\) integer atoms. Hence

\[
\sum_{D<n\le U}a_h(n)=M(U)-M(D)+O(h).
\tag{13}
\]

Cauchy's inequality and the proposed bound for \(V_h\) would give

\[
|M(U)-M(D)|\ll UX^{-\kappa/2}+h\ll UX^{-\kappa/2}.
\tag{14}
\]

As \(X\) ranges over all sufficiently large positive reals, so does
\(U\). Write

\[
D=U^r,\qquad r=\frac{14-3\kappa}{14-\kappa},\qquad
\delta=\frac{14\kappa}{14-\kappa}.
\tag{15}
\]

Then (14) becomes \(|M(U)-M(U^r)|\ll U^{1-\delta}\).
Iterating \(U\mapsto U^r\) proves

\[
M(U)\ll U^{1-\delta}.
\tag{16}
\]

For completeness, put \(\alpha=1-\delta>0\), and choose a fixed base
\(U_0\) large enough that \(U^{r\alpha}\le U^\alpha/2\) for
\(U\ge U_0\). The recursive bound
\(|M(U)|\le |M(U^r)|+cU^\alpha\) then propagates
\(|M(U)|\le C U^\alpha\), with \(C\ge2c\) and large enough to cover
the bounded base interval. This is a bound at all real scales; it does
not rely on an integer-only subsequence.

Here \(0<\delta<1/2\). Partial summation makes

\[
\sum_{n\ge1}\frac{\mu(n)}{n^z}
=z\int_1^\infty M(t)t^{-z-1}\,dt
\tag{17}
\]

holomorphic for \(\Re z>1-\delta\). It agrees with \(1/\zeta(z)\)
for \(\Re z>1\), so \(\zeta\) has no zeros in
\(\Re z>1-\delta\). Since \(\delta>\kappa/2\), this is strictly
stronger than the desired strip \(\Re z>1-\kappa/2\).

This is an implication theorem. It does not say that the proposed variance
estimate is false or that every use of Cauchy's inequality is inadmissible.
It shows why a generic uncentered square-root-cancellation input would
assume stronger arithmetic information than the original target.

For exact autocorrelation work, retain the shifted bands:

\[
\begin{aligned}
Uh^2V_h={}&\sum_{j=1}^h\sum_{D<n\le U}\mu(n+j)^2\\
&+2\sum_{a=1}^{h-1}\sum_{j=1}^{h-a}
\sum_{D<n\le U}\mu(n+j)\mu(n+j+a).
\end{aligned}
\tag{18}
\]

Replacing every translated band by \((D,U]\) incurs an \(O(h/U)\)
error in \(V_h\). At (9), this is \(O(X^{-\kappa/2})\), larger than
the \(X^{-\kappa}\) variance budget. Such an endpoint simplification
therefore cannot be used at the proposed precision without further work.

## 3. Retain the coherent mean explicitly

For \(N>0\), set

\[
\bar a_h=\frac1N\sum_{D<n\le U}a_h(n),\qquad
B_X=\sum_{D<n\le U}W_X(n).
\tag{19}
\]

The exact centered decomposition is

\[
\boxed{\quad
\mathcal I_{(D,U]}=\bar a_h B_X
+\sum_{D<n\le U}(a_h(n)-\bar a_h)W_X(n)+R_h.
\quad}
\tag{20}
\]

Moreover,

\[
V_h=\frac NU|\bar a_h|^2
+\frac1U\sum_{D<n\le U}|a_h(n)-\bar a_h|^2.
\tag{21}
\]

A centered dispersion estimate can control fluctuations without assuming
a small mean. It leaves the signed coherent contribution \(\bar a_hB_X\),
whose second factor is exactly

\[
B_X=-\frac1X\int_U^T\epsilon(t)
\sum_{D<n\le U}S(X/(nt))\,dt.
\tag{22}
\]

The probe's zero integral does not automatically remove this coherent
component. To see the limitation precisely, define the continuous kernel
primitives

\[
K_0(v)=\sum_{k\ge1}\ell(kv),\qquad
B_0(v)=\sum_{k\ge1}\frac1k\int_{kv}^{\infty}\ell(y)\,dy.
\]

The centering calculation gives \(B_0(v)=qc_w+O_w(v^8)\) at zero,
while \(B_0'=-K_0\) and \(S(1/v)=vK_0'(v)\). Therefore

\[
\int_0^r S(1/v)\,dv=rK_0(r)+B_0(r)-qc_w,
\qquad
\int_0^C S(1/v)\,dv=-qc_w\ne0.
\tag{23}
\]

Thus even the continuous divisor-average kernel is not identically zero.
This proves neither a lower bound nor a sign for the actual discrete,
prime-error-weighted quantity \(B_X\).

No estimate here gives the eventual sign or requisite fixed power of the
coherent contribution. Equations (10) and (20) provide an exact signed target;
(12)--(18) identify where a factorwise dispersion shortcut would require
stronger arithmetic information and where its endpoint budget fails.
Existing logarithmic short-interval results cannot be substituted for
the power input \(V_h\ll X^{-\kappa}\).


## Source scope

For comparison with an available input, the illustrative kappa=0.01 gives
h=X^(277/560) and divisor scales between X^(1397/2800) and X^(1399/2800).
For sufficiently small fixed epsilon these window lengths lie within the
all-interval range of Matomäki, Shao, Tao and Teräväinen,
[Higher uniformity I, Theorem 1.1(i)](https://arxiv.org/html/2204.03754v4).
Its Möbius conclusion supplies arbitrary fixed logarithmic savings; it does
not supply the power variance bound proposed after (12). The later
[almost-all-intervals paper](https://arxiv.org/html/2411.05770v2)
also must not be read as providing that fixed-power input. This source
check imports no new theorem into the reduction or the stronger-strip
implication, both of which were proved directly above.
