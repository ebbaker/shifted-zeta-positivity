# First research round — quantified approximation results

14 November 2026, America/New_York; research began 13 November. Prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance. The coordinator's actual backend/effort are unavailable in chat 0002's recorded configurations. Conceptual workers were explicitly dispatched as **gpt-6-astra / ultra**, execution and assessment workers as **gpt-6.1-sol / ultra**. The separate assessment passes share their workers and source premises with the derivations; they are internal LLM assessments, not independent specialist review.

## Main gain

The coefficient and chain branches combine to remove the previously unknown monic-norm factor from the finite-chain scalar error. Put \(K=X+\log(1/\varepsilon)+1\). The [shared transfer proof](03_TN6_E01_COEFFICIENT_TO_SCALAR_TRANSFER_20261113.md) gives the explicit sufficient depth

\[
 N=\left\lceil4K\log(16K)\right\rceil,
 \qquad
 \sup_{0\le\tau\le1/2,\ |x|\le X}
 |H_{1/2-\tau}(x)-H_N(\tau,x)|
 \le H_{1/2}(0)\varepsilon,
 \quad 0<\varepsilon\le1.
\]

Here \(H_N=(Z_*/2)\langle e_0,e^{-\tau J_N^2}e^{ixJ_N}e_0\rangle\), with \(J_N\) the principal N-site matrix of the fixed complete-source chain at \(\lambda=1/2\). This is an absolute scalar approximation theorem. Its sufficient depth grows like \(K\log(K+1)\); it is not an optimal-depth claim, state transport estimate or computational cost bound. The normalization is the fixed positive base mass, not division by the field at the observation.

