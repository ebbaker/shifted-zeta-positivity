# MC11-AR-E02 return and AR-E03 model-change continuation

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6.1-sol (Codex), actual recorded effort ultra**. Existing thread `01a1aa23-3513-7681-bad6-d8c15b6914fb`, MC11 history0003. [Register02](../02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) is the sole live register; this is the E02 r1 return and continuation, not a revised source/pairing contract.

| Next task | Type | Recommended model and reason | Ready or dependency | Expected output |
| --- | --- | --- | --- | --- |
| **MC11-AR-E03 r1 — default next** | E — execution | **Sol**; the derivative recurrence, source estimates and endpoint integration by parts are frozen | E02 prerequisite supplied by the proved-in-note return; ready for separate author activation | Arbitrary finite-index source, Hilbert membership, moments and endpoint-correct cross-pairing theorem |
| MC11-B01 — retained alternative | B — brainstorm | Astra; the signed all-order estimate remains a conceptual choice | Independently ready from E04; default angular route also consumes E03 | At most two analytic routes and a frozen E05 lemma, or scoped stop |
| MC11-AR-E04 | E — execution | Sol; fixed claim-by-claim analytic assessment | Conditional on finished source/model returns and E05 if activated | Scoped assessment of domains, sources, limits, indices and signed estimates actually supplied |

## Completed E02 return

