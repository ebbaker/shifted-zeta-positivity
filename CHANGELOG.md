# Changelog

All notable changes to the released contents of this repository. Dates are the
dates of the underlying work; the repository itself was created in September 2026.

## [Unreleased]

### 2026-09-11 — storage-depth writing project closeout

- Merge `critical_path` into `main` with its five research commits preserved;
  no large numerical data enters the main tree or history.
- Update current README navigation, manuscript counts, the paper layout,
  repository metadata and the code/verification indexes for storage-depth v0.3.
- Standardize current archive documentation on `szp-archive`, locally
  `/Users/Shared/szp-archive`; keep historical draft snapshots unchanged.
- Move the existing lessons-learned note to `notes/`, retaining the author's
  pending wording change. Supersymmetric briefs are for a separate project.
- Record build, checksum, size and archive checks in
  `papers/storage-depth/CLOSEOUT.md`; refresh the current package manifests.
- Correct the dependency appendix to distinguish the failed 32-mode tests
  from the successful 96-mode R18 result; rebuild the 21-page PDF after
  minor typesetting fixes. No numerical constant or record changes.
- Document the author-accepted absence of the two regenerable R18 matrices
  and the intentionally omitted large Claude Fourier-analysis outputs.
- Keep the paper at working-draft v0.3. Independent normalization review,
  mathematical review and formal verification remain open; no release or DOI
  is created by this closeout.

### 2026-09-10 / 11 — storage-depth paper (branch `critical_path`): v0.1, v0.2, review, v0.3

- **New working draft `papers/storage-depth/`** — *Residual-controlled depth
  extension of finite-horizon Weil positivity: a spatial continuation past log 7
  for the shifted-zeta transfer* (v0.3, 21 pp.). Continues `weil-depth/` past
  `log 7` by splitting the interval at `log 7`, continuing old inputs onto a
  quarter slab of length `log(8/7)/4` by a Galerkin map, and certifying the
  graph-transformed Schur tests against the infinite polynomial complements.
  Certified in Arb ball arithmetic (working normalization):
  `2.99e-29 ≤ λ_min(Q_{0,L_q}) ≤ 3.29e-29` at `L_q = (3/4) log 14`, residual
  factor `R*F^{-1}R ≤ 0.78 H_J`, comparison `H_J ≥ 1.13e-7 A`, small-shift
  contraction for `ω ≤ 9e-16`; at `L_2 = log(56)/2` the 32-mode-slab build
  certifies only `H_{J_2} ≥ 5.01e-8 A_2` and the upper bound `1.89e-30` (its
  failed floor and residual tests diagnosed as an artifact of the three-interval
  complement floor), and the 96-mode-slab build of 11 Sept then certifies
  `1.69e-30 ≤ λ_min(Q_{0,L_2}) ≤ 1.89e-30`, residual factor `0.8`,
  `H_{J_2} ≥ 5.25e-8 A_2` and contraction for `ω ≤ 2e-16` (record R18). A direct-floor lemma
  (`M_θ ≥ m ⇒ Q ≥ m/τ²`) replaces the scalar comparison in the conditional
  all-depth scheme; a dimension estimate places the method's horizon near
  `L = 3`; a Fourier-side computation shows the near-null vector is tuned to
  vanish at the low zeros and that the certificate constrains zeros only below
  height about 70.
- Provenance: v0.1 and v0.2 drafted on 10 Sept by OpenAI models (five research
  packets, then a consolidated record); v0.2 reviewed by Claude with an
  independent re-implementation of the validators (`archive/reviews/`), which
  found the floors understated by four orders of magnitude and diagnosed the
  second step; v0.3 rewritten by Claude as a paper with the numbers re-derived
  through the repository's code path (records R14–R18: archive-based bisection
  replays, ball Rayleigh upper bounds, hypothetical-floor diagnostics,
  Fourier-side zero sums, the 96-mode-slab rebuild). Earlier drafts preserved under `archive/drafts/`.
- New tools under `numerics/recursion/`: `stream_io.py` (streaming dual-hash
  loader that runs in a few GB of memory), `replay_floor.py` (archive-based
  replays with bisection), `rayleigh_upper.py`; `numerics/fourier_side/` for the
  zero-sum diagnostic; `build_step_seed.py`, `build_from_seed_v2.py` and
  `numerics/tools/` for the 96-mode rebuild. Six matrix archives (about 1.6 GB, two of
  them built in a cloud container and to be regenerated locally) live outside git under
  `shifted-zeta-positivity-archive/storage-depth/numerics-archives/`.
- Root README, `papers/README.md` and `MANIFEST.md` describe the seventh
  manuscript. No human review; not released.

### 2026-09-09 / 10 — finite-horizon Weil paper (branch `finite-horizon-weil`); large-file convention

- **New working draft `papers/weil-depth/`** — *Finite-horizon Weil coercivity and
  shifted-zeta contraction: two-sided certificates for the finite-window Weil form
  through total horizon log 7* (22 pp.). Computer-assisted two-sided enclosures of
  `λ_min(Q_{0,L})` at `L = log 2, …, log 6, 9/5, log 7` in Arb ball arithmetic
  (analytic infinite-tail bound, full-output parity Grams, Schur test with an
  explicit profile remainder; ball Rayleigh upper bounds), reproduced by an
  independent implementation and checked against the Fourier-side form; each
  floor converted to a small-shift contraction of the transfer. Finite-depth
  statements only. Three machine-assisted review rounds on 9–10 Sept (v0.1 → v0.2
  Codex; v0.2 → v0.3 Claude with independent recomputation; v0.3 → v0.4 ChatGPT),
  each archived with the draft it reviewed under `archive/`. v0.4 changes are
  presentation and scope only: directed rounding in the certificate table,
  decay and horizon-ceiling claims restated as observations and resource
  projections, one denominator bound in the Laplace-line lemma corrected,
  classical hypotheses (Yoshida, Connes–Consani) cited as printed. No human
  review; not released.
- **Large-file convention.** New `LARGE_FILES.md`: committed files stay below
  about 1 MB; regenerable derived data are kept outside git in a sibling
  `shifted-zeta-positivity-archive/<slug>/numerics-archives/` folder, bound to
  the tree by file and content hashes in the small certificate records,
  described by a tracked `ARCHIVES.md` per paper, and located by scripts through
  an environment variable; pre-commit size check; repair procedure; what a
  release archives. Git LFS and shared drives rejected (LFS objects are absent
  from the tarball Zenodo archives). Root `.gitignore` excludes
  `numerics-archives/`. First instance: `papers/weil-depth/ARCHIVES.md` (about
  122 MB of ball matrices). The branch's early history still references those
  blobs; it is to be squash-merged into `main`, whose history has none.
- Root README, `papers/README.md` and `MANIFEST.md` describe the sixth manuscript
  and its layout; `build-latex.yml` builds the seventh PDF
  (`papers/weil-depth/manuscript/finite_horizon_weil.tex`, 22 pages).

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
