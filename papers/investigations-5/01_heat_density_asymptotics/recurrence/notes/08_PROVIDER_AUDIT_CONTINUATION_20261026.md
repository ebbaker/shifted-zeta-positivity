# Continuation for certified evaluation of the recurrence hierarchy

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Recurrence chat0002, thread `01a176bf-7fd6-7fa2-ad1c-0fe1585f43c6`.

**Next session: Analysis — Sol, HDA-R05-AN03 r1. READY_FOR_SOL, not
executed.** The [bounded request](../research-progress/handoffs/HDA-R05-AN03.md)
is the execution contract; the [progress register][progress] owns live
status. This note supersedes Note01's opening three-round sequence for
next-session routing. Those comparisons and the two subsequent R05
audits are completed at their bounded scopes.

## Where the research stands

The [27-page analytical manuscript](../manuscript/main.tex) now derives
the fixed-order and fixed compact-time hierarchy, controlled order
growth, RS analytic quadrature, and conditional evaluation bounds.
Its Sections 1.1 and 4.5 explain what the preceding simplest and higher
approximations retain. Every frozen level keeps all arithmetic modes
and matches its fluctuation order p with RS order K=2p; p=1 retains
C0--C2 and p=2 retains C0--C4. The earlier target-dependent first
correction has a different differentiated formula and residual.

The reusable results are natural-scale O(X^-(p+3/4)) for each fixed p
on declared fixed compact positive T-intervals, and outer accuracy
exp(-L²/4) for p=floor(L/2), K=2p on [1,2]. Note06 adds sufficient
finite evaluation-error conditions, analytic O(L²)-node Gauss quadrature
per branch, and requested normalized accuracy
3L²/(8log2)+O(Llog L) bits. These do not yet certify the computational
providers or a concrete evaluator. Broad R05 remains **Partial**.

The next gain is analytical: construct finite provider algorithms and
prove that their delivered errors meet the existing inequalities.
Numerical implementation and sampled checks are later supporting work.
The source notes have same-model internal assessments; the manuscript
has a same-session authoring assessment. Neither supplies independent
specialist validation.

## Read in this order

1. Repository AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md, LARGE_FILES.md,
   REFERENCE_WORKFLOW.md and tools/CHAT_HISTORY.md. Refresh this chat's
   existing registration, or register a genuinely new research chat in
   recurrence/chat-histories/ with its own identity. Record actual model
   and effort; do not infer them from the recommended owner.
2. The [current overview][overview], [live register][progress], and
   [AN03 r1 request](../research-progress/handoffs/HDA-R05-AN03.md).
3. [Note06][evaluation], especially E4--5, E9--11, E18--29 and its final
   provider gates; [Review05][evalreview]; and the
   [AN02 return](../research-progress/handoffs/HDA-R05-AN02.md).
4. [Note05][growth] for the chosen order, structural gates and half-target
   truncation onset. Use manuscript Sections 6--8 for the coherent
   derivation, and [Note07][integration]/[Review06][integrationreview]
   for integration scope. The [planning input record][inputs] identifies
   source versions; recheck current files and record any differences.
5. The [result index][results], [heat-flow cluster][heat],
   [control screen][controls], [avoid index][avoid] and
   [separate-error pattern][separate]. Read new primary sources only for
   specific missing provider estimates; do not import unverified blanket
   precision conclusions.

## First working step and completion test

Start by constructing a contract table with one row for each required
provider: supported input domain, finite algorithm, truncation error,
rounding error, delivered quantity, and the Note06 inequality it must
satisfy. Fix the exact-input/frozen-descriptor or certified guard-strip
model before choosing precisions. Then follow AN03's four ordered stages:
descriptor geometry, scalar/gamma data, RS/Gauss data, and the composed
finite budget. Routine derivations are part of the assignment.

Reserve half of exp(-L²/4) for the already-proved truncation. The remaining
center-normalized budget is
\(\varepsilon_X=c_o e^{-3L^2/8}/(2C_\chi)\): scale error consumes at
most epsilon_X/2 and each of the five evaluation categories at most
epsilon_X/20, as in E5. Keep all modes, both arms, the bounded integral,
the unit buffers and every specified derivative channel.

A successful return replaces named provider assumptions by proved
algorithmic bounds for a declared input class. If a construction cannot
meet one inequality, save that precise gap and the attempted route;
do not present the original conditional specification again as a new
closure. The frozen symbolic heat residual and independently rounded
channel defects remain distinct; a residual_z output requires its own
mixed channel. Preserve the true input and endpoint costs.

Save the proof/attempt in notes/, an internal assessment in reviews/, and
small provenance records; append the packet return/disposition and
update the sole register. Do not rerun R01--R03 or AN01--AN02 merely to
reconstruct context. The manuscript sources and existing build record
already identify the current draft.

## Priorities after the bounded audit

The next follow-up is useful total cost and height onsets, including
provider bit costs, storage and every one of the N arithmetic modes.
After its disposition, consider a specified joint time/order/height
limit, then a quantitative continuous deformation or reconstruction
gain, and the parent physical consumers. Independent mathematical
validation remains a standing need across the program. R04/R06 are
NOT_STARTED; HDA-A02 Partial, HDA-17 Partial, HDA-18 Gated and HDA-20
unfulfilled are unchanged.

This is an approximation/evaluation milestone under [avoid01][target],
not an RH criterion. Euler-factor/finite-prime controls fail the full
unchanged canonical coefficients; weighted-square/cutoff controls fail
the full canonical completion; reflected, smooth and positive-primitive
controls lack the same gamma/arithmetic identity. Their heat identities
can survive. No collision or physical conclusion follows from exact
evolution or numerical accuracy alone.

## Prompt for the next session

> Continue the recurrence investigation from
> `notes/08_PROVIDER_AUDIT_CONTINUATION_20261026.md` and execute
> `research-progress/handoffs/HDA-R05-AN03.md`, request r1. Keep the work
> analytical. Construct certified finite provider algorithms that meet
> Note06's actual input, geometry and rounding inequalities for the
> exp(-L²/4) target, or identify the first precise unpaid provider bound.
> Preserve the canonical model, full arithmetic population and retained
> RS integral. Save the proof or bounded attempt, internal assessment,
> provenance and packet disposition, and update the overview and sole
> progress register. Do not start a numerical campaign or the later
> research tasks.

[progress]: ../research-progress/01_RECURRENCE_RESEARCH_PROGRESS_20261026.md
[overview]: ../research-overview/01_RECURRENCE_RESEARCH_OVERVIEW_20261026.md
[evaluation]: 06_COEFFICIENT_ROUNDING_AND_RS_QUADRATURE_20261026.md
[evalreview]: ../reviews/05_EVALUATION_ERROR_ASSESSMENT_20261026.md
[growth]: 05_CONTROLLED_ORDER_GROWTH_AUDIT_20261026.md
[integration]: 07_MANUSCRIPT_INTEGRATION_20261026.md
[integrationreview]: ../reviews/06_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261026.md
[inputs]: 08_PROVIDER_AUDIT_CONTINUATION_INPUTS_20261026.json
[results]: ../../../../../result-summaries/README.md
[heat]: ../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[separate]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[target]: ../../../../../avoid/01_restating_the_target.md