**MC11-AR-E02 r1 is complete: all requested assertions are proved in-note without correction.** [Research Note07](../../notes/07_MC11_AR_E02_R1_BOUNDED_POTENTIAL_DEFECT_AND_RIGIDITY_20261105.md) gives the kernel construction, strictness proof, complete-sum estimates and finite u-derivative transport. [The input/return record](07_MC11_AR_E02_R1_INPUTS_AND_RETURN_20261105.json) preserves the six matched frozen hashes, actual configuration and output versions. [BR01's issued Note06](../../notes/06_MC11_BR01_R1_FROZEN_CYLINDER_MODEL_AND_ANALYTIC_CONTRACT_20261105.md) and [handoff06](06_MC11_BR01_RETURN_AND_AR_E02_MODEL_CONTINUATION_20261105.md) remain unchanged.

For every bounded nonnegative scalar V on the complete radial line, the domains stay those of L_0 and H_n,0. A positive Neumann expansion about the constant potential M=||V||∞ constructs continuous strictly positive scalar Green kernels, with pointwise comparison between constant-M and free kernels. The continuous-kernel resolvent identity justifies the diagonal strictness argument even for measurable V. For every n≥1,
\[
 \frac{2n}{\sqrt{4n^2+M}}\le b_n=4nG_{n,V}(0,0)\le1,
 \quad
 0\le1-b_n\le1-(1+M/(4n^2))^{-1/2}\le M/(8n^2).
\]
If V is not zero a.e., every 1−b_n is strictly positive. The unchanged readout therefore satisfies Q_s(t)−R_V,s(t)≥(1−b_1)e^{-t}>0 at every t>0, s∈[0,1], including s=0. Exact recovery at even one such pair is equivalent to V=0 a.e. This is scoped to the fixed cylinder/probe/readout and bounded nonnegative comparison class; it says nothing universal about other potentials, confinement, boundaries or observations.

Every fixed t-derivative has the exact nonnegative defect series and the requested M/8-weighted bound. Note07 (17)–(19) give explicit complete tails uniform on t≥ε>0, s∈[0,1]. The affine s derivative omits n=1; higher s derivatives vanish. Note07 (20)–(22) establish each finite u derivative under the prescribed external t=πe^{4u}, e^u and (∂_u²−1)/8 map, with an explicit uniform source-half-line tail. Constants depend on derivative order. The source variable, fixed physical probe and independent evolution time remain distinct.

This used one analytic derivation, no extra regrouping, no spectral scan, quadrature, numerical acquisition, new potential or compensated readout. The actual theta model remains V=0. Deformed comparison functions were used only for derivative/error transport; their moments and determinant defects were not investigated. Proof-author checks and a read-only same-model complete-sum check support the return; it is not a separate assessment or independent specialist review.

## What stays frozen for AR-E03

Activate the **existing r1**, [handoff06's source/pairing request](06_MC11_BR01_RETURN_AND_AR_E02_MODEL_CONTINUATION_20261105.md#frozen-mc11-ar-e03-request-r1), using BR01 Note06 §6 (12)–(16). This return supplies its relevant E02 prerequisite and does not change any target, index range, endpoint rule or evidence standard. AR-E03 remains **unstarted** until separately activated. At that activation verify/freeze the actual Note07 and return-record versions, rather than relying on a prospective hash or treating this packet as execution.

The existing contract requires V=0, all s∈[0,1], the ordinary du Hilbert metric, fixed scalar-to-spinor isometry J and normalized wedges. Prove the prescribed P_m and H_m recurrences, complete-sum/integration justifications, a positive n=1 source lower bound, and finite-index Hilbert membership and moments. Retain the exact endpoint rule
\[
 \langle f_i,g_\ell\rangle=
 \begin{cases}c_{\ell-i}(s),&\ell\ge i,\\
 -\Phi_s^{(2(i-\ell)-1)}(0),&\ell<i.\end{cases}
\]
The determinant family is q≥1 and integer k≥q−1, including k=q−1,q,q+1. General filtered odd endpoint derivatives are not assumed zero; for lower shifts use the endpoint rule rather than artificial negative-index coefficients. The Fock direct sum and Hilbert isometry assert no Hamiltonian-domain membership, finite-energy preparation or determinant sign.

One proof pass and at most one local correction, no moment table or finite-order campaign. Reuse E02's complete-sum source differentiation; finish only E03's remaining membership/integral/endpoint dictionary. A changed physical preparation or observation goes to BR01; a signed order-dependent inequality goes to B01. Neither this generic potential rigidity nor a future all-index pairing identity replaces that signed estimate.

## Model and history continuity

Actual completed configuration: **gpt-6.1-sol / ultra**. The default next task remains Sol's E03 execution, so a model change is not needed for routing; Edward Baker selects the actual model, effort and chat. If a model is changed here, preserve this existing thread and its sole history **0003**, `chat-histories/0003_2026-11-05T05-16-36Z_begin-mc11-ar-e01-research.json`. Its unchanged title refers to the originating AR-E01 task; it now also records E02. Do not import this continuation into BR01's distinct history0004. A genuinely new chat receives its own actual identity/title and registration.

The previous exact-turn final capture was verified at this turn's start. Continue routine start/end refresh with `tools/refresh_chat_history.py` and the bounded exact-turn deferred final capture until trusted hook activation is verified; never hand-edit registered JSON or prewrite an unsent final reply. This packet creates no chat, changes no model setting and schedules no research.

Read the [result index](../../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../../avoid/README.md), [target-reformulation caution](../../../../../../../../avoid/01_restating_the_target.md), [re-realization caution](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [review provenance](../../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md) and [scoped-exclusion rule](../../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). Note07 applies the [collision-control screen](../../../../../../../../result-summaries/12_collision_controls_and_screening.md) without claiming that controls violate the generic resolvent bounds. There is no new RH criterion or determinant-sign conclusion.

## Pasteable continuation prompt

> Read root AGENTS.md, tools/CHAT_HISTORY.md and GPT_RESEARCH_MODEL_WORKFLOW.md, then MC11's sole Register02, the unchanged BR01 Note06/handoff06 and the AR-E02 Note07/return record. Continue **[E] MC11-AR-E03 r1 — Sol**, separately activating and freezing the actual E02 return versions. E02 proved the all-n bounded-nonnegative-potential response-defect and exact-recovery rigidity theorem with the readout fixed; the selected source remains V=0. Execute the existing Note06 §6 contract for every finite derivative, moment and pairing index, all s∈[0,1], q≥1 and k≥q−1. Retain odd endpoint terms outside that range, ordinary du metric, normalized wedges and the frozen Hilbert embedding; claim no preparation/energy-domain or signed-determinant consequence. Reuse E02's complete-sum derivative estimates. One proof pass, at most one local correction; no numerical acquisition, moment table or finite-order sign survey. Preserve history0003 if continuing this existing chat, record actual model/effort, save notes/progress/continuation, and stop at the E03 boundary.
