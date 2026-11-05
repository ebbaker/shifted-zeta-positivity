# MC11-BR01 return and AR-E02 model-change continuation

5 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance from **gpt-6-astra (Codex), actual recorded effort max**. Thread `01a1aa32-c540-7671-aa14-f080cfbedd5d`, MC11 history0004. This packet freezes the next requests and records the B decision; [Register02](../02_ANGULAR_RADIAL_THETA_MODEL_RESEARCH_PROGRESS_20261105.md) alone owns live status.

| Next task | Type | Recommended model and reason | Ready or dependency | Expected output |
| --- | --- | --- | --- | --- |
| **MC11-AR-E02 r1 — default next** | E — execution | **Sol**; bounded perturbation, scalar Green comparison and Gaussian summation are now fixed | Ready, unstarted; activate explicitly | One all-index potential-defect/rigidity theorem with domains and complete-sum differentiations, or precise failed assertion |
| MC11-AR-E03 r1 | E — execution | **Sol**; source recurrence and endpoint-preserving integration by parts are fixed | Conditional on relevant AR-E02 return | Arbitrary-index source, Hilbert membership and cross-pairing theorem |
| MC11-B01 — retained alternative | B — brainstorm | **Astra**; a signed cofactor estimate remains a conceptual choice | Independently ready from E04; default angular route consumes E02/E03 | At most two proof routes and one frozen E05 lemma, or scoped stop |

## Completed B decision

**MC11-BR01 r1 is complete as model selection and contract preparation.** [Research Note06](../../notes/06_MC11_BR01_R1_FROZEN_CYLINDER_MODEL_AND_ANALYTIC_CONTRACT_20261105.md) is the canonical mathematical contract. It compares exactly two models and selects:

- **Geometry and measure:** the complete product R_v×S² with metric dv²+g_S²/4; rank-two spinors, represented in L²(R,dv;K), K=L²(S²,Σ;dΩ), with the stated constant metric-volume identification.
- **Operator and boundary:** the accepted full-line self-adjoint L_0=D_C²=-∂_v²+4D². No wall, half-line extension or normalizable radial ground-sector restriction.
- **Potential:** V=0 for the actual theta model. One additional test class, V∈L∞(R), V≥0 a.e., enters only the prescribed second-order comparison L_V=L_0+VI, with unchanged domain and readout.
- **Observable:** the angular heat-damped radial-diagonal Green response at the fixed interior probe v=0, with external B_s=P_1+s(I-P_1). It recovers Q_s for every s∈[0,1] at V=0. W=(4|D|)⁻¹ uses dimensionless unit-sphere D and is not rescaled with a source radius.
- **Time and source map:** τ in e^{-τL_0} is independent of angular damping t. The map t=πe^{4u}, factor e^u and differential observation (∂_u²−1)/8 remain external. The source coordinate u is not a moving radial probe or the physical evolution time.
- **Encoding:** a fixed smooth normalized D=+1 eigenspinor χ gives the stated zero-extension isometry from L²(0,∞) to full-cylinder spinors. It preserves auxiliary pairings; it asserts neither a parallel spinor nor Hamiltonian-domain membership/preparation.

The Euclidean whole-space/spherical-readout candidate is deferred, with its domain and readout specified in Note06 §2. It would still insert W and would need the filtered modular defect accounted for beyond s=1. This is a research choice, not a universal Euclidean obstruction. Confinement is unnecessary for the chosen Green response; a finite full-space partition function is not the selected observation.

The new gain is a fixed, nonambiguous model and two executable analytic requests. AR-E01's free identity is reused, not reported as a new proof. The proposed potential theorem and general pairing theorem are **not yet executed or accepted**. No new signed determinant estimate, numerical acquisition, manuscript or model setting change occurred. Checking of this contract is by its authoring assistant with shared accepted inputs, not separate specialist review.

## Frozen MC11-AR-E02 request r1

Parent: Overview02 / BR01 r1. **E — execution; recommended Sol.** Exact request: Note06 §§3–5, especially (7)–(11). [Frozen input versions](06_MC11_AR_E02_R1_FROZEN_INPUTS_20261105.json) identify the issued note and prior premises. [BR01 activation versions](06_MC11_BR01_R1_INPUT_VERSIONS_20261105.json) retain the earlier consumed snapshots. Check hashes before activation; do not rewrite the request or its evidence to conceal a mismatch. The mutable register is not a frozen theorem input.

For every n≥1, prove the scalar kernels of H_n,V=-∂²+4n²+V on H²(R), their positivity and diagonal comparison. With M=||V||∞ and b_n=4nG_n,V(0,0), the target is

    2n / sqrt(4n²+M) ≤ b_n ≤ 1,
    0 ≤ 1−b_n ≤ 1−(1+M/(4n²))^(−1/2) ≤ M/(8n²).

