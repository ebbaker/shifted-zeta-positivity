# QTT research progress

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and effort are
unavailable in recorded configurations.

**This file is the sole current task-status register for the QTT family.**
The parent provides navigation, not a second set of status rows. Re-read
this file before editing; one writer owns each active artifact and must
preserve updates from other chats.

| Task | Type and recommended model | Current status | Dependencies and output |
| --- | --- | --- | --- |
| QTT-B01 | B — GPT-6 Astra / Ultra; choosing the observation norm and useful rank target is conceptual | Complete: one round, three options | [Decision](../brainstorm/notes/01_QTT_B01_OBSERVATION_NORM_DECISION_20261113.md) selects a compact scaled absolute-error allowance and scalar polynomial baseline; no sign or speed claim. |
| QTT-E01 | E — GPT-6.1 Sol / Ultra; fixed derivation and error accounting | Complete, proved in-note on first tuple | [Frozen r1](handoffs/QTT-E01-r1.md), [proof](../notes/04_QTT_E01_COMPACT_RANK_ERROR_BOUND_20261114.md) and [return](handoffs/QTT-E01-r1-return.md). Exact rank at most 641 and scaled absolute error below 2^-36. |
| QTT-E02 | E — GPT-6.1 Sol / Ultra; fixed assessment | Complete, accepted without mathematical correction within scope | [Frozen r1](handoffs/QTT-E02-r1.md) and [same-worker internal assessment](../reviews/01_QTT_E02_RANK_ERROR_ASSESSMENT_20261114.md). |
| QTT-E03 | E — GPT-6.1 Sol / Ultra; integration of the fixed proof and assessment | Complete; parent cross-review accepted the draft within scope | [TN6-E04 r1](../../research-progress/handoffs/TN6-E04-r1.md), [manuscript](../manuscript/README.md), [integration](../notes/05_QTT_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md) and [internal assessment](../reviews/02_QTT_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md). |

The [plan](../research-plan/01_QTT_RESEARCH_PLAN_20261113.md) owns task
specifications, including deliverables, evidence standards, work limits,
routine choices and escalation triggers. No E request was issued at setup;
[QTT-E01 r1](handoffs/QTT-E01-r1.md) is now the first issued request.

## Parallel continuation authorization — 13 November 2026

Edward Baker selects **GPT-6 Astra / Ultra** for B tasks and **GPT-6.1
Sol / Ultra** for E tasks and authorizes parallel branch work, subagent
handoffs, and continuing into the next ready task without renewed
permission. See the [canonical continuation](../../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md).
Record each return and freeze/check the next request, then proceed through
B01 → E01 → E02 as dependencies become ready. The permitted bounded
correction/response passes are included. Earlier setup-only activation
restrictions are superseded; finite limits, evidence standards and missing-
input stops remain. No task is recorded as started by this documentation
update. Author-selected future settings are distinct from actual authoring
metadata, which remain unavailable.

## Setup event

**13 November 2026:** Branch structure and navigation completed under the
author's setup request. The [crosswalk](../notes/02_QTT_SETUP_AND_SOURCE_CROSSWALK_20261113.md)
preserves inherited evidence in place; its existing floating pilot and
same-assistant review are not new QTT task completions. No mathematical
execution, numerical rerun, additional chat or manuscript was authorized
by folder creation. The [setup manifest](../numerics/01_QTT_SETUP_INPUT_MANIFEST_20261113.json)
records source identities, not mathematical validation.

**13 November 2026, collection branch-planning refresh:** retained this
sole register and all QTT task rows while the author requested plans and
registers for every sub-investigation. Added parent/interface navigation
to the existing plan; no task transition, new packet or mathematical
execution. Prepared for Edward Baker with OpenAI Codex assistance; actual
model/effort unavailable. The [TN6 register](../../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
owns shared work only; the [collection continuation](../../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
routes to the branch registers without copying their live status.

**13 November 2026, QTT-B01 return:** one bounded comparison selected a
complete-source Chebyshev/heat-polynomial QTT allowance on
0<=lambda<=1/2, 40<=x<=80, |y|<=8. Exact source coefficients, tail,
quadrature, normalization and optional computed-error budgets are explicit.
The scalar baseline integrates the same polynomial exactly and has no
larger error allowance. The three-atom event and catalog screen prevent
interpreting low rank as a sign barrier. Requested/dispatched authoring
model gpt-6-astra, effort ultra; independent backend metadata unavailable.
No E derivation, numerical campaign or assessment has run in B01.

**13–14 November 2026, QTT-E01 return:** [Proved in-note](handoffs/QTT-E01-r1-return.md) on the first tuple. The matched scalar integral omits midpoint error. Tool dispatch gpt-6.1-sol / ultra. Separate backend verification unavailable. No numerical experiment.
Use the [canonical continuation and prompt](../notes/01_QTT_CONTINUATION_AND_PROMPT_20261113.md).
The author selects actual model and effort; recommendations are not
recorded execution settings.


**14 November 2026, QTT-E02 return:** [Accepted without mathematical
correction within scope](../reviews/01_QTT_E02_RANK_ERROR_ASSESSMENT_20261114.md)
after verifying four assessment inputs and 22 inherited identities.
Separate same-worker internal assessment. Tool dispatch gpt-6.1-sol /
ultra. Separate backend verification unavailable. The fixed QTT round is
complete.

**14 November 2026, QTT-E03 return:** The fixed QTT result is integrated
in a buildable [draft](../manuscript/README.md). The proof and comparison
preserve the complete source and the exact coefficient/contraction scope.
The [internal assessment](../reviews/02_QTT_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md)
requires no correction to the frozen theorem. Recorded drafting dispatch
gpt-6.1-sol / ultra; separate backend attestation unavailable. Rendered
page and cross-manuscript checks pass to the parent.

## 14 November 2026 — parent manuscript checks completed

For Edward Baker with OpenAI Codex assistance; manuscript and review
workers dispatched Sol 6.1/Ultra, coordinator backend/effort unavailable.
The parent [cross-review](../../reviews/03_TN6_ANALYTICAL_MANUSCRIPT_CROSS_REVIEW_20261114.md)
accepted all four analytical drafts within stated scope, with shared
premises and contributor overlap disclosed. The [combined build](../../numerics/15_TN6_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json)
and [final document check](../../numerics/18_TN6_MANUSCRIPT_FINAL_CHECK_20261114.json)
record the current external PDF identities and all-page inspection.
The [current handoff](../../notes/10_ANALYTICAL_MANUSCRIPTS_CONTINUATION_AND_MODEL_HANDOFF_20261114.md)
prioritizes one bounded analytical improvement next. No new numerical
experiment or change to the earlier proof status.
