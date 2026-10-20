# Direct physical winding: paired time faces and wall transport

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
actual reasoning effort **max**, verified from the recorded turn metadata.

**Status: initial investigation, elementary deductions and exact finite
controls; author self-checks only.** No new theta values were acquired,
no previously uncovered theta region was certified, and no opposing
arithmetic estimate was obtained.

The useful outcome is a precise description of the additional boundary
data, together with two tests that prevent an incomplete certificate:

- Relative phase between the two time faces determines the physical
  winding only after the integer phase transport on both spatial walls
  is retained.
- There are exact heat polynomials with a uniformly positive paired-face
  dot product but physical winding **−2**. One example has two ordinary
  double events, so this issue is not confined to higher multiplicity.
- Near any ordinary double event, sufficiently accurate local Taylor data
  actually **force** the unfavorable relative-phase crossing. The explicit
  bounds below sharpen the description of this obstruction in the new
  observable; they do not overcome the earlier remainder obstruction.

This continues [brainstorm 03, §5][brainstorm]. It follows the
[result index][results], [control cluster][controls], [topology
cluster][topology], and [avoid index][avoid], especially [target
classification][a01], [control premises][a02], [scope][a07], and
[signed recombination][a12]. The all-domain noncollision target remains
RH-strength. The deliverable here is a bounded information audit, not a
new global criterion offered as progress toward RH.

## 1. The physical object and the bounded question

Let the unchanged real heat flow satisfy \(H_t=-H_{xx}\), and write
\[
 J(t,x)=H(t,x)+iH_x(t,x),\qquad
 D=[t_-,t_+]\times[a,b].
\]
Orient the boundary by \(dt\wedge dx\): left spatial wall upwards in
time, final time face to the right, right wall downwards, initial time
face to the left. Under the analytic and isolation hypotheses of the
[physical index theorem][index], a nonzero whole boundary gives
\[
 W_D=\operatorname{wind}_{\partial D}J
     =-\sum_{(t,x)\in\operatorname{int}D:\,J=0}
          \left\lfloor\frac{m(t,x)}2\right\rfloor .
 \tag{1}
\]
Every event contributes negatively. Thus a certified \(W_D>-1\), or
equivalently the integer value zero, excludes all interior multiplicities.
Boundary nonvanishing then gives noncollision on the closed rectangle.
This is an imported theorem, not a new result of this note.

The bounded question is whether *paired* time-face information can
replace two separately resolved phase traces, while retaining the wall
data needed for (1). This could cancel large common spatial rotation.
Before acquiring more theta data, this note derives the required
identity, tests the omitted-wall shortcut, and checks the proposed
interface against local event data and the existing theta certificate.

## 2. An exact relative-phase decomposition

Put \(J_\pm(x)=J(t_\pm,x)\), and form
\[
 R(x)=J_+(x)\overline{J_-(x)}=C(x)+iS(x),
 \tag{2}
\]
where
\[
 \begin{split}
 C&=H_+H_-+H_{x,+}H_{x,-},\\
 S&=H_-H_{x,+}-H_+H_{x,-}.
 \end{split}
 \tag{3}
\]
The letter \(S\) in this note denotes this paired determinant, not the
deflated reciprocal-square sum \(S_2\). Negative real values of \(R\)
mean that the two physical jets are antiparallel.

Assume the whole physical boundary is nonzero and \(R(a),R(b)\) are
off the closed negative real axis. Choose a continuous argument
\(\phi(x)\) of \(R\) along the spatial interval. Let
\(r_c=\operatorname{Arg}R(c)\in(-\pi,\pi)\) at \(c=a,b\).
Let \(\delta_c\) be the continuous argument change of \(J(t,c)\)
from \(t_-\) to \(t_+\), retaining all turns. Define integers
\[
 n_R=\frac{\phi(b)-\phi(a)-r_b+r_a}{2\pi},\qquad
 k_c=\frac{\delta_c-r_c}{2\pi}.
 \tag{4}
\]
Then
\[
 \boxed{W_D=n_R+k_a-k_b.}
 \tag{5}
\]

