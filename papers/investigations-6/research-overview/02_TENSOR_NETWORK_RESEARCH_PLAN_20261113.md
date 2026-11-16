# Investigations 6 — Collection research plan

13 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are unavailable: this chat's recorded `model_configurations` is empty.
Recommendations below are task routing, not claims about the authoring model.

**Continuation authorized; this documentation update starts no research.** This plan covers all four
branches and their shared interfaces. It lives in `research-overview/` at
the author's explicit request, an adaptation of the usual separate plan
directory in [INVESTIGATION_SETUP_WORKFLOW](../../../INVESTIGATION_SETUP_WORKFLOW.md).
The [scientific overview](01_TENSOR_NETWORK_PROGRAM_OVERVIEW_20261113.md)
remains the background document. The [parent progress file](../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
is the sole current register for **TN6** shared tasks only.

## 1. Objective and inherited starting point

**13 November 2026 authorization:** Edward Baker selects Astra / Ultra
for coordination and B tasks and Sol 6.1 / Ultra for E tasks. The
[canonical parallel continuation](../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
authorizes the four branch lanes and progression through ready tasks,
including subagent handoffs, without renewed permission. Record each
return, freeze/check the successor contract, then continue. Earlier
setup-only activation/stop restrictions are superseded; mathematical
dependencies, finite limits and evidence requirements remain. Requested
future settings are not inferred authoring metadata.

Obtain one useful, quantified relation between the complete theta source,
its tensor or polynomial representation, and a specified observation of
the Newman field. A first outcome may concern approximation, propagation,
coefficient structure or convergence. It need not prove a zero exclusion.
Its value must be stated through an actual bound, domain and comparison,
or a precisely scoped failure, rather than the existence of another exact
representation.

The [source crosswalk](../notes/02_BRANCH_SOURCE_CROSSWALK_20261113.md)
retains the founding evidence in Investigation 5:

| Starting evidence | Current meaning | Unpaid step |
| --- | --- | --- |
| [Brainstorm 01](../../investigations-5/brainstorm/01_MPS_NEWMAN_FLOW_20261113.md), finite QTT construction and floating pilot | Exploratory representation and approximation analysis | Quantified rank/error transfer at a chosen height scale and tolerance |
| [Brainstorm 02 §§2–3, equations (2)–(7)](../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md), fixed Jacobi orbit and single-excitation MPS | Exact representation identities | Useful propagation rate or recursive computation of amplitudes |
| Brainstorm 02 §4, equation (8), moving coefficients | Inherited generic Volterra identity | A useful relation using the unchanged theta initial data |
| Brainstorm 02 §§5–6, equations (9)–(11), scale products | Exact compact constructions with stated topology and full-line readout assembly | Manageable recursive factors and quantified growing-height/full-source costs |
| [Exact-height self-check](../../investigations-5/brainstorm/reviews/02_EXACT_HEIGHT_SELF_CHECK_20261113.md) | Same-assistant analytical check | No independent review, signed Green estimate or new zero exclusion |

Read the [result index](../../../result-summaries/README.md) and
[avoid index](../../../avoid/README.md), especially
[classification 01](../../../avoid/01_restating_the_target.md),
[controls 12](../../../result-summaries/12_collision_controls_and_screening.md),
[control premises 02](../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate realizations 03](../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[scoped exclusions 07](../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [numerics before a question 10](../../../avoid/10_numerics_ahead_of_the_question.md).
The existing identities are representations, the pilot is a diagnostic,
and future quantified bounds are candidate intermediate milestones. An
RH-equivalent reformulation must be identified once as such; surrogate
checks do not support it as progress. This plan proposes no new criterion
or quantitative inequality and does not rerun inherited control certificates.

## 2. Common mathematical contract

Preserve the complete theta source of
[GNP §2](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/02_source.tex):

\[
W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du,
\qquad H_0(z)=\xi(1/2-iz/2)/8.
\]

Initially \(0\le\lambda\le1/2\), \(\tau=1/2-\lambda\),
\(z=x+iy\), with real Newman height \(x\) twice zeta height.
Every estimate must specify its own finite observation domain or explicit
growing-height regime; the initial time interval is not a claim of
uniformity in height. Source tails remain paid when a computation uses
a cutoff. No isolated summand replaces the complete source.

Keep source coordinate \(u\), height \(x\), reversed time \(\tau\),
polynomial degree \(n\) and binary resolution \(k\) distinct. The fixed
weighted-space realization uses \(d\mu_*=W_{1/2}du/Z_*\) and

\[
H_{1/2-\tau}(z)=\frac{Z_*}{2}
\langle e_0,e^{-\tau J_*^2}e^{izJ_*}e_0\rangle.
\]

The moving-basis realization instead uses
\(H_\lambda(z)=Z_\lambda\langle e_0,e^{izJ(\lambda)}e_0\rangle/2\).
Here \(\beta_n=h_n/h_{n-1}\), \(\beta_0=0\),
\(\partial_\lambda\beta_n=\beta_n(\beta_{n+1}-\beta_{n-1})\).
Any interface must retain scalar normalization and, when differentiating
moving-basis states, the connection terms. Complex-height exponentials
act on the inherited prepared-vector domains; boundedness on the whole
Hilbert space is not assumed.

These are inherited formulas, not a fresh theorem import. The
[reference guide](../references/README.md) links the canonical bibliography
and passage records: Chin et al. §3, Theorem 3.1 for the chain-mapping
precedent; Van Assche §2.3, Theorem 2.4 and symmetric specialization for the
coefficient flow. Their recorded inspection limits remain unchanged.

## 3. Workstreams across the entire collection

These are planning briefs and interfaces, not a second register of branch
tasks. Branch 01 retains its existing IDs and specifications. Following
the author's subsequent 13 November request, branches 02–04 now have
their own bounded plans and sole registers. Their first B decisions remain
unresolved, authorized and not started. Their first conceptual rounds compare at most three options
within the listed branch, select one scope or record why none is ready,
and record the decision before proceeding into ready E tasks under the
standing authorization. A concrete theorem, norm or
architecture is deliberately not invented here.

| Branch and authoritative entry | First bounded question and required planning output | Evidence needed for a later result; possible scoped stop |
| --- | --- | --- |
| [01 — QTT](../01_qtt_newman_flow/research-plan/01_QTT_RESEARCH_PLAN_20261113.md) | Existing QTT-B01 chooses one observation norm, quantitative rank/error target, domain and baseline. Preserve its existing one-round, at-most-three-formulation limit. | Rank as a function of tolerance and domain, with source, quadrature, evolution, compression, normalization and arithmetic costs transferred to the observation. Stop the specified allowance if cancellation defeats its benefit; no inference of universal QTT failure. |
| [02 — Jacobi chain](../02_jacobi_chain_height_flow/research-overview/01_JACOBI_CHAIN_RESEARCH_OVERVIEW_20261113.md) | Choose one propagation or recursive-amplitude question for fixed \(J_*\), its state/readout norm and height regime; identify whether actual coupling bounds are required. Save that B decision and a branch-owned derivation contract if tractable. | An explicit height-dependent region/tail bound or usable recurrence with a stated consequence. A fixed-prefix limitation is inherited and supplies no transport rate. A failure applies to the selected basis, truncation or estimating class. |
| [03 — Volterra coefficients](../03_volterra_coefficient_dynamics/research-overview/01_VOLTERRA_RESEARCH_OVERVIEW_20261113.md) | Choose one theta-dependent coefficient relation or estimate, its \(n,\lambda\) domain and consumer; distinguish source input from the generic lattice law. | Explicit constants/quantifiers and a proof from the unchanged source, or the exact missing premise. Re-deriving the generic flow or a Hankel determinant identity alone does not supply a theta estimate; failed finite closure excludes only the tested closure class. |
| [04 — Infinite products](../04_exact_infinite_tensor_products/research-overview/01_INFINITE_PRODUCTS_RESEARCH_OVERVIEW_20261113.md) | Choose one architecture, convergence topology and parameter regime, including how compact intervals assemble the full source; compare the inherited phase/ratio products with at most two justified alternatives. | A recursive core rule or quantified contraction/remainder with growing support, height and source-tail costs visible. Compact \(\min f>0\) is not a global floor; failure of the chosen dyadic bound does not exclude other exact networks. |

For JCH-B01, VCD-B01 and ITP-B01, **GPT-6 Astra** is recommended because
the observable/target or architecture remains undecided. Routine notation,
basis convention and equivalent algebra are permitted; a change of source,
consumer or evidence standard must be recorded as a B scope change.
Once fixed, analytical derivation, implementation and assessment are
separately classified **E / GPT-6.1 Sol** with finite limits before work.
Recommended models do not select the actual model or effort for Edward Baker.

Branch-owned specifications and live registers are now available for
[JCH](../02_jacobi_chain_height_flow/research-plan/01_JACOBI_CHAIN_RESEARCH_PLAN_20261113.md)
([progress](../02_jacobi_chain_height_flow/research-progress/01_JACOBI_CHAIN_RESEARCH_PROGRESS_20261113.md)),
[VCD](../03_volterra_coefficient_dynamics/research-plan/01_VOLTERRA_RESEARCH_PLAN_20261113.md)
([progress](../03_volterra_coefficient_dynamics/research-progress/01_VOLTERRA_RESEARCH_PROGRESS_20261113.md))
and [ITP](../04_exact_infinite_tensor_products/research-plan/01_INFINITE_PRODUCTS_RESEARCH_PLAN_20261113.md)
([progress](../04_exact_infinite_tensor_products/research-progress/01_INFINITE_PRODUCTS_RESEARCH_PROGRESS_20261113.md)).
Each branch reserves E01 for its selected derivation and E02 for assessment;
read those local specifications rather than infer an execution packet here.

The [canonical continuation note](../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
contains the branch-opening prompts. The QTT
[sole register](../01_qtt_newman_flow/research-progress/01_QTT_RESEARCH_PROGRESS_20261113.md)
alone owns QTT status. No branch is required to wait for TN6-B01 or another
branch's conceptual opening. No priority among the four is imposed.

## 4. Dependencies and decision gates

There are three plausible interfaces, all conditional on useful inputs:

| Provider → consumer | What must cross the interface |
| --- | --- |
| 03 → 02 | A proved coefficient estimate, its degree/time domain, and its specialization to \(J_*\); moving-basis identities alone do not provide a propagation rate. |
| 04 → 01 | A specified finite truncation/tensor ordering, error norm, rank or support cost and full-source readout error; compact exactness alone does not provide a finite QTT advantage. |
| Any branch → a signed-field consumer | A quantitative estimate for the literal field/required jets with all normalization, tail, cancellation and denominator payments. A positive state norm or self-adjoint spectrum is insufficient. |

The [Green identity](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/05_green.tex),
[boundary-log acquisition](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/07_boundary_log.tex)
and [deflation](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/09_deflation.tex)
are possible consumers, not commitments. If a computational comparison is
chosen, match the complete [Riemann–Siegel baseline](../../investigations-5/09_green_potentials_newman_flow/manuscript/sections/10_riemann_siegel.tex),
including both arms and remainder, or explain a different matched baseline.

The decision sequence is conditional rather than a mandatory campaign:

1. **Choose a question.** Use a branch opening for branch-local work or
   TN6-B01 for a shared interface. Fix one observable, domain, method and
   measurable/analytic completion test before implementation.
2. **Obtain and assess a bounded return.** Derive the chosen bound or report
   the specific failed allowance under its own branch register. Samples,
   rigorous enclosures and proofs keep separate evidence labels.
3. **Combine only compatible returns.** A shared interface proceeds only
   after its named inputs exist and their hypotheses match. Otherwise keep
   the missing input explicit; do not fill it with a favorable assumption.
4. **Stop or continue by decision.** One useful estimate or scoped failed
   route can finish the selected round. A new consumer, expanded domain or
   wider numerical scan requires a new or revised classified task.

## 5. Shared tasks and bounded specifications

### TN6-B01 — Select one useful cross-branch interface

**B; recommended GPT-6 Astra.** The conceptual choice is what information
one representation can supply to another or to a common field consumer.
Ready and authorized for conceptual planning on inherited inputs; not started. Depend on
the four overviews, source crosswalk, canonical references and controls,
not completion of QTT-B01. The choice of consumer, norm and domain remains
open. This task does not decide QTT's formulation or prove a branch theorem.

**Limit and deliverable:** one conceptual round, at most four inherited
representation options, one common consumer and at most one matched
baseline. Save one decision in parent `brainstorm/notes/`, identifying the
selected provider/consumer, exact mathematical input needed, quantitative
acceptance test and branch that owns each missing result. Alternatively
record why none of the compared interfaces yet offers a useful contract.
No numerical campaign or new branch is included.

**Evidence/completion:** an explicit interface contract whose assumptions
and output are distinguishable from the target itself, or a justified
scoped stop. Include the claim classification and actual control-premise
screen below. If inputs exist, freeze `TN6-E01-r1.md` in parent
`research-progress/handoffs/`; otherwise record an input checklist and
leave E01 reserved. Do not manufacture an executable packet around an
unsettled source, generator, observation or success test.

**Routine choices/escalation:** notation, equivalent normalizations with
their exact readout map, and selection among existing interfaces are
permitted. A new physical source, unexplained norm change, new consumer
after selection or unproved arithmetic input requires an explicit B01
scope decision or branch B task. Record this round at its decision boundary,
then begin ready TN6-E01 using Sol 6.1 / Ultra without renewed permission.

### TN6-E01 — Check one frozen interface and its quantitative consequence

**E; recommended GPT-6.1 Sol.** This is fixed analytical compatibility and
error accounting once TN6-B01 supplies the question and method. **Reserved;
not ready.** Dependencies: completed B01 decision, one frozen request,
the exact provider result(s) and their assessments or explicit review
limitations, and a fixed consumer specification. No request is issued now.

**Deliverable:** one parent `notes/` return establishing the specified
transfer/comparison, or locating the precise missing premise or failed
allowance. Link the branch proof and source versions; do not redo a branch
theorem under a parent ID. An assessment of a stated result belongs in
parent `reviews/`, with reviewer provenance and shared-premise scope.

**Evidence/completion:** check the source, clocks, maps, domains, constants
and full error budget against the frozen acceptance test. Report whether
the actual number/rate meets that test, fails it, or remains conditional
on a named unproved input. A failed upper allowance is not a lower bound
on the true error or signed field. An exact identity without the required
quantitative consequence must retain that limitation.

**Finite limit:** one interface, one consumer/domain/baseline, one return
and at most one correction pass. Equivalent algebra and standard estimates
with verified hypotheses are routine choices. No new computation is
authorized by this placeholder; any necessary diagnostic requires explicit
finite cases, precision/refinement limits and a stop rule in the request.
A changed mechanism, domain, observable or unresolved conceptual premise
returns to TN6-B01 or the named branch B owner. Stop after the disposition;
there is no automatic synthesis, manuscript or larger campaign.

## 6. Claim and control gate for future proposals

Apply [controls 12](../../../result-summaries/12_collision_controls_and_screening.md)
to each new proposed estimate, using its actual domain and witness. The
inherited [Brainstorm 02 §8 screen](../../investigations-5/brainstorm/02_EXACT_HEIGHT_TENSOR_NETWORKS_20261113.md)
names missing premises: unchanged canonical source/arithmetic for
Euler-factor controls; complete coefficients/full reflection for weighted
squares; integer-square arithmetic for reflected super-Gaussians; complete
arithmetic source for shape/positive-primitive controls; full reflection
and unchanged infinite data for finite-prime controls; full theta profile
and, at atomic thresholds, eventual simplicity for finite-profile controls;
ordinary Dirichlet arithmetic for RH-conditional endpoint controls; and
literal Fourier/Newman readout for altered-kernel controls. Preserve each
control's regularity and conditional status from the catalog.

The regular atomic example \(2+2e^{\lambda-T}\cos x\) has a double
event at \((T,\pi)\); exact chain/Volterra evolution therefore supplies
no generic collision exclusion. Smooth colliding sources separately test
arguments that require a positive density or local refinement products.

This inherited screen is background, not a pass for an untested inequality.
For each future proposal record the witness, shared premises, the **specific
estimate or premise actually failed**, and the implication for the proposed
claim. “Not theta” alone does not show that an inequality fails. A finite
certificate need reject a control only on a domain containing its event
or when the claimed bound contradicts its witness. If that comparison is
unresolved, the sign claim remains unestablished. Negative conclusions
name the exact representation, truncation, regularity and parameter class.

## 7. Ownership, records and continuation

The parent owns TN6 shared decisions and transfers. QTT retains its own
plan/register; JCH, VCD and ITP IDs and live rows belong to their branches.
The parent links their registers rather than copying status. No existing
task or issued packet is superseded. The original planning deferral was
superseded first for the parent and then, by the subsequent author request,
for the branch plans/registers. The later parallel-continuation request
authorizes ready research and model handoffs; actual starts are recorded
only when work begins.

Use [REFERENCE_WORKFLOW](../../../REFERENCE_WORKFLOW.md) at point of use.
This setup reuses existing catalog records; it performs no fresh article
inspection or PDF download. Record new checked passages immediately,
preserving older inspection limits and failed download records. Sources
and small execution records stay in-tree; large data and third-party PDFs
follow [LARGE_FILES](../../../LARGE_FILES.md).

Parent derivations go in `notes/`, decisions in `brainstorm/notes/`, small
records in `numerics/`, assessments in `reviews/`, and issued requests in
`research-progress/handoffs/`. Each return records date, intended author,
actual model/effort when available, exact input versions, evidence level,
failed cases, corrections and disposition. Keep one writer per artifact.
Use the [planning input manifest](../numerics/02_PROGRAM_PLAN_INPUT_MANIFEST_20261113.json)
for this setup's pre-edit source identities, not as proof validation.

The [continuation note](../notes/01_BRANCH_OVERVIEWS_AND_CONTINUATION_20261113.md)
is the canonical prompt set. Shared conversations use parent
[chat-histories](../chat-histories/README.md); registered chats keep their
existing unique homes. Follow the recorder's integrity checks and bounded
exact-turn final capture. Update `DRAFT_HISTORY.md` for meaningful milestones.
If later work closes an investigation or reaches a manuscript milestone,
update the applicable result/avoid entry with source path and quotation;
this planning setup is neither event and adds no result-summary claim.

## 14 November 2026 — TN6-B02 acquisition round

Prepared for Edward Baker with substantial OpenAI Codex LLM assistance;
worker explicitly dispatched **gpt-6-astra / ultra**, without independent
backend/effort attestation. TN6-B01/E01 are completed, as recorded in the
sole parent register; their earlier prospective text above is historical.

**TN6-B02 — B, GPT-6 Astra / Ultra, active.** The author explicitly
continues [the acquisition decision](../notes/05_RESEARCH_CONTINUATION_AND_MODEL_HANDOFF_20261114.md).
Compare at most three complete-source approaches: moment/Gram recovery,
orthogonalization against an enclosed measure, and equivalent Gaussian
quadrature. Choose one modest finite coefficient count and one finite
height/time domain, absolute error scale and matched direct baseline.
Deliver one decision and either a frozen executable TN6-E02 packet with
conditioning, full source/tails, normalization and evaluation errors
paid, or a precise scoped stop. No numerics or manuscript belongs to B02.
The coefficients must actually be acquired by its successor; another
identity that simply renames the error is not completion.

**TN6-E02 — E, GPT-6.1 Sol / Ultra, reserved until B02 freezes r1.**
Implement one fixed acquisition/benchmark within prescribed arithmetic,
precision/refinement and runtime ceilings; return a rigorous certificate
or exact failed allowance, with floating diagnostics separately labeled.

**TN6-E03 — E, GPT-6.1 Sol / Ultra, dependent on E02.** One bounded internal
assessment, at most one implementation correction pass within E02 limits;
no expanded benchmark or mechanism. Model change alone is not specialist
independence. The sole parent register owns activation and disposition.

**B02 disposition, 14 November 2026:** the
[completed decision](../brainstorm/notes/02_TN6_B02_FINITE_COEFFICIENT_ACQUISITION_DECISION_20261114.md)
selects parity moment/LDL acquisition, N=16, |x|<=8 and the full reversed
time interval, normalized absolute target10^-8, with nine evaluated
points and a complete direct-integral baseline. [TN6-E02 r1](../research-progress/handoffs/TN6-E02-r1.md)
is now ready and frozen; its exact tuple, full error ledger, precision and
work ceilings supersede the prospective reservation above. TN6-E03 remains
dependent on that return. The root owns subsequent task-status edits.
No numerical certificate, manuscript or larger campaign was produced by B02.


**14 November 2026 — bounded round disposition:** B02/E02/E03 are complete
at their issued scope; the [sole register](../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md)
owns those statuses. The [current continuation](../notes/08_TN6_CONTINUATION_AND_MODEL_HANDOFF_20261114.md)
proposes a conceptual consumer decision, not a new issued E task. Its
candidate harder benchmark must return through an explicit B02 revision
before any expanded execution. The earlier activation/reservation wording
above is dated history. For Edward Baker with OpenAI Codex assistance;
B02 dispatched Astra/Ultra, E02/E03 Sol 6.1/Ultra, coordinator backend/effort
unavailable.
