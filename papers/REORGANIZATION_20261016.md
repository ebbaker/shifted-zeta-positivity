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
