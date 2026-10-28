# GPT research workflow with tasks classified before execution

28 October 2026, America/New_York. Revised for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**, Investigation05 chat0008. The original 24 October guidance and its Sol-first revision were prepared with gpt-6-astra, at the recorded efforts max and xhigh respectively.

This is the canonical GPT research-model guidance for the repository. Edward Baker now asks that upcoming work be divided into conceptual tasks and straightforward execution **when the research plan is written**, so he can choose Astra or Sol before starting. The current model must not keep ownership merely because it has the context. This supersedes routing decided only after a research session. Straightforward analytical work remains suitable for Sol.

## Two task types

| Shorthand | Meaning | Default recommendation |
| --- | --- | --- |
| **B — brainstorm** | A consequential conceptual choice remains: selecting or changing a mechanism, equation, observable, proof strategy, or research direction; resolving a difficult structural bottleneck. The output is a mathematical decision, argument, or a usable contract for further work. | **Astra** for these open or difficult decisions; state the actual conceptual difficulty. A bounded, modest comparison can be explicitly assigned to Sol before it starts. |
| **E — execution** | The objective, mathematical route, inputs and completion test are specified. Includes routine analytical derivations, algebra, implementing a fixed formula, bounded numerics, debugging, error accounting, checking a stated proof, and integrating accepted results. | **Sol**. A task does not become B merely because it contains a proof, analysis, or careful verification. |
| **Author decision** | Selecting the actual model, effort and chat, or overriding a recommendation. | **Edward Baker**. Record an override without changing what the task type means. |

Use the available GPT-6 Astra and GPT-6.1 Sol choices for these recommendations. The labels describe the work; they are not a claim that either model is incapable of the other type. A mixed task should normally become a B decision followed by a separately identified E task, with its dependency recorded. Do not label an unresolved design choice E just because it ends in a computation.

OpenAI's [model-selection guidance](https://learn.chatgpt.com/docs/model-selection), consulted 28 October 2026, describes Astra for ambiguous and deep analytical work and Sol for complex work with time and cost constraints. The B/E split here is the author's research policy, not an official product taxonomy or a measured savings claim. Preserve the user-selected effort; this policy does not change model settings.

## Classify before work starts

Every active research task in an overview or progress register must state:

- stable task ID and **B** or **E** type;
- recommended model and a task-specific reason;
- readiness and dependencies;
- concrete deliverable, evidence standard and completion condition;
- finite scope or work limit, and the event requiring a return to conceptual work.

Record this before the first substantive research action. If a task arrives unclassified, classify it at the start from its requirements, rather than postponing that decision until after the work. Routine inspection needed to understand the task is allowed.

An E task may resolve ordinary implementation choices, fix a normalization slip, complete a standard estimate or refine within its declared limits. It may not silently change the physical source, invariant, observable, equation, mathematical target or evidence standard. If such a change is needed, retain the current evidence, identify the affected dependency, and create or update a B task before continuing that dependent work. Continue unaffected work within the existing E scope.

Reclassification requires a dated reason tied to new evidence: what conceptual choice appeared or what has now been settled. Keep the original task identity and prior results. Do not increase difficulty merely because the current model is Astra, or call a speculative problem routine because the current model is Sol.

## Prevent model inertia at task boundaries

Once a B task supplies a tractable contract, list its E follow-through and recommend Sol immediately. Do not keep numerical coding, debugging, routine derivations or manuscript production attached to the B task to preserve the current model's ownership. Numerical implementation and execution are assigned to Sol; ordinary document edits, hashes and chat capture remain housekeeping available to either model.

Once an E task meets its completion condition, record its result and stop at that boundary. An unfavorable measurement or a precise failed bound can complete an E task. It does not authorize a wider scan, a new PDE, a revised observable or a larger campaign. Follow a previously declared E dependency when authorized, or identify the B decision needed next.

Sol may close an E task and assess its routine evidence without mandatory Astra approval. A numerical discrepancy first gets bounded implementation diagnosis within the packet; an unresolved mathematical premise is a B escalation. A model change is not independent specialist review.

## Continuation notes and final recommendations

Put a small routing table near the start of every continuation note:

| Next task | Type | Recommended model | Ready or dependency | Expected output |
| --- | --- | --- | --- | --- |
| Named bounded task | E — execution | Sol | Ready | Concrete measured or calculated return |
| Named conceptual decision | B — brainstorm | Astra, with reason | Ready or named input | Decision, proof route or frozen contract |

