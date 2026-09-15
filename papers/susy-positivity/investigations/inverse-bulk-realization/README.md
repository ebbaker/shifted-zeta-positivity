# Inverse bulk realization of the localized Weil form

15 September 2026. Fit the **complete** localized Weil pairing to an
independently positive field-theoretic or observable-sector norm.
The intended contribution is an exact matching theorem, potentially
conditional on construction of a credible specified theory. An already
completed construction is not an eligibility requirement.

The [current working manuscript](manuscript.pdf), *Sphere and Schur sources for
the localized Weil form*, collects the present results in a self-contained
draft. Its [TeX source](manuscript.tex) has internal equation labels and does
not input the shared background. Reviewed versions are preserved in
[drafts/](drafts/README.md); version 0.2 is current and version 0.1 is
preserved unchanged.
See the [build guide](BUILD.md) and [coverage map](MANUSCRIPT_COVERAGE.md).

Start with the [broad program overview](../../brainstorm/INVERSE_BULK_AND_DEFECT_DIRECTIONS.md)
for the ideas and alternatives. The
[current focused investigation](notes/SCHUR_DRESSED_RETURNS_AND_GLUING.md)
constructs dressed Schur return states, computes their full local norm,
and tests their magnetic domain and two-prime gluing.
No system has yet supplied the full Weil pairing. The working manuscript
records the preliminary source results and open joint matching problem;
it does not announce a completed reduction to a particular field theory.

## Reading map: broad material and focused calculations

| Document | Scope | Role |
|---|---|---|
| [Working manuscript](manuscript.pdf) | Synthesis of current results | Self-contained target, exact source calculations and proofs, scoped exclusions, and the remaining full matching problem. |
| [Dated drafts](drafts/README.md) | Version history | Complete buildable snapshots with PDFs and file hashes; earlier versions are preserved unchanged. |
| [Program overview in brainstorm](../../brainstorm/INVERSE_BULK_AND_DEFECT_DIRECTIONS.md) | Broad | Motivation, the conditional-construction goal, broadened boundary concepts, candidate families, and criteria for a specific paper. |
| [Defect-observable survey](notes/DEFECT_OBSERVABLE_SURVEY.md) | Broad | Literature comparison and alternatives, including Liouville, integrable defects, gauge networks, and arithmetic/free-field controls. |
| [Foundational analysis](notes/ANALYSIS.md) | General framework, with specific model tests | Full matching target, physical positivity, rational-feedback obstruction, positive gamma refinement, and the original junction proposal. |
| [Dressed Schur returns and gluing](notes/SCHUR_DRESSED_RETURNS_AND_GLUING.md) | Focused; current | One fixed Schur parameter, an exact positive local prime norm, its compulsory contact, magnetic domain requirements, and a mixed-return gluing test. |
| [Sphere and Schur pairings](notes/SPHERE_AND_SCHUR_PAIRINGS.md) | Focused; first comparison | Gaussian boundary gamma data, interacting rank-one norms, conformal Wilson pairing, Schur local-factor and common-state tests, and the next source choices. |
| [Gauge-transfer test](notes/GAUGE_TRANSFER_TEST.md) | Focused; earlier | Winding versus transfer, a positive disk model, and two first-prime preparations with exact mismatches. |
| [Notes index](notes/README.md) | Navigation | Reading order and the status of each retained note. |
| [Checks and records](numerics/README.md) | Supporting calculations | Small reproducible algebra programs and their explicitly scoped results. |

The latest note gives an explicit electric dressing and one magnetic
insertion whose positive norm has every required single-prime repetition
coefficient. All primes use the same Schur quantization parameter. The
norm also fixes the known positive contact: this is an explicit Schur
realization of the existing positive prime reference, not a full Weil
identity. A simple coherent sum produces forbidden mixed returns.

**Version 0.2 settles what that construction can become.** The manuscript now
records the target in spectral form, and proves that the architecture the
dressed construction leads to cannot be completed: by an elementary
interference bound, no coherent source has the positive gamma energy and the
summed positive prime references as its two channel norms. The bound fails at
explicit test functions --- the indicator of the interval already violates it
at \(L=5/4\) --- and fails by a growing factor as \(L\) increases. The
negative contact and the rank-two pole term must therefore come from a
compression or projection inside one space, not from further positive
channels. That, rather than another prime-channel identity, is the next
object to construct.

## Working direction

Continue with charge-neutral Schur RG/interface preparations that retain
the full gauge and Weyl terms, alongside sphere boundary/vortex modules
with an actual correspondence on the Gaussian normalization control.
Every candidate must now also pass the interference bound of Section 7.4
for each decomposition whose channel norms it computes separately, and must
produce the contact and the signed poles from one mechanism. Compare the
compressed-scaling-action mechanism of Connes and Consani, cited in the
manuscript, which produces a negative archimedean contact by projection.
A failed identity changes the choice of source or model;
it does not initiate progressively more complicated residual estimates.
Retain the other systems as alternatives. Use this working manuscript to
develop the current calculations; specialize the proposed field-theory
reduction when a concrete joint source and complete matching results justify it.
Only the forward construction-to-RH direction belongs to this program.

## Reproduction and preservation

Run from this directory:

```sh
python3 numerics/check_matching.py
python3 numerics/check_gauge_transfer.py
python3 numerics/check_sphere_schur.py
python3 numerics/check_dressed_schur.py
python3 numerics/check_explicit_formula.py
python3 numerics/check_channel_bound.py
python3 validation/drafts.py check --replay
```

The programs print small records and do not overwrite the preserved
results in `numerics/records/`. The three original research notes now
live in `notes/`, with their filenames retained and navigation repaired.
The earlier check programs and records are preserved unchanged; the
generic `checks.json` is now `numerics/records/matching-checks.json`.
Successive focused notes and their checks document each continuation separately.
The [draft tool](validation/README.md) records reviewed builds and saves new
versions without overwriting historical drafts.
Follow the repository's [large-file policy](../../../../LARGE_FILES.md).

Related material: [shared framework](../../PROGRAM_OVERVIEW.md),
[ground-state geometry](../arithmetic-ground-state-geometry/README.md),
[earlier assessment](../../brainstorm/ASSESSMENT.md), and
[finite-response novelty assessment](../../manuscripts/finite-response-weil-positivity/EVALUATION.md).
