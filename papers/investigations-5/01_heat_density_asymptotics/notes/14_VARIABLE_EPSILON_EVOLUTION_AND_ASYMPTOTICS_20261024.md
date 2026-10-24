# Variable epsilon: exact evolution, weak bias, and two asymptotic choices

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**.

**Status: identities and estimates proved in-note; exact polynomial
control checks; same-assistant review only.** Written after the
[fixed-regulator manuscript][manuscript], as requested. This note treats
epsilon as a positive function of heat time and height, and also gives
the more general spatial formulas. The theta heat equation is unchanged.

There are two distinct corrections. A variable regulator adds forcing
to the potential equation. Spatial variation also breaks the identity
between the positive algebraic density and the Laplacian of that
potential. Both corrections are needed; adding only a forcing term to
the old density equation is generally wrong.

This is an approximation and evolution-bookkeeping milestone, not an
RH-equivalent criterion or an endpoint-simplicity claim. See the
[result index][results], [avoid index][avoid], particularly
[constant/normalization slips][a08] and [scope][a07], and the
[collision-control register][controls].

## 1. Definitions and what changes

Let H(t,z) be holomorphic in z=x+iy and solve H_t=-H_zz. In applications
it is the unchanged canonical theta field of Notes [11][negative] and
[12][positive]. Take a smooth positive regulator and put

\[
q(t,x,y)=\epsilon(t,x,y)^2,\quad r=\log q,\quad
f=|H|^2,\quad D=f+q,\quad S=\log D,\quad w=q/D.
\tag{VE1}
\]

The positive density and its natural frozen-regulator current remain

\[
\rho=\frac{q|H_z|^2}{\pi D^2},\qquad
j=\frac{qH_{zz}\overline{H_z}}{\pi D^2},\qquad
\mathbf j=(\Re j,\Im j).
\tag{VE2}
\]

These are smooth at zeros because q>0. Define separately

\[
\widetilde\rho=\frac{\Delta S}{4\pi},\qquad
C_\epsilon=\widetilde\rho-\rho.
\tag{VE3}
\]

Unlike rho, tilde-rho need not be nonnegative. Spatial derivatives in
this note act on both H and q. The required time/space differentiability
can be reduced for individual identities; smooth q suffices for all
displayed differentiated equations. Weak forms need only the derivatives
appearing in their pairings.

## 2. The potential forcing

Write square=partial_x^2-partial_y^2. Direct differentiation gives

\[
\boxed{
S_t=-\frac12\{\square S+S_x^2-S_y^2\}+\mathcal B_\epsilon,
\qquad
\mathcal B_\epsilon=\frac{q_t+\tfrac12(q_{xx}-q_{yy})}{D}.}
\tag{VE4}
\]

Equivalently,

\[
\mathcal B_\epsilon
=w\left[r_t+\frac12(r_{xx}-r_{yy}+r_x^2-r_y^2)\right].
\tag{VE5}
\]

Indeed f_t=-2 Re(H_zz conjugate(H)),
f_xx-f_yy=4 Re(H_zz conjugate(H)), and
square S+S_x^2-S_y^2=(square D)/D. These identities prove VE4 without
division by H.

For the author's height/time choice epsilon=epsilon(t,x),

\[
\boxed{
\mathcal B_\epsilon
=\frac{2\epsilon\epsilon_t+\epsilon\epsilon_{xx}+\epsilon_x^2}
{|H|^2+\epsilon^2}
=w\{r_t+\tfrac12(r_{xx}+r_x^2)\}.}
\tag{VE6}
\]

If epsilon depends only on time, this is w r_t=2w epsilon_t/epsilon.
It is a measurement forcing: it does not alter H_t=-H_zz.

## 3. Spatial variation changes the density-potential relation

The exact correction is

\[
\boxed{
4\pi C_\epsilon
=\frac{\Delta q}{D}
-\frac{2\nabla f\cdot\nabla q+|\nabla q|^2}{D^2}.}
\tag{VE7}
\]

