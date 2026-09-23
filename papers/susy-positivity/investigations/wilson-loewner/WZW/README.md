# Thermal arithmetic orbit weights and the shifted-zeta equation

The live [manuscript](manuscript.pdf), **Thermal arithmetic orbit weights and the shifted-zeta equation: Bost–Connes coefficients and the causal realization problem**, now starts with and focuses on the current orbit-weight investigation. The editable entry point is [manuscript.tex](manuscript.tex). This is a 12-page revision prepared for Edward Baker with GPT-6 (Codex) assistance, 23 September 2026.

The central result is the exact identity `c_n(omega) = n^((beta-1)/2) phi_beta(P_n)`, with `beta = 2 omega`: native primitive thermal probabilities supply all the required Euler coefficients after explicit centering. The manuscript derives that identity, the finite-place positive model, the local ordinary norms, the failure of a particular common product embedding, and the noncontractivity of the bare Euler delay train. It then specifies the unresolved coupling to an archimedean radiation channel. A causal completed physical realization is not claimed.

Section 6 gives a brief retrospective on the WZW collar, direct arithmetic Loewner source, Brownian readouts, cusp load, fractional clock and scalar holonomy tests, with references to their detailed notes. The modular Hodge half-shift realization is retained as a positive benchmark; the failed cusp deformation is distinguished from that result. Appendix A documents the existing 87-case orbit-weight diagnostic, historical suite counts, provenance and LLM assistance. No new numerical experiment is claimed for this editorial integration.

## Current research and verification

- [Orbit-weight research note](notes/ARITHMETIC_ORBIT_WEIGHTS_AND_BOST_CONNES_TEST_20260923.md), [87 controls](numerics/records/arithmetic-orbit-weights-20260923.json), [diagnostic](numerics/check_arithmetic_orbit_weights.py), and [research audit](reviews/review_codex_arithmetic_orbit_weights_20260923.md).
- [Current manuscript audit](reviews/review_codex_thermal_manuscript_20260923.md), including claim boundaries and page review. All audits are by the same assistant; no independent specialist review has been completed.
- [Build instructions](BUILD.md), [build identity record](BUILD_RECORD.json), and [concise milestone index](DRAFT_HISTOR.md).
- [Notes index](notes/README.md), [numerical replay instructions](numerics/README.md), and [reviews index](reviews/README.md).

## Detailed earlier investigations

| Investigation | Detailed record |
|---|---|
| Fractional cusp field | [Positive memory law, leading match and scalar-clock exclusion](notes/CONTINUOUS_EXPONENT_AND_FRACTIONAL_CUSP_TEST_20260923.md) |
| Modular Hodge scattering | [Exact half-shift channel, unsuccessful cusp load and corrected earlier quadratures](notes/MODULAR_HODGE_SCATTERING_AND_CUSP_COUPLING_TEST_20260923.md) |
| Brownian bridge readout | [Causal first-passage response, arithmetic mismatch and logarithmic phase](notes/BROWNIAN_BRIDGE_READOUT_TEST_20260923.md) |
| Independent-source search | [Primary-literature comparison and candidate selection](notes/INDEPENDENT_ARITHMETIC_SOURCE_SEARCH_20260923.md) |
| Bounded WZW collar | [Full-module reflected readout and primary spectral exclusion](notes/BOUNDED_ARITHMETIC_READOUT_TEST_20260923.md) |
| Direct arithmetic source | [Generalized Loewner flows, shift equation and operator-norm limitations](../notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md) |
| Original WZW pilot | [Deterministic SU(2) level-2 calculation](../notes/SU2_LEVEL2_DETERMINISTIC_LOEWNER_PILOT_20260922.md) |

The detailed notes retain their original research dates and status statements; the present manuscript incorporates the current result and summarizes the earlier tests. The original [continuation note](notes/CONTINUATION_AFTER_WZW_WRITEUP_20260923.md) and [first manuscript audit](reviews/review_codex_manuscript_20260923.md) describe the preceding WZW-led synthesis. The earlier seven section fragments remain in `sections/` for provenance but are no longer loaded by the current entry point; the build record distinguishes them from active TeX inputs. No dated manuscript snapshot is created.

New research belongs in `notes`, numerical work in `numerics`, and reviews in `reviews`. The parent [Wilson–Loewner manuscript](../README.md) remains unchanged by this revision.
