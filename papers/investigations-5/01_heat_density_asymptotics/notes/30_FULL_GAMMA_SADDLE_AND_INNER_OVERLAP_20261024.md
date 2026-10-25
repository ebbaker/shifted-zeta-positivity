# Full gamma saddles: a uniform static comparison and inner overlap

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this chat's session metadata. Chat 0007, thread
`01a17067-eabc-7872-abc9-d9319b53bc41`.

**Status: proved in-note; same-assistant review only.** This continues
[Note 29][n29] and HDA-19. Replacing the linearized gamma factors by their
full implicit saddles, including the quadratic Gaussian determinant,
removes the previous exponential restriction on time. The new field is
defined by gamma functions and a uniquely specified scalar implicit
equation; its density retains the fixed spatial average and the unchanged
physical regulator.

The static error is
`C t^(3/2)/(1+X+t log(2+t+X))^2`, for t>=32 and t+X sufficiently
large, with fixed transverse and averaging buffers. Consequently it is
`O(1/(sqrt(t) log^2 t))` uniformly over **all real heights** at sufficiently
large positive time, and `O(1/(sqrt(X) log^(3/2) X))` uniformly over t>=32
at sufficiently large height. On each compact time interval it is
`O_T(X^-2)`. The same rates hold for the physical averaged potential and
filtered regulator weight, with spatial derivatives through order four.

This supplies a static overlap with Note 19's inner window. It does not
complete positive current/time/actual-covariance comparison, the finite-time
bridge, or all-time evolution. HDA-19 and HDA-16 remain Partial; HDA-18
remains Gated. The exact, nonzero heat residual of the new field is given
below. Constants and onsets are not numerically instantiated. No numerical,
machine-symbolic or exact-arithmetic execution was performed. See the
[same-assistant assessment][review].

## 1. Contract, model and quantitative statement

Keep the canonical complete source, normalization and heat equation:

\[
H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad H_t=-H_{zz},\quad H(0,z)=\xi((1+iz)/2)/8.
\tag{FS1}
\]

Use the exact q=epsilon_g^2 of [Note 20][n20], with no mass normalization.
Fix ell,h>0 and |y|<=Y, and retain
`K(u,v)=k_ell(u)k_h(v)`, `k(v)=(315/256)(1-v^2)^4 1_{|v|<=1}`.
All arguments include a fixed enlargement of
`|Re z-x|<=ell+2`, `|Im z|<=Y+h+2`, sufficient to contain every root
collar meeting the support. Constants may depend on these fixed data and
the fixed regulator parameter. They are independent of t and x in the
stated domain. Set

\[
X=|x|,\quad R=2+t+X,\quad \mathcal L=\log R,\quad
N=1+X+t\mathcal L,\qquad e(t,X)=\frac{t^{3/2}}{N^2}.
\tag{FS2}
\]

Use the **exact** gamma factor and its logarithmic derivative:

\[
\mathcal M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),
\qquad \alpha(w)=\mathcal M'(w)/\mathcal M(w).
\]

For w=(1+iz)/2 or 1-w, let p=p_t(w) be the large right-half-plane
solution specified in Section 2, and put

\[
p=w+\frac t2\alpha(p),\quad v_*=p-w,\quad
B=1-\frac t2\alpha'(p),
\qquad
\mathcal S_t(w)=\frac{\mathcal M(p)e^{-v_*^2/t}}{\sqrt B},
\tag{FS3}
\]
\[
P_*(t,z)=\mathcal S_t((1+iz)/2)+\mathcal S_t((1-iz)/2).
\tag{FS4}
\]

The square root is the branch near 1. This is a local holomorphic field
on the full required strips, and for late time on the whole fixed-width
horizontal strip. No assertion of an entire continuation through every
possible saddle branch is needed. No theta zeros, measured moments or
target-density values enter FS3.

For F=H or P_* define

\[
S_F=\log(|F|^2+q),\quad w_F=q/(|F|^2+q),\quad
U_F=K*S_F,\quad W_F=K*w_F,
\]
\[
\rho_F=\frac{q|F_z|^2}{\pi(|F|^2+q)^2},\qquad R_F=K*\rho_F.
\tag{FS5}
\]

