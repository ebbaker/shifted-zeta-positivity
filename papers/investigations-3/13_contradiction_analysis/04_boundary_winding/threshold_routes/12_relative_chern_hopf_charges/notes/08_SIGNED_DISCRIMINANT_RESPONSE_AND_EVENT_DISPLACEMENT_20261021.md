# Signed discriminant response, event displacement, and finite-moment limits

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **ultra**, supplied from the parent turn's verified
metadata; the delegated agent inherits that configuration. Proofs are by
the authoring assistant. Separate same-model checks are recorded in [Review 08][review];
no independent specialist validation is claimed.

**Status: proved below under the displayed hypotheses.** The new results
are an exact logarithmic response formula for a proper two-root
discriminant, an explicit quadratic remainder for its signed first
variation, and the first two derivatives of a real double-event time
under an affine source perturbation. A matching control construction
shows that any finite collection of the specified complete envelope
moments can stay exactly fixed while a local event moves to either side
of zero. This last result is about a constructed colliding source; its
moment values are not the actual theta moment values, and no global
positive-time real-rootedness is claimed.

Appendix A additionally composes this consumer with BW14's canonical
theta-tail law. It proves a signed complete-source discriminant interval,
strictly narrower than the matched pointwise envelope with the same
nonlinear payment, and conditional applicability near each putative
double. Its lower bound is not proved positive.

No positive signed margin for the unchanged theta source is proved. The response
formula supplies a concrete coupled consumer and an error payment for
ECE-02; it does not complete ECE-02 or exclude an endpoint. The
finite-moment obstruction is scoped to the stated information class.

Read the [result index][results], [collision control register][controls]
and [avoid index][avoid], particularly [target classification][a01],
[matching controls][a02], [scope][a07] and [coupled estimates][a12]. The
identity that endpoint integration constant equals endpoint discriminant
remains the target already stated in the [program][program]. The gains
here are quantitative response and a proved local information limitation.

## 1. A fixed-cap comparison that permits an internal double

Fix a real time t for the moment. Let F and H=F+E be holomorphic near the
closed disk |z-a|<=R, where a is real. Suppose F is nonzero on its boundary
Gamma, has exactly two zeros counted with multiplicity inside, and both
are in |z-a|<r<R. Write c for their centroid and Delta_F for their squared
difference. The roots may coincide. Assume the complete wall estimate

\[
 q:=\sup_\Gamma |E/F|<1.                                      \tag{1}
\]

Rouche's argument gives two roots of H_s=F+sE in the disk for every
real 0<=s<=1 (indeed for complex |s|q<1). Thus H has a proper two-root
fiber. If a smaller target inner disk is needed for Note 05, its separate
count/wall must still be supplied; (1) alone does not supply that collar.
For this fixed-cap response no heat equation or smaller target disk is
needed. The reference roots imply |c-a|<=r.

Set f=E/F on the wall. Because |f|<1, the series

\[
 \ell=\log(1+f)=\sum_{n\ge1}(-1)^{n+1}f^n/n                  \tag{2}
\]

is a single-valued analytic function on an annulus around Gamma. It need
not extend through the interior zeros of F. Define
I[g]=(2 pi i)^{-1} integral_Gamma g(z) dz. Then the exact response is

\[
 \boxed{\Delta_H-\Delta_F
 =-4I[(z-c)\ell]-(I[\ell])^2.}                              \tag{3}
\]

**Proof.** Let w=z-a and let S_k be the sum of the kth powers of the two
centered roots, equivalently I[w^k F_z/F]. On the annulus,
H_z/H-F_z/F=ell_z. Integration by parts along the closed contour gives
S_1(H)-S_1(F)=-I[ell] and S_2(H)-S_2(F)=-2I[w ell]. Since
Delta=2S_2-S_1^2 and S_1(F)=2(c-a), expanding the square gives (3).
No division by the internal root gap occurs. All contour orientations are
counterclockwise. The same proof applies at a multiple root because the
argument-principle moments count multiplicities.

The signed first variation is

\[
 L_F(E)=-4I[(z-c)E/F].                                      \tag{4}
\]

Put l_1(q)=-log(1-q) and l_2(q)=-log(1-q)-q. The uniformly convergent
series gives |ell|<=l_1 and |ell-f|<=l_2, hence

