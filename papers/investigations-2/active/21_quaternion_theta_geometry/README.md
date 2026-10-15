# Quaternion theta geometry and RH criteria

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Latest research continuation: **gpt-6-astra**, reasoning effort **ultra**.
The integrated manuscript used **gpt-6-astra (Codex)**, effort **ultra**;
earlier investigation setup and certificates also used **gpt-6.1-sol**.

**Investigation 21 is active at Edward Baker's request.** It develops the
quaternion first jet of the theta heat family as a possible source of a
signed current or boundary identity that excludes positive-time zero
collisions. The exact first-order equations and RH criterion map are the
starting point. Complete-source central estimates, quantitative
imaginary-gluing stability, and complete-source certificates for both
stationary signs over the full possible positive-threshold time range
through height 112 are now established, with the safe physical norm gap
|F|>1e-17. The newest cells certify both stationary implications directly,
even where the previous uniform residual-cone enclosure is unresolved.
The current continuation proves an outer comparison for a height-dependent
delay and a full earlier-time comparison on both new finite branches.
Oscillatory block cancellation now proves both Laguerre forms positive
at sufficiently large heights whenever t log(|x|/(4 pi))>=61/24,
including that boundary, with an unevaluated height cutoff. A separate fully explicit bound applies at
|x|>=4 pi exp(10^9) with t log(|x|/(4 pi))>=5. The finite transition
strip and inner small-time region remain open.

This program was promoted from the quaternion branch of
[investigation 20](../20_constrained_operator_squares/README.md).
The [original quaternion note](../20_constrained_operator_squares/brainstorm/02_QUATERNION_JET_AND_HEAT_OPERATOR_20261014.md)
and [original handoff](../20_constrained_operator_squares/brainstorm/03_QUATERNION_CONTINUATION_20261014.md)
retain the proposal's provenance. New quaternion research belongs here.

## Start here

The [latest closed-strip extension](notes/32_CLOSED_STRIP_EXTENSION_AND_MIDDLE_BLOCK_LEMMA_20261014.md)
proves full positivity and both signed cutoff estimates for theta>=61/24.
It resolves the previously excluded boundary theta=8/3. The requested
lower strip 5/2<=theta<61/24, including theta=5/2, remains open; a precise
conditional middle-block lemma identifies a sufficient missing arithmetic
estimate. [Review 23](reviews/23_CLOSED_STRIP_AND_MIDDLE_BLOCK_REVIEW_20261014.md)
audits the proof and 97 exact checks. The finite cover through 112 and
the manuscript are unchanged.

The [resume handoff](notes/26_CONTINUATION_AND_CHAT_HISTORY_HANDOFF_20261014.md)
records the current results, validation, next signed arithmetic-block
estimate, and verified chat-history identity. The
[latest research](notes/25_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_20261014.md)
proves a prescribed height-dependent Gaussian delay has favorable retained
and absorption products on both current stationary sets when
t log(|x|/(4 pi))>=13/4 and height is sufficiently large. The proof pays
the full zeta phase. This comparison lies in the already favorable outer
region, with an unevaluated cutoff.

New complete-source calculations extend the finite cover from 104 to 112.
On both genuine new stationary branches, the products are positive for
**every earlier time** s in [0,t], including both the half-time and smooth
delay rules. Common spatial coefficients preserve the needed correlation.
The [internal review](reviews/19_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_REVIEW_20261014.md)
and [validation receipt](numerics/PHASE_CONTROLLED_CUSP_CONTINUATION_CHECKS_20261014.json)
record 21 exact identities, 1,321 exact audit checks, and two fresh
192-bit quadrature replays. The unbounded inner cusp remains open.

[Note 24](notes/24_PROPORTIONAL_DELAY_PHASE_OBSTRUCTION_AND_CONTINUATION_20261014.md)
explains the preceding obstruction: every nontrivial height-independent
delay with both comparison times positive fails global exact retained
positivity. The new height-dependent rule repairs that outer mechanism.

