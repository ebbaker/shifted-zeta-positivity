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
> (`papers/first-slab-positivity/`, v1.0). The other five manuscripts are
> committed as clearly labelled **working drafts**: they have passed internal
> review rounds but **not** external human review, no release or DOI covers
> them as finished work, and each folder's `STATUS.md` says exactly what has
> been checked and what blocks release. Nothing in this repository claims
> progress toward the Riemann hypothesis or a new zero-free region. The
> per-statement verification status of the released result is in `blueprint/`
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

Folder names are the `papers/` slugs; quoted lines are the manuscripts' actual
titles; "Paper 1–3" are the working labels used throughout `notes/` and
`verification/`.

```
                 Suzuki: Ψ_ω, Θ_ω, canonical systems  [arXiv 1204.1827, 2206.03682]
                                     │
        ┌────────────────────────────┼────────────────────────────────┐
        ▼                            ▼                                ▼
 papers/psi-omega-margin/     papers/omega-string/           papers/first-slab-positivity/
 (Paper 1, time domain)       (Paper 2, inverse-spectral)    (preprint v1.0, operator side)
 "The margin in the shifted   "The shifted zeta string:      "Archimedean first-slab
  screw-function criterion     an unconditional inverse-      positivity for shifted zeta
  for zero-free half-planes"   spectral family and its        canonical systems: an off-
 + concise "Quantitative       RH endpoint"                   center Weil generator and a
  asymptotics for Suzuki's                                    radial energy identity"
  shifted screw functions"
 Ψ_ω = (ξ'/ξ)(½+ω)·t + …;     q_ω, ρ_ω, m_ω; RH ⟺ family     ‖H_{ω,L}‖<1 on L≤log 2, 0<ω≤½;
 margin, threshold, order     extends to all ω>0; endpoint   off-center Weil generator;
 parameter, windows           degeneration                   Arb interval certificate
 [draft, 21 pp. + 9 pp.]      [draft v5, 13 pp.]             [released]
        │                            │
        └──────────────┬─────────────┘
                       ▼
                 papers/defect-depth/  (Paper 3)  [draft v1, 15 pp.]
                 "Detection depth of spectral defects in shifted zeta strings"
                 how a hypothetical off-line quartet is detected in each
                 coordinate: Christoffel/CF depth vs time-domain envelope
                 (grew out of the finite Ihara-zeta laboratory, papers/defect-depth/code/)
```

Continuing the operator side of the preprint past the prime-free first slab:

```
 papers/weil-depth/  [working draft v0.4, 22 pp.]  (9–10 Sept 2026)
 "Finite-horizon Weil coercivity and shifted-zeta contraction: two-sided certificates
  for the finite-window Weil form through total horizon log 7"
 m_j ≤ λ_min(Q_{0,L_j}) ≤ μ_j certified in Arb ball arithmetic at L = log 2, …, log 6, 9/5, log 7
 (prime-power delays 2, 3, 4, 5 active; even ground state at every horizon); each floor
 gives a small-shift contraction ‖V_{ω,L}‖ ≤ e^{−dω}. Finite-depth statements only.
 Layout differs from the other folders (manuscript/, numerics/, archive/); its ~13 MB
 ball-matrix archives are kept outside git — see LARGE_FILES.md and the folder's ARCHIVES.md.
```

Separately, and **before** the Suzuki line of work began:

```
 papers/rh-detector/  [draft, 10 pp.]  (24–25 Aug 2026; unrelated to the Suzuki program)
 "A certified velocity-residual detector for off-axis zeros of the Riemann Ξ-function,
  and the De Bruijn–Newman flow as a matrix pencil on Calogero–Moser space"
```

| Directory | What it holds |
|---|---|
| `papers/` | One folder per manuscript: source, PDF, `README.md`, `STATUS.md`, and the paper's own reproduction code under `code/` where it exists. `first-slab-positivity/` is the released preprint; the other five are working drafts (see `papers/README.md`). `weil-depth/` keeps its large derived data outside git, described by its tracked `ARCHIVES.md`. |
| `blueprint/` | Statement inventory per released paper: every definition, lemma and theorem stated self-contained, with its dependency graph, proof status, human-verification status and formalization feasibility. The entry point for formalizers. |
| `statements/` | The same inventory as machine-readable YAML (`ledger.yaml`). |
| `verification/` | What has been checked, how, by whom; referee-round records; independent recomputation scripts; checklists for volunteers. |
| `notes/` | Index and preparation checklist for a planned research-log migration. The indexed round reports are not yet included; see `MANIFEST.md`. |
| `code/` | The release gate for the first-slab certificate code (not yet released). Per-paper reproduction scripts live next to their papers. |
| `references/` | Bibliography of external sources used. No third-party PDFs are redistributed. |
| `environment/` | Pinned Python environment for the verification scripts; each paper's `code/` has its own `requirements.txt`. |

## Large files

Git holds sources and small records only. Derived data that committed code
regenerates deterministically — at present the ball-matrix archives of
`papers/weil-depth/`, about 13 MB per horizon and 122 MB in all — are kept
outside the repository in a sibling folder, bound to the tree by the hashes
recorded in the small certificate files, and described by a tracked guide in
the paper folder (`papers/weil-depth/ARCHIVES.md`). The convention (a 1 MB
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
in `papers/first-slab-positivity/CITATION.cff`).

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
> `papers/first-slab-positivity/`, commit ⟨hash⟩.

Once a release is archived, cite the *version* DOI (it pins the content) and
name the folder:

> E. Baker, *⟨title⟩*, preprint v⟨X.Y⟩, in: *shifted-zeta-positivity*,
> release v⟨A.B⟩, Zenodo, doi:10.5281/zenodo.⟨version DOI⟩, folder
> `papers/⟨slug⟩/`, 2026.

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
feasible a Lean/Mathlib formalization looks. The five working drafts do not
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
