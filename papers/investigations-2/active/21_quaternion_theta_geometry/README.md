# Quaternion theta geometry and RH criteria

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

**Investigation 21 is active at Edward Baker's request.** It develops the
quaternion first jet of the theta heat family as a possible source of a
signed current or boundary identity that excludes positive-time zero
collisions. The exact first-order equations and RH criterion map are the
starting point. Complete-source central estimates, quantitative
imaginary-gluing stability, and a compensated certificate for both
stationary signs over the full possible positive-threshold time range
through height 100 are now established, with an explicit physical norm
gap. The signed estimate at arbitrary heights remains open.

This program was promoted from the quaternion branch of
[investigation 20](../20_constrained_operator_squares/README.md).
The [original quaternion note](../20_constrained_operator_squares/brainstorm/02_QUATERNION_JET_AND_HEAT_OPERATOR_20261014.md)
and [original handoff](../20_constrained_operator_squares/brainstorm/03_QUATERNION_CONTINUATION_20261014.md)
retain the proposal's provenance. New quaternion research belongs here.

## Start here

The [current summary and continuation note](notes/14_SUMMARY_AND_CONTINUATION_20261014.md)
consolidates the established results, remaining signed theorem, replay
commands, and a concrete next session prompt.

Read the [height-100 continuation](notes/11_CORRELATED_TRANSPORT_AND_HEIGHT_100_CERTIFICATE_20261014.md)
for the current bounded result: both stationary signs on 0<=t<=1/2,
|x|<=100, and |F|>1e-16 there. Any positive threshold collision must
have |a|>100. The [shifted-contour payments](notes/12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md)
give absolute jet errors at the gamma exponential scale for arbitrary
heights. The remaining signed target is specified in the
[normalized collision-cusp note](notes/13_NORMALIZED_SIGN_TARGET_IN_THE_COLLISION_CUSP_20261014.md). The [guarded time-collar theorem](notes/10_FORWARD_STATIONARY_COLLARS_AND_BRANCH_CREATION_20261014.md)
gives a precise next continuation mechanism. The
[continuation note](notes/7_CONTINUATION_AND_NEXT_SIGNED_ESTIMATE_20261014.md)
preserves its target and workflow.

1. [Self-contained manuscript](manuscript/quaternion_theta_geometry.tex)
   derives the scalar RH criteria and their quaternion translations, with
   complete proofs of the bounded theta estimates. Its
   [integration review](reviews/4_MANUSCRIPT_CONVENTION_AND_FOUNDATION_AUDIT_20261014.md)
   records the convention, foundation, and equation checks.
2. [Standard Fueter lift with independent time](notes/3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md)
   fixes the adopted quaternion coordinates and proves regularity while
   keeping Newman time separate.
3. [RH criteria and quaternion setup](notes/1_RH_CRITERIA_AND_QUATERNION_SETUP_20261014.md)
   fixes the source, exact RH endpoints, stationary signs, bounded
   losses, and polynomial control.
4. [Initial research program](notes/2_INITIAL_RESEARCH_PROGRAM_20261014.md)
   specifies the first deliverable and the conditions for continuing.
5. [Cauchy Fueter boundary and current reformulations](notes/4_CAUCHY_FUETER_BOUNDARY_AND_CURRENT_REFORMULATIONS_20261014.md)
   gives conjugate-Fueter evolution, signed boundary moments, and a
   unified norm-time stationary target.
6. [Complete theta central estimate](notes/5_COMPLETE_THETA_CENTRAL_ESTIMATE_20261014.md)
   proves an analytic norm gap on \(0\le t\le1,|x|\le8\), with the
   entire source tail paid.
7. [Imaginary gluing stability](notes/6_IMAGINARY_GLUING_STABILITY_AND_HEIGHT_OBSTRUCTION_20261014.md)
   bounds physical jet errors from the full angular defect at one scale
   and identifies the remaining high-height compensation.
