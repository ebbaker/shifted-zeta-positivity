# VCD-E08 r1 — full canonical-score rigidity and boundary defect transport

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex assistance. Type E; parent B03 decision05. Explicit helper dispatch gpt-6.1-sol/ultra; actual lead backend/effort unavailable. One frozen theorem bundle and one correction pass. No numerics, no new zero criterion. Source W_theta and Fourier readout unchanged; default lambda=0, fixed allowed lambda optional with hypotheses checked.

## Claims and proof route

Let nu be an even probability measure of infinite support with integral exp(R|u|)(1+|V_theta'(u)|)dnu finite for every R>0, and positive Jacobi links. Suppose a_n integral V_theta' q_n q_(n-1) dnu=n for every n>=1, where q_n are its own orthonormal polynomials. Prove nu=mu_theta. Route: q_n q_(n-1) form a triangular basis of odd polynomials; canonical adjacent equations give integral f' dnu=integral V_theta' f dnu for all polynomials, by derivative orthogonality. Exponential integrability permits Fourier expansion, hence the distributional identity nu'=-V_theta' nu. Multiply locally by exp(V_theta) and conclude normalized nu=mu_theta. Give necessary density/regularity justification for a measure, not only densities. This is unconditional source identification, not a Fourier-zero assertion.

Define polynomial Stein defects s_k=integral (V_theta' u^k-k u^(k-1))dnu, and adjacent e_n=a_n integral V_theta' q_nq_(n-1)dnu-n. Derive triangular conversion with leading coefficient kappa_(n-1)^2 in e_n versus s_(2n-1), where kappa_j is leading coefficient of q_j. Identify precisely what finite adjacent zeros determine (all odd test degrees <=2N-1), and what new test is introduced at N+1. Do not assert uniform conditioning.

For an even positive locally absolutely continuous density with own-score IBP and enough integrability, define E_ij=integral(V_theta'-V_nu')q_iq_j dnu. Derive [J,E]=0 entrywise and exact cut formula [J_N,E_N]=-a_N e_(N-1) E_(N,head)+a_N E_(head,N)e_(N-1)^T, checking orientation. Tail row/column are unpaid; this is not finite closure. If b=V_theta'-V_nu' bounded, record ||E_N||<=||b||infinity, but do not infer Fourier-zero control. Compare E07 controls: finite zero rows and small bounded defect do not imply full rigidity.

Deliver only notes/08_VCD_E08_FULL_SCORE_RIGIDITY_20261116.md and handoffs/VCD-E08-r1-return.md. Standard polynomial/distribution arguments may be derived directly; new imported facts require verified primary sources and reference details to root. Completion: full proof/qualified correction with explicit finite-boundary formula and unpaid quantities. New invariant/zero inequality returns to B03. Do not edit shared files or chat registry.

## Frozen inputs
- `papers/investigations-6/03_volterra_coefficient_dynamics/brainstorm/notes/05_VCD_B03_FULL_SCORE_AND_TAIL_DEFECT_DECISION_20261116.md` SHA-256 `ad83eb4a191f158367c5100fef75808e14a01d694fed55a0aa5abab1539e890d`
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/04_VCD_E04_TAIL_FOUNDATIONS_20261116.md` SHA-256 `116f29472c162272fa554a564f1c88ea02573ee27bd43ee36c2e8e9eefc63880`
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md` SHA-256 `428b059ee5a6d522afcd4ae3596b2358540ccef16259e0a817604e3f86eca6a1`
- `papers/investigations-6/03_volterra_coefficient_dynamics/research-progress/handoffs/VCD-E07-r1.md` SHA-256 `8a3575b830ddf260f3ffa08a139554c537d5503142932f7842ba1822f02f60d9`
- `papers/investigations-6/03_volterra_coefficient_dynamics/manuscript/main.tex` SHA-256 `18346543517c374c5e55d095b6c6847a0ef21f2e18917fff428d54901cf60dcc`
