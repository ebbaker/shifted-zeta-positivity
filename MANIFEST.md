# Manifest — what goes where

Provenance record for the repository: which files were written for it, which
were carried over from the private project store, and which are still
missing. Updated 11 September 2026.

## Written for the repository

```
README.md  CITATION.cff  CHANGELOG.md  CONTRIBUTING.md  RELEASING.md  MANIFEST.md  LARGE_FILES.md
.gitignore  .zenodo.json   (LICENSE: the repository's licensing-by-material-type notice)
.github/ISSUE_TEMPLATE/{verification-report,possible-error,formalization}.md
.github/labels.yml  .github/workflows/{build-latex,check-first-slab,check-hygiene}.yml
blueprint/README.md  blueprint/first-slab/statements.md
statements/README.md  statements/ledger.yaml
environment/{requirements,requirements_metadata}.txt
tools/{check_citations,check_repository_hygiene}.py
papers/README.md
papers/{shifted-zeta,misc}/README.md              (project indexes)
papers/shifted-zeta/*/{README,STATUS,VERIFICATION_STATUS}.md  (where applicable; six folders)
papers/misc/rh-detector/{README,STATUS}.md
papers/susy-positivity/{README,PROGRAM_OVERVIEW}.md (shared program guide)
papers/susy-positivity/background{,_section}.tex + background.pdf
papers/susy-positivity/CONTINUATION_BULK_BOUNDARY_SUPERSPACE_20260912.md
papers/susy-positivity/attempts/positive-factorizations/** (manuscript and support)
papers/susy-positivity/{REORGANIZATION_20260912.md,validation/} (fresh verification)
papers/shifted-zeta/weil-depth/**   (drafted in the repository, Sept 2026, on the branch finite-horizon-weil:
                        manuscript/, numerics/, archive/, ARCHIVES.md, CONTINUATION.md,
                        BUILD_RECORD.json, SHA256SUMS.txt; its ~122 MB of ball-matrix archives
                        are kept outside git — LARGE_FILES.md, papers/shifted-zeta/weil-depth/ARCHIVES.md)
papers/shifted-zeta/storage-depth/**  (drafted 10 Sept 2026 on the branch critical_path by OpenAI models
                        (v0.1, v0.2) and rewritten as v0.3 by Claude after review: manuscript/,
                        numerics/ (recursion/, fourier_side/, records/), archive/ (drafts v0.1 and
                        v0.2, reviews, background), ARCHIVES.md, CLAIMS.json, BUILD_RECORD.json,
                        SHA256SUMS.txt; its ~1.6 GB of matrix archives are kept outside git —
                        LARGE_FILES.md, papers/shifted-zeta/storage-depth/ARCHIVES.md)
papers/shifted-zeta/first-slab-positivity/{CITATION.cff,.zenodo.json,LICENSE.md,VERIFICATION_STATUS.md}
papers/shifted-zeta/psi-omega-margin/supplementary/DERIVATION_AND_VERIFICATION.md   (authored clean, 9 Sept)
papers/{shifted-zeta,misc}/*/code/{README.md,requirements.txt}
verification/README.md
verification/first-slab/{CHECKLIST.md,PROTOCOL_C1_C2.md,CERTIFICATE_RERUN_20260909.md}
verification/first-slab/reviews/{README.md,REVIEW_round2_verdict_20260903.md}
verification/first-slab/scripts/{README.md,verify_referee_checks_20260831.py,verify_preprint_checks_20260905.py}
verification/first-slab/scripts/{verify_stable_volterra_20260909.py,requirements_stable_checks.txt}   (from the 9 Sept external review)
notes/README.md  notes/REDACTION_CHECKLIST.md
code/README.md  code/certificates/first-slab/README.md
references/README.md
```

## Carried over from the project store — done

| Project document | Repository location | Note |
|---|---|---|
| `PAPER_first_slab_positivity_preprint_v1.tex` | `papers/shifted-zeta/first-slab-positivity/first_slab_positivity.tex` (+ PDF) | released, v1.0 |
| `PAPER_psi_omega_margin.tex`, `PAPER_psi_omega_concise.tex` | `papers/shifted-zeta/psi-omega-margin/` (+ PDFs) | **working drafts**, committed 9 Sept 2026; author block filled |
| `c1_xi_values.py` … `c8_prime_side_chi.py` (recovered) | `papers/shifted-zeta/psi-omega-margin/code/` | 27 Aug recomputation set |
| `PROGRESS_psi_omega_next_steps.md` | `papers/shifted-zeta/psi-omega-margin/supplementary/NEXT_STEPS.md` | redacted copy (checklist items 1, 4, 5 applied; sign-off pending) |
| `PAPER_omega_string.tex` | `papers/shifted-zeta/omega-string/` (+ PDF, `fig_density.png` regenerated) | **working draft v5**, committed 8 Sept 2026; author block filled |
| round-15 verification scripts (reconstructed) | `papers/shifted-zeta/omega-string/{fig_density,v1_identities,v2_thmE_kasahara}.py` | |
| `PAPER_defect_depth.tex` | `papers/shifted-zeta/defect-depth/` (+ PDF) | **working draft v1**, committed 9 Sept 2026 |
| `lab_ihara_core.py`, `lab_ihara_experiments.py` | `papers/shifted-zeta/defect-depth/code/` | laboratory record through round 5 |
| `PAPER_rh_detector.tex` | `papers/misc/rh-detector/` (+ PDF) | **working draft**, committed 9 Sept 2026; separate thread, predates the Suzuki program |
| `h1`, `h3`, `h4`, `d1`, `d4`, `v1` + `zeros1001.json`, `beta_zeros.json` (regenerated 25 Aug) | `papers/misc/rh-detector/code/` | smoke-tested 9 Sept |
| `REVIEW_ROUND2_verdict_20260903.md` | `verification/first-slab/reviews/` | |
| `verify_referee_checks_20260831.py`, `verify_preprint_checks_20260905.py` | `verification/first-slab/scripts/` | |
| `PROTOCOL_C1_C2_verification_20260906.md` | `verification/first-slab/PROTOCOL_C1_C2.md` | |

