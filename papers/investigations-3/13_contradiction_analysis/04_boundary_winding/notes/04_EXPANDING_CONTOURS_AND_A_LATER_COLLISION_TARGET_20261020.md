# Expanding contours and a later-collision target

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**,
actual reasoning effort **max**, verified from this chat's metadata.

**Status: discussion follow-up, conditional deductions and an exact
analytic control; author self-checks only.** No theta boundary estimate,
new excluded region, or later collision has been established.

Edward Baker proposed an expanding “light cone” from a hypothetical
collision at \(T=\Lambda>0\), closed by a distant cap. His subsequent
correction gives the appropriate target: obtain a **more negative**
boundary winding than the initial event alone contributes. The idea
fits the project's later-witness route, provided the apex, wall flux,
and cap are all retained.

This follows [Note 03][paired] and the [later-witness discussion][later].
The [result index][results], [index theorem][index], [control
cluster][controls], and [avoid index][avoid] apply, particularly
[target classification][a01], [scoped conclusions][a07], and
[signed recombination][a12]. The criterion below is a reformulation of
the desired later witness; the explicit control and apex regularization
clarify what a useful new arithmetic estimate must do.

The idea is now organized as [route BW-09](../threshold_routes/09_expanding_contour_later_collision/README.md),
with a research overview and separate progress register. This note
remains the originating analysis; the program handoff adds no new
theta estimate.

## 1. The corrected inequality

Let \(p=(T,a)\) be an isolated spatial zero of multiplicity \(m_0\ge2\),
and set \(q_0=\lfloor m_0/2\rfloor\). Use a bounded domain \(\Omega_R\)
with nonzero physical jet \(J=H+iH_x\) on its complete boundary.
Require that \(p\) is interior and is its **only collision at times
\(t\le T\)**. The portion at those times can be confined to a small
isolating neighborhood. Other simultaneous events, including a possible
mirror event, must not silently enter that portion.

With \(dt\wedge dx\) orientation and
\[
 \beta=d\arg J
 =\frac{(H_xH_{xx}-HH_{xxx})\,dt+(HH_{xx}-H_x^2)\,dx}
        {H^2+H_x^2},
\]
the inherited index theorem gives
\[
 \boxed{\frac1{2\pi}\oint_{\partial\Omega_R}\beta
       =-q_0-K_{\rm later}(\Omega_R),\qquad
 K_{\rm later}=\sum_{\substack{(t,x)\in\Omega_R\\t>T,\ J=0}}
                      \left\lfloor\frac{m(t,x)}2\right\rfloor .}
 \tag{1}
\]
Consequently the sufficient arithmetic target is
\[
 \boxed{\oint_{\partial\Omega_R}\beta<-2\pi q_0.}
 \tag{2}
\]
For an ordinary double, \(q_0=1\); a strict bound below \(-2\pi\)
forces an integer winding at most \(-2\), hence a later collision.
For a fourth-order initial event, \(-2\) is already its own winding
and is not evidence of a later event.

At an actual theta threshold, every strictly later slice is real and
simple. A later multiple zero would have nonreal predecessors still
above \(T\), by [Polymath, Proposition 3.1(ii)][polymath]. Thus (2),
if independently proved from applicable theta information, would
contradict the threshold hypothesis.

A genuinely nonintegral certified interval for the **complete closed**
integral would instead contradict the boundary-degree theorem directly.
Adding interior collisions does not repair nonintegrality: each adds
another integer. The useful target here is to exclude the initial
integer \(-q_0\) on its more negative side. One finite cap suffices;
an infinite limit is optional.

## 2. Making the apex legitimate

The physical jet vanishes at the collision, so a contour passing through
that point has no ordinary physical winding. Two constructions repair this.

**Include the event in a small lower neighborhood.** Start the closed
contour slightly before \(T\), surround \(p\), and then expand into the
future. Choose the entire part at \(t\le T\) inside the isolating
neighborhood. This gives (1) directly.

