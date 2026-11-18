# DLMF passages for the complex-index contour question

17 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual lead model and effort unavailable in
this chat's recorded configurations. Intended research effort: **ultra**;
recommended conceptual lead: **Astra**; expressly authorized bounded
helpers: **GPT-6.1 Sol/ultra**. Requested settings are not serving attestation.

**Selected primary passages inspected 17 November 2026 (UTC 18 November).**
Institutional author: National Institute of Standards and Technology,
*Digital Library of Mathematical Functions*. Online edition accessed at the
links below; release identifier not recorded. No full book/paper reading or
PDF download is claimed. These are branch-use annotations; the reusable
[bibliography](../../../references/induction.bib) remains canonical.

- [§2.5(i), equations 2.5.1–2.5.7](https://dlmf.nist.gov/2.5): Mellin
  definition, inversion on a line inside its convergence strip,
  convolution and contour-shift residues with the remaining contour.
  The displayed shift is conditional on continuation and permissible
  deformation. A CM proof must establish these hypotheses for its actual
  kernel and complete divisor; the general formulas do not supply them.
- [5.9.1](https://dlmf.nist.gov/5.9.E1): with the exponent parameter set to
  one, the positive-ray gamma integral requires Re a>0, Re p>0 and
  principal powers. This reinspects the inherited [GT passage record](../../references/02_VCD_GT_XI_QUADRATURE_BOUND_SOURCES_20261116.md#gamma-transform-passage-17-november-2026-chat0007).
  Near denominators need not satisfy the sector; the complete sum needs
  an absolute interchange. This is not itself integration in the p plane.
- [5.11.9](https://dlmf.nist.gov/5.11.E9): gamma magnitude asymptotics as
  the imaginary part tends to either infinity, uniformly for bounded real
  parts. This identifies a possible ingredient for vertical-tail estimates.
  It gives neither an explicit global constant here nor uniformity as the
  real part grows; the actual power-spectrum growth must also be paid.

Consumer: [overview](../research-overview/01_VCD_GT_CM_RESEARCH_OVERVIEW_20261117.md),
B01 representation selection and E01 source audit, then E03/E05 only if a
fixed proof contract imports the stated passage. No new theorem about the
canonical field is proved by this source inspection. Preserve the distinction
between a Mellin variable, a spatial contour and a heat/Gaussian scale.

## Chebyshev normalization check, 18 November 2026

Prepared for Edward Baker with Codex LLM assistance; actual root model and
effort unavailable in CM chat0006. Selected primary passages inspected:
[NIST DLMF 18.5.1](https://dlmf.nist.gov/18.5.E1),
[18.5.2](https://dlmf.nist.gov/18.5.E2), and the normalization context in
[Table18.3.1](https://dlmf.nist.gov/18.3). The online edition was retrieved
on 18 November 2026; its release identifier was not recorded. No PDF was
downloaded. The displayed first-kind formula is T_n(cos theta)=cos(n theta),
with its equivalent Laurent form, and the second-kind formula is
U_n(cos theta)=sin((n+1)theta)/sin theta (with continuous endpoint values).
These check the standard normalization used in
[Note45](../notes/45_VCD_GT_CM_E38_CARDINAL_SOURCE_REFINEMENT_20261118.md).
The discrete endpoint weights, cardinal norm bound and actual reconstruction
audit are proved in that note; they are not asserted to be theorems imported
from these DLMF passages. This is selected-formula inspection, not a
literature review or novelty claim. Canonical BibTeX key: NISTDLMFChebyshev.

## Gaussian and polynomial-heat normalization check, 18 November 2026

Prepared for Edward Baker with OpenAI Codex assistance; actual root model
and effort unavailable in CM chat0006. Rechecked
[DLMF5.9.1](https://dlmf.nist.gov/5.9.E1) with positive real Gaussian
parameter, and inspected [18.12.15](https://dlmf.nist.gov/18.12.E15),
the physicists' Hermite generating function exp(2xz-z²). The former has
Re(nu)>0, mu>0 and Re(z)>0, with principal powers; mu=2 supplies the
Gaussian absolute moments after the appropriate normalization. These are
selected primary formula checks on the online edition, retrieved18 November
2026; release identifier not recorded, no PDF downloaded.

Consumers: CM E16 Notes47–48 and E40's finite polynomial sign/variance
checks. The common-time product-tail estimate and contour transfers are
proved in those notes; neither an uninspected heat-semigroup theorem nor
a priority claim is imported from DLMF. Gamma bibliography ownership remains
NISTDLMFZetaGamma; the Hermite convention uses NISTDLMFHermiteHeat.
