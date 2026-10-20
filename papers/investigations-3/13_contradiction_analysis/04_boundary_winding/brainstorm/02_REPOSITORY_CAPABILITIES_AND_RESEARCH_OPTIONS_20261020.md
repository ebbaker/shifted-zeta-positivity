# Repository capabilities for threshold signed arithmetic

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
actual reasoning effort **max**, verified from recorded turn metadata.

**The repository contains substantial machinery for this problem, but I
found no existing estimate that supplies the missing opposing sign. The
strongest combination is complete arithmetic approximation, correlated
analytic error control, and direct theta evaluation. A second possibility
is to combine actual imaginary-axis data with an optimized bound on the
remaining zeros.**

This survey supplements the [results synthesis][synthesis] and is paired
with a [targeted literature review][literature]. It screens all 17
[result-summary clusters][results], then follows the most relevant
capabilities to their notes, code and internal reviews. It is not a fresh
audit of every proof or a replay of the numerical certificates. The
source checkout was at `574b658061c5144a78d44a805fe2c116d86f9397`;
the existing synthesis and chat-history changes were also present.
No research task is activated or marked complete by this survey.

The [active program][program], [progress register][progress] and
[patterns to avoid][avoid] govern the assessment, particularly
[target classification][a01], [control screening][a02],
[scoped exclusions][a07], and [preserving signed cancellation][a12].
Repository proof and certificate descriptions below retain their
source status. The cited reviews are internal LLM reviews, without
independent specialist human validation.

## The missing estimate

At a hypothetical ordinary double threshold event of the unchanged theta
flow, \(T=\Lambda>0\), \(a>0\), put \(h_j=\partial_x^jH(T,a)\).
The event conditions are \(h_0=h_1=0\), \(h_2\ne0\). For a proved
\(0<L\le L_2(a)\), the existing necessary inequality is

\[
Q_L=2h_3^2-3h_2h_4-18Lh_2^2>0.
\]

The desired independent arithmetic estimate is \(Q_L\le0\), or a
strictly improved upper bound with its remaining deficit quantified.
These are unknown event parameters, not an observed theta collision.
A global exclusion of every positive threshold event would settle RH;
the useful immediate targets are restricted estimates.

The latest round already rules out the selected homogeneous
norm-plus-finite-Gram relaxation. Positivity of the multiplier does not
repair the selected information loss. Finite profile samples can also
remain fixed along constructed colliding families with unbounded \(S_2\).
The [synthesis][synthesis] distinguishes the premises of these
obstructions. None proves that every use of actual theta coefficients,
actual theta profile values, or an independently paid gap must fail.

## Capabilities closest to the target

| Capability | Established resource | What a new application must supply |
| --- | --- | --- |
| Cancellation through a moving arithmetic cutoff | Project 11 S03: complete corrected residual increments, including transitions and infinite tails | A bound for the retained physical fourth jet, with the same phase, source and cutoff |
| Correlated analytic errors | Project 11 S02: a joint real Schur description of residual derivatives through order two | A complete order-four extension and an event-conditioned physical consumer |
| Direct complete-source evaluation | Project 11 shifted contour evaluator, cell propagation and outward error records | A validated fourth-order contract on a useful domain and comparison against the strongest direct method |
| Counts of distant zeros | Project 06: explicit unit-window counts, with multiplicity | A kernel-specific tail budget; nearby spacing remains a separate problem |
| Exact coefficient information | Investigation 22: coefficient rigidity, recurrence-defect identities and weighted stability | A signed observation that benefits from that information |
| Signed averages and exact evolution identities | Investigations 21–22: weighted Laguerre averages and complete-source heat identities | A paid conversion from an average or nonlocal identity to the required local sign |

### 1. Arithmetic cancellation is already available

[S03 Note 10][uar04] proves, from its named analytic inputs and with
outward checks of constants, a complete ordinary piecewise corrected
residual-increment bound

\[
|I_t(v_0,v)|<3.246e^{-13/(16t)}<2.846\times10^{-7}
\]

