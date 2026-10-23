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
Sonin trace comparisons, and since October variance exponents, quasi-RH
descent, Newman heat flow and theta geometry. Each investigation records its own assumptions, results, limitations, and
relation to the common arithmetic target.

Edward Baker — August–October 2026. **Overview updated 3 October 2026; layout and tables updated 16 October 2026.**

> **Status and disclosure.** No proof of RH, all-support Weil positivity, or
> new zero-free region is claimed. The first-slab manuscript is a release-stage
> preprint (v1.0); the other manuscripts and investigations remain working
> research. No repository release tag or DOI exists yet. The work uses
> substantial language-model assistance under the author's direction. Internal
> reviews, independent numerical recomputations, interval certificates, and
> exploratory calculations have different evidential roles; the linked records
> state their scope. Specialist mathematical review remains outstanding. The
> primary first-slab Arb certificate bundle is still outside the public tree
> pending its [release gate](papers/weil-positivity/shifted-zeta/first-slab-positivity/CERTIFICATE_CODE.md).

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
produced in that collaboration, under the author's direction, in referee-style
rounds recorded beside each paper (for the first slab, in its
[`verification/`](papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/README.md) folder and the
[research log](early-chat-logs/initial-project-files/rh3/RESEARCH_LOG_INDEX.md)). The author is responsible for the content; the
per-statement record of what has and has not been independently checked is in
the first slab's [`blueprint/`](papers/weil-positivity/shifted-zeta/first-slab-positivity/blueprint/README.md) and `verification/`
folders and in the other papers' status files.

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
[shared background](papers/weil-positivity/susy-positivity/background.pdf),
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
| **Shifted-zeta criteria and inverse spectra:** [psi-omega-margin](papers/weil-positivity/shifted-zeta/psi-omega-margin/README.md), [omega-string](papers/weil-positivity/shifted-zeta/omega-string/README.md), [defect-depth](papers/weil-positivity/shifted-zeta/defect-depth/README.md) | Quantitative time-domain criteria, the shifted string/canonical-system family, and controlled models of how an off-line zero would become detectable. | Criteria and conditional endpoint descriptions do not establish the required positive family. Uniform detection of every possible defect remains open. |
| **Finite-window positivity and continuation:** [first-slab](papers/weil-positivity/shifted-zeta/first-slab-positivity/README.md), [Weil-depth](papers/weil-positivity/shifted-zeta/weil-depth/README.md), [storage-depth](papers/weil-positivity/shifted-zeta/storage-depth/README.md), [critical path](papers/weil-positivity/susy-positivity/investigations/critical-path/README.md) | Analytic first-slab bounds, all-input finite-window certificates, tail control, residual estimates, and cumulative append methods. Weil-depth reaches `log 7`; storage-depth extends beyond it. | Finite certificates are a methodological base. Neither successive joins nor small-shift estimates yet supply an unbounded continuation with controlled losses. |
| **Positive factors and supersymmetric geometry:** [positive factorizations](papers/weil-positivity/susy-positivity/investigations/previous/positive-factorizations/README.md), [topological SUSY bulk](papers/weil-positivity/susy-positivity/investigations/previous/topological-susy-bulk/README.md), [arithmetic ground-state geometry](papers/weil-positivity/susy-positivity/investigations/previous/arithmetic-ground-state-geometry/README.md) | Short-window and restricted-sector factors, positive gamma kinetic constructions, interacting source models, boundary corrections, and obstructions to specified scalar or pairwise completions. | A joint arithmetic factor or source law valid at arbitrary length has not been obtained. Auxiliary positivity leaves signed remainders or finite-response conditions to control. |
| **Bulk sources and response reductions:** [inverse bulk realization](papers/weil-positivity/susy-positivity/investigations/previous/inverse-bulk-realization/README.md), [source selection rules](papers/weil-positivity/susy-positivity/investigations/previous/source-selection-rules/README.md), [finite-response note](papers/weil-positivity/susy-positivity/manuscripts/finite-response-weil-positivity/README.md) | Tests of exact source matching, jump-form descriptions, boundary corrections, Schur reductions, and response enclosures. | Matching individual terms does not construct a common positive source. The finite-response sign problem remains open; publication of that technical note is deferred. |
| **Transfer structure and deformation:** [Wilson lines](papers/weil-positivity/susy-positivity/investigations/wilson-lines/README.md), [Loewner](papers/weil-positivity/susy-positivity/investigations/loewner/README.md), [fractional dimension](papers/weil-positivity/susy-positivity/investigations/fractional-dimension/README.md) | Phase/transfer identities, a positive-measure and exponential-memory decomposition, free boundary models, and a geometric interpretation of the shift parameter. | The original Loewner proposal is closed within its tested scope. Fractional continuation does not supply a positive underlying space, and boundary phase identities alone do not prove transfer contraction. |
| **Physical evolution and arithmetic realization:** [Wilson–Loewner](papers/weil-positivity/susy-positivity/investigations/wilson-loewner/README.md), [YM](papers/weil-positivity/susy-positivity/investigations/wilson-loewner/YM/README.md), [N=4 SYM](papers/weil-positivity/susy-positivity/investigations/wilson-loewner/N4SYM/README.md), [WZW / thermal arithmetic](papers/weil-positivity/susy-positivity/investigations/wilson-loewner/WZW/README.md) | Wilson-loop evolution and reflection constructions, displacement and memory responses, thermal arithmetic coefficient identities, signed Weil pairings, and source-domain obstructions. | No physical channel or source norm realizing the complete arithmetic target has yet been obtained. The tested response, interface, and source constructions have specific limitations; general physical realization remains open. |
| **Spectral and geometric realizations:** [CCM operators](papers/investigations/ccm-operator-realizations/README.md), [CCM fractal Laplacians](papers/investigations/ccm-fractal-laplacians/README.md) | Connes–Consani–Moscovici operator realizations by finite mechanics, strings and graph Dirac systems; ground-state and threshold comparisons; resistance-form tests and geometric obstructions. | Arithmetic ground-state control and identification of a limiting spectrum with Xi remain unresolved. CCM is temporarily paused after the endpoint-energy obstruction; the tested direct fractal-coordinate realization also fails within its stated scope. |
| **Arithmetic storage and Sonin traces:** [arithmetic-storage summary](papers/weil-positivity/susy-positivity/investigations/wilson-loewner/arithmetic-storage/PROJECT_SUMMARY.md), [critical-boundary manuscript](papers/investigations/sonin-critical-boundary/README.md) | First-prime join analysis, exact signed place-addition laws, actual-projection trace tools, and critical-boundary estimates and limits for the zeta-phase family. | The arithmetic residual sign and identification of a positive limit with the complete Weil form remain open. Critical-line mass in a majorant or Abel limit does not settle exact projection mass survival or the contribution of off-line zeros. |
| **Variance exponents and quasi-RH descent:** [prime-variance exponents](papers/quasi-rh/prime-variance-exponents/README.md), [exponent descent](papers/quasi-rh/quasi-rh-exponent-descent/README.md), [character amplification](papers/quasi-rh/quasi-rh-character-amplification/README.md) | The equivalence of a fixed variance exponent for one prepared prime response with a closed zero strip, finite variance certificates, short- and mixed-family reductions, and a conditional amplification boundary. | The first fixed global exponent below one remains open. The amplification boundary rests on imported inputs and has since been superseded; no descent step to RH is established. |
| **Newman heat flow and theta geometry:** [Newman-collision projects](papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/README.md), [second portfolio](papers/investigations-2/README.md), [Euler-factor controls](papers/investigations-2/active/19_euler_factor_controls/README.md), [quaternion theta geometry](papers/investigations-2/active/21_quaternion_theta_geometry/README.md), [theta manifold geometry](papers/investigations-2/active/22_theta_manifold_geometry/README.md) | Heat-flow reductions and finite Newman certificates, audits of the quasi-RH sources and of a Newman certificate, Euler-factor control witnesses, and signed forms and connections on the theta jet geometry near possible collisions. | Exclusion of every positive-time collision and a theta-specific sign or turning estimate remain open; the Euler-factor witnesses are controls for screening proposed mechanisms. |
| **Earlier zero diagnostics:** [RH detector](papers/misc/rh-detector/README.md) | Velocity-residual tests, synthetic defect experiments, and a De Bruijn–Newman interpretation of a matrix pencil. | Interval certification remains incomplete. The finite diagnostics do not provide a uniform theorem excluding all off-line zeros. |

