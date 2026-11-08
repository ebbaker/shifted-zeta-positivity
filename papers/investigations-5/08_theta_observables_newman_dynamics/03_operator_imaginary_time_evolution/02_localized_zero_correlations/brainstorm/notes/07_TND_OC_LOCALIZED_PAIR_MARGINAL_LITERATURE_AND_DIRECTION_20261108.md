# Localized two-zero marginals: literature review and next direction

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Actual current model and effort are
not exposed by authenticated chat0002. This is the author's requested
literature/design update, not a new theorem or an assessment of B02.

## Decision and research objective

Develop the localized **marked two-zero factorial measure** before choosing
a scalar projection:

\[
dA^{(2)}_{\lambda,X,h}
=\sum_{j\ne k}w_{X,h}(x_j)w_{X,h}(x_k)\,
  \delta_{(x_j,y_j,x_k,y_k)},\qquad z_j=x_j+iy_j .
\]

This is the two-particle marginal of a symmetrized finite configuration
measure, with the N(N-1) counting factor, as derived in [Note06](06_TND_OC_PAIR_MARGINAL_AND_RODGERS_TAO_SPACING_20261108.md).
It needs neither RH nor an auxiliary random-matrix law. The goal is
independent canonical control of selected tests and eventually their
Newman-time evolution, including nonreal zeros. This is broader than
B01's quadratic test and the two parked B03 logarithmic recipes.

Keep both transverse marks, the common position as well as separation,
and multiplicity copies. Real-axis and conjugation components may be
singular measures. An upper-half-plane representation must reconstruct
conjugate pairs and the real sector. The all-real restriction is a
benchmark; it must not silently impose real simplicity.

If averaging is useful, define its law explicitly, for example a center U
with a specified density on a finite interval. This gives a genuine random
translated configuration, not Gaussianity or independent field values.
A single real random center generally does not give a nonsingular joint
density for several complex field values; density-form Kac–Rice therefore
needs separate premises. Use measures or distributional tests first.

## Focused literature map

[Source-use04](../../references/04_TND_OC_PAIR_MARGINAL_LITERATURE_SOURCE_USE_20261108.md)
records exact versions, checked passages and hypotheses. The
[bibliography](../../references/pair_marginal_sources.bib) contains new
articles only; existing records remain at their canonical homes.
This is a targeted search and selected-passage review, not a comprehensive
survey, full proof audit or originality claim.

| Work | What to build on | Remaining difference |
| --- | --- | --- |
| Montgomery (1973); Rodgers–Tao v5 | Restricted Fourier statistics of actual zeros and a dynamical contradiction with known spacing. | Their respective real-zero hypotheses/regimes do not establish a nonreal pair law. Full sine-kernel asymptotics are not an available input. |
| BGST (2024); *Pair Correlation I*, v3 (2026) | Arithmetic complex-difference sums and horizontal multiplicity. | These are projections, not arbitrary localized marked pairs. Proportion results retain their narrow-box hypothesis. Use the corrected error term. |
| Goldston–Lee–Schettler–Suriajaya, v4 (2026) | Ordinate-only PCC implies density-one simple critical zeros without separately assuming RH. | PCC is a hypothesis. Density one permits sparse exceptions. |
| Borodin (2009), §§2,4; Hough–Krishnapur–Peres–Virág (2009), §§3.3–3.4 | Factorial correlations, generating functionals, and joint intensities from field values and derivatives. | Determinantal/Gaussian formulas require an identified law and their integrability/nondegeneracy assumptions. |
| Tao–Vu, v3 (2014), Theorems2.1,3.1 | Quantitative transfer from joint log-magnitude comparisons to local correlations, including mixed real/complex sectors. | Joint comparison and non-clustering estimates are unpaid for H. The real version also needs weak repulsion for the comparator. Independence is not an axiom of the abstract transfer theorem. |
| Matsumoto–Shirai, v2 (2013), Theorems2.1,2.7 | Real and upper-half-disk complex correlations for a real-coefficient Gaussian series. | Its special covariance supplies Pfaffian formulas, not a law or collision estimate for H. |
| Fyodorov–Sommers–Khoruzhenko (1998), §III | A complex eigenvalue joint density marginalized to finite-N correlations and weak non-Hermiticity crossover. | The Gaussian matrix law is a comparator and lacks samplewise conjugation symmetry. Broader heuristic universality is not imported as a theorem. |
| Hall–Ho–Jalowy–Kabluchko, *The heat flow, GAF, and SL(2;R)*, v2 (2025) | Exact heat evolution with a rescaled zero law invariant at each allowed fixed time. | The plane GAF has complex Gaussian coefficients. Fixed-time invariance does not control every trajectory or collision. |
| Same authors, *Zeros of random polynomials undergoing the heat flow*, v2 (2024; published 2025) | Logarithmic potentials and transport for limiting complex root distributions. | Macroscopic empirical limits do not give microscopic pair estimates or exclude finitely many nonreal zeros. |

