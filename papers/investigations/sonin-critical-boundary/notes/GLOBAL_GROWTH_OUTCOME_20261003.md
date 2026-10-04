# Global growth continuation: proved bounds and the remaining target

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
were not exposed and are not inferred. The derivations received internal
same-model cross-checks, not independent specialist refereeing.
Repository baseline: `5052fc961dc755718f2cf88516e78096eb9e8edf`.

## Main outcome

The desired global subexponential estimate is **not proved**. There are,
however, new rigorous bounds and a smaller sufficient target for the fixed
prepared polynomial probe in the current manuscript:

1. Either an eventual upper subexponential envelope or an eventual lower
   subexponential envelope, on its own, is equivalent to RH. Weighted
   integrability of just one signed part also suffices.
2. Prime powers contribute `o(1)`, so the same criteria can be imposed on
   the sum over primes alone.
3. An explicit zero-tail estimate and a published finite-height RH
   verification give `|M_g(r)|<1.47931505787654<1.48` for **every real
   separation `2<=r<=500`**. This is a bound on a continuous interval,
   not a collection of sampled prime sums.
4. Applying a known zero-free region to this smoothed source gives the
   unconditional asymptotic bound

       M_g(r)=O_c(exp(r/2-c sqrt(r)))
       for every 0<c<2 sqrt(11/5.558691)=2.813455638...

   This still has exponential rate one-half and does not reach the target.
5. A direct weighted prime-pair energy calculation exposes a false route:
   sharp truncation at `n<=X` creates an artificial last-window squared
   norm of order `X^(1-2epsilon)`. For `epsilon<1/2` this diverges even if
   RH is assumed. Finite energies must include the entire smoothing
   window or subtract the cutoff main term before taking limits.

The current manuscript includes the one-sided criterion, signed oscillation
bound, prime-only reduction, zero expansion and tail, continuous-range
certificate, and classical global envelope. The detailed cutoff proof and
the positive counting-model obstruction remain in the linked notes.

## Why the continuous-range estimate is rigorous

For the exact existing probe, `Phi(z)=G(z)G(-z)`. The sixth distributional
derivative of its source is a finite measure, giving

    |Phi(sigma+it)| <= exp(1/4) K^2 |t|^(-12),  |sigma|<=1/2.

The full explicit formula gives an absolutely convergent sum over all
nontrivial zeros. With `q=Q[g]`, `ell=1/2`, and

    delta_T=24 exp(1/4) K^2 T^(-11)(log(T)/11+1/121),
    b(r)=ell exp(-5(r-ell)/2)/(1-exp(-2(r-ell))),

verified critical-line location through height T implies, for r>ell,

    |M_g(r)| <= q+delta_T(1+exp(r/2))+b(r).

The entire verified low-zero mass is bounded by `q+delta_T`; its individual
ordinates need not be enumerated. At `T=3e12`, the scalar certificate gives
`delta_T<1.058e-116`. The diagonal upper bound is imported from the existing
hash-checked certificate. Both 192-bit and 256-bit outward runs and the
rational-endpoint replay pass.

The finite-height input is the theorem of
[Platt and Trudgian](https://doi.org/10.1112/blms.12460).
The zero-count estimate is
[Hasanalizade--Shen--Wong, Corollary 1.2](https://arxiv.org/abs/2107.06506).
The global asymptotic bound uses
[Mossinghoff--Trudgian--Yang, Theorem 1.3](https://arxiv.org/abs/2212.06867).
These are mathematical inputs, not computations rerun by this package.
No claim of a latest verification record or new zero-free region is made.

The continuous bound exceeds `q` and gives no exact pairwise positivity.
At a fixed T, its remainder grows like `delta_T exp(r/2)`; the small
coefficient does not remove the exponential growth as r tends to infinity.

## The narrowed arithmetic problem

It suffices to establish, for every epsilon>0, either one of

    sum_p (log p)/sqrt(p) phi(log p-r) <= C_epsilon exp(epsilon r),
    sum_p (log p)/sqrt(p) phi(log p-r) >= -C_epsilon exp(epsilon r),

eventually in r. The choice of sign can be fixed throughout; both bounds
are not needed. Every hypothetical zero `1/2+alpha+i gamma`, alpha>0,
forces both positive and negative exponential excursions with residue
lower bound `m_rho |Phi(alpha+i gamma)|` at exponent alpha.

A positive continuous counting measure satisfying a prime-number-type
asymptotic with any fixed remainder exponent above one-half can still
produce these exponential excursions under the exact same smoothing.
Thus positivity of the counting measure, the leading density, and the
polynomial preparation alone do not yield the missing estimate. Additional
signed arithmetic information about actual primes is required.

For the energy route, the correct finite object is

    E_epsilon(R)=integral_0^R exp(-2epsilon r)|M_g(r)|^2 dr,

using every prime power n<=exp(R+ell). These nonnegative integrals increase
to the desired full energy. No uniform bound on them has been established.
The divergent complete energy of a sharply truncated prime sum should not
be used as a proxy for this quantity.

## Files and validation

- [One-sided criteria, residue oscillations, counting model, and prime powers](GLOBAL_GROWTH_ONE_SIDED_20261003.md).
- [Zero expansion, continuous-range bound, and unconditional global envelope](GLOBAL_GROWTH_ZERO_TAIL_20261003.md).
- [Weighted energy and the sharp cutoff obstruction](GLOBAL_GROWTH_WEIGHTED_ENERGY_CUTOFF_20261003.md).
- [Numerical preflight](GLOBAL_GROWTH_ZERO_TAIL_PREFLIGHT_20261003.md).
- [Scalar certificates and replay](../numerics/global_growth_20261003/README.md).
- [Continuation review and manuscript validation](../reviews/GLOBAL_GROWTH_CONTINUATION_REVIEW_20261003.md).

No new prime sieve, zero-ordinate enumeration, numerical parameter sweep,
large data file, manuscript snapshot, Git commit, or remote push was used.
