# Localized zero correlations: current analytical manuscript

9 November 2026, America/New_York. Drafted for **Edward Baker**, with substantial OpenAI Codex LLM assistance. E14 r1, OC chat0011; recorded thread settings **gpt-6-astra / max**, per-turn backend configuration unavailable. Single-writer analytical integration and proof-author checking; no independent assessment or model change in this turn.

The current **48-page manuscript** develops the full factorial observable, complete-source approximation, the missing same-center joint input, Newman-time regularity through collisions, and two finite acquisition error theorems. Analytical derivations are primary. The finite census and conditional numerical budgets appear in Appendix G; the scalar itself remains uncomputed.

Editable source: [main.tex](main.tex). Regenerate from this investigation with `sh manuscript/build.sh`. The [PDF reading copy](../../../../../../output/pdf/08_theta_observables_newman_dynamics/localized_zero_correlations/localized_zero_correlations.pdf) is ignored output under [LARGE_FILES](../../../../../../LARGE_FILES.md). [BUILD_RECORD.json](BUILD_RECORD.json) identifies its sources and checks. The E05 and E06/E07 manuscript checkpoints remain historical; E14 supersedes their live presentation and build record in place, without a snapshot folder.

## Analytical development

| Location | Result and purpose | Source |
| --- | --- | --- |
| Sections 1–3 | Complete theta divisor, weighted full hierarchy, multiplicity/self corrections, observation heat and declared center covariance | [Framework](sections/01_framework.tex), [marginals](sections/10_gaussian_marginals.tex), [centers](sections/11_center_averaging.tex) |
| Sections 4–6 | Local logarithm stability, complete arithmetic/radial source tails, two-sided uniform pair approximation | [Log lemma](sections/03_logarithms.tex), [canonical source](sections/04_canonical.tex), [pair transfer](sections/12_full_pair_transfer.tex) |
| Section 7 | Fourier input, center-edge cost, scoped harmonic obstruction, polynomial log error and same-center moment accuracy theorem | [Joint-source derivation](sections/14_joint_source.tex) |
| Section 8 | Paired-force cancellation, explicit full/connected time moduli, Hermite assembly and complete exterior error | [Newman-time theorem](sections/15_newman_time.tex) |
| Section 9 | Gaussian physical window, exact center integration, zero/log tails and the separately marked projection | [Gaussian projection](sections/16_gaussian_projection.tex) |
| Section 10 | Explicit theta/Jensen tail; centroid error (18N+5)S2/T; direct cell-range radius <N(10u+4v)sqrt(pi)/(sT) | [Finite acquisition](sections/17_finite_acquisition.tex) |
| Section 11 | Control premises, evidence limits and outstanding analytical tasks | [Outstanding tasks](sections/08_outstanding.tex) |
| Appendices A–G | Ensemble/arithmetic comparisons, earlier scalar results, source status and supporting finite census | [Evidence appendix](sections/09_provenance.tex) |

The compact physical window, Gaussian physical window, Gaussian observation blur and Newman time are kept distinct. The time theorem is for the fixed compact window. The Gaussian projection integrates the entire observation plane, not just Q². Singleton separation is a hypothesis of the range theorem, while the centroid theorem permits unresolved multiple labels. Source approximation and a finite acquisition contract do not determine a canonical full profile.

## Evidence and continuation

Read the [result index](../../../../../../result-summaries/README.md) and [avoid index](../../../../../../avoid/README.md), particularly [cluster11](../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [geometry13](../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md), [classification01](../../../../../../avoid/01_restating_the_target.md), [scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [status19](../../../../../../avoid/19_status_files_that_lag_the_findings.md).

E02/E07/E08/E12 retain their individual internal acceptance scopes. Gaussian-window and acquisition Notes18–20/22, the arbitrary-separation statement and the present integration remain **proved in-note, proof-author checked**. E03/E04 remain pending. [Note23](../notes/23_TND_OC_E14_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261109.md) and [Review19](../reviews/19_TND_OC_E14_MANUSCRIPT_AUTHOR_CHECK_20261109.md) give the synthesis and checks. The original E13 failed gate and census evidence are unchanged; no new canonical evaluation was run.

Recommended analytical successor: **[E] TND-OC-E15 r1 / GPT-6.1 Sol**, a bounded seven-group claim audit under [Request32](../research-progress/handoffs/32_TND_OC_E15_R1_MANUSCRIPT_ASSESSMENT_REQUEST_20261109.md). **E13 r2 / Sol** remains the separate supporting endpoint evaluation under its original caps and routing-only input refresh. Both are ready, unactivated. [Continuation26](../continuation-notes/26_TND_OC_AFTER_E14_MANUSCRIPT_AND_MODEL_CHANGE_20261109.md) gives the complete model-change handoff and outstanding research tasks.
