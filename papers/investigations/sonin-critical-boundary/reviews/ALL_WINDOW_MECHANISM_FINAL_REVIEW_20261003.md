# Final mechanism review: translated probes and the spatial scalar-tail barrier

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort are not exposed and are not inferred. This is a separate-agent same-model audit, not independent specialist refereeing.

Status: the reviewed analytic reductions are consistent, and the translated-probe package passed a separate 256-bit replay. These are five positive two-dimensional Gram matrices. They do not certify a new full source window or the all-window sign. The scalar-tail obstruction is a theorem about estimates separating the arithmetic norm from archimedean energy, not about every possible certification algorithm.

## 1. Reviewed artifacts and source binding

Reviewed:

- [Translated prepared-probe criterion](../notes/ALL_WINDOW_TRANSLATED_PROBE_CRITERION_20261003.md).
- [Outward polynomial-probe generator](../numerics/all_window_mechanism_20261003/certify_translated_probe.py).
- [Spatial prime reduction and scalar-tail obstruction](../notes/ALL_WINDOW_SPATIAL_PRIME_REDUCTION_20261003.md).

The final probe generator SHA-256 is

    580357e377c032fbb3dc1012d2274771cfe01ab83fb7262bc1f656c4cdd0c907

Both [probe_192.json](../numerics/all_window_mechanism_20261003/probe_192.json) and the separate-agent [probe_256.json](../numerics/all_window_mechanism_20261003/probe_256.json) bind that source. The latter ran in 0.297 seconds using Python 3.10.0, python-flint 0.9.0, and FLINT 3.6.0. The [replay record](../numerics/all_window_mechanism_20261003/probe_replay_check.json) checks all invariant metadata, exact rational polynomial coefficients, scalar overlaps, prime-power counts, and five strictly positive minimum-eigenvalue lower bounds.

## 2. Translated covariance and its sign

For normalized real g of support width ell and autocorrelation phi, the digamma formula gives the off-diagonal archimedean kernel

    -n(|u|),   n(u)=e^(-u/2)/(1-e^(-2u)).

At r>ell the local diagonal term vanishes between the two disjoint translates. Among the two symmetric prime shifts, only the branch with log(n) near r meets the supports. Therefore

    Q(g,tau_r g)=-sum_n Lambda(n)n^(-1/2)phi(log(n)-r)
                -integral phi(u)n(r+u)du.

The coefficient is exactly one copy of each Lambda(n)/sqrt(n), not twice that coefficient. The full diagonal arithmetic form has two branches, which is a different calculation.

Pole neutrality gives integral phi(u)e^(u/2)du=0, and evenness gives the other sign as well. Expanding n(u)=e^(-u/2)+e^(-5u/2)/(1-e^(-2u)) cancels the leading tail. Since ||phi||_1<=||g||_1²<=ell, the stated bound

    |archimedean cross remainder|
       <=ell e^(-5(r-ell)/2)/(1-e^(-2(r-ell)))

is valid. Its sign is not assumed; the certified cross interval correctly uses both signs of the remainder.

The positive-definiteness necessity covers every finite translation Gram matrix and arbitrary complex coefficients. The counterexample distinguishing pairwise conditions from full positivity is correct. For sufficiency of the complete small-probe family, compact preparation and the mean-zero condition supply a compact antiderivative. Convolution with the prepared approximate identity then approximates every original compact source. Translation Riemann sums converge in smooth seminorms on a fixed compact interval; the finite prime sum and logarithmic gamma multiplier make Q continuous there. Thus the stated equivalence is an exact reduction, while its universal Gram positivity remains unproved.

The PNT asymptotic for the absolute smoothed sum has the factor e^(r/2) and the integral weighted by e^(u/2). The signed continuous term is zero. The integration-by-parts discrepancy identity has the factor e^(-r/2), the weight e^(-u/2), and derivative phi'-phi/2 with the signs as stated. Its use identifies the cancellation lost by an absolute majorant. Neither this identity nor the five numerical examples supplies the missing signed bound for every r.

## 3. Exact polynomial preparation and validated diagonal

