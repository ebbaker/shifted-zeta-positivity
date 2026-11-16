# Volterra coefficient dynamics — Research plan

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are unavailable in the shared chat's recorded configurations.
Recommended models below do not identify the model preparing this plan.

**Historical first-round plan; superseded as live plan on 16 November 2026.** Its tasks are
complete at their recorded scopes in the
[historical register](../research-progress/01_VOLTERRA_RESEARCH_PROGRESS_20261113.md).
The [new plan](02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PLAN_20261116.md) and
[sole live register](../research-progress/02_VCD_TAIL_CLOSURE_INDUCTION_RESEARCH_PROGRESS_20261116.md)
govern current tail-closure induction work. Readiness, stopping and
activation language in the remaining body is the original 13 November
planning record, not current status. Issued requests remain unchanged.
This notice was prepared for Edward Baker with OpenAI Codex assistance,
recorded configuration gpt-6-astra/max. The original plan follows the
[setup workflow](../../../../INVESTIGATION_SETUP_WORKFLOW.md) and
[B/E workflow](../../../../GPT_RESEARCH_MODEL_WORKFLOW.md). It implements
the subsequent request for branch plans, superseding the earlier planning
deferral without claiming that the first conceptual decision is complete.

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

## Objective, fixed objects and inherited evidence

Select and investigate one useful quantitative relation for the recurrence
coefficients of the **unchanged complete theta source**. Its intended
consumer may be fixed-chain transport, a coefficient comparison or a
specified field observation. The coefficient representation and generic
Volterra equation are the starting point; no special asymptotic law,
finite closure or signed-field estimate is assumed.

Use the [overview](../research-overview/01_VOLTERRA_RESEARCH_OVERVIEW_20261113.md)
and [complete GNP source](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex):

\[
W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du,
\qquad H_0(z)=\xi(1/2-iz/2)/8.
\]

Initially \(0\le\lambda\le1/2\), \(\tau=1/2-\lambda\), and
\(z=x+iy\). Real Newman height \(x\) is twice zeta height. Let
\(P_n(u;\lambda)\) be monic orthogonal polynomials for the unnormalized
measure \(W_\lambda(u)du\), with squared norms \(h_n(\lambda)\).
For \(n\ge1\), set \(\beta_n=h_n/h_{n-1}\), and \(\beta_0=0\).
The inherited relations are

\[
uP_n=P_{n+1}+\beta_nP_{n-1},\qquad
\partial_\lambda\beta_n=\beta_n(\beta_{n+1}-\beta_{n-1}),
\]
\[
H_\lambda(z)=\frac{Z_\lambda}{2}
\langle e_0,e^{izJ(\lambda)}e_0\rangle,
\qquad Z_\lambda=\int_{\mathbb R}W_\lambda(u)du,
\quad a_n(\lambda)=\sqrt{\beta_n(\lambda)}.
\]

