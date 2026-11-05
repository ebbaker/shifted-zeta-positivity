# Manuscript claim-to-source map

4 November 2026. Prepared for Edward Baker with substantial LLM assistance;
actual **gpt-6-astra / ultra**, chat0007. Task **RGD-E01 r3**, E — execution.
This is provenance for the first consolidated working draft, not a new assessment.
Sol's parallel E04 r7 assessment is now complete: all twelve obligations
were accepted within scope, without mathematical correction. The
[accepted return](../research-progress/handoffs/22_RGD_E04_R7_RETURN_AND_MODEL_CONTINUATION_20261104.md)
was integrated before this draft milestone. Its frozen inputs are unchanged.

| Manuscript material | Proof/evidence | Existing assessment | Scope retained |
| --- | --- | --- | --- |
| Green transfer; complete boundary expansion | [Note01](../notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md); [parent derivation](../../brainstorm/notes/06_RADIAL_GREEN_DETERMINANT_DERIVATION_20261104.md) | [Review01](../reviews/01_RGD_E04_R1_BOUNDARY_PRESERVING_COMPARISON_ASSESSMENT_20261104.md) | Exact analytical identity; primitive positivity alone does not sign determinants. |
| Boundary-preserving reference and joint payment | [Note01](../notes/01_BOUNDARY_PRESERVING_FIRST_MODE_COMPARISON_20261104.md) | [Review01](../reviews/01_RGD_E04_R1_BOUNDARY_PRESERVING_COMPARISON_ASSESSMENT_20261104.md) | Complete modes, spatial exterior and inner boundary retained; c0-only gain is not a determinant gain. |
| Q3,1 > 7e-23; Q3,4 > 1e-74 | [Note03](../notes/03_RGD_E02_R1_RIGOROUS_TWO_CASE_BOUND_RETURN_20261104.md) | [Review03](../reviews/03_RGD_E04_R2_TWO_CASE_CERTIFICATE_ASSESSMENT_20261104.md) | Certified saved-record floors; source, spatial, quadrature and rounding payments included. No new coverage. |
| Q4,1 > 3e-31; relative payment < 1/15 | [Note05](../notes/05_RGD_B03_PREPARATORY_ORDER_DEPENDENCE_20261104.md); [Note06](../notes/06_RGD_E02_R2_FIRST_NEXT_ORDER_RETURN_20261104.md) | [Review04](../reviews/04_RGD_E02_R2_ANALYTICAL_ASSESSMENT_AND_AUTHOR_CHECKS_20261104.md) | Exact rational propagation of existing input boxes, not new integration. Separate E04 r3 remains optional. |
| Exact compact-payment stop | [Note07](../notes/07_RGD_B03_R2_EXACT_PAYMENT_OBSTRUCTION_AND_TRUE_TAIL_20261104.md) | [Review06](../reviews/06_RGD_E04_R4_COMPLETE_SOURCE_ASSESSMENT_20261104.md) | Specified compact reference and independent moment envelopes; not determinant negativity. |
| Conditional contour margin | [Note08](../notes/08_RGD_B02_R1_COMPLETE_SOURCE_CONTOUR_MARGIN_20261104.md); [Note09](../notes/09_RGD_E04_R4_PROOF_DOMAIN_AND_CONSTANT_CHECKS_20261104.md) | [Review06](../reviews/06_RGD_E04_R4_COMPLETE_SOURCE_ASSESSMENT_20261104.md) | H1/H2 and variance constants remain unacquired; eighth-power allowance is sufficient and not improved coverage. |
| Reciprocal duality, finite-pole margin and two scoped stops | [Note10](../notes/10_RGD_B02_R2_RECIPROCAL_POLE_INDUCTION_AND_SCOPED_STOP_20261104.md); [Note11](../notes/11_RGD_E04_R5_RECIPROCAL_PROOF_AND_SCOPE_CHECKS_20261104.md) | [Review08](../reviews/08_RGD_E04_R5_RECIPROCAL_COMPARISON_ASSESSMENT_20261104.md) | Fixed-index result and finite premise; failed triangle allowance is not actual error. Boundary recurrence retained. |
| Gaussian scale obstruction; quadratic universal-reference failure | [Note12](../notes/12_RGD_B02_R3_GAUSSIAN_REFERENCE_GROWTH_STOP_20261104.md); [Note13](../notes/13_RGD_E04_R6_GAUSSIAN_PROOF_AND_SCOPE_CHECKS_20261104.md) | [Review10](../reviews/10_RGD_E04_R6_GAUSSIAN_REFERENCE_ASSESSMENT_20261104.md) | Uniform fixed slack only, 1 <= r <= M k. Quadratic witnesses are edge families, not every proportional subdomain. |
| Endpoint pair reference and classical sector margin | [Note14](../notes/14_RGD_B02_R4_ENDPOINT_PAIR_REFERENCE_AND_DIAGONAL_CONTROL_20261104.md) | [Review12](../reviews/12_RGD_E04_R7_PAIR_REFERENCE_ASSESSMENT_20261104.md) | Proved in-note, accepted within scope by E04 r7; different-model internal assessment with shared premises. Implicit complete zeros, no positive-source realization asserted. |
| Negative diagonal algebraic controls with O(q^-2) scalar defect | [Note14](../notes/14_RGD_B02_R4_ENDPOINT_PAIR_REFERENCE_AND_DIAGONAL_CONTROL_20261104.md) | [Review12](../reviews/12_RGD_E04_R7_PAIR_REFERENCE_ASSESSMENT_20261104.md) | Family varies with q; no smooth positive source/primitive, exact theta arithmetic or actual zero-prefix matching established. |