Read [the result index](../../../result-summaries/README.md), [avoid index](../../../avoid/README.md), [controls 12](../../../result-summaries/12_collision_controls_and_screening.md) and patterns [01](../../../avoid/01_restating_the_target.md), [02](../../../avoid/02_shape_only_arguments_and_the_controls.md), [03](../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [05](../../../avoid/05_same_model_reviews_and_shared_premises.md) and [07](../../../avoid/07_scoped_exclusions_read_as_universal.md). All outputs here are quantitative approximation milestones or explicitly scoped obstructions. No RH-equivalent target was tested.

## Branch returns

| Branch and proof | Acquired bound and comparison | Practical limitation |
| --- | --- | --- |
| [VCD](../03_volterra_coefficient_dynamics/notes/01_VCD_E01_LOGARITHMIC_ENVELOPE_20261113.md) | \(\beta_n+\beta_{n+1}\le\operatorname{arcosh}^2(2n+12)/16\), every integer \(n\ge0\), uniformly \(0\le\lambda\le1/2\). In particular the normalized monic norm is at most \([\operatorname{arcosh}(2N+10)/4]^{2N}\). | A proved upper envelope, not a leading coefficient asymptotic or coefficient-acquisition algorithm. Positive weighted-square collision controls share the proof. |
| [JCH](../02_jacobi_chain_height_flow/notes/02_JCH_E01_R1_FINITE_CHAIN_READOUT_20261113.md) | Scalar error at most \((Z_*/2)h_N^*\sum_{k=0}^N\tau^kx^{2N-2k}/[k!(2N-2k)!]\); a generic complete-moment fallback also proves compact convergence. The finite-chain output is exactly the same N-node Gaussian quadrature. | Exact entries, normalization and certified evaluation remain to be acquired. This is not the exact-state prefix-tail norm. The boundary uses \(J_N^2\), not \(\Pi_NJ_*^2\Pi_N\). |
| [QTT](../01_qtt_newman_flow/notes/04_QTT_E01_COMPACT_RANK_ERROR_BOUND_20261114.md) | Formal tuple \((d,m,L)=(512,64,72)\), rank at most 641, scaled error below \(2^{-36}<10^{-8}\) on \(0\le\lambda\le1/2\), \(40\le x\le80\), \(|y|\le8\). Scale \(S(x)=e^{\pi x/8}/(1+x)^{7/4}\). | Exact complete-source polynomial coefficients; no dense grid or cores were constructed. This scale is not literal gamma division across the whole box. Direct integration of the same polynomial deletes the midpoint allowance, so no computational advantage is established. |
| [ITP](../04_exact_infinite_tensor_products/notes/02_ITP_E01_EXACT_CELL_PHASE_TRANSFER_20261113.md) | Exact within-cell phase integration gives error \(\le he^{8h}V_8/4+T_8(U)\), \(V_8<868\), uniform in every real x, \(|y|\le8\), and allowed time. At \(U=2,L=30\), the allowance is below \(5\times10^{-7}\). | The tested construction has \(2^{32}\) exact formal cell masses; their acquisition and tensor ranks are unresolved. Replacing each cell phase by its center value has actual uniform real-axis error at least \(Z_\lambda/2\), a failure scoped to that fixed point-phase architecture. |

The [shared proof](03_TN6_E01_COEFFICIENT_TO_SCALAR_TRANSFER_20261113.md) composes VCD and JCH only; it is not a performance contest among the four branches. It retains the complete theta source, literal Fourier factor 1/2 and reversed Newman clock. The elementary transfer also yields
\[
 \frac{|H-H_N|}{Z_*/2}
 \le\exp\left[-N\log4+\frac{X L_N}{2}+\frac{L_N^2}{8}\right],
 \qquad L_N=\operatorname{arcosh}(2N+10).
\]
No numerical campaign, new manuscript, source-mass calculation, interval certificate or coefficient-asymptotic import was performed. The displayed constants are established by analytical inequalities, not floating samples.

## Assessment and control scope

See the internal assessments for [VCD](../03_volterra_coefficient_dynamics/reviews/01_VCD_E02_ENVELOPE_ASSESSMENT_20261113.md), [JCH](../02_jacobi_chain_height_flow/reviews/01_JCH_E02_FINITE_CHAIN_ASSESSMENT_20261113.md), [QTT](../01_qtt_newman_flow/reviews/01_QTT_E02_RANK_ERROR_ASSESSMENT_20261114.md), [ITP](../04_exact_infinite_tensor_products/reviews/01_ITP_E02_EXACT_CELL_PHASE_ASSESSMENT_20261114.md), and [the shared transfer](../reviews/01_TN6_E01_TRANSFER_ASSESSMENT_20261113.md). Frozen requests, actual returns and their input identities remain in each owning research-progress/handoffs folder and numerics manifests. Source versions are identities, not independent mathematical validation.

The actual control comparisons distinguish failed premises from inequalities that still hold at a collision. The VCD bound fails for the displayed three-atom coefficient pair and the specified Euler-factor p=23 example, but the positive weighted-square collision witnesses can satisfy both VCD and JCH. Thus even the combined depth theorem is compatible with a collision. Smooth sources can likewise satisfy the cell-projection estimate at their events. The point-phase aliasing obstruction excludes only that fixed-grid readout in a uniform all-real-height norm. No universal tensor obstruction follows.

## Records and next step

The [parent register](../research-progress/01_TENSOR_NETWORK_RESEARCH_PROGRESS_20261113.md) routes to the four sole branch registers; this note is a dated result summary, not a second live ledger. [Milestones](../DRAFT_HISTORY.md) retain the research boundary. This shared chat is [0002](../chat-histories/0002_2026-11-14T04-47-10Z_continue-investigation-6-research.json); the registry owns current capture metadata, and final capture occurs after the real final reply.

**Suggested continuation: [B] TN6-B02 — GPT-6 Astra / Ultra**, to choose a certified finite coefficient-acquisition method and matched benchmark. Follow the [model-change handoff and bounded prompt](05_RESEARCH_CONTINUATION_AND_MODEL_HANDOFF_20261114.md). New fixed derivations or computations then go to **GPT-6.1 Sol / Ultra**. The first bounded round ends at its declared assessments; this proposal does not silently activate another scan.
