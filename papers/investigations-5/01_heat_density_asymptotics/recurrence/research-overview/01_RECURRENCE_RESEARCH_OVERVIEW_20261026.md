# Research overview: recurrence and fluctuation hierarchies

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**.
Current synthesis and priority refresh: recurrence **chat0005**, thread
`01a1785a-2938-7de0-adc4-3b60db706199`. The source analytical returns in
Notes02–06 and09–11 and supporting Note12 were developed with
**gpt-6.1-sol, ultra**; their original provenance is retained.

## Current accomplishment

The [maintained manuscript](../manuscript/main.tex) now joins the fixed-order
hierarchy, controlled order growth, modular evaluation budget, finite
provider algorithms, explicit calibration, all-height onset, and total
bit-work/storage bounds. [Integration Note14](../notes/14_EFFECTIVE_MANUSCRIPT_INTEGRATION_20261026.md)
records source correspondence and checks. The complete canonical field
evaluator remains unimplemented/uncertified. Broad **HDA-R05 stays Partial**.
The [sole progress register](../research-progress/01_RECURRENCE_RESEARCH_PROGRESS_20261026.md)
owns execution status; the [continuation](../notes/15_ANALYTIC_STRENGTHENING_CONTINUATION_20261026.md)
owns the next-session handoff.

The immediate primary task is **Analysis — Sol,
[HDA-R05-AN06 r1](../research-progress/handoffs/HDA-R05-AN06.md), READY_FOR_SOL,
not executed**: sharpen the sufficient all-height onset at unchanged
accuracy and frozen choices. The existing [N02 provider packet](../research-progress/handoffs/HDA-R05-N02.md)
remains ready as a supporting component task, with its original finite
cases/caps. It is not a prerequisite for the onset proof and is no longer
the primary research recommendation. No task is dispatched by this update.

## Established analytical results

All rows retain the source status **proved in-note from named inputs**,
with same-model internal assessments. Manuscript synthesis and selected
source-formula checks do not supply independent specialist validation.

| Result | Scope and quantitative gain | Source and limit |
| --- | --- | --- |
| Fixed-order hierarchy | Every fixed p>=1 with K=2p gives natural gamma-scale O(X^-(p+3/4)); field, spatial orders0–3 and first time together. | [Note03](../notes/03_FIXED_ORDER_FLUCTUATION_HIERARCHY_20261026.md); the p=2 base is [Note02](../notes/02_FIRST_FINITE_FLUCTUATION_COMPARISON_20261026.md). |
| Compact time family | Same rate for each fixed 0<tau<=T<=B, with explicit endpoint costs and onsets. | [Note04](../notes/04_COMPACT_TIME_RECURRENCE_FAMILY_20261026.md); no moving-endpoint theorem. |
| Controlled order growth | p=floor(L/2),K=2p gives outer-envelope error exp(-L²/4), L=log(X/(4pi)), on [1,2]. | [Note05](../notes/05_CONTROLLED_ORDER_GROWTH_AUDIT_20261026.md); simultaneous factorial costs and true/artificial tails. |
| Modular evaluation budget | Scale, input, RS data, geometry, quadrature and circuit errors preserve the same target; O(L²) outer nodes per branch. | [Note06](../notes/06_COEFFICIENT_ROUNDING_AND_RS_QUADRATURE_20261026.md); delivered-data contracts supplied by later notes. |
| Finite provider constructions | Rational elementary tails, normalized gamma data/scale, Gauss and pole-safe RS coefficients, exact interior guards. | [Note09](../notes/09_FINITE_PROVIDER_ALGORITHMS_20261026.md); dyadic centers with strict descriptor witnesses, exact rational queries; separation remains. |
| Polynomial providers and full cost | Shifted Stirling jets and exact Legendre variation counts; effective C(N+1)Q^40 work and CQ^20 streamed space. | [Note10](../notes/10_EFFICIENT_PROVIDERS_AND_TOTAL_COST_20261026.md); all N~sqrt(X) modes remain, bounds are loose. |
| Explicit uniform calibration and onset | H=A=C_Gamma=c_o=1,D=4,D0=3,g_-=1/64,C_tail=640,M_H^*=1/4,C_chi=3^d,C_cal=32+d. L_*=2^22(d+1)^4, d=ceil(r+b+2). | [Note11](../notes/11_EXPLICIT_CALIBRATION_AND_HEIGHT_ONSET_20261026.md); X_*=2^(2L_*+8) is a stronger sufficient condition; no practical-height claim. |
| Effective composition | Those finite algorithms and constants close the modular contracts on the accepted input class. Sufficient delivered precision is 3L²/(8log2)+O_(r,b)(L log L). | Manuscript effective evaluation and bit-cost theorems; input length, provider-internal work and center separation are counted separately. |