## Saved finite evidence

- [E02 r1 certificate](../numerics/RGD_E02_R1_TWO_CASE_CERTIFICATE_20261104.json)
- [E02 r1 implementation and saved-record verifier](../numerics/rgd_e02_two_case_certificate.py)
- [E02 r2 exact record](../numerics/RGD_E02_R2_NEXT_ORDER_EXISTING_DATA_20261104.json)
- [E02 r2 exact verifier](../numerics/rgd_e02_r2_next_order_existing_data_check.py)

The three bounds concern **Q(r,k)=D(r+1,k)D(r-1,k)**, not D(r,k).
No new integration or numerical replay is part of this consolidation.

## Imported results and source qualifications

The manuscript bibliography is a selected copy of the existing catalogs,
not a new search or a priority audit. See [References02](../references/02_RECIPROCAL_COMPARISON_AND_FINITE_ZERO_SOURCES_20261104.md),
[References03](../references/03_GAUSSIAN_REFERENCE_AND_SCHUR_BACKGROUND_20261104.md)
and [References04](../references/04_PAIR_PRODUCT_SECTOR_AND_CONTROL_SOURCES_20261104.md).
Classical Schur duality/branching and sector positivity are attributed.
Published finite-zero inputs are not replayed. Reported fifteen-shift and
cubic-wedge coverage is not adopted as new certificate evidence.
The apparent integer mismatch in Katkova's displayed sector argument is
retained as a source qualification, not a finding that PF44 is false;
no numerical PF cutoff is imported into this manuscript's proofs.
[Note15](../notes/15_RGD_E04_R7_PAIR_REFERENCE_PROOF_AND_SCOPE_CHECKS_20261104.md)
also records the Khare p.211 mixed-sign factor display; the manuscript
carries that qualification without depending on the displayed factorization.

The full proof sections preserve all negative-index zeros. The positive
atom description applies only to the infinite first-mode reference;
the compact reference is treated algebraically. The Gaussian reference
matches C(0), C(1), p'(0) and the primitive integral; it does not assert
p_G(0)=p(0). These are exposition clarifications, not altered frozen inputs.

[INPUT_SOURCES.json](INPUT_SOURCES.json) binds the supporting versions.
[BUILD_RECORD.json](BUILD_RECORD.json) binds the built TeX sources and reading copy.
Neither hash identity nor a successful build validates a theorem.
