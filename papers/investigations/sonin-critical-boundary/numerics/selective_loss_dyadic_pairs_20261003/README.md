# Dyadic pair weights, complete caps, and shifted correlations

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal same-model checks, not independent specialist review.

This is a small **floating diagnostic**, with no outward certificate or
global arithmetic estimate. It checks the next exact reduction in the
[handoff](../../notes/NEXT_SESSION_SELECTIVE_LOSS_20261003.md), using the fixed
normalized polynomial probe from
[program 04](../../notes/selective-loss-program/04_complete_response_and_signed_pairs_20261003.md)
and the dyadic variance in
[program 06](../../notes/selective-loss-program/06_global_mechanism_tests_20261003.md).
All active prime powers are included. The largest integer tested is 257;
there is no large enumeration, fit, inverse, or growth inference.

## Exact weights checked

Write a=1/4, a0=exp(-a), b0=exp(a),
`w(t)=t^(-1/2)g(-log t)`, extended by zero, and
`V(x)=sum Lambda(n)w(n/x)`. For positive real n,m,X, let
`c=(log n+log m)/2`, `delta=(log m-log n)/2`. Then

```
W_X(n,m) = sqrt(nm) integral_lo^hi exp(2v)g(v+delta)g(v-delta)dv,
lo = max(-a+abs(delta),log X-c),
hi = min( a-abs(delta),log(2X)-c),
```

with zero weight if `hi<=lo`. This identity follows from `y=log x`,
then `v=y-c`. Independently, `t=n/x` gives

```
W_X(n,m) = n integral_L^U w(t)w((m/n)t)dt/t^2,
L = max(n/(2X),a0,a0*n/m),
U = min(n/X,b0,b0*n/m).
```

The complete arithmetic range is `a0*X<n,m<2*b0*X`; additionally
`abs(log(n/m))<1/2` is necessary for nonzero weight. Symmetry and
`W_(cX)(cn,cm)=c W_X(n,m)` are checked separately, with explicit zero-support
examples. Individual packets have support `n/b0<x<n/a0`. The lower-cap,
full-packet, and upper-cap ranges for n are, respectively,
`(a0*X,b0*X)`, `[b0*X,2*a0*X]`, and `(2*a0*X,2*b0*X)`.
The endpoints have zero packet value.

For each sample the code independently integrates `V(x)^2` in x, integrates
`exp(2y)p(y)^2` in y, and evaluates the full pair sum. The x and y integrations
split at every packet endpoint; their Gauss orders are 32. The two pair-weight
coordinates use orders 24 and 40. The signed off-diagonal is grouped into

```
C = 2 sum_(h>=1) C_h,
C_h = sum_n Lambda(n)Lambda(n+h)W_X(n,n+h).
```

`record.json` stores every `C_h`, both signs' total mass, the six unordered
cap-block contributions, the complete diagonal, and all residuals. Taking
positive parts term by term changes these sums.

## Real-X samples and the cost of incomplete caps

| X | Active prime powers | Lower/bulk/upper | Diagonal D | Signed C | Integral V² |
|---:|---:|---:|---:|---:|---:|
| 8.125 | 8 | 3/1/4 | 210.356869 | 10.350404 | 220.707273 |
| 19.375 | 14 | 4/3/7 | 1587.782289 | -678.782556 | 908.999733 |
| 53.625 | 26 | 8/5/13 | 18928.103215 | -12421.699677 | 6506.403538 |
| 101.3 | 41 | 14/6/21 | 74718.575840 | -52128.886736 | 22589.689104 |

The exact formulas apply to arbitrary positive real X. These samples, and
three-point checks across each of `X=7/a0` and `X=23/(2*b0)`, check noninteger
windows and genuine support changes. They **do not enclose numerical error
uniformly in real X**, and do not establish an interval bound.

Keeping only `X<=n<=2X` gives, respectively, 193.329929, 1053.918718,
9108.669695, and 25218.665793 instead of the complete square integrals above.
Removing either cap separately and keeping only full packets are also
recorded. Removing terms can increase or decrease the square because the
cross terms retain their signs.

Across the four principal samples, the largest absolute difference between
the direct square and the pair expansion is `1.68e-10`, between the x and y
squares `1.35e-10`, between pair-coordinate formulas `2.89e-12`, and between
the shifted sum and the original signed sum `1.82e-12`. The largest pair
symmetry residual is `4.27e-14`. These are floating comparisons, not rigorous
error bounds.