**Static comparison theorem.** There exist C,R_* such that, for
`t>=32`, `2+t+|x|>=R_*`, `|y|<=Y`,

\[
\boxed{|R_H-R_{P_*}|+
\sum_{|\gamma|\le4}\bigl(
|\partial^\gamma(U_H-U_{P_*})|+
|\partial^\gamma(W_H-W_{P_*})|\bigr)
\le C e(t,|x|).}
\tag{FS6}
\]

Here gamma is spatial only. R_* includes the fixed buffers; no claim at
a finite numerical onset is made. The corresponding field estimate on
the enlarged holomorphic domain is

\[
\boxed{|H-P_*|\le C e(t,X)
 (|\mathcal S_t(s)|+|\mathcal S_t(1-s)|),\qquad s=(1+iz)/2.}
\tag{FS7}
\]

As in Notes 27--28, the denominator is the sum of carrier amplitudes,
not |P_*|, which has zeros. Both fields in FS5 use exactly the same q.

This is an approximation milestone under [avoid/01][a01]. Read the
[result index][results], [heat-flow cluster][geometry], [control screen][controls]
and [avoid index][avoid], especially [cancellation][a12] and [scope][a07].
The control premises are recorded in Section 8.

## 2. An actual saddle branch with a fixed sector margin

For Re p>=2 and large |p|, the sectorial gamma estimates give

\[
\alpha(p)=\tfrac12\Log(p/(2\pi))+O(|p|^{-1}),\qquad
\alpha^{(j)}(p)=O_j(|p|^{-j}),\quad j\ge1.
\tag{FS8}
\]

The differentiated estimates follow from the holomorphic remainder on
a slightly larger sector and Cauchy's formula. All p used below lie in
the right half-plane, so a fixed sector such as |arg p|<=3pi/4 suffices;
its margin does not shrink with t or X. The bounds on a horizontal ray
with Re p>=2 also hold down to bounded |p| after increasing constants.
These are the inputs from [DLMF 5.11][gamma], not an imported large-time
theta theorem.

Write w=sigma+i tau_0, first with tau_0>=0 and sigma in the fixed
buffered real interval. Use the rectangle

\[
\sigma+t\mathcal L/8\le\Re p\le\sigma+t\mathcal L,
\qquad \tau_0\le\Im p\le\tau_0+t.
\tag{FS9}
\]

Replacing X by 2|tau_0| in FS2 changes scales only by fixed constants
on the relevant buffer. Uniformly in this rectangle,
`|p| asymp N` and `log|p|=mathcal L+O(log mathcal L)`.
The map p -> w+(t/2)alpha(p) maps FS9 into itself for sufficiently large
R: its real increment is `t mathcal L/4+O(t log mathcal L)` and its
imaginary increment lies between 0 and t.

Here is a check of the sign used in the last assertion. For A=Re p
large and 0<=tau<=A, the differentiated expansion
`alpha'(A+i tau)=1/[2(A+i tau)]+O(A^-2)` has positive real part.
Integrating vertically from the real axis gives Im alpha>=0. For tau>=A,
the leading half-argument is at least pi/8 and the O(1/|p|) error is
smaller. In both cases Im alpha<=1 eventually. Thus the shifted contour
goes away from the real axis; at tau_0=0 the saddle is real.

The derivative of the map is bounded by
`Ct/N<=C/mathcal L<1/2` on this convex rectangle. The contraction
principle proves existence and uniqueness there, with

\[
a:=\Re v_*\asymp t\mathcal L,\quad
|h_*|:=|\Im v_*|\le t,\quad |p|\asymp N,
\quad |B-1|\le C/\mathcal L.
\tag{FS10}
\]

More precisely `a=(t/4)log(|p|/(2pi))+O(t/|p|)`, so
`a>=t mathcal L/5` after an eventual onset. Negative tau_0 uses complex
conjugation and the reflected rectangle. Uniqueness and B!=0 give a
holomorphic branch in w, including across tau_0=0, by the implicit
function theorem. On overlapping rectangles the branches agree.
The logarithm of M is the holomorphic branch on Re p>1 that is real
on the positive real axis. B stays in a fixed disk about 1.