**Proof.** Continuous arguments \(\theta_\pm(x)\) of the nonzero time
faces give an argument \(\phi=\theta_+-\theta_-\) of \(R\). The four
oriented phase changes sum to
\[
 2\pi W_D=\delta_a+\Delta\theta_+-\delta_b-\Delta\theta_-
          =\delta_a-\delta_b+\Delta\phi.
\]
Substitute (4). The endpoint conditions ensure the principal arguments
are unambiguous. If an endpoint is antipodal, this particular branch
interface is inconclusive; the original whole-boundary winding is still
defined when \(J\ne0\).

For transverse crossings of the negative real axis by \(R\),
\[
 n_R=-\sum_{\substack{a<x<b\\ S(x)=0,\ C(x)<0}}
                      \operatorname{sgn}S'(x).
 \tag{6}
\]
An upward imaginary crossing at a negative real value is clockwise
relative to the principal branch. At a nontransverse isolated crossing,
replace the derivative sign by the one-dimensional local degree
\((\operatorname{sgn}S_{\rm after}-\operatorname{sgn}S_{\rm before})/2\).
Even tangencies contribute zero. An interval lying on the cut requires
another argument calculation; it is not silently discarded.

A convenient way to determine \(k_c\) is to close the wall trace by the
reverse straight chord between its endpoint jets. The chord avoids zero
when those endpoints are not antiparallel. Its argument change is \(r_c\),
so the resulting closed loop has degree \(k_c\). This observation allows
exact ray-crossing checks without floating argument unwrapping.

## 3. A sufficient boundary contract, including its missing premise

The following two conditions suffice:

1. On every point of the paired time faces,
   \[
      R(x)\notin(-\infty,0]\quad (a\le x\le b).
      \tag{7}
   \]
2. Each complete spatial wall trace lies in a fixed open half-plane
   whose boundary passes through the origin. The two walls may use
   different half-planes.

Condition (7) makes both time faces nonzero and gives \(n_R=0\).
Condition 2 makes each wall nonzero and confines its argument to an
interval of width \(\pi\). Consequently \(|\delta_c|<\pi\) and \(k_c=0\).
Equation (5) yields \(W_D=0\), and (1) supplies the exclusion.

The easiest version of (7) is \(C>0\), but it is stronger than necessary:
regions where \(C\le0\) are allowed if \(S\ne0\) there. More generally,
one could certify \(n_R+k_a-k_b\ge0\); the physical sign law then forces
equality. This is a one-sided winding target, not a requirement to
resolve every boundary zero of \(H\).

Condition 2 can be replaced by paid wall integers or bounds on their
difference. It cannot simply be omitted. Nor may one substitute the
principal endpoint angle for the actual wall phase change.

The [existing wall-flux identity][flux] offers another way to acquire the
same missing information:
\[
 W_D=\frac{N_- -N_+ -Q_a+Q_b}{2}.
 \tag{8}
\]
Here \(Q_a,Q_b\) count signed root transport, including tangencies.
The integers \(k_a,k_b\) in (5) are relative phase transports, not these
\(Q\)'s; neither is the fourth-order polynomial \(Q_L\).

## 4. Exact counterexamples to using only the paired faces

Consider the two complete heat polynomials
\[
 F_c(t,x)=x^4-12tx^2+12t^2+c,\qquad c=0\ \hbox{or}\ -3,
 \tag{9}
\]
on \(D=[-1,1]\times[-1/4,1/4]\). Both satisfy
\(F_t=-F_{xx}\) exactly. A translation of time puts the entire
example in positive physical times if desired.

Write \(A=12+c\). Their paired products on \(t_\pm=\pm1\) are
\[
 \begin{split}
 C_c(x)&=x^8+16x^6+(2A-144)x^4-576x^2+A^2,\\
 S_c(x)&=48x^5-48Ax.
 \end{split}
 \tag{10}
\]
Since \(x^8,16x^6\ge0\), on the **whole interval** \(|x|\le1/4\),
\[
 \begin{array}{ll}
 c=0:& C_0(x)\ge144-576/16-120/256
                       =3441/32>107,\\[2mm]
 c=-3:& C_{-3}(x)\ge81-576/16-126/256
                       =5697/128>44.
 \end{array}
 \tag{11}
\]
Thus both examples satisfy the strict paired-face condition with a large
margin, and \(n_R=0\).

