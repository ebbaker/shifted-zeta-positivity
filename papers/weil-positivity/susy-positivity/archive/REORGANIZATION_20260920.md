# Investigation focus reorganization — 20 September 2026 (UTC)

Five complete investigation packages moved into `investigations/previous/`.
The name means **outside the current research focus**, not disproved,
completed, or scientifically obsolete. All scientific scope and status remain
unchanged, including the original Loewner proposal's qualified closure.
The [program README](../README.md) is the current index; the
[previous-investigations guide](../investigations/previous/README.md) explains
the grouping.

## Delivered layout

```text
investigations/
  critical-path/                 # brief placeholder only
  wilson-loewner/
  wilson-lines/
  loewner/
  fractional-dimension/
  previous/
    README.md
    arithmetic-ground-state-geometry/
    inverse-bulk-realization/
    positive-factorizations/
    source-selection-rules/
    topological-susy-bulk/
```

Exactly these five packages moved. The five retained investigations remain at
the top level. `critical-path/` was empty and received only a short README
linking to the existing Wilson–Loewner
[shift-flow, cumulative-storage and critical-path note](../investigations/wilson-loewner/notes/SHIFT_FLOW_CUMULATIVE_STORAGE_AND_CRITICAL_PATH_20260919.md).
No critical-path research was undertaken.

## Relocation map for historical references

All paths in this table are relative to `papers/susy-positivity/`. Preserve
any suffix after the investigation name when applying the map.

| Earlier prefix | Current prefix |
|---|---|
| `investigations/arithmetic-ground-state-geometry/` | `investigations/previous/arithmetic-ground-state-geometry/` |
| `investigations/inverse-bulk-realization/` | `investigations/previous/inverse-bulk-realization/` |
| `investigations/positive-factorizations/` | `investigations/previous/positive-factorizations/` |
| `investigations/source-selection-rules/` | `investigations/previous/source-selection-rules/` |
| `investigations/topological-susy-bulk/` | `investigations/previous/topological-susy-bulk/` |

[MOVES.json](../validation/reorganization-20260920/MOVES.json) supplies the
repository-relative file map with before/after sizes and SHA-256 fingerprints.
For even older `attempts/positive-factorizations/` references, first apply the
[earlier path guide](README.md), then this map. Interpret relative references
inside a dated snapshot from its original layout before applying the map.
Commit-pinned citations retain the paths at that commit, including the
finite-response manuscript's `efb908a` citation. They must not be rewritten
as links into a revision that never had `previous/`.

## Preservation

Repository instructions and `LARGE_FILES.md` were read before edits. No
`AGENTS.md` was present in the checkout or the checked ancestor locations.
The initial Git status was clean; version 0.2 of Wilson–Loewner and its new
research note were already present. Both empty grouping/placeholder directories
also existed. A complete pre-edit file copy and SHA-256 inventory included
ignored and untracked files. Whole-directory renames preserved every original
file; none is missing at its mapped location. No commit, staging, or push was
performed.

The [historical hash audit](../validation/reorganization-20260920/HISTORICAL_HASH_AUDIT.json)
verifies **1,105 historical/evidence files** byte-for-byte. All **99**
nontransient Wilson–Loewner package files are also unchanged, including the
0.2 snapshot, manuscript, new research note, numerical evidence, package
inventory, and eleven inherited-source fingerprints.

The move map covers **549 nontransient relocated files**, of which **515**
are byte-identical. The other 34 contain only current navigation/path repairs,
three rebuilt PDFs, their current build records, validator path checks,
or refreshed current inventories. Historical draft contents, reviews, numerical
records, original manifests, and previous reorganization records were not
rewritten. Original current manifests/build records that were refreshed are
copied under `validation/reorganization-20260920/provenance/` for comparison.
Temporary build/cache files and `.DS_Store` are outside the durable file map;
they were included in the initial backup and checked for continued presence.

Current research-note edits are navigation-only. A normalized before/after
source comparison found no non-path changes to investigation Markdown or TeX.
The Loewner closure and its later Wilson–Loewner qualification are preserved.
Index version descriptions now use current package metadata: inverse bulk 0.6,
Wilson lines 0.8, Loewner 0.3, and Wilson–Loewner 0.2 (27 pages).

