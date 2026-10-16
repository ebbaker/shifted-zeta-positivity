# Marked mixed transfer: a safe principal term and the actual nonzero-frequency obstruction

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning effort are not exposed and are not inferred.

Status: exact coefficient and support calculations, an elementary bound for the principal character-pair contribution, and an audit of one proposed use of the external marked inverse machinery. No new off-diagonal saving or zero-free boundary is proved. Deep statements in the external paper are imported conditionally, not independently validated here.

Source: the [September 30 companion paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf), especially Lemmas 17.1, 17.2 and 17.5, equations (17.67)–(17.85), and §18.7, equations (18.41)–(18.50). The consulted PDF has SHA-256 `8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`. This continues [Joint inverse/plain witnesses](../notes/JOINT_WITNESS_REDUCTION_20261008.md).

## 1. Target and normalization

Let the original row width be one and write

    D = U^r, N = U^m, P_i = U^{z_i}, z = sum_i z_i,
    T = D N product_i P_i = U^L, L = r+m+z.

The relevant rectangle is

    9/25 <= delta <= 21/50, 49/100 <= x <= 1/2,
    7/10 <= r <= 37/50, 9/25 <= m <= 1/2,
    z = (1-r)/2 - nu,

where nu>0 is a fixed small capacity decrement, followed by whole-slot rounding. A sufficient new input would be

    sum_{u in C} |M_r(u) S_m(u) Q_I(u)|^2
       << U^{1+delta*m-1/5000+epsilon} (1+height)^A.

Here C is the prescribed nearly saturated buffered zero bin, not the subset defined by the witness lower bounds. All the original character zeros, prime labels, common height, and smooth tests must be retained. The following calculation applies for each fixed permitted set of tests and heights. The source's uniform Sobolev treatment would still be needed to accommodate rowwise witness selection.

Absorb bounded real norm powers and imaginary powers into the annular tests. With the same fixed zero-extended character nu_0 in all factors, the mixed polynomial is exactly

    P_u = T^(-1/2) sum_v b(v) nu_0(v) chi_v(u),

    b(v) = sum_{d k p_1...p_j=v}
             mu(d) A(Nd/D) B(Nk/N)
             product_i a_i(p_i) W_i(Np_i/P_i).

The chosen orientation may be conjugated throughout without changing the argument. The sums retain the actual disjoint physical prime lists and every original support condition. In particular, this is not a replacement by arbitrary coefficients. Nevertheless the elementary bound

    |b(v)| << d_O(v)^(j+1) << U^epsilon

holds on Nv asymptotic to T, with the permitted test-seminorm and height costs. The first inequality merely counts factorizations of the actual coefficient.

## 2. The principal character-pair contribution is already small enough

Choose a fixed nonnegative radial Schwartz majorant Phi(Nu/U) for the original row ball. Positivity gives E_C <= E_Phi, where

    E_Phi = T^(-1) sum_{v_1,v_2}
              b(v_1) conjugate(b(v_2)) nu_0(v_1) conjugate(nu_0(v_2))
              sum_u Phi(Nu/U) chi_{v_1}(u) conjugate(chi_{v_2}(u)).

Call a column pair principal when its row character is principal after retaining its zero mask. Outside the fixed excluded primes, the local sextic exponents of v_1 and v_2 must then agree modulo six. Consequently write uniquely

    v_1 = a b_1^6, v_2 = a b_2^6,

with a sixth-power-free. Fixed ray conventions can restrict this set further; enlarging to all such ideal pairs is harmless. Ideal counting gives

    # {(v_1,v_2) principal: Nv_i asymptotic to T}
      << sum_{Na <= C T} (T/Na)^(1/3)
      << T.

Indeed each b_i has norm bounded by a constant times (T/Na)^(1/6), and partial summation with the ideal-count bound O(X) gives the last inequality. The original masks can only decrease the absolute row sum. Thus, retaining all nonsquarefree columns,

    |E_principal| << T^(-1) U T U^epsilon = U^{1+epsilon}.

This is a new elementary reduction, not an invocation of the restricted canonical estimate. It needs only the source's exact local sextic character convention and ideal counting. The zero row, if introduced by the smooth majorant, uses the original zero-extension convention; equivalently keep 0<Nu throughout and subtract that row before applying Poisson. For T tending to infinity all supported columns have a prime divisor, so their zero extension at u=0 vanishes.

