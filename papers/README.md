# Papers and research projects

16 October 2026. Index of `papers/`, prepared for Edward Baker with LLM
assistance (Claude Opus 5.5, configured identifier `claude-opus-5-5`, Claude
Cowork, reasoning effort max).

The research folders are grouped by line of work. Each program or
investigation keeps its own manuscripts, notes, numerics, reviews, chat
histories and status records; the group folders only organize them. No
shared research folders remain at the repository root: the first slab keeps
its statement blueprint, verification records and certificate release gate in
[its folder](weil-positivity/shifted-zeta/first-slab-positivity/README.md),
and the RH3 research log is with the
[early project files](../early-chat-logs/initial-project-files/README.md).

| Folder | What it holds | Period | Start here |
|---|---|---|---|
| [`weil-positivity/`](weil-positivity/README.md) | The positivity line: the six shifted-zeta papers and the SUSY-positivity program, aimed at the complete central Weil form. | Aug–Sep 2026 | [Line guide](weil-positivity/README.md); [shifted-zeta guide](weil-positivity/shifted-zeta/README.md); [SUSY background](weil-positivity/susy-positivity/background.pdf). |
| [`investigations/`](investigations/README.md) | Cross-program investigations: CCM operator realizations and fractal Laplacians, character channels, the Sonin critical-boundary manuscript, and the program meta-analysis. | 26 Sep – 3 Oct 2026 | [Index](investigations/README.md); [program meta-analysis](investigations/program-meta-analysis/README.md). |
| [`quasi-rh/`](quasi-rh/README.md) | The zero-strip line: prime-variance exponents, quasi-RH exponent descent with the Newman-collision projects, and character amplification. | 3–11 Oct 2026 | [Line guide](quasi-rh/README.md). |
| [`investigations-2/`](investigations-2/README.md) | The second investigation portfolio, grown from the exponent-descent brainstorms: active and inactive program homes, the Newman certificate audit and the formal-replay crosswalk. | 12 Oct 2026 onward | [Portfolio overview](investigations-2/README.md); [active programs](investigations-2/active/README.md). |
| [`brainstorm/`](brainstorm/README.md) | Reflection between major investigation series and discussion before choosing the next program. | 16 Oct 2026 onward | [Brainstorm index](brainstorm/README.md); [investigations 3 discussion](brainstorm/investigations-3/README.md). |
| [`misc/`](misc/README.md) | Separate earlier work, currently the RH-detector draft. | Aug 2026 | [Miscellaneous papers](misc/README.md). |

Short summaries of what has been established, in the sources' own status
words, are in [result-summaries](../result-summaries/README.md): clusters
01–06 cover `weil-positivity/`, 07–08 `investigations/` and `misc/`, 09–11
`quasi-rh/`, and 10–14 plus 16 `investigations-2/` (10 and 11 span both); 15 is
repository-wide. Recurring patterns to avoid are in [avoid](../avoid/README.md).

The inter-series brainstorm entry was added on 16 October 2026 for Edward
Baker with substantial LLM assistance, **gpt-6-astra**, effort **ultra**.

## How the work developed

1. **Shifted zeta (August to early September).** Six papers on Suzuki's
   shifted screw functions: time-domain criteria, the shifted-zeta string,
   defect detection, and finite-window positivity certificates.
2. **SUSY positivity (September).** The search for an independently positive
   structure whose pairing is the complete Weil form: supersymmetric and
   gauge-theoretic sources, Wilson lines, Loewner evolution and
   Wilson–Loewner.
3. **Cross-program investigations (26 September to 3 October).** CCM spectral
   realizations, character channels and Sonin critical-boundary traces. The
   Sonin subpower milestones led to the next line.
4. **Prime variance exponents (3–4 October).** A fixed variance exponent for
   one prepared prime response is equivalent to a closed zero strip, so
   exponents tending to zero are equivalent to RH.
5. **Quasi-RH descent and amplification (8–11 October).** Whether a fixed
   zero strip can be improved to RH: arithmetic exponent descent, character
   families, and exclusion of positive-time Newman collisions.
6. **Second portfolio (12 October onward).** Audits of the quasi-RH sources
   and of a Newman certificate, Euler-factor controls, and the theta geometry
   near possible collisions.

## Status

Only [first-slab-positivity](weil-positivity/shifted-zeta/first-slab-positivity/README.md)
is at release stage (preprint v1.0); no release tag or DOI exists yet. The
other manuscripts are working drafts with their own scope and review records,
and no result in the repository has had independent specialist review. Each
line's guide and each folder's README give the current state; the
[investigations-2 overview](investigations-2/README.md) describes the active
programs.

## Older paths

Older manuscripts, notes, reviews, numerical records and chat histories keep
the paths of their time. To read one in the current checkout, apply every
later move below, oldest first, or open the file at its original commit.