\[
 \boxed{|\Delta_H-\Delta_F-L_F(E)|
 \le B(q):=4R(R+r)l_2(q)+R^2l_1(q)^2.}                       \tag{5}
\]

Indeed |I[g]|<=R sup_Gamma|g| and |z-c|<=R+r. In particular
B(q)=[2R(R+r)+R^2]q^2+O(q^3). The bound is finite at an internal double.
Its wall ratio q and spatial scale are material dependencies: this is
not a height-uniform condition number, and it does not remove a small
external wall floor.

If both functions are real-symmetric, the discriminants and (4) are real.
A rigorously established enclosure L_F(E) in [L_-,L_+] therefore gives

\[
 \Delta_F+L_- -B(q)\le\Delta_H\le\Delta_F+L_++B(q).           \tag{6}
\]

This is the selected signed observable and its error contract. A strict
positive lower bound at a negative cap can feed the Note 05 charge
consumer after its complete spatial and phase hypotheses are paid. The
same bound at t=0 directly excludes a double in that two-root fiber.
Neither application makes the inequality automatic or proves its theta
inputs. There is no claim of comparative superiority to direct exclusion.

## 2. The complete source functional

Suppose the residual is a complete cosine-source difference

\[
 E(t,z)=\int_0^\infty\psi(u)e^{tu^2}\cos(zu)\,du,
\]

with sufficient domination on the whole wall. At a real cap the first
variation is the single signed integral

\[
 L_F(E)=\int_0^\infty\psi(u)e^{tu^2}K_F(u)\,du,\qquad
 K_F(u)=-4I\left[\frac{(z-c)\cos(zu)}{F(t,z)}\right].           \tag{7}
\]

The kernel is real by conjugation symmetry. Interchanging the contour
and source integrals is justified, for example, by a proved wall floor
|F|>=delta>0 and the finite complete residual majorant

\[
 N_\psi(t,R)=\int_0^\infty|\psi(u)|e^{tu^2}\cosh(Ru)\,du.
\]

These inputs also give q<=N_psi/delta. The signed integral (7) should be
estimated before any triangle inequality over source modes or contour
arcs. Bound (5) then pays the nonlinear response. A numerical use must
include omitted modes, exterior source tails, quadrature and entire-arc
errors in both (1) and (7). No such new source acquisition is claimed here.

At an exact double of F at z=b=c, write F=U(z-b)^2. A residue calculation
in (4) gives

\[
 \boxed{L_F(E)=-4E(t,b)/U(t,b)=-8E(t,b)/F_{zz}(t,b).}          \tag{8}
\]

Thus the infinitesimal sign at the event is an oscillatory source
measurement divided by a nonzero curvature. Positivity or an absolute
moment upper bound does not determine it. Formula (8) is a sensitivity
identity, not a new theta positivity assertion.

## 3. Event-time response and a paid second-order error

Let H_s(t,z)=H_0(t,z)+sE(t,z) be a real-symmetric affine family satisfying
H_{s,t}=-H_{s,zz}; E satisfies the same heat equation. Suppose H_0 has
an ordinary real double at (tau_0,b_0):
H_0=H_{0,z}=0 and N:=H_{0,zz} is nonzero there. The Jacobian of
(H_s,H_{s,z}) with respect to (t,z) at the event has determinant -N^2.
The analytic implicit-function theorem therefore supplies a unique
local real event branch (tau_s,b_s). At a point on that branch set
N=H_{s,zz}, M=H_{s,zzz}, P=H_{s,zzzz}, with all quantities evaluated
at the event. Direct differentiation gives