Nevertheless their physical winding is \(-2\). For \(c=0\) the origin
is a fourth-order event. For \(c=-3\), the only simultaneous zeros are
\[
 (t,x)=(-1/2,0),\ (1/2,0),
 \tag{12}
\]
both ordinary doubles, because \(F_{xx}=-24t\ne0\) there.
To check exhaustiveness, \(F_x=4x(x^2-6t)\). On \(x=0\),
solve \(12t^2+c=0\); on \(x^2=6t\), the value is \(-24t^2+c\).
For \(c=-3\) the latter cannot vanish, and for \(c=0\) it adds no
event beyond the origin. Neither example has a boundary jet zero.
For \(F_{-3}\), the squared zeros are
\(6t\pm\sqrt{24t^2+3}\); both are nonnegative exactly when \(t\ge1/2\).
It therefore has an actual all-real threshold at \(t=1/2\).
An actual threshold does not repair the omitted-wall inference either.

One can see the missing turns directly. On either wall \(x=\pm1/4\),
the imaginary coordinate has its sole zero at \(t=x^2/6\), where
\[
 F_c(t,x)=c-\frac23x^4<0.
 \tag{13}
\]
As time increases, \(F_x\) crosses upward on the left wall and downward
on the right. Both endpoint real coordinates are positive, so their
short endpoint chords do not cross the negative axis. Hence
\[
 k_a=-1,\qquad k_b=1,\qquad
 W_D=0-1-1=-2.
 \tag{14}
\]
This is also checked independently by (8); both time-face root counts
are zero, and \(Q_a=2,Q_b=-2\).

The scope is precise: **paired-face positivity, even with exact heat
evolution and nonzero whole boundary, does not exclude collisions
without the wall transport.** This does not refute the full contract
in §3. In these examples its wall half-plane premise fails.

## 5. What an ordinary local event forces in the paired observable

At an ordinary double event \((T,a)\), let \(h_2=H_{xx}(T,a)\ne0\).
Use \(t=T+r^2\tau,\ x=a+ry\), and the constant target scaling
\[
 \widetilde J=
       \frac{H}{h_2r^2}
        +i\,\frac{H_x}{h_2r}.
 \tag{15}
\]
The associated real linear map has determinant
\(1/(h_2^2r^3)>0\). It preserves physical degree and antiparallelism;
no rotating-frame winding has been dropped.

The leading jets on \(\tau=\pm1\) are
\[
 p_+(y)=y^2/2-1+iy,\qquad p_-(y)=y^2/2+1+iy,
\]
and their relative product is
\[
 p_+\overline{p_-}
      =y^4/4+y^2-1+2iy.
 \tag{16}
\]
Suppose complete component errors on these faces satisfy
\[
 |\operatorname{Re}(\widetilde J_\pm-p_\pm)|\le1/8,\qquad
 |\operatorname{Im}(\widetilde J_\pm-p_\pm)|\le1/8.
 \tag{17}
\]
For \(|y|\le1/2\), use
\[
 |p_+|\le9/8,\quad |p_-|\le5/4,\quad \sqrt2<3/2.
 \]
The exact bilinear error estimate then gives
\[
 \left|\widetilde J_+\overline{\widetilde J_-}
                    -p_+\overline{p_-}\right|
 \le\frac{57}{16}\frac18+2\left(\frac18\right)^2
 =\frac{61}{128}.
 \tag{18}
\]
Consequently,
\[
 \operatorname{Re}(\widetilde J_+\overline{\widetilde J_-})
       \le-\frac{33}{128}\quad(|y|\le1/2),
 \tag{19}
\]
while its imaginary part is at most \(-67/128\) at \(y=-1/2\)
and at least \(67/128\) at \(y=1/2\). The intermediate value theorem
forces an antipodal crossing between them, with net clockwise local
contribution \(-1\).

