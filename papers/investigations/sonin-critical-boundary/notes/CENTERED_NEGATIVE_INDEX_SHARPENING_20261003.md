# An explicit linear lower bound for the centered negative block

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), separate same-model analytic continuation. Exact serving
variant and configured reasoning effort are not exposed and are not inferred.
This is internal research, not independent specialist refereeing.

The [mechanism obstruction audit](../reviews/ALL_WINDOW_MECHANISM_OBSTRUCTION_AUDIT_20261003.md)
proved that the negative index of the centered reference grows at least as
`cL-O(1)`, by packing translated negative sources. The present elementary
argument makes the coefficient explicit: the lower bound is

    negative_index((Gamma+J)|E_L)
       >= max(0, ceil(L t_star/pi)-4),                     (1)

where

    t_star = 6.1258715695008534784...,
    t_star/pi = 1.9499254820643357971... .

The decimals are supported by a small outward scalar certificate described
below. Equation (1) is a lower bound, not an asymptotic equality. It concerns
the centered reference `Gamma+J`, not the arithmetic Weil form Q.

## 1. Exact centered multiplier and its unique sign change

Use the Fourier convention `Fhat(t)=integral F(x)exp(-itx) dx` and

    gamma(t)=Re psi(1/4+it/2)-log pi,
    Jhat(t)=1/(t^2+1/4),
    m(t)=gamma(t)+Jhat(t).

The digamma recurrence gives exactly

    m(t)=Re psi(5/4+it/2)-log pi.                          (2)

Indeed the real part of `1/(1/4+it/2)` is `1/(t^2+1/4)`.
In particular

    m(0)=4-EulerGamma-pi/2-3log(2)-log(pi)<0.

With `a_n=2n+5/2`, the absolutely convergent series is

    m(t)=m(0)+sum_(n>=0) 2t^2/[a_n(a_n^2+t^2)].          (3)

Consequently m is even and strictly increasing for t>0. Integral comparison
also gives

    m(t)-m(0) >= (1/2)log(1+4t^2/25),

so m tends to infinity. There is exactly one positive root t_star, and
the negative band is precisely `(-t_star,t_star)`.

The stronger property needed below is that

    f(v):=m(sqrt(v)),  v>=0,

is increasing and concave. Each summand
`2v/[a_n(a_n^2+v)]` has positive first derivative and negative second
derivative. The differentiated series converge locally uniformly, which
justifies this conclusion also at v=0.

## 2. A Dirichlet subspace with a uniform negative upper bound

Let I_L=(-L/2,L/2), and let D_(n,L) be the span of its first n normalized
Dirichlet sine modes. Extend its functions by zero. Every F in this space
belongs to H^1(R) and therefore to the logarithmic Fourier form domain, with

    integral t^2 |Fhat(t)|^2 dt/(2pi)
       = ||F'||_2^2 <= (pi n/L)^2 ||F||_2^2.              (4)

For nonzero F, `|Fhat(t)|^2 dt/(2pi ||F||_2^2)` is a probability measure.
Jensen's inequality for the concave f, followed by monotonicity and (4),
proves

    (Gamma+J)[F] <= m(pi n/L) ||F||_2^2,
    F in D_(n,L).                                       (5)

All integrals are finite: H^1 controls the second Fourier moment, while m
has only logarithmic growth. Thus (5) is valid for every finite linear
combination, including complex coefficients.

Let E_L be the unchanged three-moment space, orthogonal to
`1, exp(x/2), exp(-x/2)`. The intersection

    D_(n,L) intersect E_L

has dimension at least n-3. If `pi n/L<t_star`, equation (5) is a strictly
negative upper bound on that entire intersection. It follows that

    negative_index((Gamma+J)|E_L) >= max(0,n-3)           (6)

for every positive integer n satisfying that strict inequality. The negative
index denotes the maximum dimension of a subspace on which the form is
strictly negative, or equivalently the number of negative eigenvalues here.
The equivalence follows from the already established compact form-domain
embedding; no spectral asymptotic is used.

The same finite-dimensional strict negative subspaces can be realized in
the original smooth source class. Approximate their basis functions in
H^1_0(I_L) by compact smooth functions and correct the three small moments
with fixed compact smooth dual functions. Form continuity and the strict
finite-dimensional margin preserve negativity for sufficiently accurate
approximations.

The largest nonnegative integer strictly below `L t_star/pi` is
`ceil(L t_star/pi)-1`. Taking it in (6), and using the zero-dimensional space
when it vanishes, gives (1). The ceiling keeps the strict boundary correct
when `L t_star/pi` is an integer. In particular,

    liminf_(L->infinity) negative_index((Gamma+J)|E_L)/L
       >= t_star/pi > 1.9499254820643357971.              (7)

With r fixed independent linear conditions in place of the three moments,
the same argument gives `max(0,ceil(L t_star/pi)-1-r)`.

## 3. Consequences and limits

Any bounded finite-rank selfadjoint correction which makes this centered
reference nonnegative has rank at least (1). Any additional conditions
removing all of its negative directions have codimension at least (1)
within E_L. These statements follow by intersecting a negative subspace
with the kernel of the correction or of the added conditions.

This sharpens only the required size of the low-frequency block in the
centered route. It leaves open the desired signed inequality

    E <= Gamma+J,

whose negative directions require correspondingly negative arithmetic
discrepancy. Neither (1) nor (7) asserts that Q has a negative direction,
and no upper bound matching (7) is proved here.

## 4. Small outward scalar certificate

The companion [scalar generator](../numerics/single_probe_joint_20261003/certify_centered_reference_zero.py)
starts with [6,7], checks
the opposite signs using Arb/Acb digamma arithmetic, and performs 64 rational
bisections at 192-bit precision. The [192-bit record](../numerics/single_probe_joint_20261003/centered_reference_zero_192.json) records
exact rational endpoints, outward enclosures of both function values,
outward density endpoints, runtime versions, and the generator's SHA-256.
The analytic monotonicity above turns the sign bracket into a unique-root
certificate. It contains no arithmetic prime sum or source discretization.

The resulting outward rational endpoints imply

    6.12587156950085347841 < t_star
                             < 6.12587156950085347848,
    1.94992548206433579713 < t_star/pi
                             < 1.94992548206433579715.

Reproduction requires Python and python-flint:

    python3 -B certify_centered_reference_zero.py --bits 192 \
      --output centered_reference_zero_192.json

For a completely rational implementable lower bound, any certified rational
`c<t_star/pi` can replace t_star/pi in (1), giving
`max(0,ceil(cL)-4)`. In particular `c=1.9499254820643357971` is valid.
