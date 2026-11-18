# Exterior counts, distances and signed gap transport across height

**Current phase, revised 17 November 2026:** develop quantitative joint
bounds for the exterior environment of an isolated two-zero cluster,
with explicit height and time dependence; extend a successful mechanism
to larger clusters. B07/B08 completed in chat0006: the canonical far-tail main term and
exact-identical-count scope test are accepted within scope by E14.
B09/B10 now supply an accepted source-based transverse mean and an
exponential count of isolated pairs with negative interaction. The
fixed-collar every-pair sign remains open. B11 now supplies accepted
time-occupation and conditional interior-interaction gains. The author
now assigns Gaussian scale development to the
[GR child](../01_gaussian_resolvent_hierarchy/README.md), and complex-power
p-plane contour evolution and bounds to the [CM sibling](../02_complex_p_mellin/README.md).
Their shared integer/resolvent/spatial inputs stay at their existing paths.
Use [Synthesis42](../notes/42_VCD_GT_B11_FIXED_COLLAR_SYNTHESIS_20261117.md)
for the parent baseline and the two child continuations linked below for
new work. Parent B12 remains an unactivated coordination gate. The [active plan][plan] and
[sole parent register][progress] retain other VCD-GT tasks; the
[setup continuation][continuation] retains its dated routing history.

Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance.
Actual lead model/effort unavailable. The author requests future lead
sessions at **ultra** and expressly authorizes **GPT-6.1 Sol/ultra** subtasks
for bounded derivations, calculations, numerical checks and assessments.
Requested settings are distinct from actual recorded settings. This live
path retains its original 16 November filename and investigation identity.

The revision implements the discussion in [progress note10][b10],
[threshold, cost and height note11][b11], [correlation predecessors and
multiplicity-two note12][b12], and [planning recommendation13][b13]. These
notes supply the reasons for the revised priorities; none proves the new
joint estimate. Read the [result index][results] and [avoid index][avoid],
especially [geometry13][geometry], [theta arithmetic14][theta],
[coefficient18][coeff], [controls12][controls], [classification01][a01],
[premises02][a02], [scope07][a07] and [joint estimates12][a12].

The author-requested [manuscript integration43](../notes/43_VCD_GT_RECENT_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261117.md)
now develops these results in dependency order, with explicit proofs,
supporting computations in Appendix B, and §19 devoted to outstanding
challenges. [Assessment20](../reviews/20_VCD_GT_E24_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261117.md)
accepts it within scope after corrections. This exposition milestone
does not activate B12 or strengthen the scientific conclusions.

**Later sibling routing, 17 November 2026:** the author now separates
[Gaussian spatial-scale work](../01_gaussian_resolvent_hierarchy/notes/08_VCD_GT_GR_SIBLING_DIVISION_AND_CONTINUATION_20261117.md)
from [complex-p/Mellin contour work](../02_complex_p_mellin/notes/01_VCD_GT_CM_SETUP_CONTINUATION_20261117.md).
The second route explicitly targets the M evolution equation as a p-plane
contour integral and an analytical bound with infinite-index potential.
Earlier sole-GR launch wording below is superseded as routing only. Each
child owns its own task IDs; canonical and integer/spatial evidence is
shared by reference. Parent B12 stays unactivated and no parent result changes.

## Question and ownership

What does the unchanged theta source force about exterior counts,
distances and signed interaction **given an isolated close pair**, and
can that information control the pair as height increases and positive
time decreases? Begin with total cluster multiplicity two. The eventual
objective is positivity/reality, allowing multiple real zeros at time zero;
a uniform positive gap or endpoint simplicity is not part of the target.

VCD-GT owns this physical-time exterior/cluster question. Source-variable
probabilities, actual-zero statistics and deterministic cluster energies
are possible tools for it. An independent general correlation theory is
not a new branch objective. The [parent][parent] owns shared VCD tasks;
[parent VCD-B07/E25][parentregister], [degree contraction][sibling2] and
[multiscale collision bounds][sibling3] retain their separate ownership.
The GT prefix is mandatory, particularly for GT-B07 versus parent B07.

