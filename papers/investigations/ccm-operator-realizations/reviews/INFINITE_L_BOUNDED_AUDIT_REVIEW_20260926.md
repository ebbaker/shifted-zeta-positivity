# Review of the bounded infinite-L audit

Date: 26 September 2026.

Drafted for Edward Baker with LLM assistance. Model: GPT-6 (Codex); the exact variant and reasoning-effort setting are not exposed in this session. This is a sequential same-agent adversarial check of [round 5](../notes/CCM_INFINITE_L_BOUNDED_AUDIT_20260926.md), not independent review or formal verification.

## Verdict

The recommendation to change approach is supported by two specific method obstructions. The scalar upper estimate cannot stay bounded even if the exact odd gap is supplied. The current high-tail estimate, when it pays for each prime translation separately, requires a cutoff growing at least exponentially in exp(L/2), at thresholds bounded below independently of L. Neither result is an obstruction to the actual Weil limit.

The exact relative trace reduces to a ground-state moment, as expected from the known CCM transform formula. The prolate part gives a useful, explicit sufficient comparison target and controls approximation of the candidate itself. It does not establish comparison with the actual Weil ground state. The note stops after the requested two mechanisms and makes no RH or new infinite-support convergence claim.

## 1. Symbol and mass bounds

The global upper bound a(t)<=one-half log(1+t^2) uses the digamma recurrence in the correct direction. At z+1=5/4+it/2, the remainder radius is 1/[12(5/4)^2]=4/75. Both reciprocal real parts being subtracted are positive. The inequality |z+1|^2<=25(1+t^2)/16 and the elementary logarithm bounds give the claimed symbol estimate uniformly, including t=0.

Jensen applies to zero extensions of H1 functions with zero endpoint values. For Je_n, the squared norms are 3/d_n^2 and 1, so the factor of one-half in the logarithm is retained. Summing the mass estimate yields the term (D+|epsilon|)L^2/8. The function log(1+c^2 x^2)/x^2 decreases, and its integral is pi*c, producing exactly sqrt(3)*L/4 for the remaining term. This is an upper estimate for the actual trace, not an equality.

The even trial Je_1 supplies the energy upper bound and the global form floor supplies the lower bound. The proof does not set epsilon to zero. For L>=2 these imply |epsilon|<=D+6. The odd first sine bounds the odd gap above by 2D+8<=4D. Thus the upper-estimate expression U/kappa is at least L^2/32 whenever kappa>0. Replacing kappa by a valid smaller certified gap increases that expression.

The distinction in the last sentence is essential: a divergent upper estimate does not force the trace to diverge. The finding rules out making this particular estimate uniform by improving only its gap input. Sharper mass control or a relative argument is not excluded.

## 2. Prime norm sum and cutoff obstruction

For every q<exp(L), the translation-fiber path has at least two vertices and pair norm at least one. The q=exp(L) endpoint is absent from S, so the lower estimate does not charge a null operator. With n=ceil(X/2)-1, the integer 2n is strictly below X, including when X itself is an even integer or a prime power.

The central binomial coefficient divides lcm(1,...,2n): each contribution to its prime valuation is zero or one, and there are at most floor(log_p(2n)) such contributions. Its lower bound by 4^n/(2n+1) is the elementary maximum-versus-average coefficient bound. Together these give S>=[(X-2)log2-log(X+1)]/sqrt(X). The simplification S>=sqrt(X)/4 for X>=16 is conservative and does not use a prime-number theorem.

In the high-tail estimate, leakage and the pole penalty are nonnegative deductions. Consequently success at threshold s requires a(T)>S+s. The frequency restriction T<2*pi*(M+1)/L and the symbol upper bound then give equation (9), with exponent one-half exp(L/2)-2C inside the square root. Taking the square root leaves one-quarter exp(L/2)-C in the asymptotic exponent. These two factors were checked separately.

The result concerns the specified estimate for L>=log16 and s>=-C with C fixed. It is not an actual spectral lower bound, a statement about all Schur methods, or an obstruction at thresholds escaping to negative infinity. Arithmetic cancellation is precisely what summing individual prime norms discards.

## 3. Coupling and trace identities

The general coefficient estimate retains the prime sum and the hyperbolic pole factor. The bound |b_n|<2 from log13 is not treated as support-uniform. Replacing 2 by beta_L in the previous geometric remainder gives the prefactor 2*beta_L; for r/K<=theta this simplifies to 2*beta_L/(1-theta). The conclusion that order L expansion terms suffice concerns a fixed absolute tolerance, not a tolerance relative to an unknown tiny energy scale.

The small-energy decomposition uses an eigenbasis of K. All contributions <v,Mv>/k are nonnegative. It would be misleading to claim cancellation between those positive contributions; the note instead requires suppression of the mass in dangerous stiffness directions.

