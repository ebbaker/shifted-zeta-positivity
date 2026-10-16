# Two clones writing the same files: conflict markers and duplicate registrations

15 October 2026. Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork.

## The pattern

Codex and Claude work from different clones and both edit the shared
indexes, READMEs and chat registries. A rebase conflicts, the markers are
committed, JSON registries stop parsing, two captures receive the same
number, and a manuscript "awaiting review" carries two variants of its
acknowledgements.

## What it looks like here

`<<<<<<< HEAD` blocks in eight files of one commit; a portfolio README
with literal markers at lines 18–39; two chats both numbered 2; a
registry that is broken until someone resolves it by hand.

## Evidence

- [Review 16](../papers/investigations-2/active/22_theta_manifold_geometry/reviews/16_JOINT_REVIEW_OF_INVESTIGATIONS_21_AND_22_CLAUDE_20261015.md) §9: commit `bd8d0a9` committed unresolved markers in eight files, six under `19_euler_factor_controls/` and the two portfolio-level Claude registry files; "The two JSON files no longer parse, so the portfolio-level Claude chat registry is broken until the markers are resolved". At commit `58871b3` the markers are still present (for example [19's DRAFT_HISTORY](../papers/investigations-2/active/19_euler_factor_controls/DRAFT_HISTORY.md) and the [manuscript](../papers/investigations-2/active/19_euler_factor_controls/manuscript/euler_factor_controls.tex)).
- [Portfolio closure review](../papers/investigations-2/brainstorm/reviews/PORTFOLIO_CLOSURE_REVIEW_CODEX_20261013.md): "Its portfolio README already contains literal merge-conflict markers at lines 18–39".
- [Parallel-plan review](../papers/investigations-2/brainstorm/reviews/REVIEW_OF_CODEX_RESPONSE_AND_PARALLEL_PLAN_CLAUDE_20261012.md) §4.2: "The two clones have already produced a rebase conflict, merge markers and duplicate chat numbering."; the root cause, "commit identities alternate between them"; and the rule adopted, "Each lane writes only in the folders it owns".
- [`AGENTS.md`](../AGENTS.md): "one recorder at a time"; [`tools/CHAT_HISTORY.md`](../tools/CHAT_HISTORY.md): never hand-edit registered histories, never replay old ids, paths, hashes or counters.
- [`tools/check_repository_hygiene.py`](../tools/check_repository_hygiene.py) checks sizes, links and manifests and, as Review 16 notes, "does not test for conflict markers; adding that test would have caught this."

## What it cost

A broken portfolio registry; a manuscript that will not compile; a
consolidation review that had to start by flagging markers; duplicate chat
numbers that the recorder now has to reserve around.

## Instead

One writer per shared file (the portfolio README, `brainstorm/`, and each
base registry), per the parallel-plan rule; resolve markers before any
commit (`git diff --check` or a grep for `^<<<<<<< ` in the pre-commit
hook); add the conflict-marker test to the hygiene checker; and let the
recorders' locks and `locate` do the numbering, which is what the Cowork
recorder's per-turn `locate`/`capture` cycle in [`tools/record_Claude_cowork_chat.py`](../tools/record_Claude_cowork_chat.py) is for.
