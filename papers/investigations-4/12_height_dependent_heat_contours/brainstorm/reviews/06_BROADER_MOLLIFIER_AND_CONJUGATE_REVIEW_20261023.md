# Review of the broader mollifier tests and conjugate moment

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. The all-rank and inverse-square derivations received review from another agent of the same model; the parent also checked the conjugate identities and independently reproduced four complete rank kernels. This is internal LLM review, not specialist or formal verification.

**Assessment:** [Note 15](../notes/15_BROADER_MOLLIFIER_TESTS_AND_CONJUGATE_MOMENT_20261023.md) proves two scoped exclusions. Its conjugate construction is an exact comparison with an unproved arithmetic input. No improved simplicity bound follows. The broad RH-to-simplicity goal remains open.

## 1. Every fixed elementary rank

The explicit baseline residue formulas give a generating polynomial of degree at most five before cancellation. The complete sum reduces to c_theta^(-1)[1/2+1/t+z/t^2+z^2/(2t^4)]. Rank one agrees with the ordinary profile (1-u)Q, and rank two reproduces Note 14 with its unordered-pair factor. The first moment at ranks at least three vanishes because the corrected shift derivative is supported on at most two distinct primes.

The independent direct calculation used homogeneous numerator division for the full kernels of ranks 3–6, instead of the generating-residue extraction. Their baseline residues at zero all vanish exactly. Those finite checks support the algebra; the degree proof, not their count, establishes all ranks.

The second Mellin residue was retained and shown to have an exponential factor that cancels the outer exponential, leaving a rational function with poles only at zero and sufficient decay. The homogeneity bounds also pay the H^1 extension in the ordinary profile. Fixed-rank finite coefficient rings, admissible complex affine envelopes and smoothing order 100+2k extend the earlier analytic localization. No rank or profile is allowed to grow with height.

The conclusion concerns fixed finite combinations with positive limiting second moment, or the limiting residual functional. Null limiting directions, products of marked statistics, arbitrary prime weights and growing families remain outside it.

## 2. Inverse-square normalization and actual moment limits

The exact prime-power calculation retains mu_2(p^2)=1. The mixed arithmetic factor at the origin is one; the square factor is 1/zeta(2). The pole exponent (r-1)(q-1) gives a raw square moment of order log T for mu_2, while its first moment has order one. The positive general D_B formula follows from the complete square kernel by exact factorial ratios; B=100 satisfies the analytic smoothing requirements.

The first-moment prime and prime-pair terms give Q(1)/2+2theta integral Q+theta^2 integral(1-u)Q. Repeated-prime terms are lower order. A minor admissibility clarification was incorporated: for a general Q(0)=0 in this first-moment assertion, use the envelope mu_2 u and write Q=uR; the degree-100 envelope applies to the second-moment extraction.

The fifteen-factor global envelope, degree-100 Mellin decay and local integrable expansion yield the claimed bounded high-smoothing raw mixed moments and square asymptotic L D_100/zeta(2)+O(1). The normalized v_T=w_mu2/sqrt(L) has bounded positive norm. Cauchy–Schwarz and H^1 approximation then prove its actual cross with P_0 tends to zero.

**The raw low-degree cross is not thereby proved.** Using the unnormalized candidate in the same density argument would introduce sqrt(L). The note correctly leaves that raw order-one formula at formal-kernel status and makes no O(1/L) gain-rate claim for P_0.

The normalized two-dimensional limiting Gram is diag(b,D_100/zeta(2)), strictly positive. Inverse-matrix convergence therefore proves the optimized quotient tends to F_theta uniformly over all projective coefficients, including height-dependent coefficients. Rescaling the second vector preserves the span at every height. Unlike the general elementary-rank family, this concrete two-dimensional test has no limiting-nullspace gap.

## 3. Conjugate direction and literature boundary

The correct dual is -chi(s)^(-1)B(1-s), not -chi(s)B(1-s). It produces overline(w_0) at zeros under RH, including repeated zeros without division by zeta'. Its cross with w_0 requires H_T=E_T w_0^2, not the Hermitian moment E_T|w_0|^2.

Rotation of the finite-T mean makes the real-part Cauchy certificate exact and no worse than the original. The centered-moment disk |H-a^2|<=b-a^2 and the two-dimensional Gram inverse yield the displayed strict-gain formulas. They also show that existing moments permit both asymptotic reality H=b and strict improvement. Neither possibility is established by the current inputs.

The contour reduction produces a chi-squared transform and square-root stationary phases. No aggregate error estimate for that transform is supplied. Hughes–Pearce-Crump labels the simpler unmollified holomorphic square conjectural; the newer chi-weighted Landau theorem does not directly supply the derivative-weighted mollified moment. The note preserves these distinctions rather than converting a conjectural source or unsummed error into an RH-only theorem.

## 4. Records and decision

The portable symbolic checks and small JSON records are linked from Note 15; they contain exact algebra and explicitly exclude arithmetic convergence from their scope. Four newly relevant primary articles have versioned catalog entries and external PDF/hash receipts. The Conrey et al. paper is only an introductory strategy lead, not an imported theorem.

The new information is a larger precisely stated exclusion and a normalized nonsquarefree test. The next missing input for conjugation is actual phase-sensitive arithmetic: a bound on the holomorphic square or a positive limiting imaginary energy. No new percentage, individual collision exclusion, manuscript revision, or universal short-mollifier ceiling is claimed. See the [result index](../../../../../result-summaries/README.md), [avoid index](../../../../../avoid/README.md), [scope discipline](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md).
