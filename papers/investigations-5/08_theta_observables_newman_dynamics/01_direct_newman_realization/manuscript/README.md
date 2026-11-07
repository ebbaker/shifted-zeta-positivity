# Conditional Newman dynamics: analytical manuscript

6 November 2026. Drafted for **Edward Baker** with substantial LLM assistance. Current integration **TND-D-E08**: primary **gpt-6-astra / ultra**, TeX synthesis **gpt-6.1-sol / ultra**, direct chat0004. The initial E05 synthesis used Astra/max, direct chat0003.

[main.tex](main.tex) is the single evolving manuscript. The current [24-page reading PDF](../../../../../output/pdf/08_theta_observables_newman_dynamics/direct_newman_realization/conditional_newman_dynamics.pdf) includes the assessed high-count phase and complete count-tail results. It builds with no warnings or unresolved references; all pages were rendered and visually checked. [BUILD_RECORD.json](BUILD_RECORD.json) identifies the exact source and PDF versions. The initial 18-page build record is preserved in the `previous_build_record` field of [E08's input receipt](../research-progress/handoffs/13_TND_D_E08_INPUTS_20261106.json). Keep this manuscript evolving and record milestones in [DRAFT_HISTORY.md](../DRAFT_HISTORY.md), without snapshot folders.

The [parent manuscript](../../manuscript/main.tex) supplies common background. The direct paper develops complete preparation and the count instrument, calibrated observation, collision diagnostics, the exact colliding control, and the new scalar count results. No numerical research experiment is used.

| Manuscript source | Development and principal inputs |
| --- | --- |
| [Introduction](sections/01_introduction.tex) | Questions, quantitative results, assumptions and separate evidence levels |
| [Preparation](sections/02_preparation.tex) | Complete cylinder/source bounds, square-root regularity and full energy moments from [E01 Note02](../notes/02_TND_D_E01_R1_CONDITIONAL_QUADRATURE_REALIZATION_20261106.md) |
| [Instrument](sections/03_instrument.tex) | Signed Kraus operations, complete count sum, aggregation, domains and strong no-count law |
| [Observation](sections/04_observation.tex) | Conditional source, absolute calibration, density cosine, covariance and state motion |
| [Count calculus](sections/05_count_calculus.tex) | Signed moments, generating identity, transfer laws and the whole-channel kernel; evidence scopes distinguished |
| [Collisions](sections/06_collisions.tex) | Double-event balances, fold, root tracking, variance, source sectors and higher multiplicity from [Note04](../notes/04_TND_D_B02_COLLISION_DYNAMICS_RECONNAISSANCE_20261106.md) |
| [Control](sections/07_control.tex) | Exact reflected colliding witness, complete domains and premise-specific limitations |
| [Canonical count phases and complete-tail errors](sections/08_high_count_results.tex) | Full proofs from [Note06](../notes/06_TND_D_E03_HIGH_COUNT_LOCALIZATION_20261106.md) and [Note07](../notes/07_TND_D_E06_COMPLETE_COUNT_TAIL_20261106.md), score nonindependence, prior scalar-center attribution and identical direct baseline |
| [Outstanding tasks](sections/08_outstanding.tex) | Independent joint source premise, B03 decision, multiplicities/ranges, analytical versus physical access and evidence boundaries |

The realization retains [E02's internal conditional assessment](../reviews/01_TND_D_E02_CONDITIONAL_REALIZATION_ASSESSMENT_20261106.md). [E04 Review03](../reviews/03_TND_D_E04_HIGH_COUNT_ASSESSMENT_20261106.md) and [E07 Review04](../reviews/04_TND_D_E07_COMPLETE_COUNT_TAIL_ASSESSMENT_20261106.md) accept the new count results within scope. One separate Sol/ultra reviewer assessed both, with shared premises and no specialist independence. Other fold, higher-multiplicity, finite-transfer and whole-channel kernel diagnostics retain proof-author status. [E08 production review](../reviews/05_TND_D_E08_MANUSCRIPT_INTEGRATION_20261106.md) does not upgrade those levels.

The phase theorem excludes eventual one-sign literal count sectors at fixed nonzero real k. The tail theorem gives absolute value/first-derivative errors on the closed time slab and all real k. Neither supplies a relative collision margin, physical post-count access, practical computed cutoff or improvement over identical scalar source analysis.

For the next session, start with [Continuation08](../notes/08_TND_D_RESULTS_AND_B03_BRAINSTORM_CONTINUATION_20261106.md): **[B] TND-D-B03 — Astra/ultra**, ready but unactivated. B02/E03/E04 and E06/E07 are complete. Potential E09/E10 require a fixed B03 contract; existing bounded follow-through authorization persists.

## Rebuild

From the repository root:

```sh
bash papers/investigations-5/08_theta_observables_newman_dynamics/01_direct_newman_realization/manuscript/build.sh
```

[build.sh](build.sh) combines the branch manuscript, parent internal, canonical MC11 and branch measurement bibliographies under ignored root `output/pdf/`, then uses TeX Live's `latexmk`, `pdflatex`, BibTeX and `plainurl.bst`. Generated PDFs and intermediates stay outside manuscript source folders and Git.

[E08 source use](../references/03_TND_D_E08_MANUSCRIPT_SOURCE_USE_20261106.md), [request](../research-progress/handoffs/13_TND_D_E08_MANUSCRIPT_AND_CONTINUATION_REQUEST_20261106.md), [return](../research-progress/handoffs/13_TND_D_E08_RETURN_20261106.json) and the [sole progress register](../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md) retain provenance. The [initial E05 review](../reviews/02_TND_D_E05_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261106.md) and [source-use receipt](../references/02_TND_D_E05_MANUSCRIPT_SOURCE_USE_20261106.md) remain historical evidence.
