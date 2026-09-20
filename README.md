# shifted-zeta-positivity

Manuscripts and verification records for computer-assisted positivity in
shifted zeta canonical systems. Reproduction scripts for several numerical
checks are included; the primary first-slab Arb certificate bundle is not yet
in the public tree (see `code/README.md`).

Research program around Suzuki's shifted screw functions $\Psi_\omega$ and the
shifted scattering function $\Theta_\omega(z)=\xi(\tfrac12-\omega-iz)/\xi(\tfrac12+\omega-iz)$
for the Riemann zeta function: quantitative criteria for zero-free half-planes,
the associated inverse-spectral (Kreĭn string / canonical system) family, and
computer-assisted positivity certificates on its prime-free first slab.

Edward Baker — August–September 2026.

> **Status and disclosure.** Everything here was developed with substantial
> language-model assistance, in adversarial referee-style rounds with independent
> numerical recomputation. One manuscript is available as a preprint
> (`papers/shifted-zeta/first-slab-positivity/`, v1.0). The other seven manuscript folders are
> committed as clearly labelled **working drafts**: they have passed internal
> review rounds but **not** external human review, no release or DOI covers
> them as finished work, and each folder's `STATUS.md` says exactly what has
> been checked and what blocks release. Nothing in this repository claims
> progress toward the Riemann hypothesis or a new zero-free region. The
> per-statement verification status of the first-slab preprint is in `blueprint/`
> and `verification/`.

## Background

The program grew out of a series of papers, some posted as preprints and some
unpublished, that the author wrote over a period beginning around 2015. The
idea was to extend the Riemann zeta function into higher dimensions and use
symmetry arguments to constrain the location of the zeros - first through
quaternionic analysis and twistor theory, later through classical solutions of
the Yang-Mills equations in four dimensions.

Beginning in August 2026 the author returned to those ideas, broadening them,
relaxing assumptions and testing related approaches, in collaboration with
Claude (Anthropic) and then also with ChatGPT (OpenAI). The first attempts used
slice regular functions; the author found no route to nontrivial constraints
there, and turned to alternatives suggested by mathematical physics: Yang-Mills
theory and its supersymmetric generalizations, and Chern-Simons theory. It
became clear that approaching the system from its boundary was more natural,
which brought the work to inverse spectral problems and to Masatoshi Suzuki's
screw functions [arXiv:1204.1827, 2206.03682]. There the program settled, on a
bulk-boundary correspondence for the shifted screw function Ψ_ω that extends and
reinterprets Suzuki's shifted setting. That is where this repository begins.

The manuscripts, research notes, verification records and code here were
produced in that collaboration, under the author's direction, in the
referee-style rounds described in `verification/` and `notes/`. The author is
responsible for the content; the per-statement record of what has and has not
been independently checked is in `blueprint/` and `verification/`.

## The pieces and how they fit

The [papers index](papers/README.md) now separates the repository into three
areas:

- **[Shifted-zeta](papers/shifted-zeta/README.md)** groups the six papers built
  on Suzuki's framework. The conceptual path is psi-omega-margin (Paper 1)
  → omega-string (Paper 2) → defect-depth (Paper 3). The operator-positivity
  path is first-slab-positivity → weil-depth → storage-depth. The project
  README gives the full manuscript inventory, reading order, and status.
- **[SUSY positivity](papers/susy-positivity/README.md)** is the separate
  research program seeking a structural explanation of Weil positivity.
  Begin with its [background](papers/susy-positivity/background.pdf) and
  [research overview](papers/susy-positivity/PROGRAM_OVERVIEW.md). The
  [program index](papers/susy-positivity/README.md) lists five retained
  investigations and five complete earlier packages under
  `investigations/previous/`, along with the standalone finite-response note
  and current research assessment.
- **[Miscellaneous papers](papers/misc/README.md)** currently holds
  [rh-detector](papers/misc/rh-detector/README.md), the earlier work on a
  velocity-residual detector and the De Bruijn–Newman flow, predating the
  Suzuki program.

The shifted-zeta program's finite-window certificates reach through `log 7`
in Weil-depth and beyond it in storage-depth, including `(3/4) log 14` and
`log(56)/2`. These remain finite-depth statements; the status files record
the working normalizations, verification evidence, and open review.

| Directory | What it holds |
|---|---|
| [`papers/`](papers/README.md) | Project groups `shifted-zeta/`, `susy-positivity/`, and `misc/`, with each program’s current package index. Each paper retains its sources, PDF, status, and reproduction materials. Large Weil-depth and storage-depth data stay outside git. |
| `blueprint/` | Statement inventory per released paper: every definition, lemma and theorem stated self-contained, with its dependency graph, proof status, human-verification status and formalization feasibility. The entry point for formalizers. |
| `statements/` | The same inventory as machine-readable YAML (`ledger.yaml`). |
| `verification/` | What has been checked, how, by whom; referee-round records; independent recomputation scripts; checklists for volunteers. |
| `notes/` | Storage-depth lessons-learned note, plus an index and preparation checklist for the historical research-log migration; see `MANIFEST.md`. |
| `code/` | The release gate for the first-slab certificate code (not yet released). Per-paper reproduction scripts live next to their papers. |
| `references/` | Bibliography of external sources used. No third-party PDFs are redistributed. |
| `environment/` | Pinned Python environment for the verification scripts; each paper's `code/` has its own `requirements.txt`. |

## Large files

