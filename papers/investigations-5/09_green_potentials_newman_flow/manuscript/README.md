# Current analytical manuscript

Established 10 November 2026. The live manuscript incorporates the audited B10 averaged theorem as of 12 November 2026, America/New_York. Prepared for Edward Baker with substantial OpenAI Codex assistance. Actual model and effort are unavailable in chat0008.

**Green Potentials and Arithmetic Observations in the Newman Flow**, drafted for Edward Baker. Read [the PDF](../../../../output/pdf/09_green_potentials_newman_flow/green_potentials_newman_flow.pdf); [main.tex](main.tex) is the live source. The current 68-page build, hash and checks are in the [12 November build record](../numerics/03_GNP_RS_B10_INTEGRATION_BUILD_RECORD_20261112.json). The [opening build](../numerics/01_GNP_MANUSCRIPT_BUILD_RECORD_20261110.json) and [11 November build](../numerics/02_GNP_RS_INTEGRATION_BUILD_RECORD_20261111.json) document earlier drafts.

| Sections | Development |
| --- | --- |
| 1–3 | Question, complete source, geometric/scalar origin, calibrated operator and energy |
| 4 | Logarithmic fields, double/higher collisions, signed coefficients and lobe scales |
| 5–6 | Complete Green identity, defect margin, exact prime baseline and pole cancellation |
| 7–9 | Log acquisition through zeros, finite-source assembly, contour deflation and integration |
| 10 | Critical-strip RS, saddles, Newman evolution and increasing-order logarithmic transfer |
| 11 | Transition-scale harmonic carrier, complete field input, uniform outer baseline, logarithmic transfer and shifted divisor |
| 12 | Coherent moment law, exact Jensen and phase-only obstructions, fixed-prefix transfer |
| 13 | Euler calibration, joint phase, fixed-P mean and density, power/exponential mean consequences, exceptional residuals and adaptive costs |
| 14 | Translated short-window residual and Green means at (c=1) |
| 15–17 | Scoped conditioning obstruction, short-mollifier floor/correction and quadratic acquisition |
| 18–20 | Parallel inputs, defect resolution, evidence/controls and current outstanding tasks |

The [source map](../notes/01_GNP_SOURCE_MAP_AND_INTEGRATION_20261110.md) gives exact inherited sources/statuses. No new numerical campaign, RH result, signed canonical smallness or independent review is claimed.

Build from the repository with:
~~~sh
bash papers/investigations-5/09_green_potentials_newman_flow/manuscript/build.sh
~~~
LaTeX/BibTeX output and page renders stay in ignored output/pdf. The bibliography is generated from canonical homes; see [references](../references/README.md). The [same-assistant production check](../reviews/01_GNP_OPENING_MANUSCRIPT_SELF_CHECK_20261110.md) is separate from the unactivated GNP-E02 assessment. [Continuation prompts](../notes/02_GNP_CONTINUATION_AND_PROMPTS_20261110.md) are ready.

The [11 November integration and derivation](../01_riemann_siegel_evolution/notes/19_GNP_RS_MANUSCRIPT_AND_AVERAGED_GREEN_VALUES_20261111.md) maps the E01–E06 sources. The [same-assistant check](../01_riemann_siegel_evolution/reviews/10_GNP_RS_MANUSCRIPT_AND_MEAN_SELF_CHECK_20261111.md) preserves the inherited review scopes. At c=1 the actual Green potential tends to zero in every finite power mean; this does not estimate every center. No numerical research or new exceptional-center mechanism was produced.

The [short-window theorem](sections/10d_short_window_means.tex) uses the
audited B10 proof to extend the quantitative residual mean to
`ell ≥ U^(17/81+rho)` at `c=1`. Its Green mean and fixed-threshold
corollaries explicitly use `P_U = floor(L_U²)` throughout the outer interval.
The [pre-integration assessment](../01_riemann_siegel_evolution/reviews/16_GNP_RS_B10_PREINTEGRATION_ASSESSMENT_20261112.md)
identifies the named published and inherited inputs. The every-center
Green estimate remains open.
