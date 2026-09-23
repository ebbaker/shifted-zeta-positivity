# WZW and the arithmetic Loewner source

The [arithmetic orbit-weight test](notes/ARITHMETIC_ORBIT_WEIGHTS_AND_BOST_CONNES_TEST_20260923.md) derives all required Euler coefficients from Bost–Connes primitive thermal projections with an explicit centering factor. This supplies an independently motivated coefficient law, while its causal scattering interface and archimedean coupling remain unresolved. The bare Euler readout is noncontractive, and the naive common Haar-product state family fails to converge. See the [87 controls](numerics/records/arithmetic-orbit-weights-20260923.json) and [same-assistant audit](reviews/review_codex_arithmetic_orbit_weights_20260923.md). Neither limitation excludes the abstract positive KMS states or a different coupled realization.

The [continuous-exponent field test](notes/CONTINUOUS_EXPONENT_AND_FRACTIONAL_CUSP_TEST_20260923.md) derives a positive fractional memory law that varies the leading power continuously. Its modular clock response passes the leading front test but fails the subleading term, unit boundary modulus, fixed first-prime delay and identity endpoint. A scoped analytical obstruction covers scalar complete-Bernstein clocks. See the [80 floating controls](numerics/records/fractional-cusp-20260923.json) and [same-assistant audit](reviews/review_codex_fractional_cusp_20260923.md). This does not exclude general unitary geometric or additional-channel deformations.

The [modular Hodge scattering test](notes/MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) supplies the exact half-shift transfer in a native gradient-field channel with a causal ordinary radiation norm. A real cusp delta load preserves losslessness but fails the arithmetic shift tangent. See the [65 controls](numerics/records/modular-scattering-20260923.json) and [same-assistant audit](reviews/review_codex_modular_scattering_20260923.md). The note also documents a general-shift quadrature correction and successful full replays of the 60-case bounded and 51-case Brownian suites. This fixed-shift result does not establish a variable-shift physical realization.

The [Brownian bridge readout test](notes/BROWNIAN_BRIDGE_READOUT_TEST_20260923.md) derives a native two-exit response with causal propagation and an exact ordinary norm balance, then excludes its arithmetic match by the short-delay and first-prime kernels. A separate logarithmic readout recovers the arithmetic boundary phase, with causality still unestablished. Its [51 floating controls](numerics/records/brownian-readout-20260923.json) and [same-assistant audit](reviews/review_codex_brownian_readout_20260923.md) are separate from the manuscript.

The [independent arithmetic-source search](notes/INDEPENDENT_ARITHMETIC_SOURCE_SEARCH_20260923.md) compares Brownian bridge moments, modular cusp scattering, adelic scaling, statistical-mechanical models, and other physical constructions. It derives the full scalar source from a Brownian observable and an exact modular-scattering match at shift 1/2, while identifying the missing causal readout or variable-shift mechanism. It recommends a bounded Brownian response test, with modular scattering as a benchmark. This literature addendum is separate from the manuscript PDF.

The [bounded arithmetic-readout test](notes/BOUNDED_ARITHMETIC_READOUT_TEST_20260923.md), completed later on 23 September, specifies a ground-normalized collar on the full boundary module. It proves a physical norm balance but excludes its fixed reflected readout as a causal arithmetic transfer. The selected primary has the wrong gamma weights and no first-prime delay. See the [audit](reviews/review_codex_bounded_readout_20260923.md) and [60 separate controls](numerics/records/boundary-readout-20260923.json). This research addendum is not incorporated into the manuscript PDF.

The standalone [manuscript](manuscript.pdf), **Boundary WZW evolution and the arithmetic Loewner source**, assembles the current results without extending the parent Wilson--Loewner manuscript. The editable entry point is [manuscript.tex](manuscript.tex); all TeX inputs are local to this folder. Prepared for Edward Baker with GPT-6 (Codex) assistance, 23 September 2026. No independent specialist review has been completed.

The write-up covers:

- The specified SU(2) level-2 boundary theory, selected algebraic blocks, complete deterministic Loewner generator, and constant-driver tensor norm balance.
- Moving-driver growth, exact composition and fusion, the distinct Chern--Simons pairing, and the compact initial limit of the raw spatial kernel.
- Generalized Loewner flows from the shifted completed xi logarithmic derivative, recovery of the full arithmetic source, and the flow linearized by log xi.
- The RH-equivalent zero-shift condition, the obstruction to a positive instantaneous arithmetic generator, and the available weighted operator bound.
- A concrete next target: a cumulative boundary or canonical response with the unweighted arithmetic norm.

These are the existing 22 September calculations presented together. This editorial integration does not claim a new physical realization, a proof of RH, or a new numerical experiment. The two existing numerical records contain 132 passing finite controls: 11 exact rational and 121 floating. Their scope is stated in the manuscript appendix.

## Working here

- [Build instructions](BUILD.md) and [build identity record](BUILD_RECORD.json).
- [Notes for further investigation](notes/README.md), beginning with the [current continuation](notes/CONTINUATION_AFTER_WZW_WRITEUP_20260923.md).
- [Internal manuscript audit](reviews/review_codex_manuscript_20260923.md).
- [Concise milestone index](DRAFT_HISTOR.md). Future milestones should use commits or tags; no dated manuscript snapshots are created.

New research notes for this branch belong in `WZW/notes`; new numerical work belongs in `WZW/numerics` when needed, and reviews in `WZW/reviews`. The historical inputs below remain in their original locations so existing citations and provenance remain valid.

## Preserved research inputs

| Input | Record or audit |
|---|---|
| [Chern--Simons/WZW proposal](../notes/CHERN_SIMONS_WZW_AND_NATURAL_LOEWNER_EVOLUTION_20260922.md) | Original proposed pilot |
| [Completed SU(2)_2 pilot](../notes/SU2_LEVEL2_DETERMINISTIC_LOEWNER_PILOT_20260922.md) | [72 checks](../numerics/records/wzw-loewner-pilot-20260922.json), [program](../numerics/check_wzw_loewner_pilot.py), [audit](../reviews/review_codex_wzw_loewner_pilot_20260922.md) |
| [Direct arithmetic-source investigation](../notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md) | [60 checks](../numerics/records/arithmetic-loewner-source-20260922.json), [program](../numerics/check_arithmetic_loewner_source.py), [audit](../reviews/review_codex_arithmetic_loewner_source_20260922.md) |
| [Parent Wilson--Loewner investigation](../README.md) | Broader physical program and causal arithmetic conventions |

See [BUILD.md](BUILD.md) for the separate diagnostic replay commands. The existing programs and records are linked rather than duplicated.
