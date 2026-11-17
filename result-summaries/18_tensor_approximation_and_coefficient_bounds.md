# Tensor approximation and coefficient bounds

14 November 2026, America/New_York. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance. Coordinator backend/effort unavailable; B workers explicitly dispatched **gpt-6-astra / ultra**, E proof/assessment workers **gpt-6.1-sol / ultra**. Dispatch metadata is distinct from backend attestation.

## Summary

Investigation 6's first bounded round gives quantified approximation results for the complete theta source, retaining \(H=\frac12\int W e^{izu}\,du\).

- **Coefficients:** \(\beta_n+\beta_{n+1}\le\operatorname{arcosh}^2(2n+12)/16\), all integer \(n\ge0\), uniformly \(0\le\lambda\le1/2\). Integration by parts and a convex exponential confinement bound prove the estimate from the complete source. Positive weighted-square collision controls can also satisfy it.
- **Finite chain:** the normalized scalar error is at most \(h_N^*\sum_{k=0}^N\tau^kx^{2N-2k}/[k!(2N-2k)!]\). Combining the coefficient envelope gives error at most \(H_{1/2}(0)\varepsilon\) on \(0\le\tau\le1/2, |x|\le X\), for \(N=\lceil4K\log(16K)\rceil\), \(K=X+\log(1/\varepsilon)+1\), \(0<\varepsilon\le1\). This is a sufficient depth, not optimal or measured cost.
- **QTT:** an exact-coefficient polynomial construction has formal rank at most 641 and scaled error below \(2^{-36}\) on its fixed height/offset box. Direct integration of the same polynomial removes the midpoint allowance.
- **Exact cell phase:** weighted source projection and exact sinc readout give absolute error below \(5\cdot10^{-7}\) at \(U=2,L=30\), for every real height, \(|\Im z|\le8\) and allowed time. The fixed center-phase lattice has actual all-real-height error at least \(Z_\lambda/2\).

## Status

Source status: **proved in-note**. Separate same-worker internal assessments accept the fixed bounds without correction. Shared-source checking does not supply independent specialist review. No numerical campaign or interval certificate was produced. The [shared proof](../papers/investigations-6/notes/03_TN6_E01_COEFFICIENT_TO_SCALAR_TRANSFER_20261113.md) states: “Actual state-prefix error and a speed advantage remain unestablished.”

## Caveats

The chain is exactly Gaussian quadrature; its finite coefficients and certified evaluation are unpaid. QTT's source coefficients and ITP's \(2^{32}\) formal masses are exact mathematical inputs, not acquired data. These absolute allowances provide neither relative accuracy at zeros nor a signed-field result. The lattice obstruction is restricted to fixed point-phase cells in a uniform all-height norm. See [controls 12](12_collision_controls_and_screening.md).

## Reusable for

Explicit finite-chain remainder/depth estimates; a full-time coefficient envelope; complete-source approximation error ledgers; separation of phase integration from point-phase aliasing. A new acquisition or signed consumer needs its own bounded contract.

## Where

The [roundup](../papers/investigations-6/notes/04_FIRST_RESEARCH_ROUND_RESULTS_20261114.md) links all four proofs, frozen requests and assessments. The [shared assessment](../papers/investigations-6/reviews/01_TN6_E01_TRANSFER_ASSESSMENT_20261113.md) covers composition. The [continuation](../papers/investigations-6/notes/05_RESEARCH_CONTINUATION_AND_MODEL_HANDOFF_20261114.md) proposes a bounded coefficient-acquisition decision; it does not activate a new campaign.


## Finite acquisition update — 14 November 2026

For Edward Baker with OpenAI Codex assistance; B02 dispatched Astra/Ultra,
E02 and its separate internal E03 assessment Sol 6.1/Ultra; coordinator
backend/effort unavailable. The earlier statements that no interval
certificate exists and coefficient acquisition is unpaid are **superseded
only for the following finite tuple**.

