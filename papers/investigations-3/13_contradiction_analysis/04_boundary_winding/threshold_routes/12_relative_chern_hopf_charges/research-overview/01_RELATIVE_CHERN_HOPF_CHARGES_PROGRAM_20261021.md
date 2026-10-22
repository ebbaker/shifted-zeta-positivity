# Relative Chern and Hopf charges research program

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, verified from this turn's metadata.

[Progress register][progress].

The active endpoint continuation now has a [dedicated research overview][endpoint-overview]
and [progress register][endpoint-progress]. It develops the signed source
obligation near a possible double zero, links the endpoint charge to BW10
and separates the height and multiplicity extensions. This work remains
in BW12; the present overview retains the broader relative-charge program.

## Objective and scope

Direction B in [the proposal note][proposals], Section 3, uses
\(G=(H,H_z):\mathbb C^2\to\mathbb C^2\) for the complete theta flow.
On a bounded domain \(B\) with smooth boundary, a nonzero boundary jet
and finitely many isolated interior joint zeros, complex orientation gives
\[
Q_B=\frac1{4\pi^2}\int_{\partial B}\alpha\wedge d\alpha
=\sum_{p\in B:\,G(p)=0}\dim_{\mathbb C}\mathcal O_p/(H,H_z),\qquad
\alpha=\frac{\operatorname{Im}(\overline H\,dH+
\overline{H_z}\,dH_z)}{|H|^2+|H_z|^2}.
\]
For a holomorphic square map on a neighborhood of a bounded closure in
complex Euclidean space, a proved nonzero boundary already makes the
interior zero set finite: it is compact analytic. [Note 02][note02],
Section 1, supplies this bounded-domain justification; no such assertion
is made for arbitrary complex manifolds.

An order-m heat event contributes \(\binom m2\), as proved in
[Investigation 22 Note 08][g08] and interpreted in [BW10 Note 25][n25].
This relative top Chern or local Hopf observation is distinct from the
ordinary second Chern class of a trivial flat bundle.

The certificate counts complex spacetime events. Its physical application
must specify how \(B\) covers a real time-zero candidate. RH controls
physical positive-time roots; it does not make every complex-time event
forbidden. The [BW10 manuscript][manuscript] leaves endpoint exclusion open.

## Inherited boundary test and controls

For a reference boundary map \(G_0\) of known degree, proposal B5 gives
\[
e_B:=\sup_{\partial B}\|G-G_0\|
<b_B:=\inf_{\partial B}\|G_0\|.
\]
The straight homotopy avoids zero. If the reference degree is zero,
positivity of local holomorphic intersection numbers excludes every
joint zero inside. The finite margin is \(b_B-e_B\). The [first finite pilot][note01]
now certifies a margin >0.00007495 on the ellipsoid
`|t/(1/100)|^2+|(z-113/4)/(1/8)|^2<1`. Its degree is zero,
but the matched direct derivative floor is stronger (>0.00007993)
and needs six rather than eight scalar source integrals. The
[receipt][receipt01] pays the complete source tails; the
[review][review01] is by the producing assistant.

The second round proves a broader comparison in [Note 02][note02]:
for a square holomorphic reference with established zero degree, its
boundary floor is an interior floor. Maximum modulus transfers the
error, giving the same direct joint margin b_B−e_B from the same data
and reference-degree proof. This is an information reduction, not a
complexity theorem. The sharp heat example contains two real roots and
their stationary point, so it is not limited to component-floor pilots.

Note 02 also gives a piecewise affine boundary-degree construction
whose degree is computed, rather than supplied by a holomorphic
zero-free reference. [Exact controls][receipt02] return 0 on the
two-root heat box, +1 on a collision box and the expected signs for
linear orientation controls. Continuous interpolation is paid on every
boundary tetrahedron. That checkpoint's [assessment][review02] is
same-assistant. The subsequent [Note 03][note03] and [receipt][receipt03]
now complete the full-theta application on a two-zero box:
`|Re t|,|Im t|<.01`, `28<Re z<43`, `|Im z|<.01`. Its boundary gap is
>3.5683e−7, while matched direct tensor interpolation gives >3.9348e−7.
Both use 1,032 scalar integrals and 2,056 boundary vertices; the direct
consumer checks 256 full cells instead of 9,228 tetrahedra plus degree
solves. Source anchors lie on the outer negative-time face. The real
slice contains exactly two simple zeros and one stationary point. The
[third assessment][review03] also remains same-assistant.

The quadratic control \(H=z^2-2t\) has charge one in a small ball in
flat ambient space. The cubic
\(H=z^3-(4+6t)z+2\) has three simple complex spacetime events, only one
with real time and position, at \(t=-1/6\). Its physical roots remain
simple and real for \(t\ge0\). Thus global complex charge is not a count
of forbidden physical events. These are B3–B4 screens, not theta examples.

