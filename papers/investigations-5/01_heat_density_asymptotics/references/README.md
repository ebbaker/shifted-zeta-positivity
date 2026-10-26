# References

24 October 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance, gpt-6-astra (Codex), recorded effort max.

## Starting manuscript and repository antecedents

- [Complex zero fields and conserved heat evolution](../../../investigations-4/12_height_dependent_heat_contours/manuscript/book.tex),
  drafted for Edward Baker, working-tree edition dated 24 October 2026.
  The opening note records its source hash. Definitions, density,
  current, evolution, mass classification and residual sections were read.
- [Differentiated saddle estimates and eventual gap shrinkage](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md),
  21 October 2026. The saddle definitions, stated fixed-label result and
  complete-source moment setup were inspected. Source status:
  proved in-note, same-assistant review only. This opening does not
  re-audit its full proof or import growing-label/complex-strip uniformity.
- [Backward filter transport and terminal precision](../../../investigations-4/12_height_dependent_heat_contours/notes/09_BACKWARD_FILTER_TRANSPORT_AND_TERMINAL_PRECISION_20261023.md),
  23 October 2026, Sections 6–8 inspected. Separates complete-field
  smoothing from root-coordinate sensitivity and states the limits of
  fixed-rank terminal data.

## Online method reference

F. W. J. Olver and R. Wong, **§2.3 Integrals of a Real Variable**,
Chapter 2, NIST Digital Library of Mathematical Functions.
[Primary source](https://dlmf.nist.gov/2.3);
[chapter authors/version](https://dlmf.nist.gov/2).
Online version 1.2.8, released 15 September 2026; retrieved 24 October 2026.

Inspected the endpoint expansion in §2.3(ii), equations 2.3.7–2.3.8,
and the opening hypotheses of §2.3(iii). Used as background for
negative-time endpoint expansions. This does not certify uniform
complex-domain, differentiated or moving-saddle errors for theta.
No full-chapter review is claimed. The online reference is retained
as a linked record; no artificial PDF copy was created.

Used in the [opening brainstorm](../notes/01_AVERAGED_DENSITY_AND_TWO_TIME_LIMITS_BRAINSTORM_20261024.md).
Reusable citation: [references.bib](references.bib).

## Filtering background found during the first research round

Robert A. Clark, Joel H. Ferziger and W. C. Reynolds, **Evaluation of
subgrid-scale models using an accurately simulated turbulent flow**,
*Journal of Fluid Mechanics* **91**(1), 1–16, 9 March 1979.
[Primary publisher record](https://www.cambridge.org/core/journals/journal-of-fluid-mechanics/article/evaluation-of-subgridscale-models-using-an-accurately-simulated-turbulent-flow/3DAEEC51F4433891450FE815F6E379F9);
[DOI](https://doi.org/10.1017/S002211207900001X). Retrieved 24 October 2026.

**Inspection:** publisher metadata and abstract only. The 2006 date on
the page is online publication, not the original article date. The
article is relevant background on comparing filtered covariances with
models derived from resolved fields. No theorem or coefficient is
imported from it; the small-width Taylor expansion in
[Note 04](../notes/04_GRADIENT_CLOSURE_AND_ACTUAL_THETA_PILOT_20261024.md)
is derived there, without a novelty claim. The inspected publisher page
offers access rather than an openly accessible PDF; no PDF was retrieved
or copied into the repository. Full-text inspection remains open before
any precise attribution to an equation in this article.

## Related gradient-closure comparison

Miralireza Nabavi and Jeonglae Kim, **Optimising subgrid-scale closures
for spectral energy transfer in turbulent flows**, *Journal of Fluid
Mechanics* **982**, A18 (10 March 2024; online 4 March).
[Primary source and DOI](https://doi.org/10.1017/jfm.2024.101).
Retrieved 24 October 2026.

**Inspection:** publisher metadata, equation (6.3), and §6.3 in the HTML.
The gradient-product model is relevant background for
[Note 04](../notes/04_GRADIENT_CLOSURE_AND_ACTUAL_THETA_PILOT_20261024.md).
The paper's turbulence-specific scale and stability conclusions are not
transferred to the theta equation. No full-paper review or novelty claim
is made. A published open-access PDF reading copy is retained outside Git;
its source URL, local path, byte size and SHA-256 are in the
[download record](DOWNLOADS_20261024.json). The hash identifies the copy,
not the validity of its mathematics.

## Complex analysis used in the coarse-transfer continuation

NIST Digital Library of Mathematical Functions, **§1.10 Functions of a
Complex Variable**, [primary source](https://dlmf.nist.gov/1.10). Retrieved
24 October 2026. Inspected §1.10(iv), equations 1.10.8–1.10.9: residues
and the argument principle for a positively oriented contour with no
boundary zeros or poles; zeros are counted with multiplicity. Also checked
the Rouche statement in §1.10(iv). The
homotopy argument in Note 09 derives the particular comparison from the
argument principle. No global real-zero or theta theorem is imported.
The quotient lower bound uses the maximum-modulus principle on its
reciprocal (§1.10(v)); the proof and nonvanishing premise are in Note 09.
This is a linked online reference; no PDF was made. Added for Edward
Baker with substantial LLM assistance, gpt-6-astra, recorded effort max.


## Positive-time high-height reference discovered in round three

D. H. J. Polymath, **Effective approximation of heat flow evolution of the
Riemann xi function, and a new upper bound for the de Bruijn-Newman
constant**, arXiv:1904.12438v2, revised 4 August 2019.
[Primary version](https://arxiv.org/abs/1904.12438v2). Retrieved
24 October 2026. Metadata and abstract inspected in this round; no
particular high-height theorem is imported. The author subsequently
prioritized the two unbounded heat-time limits. The existing reading copy
and its provenance belong to the [sibling catalog](../../../investigations-4/12_height_dependent_heat_contours/references/README.md);
no duplicate PDF was created. Large height at fixed heat time and large
heat time on growing height windows must not be conflated. Added for
Edward Baker with substantial LLM assistance, gpt-6-astra, effort max.


**Additional inspection, 24 October 2026, chat 0006; gpt-6-astra, max.**
For [Note 25](../notes/25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md),
checked the [v2 HTML](https://arxiv.org/html/1904.12438v2): normalization
(1)--(4), domain (5), Theorem 1.5's hypotheses and clock definition,
and Lemma 9.2's displayed local gamma-factor formula. The high-zero
theorem is stated for 0<t<=1/2. It is an outer-representation lead,
not an imported theorem for t>64. Extending its parameter range and
paying adaptive weak-transfer data remain work. No full-paper review or
new PDF download; the existing sibling reading copy remains canonical.

## Sibling Vandermonde and saddle inputs rechecked in round three

For [Note 12](../notes/12_GROWING_HEIGHT_STATIONARY_CLOCK_AND_VANDERMONDE_20261024.md),
rechecked BW10 Note 20's DS7--DS12 proof, including normalization, signed
mean and far-left tail. The new weighted extension is proved in Note 12.
Read HDC Note 06 Sections 1--3 (discriminant Hessian and complete forces),
HDC Note 09 Sections 1--6 (moving normalization, reference defect and
fixed-rank limits), and LHCT Note 07 Section 4 (finite-polynomial Hermite
energy and selected-cluster forcing). These are repository results with
their recorded same-model/internal review scope, not external independent
confirmation. [HDC catalog](../../../investigations-4/12_height_dependent_heat_contours/references/README.md).
No stochastic universality, unforced theta equilibrium or backward
stability is imported. Added 24 October 2026 for Edward Baker with
substantial LLM assistance, gpt-6-astra, actual effort max.

## Manuscript crosswalk and adaptive-regulator continuation

24 October 2026, for Edward Baker with substantial LLM assistance,
gpt-6-astra, actual effort max. The
[maintained manuscript](../manuscript/main.tex) cites Notes 02, 04--06,
09, 11--12 and the inspected sibling saddle/pair-matrix sources directly.
Its numerical appendix cites the execution records separately.
The bibliography's local links resolve in the checked export; the build
guide explains how they follow the checkout root.

[Note 14](../notes/14_VARIABLE_EPSILON_EVOLUTION_AND_ASYMPTOTICS_20261024.md)
derives the variable-regulator identities directly, extends Note 06's
weak logarithmic-bias argument, and applies Notes 11--12's complete-source
bounds. No new external theorem or priority claim is imported.
The [assessment](../reviews/04_MANUSCRIPT_AND_VARIABLE_EPSILON_SELF_REVIEW_20261024.md)
records same-assistant review and exact polynomial controls.


## Periodic Bernoulli formula for the explicit clock

NIST Digital Library of Mathematical Functions, **Chapter 24, Bernoulli
and Euler Polynomials**, [definitions §24.2](https://dlmf.nist.gov/24.2)
and [Fourier series §24.8](https://dlmf.nist.gov/24.8), retrieved
24 October 2026. Inspected equations 24.2.3--24.2.5 and 24.8.1--24.8.3,
including the endpoint validity for degrees at least two. The finite
periodization formula in Note 19 is derived from 24.8.3 and polynomial
integration by parts; no theta theorem is imported. This is a linked
online reference, with no PDF copy or full-chapter review. No priority
claim. Added for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), actual effort max**.


## Finite-field error-function evaluation

NIST Digital Library of Mathematical Functions, **§7.2 Definitions** and
**§7.6 Series Expansions**, [7.2.1](https://dlmf.nist.gov/7.2.E1),
[7.6.1](https://dlmf.nist.gov/7.6.E1), retrieved 24 October 2026. Checked
the defining integral, entire-function statement and convergent power
series; no full-chapter inspection or numerical stability theorem is
claimed. Note 23 derives its own local exponential truncation allowance.
These are online references, with no artificial PDF copy. Prepared for
Edward Baker with substantial LLM assistance, gpt-6-astra, actual effort max.


## Gamma-factor outer analysis, HDA-19 continuation

24 October 2026; prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), actual effort max**, chat 0006.

For [Note 27](../notes/27_COMPACT_TIME_GAMMA_OUTER_DENSITY_20261024.md),
additionally inspected Polymath v2 Section 4 through (35),
which states the Gaussian convolution for every t>0 and derives it from
the complete source. The two-factor asymptotic and adaptive-density
transfer in Note 27 are proved there with compact-time constants; they
do not extend Theorem 1.5 by changing its stated hypotheses. The gamma
factor used in the note is exact, unlike the paper's Stirling model.
The existing sibling PDF and provenance remain canonical.

- NIST DLMF, [Section 5.11](https://dlmf.nist.gov/5.11): inspected
  5.11.1--5.11.2, the bounded-real-part formula 5.11.9, and the first
  complex remainder paragraph in 5.11(ii). Used for sectorial log-gamma
  and digamma bounds. Derivative estimates are obtained in the note on
  smaller sectors by Cauchy's formula; no differentiation of a real-axis
  asymptotic is assumed.
- NIST DLMF, [Section 25.2](https://dlmf.nist.gov/25.2): inspected
  the Dirichlet series 25.2.1 and Euler summation formula 25.2.8. These
  give the paid arithmetic tail and a polynomial bound on the bounded
  middle strip.

Retrieved 24 October 2026. These are linked online references; no PDF
copies or full-chapter reviews were made. The root-collar and weak-bias
steps reuse the complex-analysis reference above and Note 14. No novelty
claim or independent validation is implied by these citations.


**Time-dependent continuation, chat 0006, 24 October 2026; gpt-6-astra,
actual effort max.** [Note 28](../notes/28_JOINT_OUTER_REGULATOR_TRANSFER_AND_SWITCH_LAYER_20261024.md) reuses and rechecked
Polymath (35), DLMF
5.11.9/5.11(ii) and 25.2.8 in the primary HTML sources above. The new
uniform regulator comparison, joint range and switch-layer estimates
are derived in the note, not imported from those sources. No new PDF.

Also inspected Sections 1--3 of the sibling
[sharp C2 divisor stability note](../../../investigations-4/notes/09_SHARP_C2_DIVISOR_STABILITY_20261022.md),
including its distinction between a compact regularization and direct
divisor perturbation. Its proved-in-note, same-assistant status is
retained. Note 28 uses the original rational adaptive density instead;
its two-potential comparison and arbitrary-positive-q local lemma are
derived separately. No multiplicity-general or independent-review claim
is imported from this sibling inspection.

**Full-saddle continuation, chat 0007, 24 October 2026; gpt-6-astra,
actual effort max.** For [Note 30](../notes/30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md),
rechecked the same primary HTML sources: Polymath v2 Section 4,
normalization (1)--(2) and exact convolution (35); DLMF 5.11.1--5.11.2,
5.11.9 and the first complex-remainder paragraph of 5.11(ii); and
25.2.1/25.2.8. The fixed right-half-plane sector, implicit gamma saddle,
uniform contour estimates, mass-anchored adaptive transfer and inner
overlap are derived in Note 30, not imported as a theorem from Polymath.
The small-time high-zero theorem is not extended by changing its
hypotheses. Also reread Note 12 (3)--(6) for the complete-source mass
bound used after the independent field proof, and Notes 27--28 for the
collar/weak-transfer contracts. No new reference, PDF copy, full-paper
review or numerical validation; existing bibliography and PDF provenance
remain canonical.

**Positive-evolution continuation, chat 0007, 24 October 2026;
gpt-6-astra, actual effort max.** [Note 31](../notes/31_POSITIVE_ALL_HEIGHT_EVOLUTION_AND_COVARIANCE_20261024.md)
uses Note 30's complete field theorem and exact residual. Inspected
[DLMF 1.9.30--1.9.31](https://dlmf.nist.gov/1.9#iii), including the
analytic-contour hypotheses and derivative formula, for the explicit
Cauchy-disk transfer; rechecked the fixed-sector condition in
[DLMF 5.11](https://dlmf.nist.gov/5.11). New pole, signed-stress,
adaptive time and flat-switch estimates are derived in Note 31.
Also reread Notes 14/16 for the exact weak identities, Note 20 for the
unchanged switch, Note 28 for analytic-unit transfer, and Note 26 for
the negative contract. No new PDF, numerical validation, whole-chapter
review or novelty claim.


## Manuscript production synchronization — 24 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**. HDA-10-MI1 r1 adds Notes 25--28 and 30 and the
version-pinned Polymath/DLMF gamma, zeta and complex-analysis entries to
`manuscript/06_references.tex`, the actual manual bibliography.
`references.bib` is a reusable catalog and is not compiled by this build.
Its BakerHeatDensityDraft2026 title now matches the retained manuscript
title, preserving historical Astra preparation and adding Sol revision
attribution. The five external URLs in the final PDF were opened for
link verification. No new PDF copy, full-paper review, theorem import or
independent mathematical audit was performed. The preceding reference
inspection scopes remain unchanged.
[Production assessment](../reviews/14_MANUSCRIPT_INTEGRATION_PRODUCTION_REVIEW_20261024.md);
[current build record](../manuscript/BUILD_RECORD_20261024.json).


## Review 15 manuscript revision — 24 October 2026

Prepared for Edward Baker with substantial LLM assistance, **gpt-6.1-sol,
actual effort ultra**. The current manual bibliography now includes Note
31 and DLMF 1.9.31, matched by reusable catalog entries. Opened the
[official Cauchy reference](https://dlmf.nist.gov/1.9.E31), equations
1.9.30--31 and their contour hypotheses, for the recorded derivative
transfer input. The full buffered disks are supplied by Note 31; no new
whole-chapter review, theorem extension or PDF download was made.
The earlier analytical inspection scopes and Astra attribution remain.
[Production assessment](../reviews/16_REVIEW15_REVISION_PRODUCTION_ASSESSMENT_20261024.md);
[current build record](../manuscript/BUILD_RECORD_20261024.json).


## Phase-transition and crossover methods — chat 0012

24 October 2026, prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort xhigh**. [Reading record](PHASE_TRANSITION_METHODS_20261024.md)
records Fisher–Barber on shift/rounding, Wilson on RG, Tong on order
parameters/correlations/scaling, and DLMF uniform-asymptotic methods.
[Note 38](../notes/38_PHASE_TRANSITION_LITERATURE_AND_JOIN_DIAGNOSTICS_20261024.md)
assesses their applicability without identifying a theta critical point or CFT.
[PDF provenance](PHASE_REFERENCES_DOWNLOADS_20261024.json) retains the
public Tong copy outside Git and Wilson local retrieval failure. No full
literature review or imported criticality theorem is claimed.


## Effective outer field input — chat 0015,25 October 2026

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. [Note 45](../notes/45_EFFECTIVE_FULL_BUFFER_OUTER_FIELD_20261025.md)
uses the following official NIST DLMF passages, inspected in primary
HTML on 25 October 2026, DLMF 1.2.8 (released 15 September 2026):

- [5.11.2 and 5.11(ii)](https://dlmf.nist.gov/5.11#ii): first omitted
  digamma term at n=1 and its complex sector remainder. The new finite
  alpha bounds and analytic-circle derivative constants are derived
  from this remainder, not imported as a theta theorem. Earlier
  24 October inspections and their scope remain recorded above.
- [5.7.8](https://dlmf.nist.gov/5.7.E8): exact imaginary digamma series
  at 1+iy; sum/integral comparison bounds the connector gamma-height
  change on Re w=2. No whole-chapter review.
- [5.12.1](https://dlmf.nist.gov/5.12.E1): beta integral with positive
  real parts, used to bound a gamma ratio on b/2 in [1/4,1]. The endpoint
  is treated by a limit; its conditions are retained.
- [25.2.1/25.2.8](https://dlmf.nist.gov/25.2): complete Dirichlet series
  on Re w>=2 and Euler summation at N=1, Re w>0. The middle estimate uses
  (w-1)zeta(w) with its removable value, rather than bounding zeta at 1.
- [1.9.30–1.9.31](https://dlmf.nist.gov/1.9.E31): Cauchy formula and
  derivative formula, with the actual full analytic disks provided by
  Note 45. The extra strip margin does not justify an arbitrary fixed
  disk radius; the chosen radius is 1/[4log(2+x)].

The effective branch, field ledger, huge onset and FI23 consumption are
new estimates in Note 45, checked only internally by the same model.
These references do not independently validate them. Online linked
records suffice under REFERENCE_WORKFLOW.md; no artificial PDF copies,
third-party PDF downloads or full-paper/whole-chapter reading claims.

## Simple solution ansätze — 25 October 2026, chat0022

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra (Codex), actual effort max**, for
[Ansatz Note01](../ansatz/notes/01_REGIME_BY_REGIME_SOLUTION_ANSATZE_20261025.md).

- NIST Digital Library of Mathematical Functions,
  [§18.18(i), Hermite expansions](https://dlmf.nist.gov/18.18#i).
  Equations 18.18.6–18.18.7 and the subsequent L² convergence paragraph
  inspected 25 October 2026. The imported fact is completeness in the
  Gaussian weighted L² space, after rescaling and restricting to even
  functions. The source-specific weighted four-jet argument is derived
  in the note. No approximation rate, finite coefficient constructor or
  theta error bound is imported. Reusable key DLMFHermiteAnsatz2026.
- NIST Digital Library of Mathematical Functions,
  [§4.13, Lambert W](https://dlmf.nist.gov/4.13).
  Equation 4.13.1, real branches and the complex branch discussion
  inspected 25 October 2026. These support algebraic inversion of the
  leading logarithmic saddle and the branch caution. They do not prove
  the new field comparison or its heat residual.
  Reusable key DLMFLambertAnsatz2026.
- Existing reference DLMFGammaOuter2026,
  [§5.11](https://dlmf.nist.gov/5.11), rechecked 25 October 2026:
  5.11.1–5.11.3, 5.11.9 and the opening sectorial remainder paragraph
  of §5.11(ii). Used to derive the leading elementary amplitude and
  phase from the manuscript's linear gamma model and to propose the
  Stirling/Lambert saddle. The original comparison domains and the
  missing differentiated budgets are stated in Ansatz Note01.

Online primary references are retained as links; no PDF copy was
created. No full-chapter review or independent validation is claimed.