[E02](../papers/investigations-6/notes/06_TN6_E02_CERTIFIED_COEFFICIENT_ACQUISITION_20261114.md)
records “certified within the frozen execution scope”: N=16, seventeen
complete-source even moments and sixteen positive coupling enclosures.
At 256 bits, the ideal nominal scalar has normalized absolute error
below 1.515e-25 on 0<=tau<=1/2, |x|<=8, in units of H_(1/2)(0). Nine
computed readouts meet that bound with rounding included. The 128-bit
coefficient-width gate failed and is preserved. [E03](../papers/investigations-6/reviews/02_TN6_E03_ACQUISITION_ASSESSMENT_20261114.md)
states “Accepted as a finite certificate at the issued scope.” Its one
unchanged replay matched the scientific payload; this remains internal
same-model, shared-premise review.

The chain's instrumented setup plus nine readouts took 1.288 s versus 0.535 s
for direct integration on the original run; achieved radii differ and no
speed law follows. This supplies reusable finite inputs and absolute
readouts, not signed, relative-error or increasing-height conclusions.
See the [roundup](../papers/investigations-6/notes/07_TN6_FINITE_ACQUISITION_ROUND_RESULTS_20261114.md)
and [current continuation](../papers/investigations-6/notes/08_TN6_CONTINUATION_AND_MODEL_HANDOFF_20261114.md).
The [editorial receipt](../papers/investigations-6/numerics/12_TN6_POST_ACQUISITION_GUIDANCE_UPDATE_20261114.json)
and [staging helper](../papers/investigations-6/numerics/prepare_tn6_e02_replay.py)
restore the exact pinned pre-update guidance for replay without changing
scientific inputs or their guards.


## Analytical manuscripts — 14 November 2026

For Edward Baker with OpenAI Codex assistance; manuscript and internal
review workers dispatched Sol 6.1/Ultra, coordinator backend/effort
unavailable. The [four-draft index](../papers/investigations-6/notes/09_ANALYTICAL_MANUSCRIPT_SCOPE_AND_RESULT_MAP_20261114.md)
now gives systematic derivations from the complete source through each
branch's quantitative results, ending with outstanding challenges.
The [cross-review](../papers/investigations-6/reviews/03_TN6_ANALYTICAL_MANUSCRIPT_CROSS_REVIEW_20261114.md)
states: “Accepted as analytical drafts within stated scope.” This is
internal shared-model review with JCH contributor overlap. It preserves
the earlier proofs' status; manuscript integration adds no new numerical
certificate or signed-field conclusion. The [current handoff](../papers/investigations-6/notes/10_ANALYTICAL_MANUSCRIPTS_CONTINUATION_AND_MODEL_HANDOFF_20261114.md)
prioritizes an analytical improvement with a named consumer. All PDFs
are external; editable TeX and small source/build records remain in-tree.


## Tail-score closure tests — 16 November 2026

For Edward Baker with OpenAI Codex assistance; lead backend/effort unavailable,
proof/assessment workers explicitly Sol6.1/ultra. Source status:
**proved in-note, internal analytical work**; E04 is **complete, checked in-note**.
[E09](../papers/investigations-6/03_volterra_coefficient_dynamics/reviews/04_VCD_E09_TAIL_SCORE_ASSESSMENT_20261116.md)
accepts notes04–08 “without mathematical correction within the stated scope”;
[E11](../papers/investigations-6/03_volterra_coefficient_dynamics/reviews/05_VCD_E11_SMOOTH_DEFECT_ASSESSMENT_20261116.md)
accepts note10. Same-model/shared-source internal assessment, not specialist review.

