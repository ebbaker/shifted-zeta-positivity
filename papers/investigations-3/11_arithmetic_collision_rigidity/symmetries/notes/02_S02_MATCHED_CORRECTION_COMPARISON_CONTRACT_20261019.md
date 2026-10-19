# INT-01 extension: S02-T1 matched correction comparison

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6.1-sol (Codex), actual reasoning effort ultra**, verified from session metadata. Internal LLM research and delegated audit; no specialist review.

## Scope, comparator and primary metric

Continue with S02-T1 after the completed S01 integration. Compare the full analytic correction with the strongest applicable implementation of transport Notes 20–22's frozen exponential. The primary metric is the uniform **Q-disk residual allowance eta**, with the same Cauchy factors (1,2,8) for derivatives 0–2. Both receive the strongest common corrected published residual, unchanged eight-mode finite sum and analytic ninth-mode matching. A win against the old absolute baseline alone does not pass a new superiority gate. This contract records the comparison after source audit and bounded term diagnostics, before retained comparison implementation; it is not an independent preregistration.

Keep B=[1/100,1/5] x [999,1001] and C=[1/100,1/5] x [1017,1019], radius R=1/2 at each real center X, and N=8 fixed on each disk. Upper enclosing rectangles are x in [998.5,1001.5] or [1016.5,1019.5], 0<=y<=1/2. Use the opening fixed grids 4/24/8 and 8/64/16 in t/x/y, 768 and 8192 complex cells, plus their real slices. Retain 192/256 bits. Do not enlarge the grid or tune parameters after the ordering is decisive.

## Objects and common ledger

Write k=pi/8, A for the original symmetric nonvanishing normalizer, and C_N(t,z)=B_t exp(-kz) J_N(t,z), with B_t=(-1)^(N+1) sqrt(pi)/4 exp(-pi^2 t/64). The candidates are F_an=(G_N-C_N(t,z))/A(t,z), and F_fr,X=(G_N-C_N(t,X) exp(-k(z-X)))/A(t,z). Hold t,N,X fixed while differentiating in z. F_fr,X is a family of analytic disk formulas, not the analytic continuation of the diagonal center-value function.

For natural cutoff m, use the exact decomposition

H-G_N+C_N^an = (H-G_m+C_m^pub) + (G_m-G_N)-(C_m^pub-C_N^pub) + (C_N^an-C_N^pub).

For the frozen candidate replace only the last analytic correction by C_N(t,X) exp(-k(z-X)). Both candidates thereby receive the SAME Note 22 printed-jump matching bound; it must not be mislabeled as a direct analytic-jump theorem. Use Eedge=2 P_* (exp(Lambda_edge)-1) on C and zero on B, with the Note 22 logarithmic endpoint refinement and all time/rectangle extrema paid. Report the original wider direct-interval transition payment separately.

Use the opening exact prefactor and corrected Corollary 6.4 remainder; also report the earlier Z B_C bound so sharpening old source data is not credited to the new correction. Bound the full continuation by K W R sup_complex |J8_z| and frozen continuation by K W R sup_real |J8_x| on the same fixed covers. No extra K is inserted by confusing fixed A(X) with analytic A(z). Report the original frozen theorem with its global profile bound separately from this stronger applicable real-slice implementation.

## Physical correlations and selection gate

Include b=(log A)_x and b_x on real centers and retain the signed b+k cancellation. The physical uncorrected error vector is -c(1,-k,k^2), c=C8(t,X)/A(t,X); in Q coordinates its leading vector is -c(1,-k-b,(k+b)^2-b_x). For a Q residual r, physical errors are (r,r_x+b r,r_xx+2b r_x+(b^2+b_x)r). Demodulated physical errors use r_x+(b+k)r and r_xx+2(b+k)r_x+((b+k)^2+b_x)r. Do not call these independent error boxes or omit normalizer derivatives.

Select frozen per-disk jets for S02-T2 if its complete eta is smaller. Retain the full analytic expression for a consumer explicitly needing a single analytic residual over the entire box (such as the existing S03 construction); the selected family must not be propagated as an unmodified heat solution. If the full formula fails the strongest-comparator gate, document this precise first-derivative-continuation-ledger limitation and stop. No evaluated whole-cell approximant, margin, cost gain, new coverage, or global improvement is implied by S02-T1.

## Validation and source discipline

Pin the original S02 note/checker, transport Notes 20–22 and matching code, relevant manuscript, and this contract. Repeat scalar/closed-cover calculations at both precisions. Verify branches, fixed cutoffs, removable-point handling, exact real-center equality, distinct derivatives and correction-wave identities. Fresh source-specific collision controls test the unchanged downstream acceptance interface using their own errors. New bound/normalization guards challenge the actual new comparison. A separate internal reader will assess the derivation, rerun decisive records and classify the result.

Follow the [result summaries](../../../../../result-summaries/README.md) and [patterns to avoid](../../../../../avoid/README.md), especially [controls](../../../../../result-summaries/12_collision_controls_and_screening.md), [normalization](../../../../../avoid/08_normalization_and_constant_slips.md), [preserving cancellations](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md), [target reformulations](../../../../../avoid/01_restating_the_target.md) and [scope](../../../../../avoid/07_scoped_exclusions_read_as_universal.md). This is a quantitative comparison, not an RH-equivalent criterion.
