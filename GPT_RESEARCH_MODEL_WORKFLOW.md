# GPT research workflow: Sol by default, Astra for exceptional difficulty

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Original guidance: gpt-6-astra, effort max.
Revised at the author's request in chat 0010: **gpt-6-astra (Codex), actual
effort xhigh**, verified from session metadata.

This is the canonical GPT model guidance for this repository. The author's
latest instruction is: “You can be more aggressive with the handoffs to
Sol. Please only reserve extra high difficulty tasks for Astra.” This
supersedes the earlier rule assigning every analytical task to Astra.
Claude's responsibilities remain governed by the author's separate assignments.

## Standing division of work

| Owner | Responsibility |
| --- | --- |
| **GPT-6.1 Sol (`gpt-6.1-sol`) — default** | Routine and moderately difficult research, analytical derivations, proof completion within established methods, error accounting, interpretation, reviews, manuscript work, and all numerical implementation/execution. Sol may formulate bounded questions, derive missing routine formulas, run diagnostics and certificates, and assess what the evidence establishes. |
| **GPT-6 Astra (`gpt-6-astra`) — exceptional difficulty** | Extra high difficulty analytical bottlenecks: genuinely new proof mechanisms, difficult uniform or singular estimates, unresolved structural compatibility, and analytical problems that remain resistant after a focused Sol attempt. State the specific difficulty when recommending Astra. |
| **Edward Baker** | Maintains the chats, chooses actual models and effort, and carries handoffs between chats. |

Default to Sol when uncertain about task difficulty. A task being analytical,
unfinished, important, or attached to an infinite-range theorem does not by
itself justify Astra. Astra should hand off as soon as the next tractable
subproblem is clear. Do not wait for an entire global proof or a fully
polished theorem before giving Sol a useful bounded analytical or numerical
assignment. Sol can complete routine missing specifications in that assignment.

Keep all numerical coding, execution, debugging, reruns, machine-symbolic
checks and exact-arithmetic verification with Sol. Astra may inspect the
code and evidence, derive difficult analytic inputs and prepare handoffs.
Ordinary file edits, hashes, manuscript production and chat capture are
housekeeping available to either model. The user-selected effort remains
unchanged; “extra high difficulty” is a routing criterion, not an instruction
to change an effort setting.

Sol may correct routine formulas and resolve routine analytical ambiguities.
Document the correction and its effect on dependent results. Preserve the
physical source, normalization, regulator and intended target. If a change
to a frozen mathematical contract is needed, record a new packet revision
before applying it; never silently reinterpret old results. Escalate a
specific hard bottleneck to Astra with the attempted route, evidence and
unpaid term. A numerical failure or counterexample must always be retained.

This remains a manual workflow. It does not authorize creating chats,
dispatching agents, sending messages between chats, scheduling research or
changing models. Existing [chat capture](tools/CHAT_HISTORY.md) continues.
Historical assignments, results and model attribution remain historical;
apply this revised division to new work rather than rewriting old records.

## End-of-chat recommendation

At the end of each research reply, name the next concrete deliverable and
owner: **Analysis — Sol**, **Numerics — Sol**, **Analysis and numerics — Sol**,
or **Analytical — Astra**. Explain briefly what decision it advances.
Recommend Astra only when you can identify the extra high difficulty.
If no further task is warranted, say so rather than inventing work.

For a Sol handoff, link the bounded packet and give a short pasteable prompt.
The packet may ask Sol to finish routine analysis before computation. A
numerical run still needs a named question, finite scope and stop rule;
Sol can supply these within an authorized exploratory-analysis assignment.
A completed Sol task does not automatically need another Astra turn.
Sol may record its disposition and continue routine follow-through or close
the packet. Use Astra review when the unresolved difficulty warrants it,
or when the author specifically requests it. Model changes do not supply
independent specialist review.

## Handoff cycle

1. **Scope and route.** Read the live ledger; state the gain, evidence,
   next bounded subproblem and any missing input. Use `ANALYSIS_READY`
   or `ANALYSIS` while developing an analytical assignment. Sol is the
   default owner; explain an exceptional Astra assignment.
2. **Prepare a bounded handoff.** Complete one request packet, link its
   revision and next owner in the existing progress register, and mark
   `READY_FOR_SOL` (or `READY_FOR_ASTRA` for a difficult escalation).
   Supply enough context to start; explicitly delegate routine derivations
   instead of blocking on their absence.
