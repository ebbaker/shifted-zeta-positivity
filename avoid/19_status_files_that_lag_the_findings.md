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

- The 5 September Codex check found the clean-room audit "converts high-precision coefficients to ordinary floats while retaining error radii smaller than the conversion error", plus a `Decimal` negation bug ([chat 0004](../papers/weil-positivity/shifted-zeta/chat-histories/chatgpt-codex/0004_2026-09-05T05-36-18Z_preprint-status-update.json)); the corrected run still passed, conditional on the archived matrices, but [VERIFICATION_STATUS.md](../papers/weil-positivity/shifted-zeta/first-slab-positivity/VERIFICATION_STATUS.md), the [checklist](../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/CHECKLIST.md) (D2: "Neither reviewer read this code.") and the ledger do not record it, and weil-depth's background calls these "the disputed archived central first-slab matrix enclosures".
- [Repository review of 9 September](../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/repository-review-20260909/REPOSITORY_REVIEW_AND_CHANGE_HANDOFF_20260909.md): "“No error survives” overstated what internal reviews establish"; the [response](../papers/weil-positivity/shifted-zeta/first-slab-positivity/verification/repository-review-20260909/Review_response_repository_review_20260909.MD) fixed the status files and says "Not touched: PDFs, .tex". The same review found a README promising Arb certificates not in the tree and placeholder DOIs.
- [`CHANGELOG.md`](../CHANGELOG.md), 2026-09-24: "check_package.py was already reporting inventory mismatches … and was not refreshed."
- The `Claude outputs/` copy of the YM verification review (removed on 16 October 2026; in the history at `0a1156e`) lacks the §7 errata present in [the reviews copy](../papers/weil-positivity/susy-positivity/investigations/wilson-loewner/YM/reviews/REVIEW_CLAUDE_MANUSCRIPT_VERIFICATION_20260925.md); the manuscript's "Theorem 7" citation was removed after review but the pointer survives in [the residual continuation note](../papers/investigations/program-meta-analysis/notes/SONIN_RESIDUAL_CONTINUATION_20260928.md) §2.
- Unflagged inconsistency: the [source-selection README](../papers/weil-positivity/susy-positivity/investigations/previous/source-selection-rules/README.md) gives a least relative margin of \(9.5\cdot10^{-4}\) where [the necessary-condition section](../papers/weil-positivity/susy-positivity/investigations/previous/source-selection-rules/sections/07_necessary.tex) gives \(3.2\cdot10^{-4}\); the inverse-bulk `BUILD_RECORD.json` is stale.
- [Sonin draft history](../papers/investigations/sonin-critical-boundary/DRAFT_HISTORY.md) ends on a working-tree revision while the manuscript doubled in length after the last cross-model round.

## What it cost

Readers of the first-slab status cannot learn of the audit issue from the
status file; the manuscript still contains an overstated sentence a review
retracted; two copies of one review disagree.

## Instead

One authoritative status file per paper, updated in the same commit as
any audit finding, with the finding's path; corrections written into the
file that made the claim with a pointer header ([`REDACTION_CHECKLIST.md`](../early-chat-logs/initial-project-files/rh3/REDACTION_CHECKLIST.md) item 9); no duplicate copies of reviews outside their `reviews/` folder; and the release gate's first step, "STATUS.md is current" ([`RELEASING.md`](../RELEASING.md)), applied at every milestone, not only at release.

**17 October 2026 evidence — gpt-6-astra, max; LLM assistance for Edward
Baker.** [Dirichlet review 03](../papers/investigations-3/01_dirichlet_newman_families/reviews/03_CROSS_MODEL_MATHEMATICAL_REVIEW_CODEX_20261017.md)
found: “Lines 6–30 still describe a pending Codex audit,” although the
next paragraph announced the completed comparison. The
[response](../papers/investigations-3/01_dirichlet_newman_families/notes/round-4/04_REVIEW_RESPONSE_AND_SIBLING_BENCHMARK_CODEX_20261017.md)
reconciles the README, manuscript, build record and stronger sibling
benchmark while preserving the historical reviews and their source hashes.

**18 October 2026 resolved manuscript lag — gpt-6-astra, actual effort max;
LLM assistance for Edward Baker.** Investigation 3/11's earlier manuscript
README described a 30-page draft “without an effective onset or cost claim”
while later Notes 11–14 already provided effective tails, finite exclusion
and a sharper exterior. [Integration Review 13](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/13_CURRENT_RESULTS_MANUSCRIPT_INTEGRATION_REVIEW_20261018.md)
records the incorporation and fresh current-source replay. The
[45-page manuscript and build record](../papers/investigations-3/11_arithmetic_collision_rigidity/manuscript/README.md),
progress tracker and status indexes now agree: “The bridge
1001<|x|<e^2000 remains open on the stated slab.” Historical certificates
retain their original source pins; a new current-source setup is generated
instead of treating an old hash as approval for revised bytes.


