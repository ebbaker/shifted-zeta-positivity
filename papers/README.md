# Manuscripts

One folder per manuscript. Each folder holds the LaTeX source and PDF, a
`README.md` describing the contents, a `STATUS.md` with stage, provenance,
verification record and release blockers, and — where the paper has
reproduction code — a `code/` subfolder with its own `requirements.txt`.

**Only `first-slab-positivity/` is released.** The other four folders are
working drafts, committed at the author's decision on 8–9 September 2026 as
an exception to the original sources-only-when-released rule: nothing in
them is covered by a release or DOI as a finished manuscript, and each
`STATUS.md` says so explicitly. Cite nothing from a draft folder without
reading its `STATUS.md`. Status as of 9 September 2026.

| Folder | Title | Stage | Released |
|---|---|---|---|
| `first-slab-positivity/` | Archimedean first-slab positivity for shifted zeta canonical systems: an off-center Weil generator and a radial energy identity | Preprint v1.0 (5 Sept 2026), 24 pp.; two adversarial review rounds; clean-room certificate audit; Part 0 of the verification checklist applied; statement inventory in `blueprint/first-slab/` | **yes** |
| `psi-omega-margin/` | The margin in the shifted screw-function criterion for zero-free half-planes ("Paper 1", 21 pp.) with the concise companion *Quantitative asymptotics for Suzuki's shifted screw functions* (9 pp., the intended submission) | Working draft after the 27 Aug fold-in; referee rounds 12–14 with independent recomputation; author block filled (Edward B. Baker III); scripts `c1`–`c8` and two supplementary notes committed | no — working draft |
| `omega-string/` | The shifted zeta string: an unconditional inverse-spectral family and its RH endpoint ("Paper 2", 13 pp.) | Working draft v5, frozen 28 Aug pending human specialist review; five referee passes; Kasahara (1975) source-verified 8 Sept; author block filled; figure script and two verification scripts committed | no — working draft |
| `defect-depth/` | Detection depth of spectral defects in shifted zeta strings ("Paper 3", 15 pp.) | Working draft v1 (29 Aug) from the Ihara laboratory; all manuscript gates GO; author block empty; 17 bibliography entries still `%% VERIFY`; figures are placeholders; laboratory code committed under `code/` | no — working draft |
| `rh-detector/` | A certified velocity-residual detector for off-axis zeros of the Riemann Ξ-function, and the De Bruijn–Newman flow as a matrix pencil on Calogero–Moser space (10 pp.) | Working draft of 25 Aug; numerics regenerated and re-verified after a workspace loss, smoke-tested 9 Sept; certified modulo floating point; author block empty; scripts and zero caches committed under `code/` | no — working draft |

**Two threads.** Papers 1–3 and the preprint form one program built on
Suzuki's shifted screw functions and shifted scattering function; they cite
each other as companions. `rh-detector/` is a **separate, earlier thread**,
written on 24–25 August 2026 before the Suzuki line of work began; it is
unrelated to that program and carries no companion cross-citations.

## How to cite a paper in this repository

Two equivalent forms. Use the **version** DOI of the release (not the concept
DOI) so that the citation pins the content. Only released folders should be
cited as manuscripts; a draft may be referred to by folder path and commit
hash as a work in progress.

*Repository form* (when the surrounding verification material matters):

> E. Baker, *⟨paper title⟩*, ⟨preprint version⟩, in: *shifted-zeta-positivity*,
> release v⟨X.Y⟩, Zenodo, doi:10.5281/zenodo.⟨version DOI⟩, folder
> `papers/⟨slug⟩/`, 2026.

*Paper-record form* (journal-style; each released paper is also deposited as
its own Zenodo record with the paper's title and abstract):

> E. Baker, *⟨paper title⟩*, ⟨preprint version⟩, Zenodo,
> doi:10.5281/zenodo.⟨paper record DOI⟩, 2026.

Filled-in blocks for released papers:

**first-slab-positivity, v1.0** — *DOIs to be pasted after the v1.0 release.*

> E. Baker, *Archimedean first-slab positivity for shifted zeta canonical
> systems: an off-center Weil generator and a radial energy identity*,
> preprint v1.0, in: *shifted-zeta-positivity*, release v1.0, Zenodo,
> doi:10.5281/zenodo.NNNNNNN, folder `papers/first-slab-positivity/`, 2026.

BibTeX skeleton (`@misc` is what Zenodo exports; adjust to your style):

```bibtex
@misc{baker2026firstslab,
  author       = {Baker, Edward},
  title        = {Archimedean first-slab positivity for shifted zeta canonical systems:
                  an off-center {W}eil generator and a radial energy identity},
  year         = {2026},
  howpublished = {Preprint v1.0, in: shifted-zeta-positivity, release v1.0, folder
                  \texttt{papers/first-slab-positivity/}},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.NNNNNNN},
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
6. `CITATION.cff` and `.zenodo.json` present in the folder; license stated.
7. PDF built from the committed `.tex` on a clean TeX Live (`latexmk -pdf`); the CI workflow passes.
8. Figures regenerated from committed scripts or data (Paper 2: `fig_density.png`; Paper 3: Figures 1–5).
9. Reproduction code under `code/` with `README.md` mapping scripts to results and a pinned `requirements.txt`; scripts that ran only inline in the notes reconstructed as files.
10. Tag the release; then deposit the paper's own Zenodo record (PDF + folder `.zenodo.json`), link the two records (`isPartOf` / `hasPart`), paste both DOIs into the citation blocks.
