# Spacetime collision degree and boundary certificates

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6-astra` (Codex); reasoning effort **ultra**, verified from the
recorded session. Parallel internal assessments used the same configuration;
they are not independent specialist or formal validation.

Status: **new bounded research direction, with an analytic seed and exact
polynomial controls; genuine-theta pilot not started**. This program comes
from the [active-direction review](../../../brainstorm/reviews/ACTIVE_DIRECTIONS_REVIEW_CODEX_20261013.md).
It uses the geometry of the physical value-and-slope pair to turn collision
counting into a boundary winding problem. The potential improvement is a
certificate or a source-specific boundary homotopy, not a new sign inferred
from topology alone.

## Physical state and local orientation

Let \(H(t,x)\) be a real analytic solution of
\(H_t=-H_{xx}\) on a neighborhood of a compact rectangle
\(R=[t_-,t_+]\times[x_-,x_+]\), and suppose the spatial zeros under
consideration have finite multiplicity. Genuine theta heat has this
property: each slice is entire and its value at zero is positive.
Set \(V=(H,H_x)\). Coordinates are ordered \((t,x)\), with the boundary
oriented counterclockwise in that plane. At an ordinary double zero,
\[
DV=\begin{pmatrix}-H_{xx}&H_x\\-H_{xxx}&H_{xx}\end{pmatrix},
\qquad \det DV=-H_{xx}^2<0.
\]
Thus every ordinary collision contributes index \(-1\). Checking only
ordinary collisions would leave the higher-multiplicity gap; the next
section closes it in the analytic heat class.

## Local index for every finite multiplicity

**Claim.** At a spatial zero of exact multiplicity \(m\ge2\), the joint
zero of \((H,H_x)\) is isolated and has local index
\(-\lfloor m/2\rfloor\).

Translate the point to \((0,0)\), and put
\(c=\partial_x^mH(0,0)/m!\ne0\). Joint analyticity and the heat equation
give the weighted leading expansion
\[
\left(\frac{H(r^2s,ry)}{cr^m},
      \frac{H_x(r^2s,ry)}{cr^{m-1}}\right)
\longrightarrow(P_m(s,y),\partial_yP_m(s,y))
\]
uniformly on compact sets as \(r\downarrow0\), where
\[
P_m(s,y)=e^{-s\partial_y^2}y^m
=\sum_{j=0}^{\lfloor m/2\rfloor}
\frac{m!(-s)^jy^{m-2j}}{j!(m-2j)!}.
\]
All lower weighted Taylor coefficients vanish because their spatial jet
order is below \(m\). The domain dilation has positive determinant; the
two target scalings also have positive joint determinant, including when
\(c<0\).

The recurrence and derivative relation are
\[
P_m=yP_{m-1}-2(m-1)sP_{m-2},\qquad P_{m,y}=mP_{m-1}.
\]
For \(s\ne0\), a common root would propagate down the recurrence to
\(P_0=1\), which is impossible. For \(s=0\), the sole joint root is
\(y=0\). Choose \(A\) larger than the absolute values of all roots of
\(P_m(1,\cdot)\), and use \(Q=[-1,1]\times[-A,A]\).
At \(s=1\), this is a scaled Hermite polynomial with \(m\) distinct real
roots. At \(s=-1\), all nonzero coefficients are positive: there are no
real roots for even \(m\), and just the simple root zero with positive
slope for odd \(m\). For \(0<s\le1\), roots scale by \(\sqrt{s}\), so
neither spatial side of \(Q\) has a zero of \(P_m\).

Count crossings of the positive imaginary ray by
\(W=P_m+iP_{m,y}\). On the edge \(s=1\), the boundary traverses increasing
\(y\). Exactly \(\lceil m/2\rceil\) roots have positive derivative, and
at each such crossing
\[
\frac{d}{dy}\arg(P_m+iP_{m,y})=-1.
\]
Each therefore contributes \(-1\). On \(s=-1\), the boundary traverses
decreasing \(y\) and contributes \(+1\) for odd \(m\), zero for even
\(m\). The spatial sides make no crossings of that ray. Consequently
\[
\operatorname{wind}_{\partial Q}W
=-\lceil m/2\rceil+(m\bmod2)=-\lfloor m/2\rfloor.
\]
The model pair has a positive minimum norm on \(\partial Q\). Uniform
convergence transfers this winding to the rescaled true pair by a straight
homotopy for every sufficiently small \(r\). Those anisotropic boundaries
foliate a punctured neighborhood: a point can be put on one by taking
\(r=\max(\sqrt{|t|},|x|/A)\). Hence there are no other joint zeros
sufficiently nearby. This proves both isolation and the index formula.

This argument is an explicit application of heat-polynomial geometry and
planar degree, with no novelty claim for its general mechanism. Classical
parabolic zero-number context is [Angenent 1988](https://people.math.wisc.edu/~angenent/preprints/1988zeroset.pdf).
The elementary Hermite root property also follows from
[orthogonal-polynomial zero theory](https://dlmf.nist.gov/18.2#vi).
Neither reference is an imported theta positivity result.

## Boundary criterion and relation to endpoint counting

Assume \(V\ne0\) throughout \(\partial R\). Compactness and the local
isolation result give finitely many interior collisions. Additivity of
planar degree yields
\[
\boxed{\operatorname{wind}_{\partial R}(H+iH_x)
=-\sum_{p\in R:\,V(p)=0}\lfloor m_p/2\rfloor.}
\]
In particular, winding zero is equivalent to absence of collisions in
this rectangle. This counts collisions, not all real or complex zeros of
a fixed-time slice. Absence of collisions alone does not assert that all
zeros in the rectangle were real initially.

If \(H\) is nonzero on the two spatial sides and the endpoint slices
have simple zeros, the same local heat geometry gives
\[
\operatorname{wind}_{\partial R}(H+iH_x)
=-\frac{Z(t_+)-Z(t_-)}2,
\]
where \(Z(t)\) counts the real roots in the spatial interval. Every event
creates \(2\lfloor m/2\rfloor\) real roots as Newman time increases.
If simple roots cross a spatial side, this endpoint formula needs their
flux; the full boundary winding includes it automatically. Thus the
proposal is related to reverse-time Sturm counting. It does not evade the
information required to establish the boundary count.

## A rigorous approximation interface

Let \(\widetilde V\) be a continuous, explicitly computable closed boundary
curve approximating the genuine real pair. If
\[
\|V-\widetilde V\|<\|\widetilde V\|
\quad\hbox{everywhere on }\partial R,
\]
then straight interpolation avoids zero and preserves winding. Component
errors \(\epsilon_0,\epsilon_1\) give the sufficient Euclidean error
\(\sqrt{\epsilon_0^2+\epsilon_1^2}\). A finite list of sampled angles is
insufficient; every intervening edge needs a homotopy enclosure.

For instance, bounds on the genuine pair along a straight segment can use
\[
\partial_tV=(-H_{xx},-H_{xxx}),\qquad
\partial_xV=(H_x,H_{xx}).
\]
The existing physical jet interface can supply these derivatives on its
declared domain. Pay the density tail, numerical quadrature, approximant
residual and natural-cutoff transitions. Piecewise approximants need
matching enclosures or explicit connectors; an artificial cutoff jump
must not create a spurious winding.

If using a real nonvanishing normalization \(G=bH\), reconstruct
\((H,H_x)=(G,G_x-(b_x/b)G)/b\). A real triangular change extending over
the rectangle with positive determinant preserves the local indices and
boundary degree. Complex carriers must first be converted to the genuine
real physical pair. The negative-index theorem applies to that heat pair,
not to an arbitrary two-component approximate field.

## Retained exact controls

The [checker](../numerics/check_collision_degree.py) uses only rational
arithmetic. It substitutes each oriented rectangle edge into the two
polynomials, converts to Bernstein coefficients and subdivides until one
coordinate has fixed strict sign. The curve and its polygonal chord then
lie in a common convex half-plane avoiding zero. Exact ray-crossing counts
give the polygon winding, hence the true polynomial boundary winding.

For \(P_m\), multiplicities 2 through 10 give
\(-1,-1,-2,-2,-3,-3,-4,-4,-5\). Reversing boundary orientation changes
every sign. The heat equation is checked coefficientwise. A collision-free
heat control \(H=x\) gives winding zero. A nonheat control
\(H=x^2+t^2-1/4\) has two opposite-index joint zeros and winding zero,
showing why the heat hypothesis cannot be omitted. The
[small record](../numerics/COLLISION_DEGREE_SEED_RECORD_20261013.json)
contains the exact outcomes and source hash. These finite controls support
the formulas; the all-multiplicity argument is the analytic proof above.

## First bounded genuine-source experiment

Select one closed genuine-theta rectangle already covered by an existing
joint-jet or finite-zero atlas, so that the target and comparison are fixed
in advance. Avoid boundary collisions or subdivide the domain if their
absence cannot be certified. Produce complete enclosures for its four
boundary curves, certify winding, and compare with interior coverage or
endpoint root counting. Record function and derivative evaluations,
precision, segment counts, tail costs and the smallest paid boundary margin.

Continue if this gives a simpler or cheaper certified covering, handles a
cell on which the existing local test is inconclusive, or accepts a new
theta reflection homotopy with a uniform estimate. Stop expansion if the
boundary work costs as much as existing coverage and supplies no additional
control. A polynomial demonstration is not evidence of a genuine-theta
cost advantage. A uniform source-based deformation of the boundary curve
would be a separate analytic objective.

## Relation to the other directions and to RH

This program uses the physical geometry highlighted by the lift without
requiring a new lift. Directions 01/02 could provide a boundary homotopy;
03 could certify difficult boundary pieces; 05 could improve the chart;
06 gives an alternative interior stationary-sign strategy. The existing
complex spatial argument-principle barrier is a useful computational
comparison but measures a different zero set.

For an RH application, the repository's threshold/no-escape reduction still
needs coverage of all relevant positive times and unbounded heights, with
small-time limits and boundary transitions controlled. The index identity
supplies none of that uniform boundary input. The first target here is a
bounded certificate comparison, followed by independent review of this seed.