The [integrated manuscript](manuscript/quaternion_theta_geometry.tex) and
its [39-page PDF](../../../../output/pdf/quaternion_theta_geometry.pdf)
incorporate Notes 19–22. The
[manuscript integration handoff](notes/23_MANUSCRIPT_INTEGRATION_AND_CROSS_TIME_CONTINUATION_20261014.md),
[integration review](reviews/17_MANUSCRIPT_CONTINUATION_INTEGRATION_REVIEW_20261014.md),
and [build record](manuscript/BUILD_RECORD.json) record that version's
proof audit, 100 fresh exact checks, compilation, and visual inspection.
The newer research in Notes 24–32 is saved separately and has not yet
been integrated into that manuscript.

The manuscript's main analytic theorem uses oscillatory blocks to prove uniform outer
positivity at t log(|x|/(4 pi)) >= 3 + epsilon. A separate fully explicit
threshold-five theorem uses |x| >= 4 pi exp(10^9). Exact paired integrals
preserve all arithmetic and integration cross terms. The manuscript also
contains the auxiliary signed-curvature identity, the direct product
absorption criterion, and complete proofs of the sharp-endpoint and finite
rational-jet closure obstructions.

**14 October 2026 preceding research update.**
[Note 31](notes/31_SIGNED_CUTOFF_LEMMA_AND_THRESHOLD_EIGHT_THIRDS_20261014.md)
lowers the sufficient asymptotic threshold to **8/3 + epsilon**, with an
unevaluated height cutoff, using complete hybrid arithmetic block bounds.
It proves the recommended signed cutoff lemma on that new subdomain,
including an explicit Gaussian pair-tail allowance. Note 32 now extends
this result to the closed threshold 61/24; the lower strip beginning at
theta=5/2, the smaller cusp, and the finite bridge remain open.
[Review 22](reviews/22_SIGNED_CUTOFF_AND_THRESHOLD_EIGHT_THIRDS_REVIEW_20261014.md)
separates the analytic argument from 84 exact rational checks. No finite
height extension or manuscript revision is included. Prepared for Edward
Baker with substantial LLM assistance; recorded gpt-6-astra, effort ultra.

[Note 22](notes/22_PROPER_SOURCE_FILTERS_AND_THETA_CORRELATIONS_20261014.md)
certifies a proper two-index split absorbing an adverse complement on both
stationary branches; the prescribed one-index split fails. A full-source
Gaussian gives an exact time comparison and 14 favorable branch/time
cells. [Note 21](notes/21_ONE_SIDED_STATIONARY_ESTIMATES_AND_THETA_PILOT_20261014.md)
supplies the eight-slab full-residual comparison and explains the extra
vanishing obligation imposed by a squared-residual condition. Those
earlier pilots stay inside the height-104 cover; Note 25 adds the new
104–112 results. The unbounded comparison near possible collisions
remains unproved.

[Note 19](notes/19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md)
and [Note 20](notes/20_EXPLICIT_OUTER_HEIGHT_BOUND_20261014.md)
retain the detailed outer and paired-source derivations. Reviews
[14](reviews/14_OSCILLATORY_BLOCKS_AND_EXPLICIT_HEIGHT_REVIEW_20261014.md),
[15](reviews/15_ONE_SIDED_STATIONARY_ESTIMATES_REVIEW_20261014.md), and
[16](reviews/16_SOURCE_FILTERS_AND_THETA_CORRELATIONS_REVIEW_20261014.md)
record their earlier independent internal audits and replays. The
[previous rewrite note](notes/18_MANUSCRIPT_REWRITE_AND_CONTINUATION_20261014.md)
and [backup receipt](manuscript/BACKUP_RECORD_20261014.json) retain the
older manuscript provenance.

