# shifted-zeta-positivity

A research program on the arithmetic, spectral, and physical structures behind
positivity criteria for the Riemann hypothesis. The repository brings together
manuscripts, analytic investigations, computer-assisted finite-window
certificates, numerical experiments, and critical reviews. Its central question
is whether the complete Weil quadratic form can be obtained from an
independently positive construction or controlled comparison, valid for every
admissible input and arbitrarily large support.

The starting framework is Suzuki's shifted screw functions $\Psi_\omega$ and
the shifted scattering function
$\Theta_\omega(z)=\xi(\tfrac12-\omega-iz)/\xi(\tfrac12+\omega-iz)$.
The program now also includes supersymmetric and gauge-theoretic source models,
Wilson-line and Loewner evolution, spectral and geometric realizations, and
Sonin trace comparisons. Each investigation records its own assumptions, results, limitations, and
relation to the common arithmetic target.

Edward Baker — August–October 2026. **Overview updated 3 October 2026.**

> **Status and disclosure.** No proof of RH, all-support Weil positivity, or
> new zero-free region is claimed. The first-slab manuscript is a release-stage
> preprint (v1.0); the other manuscripts and investigations remain working
> research. No repository release tag or DOI exists yet. The work uses
> substantial language-model assistance under the author's direction. Internal
> reviews, independent numerical recomputations, interval certificates, and
> exploratory calculations have different evidential roles; the linked records
> state their scope. Specialist mathematical review remains outstanding. The
> primary first-slab Arb certificate bundle is still outside the public tree
> pending its [release gate](code/README.md).

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
screw functions [arXiv:1204.1827, 2206.03682]. Suzuki’s framework opened a new direction: investigating shifted-zeta positivity through inverse spectral theory and possible bulk–boundary realizations. This repository begins with that work and follows the broader mathematical and physical investigations that developed from it.

The manuscripts, research notes, verification records and code here were
produced in that collaboration, under the author's direction, in the
referee-style rounds described in `verification/` and `notes/`. The author is
responsible for the content; the per-statement record of what has and has not
been independently checked is in `blueprint/` and `verification/`.

## Project overview and goals

The original shifted-zeta papers establish the program's mathematical
framework: quantitative positivity and zero-free criteria, an inverse-spectral
family of strings and canonical systems, and ways to detect hypothetical
spectral defects. The finite-depth papers then develop analytic and
computer-assisted methods for proving positivity on specified windows. Later
investigations ask what structure could explain that positivity and extend it
beyond individually certified windows.

The common RH-directed target is the **complete central Weil form**: with the
normalizations and domains in the
[shared background](papers/susy-positivity/background.pdf),
$Q_{0,L}[f]\geq0$ for every support length $L>0$ and every smooth compactly
supported complex input $f$ in that interval. The gamma, pole, and prime terms
must be retained together. A positive auxiliary system, a match to one factor,
or a finite matrix calculation supplies this target only when the required
arithmetic identity and omitted-input bounds are also established. The shift,
support length, and numerical resolution are separate parameters.

The broader goals are to:

- **Find an arithmetic positivity mechanism.** Seek a factorization, physical
  source norm, spectral comparison, or positive trace construction that
  explains the complete form without assuming its sign.
- **Connect finite results to arbitrary support.** Develop a justified
  continuation law or a family of positive forms whose limit or one-sided
  comparison gives the arithmetic target on every fixed compact source.
  A uniform positive gap at all lengths is not required.
- **Develop useful mathematics along the way.** Preserve explicit kernels,
  operator identities, quantitative bounds, physical response calculations,
  and precisely scoped obstructions, whether or not they yield an RH route.
- **Make results independently assessable.** Keep derivations and numerical
  evidence reproducible, resolve normalization and domain questions, and
  obtain specialist proof and literature review before treating working
  results as publication-ready contributions.

## Investigations and how they fit

The table summarizes the whole program. “Results” refers to the arguments and
checks recorded in the repository, within their stated hypotheses; it does
not imply completed external review. Older and paused investigations remain
part of the research record.