Git holds sources and small records only. Derived data that committed code
regenerates deterministically — at present the ball-matrix archives of
`papers/shifted-zeta/weil-depth/` (about 13 MB per horizon, 122 MB in all) and of
`papers/shifted-zeta/storage-depth/` (six recorded archives, about 1.6 GB in all; four
present locally, two regenerable) — are kept
outside the repository in `szp-archive/` (locally `/Users/Shared/szp-archive`),
bound to the tree by the hashes recorded in the small certificate files, and described by a tracked guide in
the paper folder (`papers/shifted-zeta/weil-depth/ARCHIVES.md`, `papers/shifted-zeta/storage-depth/ARCHIVES.md`). The convention (a 1 MB
ceiling on committed files, no regenerable data in git, two hashes per
dataset, hash-bound replay, an environment-variable lookup), the folder
layout, the step-by-step procedure for adding or moving such a file, the
pre-commit size check, how to repair a mistaken commit and what a release does
and does not archive are in [`LARGE_FILES.md`](LARGE_FILES.md). Git LFS and
shared drives are deliberately not used; a non-regenerable dataset would get
its own Zenodo record instead.

## Releases, DOIs and how to cite

This is a **single repository** for the whole program. Releases are git tags
`vMAJOR.MINOR`; the Zenodo–GitHub integration archives the entire tree at each
tag and mints a *version DOI*, all versions sharing one *concept DOI*.

**Current state.** No release has been tagged and no DOI exists yet; the
`v1.0` release described below is the plan for the first tag. Two version
numbers are in play and they are separate identifiers: the *repository*
version (root `CITATION.cff`, currently `0.2.0`, set to the tag when it is
created) and the *manuscript* version (`1.0`, stated in the preprint's PDF and
in `papers/shifted-zeta/first-slab-positivity/CITATION.cff`).

**What a release contains.** A tag archives everything present in the tree
at that moment — including the working-draft folders, and nothing kept
outside the tree (`LARGE_FILES.md` explains why that is complete for
regenerable data). A draft is therefore
archived *as a draft*: its `STATUS.md` states that it is not a released
manuscript, the release notes list which folders are released, and only those
folders are to be cited. Tagging is done only when everything committed is fit
to be archived permanently in that sense: released paper sources and PDFs, the
`blueprint/`, `statements/` and `verification/` records, code that has passed
its release gate, drafts whose `STATUS.md` is current, and notes that have
been through the redaction checklist. `v1.0` releases the first-slab preprint
and the material around it.

**Citing a paper in this repository.** Until a release exists, cite the
folder at a specific commit (take the hash from `git rev-parse HEAD` or the
GitHub permalink of the folder):

> E. Baker, *Archimedean first-slab positivity for shifted zeta canonical
> systems: an off-center Weil generator and a radial energy identity*,
> preprint v1.0, 2026, in: *shifted-zeta-positivity*,
> <https://github.com/ebbaker/shifted-zeta-positivity>, folder
> `papers/shifted-zeta/first-slab-positivity/`, commit ⟨hash⟩.

Once a release is archived, cite the *version* DOI (it pins the content) and
name the folder:

> E. Baker, *⟨title⟩*, preprint v⟨X.Y⟩, in: *shifted-zeta-positivity*,
> release v⟨A.B⟩, Zenodo, doi:10.5281/zenodo.⟨version DOI⟩, folder
> `⟨paper folder path⟩/`, 2026.

Angle-bracketed fields are placeholders, not identifiers; no DOI in this
repository is real until it appears in a `CITATION.cff` `doi:` field.

Each released paper folder also has its own `CITATION.cff`. Because indexers
read the *record* title, the plan is to deposit each released paper as its own
Zenodo record (PDF, using the folder's `.zenodo.json` as metadata, no code)
and link the two records with Zenodo's related identifiers
(`isPartOf` / `hasPart`). The paper record identifies the manuscript version;
the repository record additionally archives the surrounding files. Use the
paper record's DOI where a journal-style reference is wanted, the repository
version DOI where the surrounding verification material matters.

**After each release:** paste the version DOI into the citation blocks in
`papers/README.md` and the released folder's `README.md`/`CITATION.cff`, add
the paper record's DOI to the root `.zenodo.json` under `related_identifiers`
(`hasPart`), and update `CHANGELOG.md`.

## For formalizers and other verifiers

Start at `blueprint/first-slab/statements.md`: it lists every statement of the
preprint with what depends on what, whether it is proved on paper, certified
by computer, or only asserted, whether a human has checked it, and how
feasible a Lean/Mathlib formalization looks. The seven working-draft folders do not
have blueprints yet; their `STATUS.md` files carry a result-by-result
verification record in the meantime. The two premise checks the internal
review cannot perform — the normalization chain against Suzuki's paper and
the originality search — have a written protocol in
`verification/first-slab/PROTOCOL_C1_C2.md`. Issues labelled
`good-first-check` are the elementary items. `CONTRIBUTING.md` has the house
rules; the issue templates cover verification reports, possible errors and
formalization work.

## Licenses

Licensing by material type, see [`LICENSE`](LICENSE): text (papers, notes, documentation)
under CC BY 4.0; code under MIT. Third-party material is cited, not redistributed.

## Contact

Edward Baker - edwardbaker86_AT_gmail_DOT_com. Repository:
<https://github.com/ebbaker/shifted-zeta-positivity>.

This is a personal research project of the author, who is co-founder of
NeoQuortex, which develops AI-enhanced algorithms for computational chemistry and multiscale modeling leveraging next generation computing hardware. The project is independent of the
company and is not affiliated with it. Verification reports, possible errors and
formalization work: open an issue with the matching template.

ORCID ID: 0000-0001-5459-9993
