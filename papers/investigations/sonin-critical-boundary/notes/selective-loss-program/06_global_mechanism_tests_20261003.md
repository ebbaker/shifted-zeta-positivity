# Global mechanism tests and a fixed-kernel variance target

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. Separate agents using the inherited
configuration supplied the mechanism and variance derivations. These are
internal same-model checks, not independent specialist refereeing.
No unconditional global signed-pair bound or RH proof is claimed.

This continues [the complete response and signed-pair reduction](04_complete_response_and_signed_pairs_20261003.md)
and [the quadratic target and finite sign theorem](05_quadratic_target_and_finite_sign_20261003.md).
The diagonal cost is controlled. The remaining global estimate must use the
signed correlations of the actual prime channels. Differential positivity,
PNT, and frame bounds alone cannot provide it. A concrete next target is
the fixed-kernel dyadic variance in Section 7; its exact scale and RH
strength are made explicit below.

## 1. Setup and scope of the open estimate

Put a=1/4, ell=2a, c=1/4, and use zero extensions of

\[
h(v)=(1-16v^2)^8\quad(|v|<a),\qquad
g_0=-h'''+ch',\quad \nu=\|g_0\|_2^2,\quad g=g_0/\sqrt\nu.
\]

The normalized g is real and odd, with support [-a,a] and both prepared
exponential moments zero. Define

\[
p(y)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}g(y-\log n),\qquad
J(Y)=\int_0^Y p(y)^2dy.
\tag{1}
\]

All sums are locally finite. The complete window at Y includes every
delay log n<Y+a, including the final partial packets. With K_Y, D, and
Theta as in note 04, J=D+Theta. Note 05 establishes the effective global
diagonal bound

\[
0\le D(Y)\le2\log2\,(Y^2+17/16)\quad(Y\ge0).
\tag{2}
\]

Thus Theta_+(Y)<=C(1+Y)^2 suffices for quadratic J. This positive part
is scalar and is taken after every signed off-diagonal term is summed.
It is neither an entrywise clipping rule nor a matrix-order assertion.
The bounded continuum sign result in note 05 gives no global extension.

## 2. Differential factorization: preserve the endpoint cancellation

Introduce the nonnegative smooth local signal

\[
L_h(y)=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}h(y-\log n).
\]

Then p=(-L_h'''+cL_h')/sqrt(nu). The zero-extended h is sufficiently
smooth for the following integration by parts. Since log2-a>0, the
initial endpoint and its derivatives vanish. At each finite Y,

\[
\boxed{\nu J(Y)=\int_0^Y
\left[(L_h''')^2+\frac12(L_h'')^2+\frac1{16}(L_h')^2\right]dy
-\frac12L_h''(Y)L_h'(Y).}
\tag{3}
\]

The final term can have either sign. It cannot be dropped in an upper
estimate. For the continuous density dpsi(x)=dx,
L_{h,0}(y)=H_h(1/2)e^(y/2) for y>a. The positive bulk integrand is then
H_h(1/2)^2 e^y/16 and the endpoint subtraction is
H_h(1/2)^2 e^Y/16. Their exponential parts cancel exactly, leaving
only the fixed initial-cap energy. Bounding the bulk terms separately
already produces an exponential cost for this ideal density.

The same structure appears in the full-space autocorrelation:

\[
\phi=\nu^{-1}(-D_v^2)(-D_v^2+c)^2(h*h).
\tag{4}
\]

Although h*h is nonnegative, transferring these derivatives to a
positive counting measure does not preserve a usable sign.

A useful exact centering is q_h(y)=e^(-y/2)L_h(y)>=0. Conjugation gives

\[
\boxed{\nu J(Y)=\int_0^Y e^y
\left|q_h'''+\frac32q_h''+\frac12q_h'\right|^2dy.}
\tag{5}
\]

Let k(v)=e^(-v/2)h(v) and E_0(u)=e^(-u)[psi(e^u)-e^u]. For y>a,
finite-window Stieltjes integration by parts gives

\[
q_h(y)-H_h(1/2)=
\int_{y-a}^{y+a}E_0(u)[k'(y-u)+k(y-u)]du.
\tag{6}
\]

All endpoint terms vanish. Differentiating up to order three yields

\[
|q_h^{(j)}(y)-{\bf1}_{j=0}H_h(1/2)|
\le\|k^{(j+1)}+k^{(j)}\|_1
\sup_{|u-y|\le a}|E_0(u)|,\quad 0\le j\le3.
\tag{7}
\]

Ordinary PNT gives convergence of q_h to H_h(1/2) and of these
derivatives to zero. It gives no rate adequate for the exponentially
weighted norm (5). Positivity and convergence of the centered profile
therefore do not supply the required signed energy bound.

## 3. A sharp linear Bessel bound still leaves a coherent-vector gap

Fix Y, write a_n=Lambda(n)/sqrt(n), and restrict
v_n(y)=g(y-log n) to [0,Y]. Keep only the nonzero-weight active packets.
The finite positive frame operator is

\[
S_Y=\sum_n a_n^2|v_n\rangle\langle v_n|,\qquad
{\rm Tr}(S_Y)=D(Y).
\]

The elementary bound psi(x)<=C_psi x, valid with C_psi=4log2, and
Lambda(n)^2<=log(n)Lambda(n) give

\[
\sum_{|\log n-y|\le a}\frac{\Lambda(n)^2}{n}
\le C_\psi e^{2a}(y+a).
\]

Packetwise Cauchy--Schwarz and ||g||_2=1 now prove

\[
\boxed{0\le S_Y\le C_\psi e^{2a}(Y+a)I.}
\tag{8}
\]

Final partial packets cause no difficulty: each restricted packet has
norm at most one. This unconditional Bessel estimate is sharp in order.
Test against a normalized g packet centered at Y-2a. On a sufficiently
narrow fixed log block around that center, phi is bounded away from
zero. PNT gives squared prime-weight mass comparable to Y, so
||S_Y||>=c_gY for all sufficiently large Y.

Its weighted Gram matrix G_Y has entries a_na_mK_Y(log n,log m), and

\[
J(Y)=\langle{\bf1},G_Y{\bf1}\rangle,\quad
{\rm Tr}(G_Y)=D(Y),\quad\|G_Y\|=\|S_Y\|.
\tag{9}
\]

Here ||1||^2 is the number of active prime powers, asymptotic to
e^(Y+a)/(Y+a). Consequently (8) still gives exponential size for J.
A quadratic trace and linear operator norm do not control this particular
coherent coefficient vector. A successful frame argument must bound
its overlap with the growing spectral directions, using additional
signed prime correlation information.

## 4. A discrete sparse PNT model defeats the generic mechanisms

The following countermodel is not the actual prime sequence and has
no asserted Euler multiplicativity. It retains integer support,
positive logarithmic weights, PNT, the correct diagonal asymptotic,
the prepared differential kernel, and the complete top caps.

Choose 1/2<beta<1, alpha=beta-1/2, 0<delta<1, and gamma!=0 with
G(alpha+i gamma)!=0, where G(s)=int g(v)e^(-sv)dv. Such a choice
already follows by continuity from G(alpha)>0. Put

\[
M(x)=x+\delta\,{\rm Re}
\frac{x^{\beta+i\gamma}}{\beta+i\gamma}.
\tag{10}
\]

Its derivative lies strictly between zero and two for x>=1. Set
F(x)=M(x)-M(8), take c_n=0 for n<=8, and start with S_8=0=F(8).
For n>8 choose c_n in {0,log n} greedily: insert log n if
S_(n-1)<F(n), otherwise insert zero, and set S_n=S_(n-1)+c_n.
Since 0<F(n)-F(n-1)<2<log n, induction gives for every n>=8

\[
0\le S_n-F(n)\le\log n.
\tag{11}
\]

If no weight is inserted, the new excess is nonnegative and no larger
than the previous excess. If a weight is inserted, the previous excess
minus the increment of F lies in (-2,0), so the new excess lies in
(log n-2,log n). This proves the asserted interval from the exact
starting value, without an eventual-crossing qualification. Passing
from integers to real x adds only a bounded increment. Since F-M
is constant and dF=dM, therefore

\[
\widetilde\psi(x)=\sum_{n\le x}c_n=M(x)+O(\log x)\sim x.
\tag{12}
\]

For the discrete response
tilde p(y)=sum c_n/sqrt(n) g(y-log n), the continuous density part
of dM is annihilated for y>a. Its oscillatory part gives exactly
delta Re[e^((alpha+i gamma)y)G(alpha+i gamma)]. The tracking error
R=tilde psi-M is O(log x). Integration by parts against
x^(-1/2)g(y-log x), with zero endpoint values, bounds its response by

\[
C(y+a)e^{-y/2}
\int_{-a}^a e^{v/2}|g'(v)+g(v)/2|dv.
\]

Thus, with fixed countermodel parameters,

\[
\widetilde p(y)=
\delta\,{\rm Re}[e^{(\alpha+i\gamma)y}G(\alpha+i\gamma)]
+O((1+y)e^{-y/2}),\qquad
\widetilde J(Y)\asymp e^{2\alpha Y}.
\tag{13}
\]

The error cross terms have integrable absolute values because alpha<1/2.
Integrating the main square over the last fixed oscillation period
proves the uniform lower bound implicit in the asymptotic comparison.

Yet the diagonal has a bounded remainder. Since c_n^2=log(n)c_n,

\[
\widetilde A_2(t)=
\int_{1^-}^{e^t}\frac{\log x}{x}\,d\widetilde\psi(x)
=t^2/2+C_0+o(1).
\]

Indeed tilde psi-x=O(x^beta)+O(log x); its endpoint product with
(log x)/x tends to zero, and its product with that function's derivative
is absolutely integrable. The exact diagonal convolution and evenness
of g^2 then give

\[
\boxed{\widetilde D(Y)=Y^2/2+O(1),\qquad
\widetilde\Theta_+(Y)\asymp e^{2\alpha Y}.}
\tag{14}
\]

Every final packet through Y+a is included. Its PNT gives its own finite
counting constant and therefore the same linear frame bound as (8).
Hence positivity, sparse integer support,
PNT, the right diagonal, and Bessel/trace bounds collectively cannot
prove the target. An argument using genuine arithmetic relations among
the actual Euler prime channels is still possible; this countermodel
does not supply or refute such relations.

## 5. The cumulative autocorrelation has no universal favorable sign

Let q_0=-h''+h/4, so g_0=q_0', and define
Phi(s)=int_0^s phi(t)dt. Zero extension and integration by parts give

\[
\Phi(s)=\nu^{-1}\int g_0(x)q_0(x+s)dx,\qquad0\le s\le\ell.
\tag{15}
\]

The polynomial overlap limits are [-a,a-s]. The exact rational sign
check retained in the [replay](../../numerics/selective_loss_quadratic_target_20261003/replay.py)
and [internal review](../../reviews/SELECTIVE_LOSS_QUADRATIC_TARGET_REVIEW_20261003.md)
records

\[
\Phi(1/8)=
-\frac{1140808292835309014305621023}
{342620277570940280369078861824}<0.
\tag{16}
\]

Near zero Phi is positive because phi(0)=1. Thus it changes sign.
A summation-by-parts shortcut requiring Phi>=0 against a positive
counting measure does not apply to this kernel. This does not exclude
a signed arithmetic summation argument. No unchecked program is
included or treated here as an independent proof.

## 6. Exact multiplicative variance normalization

Define the fixed zero-extended multiplicative weight

\[
w(t)=t^{-1/2}g(-\log t),\quad e^{-a}\le t\le e^a,
\qquad V(x)=\sum_n\Lambda(n)w(n/x).
\]

The preparation moment gives int w(t)dt=0. Consequently V is already
centered against the continuous density; its normalization is exactly

\[
\boxed{p(\log x)=x^{-1/2}V(x),\qquad
J(Y)=\int_1^{e^Y}|V(x)|^2\,\frac{dx}{x^2}.}
\tag{17}
\]

Put mathcal V_g(X)=int_X^(2X)|V(x)|^2dx. For this fixed kernel, the
proposed dyadic estimate is

\[
\boxed{\mathcal V_g(X)\le C_gX^2\log(2X)
\quad\hbox{for all sufficiently large }X.}
\tag{18}
\]

Summing dyadic shells in (17) gives J(Y)=O_g((1+Y)^2), hence the
quadratic Theta_+ target. More generally an X^2(log X)^k estimate
gives polynomial J of degree k+1. The measure dx/x^2 in (17) is
essential: an X-average does not remove the factor X^2 in (18).
Condition (18) is sufficient, not asserted necessary for quadratic J.

It has a direct exact signed-pair version:

\[
\mathcal V_g(X)=\mathcal D_g(X)+\mathcal C_g(X),
\]
\[
\mathcal C_g(X)=2\sum_{n<m}\Lambda(n)\Lambda(m)
\int_X^{2X}w(n/x)w(m/x)dx.
\tag{19}
\]

The complete integer range is e^(-a)X<n<2e^aX; only pairs with
|log(n/m)|<ell overlap. All initial and final partial packets remain.
The positive diagonal is already O_g(X^2log(2X)) unconditionally:
its pointwise density is

\[
x\sum_n\frac{\Lambda(n)^2}{n}g(\log x-\log n)^2
\le C_\psi e^{2a}\|g\|_\infty^2x(\log x+a).
\]

Thus a concrete sufficient next theorem is
mathcal C_g(X)_+<=C_gX^2log(2X), with the positive part taken only
after the entire actual signed pair sum (19). Termwise positive
clipping would again discard the required cancellation.

## 7. Exact Selberg bridge and what it does not supply unconditionally

Let a_0=e^(-a), b_0=e^a, theta(t)=t/a_0-1, and

\[
\mathscr S(U,\theta)=\int_U^{2U}
|\psi((1+\theta)u)-\psi(u)-\theta u|^2du.
\]

Here 0<=theta(t)<=e^(2a)-1<1. Integration by parts, using w(a_0)=w(b_0)=0,
int w'=0, and int t w'=-int w=0, gives the exact centered identity

\[
V(x)=-\int_{a_0}^{b_0}w'(t)
[\psi(xt)-\psi(a_0x)-(t-a_0)x]dt.
\tag{20}
\]

This can retain correlations between signed kernel components. If
Delta_theta(u)=psi((1+theta)u)-psi(u)-theta u and
mathscr B(U;theta,eta)=int_U^(2U)Delta_theta(u)Delta_eta(u)du, then

\[
\boxed{\mathcal V_g(X)=a_0^{-1}
\int_{a_0}^{b_0}\!\int_{a_0}^{b_0}
w'(t)w'(s)\mathscr B(a_0X;\theta(t),\theta(s))\,dt\,ds.}
\tag{21}
\]

All integrals are over finite ranges; the covariance identity requires
no limiting-series interchange. Its covariance kernel is positive
semidefinite, but individual entries and w' components need not have
one sign. Formula (21) is an alternative exact target preserving the
fixed signed smoothing.

Minkowski gives the weaker sufficient comparison

\[
\mathcal V_g(X)^{1/2}\le a_0^{-1/2}
\int_{a_0}^{b_0}|w'(t)|
\mathscr S(a_0X,\theta(t))^{1/2}dt.
\tag{22}
\]

If a supplied theorem gives
mathscr S(U,theta)<=C_SU^2 theta log^2(2/theta) uniformly on the
required range, then

\[
\mathcal V_g(X)\le C_SC_{\rm ker}X^2,\quad
C_{\rm ker}=a_0\left[
\int_{a_0}^{b_0}|w'(t)|\sqrt{\theta(t)}
\log(2/\theta(t))dt\right]^2.
\tag{23}
\]

The zero endpoint is read by continuity. A kernel-only upper bound is

\[
C_{\rm ker}\le\frac8{e^2}(1-e^{-2a})D_g,\qquad
D_g=\|g'\|_2^2+\frac14.
\]

Indeed max sqrt(theta)log(2/theta)=2sqrt2/e,
int|w'|=int e^(v/2)|g'+g/2|dv, and weighted Cauchy--Schwarz gives
the latter square <=2sinh(a)D_g.

The relevant primary theorem has an RH hypothesis.
[Saffari--Vaughan (1977), Lemma 5 and (6.12)--(6.13)](https://aif.centre-mersenne.org/item/10.5802/aif.649.pdf)
prove the U^2 theta log^2(2/theta) scale for psi under RH, uniformly
for 0<theta<=1 and U>=4. Their proof first treats psi, before the
corresponding prime-only statement. Their unconditional density-based
alternative has a U^3 scale at fixed theta, with a decaying relative
factor. [Zaccagnini (2016), Sections 3.2--3.3](https://arxiv.org/pdf/1603.02952)
likewise distinguishes unconditional almost-all relative error from
the stronger RH variance. The interval-length range and the variance
magnitude are different issues.

At fixed theta, an o(U^3) variance transferred through (22) yields
only o(X^3) for mathcal V_g(X), not the X^2log X required in (18).
The conditional theorem in (23) gives J=O(1+Y), but using it as an
unconditional input would assume RH. The sources checked here supply
no unconditional bound of the needed magnitude. Nor does (22)
rule out a sharper approach using the signed covariance (21).

## 8. RH classification and the next precise obligation

For clarity about logical strength, set

\[
G(s)=\int g(v)e^{-sv}dv
=\frac{s(1/4-s^2)H_h(s)}{\sqrt\nu}.
\]

The integral representation
[DLMF 10.32.2](https://dlmf.nist.gov/10.32.E2)
expresses H_h(s) as
a sqrt(pi)Gamma(9)[2/(as)]^(17/2) I_(17/2)(as), read as its entire
normalized power series. The real-zero theorem for J_(17/2) in
[DLMF 10.21(i)](https://dlmf.nist.gov/10.21.i) shows that H_h has only
imaginary nonzero zeros. Consequently G(s)!=0 for 0<Re s<1/2.

If J has any fixed polynomial upper bound, weighted Cauchy--Schwarz
makes P(s)=int_0^infinity p(y)e^(-sy)dy holomorphic on Re s>0.
Initially on Re s>1/2, absolute summation and logarithmic differentiation
of the checked [Euler product, DLMF 25.2.11](https://dlmf.nist.gov/25.2.E11)
give

\[
P(s)=-G(s)\frac{\zeta'(s+1/2)}{\zeta(s+1/2)}.
\tag{24}
\]

The prepared zero at s=1/2 cancels the pole contribution. An
off-critical nontrivial zero rho with Re rho>1/2 would instead leave
the nonzero residue -m_rho G(rho-1/2) in Re s>0. This contradicts
holomorphy. Zero symmetry then implies RH.

Conversely, under RH the absolutely convergent smoothed explicit
formula in note 04 gives p=O_g(1), because G(i gamma)=O(|gamma|^-6)
and the zero count is O(Tlog T); the trivial-zero tail is bounded.
It follows that J=O_g(1+Y) and mathcal V_g(X)=O_g(X^2).
Thus the proposed global estimates are logically RH-strength:

\[
{\rm RH}\Longleftrightarrow
J\hbox{ has a polynomial upper bound}
\Longleftrightarrow
\Theta_+(Y)=O((1+Y)^2)
\Longleftrightarrow (18).
\tag{25}
\]

For the last equivalence, (18) implies polynomial J by shell
summation, while RH supplies the stronger X^2 bound. The fixed
signed-pair condition following (19) is also RH-strength because
its diagonal already has the target order. These equivalences
classify the open estimates; they do not prove any of them.

The next concrete analytic obligation is therefore to bound the
combined signed actual-prime correlations in (19), or equivalently
the particular weighted covariance in (21), on the X^2log X scale.
Keep the complete relative interval, both cap blocks, and the signed
kernel before estimating. Generic PNT, a favorable sign of Phi,
or a Bessel/trace inequality cannot close this obligation; their
precise failures are established above. A proof must add genuine
arithmetic information about the actual prime correlations, and a
successful global bound would have the full strength stated in (25).