Prove strict b_n<1 for every n when V is not zero a.e., equivalently when V>0 on a set of positive measure. The exact source then cannot persist at any t>0, s∈[0,1] unless V=0 a.e., because a_1=1. Retain the fixed readout; compensation by inverse b_n is a BR01 change. Prove the defect series, all fixed t-derivatives, affine s-derivative, explicit complete tail bounds on t≥ε and the finite u derivatives required by the external source map.

Route: bounded self-adjoint perturbation; scalar kernel construction/positivity; comparison with 0 and constant M; resolvent identity; Gaussian domination. Justify diagonal evaluation and strictness, not merely positive operator order. Use the accepted free kernel, not a new spectral acquisition. The work limit is one analytic derivation and at most one regrouping. An explicitly recorded routine correction within the same statement/class is permitted. Changing geometry, boundary, potential class or readout requires a dated BR01 revision. Signed or unbounded potentials and confining-potential surveys are outside r1.

Return the proof or exact failure in `notes/`, input versions and disposition in Register02, and a continuation in `research-progress/handoffs/`. Review claims belong in `reviews/` if an assessment is actually undertaken. Permitted navigation edits are MC11 README, concise DRAFT_HISTORY, references if genuinely used, and the history README. Preserve prior notes, reviews, requests, numerical records, registered archives and generated/synced instructions. No low-order calculation or potential fitting is authorized. Complete E02 at its stated boundary; do not silently start E03 or enlarge the class.

## Frozen MC11-AR-E03 request r1

**E — execution; recommended Sol; conditional.** Exact request: Note06 §6, equations (12)–(16), at V=0 and every s∈[0,1]. Freeze the accepted E02 return's versions at activation rather than inventing its future hash now.

Use the prescribed polynomial recurrences to prove every finite derivative/moment formula, positive-source lower bound and L² membership. Keep all boundary terms: the cross-pairing is c_(ℓ−i) for ℓ≥i and −Φ_s^(2(i−ℓ)−1)(0) for ℓ<i. The determinant identity is requested for every finite q≥1, k≥q−1, including k=q−1,q,q+1. General filtered odd endpoint derivatives do not vanish automatically. Use the ordinary du metric, normalized wedges and the frozen Hilbert embedding. State the Fock direct sum without adding an energy-domain claim.

One proof pass, at most one local correction; no moment table or finite-order sign campaign. A missing physical preparation principle or changed observation returns to BR01; choosing a signed all-order estimate belongs to B01. A family of identities at all finite indices is not an index-uniform sign bound.

## Evidence and model continuity

Read the [result index](../../../../../../../../result-summaries/README.md), [theta cluster](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), [patterns index](../../../../../../../../avoid/README.md), and especially [target reformulations](../../../../../../../../avoid/01_restating_the_target.md), [controls](../../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [review provenance](../../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md) and [scoped exclusions](../../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). Note06 §7 applies the [collision-control screen](../../../../../../../../result-summaries/12_collision_controls_and_screening.md) to the retained premises. The potential bound is generic, not a theta-specific sign mechanism.

Actual completed configuration: **gpt-6-astra / max**. Recommended next configuration: **Sol for E02**, because the operator, observable, theorem and route are fixed. Edward Baker selects the actual model, effort and chat. This packet changes none of those settings, creates no chat and schedules no research.

If continuing this chat after a model change, preserve thread `01a1aa32-c540-7671-aa14-f080cfbedd5d`, sole registration **0004**, actual title **Freeze MC11-BR01 analytic setup**, archive `chat-histories/0004_2026-11-05T05-33-36Z_freeze-mc11-br01-analytic-setup.json`. A new chat gets its own actual title/id and registration in this same MC11 history folder. Do not reuse AR-E01's history0003, copy its transcript, or relocate this history to a shared/formal archive. Refresh completed text at turn start and before finishing; use the bounded exact-turn `--after-turn ... --wait-seconds 60 --defer` follow-up until trusted native completion capture is verified. Never hand-edit registered JSON or claim an unsent final reply was captured.

## Pasteable continuation prompt

> Read root AGENTS.md, tools/CHAT_HISTORY.md and GPT_RESEARCH_MODEL_WORKFLOW.md; then MC11 Register02, the BR01 r1 Note06 and this return packet. Continue **[E] MC11-AR-E02 r1**, recommended Sol, after verifying its frozen input hashes. The selected model is the complete radius-1/2 cylinder, L_0=D_C², no wall, V=0, fixed-probe heat-damped Green response with external B_s and external t=πe^{4u}. Prove the specified all-n response/strictness/complete-sum theorem for the one comparison class 0≤V∈L∞(R), with unchanged readout and domains. Reuse AR-E01's accepted free kernel and R1; retain every radial contribution and independent time parameter. No spectral scan, fitted potential, confining-class expansion or determinant sign claim. Record the exact return in notes and Register02 and stop at the E02 boundary. Preserve this history's identity if continuing here, record actual model/effort, and prepare the conditional E03 continuation.