## 3. Complete convolution and every contour payment

The exact all-positive-time identity, also [Polymath (35)][poly], is

\[
H(t,z)=\frac1{\sqrt{\pi t}}\int_{\mathbb R}
e^{-v^2/t}\frac{\xi(s+v)}8\,dv.
\tag{FS11}
\]

Split at Re(s+v)=2 and -1. Reflect the left arm by xi(w)=xi(1-w)
and substitute v -> -v. Each arm is

\[
I_w=\frac1{\sqrt{\pi t}}\int_{v_0}^\infty
e^{-v^2/t}\mathcal M(w+v)\zeta(w+v)\,dv,
\quad v_0=2-\Re w,
\tag{FS12}
\]

with w=s or 1-s. The leftover middle interval has bounded length.
The endpoints depend on w for estimating purposes; the final H and
P_* are holomorphic independently of this pointwise decomposition.

For tau_0>=0 move the arm to `v=r+i h_*`, r>=v_0, retaining the
oriented vertical connector from v_0 to v_0+i h_*. The exact arm is
the shifted horizontal integral plus this connector. For tau_0<0 the
same oriented statement uses h_*<0. Throughout the deformation
Re(w+v)>=2. Thus neither the gamma poles/zeros nor the zeta pole is
crossed, and the ordinary Dirichlet series is valid on every shifted
horizontal ray and connector. At a finite right endpoint close the
rectangle first, then let the endpoint tend to infinity: its integrand
is bounded by `exp(-r^2/t+O(r log(r+2)))` for the fixed parameters,
so that vertical face vanishes. The uniform tail estimates follow next.

### 3.1 The central and infinite right portions

Write `v=v_*+u`, u real, and `m=|p|`. For u>=-a/2 the segment from
p to p+u stays in Re>1 and has modulus at least c m. Set

\[
\Gamma_p(u)=\log\mathcal M(p+u)-\log\mathcal M(p)-\alpha(p)u.
\]

FS8 and Taylor's formula with its integral remainder give, over this
whole half-line (including u arbitrarily large),

\[
|\Gamma_p(u)|\le C u^2/m,\qquad
E_p(u):=\Gamma_p(u)-\tfrac12\alpha'(p)u^2,
\quad |E_p(u)|\le C|u|^3/m^2.
\tag{FS13}
\]

For u>=0 the intervening modulus only increases, which is why these
are not bounded-u expansions used outside their domain. Exact saddle
cancellation now gives

\[
\frac{e^{-(v_*+u)^2/t}\mathcal M(p+u)}
 {e^{-v_*^2/t}\mathcal M(p)}
=e^{-Bu^2/t+E_p(u)}.
\tag{FS14}
\]

Because t/m<=C/mathcal L, both the exact modulus on the right of FS14
and `|exp(-B u^2/t)|` are at most `exp(-c u^2/t)`, with a fixed
positive c, which can be taken as 1/2. The inequality
`|e^E-1|<=|E|max(1,e^(Re E))` therefore gives

\[
\frac1{\sqrt{\pi t}}\int_{-a/2}^\infty
|e^{-Bu^2/t}(e^{E_p(u)}-1)|\,du
\le C t^{3/2}/m^2.
\tag{FS15}
\]

No `exp(t (Im alpha)^2/4)` remains. The full complex Gaussian is
`(pi t)^(-1/2) int_R exp(-B u^2/t)du=B^(-1/2)` since Re B>0.
Its missing left tail and either integral's right tail beyond u=a/2
are `O(exp(-c a^2/t))`. In particular the true infinite right tail
has been paid, not removed by naming a saddle.

### 3.2 The remaining horizontal segment on the left

For v_0<=r<=a/2 put d=a-r, A=Re p, tau=Im p. Along the horizontal
segment, `|v+i tau|/|A+i tau|>=v/A`, 2<=v<=A. FS8 implies

\[
\int_{A-d}^{A}\Re\alpha(v+i\tau)\,dv
\ge d\Re\alpha(p)-C A.
\tag{FS16}
\]

Indeed the possible logarithmic loss is at most
`-(1/2) int_0^A log(v/A)dv=A/2`; the bounded remainders contribute
O(A). This remains uniform when tau=0 or when tau is much larger than A.
Since Re alpha(p)=2a/t, comparison with the saddle exponent yields

