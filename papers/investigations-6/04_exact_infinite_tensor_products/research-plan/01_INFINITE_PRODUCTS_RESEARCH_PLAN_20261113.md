# Exact infinite tensor products — research plan

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are unavailable in the current shared chat's recorded configurations.
Recommended models below do not identify the authoring model or select
Edward Baker's actual model, effort or activation order.

**Continuation authorized; research not started by this update.** The
[ITP progress file](../research-progress/01_INFINITE_PRODUCTS_RESEARCH_PROGRESS_20261113.md)
is the sole current register for this branch. This plan follows
[INVESTIGATION_SETUP_WORKFLOW](../../../../INVESTIGATION_SETUP_WORKFLOW.md)
and the [model/task workflow](../../../../GPT_RESEARCH_MODEL_WORKFLOW.md).
The [overview](../research-overview/01_INFINITE_PRODUCTS_RESEARCH_OVERVIEW_20261113.md)
holds scientific background; the [parent plan](../../research-overview/02_TENSOR_NETWORK_RESEARCH_PLAN_20261113.md)
and [TN6 register](../../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
own shared interfaces, not ITP status. ITP-B01 does not depend on TN6-B01
or a sibling's conceptual opening.

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

## Fixed inputs and evidence boundary

Preserve the complete [GNP source](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex):

\[
 W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du,
 \qquad H_0(z)=\xi(1/2-iz/2)/8.
\]

Initially \(0\le\lambda\le1/2\), \(\tau=1/2-\lambda\),
\(z=x+iy\). Real Newman height \(x\) is twice zeta height.
Height, imaginary time and resolution are separate parameters; a future
estimate must specify their domain and which limits are uniform.

The inherited [Brainstorm 02 §§5–6, equations (9)–(10)](../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
provides, on \([a,a+\ell]\), the binary phase product

\[
 e^{ixu}=e^{ixa}\prod_{k\ge1}e^{ix\ell2^{-k}n_k},\qquad
 \|e^{ix\ell2^{-k}n_k}-I\|\le |x|\ell2^{-k}.
\]

For strictly positive \(C^1\) amplitude \(f\), dyadic averages \(f_k\)
give \(R_k=f_k/f_{k-1}\) and

\[
 f=f_0\prod_{k\ge1}R_k,\qquad
 \|R_k-I\|\le\frac{\ell\|f'\|_\infty}{\min f}\,2^{1-k}.
\]

Finite products telescope; the local product converges uniformly. Its
gates act on growing bit prefixes. Complete-line recovery is an absolutely
convergent sum of compact-interval readouts, not an asserted single global
operator-norm product with a uniform lower floor. Applying the construction
to \(W_{1/2-\tau}\) preserves the original flow and literal readout.

These are **exact representation identities** from an **open conceptual
brainstorm**, with a [same-assistant analytical check](../../../investigations-5/brainstorm/reviews/02_EXACT_HEIGHT_SELF_CHECK_20261113.md).
They supply no uniform all-height estimate, computational advantage,
bounded-rank rule or signed Green bound. The [reference-use guide](../references/README.md)
links the canonical catalog and finite quantics context; this planning
pass makes no new theorem import, article inspection or PDF retrieval.

Read the [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md),
[classification 01](../../../../avoid/01_restating_the_target.md),
[controls 12](../../../../result-summaries/12_collision_controls_and_screening.md),
[control-premise rule 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate caution 03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The products are representations. A future recursive or quantitative
estimate is a candidate intermediate milestone, measured by its actual
bound and consumer. Any RH-equivalent reformulation is identified once;
surrogate checks do not turn it into acquired progress.

## ITP-B01 — Choose a recursive architecture and first useful estimate

**B; recommended GPT-6 Astra.** The unresolved conceptual choices are the
architecture, convergence topology and first consequence beyond an exact
list of source-dependent factors. **Ready and authorized for continuation; not started.**
Inputs are the overview, inherited equations above and their self-check,
[source crosswalk](../../notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md),
reference guide, parent plan and control screen. No theta rank law, global
compact minimum or signed-readout invariant is assumed.

**Bounded scope:** one conceptual round, comparing the inherited
phase/source-ratio architecture with at most two justified alternatives.
Choose one first question, one parameter regime and one observation norm.
The question may concern a recursive core rule, a controlled limiting
contraction, or a transfer estimate; these are alternatives, not three
compulsory projects. Compare with at most one matched baseline. No numerical
campaign or new investigation is included.

**Deliverable:** one decision in `brainstorm/notes/`, explaining why the
selected architecture can expose information beyond existence, or why
the tested alternatives should be parked at their stated scope. Specify
compact versus full-line assembly; bounded versus growing real/complex
height; imaginary-time range; factor support; and the exact observation
that will consume the estimate. Preserve the full source and Fourier
factor even if a finite truncation is used.

If tractable, freeze `research-progress/handoffs/ITP-E01-r1.md` with exact
input versions, source/generator, product ordering, topology, domain,
readout map, proof route, quantitative acceptance test and finite limits.
State all source-tail, product-tail, normalization, cancellation and
arithmetic payments relevant to that consumer. Any permitted computation
needs finite cases and precision/refinement limits. If the contract or a
necessary input remains open, list it and leave E01 reserved; no executable
packet is manufactured around an undecided success test.

**Evidence and completion:** a usable fixed contract for one informative
estimate, or a justified scoped stop. Repeating telescoping, claiming
that factors approach identity, or observing invertibility is insufficient
for a signed-field conclusion. A useful negative comparison is allowed;
it names the tested architecture, norm and parameter class.

**Routine choices and escalation:** compatible tensor gauges, notation,
equivalent algebra and interval partitions may be compared inside this
round. A changed physical source, literal readout or scientific consumer,
an unexplained switch of topology, or a missing conceptual arithmetic
input requires a dated B01 scope decision. Do not silently pass that
choice to E01. Record the decision and begin the declared E task on
Sol 6.1 / Ultra when its contract is ready, under the standing authorization.

## ITP-E01 — Derive the frozen recursion, convergence or transfer bound

**E; recommended GPT-6.1 Sol.** Once the architecture, norm, domain and
method are fixed, this is a specified derivation and error-accounting
task. **Reserved; not ready.** Dependencies are a completed ITP-B01
decision and issued E01 request with all required source inputs available.
No such request exists at setup.

**Deliverable:** a `notes/` return deriving the requested recursion or
bound, including constants, hypotheses, quantifiers and full readout
transfer, or identifying the precise failed allowance. Necessary small
execution records belong in `numerics/` only when the frozen request
permits them. Proof, floating diagnostic and interval certificate remain
distinct evidence labels.

**Finite limit:** one frozen request, one architecture/domain/consumer,
one derivation and at most one correction pass. Routine algebra, tensor
gauge changes preserving the observation, and standard estimates with
checked hypotheses are permitted. Do not enlarge the height range,
replace the source, change topology or launch a scan. Such changes or an
unresolved conceptual premise return to ITP-B01.

**Completion:** meet the request's actual quantitative acceptance test,
or show why its prescribed method cannot establish it. Keep growing
factor support and constants visible. Compact convergence does not imply
uniform all-height convergence; a compact \(\min f\) does not furnish a
global floor. A failed upper allowance is not a lower bound on true error.
An exact core identity without the requested consequence retains that
limitation; the failure excludes only the tested estimating class.

## ITP-E02 — Assess the stated E01 result

**E; recommended GPT-6.1 Sol.** A fixed analytical assessment rather than
architecture selection. **Reserved; not ready.** Depend on the unchanged
E01 request, its completed return and exact source versions.

**Deliverable/evidence:** one `reviews/` report accepting, accepting with
limitations, or rejecting the stated result. Check ordering, norm/topology,
parameter uniformity, compact-to-full-line passage, support/rank claims,
literal readout and complete costs. Check the actual control-premise
comparison and whether the numerical/analytic consequence matches the
claimed milestone. Record reviewer/model/effort and shared-premise scope;
a different model is not independent specialist review.

**Limit and completion:** one assessment and, when authorized, one response
check. Routine algebra and source verification are permitted. Completion
requires an explicit disposition and any remaining premise. Routine
corrections stay in E01's frozen scope; a replacement architecture,
consumer, topology or new mathematical input returns to ITP-B01. No new
theorem campaign or numerical benchmark is included.

## Controls, ownership and stop boundary

The inherited [Brainstorm 02 §8 screen](../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
and parent plan §6 identify each catalog family's missing premise. Smooth
reflected and positive-primitive colliding sources admit local refinement
products but fail canonical integer-square arithmetic or the unchanged
complete source. Atomic controls lack a positive \(C^1\) density yet
separately test generic exact-network arguments. Altered-readout controls
fail the literal Fourier/Newman observation. These distinctions do not
prove that a new quantitative inequality fails for those controls.

Before proposing an estimate, apply the actual witnesses from controls 12,
record shared premises and the specific inequality or premise each fails,
and retain domain/regularity qualifications. A finite certificate need
reject a control only where its event or witness contradicts the claim.
“Not theta” alone is not a quantitative rejection. This setup introduces
no new estimate and reruns no control certificate.

Finite QTT accuracy comparisons stay with branch 01; height-chain evolution
and coefficient dynamics stay with branches 02–03. ITP can supply a stated
truncation or transfer input to those branches without taking their task
status. Shared composition is owned by TN6. The old overview-only deferral
is superseded by this plan and sole ITP register; no existing task, issued
request or completed identity is replaced or upgraded.

The plan may stop after one useful result, one scoped failed route or its
assessment. It commits to no manuscript, all-height theorem or additional
campaign. Follow [REFERENCE_WORKFLOW](../../../../REFERENCE_WORKFLOW.md)
at point of use and [LARGE_FILES](../../../../LARGE_FILES.md) for storage.
Use the [canonical continuation and branch prompt](../../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md).
New branch-only chats use this branch's [history folder](../chat-histories/README.md);
existing shared chats retain their unique parent registration.