[Brainstorm 02 §4, equation (8)](../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
derives the lattice law; its [same-assistant check](../../../investigations-5/brainstorm/reviews/02_EXACT_HEIGHT_SELF_CHECK_20261113.md)
checks monicity, sign and the moving/fixed-basis distinction. The
[reference guide](../references/README.md) retains Van Assche §2.3,
Theorem 2.4 and its symmetric specialization as the classical precedent.
This is reuse of inherited passage-level inspection, not fresh reading or
independent review. Reversing to \(\tau\) reverses the coefficient-flow
sign. Differentiating moving-basis states requires connection terms;
\(J(\lambda)\) cannot replace branch 02's fixed \(J(1/2)\) silently.

Read the [result index](../../../../result-summaries/README.md) and
[avoid index](../../../../avoid/README.md), especially
[classification 01](../../../../avoid/01_restating_the_target.md),
[controls 12](../../../../result-summaries/12_collision_controls_and_screening.md),
[premises 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate realizations 03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scoped exclusions 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
The formulas above are representations and a generic identity. A future
coefficient bound is a candidate intermediate estimate; it needs its
actual number/rate and consequence. An RH-equivalent reformulation is
identified once and is not supported by surrogate checks. This setup
proposes no new coefficient inequality or criterion.

## VCD-B01 — Select one theta coefficient question and consumer

**Type B; recommended GPT-6 Astra.** The unresolved choice is what
information in the full theta initial data can yield a useful coefficient
relation beyond positivity and the generic flow. The degree/time regime,
observable, comparison family and proof route remain open.

**Readiness/dependencies:** ready and authorized for continuation; not started.
Read the overview, founding note §§4 and 8, its check, reference guide,
[source crosswalk](../../notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md), and
[parent plan](../../research-overview/02_TENSOR_NETWORK_RESEARCH_PLAN_20261113.md).
No QTT, JCH or TN6 task must finish before this conceptual round. If a
chosen consumer later needs their input, name that dependency explicitly.

**Finite scope:** one conceptual round comparing at most three coefficient
questions, selecting at most one target, one \((n,\lambda)\) regime and
one consumer/baseline. Possible question classes are a quantitative growth
bound, a source-sensitive comparison or an explicit structural relation;
none is selected by this list. Distinguish finite-degree information from
uniform large-degree claims. Do not start a numerical scan or solve a
new finite closure merely to populate the plan.

**Deliverable:** save one decision in `brainstorm/notes/`, with the exact
quantity, quantifiers, unchanged source input and intended consequence,
or a scoped reason to park the compared formulations. If a tractable
derivation is specified, freeze `research-progress/handoffs/VCD-E01-r1.md`
with source versions, equations, coefficient convention, index/time and
observation domains, proof method, acceptance test, evidence standard,
permitted routine refinements and finite work limits. Identify every
unproved input. No executable packet is issued while those items are open.

**Evidence/completion:** a usable mathematical contract or a justified
scoped stop. State which theta input does work beyond the generic Volterra
law, and apply the control gate below. Re-deriving the flow or rewriting
coefficients as moment determinants is not completion by itself. A
comparison may legitimately conclude that its proposed allowance is too
weak; that is not a negative value of the actual theta coefficient.

**Routine choices/escalation:** notation, a justified coefficient
normalization with an exact conversion, and standard algebra within the
comparison are allowed. Changing the complete source, readout, target,
uniformity regime or an essential unproved arithmetic premise requires a
recorded B01 scope decision before dependent work. Record the decision
boundary, then begin E01 on Sol 6.1 / Ultra when its contract is ready,
under the standing continuation authorization.

## VCD-E01 — Derive the selected coefficient statement

**Type E; recommended GPT-6.1 Sol.** After B01 fixes its inputs, route and
success test, this is a specified analytical derivation. **Reserved; not
ready.** Depend on the completed B01 decision and frozen E01 request,
including any named consumer input; neither exists at setup.

**Deliverable/evidence:** one note in `notes/` proving the specified
statement with explicit constants, quantifiers and domains, or identifying
the precise failed step/allowance. Preserve complete-source tails and any
moment, coefficient-conditioning or normalization costs actually used.
If field consequences are claimed, retain \(Z_\lambda/2\), cancellation
and the full observation map. State conditional hypotheses as conditional.
Small authorized calculations belong in `numerics/`; floating diagnostics
and interval certificates retain distinct evidence labels.

**Completion/finite limit:** one frozen statement and proof route, one
regime and consumer, one return and at most one bounded correction pass.
Meet the frozen acceptance test or explain exactly why this method does
not establish it. A failed specified closure or estimating class does not
exclude all theta coefficient relations. No finite sample becomes an
asymptotic law. Any diagnostic needs finite cases, precision/refinement
limits and its stop rule in the issued packet before execution.

**Routine choices/escalation:** equivalent algebra, standard estimates with
checked hypotheses and correction of normalization slips are permitted.
A different source, observable, asymptotic regime, comparison mechanism or
missing conceptual theorem returns to VCD-B01. Do not widen the campaign
or create another task to compensate for an unfavorable result.

## VCD-E02 — Assess the stated coefficient result

**Type E; recommended GPT-6.1 Sol.** This is a fixed proof and consequence
assessment, not selection of a replacement mechanism. **Reserved; not
ready.** Depend on the E01 frozen request, exact input versions and
completed return, including its failures and corrections.

**Deliverable:** one report in `reviews/`, accepting, accepting with
limitations or rejecting the stated claim. Check monic normalization,
lattice sign, degree/time uniformity, tails, control premises and the
consumer's actual quantitative gain. If the claim supplies branch 02,
verify its specialization to fixed \(J(1/2)\); do not imply that coefficient
control alone proves transport. Record actual reviewer/model/effort and
shared sources; model change is not independent specialist review.

**Completion/limit:** one assessment and at most one authorized response
check, ending with a clear disposition and remaining premises. Routine
algebra and source verification are permitted. A fix within the original
contract returns to E01; a new target, missing conceptual premise or
different estimating class returns to VCD-B01. No new numerical campaign,
provider theorem or expanded consumer is part of this assessment.

## Control gate, ownership and stopping boundary

The inherited \(2+2e^{\lambda-T}\cos x\) control has regular
\(\beta_1=p,\beta_2=1-p,\beta_3=0\) through its double event,
with \(p=e^{\lambda-T}/(1+e^{\lambda-T})\). It fails the full theta
source/profile, infinite support and eventual threshold simplicity;
regular coefficient evolution alone does not exclude a collision.

Apply the actual catalog witnesses before endorsing a new inequality.
The [founding §8 screen](../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
and [parent control gate](../../research-overview/02_TENSOR_NETWORK_RESEARCH_PLAN_20261113.md)
retain each family's failed premise: unchanged canonical arithmetic for
Euler-factor controls, complete coefficients/full reflection for weighted
squares, integer-square arithmetic for reflected and primitive-compatible
smooth controls, full reflection/infinite data for finite-prime controls,
complete profile for finite-profile controls, ordinary Dirichlet arithmetic
for conditional endpoint controls, and literal Fourier observation for
altered-readout controls. Preserve regularity and conditional qualifiers.
For the proposed bound, identify the premise or quantitative inequality
each applicable witness actually fails. “Not theta” is insufficient.
A finite certificate need reject a control only where its domain contains
the collision or its bound contradicts the witness. No control certificate
is rerun by planning setup.

VCD owns coefficient questions; JCH owns fixed-basis transport, ITP owns
scale products, QTT owns finite tensor approximation, and the parent
[TN6 register](../../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
owns shared transfers only. No previous task or issued request is
superseded. Inherited identities remain in their source homes; only the
earlier branch-planning deferral is superseded by these VCD specifications.

Follow [REFERENCE_WORKFLOW](../../../../REFERENCE_WORKFLOW.md) at point of
use, retaining canonical annotations and inspected-passage limits. New
articles/checked passages are recorded promptly; this setup adds none.
Use [LARGE_FILES](../../../../LARGE_FILES.md) for derived data and PDFs.
One useful estimate, scoped failed route or assessment can end this round;
there is no compulsory manuscript or later campaign. The
[canonical continuation prompt](../../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
governs the next chat. New branch-only chats use this branch's
`chat-histories/`; already registered chats retain their unique home.