\[
\left|\frac{e^{-(r+i h_*)^2/t}\mathcal M(w+r+i h_*)}
 {e^{-v_*^2/t}\mathcal M(p)}\right|
\le e^{-d^2/t+C A}\le e^{-c t\mathcal L^2}.
\tag{FS17}
\]

Here d>=a/2, a asymp t mathcal L, and A=a+O(1). For large mathcal L,
the negative quadratic dominates C A. The segment length divided by
sqrt(t) is absorbed after reducing c. Zeta is bounded by zeta(2).

### 3.3 The connectors and the bounded middle

At the top of the connector use FS16 with A-d=2. Along Re=2 the
absolute imaginary part of alpha is uniformly bounded, even at bounded
height. Moving from tau_0+h_* back toward tau_0 costs at most
`exp(C|h_*|)` in gamma modulus; the Gaussian modulus does not increase
relative to its value at h_* because `eta^2<=h_*^2` on that segment.
Thus each connector, including its length/sqrt(t), has relative bound
`C exp(-c t mathcal L^2)` against its own saddle carrier. This works
also when the connector collapses at h_*=0.

For the middle, Euler summation and bounded-real-part Stirling, together
with compactness at bounded height, give

\[
\sup_{-1\le b\le2}|\xi(b+i\tau_0)/8|
\le C(1+|\tau_0|)^b_0|\mathcal M(2+i\tau_0)|
\tag{FS18}
\]

for a fixed finite b_0. Reflection is used on the part left of 1/2.
There are no singularities in xi in the bounded-height compact set;
M(2+i tau_0) never vanishes. The endpoint comparison just proved,
with the bounded original Gaussian coordinate, then bounds the whole
middle by `C R^b_0 exp(-c t mathcal L^2)` relative to either carrier.
The middle remains present in the error ledger.

### 3.4 All arithmetic modes

On Re(w+v)>=2 the full series gives
`|zeta(w+v)-1|<=3*2^(-Re(w+v))`.
For r=a+u>=a/2, FS14's Gaussian bound gives the relative integral

\[
C e^{-a\log2}\frac1{\sqrt{\pi t}}
\int_{\mathbb R}e^{-u^2/(2t)-u\log2}\,du
\le C e^{-a\log2+t(\log2)^2/2}
\le C R^{-t\log2/8}.
\tag{FS19}
\]

The last inequality uses a>=t mathcal L/5 and an eventual onset
independent of t>=32. The remaining horizontal segment and connectors
already have FS17's payment with zeta bounded. No finite selection of
Dirichlet or theta modes has replaced this remainder.

Combining all pieces proves first the visible three-part budget

\[
\frac{|H-P_*|}{|\mathcal S_t(s)|+|\mathcal S_t(1-s)|}
\le C\left\{\frac{t^{3/2}}{N^2}
 +R^{-t\log2/8}+R^{b_0}e^{-c t\mathcal L^2}\right\}.
\tag{FS20}
\]

Since t>=32, the arithmetic exponent is greater than 2, while
`N<=C R log R` and `t^(3/2)>=32^(3/2)`. The last two terms are
absorbed into C e(t,X) after a single eventual onset. This proves FS7.
The time floor is a convenient arithmetic allowance, not a zero-theorem
onset. This proof does not import Polymath's small-time high-zero theorem.

## 4. Physical collars and potential transfer

Differentiate the **implicit formula**, not an error term. With alpha
and its derivatives evaluated at p,

