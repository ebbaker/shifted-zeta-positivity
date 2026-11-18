# Continuation31 — From lattice compatibility to a concentration estimate

18 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. Actual model and effort unavailable in the
current guarded chat registry; helper settings inherited. Model names
below are recommendations under the project workflow, not serving claims.

## Read first and resume from the present milestone

Read the [sole progress register](../research-progress/01_VCD_GT_CM_RESEARCH_PROGRESS_20261117.md),
[overview](../research-overview/01_VCD_GT_CM_RESEARCH_OVERVIEW_20261117.md),
[plan](../research-plan/01_VCD_GT_CM_RESEARCH_PLAN_20261117.md),
[Integration30](30_VCD_GT_CM_COUPLED_LATTICE_MANUSCRIPT_INTEGRATION_20261118.md),
and [Review14](../reviews/14_VCD_GT_CM_E27_INTEGRATED_MANUSCRIPT_ASSESSMENT_20261118.md).
Then read [result summaries](../../../../../../result-summaries/README.md),
specifically [cluster18](../../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md)
and [collision controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
and [avoid](../../../../../../avoid/README.md), specifically
[classification01](../../../../../../avoid/01_restating_the_target.md),
[premises02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[coordinate changes03](../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [joint bounds12](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
The register alone owns current verdicts. Do not restart the original
complex-p setup or repeat a completed acquisition pass as new research.

The existing [manuscript](../manuscript/main.tex) now systematically develops
the coupled p,q,zero-index lattice, initial and joint-time comparisons,
canonical source acquisition and compact stopped-region logic. The
61-page [reading PDF](../../../../../../output/pdf/vcd-complex-p-mellin/complex_power_evolution.pdf)
is under ignored output. Full derivations are primary; Appendix B is
supporting inherited numerical evidence. E27's two clarification repairs
leave every formula and constant unchanged. There is no claimed new
zero coverage, stable finite closure or improvement of Lambda.

## The exact structure now available

Use M_n(p,q)=sum_{rho!=x_n,x_(n+1)}(rho−x_(n+1))^(−p)(rho−x_n)^(−q),
not independently assigned rows. For g_n=x_(n+1)−x_n and D_n=g_n²/4,

    g_n' = 4/g_n − 2g_n M_n(1,1),
    M_n(r,0)+(−g_n)^(-r)=M_(n+1)(0,r)+g_(n+1)^(-r), r>=2,
    B=H_z/H,    B_t=−B_zz−2BB_z,
    U_n=H_zz(x_n)/(2H_z(x_n)),
    sum_{n=l}^r g_n M_n(1,1)
       =2 sum_{n=l}^r 1/g_n−U_(r+1)+U_l.

The common meromorphic field generates all split moments. Strictly
separated simple charts suffice for these local formulas; all-gap
positive sums additionally require the complete divisor to be real.
The boundary identity retains correlations that independent row-error
bounds discard. Uncertain gaps still require reciprocal-error payment.
A common finite polynomial heat field preserves these identities exactly
on its own simple charts, but approximation of the canonical field over
one fixed interval has not been proved here.

**A block flux identity alone does not prevent an individual gap from
closing.** Nor does one merging pair's S/T regularity make its neighboring
edge charts regular. A successful next estimate must address concentration
and the correct chart/stop boundary, rather than increase the number of
formal lattice coordinates.

## Default next decision: B08 r2 / B / Astra

This is a **conditional next conceptual pass**, not an issued E packet.
Select at most two concrete source-specific quantities derived from the
shared B field or node forces that might control an individual-gap defect
or a maximum over a finite block through a physical time interval.
The preferred question is whether the common source can pay correlated
interior force differences, plus boundary and tail terms, with a useful
strict margin. Do not elevate that question into a theorem hypothesis
identical to the target conclusion.

For each candidate, state its exact class (representation, approximation,
conditional consumer or acquired estimate under avoid01), differential or
integral identity, canonical acquisition route, and the premise failed by
each relevant collision control. The polynomial and changed-source
controls need no numerical rerun; source equality, order, strip, count,
physical readout and integer multiplicity are separate premises.

Before any execution is issued, select one candidate and freeze:

- A concrete finite physical duration Delta and the compact pair/block,
  with independent source contour/count clearance and spatial buffers.
- The initial budget and a **strict** proposed margin after all errors.
  A stopped D>=d_stop region may infer positivity by exit exclusion;
  positivity over the desired interval may not be assumed to acquire it.
- Complete source/jet, exterior-tail, block-boundary, contour/quadrature,
  arithmetic, time-uniformity and reciprocal-gap errors. State the full
  divisor and common labels and how the estimate handles a changing
  minimizing index. Samples do not establish a time-uniform bound.
- A same-information direct comparator: common source jets or regular
  coupled D/M evolution with identical initial data, source accuracy,
  time interval and boundary payments. State the intended improvement
  in duration, margin, cost or coverage.
- One bounded E proof/acquisition task with acceptance test and a
  separate nonauthor check. If the finite comparison fails, preserve
  that scoped failure; do not launch a larger numeric campaign.

A time-dependent defect envelope or concentration functional would be a
new consumer and requires its own derivation. The exact block sum does
not already provide either. If neither candidate pays concentration,
record the missing source estimate and close that bounded pass without
claiming a universal obstruction.

## Results that constrain the next choice

Notes21 and23–25, with E22/E24, prove that the best unchanged initial-M
Riccati horizon is ~g²/4 at high canonical real-simple slices, versus
~g²/6 from two neighbors. Exact acquisition of the same initial quantity
cannot pay a fixed physical step at arbitrarily high height.

The joint variables V=1−2DM and K=2D²(12S_2+16DS_3) satisfy
D_u=−2V, V_u=(1−V²−K)/D. A whole-time K>=1−eta² and initial V<=v0
pay D>=D0−2vu, v=max(0,v0,eta). A growing canonical head acquires
v=O(log(X)^−3) on fixed positive-time slabs, hence relative squared-gap
loss O(Delta/log X). This overcomes the earlier shrinking allowance
there, but the imported source theorem already protects that exterior.
Do not present another proof of that known region as new coverage.
The source-jet and direct common-clock comparators use the same information;
the latter is sharper at fixed duration. Keep g and D error rates distinct.

Note27/E25 and manuscript Section13 select complete contour extraction
on arbitrary trial coordinates, including possibly nonreal exterior
zeros. The compact example asks for t=.1 to −.0003, Delta=.1003,
d_stop=.0001 and a proposed v=.89, with strict trial margin .0001028.
The included canonical t=0 slice forces |K|<.003, however, so the
**selected one constant-v barrier** allows <.0896. This is not a failure
of all constant-K comparisons, which may retain the initial transient,
nor of time-varying K, refreshed anchors, regular coupled dynamics or
the contour source itself. No negative-time source certificate was
acquired. More precision cannot repair the rejected consumer.

The OC interface audit20 remains scoped: fixed projections and later
finite certified scalar/census results do not automatically supply
ordered adjacent-gap or whole-time zero-exception input. Give any reused
source its actual theorem scope and complete error budget.

## Independently optional E16 r3 / E / Sol

Use [E16 r3](../research-progress/handoffs/VCD-GT-CM-E16-r3.md) with its
[seven current pins](../research-progress/handoffs/VCD-GT-CM-E16-inputs-r3.json)
and full r1 contract. Only the framework source binding changed after
manuscript integration; all scientific obligations and finite work limits
remain unchanged. This proof seeks common-time finite-field/jet/pair/moment
errors at fixed height. It remains unexecuted and does not itself acquire
a favorable sign. A later finite-block extension must separately pay all
charts, labels, denominators and uncertainty sums; it is not implicit in
the single-pair contract. E16 need not be completed before B08 r2.

## Records and a next-session prompt

Save new derivations in notes/, small executions in numerics/, assessments
in reviews/, and frozen requests/returns in research-progress/handoffs/.
Update this investigation's overview/plan only when the decision changes;
keep the sole register and concise DRAFT_HISTORY milestones current.
Preserve original notes and pin histories. Use the guarded chat recorder
for thread 01a1eecb-7917-7262-90a7-07067b76815f in this investigation's
chat-histories; refresh at the next turn and arrange the bounded exact-turn
follow-up last. Record actual metadata, never infer missing settings.

Suggested prompt:

> Read Continuation31, Review14, manuscript Sections4 and11–14, and the
> sole register with result/avoid routing. Open a bounded B08 r2 conceptual
> pass: select one common-source coupled-lattice quantity that can control
> individual-gap concentration over a finite physical interval. Derive
> the relevant identity, pay boundary/tail/time and reciprocal-gap errors,
> and state duration, strict margin and the same-information comparator
> before issuing execution. Do not treat block telescoping as a minimum
> bound or rerun known high-exterior coverage. Keep E16 r3 independently
> optional and preserve the scoped compact constant-v rejection.
