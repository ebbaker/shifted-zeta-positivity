# Research log index (RH3)

> **What is here.** This index catalogues the round reports, briefs and
> laboratory notes of the RH3 project. The documents themselves are in
> [claude/](claude/), imported unchanged from the claude.ai data export on
> 13 October 2026 (see the [folder README](../README.md) and its
> `manifest.json`). The index and the [redaction checklist](REDACTION_CHECKLIST.md)
> formed the repository-root `notes/` folder until 16 October 2026, when they
> were moved here beside the documents
> ([relocation record](../../../papers/REORGANIZATION_20261016.md)).
> Filenames below link to the copies here; a document kept elsewhere is
> linked at its location. The copies in `claude/` are the exported originals:
> the redaction checklist has not been applied to them.
>
> **Preface.** The documents catalogued here are round reports, briefs and
> laboratory notes written by a language model during working sessions
> directed by the author (Edward Baker), between 24 August and 11 September
> 2026. They are kept as the record of how the
> results in `papers/` were reached, including the routes that were tried and
> closed, claims that were later corrected in place, and one same-day
> retraction. They were not peer-reviewed. Where a note and a released paper
> disagree, the paper is current. Third-person references to "the author" (or
> "the user", where not yet edited) refer to Edward Baker.

Dated notes, round reports, briefs and laboratory reports from the project
store, kept flat under `claude/` with their original filenames so that the
cross-references inside them keep working. **Everything here is exploratory.**
Each note states what was verified and what was not; read them with that in
mind, and prefer the papers and their `blueprint/` and `verification/` records
for anything you intend to rely on.

Two independent numbering series both use "ROUND": the physics/geometry
program (rounds 1–12, 24–26 Aug) and the defect-depth manuscript preparation
(`ROUND6_closeout`, 29 Aug). Dates disambiguate.

## Reading order

If you read three notes: [`ROUND5_state_of_play.md`](claude/ROUND5_state_of_play.md) (where the geometry routes
ended), [`ROUND9_nyman_beurling_and_close.md`](claude/ROUND9_nyman_beurling_and_close.md) (the specification a proof route
would have to meet), then [`PROGRESS_psi_omega_next_steps.md`](../../../papers/weil-positivity/shifted-zeta/psi-omega-margin/supplementary/NEXT_STEPS.md) (where the
shifted-screw program comes from; redacted repository copy). If you read one: `ROUND9`.

## Index by thread

### 0 · Program-level orientation

| File | Date | One line |
|---|---|---|
| [`ROUND5_state_of_play.md`](claude/ROUND5_state_of_play.md) | 25 Aug | Orientation after five rounds: what is finished (detector, pencil corollary), what is closed (ADHM/instanton dictionary, undeformed YM, N=4 SYM as a lever) and why; method note on over-asserted claims. |
| [`BRIEF_three_live_routes.md`](claude/BRIEF_three_live_routes.md) | 26 Aug | Screens routes 3–5: Jensen polynomials of gauge counting sequences (closed by exact Sturm counts — VW/K3 fails at d = 13), Chern–Simons → Nyman–Beurling chain (dead as a chain; retarget to Nyman–Beurling survives), quaternionic Jensen (one deciding check). |
| [`ROUND9_nyman_beurling_and_close.md`](claude/ROUND9_nyman_beurling_and_close.md) | 26 Aug | Nyman–Beurling screened: exactly marginal (constant `2+γ−log4π` verified), exponentially insensitive to off-line zeros; six-point specification of what a source for RH would have to do; **closes the geometric search**. |
| [`NOTE_variation_axes.md`](claude/NOTE_variation_axes.md) | 29 Aug | Two variation axes for the Ψ_ω/bulk dictionary (boundary topology; positivity/analyticity class); conservation law "criticality relocates, is never created"; queues the Ihara laboratory, Riccati/action, Selberg ω-strings. |

### 1 · Geometry and physics routes (24–26 Aug; closed)