The desired exponent exceeds 1 by at least

    (9/25)^2 - 1/5000 = 647/5000 = 0.1294.

Therefore the raw principal column pairs have ample room in the entire requested rectangle. Improving their estimate cannot close the actual gap: the missing arithmetic input concerns the nonprincipal pair sum. This assertion is about principal *column pairs in the first expansion*, not about the transformed exceptional rows of §18.7; those are different objects.

## 3. Exact signed nonprincipal term

For each nonprincipal column pair let psi_{v_1,v_2} be its primitive row character and let R_{v_1,v_2} retain the remaining zero primes of the displayed pair. Let f_{v_1,v_2} be the primitive conductor. A fixed ray expansion, if required by the presentation, is finite and is kept term by term. Lemma 17.5 gives the exact contribution

    E_nonprincipal = U/T sum_{v_1,v_2 nonprincipal}
      b(v_1) conjugate(b(v_2)) nu_0(v_1) conjugate(nu_0(v_2))
      gamma(psi;f)/sqrt(Nf)
      sum_{a | rad R} mu(a) psi(a)/(Na)
      sum_{h != 0} conjugate(psi(h))
          F Phi( U Nh / (Na Nf) ).

Every character in this formula has its full zero extension. There is no zero-frequency term for a primitive nonprincipal character. The smooth kernel is kept whole; a conductor-dependent sharp cutoff must not be inserted into the coefficient. This is the signed off-diagonal expression before applying absolute values to column pairs, Gauss sums, divisors, or frequencies.

A bound

    |E_nonprincipal| << U^{1+delta*m-1/5000+epsilon}

for the enlarged smooth family would suffice for the desired restricted estimate, by Section 2. It is a potentially stronger task because the enlargement has discarded the buffered-bin and near-saturation information. Conversely, simply inserting 1_C(u) into the Poisson formula is invalid: the source's Schwartz profile estimates do not cover that arithmetic row selector. A proof exploiting the bin must retain it through an independently justified weighted transform or return to the signed restricted kernel before this enlargement.

## 4. Where the existing initialization fails, with actual coefficients retained

A particularly transparent part of the original sum is the core where d, k and all physical primes are squarefree and pairwise coprime. The total column v is then squarefree and

    b_core(v) = mu(v) h(v),

    h(v) = sum_{k P | v}
             mu(k) mu(P) A( Nv/(Nk NP D) ) B(Nk/N)
             product_i a_i(p_i) W_i(Np_i/P_i),
    P = product_i p_i.

All divisors here are constrained by the original supports. Squarefreeness supplies the coprimality of k, P and v/(kP). The factor h is an annular divisor sum with a free plain ideal k. It is not the product of a fixed number of individual prime-slot coefficients.

Apply only the algebraic and Poisson steps of §17.6 to this core. In the simplest overlap-free sector, its effective squarefree column length is

    D'_mixed = r+m+z,

rather than D'_inverse=r+z. The source's identity (17.69) for the first dual-row center becomes, at original row width one,

    M_init,c = 2(r+m+z) - 1 - 2 P_1.

Appending S therefore adds **2m** to that dual width. At zero conductor-gcd reduction P_1=0 and zero decrement,

    M_init,c = r+2m,

which ranges from 1.42 to 1.74 on the requested rectangle. The original inverse-only dual center is r, ranging from 0.70 to 0.74. These widths come from the genuine conductor support; the common norm-twist height does not shorten it.

More importantly, after the source substitutions

    C=t a, f=a s, v=C s n=t f n,

the extra coefficient in the putative child of equation (17.77) is exactly

    h(t f n).

For fixed t it still depends on the canonical averaged label f and on the residual column n. Decomposing the plain divisor k into its part dividing tf and its part dividing n does not remove this problem: the latter part remains a free annular ideal divisor with its original Mobius sign and the coupled plain-scale restriction. This is the precise residual coefficient that an extended induction would have to propagate.

Lemma 17.2, pages 115–116, explicitly excludes any residual b(n), even row- and label-independent residual coefficients; h(tfn) is outside that class twice over. A scalar bound h<<U^epsilon is useful for crude counting but cannot be substituted into the signed recursive estimate while retaining its cancellation. The exact coefficient closure in (17.72), (17.77), and (17.83) is where citing that lemma would fail.

## 5. Quantified failure of the formal width transfer

