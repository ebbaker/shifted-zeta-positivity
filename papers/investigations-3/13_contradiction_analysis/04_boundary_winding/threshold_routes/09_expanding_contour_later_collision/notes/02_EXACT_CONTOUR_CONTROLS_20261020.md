# Complete parabolic contour consumer and exact controls

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**,
actual reasoning effort **ultra**, verified from recorded turn metadata
by the parent execution.

**Status: proved in-note finite consumer and exact rational polynomial
replay; author self-check.** This completes the polynomial and analytic
consumer checks for BW09-02. It gives no complete theta source estimate,
new theta exclusion, or sign gain. Any separate review must be described
with its actual independence.

Read the [result index][results], [collision controls][controls], and
[avoid index][avoid], especially [target classification][a01],
[control screening][a02], [scoped conclusions][a07], and
[counts are not evidence][a04]. The desired strict winding inequality is
a reformulation of the later-event target. The gain here is a checked
finite consumer that retains the complete boundary, including the apex.

## 1. Physical geometry and orientation

Write \(k=c^2>0,\ e=\epsilon^2>0\), and choose \(B>0\) with
\[
 R=B^2/k-e>0,\qquad
 \Omega=\{y^2/k-e<\tau<R\}.
\]
The positive orientation for \(d\tau\wedge dy\) consists of the cap
\((R,y),\,y:-B\longrightarrow B\), followed by the entire parabola
\((y^2/k-e,y),\,y:B\longrightarrow-B\). Both endpoints and the
vertex \((-e,0)\) are included. Using \(y\) as the parabolic parameter
removes square roots without changing the contour.

For a physical polynomial \(H(\tau,y)\), substitute each path into the
same polynomial and its actual derivative \(H_y\). This produces exact
univariate polynomials for \(J=H+iH_y\). The checker first verifies
\(H_\tau+H_{yy}=0\) by rational coefficient arithmetic.

## 2. A complete branch-free consumer

On a boundary cell parametrized by \(s\in[0,1]\), write each component
of \(J\) in the Bernstein basis. If the coefficients of one component
are all at least \(\delta>0\), or all at most \(-\delta<0\), then that
component has the same strict sign on the **entire cell**. In particular,
\(|J|\ge\delta\) there. The Bernstein conclusion follows because its
basis functions are nonnegative and sum to one.

Replace the jet trace on that cell by the straight chord between its
two endpoint jets. Both paths lie in the same open half-plane, so their
pointwise straight homotopy avoids zero. Shared endpoints make these
cell homotopies continuous on the complete closed boundary. The
boundary degree therefore equals the degree of the endpoint polygon.
Subdivision is a means to establish a whole-cell inequality; sampling
alone never certifies an arc.

For completeness, the rational polygon degree is computed as follows.
Choose an integer \(q\) for which no vertex \((X,Y)\) obeys \(Y-qX=0\).
Such a \(q\) exists because there are finitely many nonzero vertices.
The shear
\[
 (X,Y)\longmapsto(X,Y-qX)
\]
has positive determinant and preserves degree. For an oriented edge
\((X_0,Y_0)\to(X_1,Y_1)\) of the sheared polygon, opposite signs of
\(Y_0,Y_1\) give its real-axis intercept
\[
 X_*=\frac{X_0Y_1-X_1Y_0}{Y_1-Y_0}.
\]
If \(X_*>0\), contribute \(+1\) for \(Y_1>Y_0\), and \(-1\) otherwise.
All other edges contribute zero. There are no cut vertices and no edge
through zero, so this signed sum is the winding. Every operation is
rational; no floating argument or branch unwrapping is used.

The [script][script] records every cell, half-plane margin, endpoint
jet, shear and signed ray crossing in the [receipt][receipt]. A
boundary zero is refused. In a general nonpolynomial application,
failure to find strict margins is inconclusive, not evidence of a zero.

The same proof supplies a direct theta baseline: if a retained rational
jet polynomial \(P\) has a complete component error at most \(e_j\)
on a cell, replace the strict component margin by
\[
 \min\{\pm\operatorname{component}(P)\}-e_j>0.
\]
The actual jet and the endpoint chord of \(P\) remain in the same
half-plane. Retained endpoint values must agree between adjacent cells.
All tails, quadrature, source/parameter uncertainty, derivative and
propagation errors belong in \(e_j\). This is a consumer interface;
the present script supplies no theta errors or source acquisition.

## 3. Exact conversion to the regularized forward target

