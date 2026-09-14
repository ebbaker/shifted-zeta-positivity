# Papers and research projects

The papers are organized by research program. Each manuscript keeps its own
source, PDF, status record, and associated code or numerical supplement.

| Folder | Role | Start here |
|---|---|---|
| [`shifted-zeta/`](shifted-zeta/README.md) | The six-paper program around Suzuki's shifted screw functions, inverse spectral systems, and finite-horizon positivity. | The project README explains the papers' relationships and reading order. |
| [`susy-positivity/`](susy-positivity/README.md) | The program seeking a structural explanation of Weil positivity, with individual approaches under `attempts/`. | [Background](susy-positivity/background.pdf); [program overview](susy-positivity/PROGRAM_OVERVIEW.md); [positive-factorizations attempt](susy-positivity/attempts/positive-factorizations/README.md) and [status](susy-positivity/attempts/positive-factorizations/STATUS.md). |
| [`misc/`](misc/README.md) | Separate papers outside those two programs; currently the earlier `rh-detector` draft. | [Miscellaneous papers](misc/README.md). |

## Status

As of 11 September 2026, there are eight manuscript folders. Only
[`first-slab-positivity`](shifted-zeta/first-slab-positivity/README.md) is at
release stage (preprint v1.0), intended for the planned repository `v1.0` tag.
No tag has been created and no DOI exists yet. The other seven folders are
working drafts; read each paper's `STATUS.md` (or `VERIFICATION_STATUS.md`
for the first-slab preprint) before citing it. This reorganization changes neither manuscript versions nor review status.

The SUSY program background and continuation note are at its root. Round-4
reports accompany the positive-factorizations attempt in
`susy-positivity/attempts/positive-factorizations/archive/progress-reports/`;
they have not been incorporated into manuscript v0.2.

## Layout and older paths

The six shifted-zeta folders moved from `papers/<slug>/` to
`papers/shifted-zeta/<slug>/`; `papers/rh-detector/` moved to
`papers/misc/rh-detector/`. `papers/susy-positivity/` is now a program root;
its manuscript and support moved into `attempts/positive-factorizations/`.
See its [move and validation record](susy-positivity/REORGANIZATION_20260912.md). Older
manuscripts, archived drafts, and review records retain their original path
references: apply this mapping when reading them in the current checkout,
or use their original commit for an exact historical view.

Weil-depth and storage-depth use `manuscript/`, `numerics/`, and `archive/`
subfolders, with current `BUILD_RECORD.json`, `SHA256SUMS.txt`, and
`ARCHIVES.md` at the paper root. Their large derived data stay outside git;
see the [large-file policy](../LARGE_FILES.md). Shared `blueprint/`,
`statements/`, `verification/`, `notes/`, and `code/` remain at the repository
root. The [shifted-zeta guide](shifted-zeta/README.md) links the relevant
entry points.

## How to cite a paper in this repository

Two equivalent forms. Use the **version** DOI of the release (not the concept
DOI) so that the citation pins the content. Only released folders should be
cited as manuscripts; a draft may be referred to by folder path and commit
hash as a work in progress.

*Repository form* (when the surrounding verification material matters):

> E. Baker, *⟨paper title⟩*, ⟨preprint version⟩, in: *shifted-zeta-positivity*,
> release v⟨X.Y⟩, Zenodo, doi:10.5281/zenodo.⟨version DOI⟩, folder
> `⟨paper folder path⟩/`, 2026.

*Paper-record form* (journal-style; each released paper is also deposited as
its own Zenodo record with the paper's title and abstract):

> E. Baker, *⟨paper title⟩*, ⟨preprint version⟩, Zenodo,
> doi:10.5281/zenodo.⟨paper record DOI⟩, 2026.

Citation block for the release-stage preprint:

**first-slab-positivity, v1.0** — no release or DOI exists yet. Until the
first tag, cite the folder at a commit (hash from `git rev-parse HEAD` or the
folder's GitHub permalink):

> E. Baker, *Archimedean first-slab positivity for shifted zeta canonical
> systems: an off-center Weil generator and a radial energy identity*,
> preprint v1.0, 2026, in: *shifted-zeta-positivity*,
> <https://github.com/ebbaker/shifted-zeta-positivity>, folder
> `papers/shifted-zeta/first-slab-positivity/`, commit ⟨hash⟩.

After the `v1.0` release the block becomes the repository form above with the
real version DOI. BibTeX skeleton for that stage (`@misc` is what Zenodo
exports; adjust to your style; ⟨…⟩ are placeholders, not identifiers):

```bibtex
@misc{baker2026firstslab,
  author       = {Baker, Edward},
  title        = {Archimedean first-slab positivity for shifted zeta canonical systems:
                  an off-center {W}eil generator and a radial energy identity},
  year         = {2026},
  howpublished = {Preprint v1.0, in: shifted-zeta-positivity, release v1.0, folder
                  \texttt{papers/shifted-zeta/first-slab-positivity/}},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.⟨version DOI⟩},
  note         = {Computer-assisted; verification status in the repository}
}
```

## Cross-citation policy

Papers 1–3 and the preprint cite each other as "companion manuscripts". Two
rules adopted on 28 Aug 2026 (see `notes/ROUND19_endpoint_length_and_freeze.md` §1):

- Every cross-citation carries the *name* of the cited statement ("critical-shift
  dichotomy", "linear margin", "shift-energy identity"), not only a theorem
  number, because numbering in unreleased drafts moves.
- A one-pass renumbering against the actually released version of each cited
  paper is a standing pre-release checklist item for every paper.

Current dependencies: Paper 2 cites the **concise** version of Paper 1
(numbers as of the 28 Aug copy); Paper 3 cites Papers 1 and 2 with
placeholder keys (`MarginPaper`, `StringPaper`); the preprint cites all three
as *E. Baker, manuscript, August 2026* (bibliography items `Baker2026string`,
`Baker2026margin`, `Baker2026depth`). When a companion is released, update
the citing papers to the repository form above and issue a new release.

## Release checklist (any manuscript)

1. Author block and ORCID filled in (the papers carry no institutional affiliation; see the repository README).
2. Every bibliography entry verified against the source (no `%% VERIFY` markers left).
3. Cross-citations renumbered against released versions.
4. `blueprint/<slug>/statements.md` and the corresponding `statements/ledger.yaml` section written.
5. A `VERIFICATION_STATUS.md` in the folder saying what has and has not been human-checked.
6. `CITATION.cff` (valid against the CFF 1.2.0 schema — `tools/check_citations.py`) and `.zenodo.json` present in the folder; license stated.
7. PDF built from the committed `.tex` on a clean TeX Live (`latexmk -pdf`); the CI workflow passes.
8. Figures regenerated from committed scripts or data (Paper 2: `fig_density.png`; Paper 3: Figures 1–5).
9. Reproduction code under `code/` (or `numerics/` for Weil-depth and storage-depth) with `README.md` mapping scripts to results and a pinned `requirements.txt`; scripts that ran only inline in the notes reconstructed as files.
10. Tag the release; then deposit the paper's own Zenodo record (PDF + folder `.zenodo.json`), link the two records (`isPartOf` / `hasPart`), paste both DOIs into the citation blocks.