Even if one temporarily ignores the forbidden residual coefficient, the source's canonical admissibility identities (17.85), with no inverse/physical-prime overlap, would require positive versions of

    c_1,mixed = 1-r-m-2z,
    c_2,mixed = 3-2r-2m-8z.

At z=(1-r)/2-nu these become

    c_1,mixed = 2nu-m,
    c_2,mixed = 2r-1-2m+8nu.

At zero decrement the first lies in [-1/2,-9/25], and the second lies in [-3/5,-6/25]. The actual bottleneck values are approximately -0.40839 and -0.38680, respectively. These are fixed macroscopic deficits, not epsilon losses or a missed strict endpoint. Repairing the first by dropping physical primes would require z<(1-r-m)/2; that upper bound is negative throughout the requested rectangle because r+m>=1.06. Hence even removing every prime slot does not make this naive transfer admissible.

The strict capacity decrement used by the row-count argument is much smaller than these deficits. Choosing nu large enough to make the first expression positive would demand nu>m/2>=0.18, whereas all available inverse-capacity prime length is at most 0.15. Thus this repair is impossible within the stated geometry.

Alternatively, pretending the plain ideal is one more prime-like mark of length m would replace the first marked condition by r+2(z+m)<1, whose zero-decrement excess is 2m, ranging from 0.72 to 1. It would also violate the required prime coefficient class. That bookkeeping is still less favorable.

These calculations diagnose failure of this proof transfer. They are not lower bounds on the actual mixed moment and do not show that the requested saving is false.

## 6. What the centered exceptional-row trick does and does not transfer

Section 18.7 treats transformed rows whose inducing characters lie in the fixed finite family Theta. Its exact exceptional deficit is

    A - 5M/6 - F_1 - F_2                         (18.42),

and the centered rectangle gains (L-v)_+ before absolute values, leading to

    A - 5M/6 - 2v/3 - (L-v)_+ <= (A-M)_+       (18.50).

The key input is not merely two factors with a common character. Lemma 18.3 applies to two **plain** ideal sums. Their common masked lattice main terms have the form c X^{1+it} I_i(t), so equal products of scales cancel the same product main term exactly, for the same mask and norm power.

One inverse factor does not have that lattice coefficient. Multiplying its summand by mu changes the arithmetic sum itself, so (18.45) cannot be applied to it. In a formal Mellin residue calculation for a principal inducing character, a zero rho contributing to an inverse sum would produce a normalized mixed term proportional to

    (X Y)^(1/2) X^(rho-1),

rather than a function only of XY. At a fixed product XY, changing X generally changes this term. This last display is an explanatory residue calculation, not an assertion that such a residue dominates uniformly or that zeros are simple. It identifies why an equal-product subtraction supplies no automatic counterpart of (18.47). A centered mixed theorem would need a new coefficient identity or a new bound for the surviving inverse-mode terms.

Freezing the entire plain ideal before invoking the inverse moment is also quantitatively inadequate. Triangle inequality and absolute counting give an L2 norm cost U^{m/2}, hence an energy bound U^{1+m+epsilon}. The existing buffered-bin pointwise bound already improves this to U^{1+delta*m+epsilon}; the freeze-first route is worse by (1-delta)m>=261/1250=0.2088 in the exponent.

## 7. Result of this audit and the next precise calculation

The new reduction is that the complete raw principal character-pair sum is O(U^{1+epsilon}), with a fixed 0.1294 margin relative to the target throughout the rectangle. Thus a first arithmetic proof can focus entirely on the signed nonzero-frequency expression in Section 3.

The existing marked inverse initialization neither closes on the actual residual h(tfn) nor has enough width after appending the plain factor. The exact deficits in Section 5 rule out repairing this by a small adjustment of the prime capacity or by invoking the old lemma with an enlarged coefficient constant. The source's centered plain-product cancellation does not apply unchanged either.

A useful next theorem would control the signed transformed h(tfn) family on its **genuine** support, using the annular Mobius divisor and buffered-bin correlation before positive enlargement. The present calculation does not prove such a theorem. It prevents two invalid shortcuts and isolates an off-diagonal term whose saving, if established with the original uniformity, would provide the requested mixed input.

See the [combined mixed-moment reduction](../notes/MIXED_MOMENT_REDUCTION_20261008.md)
for the complete decomposition and current remaining signed estimate.