Supporting finite gamma/Gauss implementation and replay are recorded in
[Note12](../notes/12_PROVIDER_IMPLEMENTATION_REPLAY_20261026.md) and
[Review10](../reviews/10_PROVIDER_REPLAY_ASSESSMENT_20261026.md); the
[chat0003 summary](../notes/13_CHAT0003_RESULTS_SUMMARY_20261026.md) gives
their context. These finite checks support components and do not prove
the analytical theorems or certify the complete field calculation.
Detailed numerical tables and measurements stay in those linked notes.

## Canonical model and retained information

Keep h(T,z)=H(-T,z), h_T=h_zz and H(0,z)=xi((1+iz)/2)/8.
On each fixed chart, N=floor(sqrt(X/(4pi))) and all coefficients,
partitions and endpoints are frozen under differentiation. The hierarchy
organizes the logarithmic gamma curvature by fluctuation weight, with
j U_j=sum_(r=1)^j r c_r Q_T^(r+1) U_(j-r), Q_T=d+2T partial_d.
Both arms, all n<=N, every chosen coefficient, the exact cutoff transfer,
and the bounded real RS completion remain. Exact heat evolution and
canonical approximation are separately proved.

The first frozen level retains C0–C2 and gives X^-7/4; the second retains
C0–C4 and gives X^-11/4. The preceding simplest and first-correction
ansatz allowances X^-3/4 and X^-5/4 keep their own formulas/domains.
The earlier target-dependent correction agrees at the center with the
first frozen arithmetic value but has different differentiated formulas.
These are upper allowances, not pointwise monotonicity of actual error.
The earlier ansatz growing-degree approximation also retains its separate
status; the recurrence theorem establishes the fluctuation grading.

## Ordered analytical agenda

| Priority | Proof deliverable and measurable gain | Supporting checks and boundary |
| --- | --- | --- |
| 1. Sharper sufficient onset | [AN06 r1](../research-progress/handoffs/HDA-R05-AN06.md): replace the largest coarse moment/factorial/logarithmic envelopes, derive an explicit smaller all-height threshold with the same p,K,V, target, buffers and channels. Prove coverage through every floor jump. | Optional finite interval evaluation can check derived inequalities or identify their dominant term. A passed height or fitted law does not close the task. |
| 2. Better coefficient/integral bounds | Prove uniform local pole cancellation, normalized-jet tails and C_k propagation, or sharpen ellipse/contour majorants. Require a strict finite bound or cost improvement over the current construction at identical accuracy. | N02's bounded replay can test a proved method. Preserve its cap and report a stopped method; no forced large contour run. |
| 3. Joint time/order/height | Declare a specific tau(X),B(X),p(X). Start with a lower endpoint tending toward zero and fixed upper endpoint; pay exp(Y²/(4tau)), inverse-time channels and every tail simultaneously. | Numerical time samples cannot establish uniformity. The compact-family theorem and sibling through-zero/positive-time results retain their own scopes. |
| 4. Arithmetic compression or continuous deformation | Prove reconstruction in the same field/derivative norm and quantify a reduction of the N-mode cost, or a uniform continuous-s remainder. | R04/R06 NOT_STARTED; exact identities, small model examples and moment closure analogies alone are insufficient. |
| 5. A specified physical consumer | Derive an explicit observable/covariance/joining-defect bound, including regulator dependence, from the required channels. | Parent ownership unchanged. Select checks only after the analytic consumer and its error budget are specified. |

Independent specialist review and checking the primary coefficient proofs
remain standing needs throughout. The declared source identities and
remainder domains must be retained; selected Part II identities do not
license its preliminary precision conclusions.

The full implementation remains a separate delivery obligation within
R05: RS jets/coefficients, large phases and common scale, frozen center/
guard geometry, retained-integral data and the complete mode/derivative
circuit. Its finite certificates should exercise an already stated
analytic contract and reject altered witnesses. No unbounded field or
height sweep is a priority of this agenda.

## Scope, controls and evidence discipline

This is an approximation/evaluation milestone under
[avoid01](../../../../../avoid/01_restating_the_target.md), not an RH
criterion. Read the [result index](../../../../../result-summaries/README.md),
[heat cluster](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[control screen](../../../../../result-summaries/12_collision_controls_and_screening.md)
and [avoid index](../../../../../avoid/README.md), especially
[separate bounds](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [shared-premise review limits](../../../../../avoid/05_same_model_reviews_and_shared_premises.md).
Euler-factor/finite-prime controls lack unchanged canonical coefficients;
weighted-square/cutoff controls lack the full canonical xi/RS completion;
reflected, smooth and positive-primitive controls lack the same complete
gamma/arithmetic identity. Their heat equations can survive. This checks
applicability premises; it supplies no collision exclusion.

HDA-A02 Partial, HDA-17 Partial, HDA-18 Gated and HDA-20 unfulfilled remain
unchanged. Detailed earlier requests and dispositions remain in the sole
progress register, source notes and their registered chats. This overview
supersedes their earlier next-task recommendations, not their results.