## Bounded work and acceptance criteria

1. **RCH-01 — Choose domain and reference.** State \(B\), orientation,
   boundary regularity, degree of \(G_0\) and physical coverage. Retain
   isolation hypotheses and any boundary deformation.
2. **RCH-02 — Pay the boundary.** Derive complete approximations for
   \(H,H_z\), including complex-time growth, source tails, interpolation
   and discretization. Certify \(e_B<b_B\), or identify the failed
   payment. A sampled minimum is not a full boundary floor.
3. **RCH-03 — Compare with direct exclusion.** Use the same region,
   source accuracy and acquisition accounting. Report charge, margin,
   coverage and total cost. Boundary-only evaluation can be more
   expensive; its advantage is a measured question.
4. **RCH-04 — Extend physical coverage.** After a useful finite result,
   address arbitrary heights and multiplicities. Account for unwanted
   complex-time events and the boundaries of an exhaustion.

Vanishing charge around every physical multiple-zero candidate restates
simplicity. Under [the classification rule][a01], the first milestone is
a finite paid certificate or a precise failed comparison. That first
milestone is met for the specified pilot, without a general advantage.
The former two-component holomorphic-reference proposal has now been
screened by the transfer theorem: changing the reference alone does not
improve the guaranteed uniform margin from the same certificate data.
RCH-05 records that result. RCH-06 is now complete for the exact prototype
and the declared two-zero theta comparison. Boundary feasibility is
established there, while direct interpolation wins the same-data margin
and measured consumer cost. The user's analytical question prompted the
[Note 04 assessment][note04]: RCH-07 now asks for an independently derived
source-dependent charge bound or boundary deformation. Computational
speed is one possible payoff, not the prerequisite for this research.

Note 04 gives a standard finite-cluster reduction with explicit side-wall
and time-cap hypotheses: the total charge is the winding of the monic
cluster polynomial's discriminant in complex time. It derives contour
root-moment differentiation from the heat equation and checks that the
usual reality and parity symmetries preserve, rather than reverse, the
charge. These are proved-in-note interfaces and screens, with
[same-assistant review][review04]; no theta charge bound follows yet.
The discriminant formulation connects to existing endpoint log-gap work
and retains its exterior-root forcing and unresolved endpoint residue.

A future cost experiment still requires a credible acquisition or geometry
difference. Direct consumers may reuse boundary values and analytic
extension; no interior scan is imposed merely for comparison. Stop
routine enlargement of the completed thin-box benchmark. No universal
obstruction to boundary algorithms or analytic charge methods is claimed.

## Analytical two-root continuation

[Note 05][note05] proves a narrower but quantitative component of RCH-07.
On a proper two-root heat window, Delta'=8+A Delta with A given by a
spatial contour and regular at the collision. If |A|<=K and K tau<pi/2
on a real-symmetric time rectangle of imaginary half-width tau, an
integrating-factor primitive is injective. Every event is real, there is
at most one, and the charge is half the difference of the real cap signs.
Whole time-cap nonvanishing follows from these signs and the phase bound;
it is not an additional assumed interior exclusion.

For the full theta source, Note 05 equation (24) gives a sufficient strip
width from complete moments M_1,M_2 and independently established
real-time spatial-wall floors on two nested circles. Both circles need
root count two at an anchor. The estimate uses separation from exterior
roots and contains no inverse internal gap. It remains meaningful at a
possible double event; the quadratic collision control gives charge one.

This remains a proved-in-note conditional continuation theorem with
[same-assistant review][review05]. Its first actual source application is
now [Note 06][note06]: on |Re t|,|Im t|<=.01, circles centered at 71/2
with radii 8 and 10 have complete wall floors >8.36937e-7 and >7.57583e-7
and spatial counts two. Arcwise coupled source estimates give
|A|<3.489078 and K tau<.034891. Two real sign-changing root brackets
on each cap prove Delta>144; the theorem gives charge zero on the
radius-10 product. [Review 06][review06] is self-review and the
[receipt][receipt06] records all payments. No RH or zero table is used.

RCH-09 records this finite application. RCH-07 is partially met, with a
signed estimate near a possible endpoint double and arbitrary-height
wall/collar control still open. The same numerical wall and phase
consumer permits the quadratic event, which has opposite cap signs and
charge one. The well-separated low pair is not a model of a shrinking
endpoint gap. Complete source values, rather than positive moments
alone, supply its signs. The scalar subtraction tightens the coefficient
majorant, but an uncentered payment also passes in this example.

The existing real gap equation retains its original attribution; the
BW14 real-parameter tail gain has not been silently transferred to a
complex wall. Further source work should address event-conditioned
signed information or event location, rather than repeat a known
well-separated finite pair.