The [uniform outer-region theorem](notes/17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md) is the preceding analytic result. For every epsilon>0, both Laguerre forms are strictly
positive and the first jet is nonzero whenever 0<t<=1/2, |x|>=X_epsilon,
and t log(|x|/(4 pi))>=4+epsilon. The four physical derivatives share one
nonzero zeta amplitude, with uniform relative errors. This is an analytic
consequence of the effective Polymath approximation. Its original note
leaves X_epsilon unevaluated and localizes asymptotic collisions at 4;
Notes 19 and 20 give the subsequent threshold-three improvement and the
explicit threshold-five height, with the inner region and finite transition
strip still unresolved.
See the [independent internal review](reviews/12_UNIFORM_OUTER_CUSP_INTERNAL_REVIEW_20261014.md).
Prepared 14 October 2026 with substantial LLM assistance,
**gpt-6-astra**, effort **ultra**.

The [centered residual continuation](notes/16_THETA_CENTERED_RESIDUAL_AND_SHARED_ARITHMETIC_20261014.md)
gives the preceding bounded result: an exact common arithmetic representation, explicit
sum-of-squares stationary loss identities, and a relative residual cone
on 32 closed cells covering 0<=t<=1/2, 100<=x<=104. It extends the
strict physical gap |F|>1e-16 through height 104. The all-height signed
arithmetic estimate remains open. Prepared 14 October 2026 with substantial
LLM assistance, **gpt-6-astra**, effort **ultra**.

The [height-100 summary and continuation note](notes/14_SUMMARY_AND_CONTINUATION_20261014.md)
consolidates the preceding baseline, remaining signed theorem, and replay
commands.

The subsequent [octonionic continuation](notes/15_OCTONIONIC_LIFT_AND_ASSOCIATOR_SIGN_TARGET_20261014.md)
constructs an eight-dimensional monogenic extension and expresses the
collision energy and stationary signs as oriented associators. A positive
entire-source collision control shows why an additional theta-specific
estimate is still needed. This continuation was prepared on 14 October
2026 with substantial LLM assistance, **gpt-6-astra**, effort **ultra**.

Read the [phase-controlled delay and cusp extension](notes/25_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_20261014.md)
for the current bounded result: both stationary signs on 0<=t<=1/2,
|x|<=112, and |F|>1e-17 there. The prior
[height-100](notes/11_CORRELATED_TRANSPORT_AND_HEIGHT_100_CERTIFICATE_20261014.md)
and [height-104](notes/16_THETA_CENTERED_RESIDUAL_AND_SHARED_ARITHMETIC_20261014.md)
records retain their stronger local floors. Any positive threshold
collision must have |a|>112. The [shifted-contour payments](notes/12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md)
give absolute jet errors at the gamma exponential scale for arbitrary
heights. The remaining signed target is specified in the
[normalized collision-cusp note](notes/13_NORMALIZED_SIGN_TARGET_IN_THE_COLLISION_CUSP_20261014.md). The [guarded time-collar theorem](notes/10_FORWARD_STATIONARY_COLLARS_AND_BRANCH_CREATION_20261014.md)
gives a precise next continuation mechanism. The
[continuation note](notes/7_CONTINUATION_AND_NEXT_SIGNED_ESTIMATE_20261014.md)
preserves its target and workflow.

1. [Rewritten manuscript](manuscript/quaternion_theta_geometry.tex)
   gives the complete uniform outer proof, the collision and hypercomplex
   constructions, the shared arithmetic residual, and the bounded results.
   Its [current integration review](reviews/17_MANUSCRIPT_CONTINUATION_INTEGRATION_REVIEW_20261014.md)
   records the source checks, focused independent assessment, compact
   replays, and final PDF verification. The
   [earlier audit](reviews/4_MANUSCRIPT_CONVENTION_AND_FOUNDATION_AUDIT_20261014.md)
   remains historical foundation/convention provenance.
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
    gives the height-100 baseline and prioritizes a whole-cell normalized
    contour pilot near height 100 before the global signed estimate.

