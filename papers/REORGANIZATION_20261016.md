# Grouping the papers folders by research line — 16 October 2026

Prepared for Edward Baker with LLM assistance at his request. Claude Opus 5.5
(configured identifier `claude-opus-5-5`), Claude Cowork, reasoning effort
max. Base commit `5995047`. The machine-readable record is
[REORGANIZATION_20261016.json](REORGANIZATION_20261016.json).

## What moved

Five folders moved under two new group folders. Their names and everything
inside them are unchanged, so every earlier path maps by a prefix change.

| Earlier prefix | Current prefix |
|---|---|
| `papers/shifted-zeta/` | `papers/weil-positivity/shifted-zeta/` |
| `papers/susy-positivity/` | `papers/weil-positivity/susy-positivity/` |
| `papers/prime-variance-exponents/` | `papers/quasi-rh/prime-variance-exponents/` |
| `papers/quasi-rh-exponent-descent/` | `papers/quasi-rh/quasi-rh-exponent-descent/` |
| `papers/quasi-rh-character-amplification/` | `papers/quasi-rh/quasi-rh-character-amplification/` |

`papers/investigations/`, `papers/investigations-2/` and `papers/misc/` did not
move. Earlier relocations are listed in the
[papers index](README.md#older-paths); apply them first, then this map.

All 3,167 files in the five folders, 3,140 tracked and 27 untracked or
ignored, were moved as whole directories and verified byte-identical at
their new paths. The move was staged on its own as 3,140 renames with
identical content, so it can be committed before the repairs below and
`git log --follow` keeps each file's history.

## What was edited, and what was not

Every edit is navigation-only; the JSON record lists each edited file with its
earlier path and its SHA-256 before and after.

- **Relative links:** 730 links in 229 Markdown files were recomputed from the
  file each link pointed to before the move, not by pattern substitution. They
  are in READMEs, notes, brainstorms, research overviews, reviews,
  `result-summaries/`, `avoid/` and chat-history READMEs.
- **Printed paths:** 132 repository paths written as text in current READMEs
  and in `MANIFEST.md`, `LARGE_FILES.md`, the first-slab blueprint and
  checklist, one `avoid/` entry, the weil-depth and storage-depth archive
  guides, the storage-depth closeout and the candidate-bulk-theories
  reproduction guide. Statements about earlier moves, quoted chat requests
  and the earlier-location column of the SUSY path guide keep their paths.
- **TeX:** five relative `\href`/`\path` targets in the prime-variance
  manuscript, which has no committed PDF.
- **Metadata and tooling:** GitHub URLs in both `CITATION.cff` files and two
  `ARCHIVES.md` guides; the CI build matrix; `tools/check_repository_hygiene.py`
  (new groups, new index requirements, the vacated locations);
  `tools/check_citations.py`; `statements/ledger.yaml`; a docstring in
  `tools/record_Claude_cowork_chat.py`; and `.zenodo.json`, whose description
  also gained one sentence naming `papers/quasi-rh/`, `papers/investigations/`
  and `papers/investigations-2/`.
- **Check scripts:** eleven scripts that found files by repository path:
  four in SUSY positivity's critical path, five in Wilson–Loewner arithmetic
  storage, and two in investigations-2 program 01. Only the root depth and the
  path prefixes changed; each numerics README now has a dated note.
- **Manifests:** only the entries of files edited here, and only where the
  recorded hash matched the file before the edit, in the current manifests
  that the checkers verify: weil-depth and storage-depth (`SHA256SUMS.txt`,
  `BUILD_RECORD.json`), arithmetic ground-state geometry (`manifest.json`),
  the `BUILD_RECORD.json` of fractional dimension, Loewner and Wilson lines,
  Wilson–Loewner's `PACKAGE_RECORD.json`, and the candidate-bulk-theories
  package record. Earlier mismatches were left as they were.
- **READMEs:** the [papers index](README.md) was rewritten; READMEs were added
  for [weil-positivity](weil-positivity/README.md) and
  [quasi-rh](quasi-rh/README.md); the root README tables, the investigations
  index, the shifted-zeta guide (which received the cross-citation policy) and
  the SUSY path guide were updated; `CHANGELOG.md` has a new entry.

Not rewritten: dated draft snapshots and non-README files under `archive/`,
relocation and provenance records, numerical and computation records (JSON
and text), registered chat histories, earlier `CHANGELOG.md` entries, printed
paths inside manuscripts with committed PDFs, and the dated 20 September
relocation audit `weil-positivity/susy-positivity/validation/check_reorganization.py`.
Records that hash notes or scripts edited here keep their original hashes;
the JSON record gives the before and after hash of every edited file, so
those records stay checkable against the base commit.

## Validation

Run against the state before the move and again after the edits:

- `tools/check_repository_hygiene.py --working-tree`: before and after, the
  same two pre-existing failures (links to the uncommitted
  `euler_factor_controls.pdf` in investigations-2 program 19).
- `weil-positivity/susy-positivity/validation/check_structure.py`: the same
  32 pre-existing errors before and after.
- Package validators: arithmetic ground-state geometry and topological SUSY
  bulk `check_package.py`, and `validation/drafts.py check` for Wilson lines,
  Loewner, fractional dimension, inverse bulk, source selection and
  Wilson–Loewner, pass before and after. Wilson–Loewner's `check_package.py`
  reports the same 185 pre-existing inventory mismatches before and after.
- A link audit of every Markdown file: no link that resolved before the move
  fails after it.
- Replays of the eleven edited scripts and the dependent checks (fourteen
  outputs written outside the repository; the prime-weight window at two of
  its eight documented horizons) agree before and after in every numerical
  field. Only source hashes, recorded input paths, certificate hashes derived
  from them and runtimes differ.

One check changes by design. `check_first_prime_records.py` in arithmetic
storage binds the saved 24 September records to the current source hashes,
so with its default it now stops at that assertion; it passes on fresh
replays (`--records /tmp`, as its README documents) and on the saved records
at commit `5995047`. The dated 20 September audit `check_reorganization.py`
already failed before the move and now also resolves the repository root
one level too high; run it at its own commit.

These checks establish file identity, path correctness and replay behavior,
not mathematical validity.

## Notes for using the new layout

- Commit the staged move first, then the remaining changes, and push both
  together: the CI build paths are updated in the second commit.
- GitHub URLs that point to the old folder paths stop resolving after the
  push. No release tag or DOI exists yet, so no released citation is affected.
- The `claude-investigation` branch has unmerged commits touching three files
  in `quasi-rh-exponent-descent/`; git's rename detection should carry them to
  the new location on merge.

## Root folders

Later the same day, at the author's request, the research folders at the
repository root were dissolved into the folders they serve. Base commit
`0a1156e` (the commit of the move above); same preparation (Claude Opus 5.5,
configured identifier `claude-opus-5-5`, Claude Cowork, reasoning effort max).
The JSON record's `root_folders` entry lists every file with its hashes.

| Earlier location | Current location |
|---|---|
| `blueprint/README.md`, `statements/README.md` | `papers/weil-positivity/shifted-zeta/first-slab-positivity/blueprint/README.md` (merged) |
| `blueprint/first-slab/statements.md` | `papers/weil-positivity/shifted-zeta/first-slab-positivity/blueprint/statements.md` |
| `statements/ledger.yaml` | `papers/weil-positivity/shifted-zeta/first-slab-positivity/blueprint/ledger.yaml` |
| `verification/README.md`, `verification/first-slab/<path>` | `papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/README.md`, `papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/<path>` |
| `environment/requirements.txt` | `papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/requirements.txt` |
| `environment/requirements_metadata.txt` | `tools/requirements_metadata.txt` |
| `code/README.md`, `code/certificates/first-slab/README.md` | `papers/weil-positivity/shifted-zeta/first-slab-positivity/CERTIFICATE_CODE.md` (merged; the per-paper code table repeated the papers' READMEs, and the list of unrecovered scripts is in `MANIFEST.md`) |
| `notes/README.md` | `early-chat-logs/initial-project-files/rh3/RESEARCH_LOG_INDEX.md` |
| `notes/REDACTION_CHECKLIST.md` | `early-chat-logs/initial-project-files/rh3/REDACTION_CHECKLIST.md` |
| `notes/LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md` | `papers/weil-positivity/shifted-zeta/storage-depth/` (same name) |
| `notes/supersymmetric_positivity_research_brief.md`, `.docx` | `papers/weil-positivity/susy-positivity/archive/` (same names) |
| `notes/repository-review/9:9:26/` (review and response) | `papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/repository-review-20260909/` (same names) |
| `Claude outputs/REVIEW_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md` | removed: an earlier copy, without the §7 errata, of `papers/weil-positivity/susy-positivity/investigations/wilson-loewner/YM/reviews/` (same name) |
| `Claude outputs/STRUCTURAL_REQUIREMENTS_AND_NEXT_STEPS_20260925.md` | removed: the first version (conditions R1–R4) of the revised note (N1–N4) in `…/wilson-loewner/YM/notes/` (same name) |
| `chat-histories/0001_2026-10-13T12-45-01Z_rename-draft-histor-md-files.json` | `early-chat-logs/chatgpt-codex/` (same number and name; [receipt](../early-chat-logs/chatgpt-codex/CHAT_HISTORY_RELOCATION_20261016.json)) |
| `output/pdf/quaternion_theta_geometry.pdf`, `theta_manifold_geometry.pdf` | untracked and ignored; the local copies remain |

Of the 23 moved files, 13 are byte-identical at their new paths and 10 were
then edited for paths and links: the blueprint README, statements and ledger,
the verification README, protocol, rerun record and the READMEs of `reviews/`
and `scripts/`, and the research-log index and checklist. The three merged
files were removed after their content was carried into the merged file or
found in the papers' READMEs and `MANIFEST.md`; the two removed `Claude outputs/`
files are earlier versions of the YM files. All of them are in the base commit.

**Links and paths.** Seventy-one relative links in 21 Markdown files were
recomputed from their earlier targets, as above. The other references were
edited by hand: the first-slab CI workflow and the formalization issue
template; the root, papers, shifted-zeta, first-slab and storage-depth READMEs;
`MANIFEST.md`, `CONTRIBUTING.md`, `RELEASING.md` and `.zenodo.json`; the status
files of psi-omega-margin, omega-string, defect-depth and the rh-detector;
`references/README.md`, five `avoid/` entries, two `result-summaries/`, the
chat-history guide, and the READMEs of the two `early-chat-logs/` destinations
and of the SUSY archive. In storage-depth, only the manifest entries of the two
files edited there (`CLOSEOUT.md`, `README.md`) were refreshed, followed by the
`SHA256SUMS.txt` entry of `BUILD_RECORD.json`.

**Research log.** The index and checklist now sit beside the documents they
describe, with a link to each. Both state that the copies in `rh3/claude/` are
the unchanged 13 October exports, to which the checklist has not been applied;
`RELEASING.md` and `.zenodo.json` now say so too, replacing statements that the
reports would be committed only after redaction.

**Chat history.** The root registry's only chat moved by the procedure in
`tools/CHAT_HISTORY.md`, with both registries locked and the destination
verified before the source registration and archive were removed. It keeps
number 1, which the destination's first chat also holds (the registry allows
duplicate numbers, not duplicate ids or filenames). The emptied root index was
then removed with its folder.

**Reading copies.** `git rm --cached` removed `output/pdf/` from the index,
leaving the files on disk, and `.gitignore` gained `/output/` (anchored, so
the `numerics/output/` folders stay tracked). This index removal is the only
staged change. The four READMEs of investigations 21 and 22 that linked the
PDFs now point to the `.tex` sources. Thirteen links in dated notes and
reviews of those investigations still name `output/pdf/`; they resolve in a
local checkout but not on GitHub. The investigation 22 manuscript still calls
`output/pdf` its repository reading copy, and the two build records keep the
PDF paths and hashes.

Not rewritten, as above: dated notes and reviews other than the paper status
files, relocation and provenance records (including the `manifest.json` of the
initial project files, whose `repository_counterpart` fields give the root
paths of 13 October, and the 20 September SUSY record's link to the brief),
numerical records, registered chat histories and earlier `CHANGELOG.md`
entries. Dated records that hash the edited status files or `CONTRIBUTING.md`
keep their original hashes; the JSON record gives both.

### Validation of the root step

Run on the base commit's state and after the edits:

- `tools/check_repository_hygiene.py --working-tree`: the same two
  pre-existing failures (investigation 19's uncommitted PDF).
- `weil-positivity/susy-positivity/validation/check_structure.py`: the same 32
  errors; three more links checked (the SUSY archive README).
- Package validators: the same results as after the move above (all pass;
  Wilson–Loewner's `check_package.py` lists the same 185 mismatches).
- Link audit of every Markdown file against the base commit, with moved files
  mapped back: 11,701 relative links in 1,757 files; the 188 that do not
  resolve all failed at the base commit too, so none is newly broken. The
  thirteen `output/pdf/` links above resolve only to the ignored local files.
- `blueprint/ledger.yaml` parses and its `blueprint`, `checklist`, `pdf` and
  `status_file` paths exist; the CI workflow's script, requirements and
  metadata paths exist. The moved scripts read no repository paths and were
  not rerun.
- The chat relocation was rechecked after the root folder was removed: one
  registration, unchanged archive bytes, unchanged neighbouring archives.