## Fixed objects, pair coordinates and time convention

Keep the complete canonical source and literal Fourier observation:

\[
 W_\lambda(s)=e^{\lambda s^2}\Phi(s),\quad
 Z_\lambda=\int_{\mathbb R}W_\lambda(s)\,ds,\quad
 F_\lambda(z)=Z_\lambda^{-1}\int_{\mathbb R}W_\lambda(s)e^{izs}\,ds,
 \qquad 0\le\lambda\le\tfrac12.
\]

The normalized field obeys
`partial_lambda F = -F_zz - m_2(lambda) F`. Its zeros agree with the
unnormalized Newman field, whose equation is `partial_lambda H=-H_zz`.
The direct-realization laboratory clock in investigations-5 runs in the
opposite direction; import its covariance identities with that conversion.
A Jacobi approximation `G_(N,lambda)=(exp(izJ_N(lambda)))_00` remains an
optional provider. Its eigenvalues are source quadrature nodes, not zeros
of F; increasing N changes resolution, not physical heat time. G_N has
its [actual physical residual][defect], not the exact H heat equation.

On a conjugation-invariant contour (such as the existing circle centered
on the real axis), with a paid collar and exactly two enclosed F zeros
counted with multiplicity, put

\[
 c=(z_1+z_2)/2,\qquad D=((z_1-z_2)/2)^2,\qquad
 F_\lambda(z)=((z-c)^2-D)A_\lambda(z).
\]

The deflated factor A is nonvanishing on the required neighborhood.
Conjugation makes c,D real: positive D is a real separated pair, negative
D a conjugate pair, and zero D a double. The counted tube does not assume
D>0 throughout the unknown earlier interval or nonzero individual slopes.
The algebraic squared Vandermonde is exactly 4D; its modulus square is
4|D| and loses the real/conjugate distinction. Higher clusters require
more symmetric coefficients; one discriminant does not determine them.

## Existing transport identity and its quantitative consumer

Write h=A_z/A and

\[
 K=\frac{h(c+\sqrt D)-h(c-\sqrt D)}{2\sqrt D},\quad M=-K,
 \qquad D'=2-4MD.
\]

The divided difference extends to K=h_z(c) at D=0. On `[u,v]`, set

\[
 W(t)=\exp\!\left(-4\int_t^vM(s)\,ds\right),\qquad
 W(u)D(u)=D(v)-2\int_u^vW(t)\,dt.
\]

An independent incoming lower bound L_v and complete upper cost B with
`L_v>B` suffice for positive D on the interval; equality permits a real
double at the left endpoint. This known conditional implication is stated
once, not counted as a new positivity result. Bounded M or favorable sign
alone need not pay it. With M>=kappa>=0 a sufficient cost is
`B_kappa(Delta)=(1-exp(-4 kappa Delta))/(2 kappa)`, with `B_0=2 Delta`.

[Discussion11][b11] explains why 0.59 was a convenient sufficient number
for one anchor and Delta=0.1, not a universal critical constant. For a
frozen length scale ell at a chosen height, the variables
`D_hat=D/ell^2`, `M_hat=ell^2 M` and `tau=(lambda-u)/ell^2` obey the same
law. B07 must specify how its count/distance estimate, collar, error and
useful margin depend on height and ell from the start. A vanishing but
proved sufficient margin is allowed; a fixed physical 0.59 is not a
height objective. Moving scales require their derivative terms.

## Available information and acquisition obligations

