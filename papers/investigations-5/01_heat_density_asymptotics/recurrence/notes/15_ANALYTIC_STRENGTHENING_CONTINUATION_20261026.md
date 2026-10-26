# Continuation: strengthen the effective recurrence theorem analytically

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Recurrence **chat0005**, thread 01a1785a-2938-7de0-adc4-3b60db706199.
Source analytical results retain their **gpt-6.1-sol, ultra** attribution.

## Completed in this session

The [maintained manuscript](../manuscript/main.tex) now incorporates all
analytical results through Note11. Its 42-page [reading copy](../../../../../output/pdf/heat-density-recurrence/heat-density-recurrence.pdf)
moves from canonical approximation and controlled order growth through
finite constructions and explicit calibration to effective evaluation
and full-population bit-work/storage bounds. Elementary algorithm details
remain in appendices. Numerical evidence is cited only as support, with
links to the existing notes for details.

[Integration Note14](14_EFFECTIVE_MANUSCRIPT_INTEGRATION_20261026.md),
[its input manifest](14_MANUSCRIPT_INPUTS_20261026.json),
[Review11](../reviews/11_EFFECTIVE_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261026.md)
and the [build record](../manuscript/BUILD_RECORD_20261026.json) record
source correspondence, scope and production checks. The local and
desktop compiler builds pass. All 42 pages were rendered and inspected;
the installed render matches, and the final local log has no unresolved
references, warnings, or overfull/underfull boxes. Supporting-note links
in the reading PDF resolve from its documented output folder.

The [overview](../research-overview/01_RECURRENCE_RESEARCH_OVERVIEW_20261026.md)
and [sole progress register](../research-progress/01_RECURRENCE_RESEARCH_PROGRESS_20261026.md)
are current. Their primary recommendation is analytical strengthening,
with computations chosen only to support a stated proof goal. The
integration does not add a new theorem or independent validation.
R01–R03, AN01–AN05 and N01 remain CLOSED at their bounded scopes;
broad R05 remains Partial at complete software and certification.
R04/R06 are NOT_STARTED. HDA-A02 Partial, HDA-17 Partial,
HDA-18 Gated and HDA-20 unfulfilled remain unchanged.

## Primary next task

**Analysis — Sol: [HDA-R05-AN06 r1](../research-progress/handoffs/HDA-R05-AN06.md),
READY_FOR_SOL, not executed.** Sharpen the explicit sufficient all-height
onset while keeping the existing error target and frozen choices.

The baseline is L_*=2^22 nu^4, with
L=log(X/(4pi)), nu=ceil(r+b+2)+1 and the sufficient dyadic
X_*=2^(2L_*+8). Retain p=floor(L/2), K=2p, V=8sqrt(2)L,
1<=T<=2, exact input/descriptor restrictions, both arms, every n<=N,
all RS coefficients through K, the cutoff transfer, bounded real integral,
buffers, spatial orders0–3 and first time derivative. Half of the
exp(-L²/4) allowance remains reserved for truncation.

The deliverable is a smaller explicit threshold or a terminating
construction with a proved continuous all-height envelope. Identify
where the coarse factorial, moment and logarithmic envelopes dominate.
Prove every structural/calibration/truncation gate through every p,N
jump, and rigorously quantify improvement on a declared chart family.
The existing theorem remains a fallback. A single-height certificate
or fitted numerical pattern cannot close this task. If no improvement
closes, return the exact unresolved inequality and the attempted class.

No numerical campaign is required. Any finite supporting check must be
declared in advance, evaluate an already stated analytic inequality,
and obey its case/resource cap. It must not become a full-field sweep or
a search near the enormous closed height.

## Reading order

1. Repository [AGENTS.md](../../../../../AGENTS.md),
   [LARGE_FILES.md](../../../../../LARGE_FILES.md), and
   [chat capture workflow](../../../../../tools/CHAT_HISTORY.md).