To verify it, use Delta f=4|H_z|^2 and
|grad f|^2=4f|H_z|^2 in Delta log(f+q).
Two useful equivalent forms, smooth at the zeros, are

\[
\begin{split}
4\pi C_\epsilon
&=w\Delta r+2\nabla w\cdot\nabla r-w(1-w)|\nabla r|^2\\
&=2\,\operatorname{div}(w\nabla r)
  -w\Delta r-w(1-w)|\nabla r|^2.
\end{split}
\tag{VE8}
\]

Here grad w=w(grad r-grad S). No logarithmic derivative of H is needed.
For time-only epsilon, C_epsilon=0 exactly. For height/time epsilon,
only x derivatives occur in VE7 and VE8, but the correction usually
does not vanish.

A constant nonzero heat field already distinguishes the two densities:
rho=0 while Delta log(|H|^2+q)/(4pi) can be nonzero.
The Gaussian example in Section 7 makes the sign failure quantitative.

## 4. The exact current source and the averaged equations

The frozen-regulator current no longer gives a source-free continuity
equation:

\[
\boxed{
\rho_t+\operatorname{div}\mathbf j
=(1-2w)\{r_t\rho+\nabla r\cdot\mathbf j\}
=:\mathcal S_\epsilon.}
\tag{VE9}
\]

**Proof.** At fixed q the earlier continuity identity holds.
The explicit regulator derivatives satisfy
partial_q rho=rho(1-2w)/q and partial_q j=j(1-2w)/q.
The chain rule adds q_t partial_q rho and
sum_i q_i partial_q j_i, proving VE9. Thus for epsilon(t) alone,
the source is r_t(1-2w)rho. A source in this regularized measurement
does not assert creation or destruction of holomorphic zeros.

### Fixed filters

Let F be any fixed positive normalized space-time convolution. Put
U=FS, R=F rho, Cbar=F C_epsilon, Bbar=F B_epsilon, and retain the actual
gradient covariance

\[
Q=F(S_x^2-S_y^2)-(U_x^2-U_y^2).
\]

Then

\[
U_t=-\tfrac12\{\square U+U_x^2-U_y^2+Q\}+\overline{\mathcal B},
\qquad \Delta U=4\pi(R+\overline C),
\tag{VE10}
\]

and therefore

\[
\boxed{
R_t=-\tfrac12\square R-\frac1{8\pi}\Delta(U_x^2-U_y^2+Q)
+\frac1{4\pi}\Delta\overline{\mathcal B}
-\partial_t\overline C-\tfrac12\square\overline C.}
\tag{VE11}
\]

The current version is simpler:

\[
\boxed{R_t+\operatorname{div}(F\mathbf j)=F\mathcal S_\epsilon.}
\tag{VE12}
\]

These are exact identities, not a closed reduced PDE. In particular,
F[(1-2w)r_t rho] is not generally a product of separate means.
For time-only epsilon the two Cbar terms vanish, but the forcing and
current source remain.

### Moving averaging widths are a separate correction

For a variable filter F, define
C_a[g]=partial_a(Fg)-F(partial_a g) and
C_aa[g]=partial_a^2(Fg)-F(partial_a^2 g). The latter is a second
derivative commutator, not C_a composed with itself.
With m_i=F S_i=U_i-C_i[S] and
Q=F(S_x^2-S_y^2)-(m_x^2-m_y^2), the exact formulas are

\[
\begin{split}
U_t={}&-\tfrac12\square U
-\tfrac12(m_x^2-m_y^2+Q)+F\mathcal B_\epsilon\\
&+C_t[S]+\tfrac12\{C_{xx}[S]-C_{yy}[S]\},\\
\Delta U={}&4\pi F(\rho+C_\epsilon)+C_{xx}[S]+C_{yy}[S],\\
R_t+\operatorname{div}(F\mathbf j)
={}&F\mathcal S_\epsilon+C_t[\rho]+C_x[j_x]+C_y[j_y].
\end{split}
\tag{VE13}
\]