\[
p_w=B^{-1},\qquad
D:=(\log\mathcal S_t)'(w)
=\alpha+\frac{t\alpha''}{4B^2},
\]
\[
D'=\frac{\alpha'}B+\frac{t\alpha'''}{4B^3}
 +\frac{t^2(\alpha'')^2}{4B^4}=O(N^{-1}).
\tag{FS21}
\]

Choose compatible logarithms and write
`P_*=2 A_* cos Theta_*` as in Note 27 GO17. On real x the carrier
is positive and the phase is real. On the full fixed buffer,

\[
\omega_*:=\partial_x\Theta_*(t,x)
=\tfrac12\Re D(s_x)
=\tfrac14\log(|p_t(s_x)|/(2\pi))+O(N^{-1}+tN^{-2})
\asymp\mathcal L,
\]
\[
\Theta_{*,zz}=O(N^{-1}),\qquad
|\partial_z\log\mathcal A_*|\le C.
\tag{FS22}
\]

For the carrier derivative, the difference D(s)-D(1-s) cancels the
large real logarithms; on the real axis it is 2i Im D(s), which is
bounded, and FS21 extends the bound to the fixed transverse buffer.
Hence the analytic carrier is comparable to
`A_X=|S_t((1+ix)/2)|` throughout that buffer.

Note 27's phase/Rouche argument now applies with error C e(t,X).
For sufficiently large R it yields all nearby zeros, not just a selected
subset: one real simple H zero and one real simple P_* zero per
disjoint collar of radius c/omega_*, displacement O(e/omega_*), exterior
floor c A_X, and linear interior floor c A_X omega_* times distance
to the corresponding root. There are O(omega_*) collars intersecting
the support. FS22 supplies the injective local phase coordinate and the
buffer needed for edge collars. This is an eventual local-strip statement;
it is not a new assertion about the global Newman threshold.

The arbitrary-positive-q analytic-unit lemma in Note 28 JT13--JT16
therefore gives, with the same physical q on both fields,

\[
\|S_H-S_{P_*}\|_{L^1(\Omega)}+
\|w_H-w_{P_*}\|_{L^1(\Omega)}\le C e(t,X).
\tag{FS23}
\]

Its planar translation bound is independent of a regulator floor.
Transferring derivatives to K proves the U,W part of FS6 through order
four. K has bounded weak derivatives of those orders and no boundary
delta there. This does not estimate products of unfiltered gradients.

## 5. The unchanged regulator: a uniform density payment

Write, exactly as in Note 28,
`epsilon_g(t,u)=E_0(t) exp(-beta(t)u^2/2)` and r=log q.
The weak identity used for both fields is

\[
4\pi\langle\rho_F,\psi\rangle
=\int S_F\Delta\psi+2\int w_F\nabla r\cdot\nabla\psi
 +\int\{w_F\Delta r+w_F(1-w_F)|\nabla r|^2\}\psi.
\tag{FS24}
\]

Let B_0 be a sufficiently large **fixed** constant chosen below. When
beta(t)X<=B_0, both spatial derivatives of r required by FS24 are
bounded uniformly: beta itself is globally bounded for t>=32.
Subtract FS24 and apply FS23 to obtain the density part of FS6.
This includes the unresolved-regulator layer and t=64.

For beta X>B_0, comparison to each field's own real zero measure is
used, with its own separately paid regularization error. Set

\[
\lambda_X=\frac{\sup_{|u-x|\le\ell+2}\epsilon_g(t,u)}{A_X}.
\tag{FS25}
\]

The important new issue is growing t: separately bounding log E_0 by
O(t log^2 t) would be inadequate near X of order t log t. Retain the
physical mass anchor instead. For sufficiently large t the field theorem
already holds at x=0, where P_*(t,0)=2 S_t(1/2)>0. [Note 12][n12] (3)--(6)
gives `H(t,0)/M_0(t)=1+O(kappa^-1/4)`, with its complete-source gates
holding eventually. Thus, by FS7 at zero,

\[
cM_0(t)\le A_0(t)=\mathcal S_t(1/2)\le CM_0(t).
\tag{FS26}
\]

This is used to **prove a bound**, not to fit the model. FS3 is unchanged.
Integrating the bounded real-axis logarithmic amplitude derivative from
FS22 gives `|log(A_X/A_0)|<=C X`. At t>=128 the regulator amplitude
is exactly E_0=M_0/kappa. Consequently, for X larger than the fixed buffer,

\[
\log\lambda_X\le C-\log\kappa
 -\frac{(X-\ell-2)^2}{2\kappa}+C_1X.
\tag{FS27}
\]

Choose B_0>8(C_1+1). If X/kappa>B_0, then FS27 gives
`lambda_X<=C exp(-cX)`, uniformly at these large times. Moreover
`|log lambda_X|<=C(1+X^2)` on this regime: the two-sided version of
FS26 and the amplitude-derivative bound give it directly, using
kappa<X/B_0 and the eventual positive lower bound on kappa.

It remains to cover a fixed bounded interval 32<=t<=T containing all
times not covered by FS26. For large X, FS3 and sectorial Taylor expansion
give `log A_X=-pi X/8+O_T(log^2 X)`. E_0 and beta are bounded on
this compact interval. For beta X>B_0, choosing B_0 also larger than pi
then gives the same exponential bound on lambda_X and the same polynomial
logarithmic allowance. Small X cannot occur here once R_* is enlarged.
This covers the switch interval without treating its flat onset as an
immediate positive lower bound on beta.

The actual collars and Note 28 JT21 now imply, for F=H,P_*,

\[
|R_F-K*\nu_F|\le
C(1+X^2)\lambda_X^2
\left[1+\frac{1+\log(1+C/\lambda_X^2)}{\omega_*}\right]
\le Ce^{-cX}.
\tag{FS28}
\]

All spatial regulator curvature terms remain included. Root displacement
and the O(omega_*) count give `|K*nu_H-K*nu_{P_*}|<=Ce`.
In this regime, bounded t or kappa<X/B_0 implies t<=C(1+X), and
`N<=C(1+X)log(2+X)`; hence exp(-cX) is absorbed by e(t,X).
This finishes FS6 for all regulator sizes. No claim that the density is
a zero measure in the complementary regime has been made.

## 6. Joint thresholds, all-height endpoint and inner matching

The denominators in FS2 immediately give two useful uniform consequences:

\[
\sup_{x\in\mathbb R,\ |y|\le Y}|R_H-R_{P_*}|
\le\frac C{\sqrt t\log^2(2+t)},\qquad t\ge T_*;
\tag{FS29}
\]
\[
\sup_{t\ge32,\ |y|\le Y}|R_H-R_{P_*}|(t,x,y)
\le\frac C{\sqrt X\log^{3/2}(2+X)},\qquad X\ge X_*.
\tag{FS30}
\]

The U,W spatial jets have the same consequences. For FS30 write
`u=t log(2+X)/(1+X)` and bound `u^(3/2)/(1+u)^2` by a constant.
For each fixed compact [32,T], FS6 is instead O_T(X^-2).

Thus a sufficient outer threshold can be chosen **independent of t>=32**,
X_out(t)=X_*, and for t>=T_* the theorem covers every real height.
These are existence thresholds with all buffers absorbed, not certified
numerical constants. The old exp(4t) threshold belongs to the linearized
model's old proof; it is not a restriction on FS3.

At sufficiently large t, q is precisely [Note 19][n19]'s regulator and both
theorems apply on its buffered `|x|<=X_in(t) asymp kappa^(1/3)`
window. One may take `2X_* <= |x| <= X_in(t)/2` as an explicit nonempty
overlap region with room on both sides. The triangle inequality gives

\[
\|R_{P_*}-R_L\|_{\mathrm{inner}}
\le C\kappa^{-1/2}+C t^{-1/2}\log^{-2}(2+t)
=O(\kappa^{-1/2}).
\tag{FS31}
\]

This is a comparison of two static approximations to the same physical
density, not term-by-term matching of gamma and source-saddle expansions.
The source/collar gates of Note 19 remain in force; they hold eventually.
No new finite onset or differentiated matching follows from FS31.
There is no remaining *static positive-time spatial gap* at sufficiently
large t. The finite-time transition and full evolution matching remain.

## 7. Exact heat residual and the next analytical consumer

The new model does not solve the heat equation exactly. To retain that
information explicitly, the implicit derivatives also give

\[
p_t=\frac\alpha{2B},\qquad
\partial_t\log\mathcal S_t
=\frac{\alpha^2}4+\frac{\alpha'}{4B}
 +\frac{t\alpha\alpha''}{8B^2}.
\tag{FS32}
\]

Combine this with FS21 and
`partial_zz S_t((1 +/- iz)/2)=-(1/4)partial_ww S_t`.
The alpha^2, alpha'/B and t alpha alpha'' terms cancel exactly, leaving

\[
\boxed{(\partial_t+\partial_{zz})P_*
=-\sum_{w=s,1-s}\mathcal S_t(w)
\left\{\frac{t\alpha'''(p)}{16B^3}
 +\frac{5t^2(\alpha''(p))^2}{64B^4}\right\}.}
