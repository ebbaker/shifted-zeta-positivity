# Real Thom and degree integrals: initial program

22 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6.1-sol (Codex)**,
reasoning effort **ultra**, verified from this conversation's turn metadata.

Read the [result index](../../../../result-summaries/README.md) and
[avoid index](../../../../avoid/README.md) before beginning. This is an
initial comparison program; organization adds no new theta bound.

**Current research update, 22 October 2026:** [Note 04](../notes/04_INTEGRAL_BOUNDS_WITHOUT_INTERIOR_NONVANISHING_20261022.md) gives a complete theta integral upper below 0.699 while nine retained first-jet interval boxes still contain the origin. Boundary-only enclosures pay the wider fixed collar; no complete interior nonvanishing certificate is used as a premise. The [separately fixed contract](../notes/03_INTEGRAL_BUDGET_COMPARISON_CONTRACT_20261022.md) and [internal review](../reviews/02_ACTIVE_BULK_COMPARISON_INTERNAL_REVIEW_20261022.md) record the positive-part budget and cost loss to direct. Active interval budgeting is implemented; actual nonempty theta support and a signed-cancellation advantage are not established. The original [support-only result](../notes/02_SUPPORT_REJECTION_AND_CONTROL_ANALYSIS_20261022.md) remains a scoped closure. The setup below states the inherited identity and general obligations; later records supply the acquired finite data.

## Consumer and inherited identities

Use real spacetime oriented by \(dt\wedge dx\), the unchanged physical
frame and backward heat equation
\[
F=(H,H_x),\quad E=H^2+H_x^2,\quad H_t=-H_{xx},\qquad
\mathcal L_1=H_{xx}^2-H_xH_{xxx}.
\]
Let D be bounded with piecewise smooth oriented boundary. Assume H real
analytic near its closure, no identically zero spatial slice, and F≠0 on
∂D. Its finitely many interior events have finite spatial orders m_p.
The [existing real index theorem][index] gives
\[
\beta={H\,dH_x-H_x\,dH\over E},\qquad
{1\over2\pi}\oint_{\partial D}\beta=-K(D),\quad
K(D)=\sum_{p\in D}\lfloor m_p/2\rfloor.
\]
All boundary components carry their induced orientations. The degree is
real and two-dimensional; its weights are not the complex intersection
weights \(m(m-1)/2\).

Choose \(0<b<\min_{\partial D}|F|\), and a nonnegative smooth target
density \(\rho\in C_c^\infty(B_b(0))\) with integral one. Since
\(\det D_{(t,x)}F=-\mathcal L_1\), the classical degree pullback formula
gives the exact finite-scale identity
\[
\boxed{\int_D\rho(H,H_x)\mathcal L_1\,dt\,dx=K(D).} \tag{1}
\]
The map restricted to F⁻¹(B_b) is proper over that ball, and degree is
constant there. See [Guillemin–Haine, §3.6][degree] and [Survey 05][survey].
This is another representative of the existing invariant, with no inverse
E denominator. The integrand remains signed: generic heat fields need
not have \(\mathcal L_1\ge0\). A complete upper enclosure below one
forces K=0. Declaring this criterion does not establish its upper bound.

For \(\lambda>0\), the Gaussian version has a boundary correction:
\[
I_\lambda={\lambda\over\pi}\int_D e^{-\lambda E}\mathcal L_1\,dt\,dx
=K(D)+{1\over2\pi}\oint_{\partial D}e^{-\lambda E}\beta,
\]
\[
|I_\lambda-K(D)|\le {e^{-\lambda b^2}\over2\pi}
\oint_{\partial D}|\beta|. \tag{2}
\]
Indeed \((1-e^{-\lambda E})\beta\) extends smoothly across F=0 and
its exterior derivative is \(-2\lambda e^{-\lambda E}\mathcal L_1
dt\wedge dx\). Infinite target support prevents omitting this correction.
The earlier [BW09 formula (9)][bw09] already expresses winding by the
limit of the signed bulk kernel \(\epsilon^2\mathcal L_1/
\{\pi(E+\epsilon^2)^2\}\). Its signs and boundary limit remain the baseline.

## First bounded comparison: RTD-01

Specify one domain from reusable paid data, precision, complete source
supplier, target density or Gaussian parameter, and baseline before
acquisition. The setup selected no domain or floor; the subsequent Notes01 and03 fix both for their separate bounded comparisons. Retain identical
F, orientation, coverage, source information and error accounting across
the bulk and complete-winding methods, together with a practical interior
comparator when available.

The [Investigation 22 pilot][pilot] used 698 boundary enclosures versus
255 for its interior baseline on shared source inputs. This is inherited
finite evidence, not a universal cost theorem. Charge the boundary floor
even when its acquisition is shared. A rescaling
\(\rho_b(y)=b^{-2}\rho_1(y/b)\) has amplitude b⁻² and gradient cost
b⁻³. Pay uncertain cutoff crossings, nonlinear products, interpolation,
quadrature, and all theta-index/source-ray tails for jets through H_xxx.
Do not silently truncate the complete source or discard signed cancellation.
Singular frame changes need a new Jacobian, density and floor comparison.

Record complete intervals, target error, shared/additional acquisitions
and measured cost separately. Accept a stricter complete upper allowance
or a measured acquisition benefit on equal coverage; explain which
milestone it meets. If support resolution and floor costs consume the
benefit, close that specified estimator without excluding other densities.

## Controls, endpoints and scope

The [control register][controls] and [matched-premise rule][screen] apply.
The quadratic H=x²−2t contributes K=1 on an enclosing regular domain;
all finite multiplicities require the floor(m/2) law. Weighted-square,
Euler-factor, reflected and primitive-compatible controls retain their
separate source hypotheses. The identity should pass matching collisions;
only an independently proved theta upper estimate can distinguish them.
Also use collision-free domains, boundary-event refusals and required
retention of Gaussian corrections. A finite control certificate need not
fail on a box containing no collision.

For simplicity, an integral on 0<t≤T misses t=0. Either enclose the
endpoint with negative and positive time, or formulate and pay relative
boundary data. RH gives no vanishing count at negative time. Endpoint,
all-height and global RH claims are gated beyond the first pilot. No new
source estimate or numerical acquisition was supplied by the initial setup; the linked continuation records supply finite interval data.

[survey]: ../../brainstorm/05_BROAD_SURVEY_OF_TOPOLOGICAL_INTEGRAL_FORMULAS_FOR_RH_AND_SIMPLICITY_20261022.md
[index]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[pilot]: ../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md
[bw09]: ../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/notes/05_TOPOLOGICAL_ALTERNATIVES_AND_ENERGY_OBSERVATIONS_20261020.md
[degree]: https://math.mit.edu/classes/18.952/spring2013/docs/book.pdf
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[screen]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
