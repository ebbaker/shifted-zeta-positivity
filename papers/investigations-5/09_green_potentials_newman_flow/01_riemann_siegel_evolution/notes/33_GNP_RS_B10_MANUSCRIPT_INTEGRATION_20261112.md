# B10 manuscript integration and source crosswalk

12 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, including separate integration
contributors. Child chat0008. Actual model and reasoning effort are
unavailable in the recorded configurations.

The [live manuscript, §14][manuscript] integrates the audited \(c=1\)
translated residual theorem and its Green corollary. For fixed
\(0<\rho\le47/162\), the admissible interval lengths are
\(U^{17/81+\rho}\le\ell\le U\). The theorem is uniform in
\(2\le P\le\lfloor L_U^2\rfloor\) with \(P\) constant on the outer
interval. The Green corollary uses \(P_U=\lfloor L_U^2\rfloor\)
throughout, so the omitted-prime allowance is \(O(L_U^{-3})\).
The original geometry and physical time \(1/L_X\) within each spatial
window carry through. At the block cutoff the residual-mean error is
\(O_\rho(L_U^{-3/2})\), the Green mean is \(O_\rho(L_U^{-1/3})\) and
the fixed-threshold exceptional proportion is \(O_{h,\rho}(L_U^{-1})\).

| Manuscript input | Checked source |
| --- | --- |
| Integer cutoff, contour and pole, uniform kernel moments, cumulative translated mean and real quadratic bound | [B10 §§1–3][b10], [audit §§1–2][audit], [Bourgain–Watt v1 Theorem 4 and journal record][bw] |
| Smaller coefficients, both convex endpoints, all shifts and pairs, complete cutoff freezing | [B07 §§2–4][b07], [B08 §§2–4][b08], [B10 §4][b10], [audit §3][audit], [Montgomery–Vaughan][mv] |
| Finite head and multiplier tails, physical clock and complete field, exact Fubini weight and mass | [B06 §§2–6][b06], [B07 §§2, 5][b07], [B10 §5][b10], [audit §4][audit] |
| Closed overlap \(\ell\ge\sqrt U\), cutoff-aware Green transfer and exceptional proportion | [B08 §5][b08], [B10 §5][b10], [audit §4][audit], [manuscript §13's Euler master bound][euler] |

The [result index][results] and [heat-flow cluster11][cluster] place
this averaged quantitative milestone alongside the earlier results.
The [avoid index][avoid], [premise02][a02], [separate-bounds12][a12]
and [controls12][controls] are applied through [audit §5][audit].
The named controls fail the canonical source or physical-readout inputs
specified there. No event test is inferred from the mean theorem.
B09's parameter exclusion applies to its original setup and is not
needed for §14. The Mellin estimate concerns the complete real
quadratic correlation, with individual complex-block moduli outside
its scope.

The [verification][review] and [build record][build] identify the
reading copy and the checked layout, references and mathematical
interfaces. The published inputs, HDA provider and inherited log
transfer retain their original review scopes. The integration adds no
evaluated onset, time-zero result, shrinking-depth estimate or
all-centers bound. The next substantive question is whether a positive
defect persists along \(X\mapsto(1/L_X,X)\) long enough to contradict
the permitted mass or exceptional measure. See the [model-change
return][return] for the proposed comparison and GPT-6 Astra research
recommendation.

[euler]: ../../manuscript/sections/10c_euler_references.tex
[manuscript]: ../../manuscript/sections/10d_short_window_means.tex
[b06]: 21_GNP_RS_B06_GROWING_CUTOFF_MEAN_20261112.md
[b07]: 23_GNP_RS_B07_LOCALIZED_TAIL_AND_EXACT_BOUNDARY_20261112.md
[b08]: 25_GNP_RS_B08_EXPONENT_PAIR_LOCALIZATION_20261112.md
[b10]: 29_GNP_RS_B10_SIGNED_MELLIN_MEAN_ESTIMATE_20261112.md
[audit]: 31_GNP_RS_B10_PREINTEGRATION_PROOF_AUDIT_20261112.md
[return]: 32_GNP_RS_B10_AUDIT_RETURN_AND_MODEL_CHANGE_20261112.md
[bw]: ../references/02_GNP_RS_B08_EXPONENT_PAIR_SOURCE_USE_20261112.md
[mv]: ../references/03_GNP_RS_B10_EXPONENT_PAIR_AUDIT_SOURCE_20261112.md
[review]: ../reviews/17_GNP_RS_B10_MANUSCRIPT_VERIFICATION_20261112.md
[build]: ../../numerics/03_GNP_RS_B10_INTEGRATION_BUILD_RECORD_20261112.json
[results]: ../../../../../result-summaries/README.md
[cluster]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[avoid]: ../../../../../avoid/README.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