Select one default next task when the priority is clear. Label alternatives explicitly. Explain the next unresolved decision, not merely that more research is needed. Link the existing task specification or a bounded packet and give a short pasteable prompt.

At the end of a research reply use, when further work is warranted, **Next: [B] TASK — Astra** or **Next: [E] TASK — Sol**, with the deliverable. Use the classification already recorded in the plan. Do not invent an additional task to justify keeping the session active, and do not silently reroute based on the current model. If no further work is warranted, say so.

This is a manual workflow. It does not authorize creating chats, dispatching agents, messaging other chats, scheduling research or changing models. Edward Baker chooses when and where to continue. Claude's responsibilities remain governed by the author's separate assignments. Existing [chat capture](tools/CHAT_HISTORY.md) continues.

## One live register and a bounded request

The affiliated investigation's progress file owns live task status. Use its research-progress/handoffs directory when a separate execution packet helps. Do not create competing live ledgers. If the author explicitly requests a new progress file, designate it as the sole current register, mark the previous one historical, and include a task crosswalk instead of duplicating its ongoing status.

Use stable B/E task IDs in new programs. Existing analytical/numerical IDs need not be renamed: add Type and Recommended model fields. Research status and work type are separate: B is not a status, and Ready does not mean proved.

Existing handoff phases such as ANALYSIS, NUMERICS, READY_FOR_SOL and ANALYTIC_REVIEW may be retained alongside the new type field; B/E does not overwrite their meaning. Each shared artifact has one current writer. Re-read the live entry before editing and preserve other chats’ updates and historical assignments.

A compact packet records:

    ID, parent, request revision, date, author and actual model/effort
    Type: B or E; recommended model; reason
    Live progress entry and prerequisite versions
    Question and how each possible outcome affects the next decision
    Fixed source, equations, normalization, domain and observation
    Routine choices explicitly permitted
    Outputs, acceptance condition and evidence standard
    Finite cases, precision/refinement/work limits when applicable
    Stop rule and named B escalation trigger
    Files permitted to change; prior work to reuse

    Return: actual model/effort, date, revision and input versions
    Result, failed cases, proof/code/record paths and actual errors
    Corrections, deviations and unresolved premises
    Disposition: status, consequence, next declared task/type/model

Freeze an issued request revision. Append the return or link a separate return; do not overwrite its request or failed evidence. Revise the request explicitly when its mathematical contract changes. Mathematical notes belong in notes, code and small records in numerics, and assessments in reviews. Follow [LARGE_FILES.md](LARGE_FILES.md).

## Evidence and cost discipline

Read the [result index](result-summaries/README.md) and [avoid index](avoid/README.md), especially [numerics before a question](avoid/10_numerics_ahead_of_the_question.md), [tests of what is already known](avoid/11_certifying_the_known_and_tests_that_cannot_fail.md), [shared-premise review](avoid/05_same_model_reviews_and_shared_premises.md), [parallel writers](avoid/17_parallel_writers_and_broken_registries.md), and [status](avoid/06_status_stronger_than_the_evidence.md).

A bounded diagnostic can measure feasibility, constants or a failed allowance before certification. It needs a predeclared question, finite cases and stop rule. Routine adaptive choices may be delegated inside those bounds. Selecting a new scientific question or changing direction belongs in B and must be visible before the dependent execution.

Record actual model and effort from available session metadata; do not infer them from the recommended model or requested label. Keep floating samples, exact checks, interval certificates and universal proofs distinct. Record the actual source, arithmetic, quadrature and tail payments. Report measured runtime or usage only when available; a routing preference does not establish a numerical saving.

The current investigation's [conservative-flow progress register](papers/investigations-5/05_radial_theta_collision_geometry/research-progress/04_CONSERVATIVE_THETA_FLOW_RESEARCH_PROGRESS_20261028.md) is an initial application. Other investigations retain their current mathematical statuses and history; apply the classification to their next planned tasks.

## Short prompts for the author

**Execution:**

> Read the root GPT_RESEARCH_MODEL_WORKFLOW.md and the current progress entry for [task ID]. Complete [E] [task ID], request [revision], within its declared method and limits. Save the evidence and disposition. If a new mechanism or change of mathematical target is required, record the specific B decision instead of expanding the task.

**Brainstorm:**

> Read the root GPT_RESEARCH_MODEL_WORKFLOW.md and the current progress entry for [task ID]. Resolve [B] [task ID]'s named conceptual choice. Preserve the invariant and controls. Return a usable argument or a scoped failed route, and specify the resulting E task for Sol before numerical implementation.
