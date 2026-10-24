# GPT research workflow: Astra analysis, Sol numerics

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this chat's session metadata.

This is the canonical guidance for GPT research chats in this repository,
placed at the repository root at the author's request on 24 October 2026.
The repository also uses Claude. This document defines the Astra/Sol
division within GPT work; Claude's responsibilities remain governed by
the author's separate assignments.

## Standing division of work

At the author's request, use this division for future GPT research work:

| Owner | Responsibility |
| --- | --- |
| **GPT-6 Astra (`gpt-6-astra`)** | Analytical formulas, asymptotics, proofs, hypotheses, norms, error decompositions, research priorities and interpretation of numerical evidence. Astra specifies the numerical question and decides what the returned evidence permits the analytical argument to claim. |
| **GPT-6.1 Sol (`gpt-6.1-sol`)** | All numerical implementation and execution: numerical code, evaluators, quadrature, precision and stability work, computational checks, interval or exact-arithmetic certificates, diagnostics, tables and plots. Sol reports errors and limitations explicitly. |
| **Edward Baker** | Maintains the chats, chooses the actual models and effort, and carries the handoff between chats. |

This is a manual workflow. It does not create chats, dispatch agents, send
messages between chats, schedule runs or change model settings. Existing
[chat-history capture](tools/CHAT_HISTORY.md) continues under its standing rules.
Historical results retain their actual author/model attribution.

Astra can inspect code and numerical reports and verify their provenance,
but sends numerical coding, execution, debugging and reruns to Sol. This
includes a proposed "quick numerical check" and machine-executed symbolic
or exact-arithmetic verification. Mathematical derivations remain Astra's
work. Ordinary file editing, links, hashes, manuscript production and chat
capture are housekeeping and can be performed by either owner.

Sol may choose and repair implementation details within the agreed scope
and budget. If a formula is ambiguous or apparently wrong, Sol records
the minimal evidence and returns the analytical issue to Astra. Sol does
not silently change the source, normalization, regulator, target norm,
domain, tolerances or theorem. A numerical counterexample or failed budget
must be retained; ownership never overrides contrary evidence.

## The handoff cycle

1. **Astra develops the analysis.** Use `ANALYSIS_READY` before starting
   and `ANALYSIS` while working. State the intended analytic gain and the
   remaining estimate. Request computation only when its answer will
   affect the proof, approximation, bound or choice of method.
2. **Astra prepares a request and hands off to Sol.** Complete the request
   section of one packet, link it in the existing progress register and
   mark its handoff phase `READY_FOR_SOL`. End with the packet's absolute
   path and a short prompt the author can paste into the Sol chat.
3. **Sol executes the bounded request.** Re-read the live progress entry
   and exact packet revision, record the actual model/effort, and mark
   `NUMERICS`. Work within its budget; preserve failures and stop rules.
   Append the return section, link the code and small records, and mark
   `READY_FOR_ASTRA`. Hand the author the same packet path and return prompt.
4. **Astra evaluates the return.** Mark `ANALYTIC_REVIEW`; check the result's
   scope, assumptions and error accounting. Record whether it supplies the
   requested input, remains diagnostic, exposes a scoped failure or leaves
   an unresolved issue. Integrate the justified result in notes/manuscript
   and the existing task ledger, or revise the analysis. Mark `CLOSED` only
   when the packet has a recorded disposition. Further numerical work gets
   an explicit new request revision or a separate packet.

These are handoff phases, separate from a research task's Complete, Partial,
Ready or Gated status. Completing a computation does not complete its parent
theorem. A packet may return to Astra without a successful run when the
question is ill-posed, the method fails or the budget is exhausted.

The author can keep several chats open. Each packet and shared artifact
has one current writer. Before editing a shared progress entry, re-read
it and preserve other packets' updates. Do not infer that an old chat's
local context is newer than the files. Separate packets can proceed on
disjoint artifacts when the author arranges that work.

## One compact packet, linked from the existing progress register

Create a packet only for a real numerical question. Put it in the affiliated
investigation's `research-progress/handoffs/` directory, using its task ID
and a sequence, for example `HDA-19-N01.md`. The example is not a current
assignment. Keep the existing progress file as the sole task ledger; record
the packet path, revision, handoff phase, current owner and next action there.
Do not duplicate the whole research history in the packet.

Use these three sections:

