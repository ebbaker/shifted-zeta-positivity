# Jacobi-chain height flow — Research plan

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are unavailable in the recorded configurations. Model recommendations
below follow [GPT_RESEARCH_MODEL_WORKFLOW](../../../../GPT_RESEARCH_MODEL_WORKFLOW.md)
and do not identify the authoring model or select the author's effort.

**Continuation authorized; research not started by this update.** The
[JCH progress file](../research-progress/01_JACOBI_CHAIN_RESEARCH_PROGRESS_20261113.md)
is the sole live register for this branch. The
[overview](../research-overview/01_JACOBI_CHAIN_RESEARCH_OVERVIEW_20261113.md)
owns scientific context; the [collection plan](../../research-overview/02_TENSOR_NETWORK_RESEARCH_PLAN_20261113.md)
and [TN6 register](../../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
own shared interfaces, not JCH task status.

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

## 1. Objective, inputs and fixed objects

Select and establish one useful quantitative statement about propagation
or recursive amplitudes in the fixed theta Jacobi chain. A state-tail or
transport estimate is a possible intermediate outcome; a signed-field
consequence requires its own complete readout argument. The first theorem,
norm and height regime remain open until JCH-B01.

The inherited source is [Brainstorm 02 §§2–3 and 6–8](../../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md),
with its [same-assistant analytical check](../../../investigations-5/brainstorm/reviews/02_EXACT_HEIGHT_SELF_CHECK_20261113.md).
Its exact representation identities are not a transport rate or an
independently reviewed theorem package. Preserve the complete
[GNP source](../../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex):

\[
W_\lambda=e^{\lambda u^2}\Phi,\qquad
H_\lambda(z)=\tfrac12\int_{\mathbb R}W_\lambda(u)e^{izu}du,
\qquad H_0(z)=\xi(1/2-iz/2)/8.
\]

Initially \(0\le\lambda\le1/2\), \(\tau=1/2-\lambda\),
\(z=x+iy\), and real Newman height \(x\) is twice zeta height.
Set \(Z_*=\int W_{1/2}\), \(d\mu_*=W_{1/2}du/Z_*\). The fixed
orthonormal basis gives the self-adjoint realization \(J_*\) of
multiplication by \(u\), including its domain, and

\[
v(\tau,z)=e^{-\tau J_*^2}e^{izJ_*}e_0,\qquad
H_{1/2-\tau}(z)=\tfrac{Z_*}{2}\langle e_0,v(\tau,z)\rangle,
\]
\[
\partial_xv=iJ_*v,\qquad \partial_\tau v=-J_*^2v.
\]

The prepared-vector complex-height domains remain explicit; nonreal
\(z\) does not make \(e^{izJ_*}\) bounded on the entire space.
Polynomial degree is the chain-site index, distinct from height or QTT
resolution. Branch 03's moving \(J(\lambda)\) cannot replace \(J_*\)
in these equations without connection terms.

The source note's single-excitation bond-two MPS contains the full sequence
\(v_n\). It is an encoding, not an algorithm for that sequence. Its
fixed-prefix mass escape at unbounded real height supplies no propagation
rate and concerns only that basis/truncation. Likewise the inherited
finite constant-matrix exclusion concerns autonomous finite-dimensional
linear realizations, not all recursive networks.

The [reference guide](../references/README.md) retains canonical article
records and bibliography. Chin et al. §3, Theorem 3.1 supplies the inspected
chain-mapping precedent; the full-line theta specialization is inherited
from the internal note, not from bounded-support tail asymptotics. This
planning pass adds no fresh theorem import or source inspection.

## 2. JCH-B01 — Choose the first transport or recursive-amplitude question

**Type B; recommended GPT-6 Astra.** Choosing which state/readout norm,
height regime and coefficient information can yield a useful result is
the unresolved conceptual task. **Ready and authorized for continuation; not started.**
Dependencies are the overview, inherited note/check, reference guide,
[source crosswalk](../../notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md) and
control/classification rules below. Neither QTT nor TN6-B01 must finish
first; any later coefficient input from branch 03 must be named explicitly.

**Finite scope:** one conceptual round comparing at most three formulations
within fixed-basis chain transport: a height-dependent prefix-tail bound,
a recursive-amplitude estimate, or a controlled transfer to a specified
literal-field observation. Select one question and domain, with at most
one matched non-chain baseline. These are options to assess, not estimates
asserted by this plan. No numerical campaign or branch theorem is executed.

**Deliverable:** one decision in `brainstorm/notes/`, recording the chosen
question or a scoped reason to park the compared routes. If tractable,
prepare `research-progress/handoffs/JCH-E01-r1.md` with exact input versions,
source, generator, observation, domain, proof method and acceptance test.
Freeze any coupling hypotheses, truncation/boundary convention, norm,
tolerance or claimed rate, and the normalization and cancellation payments
needed by its consumer. State whether the result is conditional on an
unproved coefficient estimate. Reserve E01 if its mathematical contract or
required inputs remain unresolved; do not invent an executable request.

**Completion/evidence:** a usable fixed derivation contract with an
interpretable quantitative outcome, or a justified failure of the compared
class. Repeating exact evolution, bond dimension two, fixed-prefix escape
or a target-equivalent sign criterion does not complete this task. Identify
what additional estimate the proposed route would actually supply.

**Routine choices and escalation:** notation, equivalent basis conventions
and an explicit source-preserving normalization are permitted. A new
physical source, moving-basis mechanism, different observation or missing
arithmetic theorem requires a recorded B scope decision or a named sibling
B dependency. Record the decision and begin the declared E follow-through
on Sol 6.1 / Ultra when ready, under the standing continuation authorization.

## 3. JCH-E01 — Derive the frozen chain estimate and readout consequence

**Type E; recommended GPT-6.1 Sol.** Once B01 fixes the target, inputs and
method, this is a specified analytical derivation and error-accounting
task. **Reserved; not ready.** Dependencies: completed JCH-B01, issued
versioned E01 request and every prerequisite result identified there.
No request or mathematical return exists at setup.

**Deliverable:** a note in `notes/` proving the selected estimate with
its domains, constants, quantifiers and observation transfer, or identifying
the precise failed allowance/missing premise. Distinguish exact-state
prefix tails from errors incurred by evolving a separately truncated
operator; they are not interchangeable by notation. Preserve all complete
source, norm, boundary, tail, normalization and cancellation costs that the
chosen method uses. An absolute state estimate alone is not a relative
error estimate for a small return amplitude.

**Evidence/completion:** meet the frozen acceptance test or show exactly
why its stated method does not meet it. Keep a conditional derivation,
floating diagnostic, rigorous enclosure and universal proof distinct.
A failed allowance does not establish a lower bound on the actual error
or exclude other chain estimates. Any negative result names its tested
norm, truncation, coefficient hypotheses and parameter regime.

**Finite limit:** one request, one selected domain and estimate, one
derivation and at most one correction pass. Equivalent algebra, justified
standard inequalities and routine normalization repairs are permitted.
No numeric run follows from this placeholder: a packet authorizing one
must specify finite cases, precision/refinement limits and a stop rule.
A new proof mechanism, enlarged domain, changed consumer or unresolved
conceptual coefficient input returns to JCH-B01; continue only unaffected
work within the fixed request. Save the return, then begin ready JCH-E02
on Sol 6.1 / Ultra without renewed permission.

## 4. JCH-E02 — Assess the specified result and its scope

**Type E; recommended GPT-6.1 Sol.** This is a fixed proof/interface audit,
not selection of a new transport mechanism. **Reserved; not ready.**
Dependencies: E01's unchanged request, completed return, exact source
versions and claimed consumer consequence.

**Deliverable/evidence:** one assessment in `reviews/`, accepting, accepting
with limitations, or rejecting the stated claim. Check normalization,
clock direction, operator/prepared-vector domains, fixed versus moving
bases, truncation errors, coefficient hypotheses, constants, control
premises and the actual quantitative consequence. Record reviewer/model/
effort when available and shared-source limitations; a model change is
not independent specialist review.

**Finite limit/completion:** one report and, if authorized, one response
check. Complete when the disposition, corrections and remaining premises
are explicit. Routine algebra and source verification are permitted; no
new theorem, replacement consumer or height scan is included. Routine
corrections remain within E01; a changed mechanism or unresolved conceptual
input returns to JCH-B01. Further ready tasks follow the standing
continuation authorization; assessment does not erase their prerequisites.

## 5. Controls, ownership and continuation

Read the [result index](../../../../result-summaries/README.md),
[avoid index](../../../../avoid/README.md),
[controls 12](../../../../result-summaries/12_collision_controls_and_screening.md),
[classification 01](../../../../avoid/01_restating_the_target.md),
[control-premise rule 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate caution 03](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md)
and [scope rule 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md).
An intermediate estimate is judged by its number/rate; an RH-equivalent
reformulation is stated once and not supported by surrogate checks.

The inherited atomic control \(2+2e^{\lambda-T}\cos x\) has a regular
finite chain at its double event \((T,\pi)\), while failing the full
theta profile/arithmetic, infinite support and eventual threshold simplicity.
Smooth reflected and positive-primitive controls separately test proposals
using a smooth positive density; they fail canonical integer-square theta
arithmetic. The complete catalog premise screen remains Brainstorm 02 §8
and the parent plan §6. For each new inequality apply the actual witnesses
and name its failed premise or estimate; absence of the literal theta source
does not by itself show the inequality fails. A finite certificate need
reject only a control whose event is in its domain or contradicts its bound.
No control computation is claimed by this planning setup.

The dated ownership change is limited to assigning previously unassigned
branch questions to JCH-B01/E01/E02. No completed identity or issued request
is transferred, superseded or counted as a task completion. Moving
coefficients remain with branch 03; QTT and exact products keep their own
families. Shared comparisons use the parent TN6 family without copying JCH
status. One useful estimate or scoped failed route may finish this round.

Use [REFERENCE_WORKFLOW](../../../../REFERENCE_WORKFLOW.md) at point of use,
preserve inspected-source limits and retain large data/third-party PDFs
outside Git under [LARGE_FILES](../../../../LARGE_FILES.md). Save derivations
in `notes/`, decisions in `brainstorm/notes/`, small computation records in
`numerics/` and assessments in `reviews/`. Each return records actual
date, model/effort, input/request versions, evidence and disposition.
The [canonical continuation prompt](../../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
routes the next **[B] JCH-B01 — Astra** decision. New branch-only chats use
this branch's [history folder](../chat-histories/README.md); the current
shared setup chat retains its parent registration. No duplicate archive,
manuscript or execution packet is created here.
