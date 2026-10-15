# 02 — Chord criterion, arithmetic bridge and next research steps

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded model **gpt-6-astra**, reasoning effort **ultra**. Updated after the research-priority review, the coefficient-core cycle, and the coupled-product continuation. This overview accompanies the [manuscript](../manuscript/theta_manifold_geometry.tex) and [reading copy](../../../../../output/pdf/theta_manifold_geometry.pdf). It supersedes the priorities in [Overview 01](01_RESEARCH_OVERVIEW_20261015.md). The new results below are saved research notes; the manuscript has not yet been revised to include them.

The main research target is now a **coefficient-coupled bound for a two-point amplitude with the complete starting factor retained**. The collision criterion is strong enough to accept a Gaussian cutoff error multiplied by square-root physical energy. An exponential average removes the endpoint derivative, and a new quantitative argument permits the single length `delta_N=1/N` at cutoff N. What remains missing is a signed estimate for the theta core.

The first continuation cycle has also sharpened the exclusions. Positive weighted-square sources can collide while satisfying both of the first two odd source endpoint identities. Direct finite elliptic shifts of the scalar source change only cutoff boundary modes and provide no favorable interior term. The effective outer budget has a substantially better constant, but still offers no practical overlap with finite computations. These findings determine the priorities below.

The subsequent [coupled-product continuation](../notes/00_research_coordination/06_COUPLED_PRODUCT_AND_REFLECTION_CONTINUATION_20261015.md) has now completed the leading identity experiment. Independent-source theta addition gives genuine coefficient relations, but its complete source matrices are indefinite even on coefficient zero-sum vectors. The natural positive-Gram ansatz and a constant rank-one repair therefore fail. The next priority is a **stationarity-aware arithmetic correction to the recombined physical observation**, retaining the full starting factor and both mixed sectors. This cycle also proves actual-theta parity cancellation asymptotics and gives a reflected positive-source collision control outside the square-coefficient class. No theta signed bound follows from the new identity.

## 1. The established collision mechanism

Write `h_j=∂_x^j H`, `E=H²+H_x²`, `W=h_j`, and

\[
\mathcal C_j(t;x,y)=W(t,x)\{W(t,y)-W_x(t,y)\},\qquad j=0,1.
\]

The starting point is stationary for the **full field**, `h_(j+1)(t,x)=0`. On a short rightward interval where W never vanishes, nonnegative C is exactly a bound of π/4 on the change in its real jet angle. At a finite collision of multiplicity `2r+j`, the stationary predecessor approaches the event while

\[
\frac{\mathcal C_j(t;x,x+\delta)}{\sqrt{E(t,x)}}\longrightarrow-d_{j,\delta}<0
\]

for each sufficiently small fixed positive δ. Consequently a locally uniform bound `C_j≥−K E^γ`, with **γ>1/2**, or an error `o(√E)`, excludes every covered finite multiplicity. The physical energy is always evaluated at the starting point, including on the odd branch. The threshold is sharp for unrestricted constants: a quadratic collision can coexist with a loss proportional to √E.

The [chord and cutoff note](../notes/02_signed_turning_control/02_CENTRAL_ENERGY_CHORD_AND_CUTOFF_TRANSFER_20261015.md) contains the proof integrated into the manuscript. The [inner-profile note](../notes/02_signed_turning_control/01_INNER_TURNING_PROFILE_20261015.md) explains the finer width `T−t` on which the angular turn concentrates.

The original pure-tail family remains valid:

\[
\mathcal C_j\ge-AE e^{aN^2}-B e^{-cN^2}.
\]

Its sufficient rate condition is **a<c**, with local uniformity and integer rounding handled as in the manuscript. The newer mixed-error criterion below is a different family, and does not remove this condition from the original theorem.

## 2. The preferred target: retain the full starting factor

If only the endpoint is truncated, with `D_N=W_N(y)−W_(N,x)(y)`, then

\[
\mathcal C_j=W(t,x)D_N+W(t,x)(D-D_N).
\]

A source tail `|D−D_N|≤ε_N→0` costs at most `ε_N√E`. Thus it is enough to prove

\[
W(t,x)D_N\ge-K_NE(t,x)
\]

for every sufficiently large fixed N, with K_N locally bounded through each possible event. For the common fixed-length version, choose N to make ε_N smaller than the negative collision limit, then approach the event at that fixed N. **No growth restriction on K_N as N→∞ is needed for this argument.** Local finiteness through each finite event is essential. See the [factor-preserving and averaged criteria](../notes/02_signed_turning_control/03_FACTOR_PRESERVING_AND_AVERAGED_CHORD_TARGETS_20261015.md).

