# Continue with setup of the cluster gap-transport investigation

16 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, parent chat0004. Actual model and
reasoning effort are unavailable in the recorded configuration. This is
a dated setup handoff, not a live research progress register.

Edward requested three route-specific READMEs and research overviews,
deferring plans and progress files until the routes are started. He chose
**cluster gap transport** first. Its [README](../README.md) and
[overview](../research-overview/01_VCD_GT_RESEARCH_OVERVIEW_20261116.md) now
exist. The default next action is to create this branch's research plan
and sole progress register; the prompt below authorizes that setup when
invoked. It does not activate a proof or numerical campaign.

| Next item | Type | Recommended model and reason | Readiness/dependencies | Expected output |
| --- | --- | --- | --- | --- |
| VCD-GT-E00: individual research setup | E — execution | GPT-6.1 Sol; the route, documents and setup scope are specified | Ready when this continuation is invoked; read the overview and inherited sources below | A bounded research plan, sole VCD-GT progress register, ownership crosswalk and next-task continuation |
| First source-estimate decision, proposed VCD-GT-B01 | B — brainstorm | GPT-6 Astra; identifying a useful signed canonical estimate is an unresolved mathematical choice | To be specified by E00, not activated by this note | A concrete estimate/proof contract or a scoped failed mechanism |

These are recommendations under the author's
[research-model workflow](../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md),
not actual model settings or permission to switch models or dispatch
agents. Edward chooses model and effort. Subsequent fixed derivation and
assessment tasks should be classified separately after their inputs and
completion tests are known.

## Current mathematical position

The [parent discussion28 §2](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md)
derives the exact pair equation D'=2+4KD and the integrating-factor
identity

\[
W(u)D(u)=D(v)-2\int_u^v W(t)\,dt,\qquad
W(t)=\exp\left(4\int_t^v K(s)\,ds\right).
\]

D is the squared half-separation of two actual F zeros; K is the divided
difference of the logarithmic derivative of the zero-free factor after
that pair is removed. Both remain regular through a double event. The
identity is local calculus with same-assistant checking. The unproved
input is a useful canonical comparison of the incoming gap with the
complete signed cost. Small approximation error or bounded K alone does
not provide it.

The exact quadratic collision has K=0 and spends its whole gap at the
event. The existing canonical two-root pilot already found that an
absolute model-unit curvature bound could dominate an otherwise tiny
approximation error. The new information regime of interest permits a
certified outer cluster while separate real-root cells or slope floors
are unavailable. This distinction must survive planning; it is not a
claim that a better signed estimate exists.

## Read before writing the plan

