# Real primitive reduction and bounded model remainder

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified from the current root turn metadata.

**Status: conditional local estimates proved in-note.** The complete energy,
relative period and both boundary payments admit a quadratic model with
explicit remainders bounded independently of the shrinking root separation.
A sharper direct upper bound strictly improves Note 01's coarse certificate
on a specified smaller window. The equally informed direct comparator has
the same estimates; no Hodge-specific advantage or theta exclusion follows.
See the [internal review][review] and [progress register][progress].

**Continuation.** [Note 04](04_ACTUAL_REGULAR_THETA_FIBER_COMPARISON_20261022.md) now acquires one actual
regular theta fiber under its own source/root contract and performs the
declared native comparison. The conditional event analysis here is retained.

Use the [result index][results], [avoid index][avoid],
[control register][controls], [criterion classification][a01],
[scoped conclusions][a07] and [coupled estimates][a12]. This is a quantitative
finite enclosure and boundary reduction. The inherited simplicity
reformulation and local nodal coefficient are not new claims.

## 1. Contract and declared comparison

Keep [Note 01][contract]'s unchanged canonical source, hypothetical ordinary
double (T,x_*), real A=H_zz/2 nonzero, complete moments M_j, disk |x|<r
and 0<tau<=sigma. All source tails, joint event equations, uncertain paths,
root charts and rounding remain paid there. Write
\[
 H=(x-\alpha)(x-\beta)V(x),\quad
 m=(\alpha+\beta)/2,\quad a=(\beta-\alpha)/2>0,\quad
 \nu=3|A|/4.
\]
The roots are real and interior. Set y_0²=(x-alpha)(x-beta), choosing
y_0(r)>0, and b=V^(-1/2) coherently with the marked outer lift. Thus
omega=b eta, eta=dx/y_0. The pure quadratic model uses the **same disk**,
not a silently recentered boundary; its energy is E_0=2 integral_Omega
1/(|x-alpha||x-beta|) dA. Its core period is 2 pi i.

The first comparison tests a complete relative-period/boundary enclosure,
then compares the resulting upper certificate with Note 01 (15). Every
root, unit, period and source observation is also supplied to direct
integration. A smaller shared direct bound is distinguished from a
Hodge-specific improvement. The diagnostic declared in §6 is a polynomial
calibration, not theta acquisition.

## 2. A single-valued real primitive retains the connector

Let q=integral_core omega, with Note 01's counterclockwise plus lift.
Let p run from the plus point over x=r to the minus point, through the
right branch beta. This is the reverse of the bottom cut orientation in
[Note 02][quadratic]. On this real event chart q is nonzero: the cut
average in §3 has one fixed nonzero phase.

Define
\[
 \lambda=i\bar q/|q|,\quad P=\operatorname{Re}(\lambda p),
 \quad S=-P|q|=\operatorname{Im}(\bar q p).
                                                               \tag{1}
\]
Since Re(lambda q)=0, h=Re(lambda F) is a globally single-valued harmonic
function on the annulus even though F is not. Choose its additive constant
so that h is odd under sheet interchange. If the plus boundary is
x=r exp(i theta), write its pulled-back differential as B(theta)dtheta,
and set
\[
 v(\theta)=\operatorname{Re}\!\left(\lambda\int_0^\theta B(s)ds\right),
 \quad t(\theta)=\operatorname{Im}(\lambda B(\theta)).
\]
Then v(0)=v(2 pi)=0, h_+=-P/2+v, h_-=-h_+. Cauchy–Riemann and Green give
\[
 \boxed{\mathcal E=\int_X|\nabla h|^2
 =\int_{\partial X}h\operatorname{Im}(\lambda\omega)
 =S+R,\quad R=2\int_0^{2\pi}v(\theta)t(\theta)d\theta.}       \tag{2}
\]
Both physical components contribute. The cut terms vanish for the real
primitive because h is single-valued; their information remains in P.
With the complex primitive and the preceding cut orientation, the real
cut payment is S/2 and the full physical-boundary payment is S/2+R.
Thus (2) does not discard half the logarithm found in Note 02.

If |B|<=K_boundary, then |v|<=K_boundary min(theta,2 pi-theta). Therefore
\[
 |R|\le2\pi^2K_{\rm boundary}^2,\qquad
 K_{\rm boundary}\le r/\sqrt{m_{\rm outer}},\quad
 m_{\rm outer}=3|A|r^2/8.                                  \tag{3}
\]
This gives the full interval [S-2 pi² K_boundary²,S+2 pi² K_boundary²]
intersected with [0,infinity). It is a bounded correction around a
potentially divergent relative period, not a bounded energy at the node.

## 3. Complete quadratic subtraction from the source chart

