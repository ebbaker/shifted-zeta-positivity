# Storage-depth writing project closeout — 11 September 2026

The [storage-depth paper](README.md), *Residual-controlled depth extension
of finite-horizon Weil positivity: a spatial continuation past log 7 for the
shifted-zeta transfer*, is closed out as working draft v0.3 (21 pages).
The `critical_path` research branch is merged into `main` with its five
research commits preserved, followed by the housekeeping changes recorded here.
This closes the writing project; it creates no release, DOI or new mathematical
certificate. [STATUS.md](STATUS.md) and [CLAIMS.json](CLAIMS.json) remain the
authoritative records of the claims and their review limits.

## Repository housekeeping

- All 26 current README files link to storage-depth. The 12 README files
  inside versioned draft snapshots remain unchanged, together with their
  original checksum and provenance records. Current archive indexes point to
  the new paper and explain the older layout.
- The root and paper indexes, blueprint/code/verification indexes, manifest,
  changelog and repository deposit metadata now agree on seven manuscript
  folders: the first-slab preprint and six working drafts.
- Current archive guides use `szp-archive`, locally
  `/Users/Shared/szp-archive`, with `WEIL_ARCHIVES` and
  `STORAGE_DEPTH_ARCHIVES` as the existing lookup variables. Historical
  snapshots retain their original paths; no loader or builder was changed.
- The existing lessons-learned note was moved from `Claude outputs/` to
  [notes/](../../../notes/README.md), retaining the author's pending wording
  change. The supersymmetric briefs belong to a separate project and commit.
- The dependency appendix now distinguishes the failed 32-mode second-step
  tests from the successful 96-mode R18 tests already reported in the body.
  Three overlong lines and a PDF bookmark warning were corrected. Numerical
  records, certificate constants and mathematical arguments were unchanged.
- Current storage-depth and Weil-depth build/checksum manifests were refreshed
  after the documentation changes. A standard-library
  [hygiene checker](../../../tools/check_repository_hygiene.py) and CI workflow
  now check file sizes, current README navigation and both current manifests.

## Checks performed

| Check | Result and scope |
|---|---|
| Original source/PDF correspondence | Clean local LaTeX rebuild: 21 pages, with identical extracted text on every page to the original committed PDF. |
| Closeout PDF | Rebuilt from the edited source, still 21 pages; rendered pages inspected. The appendix clarification and typesetting changes are described above. |
| Package integrity | Current build-record hashes, byte sizes and SHA-256 manifests checked against tracked files; archived draft files preserved. |
| Repository size | No tracked file exceeds 1 MiB; no blob introduced by the five `critical_path` research commits exceeds 1 MiB. Large numerical data remain outside git. |
| External archive integrity | All 20 entries in the pre-existing storage-depth and Weil-depth checksum manifests passed. Archive READMEs were refreshed and checksum manifests expanded to include other files present, including the R18 regeneration notes. |
| Storage matrix catalog | Four present matrices match their recorded sizes and stored-file hashes; the two R18 matrices are absent, as detailed below. Canonical matrix-content hashes and numerical certificates were not recomputed in this housekeeping audit. |

The earlier `finite-horizon-weil` branch was already squash-merged as
`76b0d32` and deleted remotely. A stale local copy can retain its old large
objects; it must not be merged into `main` again. This closeout does not
rewrite history or require a new clone.

## External data availability and accepted omissions

The six matrix records describe about 1.6 GB in total. Four matrix files
(about 675 MB) are present under `szp-archive/storage-depth/numerics-archives/`.
The following R18 matrices are **not present locally**:

- `history/first-step-96-20260911/closure_256_96.matrices.json.gz`
- `output/second-quarter-96/central_matrices.json.gz`

Their small build records, seed catalog, exact continuation file and
`REGENERATE.md` instructions are present in the archive. The committed
[ARCHIVES.md](ARCHIVES.md) preserves expected sizes, both hashes and the
regeneration commands. The author accepted this availability state for the
writing-project closeout; these matrices were not regenerated here.

Additional large Fourier-analysis outputs from Claude were intentionally
not added to `szp-archive` because of their size. The author confirmed that
this omission is acceptable. The small R17 diagnostics already in
`numerics/fourier_side/` remain tracked. Acquiring or recomputing the omitted
outputs is not a closeout task, and this record does not claim those outputs
were archived or verified.

The external review scripts, including `barrier_numerics.py`, `ladder_fit.py`,
`farband.py` and `twisted.py`, are present under
`szp-archive/storage-depth/reviews/2026-09-10_review-of-v0.2_claude/numerics/`.
The barrier/ladder note's phrase "beside this note" refers to that external
review material, not to the tracked `archive/reviews/` folder. These are
exploratory diagnostics and were not rerun as part of closeout.

## Deferred review and research

The independent normalization audit, human mathematical review, formal
verification, independent reconstruction of the spatial matrices and any
rigorous Fourier tail analysis remain open. The proposed further depth
experiments and barrier/ladder investigations are future research, not
requirements for this repository merge. No open research item has been marked
verified merely because the writing project is closed.

For a fresh packaging check, run from the repository root:

```bash
python3 tools/check_repository_hygiene.py
make -C papers/shifted-zeta/storage-depth TEXBUILD=/tmp/storage-depth-closeout
```

A rebuild changes the PDF file hash through metadata even when its text
matches. Refresh the current package manifests before committing a rebuilt
PDF; leave historical snapshot manifests unchanged.
