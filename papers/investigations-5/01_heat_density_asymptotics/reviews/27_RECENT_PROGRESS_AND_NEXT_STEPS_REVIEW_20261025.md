# Recent heat-density progress and the next useful theorem

25 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **gpt-6-astra (Codex), actual effort xhigh**,
verified from the current turn metadata. Chat **0016**, thread
`01a1738b-7f79-7091-a6cc-ae3fd6ee2fb2`.

**Assessment:** the investigation has made substantive quantitative progress
from endpoint formulas to a compatible spatial approximation on a short
finite-time slab. Sol completed HDA-18-AN01 and then AN02–AN03. The next
bounded task is the already prepared AN04. I found no blocking error in the
recent derivations inspected here. This is a focused separate-chat LLM
review, cross-model for Sol's Notes 43–45, with shared antecedent premises.
It is not a complete audit of every manuscript proof, numerical certification,
or independent specialist review; HDA-20 is not fulfilled by this review.

The [input manifest](27_RECENT_PROGRESS_REVIEW_INPUTS_20261025.json) pins the
reviewed versions. All 18 TeX sources and the existing PDF match the current
78-page build record. No new PDF was built or visually reviewed. The source
inputs to Notes 43–45 match their manifests; each frozen request remains an
unchanged byte prefix followed by its return. Numerical code and records
were inspected, not executed. The manuscript and mathematical source notes
were left unchanged.

