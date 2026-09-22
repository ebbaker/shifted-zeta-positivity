# Wilson--Loewner: shifted-zeta evolution and Wilson lines

Live revision of manuscript pair **0.5**, 21 September 2026; **no new
dated draft saved**. The archived version 0.5 of 20 September is unchanged.
Drafted for Edward Baker with OpenAI GPT-6 (Codex) assistance. Neither paper has received an
independent mathematical review.

- [Main exposition](manuscript.pdf), [LaTeX source](manuscript.tex):
  *Shifted-zeta evolution and Wilson lines: a Loewner realization program
  for cumulative positivity*.
- [Supplementary information](supplementary-information.pdf),
  [LaTeX source](supplementary-information.tex): detailed tools,
  derivations, restrictions and diagnostics.
- [Genuine Loewner growth in fixed Yang--Mills theory](notes/GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md): the current physical research direction, deriving a quantum insertion hierarchy for an actual growing trace and a specified return chord; [next-session handoff](notes/RESEARCH_CONTINUATION_AFTER_GROWING_TRACE_20260921.md). The short-time response has an explicit smooth-field error bound; continuum and closure assumptions remain stated separately. Integrated into live main Section 5 and SI S13; the archived v0.5 pair is preserved.
- [Live manuscript integration and handoff](notes/GROWING_TRACE_MANUSCRIPT_INTEGRATION_20260921.md): main Section 5 and detailed SI S13; no new draft snapshot.
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
  all-input EMA anchor and subsequent bounded append result are summarized in
  live main Section 9.4 and SI S9.5.

The main exposition takes the exact arithmetic shift equation as the
prescribed effective evolution. The immediate physical question fixes a theory and derives the quantum
evolution along a genuine Loewner trace. The longer-term hypothesis is that
an independently defined Wilson boundary observable can realize the arithmetic
equation and admit a cumulative positive-norm identity. A sequence of contractions with increasing length and vanishing
shift would imply central Weil positivity. No such physical realization,
norm identity or all-depth continuation has been established.

The arithmetic explanation of the decay rates and the local remainder
remains in Section 2.2. Both documents compile from this package; neither
loads a parent investigation or shared-background TeX source.

## Reading map

| Live main exposition | Technical companion |
|---|---|
| Sections 1--3: proposal, normalization, exact shift and defect equations | S1: arithmetic conventions and complete Beta/comb/rational factorization |
| Section 4: physical transfer hypothesis and insertion closure | S3--S4: contour dictionary, rigidity, full smooth variation and controls |
| Section 5: genuine growing-trace quantum hierarchy | S13: tip cancellation, ordered insertion equations, linear driver, explicit remainder and closure residuals |
| Section 6: fixed-window test and localization question | S10--S12: complete local/pole target, Gaussian response, scoped obstructions, auxiliary product and predictive localization controls |
| Section 7: spectral ingredients and constraints | S2, S5--S6: free kernel, Gaussian model, projectors and endpoint selection |
| Section 8: cumulative positivity and reflected amplitudes | S7--S8: adjoint, reference junction, reflection tests and bulk response |
| Section 9: separate depth--shift route and spatial gluing | S9: Schur, Cayley and simultaneous continuation algebra |
| Section 10: research agenda and statement ledger | S14--S15: 299 original finite diagnostics, separate localization and trace-growth controls, and provenance |

The companion retains the detailed former Sections 3--9, together with
the arithmetic factorization and diagnostic appendix. Key constraints stay
visible in the exposition: the subtraction sign, same-charge endpoint
vanishing, conditional interacting reflection, and the incomplete physical
response. The current pair has 24 exposition pages and 46 supplementary pages.
Historical versions 0.1--0.5 remain unchanged.

The [shift-flow note](notes/SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md)
records the proposal that led to this split. The
[critical-path investigation](../critical-path/README.md) now contains the
adaptive-EMA anchor and cumulative append investigation. The live revision reports the subsequent internal all-input bound below 0.951
for the designated arithmetic append, with specialist review outstanding.
Its proof stays in critical-path; it supplies neither an all-depth continuation
nor a physical realization.

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
| [numerics](numerics/README.md) | Four original manuscript programs (299 cases), plus separate localization, endpoint and genuine-trace controls |
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