An explicit family, in \(\tau=t-T,\ y=x-a\), is
\[
 \Omega_{\epsilon,R}
 =\{\,y^2/c^2-\epsilon^2<\tau<R\,\},
 \qquad \epsilon,c,R>0.
 \tag{3}
\]
Its two sides are \(y=\pm c\sqrt{\tau+\epsilon^2}\), joined at the
lower vertex \((-\epsilon^2,0)\), and its upper cap is \(\tau=R\).
Its portion at \(\tau\le0\) lies in
\([-\epsilon^2,0]\times[-c\epsilon,c\epsilon]\), so it can be made
isolating. Nonvanishing on the remaining boundary still needs proof.

The square-root opening reflects the local roots
\(a\pm\sqrt{2(t-T)}+O(t-T)\) at a double event. It is a convenient
geometry, not an assertion of a finite propagation speed for heat flow.
No positive-time global bound on the actual root paths follows from
this local expansion.

**Alternatively, remove the initial index explicitly for an ordinary
double.** Write \(h_2=H_{xx}(p)\ne0,\ h_3=H_{xxx}(p)\), and define
the real-linear complex field
\[
 L(\tau,y)=-h_2\tau+i(h_2y-h_3\tau).
 \tag{4}
\]
This is the actual first-order Taylor term of the physical jet. Its
real Jacobian has determinant \(-h_2^2\), so \(L\) vanishes only at
the origin and has index \(-1\). The reference \(L\) is not asserted
to be a physical heat jet.

The quotient
\[
 Z(t,x)=\frac{J(t,x)}{L(t-T,x-a)},\qquad Z(p):=1,
 \tag{5}
\]
extends continuously across \(p\). Indeed, for
\(\rho=(\tau^2+y^2)^{1/2}\), Taylor's theorem gives
\(|J-L|\le C\rho^2\), while
\[
 |L|\ge c_L\rho,\qquad
 c_L=\frac{h_2^2}{\sqrt{2h_2^2+h_3^2}}>0.
 \tag{6}
\]
The lower bound follows from the determinant and Frobenius norm of
the \(2\times2\) matrix. Hence
\[
 |Z-1|\le(C/c_L)\rho.
 \tag{7}
\]
For example, \(\rho\le c_L/(2C)\) gives \(\operatorname{Re}Z\ge1/2\)
when \(C>0\). A paid \(C\) can be obtained from second derivatives
of the physical jet, requiring spatial derivatives of \(H\) through
order five via the heat equation. No such new theta bound or uniform
curvature floor is acquired here.

Away from \(p\), division by the nonzero complex number \(L\) preserves
the index of every physical zero. Thus a bounded forward domain with
apex \(p\), otherwise contained in \(t>T\), can use the continuous
field \(Z\), provided \(Z\ne0\) on its boundary:
\[
 \operatorname{wind}_{\partial D_R}Z=-K_{\rm later}(D_R).
 \tag{8}
\]
Any negative degree would force a later collision. Off the apex its
phase form is \(\beta-d\arg L\); a small indentation can be filled
using (7). On a contour enclosing \(p\), the same subtraction changes
the physical degree by \(+1\).

This gives a precise way to start a forward contour at the event.
It is bookkeeping, not an additional theta sign. Independent absolute
error disks do not automatically remain useful after division by the
small \(L\); the vanishing Taylor remainder in (7) must be retained.
The construction uses \(h_2\ne0\) and is not a multiplicity reduction.

## 3. The cap can vanish while the original index survives

Use the complete quadratic heat control
\[
 H(\tau,y)=y^2-2\tau,\qquad J=y^2-2\tau+2iy.
 \tag{9}
\]
It has one ordinary collision, at the origin, and no later collisions.
After translating time, its all-real threshold can be any prescribed
\(T>0\). It does not have the complete theta source.

On every domain (3), \(J\) is nonzero on the boundary and the total
integral is exactly \(-2\pi\). The distribution of that phase between
the arms and cap is informative. Put
\[
 b=c\sqrt{R+\epsilon^2},\qquad
 A=b^2-2R=(c^2-2)R+c^2\epsilon^2.
 \tag{10}
\]
The positively oriented cap runs from \(y=-b\) to \(b\); the
parabolic boundary returns from \(b\) to \(-b\).
On that parabolic boundary,
\[
 H=(1-2/c^2)y^2+2\epsilon^2,\qquad H_x=2y.
 \tag{11}
\]
Neither piece can have \(J=0\): on the cap \(H_x=0\) only at \(y=0\),
where \(H=-2R\); on the parabola it happens only at its lower vertex,
where \(H=2\epsilon^2\).

