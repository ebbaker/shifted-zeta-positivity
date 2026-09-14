# Program reorganization and verification — 12 September 2026

The shared program now has its own [README](README.md), [background](background.pdf),
[overview](PROGRAM_OVERVIEW.md), and [continuation note](CONTINUATION_BULK_BOUNDARY_SUPERSPACE_20260912.md).
The [positive-factorizations attempt](attempts/positive-factorizations/README.md)
contains manuscript v0.2 and its supporting research. Future approaches belong
beside it under `attempts/<descriptive-name>/`.

## Directory overview

```text
shifted-zeta-positivity/papers/susy-positivity/
  README.md
  PROGRAM_OVERVIEW.md
  background.tex             # authoritative standalone wrapper and bibliography
  background_section.tex     # authoritative substantive section
  background.pdf
  CONTINUATION_BULK_BOUNDARY_SUPERSPACE_20260912.md
  attempts/positive-factorizations/
    README.md  RESEARCH_BRIEF.md  STATUS.md  INVESTIGATION_round3.md
    manuscript.tex  manuscript.pdf  manifest.json
    checks/                  # original rounds plus a safe replay runner
    archive/drafts/           # historical v0.1 PDF
    archive/progress-reports/ # round-4 derivations, review, reproduction code
    archive/provenance/       # original manifest, retained unchanged
  REORGANIZATION_20260912.md
  validation/reorganization-20260912/
```

## Old-to-new mapping

All paths below begin with the repository directory name. The complete
file-level mapping with before/after hashes is in [MOVES.json](validation/reorganization-20260912/MOVES.json).

| Old path | New path |
|---|---|
| `shifted-zeta-positivity/papers/susy-positivity/archive/overview/rh-formulation-next-version/rh_background_section.tex` | `shifted-zeta-positivity/papers/susy-positivity/background_section.tex` |
| `shifted-zeta-positivity/papers/susy-positivity/archive/overview/rh-formulation-next-version/rh_background_preview.tex` | `shifted-zeta-positivity/papers/susy-positivity/background.tex` |
| `shifted-zeta-positivity/papers/susy-positivity/archive/overview/rh-formulation-next-version/rh_background_preview.pdf` | `shifted-zeta-positivity/papers/susy-positivity/background.pdf` |
| `shifted-zeta-positivity/papers/susy-positivity/archive/overview/rh-formulation-next-version/CONTINUATION_BULK_BOUNDARY_SUPERSPACE_20260912.md` | `shifted-zeta-positivity/papers/susy-positivity/CONTINUATION_BULK_BOUNDARY_SUPERSPACE_20260912.md` |
| `shifted-zeta-positivity/papers/susy-positivity/archive/overview/RESEARCH_PROGRAM_OVERVIEW_20260911.md` | `shifted-zeta-positivity/papers/susy-positivity/PROGRAM_OVERVIEW.md` |
| `shifted-zeta-positivity/papers/susy-positivity/{manuscript.tex,manuscript.pdf,README.md,RESEARCH_BRIEF.md,STATUS.md,INVESTIGATION_round3.md,checks/,manifest.json}` | `shifted-zeta-positivity/papers/susy-positivity/attempts/positive-factorizations/{same names}` |
| `shifted-zeta-positivity/papers/susy-positivity/archive/{drafts/,progress-reports/}` | `shifted-zeta-positivity/papers/susy-positivity/attempts/positive-factorizations/archive/{drafts/,progress-reports/}` |

The archived v0.1 PDF, all three original checkers, all three recorded
diagnostic JSON files, and the substantive round-4 derivations/review moved
byte-for-byte. The round-4 reproducibility note retains its original Python
blocks, baseline hashes, and reported results; only navigation, invocation
instructions, and an explicit historical-status note changed. No second
authoritative background section or wrapper remains at the old location.

## Provenance and scope

The checkout was inspected and snapshotted before editing. At the user's
subsequent request, all pre-existing edits were committed separately as
`dad5312663f50e34278a265b86e7cf95a7657e75` before this reorganization was applied. This change preserves
the other papers and their existing organization.

The original [attempt manifest](attempts/positive-factorizations/archive/provenance/manifest_before_reorganization_20260912.json)
is a historical snapshot. All 12 original hashes matched the files inspected
before reorganization; see the [historical hash audit](validation/reorganization-20260912/HISTORICAL_HASH_AUDIT.json).
The [current manifest](attempts/positive-factorizations/manifest.json) records
fresh file hashes and labels the original validation separately. It does not
reinterpret historical diagnostics as new runs.

The background retains every original equation label, math block, and
bibliography key. It adds attribution to the positive-factorizations attempt,
program framing and PDF metadata, relative links, and a separate references
page. The manuscript changes only two repository bibliography references;
its mathematical text and version are unchanged. The established gamma
kinetic construction remains distinct from the open full arithmetic bulk
completion and the open specific superspace model.

## Fresh verification

- Built the standalone background (10 pages) and relocated manuscript
  (21 pages) with `latexmk -pdf -interaction=nonstopmode -halt-on-error`.
  Final logs contain no warnings, undefined references/citations, or box errors.
- Rendered and inspected every page; inspected the final background
  references layout after the last adjustment. No clipping, overlap, or
  unresolved references were found.
- Preserved all 26 background-section labels and 65 manuscript labels,
  all original math blocks, and every original bibliography key.
- Replayed the original three full checkers and both round-4 Markdown
  programs through [checks/replay.py](attempts/positive-factorizations/checks/replay.py).
  Rational certificates and separate floating-point identity diagnostics
  passed. The optimized-Python control was rejected as expected. The replay
  runs the checkers from a temporary working directory, exercises the
  relative helper imports, and preserves all historical diagnostics.
- Checked local Markdown navigation, TeX input/reference paths, local PDF
  links and PDF internal destinations; current hashes match. Active links
  resolve inside this repository without machine-specific paths.
- Updated the repository indexes, metadata, build workflow and hygiene
  checks for the program and attempt layout. Final Git whitespace and
  repository hygiene checks passed: 466 tracked files, 30 current READMEs,
  12 historical README snapshots, valid indexes and matching current manifests.
- Rebuilt both documents again from their final checkout locations; every
  PDF page content stream and extracted text matches the installed reading
  copies exactly. The replay runner also correctly refused an existing output directory.

Fresh machine-readable results are in [VERIFICATION.json](validation/reorganization-20260912/VERIFICATION.json),
with [replay results](validation/reorganization-20260912/replay/RUN_RECORD.json).
These checks validate relocation, reproducibility and document integrity;
they are not an independent specialist proof review or a new RH result.
