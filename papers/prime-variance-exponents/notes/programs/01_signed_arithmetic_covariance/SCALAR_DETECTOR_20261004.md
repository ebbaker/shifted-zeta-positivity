# The centered scalar alone detects the full variance exponent

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
These are new internal deductions from the existing manuscript and the
previously proved Landau lemma, not independent specialist refereeing.
No new global exponent, zero-free strip, or arithmetic estimate is proved.
No mathematical priority claim is made.

## 1. Outcome and corrected role of the projection split

The [preliminary investigation](PRELIMINARY_INVESTIGATION_20261004.md)
splits the centered Vaughan energy into a projected Gram term and a scalar
mismatch. That orthogonal identity remains exact on every shell. There is,
however, a stronger conclusion for the **actual arithmetic response and an
estimate on all sufficiently large real shells**:

> A power bound for the centered scalar mismatch alone is equivalent to the
> full variance bound at the same exponent. Even an eventual bound for only
> one sign of that scalar suffices. Subpower losses recover the exact endpoint.

Thus a separate projected Gram estimate is not a logically independent
global requirement once the complete scalar estimate is proved. This uses
the noncancellation theorem for the fixed arithmetic probe and, for the
one-sided version, the Landau argument. It is not a generic consequence of
orthogonal projection or a bound on one shell. The scalar estimate remains
unproved and already has the full fixed-strip strength of the program.

## 2. Exact scalar kernel and its transform

Use the fixed real probe, support constants A=e^(-1/4), B=e^(1/4), and
plus-exponent transform G from the [manuscript](../../../manuscript.tex).
Put q=7/3 and define

\[
\lambda_V(X)=\frac{\int_X^{2X}xV_g(x)\,dx}{qX^3},\qquad
S(X)=X\lambda_V(X),\qquad
\ell(u)=\int_1^2 y\,w(u/y)\,dy.
\tag{1}
\]

For every real X>0, substitution x=Xy gives

\[
S(X)=\frac1q\int_1^2 yV_g(Xy)\,dy
=\frac1q\sum_{n\ge2}\Lambda(n)\ell(n/X).
\tag{2}
\]

The sum is finite and keeps exactly the complete physical product window
AX<=n<=2BX. In particular, the support of ell is contained in [A,2B],
and the kernel vanishes at both ends. An alternative exact formula is

\[
\ell(u)=u^2\int_{u/2}^{u}w(t)t^{-3}\,dt.
\tag{3}
\]

This is an averaged signed probe, not a nonnegative kernel. Its ordinary
and logarithmic moments retain the preparation and continuum:

\[
\int_0^\infty\ell(u)\,du=q\int w=0,\qquad
\frac1q\int_0^\infty\ell(u)\log u\,du
=\int w(u)\log u\,du=c_w\ne0.
\tag{4}
\]

For the second identity write u=yt inside (1); the extra log y term is
multiplied by the zero ordinary moment of w. The nonzero constant c_w is
the one in the [Vaughan reduction](../../MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md).

Let

\[
W(z)=\int_0^\infty w(u)u^{z-1}\,du=G(1/2-z),\qquad
K(z)=\int_1^2 y^{z+1}\,dy
=\frac{2^{z+2}-1}{z+2},
\]
\[
D(z)=\frac1q\int_0^\infty\ell(u)u^{z-1}\,du
=\frac1qW(z)K(z).
\tag{5}
\]

All three functions are entire; K(-2)=log 2 is the removable value.
The only zeros of K are

\[
-2+\frac{2\pi i j}{\log2},\qquad j\in\mathbb Z\setminus\{0\}.
\tag{6}
\]

The manuscript proves G(1/2-rho)!=0 for every nontrivial zero rho with
Re rho>1/2. Equation (6) therefore gives

\[
D(\rho)\ne0\qquad(\rho\text{ nontrivial},\ \Re\rho>1/2).
\tag{7}
\]