For example, if
Fg(t,x,y)=int k(a)g(t,x+ell(t,x)a,y) da, then

\[
C_x[g]=\ell_x\int a k(a)g_x\,da,\quad
C_t[g]=\ell_t\int a k(a)g_x\,da,
\]
\[
C_{xx}[g]=\int k(a)
\{(2a\ell_x+a^2\ell_x^2)g_{xx}+a\ell_{xx}g_x\}\,da.
\tag{VE14}
\]

Arguments of g in VE14 are the shifted ones above. The regulator
corrections and these filter commutators must not be conflated.

## 5. A weak adaptive-regulator error bound

Here the logarithmic bias method from [Note 06][regulator] extends
without estimating H_z/H near zeros. Fix a time, let nu be the zero
measure including multiplicities, and set

\[
L_q=\log(1+q/|H|^2).
\]

For a real compactly supported C^2 test function psi, distributional
integration by parts and VE8 give the exact identity

\[
\boxed{
4\pi\langle\rho-\nu,\psi\rangle
=\int L_q\Delta\psi
+2\int w\nabla r\cdot\nabla\psi
+\int w\{\Delta r+(1-w)|\nabla r|^2\}\psi.}
\tag{VE15}
\]

All integrals are with respect to planar area. Indeed
tilde-rho-nu=Delta L_q/(4pi), while rho=tilde-rho-C_epsilon.
The divergence form in VE8 gives the two additional weak terms and
their signs.

Let B_1=||grad r||_infinity and B_2=||Delta r||_infinity on the test
support, and define

\[
\mathcal K_r(\psi)=\|\Delta\psi\|_\infty
+2B_1\|\nabla\psi\|_\infty
+(B_2+B_1^2)\|\psi\|_\infty.
\tag{VE16}
\]

Since 0<=w<=L_q (away from zeros, and hence almost everywhere),

\[
\boxed{
|\langle\rho-\nu,\psi\rangle|
\le\frac{\mathcal K_r(\psi)}{4\pi}\int_{\operatorname{supp}\psi}L_q.}
\tag{VE17}
\]

This is the old logarithmic-integral bound with an explicit enlarged
test-function constant. A lower bound on epsilon does not enter this
static weak estimate; upper bounds on epsilon and spatial derivatives
of log epsilon do.

To make it finite, let epsilon_max bound epsilon on the support.
If |H|>=b outside controlled disks, and
|H|>=c_j|z-a_j|^{m_j} on disk j, then

\[
\int L_q
\le |\Omega|\epsilon_{\max}^2/b^2
+\sum_j I_{m_j}((\epsilon_{\max}/c_j)^{1/m_j},R_j),
\tag{VE18}
\]
\[
I_m(a,R)=2\pi\int_0^R s\log(1+(a/s)^{2m})\,ds.
\]

The disk radii R_j must cover the part actually integrated.
In particular
I_1<=pi a^2[1+log(1+R^2/a^2)], and for m>=2,
I_m<=pi a^2[m+log2+1/(m-1)], as proved in Note 06.

**Local removal corollary.** If epsilon_delta(z)=delta a(z) with
positive smooth a on a compact buffer, then spatial derivatives of
r=2log delta+2log a are independent of delta. VE17--VE18 give weak
convergence rho_delta -> nu, at rate O(delta^2 log(1/delta)) for
simple zeros and O(delta^{2/m}) for a zero of multiplicity m>=2.
The statement includes zero-free regions and multiple zeros. It supplies
no simplicity criterion. Uniformity in time requires uniform floors,
disk data and logarithmic-derivative bounds on a common time buffer.

## 6. Negative time: matching epsilon to the source amplitude

Let t=-T and C_T=phi_0 sqrt(pi)/(2 sqrt(T)), as in Note 11.
A particularly clean time-only regulator is

\[
\epsilon(-T)=\eta C_T,\qquad \eta>0\text{ fixed}.
\tag{VE19}
\]

