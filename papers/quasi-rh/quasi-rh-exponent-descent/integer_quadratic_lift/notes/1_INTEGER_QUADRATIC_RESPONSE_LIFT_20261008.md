# A complete integer prime response in a quadratic character family

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
The deductions and same-model checks below are not independent specialist
validation. No new arithmetic moment estimate or zero-free region is proved.

There is an elementary family lift of the **complete integer prime
response**, including every prime power. Odd square rows reproduce it up
to an explicit error of size logarithmic in the row range. This resolves
the identity-and-error part of Route E1 of the
[continuation](../../notes/CODEX_CONTINUATION_20261008.md), without replacing integer
coefficients by ideal coefficients. The required new mean square remains
open. The classical squarefree quadratic large sieve does not supply it;
its extension to these rows retains a term that gives no exponent gain.

## 1. Inherited response and notation

Use the fixed real probe from the prime-variance project, with
\(w\) supported in \([A,B]\subset(0,\infty)\), \(A=e^{-1/4}\),
\(B=e^{1/4}\), and \(\int w=0\). Its complete response is

\[
V_g(x)=\sum_{n\ge2}\Lambda(n)w(n/x),\qquad
\mathcal V_g(X)=\int_X^{2X}|V_g(x)|^2\,dx.                 \tag{1}
\]

The inherited equivalence is
\(\mathcal V_g(X)=O(X^{1+2\beta})\) if and only if every nontrivial
zeta zero has real part at most \(\beta\), for \(1/2\le\beta\le1\).
The scalar version uses \(q=7/3\),

\[
\ell(v)=\int_1^2 y w(v/y)\,dy,\quad
S_1(X;\ell)=\sum_n\Lambda(n)\ell(n/X)=qX\lambda(X).        \tag{2}
\]

The probe \(\ell\) is supported in \([A,2B]\), has zero ordinary
moment, and has the nonzero logarithmic moment specified in the
[scalar detector](../../../prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/SCALAR_DETECTOR_20261004.md).
Its Mellin transform is nonzero at every forbidden zeta zero. These are
inherited theorems, not consequences of character orthogonality.

For a positive odd integer \(u\), let
\(\chi_u(n)=(n/u)\) be the Jacobi symbol, with \(\chi_1(n)=1\).
Every symbol retains its zeros when \((n,u)>1\). This is a new integer
quadratic family, not the Eisenstein sextic family of the amplification
project. No moment theorem is transferred between the two families.

## 2. Exact square rows and a uniform deletion bound

Let \(L\) be any fixed bounded profile supported in
\([A_L,C_L]\subset(0,\infty)\), and define

\[
S_u(X;L)=\sum_{n\ge2}\Lambda(n)\chi_u(n)L(n/X).
\]

For every odd positive integer \(b\), not necessarily prime or squarefree,

\[
\begin{split}
S_{b^2}(X;L)&=S_1(X;L)-E_b(X;L),\\
E_b(X;L)&=\sum_{p\mid b}\log p\sum_{k\ge1}L(p^k/X).
\end{split}                                                   \tag{3}
\]

This is exact: \(\chi_{b^2}(n)=\mathbf1_{(n,b)=1}\), and
\(\Lambda(n)\) is supported on prime powers. No prime-counting theorem,
Möbius estimate, or zero hypothesis is needed.

Put \(r_L=\log(C_L/A_L)\). For a fixed prime, at most
\(1+r_L/\log p\) of its powers lie in the profile window. Hence

\[
|E_b(X;L)|\le\|L\|_\infty
 [\log\operatorname{rad}(b)+r_L\omega(b)]
\le C_L'\log b\quad(b\ge3),                              \tag{4}
\]

