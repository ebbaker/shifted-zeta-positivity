# Complete theta on a two-zero box: boundary degree and direct comparison

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. The [assessment][review] is by the producing
assistant; no independent mathematical review is claimed.

**Result — interval-certified finite comparison.** The complete theta
jet \(G=(H,H_z)\) has charge zero on the box
\[
 B=\{|\Re t|,|\Im t|<T,\quad28<\Re z<43,\quad|\Im z|<Y\},
 \qquad T=Y=1/100.                                                \tag{1}
\]
The paid boundary homotopy has gap **greater than 3.5683e−7**. The
matched direct tensor-interpolation certificate gives a joint norm
floor **greater than 3.9348e−7** throughout the same box, from the same
source data and vertex values. Both methods use only field anchors on
the outer boundary. The direct consumer is also cheaper in this run.

At time zero, the real interval \([28,43]\) contains exactly two simple
zeros and exactly one stationary point between them. Thus neither
\(H\) nor \(H_z\) alone separates this domain. This completes the
finite two-component test proposed after [Note 01][note01] and the
prototype in [Note 02][note02]. It demonstrates full-theta feasibility,
not a boundary advantage or a global simplicity result.

The [experiment plan][plan], [replay script][script] and [small receipt][receipt]
record the budget and execution. The [result index][results], [local
geometry cluster][local], [avoid index][avoid], [classification rule][a01],
[control screen][controls] and [campaign rule][a10] govern the status.
This is a measured bounded milestone; zero charge around every possible
multiple-zero candidate would still restate the global exclusion target.

## 1. Acquisition stays on the boundary

Use the unchanged source and normalization of Note 01:
\[
 H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du,\qquad H_t=-H_{zz}.
\]
The 257 real spatial anchors are
\[
 x_k=28+kh,\qquad h=15/256,\quad k=0,\ldots,256.
\]
At each anchor acquire \(H_j(-T,x_k)\), \(j=0,1,2,3\), where
\(H_j=\partial_z^jH\). Every such point lies on the outer face
\(\Re t=-T\), including its edges. No field anchor lies in \(B\).

For each scalar integral the retained part has modes \(n=1,\ldots,4\)
and source range \(0\le u\le1\). Validated Acb quadrature pays its
returned ball radius. The omitted-mode and exterior-source proofs in
Note 01 pay everything else. At anchor time \(-T\), the absolute
factor \(e^{-Tu^2}\le1\), so the time-zero tail majorant is a valid
upper bound. The kernel and quadrature integrand remain entire. The
[Acb integral documentation][acb] describes the validated integration
interface used here; requesting a tolerance alone is not the error
certificate.

Four additional complete positive moments are acquired:
\[
 M_j=\int_0^\infty\Phi(u)u^j e^{Tu^2+Yu}\,du,
 \qquad j=2,3,4,5.                                               \tag{2}
\]
They control all needed derivatives on the closed box and the paths
from its negative-time face. Their recorded upper bounds are
approximately
\[
 (M_2,M_3,M_4,M_5)=
 (7.193038788303\cdot10^{-4},\ 1.200247523187\cdot10^{-4},
  2.320892975112\cdot10^{-5},\ 5.002609570886\cdot10^{-6}).
\]
These displayed decimals are for orientation; the replay uses outward
balls and upper endpoints. Total acquisition is **1,032 scalar
integrals and 284,832 integrand callbacks**, at 192-bit precision.
The declared limits were 1,100 integrals and 180 seconds. No mesh,
precision or acquisition-budget increase was needed.

Let \(c_{j,k}\) be rational dyadic approximations to the returned real
anchor values, with full uniform errors \(\delta_j\). Binary64 rounding
is used only to choose these exact rational centers: the difference
from the validated ball is explicitly added to the error. The largest
\(\delta_j\) is below \(6.72\cdot10^{-21}\). It is much larger than
the retained quadrature radius or source tail and still negligible
beside the interpolation payments. The approximate centers themselves
are not being treated as exact theta values.

## 2. Lift the anchors to the boundary mesh

