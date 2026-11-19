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