| Date | From | To | Record |
|---|---|---|---|
| 12 Sep 2026 | top-level manuscript files and `archive/overview/` of `papers/susy-positivity/` | the program root and `attempts/positive-factorizations/`, now `investigations/previous/positive-factorizations/` | [12 September record](weil-positivity/susy-positivity/archive/REORGANIZATION_20260912.md); [SUSY path guide](weil-positivity/susy-positivity/archive/README.md) |
| 14 Sep 2026 | `papers/<slug>/` for the six shifted-zeta papers | `papers/shifted-zeta/<slug>/` | commit `b3ac36e` |
| 14 Sep 2026 | `papers/rh-detector/` | `papers/misc/rh-detector/` | commit `b3ac36e` |
| 14 Sep 2026 | `papers/finite-response-weil-positivity/` | `papers/susy-positivity/manuscripts/finite-response-weil-positivity/` | [SUSY path guide](weil-positivity/susy-positivity/archive/README.md) |
| 20 Sep 2026 | `papers/susy-positivity/investigations/<package>/` for five packages | `papers/susy-positivity/investigations/previous/<package>/` | [20 September map](weil-positivity/susy-positivity/archive/REORGANIZATION_20260920.md) |
| 13 Oct 2026 | nine folders in `papers/investigations-2/active/` | `papers/investigations-2/inactive/` | [consolidation record](investigations-2/PORTFOLIO_CONSOLIDATION_20261013.md) |
| 16 Oct 2026 | `papers/shifted-zeta/`, `papers/susy-positivity/` | `papers/weil-positivity/shifted-zeta/`, `papers/weil-positivity/susy-positivity/` | [16 October record](REORGANIZATION_20261016.md) |
| 16 Oct 2026 | `papers/prime-variance-exponents/`, `papers/quasi-rh-exponent-descent/`, `papers/quasi-rh-character-amplification/` | `papers/quasi-rh/<same name>/` | [16 October record](REORGANIZATION_20261016.md) |
| 16 Oct 2026 | root `blueprint/first-slab/statements.md`, `blueprint/README.md`, `statements/ledger.yaml`, `verification/` (with its `first-slab/` level dropped), `environment/requirements.txt`, `code/` | the first slab's `blueprint/`, `verification/`, `verification/requirements.txt` and `CERTIFICATE_CODE.md`, in `papers/weil-positivity/shifted-zeta/first-slab-positivity/`; `environment/requirements_metadata.txt` to `tools/` | [16 October record](REORGANIZATION_20261016.md#root-folders) |
| 16 Oct 2026 | root `notes/`, `Claude outputs/`, `chat-histories/` | `early-chat-logs/initial-project-files/rh3/` (index, redaction checklist), storage-depth (lessons note), SUSY `archive/` (research brief), the first slab's `verification/repository-review-20260909/`; the YM copies already in `wilson-loewner/YM/`; `early-chat-logs/chatgpt-codex/` | [16 October record](REORGANIZATION_20261016.md#root-folders) |

Commit-pinned citations keep the paths of their commit and must not be
rewritten.

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
> `papers/weil-positivity/shifted-zeta/first-slab-positivity/`, commit ⟨hash⟩.

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
                  \texttt{papers/weil-positivity/shifted-zeta/first-slab-positivity/}},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.⟨version DOI⟩},
  note         = {Computer-assisted; verification status in the repository}
}
```

The cross-citation policy for the shifted-zeta papers is in the
[shifted-zeta guide](weil-positivity/shifted-zeta/README.md#cross-citation-policy).

## Release checklist (any manuscript)

1. Author block and ORCID filled in (the papers carry no institutional affiliation; see the repository README).
2. Every bibliography entry verified against the source (no `%% VERIFY` markers left).
3. Cross-citations renumbered against released versions.
4. `blueprint/statements.md` and `blueprint/ledger.yaml` written in the paper's folder, as in the first slab's [blueprint](weil-positivity/shifted-zeta/first-slab-positivity/blueprint/README.md).
5. A `VERIFICATION_STATUS.md` in the folder saying what has and has not been human-checked.
6. `CITATION.cff` (valid against the CFF 1.2.0 schema — `tools/check_citations.py`) and `.zenodo.json` present in the folder; license stated.
7. PDF built from the committed `.tex` on a clean TeX Live (`latexmk -pdf`); the CI workflow passes.
8. Figures regenerated from committed scripts or data (Paper 2: `fig_density.png`; Paper 3: Figures 1–5).
9. Reproduction code under `code/` (or `numerics/` for Weil-depth and storage-depth) with `README.md` mapping scripts to results and a pinned `requirements.txt`; scripts that ran only inline in the notes reconstructed as files.
10. Tag the release; then deposit the paper's own Zenodo record (PDF + folder `.zenodo.json`), link the two records (`isPartOf` / `hasPart`), paste both DOIs into the citation blocks.