The [exponential-average continuation](../notes/02_signed_turning_control/04_EXPONENTIAL_AVERAGE_AND_SHRINKING_CHORD_TARGETS_20261015.md) supplies a simpler observation:

\[
\boxed{\mathcal A_{j,\delta}
=W(t,x)^2-e^{-\delta}W(t,x)W(t,x+\delta)
=\int_0^\delta e^{-z}\mathcal C_j(t;x,x+z)\,dz.}
\]

It uses only endpoint values. At a multiplicity `2r+j` event its quotient by √E has a negative limit of size `c δ^(2r)` as δ→0. For

\[
\mathcal A_{j,\delta,N}
=W(t,x)^2-e^{-\delta}W(t,x)W_N(t,x+\delta),
\]

the complete theta source gives

\[
|\mathcal A_{j,\delta}-\mathcal A_{j,\delta,N}|
\le B_j(T_*)e^{-\pi(N+1)^2/4}\sqrt{E(t,x)},
\]

with a finite explicit source-integral constant on bounded heat-time ranges.

This also resolves a qualified version of the earlier shrinking-window concern. If prescribed `δ_N→0` and errors ε_N satisfy `ε_N=o(δ_N^m)` for **every fixed positive integer m**, the same fixed-N-then-event argument excludes all finite multiplicities. Gaussian tails and any algebraic shrinkage `δ_N=N^(−q)` satisfy this condition. More generally `log(1/δ_N)=o(N²)` works with the stated Gaussian tail. This is not a claim that an arbitrary shrinking window suffices.

The concrete preferred open target is therefore

\[
\boxed{\mathcal A_{j,1/N,N}(t,x)\ge-K_NE(t,x),\qquad j=0,1,}
\]

for full stationary starts on the covered zero-free rightward intervals, for all sufficiently large fixed N. Each K_N must be source-prescribed and locally bounded through possible events. For each fixed N, the domain must contain all sufficiently close full stationary predecessors and their entire interval of length 1/N; the proximity threshold may depend on N. The complete starting field must not be replaced by its cutoff. The exponential weight does not provide rapid Fourier decay; its benefit is the exact endpoint simplification and the retained physical amplitude. **No theta bound of this form has been proved.**

## 3. What the arithmetic experiments now establish

**Two endpoint identities are still insufficient.** The [new four-square control](../notes/05_control_families/03_TWO_ENDPOINT_SQUARE_COLLISION_20261015.md) has fixed positive coefficients, positive half-line source, primitive normalization, and

\[
\Phi'(0)=\Phi'''(0)=0,
\qquad H(T,x_*)=H_x(T,x_*)=0,
\qquad H_{xx}(T,x_*)>0,
\]

at `T=1/100`, with `83.5323729<x_*<83.5323730`. Its even source extension is C⁴ but not C⁵. It passes support-only localizers and both endpoints, but fails full reflection. A qualitative perturbation supplies positive weights on every square node; no explicit perturbation radius is certified. The endpoint constraints force a small high-mode mass in a particular normalized endpoint measure, yet this control still collides. Small mass in that measure is therefore not sufficient physical sign control.

This strengthens the [earlier one-endpoint collision](../notes/05_control_families/01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md). It does not rule out every finite endpoint hierarchy. Further endpoint additions now need a quantitative transform mechanism or a sharply bounded structural question; simply adding the next equality is lower priority.

**Full coefficient coupling remains a real discriminator.** The [reflection-rigidity theorem](../notes/05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md) forces constant coefficients for the symmetric polynomial-growth weighted integer comb. The [elliptic-shift experiment](../notes/03_theta_bundles_and_connections/05_ELLIPTIC_SHIFT_CORE_AND_PROJECTION_OBSTRUCTION_20261015.md) gives a more precise projected relation: the one-shift projected defect vanishes identically exactly when `a_n=a_0+b|n|`, under the stated evenness and growth assumptions. Fixing `a_0=1` and the normalized primitive endpoint then forces b=0. The projected relation alone is weaker than the full elliptic law. Both rigidity results identify theta; neither supplies the required inequality for its oscillatory transform.

**Direct scalar shifts have reached their useful limit.** Applying the complete physical fourth-jet operator to one translated cutoff gives exactly

\[
\Phi_N^+=\Phi_N+\tfrac12(\phi_{N+1}-\phi_N).
\]

