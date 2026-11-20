# References and source ownership

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance; founding lead recorded gpt-6-astra/max.
Helpers explicitly dispatched gpt-6.1-sol/ultra. Selected-source reading,
inherited checks and fresh imports are distinguished below.

This investigation maintains a small [standalone bibliography](references.bib)
for its draft. Detailed source annotations and external PDF reading-copy
ownership remain at the linked canonical homes. Reusing a recorded passage
is not a fresh full-paper audit. Follow [REFERENCE_WORKFLOW](../../../../REFERENCE_WORKFLOW.md)
and [LARGE_FILES](../../../../LARGE_FILES.md).

| Source | Exact use in the draft | Inspection and canonical record |
| --- | --- | --- |
| D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann xi function, and a new upper bound for the de Bruijn–Newman constant*, arXiv:1904.12438v2, 4 August 2019; DOI 10.1007/s40687-019-0193-1 | Theorems 1.2, 1.3, 1.5; §§4,6,8,9; exact arithmetic terms, term error, complete value bound, source clock and strip criterion | [Primary version](https://arxiv.org/abs/1904.12438v2); [inherited receipt02](../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/brainstorm/references/02_HEIGHT_DENSITY_SOURCE_CHECK_20261119.md). Selected source passages rechecked during E03/review; lead also checked Proposition 6.1's complete hypotheses. No full-paper or certificate replay. |
| Dave Platt and Tim Trudgian, *The Riemann hypothesis is true up to 3·10^12*, arXiv:2004.09765v1, 21 April 2020; BLMS 2021, DOI 10.1112/blms.12460 | Theorem 1's exact height and §3.4/Corollary 2's 0.2 consequence | [Primary version](https://arxiv.org/abs/2004.09765v1); [receipt03](../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/brainstorm/references/03_PLATT_TRUDGIAN_GOMILA_METHOD_COMPARISON_20261119.md). Prior turn read the short scientific text; current helpers rechecked selected criterion/endpoint uses. |
| Jude Gomila, *Proof note for the 0.1787854 bound* and native-binding lemma, revision a74738deb6d5e0f76887cb36901da08b68dca705, 21 August 2026 | Exact parameter row, arithmetic normalization, coefficient convolution and transfer to the original finite sum | [Pinned package](https://github.com/judegomila/dbn-lambda-01787854-candidate-audit/tree/a74738deb6d5e0f76887cb36901da08b68dca705); [receipt03](../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/brainstorm/references/03_PLATT_TRUDGIAN_GOMILA_METHOD_COMPARISON_20261119.md). Proof note rechecked. E03's fresh native-binding request failed, so that import uses the earlier inspected receipt plus the elementary derivation in the draft. Package presents a computer-assisted proof awaiting peer review. |
| Jude Gomila, *A new ceiling for Lambda: the de Bruijn–Newman constant is at most 0.1787854*, dated 19 August 2026, live page retrieved 19 November | Explanation and separate status of later research report | [Author page](https://www.judegomila.com/posts/riemann-lambda-0.1787854). The later 0.1782354 statement is attributed, with mathematical review pending; its research package was not audited here. |
| Brad Rodgers and Terence Tao, *The de Bruijn–Newman constant is non-negative*, arXiv:1801.05914v5, 3 July 2021; Forum of Mathematics Pi 8 (2020), e6 | Source normalization and background Lambda>=0 only | [Primary version](https://arxiv.org/abs/1801.05914v5); lead rechecked metadata/abstract on 19 November, including the stated v5 Section 8 correction. Broader prior reading remains in [receipt02](../../03_volterra_coefficient_dynamics/01_cluster_gap_transport/02_complex_p_mellin/brainstorm/references/02_HEIGHT_DENSITY_SOURCE_CHECK_20261119.md); no new import from the corrected argument. |

## Existing external reading copies

No third-party PDF is placed in this investigation. The following files
were already present; their identity was checked for the founding reading:

- Polymath v2: `/Users/Shared/szp-archive/height-dependent-heat-contours/references/1904.12438v2.pdf`,
  2158176 bytes, SHA-256 `60d0d2d381227d32f98535a5c43dedb86e333a9006d6819f0bdebdd734085603`.
- Platt–Trudgian v1: `/Users/Shared/szp-archive/heat-flow-rh-applications/references/2004.09765v1.pdf`,
  133056 bytes, SHA-256 `3362f66af9fa9373977eee70e2282ec33989d5d8b97e0852df9e32cc25b52885`.

The earlier Gomila release-PDF retrieval failed at local name resolution;
no new reading copy or hash is claimed. Accessible proof-note text and
existing pinned inspections support the limited comparison. Hashes establish
file identity, not mathematical validity.

## Internal analytical inputs

The [source/status crosswalk](../notes/02_AGC_SOURCE_AND_STATUS_CROSSWALK_20261119.md)
maps the parent manuscript and Discussion07–12 to the new self-contained
chapters. The [October audit review](../../../investigations-2/newman_certificate_audit/reviews/CROSS_MODEL_REVIEW_OF_CLAUDE_AUDIT_CODEX_20261013.md)
owns the retained-C applicability qualification and local replay scope;
stronger claims from its initial benchmark are not imported. The
[control index](../../../../result-summaries/12_collision_controls_and_screening.md)
links each original control proof and evidence level.

The parent manuscript's statement of common-time approximation remains
an inherited result under its own fixed-input hypotheses. Most of its
production/certificate examples are deliberately not reproduced: they are
supporting evidence, not the analytical mechanism of this track. The new
manuscript derives the pair, chain, hierarchy, drift, residual and transfer
formulas needed to follow the program without that repeated cross-reference.

## AGC continuation source check, 19 November 2026

Prepared for Edward Baker with OpenAI Codex assistance; actual lead settings unavailable, source helper explicitly dispatched gpt-6.1-sol/ultra. [Note06](../notes/06_AGC_E11_SOURCE_ALLOWANCE_20261119.md) spells out the unnormalized complete value budget from the same Polymath v2. The helper and lead reopened Proposition6.1 (44), Proposition6.3 (59), and Corollaries6.4–6.5/(68)–(74), checking the full omitted-correction payment and natural-cutoff domain. [Lead check](../reviews/03_AGC_SOURCE_ALLOWANCE_LEAD_CHECK_20261119.md) records the elementary carrier/defect proof and selected-source check. No new version, PDF copy, full-paper audit or external certificate replay is claimed. The log-disk and bounded-interval heat estimates are proved directly in the new notes; no novelty assertion is made for their elementary ingredients.

**Retained-correction continuation, 19 November 2026.** Prepared for Edward Baker with Codex assistance; actual lead settings unavailable, derivation and assessment helpers explicitly dispatched Sol6.1/ultra. The lead and separate assessor rechecked Polymath v2 (7), (52), (53), (68), Corollary 6.4 and its full retained remainder, with Corollary 6.5 as the omitted-correction comparator. [Note10](../notes/10_AGC_E13_R2_HOLOMORPHIC_CORRECTION_20261119.md) proves the local phase cancellation, holomorphic lift and explicit derivative payments. The exact displayed source correction is a value formula; holomorphy and its off-axis mismatch are established separately. This is selected-passage inspection of the existing version, without a new reading copy or a full-paper audit.

**Full-phase continuation, 19 November 2026.** Prepared for Edward Baker with Codex assistance; root settings unavailable, conceptual Astra/ultra and proof/assessment Sol6.1/ultra explicit dispatches. The lead, B03 author, E14 author and separate assessor reopened selected Polymath v2 passages, especially (53), (58), (59), Corollary6.4/(68), and Theorem1.2. [Note14](../notes/14_AGC_E14_UNIFORM_CORRECTION_AND_STRIP_COMPARISON_20261119.md) supplies its own entire-extension, derivative, real-part and complete-comparator proofs; [Review07](../reviews/07_AGC_UNIFORM_CORRECTION_ASSESSMENT_20261119.md) checks the imports and their scope. No new reference version, PDF download or full-paper audit is claimed.

**Three-prime continuation, 19 November 2026.** Prepared for Edward Baker with Codex assistance; root settings unavailable, B04 Astra/ultra and E16 proof/assessment Sol6.1/ultra explicit dispatches. Selected [Polymath v2](https://arxiv.org/html/1904.12438v2) definitions(9)–(22), retained Corollary6.4, Section8.5/Lemma8.5, Proposition9.1 and Theorem1.2 were rechecked. The new generalized ellipse modulus estimate is derived directly; none of Section8.5's numerical constants at t=.2 is imported at t=.1. The exact finite convolution includes its cutoff indicator, and the heat weight uses t/4, preserving Section5's warning about the stronger intermediate exponent in Section9. No new reading copy, source version, full-paper audit or novelty claim.

**Dyadic-group continuation, 19 November 2026.** Prepared for Edward
Baker with Codex assistance; root settings unavailable, B05 Astra/ultra
and E17 proof/assessment Sol6.1/ultra explicit dispatches. Selected
[Polymath v2](https://arxiv.org/html/1904.12438v2) passages were reopened:
Theorem1.2, definitions(9)–(22), Corollary6.4/(68)–(73), and
Section8.5/Lemma8.5. The inherited literal source, two complete term
errors and both retained delta payments are unchanged. The new dyadic
mean argument uses finite Fourier averaging and convexity of a real
matrix norm, proved locally; no new external theorem, t=.2 numerical
constant at t=.1, source version, reading copy or full-paper audit is
imported. The reviewer contributed a convexity preflight observation;
its assessment is internal and shares that strategy and source premises.

**Actual-phase continuation, 19 November 2026.** Prepared for Edward Baker with Codex LLM assistance, 19 November 2026; root actual settings unavailable, B06 Astra/ultra and E18 proof/assessment Sol6.1/ultra explicit dispatches. The lead and separate assessor reopened selected [Polymath v2](https://arxiv.org/html/1904.12438v2) source passages; the assessment records Theorem1.2, definitions(6)–(10), Corollary6.4/(68)–(74), Proposition6.6 and Section8.5. Note23 derives the new explicit carrier derivatives and matrix-norm variation bounds locally, reusing the accepted finite Fourier mean and eight-prime witness. No new external theorem, source version, reading copy, t=.2 numerical constant at t=.1 or full-paper audit is imported.