For an ordinary event at \((0,0)\), retain the program's actual linear
jet
\[
 L=-h_2\tau+i(h_2y-h_3\tau),\quad h_2\ne0,\qquad Z=J/L,\quad Z(0)=1.
\]
On the forward cone \(D_R=\{0<\tau<R,\ y^2<k\tau\}\), choose a
small rational bottom halfwidth \(b>0\), with \(\eta=b^2/k<R\).
The truncated boundary is:

1. cap \(y:-B\to B,\ \tau=R=B^2/k\);
2. right arm \(y:B\to b,\ \tau=y^2/k\);
3. bottom chord \(y:b\to-b,\ \tau=\eta\);
4. left arm \(y:-b\to-B,\ \tau=y^2/k\).

Assume a paid estimate \(|Z-1|\le a<1\) holds on the removed apex
piece \(0\le\tau\le\eta,\ y^2\le k\tau\). Then \(Z\) stays in the
right half-plane on that whole piece, and its boundary degree is zero.
Adding the two domain degrees cancels the common bottom chord.
Moreover \(L\) is nonzero on and inside the truncated contour, so its
degree there is zero. Consequently
\[
 \boxed{W_Z(D_R)=W_Z(D_{\eta,R})=W_J(D_{\eta,R}).}
\]
This proves the apex transfer, including its orientation. It does not
assign a physical winding to the original contour through the event.
The linear reference need not be a heat jet.

For the quadratic controls, \(L=-2\tau+2iy\) and \(J-L=y^2\), hence
\[
 |Z-1|\le\rho/2,\qquad \rho=(\tau^2+y^2)^{1/2}.
\]
On the removed piece, \(\rho\le\eta+b\). The replay takes \(b=1/32\).

For the two-event quartic translated to its first event,
\[
 H=y^4+6y^2-12\tau y^2+12\tau^2-12\tau,
 \qquad L=-12\tau+12iy.
\]
For \(\rho\le1\), direct termwise payment of this **exact polynomial
remainder** gives
\[
 |J-L|\le(42+16\rho+\rho^2)\rho^2\le59\rho^2.
\]
Thus \(k=2,\ b=1/32,\ \eta=1/2048\) give
\[
 \rho\le65/2048<1/16,\qquad
 |Z-1|\le3835/24576<1.
\]
This bound is intentionally conservative. Multiplying \(H\) by \(-1\)
also multiplies \(L\) by \(-1\), leaving \(Z\) unchanged.

## 4. Quadratic controls, including the borderline cone

For \(H=y^2-2\tau\), the only physical collision is the origin, an
ordinary double. The cap can have \(H_y=0\) only at \(y=0\), where
\(H=-2R\ne0\); the parabola can have \(H_y=0\) only at its vertex,
where \(H=2e\ne0\). This proves full boundary nonvanishing for every
\(k,e,R>0\), without an asymptotic assumption.

Put \(A=B^2-2R\) and let \(\theta\in(0,\pi)\) be the argument of
\(A+2iB\). A continuous lift gives the uniform finite formulas
\[
 I_{\rm parabola}=-2\theta,\qquad
 I_{\rm cap}=-2\pi+2\theta,\qquad W_J=-1.
\]
The parabola lift passes through argument zero at the lower vertex;
the cap lift passes through argument \(-\pi\) at its midpoint. These
facts specify the branches without guessing from endpoint principal
arguments. For \(k=2\), \(A=2e\), so as \(R\to\infty\) each open arc
contributes \(-\pi\). This is the borderline case omitted from the
earlier narrow/wide asymptotic formulas.

When \(k<2\), the two born roots cross the physical walls at
\[
 \tau_*=\frac{ke}{2-k},\qquad
 y_*^2=\frac{2ke}{2-k}.
\]
They occur on the finite boundary precisely when \(\tau_*\le R\).
Their physical jets are \(2iy_*\ne0\); these are simple root
transports, not collisions. In the recorded narrow case, the two
crossings are at \(\tau=1/4,\ y=\pm1/\sqrt2\), and are both retained.
There are no such physical-wall crossings for \(k\ge2\).

On the unshifted forward cone, the borderline \(k=2\) arms themselves
follow the two simple roots. The imaginary jet on each arm is nonzero
away from the apex. The truncated consumer and apex payment still
give \(W_Z=0\); a root-following wall supplies no later event here.

The same statements hold for \(-H\), since multiplying \(J\) by a
constant nonzero complex number preserves winding and phase changes.

## 5. Multiplicity and genuine later-event controls