These heat-flow works provide comparison models, not the missing
canonical estimate. A general GAF is not automatically determinantal;
neither a sine kernel nor a Ginibre law is assigned to H by analogy.

## Two candidates for the next bounded comparison

### Repository predecessors added at the author's request

The [heat-flow applications summary](../../../../../02_heat_flow_rh_applications/summary/CURRENT_SUMMARY.md)
and [collision-bounds summary](../../../../../03_heat_flow_collision_bounds/summary/CURRENT_SUMMARY.md)
are direct predecessors alongside the earlier HDA hierarchy. Their current
registers keep ownership; this review does not reopen their stopped tests.

- [RT Note02](../../../../../02_heat_flow_rh_applications/rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md)
  derives finite real-block pair energies and exterior-force differences,
  with a same-root error payment 2 kappa E and complete contour/boundary
  obligations. [Assessment01](../../../../../02_heat_flow_rh_applications/rodgers_tao/reviews/01_PROPAGATION_AND_CONTOUR_TRANSFER_ASSESSMENT_20261026.md)
  accepts the conditional interface after corrections, same-model internal
  only. Use it for the dynamical consumer and common-motion cancellation;
  its real simple-root energy positivity is not a complex-root theorem.
- [HCB Note01](../../../../../03_heat_flow_collision_bounds/notes/01_WHOLE_CLUSTER_POISSON_TRANSFER_AND_ACQUISITION_20261026.md)
  gives the exact ordered-pair identity
  D_P(y)=2 pi y ||p_P||_2^2-n
  =sum_(i!=j) 4y^2/((a_i-a_j)^2+4y^2).
  This is a concrete smoothed pair-statistic benchmark. Proposition1's
  conditional transfer allows repeated true roots and complex approximant
  roots, but the true population a_i is real. Its floor |P(x+iy)|>=y^n
  and positive Poisson tails do not transfer unchanged to nonreal true
  zeros. The 2/3 endpoint target belongs to RH-conditional simplicity;
  it is not the present nonreal-defect target.
- HCB-01/02 remain Partial in [Register02](../../../../../03_heat_flow_collision_bounds/research-progress/02_POST_CALIBRATION_RESEARCH_PROGRESS_20261028.md):
  one finite wall/count member was acquired under RH; uniform acquisition
  and a favorable P upper value remain open. Its later Note13/Review08
  concern arithmetic physical-jet lag correlations. Note14's resonator
  defeats the declared leading-pair triangle, not all signed correlations
  or zero-pair marginals. HCB-05 remains Open.

Candidate B must compare its intended statistic with this existing P
interface before inventing another acquisition layer. Candidate A must
retain signed arithmetic information rather than reuse HCB's stopped
absolute-lag budget. These are inherited baselines and scoped lessons,
not new estimates supplied by this literature review.

**A. Arithmetic complex-difference tests.** Start from the corrected BGST
formula and inherited Rudnick–Sarnak restricted analytic tests. Determine
which common-height, separation and transverse weights admit an explicit
remainder. The first success would be a local estimate for one specified
marked test, with scales and exceptional sets declared. A dyadic average
is not a short-window theorem, and arbitrary smooth marks are not covered
merely by analytic complex-difference tests.