The program has therefore produced several kinds of output: finite positivity
results, exact structural identities, conditional routes, and obstructions that
narrow particular proposals. Their common unresolved issue is control of the
**joint arithmetic contribution as support grows**. More numerical precision
or a new realization of an already positive finite object does not by itself
resolve that issue.

Since mid-October the RH-directed work has concentrated in the
[second investigation portfolio](papers/investigations-2/README.md), on
constrained operator squares and the theta geometry near possible Newman
collisions (investigations
[20](papers/investigations-2/active/20_constrained_operator_squares/README.md),
[21](papers/investigations-2/active/21_quaternion_theta_geometry/README.md)
and [22](papers/investigations-2/active/22_theta_manifold_geometry/README.md)),
with the [Euler-factor controls](papers/investigations-2/active/19_euler_factor_controls/README.md)
as the shared screen for proposed mechanisms. On 3 October, when this overview
was last revised, the concentration was on independently positive Sonin forms
and a direct arithmetic comparison, including finite-place transport and
finite Euler products, and the 1 October critical-boundary manuscript
revision was awaiting another review round; spectral one-sided comparisons and a genuine cumulative
continuation law remained alternative targets, and physical and geometric
branches would need a specific new mechanism beyond their recorded
obstructions. The [quasi-RH line](papers/quasi-rh/README.md) grew from the
Sonin subpower milestones. These priorities are research
judgments, not theorems excluding the alternatives. See the
[program-wide assessment](papers/investigations/program-meta-analysis/README.md)
of 26 September, the [portfolio overview](papers/investigations-2/README.md)
and the linked investigation records for the detailed reasoning and history.