Thus sufficiently accurate symmetric local data do not just leave the
slit condition unproved: they contradict it. For an actual analytic
ordinary event, the normalized remainder tends to zero with \(r\).
The [paid BW-01 remainder calculation][local-remainder] supplies the
relevant form of control; a uniform theta radius or a uniform curvature
floor has not been obtained here.

This is a quantitative restatement of the inherited local obstruction
in the paired-phase coordinates. Shrinking the event box and improving
absolute Taylor accuracy cannot produce the desired opposite winding.
A theta contradiction would need independently derived source
information incompatible with the event and hence with this crossing.

## 6. The arithmetic data that this interface would actually consume

Suppose \(P_\pm\) approximate the physical complex jets on a whole
spatial segment, with complete errors \(|J_\pm-P_\pm|\le e_\pm\).
Then for \(R_P=P_+\overline{P_-}\),
\[
 |R-R_P|\le |P_+|e_-+|P_-|e_++e_+e_-=:E_R.
 \tag{20}
\]
Uniform upper bounds are used on the right. A sufficient segment test is
\[
 \operatorname{Re}R_P>E_R
 \quad\hbox{or}\quad
 \operatorname{Im}R_P>E_R
 \quad\hbox{or}\quad
 \operatorname{Im}R_P<-E_R,
 \tag{21}
\]
where every inequality holds on the entire segment. Certified segments
must cover the complete closed interval, with the same endpoints used
by the wall certificates. Touching zero or the cut is inconclusive.
Component errors must be errors for the physical \(H,H_x\); differentiating
an undifferentiated error bound is not a substitute.

Equation (20) is a safe default, not an established improvement. A possible
gain would come from estimating the paired quantity *before* discarding
common source correlations. With
\[
 M=(J_++J_-)/2,\qquad N=(J_+-J_-)/2,
\]
one has the exact identity
\[
 R=|M|^2-|N|^2+2i\,\operatorname{Im}(N\overline M).
 \tag{22}
\]
Separate norm bounds that only prove \(|N|<|M|\) can still be too weak.
The sign of the imaginary part on the set where the real part is
nonpositive is additional information worth retaining.

For clarity, write a complete cosine heat representation as
\[
 H(t,x)=\int_0^\infty\Phi(u)e^{tu^2}\cos(ux)\,du,
 \quad t_\pm=T\pm h,\quad w(u)=\Phi(u)e^{Tu^2}.
\]
Assuming the convergence needed to differentiate and interchange these
integrals, the *complete* paired kernels are
\[
 \begin{split}
 C(x)&=\iint w(u)w(v)\cosh(h(u^2-v^2))\\
 &\qquad\cdot[\cos(ux)\cos(vx)+uv\sin(ux)\sin(vx)]\,du\,dv,\\
 S(x)&=\iint w(u)w(v)\sinh(h(u^2-v^2))\\
 &\qquad\cdot[v\cos(ux)\sin(vx)-u\sin(ux)\cos(vx)]\,du\,dv.
 \end{split}
 \tag{23}
\]
These follow by symmetrizing \(J_+\overline{J_-}\), with
\(J(t,x)=\int\Phi(u)e^{tu^2}[\cos(ux)-iu\sin(ux)]\,du\).
They specify an actual two-time observable. Source positivity does not
give either required sign: the trigonometric factors remain signed.
No sign estimate for (23) is asserted. Any truncation would have to pay
the mixed retained/tail terms and the tail/tail term as well.

The three imaginary-axis profile observations do not determine (23),
a physical wall trace, or the required integer transports. Their relaxed
positive-measure witness therefore is not a witness against *every*
possible boundary-phase argument. Conversely, requesting this additional
data does not establish that theta supplies the favorable data.
The earlier fractional-residue diagnostic and its limitations remain
as stated in [brainstorm 03][brainstorm].

## 7. Existing theta data, controls, and the next useful question

The [GEO-T1 certificate][geo] already treats
\[
 [1/100,1/5]\times[999,1001].
 \tag{24}
\]
Its retained complete boundary intervals prove \(H_x>0\) on both time
faces, \(H<0\) on the left wall, and \(H_x>0\) on the right wall.
Two vectors in the same open upper half-plane cannot be antiparallel,
so these existing intervals imply (7). The wall signs give \(k_a=k_b=0\).
The paired contract therefore recovers its established \(W_D=0\).