Every fixed finite combination of integer shifts whose coefficients sum to one similarly changes only a finite cutoff boundary band. The Gaussian remainder retains the full starting amplitude, but no favorable interior term appears. The complete operator is crucial: separate derivative terms contain a translated zero mode whose positive-time integrals diverge before cancellation. The finite primitive endpoint and corner must also stay exact. This closes the proposed direct finite-shift pilot. It does not exclude coupled products, transverse observations before restriction, nonconstant insertions, or growing shift ranges.

## 4. Ranked program after the first continuation cycle

| Priority | Bounded next task | Success criterion and stop rule |
| --- | --- | --- |
| **1. Stationarity-aware arithmetic correction** | Test one explicit arithmetic correction to the complete, recombined `A_(j,1/N,N)` using the full stationary constraint and unprojected coefficient information. The coupled addition identity is now derived; its unconditional Gram interpretation is disproved. | Prove a signed remainder estimate while retaining the infinite endpoint strip, both exchange sectors and primitive endpoints. A coefficient-rigidity statement, constant rank-one repair, or omission of a cancelling sector is insufficient. |
| **2. Test one fixed coefficient rule** | Once such an identity exists, implement its actual coefficients and remainder on a bounded theta domain, at full stationary starts, with the complete starting factor. | Certify the complete source tails and interval coverage, and state how the bound remains locally bounded as E→0. Reject rules chosen from the already observed sign or normalized by a potentially singular E. A finite pilot tests the rule; it does not prove global coverage. |
| **3. Quantify stronger arithmetic control** | Use the two-endpoint example and projected ramp family as adversarial tests. If exploring more endpoints, first formulate a norm or remainder that their hierarchy controls in the physical transform. | Obtain a quantitative bridge from coefficient coupling to `E` or `√E`; support positivity or endpoint mass concentration alone is already known to be insufficient. |
| **4. Redesign the practical outer bridge** | Seek a nonasymptotic approximation and differentiated remainder that could overlap a feasible finite certificate. State a proposed overlap height before a large sweep. | Reduce the structural domain and derivative losses, with all imported constants explicit. Merely refining the current large-height allocation does not create practical overlap. Extracting the exponent-pair constants remains useful if an explicit asymptotic theorem is the separate objective. |

The first task should focus on one fixed arithmetic correction at a time. The exact amplitude kernel, coupled identity and complete affine primitive representation are now available. The [coupled-product review](../reviews/07_COUPLED_PRODUCT_AND_REFLECTION_CONTROL_REVIEW_20261015.md) records why their natural unconstrained Gram interpretation fails. The arithmetic contribution must add a justified sign relation involving full stationarity. Enlarging the disproved parity matrices or a direct finite scalar-shift ansatz is no longer the recommended experiment.

## 5. The outer budget: genuine improvement, unchanged practical gap

The [new outer-budget note](../notes/06_effective_outer_bridge/01_LOW_INDEX_BUDGET_REFINEMENT_20261015.md) retains Investigation 21's analytic and exponent-pair hypotheses and splits its low-index sum into four ranges. This reduces

\[
A_0=\frac{36138917}{16}
\quad\text{to}\quad A_*=\frac{218227}{384},
\]

a factor exceeding **3,974**. Reallocating the budget gives the sufficient conditional log-height

\[
L\ge1+\max\{32000000,
14000\log(14155776G_0C_{\rm EP})\},
\qquad G_0=962773/671.
\]

The exponent-pair constant `C_EP` and any validity threshold remain unevaluated, and the original outer-domain restrictions, including `tL≥61/24`, remain in force. Since `x=4πe^L`, this is still far beyond practical finite verification. The new majorant itself cannot pay the required budget below approximately `L−1=31,424,688`; that is a limitation of this bound, not a lower bound on the true positivity threshold. No new unconditional numerical theta domain or small-time coverage is claimed.

## 6. Geometry and lower-priority routes

The [complete signed bridge](../notes/03_theta_bundles_and_connections/03_COMPLETE_SIGNED_CORRELATION_BRIDGE_20261015.md) remains the correct bookkeeping foundation. Its affine primitive endpoint must stay combined with the integral. The [ASD metric classification](../notes/03_theta_bundles_and_connections/02_ASD_METRIC_FREEDOM_AND_PHYSICAL_RESTRICTION_20261015.md) supplies a path-normalized metric with unchanged curvature, but the physical restricted connection and its external two-source product are flat. Transverse commutators give an exact recurrence; their presence alone does not distinguish the collision controls or establish a sign.

