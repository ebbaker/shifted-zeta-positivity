# Review of the discrete Feng moment calculation

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. The source/import audit, analytic extraction, and algebra/optimization audit were assigned to separate same-model agents and reconciled by the parent. This is internal mathematical review, not specialist review or formal verification.

**Assessment:** [Note 14](../notes/14_DISCRETE_FENG_MOMENT_REDUCTION_20261023.md) establishes the stated first moment and, in its high-smoothing class, the mixed-moment identity and finite limiting square moments. The exact algebra was reproduced by two different coefficient-extraction methods. The conclusion is a scoped absence of leading-order gain, not an improved simplicity theorem. SIMP-01 remains open.

## 1. Imports and coefficient hypotheses

Benli–Elma–Ng, arXiv:2311.13554v1, Theorem 1.1 and equations (9)–(11), is the first-moment import. Its correction remark prevents using the older Ng main term or large-sieve error unchanged. Ng is retained in the reference collection as historical correction provenance.

Heap–Li–Zhao, arXiv:2003.09368v1, Theorem 2 and equations (5)–(9), is explicitly unconditional. The paper's separate negative-moment theorem assumes simplicity; that theorem is not imported. RH is used to turn the differentiated shifted moment into the Hermitian inner product over zero labels counted with multiplicity. Shift differentiation is justified by uniform errors and Cauchy's formula.

The isolated two-prime Feng coefficient is **not** submultiplicative. The note repairs this by taking exact finite differences of small fixed affine perturbations of an admissible ordinary envelope. The coefficient modulus remains comparable to mu(n)^2 u_n or mu(n)^2 u_n^100. The inequality u_mn<=u_m u_n gives a uniform submultiplicative constant. Complex perturbations, including the imaginary polarization directions, are essential for the full complex cross moment. These finite differences recover finite-T shifted formulas; they do not by themselves establish their limiting asymptotics.

The unordered coefficient e_2(n) is restricted to squarefree support. Neither a p=q term nor an unrestricted Dirichlet convolution is silently substituted. Pratt–Robles–Zaharescu–Zeindler supplies prior-art context for this coefficient family, not the present discrete moment evaluation.

## 2. First moment

The corrected first-moment formula leaves only squarefree k=pq after shift differentiation: b(1) and prime-power terms vanish, and the k with at least three prime factors vanish to higher order. The signs and the factor pq/phi(pq) give the positive prime-pair sum in Note 14 (4).

The PNT limiting prime measure has density v dv. The unordered pair contributes a factor 1/2, the simplex convolution contributes (1-u)^3/6, and normalization by N(T)L gives

\[
 a_Q=\frac{\theta^2}{12}\int_0^1(1-u)^3Q(u)\,du.
\]

This applies to every fixed polynomial Q(0)=0. In particular Q=u gives theta^2/240. The diagonal prime contribution is negligible, and the unnormalized first-moment statement is unconditional.

## 3. Complete mixed and square kernels

The local squarefree Euler calculation retains the absent, common-divisor, first-only and second-only prime choices. All three I branches, the conjugate orientation, and both J branches are used. Swapping the two mollifiers swaps the marker side. Using a right marker again in the swapped orientation would give the wrong cross kernel.

The common-prime term in the two-sided marked square is of leading size: H_u H_v/(s+t)^2 and 1/[2(s+t)^4] must accompany H_u^2 H_v^2/4. The note retains them. A finite square limit is proved without needing a closed positive formula for every profile.

Two independent exact methods agree on the unmarked, left-marked and right-marked I kernels and the unmarked and right-marked J kernels:

1. Expand in a common shift scale and use exact mixed finite differences of the resulting homogeneous cubic/quadratic polynomial.
2. Expand homogeneous numerators, divide exactly by the apparent shift-pole factors, and extract the abc or ab coefficient directly.

The second method is preserved in the [standalone symbolic check](../numerics/14_discrete_feng_kernel_check.py), with its [execution record](../numerics/14_discrete_feng_kernel_check_20261023.json). The check also verifies the unmarked baseline, the compact partial fractions, and the exact residues. It is algebraic verification, not a numerical zeta-zero experiment or a proof of the analytic errors.

