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