\[
 \boxed{\tau'_s=E/N,\qquad b'_s=(M\tau'_s-E_z)/N,}             \tag{9}
\]
\[
 \boxed{\tau''_s=(P/N)(\tau'_s)^2
                -2(E_{zz}/N)\tau'_s-(b'_s)^2.}              \tag{10}
\]

For (10), differentiate H_s(tau_s,b_s)=0 twice. Substituting
H_tt=P, H_tz=-M, H_t=-N, E_t=-E_zz and then
N b'=M tau'-E_z reduces the cross terms to -N(b')^2.
This derivation fixes the backward-heat signs and does not use individual
root labels. In particular, if a persistent proper two-root cluster
has discriminant Delta_s, then partial_s Delta_s at the event is
-8E/N and Delta_{s,t}=8; implicit differentiation of Delta_s(tau_s)=0
recovers the first formula in (9).

Here is one explicit finite error payment. Suppose this real branch
exists on 0<=s<=1 and independently established bounds along it are
|N|>=nu>0, |P|<=C_4, |E|<=E_0 and |E_zz|<=E_2. Since -(b')^2<=0,

\[
 \tau''_s\le B_+:=C_4 E_0^2/\nu^3+2E_2E_0/\nu^2,
\]
\[
 \boxed{\tau_1\le\tau_0+E(\tau_0,b_0)/H_{0,zz}(\tau_0,b_0)
                         +B_+/2.}                            \tag{11}
\]

If the right side is strictly negative, (11) locates this event below
zero. To exclude another endpoint event, all hypotheses of the Note 05
at-most-one theorem must hold for the final family in the same window.
Existence of the branch for the full homotopy and its curvature bounds
are unpaid inputs until proved; the local implicit theorem alone does
not establish them for s=1. Curvature nu can shrink with event height.
No actual theta event-location margin is obtained here.

### 3.1 Paying continuation and curvature from common walls and cap margins

The full-branch and curvature inputs in (11) admit a quantitative payment
using the proper-cluster data. Let the reference F=H_0 and every H_s have
two roots inside |z-a|<r<R throughout the same closed time rectangle,
with common outer wall floor |H_s|>=delta>0 and a common strict phase
bound. Assume F has opposite real cap signs. Write

\[
 m=\min\{-\Delta_F(t_-),\Delta_F(t_+)\}>0.
\]

If |E/F|<=q<1 on both outer spatial circles at those two cap times, (3)
applied to sE gives the uniform bound

\[
 |\Delta_s(t_\pm)-\Delta_F(t_\pm)|
 \le C_{\rm cap}:=4R(R+r)l_1(q)+R^2l_1(q)^2.
 \tag{11a}
\]

Thus C_cap<m suffices to retain opposite nonzero signs at both caps for
all 0<=s<=1. Note 05 then gives exactly one real event for each s, with
spatial multiplicity two and Delta_{s,t}=8. The local implicit branches
from (9) patch by uniqueness along [0,1]. Compactness and the strict cap
and wall margins keep the events away from the time and spatial
boundaries. Consequently the whole real event branch required by (11)
exists; this is no longer a separate continuation assumption.

Write H_s=U_s P_s in the disk. On its outer boundary,
|P_s|<= (R+r)^2, so |U_s|>=delta/(R+r)^2. The function U_s is nonzero
throughout the disk; applying the maximum modulus principle to 1/U_s
propagates this lower bound into the entire disk. At its double event,
P_s=(z-b_s)^2 and H_{s,zz}=2U_s. Therefore

\[
 \boxed{|H_{s,zz}(\tau_s,b_s)|\ge
             \nu:=\frac{2\delta}{(R+r)^2}>0.}                 \tag{11b}
\]

This payment introduces no internal gap denominator. It retains the
external wall floor and collar scales, which may deteriorate with height.

For clarity, sufficient common geometric data can themselves be stated
at the reference walls. Suppose F has exactly two roots inside each nested
disk throughout the time rectangle, with wall floors delta_{F,r} and
delta_{F,R}. If Q_v=sup_{time,|z-a|=v}|E/F|<1 for v=r,R,
Rouche gives the same two counts for all H_s, and
|H_s|>=delta_v:=(1-Q_v)delta_{F,v}>0 on each wall. Taking delta=delta_R
and any complete bound |F_z|+|E_z|<=L on the outer wall, the common phase
condition is paid by

\[
 \frac{4RL}{\delta(R-r)^2}\,\tau<\pi/2,                       \tag{11c}
\]

where tau is the rectangle's imaginary half-width. A sharper common
coefficient estimate can replace this sufficient one. The cap q in
(11a) may be taken as Q_R. Neither the reference cap signs nor the
signed initial event displacement in (11) follows from these norm
conditions alone.

If F and E have complete source densities Phi_0 and psi, respectively,
the remaining bounds in (11) can be paid on the real event branch by

\[
 E_j=\int_0^\infty |\psi(u)|u^j e^{t_+u^2}du\quad(j=0,2),
 \qquad
 C_4=\int_0^\infty (|\Phi_0(u)|+|\psi(u)|)u^4 e^{t_+u^2}du.
 \tag{11d}
\]

Real event positions allow |cos(b_s u)|<=1 here. Every source tail must
be retained. Equations (11a)-(11d), together with the signed initial
velocity in (9), now make (11) a complete conditional location consumer.
A negative right side of (11) excludes an endpoint event in this window;
no unchanged-theta data satisfying that final strict inequality have
been supplied.

An exact countercheck uses F=z^2-2t, r=1, R=2,
|Re t|,|Im t|<=1/4, and E=z/16+c with c=+1/32 or -1/32.
Here A_s=0 exactly. Since 2|t|<3/4, the inner and outer reference
relative-error ratios are below 3/8 and 5/104, respectively, so both
counts persist. The common outer floor exceeds 99/32, giving the
permitted choice nu=11/16 in (11b), below the exact curvature 2.
The reference cap discriminants are -2,+2; using
l_1(5/104)<=5/99 gives
C_cap<=120/99+100/9801<2. Hence the entire branch is paid.
Its exact time is tau_s=sc/2-s^2/2048. For c=-1/32, (11) has
P=E_zz=0 and therefore B_+=0, yielding tau_1<=-1/64<0, in agreement
with the exact event. For c=+1/32 the event is positive; the same wall,
phase and cap-persistence mechanism does not give the negative-time
conclusion in that case. The distinction comes from the signed source
response, as required.

## 4. Exact controls for signs and nonlinear centroid motion

For H=z^2-2t+c, Delta=8t-4c and A=0. At t=0 compare F=z^2 with
E=c, on any circle R with |c|<R^2. Formula (8) gives L=-4c, and (3)
gives the exact response -4c. Consequently c=0 remains an event with
charge one in a straddling window; c=-1 and c=+1 give the positive and
negative noncrossing controls on the usual suitably enlarged disks.
The response consumer does not erase the collision.

A control that detects the centroid-square term is

\[
 H_s(t,z)=z^2-2t+s(bz+c),\qquad
 \Delta_s(t)=8t+s^2b^2-4sc.
\]

The exact first variation at s=0 is -4c, but the finite correction is
s^2b^2. Dropping the last square in (3) incorrectly doubles that
correction: the logarithmic integral alone contributes 2s^2b^2.
Its exact event is tau_s=sc/2-s^2b^2/8 and event position -sb/2.
Equations (9)-(10) give tau'_0=c/2 and tau''_s=-b^2/4, agreeing exactly.
These are algebraic controls, not numerical certification claims.

## 5. Fixed finite envelope moments do not fix local event direction

The claim concerns only moments of the form

\[
 m_j(\Phi)=\int_0^\infty\Phi(u)k_j(u)\,du,\qquad
 k_j(u)=u^{n_j}e^{T_j u^2}\cosh(Y_j u),                       \tag{12}
\]

where a finite list is fixed, n_j are nonnegative integers, T_j are
real and Y_j>=0. Normalization can be included by k=1 or k=cosh u.
These are the complete envelope moments used in absolute heat/source
bounds. The result is not asserted for arbitrary finite measurements:
one could explicitly include the event's cosine measurement in a list.

Take the reflected super-Gaussian control, translated in heat time so
its event is at zero. A self-contained convenient normalization is

\[
 \Phi_0(u)=c_0\{e^{-u^4}+\tfrac12e^{-(u-4)^4}
                            +\tfrac12e^{-(u+4)^4}\},\quad c_0>0.
\]

Its zero-time transform is H_0(0,z)=c_0 F(z)(1+cos4z), where
F(z)=integral_0^infinity e^{-u^4}cos(zu)du. At b=pi/4,
H_0=H_{0,z}=0 and H_{0,zz}=16c_0F(b)>0. For completeness,
M_4=M_0/4 by integration by parts, M_2<=M_0/2 by Cauchy-Schwarz,
and cos x>=1-x^2/2 give F(b)>=M_0(1-b^2/4)>0.
This is the exact control from [the reflected-source note][reflected],
with its heat-time shift made explicit.

**Proposition.** For every finite list (12), there is a real smooth
compactly supported perturbation psi on the positive half-line, with
smooth even extension, such that for all sufficiently small real s:

1. Phi_s=Phi_0+s psi remains strictly positive, smooth and even, with
   exactly the same source outside a fixed compact interval and near u=0;
2. every selected m_j(Phi_s) equals m_j(Phi_0) exactly;
3. its ordinary real event branch has tau_0=0 and tau'_0>0. Hence events
   occur at negative and positive times for sufficiently small negative
   and positive s respectively.

**Proof.** Choose any bounded open interval I contained in (0,infinity)
and a nonnegative smooth bump chi supported compactly in I and positive
on a subinterval. Let f(u)=cos(bu) and V=span{k_j}. In the weighted real
inner product integral chi fg, let p be the orthogonal projection of f
onto V (discard dependent k_j if necessary). Set psi=chi(f-p).
Then integral psi k_j=0, while

\[
 \int_0^\infty\psi(u)\cos(bu)du
 =\int_0^\infty\chi(u)(f(u)-p(u))^2du>0.                    \tag{13}
\]

The strict inequality holds because cos(bu) is not in this finite span
on any interval. To verify that assertion, equality on an interval
would extend analytically to all real u. Write the purported sum as a
finite sum of polynomial multiples of exp(Tu^2+Yu), using cosh's two
exponentials and grouping identical real (T,Y) pairs. Comparing the
largest quadratic growth and then the largest real linear growth as
u tends to positive infinity eliminates all growing terms. At the
remaining (T,Y)=(0,0), a polynomial cannot equal the bounded oscillating
cos(bu); after its constant part is removed the remaining terms decay,
whereas cos(bu) has no limit. A leading negative quadratic group would
already decay. This proves nonmembership, including lists containing
negative heat weights or repeated kernels.

The base source has a positive minimum on supp psi, so both signs of
s preserve positivity when |s| is small. Extension evenly across zero
is smooth because the support is away from zero. All moments (12)
remain exact. The source changes are compact, so the transformed heat
family remains jointly entire. Formula (9) and (13), divided by the
positive H_{0,zz}, give tau'_0>0. The local implicit theorem supplies
the event branch and its sign for small s. This proves the proposition.

Choose a sufficiently small proper two-root complex window around the
base event. Its strict wall margins, counts and phase condition persist
for sufficiently small |s| by uniform compact convergence; the event
stays in its interior. Thus both event directions coexist with the
same chosen finite envelope moments and the same strict local analytic
window requirements. This is a limitation of those retained data.

**Scope.** The constructed moment vector belongs to Phi_0, not theta.
Compact smooth perturbations need not preserve analyticity of the source
as a function of u, stronger shape conditions, or the earlier control's
full primitive identities. No global all-real heat slice, all-positive-
time real-rootedness, theta coefficient expansion, ordinary Dirichlet
series, or complete normalized arithmetic reflection conjunction is
claimed. Exact theta data, a measured oscillatory kernel (7), and
arguments using additional RH consequences remain outside this result.

## 6. Other controls and disposition

The general response and event formulas also hold near ordinary doubles
of the Euler-factor, weighted-square, finite-prime, reflected and
positive-primitive controls when their local two-root hypotheses are
paid. They return the actual event response; they contain no universal
positive theta sign. Euler-factor controls change Euler data;
weighted-square and finite-prime controls fail the unchanged full
coefficient/reflection conjunction; reflected and positive-primitive
controls lack the canonical theta square expansion. Controls without
an all-real heat slice test these local formulas only.

The close normalized endpoint sources in [BW10 Note 05][close] preserve
positive-time simple all-real zeros under RH and defeat a fixed positive
source-norm tolerance; their failed premise is ordinary Dirichlet-series
arithmetic. They are not asserted to preserve the exact finite moment
vector in Section 5. Conversely, the compact perturbations in Section 5
are not assigned that control's all-real or normalization preservation
list. These screens must not be merged.

ECE-02 now has a precise coupled source observable, the signed enclosure
(6), and event displacement formulas (9)-(11). Its unchanged-theta sign
is still open. The finite-moment obstruction closes only a universal
local inference from the selected exact envelope moments and strict
analytic-window data. The parameterized hypothetical-double geometry is paid in [Note 07][n07];
a numerical certificate at an unknown event and the distinguishing source
sign are not supplied. ECE-03 remains gated. No
numerical run, height-coverage conclusion, or all-multiplicity claim is
made in this note.

[program]: ../research-overview/02_ENDPOINT_CHARGE_EXCLUSION_PROGRAM_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[close]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[reflected]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/04_REFLECTION_POSITIVE_SOURCE_COLLISION_AND_MIXED_SECTORS_20261015.md

[review]: ../reviews/08_ENDPOINT_CHARGE_OPENING_ROUND_REVIEW_20261021.md
[n07]: 07_QUANTITATIVE_ENDPOINT_WINDOWS_AND_HEIGHT_COVERAGE_20261021.md

## Appendix A. The canonical theta tail in the signed response kernel

21 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), effort ultra**, supplied from root turn metadata.
This appendix applies [BW14 Note 04][tail04]'s actual-tail theorem; it
retains [BW14 Note 05][tail05]'s distinction between unshifted and
connector-corrected references. No numerical sign is asserted.

Fix a real cap t and the **unshifted** complete half-line head and tail
\[
 F=H_{S_m},\quad S_m=\sum_{n=1}^m\phi_n,\qquad
 E=H_{R_m},\quad R_m=\sum_{n>m}\phi_n,\qquad H=F+E.
 \tag{A1}
\]
Assume F has Section 1's proper two-root reference geometry and proved
wall floor delta>0. Set alpha=lambda_m, beta=lambda_(m+1), d=beta-alpha,
h(u)=exp(4u)-1, and
\[
 A=\frac{\beta^2}{\alpha^2}e^{-d},\quad
 E_m=R_m(0)/\phi_m(0)>A,\quad
 W(u)=e^{tu^2}\phi_m(u)e^{-dh(u)}.
 \tag{A2}
\]
The canonical positive measure constructed in BW14 Note 04 gives exactly
\[
 e^{tu^2}R_m(u)=W(u)\{A+(E_m-A)z_m(u)\},
 \quad z_m(0)=1,\quad z_m(\infty)=0,\quad z_m'\le0.
 \tag{A3}
\]
Write d sigma_m(v)=-z_m'(v)dv, a probability measure with
z_m(u)=sigma_m([u,infinity)). For Section 2's real kernel K_F define
\[
 J_K=\int_0^\infty WK_F\,du,\qquad
 C_K(v)=\int_0^v WK_F\,du,\qquad C_K(\infty)=J_K.
\]
The bound |K_F(u)|<=4R(R+r)cosh(Ru)/delta and complete source decay
justify Fubini. Thus the **actual** signed response satisfies
\[
 \boxed{L_F(E)=A J_K+(E_m-A)\int C_K(v)\,d\sigma_m(v),}
 \tag{A4}
\]
\[
 A J_K+(E_m-A)\min C_K\le L_F(E)
       \le A J_K+(E_m-A)\max C_K.
 \tag{A5}
\]
The extrema range over the compactified half-line. All modes and source
rays are retained. A complete sufficient wall-ratio payment is
\[
 \bar\rho=\frac{E_m}{\delta}\int_0^\infty W(u)\cosh(Ru)du<1.
\]
It gives sup_Gamma|E/F|<=bar-rho. With B the nonlinear error in (5),
\[
 \boxed{\begin{split}
 \Delta_H&\ge\Delta_F+A J_K+(E_m-A)\min C_K-B(\bar\rho),\\
 \Delta_H&\le\Delta_F+A J_K+(E_m-A)\max C_K+B(\bar\rho).
 \end{split}}
 \tag{A6}
\]
A sharper paid wall ratio may replace bar-rho. An implementation must
add acquisition and full-domain interpolation errors. No positivity
of the complete lower bound in (A6) is proved here.

**Strict matched improvement.** Suppose both reference roots lie in
Re z>0. With F=UP, residues give, for distinct roots,
\[
 K_F(u)=-2\left\{\frac{\cos(z_1u)}{U(z_1)}
                      +\frac{\cos(z_2u)}{U(z_2)}\right\}.
 \tag{A7}
\]
At a double b>0 the continuous value is -4cos(bu)/U(b).
This kernel has both signs on intervals arbitrarily far along u>0.
For distinct positive real roots it is a nonzero positive-frequency
cosine sum: its primitive is bounded and its mean square is positive.
Eventual nonnegativity would bound its square integral by its sup norm
times its bounded integral, a contradiction; eventual nonpositivity is
excluded similarly. For a conjugate pair b+/-iy, b,y>0, writing
1/U(b+iy)=c+ie gives the kernel
-4[c cos(bu)cosh(yu)+e sin(bu)sinh(yu)]. After division by exp(yu),
this is a nonzero sinusoid plus a decaying correction, proving the same
claim. The right-half-plane hypothesis matters: an imaginary-axis
reference can have a kernel of one sign.

Put f=WK_F, P_+=integral f_+ and P_-=integral f_-, with f_- positive.
The sharp pointwise relaxation using the **same** floor and ceiling
A W<=exp(tu^2)R_m<=E_m W has response interval
\[
 [A J_K-(E_m-A)P_-,\ A J_K+(E_m-A)P_+].
\]
Choose a negative interval I_- followed by a positive interval I_+.
Then d_+=min(integral_(I_-)f_-,integral_(I_+)f_+)>0 and, for every v,
P_+-C_K(v)=integral_v^infinity f_++integral_0^v f_->=d_+:
either the positive interval is wholly omitted or the negative one
wholly included. A positive interval followed by a negative one supplies
d_->0 similarly. Therefore
\[
 \boxed{\min C_K\ge-P_-+d_-,\qquad
        \max C_K\le P_+-d_+.}
 \tag{A8}
\]
These positive gains are complete integrals over chosen sign intervals.
Using the **identical** bar-rho and B(bar-rho) preserves both strict
endpoint improvements in the discriminant interval (A6). The interval
can still straddle zero. This comparison drops only multiplier
monotonicity on the pointwise side; it asserts no uniform useful gain
with height, optimality in the smaller canonical Laplace class, or
superiority over other arithmetic evaluators.

**Conditional applicability near a putative double.** For a>0, add
R<=a/2 to Note 07's radius choice and recompute r,h from that formula;
its proof and all margins persist.
The complete tails tend uniformly to zero on both nested walls of that
fixed compact window. For a sufficiently large cutoff m they are less
than half the corresponding H-wall floors. Rouche then makes F proper
on both disks, puts its roots in Re z>0, gives a common reference wall
floor delta at least half the corresponding H-wall floor, and gives
|E/F|<=|E|/(|H|-|E|)<1. The explicit envelope ratio bar-rho also tends
to zero: BW14 Note 04 gives E_m/A bounded (indeed tending to one),
while A W<=exp(tu^2)R_m, so its integral majorant is bounded by a
constant times the vanishing complete tail majorant. This proves
applicability of the estimator conditional on each hypothetical double;
it supplies no common cutoff across heights and no signed contradiction.

**Connector and control scope.** The reference (A1) is load-bearing.
BW14 Note 05's shifted or connector-corrected head changes the residual;
substitution in (A4) without restoring the connector and shifted rays
would be wrong. This appendix keeps the full original head and tail,
without resolving their modular cancellation.

Finite-prime controls can preserve the canonical prefix through m+1
and the source value at zero. They then share F,W,A,E_m and a monotone
tail law, so at a *fixed admissible reference window* the same bounds
apply. Their actual measures and responses need not equal theta's.
Their high-gap collisions do not imply that this prescribed reference
is proper or has wall ratio below one at those events, or that an event
lies in the selected window. They fail unchanged complete coefficients
and full normalized reflection; these failures are not needed for the
monotone comparison. Other source controls are not assigned (A3).

The gain is the actual-source signed enclosure (A6), its strict matched
comparison (A8), and conditional local applicability. A positive theta
margin and ECE-03 remain unproved; ECE-02 receives an analytical
estimator, not an exclusion theorem.

[tail04]: ../../14_theta_source_transform_constraints/notes/04_CANONICAL_TAIL_LAPLACE_CONSTRAINT_AND_COUPLED_ENCLOSURE_20261021.md
[tail05]: ../../14_theta_source_transform_constraints/notes/05_FINITE_REFLECTION_JETS_AND_HEAD_TAIL_STABILITY_20261021.md
