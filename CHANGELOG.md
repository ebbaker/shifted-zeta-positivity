# Changelog

All notable changes to the released contents of this repository. Dates are the
dates of the underlying work; the repository itself was created in September 2026.

## [Unreleased]

### 2026-09-09 — external repository review applied (commit `50cb4d2` reviewed)

Changes from an independent repository-and-reproducibility review of the first
commit, applied after checking each finding; none touches the mathematics or
marks a pending human check complete.

- **Citation metadata.** `papers/first-slab-positivity/CITATION.cff` used
  `type: generic`, which the CFF 1.2.0 schema does not allow at top level
  (only `software`/`dataset`); both CFF files now validate. Each is a
  `software` record for the folder's sources with a `preferred-citation` of
  type `unpublished` identifying the preprint (that is what GitHub's "Cite this
  repository" and CFF tooling read). Root CFF license is MIT (it describes
  code); the papers stay CC BY 4.0 under `LICENSE`. New `tools/check_citations.py`
  validates both files against the official schema; `environment/requirements_metadata.txt`
  pins its dependencies.
- **No example DOIs.** `10.5281/zenodo.NNNNNNN`-style placeholders removed
  from every citation block; until a release exists the blocks give a
  commit-based form, and the DOI forms use ⟨…⟩ placeholders. README, paper
  README and `papers/README.md` now say plainly that no tag or DOI exists yet
  and that repository version (`0.2.0`) and manuscript version (`1.0`) are
  separate identifiers.
- **Honest description of the tree.** Root README tagline and `.zenodo.json`
  no longer imply the Arb certificate bundle is in the repository; `notes/`
  is described as an index for a planned migration (only the index and
  redaction checklist are present); "released as a preprint" → "available as
  a preprint". "No error survives in the main proof chain" (VERIFICATION_STATUS,
  CHECKLIST) → "no unresolved error was identified in those internal reviews;
  the independent human checks remain pending".
- **License notice** links the specific CC BY 4.0 deed and legal code and
  states that the two licenses apply by material type, not as a choice;
  "dual license" wording replaced everywhere. Copyright line unchanged.
- **Stable numerical diagnostics.** New
  `verification/first-slab/scripts/verify_stable_volterra_20260909.py`
  replaces the A4 section of the 5 Sept script, whose sampled singular kernel
  and unbounded float Laplace integral were numerically unreliable and whose
  printed failures never became a nonzero exit status. The new script uses
  integrated piecewise-constant Galerkin sections with Gauss–Jacobi treatment
  of the t^(ω−1) endpoint, checks the reflection algebra, 48/96-node and
  16/32-cell consistency and four high-precision Laplace-transfer identities
  (16 checks; exit 1 on failure). Re-run here: 16/16 pass under CPython 3.12
  with the pinned `mpmath==1.4.1`, `numpy==2.4.4`, `scipy==1.17.1`; an
  injected 0.001 error produces 4 FAILs and exit 1. Diagnostics only — not an
  interval certificate and not a bound on the infinite-dimensional operator.
- **CI.** `.github/workflows/check-first-slab.yml` runs the diagnostics and the
  CFF schema check. `RELEASING.md` now says what `build-latex` does and does
  not establish (compilation and page count, not PDF/source identity), that
  JSON parsing is not Zenodo metadata validation, and where each DOI goes.
- **Certificate code recovered, not integrated.** The Investigation 7/12/13/14
  generators, audit, diagnostics, result CSVs and verifiers were recovered and
  packaged as a review candidate outside the repository; its CSV hashes match
  the 5 Sept 2026 full-regeneration record and its stored-table verifiers pass.
  All three computations were then regenerated here in a fresh pinned
  environment (CPython 3.12.3, python-flint 0.9.0, numpy 2.3.5, scipy 1.17.0,
  mpmath 1.4.1; ~4 min total) and produced byte-identical tables —
  `verification/first-slab/CERTIFICATE_RERUN_20260909.md`, noted at D4 in the
  checklist and VERIFICATION_STATUS. The code stays out of the tree until
  D1–D5 are done (`code/README.md`, `MANIFEST.md` updated to say so).
- Contact e-mail in `code/certificates/first-slab/README.md` corrected to the
  personal address.

### 2026-09-08 / 09 — working drafts committed

