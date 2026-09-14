# Inverse bulk realization of the localized Weil form

14 September 2026. Fit the **complete** localized Weil pairing to an
independently positive field-theoretic or observable-sector norm.
The intended contribution is an exact matching theorem, potentially
conditional on construction of a credible specified theory. An already
completed construction is not an eligibility requirement.

Start with the [broad program overview](../../brainstorm/INVERSE_BULK_AND_DEFECT_DIRECTIONS.md)
for the ideas and alternatives. The
[current focused investigation](notes/SPHERE_AND_SCHUR_PAIRINGS.md)
tests sphere and Schur quantization using named boundary and line-operator
sectors. No system has yet supplied the full Weil pairing, and there is
no draft paper for a selected system in this folder.

## Reading map: broad material and focused calculations

| Document | Scope | Role |
|---|---|---|
| [Program overview in brainstorm](../../brainstorm/INVERSE_BULK_AND_DEFECT_DIRECTIONS.md) | Broad | Motivation, the conditional-construction goal, broadened boundary concepts, candidate families, and criteria for a specific paper. |
| [Defect-observable survey](notes/DEFECT_OBSERVABLE_SURVEY.md) | Broad | Literature comparison and alternatives, including Liouville, integrable defects, gauge networks, and arithmetic/free-field controls. |
| [Foundational analysis](notes/ANALYSIS.md) | General framework, with specific model tests | Full matching target, physical positivity, rational-feedback obstruction, positive gamma refinement, and the original junction proposal. |
| [Sphere and Schur pairings](notes/SPHERE_AND_SCHUR_PAIRINGS.md) | Focused; current | Gaussian boundary gamma data, interacting rank-one norms, conformal Wilson pairing, Schur local-factor and common-state tests, and the next source choices. |
| [Gauge-transfer test](notes/GAUGE_TRANSFER_TEST.md) | Focused; earlier | Winding versus transfer, a positive disk model, and two first-prime preparations with exact mismatches. |
| [Notes index](notes/README.md) | Navigation | Reading order and the status of each retained note. |
| [Checks and records](numerics/README.md) | Supporting calculations | Small reproducible algebra programs and their explicitly scoped results. |

The latest note identifies the exact quarter-shift gamma factor in a
real boundary module and the local Euler factor in a Schur shift identity.
Their actual positive pairings differ from the target under the tested
source prescriptions. The most useful new tool is the Schur RG description
of the full pairing through a common state. It fixes interference and
normalization together, and motivates a more specific source calculation.
These are preliminary model-selection results, not a new RH reduction.

## Working direction

Continue with sphere boundary/vortex modules and Schur RG or interface
preparations. A failed identity changes the choice of source or model;
it does not initiate progressively more complicated residual estimates.
Retain the other systems as alternatives. Specialize a draft paper only
after a concrete system and preliminary matching results justify it.
Only the forward construction-to-RH direction belongs to this program.

## Reproduction and preservation

Run from this directory:

```sh
python3 numerics/check_matching.py
python3 numerics/check_gauge_transfer.py
python3 numerics/check_sphere_schur.py
```

The programs print small records and do not overwrite the preserved
results in `numerics/records/`. The three original research notes now
live in `notes/`, with their filenames retained and navigation repaired.
The earlier check programs and records are preserved unchanged; the
generic `checks.json` is now `numerics/records/matching-checks.json`.
The new note and check document the current investigation separately.
Follow the repository's [large-file policy](../../../../LARGE_FILES.md).

Related material: [shared framework](../../PROGRAM_OVERVIEW.md),
[ground-state geometry](../arithmetic-ground-state-geometry/README.md),
[earlier assessment](../../brainstorm/ASSESSMENT.md), and
[finite-response novelty assessment](../../manuscripts/finite-response-weil-positivity/EVALUATION.md).
