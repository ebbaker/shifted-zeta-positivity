# AGC-B02 r2: a holomorphic retained-correction contract

19 November 2026, America/New_York. Prepared for Edward Baker with OpenAI Codex LLM assistance. Actual lead backend/effort unavailable in canonical public-history metadata. A bounded algebra check was explicitly dispatched gpt-6.1-sol/ultra; dispatch is not independent backend attestation.

**B decision: contract fixed; next E13 r2 is ready, unexecuted.** The accepted r1 estimator and E12 pilot are retained. Their finite sign change is a complete allowance gain in known coverage, not new coverage. The scalar heat bound loses through its initial spatial supremum. The next calculation will retain the arithmetic correction in a genuinely holomorphic reference and pay the mismatch to the published value formula. This is the third B01 candidate, now made concrete; it does not repeat the failed separate-supremum heat calculation or enlarge the numerical campaign.

Read [results](../../../../../result-summaries/README.md), [patterns](../../../../../avoid/README.md), [Cluster18](../../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md), [Controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [classification01](../../../../../avoid/01_restating_the_target.md), [joint-bound12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [factor13](../../../../../avoid/13_a_factor_is_not_the_target.md), and [scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md). This is a finite source-acquisition task, not an RH-equivalent criterion. No useful corrected margin is asserted in this decision.

## Candidate reference, frozen for the next proof

Keep the literal H and the existing cell X=140101/10, A=2, h=1, r=9/10, t in [9/100,1/10], N=33. Put k=pi/8, w=z/2+kt and

    p(w)=1−2(sqrt(w/(2pi))−N),
    C_0(p)=[exp(pi i(p²/2+3/8))−i sqrt(2) cos(pi p/2)]/[2 cos(pi p)],
    C_0^sharp(p)=conjugate(C_0(conjugate(p))),
    A_N(w)=sqrt(w)/2 · [(w+i)C_0(p(w))+(w−i)C_0^sharp(p(w))],
    J_N(t,z)=(-1)^(N+1) sqrt(pi)/4 · exp(−kz−k²t),
    C_hol(t,z)=J_N(t,z) A_N(z/2+kt),
    Q_N=P_N−C_hol.

Use the principal square root near the positive w-axis. A coarse bound on this fixed rectangle is 0<Re p(w)<2/5, keeping the displayed C_0 denominator clear of all half-integer zeros; the next proof must document the bound. No global claim about the C_0 poles or their removability is needed.

Primary passages rechecked for this choice: [Polymath v2](https://arxiv.org/html/1904.12438v2), (52), (53), (68), Corollary6.4 and its C_t formula. On the real T-axis elementary cancellation gives

    M_0(iT) U(T) exp(i pi/8)
       =−sqrt(pi)/8 · exp(−pi T/4) sqrt(T)(T+i).

Consequently C_hol(t,x) agrees with the published C_t(x). Off the real axis the published value correction is

    C_val(t,x+iy)=J_N(t,x+iy) A_N(x/2+kt),

while the holomorphic lift uses w=x/2+kt+iy/2. It is the *lift*, not the real-part display, that may be differentiated holomorphically.

The candidate defect and mismatch identities to prove and bound are

    (partial_t+partial_z²) C_hol = J_N A_N''(w)/4,
    R_Q=R_N−J_N A_N''(w)/4,
    |C_hol−C_val| <= sqrt(pi)/4 exp(−kx−k²t)
                     · |y|/2 · sup_vertical |A_N'|.

The A_N and A_N' terms cancel exactly in the defect. A bounded nonauthor algebra check confirmed the sign, constants, branch convention, physical conjugation symmetry and vertical factor. This is candidate validation for the frozen packet, not acquisition of the derivative suprema or a corrected zero margin.

## Complete error and comparator

For H−Q_N use the retained-correction published budget (both term replacement errors and the full delta_-+delta_+ remainder) **plus** the vertical mismatch above. Reacquire count, lower denominator, center and discriminant for Q_N. Never combine the smaller error with P_N's old center or denominator. Include the complete new defect in a time consumer. Compare at identical information with direct evaluation of this same Q_N using E13 r1's refined allowance.

For an exact colliding field/reference with E=0, the strict reference discriminant still vanishes at the event. The generic contour/heat formulas retain every control with its own data. Euler-factor, weighted-square, finite-prime and finite-profile controls cannot import the unchanged theta RS budget; this source-identity failure is not itself a numerical exclusion. Changed observation kernels fail the physical equation. No new canonical claim is made until the corrected inputs and final all-time margin are paid.

## Next bounded task

[E13 r2 request](../../research-progress/handoffs/AGC-E13-r2-request.md): one derivation and one correction pass, explicit A_N' and A_N'' bounds on this same rectangle, full error/defect, and comparison decision. No numerical extension is preauthorized by this packet. A subsequent E12 revision can be frozen from the resulting bounds if worthwhile. Height/time extension B03/E14 stays conditional on a useful further acquisition; no all-height or time-zero passage is opened here.
