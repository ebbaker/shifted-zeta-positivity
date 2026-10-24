# Review of the main manuscript near-axis integration

24 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. This is internal review by the authoring assistant and separate agents using the same model, not independent specialist refereeing, cross-model validation or formal verification.

## Result and authorization

The author explicitly requested that the results of [Note 19](../notes/19_NEAR_AXIS_CLUSTER_AND_QUADRATIC_EXTERIOR_20261023.md) and [Review 16](16_BOOK_AND_NEAR_AXIS_CLUSTER_REVIEW_20261023.md) be written into [main.tex](../manuscript/main.tex). They are now in its new Section 9, supplied by [near_axis_cluster.tex](../manuscript/near_axis_cluster.tex), with a complete proof and controls. The book remains the selective manuscript and was not changed. No Git commit, tag or manuscript snapshot was created.

The integration retains the established status: a proved supporting estimate under RH allowing all multiplicities, with internal review. It asserts no new simplicity proportion, per-site exclusion, small complete collision resource, or model-boundary floor.

## Proof checks and repair

- The signed initial zero product and count use the manuscript's doubled-ordinate normalization. The fixed-strip logarithmic anchor is proved using the functional equation and an absolutely convergent Euler logarithmic derivative strictly to the right of one. The classical inputs are attributed to Elkies and DLMF; the different completion normalization is explicit.
- The exterior factor retains every omitted zero. Its linear coefficient is O(log Y), quadratic coefficient is negative with magnitude O(log Y), and its complete genus-one product bounds the far Gaussian tail.
- Finite Gaussian moments justify the complex model formula. The absolute weight uses a real tilt; it does not translate the original field onto an unproved complex integration contour.
- The elementary polynomial concentration lemma handles complex coefficients and degree zero or one. It controls the actual absolute Gaussian integral rather than a coefficient majorant, with uniform degree cost for m=O(log Y).
- Separate proof review noticed that a draft tail comparison omitted the common factor |U_a(0)P_a(v)| in its wording. Before installation, it was replaced by an explicit division-free inequality retaining that factor. The corrected argument is valid at polynomial zeros and pays the full exact and model tails.
- The s=0 endpoint is treated without division when the polynomial vanishes. The theorem does not assert error derivatives or a complex-time extension.
- The curvature-omission array is scoped to the coarse growing-degree class. Its concentration and uniform-integrability argument is analytical; its earlier finite diagnostic is not promoted to proof.
- The G_0 control has even zero multiplicities, the same two leading count terms, and a positive even source with sufficient Gaussian decay. It satisfies all consumed comparison inputs. For real w and s>0, its envelope equals its positive model, so mere conversion to a real-line relative bound does not supply simplicity.

The independent agent within this same-model session found no substantive proof gap after that wording repair. This statement describes the internal review outcome, not specialist validation.

## Integration and scope

The new notation P_a,U_a,A_a,B_a distinguishes an initial fixed-radius cluster from the existing prepared polynomial P(t,z) of a complete transported population. The model supplies neither a common nonzero wall nor an invariant zero population. A forest or coefficient application still needs a paid boundary margin, complete-count transfer, and that consumer's endpoint and flux obligations.

The missing G(u,w) != 0 hypothesis in transport_reference.tex is restored. The abstract, opening roadmap, conserved-contour section and outlook now acknowledge the acquired fixed-offset comparison/material graph in the companion book. They leave multiplicity-sensitive theta arithmetic and complete earlier-population plus one-sided end-flux bounds open.

This follows the [result index](../../../../result-summaries/README.md), its [local-flow cluster](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), the [avoid index](../../../../avoid/README.md), and the specific warnings on [shared-premise controls](../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [same-model review](../../../../avoid/05_same_model_reviews_and_shared_premises.md).

## Compilation and preservation

The complete main manuscript compiled with latexmk/pdfLaTeX to 35 pages. The final log has no unresolved references, citation warnings, overfull boxes or underfull boxes. Pages 1-23 received rendered contact-sheet inspection; a separate agent visually inspected all pages 24-35 at readable size, including the theorem box, repaired tail display, final table and bibliography. No layout defect was found.

The [build receipt](../manuscript/NEAR_AXIS_BUILD_RECORD_20261024.json) records the exact integrated source hashes, final PDF hash and unchanged book/draft hashes. The reading copy is kept in the ignored repository-root output/pdf folder under the large-file policy. Prior numerical certificates were not rerun; this turn added no numerical result. Compilation and rendering validate presentation, not the mathematical theorem.