| Investigation | Contribution to the program | Current limit or open goal |
|---|---|---|
| **Shifted-zeta criteria and inverse spectra:** [psi-omega-margin](papers/shifted-zeta/psi-omega-margin/README.md), [omega-string](papers/shifted-zeta/omega-string/README.md), [defect-depth](papers/shifted-zeta/defect-depth/README.md) | Quantitative time-domain criteria, the shifted string/canonical-system family, and controlled models of how an off-line zero would become detectable. | Criteria and conditional endpoint descriptions do not establish the required positive family. Uniform detection of every possible defect remains open. |
| **Finite-window positivity and continuation:** [first-slab](papers/shifted-zeta/first-slab-positivity/README.md), [Weil-depth](papers/shifted-zeta/weil-depth/README.md), [storage-depth](papers/shifted-zeta/storage-depth/README.md), [critical path](papers/susy-positivity/investigations/critical-path/README.md) | Analytic first-slab bounds, all-input finite-window certificates, tail control, residual estimates, and cumulative append methods. Weil-depth reaches `log 7`; storage-depth extends beyond it. | Finite certificates are a methodological base. Neither successive joins nor small-shift estimates yet supply an unbounded continuation with controlled losses. |
| **Positive factors and supersymmetric geometry:** [positive factorizations](papers/susy-positivity/investigations/previous/positive-factorizations/README.md), [topological SUSY bulk](papers/susy-positivity/investigations/previous/topological-susy-bulk/README.md), [arithmetic ground-state geometry](papers/susy-positivity/investigations/previous/arithmetic-ground-state-geometry/README.md) | Short-window and restricted-sector factors, positive gamma kinetic constructions, interacting source models, boundary corrections, and obstructions to specified scalar or pairwise completions. | A joint arithmetic factor or source law valid at arbitrary length has not been obtained. Auxiliary positivity leaves signed remainders or finite-response conditions to control. |
| **Bulk sources and response reductions:** [inverse bulk realization](papers/susy-positivity/investigations/previous/inverse-bulk-realization/README.md), [source selection rules](papers/susy-positivity/investigations/previous/source-selection-rules/README.md), [finite-response note](papers/susy-positivity/manuscripts/finite-response-weil-positivity/README.md) | Tests of exact source matching, jump-form descriptions, boundary corrections, Schur reductions, and response enclosures. | Matching individual terms does not construct a common positive source. The finite-response sign problem remains open; publication of that technical note is deferred. |
| **Transfer structure and deformation:** [Wilson lines](papers/susy-positivity/investigations/wilson-lines/README.md), [Loewner](papers/susy-positivity/investigations/loewner/README.md), [fractional dimension](papers/susy-positivity/investigations/fractional-dimension/README.md) | Phase/transfer identities, a positive-measure and exponential-memory decomposition, free boundary models, and a geometric interpretation of the shift parameter. | The original Loewner proposal is closed within its tested scope. Fractional continuation does not supply a positive underlying space, and boundary phase identities alone do not prove transfer contraction. |
| **Physical evolution and arithmetic realization:** [Wilson–Loewner](papers/susy-positivity/investigations/wilson-loewner/README.md), [YM](papers/susy-positivity/investigations/wilson-loewner/YM/README.md), [N=4 SYM](papers/susy-positivity/investigations/wilson-loewner/N4SYM/README.md), [WZW / thermal arithmetic](papers/susy-positivity/investigations/wilson-loewner/WZW/README.md) | Wilson-loop evolution and reflection constructions, displacement and memory responses, thermal arithmetic coefficient identities, signed Weil pairings, and source-domain obstructions. | No physical channel or source norm realizing the complete arithmetic target has yet been obtained. The tested response, interface, and source constructions have specific limitations; general physical realization remains open. |
| **Spectral and geometric realizations:** [CCM operators](papers/investigations/ccm-operator-realizations/README.md), [CCM fractal Laplacians](papers/investigations/ccm-fractal-laplacians/README.md) | Connes–Consani–Moscovici operator realizations by finite mechanics, strings and graph Dirac systems; ground-state and threshold comparisons; resistance-form tests and geometric obstructions. | Arithmetic ground-state control and identification of a limiting spectrum with Xi remain unresolved. CCM is temporarily paused after the endpoint-energy obstruction; the tested direct fractal-coordinate realization also fails within its stated scope. |
| **Arithmetic storage and Sonin traces:** [arithmetic-storage summary](papers/susy-positivity/investigations/wilson-loewner/arithmetic-storage/PROJECT_SUMMARY.md), [critical-boundary manuscript](papers/investigations/sonin-critical-boundary/README.md) | First-prime join analysis, exact signed place-addition laws, actual-projection trace tools, and critical-boundary estimates and limits for the zeta-phase family. | The arithmetic residual sign and identification of a positive limit with the complete Weil form remain open. Critical-line mass in a majorant or Abel limit does not settle exact projection mass survival or the contribution of off-line zeros. |
| **Earlier zero diagnostics:** [RH detector](papers/misc/rh-detector/README.md) | Velocity-residual tests, synthetic defect experiments, and a De Bruijn–Newman interpretation of a matrix pencil. | Interval certification remains incomplete. The finite diagnostics do not provide a uniform theorem excluding all off-line zeros. |

