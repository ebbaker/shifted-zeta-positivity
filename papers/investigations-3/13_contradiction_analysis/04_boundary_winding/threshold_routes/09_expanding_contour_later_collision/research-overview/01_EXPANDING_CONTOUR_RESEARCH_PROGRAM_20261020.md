# Research program for expanding heat flow contours and later collisions

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
actual reasoning effort **max**, verified from recorded turn metadata.

**Status: prepared.** This program seeks one complete signed boundary
estimate that forces an additional collision after a hypothetical positive
theta threshold. The first round is finite and bounded. Its useful outcomes
are a quantified improvement, a restricted exclusion, or a precise
obstruction to the selected estimating method.

Edward Baker proposed the expanding “light cone” and corrected the target
to a larger negative integral. [Note 04][origin] supplies the initial
conditional deductions and analytic quadratic control, with author
self-checks only. This ninth route develops that idea as a concrete
approach to BW-03 and BW-04. [The local register][progress] governs BW09
tasks; the [parent register][parent-progress] retains the BW2 arithmetic
and profile work.

**Terminology update, 20 October 2026:** prepared for Edward Baker with substantial LLM assistance, gpt-6-astra (Codex), actual effort ultra. Use “heat flow contour” prospectively; the earlier quoted “light cone” records the proposal's history. [Note 06](../notes/06_HEAT_FLOW_CONTOURS_AND_GAUSSIAN_CAP_ENERGY_20261020.md) clarifies the heat direction, enclosed-collision split, level curves and Gaussian cap energy. This terminology update changes no signed estimate or acceptance condition below.

Read the [result index][results], especially [topology][topology] and
[collision controls][controls], and the [avoid index][avoid]. The governing
rules are [target classification][a01], [own-source control screening][a02],
[scoped conclusions][a07], [a numerical question before acquisition][a10],
[signed recombination][a12], and [a measured gain before expansion][a20].
The degree criterion below reformulates the desired later witness. It
becomes a research gain only when a new applicable estimate supplies its
sign or a smaller, explicitly measured deficit.

## The mathematical target

Use the unchanged theta heat flow \(H_t=-H_{xx}\), with
\(H(0,z)=\xi((1+iz)/2)/8\), and the physical jet
\[
 J=H+iH_x,\qquad
 \beta=d\arg J=
 \frac{(H_xH_{xx}-HH_{xxx})\,dt+(HH_{xx}-H_x^2)\,dx}
      {H^2+H_x^2}.
 \tag{1}
\]
Orient by \(dt\wedge dx\). Assume an isolated threshold event
\(p=(T,a)\), \(T=\Lambda>0\), of spatial multiplicity \(m_0\ge2\), and
put \(q_0=\lfloor m_0/2\rfloor\). A bounded Jordan domain \(\Omega\)
must contain \(p\), have \(J\ne0\) on its entire boundary, and contain
no other collision at \(t\le T\). Under the [physical index theorem][index],
\[
 W_J(\Omega)=\frac1{2\pi}\oint_{\partial\Omega}\beta
       =-q_0-K_{\rm later},\qquad
 K_{\rm later}=\sum_{\substack{(t,x)\in\Omega\\t>T,\ J=0}}
                         \left\lfloor m(t,x)/2\right\rfloor.
 \tag{2}
\]
The target is a rigorous **upper** bound
\[
                  U_J<-q_0.                         \tag{3}
\]
For an ordinary double, \(q_0=1\), so integrality gives \(W_J\le-2\).
Every strictly later theta slice is real and simple; a later multiple
zero would have nonreal predecessors still above \(T\), by the classical
local splitting result cited in [Note 04][origin]. Thus (3) contradicts
the threshold assumption on the event class to which the estimate applies.

A fully nonintegral interval for a closed-loop degree would contradict
degree theory directly; extra interior events cannot repair it. The
present program instead excludes the initial integer on its negative
side. For \(m_0=4\), winding \(-2\) is already the initial contribution.
The degree formula covers finite multiplicities, but the first
regularized estimating attempt below assumes \(m_0=2\).

