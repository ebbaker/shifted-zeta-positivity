# Mixed-witness kernel: small conductors are already harmless

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); the exact serving variant and configured reasoning effort
are not exposed and are not inferred.

**Status.** This note proves an exact kernel identity and an elementary
coefficient-pair bound. With the already imported scalar exceptional-row count,
these remove the complete plain-variable diagonal and all remaining
ratio-character conductor blocks of norm at most `U^(4/5)` from the proposed mixed-moment estimate, with a fixed exponent margin. The
remaining large-conductor off-diagonal estimate is open. This does not prove
the new mixed moment or raise the current conditional boundary.

The source is the [September 30 companion paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf),
Sections 4, 8, 17.1 and 19. Its consulted PDF has SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The notation and target are from the [joint-witness reduction](JOINT_WITNESS_REDUCTION_20261008.md)
and [localized target](LOCALIZED_JOINT_WITNESS_TARGET_20261008.md).
The external detector and marginal moment theorems remain imported assumptions.

## 1. Actual coefficients, before any enlargement

Fix the witness presentation, all continuous profile parameters, and the
selected whole physical prime slots. The common character is

    psi_u(n) = nu(n) chi_n(u)^epsilon,  epsilon in {+1,-1},

where nu belongs to the fixed finite ray family. Every original zero extension
is retained. Write D=U^r, N=U^m, P_i=U^{w_i}, z=sum_i w_i, and
X=DN product_i P_i. After the source's fixed finite ray decomposition, one
summand of the actual product is exactly

    F(u) = M_r(u) S_m(u) Q_I(u)
         = X^(-1/2) sum_n b(n) nu(n) chi_n(u)^epsilon,

    b(n) = sum_{d k product_i p_i=n}
             mu_K(d) A(Nd/D) B(Nk/N)
             product_i [a_i(p_i) W_i(Np_i/P_i)].                 (1)

Here Nn is ideal norm, the p_i belong to the original disjoint prime supports,
|a_i|<=1, and A,B,W_i include their actual annular norm powers and heights.
In particular A retains the truncated-inverse factor V_<=. Their fixed compact
supports imply cX<=Nn<=CX with fixed c,C>0. The source's common witness height
is in A and B; the separate physical heights stay in the W_i. Equation (1)
does not replace them by freely chosen or row-dependent coefficients.

There are at most a fixed divisor-function number of factorizations in (1).
For every epsilon_0>0,

    |b(n)| <= C_(epsilon_0) (Nn)^(epsilon_0),
    sum_n X^(-1)|b(n)|^2 <= C_(epsilon_0) X^(epsilon_0).         (2)

The constants depend on the fixed number of slots, supports and smooth
seminorms. The bound is unaffected by additional fixed coefficient masks.
A fixed finite sum of presentations is handled by the source's finite-sum
Cauchy inequality before this calculation. No arbitrary-coefficient moment
theorem is being invoked.

For rowwise witness parameters, first use the source's Sobolev argument on
the entire positive norm. Every resulting integral has one fixed parameter
choice in (1); derivatives insert permitted logarithmic profile weights.
The bounds below are uniform for these derivative profiles and incur the
usual fixed polynomial height cost. Expanding with a different coefficient
array for every row would not give the kernel below.

## 2. Exact ratio character and the mask that survives it