where one may take
\(C_L'=\|L\|_\infty(1+r_L/\log3)\), since \(b\) is odd.
Set \(E_1=0\). The bound holds for every real \(X>0\), including
windows cutting a prime-power sequence at either endpoint. In particular,
all \(b^2\le H\) have error \(O_L(\log(2H))\).

There are exactly

\[
R(H)=\#\{1\le b\le\sqrt H:b\text{ odd}\}
=\left\lfloor\frac{\lfloor\sqrt H\rfloor+1}{2}\right\rfloor
\asymp\sqrt H                                                     \tag{5}
\]

distinct square rows. Composite roots supply the full square-root count;
no prime-density loss is necessary for this prime-response lift.

## 3. The complete Hilbert space lift

On \(y\in[1,2]\), set

\[
F_X(y)=V_g(Xy),\qquad
T_u(X;y)=\sum_n\Lambda(n)\chi_u(n)w(n/(Xy)).
\]

Equation (3), with the original physical window, yields
\(T_{b^2}=F_X-E_b\). The deletion bound is uniform in \(y\), so
\(\|E_b\|_{L^2[1,2]}\ll_w\log(2H)\) for \(b^2\le H\).
Minkowski's inequality in the direct sum of these \(R(H)\) Hilbert spaces
gives

\[
\boxed{\quad
\|F_X\|_2\le R(H)^{-1/2}
\left(\sum_{\substack{u\le H\\u\ {
m odd}}}\|T_u(X;\cdot)\|_2^2\right)^{1/2}
+C_w\log(2H).\quad}                                      \tag{6}
\]

Only a positive sum of whole row norms is enlarged. No arithmetic
selector is inserted into a transform. Both the variation across the full
physical shell and all prime powers survive. The continuum contribution
in (1) is exactly zero because \(\int w=0\); no nonzero term from a
Vaughan decomposition has been omitted.

Suppose, as a **new unproved input**, for fixed \(h>0\), \(a\ge0\),
and every \(\varepsilon>0\), that

\[
\mathcal E_w(X,X^h):=
\sum_{\substack{u\le X^h\\u\ {
m odd}}}\|T_u(X;\cdot)\|_2^2
\ll_{w,h,a,\varepsilon}X^{1+a+h+\varepsilon}               \tag{7}
\]

for every sufficiently large real \(X\). Since
\(\mathcal V_g(X)=X\|F_X\|_2^2\), (6) proves

\[
\mathcal V_g(X)\ll X^{2+a+h/2+\varepsilon}+X\log^2X,
\qquad
\beta_{\rm out}=\frac12+\frac a2+\frac h4.                \tag{8}
\]

When \(1/2\le\beta_{\rm out}<1\), apply the inherited strip equivalence
at every exponent slightly larger than \(\beta_{\rm out}\) and intersect
the resulting closed strips. The resulting zero bound is
\(\Re\rho\le\beta_{\rm out}\). This use of every epsilon does not assume
that a rightmost zero exists or that its height is bounded.

The weaker scalar moment hypothesis

\[
\mathcal E_L(X,X^h):=
\sum_{\substack{u\le X^h\\u\ {
m odd}}}|S_u(X;\ell)|^2
\ll X^{1+a+h+\varepsilon}                                \tag{9}
\]

suffices for the same conclusion by (3) and the inherited scalar detector.
The exact normalization is \(S_1=qX\lambda\). The deletion error in
\(\lambda\) is \(O(\log X/X)\), far below the endpoint response scale.
The norm hypothesis (7) implies (9) by Cauchy in \(y\).

For orientation only, a hypothetical lossless theorem at \(h=1\) gives
\(\beta_{\rm out}=3/4\); at \(h=1/2\) it gives \(5/8\).
To improve an existing \(\beta_0\), the condition is
\(a+h/2<2\beta_0-1\). Arbitrarily small fixed positive \(h\), with
\(a\to0\), would imply RH directly. These moments are not supplied by
zeta-only quasi-RH. They control many quadratic twists as well as the
coherent principal rows.

## 4. Exact primitive grouping exposes the coherent component

Every odd row has a unique decomposition \(u=ab^2\) with \(a\) odd and
squarefree; \((a,b)=1\) is **not** required. For example \(u=27\) has
\(a=b=3\). The exact identity is

\[
\begin{split}
\chi_{ab^2}(n)&=\chi_a(n)\mathbf1_{(n,b)=1},\\
S_{ab^2}(X;L)&=S_a(X;L)-E_{a,b}(X;L),\\
E_{a,b}(X;L)&=\sum_{p\mid b}\log p\sum_{k\ge1}
                 \chi_a(p^k)L(p^k/X).
\end{split}                                                   \tag{10}
\]

Primes shared by \(a\) and \(b\) contribute zero in the last line.
The same bound (4) applies. Define

\[
\mathcal M_L(X,H)=
\sum_{\substack{a\le H\\a\ {
m odd\ squarefree}}}
R(H/a)|S_a(X;L)|^2.
\]

The vector triangle inequality proves

\[
\left|\sqrt{\mathcal E_L(X,H)}-\sqrt{\mathcal M_L(X,H)}\right|
\ll_L H^{1/2}\log(2H).                                   \tag{11}
\]

There is an identical statement for the Hilbert space energy. In
particular, the term \(R(H)|S_1|^2\) is an actual coherent component of
the moment, not a fluctuation that averaging can remove. A theorem about
squarefree or primitive nonprincipal rows does not control it. The square
rows alone essentially restate the target: if
\(\mathcal E_{\rm sq}=\sum_{b\ {
m odd},\,b^2\le H}|S_{b^2}|^2\),
then

\[
\left|R(H)^{-1/2}\sqrt{\mathcal E_{\rm sq}}-|S_1|\right|
\ll_L\log(2H).                                           \tag{12}
\]

Thus the new lift does not manufacture independent witnesses. It precisely
identifies the principal component that a useful family estimate must
bound. Deleting that component also deletes this replication argument.

## 5. A complete signed prime-pair kernel

The finite scalar moment expands exactly as

\[
\mathcal E_L(X,H)=\sum_{n,m\ge2}\Lambda(n)\Lambda(m)
L(n/X)\overline{L(m/X)}\,\mathcal K_H(n,m),
\quad
\mathcal K_H(n,m)=\sum_{\substack{u\le H\\u\ {
m odd}}}
\left(\frac{nm}{u}\right).                               \tag{13}
\]

The Hilbert version replaces the two profile factors by
\(\int_1^2w(n/(Xy))\overline{w(m/(Xy))}\,dy\). Both sums are finite;
the full product window, continuum preparation, and prime-power terms
are retained. In particular,

\[
\mathcal K_H(p,p)=\#\{u\le H:u\ {
m odd},\ p\nmid u\},
\]

