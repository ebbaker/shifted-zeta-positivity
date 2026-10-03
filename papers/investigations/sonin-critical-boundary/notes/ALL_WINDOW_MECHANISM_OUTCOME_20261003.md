# All-window mechanism: effective reductions and the cancellation that remains

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and reasoning effort not exposed.
The results below have internal separate-agent same-model audits, not
independent specialist refereeing. The all-window sign remains unproved.

This continuation pursued the all-window estimate after the certified
L=6/5 comparison. It produced effective relative-tail and resolvent
certificates, a rigorous limitation of the scalar-tail strategy, and a
concrete signed-prime covariance test. No further full-source support
certificate was attempted. The original manuscript and both earlier
certificate packages were preserved.

## 1. Effective relative tails now retain the mixed terms

For every fixed finite prime set S and support length L, the prior work
provides the positive source operator B, bounded selfadjoint correction K,
and compact relative correction H=B^(-1/2)KB^(-1/2). The new
[effective-tail note](ALL_WINDOW_EFFECTIVE_RELATIVE_TAILS_20261003.md)
quantifies that reduction.

If ||K||<=k and the B eigenvalues are b_1<=b_2<=..., let E_n be the
actual first-n-mode spectral projection. Then

    J_n=E_n H+H E_n-E_n H E_n,
    rank(J_n)<=2n,
    ||H-J_n||<=k/b_(n+1).                                (1)

This retains the mixed columns in the finite-rank approximation. Simple
compression E_n H E_n would additionally require a mixed-term bound
involving the unknown bottom gap. Formula (1) removes that dependence
from the remainder, but requires the **full** columns H E_n and a
certified spectral subspace; a numerical head cannot merely be declared
to be that subspace.

Time-band concentration supplies explicit eigenvalue counts. If a proved
lower bound is B>=a M_L-dI, where M_L has multiplier
`m(t)=log(1+4t²)/2`, set E=(Lambda+d)/a. For E>=0,

    N_B(Lambda) <= (L/(2pi))(E+1) sqrt(exp(2(E+1))-1).      (2)

The positive and negative relative eigenvalue counts beyond epsilon are
each bounded by N_B(k/epsilon). The note also gives a concrete shifted
resolvent certificate for a numerical B gap using a specified exact
moment-projected Legendre space, finitely many full equation residuals,
and a complete complementary error. It assumes neither arithmetic
positivity nor precomputed B eigenvectors.

These constructions are effective reductions, not completed numerical
gap calculations. Their currently available constants are far too
pessimistic: already at L=6/5, the direct count bound at relative
threshold 1/2 has base-ten logarithm about 4512. This is an upper bound
from a weak estimate, not a necessary rank. No computation at that scale
was launched. The actual inverse metric transport comparison was already
established in earlier repository work and is credited explicitly.

## 2. A precise reason separate scalar tails cannot scale

The [spatial arithmetic analysis](ALL_WINDOW_SPATIAL_PRIME_REDUCTION_20261003.md)
proves more than poor constants for one implementation. Define the
complete finite shift operator on I_L by

    W_L=sum_{log n<L} Lambda(n)/sqrt(n) (S_log n+S_log n*),
    omega_L=||W_L||.

For **every** finite-dimensional source subspace M,

    sup_{F perpendicular to M, ||F||=1} <F,W_L F>=omega_L. (3)

This includes the three fixed moment functions and any additional finite
head. The proof modulates a near-extremal source along simultaneous
recurrences of all active prime phases. These modulations converge weakly
to zero, so finite-dimensional projection and exact smooth moment
correction do not reduce their limiting arithmetic Rayleigh value.

Unconditional PNT estimates applied to a pair of endpoint packets give
`omega_L>=c exp(L/2)` for large L, with c>0. Thus finite-rank source
truncation cannot make the unweighted arithmetic norm small. More
precisely, a positive estimate obtained by bounding Gamma and W separately
on a codimension-N tail can succeed only if

    N+4 > (L/(2pi)) sqrt(exp(2[omega_L-gamma(0)-4])-1).     (4)

This forces doubly exponential rank for that class of estimates, even
with an optimally chosen head. It is not a complexity bound for every
algorithm: the recurrent sources also have growing archimedean energy.
The obstruction concerns discarding the correlation between that energy
and arithmetic alignment.

Continuous-prime centering does not evade (3). On the neutral source
space its discrepancy is E_L=W_L+J_L, where J_L is compact with kernel
exp(-|x-y|/2). Hence the essential spectral top of E_L is still omega_L.
In particular `E_L<=poly(L) I` in bare L2 is false for large L. A useful
estimate must retain the source energy, its direction, and its mixed terms.

## 3. The centered low-frequency block must also grow

