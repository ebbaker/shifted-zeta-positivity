# VCD-E10 r1 — smooth next-score defect freedom

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex assistance. Type E; parent B03 decision06. Explicit helper dispatch gpt-6.1-sol/ultra; lead backend/effort unavailable. One fixed construction, one correction pass; no numerics or zero claim.

Fix N>=1 at lambda=0, canonical mu and score V'. Prove or correct the following finite-step statement. There exists even h in C_c^infinity(R), supported away from 0, such that nu=(1+epsilon h)mu is positive and has identical moments through 2N (so q_0,...,q_N and a_1,...,a_N are unchanged); its canonical adjacent defects e_j vanish for j<N but e_N!=0. The source is smooth and equals theta outside a compact set; the own/canonical score difference can be arbitrarily small in L-infinity by scaling epsilon. No assertion about nonreal zeros for this smooth perturbation.

Route: impose the finite real linear constraints integral u^(2k)h dmu=0 for k=0,...,N and integral V' q_j q_(j-1) h dmu=0 for j=1,...,N-1. Target L_N(h)=integral V' q_N q_(N-1)h dmu!=0. Show target test function is outside the span of the constraints on positive u: otherwise V'(u)Q(u)=P(u), with Q an odd polynomial of degree 2N-1 with nonzero leading coefficient and P an even polynomial, contradicting V'(u)~4πe^(4u) as u→+infinity. Elementary finite-dimensional duality on even smooth bumps gives h in the joint kernel but outside target kernel; provide proof of that duality or explicit separated-bump linear algebra. Scale to positivity and small bounded score difference. The exact equality of q_N makes the target adjacent defect precisely epsilon a_N L_N(h). Matching finite smoothness is not the same as retaining canonical arithmetic.

State how this complements E08 commutator endpoint cancellation. You may reuse provisional E08 statement as motivation only; derive any identity you need independently. Do not turn lack of exact next-step propagation into a zero-location obstruction or a universal no-go. Screen actual premises: square support/canonical full source fails; source tails, smoothness and arbitrary small score difference pass. Compare E07's nonsmooth/nonreal control without merging their preservation lists.

Outputs only notes/10_VCD_E10_SMOOTH_NEXT_DEFECT_FREEDOM_20261116.md and research-progress/handoffs/VCD-E10-r1-return.md. Routine proof repair permitted; changed invariant goes to B03. No shared/status/chat edits.

## Pinned sources
- `papers/investigations-6/03_volterra_coefficient_dynamics/brainstorm/notes/06_VCD_B03_SMOOTH_NEXT_DEFECT_DECISION_20261116.md` SHA-256 `74fc048a7aa54a734979505f198da14dcfe36c192693acbde2049269e019343b`
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/05_VCD_E05_SOURCE_SCORE_RESIDUAL_20261116.md` SHA-256 `428b059ee5a6d522afcd4ae3596b2358540ccef16259e0a817604e3f86eca6a1`
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/06_VCD_E06_EXPONENTIAL_SCORE_RESIDUAL_20261116.md` SHA-256 `6ef63b32c053f3baf3c7df1ecbf7dd11947958eb091f3b2cb527280a4da95c47`
- `papers/investigations-6/03_volterra_coefficient_dynamics/notes/07_VCD_E07_FINITE_CANONICAL_SCORE_CONTROLS_20261116.md` SHA-256 `ee0cfd6ba86972c96c0c0cb8a8713892f1f897cc25e4ab1710550500ec075d1d`