For the exact rank-one square, the boundary sum is s=a0+2 sum(a_n). The determinant is product(d_n^2)*a0/s, so positivity makes the mean nonzero. The inverse trace correction is 2/a0 times sum(a_n/d_n^2). Adding the infinite free trace changes the first term to L^2/24. Direct integration gives the same half second moment. These constants agree with the normalized transform identity.

The transform is centered in logarithmic coordinates and normalized at zero, removing the irrelevant phase and scalar from the source formula. The free tail is included in the sinc factor throughout. The trace identity does not turn a signed ground profile into a probability density. No pointwise sign claim is used.

The logarithmic diagonal comparison family has M_nn=log(1+d_n^2)/d_n^2 and K_nn=log(1+d_n^2), hence trace L^2/24 after adding the free modes. It satisfies the stated generic structural conditions. It has no arithmetic prime/pole distribution, and the note does not label it a CCM counterexample. Its role is limited to disproving an inference from those generic properties alone.

## 4. Prolate input, tails, and normalization

The prolate asymptotic estimate (P) is explicitly cited as input. The review has checked how the audit uses that input, not independently verified the underlying classical prolate theorem. The missing approximation to the actual Weil ground state is never assumed to follow from (P).

The passage from h_lambda to its arithmetic sum contains two errors: the finite-sum approximation and the omitted Gaussian terms. Both appear in the note. The finite term has pointwise bound C*lambda^(-1)*exp(-x/2), whose integral on the logarithmic interval is at most 2C*lambda^(-1/2). The omitted sum is bounded by the decreasing Gaussian envelope plus its integral divided by the sampling step. The exterior tails of the Xi kernel are also retained.

Even symmetrization is explicit and contracts both the symmetric weighted L1 norm and L2 norm. It therefore avoids silently assuming exact reflection symmetry for the unsymmetrized prolate arithmetic sum. The limiting Xi kernel has nonzero integral and positive L2 norm, so the subsequent normalizations are bounded away from zero for sufficiently large support. They do not use endpoint normalization, which could have a very different scale.

## 5. Fourier-resolution and comparison thresholds

The Fourier projection estimate is applied to the restricted true kernel, whose equal endpoint values place it in periodic H1. It is not applied to the zero extension as if its weak derivative had no boundary contribution. Its derivative norm after L2 normalization stays bounded. Comparing the candidate to that restriction then gives C*sqrt(L)*exp(-L/4)+C'*L/(N+1) without requiring derivative estimates for the candidate.

N of order at least L^(7/2) makes the latter error O(L^(-5/2)) and the free trace O(L^(-3/2)). This is only a sufficient resolution schedule for the candidate. It proves no Fourier convergence rate for the true Weil eigenvector.

For the transfer lemma, the denominator stays at least a/2 because |integral(u-v)|<=sqrt(L)*delta. The second-moment functional has L2 norm sqrt(integral(x^4))=L^(5/2)/sqrt(80). The one-half in tau cancels the factor 2 from the denominator bound, yielding equation (16). The real-transform estimate follows from the same normalization calculation. No positivity of u or v is required.

If the unproved ground-state comparison (18) held, these estimates would give a bounded positive spectral trace and identification on a real interval. The previously established normal-family criterion then applies. The reasoning is conditional; the new comparison target is not an unconditional Xi theorem or a new verification of the finite CCM hypotheses.

## 6. The residual test uses an even-sector separation

For a normalized projected candidate, excited even eigenvalues are at least epsilon_1^+. If rho<epsilon_1^+ and sigma is a positive lower bound on their distance from rho, the squared excited weight is at most r^2/sigma^2. Sign-aligned ground-vector distance is at most sqrt(2)*r/sigma. Normalizing the Fourier projection contributes at most sqrt(2) times the discarded norm, giving (19).

This test needs the second **even** level. The odd gap considered in the previous rounds does not establish it or prove even-ground simplicity. A small residual without this separation can describe a vector anywhere in a low-energy even cluster. A prolate gap also cannot be substituted for a Weil gap without a comparison theorem.

The decisive ratio r/sigma remains unbounded by any result in the audit. A proof of its stated L-dependence would require new arithmetic control. The candidate concentration and polynomial resolution estimates do not supply it.

## 7. Controls and disposition

The new control program uses Fraction and integer arithmetic. Matrix inversion and elimination check the trace and determinant formulas through distinct finite calculations, including signed coefficients. There are 20 rational spectral-parameter comparisons and 256 integer checks of the binomial ingredients. These controls support normalization and arithmetic consistency; they are not proofs for all n or certified eigenvalue computations. Those scope distinctions also appear in the saved record.

No new arithmetic support sweep, large matrix, third-party PDF, snapshot, commit, or release is part of this round. Earlier notes and programs are preserved. The overview and navigation should record the completed audit and its decision rather than continuing to present the fixed-L Schur computation as the next default task.

The audit is complete within its two-mechanism scope. Changing approach is justified; claiming the infinite-L problem solved, disproved, or nearly solved would not be. A further research round should start from a concrete arithmetic estimate for (20) or a stated alternative normalized-moment comparison, with its assumptions exposed.
