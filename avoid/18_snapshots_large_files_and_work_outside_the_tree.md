# Snapshot sprawl, large data in history, and work that exists only outside the tree

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

Manuscript milestones are saved as copied folders instead of commits;
derived matrices enter git history; results exist as sandbox links in a
chat, in a session workspace that was lost, or in matrices that are "not
present locally"; references point to commit hashes that no longer exist
or to files that moved. The tree then describes work it does not contain.

## What it looks like here

Thirty-nine preserved snapshot folders, nine of them one day's drafts of
one manuscript; a 122 MB branch history; an audited manuscript
overwritten before its folder was committed; a lost workspace; a
commit pin that "no longer exists in the repository".

## Evidence

- [WZW assessment](../papers/susy-positivity/investigations/wilson-loewner/WZW/reviews/review_claude_wzw_program_assessment_20260924.md) §4: the audited manuscript "was never committed and was overwritten before the folder was committed."; the filename typo `DRAFT_HISTOR.md` spread to 11 files before the 13 October rename ([`CHANGELOG.md`](../CHANGELOG.md)).
- `papers/susy-positivity/investigations/wilson-lines/drafts/` holds v01–v08, all dated 17 September, growing from 18 to 47 pages; [`AGENTS.md`](../AGENTS.md) now says "create no new manuscript snapshot folders" and the [Wilson–Loewner draft history](../papers/susy-positivity/investigations/wilson-loewner/DRAFT_HISTORY.md) says milestones "should reference commits or tags".
- [`LARGE_FILES.md`](../LARGE_FILES.md) §3: the finite-horizon branch history held about 122 MB of matrices; "A stale local copy can still retain its old large blobs, so it must not be merged into main again."
- [RH-detector STATUS](../papers/misc/rh-detector/STATUS.md): "The original session workspace was lost in a service outage around 24–25 August 2026"; defect-depth's round-6 runs were "not saved as standalone files" ([STATUS](../papers/shifted-zeta/defect-depth/STATUS.md)); the second-slab certificates exist only as sandbox links in a chat log ([chat 0004](../papers/shifted-zeta/chat-histories/chatgpt-codex/0004_2026-09-05T05-36-18Z_preprint-status-update.json)); the storage-depth R18 matrices are "not present locally" ([CLOSEOUT](../papers/shifted-zeta/storage-depth/CLOSEOUT.md)).
- Dangling references: the storage-depth v0.2 commit pin "no longer exists in the repository" ([v0.2 review](../papers/shifted-zeta/storage-depth/archive/reviews/REVIEW_storage-depth_v0.2_claude_20260910.md) §2); [`verification/README.md`](../verification/README.md) cites ROUND files that live under `early-chat-logs/initial-project-files/rh3/claude/`; the first-slab reviews README lists a round-1 review absent from that folder; a review cited by [external review 12](../papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/reviews/12_EXTERNAL_REVIEW_OF_MERGED_PROJECT_CLAUDE_20261011.md) is not in the tree.

## What it cost

A manuscript that was reviewed and then lost; an 11-file rename; a
branch that cannot be merged; certificates that cannot be replayed from
the tree; readers sent to files that are not there.

## Instead

Milestones in `DRAFT_HISTORY.md` pointing at commits or tags, no snapshot
folders ([`AGENTS.md`](../AGENTS.md)); derived data outside git bound by two hashes with the regeneration command recorded ([`LARGE_FILES.md`](../LARGE_FILES.md) §1); every certificate's inputs either in the tree or hash-bound with the replay command; every path cited in a note checked by the hygiene checker's link test; and when something is accepted as missing, say so in a closeout file, as storage-depth's does.