| Storage-depth lessons-learned note | `notes/LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md` | Moved from `Claude outputs/`, preserving the author's pending wording change; exploratory design guidance, not a certified result. |

Storage-depth closeout adds `papers/shifted-zeta/storage-depth/CLOSEOUT.md` and
`numerics/README.md`, updates the current navigation and external archive
guides, and refreshes the current checksum records. Supersymmetric briefs
were excluded from that closeout. The later `susy-positivity` work now lives
under the shared program root `papers/susy-positivity/`. Its positive-factorizations
manuscript and supporting notes are in `attempts/positive-factorizations/`,
with historical drafts and round-4 reports preserved inside that attempt.

## Still to carry over (after the redaction checklist)

| Project document | Destination | Note |
|---|---|---|
| `REVIEW_first_slab_positivity_20260831.md` | `verification/first-slab/reviews/REVIEW_round1_20260831.md` | rename as shown |
| `VERIFICATION_CHECKLIST_first_slab_20260904.md` | — | superseded by `verification/first-slab/CHECKLIST.md` (renumbered to v1.0); keep in the project only |
| `Lab_Tower_Check.py` (top level) | `code/labs/tower/` or drop | confirm purpose from header first |
| `BRIEF_instanton_size.md` (top level), `ASSESSMENT_instanton_size.md` | `notes/` | |
| `ROUND2_full_YM_and_results.md` … `ROUND12_execution_and_a_retraction.md` (physics series, 11 files incl. `ROUND6_unscreened_sweep.md`) | `notes/` | |
| `BRIEF_three_live_routes.md` | `notes/` | redaction item 3 (named-paper verdict) |
| `NOTE_offaxis_detector.md`, `NOTE_pencil_and_DBN.md`, `NOTE_n4_sym_seam.md`, `NOTE_4d_anisotropic_cycles.md`, `NOTE_existence_loophole.md`, `NOTE_n4_reformulation.md`, `NOTE_freeboson_Lfunction.md`, `NOTE_riemann_maass_sum_rules.md`, `NOTE_connes_weil_dirichlet_form.md` | `notes/` | |
| `NOTE_psi_omega_margin.md`, `ROUND13_psi_omega_recheck.md`, `NOTE_oneside_criterion.md`, `ROUND14_concise_draft_check.md` | `notes/` | the substance is summarised in `papers/shifted-zeta/psi-omega-margin/supplementary/DERIVATION_AND_VERIFICATION.md` |
| `NOTE_omega_string.md`, `ROUND15_…` … `ROUND19_endpoint_length_and_freeze.md` | `notes/` | redaction item 2 (ROUND19 §5 shortlist) |
| `NOTE_variation_axes.md`, `LAB_ihara_round1.md` … `LAB_ihara_round5.md`, `ROUND6_closeout.md` | `notes/` | redaction item 6 (memo filenames) |
| `NOTE_preprint_v1_deposit_20260905.md`, `VERIFICATION_STATUS_preprint_v1_20260905.md`, `REPO_*`, `BLUEPRINT_*`, `STATEMENTS_*` | — | project-side copies of repository files |
| `*.pdf` in the project files (Suzuki, Connes, Burnol, Perlmutter, Dorigoni, Dorey et al., Atiyah, Nakajima, Kronheimer, LeBrun, Witten, Pool) | **do not commit** | third-party; listed in `references/README.md` |

## Not present anywhere (ran in session workspaces; recover or regenerate)

- Paper 3, round-6 inline runs: amplitude certification, `s₀` five-point scan,
  unscaled real-ζ suite, envelope bracketing (`papers/shifted-zeta/defect-depth/STATUS.md`, item 5);
  round-4 crossover scans.
- Paper 2: the Herglotz-peeling reconstruction pipeline (numerics-polish pass).
- Closed geometry/physics routes: `nb1.py` (Nyman–Beurling); `no_screen.py`,
  `verify.py`, `jensen_vw.py`, `margin_vw2.py`, `check13.py` (Jensen screen);
  `n1_residues.py`, `n2_checks.py`, `p1_freeboson.py`, `p2b_lattice.py`,
  `m1_riemann_maass.py`, `c1_weilform.py` (round 12); `h2_edge80.py`,
  `h5_surrogate.py`, `h6_law.py` (detector, not needed by the paper).
- ~~First slab: the Investigation 7/12/13/14 certificate code and CSVs~~ —
  **recovered 9 Sept 2026** and packaged as a review candidate outside the
  repository (generators, audit, diagnostics, result CSVs, `verify_*` scripts,
  pins, hash manifest, historical notes and manifests); still release-gated by
  D1–D5 (`code/README.md`).