Let E=exp[-(xi^2-upsilon^2)/2]. The exact Gaussian density then gives

\[
\boxed{
T\rho_{\epsilon(-T)}
  (-T,\sqrt T(\xi+i\upsilon))
\longrightarrow
F_\eta(\xi,\upsilon)
=\frac{\eta^2(\xi^2+\upsilon^2)E}
{4\pi(\eta^2+E)^2}.}
\tag{VE20}
\]

The error is O_(A,eta)(1/T), uniformly for every real xi and
|upsilon|<=A. Thus a changing regulator produces a different stationary
scaled profile: T rho, rather than T^2 rho for fixed epsilon.

**Explicit bound and proof.** Use the complete-source quantities
d_0,d_1,Q_0,P from Note 11, with the same transverse parameter A.
For each fixed T, its density stability inequality is still valid with
epsilon=eta C_T. Thus

\[
\left|T\rho-F_\eta\right|
\le T\left\{
\frac{2P d_1}{\pi\eta^2 C_T^2}
+\frac{4Q_0P^2d_0}{\pi\eta^4 C_T^4}
\right\}=O(T^{-1}).
\tag{VE21}
\]

No denominator expansion or height cutoff is needed: F_eta is exactly
T times the Gaussian density under VE19. Positive normalized averages
transfer this bound on the stated buffer.

Here r_t=1/T, C_epsilon=0, B_epsilon=w/T, and the exact current source
is (1-2w)rho/T. Changing epsilon to preserve a nontrivial scaled profile
does not permit dropping those terms from an evolution equation.

## 7. A zero-free Gaussian control for height adaptation

Height adaptation can also manufacture a substantial background.
Consider the **exact** zero-free heat field

\[
G_T(z)=C_Te^{-z^2/(4T)},\quad t=-T,
\qquad
q(T,x)=\eta^2C_T^2e^{-x^2/(2T)}.
\tag{VE22}
\]

This is a height/time regulator, with no y dependence. Its logarithm
satisfies

\[
r_t=T^{-1}-x^2/(2T^2),\quad r_x=-x/T,\quad r_{xx}=-1/T,
\qquad \mathcal B_\epsilon=w/(2T).
\tag{VE23}
\]

On y=0, w=eta^2/(1+eta^2) is constant in x, but

\[
\boxed{
\rho=\frac{\eta^2x^2}{4\pi T^2(1+\eta^2)^2},
\qquad
\widetilde\rho=-\frac{w}{4\pi T}<0.}
\tag{VE24}
\]

For the second equality, write
S=log C_T^2-x^2/(2T)+log(e^{y^2/(2T)}+eta^2).
Then S_xx=-1/T and S_yy=(1-w)/T at y=0.
The positive density in VE24 follows from |G_T'/G_T|=|z|/(2T).

For instance eta^2=1/2,T=2,x=3 gives
pi rho=1/8, pi tilde-rho=-1/24 and B_epsilon=1/12.
The field has no zeros at all. This control demonstrates both why the
curvature correction cannot be omitted and why simply making epsilon
track a decaying real-axis envelope need not yield a useful all-height
zero density. It is a scoped counterexample to that prescription,
not an exclusion of every adaptive regulator.

The tempting choice epsilon=eta|H| is not a positive smooth regulator
at zeros and is outside VE1's hypotheses.

## 8. Positive time: an adaptive choice with a retained clock error

Keep the complete-source definitions M,mu,v,L,kappa and the fixed
transverse and averaging widths Y>h>0, ell>0 from Note 12.
Use its explicit upper moment allowances to construct the carrier disks
and floors, on X~kappa^(1/3). For a fixed exponent p>1/2 choose

\[
\boxed{
\epsilon(t,x)=M(t)\kappa(t)^{-p}\exp[-v(t)x^2/2].}
\tag{VE25}
\]

