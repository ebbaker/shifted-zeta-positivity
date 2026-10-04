# Primary-source audit for the balanced arithmetic continuation

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is an internal source audit and mathematical diagnostic, not independent
specialist review.

## Finding

The strongest useful next input located in this bounded literature search is
a Type II major-arc lemma with an explicit Dirichlet-polynomial hypothesis.
It is a reusable conditional estimate, not an unconditional improvement of
the prime variance exponent. Modern uniformity theorems give logarithmic
savings for Möbius and von Mangoldt coefficients in the relevant ranges.
Their power-saving divisor-function results cannot be transferred to primes
by replacing coefficients with absolute majorants.

The new unconditional progress is instead the arithmetic localization proved
in [the companion reduction note](MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md):
the discarded sectors have quadratic shell variance, and the surviving
balanced coefficients and continuum subtraction are explicit. The present
note supplies references, a proposed signed diagnostic, and the precise
limitation of one plausible modern input. No fixed exponent below one has
been established.

The prior
[global mechanism tests](../../investigations/sonin-critical-boundary/notes/selective-loss-program/06_global_mechanism_tests_20261003.md),
[actual-error frequency audit](../../investigations/sonin-critical-boundary/notes/selective-loss-program/09_actual_error_projection_and_frequency_20261003.md),
and [short-interval transfer](../../investigations/sonin-critical-boundary/notes/subpower-milestones/02_short_interval_transfer_and_gate_20261003.md)
were read before selecting this direction. The Saffari–Vaughan range audit is
not repeated.

## 1. Exact identity and grouping convention

Terence Tao, *254A, Notes 3: The large sieve and the Bombieri–Vinogradov
theorem*, 10 January 2015, Lemma 18, equation (32), gives the identity and
an elementary convolution proof:

\[
\Lambda=\Lambda_{\le V}+\mu_{\le U}*\log
-\mu_{\le U}*\Lambda_{\le V}*1+\mu_{>U}*\Lambda_{>V}*1.
\]

