# Fixed localized comparator and actual level-arc controls

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), reasoning effort ultra**,
verified from parent metadata. Separate same-model derivation and
implementation review; no independent implementation or specialist review.

**Outcome.** One separately frozen later-cap comparison proves a strictly
positive localized Laguerre average, so its desired negative sign is
impossible on that cap. Exact level-arc controls clarify the still-missing
theta continuation contract. This finishes the selected HFCE-04 comparison;
it does not execute HFCE-05 for theta or activate root-interaction energy.

Read with the [result index][results], [collision controls][controls],
and [avoid index][avoid], particularly [reformulations][a01] and
[scoped exclusions][a07]. These are a quantitative comparison and explicit
control geometries, not another claimed RH reduction.

## 1. Frozen weight, time and complete theta comparison

After [the primary assessment][primary], freeze
\[
 \psi_L(y)=\frac{35}{32L}(1-y^2/L^2)^3_+,\qquad L=1/10,
 \qquad r=1/100.
\]
The weight is nonnegative, compactly supported, \(C^2\), and has mass one.
For the same initial parameter labels
\(T\in[.109999,.110001]\), \(a\in[1001.25,1001.5]\), its later cap is
\[
 t=T+r\in[.119999,.120001],\qquad
 x=a+y\in[1001.15,1001.6].
\]
The initial box is already excluded. Consequently this is a declared
cost/sign comparison of the actual theta functional, not an argument
conditional on an existing event there. There is no claim that this support
escapes an event-dependent local positive neighborhood.

The [contract][contract] was written before evaluation: one full cap box,
192/256-bit arithmetic, no subdivisions, no new quadratures, a 300-second
limit, and the strongest available pointwise competitor first. If it proves
\(Q=H_x^2-HH_{xx}>0\), its positive average settles the chosen sign question
and weighted integration stops.

The source cache and pins are the same as in Note 07. Component \(j=2\)
uses midpoint derivatives through order \(2+24+2\cdot12=50\) and
remainder derivatives through \(2+24+2\cdot13=52\). Both are present.
The actual increments are \(R_x=8/5\), \(\Delta=.015001\).
The complete physical mode/source tail formulas in the manuscript extend
to \(j=2\) with the same shift and cutoffs. Their new tangent check gives
\(D_{n,2}>4121.1429\); the retained-source logarithmic second derivative
is negative since
\[
 2T_{\max}-16c\lambda_n e^{4u}-2/(u+d)^2<0
 \quad(u\ge2).
\]
The nonstationary \(Q_2=d^2+2d/B+2/B^2\) factor is paid in the omitted
mode bound. The \(j=2\) normalized omitted-mode allowance is
\(<2.447831\,10^{-13}\), and the retained-source tail is
\(<1.168297\,10^{-435}\).

Each component polynomial is enclosed by Horner and tensor Bernstein
bounds. The consumer also forms the correlated polynomial
\(P_1^2-P_0P_2\) and uses its tensor Bernstein coefficient hull over the
entire two-parameter box. If \(|P_j|\le B_j\) and component errors are
\(\varepsilon_j\), its complete product allowance is
\[
 2B_1\varepsilon_1+\varepsilon_1^2+
 B_0\varepsilon_2+B_2\varepsilon_0+\varepsilon_0\varepsilon_2.
\]
This requires certified component approximations, not
\(P_1=\partial_xP_0\). Whole-parameter variation and arithmetic rounding
are inside the interval polynomials.

The [receipt][receipt] gives, conservatively at both precisions,
\[
 \frac{Q(t,x)}{G_*^2}>0.00168232756063.
\]
The complete product allowance is below \(1.14817\,10^{-10}\).
Because \(\psi_L\ge0\) and \(\int\psi_L=1\), it follows directly that
\[
 \frac{A_\psi(T+r,a)}{G_*^2}
 =\frac1{G_*^2}\int\psi_L(y)Q(T+r,a+y)\,dy
 >0.00168232756063 .
\]
Thus the *actual* selected negative-average target fails throughout this
declared cap. Unlike the Gaussian estimator's inconclusive interval,
this is a positive physical lower bound.

There was no weighted quadrature to pay or perform after this gate.
The inherited source acquisition is charged separately. Obtaining
\(H_{xx}\) used zero new quadratures but nonzero component and polynomial
work, separately timed in the receipt. It is not treated as free.
The run took less than a second; that fact is a finite execution record,
not a general efficiency theorem or a new coverage claim.

## 2. Explicit product budget and own controls