If \(c^2>2\), then \(A>0\). Let
\(\alpha_R=\arctan(2b/A)\in(0,\pi/2)\). Continuous phase tracking gives
\[
 I_{\rm arms}=-2\alpha_R,\qquad
 I_{\rm cap}=-2\pi+2\alpha_R.
 \tag{12}
\]
As \(R\to\infty\), the arms' contribution tends to zero but the
cap's contribution tends to \(-2\pi\).

If \(0<c^2<2\) and \(R>c^2\epsilon^2/(2-c^2)\), then \(A<0\).
Let \(\gamma_R=\arctan(2b/|A|)\). Now
\[
 I_{\rm arms}=-2\pi+2\gamma_R,\qquad
 I_{\rm cap}=-2\gamma_R.
 \tag{13}
\]
The cap contribution **does tend to zero**, but the arms retain
\(-2\pi\). The born roots cross the walls at
\(\tau=c^2\epsilon^2/(2-c^2)\); these are simple spatial-root crossings,
not new physical collisions. Their transport cannot be discarded.

These formulas follow by taking continuous arguments at the endpoints
and through the cap's negative-real-axis crossing. As a differential
check, the exact phase form is
\[
 \beta=
 \frac{4y\,d\tau-(2y^2+4\tau)\,dy}
      {(y^2-2\tau)^2+4y^2}.
 \tag{14}
\]
On the cap its coefficient is strictly negative. On the parabola it
is the derivative of the continuously lifted argument of (11).
In both (12) and (13), the sum is \(-2\pi\), in agreement with the
single physical index. Individual open-arc integrals are not integers.

Thus a vanishing cap is a plausible analytic ingredient, but does
not itself force the extra unit of winding.

## 4. The actual estimate request

For an ordinary initial double, a sufficient finite calculation is
\[
 I_{\rm arms}\le-2\pi-\eta,\qquad
 |I_{\rm cap}|\le e<\eta.
 \tag{15}
\]
More generally, retain signed upper bounds and prove
\[
 U_{\rm arms}+U_{\rm cap}<-2\pi q_0
 \tag{16}
\]
with every boundary approximation and integration error included.
A joint estimate can retain cancellations that separate absolute
bounds lose. Alternatively, bound the degree of the regularized
field (5) strictly below zero on a complete future contour.

Decay of \(H,H_x\) alone does not bound these phase integrals:
\[
 d\arg(AJ)=d\arg J\qquad(A>0).
 \tag{17}
\]
A loop \(e^{-R}e^{-i\theta}\) tends uniformly to zero and still has
degree \(-1\) for every finite \(R\). For theta, the known
[large-height decay][largeheight] is therefore not a reason to drop a cap. Bounds valid for bounded
heat time also cannot be applied to the joint limit
\(t\to\infty,\ x\asymp\sqrt t\) without a new uniform argument.

The analytic control screen is decisive at the stated level: the
quadratic control satisfies the heat equation, an actual threshold,
an isolated double event and no future events, and it fails (2)
by equality for every cone. The positive-source threshold controls
in [cluster 12][controls] likewise cannot be forced to have a later
collision by generic contour topology; the complete theta-source
estimate must supply the distinguishing input. Their missing theta
premises are documented there. No new numerical cone certificate for
those nonpolynomial sources is claimed.

The proposed direction is consequently precise: choose walls whose
phase and root transport admit an effective **theta-specific** estimate,
and seek one extra negative unit beyond the initial event. The apex
can be handled rigorously, and a finite cap is enough. The unresolved
work is the signed boundary estimate, not an infinite iteration.

[paired]: 03_DIRECT_PHYSICAL_WINDING_RELATIVE_PHASE_AND_WALLS_20261020.md
[later]: 02_THRESHOLD_DOUBLE_EVENTS_AND_LATER_WITNESSES_ASTRA_20261019.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[index]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[polymath]: https://arxiv.org/html/1904.12438v2#S3
[largeheight]: https://arxiv.org/html/1904.12438v2#S1