The [mechanism obstruction audit](../reviews/ALL_WINDOW_MECHANISM_OBSTRUCTION_AUDIT_20261003.md)
addresses the other side of Q=Gamma+J-E. The reference multiplier
`gamma(t)+1/(t²+1/4)` is negative on an open interval near zero. Exact
preparation and mean neutrality do not remove that interval on large
supports. A prepared modulated packet gives a negative reference value.

The reference has off-diagonal kernel

    -exp(-5|u|/2)/(1-exp(-2|u|)).

Widely separated translates of one negative prepared packet therefore
produce negative subspaces of dimension at least cL-O(1). Consequently
no fixed-rank repair, or fixed number of additional conditions, can make
Gamma+J nonnegative on every window. A growing low-frequency block is
unavoidable in this centered route. This does not rule out the desired
one-sided estimate E<=Gamma+J; on those directions it requires negative
signed discrepancy. Replacing it by an absolute error would destroy
the sign needed for the comparison.

## 4. A concrete cancellation test with outward arithmetic

The [translated-probe criterion](ALL_WINDOW_TRANSLATED_PROBE_CRITERION_20261003.md)
isolates a long-range arithmetic quantity whose size is forced by
all-window positivity. For a fixed normalized real prepared probe g of
support width ell, write phi=autocorrelation(g). At separation r>ell,

    C_g(r)=Q(g,tau_r g)=-M_g(r)+epsilon_g(r),
    M_g(r)=sum_n Lambda(n)/sqrt(n) phi(log n-r),
    |epsilon_g(r)|<=ell exp(-5(r-ell)/2)/(1-exp(-2(r-ell))). (5)

The continuous main density vanishes exactly by pole neutrality. Yet the
absolute version of M_g grows asymptotically as a strictly positive
constant times exp(r/2). This proves why taking absolute values even
after source smoothing loses the intended cancellation.

A bounded scalar experiment uses one exact polynomial prepared probe of
width 1/2 and only separations 4,6,8,10,12. Validated diagonal integration
gives Q[g] approximately 1.466940031. All five two-source Gram matrices
pass outward checks. At separation 12,

    signed prime sum:          approximately -0.777399216,
    absolute prime majorant:  approximately 90.360168757,
    certified Gram margin:    greater than 0.68954.

The [small reproducible package](../numerics/all_window_mechanism_20261003/README.md)
includes every prime power, exact rational autocorrelation, and 192/256-bit
records. These are finite two-dimensional checks, not positivity on the
full length 12.5 source space or at untested separations.

For a complete family of prepared approximate-identity probes, positivity
of **all** finite translate Gram matrices is equivalent to the original
all-window target. Pairwise bounds alone are insufficient. The note
proves this density statement and identifies the signed prime-error
integral a global estimate would need to control. It does not manufacture
a positive covariance or assume a zero-sampling measure.

## 5. Certificate completeness does not close the global quantifier

The obstruction audit proves a useful exact statement: at any fixed L
where Q has a strictly positive gap, sufficiently large signed frequency
cutoffs and sufficiently accurate finite approximations eventually give
a certificate. This follows from compactness of each bounded-band
operator and monotone convergence of the truncated forms, not from an
unjustified norm limit.

That theorem is conditional on the gap at the chosen window. Under RH,
strict fixed-window gaps can also be justified without assuming simple
zeros; this is recorded only as a conditional diagnostic. Neither
statement proves that all finite-window certificate searches terminate.
Local continuity or smaller adaptive steps still permits accumulation
at an unknown finite point where the margin vanishes.

## 6. The next theorem to pursue

The remaining target is still Q>=0 on an unbounded sequence of nested
windows with the same three moments. The new results narrow the useful
estimate: it must bound the **joint signed energy-relative operator** or
its actual prime-covariance Gram matrices, instead of separately bounding
the two terms by their worst scalar values.

One concrete operator formulation uses the positive reference
`A_L=Gamma_L+(1-gamma(0))I` on the neutral source space and
`V_L=W_L+(1-gamma(0))I`. Arithmetic positivity is equivalent to
`A_L^(-1/2)V_L A_L^(-1/2)<=I`. A sufficient scalable proof must control
its complementary and mixed blocks in a specified source decomposition,
along with the finite comparison, on unbounded L. Equations (1)--(2)
and the full-residual construction provide legitimate certificates for
such blocks when the required estimates are available; (3)--(4) explain
why an independent arithmetic norm is inadequate.

An alternative direct arithmetic formulation is to prove the entire
translate-Gram positivity in §4, preserving the signs of the centered
prime sums. The bounded probe experiment is evidence about this proposed
mechanism, not evidence that all Gram sizes or all separations pass.
No signed global bound, nonaccumulating recurrence, or all-window theorem
has yet been obtained. The next bounded work should target one of these
joint estimates, with its hypotheses and cost stated before a larger run.
