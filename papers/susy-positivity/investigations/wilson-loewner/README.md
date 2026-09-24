# Wilson--Loewner: shifted-zeta evolution and Wilson lines

The [second arithmetic-storage session](arithmetic-storage/notes/FIRST_PRIME_JOIN_EQUIVALENCE_AND_PRIME_WEIGHT_RIGIDITY_20260924.md) (Claude, 24 September 2026; not committed) shows that the append hypothesis is joined-window positivity. It closes the first-prime join with the weil-depth pipeline and certifies that the prime-2 weight is pinned by positivity on (0, log 3). See its [review](arithmetic-storage/reviews/review_claude_first_prime_session_20260924.md) and [continuation](arithmetic-storage/notes/RESEARCH_CONTINUATION_AFTER_FIRST_PRIME_CLOSURE_20260924.md).

The [first arithmetic-storage analysis](arithmetic-storage/notes/FIRST_PRIME_CONTINUATION_ANALYSIS_20260924.md) establishes internal all-input local bounds for the first-prime join and rigorously separates failure of the inherited 128-mode energy proxy from the complete arithmetic form. Finite-input complete-coupling tests are favorable; an all-input first-prime contraction is not yet proved. The [handoff](arithmetic-storage/notes/RESEARCH_CONTINUATION_AFTER_FIRST_PRIME_INPUTS_20260924.md) specifies the remaining estimate.

The new [arithmetic-storage program](arithmetic-storage/README.md) develops cumulative positivity beyond the completed prime-free append, the actual first-prime Sonin remainder, and a focused canonical-system comparison. Its [program note](arithmetic-storage/notes/ARITHMETIC_STORAGE_PROGRAM_AND_GOALS_20260924.md) records the existing internal bound below 0.951 and sets the next benchmark across log 2. This is a research plan; no new certificate or physical realization is claimed.

The [cross-theory lessons note](notes/LESSONS_FROM_WZW_FOR_YM_AND_N4SYM_20260923.md) applies the WZW and later response tests to the parent YM/SYM program. A new [N4SYM investigation](N4SYM/README.md) contains a detailed proposal for displacement-operator response, genuine Loewner growth and physical energy accounting. These are research notes and a proposal; no new physical realization or numerical result is claimed. Its [first working session](N4SYM/README.md#status-after-the-first-session-2324-september-2026-claude-opus-55) (Claude Opus 5.5, 23–24 September) found the linear straight-line displacement response to be local (Abraham–Lorentz), which closes that channel as an arithmetic candidate. It replaced the proposal's first growing-trace observable by a flipped-return loop, analyzed through two exact smooth-field evolution equations and one-loop calculations, with 196 separate standard-library diagnostics. A second session (24 September) showed that the near-BPS corner coefficient of that loop is one-loop exact as s → 0, with effective coupling λ|s| and a √(λ|s|) window at strong coupling from the classical string. It also computed a finite rounded family and audited Schwinger–Dyson closure, bringing the diagnostics to 272 cases. A third session (24 September; Claude Fable 5.1) took the arithmetic route the author chose: the finite-mass heavy source (string endpoint at z_m = √λ/2πm) is the first channel with memory, but its memory is one exponential, its boundary field is exactly local in retarded time (a closed-form quartic transfer function, contradicting a 1999 broadening claim if a referee reading holds), and the channel fails the front-and-tangent test; the quartic straight-line response has memory with a coupling-dependent exponent Δ₆(λ) but no scale, so no fixed delays. No arithmetic comparison was run. The diagnostics stand at 472 cases, and a first draft manuscript covering the three sessions exists in [N4SYM](N4SYM/README.md). No independent review.

The [standalone manuscript in the WZW investigation](WZW/manuscript.pdf) now focuses on **Thermal arithmetic orbit weights and the shifted-zeta equation**: the Bost–Connes primitive coefficient identity, its ordinary-norm limitations and the missing causal physical interface. Earlier unsuccessful readouts are summarized near the end with references to their detailed notes. See the [editable source](WZW/manuscript.tex), [research note](WZW/notes/ARITHMETIC_ORBIT_WEIGHTS_AND_BOST_CONNES_TEST_20260923.md) and [WZW package](WZW/README.md). The parent manuscript pair below retains its existing scope.

The [22 September arithmetic-source investigation](notes/ARITHMETIC_SOURCE_AND_GENERALIZED_LOEWNER_EVOLUTION_20260922.md) established the preceding arithmetic-matching framework. A shifted xi logarithmic derivative defines an actual generalized Loewner flow and recovers the full arithmetic source. The note also identifies the RH-equivalent zero-shift condition, the failure of instantaneous generator positivity, and the length-dependent cost of removing a safe spectral weight. The next target is a cumulative boundary or canonical response with a specified norm. See the [internal audit](reviews/review_codex_arithmetic_loewner_source_20260922.md), [60 checks](numerics/records/arithmetic-loewner-source-20260922.json), and [milestone index](DRAFT_HISTORY.md).

The [preceding SU(2)_2 boundary pilot](notes/SU2_LEVEL2_DETERMINISTIC_LOEWNER_PILOT_20260922.md) completed the proposed WZW calculation: explicit blocks, deterministic evolution, a constant-driver tensor norm balance, fusion/gluing, and a spatial-smearing limitation. It remains a physical benchmark; its further sewing calculation is deferred while the arithmetic source and operator dictionary are specified. See the [pilot audit](reviews/review_codex_wzw_loewner_pilot_20260922.md) and [72 checks](numerics/records/wzw-loewner-pilot-20260922.json). Both are separate research addenda; the manuscript pair below is unchanged.

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
- [Genuine Loewner growth in fixed Yang--Mills theory](notes/GENUINE_LOEWNER_TRACE_YM_HIERARCHY_20260921.md): the preceding physical calculation, deriving a quantum insertion hierarchy for an actual growing trace and a specified return chord; [next-session handoff](notes/RESEARCH_CONTINUATION_AFTER_GROWING_TRACE_20260921.md). The short-time response has an explicit smooth-field error bound; continuum and closure assumptions remain stated separately. Integrated into live main Section 5 and SI S13; the archived v0.5 pair is preserved.
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
prescribed effective evolution. The immediate arithmetic question now starts from the completed xi logarithmic derivative and asks for a cumulative boundary or canonical response with the correct operator norm. Deterministic WZW boundary evolution and the earlier growing-trace YM hierarchy remain complementary physical calculations. The longer-term hypothesis is that
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
