# Canonical close-pair source use

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, branch chat0002. Lead actual recorded
model and effort unavailable. This is selected-passage inspection, not a
full-paper audit or verification of the historical zero computation.

The canonical record for George Csordas, Wayne Smith and Richard S. Varga,
*Lehmer Pairs of Zeros, the de Bruijn–Newman Constant Λ, and the Riemann
Hypothesis*, Constructive Approximation **10** (1994), 107–129,
[DOI 10.1007/BF01205170](https://doi.org/10.1007/BF01205170), remains in the
[auxiliary-flow catalog](../../../../investigations-5/06_auxiliary_collision_flows/references/sources.json)
and [bibliography](../../../../investigations-5/06_auxiliary_collision_flows/references/sources.bib),
key `CsordasSmithVarga1994`. The
[DY02 annotation](../../../../investigations-5/06_auxiliary_collision_flows/lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md#dy02)
retains the earlier use. No competing article catalog is created here.

## Passages actually checked

The [author-hosted published PDF](https://www.math.kent.edu/~varga/pub/paper_206.pdf)
was downloaded and its first three pages rendered and visually inspected:

- p.107, (1.1)–(1.2): the full Fourier source and its physical coordinate;
- p.108, (1.3) and (1.3′): the heat deformation and the factor 1/8 at time zero;
- p.109, (1.9): the first Lehmer pair in that physical coordinate, approximately
  14010.125732349841 and 14010.201129345293; Definition 1/(1.10)–(1.11)
  places it in the gap-plus-exterior-interaction framework.

The article's critical-line xi notation is translated here as
`H_0(z)=xi_std((1+iz)/2)/8`, with
`xi_std(s)=s(s-1)pi^(-s/2)Gamma(s/2)zeta(s)/2`; thus physical `z=2 gamma`.
The source formula and approximate pair location are the only new external
uses in [B04](../brainstorm/notes/04_VCD_GT_B04_CANONICAL_LEHMER_ACQUISITION_20261116.md).
The Gaussian oracle is derived in E08. The historical lower-bound theorem,
global zero indexing, an all-real slice, and a positive-time tube certificate
are not imported as acquisition inputs.

Reading copy: `/private/tmp/vcd-gt-references/csordas-smith-varga-1994-paper206.pdf`,
retrieved 16 November 2026 from the author URL; 1,905,194 bytes; SHA-256
`21f89671068177ccf0db285c1caddf511848c28798a0b58f3edb551bfdefe8db`.
This matches the already cataloged 28 October reading copy at
`/Users/Shared/szp-archive/auxiliary-collision-flows/references/CsordasSmithVarga1994_reading_copy_20261028.pdf`;
that catalog retains original archival provenance. The temporary copy and
rendered images stay outside Git. The PDF is scanned: text extraction was
empty, so the checked passages above refer to the rendered pages. Hash
identity does not validate the mathematics.

## Sibling stop and limits

The [OA source-use record](../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/references/03_TND_OA_B03_LEHMER_SOURCE_USE_20261109.md)
and [OA decision08](../../../../investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/03_collision_constraints/notes/08_TND_OA_B03_LEHMER_DIRECTION_AND_ACQUISITION_STOP_20261109.md)
were read. They record the missing positive-time acquisition and the wrong
direction of an upper exterior inverse-square sum for survival. This round
proposes a different, complete-source acquisition and leaves the OA status
unchanged. Stopple's RH assumption and the corrected COSV lower-bound result
are not silently used. A search also surfaced the author's `paper_209.pdf`;
its indexed excerpt was discovery only, and no theorem from it is used.

Follow [REFERENCE_WORKFLOW](../../../../../REFERENCE_WORKFLOW.md),
[results](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[avoid](../../../../../avoid/README.md), and especially
[unchecked imports](../../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
