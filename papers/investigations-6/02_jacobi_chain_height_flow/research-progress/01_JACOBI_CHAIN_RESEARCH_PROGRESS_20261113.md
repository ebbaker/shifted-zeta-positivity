# Jacobi-chain height flow — Research progress

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and effort
are unavailable in recorded configurations.

**This is the sole current task-status register for the JCH family.**
Re-read it before editing and preserve other chats' updates. The
[plan](../research-plan/01_JACOBI_CHAIN_RESEARCH_PLAN_20261113.md) supplies
the specifications, finite limits, routine choices and escalation rules.
The parent [TN6 register](../../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
links here and owns only shared tasks.

| Task | Type and recommended model/reason | Current status | Dependencies and output |
| --- | --- | --- | --- |
| JCH-B01 | B — GPT-6 Astra / Ultra; chose the scalar finite-chain readout and its error norm | Complete: fixed contract, no proof claimed | [Decision](../brainstorm/notes/01_JCH_B01_READOUT_DECISION_20261113.md); three formulations compared; generic Gauss/Hermite scalar estimate selected. |
| JCH-E01 | E — GPT-6.1 Sol / Ultra; fixed analytical derivation and observation-error accounting | Complete, proved in-note | [r1 request](handoffs/JCH-E01-r1.md), [proof](../notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md), [return](handoffs/JCH-E01-r1-return.md). R2–R4 on each bounded real rectangle. |
| JCH-E02 | E — GPT-6.1 Sol / Ultra; fixed proof/interface assessment | Complete, accepted within scope by same-worker internal assessment | [r1 request](handoffs/JCH-E02-r1.md), [assessment](../reviews/01_JCH_E02_FINITE_CHAIN_ASSESSMENT_20261113.md), [return](handoffs/JCH-E02-r1-return.md). No correction or optional response check. |
| JCH-E03 | E — GPT-6.1 Sol / Ultra; integrate and check the frozen analytical results and existing certificate | Branch manuscript complete and internally assessed, 14 November 2026 | [TN6-E04 r1](../../research-progress/handoffs/TN6-E04-r1.md), [manifest14](../../numerics/14_TN6_E04_MANUSCRIPT_INPUTS_20261114.json); [draft](../manuscript/README.md), [source map](../notes/03_JCH_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md), [assessment](../reviews/02_JCH_ANALYTICAL_MANUSCRIPT_ASSESSMENT_20261114.md), [build](../numerics/02_JCH_E03_MANUSCRIPT_BUILD_20261114.json). One externally built draft and a bounded check; parent four-paper visual and cross-manuscript review is complete. |

At setup there was no issued JCH request or mathematical execution. B01 now
selects a real-height scalar estimate and issues E01 r1. The core estimate
has no unproved coefficient prerequisite; numerical coefficient acquisition
and a sharper VCD input remain separate. Readiness is not proof. No
numerical run or E01 execution is claimed by the B01 return.

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

## Evidence and ownership crosswalk

The inherited fixed-basis identity and bond-two single-excitation encoding
remain exact representation identities with a same-assistant analytical
check. Fixed-prefix mass escape supplies no transport rate; no signed-field
bound is acquired by this plan. See the [overview](../research-overview/01_JACOBI_CHAIN_RESEARCH_OVERVIEW_20261113.md),
[reference guide](../references/README.md) and parent
[source crosswalk](../../notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md).

On 13 November 2026, the author's branch-planning request superseded the
earlier deferral for this branch. Previously unassigned branch questions
now have JCH task IDs. No existing task, issued packet or completed result
was moved or superseded. This register replaces no earlier live register;
the old progress README was only a directory guide. QTT, VCD, ITP and TN6
keep separate owners.

## Event log and update rule

- **13 November 2026 — Branch planning setup:** Added the bounded B/E plan,
  this sole JCH register and current navigation; linked the canonical
  continuation and reused reference records. Planning only; all research
  tasks remain unactivated. Prepared for Edward Baker with OpenAI Codex
  assistance; actual model/effort unavailable. See [DRAFT_HISTORY](../DRAFT_HISTORY.md).

Later updates record date, actual model/effort when available, request and
input versions, output paths, evidence level, result/failed premise and
disposition. Preserve issued requests and unfavorable returns. A conceptual
contract change returns to JCH-B01; a routine correction remains within
E01. No model change is represented as independent specialist review.

## Continuation

**The JCH-B01 → E01 → E02 sequence is complete.** The parent
[TN6 register](../../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
owns any shared comparison. A new branch mechanism, observable or
coefficient acquisition requires a new scoped decision.
Read the [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md) and the plan's specific controls
before proposing an estimate. Follow [REFERENCE_WORKFLOW](../../../../REFERENCE_WORKFLOW.md)
and [chat-history guidance](../../../../tools/CHAT_HISTORY.md). New
branch-only chats use [this history folder](../chat-histories/README.md);
already registered chats keep their unique existing home.

## 13 November 2026 — B01 return

Prepared for Edward Baker with OpenAI Codex assistance; dispatch selection
**gpt-6-astra / ultra**, actual backend model/effort unavailable. One round
compared exactly three formulations and selected a generic Gauss/Hermite
scalar-readout estimate. [Decision](../brainstorm/notes/01_JCH_B01_READOUT_DECISION_20261113.md),
[source/control screen](../notes/01_JCH_B01_SOURCE_AND_CONTROL_SCREEN_20261113.md),
[reference inspection](../references/01_DLMF_GAUSS_QUADRATURE_20261113.md) and
[frozen E01 r1](handoffs/JCH-E01-r1.md) are saved. No theta-specific
coefficient theorem, signed lower margin, relative accuracy or numerical
certificate is asserted. The matched Gaussian-quadrature baseline is
algebraically identical. E01 ownership transfers to the coordinator for
Sol 6.1 / Ultra dispatch; the B worker does not execute its own packet.

## 13 November 2026 — E01 and E02 returns

Prepared for Edward Baker with OpenAI Codex assistance. Execution dispatch
**gpt-6.1-sol / ultra** for both passes, actual backend model/effort
unavailable. The E01 r1 input and return versions are recorded in its
[return](handoffs/JCH-E01-r1-return.md). Its [proof note](../notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md)
proves R2, including the omitted edge \(a_N\), and R3/R4 with the complete
source moment, with no mathematical correction or numerical campaign.
The [E02 r1 return](handoffs/JCH-E02-r1-return.md) records the second
freeze and same-worker assessment. Its disposition preserves the
literal Gauss-quadrature equivalence, real scalar scope and unpaid
certification and relative-margin costs.

## 14 November 2026 — E03 manuscript return

For Edward Baker with substantial OpenAI Codex assistance. Execution
dispatch GPT-6.1 Sol / Ultra; backend and runtime effort attestation
unavailable. Frozen scope fixes one manuscript integrating the accepted
real-scalar and coefficient bounds and the existing finite supporting
certificate. The branch draft and same-worker assessment are complete.
The prepared-state prefix rate, growing-height behavior, coefficient
conditioning and signed margin remain open. Any change of the mathematical
target belongs to a separate scoped decision. The source and external
reading copy transfer to the parent for final build and visual checks.

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
