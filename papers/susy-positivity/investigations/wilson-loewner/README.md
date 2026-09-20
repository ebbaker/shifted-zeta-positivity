# Wilson--Loewner: shifted-zeta evolution and Wilson lines

Working manuscript pair **0.5**, 20 September 2026. Drafted for Edward
Baker with OpenAI GPT-6 (Codex) assistance. Neither paper has received an
independent mathematical review.

- [Main exposition](manuscript.pdf), [LaTeX source](manuscript.tex):
  *Shifted-zeta evolution and Wilson lines: a Loewner realization program
  for cumulative positivity*.
- [Supplementary information](supplementary-information.pdf),
  [LaTeX source](supplementary-information.tex): detailed tools,
  derivations, restrictions and diagnostics.
- [Gaussian pair-interface endpoint response](notes/GAUSSIAN_PAIR_INTERFACE_ENDPOINT_RESPONSE_20260920.md):
  a specified neutral Gaussian preparation excites an infinite protected
  composite tower, but the charged endpoint fixes nonuniform weights and
  fails the omitted-channel test; [source audit](reviews/review_codex_endpoint_sources_20260920.md)
  and [latest handoff](notes/RESEARCH_CONTINUATION_AFTER_GAUSSIAN_ENDPOINT_20260920.md).
  This research addendum preserves the version-0.5 manuscript pair.
- [Hodge radial channel and program assessment](notes/HODGE_RADIAL_CHANNEL_AND_PROGRAM_ASSESSMENT_20260920.md):
  canonical protected evolution exists, but loses the higher elementary spatial
  modes; a matching composite-state character is not an endpoint response.
- [Version 0.5 integration and handoff](notes/LOCALIZATION_RESULTS_MANUSCRIPT_INTEGRATION_20260920.md).
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
  sufficient limiting routes and 57 separate finite controls. The subsequent
  all-input EMA anchor and unresolved append estimate are summarized in
  main Section 8.4 and SI S9.5.

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
| Section 5: fixed-window test and localization question | S10--S12: complete local/pole target, Gaussian response, scoped obstructions, auxiliary product and predictive localization controls |
| Section 6: spectral ingredients and constraints | S2, S5--S6: free kernel, Gaussian model, projectors and endpoint selection |
| Section 7: cumulative positivity and reflected amplitudes | S7--S8: adjoint, reference junction, reflection tests and bulk response |
| Section 8: depth--shift route and spatial gluing | S9: Schur, Cayley and simultaneous continuation algebra |
| Section 9: research agenda and statement ledger | S13--S14: 299 original finite diagnostics, three additional localization controls and provenance |

The companion retains the detailed former Sections 3--9, together with
the arithmetic factorization and diagnostic appendix. Key constraints stay
visible in the exposition: the subtraction sign, same-charge endpoint
vanishing, conditional interacting reflection, and the incomplete physical
response. The current pair has 20 exposition pages and 39 supplementary pages.
Historical versions 0.1--0.4 remain unchanged.

The [shift-flow note](notes/SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md)
records the proposal that led to this split. The
[critical-path investigation](../critical-path/README.md) now contains the
adaptive-EMA anchor and cumulative append investigation. Version 0.5 imports
these internally checked results with their review status; it does not claim
an all-input coupling bound or an all-depth continuation.

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
| [numerics](numerics/README.md) | Four manuscript diagnostic programs (299 cases), plus three separately replayed localization control programs |
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
