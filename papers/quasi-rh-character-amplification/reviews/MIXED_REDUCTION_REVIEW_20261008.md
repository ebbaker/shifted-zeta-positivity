# Scoped review of the mixed-kernel and primitive-row-conductor reductions

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning effort are not exposed and are not inferred.

Reviewed: [Mixed-witness kernel](../notes/MIXED_KERNEL_CONDUCTOR_REDUCTION_20261008.md), [Primitive-conductor localization](../notes/SATURATED_MIXED_ARITHMETIC_20261008.md), and the accompanying [exact local checker](../numerics/check_mixed_kernel.py). Source comparisons use the September 30 companion PDF, SHA-256 `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`, especially §§8.1–8.2, Lemma 17.1, and §19.2. This review is independent of the derivations in those two notes. It checks their displayed reductions, not the deep proofs of the external source.

**Verdict: the stated conditional reductions pass this scoped review.** They do not establish the remaining large-conductor signed correlation or the new mixed moment. No increase in the investigation's conditional zero-free boundary follows yet.

## 1. Exact ratio character and retained zeros

For each prime outside the fixed excluded set, reducing the difference of the two column valuations modulo six gives the correct local sextic character. A zero residue removes the local phase but leaves its zero on nonunits whenever either original column contains the prime. Thus the displayed E-mask is necessary and sufficient. In particular, the example p^6 versus the unit ideal correctly leaves a puncture at p.

The moving conductor is the radical f of the nonzero valuation residues, not the norm of the sixth-power-free representative with those residues as exponents. Every nonzero power of the source's local sextic character is nonprincipal and primitive at its good prime; the finite fixed ray factors cannot cancel its ramification there. The additional E-primes are zeros, not additional ramified conductor primes. The row sum remains over the original physical element rows with their unit factors.

These identities agree with the local conventions used in the external paper's §8.1 and §17.5. They do not require replacing the denominator symbol by an incompletely masked reciprocal symbol.

## 2. Pair count and small-conductor norm bound

The estimate

    # {(n,n'): Nn,Nn' <= C X, Nf(n,n') <= V}
        << X V^(1/2+epsilon)

is justified by the note's argument. After n=gA, n'=gB with coprime A,B, the unique sixth-power decompositions leave coprime sixth-power-free a_0,b_0. Each prime in f has precisely ten possibilities: two sides and one of five nonzero exponents. Counting g by X/max(NA,NB), bounding max from below by the geometric mean, and summing the two ideal sixth-power factors produces convergent sums with exponent 3. The remaining f-sum is bounded using 10^omega(f)<<Nf^epsilon and ideal counting.

No lower annular bound is required for this upper estimate, so replacing the actual annular supports by upper norm bounds is legitimate. If a prospective g-scale is below one, its count is zero, and the displayed positive majorant remains valid. The actual smooth and divisor-bounded tuple coefficients therefore give the absolute block bound

    X^(-1) sum_{Nf<=V} |coefficient * K_C| 
       << (#C) V^(1/2+epsilon) X^epsilon.

The same conclusion holds after deleting k=k' tuple pairs. Although the remaining composite-column coefficient need not factor as b(n) conjugate(b(n')), its absolute tuple sum is bounded by the same fixed divisor-function majorant. This correctly avoids applying an arbitrary-coefficient moment theorem.

## 3. Plain-variable diagonal and the decomposition order

The complete k=k' block is positive after summing the inverse/prime factors:

    N^(-1) sum_k |B(Nk/N)|^2
       sum_{u in C} |M_r(u)Q_I(u)|^2 1_{(u,k)=1},

with any additional fixed character zeros retained. Dropping the displayed mask at this stage is valid by positivity. The plain coefficient square mass is O(1), and the source's original marked inverse moment then gives O(U^(1+epsilon)), with its strict capacity and height hypotheses unchanged.

The proposed ordering exhausts the full moment without double counting:

1. Remove the low primitive-row-conductor set using a positive moment bound.
2. On the remaining rows, remove all k=k' tuples as the positive plain-variable diagonal.
3. Among k!=k' tuples, bound the Nf<=U^(4/5) block absolutely.
4. Retain the signed k!=k', Nf>U^(4/5) block.

The last block is not asserted to be positive. An upper bound for its real part suffices, because the complete moment is real and the removed absolute errors are already controlled. Bounding the absolute value of that entire summed block is stronger but also sufficient. Taking absolute values separately for every retained pair would ask for a substantially stronger estimate and is not justified by these reductions.

## 4. Use of the old profile-bin count and exact margins

The scalar count R* is available for the full fixed buffered zero/profile bin. Proposition 19.2 may choose detector witnesses separately to prove that count; it does not require the current prescribed r,m pair to be large on every counted row. Consequently applying the old count to C, or to a subset selected by primitive row conductor, is noncircular.

The inherited fixed choice kappa=3/4, justified conditionally by beta_*<=7/8 in the existing investigation, is important here. The September 30 source originally records a Delta/4 allowance for its dynamic-kappa comparison. That allowance is absent in this investigation's already-established fixed-kappa scalar formula; the present notes use that formula and should continue to cite the existing localized/geometry derivation rather than silently importing the dynamic statement verbatim.

Using t_0-1<3/20 yields

    R* <= 9/8 - 23 delta/20.

