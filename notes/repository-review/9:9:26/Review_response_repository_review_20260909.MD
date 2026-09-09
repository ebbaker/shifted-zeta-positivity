# Response to the 9 September 2026 repository review

Review received: `REPOSITORY_REVIEW_AND_CHANGE_HANDOFF_20260909.md` + bundle
`REPOSITORY_CHANGES_20260909/` (patch, overlay files, certificate candidate,
validation logs). Reviewed snapshot `50cb4d2` = the repo's first commit; the
patch applied cleanly to it and the overlay files were byte-identical to the
patch result.

## Verdict on each finding

| # | Finding | Verdict | What was done |
|---|---|---|---|
| 1 | Root description promised Arb certificates not in the tree | **Correct** | Tagline, `.zenodo.json`, `code/README.md`, `MANIFEST.md` reworded; certificate code recovered as a review candidate, kept out of the tree (D1–D5). |
| 2 | Paper `CITATION.cff` had invalid top-level `type: generic` | **Correct** — confirmed against the official CFF 1.2.0 schema (top-level `type` ∈ {software, dataset}); original root passed, paper failed | Both files now `type: software` + `preferred-citation` (type `unpublished`) for the preprint; both validate. Root license MIT (describes code), paper stays CC BY 4.0. `tools/check_citations.py` + `environment/requirements_metadata.txt` added. |
| 3 | Example DOIs / future deposits readable as done; repo vs manuscript version unclear | **Correct in substance; implementation modified** | Removed every `NNNNNNN`/`XXXXXXX` placeholder. Did *not* hard-code the reviewer's commit hash into the READMEs (a file cannot cite the commit that contains it — stale on the next commit); used a commit-based interim form with ⟨hash⟩ and DOI forms with ⟨…⟩ placeholders. Added a "Current state" paragraph: no tag, no DOI; repo version `0.2.0` vs manuscript `1.0` are separate identifiers. |
| 4 | LICENSE linked the CC homepage; "dual license" ambiguous | **Correct** | Reviewer's LICENSE taken as-is (specific deed + legal code, scope by material type, copyright line unchanged); "dual license" wording replaced everywhere. |
| 5 | Notes index described reports not present | **Correct** | Preface rewritten (one block, not two stacked review-dated quotes): only the index and redaction checklist are present; migration is per-file and recorded in the checklist. |
| 6 | "No error survives" overstated | **Correct** | Reviewer's wording taken in `VERIFICATION_STATUS.md` and `CHECKLIST.md`. |
| 7 | Historical A4 numerics unstable; failures never a nonzero exit | **Correct** | `verify_stable_volterra_20260909.py` reviewed line by line against the paper's eq. (kappa-explicit) and Galerkin overlap algebra — formula and index rules are right; re-run: 16/16 pass under pinned CPython 3.12 env; injected 0.001 → 4 FAIL, exit 1. Committed with its requirements and README section. |
| 8 | CI did not run numerics or CFF checks | **Correct** | `check-first-slab.yml` added (staged under `_github/`, needs `mv` to `.github/`), with `--retry 3` on the schema download. RELEASING.md updated on what `build-latex` does/doesn't establish. |

Rejected/modified wording: the reviewer's "Repository state at the 9 September
2026 review" paragraphs in README and RELEASING were review-meta text that
would age badly; folded into durable statements. The reviewer's `.zenodo.json`
description contained an instruction to the author ("Confirm these descriptions
against the tagged tree before depositing") — moved to RELEASING gate step 1;
the deposit description itself rewritten to be true at tag time and to keep
the blueprint/statements/verification description.

## Certificate candidate — what was checked

Not integrated (gate D1–D5). Independently verified here:

- Candidate `SHA256SUMS` passes; the four result-table hashes equal those in the
  author's 5 Sept regeneration record.
- Stored-table verifiers pass (724 / 90 / 783 + 1360 rows).
- **Full regeneration** of Investigations 12 (`--certify`), 13 and 14 in a
  fresh venv (CPython 3.12.3; mpmath 1.4.1, numpy 2.3.5, python-flint 0.9.0,
  scipy 1.17.0): ~1 min / 39 s / 1 min 54 s; all four tables **byte-identical**
  to the archived ones. Kernel-norm enclosure `0.012293050401142319 ± 6.84e-19`,
  Taylor remainder `1.533e-12`, 512 boxes, min LDL pivot `0.0232681`, max Schur
  loss `9.96e-5`, min Weyl margins `6.116350109501e-4` / `5.261670009275e-2`,
  audit margin `6.116514636999e-4` — all as in the preprint.
- Recorded as `verification/first-slab/CERTIFICATE_RERUN_20260909.md`; D4 in
  CHECKLIST and VERIFICATION_STATUS annotated with the two clean reruns.

Still open before the code can be released: D1 (rederive the Investigation 7
tail majorants), D2 (second reader for the interval LDLᵀ / box construction),
D3 (full primary-vs-audit row diff), D5 (stale passages in Investigation 12 §4,
§8.4 and Investigation 14 opening list / §9; the candidate README lists them).

## Files written to the repo (24)

Modified: `README.md`, `LICENSE`, `CITATION.cff`, `.zenodo.json`, `RELEASING.md`,
`CHANGELOG.md`, `MANIFEST.md`, `notes/README.md`, `papers/README.md`,
`papers/first-slab-positivity/{README.md,CITATION.cff,VERIFICATION_STATUS.md}`,
`verification/README.md`, `verification/first-slab/CHECKLIST.md`,
`verification/first-slab/scripts/README.md`, `code/README.md`,
`code/certificates/first-slab/README.md` (also: contact e-mail corrected to the
personal address).
New: `verification/first-slab/CERTIFICATE_RERUN_20260909.md`,
`verification/first-slab/scripts/{verify_stable_volterra_20260909.py,requirements_stable_checks.txt}`,
`tools/check_citations.py`, `environment/requirements_metadata.txt`,
`_github/workflows/check-first-slab.yml` (+ `_github/README.md` move note).

Not touched: PDFs, `.tex`, historical scripts, `statements/ledger.yaml`,
`blueprint/`, draft folders.