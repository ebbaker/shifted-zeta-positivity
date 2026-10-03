# Translated prepared probes and the signed arithmetic obligation

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and reasoning effort not exposed.
Internal research, not independent specialist refereeing. No new literature
priority is claimed for the positive-definite-distribution criterion.

## A concrete long-range quantity

Fix a nonzero real smooth source g of support width ell<log2 satisfying
the original three moments, and normalize ||g||_2=1. Let

    phi(u)=integral g(x)g(x+u)dx,
    tau_r g(x)=g(x-r),
    C_g(r)=Q(g,tau_r g),
    M_g(r)=sum_{n>=2} Lambda(n)/sqrt(n) phi(log n-r).

For each fixed r the prime sum is finite, supported on
`e^(r-ell)<n<e^(r+ell)`. No support-independent infinite prime multiplier
is introduced. Translation preserves all three zero moments, and Q is
the same translation-invariant form across nested windows. Consequently
all-window positivity requires

    |C_g(r)| <= Q[g]                    for every r,

and, more strongly, positive semidefiniteness of every finite matrix
`[C_g(r_j-r_i)]`. The latter includes arbitrary complex coefficients.
Pairwise bounds alone do not imply these matrix inequalities: a matrix
with diagonal 1 and all three off-diagonal entries -3/4 has positive
two-by-two principal blocks but a negative eigenvalue -1/2.

