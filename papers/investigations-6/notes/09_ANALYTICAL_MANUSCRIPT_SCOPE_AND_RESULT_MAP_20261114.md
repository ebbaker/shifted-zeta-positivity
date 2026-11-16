# Four analytical manuscripts: development and result map

14 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Manuscript workers explicitly
dispatched **gpt-6.1-sol / ultra** under the author's standing selection;
coordinator backend and effort unavailable. Dispatch is not independent
backend attestation.

**Four analytical drafts completed.** The [sole parent register](../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
owns TN6-E04 status. Its [frozen contract](../research-progress/handoffs/TN6-E04-r1.md)
and [30 source identities](../numerics/14_TN6_E04_MANUSCRIPT_INPUTS_20261114.json)
define integration of the established analytical results, with routine
supporting derivations. Manuscript production does not activate the
previously proposed new benchmark. Each branch owns its E03 manuscript
integration row and its living `manuscript/` source directory.

## Common development

All four papers start from the complete even theta source, the physical
factor 1/2 in the full-line Fourier integral and reversed time
tau=1/2-lambda. Analytical statements retain their original domains,
normalizations and observation norms. Every paper gives the definitions
and proofs needed for its own development; companion results are stated
with their hypotheses when imported. The final scientific section of
each paper describes outstanding challenges. Numerical records support
the mathematics and do not replace its proof.

| Manuscript | Main analytical sequence | Original proof source |
| --- | --- | --- |
| QTT Newman flow | Complete-source analytic bounds; polynomial approximation; constructive binary tensor ranks; fixed-box scaled observation theorem; direct polynomial comparison | [QTT proof](../01_qtt_newman_flow/notes/04_QTT_E01_COMPACT_RANK_ERROR_BOUND_20261114.md) |
| Jacobi-chain height flow | Orthogonal-polynomial spectral realization; height/heat evolution; one-excitation representation; finite Gaussian rule; Hermite-Gaussian scalar remainder; explicit depth and uncertainty transfer | [JCH proof](../02_jacobi_chain_height_flow/notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md), [shared transfer](03_TN6_E01_COEFFICIENT_TO_SCALAR_TRANSFER_20261113.md) |
| Volterra coefficient dynamics | Moment differentiation and recurrence; Volterra/Lax identities; complete-source score and confinement; monic integration by parts and Jensen; uniform logarithmic coefficient and norm-product bounds | [VCD proof](../03_volterra_coefficient_dynamics/notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md) |
| Exact infinite tensor products | Compatible mass refinement and state limits; weighted source projection; exact cell phase; uniform strip transfer; fixed point-phase aliasing obstruction | [ITP proof](../04_exact_infinite_tensor_products/notes/02_ITP_E01_EXACT_CELL_PHASE_TRANSFER_20261113.md) |

The [finite acquisition certificate](../numerics/09_TN6_E02_R1_CERTIFICATE_20261114.json)
can support the Jacobi manuscript's practical discussion. Its finite
domain, failed 128-bit allowance, successful 256-bit calculation and
internal assessment are retained. It supplies neither a universal
conditioning law nor a speed advantage. No new numerical experiment
is requested for these drafts.

## Proof and claim boundaries

Read the [result index](../../../result-summaries/README.md) and
[avoid index](../../../avoid/README.md), specifically the
[tensor cluster](../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
[controls 12](../../../result-summaries/12_collision_controls_and_screening.md)
and patterns [01](../../../avoid/01_restating_the_target.md),
[02](../../../avoid/02_shape_only_arguments_and_the_controls.md),
[03](../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[05](../../../avoid/05_same_model_reviews_and_shared_premises.md),
[06](../../../avoid/06_status_stronger_than_the_evidence.md),
[07](../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../avoid/08_normalization_and_constant_slips.md),
[16](../../../avoid/16_unchecked_imports_and_novelty_claims.md),
[18](../../../avoid/18_snapshots_large_files_and_work_outside_the_tree.md)
and [20](../../../avoid/20_volume_without_a_gain.md).

The manuscripts classify the results as representations, intermediate
coefficient bounds and quantitative absolute approximations. The actual
collision screens remain in the source decisions and proofs. Positive
coefficients or positive source measures do not establish a signed-field
claim; modified weighted-square sources can retain the coefficient
envelope at collisions. The all-height lattice obstruction concerns fixed
point phases, and does not exclude exact phase integration. Exact formal
tensor ranks do not pay coefficient acquisition or contraction precision.

## Files and build policy

Editable TeX and companion source maps/reviews remain within each branch.
The [build helper](../numerics/build_analytical_manuscripts.py) refuses
output directories inside the repository. The author's explicit request
uses the external reading-copy root
`/private/tmp/investigations-6-manuscripts-20261114/`, with subdirectories
`qtt`, `jch`, `vcd` and `itp`. All PDFs, TeX auxiliary files, logs and
rendered previews are external. These temporary reading copies can be
rebuilt from the retained sources; no manuscript snapshot is created.

The [combined build record](../numerics/15_TN6_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json)
identifies exact sources, PDF hashes, page counts and compiler observations.
The [cross-review](../reviews/03_TN6_ANALYTICAL_MANUSCRIPT_CROSS_REVIEW_20261114.md)
states: **“Accepted as analytical drafts within stated scope.”** Its
[record](../numerics/16_TN6_MANUSCRIPT_CROSS_REVIEW_20261114.json) binds
the four reviewed sources. A bounded VCD response added the explicit
endpoint/Mellin normalization and clarified the remaining depth problem.
Internal mathematical assessment and visual inspection are distinct
checks. Shared-model/source review, with JCH contributor overlap, is not
independent specialist review.

## Reading copies and editable sources

| Draft | Editable source | External reading PDF |
| --- | --- | --- |
| QTT Newman flow | [main.tex](../01_qtt_newman_flow/manuscript/main.tex) | [QTT PDF](/private/tmp/investigations-6-manuscripts-20261114/qtt/qtt_newman_flow.pdf) |
| Jacobi-chain height flow | [main.tex](../02_jacobi_chain_height_flow/manuscript/main.tex) | [Jacobi PDF](/private/tmp/investigations-6-manuscripts-20261114/jch/jacobi_chain_height_flow.pdf) |
| Volterra coefficient dynamics | [main.tex](../03_volterra_coefficient_dynamics/manuscript/main.tex) | [Volterra PDF](/private/tmp/investigations-6-manuscripts-20261114/vcd/volterra_coefficient_dynamics.pdf) |
| Exact infinite tensor products | [main.tex](../04_exact_infinite_tensor_products/manuscript/main.tex) | [Infinite-products PDF](/private/tmp/investigations-6-manuscripts-20261114/itp/exact_infinite_tensor_products.pdf) |

Each paper supplies its own source derivation, proofs and final outstanding
challenges. The [completion return](../research-progress/handoffs/TN6-E04-r1-return.md)
and [final document checks](../numerics/18_TN6_MANUSCRIPT_FINAL_CHECK_20261114.json)
record completion separately from the analytical status of earlier results.
The [continuation/model handoff](10_ANALYTICAL_MANUSCRIPTS_CONTINUATION_AND_MODEL_HANDOFF_20261114.md)
prioritizes a bounded analytical improvement with a specified consumer,
using Astra/Ultra for the conceptual choice and Sol 6.1/Ultra for ready
execution. No further numerical campaign is activated by this integration.