for every prefix of
\([4\pi e^{1/t},4\pi e^{2/t}]\), \(0<t\le1/20\).
The entering arithmetic mode is matched with the changing
Riemann–Siegel edge before taking absolute values. The payment includes
retained signed contributions, gamma/heat corrections, both endpoints
and every cutoff transition. This is considerably more useful than a
small bound on an omitted tail alone.

[Note 13][uar13] rebases the estimate at arbitrary endpoints in that
sector. It also proves qualitative edge and transition extensions on a
fixed positive compact band of \(t\log(x/(4\pi))\), for sufficiently
small \(t\). The latter has no new explicit onset or transferable
numerical constants. [Review 18][uar-review] states these limits
carefully: higher spatial derivatives of the error do not themselves
supply a complete higher-jet physical certificate.

The practical lesson comes from [the matched comparison][uar06]:
on its small paid box, the direct normalized energy bound exceeds
\(0.27778656\), while transported certification gives
\(0.27778628\), at the same dominant acquisition of 44,052 modes per
precision. That bounded transport configuration was stopped. Any reuse
must improve the relevant signed bound, coverage, or cost against the
strongest applicable comparator.

**Use here:** preserve the complete arithmetic model and its phase
correlations while estimating \(h_2h_4\) and \(h_3^2\) together.
The missing result concerns the retained model at an event; further
shrinking an already tiny residual need not help.

### 2. Joint analytic errors are a useful alternative to independent boxes

[S02 Note 03][schur] and its [review][schur-review] retain the dependence
among the first three Taylor coefficients of a real analytic disk map.
This gives complete physical jets through order two and stronger signed
tests than independent coordinate boxes on the same pilot cover.
The complete-source reference nevertheless has the stronger physical
margin. The result is a scoped comparison, not new coverage.

This offers a plausible representation for a new attempt: an arithmetic
approximant plus one shared analytic residual, constrained by the two
event equations. That representation contains an actual source-dependent
center. It differs from maximizing over arbitrary multipliers in a
homogeneous Gram ball. Extending the Schur coefficients to order four,
paying the disk errors, and demonstrating a gain are still work.

There is a useful algebraic simplification for the physical return.
Write \(H=AF\), where \(A\) is a nonzero real positive normalizer near
the real event, and put \(\alpha=(\log A)_x\), \(f_j=\partial_x^jF\).
At the exact event, \(f_0=f_1=0\), and

\[
\frac{Q_L}{A^2}
=2f_3^2-3f_2f_4-18\bigl(L+\alpha_x\bigr)f_2^2. \tag{1}
\]

Indeed \(h_2/A=f_2\), \(h_3/A=f_3+3\alpha f_2\), and
\(h_4/A=f_4+4\alpha f_3+6(\alpha_x+\alpha^2)f_2\);
substitution cancels the mixed \(\alpha f_2f_3\) and
\(\alpha^2f_2^2\) terms. This elementary bookkeeping identity is
included to specify an interface, not claimed as a new signed estimate.
It shows exactly which normalizer curvature must be retained.
An approximate event cannot be substituted for the exact cancellations;
its residual constraints must remain in the enclosure.

### 3. Direct theta evaluation is the benchmark to reuse

The [shifted-evaluator note][evaluator-note] gives a validated interval
evaluator on \([.01,.2]\times[25,45]\), with matched complex tests.
It retains reflected source terms before truncation and separately pays
omitted modes, source tails, quadrature, subsequent arithmetic and
whole-cell Taylor propagation.

The [implementation][evaluator-code] already has a parameterized
component order and derivative-tail loops. Its documented validation
uses components zero through two, midpoint derivatives through 76 and
remainder derivatives through 78. Those high internal orders support
Taylor propagation; they are not an existing fourth-jet certificate.
The required next deliverable is a checked fourth-order output contract,
not merely changing an argument.