For an \(H,H_x\)-only implementation,
\[
 A_\psi=2\int\psi_L H_x^2-\frac12\int\psi_L''H^2.
\]
Here \(\int|\psi_L''|=84/(5\sqrt5L^2)\), so its uniform component
product payment is
\[
 2(2B_1\varepsilon_1+\varepsilon_1^2)
 +\frac{42}{5\sqrt5L^2}(2B_0\varepsilon_0+\varepsilon_0^2).
\]
To check the derivative norm, put \(b(z)=(1-z^2)^3\).
Then \(b''=-6(1-z^2)(1-5z^2)\), and the total variation of \(b'\)
on \([-1,1]\) is four times its maximum magnitude, attained at
\(|z|=1/\sqrt5\). The factor \(L^{-2}\) is a real cost of narrowing
the support. This alternative's retained integration was not executed.

Direct polynomial integration gives
\[
 \int\psi_L y^2=L^2/9,\quad
 \int\psi_L y^4=L^4/33,\quad
 \int\psi_L y^6=5L^6/429.
\]
For the ordinary quadratic/cubic control with its own initial jets,
\[
 H=h_2(y^2/2-\tau)+h_3(y^3/6-\tau y),
 \qquad
 A_\psi=h_2^2(\tau+L^2/18)+h_3^2(\tau^2+L^4/396)>0
 \quad(\tau>0).
\]
For the bounded positive atomic actual-threshold control
\(H=1-e^\tau\cos y\), putting \(q=e^\tau\) gives
\[
 Q=q^2-q\cos y,\qquad A_\psi\ge q(q-1)>0\quad(\tau>0).
\]
It lacks the unchanged theta source; generic source positivity and
threshold behavior do not force the opposite sign.

For the fourth-order heat polynomial,
\[
 Q=4y^2[(y^2-3\tau)^2+27\tau^2]+288\tau^3>0
 \quad(\tau>0).
\]
Its ordinary normalization is refused because its initial \(h_2=0\).
For the two-event quartic
\[
 H(\tau,y)=y^4+(6-12\tau)y^2+12\tau(\tau-1),
\]
the fixed values \(\tau=3/4,L=1\) instead give
\[
 Q=4y^6-6y^4+45y^2-27/2,\qquad
 A_\psi=-7409/858<0,\qquad Q(0)=-27/2.
\]
The same-data pointwise witness is stronger here. The first event at
\(\tau=0\) is not this field's all-real threshold; the latter is at
\(\tau=1\). That failed premise prevents transferring this later
negative witness to an actual threshold.

The bump moments and polynomial averages are replayed by exact rational
differentiation, multiplication and integration. A negative quartic
fixture is also passed through the actual correlated polynomial/Bernstein
consumer. Controls use their own data and zero polynomial source errors.
The other source families in [cluster 12][controls] are not silently
assigned theta coefficients or theta error budgets.

## 3. What a local level-arc certificate can and cannot do

Let \(F=H/h_2\) at an ordinary event. Fix \(e,\epsilon>0\),
\(R>\epsilon\), \(L^2/2>R+e+\epsilon\). On the entire rectangle
\[
 K=[-(e+2\epsilon),R]\times[-L,L]
\]
suppose
\[
 |F-(y^2/2-\tau)|\le\epsilon,\qquad F_{yy}>0.
\]
The heat equation implies \(F_\tau<0\). On the bottom \(F>e\);
on the top \(F(R,0)<0\) and \(F(R,\pm L)>e\).
Strict convexity gives exactly two top intersections with \(F=e\)
and exactly two zeros between them. For each \(y\) between those
intersections, strict time decrease gives a unique graph \(\tau=g(y)\)
with \(F=e\), lying below \(R\) except at its two endpoints. It and the
cap form a Jordan contour enclosing the initial event. The boundary
jet is nonzero, and its degree is \(-1\).

Thus **this whole-rectangle quadratic/convexity certificate supplies
exactly two cap zeros**, not the four needed for an additional event.
This is a scoped limit of that sufficient local certificate.
Positivity of curvature only on the arc does not have this consequence.

For a complete countercheck, take the two-event quartic above,
\(h_2=12\), and choose \(F=H/12=e=1/12\).
Its actual lower level branch is
\[
 g(y)=\frac{1+y^2-\sqrt{4/3+(2/3)y^4}}2 .
\]
It is strictly increasing for \(y>0\), and on it
\[
 F_\tau=-\sqrt{4/3+(2/3)y^4}<0,\qquad
 F_{yy}=\sqrt{4/3+(2/3)y^4}>0.
\]
At cap \(R=5/4\), the chosen connected arc has exactly two endpoints
\[
 y_\pm=\pm\sqrt{(9+\sqrt{70})/2}.
\]
The cap has four simple interior roots
\[
 \pm\sqrt{(9+\sqrt{66})/2},\qquad
 \pm\sqrt{(9-\sqrt{66})/2}.
\]
The separate upper level branch has two other cap intersections; they
are not endpoints of the selected lower arc. Distinguishing the
connected component is indispensable.

The selected graph and cap enclose exactly the events \((0,0)\) and
\((1,0)\). On the arc \(H=1\), so \(|J|\ge1\); at cap roots \(H_x\ne0\).
There are no boundary collisions. Its physical degree is \(-2\), and
after the initial ordinary event is removed its degree is \(-1\).
This is a complete detector control, not a theta claim: again its
first event fails the actual-threshold premise.

For contrast, the positive atomic actual-threshold control has the
connected level arc
\[
 g(y)=\log((1-e)/\cos y),\quad |y|<\pi/2,\quad 0<e<1.
\]
At any \(R>0\) its endpoints are
\(\pm\arccos((1-e)e^{-R})\), while its only two interior cap roots are
\(\pm\arccos(e^{-R})\). Its degree is \(-1\), with no later event.

HFCE-05 for theta remains **unexecuted**: these exact controls supply
neither an actual theta event-relative arc nor its continuation, cap
endpoints, nonzero curvature normalization, or cap count. HFCE-07
remains **deferred**: no complete or renormalized root system and
independently estimable arithmetic contradiction statistic has been
provided. Neither missing contract is replaced by the successful
polynomial controls.

[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[primary]: 07_FIXED_GAUSSIAN_COMPARISON_20261020.md
[contract]: ../numerics/HFCE_LOCALIZED_CONTRACT_20261020.md
[receipt]: ../numerics/HFCE_LOCALIZED_COMPARISON_20261020.json

[Separate same-model review](../reviews/05_HFCE_BOUNDED_ROUND_REVIEW_20261020.md)
records the analytic checks and executable replay.