The [digamma partial-fraction expansion](https://dlmf.nist.gov/5.7.E6)
gives

    gamma(t)-gamma(0)=2 integral_0^infty n(u)(1-cos(tu))du,
    n(u)=e^(-u/2)/(1-e^(-2u)).

Thus the off-diagonal kernel of Gamma is `-n(|u|)`. For r>ell,

    C_g(r) = -M_g(r) - integral_{-ell}^ell phi(u)n(r+u)du.       (1)

The single positive prime branch survives in this formula; inserting
an extra factor2 would be incorrect. Phi is real even, and

    integral phi(u)e^(u/2)du
      = (integral g(x)e^(x/2)dx)(integral g(x)e^(-x/2)dx)=0.

The leading `e^(-r/2)` term of n therefore cancels exactly. Since
`||phi||_1<=||g||_1²<=ell`, (1) yields the explicit comparison

    C_g(r) = -M_g(r) + epsilon_g(r),
    |epsilon_g(r)| <= ell e^(-5(r-ell)/2)/(1-e^(-2(r-ell))).    (2)

The long-range obligation is therefore a signed, smoothed prime estimate.
All-window positivity implies `|M_g(r)|<=Q[g]+O_g(e^(-5r/2))`.
This statement is about a fixed prepared probe, not an unprepared endpoint
packet or the norm of the entire prime-shift operator.

## Why taking absolute values after smoothing still loses the mechanism

Put `A_g(r)=sum Lambda(n)/sqrt(n) |phi(log n-r)|`. Partial summation
from the [prime number theorem](https://dlmf.nist.gov/27.12) gives, for this
fixed compactly supported continuous profile,

    A_g(r) ~ e^(r/2) integral e^(u/2)|phi(u)|du,               (3)

and the integral is strictly positive. In contrast, the same continuous
main term with signed phi is identically zero by pole neutrality.
Thus taking absolute values even after source smoothing loses an
exponentially large cancellation. This proves a limitation of that
absolute majorant, not a lower bound on the signed M_g.

Writing `R(x)=psi(x)-x`, integration by parts gives the exact identity

    M_g(r) = -e^(-r/2) integral R(e^(r+u)) e^(-u/2)
                                  [phi'(u)-phi(u)/2]du.      (4)

An estimate `|R(x)|<=x eta(log x)` therefore gives at best
`e^(r/2) sup_{|u|<=ell} eta(r+u)` times a fixed profile norm if applied
by absolute values. A qualitative PNT error tending to zero does not
provide (2)'s required bounded signed estimate. This is not a claim that
every possible use of prime-number theory must fail: (4) identifies where
oscillation must remain in a successful estimate.

## A complete probe family and its limits

Let rho_epsilon be a real even compact smooth approximate identity and
`g_epsilon=(-d²/dx²+1/4) d rho_epsilon/dx`. Each is a real three-moment
source of small support. The following statements are equivalent:

1. Q is nonnegative on the original source class for all compact supports.
2. For every sufficiently small epsilon, every finite translate Gram
   matrix of g_epsilon is positive semidefinite.

For the nontrivial direction, every original source has the form
`F=(-d²+1/4)h` with compact smooth mean-zero h. Its antiderivative k is
compact smooth, so `F=(-d²+1/4)d k/dx`. Now
`g_epsilon*k=rho_epsilon*F` is a limit of finite linear combinations
of translates of g_epsilon on a fixed compact interval. Riemann sums
converge in every smooth seminorm; Q is continuous there because its
prime list is finite and the gamma multiplier has logarithmic growth.
Let epsilon tend to zero to obtain Q[F]>=0.

This is an exact reduction, not a proof of statement 2. An arbitrarily
invented positive covariance cannot be substituted for the arithmetic
values in (1). Neither the pairwise inequality nor finitely many sampled
separations establishes the required positive-definiteness theorem.

## Bounded scalar test: preflight recorded before execution

To test the cancellation identified by (2)--(4), use a single explicit
form-domain probe of width ell=1/2:

    h(x)=(1-16x²)^8 on |x|<1/4, zero outside,
    g=(-d²/dx²+1/4)h', normalized in L2.

This polynomial probe has sufficient endpoint vanishing for the preparation
and all three moments to hold exactly by integration by parts. It is not
C-infinity at the boundary; it lies in the logarithmic form closure and
can be approximated there by smooth exactly neutral sources. The general
criterion above remains stated for smooth probes.

Its normalized autocorrelation on `0<=u<=1/2` is an exact rational
polynomial, continued evenly. Evaluate only separations r=4,6,8,10,12.
The largest prime-power cutoff is below269000; a simple sieve plus all
prime powers suffices. No higher-window full-source certificate or
adaptive support sweep is being run. The purpose is to compare signed
prime covariance with the exponentially growing absolute majorant on
the same source, not to claim a global sign from five examples.

Budget: at most 300000 sieve entries, five separations, polynomial degree
at most 31, Arb/Acb192-bit arithmetic, at most two runs at different
precisions, and 60 seconds per run. Record only code and small rational
endpoint results. Use the exact bound (2) for the off-diagonal gamma
remainder. The diagonal Q[g]=Gamma[g] can be integrated independently:

    Gamma[g]=gamma(0)+2 integral_0^ell n(u)(1-phi(u))du
                      +2[atanh(e^(-ell/2))+atan(e^(-ell/2))].

The integrand's removable origin is handled analytically: write
`(1-phi(u))/u` as a polynomial and use
`u n(u)=e^(u/2)/(2 * 0F1(3/2;u²/4))`. Acb's validated meromorphic
integration then supplies an enclosure. No floating quadrature decides
the sign. The results below record the precise scope of the scalar checks.

## Executed scalar result

The [outward probe package](../numerics/all_window_mechanism_20261003/README.md)
uses exact rational autocorrelation coefficients and includes every active
prime power. Its 192-bit run passed in less than one second, with

    1.46694003100528 < Q[g] < 1.46694003100529.

The following are rounded display values, not outward endpoints; exact
rational enclosures are saved in the records. Gram margins in the last
column are rounded down from the certified lower bounds.

| Separation r | Signed M_g(r) | Absolute A_g(r) | A_g(r)e^(-r/2) | Certified two-source Gram margin > |
|---|---:|---:|---:|---:|
|4| -0.390095 |1.750559|0.236912|1.07676|
|6| -0.595013 |4.623734|0.230202|0.87192|
|8| -0.652488 |12.432313|0.227706|0.81445|
|10| 0.548012 |33.609043|0.226456|0.91892|
|12| -0.777399 |90.360169|0.223980|0.68954|

For each listed r the validated inequality is
`Q[g]-|M_g(r)|-bound(2)>0`, which proves positivity of that two-dimensional
translate Gram, including complex coefficients. The diagonal source
is normalized in L2, and the translates are disjoint. These are five
finite-dimensional checks; they supply no full-source positivity at
length 12.5 and no bound at untested separations.

Already at r=4 the absolute majorant exceeds Q[g], while the signed
covariance passes. At r=12 the gap between 90.36 and 0.7774 is substantial.
The fixed-source asymptotic (3), rather than these five rows, proves why
the absolute majorant eventually grows exponentially. The rows only
provide a reproducible test of the exact sign-preserving arithmetic
quantity that a global mechanism would have to control.