The [session synthesis](../papers/investigations-6/03_volterra_coefficient_dynamics/notes/09_VCD_CONNECTED_RESEARCH_SYNTHESIS_20261116.md)
routes the proofs: a fixed polynomial score leaves a residual
\(n+O_p(\log^{d+1}n)\); the exact reference
\(V_\lambda'=8\pi\sinh(4u)-2\lambda u+b\), bounded \(b\), gives relative
adjacent score error \(O(\log n/n)\). All exact canonical adjacent
identities identify theta under the stated exponential-integrability
hypotheses. The next adjacent defect cancels from the finite commutator.

Finite square-mode controls preserve any prescribed finite head/canonical
score rows and arbitrarily small bounded score difference while having
nonreal zeros; they lose higher smooth reflection. Separate smooth compact
multiplier controls preserve the full endpoint jet, real tails and common
envelope while changing the next defect; their zeros are open. Do not
merge these conclusions or infer failure of growing-degree compact
confinement. No signed Fourier margin, zero-strip theorem or numerical
certificate is supplied. Actual unscaled moving tail responses are also
unbounded across sites at fixed nonzero imaginary height.

## Midpoint comparison and calibration — 16 November 2026

For Edward Baker with Codex assistance; lead actual settings unavailable, proof/assessment dispatches Sol6.1/ultra. Source status **Complete, proved in-note**; [E14](../papers/investigations-6/03_volterra_coefficient_dynamics/reviews/06_VCD_E14_MIDPOINT_SESSION_ASSESSMENT_20261116.md) accepts within scope after synthesis wording clarification, with no proof correction. Separate internal shared-model review, not specialist independence.

[Synthesis15](../papers/investigations-6/03_volterra_coefficient_dynamics/notes/15_VCD_MIDPOINT_RESEARCH_SYNTHESIS_20261116.md) routes four results. E13 expresses both midpoint terms with one boundary memory. E15 proves that any entire scalar kernel shared consistently by those terms gives exactly its direct full-height Volterra response, with signed kernel-error transport and first discrepancy order 2N+q. E12 preserves finite canonical b/score/head and midpoint jets while varying the omitted response locally in a smooth compact-multiplier class; its zero locations remain open. E16 gives an additional factor theta^(r+1), 0<theta<1, over the same moment-only disk bound after exact c_0 derivative calibration and a common relative source tolerance. It states: “A uniform positive lower radius does not follow.”

The conditional calibration gain and finite freedom coexist. No model with those data/tolerances is constructed, no growing-height costs are paid, and no source-specific signed Fourier margin or zero induction is proved.

## Complete-source Fourier estimates — 16 November 2026

For Edward Baker with Codex assistance; lead actual settings unavailable,
proof/assessment dispatches Sol6.1/ultra. Source status **proved in-note**
(E17: **Complete, proved in-note**). [E20](../papers/investigations-6/03_volterra_coefficient_dynamics/reviews/07_VCD_E20_CANONICAL_FOURIER_ASSESSMENT_20261116.md)
records “Accepted in the stated scope.” Separate internal shared-model,
shared-source review; no mathematical correction or specialist independence.

[Synthesis19](../papers/investigations-6/03_volterra_coefficient_dynamics/notes/19_VCD_B05_CANONICAL_FOURIER_ESTIMATE_SYNTHESIS_20261116.md)
routes the complete-source contour allowance, exterior Fourier scales and
exact arithmetic normalization. At time zero and fixed (0<y<1), it gives
(|B(x+iy)|=O_y(e^{-pi x/8}x^{(13-y)/4})). E19 proves that every fixed real
projection of (B/(4pi F(z+4i))) is unbounded both ways on every height tail;
(|B|/[4pi(|F(z+4i)|-|F(z-4i)|)]) has infinite limsup. The source states:
“The uniform-in-height reverse-triangle comparison fails for the exact
canonical source itself.” This supersedes E18's pending comparison only
for that global consumer. The pointwise sufficient test remains valid.

The optimized contour-majorant asymptotic is not an actual-field lower bound.
No zeros, density, effective heights or degree induction are obtained.
Adaptive/correlated consumers and selected subregions remain outside the
obstruction. Reusable for Fourier-scale source bounds and screening these
specific uniform comparisons before attempting further error improvement.

## Signed quadrature-error consumer — 16 November 2026

For Edward Baker with Codex assistance; lead actual settings unavailable,
proof/assessment dispatches Sol6.1/ultra. E21 is **Complete, proved in-note**;
E22 is **Proved in-note for the defined error law**; E24 is **Proved in-note
under the stated quadrature-error and phase inputs**. Completed return
addenda pin those dependencies. [E23](../papers/investigations-6/03_volterra_coefficient_dynamics/reviews/08_VCD_E23_SIGNED_ERROR_CONSUMER_ASSESSMENT_20261116.md)
accepts the proofs and clarified synthesis within scope, separate internal
shared-model review with no proof correction.

[Synthesis23](../papers/investigations-6/03_volterra_coefficient_dynamics/notes/23_VCD_B06_SIGNED_ERROR_CONSUMER_SYNTHESIS_20261116.md)
gives (F-G_N=L_NE_N), where (L_N) is the first omitted-walk term and
(E_N) a symmetric error characteristic function. Explicit source and
simplex bounds yield (|E_N-1|=O(|z|^2log^2(N+1)/N)), uniformly on
(|Im z|le1), with real even/odd quadrature brackets. A positive-amplitude
directed enclosure uses only the available prefix and supplies pointwise
exclusions and conditional contour counts. At equal coefficient cost,
the next physical head has smaller actual error near zero than the plain
monomial correction; no all-region actual ordering is proved.

“The phase budget is proved; a canonical placement of the finite-model
margin is not.” Weighted-square controls pass the phase estimate. The
canonical contour separation, model zero count and degree induction remain
open. Reusable for signed error acquisition and fair prefix-cost comparison,
not an unconditional Fourier-zero theorem.

## Readout manuscript integration — 16 November 2026

For Edward Baker with OpenAI Codex assistance; actual model/effort unavailable.
The [expanded VCD manuscript](../papers/investigations-6/03_volterra_coefficient_dynamics/manuscript/README.md)
integrates the relevant established memory, score, midpoint and signed-error
results with self-contained background. It derives the polynomial
Christoffel–Darboux phase identity and a conditional local zero-displacement
lemma, while separating both from the unproved canonical Fourier geometry.
[Assessment09](../papers/investigations-6/03_volterra_coefficient_dynamics/reviews/09_VCD_READOUT_MANUSCRIPT_ASSESSMENT_20261116.md)
records “same-assistant analytical and document check completed within the
stated scope.” This preserves earlier source statuses and is not independent
review. [Integration25](../papers/investigations-6/03_volterra_coefficient_dynamics/notes/25_VCD_ANALYTICAL_READOUT_MANUSCRIPT_INTEGRATION_20261116.md)
routes proofs, control premises and reading references. No new canonical zero
theorem or numerical campaign; B07 remains unactivated. Reading PDF in the
ignored root output folder, sources and small build record in the investigation.

**Fixed-zero follow-up, 16 November 2026:** [note26](../papers/investigations-6/03_volterra_coefficient_dynamics/notes/26_VCD_FIXED_ZERO_STABILIZATION_AND_PHASE_20261116.md) states “analytical corollary derived and incorporated; same-assistant checking only.” Manuscript Proposition 10.2 gives isolated-cluster stability; Corollary 10.3 gives an alternating displacement asymptotic at each fixed simple real limiting zero, with degree ratio O_r(log²(N+1)/N²). This supplies no uniform threshold over increasing zero index and does not imply reality of all limiting zeros. [Assessment10](../papers/investigations-6/03_volterra_coefficient_dynamics/reviews/10_VCD_FIXED_ZERO_COROLLARY_ASSESSMENT_20261116.md); for Edward Baker with Codex assistance, actual model/effort unavailable.

**Unresolved clusters, 16 November 2026:** [note27](../papers/investigations-6/03_volterra_coefficient_dynamics/notes/27_VCD_CLUSTER_RESOLUTION_AND_HEAT_COLLISIONS_20261116.md) records “local analytical consequences derived and incorporated; same-assistant checking only.” Manuscript Propositions 10.4–10.6 make compact convergence uniform on compact heat-time intervals, bound pair center/discriminant errors from a contour margin, and derive shrinking uncertainty near a stipulated fixed double event. This survives loss of individual simplicity but neither asserts nor excludes a theta collision. [Assessment11](../papers/investigations-6/03_volterra_coefficient_dynamics/reviews/11_VCD_CLUSTER_RESOLUTION_ASSESSMENT_20261116.md); for Edward Baker with Codex assistance, actual model/effort unavailable.


## Cluster-gap physical residual — 16 November 2026

For Edward Baker with Codex assistance; lead recorded settings unavailable, proof/assessment dispatches Sol6.1/ultra. [GT synthesis07](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/07_VCD_GT_RESEARCH_SYNTHESIS_20261116.md) records the explicit physical-time phase extension, full coordinate transfer and exact Jacobi heat defect. [Note06](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/06_VCD_GT_E03_FIXED_EVENT_DEFECT_20261116.md) is **“Proved in-note conditional on one fixed isolated double event.”** It gives a unique nearby model double time and alternating leading displacement. On a slab of length N^-3, the actual signed defect integral's magnitude divided by the next-head discriminant error is asymptotic to 16N/(beta_(N+1)(T)a^4), at equal acquired coefficient input. The complete endpoint/transfer combination can still cancel. [E05 r3](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/05_VCD_GT_FIXED_EVENT_AND_SYNTHESIS_ASSESSMENT_20261116.md) accepts the proof without mathematical correction and the synthesis after a source-scope clarification; internal shared-premise review. No canonical event, signed gap margin or descent is acquired; this refines the fixed-event resolution entry above without asserting a collision exclusion.

**Critical-scale continuation, 16 November 2026:** [Note09](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/09_VCD_GT_E03_CRITICAL_SCALE_COMPENSATION_20261116.md) remains **“Proved in-note conditional on one fixed isolated double event.”** It gives uniform joint error/residual/drift profiles at t=T+s/N². [Note10](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/10_VCD_GT_E07_DEFLATION_KERNEL_20261116.md) directly derives the normalized curvature kernel, with value −4/(3a⁴) at the event. [Synthesis11](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/11_VCD_GT_CRITICAL_SCALE_SYNTHESIS_AND_CONTINUATION_20261116.md) combines them to resolve the relative subcritical drift and quantifies separate-term overpayment, without a canonical margin or theta-specific distinction. [Assessment06](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/06_VCD_GT_CRITICAL_SCALE_ASSESSMENT_20261116.md) accepts within scope after exact target/weighting and source/cost clarification. For Edward Baker with Codex assistance; lead settings unavailable, helpers Sol6.1/ultra, internal shared-premise review.

**Canonical local application, 16 November 2026:** [GT Note15](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/15_VCD_GT_E04_CERTIFIED_SIGNED_GAP_20261116.md) records **“Certified local enclosure”** on the fixed first-Lehmer-pair tube, t in [0,1/10]. Complete xi convolution, explicit source errors, tensor interpolation and annular contour payments acquire count/collar and K<=-0.59. The signed margin exceeds 0.00058487578; the absolute-cost margin is below -0.02126314189. [Synthesis16](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/16_VCD_GT_CANONICAL_SIGNED_GAP_SYNTHESIS_20261116.md) states: “Direct endpoint evaluation is cheaper and tighter on this input class.” The comparator receives the same paid geometry. [Assessment08](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/08_VCD_GT_CANONICAL_GAP_CERTIFICATE_ASSESSMENT_20261116.md) accepts proof/code/replay after wording clarifications, with quadratic collision and altered-input checks. This supplies one local canonical signed estimate, not a general source inequality, new zero coverage or Newman bound. For Edward Baker with Codex assistance; lead settings unavailable, helpers Sol6.1/ultra, internal shared-premise review.


**B06 scoped follow-through, 16 November 2026:** [GT Note18](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/18_VCD_GT_E03_SOURCE_MODE_ALLOWANCE_20261116.md), **proved in-note under the stated local hypotheses**, states: “This rules out passing the chosen bound (3) with these \(r,R,B\).” The exact second Laurent coefficient plus the frozen separate Cauchy tail gives an upper allowance at least 63111/490, so it cannot certify K≤-59/100; this is no lower bound on actual K. [Note19](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/19_VCD_GT_E03_MATCHED_GAP_MINIMUM_20261116.md) proves D′≥19/32 from the existing certificate, identifying the fixed-tube minimum with its already enclosed D(0). [Assessment09](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/09_VCD_GT_B06_SOURCE_MODE_MINIMUM_ASSESSMENT_20261116.md) accepts both without required correction. No new source acquisition, general sign, total-cost theorem or universal transport exclusion. For Edward Baker with Codex assistance; lead settings unavailable, helpers Sol6.1/ultra, internal shared-premise review.


**Joint exterior-sign continuation, 16 November 2026:** [GT Note21](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/21_VCD_GT_E03_JOINT_CONJUGATE_SOURCE_ESTIMATE_20261116.md), **“Proved in-note conditional on the stated enlarged geometry,”** groups conjugate divisor terms before estimation. [Note22](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/22_VCD_GT_E04_JOINT_STRIP_GEOMETRY_20261116.md) acquires that geometry on the fixed canonical tube using the same source cache. All omitted exterior groups are favorable; the reflected pair supplies K≤−5000/1962848636289. [Assessment10](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/10_VCD_GT_JOINT_SOURCE_ASSESSMENT_20261116.md) accepts the proof and bounded replay within scope. The mirror-only allowance cannot pay the useful cost threshold; an even quartic witnesses structural insufficiency in the stated analytic class. [Synthesis23](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/23_VCD_GT_JOINT_SOURCE_SYNTHESIS_AND_CONTINUATION_20261116.md) states the additional lower-mass gate. No all-real exterior premise, new source values, uniform height result or direct-method advantage. For Edward Baker with Codex assistance; lead settings unavailable, helpers Sol6.1/ultra; internal shared-premise review.


**Analytical manuscript milestone, 16 November 2026:** the [integrated
manuscript map](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/25_VCD_GT_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261116.md)
connects the above results to normalized deflated Fourier curvature and its
exact finite/continuous formulas. [E05 r9](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/11_VCD_GT_MANUSCRIPT_INTEGRATION_ASSESSMENT_20261116.md)
states: **“Accepted within scope as an analytical manuscript integration.”**
The five-atom control has negative deflated curvature and fails width one;
the four-atom positive undeflated Laguerre expression still admits nonreal
zeros. No canonical Fourier magnitude, new numerical acquisition or global
confinement follows. [Continuation26](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/26_VCD_GT_RESEARCH_CONTINUATION_20261116.md)
keeps the exterior-mass and Fourier proposals distinct. For Edward Baker
with Codex assistance; lead settings unavailable, helpers Sol6.1/ultra,
internal shared-premise review.

**Sharp exterior-weight feasibility, 16 November 2026:** [GT Note27](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/27_VCD_GT_E03_SHARP_EXTERIOR_MASS_20261116.md), **“Proved in-note for the stated rectangular information class,”** gives the exact four-corner minimum of the conjugate weight. At width one and |D|<=1/5, the old allowance cannot reach 0.59 with nine additional occurrences; the sharp rectangular allowance cannot with four. Ten and five are necessary counts, not sufficient canonical manifests. A paid conjugation-invariant singleton count instead forces its selected zero real. [Note28](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/28_VCD_GT_E03_FOURIER_GROUPING_SCREENS_20261116.md), **“Proved in-note for the two stated groupings,”** rejects the unchanged natural Fourier Gram matrix and the continuous constant-mode/absolute-remainder allowance; neither proves canonical negativity. [Assessment12](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/12_VCD_GT_SHARP_MASS_FOURIER_ASSESSMENT_20261116.md) accepts within scope after one status clarification, no mathematical correction, with exact arithmetic replay. [Synthesis29](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/29_VCD_GT_SHARP_MASS_SYNTHESIS_AND_CONTINUATION_20261116.md) retains the unpaid actual count/location gate. No new canonical source magnitude or acquisition. For Edward Baker with Codex assistance; actual settings unavailable, separate-agent internal shared-premise review.

**Concrete exterior mass acquired, 16 November 2026:** [GT Synthesis32](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/32_VCD_GT_EXTERIOR_MASS_SYNTHESIS_AND_CONTINUATION_20261116.md) states **“Local exterior lower mass acquired and accepted within scope.”** All 176 explicit moving real brackets have full-time opposite endpoint signs on t in [0,1/10]. Their lower counts and locations, with independently replayed 512-cell target coordinates, supply -K>0.5937558081007126288>0.59 without measured K. [Assessment13](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/13_VCD_GT_EXTERIOR_MASS_CERTIFICATE_ASSESSMENT_20261116.md) accepts within scope; one replay matches every mathematical field and altered/missing identities reject. This supersedes the preceding entry's unpaid finite count/location gate. No exact singleton counts, new target reality, height-uniform theorem or cost advantage: positive D was already paid, and the old measured curvature is stronger. For Edward Baker with Codex assistance; actual settings unavailable, separate-agent internal shared-premise review.


**Canonical far exterior and counted near-field scope, 17 November 2026.**
For Edward Baker with Codex assistance; lead settings unavailable, conceptual
Astra/ultra and proof/review Sol6.1/ultra dispatches. [GT Note33](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/33_VCD_GT_E12_UNIFORM_SIGNED_FAR_EXTERIOR_20261117.md)
is **“Proved in-note”**: for the stated isolated canonical pair, t∈[0,1/2],
c≥16π, |D|≤1 and 3≤R≤c/2, its full signed far sum is log(c/(4π))/(2πR) with
error O(log(2+c)/R²+log(2+c)/R³+log(2+c)/c). Constants are unevaluated.
[Note34](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/34_VCD_GT_E15_IDENTICAL_COUNTS_OPPOSITE_SIGNS_20261117.md)
proves an identical-horizontal-count control with normalized interaction
limits 1/2 and −1/16 in a fixed-slice analytic-divisor class; source/time
hypotheses are not supplied. [Assessment15](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/15_VCD_GT_E14_FAR_EXTERIOR_AND_COUNT_SCOPE_ASSESSMENT_20261117.md)
states: “Accept both mathematical proofs within the frozen scope.” It
supersedes pending-review language after one synthesis scope clarification,
without proof corrections. The canonical near field and incoming budget
remain open; no new positivity region or specialist review.


**Source-based nearby interaction and exceptional pairs, 17 November 2026.**
Prepared for Edward Baker with Codex assistance; actual root settings
unavailable, Astra/ultra conceptual and Sol6.1/ultra proof/review dispatches.
[GT Note37](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/37_VCD_GT_E17_AVERAGED_TRANSVERSE_CORRECTION_20261117.md),
**proved in-note**, contracts the inherited canonical transverse second
moment to a center mean C/a^3, versus the matched count-only C0/a, with an
exact both-D-sign radial correction. [Note38](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/38_VCD_GT_E19_ISOLATED_PAIR_EXCEPTION_COUNT_20261117.md)
proves an O_b(T log(T) exp(-2ba/3)) count of independently isolated pairs
with negative near/full interaction, plus an O(T log(T)/(a^4 h))
large-transverse-loss count, within its stated collar/height domain and
uniformly for 0<=t<=1/2. [Note36](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/36_VCD_GT_E16_COMPLETE_SOURCE_PHASE_ALLOWANCE_20261117.md)
proves a negative limiting favorable-phase-only lower allowance, not
negative actual curvature. [Assessment17](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/17_VCD_GT_E18_SOURCE_AND_PAIR_COUNT_ASSESSMENT_20261117.md)
accepts all three proofs and the synthesis within scope, without required
correction. Fixed-slice opposite-sign controls preserve both moment and
density upper bounds. No every-pair sign, incoming cost, new reality
region or specialist review follows.

**Fixed-collar dynamic estimates, 17 November 2026.** For Edward Baker
with Codex assistance; root settings unavailable, conceptual Astra/ultra
and proof/review Sol6.1/ultra dispatches. [GT Note40](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/40_VCD_GT_E20_FIXED_COLLAR_TIME_OCCUPATION_20261117.md),
**proved in-note**, retains conjugate dissipation to bound negative-pair
time occupation by O(T/log T) plus boundary terms at fixed collar and
fixed physical duration, improving the integrated O(T log T) slice
allowance. [Note41](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/41_VCD_GT_E21_EXACT_INTERACTION_RICCATI_BOUND_20261117.md)
proves M'=2M²-12S2-16DS3 for the complete canonical divisor and improves
the normalized interior lower allowance to -O(sqrt(log T)) on a paid tube.
It states: “The tube length by itself supplies no such sign guarantee.”
[Assessment19](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/reviews/19_VCD_GT_E22_FIXED_COLLAR_ASSESSMENT_20261117.md)
accepts both proofs and synthesis within scope without required correction.
The improved integrated multiplier still diverges; the combined allowance
does not exclude one exception or acquire a tube, incoming anchor or new
reality region. Internal shared-premise assessment, no specialist review.

**Analytical manuscript milestone, 17 November 2026.**
[GT Integration43](../papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/notes/43_VCD_GT_RECENT_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261117.md)
states “E23 exposition milestone complete; accepted within scope by E24”
after its recorded corrections. The existing manuscript derives the sharp
weights, signed far tail, transverse means/counts, fixed-collar occupation,
exact interaction law and scoped Fourier limits in dependency order.
The scientific statuses above are unchanged; numerical evidence supports
the theory in Appendix B. For Edward Baker with Codex assistance; root
settings unavailable, Sol6.1/ultra helper dispatches, internal shared premises.