For two column ideals n,n', put

    e_p = (v_p(n)-v_p(n')) mod 6, chosen in {0,1,2,3,4,5},
    c(n,n') = product_{e_p != 0} p^(e_p),
    f(n,n') = rad(c(n,n')),
    E(n,n') = product_{p|nn', e_p=0} p.                        (3)

These are pairwise unambiguous ideals, represented by multiplicative primary
generators where necessary. For every element row u, including nonunits,

    chi_n(u)^epsilon conjugate(chi_n'(u)^epsilon)
       = chi_c(u)^epsilon 1_{(u,E)=1}.                        (4)

The character on the right is zero at primes of f. Thus f and E together
retain the full original zero support rad(nn'). A valuation difference of
six creates no nontrivial local character, but it does retain its zero.
For example n=p^6,n'=1 gives 1_{p does not divide u}, not the constant one.

As a character of the element row, chi_c has exact moving conductor f:
at p|f its restriction to the residue-field units has order
6/gcd(6,e_p)>1, and hence conductor p. The complete finite conductor may
include only the already fixed factors in S if one projects to fixed ray
classes. In particular the moving conductor norm is **Nf**, not Nc, and no
prime of E is ramified merely because it belongs to the zero support.
This elementary conductor assertion uses the denominator-symbol definition;
one need not replace it by a moving numerator character or remove a mask.

For a fixed selected row set C, define

    K_C(c;E) = sum_{u in C} chi_c(u)^epsilon 1_{(u,E)=1}.

Then the mixed norm has the exact expansion

    sum_{u in C}|F(u)|^2
      = X^(-1) sum_{n,n'} b(n) conjugate(b(n'))
          nu(n) conjugate(nu(n')) K_C(c(n,n');E(n,n')).       (5)

The norm includes the actual sixth-power-free physical element rows and their
unit factors. They are not replaced by ideal rows. The trivial bound
|K_C|<=#C remains true with all these restrictions and is all that is used
below.

## 3. A coefficient-pair counting lemma

Let n,n' range over ideals of norm at most CX. For V>=1, the number of pairs
with Nf(n,n')<=V is

    O_epsilon(X V^(1/2+epsilon)).                             (6)

To prove this, write g=(n,n'), n=g A and n'=g B, with (A,B)=1. Extract sixth
powers uniquely:

    A=a_0 a^6,  B=b_0 b^6,

where a_0,b_0 are sixth-power-free, coprime, and

    rad(a_0 b_0)=f.

At each prime of the squarefree ideal f, there are ten possible allocations:
choose a side and an exponent in {1,...,5}. Fix one such allocation. Counting
g by its norm gives at most

    O( X / max(Na_0 (Na)^6, Nb_0 (Nb)^6) )
      <= O( X (N(a_0 b_0))^(-1/2) (N(ab))^(-3) ).            (7)

The count is zero if the maximum exceeds CX. Dropping this restriction and
the coprimality restrictions only enlarges the bound. The ideal sums of
(Na)^(-3) and (Nb)^(-3) converge. Since N(a_0 b_0)>=Nf, summing the ten local
allocations costs at most 10^omega(f)(Nf)^(-1/2). Finally

    sum_{Nf<=V, f squarefree} 10^omega(f) (Nf)^(-1/2)
      <<_epsilon V^(1/2+epsilon)

by the elementary divisor bound and ideal counting. This proves (6).

Combining (2), (5), (6), and |K_C|<=#C proves the following **absolute** block
bound, before any cancellation among pairs:

    X^(-1) sum_{Nf(n,n')<=V}
       |b(n)b(n') K_C(c;E)|
      <<_epsilon (#C) V^(1/2+epsilon) X^epsilon.              (8)

All masks and coefficient restrictions may remain in place. Hence this is
valid for the irregular zero/profile class itself, without asserting any
character cancellation on that class.

In particular V=1 covers every pair with n/n' a sixth power in the fractional
ideal group, including the ordinary diagonal. These pairs contribute at most
(#C) X^epsilon. The ordinary diagonal alone satisfies the same conclusion
directly from (2). Sixth-power-equivalent columns are therefore not the
obstruction at the proposed exponents.

## 4. The whole plain-variable diagonal is also controlled

One can remove a larger positive block than the composite-column diagonal.
Expand only the plain witness in |M_r Q_I S_m|^2. The terms in which its two
ideal indices agree, k=k', contribute exactly

    D_plain = N^(-1) sum_k |B(Nk/N)|^2
                 sum_{u in C}|M_r(u)Q_I(u)|^2 1_{(u,k)=1}.   (9)

The fixed ray character has modulus one on the original good support; if an
extra fixed zero is present it is simply retained in this nonnegative sum.
Drop the displayed row mask only after this positive expression is formed.
The normalized plain coefficient square sum is O(1), by ideal counting and
bounded annular profiles. The existing marked inverse moment therefore gives

    D_plain << U^(1+epsilon)(1+T_1)^A,                        (10)

provided the selected whole slots obey its two original strict capacity
conditions. Those are exactly the conditions already imposed at the inverse
capacity in the localized target. This argument does not require arbitrary
inverse coefficients or any new mixed moment.

The block (9) includes all inverse/prime off-diagonal terms paired with equal
plain ideals, even if the resulting composite columns differ. To combine it
with the conductor reduction without double counting, retain tuple indices
in (1), first remove k=k', and then split the k!=k' tuples according to (3).
The small-conductor bound (8) is unchanged: the sum of absolute weights of
all factorizations producing a fixed n is also divisor-bounded, and a tuple
restriction can only decrease that positive majorant. The restricted
coefficient need no longer factor as b(n) conjugate(b(n')); its pointwise
absolute bound is enough for this application.

## 5. Quantitative removal at the localized target

The desired exponent is

    K_target = 1 + delta m - 1/5000,

on delta in [9/25,21/50], m in [9/25,1/2]. First, using only the trivial
physical-row count #C<<U, (8) with V=U^(1/4) gives exponent 9/8. Its uniform
margin below the target is

    (1+(9/25)^2-1/5000) - 9/8 = 11/2500.                   (11)

Thus a small-conductor block is harmless even without using exceptional-row
sparsity.

More usefully, the scalar count already assumed in this investigation gives

    #C << U^(R*+epsilon) (1+T_1)^A,
    R* = 1-delta + (5/6-delta)(t_0-1).

This is the count for the full fixed buffered zero/profile bin, before
asking that a particular r,m witness pair is large. Its proof may select
witnesses separately; no new mixed estimate is needed to count C. The
localized rectangle has t_0-1<3/20, as checked in the existing profile and
localized-target calculations. Consequently

    R* <= 9/8 - 23 delta/20.

Taking **V=U^(4/5)** in (8) therefore gives exponent at most

    R* + 2/5 <= 61/40 - 23 delta/20.

The target surplus is uniformly at least

    delta(m+23/20) - 21/40 - 1/5000
      >= (9/25)(9/25+23/20)-21/40-1/5000
      = 23/1250.                                            (12)

This fixed 0.0184 surplus is much larger than the required 1/5000 mixed
saving. It absorbs the arbitrarily small divisor/Sobolev losses in the
existing order of parameter choices, with the source's height cost retained.
The count hypothesis and height conventions remain conditional on the
external results; the pair counting in Section 3 is elementary.

## 6. What remains after this reduction

To prove the proposed mixed moment, it now suffices to upper-bound the real
part of the remaining coefficient-weighted **tuple** sum in (5), restricted to

    k != k' and Nf(n,n') > U^(4/5),                           (13)

by U^(K_target+epsilon)(1+T_1)^A. Since (8) bounds the removed block in absolute
value with a fixed surplus, this implication does not require that either
block be separately positive. Demanding a bound for the absolute value of
the remaining summed block is a convenient stronger formulation; demanding
the sum of the absolute values of its individual pairs would be much
stronger still and is not supplied here.

The unresolved block has a genuinely moving nonprincipal ratio character.
It also excludes column pairs with gcd norm at least a fixed multiple of
X/U^(2/5), since Nf<=N(nn'/(n,n')^2). This is a multiplicative notion of
proximity: similar numerical norms alone do not imply a small conductor.

The obstacle is specific. C is chosen by zeros and near-saturated prime-slot
amplitudes, so its indicator is not a smooth complete row weight. One cannot
apply a complete-row character-sum estimate to K_C merely because chi_c is
nonprincipal. Positivity permits enlarging the **whole** mixed norm to a
complete row family, but not replacing the signed block in (5) term by term
by a complete-row kernel. Such an enlargement is a distinct sufficient route
and still requires an estimate for the actual mixed coefficient class (1).

The next arithmetic calculation should therefore retain (1), the large
moving conductor (13), and the row-selection issue explicitly. The existing
Möbius-squarefree marked moment does not automatically accept the convolution
(1), whose plain variable allows higher prime powers. No such extension is
claimed by this reduction.

See the [combined mixed-moment reduction](MIXED_MOMENT_REDUCTION_20261008.md)
for the complete decomposition and current remaining signed estimate.