**B. Direct weak pair statistics from correlated log fields.** Use the
zero-measure identity in each variable, retain the self-index correction,
and compare with Tao–Vu's transfer architecture. Determine whether E02
supports a two-variable acquisition bound and identify the additional
independent joint estimate needed for a favorable value. This differs
from B03's scalar recipes. A transfer theorem need not require a
Vandermonde density; a useful comparator still needs justification.

Compare these two once each, with at most one focused clarification.
Before a dynamical hierarchy, specify the collision regime, time interval,
outside-window interactions and dependence on higher correlations.
For exp[-tau D²/2], Newman time is lambda=tau/2 in unchanged coordinates;
for the polynomial convention exp[-t D²/(2n)], it is lambda=t/(2n).
Spatial rescaling changes these relations.

For each candidate record the exact observable; deterministic or averaged
quantifier; x=2 gamma normalization; horizontal and transverse scales;
self-pair/multiplicity rules; a chosen pair's response; independent input;
and complete remainder. Compare the signal with the full background.
Averaging centers over length L may dilute a local defect by h/L.
All-height exclusion would also need to address arbitrarily small
transverse displacement and isolated exceptions.

## Classification and control screen

This is a **representation and quantitative-milestone program**, not a new
RH-equivalent criterion. The first milestone is an independently estimated
test with a stated error/regime, or scoped failure naming the unpaid input.
A definition, marginal identity or random-matrix calculation is not a
gain toward zero exclusion.

The [result index](../../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../../avoid/README.md) govern, especially
[classification01](../../../../../../../avoid/01_restating_the_target.md),
[control screen12](../../../../../../../result-summaries/12_collision_controls_and_screening.md),
[shape-only02](../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [source-use16](../../../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
The analytical screen uses the recorded controls, not new simulations:

| Control | Shared premises and distinguishing premise |
| --- | --- |
| Euler-factor controls | Localization and factorial identities survive. They alter the exact zeta/theta arithmetic; generic pair positivity does not exclude them. |
| Weighted-square controls | Positive square support and marginals survive. Full normalized reflection fails. |
| Reflected super-Gaussian control | Reflection and Gram positivity survive. Theta's integer-square arithmetic is absent. |
| Smooth shape / positive-primitive controls | Named positivity, decay and primitive properties survive. Complete theta arithmetic square expansion is absent. |
| Finite-prime orbit controls | Selected finite arithmetic constraints and measurements can survive. Full reflection fails. |

None is excluded by marginalization itself. The distinguishing premises
are candidates for a quantitative argument, not evidence that its desired
inequality follows. Retain normalized local polynomial controls when
testing a proposed stability bound. B03 supplies no universal no-go.

## Correction discovered and next action

BGST2026 v3 §3 corrects the older unconditional theorem's error term.
The parent manuscript's imported (eq:BGST) in
[11_complex_statistics.tex](../../../manuscript/sections/11_complex_statistics.tex)
reproduces the older v1 formula. **Do not reuse that uniform bound before
reconciliation.** The canonical source record now flags the issue.
This is not a completed dependency audit or a claim that all applications
fail; the authors preserve their original applications.

The [sole register](../../research-progress/01_TND_OC_RESEARCH_PROGRESS_20261107.md)
records **B04 ready for the two-candidate comparison; literature groundwork
complete, technical comparison not started**. Recommend GPT-6 Astra at
the author's selected effort for B04. A fixed BGST import reconciliation
is suitable for GPT-6.1 Sol at ultra where supported before candidate A
consumes it. E03 remains the unchanged pending B02 audit; E02 stays
accepted and B02 author-checked only. See
[Continuation07](../../continuation-notes/07_TND_OC_PAIR_MARGINAL_DIRECTION_AND_LITERATURE_20261108.md).
No model switch, independent assessment or numerical campaign occurred.
