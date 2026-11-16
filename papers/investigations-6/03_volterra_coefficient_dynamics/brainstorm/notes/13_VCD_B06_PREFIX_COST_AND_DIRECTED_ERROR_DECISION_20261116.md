# B06 pass2 — match the coefficient cost and retain a directed error

16November2026, America/New_York. Prepared for Edward Baker with substantial OpenAI Codex assistance. Lead actual model/effort unavailable; proof/assessment dispatches gpt-6.1-sol/ultra, separate backend attestation unavailable.

**Follow-up decision, proof pending.** [Decision12](12_VCD_B06_ERROR_PHASE_CONSUMER_DECISION_20261116.md) selected the complete E15 quadrature-error phase. E21 confirms the law/moments; E22 confirms its proposed quantitative rate while drafting. Preserve [result index](../../../../../result-summaries/README.md), [cluster18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [avoid index](../../../../../avoid/README.md), [classification01](../../../../../avoid/01_restating_the_target.md), [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), [separate-bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md) and [control catalog12](../../../../../result-summaries/12_collision_controls_and_screening.md).

## A correction must be compared with the next physical head

The corrected readout G_N+L_N requires beta_1,...,beta_N: G_N needs beta_1,...,beta_(N-1), and h_N^*=product_(1..N)beta_j needs beta_N. The next physical quadrature G_(N+1) uses exactly that same input set. Its error is L_(N+1)E_(N+1), with
L_(N+1)/L_N = -beta_(N+1) z²/[(2N+1)(2N+2)].
The extra unknown beta_(N+1) can be bounded by the proved envelope; it is not needed to compute G_(N+1). Thus the next-head error allowance relative to |L_N| has order |z|²log²N/N² on the same bounded-phase range, while the plain monomial-correction allowance has order |z|²log²N/N.

There is also an exact local comparison: as z approaches0 through nonzero values,
(F-G_N-L_N)/(F-G_(N+1)) tends to
[beta_N+beta_(N+1)+2sum_(j=1)^(N-1)beta_j]/beta_(N+1)>1.
This follows from E21's variance and the first nonzero next-head coefficient. It is local actual-error ordering and an asymptotic comparison of specified allowances, not an all-z modulus ordering. Do not declare the corrected scalar a superior model at equal input cost without a separate geometric advantage.

## Selected implementation: an oriented enclosure at the available prefix

At a fixed available head N suppose only beta_1,...,beta_(N-1) are acquired. The phase formula remains
F=G_N+d_N(z) a_N E_N(z), d_N(z)=(-1)^N z^(2N),
a_N=(product_(j=1)^(N-1)beta_j) beta_N/(2N)! >0.
The symbol a_N here is an error amplitude, NOT a Jacobi link; use a distinct notation in the proof. The adjacent envelope gives
0<beta_N<=B_(N-1)-beta_(N-1), with beta_0=0,
so the error amplitude has a computable upper bound A_N from the known prefix and B_(N-1). The degree-only E22 budget epsilon_N does not need the missing link. For z!=0 let w=G_N/d_N. A possible zero must satisfy
-w=a_N E_N in union_(0<a<=A_N) {a(1+eta): |eta|<=epsilon_N}.
This set retains the sign of the missing amplitude and the known omitted-walk phase.

A readily computable sufficient test is dist(-w,[0,A_N])>A_N epsilon_N. A useful amplitude-free special case when epsilon_N<1 is Re w>=0: the actual amplitude is strictly positive and Re E_N>=1-epsilon_N>0, so F cannot vanish there, even if G_N=0. The zero at z=0 is excluded separately by F(0)=1. When an exact amplitude is acquired, the smaller disk |w+a_N|>a_N epsilon_N is available, but the next physical head must be compared at that cost.

For a contour, require a strict certified separation from the closed union 0<=a<=A_N (a subset of the larger capsule). This contains every straight homotopy error t a_N E_N, 0<=t<=1, so F and G_N have equal zero counts when the contour hypotheses are paid. A mere pointwise half-plane observation is not a global contour count. The union also implies a sector constraint: for epsilon_N<1, any nonzero point in it has argument within arcsin(epsilon_N) of the positive ray; hence any F zero lies where -G_N/d_N lies in that sector and has modulus at most A_N(1+epsilon_N). Derive the geometric statements rather than assuming their boundary cases.

This selects a signed consumer of the exact E15 aggregate error with a degree-only phase allowance and a finite-prefix amplitude bound. It does not select a new phase from F, does not use B05's disproved fixed normalization, and does not assume finite models are real-rooted. The still-unproved input is a useful canonical placement of the finite-head phase/margin on expanding compact contours, or an accompanying real zero count. Weighted-square collision controls share the phase theorem and therefore can pass some local tests; no assertion that this full family of margins holds for them or theta is made.

Freeze E24 for this exact same-input comparison and directed-error geometry, with E21/E22 phase identification conditional until final proof pins are supplied in the return. E23 will separately assess the three proofs and final synthesis. No coefficient campaign or new numerical window.
