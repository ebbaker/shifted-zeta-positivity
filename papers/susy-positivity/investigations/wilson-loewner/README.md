# Wilson--Loewner: shifted-zeta evolution and Wilson lines

Working manuscript pair **0.4**, 20 September 2026. Drafted for Edward
Baker with OpenAI GPT-6 (Codex) assistance. Neither paper has received an
independent mathematical review.

- [Main exposition](manuscript.pdf), [LaTeX source](manuscript.tex):
  *Shifted-zeta evolution and Wilson lines: a Loewner realization program
  for cumulative positivity*.
- [Supplementary information](supplementary-information.pdf),
  [LaTeX source](supplementary-information.tex): detailed tools,
  derivations, restrictions and diagnostics.
- [Spatial radial-descent test](notes/SPATIAL_RADIAL_DESCENT_OBSTRUCTION_20260920.md)
  and [next-session handoff](notes/RESEARCH_CONTINUATION_AFTER_RADIAL_DESCENT_20260920.md):
  ordinary spatial dilation fails closure in the specified free Higgs
  hemisphere sector; the actual two-scalar state and 83 separate checks.
- [Predictive hemisphere-localization control](notes/PREDICTIVE_LOCALIZATION_HEMISPHERE_TEST_20260920.md):
  the preceding Gaussian/Mellin calculation and its conditional dictionary.
- [Research continuation for the next chat](notes/RESEARCH_CONTINUATION_20260920.md):
  prioritized directions, first calculations, and remaining proof obligations.
- [Fixed-window Wilson response calculation](notes/FIXED_WINDOW_WILSON_RESPONSE_OBSTRUCTION_20260920.md):
  a causal normalized readout, full local/pole matching conditions, and a
  scoped regularity obstruction; 31 additional research diagnostics.
- [Build guide](BUILD.md), [dated manuscript pairs](drafts/README.md),
  and [restructuring handoff](notes/MANUSCRIPT_SPLIT_AND_PROGRAM_20260920.md).
- [Adaptive EMA continuation](../critical-path/notes/EMA_SMOOTHING_AND_POSITIVITY_CONTINUATION_20260920.md):
  evaluation of boundary and path smoothing, exact filter-energy identities,
  sufficient limiting routes and 57 separate finite controls; not yet integrated
  into the manuscript pair.

The main exposition takes the exact arithmetic shift equation as the
prescribed effective evolution. The research hypothesis is that an
independently defined Wilson boundary observable on Loewner-generated
contours can realize that equation and admit a cumulative positive-norm
identity. A sequence of contractions with increasing length and vanishing
shift would imply central Weil positivity. No such physical realization,
norm identity or all-depth continuation has been established.

The arithmetic explanation of the decay rates and the local remainder
remains in Section 2.2. Both documents compile from this package; neither
loads a parent investigation or shared-background TeX source.

## Reading map

| Main exposition | Technical companion |
|---|---|
| Sections 1--3: proposal, normalization, exact shift and defect equations | S1: arithmetic conventions and complete Beta/comb/rational factorization |
| Section 4: physical transfer hypothesis and insertion closure | S3--S4: contour dictionary, rigidity, full smooth variation and controls |
| Section 5: fixed-window test and localization question | S10--S11: complete local/pole target, Gaussian response, scoped obstructions and auxiliary boson--fermion product |
| Section 6: spectral ingredients and constraints | S2, S5--S6: free kernel, Gaussian model, projectors and endpoint selection |
| Section 7: cumulative positivity and reflected amplitudes | S7--S8: adjoint, reference junction, reflection tests and bulk response |
| Section 8: depth--shift route and spatial gluing | S9: Schur, Cayley and simultaneous continuation algebra |
| Section 9: research agenda and statement ledger | S12--S13: 299 finite diagnostics and provenance |

The companion retains the detailed former Sections 3--9, together with
the arithmetic factorization and diagnostic appendix. Key constraints stay
visible in the exposition: the subtraction sign, same-charge endpoint
vanishing, conditional interacting reflection, and the incomplete physical
response. The current pair has 18 exposition pages and 33 supplementary pages.
Historical versions 0.1--0.3 remain unchanged.

The [shift-flow note](notes/SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md)
records the proposal that led to this split. The
[critical-path investigation](../critical-path/README.md) now contains the
adaptive-EMA evaluation and next-session continuation plan. The version 0.4
manuscript pair remains unchanged by that subsequent research.

## Underlying research

1. [Opening note](notes/OPENING_NOTE_20260919.md): relation to the two parent
   investigations, narrowed scope of the previous closure, and proof target.
2. [Smooth variation and the constant driver](notes/SMOOTH_VARIATION_AND_CONSTANT_DRIVER_20260919.md):
   the first calculations, proofs, controls and status ledger.
3. [Defect projectors and endpoint polarizations](notes/DEFECT_PROJECTORS_AND_ENDPOINT_POLARIZATIONS_20260919.md):
   contour freedom, the vanishing same-charge pairing, and adjoint controls.
4. [Reflection, junction and bulk response](notes/REFLECTION_JUNCTION_AND_BULK_RESPONSE_20260919.md):
   the physical reflected map, color gluing, scalar-rotation tests and a
   first nonzero bulk shape response.
5. [Third research continuation](notes/CONTINUATION_20260919_SESSION3.md): complete
   the endpoint and defect terms at the first interaction order.
   The [first](notes/CONTINUATION_20260919.md) and
   [second](notes/CONTINUATION_20260919_SESSION2.md) handoffs are preserved.

## Package map

| Location | Purpose |
|---|---|
| [notes](notes/README.md) | Dated research and continuation notes |
| [numerics](numerics/README.md) | Four manuscript diagnostic programs (299 cases), plus two subsequent localization research programs |
| [validation](validation/README.md) | Both-document build records, snapshots and package inventory |
| [reviews](reviews/README.md) | Independent reviews; none yet |
| [drafts](drafts/README.md) | Immutable standalone manuscript snapshots |

Run the portable checks from this directory:

    python3 validation/drafts.py check --replay

The broader live inventory is checked with:

    python3 validation/check_package.py check

The checks establish identity and reproduce finite diagnostic comparisons;
they do not prove the realization hypothesis, interacting positivity or RH.
See [BUILD_RECORD.json](BUILD_RECORD.json),
[MANUSCRIPT_SOURCES.json](MANUSCRIPT_SOURCES.json) and
[PACKAGE_RECORD.json](PACKAGE_RECORD.json).

The [shared background](../../background.pdf) fixes the arithmetic
normalization. The parent [Wilson-lines](../wilson-lines/README.md),
[Loewner](../loewner/README.md) and
[fractional-dimension](../fractional-dimension/README.md) investigations
remain source research for this program.