At V=U^(4/5), the removed block exponent is R*+2/5. Its minimum surplus below 1+delta*m-1/5000 is exactly

    (9/25)(9/25+23/20) - 21/40 - 1/5000
      = 23/1250.

The weaker check with only #C<<U and V=U^(1/4) gives 11/2500. Both fractions are correct. Arbitrarily small divisor, profile and Sobolev losses can be reserved below these fixed positive margins in the previously prescribed parameter order; height factors must still be retained until that order absorbs them.

## 5. Primitive row-conductor localization

The row-conductor parameter theta=log Q_psi/log U is different from the column-pair conductor f. The distinction is maintained correctly.

Before replacing Q_psi by O(U), the primitive functional equation in the proof of source Lemma 8.1 contributes Q_psi^(a-1/2+6e). The other primitive L-value has the buffered U^epsilon bound. On the current hard box the reflected real part is bounded away from zero, so the deleted Euler product, whose radical has polynomial size in U, costs only U^epsilon after allocating the preliminary losses. Repeating the source's finite-height Mellin shift yields

    |S_m(psi)|^2 << U^[delta(theta-m)+epsilon](1+T_1)^A.

The central contour and tail orders remain those permitted by Lemma 8.2; a sufficiently large fixed tail order also handles a negative displayed exponent. Combining this with its direct bound gives the stated minimum of m and theta-m.

On theta<=2m-1/1000, the squared plain factor therefore gains at least

    delta/1000 >= 9/25000
                  = 1/5000 + 1/6250.

After this pointwise estimate, positivity permits enlarging the remaining marked inverse norm to the full original row family. This proves the stated partial mixed saving without applying a moment at the smaller, unjustified row scale U^theta. The source detector's actual plain spike then forces theta>=2m up to the explicit controllable losses; the note correctly does not impose that spike on every row of the larger moment class C.

## 6. Restricted kernels cannot be replaced termwise by complete Poisson kernels

The class C, and its retained high-conductor subset, depends on zero bins and prime amplitudes. Its indicator is not the smooth complete-row weight required by source Lemma 17.5. The identity for K_C is exact, but a complete-row Poisson formula is not an identity for that restricted kernel.

Positivity allows enlargement of the whole mixed norm. It does not allow termwise enlargement of a signed column-pair block, and it does not preserve a favorable restricted kernel through an unexplained complete-row replacement. Both reviewed notes state this limitation and keep the row-selection issue inside the unresolved arithmetic estimate. The earlier marked-transfer audit describes a separate sufficient route through a complete smooth family; that route must not be conflated with the restricted decomposition reviewed here.

## 7. Reproducibility and scope

The checker was rerun successfully using exact integers and rational fractions. It reproduced 6,561 valuation-pair checks, including 225 sixth-power-equivalent pairs and 2,072 pairs with a nontrivial retained mask. The output margins are 11/2500 and 23/1250. The local phase identities, masks and reconstruction checks are valid finite tests; the infinite pair-count estimate is established by the analytic argument in Section 3 of the kernel note, not by that finite enumeration.

The review does not prove the remaining signed large-conductor block, the source's moment theorems, or any stronger zero-free boundary. The new verified outcome is a narrower statement of the missing arithmetic input, with two distinct conductor restrictions and a positive removal of the complete plain-variable diagonal.

## 8. Combined synthesis and extended checker

The subsequent [combined synthesis](../notes/MIXED_MOMENT_REDUCTION_20261008.md) was also checked, in particular its equation (13). At fixed separating parameters, partitioning the row set into the low- and high-primitive-conductor pieces is an exact positive decomposition. On the high-conductor piece, the tuple split into k=k', k!=k' with small ratio conductor, and k!=k' with large ratio conductor is disjoint and exhaustive. The absolute estimate for the middle piece remains valid after imposing the unequal-plain-ideal restriction.

The three discarded contributions have margins at least 1/6250, 647/5000 and 23/1250 below K=1+delta*m-1/5000. Their common minimum is 1/6250. Therefore the synthesis correctly obtains

    sum_C |M_r S_m Q_I|^2
       = Re(T_large) + O(U^(K-1/6250+epsilon)(1+T_1)^A),

where the implicit height order is increased, if necessary, to cover all three bounds. The cutoff regions are invariant under exchanging the two tuples. Their complete pair sums are thus real, and taking a real part is legitimate. The error is signed only because the small ratio-conductor block need not be positive; its absolute control supplies the stated equality with an O-term.

The quantifiers are adequate: fixed parameter identities first, arbitrary small subsidiary losses in the inherited order, and a uniform estimate for all source-permitted derivative profiles before applying Sobolev to rowwise choices. The identity does not insert separately selected row heights into a single coefficient array. The primitive row-conductor and ratio-character conductor restrictions remain separate.

The extended checker was rerun successfully. Its new exact outputs are row-conductor margin 1/6250, plain-diagonal margin 647/5000, combined margin 1/6250, and formal zero-decrement width intervals [-1/2,-9/25] and [-3/5,-6/25]. The width extrema follow from affine functions on the stated rectangle, so checking their rational corners covers these extrema exactly. The revised program writes its result to standard output without modifying the saved record; the record should be regenerated from that output when installing the files.