## Reading guide and repository layout

Start with the [shifted-zeta guide](papers/weil-positivity/shifted-zeta/README.md) for the original
six-paper framework, or the
[SUSY-positivity background](papers/weil-positivity/susy-positivity/background.pdf) and
[program guide](papers/weil-positivity/susy-positivity/README.md) for the broader search for a
structural explanation. The
[program meta-analysis](papers/investigations/program-meta-analysis/README.md)
compares approaches across the repository. For the October work, start with
the [quasi-RH line](papers/quasi-rh/README.md) and the
[second investigation portfolio](papers/investigations-2/README.md). The
[papers index](papers/README.md) maps every research folder, how the lines
developed, and earlier paths. Use the individual investigation
links above for current work: older indexes and manuscript summaries can
precede later dated notes and review corrections.

| Directory | What it holds |
|---|---|
| [`papers/`](papers/README.md) | Index of the research folders, how the lines of work developed, citation forms, the release checklist, and earlier paths. |
| [`papers/weil-positivity/`](papers/weil-positivity/README.md) | The positivity line: the six shifted-zeta manuscripts ([`shifted-zeta/`](papers/weil-positivity/shifted-zeta/README.md)) and the SUSY-positivity program ([`susy-positivity/`](papers/weil-positivity/susy-positivity/README.md)) with its shared background, investigations, earlier packages and finite-response note. |
| [`papers/investigations/`](papers/investigations/README.md) | Cross-program assessments, CCM operator and fractal investigations, character channels, and the Sonin critical-boundary manuscript. |
| [`papers/quasi-rh/`](papers/quasi-rh/README.md) | The zero-strip line: prime-variance exponents, quasi-RH exponent descent with the Newman-collision projects, and character amplification. |
| [`papers/investigations-2/`](papers/investigations-2/README.md) | The second investigation portfolio: active and inactive program homes, audits, shared planning and chat histories. |
| [`papers/misc/`](papers/misc/README.md) | Separate work, currently the earlier RH-detector draft. |
| [`result-summaries/`](result-summaries/README.md) | Short summaries of the established results, in the sources' own status words, routing to the manuscripts, certificates and reviews that hold them. |
| [`avoid/`](avoid/README.md) | Recurring patterns to avoid in this project, each with anecdotal evidence and references to the repository. |
| [`references/`](references/README.md) | External-source bibliography; third-party PDFs are not redistributed. |
| `early-chat-logs/` | Chat records without an investigation home — the early and repository-wide [Codex chats](early-chat-logs/chatgpt-codex/README.md) and [Claude chats](early-chat-logs/claude-cowork/README.md), which also hold the Claude repository-maintenance sessions — and the [claude.ai project files](early-chat-logs/initial-project-files/README.md) of the first three projects, with the RH3 [research-log index](early-chat-logs/initial-project-files/rh3/RESEARCH_LOG_INDEX.md) and its redaction checklist. |
| [`tools/`](tools/CHAT_HISTORY.md) | Chat recorders and the chat-history guide, the repository hygiene and citation checkers, and the CI's pinned metadata requirements. |