Read this assessment with the [result index](../../../../result-summaries/README.md),
[heat-geometry cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid index](../../../../avoid/README.md). In particular,
[avoid 01](../../../../avoid/01_restating_the_target.md) classifies this as
quantitative approximation work, [avoid 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md)
limits the negative conclusions, and
[avoid 12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
explains why the signed cancellations and complete terms matter.

## What the manuscript establishes at high level

The object is the unnormalized, regularized density of the canonical theta
heat field, averaged over a fixed spatial window. The density is accompanied
by a physical potential, current, regulator corrections and an actual signed
gradient covariance. Preserving the absolute scale is essential: the work is
not merely matching the appearance of rescaled peak plots.

The main results are written approximation theorems with stated domains:

- At large negative time, a Gaussian field controls the full real-height
  axis. Under the common adaptive regulator, the density error is
  O(T^-2), current error O(T^-5/2), and direct density-time and covariance
  errors O(T^-3); the covariance-Laplacian error is O(T^-4).
- At large positive time, the full gamma-saddle field controls every real
  height. Static density and potential-jet errors are
  O(t^-1/2 log^-2(2+t)); the current, direct time, forcing/source and actual
  covariance errors are O(t^-1/2). Its nonzero heat residual is retained.
  A sharper explicit clock describes the buffered inner window, including
  lattice phase and transport.
- On compact full buffers, finite positive sources can approximate the
  canonical field. Weak identities transfer field errors of orders zero
  and two to the complete filtered system; a time-only blend has a paid
  residual. Compactness supplies the positive regulator floor used by these
  transfer coefficients; it supplies no global floor over unbounded heights.

The manuscript's endpoint and transfer claims are stronger than static
shape matching because they estimate the current, direct time terms and
actual covariance separately. They do not derive an autonomous equation
for density alone, solve a stable reduced boundary-value problem, or prove
RH/simplicity. For variable regulator, density is not simply the Laplacian
of potential: the curvature correction is load-bearing.

The integrated manuscript ends at Notes 34–37 with Note 38's scoped
interpretation. Its statements that spatial compatibility remains unpaid
are historical to that version. Notes 42–45 supply a partial resolution,
not the full all-time assembly. The current progress register is ahead of
the investigation README's opening summary and the manuscript coverage table.

## What Notes 42–45 add

| Source | Actual gain | Remaining scope limit |
| --- | --- | --- |
| [Note 42](../notes/42_GAP_LOCALIZED_SPATIAL_DEFECTS_20261024.md) | Place a smooth spatial transition in a zero-free model gap. Derive the nonholomorphic and heat defects exactly and bound them using the field floor. | Local transition estimates on a fixed after-switch slab, not yet a full-support comparison. |
| [Note 43](../notes/43_FULL_SUPPORT_FIXED_GAP_TRANSFER_20261024.md) | Complete the core/exterior/transition comparison on every full averaging support, including actual covariance and direct time/source/curvature rows. | Finite source and geometry requirements; fixed slab width O(1/log X), constants initially uninstantiated. |
| [Note 44](../notes/44_FINITE_INPUTS_CLIPPED_SOURCE_AND_OUTER_GATE_20261024.md) | Give explicit core/cutoff/regulator formulas and a positive clipped cubic source with a constructive size bound. | A sufficient finite construction, not an executed or affordable source. The outer field requirement was then unpaid. |
| [Note 45](../notes/45_EFFECTIVE_FULL_BUFFER_OUTER_FIELD_20261025.md) | Supply explicit full-buffer field and three-jet constants on 95<=t<=97, paying the previous outer field requirement. | Enormous sufficient onsets; remaining exterior observable constants and complete budgets still unpaid. |

The main mechanism in Note 42 is sound in the inspected scope. On the
transition, |F| is bounded below by a fixed fraction of the carrier sum A.
Thus the new terms can be bounded relative to F without division by a
vanishing global regulator. This is why allowing a carefully controlled
nonholomorphic approximant becomes useful. The generalized density remains
an approximation observable; no zero-count interpretation of that
nonholomorphic field follows.

Note 43 closes the requested local-to-full-support gap. Its primitive
integrals are split into nonnegative core/band/exterior contributions before
weak differentiation. It does not apply a whole-support signed estimate to
a truncated piece. The exterior signed heat term has its own smooth test
partition and both cutoff derivatives are paid. The covariance is formed
from the joined field's signed stress and its actual filtered mean products.
The largest full allowance remains

    O_J(log^3 X/X^2 + log^2 X/X^3),

with polynomial-exponential terms retained. The core source accuracy is
chosen to satisfy the finite coefficient table. This is a genuine decreasing
error estimate under its premises, not a small-residual propagation claim.

Note 44's positive clipping is a useful improvement. Pointwise projection
f=max(0,p) cannot increase error against the nonnegative complete source.
It preserves the cubic fourth-order remainder, unlike a second-order linear
fallback. The source's corners do not prevent its compact integral from
being entire and exactly heat-evolving. Interpolation, omitted modes, nodal
arithmetic and complete tail total 29 epsilon/64 for each of four jets;
later evaluation/filter arithmetic is still separate. The sufficient cell
count has the form

    M = epsilon^(-1/4) exp(O(log^2 log(1/epsilon))).

This is an upper bound for that constructor, not a lower bound for all
positive approximations. The older sampled Hermite allowance success also
remains a diagnostic, not a continuous finite-core certificate.

Note 45 turns an eventual outer comparison into an explicit one:

    |H-P| <= 12000 A/x^2,
    95<=t<=97, |Im z|<=5, x>=2^2048.

Full analytic circles of radius 1/[4log(2+x)] give derivatives through
three on the smaller strip, with constants 12000, 384000, 3072000 and
36864000 at x>=2^2049. At X>=2^2050 the gap field debit is at most
1179648000/X^2. The local field-floor requirement therefore has a stated
finite sufficient regime. That fact does not supply an evaluated gap
index, a source realization, or the entire observable ledger.

## Focused mathematical checks and qualifications

I inspected the defect identities and local envelopes, the primitive/time/
covariance/partition assembly, the positive-source construction, and the
explicit outer proof. The supporting manuscript reading concentrated on
normalization, exact adaptive equations, endpoint theorem quantifiers,
compact transfer, full-saddle comparison, signed-pole covariance and residual
rows. This is deliberately a statement of review coverage, not a claim of
having independently reproved the full manuscript.

The full-support assembly preserves the terms most likely to be lost:
TC and TC_t, Xi, TJ, both component and join heat residuals, DE and DB,
both regulator-curvature derivatives, and the difference of the actual
filtered mean products. The use of a fixed central cap plus the exterior
O(log X) gradient cap in FT13 is necessary for its decay; substituting the
crude growing-core potential bound would change the conclusion.

For Note 45, the checked chain includes the contraction branch, Gaussian
remainder without an exp(|cubic error|) loss, the left horizontal segment,
connectors, bounded middle, every arithmetic mode, and Cauchy-circle carrier
comparability. The cancellation of the zeta pole is needed for the middle.
I checked the cited classical inputs against the official
[DLMF complex digamma remainder](https://dlmf.nist.gov/5.11#ii),
[imaginary digamma series](https://dlmf.nist.gov/5.7.E8),
[beta integral](https://dlmf.nist.gov/5.12.E1), and
[Euler summation formula](https://dlmf.nist.gov/25.2.E8).
Their relevant domain restrictions are respected in the inspected argument.
This source check does not externally certify the new estimates.

The six polynomial cases/76 exact assertions and the later five/six scalar
checks have the narrow scopes recorded by Sol. They are useful algebra and
constant checks; they do not prove the collar comparison, global time
coverage or numerical affordability. I did not rerun them, consistent with
the repository's Sol numerical-work assignment.

The huge outer onset and source cost are substantial practical limitations.
The explicit core floor in FI12 falls as exp(-R_c^2/452). With the coarse
transfer table, source tolerances can consequently fall as exp(-a X^2).
FI22 then supplies a construction with exponentially large cell count in
X^2. The formula is mathematically finite; it gives no realistic executable
core at the present outer cutoff. It also gives no impossibility theorem
for better local transfer or other source representations.

## Recommended sequence

1. **Analysis — Sol: complete the existing [HDA-18-AN04 r1](../research-progress/handoffs/HDA-18-AN04.md).**
   Make the model-gap selection, root pairing, slope/unit, signed-pole,
   weighted-regulator and exterior signed-source constants explicit. Close
   one declared full observable budget, including the actual covariance,
   using Note 44's finite source tolerances. The output should be one
   theorem with a finite sufficient onset and row targets, or one exact
   unpaid inequality. Another list of unspecified constants is not this
   deliverable. The huge onset need not be optimized to complete this
   bounded analytical step. No numerical source construction is implied.

2. **Analysis — Sol initially: cover one time interval of fixed positive
   width after the switch.** The next mathematical target after AN04 is
   the same full tuple throughout, for example, [95,97], with a controlled
   spatial assembly. The current fixed-gap construction supplies only
   shrinking slabs: GS2 imposes an O(1/log X) upper restriction, and FI6
   can be more conservative. Choose a moving model gap or a finite cover of overlapping fixed-gap
   slabs and prove the temporal compatibility. For a moving cutoff the
   exact additional heat term is lambda_t(P-G); B_t, (B_z)_t and any
   moving test/support terms must also be paid. Note 34's holomorphic time
   theorem cannot simply be applied to already nonholomorphic spatial
   blends. This recommendation is a new proof target, not an asserted
   extension of Note 43. Escalate only a named estimate that resists a
   focused Sol attempt.

3. **Analysis — Sol: improve the conditioning of the growing core.**
   Before attempting a large source construction, test whether local
   amplitude bounds and paired-root collar estimates can confine use of
   the worst regulator floor to a fixed central region. The consumer is
   FT20/FI15b: show a quantitatively less stringent permitted source error
   at the same full observable targets, with actual covariance and the
   time/source rows retained. This is a question about better sufficient
   estimates, not a claim that the exponential cost has already been
   removed. The separate frozen-point arithmetic/filter certificate remains
   a useful bounded numerical task for Sol; it does not by itself close
   the growing core or global join.

4. **Analysis/manuscript — Sol: integrate the reviewed spatial result
   after the complete budget is available.** Add a compact spatial-join
   section with the defect equations, full-support theorem, source gate,
   explicit outer input and limits. Update the model/domain table and
   remaining-work discussion together. Keep most finite-constant detail
   in linked notes or an appendix. Refresh the README's latest-status
   pointer. Preserve the all-time/crossover and independent-review gaps.

Crossing t=64 and attaching both infinite-time endpoint regimes follow as
separate global-coverage obligations. The compact-time outer theorem already
covers the switch, but Note 42's exponentially small regulator-to-field
ratio is not uniform there. A spatial join crossing that layer needs a new
uniform payment; the fixed after-switch argument cannot be carried across
unchanged. Direct time averaging can be considered once one full time
support is covered with paid terms, not as a substitute for that coverage.

The crossover/correlation program HDA-21 is worthwhile as a secondary
analytical specification. Its known jump is induced by the chosen regulator;
64 is not an intrinsic singular time of H. A meaningful further result needs
a specified separated-point connected correlation and perturbation/response,
with differentiated error bounds. Neither the existing signed Q nor the
O(1) absolute layer approximation supplies a divergence of correlation
length or a closed statistical-mechanical model.

## Control screen and disposition

Generic heat/defect identities and positive-source approximation permit
collisions, including heat polynomials. A selected gap floor fails if the
transition crosses a zero; another zero-free gap does not exclude collisions
elsewhere. Euler-factor controls lack the unchanged completion; weighted-square
and finite-prime controls lack the full canonical coefficient/reflection
input; reflected and smooth positive-primitive controls lack the exact
canonical gamma/source identity; atomic/polynomial controls lack the smooth
canonical source. Those are failures of premises used by the theta-specific
comparison, not claims that every control fails each derived inequality.
No new sign criterion or global exclusion is proposed.

AN01–AN03 are closed at their recorded analytical scopes; AN04 is prepared
and unexecuted. HDA-17 remains Partial, HDA-18 Gated and HDA-20 unfulfilled.
This review records an assessment, not a new research milestone, and creates
no snapshot or manuscript revision.

**Next concrete deliverable and owner: Analysis — Sol, AN04 r1.**
Pasteable prompt: “Complete HDA-18-AN04 r1 using Notes 43–45 and Review 27.
Return one explicit full-support observable budget on the stated fixed-gap
slab, including all covariance, curvature, heat and partition terms, with
finite source tolerances or the first unpaid inequality. Preserve the
analytical-only limits and distinguish finite existence from affordable
execution. Do not begin a theta sweep or an all-time extension in this packet.”