| File | Date | One line |
|---|---|---|
| [`BRIEF_instanton_size.md`](../rh2/claude/BRIEF_instanton_size.md) (top-level in the project store; kept once, as the RH2 copy) | 24 Aug | Self-contained brief: Ξ's Hadamard product vs the ADHM determinant; Im(zero) = √2 × instanton size; matching-rigidity theorem for all charges and classical groups; verdict *not viable* (the size is a free modulus; noncommutative deformation bounds it away from zero). |
| [`ASSESSMENT_instanton_size.md`](claude/ASSESSMENT_instanton_size.md) | 24 Aug | Assessment accompanying the brief. |
| [`ROUND2_full_YM_and_results.md`](claude/ROUND2_full_YM_and_results.md) | 24 Aug | Full Yang–Mills matching; closes undeformed YM, non-self-dual solutions, Vafa–Witten, 2D YM. |
| [`ROUND3_correction_and_bridge.md`](claude/ROUND3_correction_and_bridge.md), [`ROUND3_verification_and_detector.md`](claude/ROUND3_verification_and_detector.md) | 24 Aug | A round-2 correction; verification pass; the velocity-residual detector prototype and the margin map. |
| [`ROUND4_certificates_and_edge_law.md`](claude/ROUND4_certificates_and_edge_law.md) | 24 Aug | Detector made certificate-grade (exact RvM decomposition + Trudgian's `\|S(t)\|` bound); `n = 0` edge law derived (fixed collision of zeros #4/#5 over growing variance, exponent 4); pencil identity traced to Wilson's tau-function formula. |
| [`NOTE_offaxis_detector.md`](claude/NOTE_offaxis_detector.md), [`NOTE_pencil_and_DBN.md`](claude/NOTE_pencil_and_DBN.md) | 24 Aug | Drafts that became `papers/misc/rh-detector/` — the detector thread, which predates the Suzuki program. |
| [`NOTE_n4_sym_seam.md`](claude/NOTE_n4_sym_seam.md) | 25 Aug | N=4 SYM as a lever on the zeros: ξ cancels in the spectral decomposition; Sarnak's ceiling is PNT; closed. |
| [`ROUND6_unscreened_sweep.md`](claude/ROUND6_unscreened_sweep.md) | 26 Aug | Sweep of unscreened routes; the quantifier-order finding (RH is the line `n = 0, d → ∞` every Jensen wedge misses) and the Gaussian-slack kernel no-go. |
| [`ROUND7_nonlinear_preservers_and_KP.md`](claude/ROUND7_nonlinear_preservers_and_KP.md) | 26 Aug | Nonlinear hyperbolicity preservers and KP; source of the three routes screened in the brief. |
| [`NOTE_4d_anisotropic_cycles.md`](claude/NOTE_4d_anisotropic_cycles.md) | 26 Aug | Quaternionic/4-dimensional Jensen route closed: Perotti's formula specialises to classical Jensen plus `Re(p₂)/(4R²)`; SO(3)-invariant integrals are blind to the real axis. |
| [`ROUND8_closures.md`](claude/ROUND8_closures.md) | 26 Aug | Closures of routes 3, 4 and 5(a); the degeneration screen. |
| [`ROUND10_boundary_data.md`](claude/ROUND10_boundary_data.md) | 26 Aug | Boundary-data reframing; five-slot screen; torus/p-adic/adelic verdicts; Connes–van Suijlekom truncated Weil form identified as the one live architecture; Lax–Phillips contraction argument refuted. |
| [`NOTE_existence_loophole.md`](claude/NOTE_existence_loophole.md) | 26 Aug | Existence reframing; Prop. 3.1 (semialgebraic descriptions); falsification-criteria list; Burnol's separability obstruction added as criterion 5. |
| [`ROUND11_freeboson_and_positivity.md`](claude/ROUND11_freeboson_and_positivity.md) | 26 Aug | Compact free-boson L-function derived and confirmed against Perlmutter (10.33)–(10.35); Connes ↔ Fourier-optimization seam confirmed empty; Connes architecture's missing step narrowed to two facts; Burnol read in full (vacuity remark, spanning threshold, undeveloped Kreĭn string). |
| [`NOTE_n4_reformulation.md`](claude/NOTE_n4_reformulation.md) | 26 Aug (rewritten) | Dorigoni–Treilis N=4 zero-mode residues; transcription confirmed against print; constant corrected to `8.07e−6`. |
| [`NOTE_freeboson_Lfunction.md`](claude/NOTE_freeboson_Lfunction.md) | 26 Aug | `L_Z^{(c=1)}`, `Q_Z`; all analytic-factor zeros on `Re s = ½`; sharp threshold `A₂ ≥ A₁` for two-pair lattice cores. |
| [`NOTE_riemann_maass_sum_rules.md`](claude/NOTE_riemann_maass_sum_rules.md) | 26 Aug | Perlmutter §11.2 sum rules written out (Kuznetsov split); a second RH-detector of Dorigoni–Treilis shape; no high-energy testing window. |
| [`NOTE_connes_weil_dirichlet_form.md`](claude/NOTE_connes_weil_dirichlet_form.md) | 26 Aug (corrected same day) | Beurling–Deny reading of Connes' `A_λ`; novelty **withdrawn** (Suzuki 2606.09096 Thm 1.4 has it); what survives: §6.6(i) proved at small `a`, open at large `a`; the odd-sector experiment. |
| [`ROUND12_execution_and_a_retraction.md`](claude/ROUND12_execution_and_a_retraction.md) | 26 Aug | Executes ROUND11's items; records the retraction; **discovers the Suzuki screw-function program**, which the record had missed entirely — the pivot to the shifted-screw thread (`papers/weil-positivity/shifted-zeta/psi-omega-margin/`). |

### 2 · Shifted screw functions Ψ_ω (26–28 Aug) → `papers/weil-positivity/shifted-zeta/psi-omega-margin/`

| File | Date | One line |
|---|---|---|
| [`NOTE_psi_omega_margin.md`](claude/NOTE_psi_omega_margin.md) | 27 Aug | The margin `Ψ_ω(t) = (ξ'/ξ)(½+ω)t + …`; the note that became Paper 1. |
| [`ROUND13_psi_omega_recheck.md`](claude/ROUND13_psi_omega_recheck.md) | 27 Aug | Referee-style recheck of the margin paper; four next steps. |
| [`NOTE_oneside_criterion.md`](claude/NOTE_oneside_criterion.md) | 27 Aug | One-sided and `L¹` forms; losslessness theorem (no formal operation inside the family improves an exponent); problem P2 (Weil positivity with exponential defect). |
| [`PROGRESS_psi_omega_next_steps.md`](../../../papers/weil-positivity/shifted-zeta/psi-omega-margin/supplementary/NEXT_STEPS.md) (redacted repository copy, `NEXT_STEPS.md`) | 27 Aug | The four steps executed and verified: windows through zero-free regions (endpoint law `t₊ ≈ 0.72(½−ω)⁻²`), Dirichlet/Selberg-class margin and Siegel blindness, order-parameter theorem, Bombieri §8 priority check; letter to Suzuki drafted. |
| [`ROUND14_concise_draft_check.md`](claude/ROUND14_concise_draft_check.md) | 28 Aug | Check of the concise variant of Paper 1. |

### 3 · The shifted zeta string (28 Aug) → `papers/weil-positivity/shifted-zeta/omega-string/`

| File | Date | One line |
|---|---|---|
| [`NOTE_omega_string.md`](claude/NOTE_omega_string.md) | 28 Aug | The inverse-spectral family `q_ω`, `ρ_ω`, `m_ω`; became Paper 2. |
| [`ROUND15_referee_audit_omega_string.md`](claude/ROUND15_referee_audit_omega_string.md), [`ROUND16_referee_round2_fixes.md`](claude/ROUND16_referee_round2_fixes.md), [`ROUND17_round3_fixes.md`](claude/ROUND17_round3_fixes.md), [`ROUND18_kasahara_verified_and_sync.md`](claude/ROUND18_kasahara_verified_and_sync.md) | 28 Aug | Five referee passes on Paper 2; Kasahara's regular-variation theorem checked against the original; cross-consistency with Paper 1. |
| [`ROUND19_endpoint_length_and_freeze.md`](claude/ROUND19_endpoint_length_and_freeze.md) | 28 Aug | Endpoint length collapse (`L_ω = ∞` vs `L_ξ = B(0)`); critical-member laws; citation-numbering policy; **freeze pending human review**; outreach shortlist. |

### 4 · The finite (Ihara) laboratory and defect depth (29 Aug) → `papers/weil-positivity/shifted-zeta/defect-depth/`

| File | Date | One line |
|---|---|---|
| [`LAB_ihara_round1.md`](claude/LAB_ihara_round1.md) | 29 Aug | For finite (q+1)-regular graphs the whole chain Ψ_ω → q_ω → σ_ω → string is finite and exact; Ramanujan ⟺ Stieltjes string (20+ graphs); finite Siegel anatomy (three inequivalent criteria); ω-flow indices; covers land at the IR end. |
| [`LAB_ihara_round2.md`](claude/LAB_ihara_round2.md), [`LAB_ihara_round3_results.md`](claude/LAB_ihara_round3_results.md), [`LAB_ihara_round4_results.md`](claude/LAB_ihara_round4_results.md) | 29 Aug | Irregular graphs, twists, periodic towers, the Christoffel depth mechanism and the discrete/continuum crossover. |
| [`LAB_ihara_round5.md`](claude/LAB_ihara_round5.md) | 29 Aug | Compactified moments = binomial transform of Taylor coefficients (canonical); ω > 0 depth law theorem-grade (Stahl–Totik); time-domain constant `log(2(ξ'/ξ)(½+ω)/(δ−ω))`; flux Hessian sees triangles. |
| [`ROUND6_closeout.md`](claude/ROUND6_closeout.md) | 29 Aug | All manuscript gates for Paper 3 resolved (amplitude-2 normalization fixes the log 2 discrepancy; `s₀`-dependence measured, "intrinsic" dropped); GO for drafting. |

### 5 · First-slab positivity (31 Aug – 5 Sept) → `papers/weil-positivity/shifted-zeta/first-slab-positivity/`

The review records and recomputation scripts are in the first slab's
[verification/](../../../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/README.md) folder and the statement
inventory in its [blueprint/](../../../papers/weil-positivity/shifted-zeta/first-slab-positivity/blueprint/README.md). The working drafts
are superseded by the preprint and are not kept. Kept here: the round-1 review
[`REVIEW_first_slab_positivity_20260831.md`](claude/REVIEW_first_slab_positivity_20260831.md), the checklist before renumbering
[`VERIFICATION_CHECKLIST_first_slab_20260904.md`](claude/VERIFICATION_CHECKLIST_first_slab_20260904.md), the deposit note
[`NOTE_preprint_v1_deposit_20260905.md`](claude/NOTE_preprint_v1_deposit_20260905.md) and the C1/C2 session handoff
[`HANDOFF_C1_C2_session_20260910.md`](claude/HANDOFF_C1_C2_session_20260910.md).

### 6 · Finite-horizon Weil positivity and storage depth (9–11 Sept)

The current papers are [Weil-depth](../../../papers/weil-positivity/shifted-zeta/weil-depth/README.md) and
[storage-depth](../../../papers/weil-positivity/shifted-zeta/storage-depth/README.md). The storage-depth
[closeout record](../../../papers/weil-positivity/shifted-zeta/storage-depth/CLOSEOUT.md) records the writing
project's completed work and remaining verification limits. Kept here:
[`NOTE_weil_depth_v0.3_20260909.md`](claude/NOTE_weil_depth_v0.3_20260909.md), [`NOTE_weil_depth_v0.4_20260910.md`](claude/NOTE_weil_depth_v0.4_20260910.md) and
[`HANDOFF_storage_depth_v0.3_20260910.md`](claude/HANDOFF_storage_depth_v0.3_20260910.md).

| Present file | Role |
|---|---|
| [Lessons learned](../../../papers/weil-positivity/shifted-zeta/storage-depth/LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md) | Exploratory design guidance; moved from `Claude outputs/`, including the author's pending wording change; in `notes/` until 16 October 2026. |
| [Barrier theorem and ladder conjecture note](../../../papers/weil-positivity/shifted-zeta/storage-depth/archive/reviews/NOTE_barrier_theorem_and_ladder_conjecture_20260911.md) | Draft arguments and diagnostic fits; distinct from the manuscript's certified records. |
| [Depth strategy](../../../papers/weil-positivity/shifted-zeta/storage-depth/archive/drafts/v3/NOTE_depth_strategy_20260911.md) | Historical options for extending the method. |

### 7 · Supersymmetric positivity (11 September 2026; active)

The separate investigation is in [papers/weil-positivity/susy-positivity](../../../papers/weil-positivity/susy-positivity/README.md).
Its [companion brief](../../../papers/weil-positivity/susy-positivity/investigations/previous/positive-factorizations/RESEARCH_BRIEF.md) records the current
motivation; [round 3](../../../papers/weil-positivity/susy-positivity/investigations/previous/positive-factorizations/INVESTIGATION_round3.md) constructs
an odd-sector factor and certifies the first prime's stabilizing role on a
linear input. The [original pedagogical brief](../../../papers/weil-positivity/susy-positivity/archive/supersymmetric_positivity_research_brief.md)
is historical motivation. The even-sector completion and joint prime model
remain open; see the [status ledger](../../../papers/weil-positivity/susy-positivity/investigations/previous/positive-factorizations/STATUS.md).

## Code referenced by the notes

Scripts named in the notes were run in session workspaces. Those that have
been recovered or regenerated now live next to their papers:
`papers/weil-positivity/shifted-zeta/psi-omega-margin/code/` (`c1`–`c8`), `papers/weil-positivity/shifted-zeta/omega-string/`
(`fig_density.py`, `v1_identities.py`, `v2_thmE_kasahara.py`),
`papers/weil-positivity/shifted-zeta/defect-depth/code/` (the Ihara laboratory core and experiment record),
and `papers/misc/rh-detector/code/` (`h1`, `h3`, `h4`, `d1`, `d4`, `v1` and the zero
caches). Scripts from the closed geometry/physics routes (`nb1.py`, the Jensen
screen, the round-12 scripts) and the defect-depth round-6 inline runs have
not been recovered; see [MANIFEST.md](../../../MANIFEST.md).