```text
ID / parent task / request revision / date:
Request author and actual model/effort:
Next owner:
Current phase (the progress register owns the live phase):
Read first: exact files and sections; required repository instructions.
Input versions: commit where available, plus hashes for relevant uncommitted inputs.
Files this packet may write:

REQUEST — Astra
Analytical statement or bound being advanced, with a note/equation reference:
Question the computation can answer and how each outcome changes the analysis:
Exact formulas and conventions, domain, regulator, kernels and normalizations:
Required outputs and whether diagnostic, exact or interval-certified:
Error components to report separately; tolerance/precision requirements:
Finite cases or adaptive selection rule; refinement and work limits:
Numerical stopping rule; analytical remainder or infinite-range obligation:
Existing code/results to reuse; expected output locations and return prompt:

RETURN — Sol
Actual model/effort, date, thread ID, request revision and input versions used:
Outcome and decision-relevant numbers, including every failed requested case:
Code and small execution-record paths; reproduction command and environment:
Source/truncation, arithmetic and integration errors and unresolved components:
Checks, stopping reason, actual work/runtime, and available usage data:
Deviations from the request, implementation limitations and analytical questions:

ANALYTICAL DISPOSITION — Astra
Actual model/effort and date; exact return reviewed:
Accepted input, diagnostic only, scoped failure or further work needed:
What changed in the bound, domain, formula or proof; what did not follow:
Evidence links, research-task status changes if justified, and next action:
```

Freeze the dispatched request revision. Sol appends its return without
rewriting the request or prior evidence. A mathematical change creates a
new explicitly numbered revision; retain the old request and return so
results cannot be silently applied to different inputs. If required input
files changed, record the mismatch and resolve it before using the result.
Keep mathematical derivations in `notes/`, code and small execution records
in `numerics/`, and assessments in `reviews/`; link them from the packet.
Apply [LARGE_FILES.md](LARGE_FILES.md) to generated data and PDFs.

## Usage discipline and evidential scope

- Read the focused source list and current progress first, while following
  the repository's required instructions and indexes. Reuse recorded work.
- Astra should supply enough mathematics that Sol need not rediscover the
  objective. Sol should return a short decision summary plus evidence links
  so Astra need not repeat the numerical run to understand it.
- Before dispatch, give a finite work budget and stop condition. Do not
  automatically increase heights, sample counts, precision or refinement
  rounds. Sol can adapt within the specified limits; a scope/budget increase
  returns for a revised analytical request.
- Keep the author's selected effort unless they choose another. Record
  the actual setting, and mark unavailable metadata as unknown. A requested
  model label is not proof of which model executed a turn. If the active
  model does not match the role, prepare the handoff rather than doing that
  role's research under an incorrect label.
- Record runtime and model usage when actually available. Do not infer
  account savings from the role assignment. Avoid
  reruns solely to produce a nicer table or to keep the other chat busy.
- Floating observations remain diagnostics. Exact or interval computations
  need their stated coverage and full error accounting. An unbounded-height
  conclusion still needs an analytical argument covering the unsampled range.
  Different models sharing inputs do not constitute independent specialist
  review, and a Sol numerical report alone does not fulfill HDA-20.

Read the [result index](result-summaries/README.md) and
[avoid index](avoid/README.md), especially
[numerics before a question](avoid/10_numerics_ahead_of_the_question.md),
[shared-premise reviews](avoid/05_same_model_reviews_and_shared_premises.md),
[parallel writers](avoid/17_parallel_writers_and_broken_registries.md)
and [evidence/status](avoid/06_status_stronger_than_the_evidence.md).

## Prompts for the author to carry between chats

Replace the packet placeholder with the actual absolute path and revision.
These templates do not dispatch anything or change the selected model.

**To the Sol chat:**

> Follow `/Users/ebbaker/Documents/shifted-zeta-positivity/GPT_RESEARCH_MODEL_WORKFLOW.md`.
> Read `[absolute packet path, revision]` and its current progress entry.
> Execute only the specified numerical request using GPT-6.1 Sol, within its
> budget and stop rules. Save the code and records, append the Sol return,
> and hand it back to Astra. Keep analytical changes as questions for Astra.

**Back to the Astra chat:**

> Follow `/Users/ebbaker/Documents/shifted-zeta-positivity/GPT_RESEARCH_MODEL_WORKFLOW.md`.
> Review Sol's return in `[absolute packet path, revision]` using GPT-6 Astra.
> Decide what it establishes for the analytical goal, update the research
> notes and progress, and continue the analysis. Prepare another bounded
> request only if a specific analytical need remains; do not rerun numerics.

For model selection, the desktop app's model/effort control is beneath the
composer; the actual options depend on the account and client. See the
[official OpenAI model guidance](https://learn.chatgpt.com/docs/models),
checked 24 October 2026.

## Current adoption

The [heat-density progress register](papers/investigations-5/01_heat_density_asymptotics/research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
holds the current owner and next action. Its analytical infinite-height
priority remains in force. This workflow creates no numerical assignment
by itself and changes no research result or completion status.
