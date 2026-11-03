# MC08-E01 continuation and model-change handoff

2 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance; actual **gpt-6.1-sol (Codex), reasoning effort ultra**, verified in chat `01a19d66-56e2-7ff2-a549-03561c41f801`, turn `01a19d66-5954-7bd1-a3e4-a07132e0161f`.

**Next: [B] MC08-B01 — Astra**, the already planned architecture decision. E01 r1 is complete; do not rerun its proof or begin an interval-optimization campaign without a consumer. No model switch, new chat or E02 dispatch is performed by this handoff.

## Result to carry forward

The [frozen E01 return](../../notes/01_NO_JUMP_ADMISSIBILITY_AUDIT_20261102.md) proves, for the complete time-zero theta source and original normalization,
\[
0\le v\le1/25,\qquad
R(v)=-(G(v)+G(v)^\dagger)\ge\frac1{8000}(2I-S-S^\dagger)\ge0.
\]
This holds directly on \(\ell^2(\mathbb N_0)\). The relative bound has no positive spectral gap. The proof pays the zero-angle limit analytically.

The paid constants are \(c_0>207/3344\), \(b_1>1/1000\), \((F(4)-c_0)/c_0<320/8073<1/25\), and \(|b_n|\le1/(24\,4^n)\). The exact logarithmic coefficient tail on the interval is at most \(2650133/3073907232<7/8000\). The complete-source primitive identity \(\Phi=(\psi''-\psi)/8\) and canonical \(\psi'(0)=-1/2\) yield all normalization constants. No quadrature, theta truncation, mode scan or angular sampling was used. The [support program](../../numerics/mc08_e01_exact_bounds.py) and [record](../../numerics/MC08_E01_EXACT_BOUNDS_20261102.json) replay only the finite algebra and rational bounds.

On this interval \(H=i(G-G^\dagger)/2\), \(L=\sqrt R\) are bounded and norm-continuous. The bounded trace-class jump expansion supplies a common CPTP, CP-divisible one-particle evolution with exact no-jump operator \(V(b,a)=K_bK_a^{-1}\). The scalar normalization \(F(v)\) is unchanged. This construction is direct on the infinite one-particle space; it does not await a mode limit. The estimate does not cover \(v=1\), and makes no failure claim there.

## Boundaries for the next model

- The abstract one-particle jump \(\sqrt R\) is not the proposed linear fermionic-loss instrument. B01 must select the common physical architecture before E02 writes that construction.
- Every finite-mode compression inherits the same positivity bound, but \(\sqrt{R_N}\) is generally not the compression of \(\sqrt R\). Do not assume finite completed channels are invariant restrictions of the infinite completion.
- For every fixed finite particle sector, \(\wedge^rK_v\) and its bounded no-jump generator are available. Full-Fock jump dynamics, its unbounded-generator domain, convergence and reservoir realization are not proved.
- Preserve the ordered occupation basis, phase, vacuum, and the real signed matrix element, including its positive prefactor. Conditional normalization and the no-jump probability must be retained. Transition probabilities alone erase the sign.
- The polynomial \(F_*(w)=1+w+2w^2\) is dissipative on \(0\le v<1/\sqrt2\) but has amplitude \(-v^2/F_*(v)^2<0\). Thus even the newly proved dynamical premise does not sign arbitrary fermion minors. Negative classical step rates can coexist with dissipativity.
- No new neighboring-index ratio or Mellin-curvature range was proved. \(v\) remains jump-length activity, not real Mellin tilt or heat time. Any future signed comparison must keep its denominator, exact index range and complete source tails.

E01 has same-model read-only checks of the symbol, constants, polynomial control and written scope. They share inputs and do not complete the planned separate **MC08-E03**, which still awaits frozen E01/E02 returns. No specialist or cross-model review of this new E01 result is claimed.

## B01 deliverable and routing

Read the [sole live register](../01_OPEN_QUANTUM_DYNAMICS_RESEARCH_PROGRESS_20261102.md) and [overview](../../research-overview/01_OPEN_QUANTUM_DYNAMICS_RESEARCH_OVERVIEW_20261102.md). Compare at most two architectures, defaulting to time-dependent quadratic \(d\Gamma(H_N)\) plus linear fermionic loss with \(B_N^\dagger B_N=R_N\). Use an explicit reservoir/repeated-interaction or memory alternative only if needed. Select one; state what is an exact finite-mode identity, an infinite-mode theorem, or a physical approximation.

Freeze locality/coupling range, environment preparation and size, time dependence, measurement instrument, success probability, parity/reference-phase readout and mode/particle limit obligations. Return the planned `notes/02_OPEN_SYSTEM_ARCHITECTURE_DECISION_YYYYMMDD.md` and a bounded E02 contract. E02 is **[E] — Sol** after that contract; E03 is **[E] — Sol, separate checker** after the frozen returns. B02 remains blocked on the reviewed realization or a stated scoped obstruction. No new mechanism search or numerical budget is issued here.

Follow the [result index](../../../../../../../../result-summaries/README.md), specifically [theta physical assessments](../../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md), and the [avoid index](../../../../../../../../avoid/README.md), specifically [generic re-realizations](../../../../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md), [control discipline](../../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md) and [scoped exclusions](../../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md). These are source pointers, not new evidence for a sign theorem. The [B/E workflow](../../../../../../../../GPT_RESEARCH_MODEL_WORKFLOW.md) governs routing.

## Model-change procedure and pasteable continuation

Record the actual new model and effort from turn metadata; do not infer them from the recommended task label. Keep this same chat's registration if continuing here. A genuinely new MC08 chat gets its own unique registration under the branch's `chat-histories/`; the existing brainstorm archive stays in place. Refresh histories at the beginning/end according to the repository workflow. Use the current progress entry as the sole status authority and preserve the frozen E01 proof and support record.

> Read repository AGENTS.md, GPT_RESEARCH_MODEL_WORKFLOW.md, the MC08 sole progress register, notes/01_NO_JUMP_ADMISSIBILITY_AUDIT_20261102.md and research-progress/handoffs/01_MC08_E01_CONTINUATION_20261102.md. Complete **[B] MC08-B01 — Astra**: choose one common physical architecture using the proved interval 0<=v<=1/25 and exact unchanged K_v. Compare at most two constructions, preserve the signed occupation amplitude and no-jump instrument, specify finite/infinite scope and readout/parity obligations, and issue the bounded E02 contract. Record actual model/effort and preserve the current checking status. Do not treat local Lindblad admissibility as a theta minor-sign theorem or start numerical execution before the contract exists.