The program has therefore produced several kinds of output: finite positivity
results, exact structural identities, conditional routes, and obstructions that
narrow particular proposals. Their common unresolved issue is control of the
**joint arithmetic contribution as support grows**. More numerical precision
or a new realization of an already positive finite object does not by itself
resolve that issue.

The current concentration of RH-directed work is on independently positive
Sonin forms and a direct arithmetic comparison, including finite-place
transport and finite Euler products. The 1 October critical-boundary manuscript
revision is awaiting another review round before author review. Spectral
one-sided comparisons and a genuine cumulative continuation law remain
alternative targets; physical and geometric branches would need a specific
new mechanism beyond their recorded obstructions. This prioritization is a
research judgment, not a theorem excluding those alternatives. See the
[program-wide assessment](papers/investigations/program-meta-analysis/README.md)
and the linked investigation records for the detailed reasoning and history.

## Reading guide and repository layout

Start with the [shifted-zeta guide](papers/shifted-zeta/README.md) for the original
six-paper framework, or the
[SUSY-positivity background](papers/susy-positivity/background.pdf) and
[program guide](papers/susy-positivity/README.md) for the broader search for a
structural explanation. The
[program meta-analysis](papers/investigations/program-meta-analysis/README.md)
compares approaches across the repository. Use the individual investigation
links above for current work: older indexes and manuscript summaries can
precede later dated notes and review corrections.

| Directory | What it holds |
|---|---|
| [`papers/shifted-zeta/`](papers/shifted-zeta/README.md) | The six original manuscripts, status records, and reproduction materials. |
| [`papers/susy-positivity/`](papers/susy-positivity/README.md) | Shared background, factorization and physical investigations, Wilson–Loewner subprograms, earlier packages, and the finite-response note. |
| [`papers/investigations/`](papers/investigations/) | Cross-program assessments, CCM operator and fractal investigations, and the Sonin critical-boundary manuscript. |
| [`papers/misc/`](papers/misc/README.md) | Separate work, currently the earlier RH-detector draft. |
| [`blueprint/`](blueprint/README.md) and [`statements/`](statements/README.md) | First-slab statement inventory, dependencies, proof and human-verification status, and machine-readable ledger. |
| [`verification/`](verification/README.md) | Referee-round records, independent recomputation scripts, and outstanding verification checklists. |
| [`notes/`](notes/README.md) | Shared lessons and historical research-log migration; investigation-specific research stays with its investigation. |
| [`code/`](code/README.md) and `environment/` | First-slab certificate release gate and shared verification environment. Most reproduction code lives beside its investigation. |
| [`references/`](references/README.md) | External-source bibliography; third-party PDFs are not redistributed. |

Within each investigation, incremental research belongs in `notes/`, numerical
work in `numerics/`, and reviews in `reviews/`, with model and reasoning-effort
metadata in notes and reviews. Existing snapshots are historical records;
future manuscript milestones should point to Git commits or tags in the local
`DRAFT_HISTOR.md` (or existing `DRAFT_HISTORY.md`), without new snapshot folders.

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
archived *as a draft*: its status and review records identify it as work in
progress, the release notes list which folders are released, and only those
folders are to be cited. Tagging is done only when everything committed is fit
to be archived permanently in that sense: released paper sources and PDFs, the
`blueprint/`, `statements/` and `verification/` records, code that has passed
its release gate, drafts whose status records are current, and notes that have
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
feasible a Lean/Mathlib formalization looks. The later investigations do not
yet have comparable statement blueprints. Use their dated status files,
research notes, and `reviews/` records to identify the exact claims and
remaining checks; a manuscript may lag its subsequent notes. The two premise
checks the internal review cannot perform — the normalization chain against Suzuki's paper and
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