| Input | Established scope and remaining obligation |
| --- | --- |
| Pair calculus and coordinate transfer | [Note04][coords] supplies conditional contour/coordinate payments without an inverse internal gap. Geometry, count, log branch, buffer and incoming anchor still need independent acquisition on each proposed domain. |
| Jacobi/source estimates | [GT Note03][timeproof] extends the parent's stated signed phase estimates uniformly to physical time [0,1/2]. Coefficient bounds do not supply actual coefficients or model zero counts. Pay coordinate changes separately from transfers at common arguments. Give each acquired coefficient also to the next-head/direct comparator. |
| Conditional fixed-event analysis | [Synthesis11][critical] gives signed critical-scale compensation and curvature response conditional on a stipulated event. It acquires no canonical event or exclusion. |
| Local canonical benchmark | [Synthesis16][s16] certifies one pair tube near a=14010.1 on [0,0.1]. The direct endpoint result is tighter and cheaper under the same paid geometry; it also gives qualitative forward-slab reality through the pair law. |
| Exterior sign and count interface | [Note21][s21] groups the order-one divisor under strip and separation hypotheses. [Notes27][s27] and [30][s30] supply sharp weights and lower counts from moving boundaries. The hypotheses and complete remainder must be paid on a new height-dependent tube. |
| Latest finite acquisition | [Synthesis32][s32], accepted by [Assessment13][a13], obtains at least one real occurrence in each of 176 disjoint affine brackets on every slice and M>0.5937558081007126288 using 512-cell target coordinates. No singleton count, simplicity or persistent label is assumed. Target D>0 was already paid; this does not establish a new reality region or a height law. |
| General exterior environment | A quantitative relation between the close pair and its exterior population is open. Neither global mean counts nor source identification supplies the required conditioned local estimate. |

## Correlation and collective routes to compare