\tag{FS33}
\]
\[
|(\partial_t+\partial_{zz})P_*|
\le C\frac t{N^3}
(|\mathcal S_t(s)|+|\mathcal S_t(1-s)|).
\tag{FS34}
\]

This exact field residual is a useful HDA-16 input. It is not a propagated
error theorem. In particular FS6 is not differentiated to obtain density
time error, current, potential time derivative, forcing, actual Q or
Delta Q. The adaptive equations retain both derivatives of filtered
curvature, the actual covariance, and the source terms from Note 14.

**Next: Analytical — Astra, HDA-16.** Derive direct time/current and
physical-potential-time comparisons for H and P_* on the new all-height
late-time domain, starting from the complete shifted convolution and FS33.
Then estimate actual gradient-product covariance and its Laplacian, with
the same regulator. State every root-motion, small-denominator and weak
source payment rather than differentiating FS6. This is the missing
positive counterpart to Note 26 and the next necessary input to HDA-18.
No bounded numerical question is needed for the present decision; the
Sol queue remains empty. HDA-20's distinct-reviewer audit remains open.

## 8. Scope, controls, evidence and remaining obligations

| Item | Payment or remaining obligation |
| --- | --- |
| Source and contours | FS11--FS20 retain both reflected arms, both connectors, the middle, every arithmetic mode and both infinite ends. No poles are crossed. |
| Parameter uniformity | Fixed right-half-plane sector; contraction ratio O(1/log R); constants independent of t>=32 and X in the declared domain. |
| Observable transfer | Actual simple collars, analytic units, arbitrary-positive-q L1 lemma, and a separate mass-anchored regulator payment. |
| Static gain | FS6, both joint limits FS29--FS30, and actual inner overlap FS31. The spatial average of the special-function field remains part of the formula. |
| Evolution | Exact residual FS33--FS34; positive current/time/forcing/actual covariance comparison is not yet established. |
| Onsets and validation | Eventual thresholds only; no numerical certificate or independent specialist review. |
| All-time assembly | Finite-transition budget, differentiated joining and complete boundary/source contract remain unfinished. No new manuscript snapshot or integration. |

