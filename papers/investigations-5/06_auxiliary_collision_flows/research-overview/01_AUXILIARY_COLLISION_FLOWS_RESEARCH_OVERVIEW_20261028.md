# Auxiliary flows for collision analysis research overview

28 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.

**Status: research background and plan, updated at the author's request.**
The leading objective is an independent estimate that could constrain
canonical theta collisions. This investigation explores modified
de Bruijn–Newman flows and auxiliary evolutions that might make such an
estimate accessible. The starting material comes from Investigation05's
[geometry discussion][n37] and [auxiliary source-flow assessment][n38].

The [planning section](#research-plan-for-an-independent-theta-estimate)
classifies upcoming work as B / brainstorm or E / execution before it
starts. [Progress01][progress] owns live status. No candidate flow,
numerical campaign or new canonical estimate is selected or established
merely by creating the plan.

## Motivation and relationship to the earlier investigation

Investigation05 began with radial theta geometry and developed several
ways to represent or evolve the source while retaining access to its
spectral observation. The present direction takes the freedom to design
an auxiliary evolution as its central idea. A useful flow might turn a
collision into a pronounced response, expose information in a different
combination, or admit an estimate that is difficult to see in the original
formulation.

The dimension, geometry and generator remain open. Three-dimensional
radial structure is available when it contributes a useful relation, but
is not a premise of this investigation. Local differential terms,
nonlocal source perturbations and coupled fields all fit its scope.
The original conservative theta-flow program remains in Investigation05
with its existing task states. This investigation now has its own ACF task
contracts and [sole live progress register][progress].

Two possible benefits should remain distinct. A better diagnostic could
resolve a collision or near collision more effectively at a stated cost.
An exclusion argument would additionally need independently established
information that prevents the relevant response for the canonical theta
source. The author has selected the independent estimate as the leading
objective; diagnostic improvement can support it. Amplification alone does
not supply that estimate.

## Canonical field and collision convention

Use the repository normalization
\[
H(t,z)=\int_0^\infty\Phi(u)e^{tu^2}\cos(zu)\,du,
\qquad
\Phi(u)=\sum_{n\ge1}
(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]
Then
\[
H_t=-H_{zz},\qquad
H(0,z)=\frac18\xi\!\left(\frac{1+iz}{2}\right).
\]
The complete source is positive on the half-line and has
double-exponential decay. The [reference guide][references] routes to the
checked Rodgers–Tao normalization and the Newman–Wu source-weighting
background, retaining their different conventions and inspection scopes.

The local calculations inherited here concern a nondegenerate real double
event
\[
H(T,a)=H_z(T,a)=0,\qquad A=H_{zz}(T,a)\ne0.
\]
Higher multiplicities, uniform height ranges and global threshold
conclusions are not established by these local formulas.

## What the previous auxiliary flows contribute

| Background | What is available | Limit retained here |
| --- | --- | --- |
| [Conserved-density heat, Note25][n25] | A collision removes leading diffusion modes of the marked value and derivative densities | A generic diagnostic under moment assumptions; it works in any dimension and admits colliding controls |
| [Feedback magnifier, Note28][n28] | A conservative feedback flow with a finite breakdown deadline at a marked collision, proved in-note with same-assistant checks | Global regularity reformulates pointwise noncollision; no independent theta bound preventing breakdown |
| [Positive carrier, Note29][n29] | Quantitative regularity from an independently known first-jet margin | The comparison does not acquire that margin or enlarge its already separated theta domain |
| [Propagated source relation, Note31][n31] | Explicit preparation residual, forced commutator and domain conditions for the fixed feedback model, proved in-note with same-assistant checks | The zero-residual variant fails; estimates retaining the residual and other relations remain open |
| [Linear combined flow, Brainstorm08][b08] | An exact solution of the specified Newman/cylinder-heat combination | Its zeros are the original heat zeros after a nonvanishing factor and coordinate/time rescaling |
| [Source perturbations, Note38][n38] | General local response identities, a bounded cosine perturbation and an exact positive-source control | No demonstrated improvement in sensitivity, cost or collision exclusion |

These findings motivate freedom to change the flow and observable
together. They do not select the earlier feedback construction as the
default continuation or rule out other geometric estimates.

## Two parameters retain a clear connection to the original problem

A convenient source-defined family from Note38 is
\[
F(t,s,z)=\int_0^\infty\Phi(u)e^{tu^2+s q(u)}\cos(zu)\,du.
\tag{1}
\]
Here t remains Newman time and s is a new auxiliary parameter. For bounded
real even q, the theta tail makes F entire in t,s,z; F is even in z and
real on the real axis for real t,s. Its physical slice is exactly
F(t,0,z)=H(t,z), and F_t=-F_{zz} throughout the family.

The new source remains positive for real s. This does not transfer
Newman's all-real-zero monotonicity to the s direction. A deformation
that changes zeros needs a justified comparison back to the physical
slice. An evolution that preserves the complete observation, or preserves
zeros through a known nonvanishing factor, has a different role. These
possibilities remain available without being identified with each other.

Define the initial auxiliary response
\[
R_q(t,z)=F_s(t,0,z)
=\int_0^\infty q(u)\Phi(u)e^{tu^2}\cos(zu)\,du.
\]
At a simple zero, its motion under s is
\(z'(0)=-R_q/H_z\). Near the double event, writing
\(\tau=t-T\) and \(\eta=z-a\), the leading expansion is
\[
F(t,s,z)=\frac A2\eta^2-A\tau+sR_q(T,a)+\text{higher terms}.
\tag{2}
\]
More precisely, the squared gap D of the two nearby zeros is analytic and
satisfies
\[
D(t,s)=8\tau-8\frac{R_q(T,a)}A s
+O\bigl((|\tau|+|s|)^2\bigr).
\tag{3}
\]
The nearby curve of double events has T'(0)=R_q(T,a)/A. These inherited
identities describe a response; they do not bound it. The source note
contains the remainder, implicit-function calculation and qualifications.

## Candidate examples already discussed

The following are mathematical examples, not a selected program.

| Source weight q | Auxiliary equation or effect | Interpretation |
| --- | --- | --- |
| 1 | F_s=F | Changes amplitude |
| u^2 | F_s=-F_zz | Replaces t by t+s |
| u^4 | F_s=F_zzzz | A local higher-order direction; its response can vanish at a double event |
| cos(au), with a fixed | F_s=(F(z+a)+F(z-a))/2 | A bounded nonlocal direction with a positive response at the mark |

The quartic case also converges for all complex parameters for the
canonical theta source. Following s=epsilon*t gives
\[
\widetilde F_t=-\widetilde F_{zz}
+\epsilon\widetilde F_{zzzz},\qquad
\widetilde F(0,z)=H(0,z).
\]
This makes a natural local modification concrete. The quadratic heat
model z^2-2t has a double event and zero fourth derivative, so higher
derivative order by itself is not a guaranteed collision signal. In
addition, multiplying a Gaussian-tail control by e^{su^4} is not an
admissible two-sided perturbation at s=0; its integral diverges for s>0.

For regular holomorphic evolutions with terms b(t,z)F_z+c(t,z)F, both
added terms vanish at a double event. They retain the leading local
heat splitting, although nonconstant coefficients can change global
dynamics and higher terms. Constant drift bF_z translates the argument;
linear drift bzF_z dilates it with a time change. With constant b,c,
the two explicit solutions are respectively
\[
e^{c\tau}H(\tau,z+b\tau),\qquad
e^{c\tau}H(\sigma(\tau),e^{b\tau}z),\quad
\sigma'=e^{2b\tau},\quad\sigma(0)=0.
\]
The corresponding distinction has been corrected in Note38. These are
scoped comparisons, not exclusions of general drift, potential, nonlinear
or coupled constructions.

## The bounded cosine response

For q_a(u)=cos(au), fix a>0 independently of s and of the running
spectral variable z. The exact auxiliary equation is
\[
F_s(t,s,z)=\frac12\{F(t,s,z+a)+F(t,s,z-a)\}.
\tag{4}
\]
At the mark, the first response is
\[
P_a(t):=F_s(t,0,a)
=\int_0^\infty\Phi(u)e^{tu^2}\cos^2(au)\,du
=\frac{H(t,0)+H(t,2a)}2>0.
\tag{5}
\]
Strict positivity follows from the positive continuous density; also
\(P_a(t)\le H(t,0)\). Since \(|q_a|\le1\), the source perturbation costs at most
e^{|s|} in absolute majorants, and its difference from the original source
costs at most e^{|s|}-1. The generator contains no inverse zero value or
inverse first derivative.

At a double event, equation(3) gives
\[
(z_+(s)-z_-(s))^2=-8\frac{P_a(T)}A s+O(s^2).
\tag{6}
\]
This gives a definite square-root unfolding. The same exponent already
occurs in Newman time, where D_t=8. Positivity of P_a holds away from
collisions too, so it is not by itself a collision certificate. The
response ratio still contains A, and a different mark generally requires
a different auxiliary flow.

On the single path s=epsilon*t, this example becomes
\[
\widetilde F_t=-\widetilde F_{zz}
+\frac\epsilon2\{\widetilde F(t,z+a)+\widetilde F(t,z-a)\},
\qquad \widetilde F(0,z)=H(0,z).
\tag{7}
\]
Keeping the parameters separate first makes the original slice and the
auxiliary response explicit. Neither form is selected as the eventual
research flow.

## Controls and interpretation

Note38 evaluates the cosine response exactly on the positive control
\[
\Phi_*(u)=(64u^4+6)e^{-(4+T_c)u^2},\qquad
T_c=\tfrac14,
\]
whose double event is at \(a=2\sqrt6\). With \(C=\sqrt\pi/16\), its curvature
and response are
\[
A=12Ce^{-3/2},\qquad P_a=C(18+162e^{-6})>0.
\]
This is a successful diagnostic response on an admitted colliding source.
The control lacks canonical square arithmetic and the theta tail, but
fails no premise of the bounded-tilt calculation.

The [control register][controls] and Note38's family screen retain the
other distinctions: Euler-factor controls alter the canonical factors;
weighted-square and finite-prime controls lack complete coefficients or
full reflection; reflected and positive-primitive controls lack canonical
square arithmetic. Their admitted positive continuous sources share the
cosine-response calculation. Atomic measures require a support check for
strict positivity. No separating theta estimate has yet been acquired.

An improved diagnostic would need a quantitative advantage after
normalization, error growth and evaluation cost are accounted for. An
exclusion would require additional information specific to the complete
canonical source. Replacing that missing information by a global
regularity assertion equivalent to noncollision would return to the
earlier reformulation. These distinctions govern the plan below. The
first task selects a concrete mechanism and intended estimate; neither
has already been acquired.

The [result index][results], particularly [heat flow][heat],
[collision controls][controls] and [geometric realizations][geometry],
and the [avoid index][avoid] are the common background. The specific
guidance on [target classification][a01], [control premises][a02],
[coordinate changes][a03] and [scoped conclusions][a07] applies.
The inherited calculations have the same-assistant checking stated in
their source notes; this overview adds no independent mathematical review.

## Research plan for an independent theta estimate

**Planning added at the author's request, 28 October 2026.** Prepared for
Edward Baker with substantial LLM assistance, **gpt-6-astra (Codex),
recorded effort max**, Investigation06 chat0002. The [brainstorm][brainstorm]
records the author's choice: an independent estimate constraining canonical
theta collisions is the leading objective. Diagnostic improvement is a
supporting possibility. The flow, observable and geometric dimension remain
open. The [research-progress note][progress] is the sole live task register;
the specifications below define the initial scope and dependencies.

### Mathematical objective and comparison standard

Seek an estimate derived from the complete canonical source that places a
new quantitative restriction on hypothetical collisions, or excludes them
on a stated domain. The estimate may be event-conditioned, but its proof
must not assume the first-jet margin, real-zero geometry or regularity that
it is intended to establish. A reformulation can become useful through a
new proof of its missing bound; rewriting that bound is not a completion.

Two proof mechanisms remain available. A regular auxiliary evolution may
have an observable whose collision-forced behavior is incompatible with a
theta estimate. A singular collision magnifier may admit an independent
a priori bound preventing its forced breakdown. The cosine family and the
earlier feedback system are comparison examples for these mechanisms.
Their current identities and regularity statements supply no new canonical
exclusion. The survey's restrictions apply only to their stated operator
and source classes; the [stable-model obstructions][stable-models] must
also be checked before proposing another spin or quartic realization.

The first result can be bounded in time and height. Compare it with existing
direct estimates on the same domain and with the same available source
information. A repeated known exclusion region is a method check unless a
separate quantitative benefit is established. Uniform height, limiting
time, higher multiplicity and global threshold conclusions belong to the
later coverage task; the inherited local double-event formulas do not
supply them.

### Classification and initial routing

Follow [GPT_RESEARCH_MODEL_WORKFLOW][workflow]. **B — brainstorm** identifies
an unresolved consequential mathematical choice; **E — execution** identifies
work whose route and completion test have been fixed, including routine
proofs. Recommendations do not change the selected model or effort. Edward
Baker chooses the model, effort and chat; this plan dispatches no work.

| Task | Type | Recommended model and reason | Initial readiness and dependency |
| --- | --- | --- | --- |
| ACF-B01 | B | Astra — choose a flow, observable and plausible independent estimate together | Ready; overview, survey, brainstorm and inherited controls |
| ACF-E01 | E | Sol — derive and check a fixed analytic contract | Gated by B01 candidate C1 and an issued E01 request |
| ACF-B02 | B | Astra — resolve the signed theta estimate or its structural obstruction | Gated by the candidate and E01 identity/control return |
| ACF-E02 | E | Sol — bounded measurements from fixed formulas | Optional; gated by a specific acquisition question and issued request from B02 |
| ACF-E03 | E | Sol — complete a fixed proof and any required rigorous finite bounds | Gated by a tractable B02 proof contract; E02 only if that contract requires it |
| ACF-E04 | E | Sol — check a frozen proof or scoped failure against its inputs and controls | Gated by one completed, versioned mathematical return |
| ACF-B03 | B | Astra — decide whether an accepted estimate extends in time, height or multiplicity | Gated by an E04-assessed quantitative canonical gain |
| ACF-E05 | E | Sol — integrate one assessed result with its settled scope | Gated by an E04 disposition; no dependency on B03 unless its extension is being integrated |

The E entries are conditional assignments, not ready execution packets.
Their hypotheses and finite limits must be supplied before they start.
Only B01 is ready at plan creation. Current status belongs in [Progress01][progress].

### ACF-B01 Mechanism and estimate selection

**Type B; recommend Astra.** The conceptual difficulty is to find a flow
that makes an independent source estimate accessible, rather than merely
changing local collision speed. Inputs are this overview, the [survey][survey],
the [brainstorm][brainstorm], [Note29][n29], [Note31][n31], the control
register and the scoped stable-model results. No numerical prerequisite
is imposed. The fixed-feedback CTF-B02 remains owned by Investigation05;
if that family is revisited here, identify the different equation,
observable or estimate question instead of duplicating its existing task.

**Scope and deliverable:** compare at most **two concrete candidates in
one bounded round**, drawn from local, nonlocal or coupled systems. Choose
at most one candidate, C1, or give a scoped reason neither provides a usable
route. Do not repeat the entire literature survey, introduce a third
candidate in the same round, or start a numerical search. For a selected
candidate, write the following contract:

- Complete source, equations, initial data, independent parameters,
  analytic domain, and exact recovery of H on the physical slice or through
  the preserved observation. State how physical parameter derivatives evolve.
- One normalized observable and the behavior forced by a hypothetical
  event, with its multiplicity and parameter range stated.
- The proposed canonical inequality, which proof inputs are established,
  and the specific signed relation or estimate still missing. Identify the
  source term expected to do the separating work.
- The relevant controls, all boundary, preparation, commutator and tail
  terms, and a direct comparison using the same source information.
- One useful bounded target domain or a precisely stated parametric domain,
  the intended evidence standard, and a fixed analytical route for E01.

**Completion:** a reasoned candidate decision and versioned E01 request,
or a documented failure of the two tested candidates. The decision must
explain why the remaining question is a specific estimate rather than a
renamed noncollision assertion. It is a design result, not proof of that
estimate. If neither candidate survives, retain the failures and recommend
a new B01 request only with a named different idea; no E task is released.

### ACF-E01 Fixed identities and control accounting

**Type E; recommend Sol.** Start only after B01 freezes C1, its formulas,
domain and request revision. Derive the prescribed observable evolution,
physical-slice relation, actual parameter-jet equations, analytic-domain
conditions and complete residual terms. Check only the literature results
used by that contract, with their hypotheses. Apply the named controls
analytically; use the same domain and normalization as the theta claim.

**Scope and completion:** one candidate and one request revision. Return a
note containing the complete identities, a list of established and missing
estimates, and the actual control outcomes; exact algebra or bounded checks
may support the derivation but do not certify an unbounded claim. The
request must state the permitted exact checks; it contains no PDE simulation
or scan by default. Ordinary algebra, normalization corrections and standard
domination arguments are E work. A changed source, equation or observable,
or an existence/domain question requiring a new proof strategy, returns
to B01; a difficult new canonical bound belongs in B02. Record any
affected failed dependency and finish unaffected checks within the request.

### ACF-B02 Independent canonical estimate

**Type B; recommend Astra.** With C1 and E01 available, address **one named
missing estimate in one bounded round**. The difficulty is the actual
signed theta comparison, cancellation or interaction bound; generic source
positivity and an assumed first-jet floor are not substitutes. Retain the
complete source terms identified by E01. Diagnose where the actual bound,
including its constants, would fail on a relevant colliding control.

**Deliverable and completion:** a proved estimate, a tractable proof contract
for E03 with every unproved premise explicit, or a precise failure of this
route. If finite measurements would decide a specified feasibility question,
issue an optional E02 request explaining both favorable and unfavorable
outcomes. If rigorous constants are already the only missing inputs, route
directly to E03. A numerical request may be released by a recorded partial
B02 return; it does not require declaring the canonical estimate complete.
Do not open a new flow, enlarge the target domain or invent a new scan to
rescue a failed bound. Those changes require a visible B01 or B02 revision.

### ACF-E02 Optional finite feasibility measurement

**Type E; recommend Sol.** This task is available only when B02 specifies
the exact formulas, quantities and decision they inform. Before starting,
the request must freeze the finite cases, source truncation, quadrature,
initial and maximum precision, allowed refinements, total work limit and
stopping threshold. None of those numerical choices is selected by this
planning document.

**Scope and completion:** exactly one issued packet. Return reproducible
code and a small record of every requested case, errors, failed allowances
and measured costs when relevant. Floating evidence remains floating.
An unfavorable result or reaching the declared cap completes the bounded
measurement; do not change the observable or extend the cases. Routine
implementation diagnosis stays in E02 within its limit. An unresolved
mathematical premise returns to B02; changing the mechanism returns to B01.
This optional pilot is not a compulsory step before an analytic proof.

### ACF-E03 Fixed proof completion and rigorous acquisition

**Type E; recommend Sol.** Begin when B02 has supplied a fixed mathematical
route, hypotheses, target domain and acceptance inequality. Complete the
standard estimates and, if needed, acquire only the finite quantities that
the proof consumes. The issued request must name every lemma or finite
case, define its work limits, and distinguish analytic proof obligations
from exact or interval calculations. If the proof is purely analytic,
no numerical stage is required.

**Scope and completion:** one contract and one target domain. Return a
complete proof or a scoped failed premise/budget, with source truncation,
arithmetic, quadrature, parameter propagation, boundary and tail payments
where applicable. Any certificate records inputs and verification hashes,
uses appropriate exact or outward-rounded arithmetic, and checks rejection
of a deliberately altered input. Report the actual domain and comparison
with established direct coverage. Routine corrections are allowed; a new
lemma needing a new proof strategy or a changed target returns to B02.
Do not silently replace a failed certificate by an expanded campaign.

### ACF-E04 Assessment of one frozen return

**Type E; recommend Sol.** Review one versioned proof, certificate or scoped
negative result from B02/E03; the result's scientific question and claimed
scope are fixed. Check logical dependencies, imported hypotheses,
normalization, all residual payments, and the collision controls relevant
to that claim. Recompute only the finite checks supplied by its request,
within the same declared limits.

**Scope and completion:** one review report with source hashes, actual model
and effort, same-assistant/same-model/cross-model relationship, supported
claims, corrections and unresolved premises. No specialist independence is
implied by changing models. A correct scoped failure is a valid assessed
result. Routine fixes can be verified within this return; a new mechanism
returns to B01 and a new mathematical argument to B02. This assessment
does not independently authorize starting B03 or a numerical extension.

### ACF-B03 Coverage and threshold relevance

**Type B; recommend Astra.** After an assessed quantitative canonical gain,
choose **one** extension question: time range, height range, higher
multiplicity, or compatibility with a stated threshold reduction. Use the
actual constants and proof scope, not numerical extrapolation. Consult the
relevant existing reduction before claiming what the extension would imply.

**Completion:** an extension argument, a precise coverage gap, or a frozen
execution request for a standard remaining step. Limit the round to the
selected coverage question. A simultaneous change of flow or observable
returns to B01. A missing new signed estimate belongs in a dated B02 return.
Any follow-through computation receives its E classification and finite
contract before it starts; no automatic all-height campaign is prescribed.

### ACF-E05 Integration of an assessed result

**Type E; recommend Sol.** Integrate one E04-assessed return into the overview,
live register, folder navigation and appropriate research notes. Preserve
failed evidence and the source's status words. Update the result and avoid
indexes only when their repository inclusion rules apply. Check links and
file sizes. This is routine production after the mathematical interpretation
has been settled; ordinary chat capture and small status edits remain
housekeeping available to either model.

**Completion:** one coherent documentation update linking the proof,
assessment and any code/records. No new manuscript or snapshot is part of
this task. A new mathematical interpretation returns to B02 or B03. The
present plan creation is housekeeping, not completion of this future task.

### Sequence and records

The default sequence is **B01 → E01 → B02**. A successful B02 route proceeds
to E03 and E04; E02 is an optional measurement, and a complete B02 proof can
go directly to E04. A completed negative result can also go to E04/E05 without
opening a numerical task. After an assessed gain, B03 addresses one extension
while E05 can integrate the bounded result independently.

Issue execution requests under `research-progress/handoffs/` only when their
contracts are fixed. Each request records its revision, input versions,
permitted choices/files, evidence standard, finite work limits and B return
condition. Preserve the issued request; append or link its return. Save
exploratory decisions in `brainstorm/`, derivations in `notes/`, computation
code and small records in `numerics/`, and assessments in `reviews/`.
Record actual model/effort and the actual limits of every result. Follow the
[numerical-scope rule][a10], [known-result test rule][a11], [review rule][a05],
[status rule][a06] and [single-writer rule][a17].

**Default next task: [B] ACF-B01 — Astra.** Compare at most two concrete
flow/observable candidates for an independent theta estimate; return one
usable analytical contract or a scoped failure. No ACF research task has
been executed by writing this plan.


## Source and conversation continuity

The original notes and reference annotations remain in Investigation05.
This investigation links to them and will hold subsequent work developed
for this direction. Its [folder guide][root] and [reference guide][references]
provide the entry points.

The founding conversation, *Assess auxiliary flow strategy*, retains its
unique Investigation05 chat0017 registration; [the history guide][history]
links to that archive. The current planning conversation, **Discuss auxiliary
collision research**, is uniquely registered here as chat0002. The author
requested the plan and progress register after the [post-survey
brainstorm][brainstorm]; their creation supersedes the earlier planning
deferral without changing any inherited mathematical status.

[root]: ../README.md
[history]: ../chat-histories/README.md
[references]: ../references/README.md
[n25]: ../../05_radial_theta_collision_geometry/notes/25_TOTAL_INTEGRAL_CONSERVATION_AND_DIRECTION_FREE_HEAT_FLOW_20261027.md
[n28]: ../../05_radial_theta_collision_geometry/notes/28_ENERGY_NORMALIZED_CONSERVATIVE_COLLISION_MAGNIFIER_20261028.md
[n29]: ../../05_radial_theta_collision_geometry/notes/29_POSITIVE_CARRIER_COMPARISON_AND_QUANTITATIVE_REGULARITY_20261028.md
[n37]: ../../05_radial_theta_collision_geometry/notes/37_GEOMETRY_DISCUSSION_AND_RETURN_CONTINUATION_20261028.md
[n38]: ../../05_radial_theta_collision_geometry/notes/38_AUXILIARY_SOURCE_FLOWS_AND_COLLISION_RESPONSE_20261028.md
[b08]: ../../05_radial_theta_collision_geometry/brainstorm/08_ZERO_TIME_RESCALINGS_AND_FLOW_BRAINSTORM_20261028.md
[results]: ../../../../result-summaries/README.md
[heat]: ../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../result-summaries/16_hypercomplex_reductions_and_geometric_realizations.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a03]: ../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md

[progress]: ../research-progress/01_AUXILIARY_COLLISION_FLOWS_RESEARCH_PROGRESS_20261028.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[brainstorm]: ../brainstorm/01_AUXILIARY_FLOW_PAYOFFS_AND_COMPARISON_20261028.md
[survey]: ../lit-survey/01_AUXILIARY_COLLISION_FLOWS_ANNOTATED_LITERATURE_SURVEY_20261028.md
[stable-models]: ../../../../result-summaries/17_constructive_stable_model_obstructions.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a06]: ../../../../avoid/06_status_stronger_than_the_evidence.md
[a10]: ../../../../avoid/10_numerics_ahead_of_the_question.md
[a11]: ../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[a17]: ../../../../avoid/17_parallel_writers_and_broken_registries.md

[n31]: ../../05_radial_theta_collision_geometry/notes/31_CANONICAL_SOURCE_RELATION_AND_PREPARATORY_COMMUTATOR_20261028.md
