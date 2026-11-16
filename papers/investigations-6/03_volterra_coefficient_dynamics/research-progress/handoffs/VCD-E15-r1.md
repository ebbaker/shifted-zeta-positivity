# VCD-E15 r1 — shared-memory midpoint equivalence and exact error transport

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex assistance. Type E, parent B04 decision08. Explicit dispatch gpt-6.1-sol/ultra; separate backend attestation unavailable. Lead actual model/effort unavailable. One fixed analytical comparison and one correction pass; no numerical campaign.

Prove/correct decision08's fixed comparison. Let A=J_N real symmetric, e=e_(N-1), beta=beta_N>0, and k any scalar entire kernel. Establish unique entire y_k solving y'=iAy-beta e(k*e^T y), y(0)=e0, using complex straight-segment convolution. Define T_k similarly with initial matrix I and f_k=e0^T T_k e0. This is a finite Volterra model, not automatically a positive-measure or canonical-source realization.

1. Prove H_k(t,s)=y_k(t)^T y_k(s)-beta ∫_0^t∫_0^s k(t+s-u-v)(e^T y_k(u))(e^T y_k(v)) dv du equals f_k(t+s), for all complex t,s. Use (partial_t-partial_s)H=0 plus H(t,0)=f_k(t). At t=s=z/2 this is the exact common-kernel midpoint model in E13, including both errors and its full kernel horizon. In particular its output is the same direct full-height Volterra approximant. k=0 recovers bare quadrature. Do not claim k=0 is a normalized physical tail.
2. For k,l entire, delta k=k-l, prove f_k-f_l=-beta (e0^T T_k e)*(delta k)*(e^T T_l e0). Derive through Volterra variation-of-constants or a rigorous convolution identity; no unavailable Laplace transform for arbitrary entire k. Preserve this signed correlation before taking absolute values.
3. If the first nonzero derivative of delta k at zero has order q, prove the scalar difference first occurs at order 2N+q, with coefficient (-1)^N(product_{j=1}^N beta_j) delta k^(q)(0)/(2N+q)!, and explain the all-equal/flat case. Prefix tridiagonal propagation determines leading boundary transfers. Both normalized even kernels have q>=2 unless identical.
4. Give an explicit fixed-disk bound. One sufficient candidate, for radius R, M=max(sup|k|,sup|l|) on |z|<=R, eps=sup|delta k|, L=||A||+beta M R, is ||T||<=exp(L|z|) and |f_k-f_l|<=beta eps |z|^2 exp(L|z|)/2. Prove or correct; state its absolute/generic scope and no uniform moving-tail control. Better bounds are optional only if routine within this route.

Connect to actual theta k_N and exact canonical b from E06 without asserting the generic result uses b or determines k_N. Identify unprovided premises for zero transfer: justified source-sensitive kernel error, modeled zero-free margin/contour, and degree or terminal control. Preserve E07/E10 distinct classes and the catalog screen. No sign or zero-confinement theorem, no universal no-go, no claim that alternative joint models or improved kernels fail.

Own only notes/13_VCD_E15_SHARED_MEMORY_EQUIVALENCE_20261116.md and research-progress/handoffs/VCD-E15-r1-return.md. Read root rules and result/avoid indexes. Use direct proofs and accepted local inputs; newly imported theorems require primary-source checking. Return a scoped disposition and all corrections. No shared register/navigation/chat edits.

## Pinned inputs
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/11_VCD_E13_MIDPOINT_AUDIT_20261116.md` SHA-256 `689a7d228dd4e5722cdb9734f9895c176d0bf442dfaccb5e1193013a4283620f`
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/04_VCD_E04_TAIL_FOUNDATIONS_20261116.md` SHA-256 `116f29472c162272fa554a564f1c88ea02573ee27bd43ee36c2e8e9eefc63880`
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md` SHA-256 `6ef63b32c053f3baf3c7df1ecbf7dd11947958eb091f3b2cb527280a4da95c47`
- `papers/investigations-6/03_volterra_coefficient_dynamics/brainstorm/notes/08_VCD_B04_SHARED_MEMORY_COMPARISON_DECISION_20261116.md` SHA-256 `ce709c23c49adc703307e7f6c529c26a6afd9f722c70981be8bf1c70387f8b35`