The simplex formula in Note 01 yields
\[
 |V|\ge\nu,\quad |V'|\le M_3/6,\quad |V''|\le M_4/12,
\]
\[
 |b|\le\nu^{-1/2},\quad |b'|\le L:=\frac{M_3}{12\nu^{3/2}},\quad
 |b''|\le K:=\frac{M_3^2}{48\nu^{5/2}}+\frac{M_4}{24\nu^{3/2}}.
                                                               \tag{4}
\]
The simplex barycentric integrals are 1/6 and 1/12. Collapsing the core
contour onto its real cut, with the chosen square root, gives
\[
 c:=\frac q{2\pi i}=\frac1\pi\int_0^\pi b(m+a\cos\theta)d\theta,
 \quad b_0=b(m),\quad |c-b_0|\le Ka^2/4.                  \tag{5}
\]
The linear Taylor term averages to zero. Also |c|<=nu^(-1/2).
The zero-period differential omega-c eta has a globally single-valued
holomorphic primitive G. Normalize G(beta)=0. Sheet interchange gives
G odd, hence G=y_0 f(x), with f holomorphic on the base disk, including
the branch points. In particular
\[
 ((x-m)^2-a^2)f'+(x-m)f=b-c.
\]
An exact identity retaining the whole quadratic energy is
\[
 \mathcal E=|c|^2\mathcal E_0+
 2\operatorname{Re}\!\left[\bar c\frac i2\int_{\partial X}G\bar\eta\right]
 +\frac i2\int_{\partial X}G\,d\bar G.                     \tag{6}
\]
The correction forms are single-valued, so every paired cut cancels in
them. The entire degeneration remains in E_0.

Here are explicit complete bounds. Put d_1=|x-alpha|, d_2=|x-beta|.
Polar Cauchy–Schwarz about any point alpha inside a radius-r disk gives
integral_Omega 1/d_1 dA<=2 pi r: the radial exit lengths rho obey
integral rho²=2 pi r². Since |x-m|<=(d_1+d_2)/2 and |x-m|<=2r,
\[
 I_1:=\int_\Omega\frac{|x-m|}{d_1d_2}dA\le2\pi r,\qquad
 I_2:=\int_\Omega\frac{|x-m|^2}{d_1d_2}dA\le4\pi r^2.
\]
Expanding |b_0+(b-b_0)|², without dropping its cross term, proves
\[
 |\mathcal E-|b_0|^2\mathcal E_0|\le C_{\rm osc},\qquad
 C_{\rm osc}=8\pi rL/\sqrt\nu+8\pi r^2L^2.                 \tag{7}
\]
Let R_-=r-|m|>a and R_+=r+|m|<=2r. Inclusion of centered disks and
Note 02's exact quadratic bounds give
\[
 4\pi\operatorname{arcosh}(R_-/a)\le\mathcal E_0
                      \le4\pi\operatorname{arsinh}(R_+/a).
                                                               \tag{8}
\]
Since a² arsinh(R_+/a)<=a R_+<=R_+², (5), (7) and (8) give
\[
 \boxed{|\mathcal E-|c|^2\mathcal E_0|\le C_E:=
 C_{\rm osc}+8\pi Kr^2/\sqrt\nu.}                         \tag{9}
\]
All constants are independent of the pair gap within the paid chart.
This is a finite-error theorem, not a claim of a new nodal coefficient.

Put ell=r-m>a and p_0=-2 arcosh(ell/a), matching p's plus-to-minus
orientation. Along the real path, |b(m+y)-b_0|<=Ly. Hence
\[
 |p-b_0p_0|\le2L\sqrt{\ell^2-a^2}\le4Lr,
\]
\[
 \boxed{|p-cp_0|\le C_p:=4Lr+2Kr^2.}                       \tag{10}
\]
For the last term use |c-b_0|<=Ka²/4 and
a² arcosh(ell/a)<=a ell<=ell²<=4r². With E_cuts=S/2,
\[
 |E_{\rm cuts}+\pi|c|^2p_0|\le\pi|c|C_p,
\]
\[
 \boxed{|E_{\rm physical}-|c|^2(\mathcal E_0+\pi p_0)|
                      \le C_E+\pi|c|C_p.}                \tag{11}
\]
Equations (9)–(11) pay the relative period and full physical boundary
together. Neither term is required to stay bounded; their quadratic
model terms retain both logarithmic contributions.

## 4. A strict improvement over the coarse direct certificate

All constants in the following sufficient window are specified before
data acquisition. The chart bounds imply
\[
 6\tau/5\le a^2\le10\tau/3,\quad
 |m|\le\frac{28M_3}{27|A|}\tau,\quad
 |V(m)-A|\le J\tau,\quad
 J=\frac{14M_3^2}{27|A|}+\frac{23M_4}{36}.                 \tag{12}
\]
For detail, the critical point obeys |c_critical|<=2M_3 tau/(3|A|).
Symmetric Taylor expansion at m gives |H_z(t,m)|<=M_3 a²/6; dividing
by the curvature floor gives |m-c_critical|<=M_3 a²/(9|A|).
In the simplex for V(m), the linear spatial term cancels and its second
moment gives |V(m)-H_zz(t,m)/2|<=M_4 a²/24. Combining the time and
spatial derivative bounds gives (12).