The code constructs h(x)=(1-16x²)^8 on (-1/4,1/4), then g=-h'''+h'/4. The eighth-order endpoint zero of h gives the required vanishing of h',h'' for integration by parts. Thus both exponential moments vanish exactly. The mean vanishes exactly as the integral of a derivative. The code also checks these endpoint and mean relations over rational arithmetic.

The source g has a fifth-order endpoint zero and its zero extension belongs to the logarithmic form domain. It is not claimed to be globally smooth. Exact moment-preserving smooth approximation can be obtained by mollifying h first and then applying the same preparation/derivative operator; supports may enlarge by an arbitrarily small amount. All conclusions for the polynomial probe are stated in this form closure.

The exact rational autocorrelation construction expands

    integral_{-a}^{a-u} g(x)g(x+u)dx,   a=1/4,

with the binomial theorem, integrates each monomial, and divides by the exact source norm squared. The stored degree is 31. Its value at zero is one, its first derivative at zero is zero, and its value at ell=1/2 is zero. The independently evaluated direct rational norm agrees with the correlation constant. Even continuation is appropriate for this real autocorrelation.

Because ell<log(2), the diagonal prime form vanishes exactly. The gamma diagonal is

    gamma(0)+2 integral_0^ell n(u)(1-phi(u))du
       +2[atanh(e^(-ell/2))+atan(e^(-ell/2))].

The final term follows by substituting z=e^(-u/2) in the tail integral; it includes the correct factor two. At the origin, (1-phi(u))/u is a polynomial, and

    u n(u)=e^(u/2)/[2 * 0F1(3/2;u²/4)].

This matches the implementation. The Acb callback uses only entire polynomial, exponential, and 0F1 operations followed by division. Its possible poles are detected by denominator balls containing zero; no unverified branch analyticity is introduced by ignoring the unused callback flag. The real segment contains no pole. Finite output and an imaginary enclosure containing zero are required before the real enclosure is used. This is validated integration, not floating quadrature.

## 4. Completed replay and exact scope

The 256-bit diagonal enclosure gives

    Q[g]=1.466940031005284598... > 1.46694003.

The sieve limit is 268338 and it produces 23661 prime-power rows. All powers use log(p)/sqrt(p^m), and the support and sign branches are resolved in Arb; unresolved thresholds cause failure. The five lower bounds for the least eigenvalue of each two-source Gram are:

| Separation r | Prime-power terms | Certified lower bound exceeds |
|---:|---:|---:|
| 4 | 16 | 1.07676584 |
| 6 | 75 | 0.87192614 |
| 8 | 390 | 0.81445202 |
| 10 | 2290 | 0.91892772 |
| 12 | 14077 | 0.68954081 |

The diagonal is the same for both translates. The minimum eigenvalue is at least Q[g]-|M_g(r)|-remainder, exactly the quantity evaluated by the generator. The separate replay compares genuine scalar ball enclosures for overlap. Cross endpoints and minimum-eigenvalue lower bounds are bounds rather than enclosures of one precision-independent endpoint; they are checked as such, with overlap of the resulting complete cross intervals and strict positivity at both precisions.

The experiment establishes positivity on five particular two-dimensional spans, with their stated form-domain source. It does not establish positivity on every source supported in the union's containing window, on all translations of this source, or on higher-order Gram matrices. The PNT asymptotic is supplied by the analytic argument, not inferred by fitting these five rows.

## 5. Audit of the spatial reduction

The single-shift norm formula correctly uses ceil(L/a). When L/a is integral, chains of the longer length occur only on a null endpoint set; the stated essential norm remains correct. Positive kernel domination shows that the spectral top of the finite sum W_L equals its operator norm.

The simultaneous-recurrence argument is valid without a Diophantine rate. High modulations recur arbitrarily close to one on all finitely many active prime phases, hence on every active prime-power phase. They converge weakly to zero and therefore avoid any fixed finite-dimensional head. Small exact moment corrections restore the smooth source class. This proves finite-codimension invariance of the spectral top and norm, rather than merely giving a lower bound from a selected numerical family. The modulation raises archimedean energy, so the argument does not produce a negative Weil source.

The two nonnegative packets near opposite support edges produce the correct single cross contribution in the exponential lower bound for ||W_L||. Their continuous PNT main term is strictly positive because these auxiliary packets are unprepared; preparation is supplied later by recurrence and correction. There is no conflict with the neutral-probe cancellation in Sections 2-4 above.

The min-max indexing in the scalar-tail obstruction is correct. For a codimension-N tail in E_L, the best lower scalar gamma floor cannot exceed eigenvalue N+1. The first N+4 Dirichlet modes lose at most three dimensions under the original moments and retain at least N+1 dimensions. Concavity of log and the common Dirichlet derivative-energy bound then give the stated upper bound on that eigenvalue. The two-sided digamma estimate follows from integral comparison of the decreasing series summand and its first-term bound of four. Solving the resulting necessary scalar-floor inequality gives the displayed doubly exponential rank barrier.

The fractional Legendre-tail constant used for b_N matches the existing Weil-depth lemma: adding log(4pi) to the log(|t|/(2pi)) floor and then adding kappa=1-gamma(0) gives H_N-EulerGamma+1+log(4/L). The invoked lemma assumes N>=1; this convention should remain explicit. Restricting to the three-moment space does not invalidate min-max, since the intersection of that space with the Legendre tail has codimension at most N there.

The Schur complement retains the exact E_L-compressed W. Thus

    G_N=P W (I-P) W P=P W² P-(P W P)²

is correct and contains every omitted mode. In any implementation W² must retain the intermediate moment compression; replacing it by the square of an uncompressed shift sum would change the formula. The note explicitly requires the compressed interpretation. Its norm approximation bound is conservative and valid.

Finally, J_L is positive compact, and compression away from three moments is a finite-rank perturbation on the ambient interval space. The centered discrepancy P_E(W_L+J_L)P_E therefore has essential spectral top ||W_L||. This rules out a polynomial-in-L bare L2 upper bound for that discrepancy. It does not exclude a signed comparison tied to archimedean energy on the same directions. The exact null multiplier and the zero-mean null multiplier have the stated constants; their source compression is zero, while their decay cannot remove the nondecaying prime phases in a worst-case high-frequency amplitude estimate.

## 6. Companion effective-relative-tail audit

A separate agent independently checked [Effective relative tails](../notes/ALL_WINDOW_EFFECTIVE_RELATIVE_TAILS_20261003.md), including its time-band count, mixed-column approximation, and shifted-resolvent certificate. This review incorporates that result; the agent did not edit this review file. No substantive error was found in the displayed counting formulas or resolvent formulas.

In particular, Tr(A_R)<=LR/pi and the eigenvalue min-max indexing are consistent. The approximation J_n=EH+HE-EHE has rank at most 2n because its range is contained in Ran(E)+Ran(HE); it retains the mixed columns rather than pretending that EHE alone is sufficient. Its complementary error uses k/b_(n+1), without requiring an unknown lower gap in that remainder.

For the shifted resolvent, order reversal is applied to positive operators, and the scalar convex-chord bound is then applied by functional calculus. No commutation of the chosen source projection with B or A_R is assumed. The raw Legendre plane tail controls distance to the span of exactly moment-projected polynomials because the moment projection is contractive. If the full-column residual norm is r, then Delta=R_tau U-Y has norm at most r/tau; the three selfadjoint correction terms give the stated 3r/tau error. Finally a bound R_tau<=(mu+eta)I implies beta>=1/(mu+eta)-tau, with positivity requiring mu+eta<1/tau. These are genuine sufficient certificate inputs, but the note supplies no computed full residual columns or numerical beta.

The cost discussion appropriately describes the displayed sufficient estimates. It does not claim that their large rank bounds are necessary for every alternative method or that finite relative eigenvalue counts establish H<=I.

## 7. Companion obstruction and completeness audit

Another separate agent independently reviewed [the mechanism obstruction audit](ALL_WINDOW_MECHANISM_OBSTRUCTION_AUDIT_20261003.md). It confirmed the exact centered off-diagonal kernel, the fixed-spacing lattice argument giving negative index at least cL-O(1), and the fixed-window signed-cutoff completeness lemma. In the latter, weak convergence correctly retains the escaped unit norm through the term lambda(1-||u||²); omitting that term would invalidate the argument. The conclusion remains conditional on a strict positive fixed-window gap.

That reviewer also checked the cited primary multiplicity source directly. The conditional RH multiplicity bound and Riemann-von Mangoldt yield a superlinear count of distinct ordinates, so the Fourier-transform/Jensen kernel argument does not silently assume simple zeros. Neither conditional completeness nor local continuation supplies an unconditional nonaccumulation theorem.

## 8. Final logical assessment

No substantive flaw was found in these reviewed mechanisms or the bounded probe replay. Their combination sharpens the research target: fixed finite-dimensional deflation does not lower the arithmetic norm, centering does not create a small L2 remainder, and absolute source-smoothed prime sums grow exponentially even when the signed continuous term cancels. A successful all-window proof must control signed arithmetic and source energy jointly, including growing finite blocks and all mixed terms.

The new probe equivalence gives a concrete arithmetic covariance whose full positive definiteness would suffice. The five positive two-source matrices check that proposed quantity locally in separation and test the implementation. They leave its universal positive definiteness, or an alternative unbounded-window continuation theorem, open.