16. [Octonionic lift and associator sign target](notes/15_OCTONIONIC_LIFT_AND_ASSOCIATOR_SIGN_TARGET_20261014.md)
    proves the explicit monogenic extension, signed associator identities,
    and positive analytic-source collision control. Its
    [internal review](reviews/10_OCTONIONIC_LIFT_AND_ASSOCIATOR_INTERNAL_REVIEW_20261014.md)
    includes independent replay of 248 exact algebra checks; the proposed
    all-height theta-specific radial residual estimate remains unproved.

17. [Theta centered residual and shared arithmetic](notes/16_THETA_CENTERED_RESIDUAL_AND_SHARED_ARITHMETIC_20261014.md)
    proves an exact common-kernel representation with logarithmic weights,
    complete new tail payments, and stationary sum-of-squares identities.
    A validated relative cone on 32 closed cells extends both stationary
    signs and the physical gap through height 104; its
    [internal review](reviews/11_THETA_CENTERED_RESIDUAL_INTERNAL_REVIEW_20261014.md)
    independently replays the calculation and audits the exact endpoints.

18. [Uniform outer-region signs and threshold four](notes/17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md)
    proves both full Laguerre inequalities beyond X_epsilon in the region
    t log(|x|/(4 pi))>=4+epsilon, retaining a common nonzero arithmetic
    amplitude. Shrinking complex discs pay all four derivative errors
    without differentiating a moving cutoff. Signed inner-region targets
    remain necessary; small residual cones and phase-free integrand
    positivity impose stronger conditions.

19. [Manuscript rewrite and continuation](notes/18_MANUSCRIPT_REWRITE_AND_CONTINUATION_20261014.md)
    describes the new exposition, preserved backup, validation scope, and
    the signed inner-region and explicit outer-cutoff targets.

20. [Oscillatory blocks and paired forms](notes/19_OSCILLATORY_BLOCKS_AND_PAIRED_LAGUERRE_FORMS_20261014.md)
    proves the sufficient threshold-three theorem and exact source pairings.
21. [Explicit outer height](notes/20_EXPLICIT_OUTER_HEIGHT_BOUND_20261014.md)
    evaluates a separate conservative threshold-five cutoff.
22. [One-sided stationary estimates](notes/21_ONE_SIDED_STATIONARY_ESTIMATES_AND_THETA_PILOT_20261014.md)
    gives the favorable-curvature split and its full-theta pilot.
23. [Proper filters and theta correlations](notes/22_PROPER_SOURCE_FILTERS_AND_THETA_CORRELATIONS_20261014.md)
    gives both proper-filter pilots and the analytic obstructions.
24. [Integrated manuscript and cross-time continuation](notes/23_MANUSCRIPT_INTEGRATION_AND_CROSS_TIME_CONTINUATION_20261014.md)
    records the current manuscript, validation, next objective, and verified
    history identity.
25. [Proportional delay phase obstruction](notes/24_PROPORTIONAL_DELAY_PHASE_OBSTRUCTION_AND_CONTINUATION_20261014.md)
    derives the exact complex cross-time products, certifies 16 bounded
    half-time cases, and excludes height-independent delays with
    0<delta(t)<t at a positive time from global exact retained positivity.
26. [Phase controlled delay and cusp extension](notes/25_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_20261014.md)
    proves the repaired outer comparison and extends the finite cover
    through 112, with all-earlier-time signs on both new branches.
27. [Continuation and chat-history handoff](notes/26_CONTINUATION_AND_CHAT_HISTORY_HANDOFF_20261014.md)
    consolidates the current domains, exact next task, reproduction links,
    manuscript status, and preserved history identity.

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
and [correlated-source extension](notes/11_CORRELATED_TRANSPORT_AND_HEIGHT_100_CERTIFICATE_20261014.md),
together with the [centered residual band](notes/16_THETA_CENTERED_RESIDUAL_AND_SHARED_ARITHMETIC_20261014.md),
now prove both stationary signs and a direct physical norm gap on
0<=t<=1/2, |x|<=104. Every stationary sign and physical norm decision is
resolved in this bounded cover; the new band does not assert branch
existence or uniqueness. At arbitrary heights,
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