Project 11 also records finite noncollision coverage through
\(|x|\le1000\), \(0<t\le.2\), and [an explicit real first-jet
exterior][outer] beginning at \(\exp(20/\epsilon)\) for
\(\epsilon\le t\le1/2\). On its \([.01,.2]\) slab the stated bridge
is \(1001<|x|<e^{2000}\). Thus small-height tests are useful for
validation and matched comparisons, but should not be presented as new
collision exclusions. Real first-jet exclusion also does not provide the
missing final-time complex exterior in a global Newman-bound argument.

### 4. Zero counts can pay distant contributions

[Project 06, round 2][counts] proves in-note from named imports

\[
K_t(X)\le0.9\log(X+2)+6,\qquad
0<t\le1/2,\quad X\ge100000,
\]

where \(K_t(X)\) counts **all complex zeros with multiplicity whose real
parts lie in \((X,X+1]\)**. The reduced cutoff and constants have
same-model checks; the earlier cross-model review applies to the
preceding, weaker theorem, not automatically to this version.

Under the hypothetical all-real threshold assumption, these counts can
bound distant pieces of the deflated inverse-square sum or of a
profile reconstruction. The application would sum explicit kernel
suprema over unit windows, treating the uncovered finite range
separately. No such application-specific bound has been evaluated here.
An upper count allows clustering inside a window and therefore supplies
neither a nearest-neighbor gap nor a curvature floor.

### 5. Coefficient rigidity is a constraint, with a documented sign gap

[Investigation 22][coeff-summary] identifies the exact theta coefficients
from its full addition relations and endpoint normalization.
Its [recurrence study][recurrence] also gives complete physical mode
bounds and weighted defect-to-observation identities. For normalized
nonnegative coefficients, finitely many second-difference conditions
alone have sharply algebraic stability; fixing the first coefficient
as well improves the corresponding remainder to a Gaussian tail.

This is valuable when specifying which coefficient information a finite
relaxation genuinely retains. It could provide error bounds for an
approximation centered at the exact coefficients. It does not sign the
centered observation. The [review][recurrence-review] explains why the
tested current/normalization construction merely returns the unknown
signed observation at its boundary. Repeating that construction with a
different notation would not address \(Q_L\).

### 6. Signed averages may support a nonlocal estimate, but do not localize for free

[Cluster 16][geometry] records sharp weighted lower bounds for Laguerre
averages and positive origin-centered Gaussian averages of the complete
theta expressions. Translation introduces oscillation. [Cluster 14][coeff-summary]
records complete-source correlation identities, including the hierarchy
\((\partial_t+\partial_x^2)\mathcal L_j=2\mathcal L_{j+1}\),
where \(\mathcal L_j=h_{j+1}^2-h_jh_{j+2}\).

These are plausible inputs to a specified nonlocal argument. Neither
an integral lower bound nor the evolution identity gives the required
pointwise fourth-order upper bound. The boundary-winding result that
later local witnesses are absent further requires a proposed witness
to be genuinely nonlocal for the same function.

## A distinct profile experiment worth considering