This regulator is defined without choosing theta zeros. It is positive
at every finite height; its physical magnitude can be large, while its
ratio to M is small. The asymptotic conclusions below concern only the
proved inner window with |x|+ell+r_disk<X and |y|+h<=Y.

Its spatial logarithmic derivatives are

\[
r_x=-2vx,\qquad \Delta r=-2v.
\tag{VE26}
\]

Uniformly on the buffer, B_1=O(kappa^(-2/3)),
B_2=O(kappa^(-1)), and epsilon_max/M<=kappa^(-p).
Apply VE17 to the translated averaging kernel K, and VE18 to H/M.
The source-allowance construction has
b_*=Theta(kappa^(-1/2)), c_*=Theta(L),
r_disk=Theta(kappa^(-1/2)/L), and n_ell=O(L).
Thus the explicit new regulator allowance is

\[
\mathcal E_{\rm reg}^{\rm var}
=\frac{\mathcal K_r(K)}{4\pi}
\left\{
\frac{4\ell h\,\kappa^{-2p}}{b_*^2}
+n_\ell\overline I_1(\kappa^{-p}/c_*,2r_{\rm disk})
\right\}
=O(\kappa^{1-2p}).
\tag{VE27}
\]

The disk term is
O(kappa^(-2p) log(kappa)/L), smaller than the outside term.
The constants are uniform on the buffered growing window at fixed
ell,h,Y,p. Taking the explicit upper moment allowances, rather than
asserting only an upper order for an unknown delta, justifies the
two-sided floor orders used here.

Combining this with Note 12's unchanged root and lattice errors proves

\[
\boxed{
K*\rho_{\epsilon(t,\cdot)}(t,x,y)
=\frac{L(t)}{\pi}k_h(y)
+O(\kappa^{-1/2}+L^{-3}+\kappa^{1-2p}).}
\tag{VE28}
\]

In particular p>=3/4 retains the earlier error rate.
The simple choice p=1 makes the new regulator contribution O(kappa^-1).
The normalized shape pi R/L is still stationary on this growing window.
No new theta root calculation is needed.

### Its evolution terms are explicit and need not be small

Let m_j=E[(u-mu)^j] be centered source moments.
Differentiating the complete probability law gives

\[
(\log M)'=\mu^2+v,\qquad
v'=2\mu m_3+m_4-v^2,\qquad
L'=2L/\kappa,\quad \kappa'=8L+8tL'-2.
\tag{VE29}
\]

For VE25,

\[
r_t=2(\mu^2+v)-2p\kappa'/\kappa-v'x^2,
\tag{VE30}
\]
\[
\boxed{
\mathcal B_\epsilon
=w\{2\mu^2+v-2p\kappa'/\kappa+(2v^2-v')x^2\},\quad
\mathcal S_\epsilon=(1-2w)\{r_t\rho-2vx\,j_x\}.}
\tag{VE31}
\]

For example, v'=Cov((u-mu)^2,u^2)
=2mu m_3+m_4-v^2; the derivative of mu inside the centered square has
zero mean. This proves the moment identity, with no source truncation.

The leading r_t includes 2mu^2. A small static regulator-bias bound
therefore does not justify treating the temporal correction as small.
The cancellations needed for a quantitative averaged current or
covariance evolution still require estimates.


### A fully explicit version using the saddle alone

The complete moments in VE25 are not necessary for a regulator with
this rate. Put

\[
M_0(t)=2\pi^2e^{q_t(L)}\sqrt{\frac{2\pi}{\kappa}},\qquad
\boxed{\epsilon_{\rm sad}(t,x)
=M_0(t)\kappa(t)^{-p}\exp[-x^2/(2\kappa(t))].}
\tag{VE32}
\]

Here q_t(u)=tu^2+9u-pi exp(4u) is the source saddle exponent
from Note 12, distinct from the regulator square q in VE1.
Both L (through its displayed Lambert-W expression) and kappa are
explicit scalar functions of t. This prescription uses neither source
moment integrals nor theta zeros.