The residue identity leaves a main t^-4 term and exp(-theta t) times a rational remainder. The latter integrates to zero after cancellation of the outer exponential: its poles are at zero and it decays at least as t^-2. This proves the formal cross identity for all polynomial Q(0)=0, beyond the finitely many monomial checks.

## 4. Analytic limits and ordinary-profile extension

Appendix A gives an explicit sufficient class Q=u^100 R. The exponent 100 is deliberately conservative. Its finite coefficient-ring Euler factorization controls the marked factors uniformly even when an unmarked small-prime factor could vanish; taking its logarithm globally would not be justified.

Both local zeta quotients have equal numerator and denominator pole counts, so their rational limits are F and G with no extra factor of L. The global O(L^10) envelope and Mellin cutoff L^(1/4) give tails O(L^-15). The local expansion integrates with error O(1/L). Separated Cauchy circles avoid the individual shift-pole hyperplanes, whose poles cancel in the complete branch sum. The normalization includes the time derivative or explicit logarithm and the two zeta shift derivatives.

The baseline P_0 is extended from the smoothed ordinary class through H^1 approximation. The ordinary quadratic form is continuous in that norm, the Feng square limit is finite, and Cauchy–Schwarz controls the actual cross difference. The displayed mixed kernel also defines a continuous functional of the ordinary profile; its inversions use endpoint values, integrals/convolutions, and at most second derivatives of the fixed smoothed Q. Thus the formal baseline evaluation equals the actual limiting cross moment.

This argument does **not** extend the marked profile Q down to u. For that low-smoothing profile, the first moment is proved but the second-moment passage remains open in this note.

## 5. Optimization scope and strategic consequence

For the proved class,

\[
 b_{0Q}=\frac{\theta(1+\theta)^3}{72}
           \int_0^1(1-u)^3Q(u)\,du,
 \qquad a_Q-c_\theta b_{0Q}=0,
 \quad c_\theta=\frac{6\theta}{(1+\theta)^3}.
\]

The ordinary quadratic form gives the same normal equation for ordinary profile variations. Consequently the baseline minimizes the limiting residual norm over every fixed finite span of these directions. Each fixed combination with **positive limiting second moment** has leading Cauchy quotient at most 1-(1+theta)^(-3). This is a global assertion in that finite span, not merely a zero derivative in a single direction.

A limiting null direction has first and second moments both zero. Its leading quotient is 0/0, so lower-order effects and height-dependent rescaling are not excluded. Neither positive semidefiniteness nor the residual identity removes this issue. Growing families, varying profiles and simultaneous theta(T)->1/2 also lie outside the result. The 19/27 endpoint is the usual iterated limit.

Čech–Matomäki, arXiv:2501.12526v3, supplies closely matched prior art for the general projection criterion and the nullspace caution. Its arithmetic applications do not supply this zeta/Feng identity. Conrey–Ghosh–Gonek's historical optimization is for prescribed ordinary mu P coefficients and used a historical GLH premise; it is not a proof of optimality for enriched arithmetic coefficients. No novelty or exhaustive priority claim is made for the present calculation.

The strongest next question from this round is whether the normal equation has a larger arithmetic domain of validity, or whether a concrete different coefficient structure has nonzero residual correlation. The first/cross-moment test should precede any expensive coefficient optimization. Extending the present two-prime result to less smoothing would strengthen its scope, but the formal identity already indicates that this extension alone would not produce a leading gain. No claim about all mollifiers, all arithmetic observables, or every-zero simplicity follows.

## 6. Research records

This is a source-specific arithmetic calculation, not an RH-equivalent criterion or a generic shape argument. Multiple-zero labels remain compatible with the residual norm; no individual collision has been excluded. See the repository [result index](../../../../../result-summaries/README.md), [avoid index](../../../../../avoid/README.md), [collision controls](../../../../../result-summaries/12_collision_controls_and_screening.md), and [scope discipline](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

All five newly encountered papers from this round have version/source-specific records, archived public PDFs, byte sizes and SHA-256 receipts in the [reference collection](../../references/README.md). Retrieval and passage checking do not certify their full proofs. The note and this review remain exploratory research; the manuscripts and earlier mathematical statuses are unchanged.