## Required control response

The [proposal screen][proposals], Section 7, and [control register][controls]
govern every new estimate. Polynomial heat models fail unchanged theta
source and arithmetic. [Close-source endpoints][n05] fail ordinary
Dirichlet-series arithmetic despite all-real positive-time simplicity.
Euler-factor controls alter Euler data; square-source and finite-prime
controls lack full normalized reflection or unchanged coefficients;
reflected and positive-primitive controls lack the canonical square
expansion. Keep each preservation list separate.

A degree-zero certificate must fail on a domain containing a control's
joint zero. It may succeed on a collision-free control domain. One
successful boundary does not prove global theta exclusion, and one costly
boundary does not exclude all boundary methods.

## Reading and interfaces

Read the [result index][results], [local multiplicities][local],
[avoid index][avoid] and the rules on [controls][a02], [lifts][a03]
and [scope][a07]. [Note 25][n25] and [its internal assessment][r23]
supply normalization, not an arithmetic upper estimate.

[BW-11][A] and [BW-13][C] share the complete heat family with different
observations. [BW-14][D] may supply a source estimate if one is derived.
[HMC-05/06 retain their existing status][hmc].

[A]: ../../11_global_physical_jet_geometry/README.md
[C]: ../../13_spectral_covers_and_periods/README.md
[D]: ../../14_theta_source_transform_constraints/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[g08]: ../../../../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/08_REAL_AND_COMPLEX_COLLISION_MULTIPLICITIES_20261015.md
[hmc]: ../../10_rh_implies_simple_zeros/research-progress/02_HEAT_ROOT_MOTION_AND_SIGNED_CONTOURS_PROGRESS_20261021.md
[local]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[manuscript]: ../../10_rh_implies_simple_zeros/manuscript/main.tex
[n05]: ../../10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md
[n25]: ../../10_rh_implies_simple_zeros/notes/25_MULTIPLICITY_SELECTIVE_CHERN_AND_HOPF_OBSERVATIONS_20261021.md
[progress]: ../research-progress/01_RELATIVE_CHERN_HOPF_CHARGES_PROGRESS_20261021.md
[proposals]: ../../10_rh_implies_simple_zeros/brainstorm/04_GLOBAL_HEAT_GEOMETRY_PROPOSALS_AND_INITIAL_SCREENS_20261021.md
[r23]: ../../10_rh_implies_simple_zeros/reviews/23_GAUSS_AREA_AND_CURVATURE_FLUX_REVIEW_20261021.md
[results]: ../../../../../../../result-summaries/README.md

[note01]: ../notes/01_BOUNDED_THETA_CHARGE_AND_DIRECT_COMPARISON_20261021.md
[receipt01]: ../numerics/RELATIVE_CHARGE_PILOT_20261021.json
[review01]: ../reviews/01_BOUNDED_CHARGE_INTERNAL_REVIEW_20261021.md

[note02]: ../notes/02_HOLOMORPHIC_REFERENCE_TRANSFER_AND_BOUNDARY_DEGREE_20261021.md
[receipt02]: ../numerics/BOUNDARY_DEGREE_CONTROLS_20261021.json
[review02]: ../reviews/02_REFERENCE_TRANSFER_AND_BOUNDARY_DEGREE_REVIEW_20261021.md

[note03]: ../notes/03_TWO_ZERO_THETA_BOUNDARY_AND_DIRECT_COMPARISON_20261021.md
[receipt03]: ../numerics/TWO_ZERO_THETA_COMPARISON_20261021.json
[review03]: ../reviews/03_TWO_ZERO_THETA_COMPARISON_REVIEW_20261021.md

[note04]: ../notes/04_ANALYTICAL_SCOPE_AND_POTENTIAL_OF_RELATIVE_CHARGE_20261021.md
[review04]: ../reviews/04_ANALYTICAL_SCOPE_AND_DISCRIMINANT_REVIEW_20261021.md

[note05]: ../notes/05_TWO_ROOT_DISCRIMINANT_FLOW_AND_REAL_CAP_CHARGE_20261021.md
[review05]: ../reviews/05_TWO_ROOT_DISCRIMINANT_AND_CAP_REVIEW_20261021.md

[note06]: ../notes/06_COMPLETE_THETA_WALLS_AND_REAL_CAP_APPLICATION_20261021.md
[review06]: ../reviews/06_COMPLETE_THETA_REAL_CAP_APPLICATION_REVIEW_20261021.md
[receipt06]: ../numerics/REAL_CAP_THETA_APPLICATION_20261021.json

[endpoint-overview]: 02_ENDPOINT_CHARGE_EXCLUSION_PROGRAM_20261021.md
[endpoint-progress]: ../research-progress/02_ENDPOINT_CHARGE_EXCLUSION_PROGRESS_20261021.md