Since |V(m)|>=nu,
1/|V(m)|<=1/|A|+J tau/(|A|nu). Set
\[
 D=2r\sqrt{5/6},\quad c_*=\log2+1/4,
\]
\[
 K_* =\max\{0,3|A|C_{\rm osc}/(2\pi)+7c_*-16\},
 \quad s_* =\min\{\sigma,D^2,\nu/(6J),D^2e^{-2(K_*+1)}\}.
                                                               \tag{13}
\]
For theta moments J>0; if a polynomial calibration has J=0 omit its
division term. On 0<tau<=s_* a valid upper is
\[
 U(\tau)=4\pi\left(\frac1{|A|}+\frac{J\tau}{|A|\nu}\right)
       \operatorname{arsinh}(D/\sqrt\tau)+C_{\rm osc}.     \tag{14}
\]
It follows from (7), (8), a²>=6 tau/5 and R_+<=2r.
The coefficient is at most 7/(6|A|). For x>=1,
arsinh x<=log x+log2+1/4. Writing ell_*=log(D/sqrt(tau)) and comparing
with Note 01's B gives
\[
 B(\tau)-U(\tau)\ge\frac{2\pi}{3|A|}
 \left[\ell_*+16-7c_*-\frac{3|A|C_{\rm osc}}{2\pi}\right]
 \ge\frac{2\pi}{3|A|}>0.                                 \tag{15}
\]
Thus [s_*/2,s_*] is one declared bounded window with strict containment
[0,U] inside the previous [0,B]. This is a sharper **shared direct
baseline**, not a win over a direct method given the same model and
constraints. Both uppers diverge; the quantitative subtraction is
consistent with the inherited local logarithmic coefficient.

## 5. Acquired errors and matched controls

If measured periods have errors epsilon_q, epsilon_p, the center S in
(1) has the full additional error
\[
 |\widehat q|\epsilon_p+|\widehat p|\epsilon_q
                                   +\epsilon_q\epsilon_p.       \tag{16}
\]
Because p grows logarithmically, fixed absolute core-period error causes
logarithmic energy uncertainty. An acquired O(1) remainder requires
improving q accuracy or a paid correlated product bound. An O(1) exact
remainder alone does not establish numerical conditioning or speed.

For (2), prefer the nonsingular center S=Im(bar q p) over treating lambda
as an error-free observation. If R is acquired, the errors in its v and t
include their shared q-dependent rotation and cumulative primitive error,
with the full bilinear product payment as in Note 01 (7). Using (3)
instead needs a certified K_boundary. Uncertain roots, m,a,V, the model
E_0 and constants in (4), (12)–(14) require joint enclosures; interval
uncertainty may erase the exact-data improvement in (15).

The quadratic has V constant: G=0, C_E=C_p=0, and retains divergent p_0
and energy exactly. Neighboring-root and other ordinary-double charts
retain the same generic estimates. Euler factors change canonical
arithmetic; weighted-square/finite-prime controls fail the complete
normalized reflection conjunction and unchanged full coefficients;
reflected/primitive controls lack canonical square coefficients, with
their preservation lists kept separate. None of these failed literal
theta premises enters the generic proof as a discriminator. These bounds
are collision-compatible and imply no all-height or all-multiplicity
endpoint exclusion. RHE-05 remains gated.

## 6. Bounded calibration and next gate

The [diagnostic][script] uses the exact heat polynomial
H(t,x)=x²+epsilon x³-2t-6 epsilon t x, epsilon=1/10, A=1.
For the inherited local derivative-chart construction use
M_2=13/5, M_3=3/5, M_4=M_6=0, r=5/12 and the resulting sigma.
These are direct polynomial sup bounds replacing theta moments, not
canonical-source values. Interpret the sigma term |A|/(4M_4) as infinity
when M_4=0, so it is omitted in this polynomial check. Evaluate
tau=s_*/2,s_*/4,s_*/8. Before execution
the checks are fixed: the full real-primitive identity, quadratic model
remainder, relative-period remainder and strict upper comparison.
The receipt records the script hash, precision and quadrature schedule.
This is floating diagnostic evidence; equations (2), (9)–(15) are proved
above without numerical reliance.

The next acquisition candidate should use full boundary data to compute
R or G with joint errors, aiming at a smaller **complete** interval or
measured total cost than direct evaluation receiving all those data.
An actual regular theta fiber can test this without locating a hypothetical
double, but needs its own paid root/unit chart; the event-conditioned
constants above cannot be claimed acquired for that regular fiber.
A finite source-paid remainder is now available; a theta-specific signed
restriction or Hodge-specific efficiency gain remains open. A numerical
campaign is not justified merely by the exact subtraction.

[contract]: 01_FINITE_COVER_CONTRACT_AND_ENERGY_ENCLOSURE_20261022.md
[quadratic]: 02_FULL_QUADRATIC_ENERGY_AND_TRANSVERSE_PAYMENT_20261022.md
[review]: ../reviews/02_REAL_PRIMITIVE_AND_MODEL_REMAINDER_REVIEW_20261022.md
[progress]: ../research-progress/01_RECIPROCAL_HODGE_ENERGY_PROGRESS_20261022.md
[script]: ../numerics/02_coupled_energy_diagnostic_20261022.py
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