Use the [result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and [approximation18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
together with the [avoid index](../../../../../avoid/README.md), especially
[01](../../../../../avoid/01_restating_the_target.md),
[02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md),
[14](../../../../../avoid/14_convenience_hypotheses_and_circular_definitions.md),
and [15](../../../../../avoid/15_ignoring_sibling_results_and_unfinished_closures.md).

The mathematical reading order is:

1. [Branch overview](../research-overview/01_VCD_GT_RESEARCH_OVERVIEW_20261116.md) and [discussion28](../../notes/28_VCD_COLLISION_CONTROL_ROUTE_DISCUSSION_20261116.md), including its control screen.
2. [Manuscript cluster section](../../manuscript/sections/cluster_resolution.tex), Propositions 10.4–10.6, and [note27](../../notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md).
3. [Synthesis23](../../notes/23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md) and its linked signed-error notes, preserving their degree/height domains and coefficient costs.
4. Rodgers–Tao branch [note02 §§3–7](../../../../investigations-5/02_heat_flow_rh_applications/rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md) and [note03 §§4–6](../../../../investigations-5/02_heat_flow_rh_applications/rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md): inherited transfer, exact collision control, certified pilot and its scoped stop.
5. The [parent live register](../../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md), for ownership and current source statuses, and [reference catalog](../../references/README.md) with [bibliography](../../references/induction.bib).

The branch has no plan or progress file yet. At startup, inspect for
files created since this handoff and continue them if present. Otherwise
create dated files under `research-plan/` and `research-progress/`, naming
the latter the sole VCD-GT register. Do not create a second live ledger
or reassign parent B07/E25 implicitly. The degree-contraction and
multiscale siblings remain at overview-only setup until individually
started.

## Self-contained continuation prompt

```text
Begin the individual research setup for the first VCD collision route:
papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/.
Edward selected this approach first. Complete VCD-GT-E00 (E: fixed setup;
recommended GPT-6.1 Sol), using the selected model/effort without claiming
unavailable settings. This request creates the research plan and sole
progress register; it does not execute the ensuing research tasks.

Read AGENTS.md, INVESTIGATION_SETUP_WORKFLOW.md, GPT_RESEARCH_MODEL_WORKFLOW.md,
REFERENCE_WORKFLOW.md, LARGE_FILES.md and tools/CHAT_HISTORY.md. Read root
result-summaries/README.md and avoid/README.md, specifically result clusters
12/13/18 and avoid patterns 01/02/07/12/14/15. Read the branch README and
research-overview/01_VCD_GT_RESEARCH_OVERVIEW_20261116.md, parent notes27/28,
the parent manuscript's sections/cluster_resolution.tex, synthesis23 and
its signed-error sources, and the current parent progress register02.
Reuse the Rodgers–Tao branch notes02/03 cited in the overview and the
parent reference catalog; preserve their hypotheses and review scope.

Keep the complete W_lambda=exp(lambda*u²)Phi, normalized Fourier field F,
and canonical readout G_(N,lambda)=(exp(iz J_N(lambda)))_00. N controls
approximation; lambda is physical heat time. The initial setting is one
isolated two-zero cluster with a paid outer contour count, boundary margin
and buffer on a specified compact time interval. Its symmetric coordinate
D=((z1-z2)/2)² obeys D'=2+4KD. The required input is a useful bound for
the signed interaction cost relative to an independently acquired incoming
gap. Do not replace this with source-node interlacing, a Jensen route,
finite-stage reality, assumed nonvanishing root slopes, or an exact heat
equation for G_N.

Inspect the destination first. Create or continue one dated research plan
and one sole VCD-GT progress register, with a crosswalk to inherited parent
results. Parent VCD-B07/E25 and issued packets keep their existing status
unless Edward separately directs a transfer. Record E00 as setup, not as
a mathematical gain. Reserve a bounded B decision for the missing signed
estimate and separate E tasks for any fixed derivation or assessment after
its route is specified. Give each proposed task its type, model recommendation
and reason, dependencies, actual inputs, deliverable, evidence standard,
finite scope, completion condition and conceptual stop/return condition.
Do not turn an unproved source estimate into a ready execution premise.

The initial B question should compare at most two concrete ways to use
canonical information in the signed gap budget. State which data are
available, which would have to be acquired, and how a conclusion would
improve an equally informed direct comparison. Preserve all outer-contour
and coordinate-error payments. Explain why the older absolute-curvature
pilot is not simply being repeated. A scoped failure of the selected
information class is a valid outcome; an additional representation alone
is not the intended gain. Do not resolve or execute this B question as
part of the current setup task.

Carry the analytical collision-control screen and identify the premise
each control actually fails. The exact quadratic model must exhaust its
gap budget at the event. Positive-source controls must not be dismissed
merely for being noncanonical. A missing exact theta identity is not
evidence that a proposed inequality fails on a control. Preserve the
distinction between a local event and a finite all-real threshold, and
between reality and endpoint simplicity. Larger clusters, high-height
coverage, contour changes and completion of the time descent remain
explicit separate obligations.

Finish with the plan, sole register, concise branch DRAFT_HISTORY entry,
and an updated continuation identifying the next classified task and its
readiness. Add only useful working-directory/reference/history pointers
needed for startup. Link canonical article records and bibliography; record
newly inspected passages immediately if any are actually needed. Preserve
the present dated handoff and the existing mathematical evidence. Check
links, ownership, source statuses and file sizes. This setup requires no
numerical run, new manuscript, PDF, chat creation or subagent dispatch.

Refresh a registered research chat at turn start and end. A new branch-only
chat belongs in this branch's chat-histories/ and must use its actual id,
title and source; an already registered chat retains its current home.
Use tools/refresh_chat_history.py with the shared lock and integrity checks.
Arrange the actual-current-turn --after-turn --defer capture as the last
tool action before the final reply unless a trusted hook is verified.
Never reuse the old chat0004 turn id or prewrite a planned final answer.
```

## Completion boundary and files

The setup is complete when the plan and sole register make the first
unresolved research decision executable as a bounded conceptual task,
with genuine prerequisites and scoped outcomes. It need not solve that
decision. Continue routine document work without renewed permission.
Future analytical notes belong in `notes/`, assessments in `reviews/`,
and supporting computation records in `numerics/`. The root
[large-file guidance](../../../../../LARGE_FILES.md) and
[reference workflow](../../../../../REFERENCE_WORKFLOW.md) apply; no
working manuscript snapshot or generated PDF belongs in these folders.