This uses the unchanged identity xi/8=M zeta, exact reflection and the
ordinary full Dirichlet series. The [collision-control screen][controls]
has the same premise outcomes as Note 27 Section 8: Euler-factor controls
alter the completed transform; weighted-square/finite-tail controls lack
the unchanged coefficients and full reflection; reflected, smooth and
positive-primitive controls lack this canonical gamma-times-zeta identity;
finite-prime orbit controls lack full reflection; atomic/finite-profile
controls lack the completed xi source; RH-conditional normalized-endpoint
controls fail ordinary Dirichlet-series arithmetic. The general collar
lemma can hold on their simple-root subdomains and excludes none of them
globally. This is a premise audit, not a numerical rerun of controls.

Neither the useful saddle change nor the inner overlap proves RH, a
global collision exclusion at early time, or a closed evolution equation.
The lower time 32 is outside that question. The complete-source mass bound
is used only after the independent field proof, avoiding a fitted or
circular amplitude anchor. Standard inputs and the primary passages
checked for this continuation are recorded in the [reference catalog][refs].

[n12]: 12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md
[n19]: 19_EXPLICIT_SADDLE_CLOCK_AND_EXACT_PHASE_20261024.md
[n20]: 20_GLOBAL_REGULATOR_AND_FINITE_SOURCE_BRIDGE_20261024.md
[n29]: 29_CONTINUATION_JOINT_OUTER_TO_INNER_MATCHING_20261024.md
[review]: ../reviews/12_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_SELF_REVIEW_20261024.md
[refs]: ../references/README.md
[poly]: https://arxiv.org/html/1904.12438v2
[gamma]: https://dlmf.nist.gov/5.11
[results]: ../../../../result-summaries/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