Use one subinterval in each time coordinate and in imaginary position,
and 256 subintervals in real position. There are
\[
 (2)(2)(257)(2)=2056
\]
boundary vertices. At \(t=t_r+it_i\), \(z=x_k+iy\), their rational
approximations are
\[
 V_j=c_{j,k}+iy\,c_{j+1,k}-(t+T)c_{j+2,k},\qquad j=0,1.           \tag{3}
\]
The shift is \(t+T\), since acquisition is at time \(-T\).
Its largest modulus is \(L=\sqrt5\,T\), not \(\sqrt2\,T\).
The second-order heat Taylor formula gives
\[
 E_j=\delta_j+Y\delta_{j+1}+L\delta_{j+2}
   +\tfrac12\left(Y^2M_{j+2}+2YL M_{j+3}+L^2M_{j+4}\right).       \tag{4}
\]
All line segments lie in the closed box, so (2) controls their actual
real time; \(T\) in the exponential is not replaced by the displacement
\(2T\). The receipt gives
\[
 E_0<6.860578\cdot10^{-8},\qquad E_1<1.244157\cdot10^{-8}.
\]
Thus there are no direct complex-vertex source integrals: the 2,056
vertex values come from boundary-face jets with a paid lift.

The acquisition location matters. A development audit caught that
lifting from time-zero anchors would use interior field values. The
recorded implementation acquires on \(\Re t=-T\) and pays both the
larger displacement in (4) and the real-slice transfer in Section 5.
The saved receipt is from this corrected boundary-acquisition version.

## 3. The boundary charge calculation

Triangulate every rectangular boundary cell using the coordinate-order
Kuhn subdivision of Note 02. For mesh counts \((1,1,N,1)\), the number
of tetrahedra is
\[
 12\sum_{a=0}^3\prod_{b\ne a}N_b=36N+12=9228.                    \tag{5}
\]
Shared vertices are cached, and induced triangulations agree along
intersections of boundary faces. Corners are handled by Brouwer degree;
no unpriced smoothing is used. The domain and target orientation is
\((\Re t,\Im t,\Re z,\Im z)\).

Let \(L_\partial\) be the piecewise affine interpolant of (3). For
each tetrahedron, the coordinate box containing all four vertex images
gives a lower bound for its entire image convex hull. A rational
square-root lower bound is taken with denominator \(10^{18}\); all
origin-distance calculations are exact before this downward rounding.

For face axis \(a\), set that coordinate's variance to zero and use
\[
 (v_0,v_1,v_2,v_3)=(T^2,T^2,h^2/4,Y^2),\quad
 V_t=\sum_{b\in\{0,1\}\setminus\{a\}}v_b,\quad
 V_z=\sum_{b\in\{2,3\}\setminus\{a\}}v_b.
\]
The source error (4) plus the whole-simplex interpolation error is
\[
 e_{j,a}=E_j+\tfrac12\left(M_{j+4}V_t
             +2M_{j+3}\sqrt{V_tV_z}+M_{j+2}V_z\right).            \tag{6}
\]
The largest vector error is on a time face. The certified minimum PL
floor and largest vector error are, respectively,
\[
 b_\partial=\frac{814994811761}{10^{18}},\qquad
 e_\partial<4.581616\cdot10^{-7}.
\]
Checking the appropriate error for every tetrahedron gives the sharper
recorded gap
\[
 \gamma_\partial>
             3.56833296410590\cdot10^{-7}.                        \tag{7}
\]
These are bounds over every complete simplex, not sampled minima.

The degree consumer then cones the boundary to the box center
\((t,z)=(0,71/2)\), assigning the artificial target value zero there.
This is a topological extension; no actual interior field value is
sampled or approximated by that assignment. Exact rational elimination
counts signed preimages of
\[
 v=(1/1000000000039,\ 1/1000000000061,\
     1/1000000000063,\ 1/1000000000091).
\]
Its norm is below the PL boundary clearance. Every one of the 9,228
cone simplices puts that target outside its image; there are no
ambiguous face hits or singular consistent systems. The degree is
therefore **zero**, without using the direct exclusion result below.

The homotopy from \(L_\partial\) to \(G\) is paid by (6)–(7).
Holomorphicity and the compact-fiber argument in Note 02 make all
interior zeros isolated with positive local charge, so degree zero
excludes them. The minimum principle in Note 02 also transfers the
actual boundary floor (7) into the interior after zero-freeness is
known. This puts the boundary and direct margins on a common norm
interpretation.