## Two legitimate ways to handle the collision

Write \(\tau=t-T\) and \(y=x-a\). The primary physical contour is the
boundary of
\[
 \Omega_{\epsilon,R}
   =\{\,y^2/c^2-\epsilon^2<\tau<R\,\},
 \qquad \epsilon,c,R>0.                              \tag{4}
\]
The cap runs from \(y=-c\sqrt{R+\epsilon^2}\) to
\(y=c\sqrt{R+\epsilon^2}\); the parabolic boundary returns to the left
endpoint. Choose its part at \(\tau\le0\) inside an isolating neighborhood
of \(p\), with \(\epsilon^2<T\) if the calculation is to stay at positive
heat time. In particular, exclude any simultaneous mirror collision.
The lower vertex, both arms, cap and corners all belong to the boundary
contract. Smallness of the lower part does not make its phase negligible.

For an ordinary double, the alternative uses the actual linear Taylor
term of \(J\):
\[
 L(\tau,y)=-h_2\tau+i(h_2y-h_3\tau),\qquad
 h_j=\partial_x^jH(T,a),\qquad h_2\ne0.
 \tag{5}
\]
The continuous field \(Z=J/L\), extended by \(Z(p)=1\), removes the
initial index. With the complete Taylor bound
\[
 |J-L|\le C\rho^2,\quad
 |L|\ge c_L\rho,\quad
 c_L=\frac{h_2^2}{\sqrt{2h_2^2+h_3^2}},\quad
 \rho=(\tau^2+y^2)^{1/2},
 \tag{6}
\]
one has \(|Z-1|\le C\rho/c_L\), so a sufficiently small apex patch
stays in the right half-plane. Paying \(C\) by second derivatives of
\(J\) requires physical spatial derivatives through order five.

On \(D_R=\{0<\tau<R,\ y^2<c^2\tau\}\), whose closure includes \(p\),
nonzero \(Z\) on the full boundary gives
\[
 W_Z(D_R)=-K_{\rm later}(D_R),\qquad U_Z<0
             \ \Longrightarrow\ K_{\rm later}\ge1.  \tag{7}
\]
Off the apex use \(\beta-d\arg L\); fill the apex using (6).
\(Z\) is not a heat solution. Index preservation at other zeros follows
from multiplication by the nonzero complex function \(1/L\).
On a loop enclosing \(p\), \(W_Z=W_J+1\); the physical winding on
a contour passing through \(p\) is itself undefined.

The square-root opening follows the local double-root scale. It implies
neither finite heat propagation nor a global bound on root trajectories.
No uniform positive lower bound for \(|h_2|\) is assumed. A numerical
subclass requiring such a bound must state it; an event-dependent analytic
radius is a different kind of result.

## What the inherited work already rules out

The [quadratic control][origin], \(H=y^2-2\tau\), has a genuine
all-real threshold, one double event and no future collision. On every
contour (4), \(W_J=-1\). If \(c^2>2\), the arms' phase tends to zero
and the cap tends to \(-2\pi\). If \(0<c^2<2\), the cap tends to zero
and the arms retain \(-2\pi\), including simple-root crossings of the
walls. A vanishing cap alone therefore cannot give (3).

The [paid local forward neighborhood][forward] has no later collision
and zero physical winding on every wholly later Jordan region inside it.
A successful estimate must involve a region extending beyond that
neighborhood or directly contradict another premise of the event.
Apex regularization and smaller Taylor errors alone do not provide that
nonlocal input.

The [direct-winding study][paired] also shows that paired faces can look
favorable while omitted walls carry winding \(-2\). Its existing
[control receipt][paired-check] is useful infrastructure. Its fixed
[theta comparison][comparison] covered an already certified box and gave
no cost advantage. Repeating that box is not a new exclusion.

Finally, the failed [three-observation profile relaxation][profile]
allows fractional positive masses. Boundary phase and wall transport
retain information absent from those observations, but no theorem yet
shows that the new information defeats every replacement witness.
The failed estimator classes remain closed in their stated scopes.
This route does not require a successful \(Q_L\) estimate to begin.