which is not the unmasked odd-row count. Reality or positivity of the
whole energy does not make all its signed pair contributions positive.
A useful arithmetic estimate would bound this whole form with its actual
profile signs, to the scale (7) or (9).

The fixed-delay scalar from the
[arithmetic feedback note](../../fixed_scale_descent/notes/3_ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md)
also lifts with no additional identity problem. For fixed \(c>1\),
\(0<r<1\), define \(L(v)=\ell(v)-rc^\beta\ell(cv)\). Then

\[
S_1(X;L)=qX[\lambda(X)-rc^{\beta-1}\lambda(X/c)].          \tag{14}
\]

Its support is \([A/c,2B]\), its ordinary moment is zero, and
\(q^{-1}\int L(v)v^{z-1}dv=D(z)(1-rc^{\beta-z})\). Equations (3)--(13)
apply to this entire signal, with constants depending on the fixed
\(\beta,c,r\). If it is re-expanded into mixed Möbius/von Mangoldt
terms, both moving cutoffs, both continua, and the inherited
\(O(X^{-7/12})\) comparison must still be kept. The lift itself has no
such decomposition error.

## 6. What the classical squarefree large sieve actually gives

Heath-Brown's [Theorem 1, p. 237](https://matwbn.icm.edu.pl/ksiazki/aa/aa72/aa7234.pdf)
states

\[
\sum_{a\le Q}^{*}\left|\sum_{n\le N}^{*}c_n(n/a)\right|^2
\ll_\varepsilon(QN)^\varepsilon(Q+N)\sum_{n\le N}^{*}|c_n|^2, \tag{15}
\]

where both stars restrict to positive odd squarefree integers. This
source theorem is used as an input; its proof is not replayed here.
The following application and its limitation are deductions in this note.

First separate the odd-prime terms of \(S_u\) from higher prime powers
and the prime 2. Elementary counting bounds the latter uniformly by
\(O_L(X^{1/2}\log^2(2X))\), whose full-row squared norm is
\(O_L(HX\log^4(2X))\). For each fixed odd \(b\le\sqrt H\), apply
(15) to \(a\le H/b^2\) with coefficients

\[
c_p=\log p\,L(p/X)\mathbf1_{p\nmid b}
\]

on odd primes. These coefficients do not depend on \(a\), and their
squared norm is \(O_L(X\log^2(2X))\) by elementary counting. The
decomposition \(u=ab^2\) and \(\sum b^{-2}=O(1)\) give

\[
\boxed{\quad
\mathcal E_L(X,H)\ll_{L,\varepsilon}
(HX)^\varepsilon[HX+X^2\sqrt H]\quad(X,H\ge2).
\quad}                                                     \tag{16}
\]