## 4. A direct comparator using exactly the same vertices

Divide the full box into 256 four-dimensional cells, one for each real
spatial subinterval. Each cell has 16 vertices, and **every one is an
outer-boundary vertex**: the other three coordinates each have only one
mesh interval. The direct method therefore needs no interior field
acquisition and uses the same cached values (3).

Use their tensor-product multilinear interpolant \(L_\square\) on
each cell. It is a convex combination of the 16 images, so the same
coordinate-hull construction supplies a full-cell norm floor.
For a twice differentiable complex-valued function on a real interval
of length \(d\), linear interpolation has error at most
\(d^2\sup|f''|/8\). This follows from the interpolation Peano kernel
and is valid for complex values. Tensor interpolation in the four
coordinates is a product of sup-norm contractions. Telescoping its
four errors consequently gives a **sum of pure second-derivative
bounds**, without a mixed-derivative term.

The complete component error for the direct consumer is therefore
\[
 D_j=E_j+T^2M_{j+4}+(h^2/8+Y^2/2)M_{j+2},\qquad j=0,1.           \tag{8}
\]
The two time coordinates each contribute \((2T)^2M_{j+4}/8\);
real and imaginary position contribute \(h^2M_{j+2}/8\) and
\((2Y)^2M_{j+2}/8\). Errors in the vertex values enter through (4)
and convexity. This estimates \(G\) throughout each full cell, rather
than inferring an interior bound from a surface count.

In this run the worst full-cell hull has the same floor
\(814994811761/10^{18}\) as the boundary calculation. The direct
vector error is below \(4.215131\cdot10^{-7}\), and the recorded
joint floor is
\[
 \gamma_\square>
             3.93481791313081\cdot10^{-7}.                        \tag{9}
\]
It exceeds (7) by more than \(3.66484\cdot10^{-8}\), about 10.3% of
the boundary margin. Both worst cells occur near real position 42.7.
This is an executed comparison, not a claim that tensor interpolation
is universally stronger than simplicial boundary interpolation.

| Quantity | Boundary degree | Direct tensor interpolation |
| --- | ---: | ---: |
| Complete scalar source integrals | 1,032, shared | Same 1,032 |
| Source integrand callbacks | 284,832, shared | Same 284,832 |
| Cached vertex approximations | 2,056 | Same 2,056 |
| Actual interior field anchors | 0 | 0 |
| Norm-floor checks | 9,228 tetrahedra | 256 full cells |
| Additional exact degree solves | 9,228 | 0 |
| Certified joint-floor consequence | >3.5683e−7 | >3.9348e−7 |
| Consumer elapsed time in the recorded run | 1.926 s | 0.0172 s |

Shared acquisition took about 4.279 seconds. The consumer times are
sequential measurements within one run, excluding shared acquisition;
they are not whole-program speed ratios or a claim of optimal direct
cost. Array construction, real-slice coverage checks and common setup
are not a boundary saving. Precision alone would not remove the main
Taylor/interpolation payments visible in (4), (6) and (8).

## 5. Certified nonvacuous physical coverage

The same boundary jets transfer to time zero by
\[
 H_j(0,x_k)=c_{j,k}-Tc_{j+2,k}+r_{j,k},\qquad
 |r_{j,k}|\le\delta_j+T\delta_{j+2}+\tfrac12T^2M_{j+4},\ j=0,1.
\]
For the curvature check use
\(H_2(0,x_k)=c_{2,k}+r_{2,k}\) with
\(|r_{2,k}|\le\delta_2+TM_4\). No new integrals or root-table input
are used. Along each real subinterval, the linear interpolation errors
for \(H\) and \(H_z\) additionally cost \(h^2M_2/8\) and
\(h^2M_3/8\).

All intervals not excluded from zero by these bounds are grouped into
adjacent clusters. For \(H\), there are exactly two clusters. The
complete \(H_z\) enclosure has one strict sign throughout each, and
opposite \(H\) signs occur at its ends. Every other interval excludes
\(H=0\). For \(H_z\), there is exactly one cluster; the bound
\(c_{2,k}-\delta_2-TM_4-hM_3>0\) on each of its intervals proves
strict increase there. Its end signs are opposite. This proves exact
counts and uniqueness, rather than inferring them from sample signs.

