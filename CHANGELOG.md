# Changelog

All notable changes to the released contents of this repository. Dates are the
dates of the underlying work; the repository itself was created in September 2026.

## [Unreleased]

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
