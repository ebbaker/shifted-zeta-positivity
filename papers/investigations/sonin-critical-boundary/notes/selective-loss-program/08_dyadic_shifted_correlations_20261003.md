# Dyadic prime pairs and the remaining arithmetic error

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Internal checks by agents using the inherited model configuration are not
independent specialist review.

This carries out the three continuation steps in the
[handoff](../NEXT_SESSION_SELECTIVE_LOSS_20261003.md). The dyadic pair
weight and its shifted-correlation expansion are exact, including both
boundary caps. An unconditional singular-series mean theorem isolates a
negative arithmetic main term whose leading coefficient cancels the
positive diagonal. The remaining estimate concerns the **signed error of
the actual prime correlations**. That estimate is still open and has RH
strength for this probe. The singular-series calculation is not a theorem
approximating the actual prime pairs.

## 1. Fixed probe and exact pair weight

Keep the normalized real odd probe from notes 04--07:

\[
a=1/4,\quad A=e^{-a},\quad B=e^a,\quad
h(v)=(1-16v^2)^8\mathbf1_{|v|<a},
\]
\[
g=(-h'''+h'/4)/\sqrt\nu,\qquad
\nu=146640624550936576/37921101075.
\]

All functions use zero extensions. Write

\[
w(t)=t^{-1/2}g(-\log t),\quad
V(x)=\sum_{n\ge2}\Lambda(n)w(n/x),\quad
\mathcal V(X)=\int_X^{2X}V(x)^2dx.
\]

Preparation gives \(\int w=0\), and normalization gives
\(\int w^2=\int g^2=1\). For any positive real \(n,m\), define

\[
W_X(n,m)=\int_X^{2X}w(n/x)w(m/x)dx
=X\Omega(n/X,m/X),
\]
\[
\Omega(u,v)=\int_1^2w(u/t)w(v/t)dt.
\tag{1}
\]

For \(n\le m\), put \(M=\sqrt{nm}\) and
\(\delta=\tfrac12\log(m/n)\). Changing variables \(x=Me^z\) gives

\[
\boxed{W_X(n,m)=M\int_L^U e^{2z}
g(z+\delta)g(z-\delta)dz,}
\tag{2}
\]
\[
L=\max\{\log(X/M),-a+\delta\},\qquad
U=\min\{\log(2X/M),a-\delta\}.
\]

The value is zero if \(L\ge U\). Equivalently its integration in
\(x\) is over
\([\max(X,Am),\min(2X,Bn)]\). In particular every nonzero pair has

\[
AX<n,m<2BX,\qquad |\log(m/n)|<2a.
\tag{3}
\]

The untruncated pair weight is the same integral with
\(L=-a+\delta\), \(U=a-\delta\). Only two disjoint blocks of active
pairs differ from it: the lower square \((AX,BX)^2\) and upper square
\((2AX,2BX)^2\). Indeed lower truncation requires \(m<BX\), and
upper truncation requires \(n>2AX\). They cannot both occur since
\(B<2A\). These are pair caps, not permission to discard the corresponding
integers. A pair outside these squares already has its full overlap even
if one packet by itself is partial.

## 2. Exact shifted correlations

Finite expansion of the square gives

\[
\mathcal V(X)=\mathcal D(X)+\mathcal C(X),\qquad
\mathcal D(X)=\sum_{n\ge2}\Lambda(n)^2W_X(n,n),
\]
\[
\boxed{\mathcal C(X)=2\sum_{h\ge1}\sum_{n\ge2}
\Lambda(n)\Lambda(n+h)W_X(n,n+h).}
\tag{4}
\]

Only \(h<2(B-A)X\) contributes. With \(\kappa=B/A-1\), its exact
real support in the first coordinate is

\[
\max(AX,h/\kappa)<n<2BX-h.
\tag{5}
\]

The arithmetic sum also imposes \(n\ge2\); no integer rounding of \(X\)
is needed. Endpoints have weight zero. Thus (4) holds for every real
\(X>0\), including noninteger shells. The signs of \(W_X\) remain inside
the combined sum. Taking a positive part entry by entry would change the
problem.

The diagonal is already \(O_g(X^2\log(2X))\) by note 06. PNT and partial
summation give the sharper leading coefficient

\[
\mathcal D(X)=(3/2+o(1))X^2\log X.
\tag{6}
\]

To see the coefficient, \(\sum_{n\le T}\Lambda(n)^2\sim T\log T\),
with higher powers lower order. Integration against the fixed compact
weight \(W_X(t,t)=X\Omega(t/X,t/X)\) gives coefficient
\(\int\Omega(u,u)du=\int_1^2t\,dt\int w^2=3/2\).
This uses unconditional PNT, not a prime-pair asymptotic. The corresponding
continuum logarithmic diagonal is exactly

\[
\int_0^\infty\log t\,W_X(t,t)dt
=X^2\left[\frac32\log X+2\log2-\frac34\right].
\tag{7}
\]

Here \(\int\log t\,w(t)^2dt=-\int v g(v)^2dv=0\). Formula (7) is
a continuum calculation; (6) alone does not give a constant-order
asymptotic for the actual diagonal.

## 3. Continuum cancellation requires both caps

For each real \(n>0\), finite Fubini gives the exact row cancellation

\[
\int_0^\infty W_X(n,m)dm
=\int_X^{2X}w(n/x)x\,dx\int_0^\infty w(t)dt=0.
\tag{8}
\]

Consequently \(\iint W_X(n,m)dn\,dm=0\). This cancellation is complete
on the finite active band in (3). It does not estimate the arithmetic
discrepancy of its atoms.

There is a direct obstruction to replacing the cap weights by whole
packets. Let \(W_\infty\) integrate over all \(x>0\). On the same active
coordinate band \(\mathcal I_X=(AX,2BX)\),

\[
\iint_{\mathcal I_X^2}W_\infty(n,m)dn\,dm
=\int_0^\infty\left[\int_{AX}^{2BX}w(t/x)dt\right]^2dx
=c_gX^3,\qquad c_g>0.
\tag{9}
\]

For \(X\le x\le2X\) the inner integral is zero; the positive energy
comes from the two exterior intervals. The constant is finite by support
and is positive because a nonzero \(w\) has a nonzero partial integral
on some cap. Thus removing the cap truncations creates an artificial
\(X^3\) continuum main, larger than the requested \(X^2\log X\) scale.

## 4. Collapse of the continuum pair weight to the shift variable

Define the additive autocorrelation of this multiplicative weight by

\[
C_w(q)=\int_0^\infty w(t)w(t+q)dt\quad(q\ge0),\qquad
F(q)=\int_1^2tC_w(q/t)dt,
\]

and extend them evenly to the real line. Then

\[
\boxed{H_X(h):=\int_0^\infty W_X(t,t+h)dt=X^2F(h/X).}
\tag{10}
\]

The function \(F\) is at least \(C^2\), compactly supported in
\([-2(B-A),2(B-A)]\), and

\[
F(0)=3/2,\qquad F'(0)=0,\qquad
\int_0^\infty F(q)dq=0.
\tag{11}
\]

The last identity follows from
\(\int_0^\infty C_w=\tfrac12(\int w)^2=0\) and scaling inside the
\(t\) integral. In particular \(F\) must change sign. It is not the
logarithmic autocorrelation \(\phi\) used in the earlier notes.

The composite trapezoid estimate with integrable \(F''\), for mesh
\(1/X\), now gives uniformly for real \(X\ge1\)

\[
2\sum_{h\ge1}H_X(h)=-\frac32X^2+O_g(X).
\tag{12}
\]

This is the continuum-density-one baseline sampled at integer shifts.
It already contains cancellation between different signs of \(F\).
It is not the correct prime-pair main at each individual shift: parity
alone makes the distinction essential.

## 5. An unconditional singular series main

Let \(\mathfrak S(h)=0\) for odd positive \(h\), and for even \(h\)
use the usual two-prime singular series

\[
\mathfrak S(h)=2\prod_{p>2}\left(1-\frac1{(p-1)^2}\right)
\prod_{p\mid h,\ p>2}\frac{p-1}{p-2}.
\]

[Montgomery and Soundararajan, equation (16)](https://arxiv.org/pdf/math/0409258)
give an unconditional averaged identity for this series. In the present
notation it says, initially for integer \(H\),

\[
T(H):=\sum_{1\le h<H}(H-h)(\mathfrak S(h)-1)
=-\frac12H\log H+\frac{A_{\rm SS}}2H
+O_\epsilon(H^{1/2+\epsilon}),
\tag{13}
\]
\[
A_{\rm SS}=2-\gamma-\log(2\pi).
\]

Piecewise linear interpolation extends (13) to real \(H\ge2\); the
interpolation error of its smooth main is \(O(1/H)\). This input concerns
only the explicit singular series. The next calculation is our application
to the fixed smoothing kernel, rather than a statement about actual
von Mangoldt correlations.

Distributionally \(T''=\sum_{h\ge1}(\mathfrak S(h)-1)\delta_h\).
Twice integrating by parts, using \(T(0)=T'(0)=0\) and compact support,
gives

\[
\sum_{h\ge1}(\mathfrak S(h)-1)F(h/X)
=X^{-2}\int_0^\infty T(t)F''(t/X)dt
=-\frac{F(0)}2\log X+c_F+O_{g,\epsilon}(X^{-1/2+\epsilon}),
\tag{14}
\]
\[
c_F=\frac{A_{\rm SS}}2F(0)
-\frac12\int_0^\infty q\log q\,F''(q)dq.
\]

The integral is finite at zero. Substitution \(t=Xq\) and
\(\int_0^\infty qF''(q)dq=F(0)\) establish the constants and signs.
The bounded interval \(t<2\) contributes \(O_g(X^{-2})\); it is not
covered by using the large-\(t\) error formula at zero. Fix
\(0<\epsilon<1/2\) throughout these asymptotics.

Combining (10), (12), and (14), the complete singular-series off-diagonal
main is therefore

\[
\boxed{\mathcal C_{\rm SS}(X):=
2\sum_{h\ge1}\mathfrak S(h)H_X(h)
=-\frac32X^2\log X+(2c_F-3/2)X^2
+O_{g,\epsilon}(X^{3/2+\epsilon}).}
\tag{15}
\]

Equations (6) and (15) prove
\(\mathcal D(X)+\mathcal C_{\rm SS}(X)=o(X^2\log X)\).
The leading diagonal is thus canceled by this arithmetic model,
unconditionally as a calculation of the model. No estimate for the
difference between the model and the actual prime pairs has been supplied.

## 6. The precise remaining signed arithmetic estimate

Define the actual correlation error, with all caps retained, by

\[
\boxed{\mathcal R(X)=2\sum_{h\ge1}
\left[\sum_{n\ge2}\Lambda(n)\Lambda(n+h)W_X(n,n+h)
-\mathfrak S(h)H_X(h)\right].}
\tag{16}
\]

Then exactly

\[
\mathcal V(X)=\mathcal D(X)+\mathcal C_{\rm SS}(X)+\mathcal R(X).
\tag{17}
\]

The concrete remaining target is

\[
\boxed{\mathcal R(X)_+\le C_gX^2\log(2X)
\quad\text{for every sufficiently large real }X.}
\tag{18}
\]

It is equivalent to the handoff's dyadic target, since the other two
terms in (17) are \(O_g(X^2\log X)\). The positive part is taken only
after every signed error has been added. Under RH the established bounded
\(p\) gives \(\mathcal V(X)=O_g(X^2)\), so (18) has precisely the RH
strength already proved in note 06. This is a more explicit obligation,
not a weakening of that strength.

There is also an exact partial-summation version. For \(X\ge2B\), put
\(l=\max(AX,h/\kappa)\), \(u=2BX-h\), and omit \(l\ge u\). Set

\[
E_{X,h}(t)=\sum_{l<n\le t}\Lambda(n)\Lambda(n+h)
-\mathfrak S(h)(t-l),\qquad l\le t\le u.
\]

Since \(W_X(t,t+h)\) vanishes at both ends,

\[
\mathcal R(X)=-2\sum_h\int_l^u
E_{X,h}(t)\frac{d}{dt}W_X(t,t+h)dt.
\tag{19}
\]

Uniformly in the active shifts,
\(|dW_X(t,t+h)/dt|=O_g(1)\) and
\(\int_l^u|dW_X/dt|dt=O_g(X)\), directly from (1).
These formulas identify exactly the endpoint uniformity and joint signed
summation an arithmetic input must provide.

One may instead center on density one. That gives (12) as the baseline
and an equivalent signed error target. It makes termwise absolute estimates
especially unsuitable: for odd \(h\), a nonzero \(\Lambda(n)\Lambda(n+h)\)
requires the even member to be a power of two. In a nondegenerate block
of length comparable to \(X\), there are only boundedly many such powers,
while the density-one main has size \(X\). Its local cumulative error is
\(-(t-l)+O_g(\log X)\), even before any
unknown even-shift correlations are considered. Singular-series centering
handles this known parity structure.

## 7. Arithmetic input audit and further work

[Matomäki, Radziwiłł, and Tao, Theorem 1.3(i)](https://arxiv.org/pdf/1707.01315)
is an unconditional almost-all-shifts asymptotic, with error
\(O_{A_1,\epsilon}(N\log^{-A_1}N)\), for
\(N^{8/33+\epsilon}\le H\le N^{1-\epsilon}\) and shift center
\(0\le h_0\le N^{1-\epsilon}\), outside
\(O_{A_1,\epsilon}(H\log^{-A_1}N)\) exceptional shifts. The theorem as
stated does not cover all proportional shifts
in (5). Their footnote 6 explains that earlier methods extend to
\(H\asymp N\), so range alone is not an intrinsic obstruction. More
decisively, even granting such an extension, compatible cap weights,
uniform partial sums, and control of exceptional shifts, taking the errors
absolutely yields \(O(X^3\log^{-A_1}X)\). No fixed logarithmic saving
reaches (18). This scale comparison is our inference, not their theorem.

Even a hypothetical uniform square-root error for each shift would give
\(O(X^{5/2+\epsilon})\) by this absolute summation. The task needs
cancellation between the errors paired with the signed derivative in
(19), or a theorem for the whole weighted sum (16).

The singular-series identity (13) is unconditional.
Montgomery--Soundararajan's theorem for **actual** prime moments separately
assumes quantitative prime-tuple errors, including a one-point
\(O_\epsilon(N^{1/2+\epsilon})\) hypothesis for every \(\epsilon>0\)
equivalent to RH; it cannot be imported as an unconditional correlation
estimate. The Selberg bound audited in note 06 also assumes RH at the
needed \(X^2\) scale. Neither supplies the missing input.

Higher powers do not obstruct a prime-only formulation. Note 04 proves
that \(b(y)=p(y)-p_{\mathbb P}(y)\) is uniformly bounded. Therefore
\(V(x)-V_{\mathbb P}(x)=\sqrt x\,b(\log x)\) has dyadic squared norm
\(O_g(X^2)\). The triangle inequality proves equivalence of the target
for full prime powers and primes alone. It does **not** bound the mixed
variance difference by \(O(X^2)\) without controlling the prime signal.

The next useful theorem would estimate (16) or (19) directly, for all
sufficiently large real \(X\). It must retain the signed kernel, both
caps, the proportional shift range, and all actual prime correlations.
A proposed averaged theorem should first be translated through (19),
including exceptional shifts, before being accepted as an input.

The [numerical package](../../numerics/selective_loss_dyadic_pairs_20261003/README.md)
checks the pair, shifted-sum, cap, and continuum identities on small real
shells. Those floating checks do not certify an arithmetic error bound.
The [internal review](../../reviews/SELECTIVE_LOSS_DYADIC_CORRELATION_REVIEW_20261003.md)
records the algebra and hypothesis audit. No manuscript revision, snapshot,
commit, or push is part of this continuation.

The [next continuation](09_actual_error_projection_and_frequency_20261003.md)
sharpens the model to its constant-order term and proves an unconditional
quadratic bound for the negative part of the actual remainder. It removes
four harmless Chebyshev-error trends and controls the outer additive
frequencies. The central signed projection and the positive remainder
bound remain open.