B07 compares at most two concrete approaches in one decision pass, using
[Discussion12's source map][b12]:

1. **A joint count/distance or signed-field estimate for the selected
   pair.** Retain the actual relation between c,D and its exterior. A real
   exterior root r contributes `1/((r-c)^2-D)` to M. The finite factorial
   identity in [OG Advisory10 section 4][og10] contracts a three-zero
   measure with this selected-pair kernel. A complete three-point profile
   is not mandatory if the consumed weighted expression can be bounded.
2. **A collective signed source or cluster-energy estimate for the same
   consumer.** Retain cancellations before bounding separate sectors.
   [Direct source covariance][direct], [inserted-ensemble Ward identities][ward]
   and [deterministic Vandermonde/Hessian comparisons][clock] provide
   different interfaces, not interchangeable positivity theorems. Select
   the actual observable and source estimate before assigning execution.

The [OC diagnosis][oc14] separates source probabilities from zero laws.
Its [full marked-pair time bound][oc17], accepted [within internal scope][ocreview],
works at fixed finite height and positive blur through multiple events.
Its initial arithmetic profile and a useful shrinking-resolution margin
remain unacquired. Preserve the common center, both imaginary marks and
multiplicity labels. A conditional density ratio requires a valid measure,
disintegration and normalization; isolation adds a condition on the rest
of the divisor. An average needs a quantitative visibility argument to
exclude every exception. Fixed positive smoothing error does not control
a singular kernel at arbitrarily small separation.

The [positive source-node ensemble][ensemble] keeps its signed insertion;
its order is not zero multiplicity. The [order-four monotonicity stop][signed]
and fixed-polynomial Ward nonclosure exclude only those specified routes.
The late-time clock theorem retains its time regime and exterior force.
The [signed Mellin estimate][signedgain] improved an averaged window
exponent from 17/72 to 17/81; its recorded proof/checking scope and absence
of an every-center bound remain. These are useful precedents, not imported
solutions to the present count/distance problem.

## B07/B08 continuation, 17 November 2026

[Decision15](../brainstorm/notes/15_VCD_GT_B07_NEAR_FAR_COUNT_DECISION_20261117.md)
selects the uniform complete-divisor far-field main term, keeping every
nearby group signed. [Source-use05](../references/05_VCD_GT_UNIFORM_COUNT_SOURCE_USE_20261117.md)
checks the cumulative real-part count in Polymath Theorem1.5(iv); this
input has no exp(C/t) onset. [Note33](../notes/33_VCD_GT_E12_UNIFORM_SIGNED_FAR_EXTERIOR_20261117.md)
pays its time-zero endpoint and gives T_R=log(c/(4π))/(2πR) with the
specified discrepancy, kernel and remote errors. At R=√L, L=log(c/(4π)),
its normalized contribution at ℓ=1/L is 1/(2πL^(3/2))+O(L^−2).
This supplies a uniform far-tail component; the full near sum is unpaid.

[Decision16](../brainstorm/notes/16_VCD_GT_B08_IDENTICAL_COUNT_SCOPE_DECISION_20261117.md)
and [Note34](../notes/34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md)
compare two real even order-one fixed-slice fields with identical horizontal
counts, width one and the same microscopic target collar, but normalized
interaction limits 1/2 and −1/16. They change the theta source and do not
supply a common physical-time tube. This tests the reduced count-only
information class, not source-specific or dynamic estimates. The sole
register owns current assessment and successor status.

## Source-based near-interaction estimates, 17 November 2026

[Notes37–39](../notes/39_VCD_GT_B09_B10_SOURCE_ESTIMATE_SYNTHESIS_20261117.md)
contract the inherited canonical transverse moment/density against the
actual exterior correction. With ell=1/log T and exclusion radius a ell,
the center mean is C/a^3 versus the equally averaged count-only C0/a.
The exact radial comparison includes both D signs. Under the independently
paid isolated-pair geometry, negative-q incidence and pair packing give
N{S_R<0}, N{M<0} <= C_b T log(T) exp(-2ba/3), fixed 0<b<1/2, uniformly
for 0<=t<=1/2. The general large-Xi count is O(T log(T)/(a^4 h)).
The proof notes state all height, radius and pair-size restrictions.

These count exceptions; they do not prove an individual incoming margin
or full signed-cost bound. The independently required growing collar is
not acquired. Note34's controls preserve both aggregate source estimates
on their fixed slices, so source naming alone does not distinguish their
bad selected center. The complementary [Note36](../notes/36_VCD_GT_E16_COMPLETE_SOURCE_PHASE_ALLOWANCE_20261117.md)
proves that even the optimal favorable-phase-only lower allowance has a
negative limit; it does not prove negative actual curvature. E18 accepts
this batch within scope, with shared-premise internal review. B11 then
selected the common-time inputs below; no numerical scan or larger-cluster
work followed automatically.

## Fixed-collar common-time gains, 17 November 2026

[Synthesis42](../notes/42_VCD_GT_B11_FIXED_COLLAR_SYNTHESIS_20261117.md)
integrates the accepted E20/E21 proofs. At fixed a and fixed physical
duration, retained conjugate dissipation and source second/third moments
give negative-pair time occupation O(T/log T) with explicit boundary cost.
This saves two logarithms relative to integrating the old slice allowance.
The exact complete interaction law M'=2M²-12S2-16DS3 gives an interior
normalized lower bound -O(sqrt(log T)) instead of -O(log T), conditional
on the same independently paid tube lasting through a microscopic buffer.
The integrated transport allowance improves but still diverges.

Both D signs and doubles are included. Occupation plus the paid modulus
still fails to exclude one exception; neither negative visibility nor a
long tube is acquired from a snapshot. The equally informed direct method
gets the same estimates. E22's separate internal assessment accepts within
scope without required correction; source premises remain shared. The
earlier B12 next-action route is now assigned to the
[Gaussian/resolvent child continuation](../01_gaussian_resolvent_hierarchy/notes/01_VCD_GT_GR_SETUP_CONTINUATION_20261117.md).
The intended consumer remains a concrete sign-sensitive forcing estimate;
parent B12 is unactivated, with no all-pair sign claimed.

## Height, time and higher-multiplicity obligations

The width-one strip alone does not give the same remainder sign in
shrinking windows. For exterior coordinate x+iy relative to c, a conjugate
pair contributes twice

\[
 \frac{x^2-y^2-D}{(x^2-y^2-D)^2+4x^2y^2}.
\]

Thus nearby nonreal groups require transverse/separation information or a
joint signed estimate; they cannot silently be dropped as favorable.
Contour membership changes and loss of isolation need their own treatment.

The inherited Polymath v2 Theorem 1.5(i)–(ii), with [checked source records][polycatalog]
and [Discussion11][b11], gives eventual real/simple localized high zeros
at positive time with onset of shape exp(C/t). A fixed b>0 gives a common
finite exceptional range for b<=t<=1/2. The existing [positive-threshold
analysis, section 3][finiteevent] and [finite-collision proposition][collisionman]
therefore reduce Lambda=T>0 to a finite real multiple zero at T. Its
multiplicity is at least two, not necessarily two, and the range worsens
as T tends to zero. A double-only theorem needs a higher-multiplicity
extension or an independently justified reduction. Rodgers–Tao's
negative-threshold estimates do not transfer by relabeling time.

A pair theorem should track its constants and dependence on height, time,
conditioning and separation before a larger-cluster extension is selected.
For larger clusters retain symmetric coefficients, internal interactions
and complete exterior coupling. Neither infinitely many tiny descent steps
nor density-one information establishes full time-zero reality by itself.

## Classification and collision controls

Use [controls12][controls], [Note21's premise screen][s21], [Note30's screen][s30]
and [Discussions11–12][b11]. The identities are generic; the desired new
result is an independently paid quantitative estimate. Each selected
candidate must state the failed, satisfied or untested premises for the
relevant controls, rather than relying only on the phrase 'actual theta'.

| Control family | Existing screen and obligation for the new estimate |
| --- | --- |
| Quadratic and even quartic heat controls | Favorable sign or bounded interaction does not pay passage; additional exterior real-count premises fail in the stated examples. |
| Reflected super-Gaussian/nonzero Gaussian-factor classes | The order-at-most-one premise fails in the recorded screen; source positivity/reflection alone do not suffice. |
| Specified weighted-square, finite-source/score and finite-prime endpoint-defective classes | Complete reflection/source data and the global finite-strip premise fail as recorded. Matched finite data alone do not discriminate. |
| Euler-factor translates and damped smooth/positive-primitive controls | Generic flow/order can survive; required local geometry, strip where applicable, counts and quantitative joint inequality remain untested unless separately evaluated. |
| Fixed-event/finite-profile threshold and RH-conditional endpoint controls | Preserve their separate premises and quantifiers. Finite profiles do not control the jet; escaping time-zero doubles cannot be used to demand endpoint simplicity. |
| Changed observation kernels and abstract profile relaxations | Fail the full cosine/Newman or actual-divisor premise, respectively; they are not physical theta collisions. |

No new control certificate was run for this planning revision. A future
numerical screen needs a frozen finite question, and a documentary premise
screen must not be reported as a numerical test of an unproved inequality.

## Success, comparison and current routing

A gain can be a proved exterior count/distance allowance, a signed
interaction or integrated-cost bound, a larger valid range or useful
height rate, or a precise obstruction for a specified information class.
New notation, an unacquired favorable margin and repetitions of the known
pair at higher precision are not main milestones. The [separate-bounds
pattern][a12] and [known-region pattern][a11] apply.

The direct route receives identical geometry, coefficients, source values
and any newly proved exterior estimate. Its contour discriminant does not
require individual root slopes. The pilot's 65 versus 196673 evaluations
are a conditional local implementation comparison, not an end-to-end
complexity theorem. A structural theorem can be valuable without beating
that local runtime. [Discussion11][b11] records the full comparison.

The [plan][plan] fixes B07 and conditional E12–E14, followed by B08 only
when evidence identifies the next question. A research prompt authorizes
many connected in-scope B/E steps; helper limits constrain individual
requests, not session length. The [register][progress] alone owns live
status. [Reference ownership][refs] retains inherited article records;
[setup E11][request] and its assessment record documentation, not a new
mathematical result. The existing manuscript and frozen scientific returns
remain at their current status.

[continuation]: ../brainstorm/notes/14_VCD_GT_CORRELATION_HEIGHT_CONTINUATION_20261117.md
[plan]: ../research-plan/01_VCD_GT_RESEARCH_PLAN_20261116.md
[progress]: ../research-progress/01_VCD_GT_RESEARCH_PROGRESS_20261116.md
[b10]: ../brainstorm/notes/10_VCD_GT_PROGRESS_DISCUSSION_20261117.md
[b11]: ../brainstorm/notes/11_VCD_GT_THRESHOLD_AND_HEIGHT_STRATEGY_DISCUSSION_20261117.md
[b12]: ../brainstorm/notes/12_VCD_GT_CORRELATION_PREDECESSORS_AND_DOUBLE_CLUSTER_DISCUSSION_20261117.md
[b13]: ../brainstorm/notes/13_VCD_GT_PLANNING_REVISION_RECOMMENDATION_20261117.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[geometry]: ../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[coeff]: ../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[parent]: ../../README.md
[parentregister]: ../../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md
[sibling2]: ../../02_degree_nonreality_contraction/README.md
[sibling3]: ../../03_multiscale_collision_bounds/README.md
[defect]: ../notes/05_VCD_GT_E03_PHYSICAL_MODEL_DEFECT_20261116.md
[coords]: ../notes/04_VCD_GT_E02_COMPLETE_COORDINATE_TRANSFER_20261116.md
[timeproof]: ../notes/03_VCD_GT_E01_PHYSICAL_TIME_SIGNED_ERROR_20261116.md
[critical]: ../notes/11_VCD_GT_CRITICAL_SCALE_SYNTHESIS_AND_CONTINUATION_20261116.md
[s16]: ../notes/16_VCD_GT_CANONICAL_SIGNED_GAP_SYNTHESIS_20261116.md
[s21]: ../notes/21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md
[s27]: ../notes/27_VCD_GT_E03_SHARP_EXTERIOR_MASS_20261116.md
[s30]: ../notes/30_VCD_GT_E03_REAL_BRACKETS_AND_MOVING_BOUNDARIES_20261116.md
[s32]: ../notes/32_VCD_GT_EXTERIOR_MASS_SYNTHESIS_AND_CONTINUATION_20261116.md
[a13]: ../reviews/13_VCD_GT_EXTERIOR_MASS_CERTIFICATE_ASSESSMENT_20261116.md
[og10]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/01_green_potential_resolvent/brainstorm/notes/10_TND_OG_COLLISION_DYNAMICS_AND_PARALLEL_PROBES_20261108.md
[direct]: ../../../../investigations-5/08_theta_observables_newman_dynamics/01_direct_newman_realization/notes/04_TND_D_B02_COLLISION_DYNAMICS_RECONNAISSANCE_20261106.md
[ward]: ../../../../investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/04_biorthogonal_ensembles/notes/01_INSERTED_ENSEMBLE_IDENTITY_RETURN_20261101.md
[clock]: ../../../../investigations-5/01_heat_density_asymptotics/notes/12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md
[oc14]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/notes/14_TND_OC_B08_ARITHMETIC_MARGINAL_COLLISION_FRICTION_20261108.md
[oc17]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/notes/17_TND_OC_E10_R1_FULL_MARKED_PAIR_EVOLUTION_PROOF_20261108.md
[ocreview]: ../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/02_localized_zero_correlations/reviews/14_TND_OC_E12_R1_FULL_MARKED_PAIR_CLAIM_ASSESSMENT_20261108.md
[ensemble]: ../../../../investigations-5/07_positive_theta_primitives/01_jensen/01_mellin_curvature/04_biorthogonal_ensembles/README.md
[signed]: ../../../../investigations-5/07_positive_theta_primitives/01_jensen/02_signed_averaging/notes/01_INITIAL_BRANCH_EVALUATION_20261101.md
[signedgain]: ../../../../investigations-5/09_green_potentials_newman_flow/01_riemann_siegel_evolution/notes/29_GNP_RS_B10_SIGNED_MELLIN_MEAN_ESTIMATE_20261112.md
[polycatalog]: ../../../../investigations-5/02_heat_flow_rh_applications/references/sources.json
[finiteevent]: ../../../../investigations-5/02_heat_flow_rh_applications/notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md
[collisionman]: ../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex
[a11]: ../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[refs]: ../references/README.md
[request]: ../research-progress/handoffs/VCD-GT-E11-r1.md