This is the exact convention used in the companion note. In particular, the
last factor \(1\) must remain. The lecture subsequently groups it with the
Möbius factor. [Author-hosted source](https://terrytao.wordpress.com/2015/01/10/254a-notes-3-the-large-sieve-and-the-bombieri-vinogradov-theorem/).

For our calculation the alternative grouping is also exact:

\[
b_V(n):=(\Lambda_{>V}*1)(n)
=\sum_{\substack{r\mid n\\r>V}}\Lambda(r),
\qquad 0\le b_V(n)\le\log n,
\]
\[
B_X(x)=\sum_{m>U,n>V}\mu(m)b_V(n)w(mn/x).
\tag{1}
\]

Thus (1) equals the companion note's \(A_U*\Lambda_{>V}\) expression,
not a different bilinear approximation. Both regroupings are finite on
each support window. With \(U=V=X^{11/24}\), the companion note proves

\[
V_g(x)=B_X(x)+c_wM_1(U)x+E_X(x),\qquad
\|E_X\|_{L^2(X,2X)}=O_g(X),
\tag{2}
\]
\[
M_1(U)=\sum_{d\le U}\frac{\mu(d)}d,\qquad
c_w=\int_A^B w(t)\log t\,dt
=-\frac{H(-1/2)}{2\sqrt\nu}<0.
\]

Equation (2), including the nonzero continuum term, is essential when
evaluating any proposed input. Bounding \(B_X\) alone is a different and
potentially much stronger target.

## 2. Modern primary sources and their quantitative scope

Kaisa Matomäki, Xuancheng Shao, Terence Tao, and Joni Teräväinen,
*Higher uniformity of arithmetic functions in short intervals I. All
intervals*, Forum of Mathematics, Pi 11 (2023), e29,
DOI [10.1017/fmp.2023.28](https://doi.org/10.1017/fmp.2023.28).
The checked [arXiv version 4](https://arxiv.org/abs/2204.03754v4) is dated
28 February 2024 and records corrections to the published version.
Theorem 1.1(i)–(ii) bounds the relevant maximal nilsequence sums for
\(\mu\) and \(\Lambda-\Lambda^\sharp\) by \(H\log^{-A}X\), for arbitrary
fixed \(A\), when \(X^{5/8+\epsilon}\le H\le X^{1-\epsilon}\), at fixed
nilsequence complexity. Part (iv) reaches \(X^{3/5+\epsilon}\) for
\(\mu\) with only a \(\log^{-1/4}X\) saving. Part (iii)'s genuine power
savings concern divisor functions. Here
\(\Lambda^\sharp(n)=P(R)\mathbf1_{(n,P(R))=1}/\phi(P(R))\),
\(P(R)=\prod_{p<R}p\), \(R=\exp((\log X)^{1/10})\).
[Primary text, Theorem 1.1, pp. 3–4](https://arxiv.org/pdf/2204.03754v4).

Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao, and Joni
Teräväinen, *Higher uniformity of arithmetic functions in short intervals
II. Almost all intervals*,
[arXiv:2411.05770v2](https://arxiv.org/abs/2411.05770v2),
23 January 2026. Theorem 1.1(i)–(ii), at fixed complexity, gives
\(H\log^{-A}X\) outside measure \(O_A(X\log^{-A}X)\), for
\(\mu,\Lambda-\Lambda^\sharp\) and
\(X^{1/3+\epsilon}\le H\le X^{1-\epsilon}\).

Its Lemma 3.5(ii),(iv), pp. 29–31, is the relevant conditional input.
For divisor-bounded \(a,b\), put
\[
A_M(s)=\sum_{m\sim M}a(m)m^{-s},\quad
S_H(x)=\sum_{\substack{x<mn\le x+H\\m\sim M}}a(m)b(n).
\]
Assume \(1\le W\le X^{\epsilon/1000}\),
\(X^\epsilon\le M\le HX^{-\epsilon}\), \(H\ge X^{2\epsilon}\).
Then:

| Hypothesis | Additional range | Controlled expression |
|---|---|---|
| \(\sup_{W\le |t|\le XW/H}|A_M(1+it)|\le W^{-1/3}\) | \(H\le H_2\le X/W^4\) | \(D=S_H-(H/H_2)S_{H_2}\) |
| \(\sup_{|t|\le XW/H}|A_M(1+it)|\le W^{-1/3}\) | \(H\le X\) | \(D=S_H\) |

The conclusion is \(|D|\le HW^{-1/10}\) outside measure
\(O_{\epsilon,C}(X\log^{O_C(1)}X/W^{1/10})\). Its proof, equations
(3.7)–(3.8), gives
\[
X^{-1}\int_X^{2X}|D(x)|^2\,dx
\ll_{\epsilon,C}H^2\log^{O_C(1)}X/W^{3/10}.
\tag{3}
\]
Section 3.5, p. 38, uses \(W=\log^{100A}X\) for \(\mu,\Lambda\);
the power choice there concerns divisor functions.
[Primary text](https://arxiv.org/pdf/2411.05770v2).

## 3. What the modern input would and would not settle here

The following are consequences and proposed applications, not claims made
by the cited authors.

At \(H=X^{3/4}\), all surviving lengths
\(X^{11/24}<M\le2B X^{13/24}\) in (1) satisfy the length condition of
Lemma 3.5(ii),(iv), for a sufficiently small fixed \(\epsilon>0\) and
large \(X\). Normalize \(b_V\) by \(\log(3X)\) before invoking a literal
divisor-bounded coefficient hypothesis; restore the logarithm afterwards.
Support cutoffs and terminal partial dyadic blocks must be retained.

The new hypothesis needed for a power-saving application would be, for some
fixed \(\omega>0\),

\[
\sup_{|t|\le X^{1/4+\omega}}
\left|\sum_{\substack{m\sim M\\m>U}}
\frac{\mu(m)}{m^{1+it}}\right|
\le X^{-\omega/3}
\tag{4}
\]

uniformly over the required blocks, with compatible constants and the
lemma's upper restriction on \(\omega\). This is a candidate missing input,
not an available estimate. Even the value \(t=0\) demands polynomial
cancellation of the Möbius coefficients. Generic coefficient norms do not
give (4). A full family of such uniform bounds is much stronger than the
logarithmic cancellation currently supplied by the cited applications.

Dropping \(|t|<W\) changes the theorem to the first line of the table: it
controls only a difference between short and longer sums. The longer-sum
response remains. It cannot be erased merely because \(\int w=0\), since
that response need not be constant and (2) already displays a nonzero
linear component. Recovering that missing response is an additional
arithmetic problem.

Using \(W=(\log X)^L\) in (3) produces logarithmic savings. For orientation,
the existing short-interval transfer has a factor of order \(X^2/H^2\):
a bound \(XH^2(\log X)^{-A}\) therefore leads to order
\(X^3(\log X)^{-A}\), after allowing other logarithmic factors.
No fixed \(A\) gives \(X^{3-\kappa}\) for a fixed \(\kappa>0\).
The exceptional-set formulation alone has the same issue: its logarithmic
measure and a crude bound on the exceptional part do not yield a power.

Consequently a useful future arithmetic theorem should preserve the
centering in (2), or estimate signed products of the actual factors
directly. Importing a pointwise bound for every Möbius factor is a clean
sufficient route but may impose substantially more cancellation than the
original centered question needs.

## 4. A signed pilot with two distinguishable failure modes

This section is an elementary proposal derived from (2).
Use the real \(L^2(X,2X)\) inner product and put
\[
\lambda_X=\frac{\langle B_X,x\rangle}{\langle x,x\rangle},
\qquad \langle x,x\rangle=\frac73X^3,\qquad
B_X^\perp=B_X-\lambda_Xx.
\]
Orthogonality gives the exact decomposition
\[
\boxed{\quad
Q_X:=\|B_X+c_wM_1(U)x\|_2^2
=\|B_X^\perp\|_2^2+
\frac73X^3|\lambda_X+c_wM_1(U)|^2.
\quad}
\tag{5}
\]
Thus the proposed power-saving target \(Q_X\ll X^{3-\kappa}\) is
equivalent to the simultaneous estimates
\[
\|B_X^\perp\|_2^2\ll X^{3-\kappa},
\qquad
|\lambda_X+c_wM_1(U)|\ll X^{-\kappa/2}.
\tag{6}
\]
These are unproved. Equation (5) makes a pilot more informative by
separating the fluctuating shape from the cancellation of the continuum
coefficient.

For several actual coefficient ranges, record:

1. \(M_1(U)\), \(c_wM_1(U)\), \(\lambda_X\), and their mismatch.
2. Both nonnegative terms in (5), their sum, and the original prime
   variance; check the norm comparison justified by (2).
3. The three signed expansion terms
   \[
   I_0=\int B_X^2,\quad
   I_1=2c_wM_1(U)\int xB_X(x)\,dx,\quad
   I_2=\tfrac73c_w^2M_1(U)^2X^3.
   \]
   Their sum must agree with \(Q_X\).
4. If \(B_X=\sum_j B_{X,j}\) is split into factor blocks, retain the
   signed Gram entries \(\int B_{X,i}B_{X,j}\). Comparing their signed
   sum with the sum of absolute entries diagnoses cancellation discarded
   by a coefficient-norm bound.

Use stable direct evaluation of the centered sum, alongside the expansion,
because subtraction between \(I_0,I_1,I_2\) can lose numerical precision.
Record quadrature refinement, arithmetic cutoff conventions, and the
verified range. A finite pilot verifies identities and distinguishes
candidate mechanisms. It cannot establish (6) at all heights.

## 5. Why generic balanced Type II norms cannot suffice

Here is a simple obstruction independent of any unproved prime theorem.
Choose a point \(t_0\) in the support where \(w(t_0)\ne0\), and a small
closed neighborhood on which \(w\) has constant sign and
\(|w|\ge c>0\). Choose \(x_0=rX\), \(1<r<2\), and short relative
intervals of integers
\[
m\in[\alpha\sqrt X,(\alpha+\eta)\sqrt X],\qquad
n\in[\beta\sqrt X,(\beta+\eta)\sqrt X],
\]
where \(\alpha\beta=rt_0\). For a fixed sufficiently small \(\eta>0\)
and an \(x\)-interval of length \(c'X\) about \(x_0\), every ratio
\(mn/x\) lies in that neighborhood.

Take the two coefficient sequences to be indicators of these intervals.
They are bounded by one and supported inside the permitted balanced
factor range for all large \(X\). There are \(\asymp X\) contributing
pairs, all with the same sign. Hence the smooth bilinear sum has
amplitude \(\gg X\) on an interval of length \(\gg X\), and its squared
shell norm is \(\gg X^3\).

This rules out a power improvement from balanced support and generic
divisor bounds alone. It does not rule out estimates using the actual
Möbius signs, the convolution identities, or the signed centering.
Those are exactly the structures the next theorem or pilot must retain.