The first-slab preprint keeps its statement blueprint, verification records and
certificate release gate in [its own folder](papers/weil-positivity/shifted-zeta/first-slab-positivity/README.md); these were
repository-root folders until 16 October 2026 (see the
[relocation record](papers/REORGANIZATION_20261016.md)). Reproduction code
lives beside each paper or investigation. Keep generated working-draft PDFs
out of the individual research and manuscript folders. Build local reading
copies into the root `output/pdf/<paper-or-investigation>/` directory, which
is not tracked, and rebuild them from the `.tex` sources; see the standing
[PDF storage rule](LARGE_FILES.md#1-the-convention).

Within each investigation, incremental research belongs in `notes/`, numerical
work in `numerics/`, and reviews in `reviews/`, with model and reasoning-effort
metadata in notes and reviews. Existing snapshots are historical records;
future manuscript milestones should point to Git commits or tags in the local
`DRAFT_HISTORY.md`, without new snapshot folders.

## Research chat histories

Save each research conversation in its investigation's `chat-histories/`;
use the shared portfolio archive for conversations spanning the program.
The [chat-history guide](tools/CHAT_HISTORY.md) covers registration,
automatic refresh, final-reply capture, integrity checks and
[moves between investigations](tools/CHAT_HISTORY.md#move-an-existing-chat-to-another-investigation).

When the user requests a move, preserve the original conversation identity,
number, filename, creation time, first-capture provenance and public text:

1. Refresh the existing archive, lock both registries, recover pending
   transactions, and validate the source and destination.
2. Back up both registry states and the archive, then transfer its exact
   bytes and complete entry. Verify the destination before removing the
   source registration and file; preserve numbering reservations.
3. Check that only the new registration remains, record the relocation,
   update links, and resume refresh and bounded final capture there.

The refresh tool's `--history-dir` flag does not relocate an existing
registration. Follow the detailed guide for destination initialization,
ordered locks, transaction helpers, rollback and interrupted transfers;
do not hand-edit registered histories or create a second canonical copy.

## Large files

Git holds sources and small records only. Derived data that committed code
regenerates deterministically — at present the ball-matrix archives of
`papers/weil-positivity/shifted-zeta/weil-depth/` (about 13 MB per horizon, 122 MB in all) and of
`papers/weil-positivity/shifted-zeta/storage-depth/` (six recorded archives, about 1.6 GB in all; four
present locally, two regenerable) — are kept
outside the repository in `szp-archive/` (locally `/Users/Shared/szp-archive`),
bound to the tree by the hashes recorded in the small certificate files, and described by a tracked guide in
the paper folder (`papers/weil-positivity/shifted-zeta/weil-depth/ARCHIVES.md`, `papers/weil-positivity/shifted-zeta/storage-depth/ARCHIVES.md`). The convention (a 1 MB
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
in `papers/weil-positivity/shifted-zeta/first-slab-positivity/CITATION.cff`).

**What a release contains.** A tag archives everything present in the tree
at that moment — including the working-draft folders, and nothing kept
outside the tree (`LARGE_FILES.md` explains why that is complete for
regenerable data). A draft is therefore
archived *as a draft*: its status and review records identify it as work in
progress, the release notes list which folders are released, and only those
folders are to be cited. Tagging is done only when everything committed is fit
to be archived permanently in that sense: released paper sources and PDFs with
their `blueprint/` and `verification/` records, code that has passed its
release gate, drafts whose status records are current, and research notes that
have been through the redaction checklist. `v1.0` releases the first-slab preprint
and the material around it.

**Citing a paper in this repository.** Until a release exists, cite the
folder at a specific commit (take the hash from `git rev-parse HEAD` or the
GitHub permalink of the folder):

> E. Baker, *Archimedean first-slab positivity for shifted zeta canonical
> systems: an off-center Weil generator and a radial energy identity*,
> preprint v1.0, 2026, in: *shifted-zeta-positivity*,
> <https://github.com/ebbaker/shifted-zeta-positivity>, folder
> `papers/weil-positivity/shifted-zeta/first-slab-positivity/`, commit ⟨hash⟩.

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

Start at the first slab's [`blueprint/statements.md`](papers/weil-positivity/shifted-zeta/first-slab-positivity/blueprint/statements.md):
it lists every statement of the preprint with what depends on what, whether it is proved on paper, certified
by computer, or only asserted, whether a human has checked it, and how
feasible a Lean/Mathlib formalization looks. The later investigations do not
yet have comparable statement blueprints. Use their dated status files,
research notes, and `reviews/` records to identify the exact claims and
remaining checks; a manuscript may lag its subsequent notes. The two premise
checks the internal review cannot perform — the normalization chain against Suzuki's paper and
the originality search — have a written protocol in the same folder,
[`verification/PROTOCOL_C1_C2.md`](papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/PROTOCOL_C1_C2.md). Issues labelled
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