Small changes to epsilon absorb the displayed logarithms. The same proof
applies at every \(y\in[1,2]\) with uniform coefficient norms, and can
be integrated to give (16) for \(\mathcal E_w\). Restoring higher prime
powers here is an upper-bound step; none were deleted from the exact lift.

Dividing (16) by \(R(H)\asymp\sqrt H\) and taking square roots leaves

\[
|S_1(X;L)|\ll (HX)^\varepsilon
[X^{1/2}H^{1/4}+X]+O_L(\log(2H)).                        \tag{17}
\]

The \(X\) term prevents any sublinear power bound. In particular,
replacing (15)'s squarefree row set by all rows and keeping just
\((H+X)\sum|c_n|^2\) would be an invalid theorem transfer. The simple
coherent-row lower bound explains the error independently of the proof:
nonnegative prime coefficients make every square row essentially a copy
of their full sum.

## 7. A conductor localization of the new moment

For \(1<h<2\), \(H=X^h\), put \(A_0=X^2/H=X^{2-h}\).
The squarefree-kernel range \(a>A_0\) already fits the lossless target.
Indeed, on a dyadic block \(A<a\le2A\le2H\),
\(R(H/a)\ll\sqrt{H/A}\). Apply (15) to the odd-prime part of
\(S_a\), then sum the resulting geometric block bounds. The higher
prime powers contribute \(O(HX\log^4(2X))\). Thus

\[
\sum_{\substack{A_0<a\le H\\a\ {\rm odd\ squarefree}}}
R(H/a)|S_a(X;L)|^2
\ll_{L,\varepsilon}(HX)^\varepsilon
 [HX+X^2\sqrt{H/A_0}]
\ll (HX)^{1+\varepsilon}.                               \tag{18}
\]

Endpoint blocks may be partial; positive enlargement into a full dyadic
block is permitted. No cancellation between different blocks is assumed.
The same estimate holds for the profile-valued norm. Equation (11) pays
for replacing primitive rows by their original masked copies.

Consequently the following precise remaining scalar input is sufficient
for (9) with loss \(a=0\):

\[
\boxed{\quad
\sum_{\substack{a\le X^{2-h}\\a\ {\rm odd\ squarefree}}}
\frac{|S_a(X;\ell)|^2}{\sqrt a}
\ll_{h,\varepsilon} X^{1+h/2+\varepsilon},
\qquad 1<h<2.\quad}                                    \tag{19}
\]

In fact \(R(H/a)\asymp\sqrt{H/a}\) for \(a\le H\), so (11) shows
that (19) is also necessary at this exponent if the full moment (9)
holds, with the usual epsilon convention. The error
\(H\log^2(2H)\) is smaller than \(HX\). For the odd squarefree kernel,
\(\chi_a\) is primitive modulo \(a\) (with \(a=1\) the principal
character), so this is a genuine conductor localization.

For example, choose \(h=7/5\). The remaining conductor range is
\(a\le X^{3/5}\), its weighted energy target is
\(X^{17/10+\varepsilon}\), and the conditional zero boundary is
\(17/20<7/8\). The \(a=1\) term in (19) already requires precisely
the improved scalar power \(|S_1|\ll X^{17/20+\varepsilon}\).
This is not an easier proof of that power merely by renaming it. It
identifies a complete signed family obligation and shows that the larger
conductor range needs no new theorem for this first bounded target.
At \(h\le1\), the same cutoff is at or beyond \(H\), so this large
conductor argument gives no useful complementary range. In particular,
it is not an RH iteration theorem.

## 8. Changed next task and finite checks

The bridge identity is now complete. A next analytic task is to prove
the localized weighted estimate (19), or improve the signed form (13)
with the original prepared prime coefficients below
the \(X^2\sqrt H\) term in (16). At \(H=X\), the proposed lossless
target is \(X^{2+\varepsilon}\), compared with the available
\(X^{5/2+\varepsilon}\) upper bound. This is a substantial new estimate,
not a small correction to the classical theorem. The principal component
(12) is an obligatory check on every proposed argument.

The [finite check script](../../numerics/check_integer_quadratic_lift.py)
verifies the Jacobi masks, unique squarefree decomposition, exact
prime-power deletion coefficients, full signed Gram identity, and
exponent bookkeeping using integer and rational arithmetic. It includes
shared factors between \(a\) and \(b\), composite roots, boundary rows,
and the diagonal mask countercheck. It does not test a conjectural
asymptotic moment numerically or certify a new strip.