The complete-source normalization gives
M_0/M<=sqrt(2pi)/Z_-=:C_M, with C_M->1. In VE27 replace kappa^(-p)
by C_M kappa^(-p), B_1 by sup 2|x|/kappa, and B_2 by 2/kappa.
These are explicit finite allowances and have the same orders, proving
VE28 for epsilon_sad as well.

For this choice the evolution forcing is also explicit. Since
d[q_t(L(t))]/dt=L^2 by stationarity of the saddle,

\[
r_t=2L^2-(2p+1)\kappa'/\kappa+x^2\kappa'/\kappa^2,\qquad
r_x=-2x/\kappa,\quad r_{xx}=-2/\kappa,
\tag{VE33}
\]
\[
\boxed{
\mathcal B_{\epsilon_{\rm sad}}
=w\left\{2L^2-(2p+1)\frac{\kappa'}{\kappa}
-\frac1\kappa+\frac{(\kappa'+2)x^2}{\kappa^2}\right\},\qquad
\mathcal S_{\epsilon_{\rm sad}}
=(1-2w)\{r_t\rho-2xj_x/\kappa\}.}
\tag{VE34}
\]

For a concrete recommended starting choice take p=1.
Its regulator bias is O(kappa^-1), within the previously proved
O(kappa^-1/2+L^-3) total error on the buffered growing window.
The explicit prescription is defined beyond that window, but the
asymptotic error theorem is not: the Gaussian control in Section 7
prevents inferring a useful outer-height density merely from the formula.

## 9. Validation, controls and remaining work

The [exact check script][checkscript] expands polynomial identities
over rational coefficients, with no external symbolic package.
For H=z^2-2t it checks potential forcing, the direct curvature
correction, the divergence form of that correction, and the current
source for q=1, 1+t^2, 1+t^2+x^2, and 1+t^2+x^2+2y^2.
All **16 cleared polynomial residuals are identically zero**.
The nonconstant controls explicitly detect nonzero terms that would be
lost by reusing the fixed-epsilon equations. This polynomial has a
double event at t=z=0; the identities remain valid there.
The small [record][checkrecord] includes exact Gaussian coefficients
from VE24, as a formula check rather than a separate theta computation.

The generic identities and weak-bias theorem apply to collision
controls when their holomorphy and local floor hypotheses hold.
They are not required to reject a collision: multiplicity is explicitly
allowed. The canonical endpoint estimates additionally use the exact
source assumptions of Notes 11--12; their existing control screen
continues to apply. Changing epsilon does not change the zero set,
the Vandermonde, the exterior force, or the underlying heat equation.

**What is gained:** the full adaptive-regulator equations, a weak
error budget that retains spatial logarithmic derivatives, an all-height
negative-time stationary profile with O(T^-1) scaled error, and an
explicit positive-time height/time regulator preserving the existing
inner clock rate, including a version that uses only the scalar saddle.

**Still open:** a useful positive-time outer-height approximation for
a chosen adaptive regulator, uniformly through the amplitude turnover;
bounds on the new forcing/current averages and differentiated
covariances; a stable reduced boundary evolution; independently
reviewed proofs and certified finite source-onset data. The fixed-epsilon
all-height obstruction in Note 11 is inapplicable to a regulator that
vanishes with height, but its inapplicability is not a proof of a global
stationary clock. The Gaussian control shows that such a conclusion
requires additional work.

[manuscript]: ../manuscript/main.tex
[negative]: 11_TWO_TIME_LIMITS_ALL_HEIGHT_ERROR_20261024.md
[positive]: 12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md
[regulator]: 06_REGULATOR_BIAS_FOR_SMOOTHED_ZERO_COUNTS_20261024.md
[checkscript]: ../numerics/variable_epsilon_identity_checks.py
[checkrecord]: ../numerics/VARIABLE_EPSILON_IDENTITIES_20261024.json
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[a08]: ../../../../avoid/08_normalization_and_constant_slips.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