- The four companion manuscripts are now in the tree as clearly labelled
  working drafts, each with `README.md`, `STATUS.md` and reproduction code:
  `papers/psi-omega-margin/` (full 21 pp. + concise 9 pp., scripts `c1`–`c8`,
  two supplementary notes), `papers/omega-string/` (v5, 13 pp., figure script,
  two verification scripts; Kasahara 1975 source-verified), `papers/defect-depth/`
  (v1, 15 pp., Ihara laboratory code), `papers/rh-detector/` (10 pp., scripts and
  zero caches; numerics re-verified). None is released; no DOI covers them.
- Folder slugs fixed to the actual names (`psi-omega-margin`, `omega-string`,
  `defect-depth`, `rh-detector`) throughout the READMEs, STATUS files, notes
  index and manifest; `rh-detector` marked as a separate thread that predates
  the Suzuki program.
- Author blocks filled in Papers 1 and 2 (Edward B. Baker III); contact email
  changed to the author's personal address in the preprint and all metadata;
  ORCID `0000-0001-5459-9993` added to `CITATION.cff` and `.zenodo.json`; no
  institutional affiliation in any paper (README carries the one mention).
- README: background section expanded (2015 origins; slice-regular,
  Yang–Mills and Chern–Simons phases; the turn to Suzuki's screw functions).
- `verification/first-slab/PROTOCOL_C1_C2.md` (6 Sept): step-by-step protocol
  for the two premise checks — normalization chain against Suzuki [1] and the
  originality search — written so the checker is not anchored by the preprint.
- `code/README.md` now points to the per-paper `code/` folders; the CI workflow
  builds all six PDFs.

- Single-repository plan adopted: releases archive the whole tree; each
  released paper is additionally deposited as its own Zenodo record linked by
  related identifiers (`README.md`, `RELEASING.md`, root `.zenodo.json`).
- `blueprint/first-slab/statements.md`: 30-statement inventory of the preprint
  with dependency graph, proof status, human-check status and formalization
  feasibility; machine-readable twin `statements/ledger.yaml`.
- `notes/REDACTION_CHECKLIST.md` and preface for the research log.
- Formalization section in `CONTRIBUTING.md`, `formalization` issue template,
  suggested labels.
- Program repository scaffold: papers/, verification/, notes/, code/, references/.
- Status files for the four unreleased manuscripts.
- Public verification checklist for the first-slab preprint, keyed to v1.0 numbering.

## [first-slab-positivity v1.0] — 2026-09-05

First deposited preprint: *Archimedean first-slab positivity for shifted zeta
canonical systems: an off-center Weil generator and a radial energy identity*.
Relative to the working draft of 3 September:

- Lemma 7.1 (block-Schur coercivity) and Remark 7.2 added; Theorem B now states
  the coercivity constant `c_* = 6.1159e−4` on `D_log` (the certified margin
  `6.11635e−4` is `~4e−8` above the exact block-Schur constant).
- §1.1 and abstract pinned to Suzuki's exact statements (Prop. 1.2, Thm. 2.2,
  Lemma 4.1 of arXiv:1204.1827); single-shift "equivalence" removed.
- §9.3 rewritten: strict finite-section contractivity for `ω > ½` is Suzuki's
  Lemma 4.4; Theorem A positioned as the complementary `0 < ω ≤ ½` result.
- Missing case-split line inserted in Lemma 6.1 (`a ≥ L/2 > t₀`).
- Private author-verification notice replaced by public §13 *Verification status*
  and Appendix C ledger row for `ω > ½`.
- Repository metadata: README, CITATION.cff, .zenodo.json, LICENSE (CC BY 4.0),
  VERIFICATION_STATUS.md.

### Earlier internal history (not released)

- 2026-09-03 — second referee round: all ten round-1 items resolved and
  re-verified (`verification/first-slab/reviews/REVIEW_round2_verdict_20260903.md`).
- 2026-08-31 — first referee round on the working draft
  (`REVIEW_round1_20260831.md`): endpoint lemma, sharp kernel bound (margin
  doubled), positivity horizon, Prop. 4.1 proof rewrite, §8 gaps.
- 2026-08-29 — defect-depth draft v1; Ihara laboratory rounds 1–5.
- 2026-08-28 — shifted zeta string paper frozen at v5 pending human review.
- 2026-08-27 — psi_omega_margin paper: next steps folded in (21 pp.).
- 2026-08-26 — geometry/physics routes closed (ROUND9); Suzuki screw-function
  program found (ROUND12) — pivot to the psi_omega_margin thread.
- 2026-08-24/25 — instanton-size brief; certified off-axis detector; pencil corollary.