## Independent continuum checks

The prepared exponential moment implies `integral w(t)dt=0`. Hence

```
integral integral W_X(n,m)dn dm
  = integral_X^(2X) [integral_0^infinity w(n/x)dn]^2dx = 0.
```

An independent pair-weight double quadrature uses the fixed complete
rectangle `[a0*X,2*b0*X]^2`, split into its three cap intervals. At X=1,
outer orders 48 and 80 give `2.19e-14` and `-1.05e-17`. Direct integration
of the continuum density gives a square of `7.99e-34`, with the numerical
`integral w=1.85e-17`. The continuum double integral has no arithmetic
diagonal term: its diagonal has Lebesgue measure zero. Absolute-kernel
integrals in the record are magnitude diagnostics; the nonsmooth absolute
value has visibly weaker quadrature stability than the signed integral.

Replacing the complete continuum density by its restriction to `[X,2X]`
leaves

```
integral_X^(2X) [integral_X^(2X) w(n/x)dn]^2dx
   = 0.0065923154786104... * X^3.
```

This positive coefficient is reproduced by independent pair-weight double
quadratures and by squaring the truncated continuum signal. The coefficient
is floating; the exact positive X³ scaling follows from change of variables.
Thus even the smooth main loses its exact cancellation under this incomplete
cutoff. This is a boundary diagnostic, not a prime-correlation estimate.

A different change retains every density atom in the complete active band
`[a0*X,2*b0*X]` but replaces the dyadic `W_X` by the whole-packet weight
`W_infinity=integral_0^infinity w(n/x)w(m/x)dx`. Its continuum pair square is

```
integral integral_(complete band) W_infinity(n,m)dn dm
   = 0.0277206222438185... * X^3.
```

This coefficient is independently checked by whole-packet double
quadrature, giving `0.0277206222438181` at outer order 80, and by squaring
the complete-band continuum signal over the exterior x intervals.
The lower exterior interval `(exp(-2a)*X,X)` contributes
`0.0007521839932260*X^3`; the upper interval `(2X,2*exp(2a)*X)` contributes
`0.0269684382505925*X^3`. The signal is zero throughout the dyadic x interval.
This checks the whole-packet cap obstruction in
[program 08, equation (9)](../../notes/selective-loss-program/08_dyadic_shifted_correlations_20261003.md).
Replacing cap weights and dropping atoms to `[X,2X]` are distinct changes;
both create artificial positive X³ terms, with different coefficients.

For the fixed-shift continuum density, independently check

```
H_X(h)=integral W_X(t,t+h)dt=X^2 F(h/X),
F(q)=integral_1^2 u C_w(q/u)du,
C_w(z)=integral w(t)w(t+z)dt.
```

Samples at q=0, 0.05, 0.2, 0.45, 0.7, 0.95, and 1.02 have a maximum
identity discrepancy of `7.78e-15`. They include positive and negative F:
`F(0.05)=0.846879733`, `F(0.2)=-0.697096969`,
`F(0.45)=0.0932840095`, and `F(0.7)=-0.00668083089`.
The exact normalization gives `F(0)=3/2`,
`integral_0^infinity F(q)dq=(7/6)(integral w)^2=0`, and support
`q<2*(b0-a0)=1.010449267...`. The last integral is an analytic identity;
the script does not approximate it on a dense grid or test a singular-series
asymptotic.

## Reproduction and scope

Run from this directory with the existing NumPy dependency:

```
OPENBLAS_NUM_THREADS=1 python3 diagnostic.py
```

The run takes about 0.6 seconds here and rewrites `record.json`, including
the script SHA-256, runtime, Python executable/version, NumPy version, orders, samples,
truncation comparisons, and consistency checks. No dependency installation
is required. Assertions are numerical consistency checks, with floating
tolerances; they certify no analytic statement.
The executable used was
`/Library/Frameworks/Python.framework/Versions/3.10/bin/python3`, with
NumPy 1.25.1.

The missing global input remains an estimate for the combined signed
actual-prime remainder on the `X^2 log(2X)` scale, uniformly for sufficiently
large real X. These small computations supply no such input, no positive
source-wide Sonin complement, and no RH proof.