## Current navigation, dependencies and builds

Current Markdown navigation, TeX hyperlinks and printed bibliography paths,
CI build paths, package-validator paths, and repository indexes now follow the
new layout. `check_structure.py` enforces the exact grouping and scans
`previous/` normally, including source syntax, links and recorded files.
Current inventories were refreshed only after historical preservation checks;
recorded numerical outputs were never regenerated in place. The Wilson–Loewner
inventory and inherited hashes needed no changes and passed unchanged.

Four current PDFs were rebuilt and recorded with their existing procedures:
positive factorizations (21 pages), topological bulk (40), source selection
(15), and Wilson lines (47). The first two repair relative hyperlinks; the
latter two update printed bibliography paths, with line-break opportunities
for the longer names. Versions, mathematics and page counts are unchanged.
All 123 pages were rendered and compared against the pre-move PDFs: 112 pages
are pixel-identical; the other 11 were rendered at higher resolution and
visually inspected. Text changes are confined to the two affected
bibliographies. Final logs have no undefined/multiply-defined references or
overfull boxes; existing underfull warnings are recorded. See
[BUILD_VERIFICATION.json](../validation/reorganization-20260920/BUILD_VERIFICATION.json).
Historical snapshots were not rebuilt or edited.

## Validation and pre-existing failures

The [verification record](../validation/reorganization-20260920/VERIFICATION.json)
and [baseline](../validation/reorganization-20260920/BASELINE.json) distinguish
relocation checks from existing numerical-record disagreements.

- Program structure, all package integrity/snapshot checks, the dated
  relocation fingerprint audit, and repository hygiene pass.
- Arithmetic ground-state geometry reproduces all 59 exact-algebra checks.
  The complete [positive-factorizations replay](../validation/reorganization-20260920/replay/RUN_RECORD.json)
  passes, including helper imports,
  all three rounds, both round-4 programs, and rejection of optimized Python.
  Wilson–Loewner's two validators pass with all 268 diagnostic cases.
- Before any edits, strict replay already failed for inverse bulk
  (`check_explicit_formula.py`), source selection (`check_collatz_wielandt.py`),
  Wilson lines (`check_causal_commutation.py`), Loewner
  (`check_contraction_margin.py`), and fractional dimension
  (`check_which_dimension.py`). Their post-move first failures are identical.
  Further comparisons cover all 26 registered programs in these packages,
  including sibling helper imports: before/after stdout is byte-identical.
  Additional saved-record differences are itemized in
  [REPLAY_COMPARISON.json](../validation/reorganization-20260920/REPLAY_COMPARISON.json).
- Topological bulk's replay has the same existing first-program tolerance
  failure in the pre-move copy and relocated package:
  `product_mixed_difference_error` is about `6.16e-8` against recorded
  `1.72e-8`, exceeding its existing `5e-9` tolerance. All four programs were
  also run separately in both locations; their outputs agree within the
  unchanged tolerance (maximum absolute difference `3.02e-17`). See the
  [comparison](../validation/reorganization-20260920/TOPOLOGICAL_REPLAY_COMPARISON.json).
  Neither the reference evidence nor the acceptance thresholds were changed.
- The repository-wide current Markdown audit introduces no unresolved links.
  One pre-existing absolute reference in
  [the root research brief](../../../notes/supersymmetric_positivity_research_brief.md)
  still points to `Claude outputs/LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md`.
  That old brief is unchanged; the accessible note is now
  [here](../../../notes/LESSONS_LEARNED_manifest_positivity_design_guidance_20260911.md).
  Historical links are retained intentionally and resolved with the maps above.

These checks establish preservation, path correctness and replay behavior;
they do not certify mathematical proofs or alter scientific conclusions.

Re-run from the repository root:

```sh
python3 papers/susy-positivity/validation/check_structure.py
python3 papers/susy-positivity/validation/check_reorganization.py
python3 tools/check_repository_hygiene.py --working-tree
```

Use each package's own validator/replay instructions for its full checks.
`--working-tree` includes unstaged relocated and new files without changing the
Git index. The dated reorganization checker pins this delivered layout's file
contents; future research can legitimately change current files, while
historical evidence must remain unchanged.