8. [Investigation 20's manuscript](../20_constrained_operator_squares/manuscript/constrained_operator_squares.tex)
   supplies the imported collision reduction, predecessor charts,
   locally bounded loss theorem, and existing operator obstructions.
9. [Compensated stationary signs](notes/8_COMPENSATED_STATIONARY_SIGN_DERIVATION_20261014.md)
   pays the K=2, N=3 four-jet remainder and certifies both genuine
   stationary observations on \(1/200\le t\le3/50,\ 7\le x\le41\).
   Its [internal review](reviews/5_COMPENSATED_STATIONARY_SIGN_INTERNAL_REVIEW_20261014.md)
   audits the full cell cover, arithmetic cross terms, and shifted controls.

10. [Full threshold time cover](notes/9_FULL_THRESHOLD_TIME_COVER_AND_HEIGHT_41_GAP_20261014.md)
    certifies 272 cells with no unresolved signs or branch windows and
    derives a direct physical norm lower bound.
11. [Guarded forward collars](notes/10_FORWARD_STATIONARY_COLLARS_AND_BRANCH_CREATION_20261014.md)
    propagate signed amplitudes along regular branches, with complete
    source-moment guards against branch creation and boundary entry.

12. [Correlated transport through height 100](notes/11_CORRELATED_TRANSPORT_AND_HEIGHT_100_CERTIFICATE_20261014.md)
    preserves theta-index cancellation in common Taylor coefficients and
    verifies 510 further closed cells.
13. [Shifted complete-source contours](notes/12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md)
    provide explicit all-index and integration payments with normalized
    error arbitrarily small as a power of height.
14. [Normalized moving-domain sign target](notes/13_NORMALIZED_SIGN_TARGET_IN_THE_COLLISION_CUSP_20261014.md)
    derives the necessary condition T log|a|<=C for a collision, and
    states the signed or locally bounded-loss remainder still unproved.

15. [Summary and continuation](notes/14_SUMMARY_AND_CONTINUATION_20261014.md)
    gives the current baseline and prioritizes a whole-cell normalized
    contour pilot near height 100 before the global signed estimate.

## Objective and first target

Keep Newman time t as an independent real parameter, use
\(q=z_0+\mathbf jz_1\), and define the adopted theta field

\[
F(t,q)=H(t+\overline{z_1},z_0)
+\mathbf jH_z(t+\overline{z_1},z_0).
\]

It is standard left Fueter-regular for each real t. At real quaternion
argument q=x, it equals \(H(t,x)+\mathbf jH_x(t,x)\). The exact endpoint is

\[
\boxed{\mathrm{RH}\quad\Longleftrightarrow\quad
F(t,x)\ne0\quad\text{for every }t>0,\ x\in\mathbb R.}
\]

The physical norm is \(\mathcal E(t,x)=|F(t,x)|^2=H^2+H_x^2\).
The second complex coordinate is independent and acts as a heat-time
displacement inside H; it does not replace external time.

The initial construction target is a theta-specific identity controlling
both stationary Laguerre forms, or allowing a negative loss bounded by
\(K_j\mathcal E\) with \(K_j\) locally bounded through every candidate
collision. Each proposed estimate must state its domain and how it covers
the relevant predecessor curves.

The separate spectral alternative is
\(\mathcal C_0(0,z)\ge0\) for every complex z, where
\(\mathcal C_0=\tfrac12\partial_y^2|H(t,x+iy)|^2\).
The total quaternion norm cannot replace the scalar modulus in that criterion.

## First research deliverable

The [boundary and current note](notes/4_CAUCHY_FUETER_BOUNDARY_AND_CURRENT_REFORMULATIONS_20261014.md)
records exact general identities and their remaining signed target.
The [central bound](notes/5_COMPLETE_THETA_CENTRAL_ESTIMATE_20261014.md) and
[gluing defect estimate](notes/6_IMAGINARY_GLUING_STABILITY_AND_HEIGHT_OBSTRUCTION_20261014.md)
supply bounded source-specific results. The
[compensated certificate](notes/8_COMPENSATED_STATIONARY_SIGN_DERIVATION_20261014.md)
controls the full signed arithmetic cross terms on its padded rectangle.
The [full-time result](notes/9_FULL_THRESHOLD_TIME_COVER_AND_HEIGHT_41_GAP_20261014.md)
and [correlated-source extension](notes/11_CORRELATED_TRANSPORT_AND_HEIGHT_100_CERTIFICATE_20261014.md)
now prove both stationary signs and a direct physical norm gap on
0<=t<=1/2, |x|<=100. Every sign, norm and merged branch window is
resolved in this bounded cover. At arbitrary heights,
[contour payments](notes/12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md)
address absolute approximation; the
[normalized signed target](notes/13_NORMALIZED_SIGN_TARGET_IN_THE_COLLISION_CUSP_20261014.md)
in the moving small-time region remains open.

Produce one short formula note giving either an exact theta-specific
current or boundary identity with its unresolved signed remainder, or a
precise obstruction for a declared operator class. State which criterion
the identity controls and which arithmetic source property it uses.
Retain the jet constraint, every oscillatory term, boundary contribution,
and approximation remainder. An operator factorization alone does not
establish the observation's sign.

## Connections and scope

- [20](../20_constrained_operator_squares/README.md) retains the general
  constrained operator method and quantum-energy application. This
  investigation focuses on the quaternion theta branch.
- [02](../02_angular_jacobi_gluing/README.md) supplies the full imaginary
  gluing information to investigate in a source-specific identity.
- [06](../06_paired_kernel_factorization/README.md) supplies the complete
  paired stationary kernels and their signed cross terms.
- [19](../19_euler_factor_controls/README.md) supplies arithmetic controls
  for checking the hypotheses of a proposed mechanism.

The polynomial heat control and the existing source controls test general
implications. A theorem restricted to genuine theta must identify the
additional property it needs. Passing a finite control screen does not
establish a global sign.

## Research records

Save derivations in `notes/`, tentative candidates in `brainstorm/`,
reproducible calculations and small records in `numerics/`, and assessments
in `reviews/`. Include the date, intended author, LLM assistance, recorded
model and effort. Numerical claims should be linked to their dedicated
notes and certificates.

Future investigation-specific chats belong in
[chat-histories](chat-histories/README.md). At the author's request, the
founding conversation now has its sole registration in this investigation;
its original identity, number 7, filename and first-capture provenance are
preserved in the [relocation record](CHAT_HISTORY_RELOCATION_20261014.json). Follow the repository's
[AGENTS.md](../../../../AGENTS.md),
[history guide](../../../../tools/CHAT_HISTORY.md), and
[large-file policy](../../../../LARGE_FILES.md).
Keep concise milestones in [DRAFT_HISTORY.md](DRAFT_HISTORY.md).
The manuscript was created at the author's explicit request. Keep it as
one stable source and record future milestones in the history; create no
manuscript snapshot folders.