For \(H=y^4-12\tau y^2+12\tau^2\),
\[
 H_y=4y(y^2-6\tau).
\]
At \(y=0\), the simultaneous-zero equation is \(12\tau^2=0\);
at \(y^2=6\tau\), it is \(-24\tau^2=0\). Thus the only event is
\((0,0)\), of multiplicity four. Its physical contribution is \(-2\).
The double quotient must refuse this input because \(h_2=0\).
This control has no later collision and cannot satisfy a strict bound
below its initial contribution \(-q_0=-2\).

For \(F(t,y)=y^4-12ty^2+12t^2-3\), the same factorization of \(F_y\)
shows that its only events are \((t,y)=(-1/2,0),(1/2,0)\).
On the alternative branch \(y^2=6t\), \(F=-24t^2-3\) never vanishes.
Translate \(t=\tau-1/2\). The events are then \(\tau=0,1\), with
\(h_2=12,-12\), respectively. The physical domain below contains both
and only the first at times \(\tau\le0\); the forward domain contains
only the later event. Their degrees are \(-2\) and \(-1\), respectively.

The first event is **not** the all-real threshold: the squared roots
of the unshifted quartic are \(6t\pm\sqrt{24t^2+3}\), both nonnegative
exactly for \(t\ge1/2\). This control tests actual later-event detection
without contradicting threshold simplicity.

## 6. Replay receipt and limits

The physical cases all use \(B=2,\ e=1/4\); the forward cases use
\(B=2,\ e=0,\ b=1/32\). Each row was repeated with both overall signs.
The separation bound is a conservative certified lower bound for
\(|J|\) on the complete physical or truncated boundary. It is not a
lower bound for \(|Z|\). The separate apex estimate for
\(\operatorname{Re}Z\) pays the omitted patch; no quotient modulus
lower bound away from that patch is needed in this homotopy consumer.

| Field and target | \(k\) | \(R\) | Cells | Separation bound | Degree |
| --- | ---: | ---: | ---: | ---: | ---: |
| quadratic, physical narrow | 1 | 15/4 | 7 | 1/4 | -1 |
| quadratic, physical borderline | 2 | 7/4 | 5 | 1/2 | -1 |
| quadratic, physical wide | 4 | 3/4 | 6 | 1/2 | -1 |
| quadratic, regularized narrow | 1 | 4 | 4 | 1/1024 | 0 |
| quadratic, regularized borderline | 2 | 2 | 10 | 3/4096 | 0 |
| quadratic, regularized wide | 4 | 1 | 10 | 1/4096 | 0 |
| multiplicity four, physical | 4 | 3/4 | 12 | 3/4 | -2 |
| two-event quartic, physical | 2 | 7/4 | 12 | 145/128 | -2 |
| two-event quartic, regularized | 2 | 2 | 7 | 1/524288 | -1 |

The checker also actually refuses a physical contour through the
initial event, a cap through the later event, and the fourth-order
event submitted to the double quotient contract. Polynomial
coefficients and contour parameters are exact: there is no floating
rounding, quadrature, tail or parameter error. The apex estimates above
are separate analytic payments, with their rational values in the
receipt. The receipt is about 58 KB and records a hash of its generating
script. The cell counts are implementation data, not mathematical
evidence for a theta sign.

For the nonpolynomial controls in [cluster 12][controls], the applicable
analytic screen is local. At any stated isolated ordinary analytic
event, the paid Taylor quotient lies in a right half-plane on a
sufficiently small event-dependent neighborhood. Hence a sufficiently
small regularized forward cone has degree zero; a sufficiently small
physical contour surrounding that event has degree \(-1\).
The atomic actual-threshold, weighted-square, reflected,
positive-primitive and finite-prime examples with such events
therefore cannot yield the requested negative regularized degree
from these local facts alone. This is an analytic small-domain
screen, not a new numerical large-cone computation. No common radius
or uniform curvature lower bound is asserted.

Their complete coefficients differ from theta, but that distinction
alone is not a quantitative sign calculation. The present favorable
target \(U_Z<0\) specifically fails on the quadratic control and on
each such small local cone, because the exact degree is zero.
Euler-factor threshold lower bounds do not identify an ordinary
threshold event to submit to this contract. Smooth-density and
two-channel positive auxiliary objects do not, by themselves, supply
its physical event hypothesis. No missing event or damping parameter
has been invented.

The next mathematical input remains a complete theta estimate on a
declared contour beyond the paid initial neighborhood. The consumer
now has correct controls, but it provides no such estimate and no
improvement \(G\) over a same-data theta baseline.

[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a04]: ../../../../../../../avoid/04_counts_and_precision_as_evidence.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[script]: ../numerics/check_expanding_contour_controls.py
[receipt]: ../numerics/EXPANDING_CONTOUR_CONTROLS_20261020.json