This is a logical reuse of the existing receipt, not new theta
quadrature. The [checker][checker] verifies the exact recorded partition,
signs, positive margins and receipt hash. That does not independently
recertify the source integration. Its original optimized interior
baseline already passed in seven complete calls, versus ten for winding;
its declared cost-gain gate failed. Repackaging that box earns neither
new coverage nor a performance claim.

The exact new finite checks use each polynomial's own data:

| Control | \(n_R\) | \((k_a,k_b)\) | Physical \(W_D\) |
| --- | ---: | --- | ---: |
| \(H=1\), \(H=x\) | 0 | \((0,0)\) | 0 |
| \(x^2-2t\) on \([-1,1]^2\) | −1 | \((0,0)\) | −1 |
| \(x^3-6tx\) on \([-1,1]^2\) | −1 | \((0,0)\) | −1 |
| \(F_0\) on the narrow rectangle | 0 | \((-1,1)\) | −2 |
| \(F_{-3}\) on the narrow rectangle | 0 | \((-1,1)\) | −2 |

The same outcomes hold after multiplying each field by −1. Rational
Sturm isolation computes the full boundary winding and independently
checks the root-flux formula. A boundary collision is rejected, and
uncertainty reaching the excluded cut is not certified. The
[small record][record] retains the polynomial coefficients, margins,
source identities and scope. Sixteen exact positive finite-atom
calculations also check the factors and signs in (23), using rational
heat weights and trigonometric values. These checks support conventions and the
finite examples; they do not prove a theta estimate.

For the nonpolynomial families in [control cluster 12][controls], the
screen is analytic rather than a new numerical acquisition:

- At their stated ordinary double events, the positive weighted-square,
  reflected, smooth positive-primitive, finite-prime-compatible, atomic
  threshold, and continuous finite-profile controls satisfy the local
  analytic argument of §5. On sufficiently small normalized event
  rectangles, their own jets force the unfavorable crossing. Positivity,
  the heat equation, or a genuine threshold cannot imply (7).
- The finite weighted-square and finite-prime controls also fail full
  normalized theta source reflection; the reflected and smooth primitive
  controls lack theta's complete normalized square expansion. The atomic
  and continuous profile controls are changed sources and do not match
  the complete theta source or full imaginary-axis profile. These
  distinctions explain why a future complete-theta estimate need not
  apply to them; they are not measurements of its sign.
- The Euler negative-Laguerre witness alone is not a simultaneous
  physical-jet zero. It need not fail a valid local noncollision
  certificate. Euler modifications alter the source coefficients.
  No new Euler paired-phase or wall enclosure is claimed here.

The most useful next step is consequently **a source estimate for the
coupled pair (3), together with paid wall transport**, on a declared
domain where it could add information to the strongest same-source
interior test. The target may be absence of antipodal crossings, or
the weaker signed integer bound in (5). A fixed half-plane on each
wall is a convenient sufficient condition, not an assumed property
of the domain.

Before a numerical campaign, identify why this paired estimate could
be stronger: a common analytic residual, cancellation in (23), or a
proved bound on wall transport. Merely applying (20) to the same
independent disks supplies no demonstrated advantage. If only the
local event Taylor data or the already-covered box (24) are available,
the present study identifies the stopping point. The original direct
physical winding program remains open.

[brainstorm]: ../brainstorm/03_TOPOLOGICAL_BOUNDARY_DATA_AND_PROFILE_WITNESSES_20261020.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[topology]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[index]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[flux]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[local-remainder]: ../threshold_routes/01_local_double_winding/notes/03_PAIRED_FACE_REMAINDER_OBSTRUCTION_20261019.md
[geo]: ../../../11_arithmetic_collision_rigidity/symmetries/notes/06_GEO_T1_WINDING_AND_DIRECT_COMPARISON_20261019.md
[checker]: ../numerics/check_direct_winding_relative_phase.py
[record]: ../numerics/DIRECT_WINDING_RELATIVE_PHASE_20261020.json