2. The [result index](../../../../../result-summaries/README.md),
   [heat-flow cluster](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
   [control screen](../../../../../result-summaries/12_collision_controls_and_screening.md),
   [avoid index](../../../../../avoid/README.md), especially
   [milestone classification](../../../../../avoid/01_restating_the_target.md),
   [shared-premise limits](../../../../../avoid/05_same_model_reviews_and_shared_premises.md)
   and [separate error bounds](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
3. Current overview, sole register, this note and the exact AN06 r1 packet.
4. Manuscript sections 5, 7, 9 and 10, with appendices A–B; then
   [Note05](05_CONTROLLED_ORDER_GROWTH_AUDIT_20261026.md),
   [Note06](06_COEFFICIENT_ROUNDING_AND_RS_QUADRATURE_20261026.md),
   [Note10](10_EFFICIENT_PROVIDERS_AND_TOTAL_COST_20261026.md) and
   [Note11](11_EXPLICIT_CALIBRATION_AND_HEIGHT_ONSET_20261026.md).
   Use [Note09](09_FINITE_PROVIDER_ALGORITHMS_20261026.md) for the exact
   input class and delivery contract.
5. [Review04](../reviews/04_CONTROLLED_ORDER_GROWTH_ASSESSMENT_20261026.md),
   [Review05](../reviews/05_EVALUATION_ERROR_ASSESSMENT_20261026.md),
   [Review07](../reviews/07_FINITE_PROVIDER_ALGORITHM_ASSESSMENT_20261026.md),
   [Review08](../reviews/08_EFFICIENT_PROVIDER_AND_COST_ASSESSMENT_20261026.md),
   [Review09](../reviews/09_EXPLICIT_CALIBRATION_ASSESSMENT_20261026.md),
   [source audit04](../references/04_EFFICIENT_PROVIDER_SOURCE_AUDIT_20261026.md)
   and [source audit05](../references/05_EXPLICIT_CALIBRATION_SOURCE_AUDIT_20261026.md).
   Note14/Review11 explain integration choices without replacing the sources.

Record the actual model/effort and exact input versions before execution.
Advance AN06 from READY_FOR_SOL only when it is resumed. Save the proof
and assessment in the next available notes/ and reviews/ numbers, update
the packet return/disposition and sole register, and integrate a new
result only when its stated proof obligation has closed.

## Subsequent analytical work and supporting software

After the onset comparison, the strongest analytical directions are:
uniform improvements to pole-safe coefficient/integral bounds at identical
accuracy; a specified moving lower time endpoint with all moments, buffers
and inverse-time factors paid; a reconstruction theorem that quantifies
arithmetic compression or continuous deformation; and an error estimate
for a specified physical consumer. Independent specialist review of the
named source chain and composed argument remains useful throughout.

The existing [HDA-R05-N02 r1](../research-progress/handoffs/HDA-R05-N02.md)
remains READY_FOR_SOL as a separate bounded supporting task for normalized
F_0 jets and weighted C_k delivery. Its original cases, resource caps and
stop rules remain unchanged. It is not a prerequisite for AN06.
[Note12](12_PROVIDER_IMPLEMENTATION_REPLAY_20261026.md),
[Review10](../reviews/10_PROVIDER_REPLAY_ASSESSMENT_20261026.md) and
[Note13](13_CHAT0003_RESULTS_SUMMARY_20261026.md) contain the finite
component evidence and limitations. No new thread, agent or numerical
run was dispatched in preparing this continuation.

This is an approximation/evaluation milestone, not an RH criterion.
Euler-factor/finite-prime controls lose the unchanged canonical
coefficients; weighted-square/cutoff controls lose the full canonical
xi/RS completion; reflected, smooth and positive-primitive controls lose
the same complete gamma/arithmetic identity. Their heat equations can
survive. The applicability screen supplies no collision exclusion.

## Verified conversation provenance

The [history verification receipt](15_CHAT_HISTORY_VERIFICATION_20261026.json)
was recorded after manuscript installation. Under the shared registry
lock, all five recurrence captures passed stored-byte and canonical-content
hash checks, identity/number checks, linear public-message and count
checks, and unique-registration checks across the repository's papers
history directories. The current capture also matched the completed
public source exactly, including the preceding final reply and this
manuscript request.

Current identity: **Summarize heat density results**, recurrence chat0005,
[canonical archive](../chat-histories/0005_2026-10-26T13-15-37Z_summarize-heat-density-results.json).
Creation and first-capture provenance, filename and number are preserved.
The receipt records 14 completed public messages at
2026-10-26T14:28:59.825Z, with verification at 2026-10-26T14:30:21.624479+00:00.
The live index owns later counts and hashes; no archive JSON was edited
by hand, moved, copied or renumbered.

This point-in-time receipt precedes the current final reply. The standing
workflow refreshes completed public text again and launches the bounded
exact-turn follow-up as the last tool action. At the next turn, verify that
worker's result or refresh the unique registration to include the real
final message. No native completion-hook activation is claimed.

## Pasteable next-session request

Continue the recurrence investigation under HDA-R05-AN06 r1. Read
notes/15_ANALYTIC_STRENGTHENING_CONTINUATION_20261026.md, the current
overview and sole progress register, then the exact handoff and source
notes it identifies. Sharpen the sufficient all-height onset at the
unchanged exp(-L²/4) field/derivative accuracy, p=floor(L/2), K=2p,
V=8sqrt(2)L and time interval [1,2]. Preserve exact input restrictions,
all modes, coefficients, buffers, cutoff transfer and the retained
completion integral. Prove every gate through every floor jump and
compare the improved bound with L_*=2^22 nu^4; retain the old bound
as a fallback. Prioritize the analytic proof, using only declared
bounded checks in support. Save the proof, assessment, precise limits
and disposition; update the overview/progress and manuscript only for
a closed result. Preserve and refresh this conversation's unique
history registration, verify its integrity, and write a continuation.