The narrower certified sign brackets are:

| Object at \(t=0\) | Rational bracket | Decimal bracket |
| --- | --- | --- |
| First zero in the box | \([1807/64,7243/256]\) | [28.234375, 28.29296875] |
| Unique intervening stationary point | \([3989/128,7993/256]\) | [31.1640625, 31.22265625] |
| Second zero in the box | \([10753/256,673/16]\) | [42.00390625, 42.0625] |

The receipt gives each sign enclosure, the larger clusters used for
uniqueness, and the monotonic derivative floors. Both zeros are simple.
This establishes that the box genuinely needs both jet components.
It does not identify all theta zeros outside \([28,43]\), assume RH,
or turn finite coverage into an exhaustion.

## 6. Controls, scope and research decision

The anisotropic mesh adaptation receives fresh exact-rational checks:

| Control | Mesh | Charge | Paid boundary gap |
| --- | --- | ---: | ---: |
| \((t,z)\) | (1,1,4,1) | +1 | 1 |
| \((\overline t,z)\) | (1,1,4,1) | −1 | 1 |
| \((z^2-2t,2z)\) | (1,1,8,1) | +1 | 1923/102400 |

The quadratic control has radii \((T,T,R,Y)=(1/100,1/100,1/8,1/100)\).
It preserves the heat equation and contains an actual joint event;
charge zero must fail, and the computed result is one. The time
conjugation control deliberately fails holomorphicity and checks
orientation, not positivity of complex intersection numbers.

The broader [control register][controls] retains its status. The
source-family screen from Note 02 is applied analytically here, not
numerically reacquired: Euler-factor controls change Euler data;
weighted-square and finite-prime controls lack unchanged coefficients
and full normalized reflection; reflected controls lack canonical
integer-square support; shape, primitive and auxiliary-channel controls
lack the unchanged arithmetic source; close-source endpoint controls
fail ordinary Dirichlet-series arithmetic. Polynomial and earlier
counter-kernel examples also fail the unchanged theta source. None may
be assigned this run's vertex values or source errors. On a domain
actually enclosing an isolated control event, a valid charge computation
cannot return zero. A collision-free control subdomain may pass.

**RCH-06 is complete for (1) and this declared implementation.** The
boundary method now works with complete theta data on a region where
both components are necessary. The fair direct comparator gives a
stronger margin and lower measured consumer cost with identical
acquisition. **This thin-box implementation does not establish a
boundary advantage.** Stop routine mesh/precision enlargement of this
benchmark as evidence for one.

The scope of that stop is the box, the boundary-face jet acquisition,
the stated interpolation payments and the matched tensor consumer.
It is not a universal obstruction to relative-charge algorithms; see
[the scope rule][a07]. A further cost experiment should first identify
a domain and acquisition scheme with a credible difference between
boundary and competitive direct work. Adding transverse subdivisions
can create interior grid vertices, but does not prove that a direct
method needs to acquire them: boundary reuse and analytic extension
remain legitimate competitors. RCH-07 records this analytical selection
gate; no larger acquisition is part of this checkpoint.

The recorded gain is a working finite certificate and a decisive
comparison for this implementation. No new arithmetic estimate excludes
all endpoint multiple zeros. RCH-04 remains gated, and HMC-05/06 retain
their inherited statuses. The [progress register][progress] preserves all
three checkpoints and the [self-review][review] records the remaining
validation limits.

[note01]: 01_BOUNDED_THETA_CHARGE_AND_DIRECT_COMPARISON_20261021.md
[note02]: 02_HOLOMORPHIC_REFERENCE_TRANSFER_AND_BOUNDARY_DEGREE_20261021.md
[review]: ../reviews/03_TWO_ZERO_THETA_COMPARISON_REVIEW_20261021.md
[plan]: ../numerics/TWO_ZERO_EXPERIMENT_PLAN_20261021.json
[script]: ../numerics/certify_two_zero_boundary_comparison.py
[receipt]: ../numerics/TWO_ZERO_THETA_COMPARISON_20261021.json
[progress]: ../research-progress/01_RELATIVE_CHERN_HOPF_CHARGES_PROGRESS_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[acb]: https://python-flint.readthedocs.io/en/latest/acb.html#flint.acb.integral