The most relevant new external method found is
[Bertsimas–Popescu's moment-bound duality][bp]. The following is a
proposed adaptation using the repository's paired-product identity,
not a theorem supplied by that paper or an executed numerical result.

Set \(A=a^2\), \(B_i=b_i^2>0\). Remove the known double pair from
actual imaginary-axis observations:

\[
R_i=\frac{D_T(b_i)}{b_i}-\frac4{A+B_i}
   =\sum_{\rho>0,\ \rho\ne a}\frac{2m_\rho}{\rho^2+B_i}.
\]

The counting measure has infinite mass. Instead use the finite positive
measure
\[
\mu=\sum_{\rho>0,\ \rho\ne a}
       \frac{2m_\rho}{\rho^2+B_0}\,\delta_{\rho^2}.
\]
Then \(\mu([0,\infty))=R_0\) and
\(\int (y+B_0)/(y+B_i)\,d\mu=R_i\).
This converts the actual profile constraints into linear observations
of one finite measure.

For a bounded neighborhood \(I\) of \(A\), seek a rational combination
of those observation functions that majorizes
\((y+B_0)\mathbf1_I(y)/2\) on the entire half-line.
Its integral is an upper bound for the integer number of other positive
zeros in \(I\), with multiplicity. A certified bound strictly below one
would exclude such zeros. Merely bounding the weighted mass by a small
positive number would not do this; the counting weight matters.

If a gap is established, the remaining target is

\[
S_2=\frac1{2a^2}
 +\int\frac{(A+y)(y+B_0)}{(A-y)^2}\,d\mu(y).
\]

A second majorant on the gap complement could give an upper bound.
To contradict BW-08 it must reach \(S_2\le L\); a gap alone is
insufficient. Before a gap, the pole at \(y=A\) prevents this simple
bounded-majorant strategy.

Every profile interval and every event-parameter interval must be paid.
If an observation has error \(\varepsilon_i\), a dual combination with
coefficient \(c_i\) costs at least \(\sum_i|c_i|\varepsilon_i\).
A global majorant and complete observations already include the infinite
tail; a truncated implementation needs an additional tail budget, for
which Project 06 may help. Positive denominators permit polynomial
certificate checks after clearing them. Numerical optimizer output
alone would not establish the majorization.

The [finite-profile obstruction][profiles] is the essential adversarial
test. It fixes constructed vectors, not the actual theta vector, and
its one-sample gap criterion fails against the theta floor. Thus this
proposal must use actual data and must report failure when its feasible
class still contains the colliding controls. There is no promise that
the needed sample accuracy is achievable or that any selected vector
will certify a gap.

## Breadth of the survey and lower-priority resources

| Summary clusters screened | Potential reuse | Limitation for this program |
| --- | --- | --- |
| [01–02: finite Weil positivity][finite] | Exact Schur complements, certified anchors, tail/error ledgers | Different quadratic forms and finite support windows; no established transfer to \(Q_L\) |
| [03–06: strings, positive factors, transfer and physical channels][strings] | Realization and localization techniques; useful scoped obstructions | Critical positivity or the signed mixed pairing remains unproved; positive factors do not supply the full theta sign |
| [07–09: Sonin, characters, detector, prime variance][sonin] | Finite operator comparisons, heat-polynomial controls, conditional strip machinery | Several natural target criteria are RH-equivalent; conductor-family results do not transfer to fixed zeta |
| [10: quasi-RH audits][quasi] | Import and dependency audits, conditional comparison methods | Audited claims and formal comparator replays are not an independently established new strip theorem |
| [11–14: heat flow, controls, local geometry, arithmetic identities][heat] | The main analytic and computational inputs identified above | Their current signs, domains and source distinctions must remain explicit |
| [15: verification infrastructure][verification] | Outward arithmetic, exact rational certificates, source hashes, replay records | Verification format does not prove an unprovided analytic premise |
| [16–17: geometry and stable models][stable] | Signed-average tools and additional model controls | Re-realization does not supply a sign; model exclusions retain their stated classes |

The best next step is a bounded decision between the following contracts.
These are brainstorming options, not amendments to the execution register.

| Candidate | First deliverable | Acceptance or stopping rule |
| --- | --- | --- |
| **A. Fourth-order arithmetic comparison** | One justified source/domain with complete derivatives through four, a shared residual, exact event constraints, and the physical return (1) | Improve the upper bound for \(Q_L\) against a matched direct/reference bound and state the deficit; stop if the useful information collapses to the closed homogeneous relaxation or only an omitted tail improves |
| **B. Actual-profile feasibility test** | A declared event box, complete profile intervals, a gap/count majorant and its sensitivity budget | Certify a count below one and then an \(S_2\) upper bound, or identify precisely why the data cannot support that consumer; stop if only generic floors or constructed profile vectors are used |
| **C. Nonlocal witness** | A relation for the unchanged function outside the proved forward neighborhood, with a specified signed average or boundary term | Continue only when that relation gives a quantitative implication; another local collision identity is insufficient |

I would give A priority because it uses the strongest existing arithmetic
estimates directly. B is a distinct, relatively inexpensive feasibility
question before any large profile-acquisition campaign. Coefficient
stability, zero-count tails and certificate infrastructure support either
where their hypotheses apply.

For A, colliding polynomial/atomic/smooth controls must be processed with
their own approximation and residual data; theta constants cannot be
assigned to them. Weighted-square, finite-prime and reflected controls
fail the unchanged full theta coefficients or the required complete
arithmetic identity. That failure permits an arithmetic distinction but
does not prove the sign. For B, use the controls' own profile vectors and
known neighboring roots: a purported gap certificate that excludes one
of those roots is invalid. No uniform lower bound for \(|h_2|\) is assumed
in either proposal.

[synthesis]: 01_SIGNED_ARITHMETIC_RESULTS_AND_NEXT_QUESTIONS_20261020.md
[literature]: ../reviews/02_TARGETED_LITERATURE_REVIEW_FOR_THRESHOLD_ARITHMETIC_20261020.md
[program]: ../research-overview/02_THRESHOLD_SIGNED_ARITHMETIC_RESEARCH_PROGRAM_20261020.md
[progress]: ../research-progress/02_THRESHOLD_SIGNED_ARITHMETIC_PROGRESS_20261020.md
[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[uar04]: ../../../11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/10_UNIFORM_SIGNED_RESIDUAL_INCREMENT_20261019.md
[uar13]: ../../../11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/13_REBASED_RESIDUAL_AND_COMPACT_SECTOR_EDGE_EXTENSIONS_20261019.md
[uar-review]: ../../../11_arithmetic_collision_rigidity/reviews/18_UAR_ANALYTIC_MANUSCRIPT_AND_GENERALIZATION_REVIEW_20261019.md
[uar06]: ../../../11_arithmetic_collision_rigidity/symmetries/03_normalized_jet_rotation/notes/12_MATCHED_COMPLETE_CONSUMER_AND_COST_COMPARISON_20261019.md
[schur]: ../../../11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md
[schur-review]: ../../../11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/reviews/03_COMPLETE_JET_INTERNAL_REVIEW_20261019.md
[evaluator-note]: ../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/07_SHIFTED_EVALUATOR_AND_COMPLETE_ERROR_BUDGET_20261018.md
[evaluator-code]: ../../../11_arithmetic_collision_rigidity/numerics/certify_shifted_theta_jet.py
[outer]: ../../../11_arithmetic_collision_rigidity/notes/02_updated_research_plan/14_SHARPER_OUTER_EXCLUSION_AND_CONSTANT_DISTANCE_CONTOURS_20261018.md
[counts]: ../../../06_explicit_heat_zero_counts/notes/round-2/01_LOWER_CUTOFF_AND_PAIRED_EXTRACTION_CODEX_20261017.md
[coeff-summary]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[recurrence]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/08_ADJOINT_RECURRENCE_ENDPOINT_EXPERIMENT_20261015.md
[recurrence-review]: ../../../../investigations-2/active/22_theta_manifold_geometry/reviews/08_ADJOINT_RECURRENCE_AND_GEOMETRIC_REVIEW_20261015.md
[geometry]: ../../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[profiles]: ../threshold_routes/08_deflated_jet_hierarchy/notes/05_FINITE_PROFILE_CONDITIONING_OBSTRUCTIONS_20261020.md
[finite]: ../../../../../result-summaries/02_finite_horizon_certificates.md
[strings]: ../../../../../result-summaries/03_shifted_zeta_criteria_and_strings.md
[sonin]: ../../../../../result-summaries/07_sonin_critical_boundary.md
[quasi]: ../../../../../result-summaries/10_quasi_rh_audits_and_amplification.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[verification]: ../../../../../result-summaries/15_verification_infrastructure.md
[stable]: ../../../../../result-summaries/17_constructive_stable_model_obstructions.md
[bp]: https://flora.insead.edu/fichiersti_wp/inseadwp2004/2004-62.pdf