| Route | Current assessment | Condition for renewed priority |
| --- | --- | --- |
| Period-two contour transport | Complete identity established; separate shifted-ray and bottom-edge estimates lose large cancellations. | Preserve the full packet and mixed products with physical-energy scaling. Exponential growth with spectral height alone is not a local-criterion impossibility if coefficients remain finite through each finite event. |
| Natural fiber Hilbert norm | The studied lift does not decay with the physical point value, and its proposed positive-heat integral fails. | A justified observation space that retains physical decay and improves the signed estimate. |
| Compact ASD extension | The unchanged smooth compact Kähler construction conflicts with degree one on the fibers. | Explicit modified, singular, meromorphic or boundary data, together with a useful signed consequence. |
| Global Pick or Hermite–Biehler positivity | No new positive kernel is established; the proposed target may already demand the desired real-rootedness. | An independently justified kernel and positivity mechanism that survives the controls. |
| Additional geometric packaging | Physical jet surfaces and calibrated inclusions are established, but also allow generic collision controls. | A specific new estimate for the physical two-point observation. |

The [contour note](../notes/03_theta_bundles_and_connections/04_PERIOD_TWO_CONTOUR_PACKET_AND_SECTOR_OBSTRUCTION_20261015.md), [priority review](../reviews/05_RESEARCH_PROGRESS_AND_PRIORITY_PATHS_20261015.md), and earlier [strategy note](../notes/00_research_coordination/03_PRIORITIZED_SIGNED_BOUND_RESEARCH_PATHS_20261015.md) preserve the detailed diagnostics. Their prospective direct-shift and second-endpoint tasks are now completed as described above.

## 7. Verification, manuscript boundary and handoff

The [coefficient-core review](../reviews/06_COEFFICIENT_CORE_AND_TWO_ENDPOINT_REVIEW_20261015.md) and [continuation handoff](../notes/00_research_coordination/05_COEFFICIENT_CORE_AND_TWO_ENDPOINT_CONTINUATION_20261015.md) separate analytic proofs, exact checks, validated intervals, exploratory discovery and imported hypotheses. Four new checkers pass **2,136 overlapping exact assertions** and **26 mixed or validated assertions**; the latter certificate uses 44 complete integrals at 160-bit precision with real tails included. The [new manifest](../numerics/COEFFICIENT_CORE_AND_TWO_ENDPOINT_CHECKS_20261015.json) binds the installed notes, checkers and receipts and records independent replays. These counts are not numbers of distinct theorems.

The subsequent [coupled-product review](../reviews/07_COUPLED_PRODUCT_AND_REFLECTION_CONTROL_REVIEW_20261015.md) and [latest handoff](../notes/00_research_coordination/06_COUPLED_PRODUCT_AND_REFLECTION_CONTINUATION_20261015.md) record three additional notes and independent replays: **3,278 exact assertions** and **38 mixed or validated assertions**, bound by the [coupled continuation manifest](../numerics/COUPLED_PRODUCT_CONTINUATION_CHECKS_20261015.json). The [history audit](../numerics/COUPLED_PRODUCT_CHAT_HISTORY_VERIFICATION_20261015.json) separately confirms registration 19, content integrity, and the preceding final's deferred capture. The source identities are now integrated in manuscript sections 9.3–9.4; the newer negative controls are brief cited remarks.

The previous manifests retain their historical 6,897 exact and 123 validated or mixed assertions across eleven checkers. The [build record](../manuscript/BUILD_RECORD.json) now identifies the revised 43-page manuscript. Exponential-average transfer, coefficient coupling, recurrence stability and boundary geometry are integrated; negative findings are briefly summarized. The conditional outer-budget refinement remains separate research. No theta signed-core bound or RH conclusion has been established.

The original overview/integration conversation retains formal-replay history **18**, with its [canonical history](../../../formal_replay_crosswalk/chat-histories/0018_2026-10-15T11-51-01Z_continue-theta-manifold-research.json). This priority review and continuation retain the current conversation's separate formal-replay history **19**, as required by the local standing instruction; it is not re-registered here. The formal replay [registry](../../../formal_replay_crosswalk/chat-histories/index.json) supplies current capture metadata. The earlier creation chat remains history 17 in this investigation. Chat provenance records work performed, not mathematical validity.

The latest [recurrence manuscript handoff](../notes/00_research_coordination/09_MANUSCRIPT_RECURRENCE_INTEGRATION_AND_NEXT_CHAT_20261015.md) supersedes this overview for the immediate next calculation. It records the explicit recurrence boundary obstruction and proposed signed trace estimate, with the 43-page integrated manuscript and formal replay history 20.