**19 October 2026 symmetry status synchronization — gpt-6-astra, max;
LLM assistance for Edward Baker.** [Review 15](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/15_MANUSCRIPT_AND_SYMMETRY_ACCOMPLISHMENTS_REVIEW_ASTRA_20261019.md)
found that the compact S05 row “still lists only source-range improvements”
after its complete consumer comparison. The S04/S05 rows, current plan
pointers and manuscript summary are now synchronized, while original
task contracts remain historical. [Integration review 16](../papers/investigations-3/11_arithmetic_collision_rigidity/reviews/16_SYMMETRY_PROGRAM_AND_MANUSCRIPT_INTEGRATION_REVIEW_20261019.md)
distinguishes documentation completion from new estimating or coverage gains.


**25 October 2026 — preserving one live ansatz plan.** For Edward Baker,
LLM assistance **gpt-6-astra, recorded effort max**.
[Note09](../papers/investigations-5/01_heat_density_asymptotics/ansatz/notes/09_EVOLUTION_MANUSCRIPT_AND_PRIORITY_REVISION_20261025.md)
records: “Historical frozen requests and returns are preserved.” The
author's new evolution-first priority is carried into the manuscript,
Overview02, Progress02 and pending-packet navigation; the old pair is
explicitly superseded. This prevents two competing live priorities
without rewriting historical evidence or promoting an unproved estimate.


**26 October 2026 — separate central synthesis from pending companion revision.**
For Edward Baker with LLM assistance, **gpt-6-astra, actual effort max**.
The [Book production review](../papers/investigations-5/01_heat_density_asymptotics/reviews/42_BOOK_SYNTHESIS_PRODUCTION_REVIEW_20261026.md)
records: “Companion revisions are planned, not executed.” The Book cites
the newer positive hierarchy and evaluation proof notes directly while
the three older manuscripts await their explicit Sol revision packet.
Current navigation marks the earlier central-parent proposal superseded;
the new coordination register links existing scientific owners instead of
creating competing live phases. Publication of a synthesis must not make
an older companion appear already synchronized.


**26 October 2026 — companion lag resolved.** For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort ultra**, chat0024. [Review43](../papers/investigations-5/01_heat_density_asymptotics/reviews/43_BOOK_COMPANION_INTEGRATION_PRODUCTION_REVIEW_20261026.md) states: “Companion production is complete; scientific claims retain their sourced scopes.” The earlier Review42 checkpoint remains historical. New source proofs are integrated at their actual technical homes, a phase-selector existence/selection-margin slip is corrected against the original source, and current navigation/build records now agree. Concurrent later research returns are explicitly pinned as source supplements rather than silently folded into earlier proof provenance.

**26 October 2026 — six bounded closures and their manuscript interfaces.**
For Edward Baker with substantial LLM assistance, **gpt-6.1-sol, actual effort
ultra**, chat0027. [B02 Review45](../papers/investigations-5/01_heat_density_asymptotics/reviews/45_B02_R2_MANUSCRIPT_INTEGRATION_PRODUCTION_ASSESSMENT_20261026.md)
records: “Production completion changes proof placement and current navigation,
not scientific evidence status.” Current manuscripts/READMEs no longer call
completed regional field and fixed-P4 returns unexecuted. Frozen requests,
source notes, older builds and wider physical/core/cost/audit gates retain
their original scope; production status is reconciled in its sole Book register.

**26 October 2026 — Summary76 and completed pilot synchronized.**
For Edward Baker with LLM assistance, **gpt-6-astra, actual effort max**.
[Book Review52](../papers/investigations-5/01_heat_density_asymptotics/reviews/52_BOOK_SUMMARY76_PRODUCTION_REVIEW_20261026.md)
records: “The complete weak consumer is no longer an open fixed-data task;
shrinking-resolution and practical global-time cost remain separate.”
The synthesis now includes Notes71–75 and the completed RT pilot while
preserving their bounded hypotheses. New combined work has one HCB
register in Investigation03; original RT/HDA IDs and dated requests remain
in their existing homes. Closing a scoped consumer does not close its
shrinking-resolution or global-cost extension.