## Candidate estimates in order of priority

### Shared source remainder after removing the initial index

Start with a finite contour and a coupled estimate for \(Z\) or for
its accumulated phase. Preserve the exact event cancellations in the
complete source integral. In the normalization of the [forward note][forward],
define
\[
 w_T(u)=e^{Tu^2}\Phi(u),\qquad
 K(\tau,y;u)=e^{\tau u^2}
     \{\cos((a+y)u)-iu\sin((a+y)u)\}.
\]
Then the event identities give the exact representation
\[
 J-L=\int_0^\infty w_T(u)
  [K(\tau,y;u)-K(0,0;u)-\tau K_\tau(0,0;u)
                                  -yK_y(0,0;u)]\,du. \tag{8}
\]
This is a proposed source interface for preserving correlated errors,
not a new signed estimate. It is available to general admissible sources;
the distinguishing bound must use the unchanged complete theta source.
Separate absolute bounds on its four terms discard its useful
vanishing at the apex.

The first feasibility question is whether one coupled source observation
can improve the upper bound for the complete phase, after all errors,
over the same-data direct boundary consumer. Test that question before
extending the time range or collecting a large height grid.

### Moving walls and root transport

For a wall \(x=w(t)\), the pulled-back phase is
\[
 \beta|_w=
 \frac{H_xH_{xx}-HH_{xxx}
       +w'(t)(HH_{xx}-H_x^2)}{H^2+H_x^2}\,dt.       \tag{9}
\]
The wall velocity term is essential. Seek a signed combined wall and
cap bound, or an equivalent wall-aware root-count identity derived from
the [existing flux formula][walls]. Record continuous phase branches and
all simple-root crossings. A root leaving the cone can transport the
initial winding without producing a later collision.

For the ordinary-double physical contour, sufficient bounds are
\(I_{\rm arms}\le-2\pi-\eta\) and \(|I_{\rm cap}|\le e<\eta\).
More generally retain signed upper bounds whose sum is below
\(-2\pi q_0\); a joint estimate may be sharper. No sign of an individual
open arc is a substitute for the closed sum.

### Walls following simple roots

As a bounded alternative, examine the two real roots born at the double
event. Along a smooth simple-root path \(H(t,w(t))=0\),
\(J=iH_x\) has constant phase while the sign of \(H_x\) is fixed.
This could simplify a wall integral. The work moves to proving
continuation to a chosen cap, controlling the cap's phase, and accounting
for the apex. Loss of a graph or escape from a finite chart does not
by itself prove a collision. Use this geometry only with a complete
existence and endpoint contract; do not assume the future event to
define the walls.

## The first bounded execution round

**BW09-01 — Fix the contract and audit the inherited argument.**
Choose the ordinary-double event class, finite \(R\), one geometry and
one primary degree target. State the parameter ranges for \(T,a,h_2,h_3\),
the isolation premise, the forward-neighborhood radius, and every
boundary nonvanishing requirement. Explain which new quantitative theta
observation could distinguish the controls. The first note must end with
one actual estimate request and a baseline, not another global criterion.
Record source versions from the working tree, including uncommitted inputs.

**BW09-02 — Implement and check the complete contour consumer.**
Retain the apex, orientation, branch lifts, wall crossings and cap
endpoints. A rational or interval replay of the analytic cone control
checks the consumer, not the theta target. Use the control table below;
either prove a case analytically or record its actual numerical parameters
and errors. No source acquisition is needed merely to recheck the index law.

**BW09-03 — Test one complete theta source estimate.**
Use the contract from BW09-01 and the checked consumer. The existing
[sixth-derivative interface][interface] is a starting resource only on its
validated domains; validate any extension to moving walls or larger time.
Pay all source tails, quadrature, parameter uncertainty, cell propagation
and product errors. If integrating (1) or (9), prove a denominator lower
bound on each complete arc. A certified homotopy may instead prove the
degree without numerical integration. Near the apex use (6) or (8),
not division of independent constant residual disks by a small \(L\).

A retained approximant need not solve the heat equation. If a residual
heat relation is used, include the defect
\(r_t+r_{xx}=-(P_t+P_{xx})\). Independently approximated derivative
components are not automatically derivatives of the same approximant.
First check whether complete first-jet data already exclude the event.
Such an exclusion is useful if new, but an empty event class is not
a phase-estimate gain.

**BW09-04 — Assess one coherent round.**
Compare with the strongest applicable complete direct, half-plane,
wall-flux or relative-phase consumer on the same domain and source data.
State what was improved, what deficit remains, and which selected method
failed if no gain was obtained. Record actual review independence; a
self-check is not an independent review. Update this route's register
and add only a pointer to the parent.

## Control requirements

The inherited analytic and premise screens below are already informative.
New contour implementations still need their own replay. No new
nonpolynomial cone computation is claimed in this planning handoff.

| Control | Required outcome or premise distinction |
| --- | --- |
| \(H=y^2-2\tau\), either overall sign | \(W_J=-1\), regularized degree zero; narrow, wide and borderline \(c^2=2\) cones must never invent a later event. It lacks the theta source. |
| \(H=y^4-12\tau y^2+12\tau^2\) | One multiplicity-four event contributes \(-2\); this is not two successive double events. The double-event quotient contract must refuse \(h_2=0\). |
| \(H=y^4-12\tau y^2+12\tau^2-3\) | Its events at \((-\tfrac12,0)\) and \((\tfrac12,0)\) are ordinary doubles. A domain isolating the first as its only earlier event and containing both must have \(W_J=-2\). The earlier time is not its all-real threshold; it tests detection of a real later event without challenging threshold simplicity. |
| [Positive atomic actual-threshold family][atomic] and the exact finite-profile families in [cluster 12][controls] | Generic positivity, event cancellation and selected profile data do not force an extra event. They fail complete theta coefficients, full profile growth and eventual simplicity at the threshold. Isolate one event; do not include their simultaneous copies unnoticed. |
| Euler-factor controls | Use their own source and margins. A lower bound for their threshold is not an identified threshold event. Their complete coefficients differ from theta. |
| Weighted-square and finite-prime controls | Local collision data can test an applicable local contract; their event times are not supplied finite all-real thresholds. Full reflection or unchanged complete coefficients fail as recorded in [cluster 12][controls]. |
| Reflected, smooth and positive-primitive controls | Reflection and auxiliary positivity alone supply no new boundary sign. Use established events and their own derivative bounds; complete theta arithmetic is absent. |
| Smooth-density and two-channel constructions | Positive auxiliary objects alone do not supply this physical event and contour contract. Do not invent a threshold or numerical damping parameter. |

For an actual proposed quantitative inequality, substitute each applicable
control's own data and name the inequality or premise that fails.
“Not theta” is not a calculation of a sign deficit. The quadratic control
already proves that heat flow, a true threshold and this contour geometry
alone cannot supply the desired strict inequality.

## Measurements and stopping decisions

Use winding units throughout. For two valid upper bounds on the same
physical target and event class, record
\[
 G=U_{\rm base}-U_{\rm new},\qquad
 d=\max(U_{\rm new}+q_0,0),\qquad
 \delta=-q_0-U_{\rm new}.                           \tag{10}
\]
For the regularized target replace \(q_0\) by zero. \(G>0\) measures
an improvement; only \(\delta>0\) gives the stated contradiction.
Equality gives no strict margin. If no complete bound exists, report it
as unavailable, not as zero. Arc bounds, apex radius, boundary separation,
event coverage, multiplicities, acquisition cost and consumer cost must
accompany any numerical claim.

Stop the selected attempt if the new observation is implied by a failed
information class, if its complete error budget gives no improvement,
or if its premise already assumes the required extra winding. Preserve a
precise obstruction or short unsuccessful budget record. Do not enlarge
a numerical campaign merely because the first contour is inconclusive.
A new method can resume with a changed quantitative premise.

## Conditional extensions

**BW09-05 — A cap at infinity.** Activate after a concrete asymptotic
source estimate or finite-contour result makes this useful. Prove uniform
boundary nonvanishing, convergence or a usable finite-cap bound, and
control of all wall transport as the cap moves. Decay of \(H,H_x\)
alone is insufficient: positive rescaling leaves \(d\arg J\) unchanged.
Bounded-time high-height estimates do not cover
\(t\to\infty,\ x\asymp\sqrt t\) without a new uniform proof.
An infinite-domain collision count additionally requires an exhaustion
argument; a finite cap satisfying (3) avoids that requirement.

**BW09-06 — Higher multiplicities and event coverage.** Activate after a
useful signed estimate exists. The physical formula (2) already has the
correct initial index for every finite multiplicity. Any replacement
for the double-event reference \(L\) must pay its own nonvanishing,
index, remainder and physical transfer. Differentiation does not preserve
an arithmetic estimate without proof. Compare each restricted exclusion
with the [current coverage ledger][coverage]; global event heights,
all multiplicities and the time range remain separate obligations.
No global threshold exclusion follows from a single bounded successful
test.

[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a10]: ../../../../../../../avoid/10_numerics_ahead_of_the_question.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
[atomic]: ../../01_local_double_winding/notes/04_EVENT_CONDITIONED_POSITIVE_SOURCE_OBSTRUCTION_20261020.md
[avoid]: ../../../../../../../avoid/README.md
[comparison]: ../../../../../11_arithmetic_collision_rigidity/symmetries/notes/06_GEO_T1_WINDING_AND_DIRECT_COMPARISON_20261019.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[coverage]: ../../../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/13_VERTICAL_WALL_AND_FINITE_HEIGHT_NONCOLLISION_20261018.md
[forward]: ../../05_later_laguerre_violation/notes/02_QUANTITATIVE_FORWARD_NEIGHBORHOOD_EXCLUSION_20261020.md
[index]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md
[interface]: ../../../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/15_COMPLETE_FOURTH_ORDER_INTERFACE_20261020.md
[origin]: ../../../notes/04_EXPANDING_CONTOURS_AND_A_LATER_COLLISION_TARGET_20261020.md
[paired]: ../../../notes/03_DIRECT_PHYSICAL_WINDING_RELATIVE_PHASE_AND_WALLS_20261020.md
[paired-check]: ../../../numerics/DIRECT_WINDING_RELATIVE_PHASE_20261020.json
[parent-progress]: ../../../research-progress/02_THRESHOLD_SIGNED_ARITHMETIC_PROGRESS_20261020.md
[profile]: ../../08_deflated_jet_hierarchy/notes/06_ACTUAL_PROFILE_OBSERVATIONS_AND_RELAXED_DUAL_FAILURE_20261020.md
[progress]: ../research-progress/01_EXPANDING_CONTOUR_PROGRESS_20261020.md
[results]: ../../../../../../../result-summaries/README.md
[topology]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[walls]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md

## Heat flow contour and energy continuation

20 October 2026; gpt-6-astra, actual effort ultra, with substantial LLM
assistance for Edward Baker. The [bounded heat-flow and energy program](02_HEAT_FLOW_CONTOUR_AND_ENERGY_PROGRAM_20261020.md)
and its [HFCE register](../research-progress/02_HEAT_FLOW_CONTOUR_AND_ENERGY_PROGRESS_20261020.md) make the Gaussian
cap, localized BW-05 and nonzero-level alternatives into explicit tasks.
Their preparation does not complete a signed theta estimate or broaden
coverage. This original program and the BW09 register retain authority
over the later-collision target and conditional extensions.

At the user's explicit request, the existing results have also been
consolidated in a [self-contained single-file manuscript](../manuscript/main.tex).
This is a documentation milestone, not activation of broad numerical
acquisition or a new quantitative result.
