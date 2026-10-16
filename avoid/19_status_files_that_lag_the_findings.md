# Status files, READMEs and manuscripts that lag the findings of audits

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

An audit finds a problem; the finding is recorded in a review, a response
file or a chat log; the authoritative status file, checklist, README or
manuscript is not updated, or is updated in one copy and not another. The
tree then has two accounts of the same result and a reader who starts at
the status file gets the older one.

## What it looks like here

A float-conversion bug in the clean-room audit code recorded only in a
chat JSON while the manuscript's ledger still says "Independent
implementation audit & passed"; a sentence corrected in a status file and
not in the `.tex`; a README promising Arb certificates that are not in
the tree; duplicate reviews that differ by an errata section; an
inventory checker reporting mismatches that nobody refreshed.

## Evidence

- The 5 September Codex check found the clean-room audit "converts high-precision coefficients to ordinary floats while retaining error radii smaller than the conversion error", plus a `Decimal` negation bug ([chat 0004](../papers/shifted-zeta/chat-histories/chatgpt-codex/0004_2026-09-05T05-36-18Z_preprint-status-update.json)); the corrected run still passed, conditional on the archived matrices, but [VERIFICATION_STATUS.md](../papers/shifted-zeta/first-slab-positivity/VERIFICATION_STATUS.md), the [checklist](../verification/first-slab/CHECKLIST.md) (D2: "Neither reviewer read this code.") and the ledger do not record it, and weil-depth's background calls these "the disputed archived central first-slab matrix enclosures".
- [Repository review of 9 September](../notes/repository-review/9:9:26/REPOSITORY_REVIEW_AND_CHANGE_HANDOFF_20260909.md): "“No error survives” overstated what internal reviews establish"; the [response](../notes/repository-review/9:9:26/Review_response_repository_review_20260909.MD) fixed the status files and says "Not touched: PDFs, .tex". The same review found a README promising Arb certificates not in the tree and placeholder DOIs.
- [`CHANGELOG.md`](../CHANGELOG.md), 2026-09-24: "check_package.py was already reporting inventory mismatches … and was not refreshed."
- The `Claude outputs/` copy of the YM verification review lacks the §7 errata present in [the reviews copy](../papers/susy-positivity/investigations/wilson-loewner/YM/reviews/REVIEW_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md); the manuscript's "Theorem 7" citation was removed after review but the pointer survives in [the residual continuation note](../papers/investigations/program-meta-analysis/notes/SONIN_RESIDUAL_CONTINUATION_20260928.md) §2.
- Unflagged inconsistency: the [source-selection README](../papers/susy-positivity/investigations/previous/source-selection-rules/README.md) gives a least relative margin of \(9.5\cdot10^{-4}\) where [the necessary-condition section](../papers/susy-positivity/investigations/previous/source-selection-rules/sections/07_necessary.tex) gives \(3.2\cdot10^{-4}\); the inverse-bulk `BUILD_RECORD.json` is stale.
- [Sonin draft history](../papers/investigations/sonin-critical-boundary/DRAFT_HISTORY.md) ends on a working-tree revision while the manuscript doubled in length after the last cross-model round.

## What it cost

Readers of the first-slab status cannot learn of the audit issue from the
status file; the manuscript still contains an overstated sentence a review
retracted; two copies of one review disagree.

## Instead

One authoritative status file per paper, updated in the same commit as
any audit finding, with the finding's path; corrections written into the
file that made the claim with a pointer header ([`notes/REDACTION_CHECKLIST.md`](../notes/REDACTION_CHECKLIST.md) item 9); no duplicate copies of reviews outside their `reviews/` folder; and the release gate's first step, "STATUS.md is current" ([`RELEASING.md`](../RELEASING.md)), applied at every milestone, not only at release.