Also K(1)=q, D(1)=0, and D'(1)=c_w. The zero of D at one is simple.
The averaging has introduced no new cancellation in the half-plane relevant
to a forbidden zero.

## 3. True transforms and the initial cap

Since S(X)=0 for 0<X<A, the full multiplicative integral has no lower
endpoint problem. For Re z>1, absolute termwise integration in (2) gives

\[
\int_0^\infty S(X)X^{-z-1}\,dX
=D(z)\sum_{n\ge2}\Lambda(n)n^{-z}
=-D(z)\frac{\zeta'}{\zeta}(z).
\tag{8}
\]

One can instead use the true one-sided logarithmic Laplace transform

\[
\mathcal L_S(z)=\int_0^\infty e^{-zt}S(e^t)\,dt.
\]

Unlike the original p_g transform in the manuscript, this averaged probe
has a small initial cap. Its full logarithmic support starts at t=-a,
a=1/4. Only n=2 contributes on -a<=t<0: the n=3 packet starts at
log(3/(2B))>0. Consequently, for Re z>1,

\[
\boxed{\quad
\mathcal L_S(z)=-D(z)\frac{\zeta'}{\zeta}(z)-C_0(z),\qquad
C_0(z)=\frac{\log2}{q}\int_{-a}^0 e^{-zt}\ell(2e^{-t})\,dt.
\quad}
\tag{9}
\]

C_0 is entire. Omitting it would make the asserted transform identity
incorrect, although it does not change any pole-detection conclusion.
Starting at any other fixed logarithmic threshold likewise changes the
transform by an entire compact-interval correction. Moving shell cutoffs
are not substituted into (8) or (9).

## 4. Scalar, strip, and energy equivalence

Fix 0<=kappa<=1 and put b=1-kappa/2. Each of the following statements,
with estimates on all sufficiently large real X, is equivalent:

1. |lambda_V(X)|=O(X^(-kappa/2)).
2. For every epsilon>0,
   |lambda_V(X)|=O_epsilon(X^(-kappa/2+epsilon)).
3. Every nontrivial zero satisfies Re rho<=b, equivalently
   |Re rho-1/2|<=(1-kappa)/2.
4. The exact energy satisfies mathcal V_g(X)=O(X^(3-kappa)).

**Proof.** Statement 1 implies 2. Under 2, S(X)=O_epsilon(X^(b+epsilon)).
For every sigma>b choose epsilon<sigma-b. The integral in (8), or the
true one-sided integral in (9), then converges absolutely and locally
uniformly in Re z>b, and is holomorphic there. Compact initial intervals
cause no problem. Meromorphic uniqueness identifies this holomorphic
transform with the right side of (8) or (9).

The pole of zeta at one is canceled by D(1)=0. If a nontrivial zero rho
of multiplicity m_rho had Re rho>b>=1/2, (7) would leave the nonzero
simple residue

\[
\mathop{\rm Res}_{z=\rho}
\left(-D(z)\frac{\zeta'}{\zeta}(z)\right)
=-m_\rho D(\rho).
\tag{10}
\]

That contradicts holomorphy. This proves 3; the reflected boundary follows
from the functional equation. The manuscript's fixed-exponent theorem
gives 3 implies 4. Finally Cauchy--Schwarz gives

\[
|\lambda_V(X)|
\le\frac{\|V_g\|_{L^2(X,2X)}}{\sqrt q\,X^{3/2}},
\tag{11}
\]

so 4 implies 1. QED.

This proves the subpower endpoint directly: no uniform constants or
starting thresholds in epsilon are required. Boundary zeros are allowed.
Multiplicity changes the residue in (10), not the pole order. In
particular, an exact scalar envelope gives at most an O(1/epsilon)
transform bound when approaching a boundary pole from the right, which
is compatible with a simple pole. At b=1/2, some boundary coefficients
may themselves vanish; this is irrelevant because only zeros strictly
to the right have to be excluded. No convergence on the boundary line is
asserted, and no rightmost zero or spectral gap is assumed.

The quantifier is all sufficiently large real X. A finite numerical range
or an estimate only at selected sampled scales does not meet the hypothesis
of this proof without an additional uniform interpolation argument.

## 5. Either one-sided scalar envelope suffices

The equivalent assertions in section 4 can be supplemented by either of
the following assertions separately:

\[
\lambda_V(X)\le C X^{-\kappa/2}\quad\text{eventually},
\qquad\text{or}\qquad
\lambda_V(X)\ge-C X^{-\kappa/2}\quad\text{eventually}.
\tag{12}
\]

Either one, with some C>=0, suffices; they are not assumed jointly.
The same statement holds if the chosen sign has an arbitrary subpower
loss, meaning that its corresponding inequality holds with
C_epsilon X^(-kappa/2+epsilon) for every epsilon>0.

**Proof.** This is the Landau mechanism proved in
[One-sided continuation, sections 1--3](../../../../investigations/sonin-critical-boundary/notes/GLOBAL_GROWTH_ONE_SIDED_20261003.md),
applied to the new exact transform (9). Details follow to specify the
different probe and cap.

The elementary Chebyshev bound and compact support give S(e^t)=O(e^t)
as t tends to infinity. In the upper-envelope case define, for a fixed
sufficiently large t_0>=0,

\[
f(t)=\mathbf1_{[t_0,\infty)}(t)
\bigl(Ce^{bt}-S(e^t)\bigr)\ge0.
\tag{13}
\]

Its real Laplace convergence abscissa sigma_c is at most one, or is minus
infinity. Initially in Re z>1 its transform equals

\[
\mathcal L_f(z)=\frac{Ce^{-(z-b)t_0}}{z-b}
-\mathcal L_S(z)+\int_0^{t_0}e^{-zt}S(e^t)\,dt.
\tag{14}
\]

The meromorphic expression on the right is holomorphic near every real
z>b. Indeed zeta has no positive real zero: for 0<z<1 this follows from
the positive alternating eta series and the negative denominator
1-2^(1-z), while for z>1 it follows from its positive convergent series.
The pole at z=1 is removed by D(1)=0. Both finite-interval corrections
are entire, and the majorant's possible pole lies at z=b.

If sigma_c>b, meromorphic uniqueness continues (14) throughout its
convergence half-plane and supplies a holomorphic continuation near the
real point sigma_c. The Landau lemma for a nonnegative Laplace transform
forbids this. Hence sigma_c<=b. In particular, for every sigma>b,

\[
\int_{t_0}^\infty e^{-\sigma t}|S(e^t)|\,dt
\le\int_{t_0}^\infty e^{-\sigma t}
\bigl(Ce^{bt}+f(t)\bigr)\,dt<\infty.
\tag{15}
\]

Thus (9) is a true holomorphic transform in Re z>b and the residue
argument in section 4 gives the closed strip and exact energy. The lower
envelope uses f=1_[t_0,infinity)(Ce^(bt)+S(e^t)) instead. Conversely the
two-sided estimate from section 4 supplies each one-sided envelope.

For the subpower version apply the argument with b+epsilon, using
arbitrarily small positive epsilon, and intersect the resulting closed
right-half-plane restrictions. The exact strip Re rho<=b follows and
the manuscript recovers the exact variance endpoint and hence the exact
two-sided scalar bound. QED.

For clarity, the only positivity here is the nonnegative tail (13), which
is available **after** the hypothetical one-sided inequality. Holomorphic
continuation near the positive real axis alone supplies no estimate for
the signed response and cannot create that tail. Nothing in this argument
proves either inequality in (12).

## 6. Transfer to the complete centered Vaughan scalar

Use U=V=X^(11/24), held fixed as x varies on [X,2X], and retain the exact
centered response

\[
T_X(x)=B_{U,V}(x)+c_wM_1(U)x,
\quad A_U(m)=\sum_{d\mid m,\ d>U}\mu(d),
\quad M_1(U)=\sum_{d\le U}\frac{\mu(d)}d.
\]

Its scalar is precisely

\[
\boxed{\quad
J(X):=\frac{\langle T_X,x\rangle}{qX^3}
=c_wM_1(U)+\frac1{qX}
\sum_{m>U,n>V}A_U(m)\Lambda(n)\ell(mn/X).
\quad}
\tag{16}
\]

This formula retains all prime powers in Lambda, the exact product window
AX<=mn<=2BX, and every terminal partial block. Partitioning m into the
preliminary note's complete blocks gives J=c_wM_1(U)+sum_j lambda_j.
The continuum coefficient is not discarded or separately bounded.

The [proved Vaughan error](../../MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md)
is ||T_X-V_g||_2=O(X). Therefore

\[
|J(X)-\lambda_V(X)|
\le\frac{\|T_X-V_g\|_2}{\sqrt q\,X^{3/2}}
=O(X^{-1/2}).
\tag{17}
\]

For 0<=kappa<=1 this error fits every exact or subpower envelope above,
including kappa=1. Consequently **each** of the following all-real-X
conditions alone is equivalent to mathcal V_g(X)=O(X^(3-kappa)):

\[
|J(X)|\ll X^{-\kappa/2+o(1)},\qquad
J(X)\le C_\epsilon X^{-\kappa/2+\epsilon}\ (\forall\epsilon>0),
\qquad
J(X)\ge-C_\epsilon X^{-\kappa/2+\epsilon}\ (\forall\epsilon>0).
\tag{18}
\]

The exact envelopes without o(1) or epsilon are equivalent as well. Thus,
at the illustrative audit budget kappa=0.01, it is enough to prove either
J(X)<=C_epsilon X^(-0.005+epsilon) or its lower analogue on all sufficiently
large real X, for every epsilon>0. This is an explicit signed arithmetic
target with the same difficulty class as the full fixed-strip problem;
it is not an available estimate. A bound for B alone or M_1 alone would
be a different, generally stronger obligation.

Once (18) is established, the original energy theorem and (17)'s parent
norm comparison give ||T_X||_2^2=O(X^(3-kappa)); its projected Gram term
then obeys the same bound by contractivity. This explains precisely the
global redundancy of requiring a second independent Gram estimate.

## 7. Why no generic scalar-to-energy inequality is asserted

For an arbitrary response consider V_*(x)=x sin(x^2). Integration by
parts gives

\[
\int_X^{2X}xV_*(x)\,dx=O(X),\qquad
\lambda_*(X)=O(X^{-2}),
\]
\[
\int_X^{2X}|V_*(x)|^2\,dx
=\frac76X^3+O(X).
\tag{19}
\]

Thus even a very small scalar at every scale need not control a generic
response's energy. The proof here uses the exact arithmetic transform,
its forbidden-zero noncancellation, and the manuscript's converse spectral
bound. It produces no shell-local norm inequality and no uniform constant
relating an arbitrary scalar envelope to an arbitrary Gram matrix.

## 8. Verification scope and next arithmetic obligation

The deductions above check the normalization q, the full averaged support,
the kernel moments, the simple preparation zero, the added transform's
zero set, the n=2 initial cap, zero multiplicities, both boundary endpoints,
the all-real-X quantifier, and the centered-Vaughan error exponent.
They require no new numerical input and no additional cited distribution
theorem. The Landau step is reproduced from the existing internally proved
lemma; it is not a new oscillation theorem.

The useful next investigation is whether an actual product-level arithmetic
identity can establish **one sign** of (16) with a fixed power saving while
retaining the continuum and every cap. This reformulation reduces the
number of distinct estimates demanded by the earlier projection plan.
It does not lower the spectral strength of the missing estimate and does
not turn generic coefficient bounds or a factorwise Mertens assumption
into a proved contraction.