3. **Execute.** Re-read the exact request revision and live entry. Record
   actual model/effort. Use `ANALYSIS` for analytical work and `NUMERICS`
   for computation. Preserve failed attempts, input versions, finite work
   limits and stop conditions. Append the return with evidence paths.
4. **Disposition and continuation.** Sol may assess routine results and
   close them with a recorded disposition, or prepare the next bounded
   Sol task. Use `ANALYTIC_REVIEW` during review, and `CLOSED` only after
   the evidence and remaining limits are recorded. Escalate to
   `READY_FOR_ASTRA` only with a specific hard question or at the author's
   request. Astra hands routine follow-through back to Sol promptly.

Handoff phases are separate from Complete, Partial, Ready or Gated research
statuses. A failed computation can be a completed bounded task without
completing its parent theorem. Each shared artifact has one current writer;
re-read before editing and preserve other chats' updates.

## One compact packet in the existing progress register

Use the affiliated investigation's `research-progress/handoffs/` directory.
Use a parent task ID and sequence; `-A01` can identify analytical work,
`-N01` numerical work, and `-AN01` mixed work. Keep the existing progress
file as the sole ledger. Do not create a new ledger or duplicate research
history. A small, actionable packet is preferable to delaying delegation.

```text
ID / parent task / request revision / date:
Request author and actual model/effort:
Next owner and reason for routing:
Current phase (the progress register owns live status):
Read first / input versions / files this packet may write:

REQUEST
Concrete analytical or numerical question and how outcomes affect the decision:
Established formulas, conventions, domain, regulator, norms and source:
Routine derivations or choices explicitly delegated to Sol:
Outputs, evidence standard and acceptance conditions:
For computation: finite cases, error categories, precision and work limits:
Stop conditions, unbounded remainder and genuinely hard escalation triggers:
Existing work to reuse; output locations:

RETURN
Actual model/effort, date, thread ID, revision and input versions:
Result and failed cases; proof, code and small execution-record paths:
Errors, limitations, reproduction details and actual work/runtime if available:
Corrections, deviations and unresolved analytical questions:

DISPOSITION — named owner
Exact evidence reviewed; accepted input, diagnostic, scoped failure or open:
What changes in the argument and what does not follow:
Research-task status, next deliverable and justified next owner:
```

Freeze a handed-off revision. Append returns rather than overwriting the
request or prior evidence. Record a new revision for a changed contract;
check changed input files before reusing a result. Save mathematics in
`notes/`, code and small execution records in `numerics/`, and assessments
in `reviews/`. Follow [LARGE_FILES.md](LARGE_FILES.md).

## Evidence and work limits

Read the [result index](result-summaries/README.md) and
[avoid index](avoid/README.md), especially
[numerics before a question](avoid/10_numerics_ahead_of_the_question.md),
[shared-premise review](avoid/05_same_model_reviews_and_shared_premises.md),
[parallel writers](avoid/17_parallel_writers_and_broken_registries.md) and
[status](avoid/06_status_stronger_than_the_evidence.md).

A bounded diagnostic is useful before certification when it chooses a
method, exposes a failed budget or tests an explicit assumption. Do not
require the final global error theorem before such a diagnostic. Label
samples as samples; interval/exact claims need their actual coverage and
separate source, arithmetic, integration and remainder payments. Sol may
choose refinements within the request's finite limits. A scope/budget
increase needs a revised request with its reason, not automatic expansion.

Record actual model and effort from available metadata; do not infer them
from a requested label or claim savings without usage evidence. If a task
falls outside the active model's assigned role, prepare the appropriate
handoff. Preserve the author's selected settings. No routine Sol proof or
interpretation requires Astra approval solely because it is analytical.

## Prompts for the author

**To Sol:**

> Follow `/Users/ebbaker/Documents/shifted-zeta-positivity/GPT_RESEARCH_MODEL_WORKFLOW.md`.
> Continue `[absolute packet path, revision]` and its live progress entry.
> Complete the delegated analysis and/or computation within its limits,
> save evidence and disposition, and update progress and chat history.
> Escalate only a specifically identified extra high difficulty bottleneck.

**To Astra when warranted:**

> Follow `/Users/ebbaker/Documents/shifted-zeta-positivity/GPT_RESEARCH_MODEL_WORKFLOW.md`.
> Resolve the difficult analytical bottleneck in `[packet path, revision]`,
> using Sol's return and failed attempts. Save the proof or precise failed
> route, then hand tractable follow-through back to Sol.

The [heat-density progress register](papers/investigations-5/01_heat_density_asymptotics/research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md)
owns its live assignments. This policy revision changes routing, not the
truth or completion status of any mathematical result.
