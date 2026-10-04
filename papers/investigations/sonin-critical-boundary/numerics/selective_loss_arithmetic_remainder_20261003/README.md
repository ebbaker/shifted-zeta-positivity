# Actual signed arithmetic remainder against the singular-series main

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Internal same-model checks, not independent specialist review.

This package computes the exact finite remainder proposed in
[program 08, equations (16)–(18)](../../notes/selective-loss-program/08_dyadic_shifted_correlations_20261003.md):

```
R(X)=2 sum_(h>=1) [sum_n Lambda(n)Lambda(n+h)W_X(n,n+h)−SS(h)H_X(h)],
H_X(h)=X² F(h/X),
V_square(X)=D_actual(X)+C_SS(X)+R(X),
C_SS(X)=2 sum_(h>=1) SS(h)H_X(h).
```

Every active prime power and every integer shift `1<=h<2*(b0-a0)*X` is
included. The coordinate band is `a0*X<n,m<2*b0*X`, including both caps.
The script reuses the fixed normalized g, w, prime-power sieve, and direct
variance quadrature from the
[previous diagnostic](../selective_loss_dyadic_pairs_20261003/diagnostic.py),
without changing those definitions or writing a cache to that directory.
All calculations are floating diagnostics. They supply no global rate or
uniform interval enclosure.

## Signed actual data

| Real X | Prime powers | V_actual/X² | (D_actual+C_SS)/X² | R_actual/X² |
|---:|---:|---:|---:|---:|
| 19.375 | 14 | 2.421476917 | 2.603816362 | -0.182339445 |
| 53.625 | 26 | 2.262592718 | 2.048818879 | 0.213773839 |
| 101.3 | 41 | 2.201361482 | 2.330221582 | -0.128860100 |
| 201.75 | 67 | 2.238199591 | 1.961836434 | 0.276363157 |
| 501.125 | 138 | 1.664739062 | 2.069577289 | -0.404838227 |

These are five small shells, not a growth law. In particular they provide
no estimate for `R(X)_+` at unbounded X. Both signs of the actual remainder
occur in these examples, and the model coefficient below does not determine
the actual variance.

The record retains every signed per-shift residual, including shifts whose
actual sum is zero but whose model weight is nonzero. At X=501.125, the
positive residual mass across shifts is `2551844.992737`, the negative mass
is `-2653510.504958`, and their combined remainder is `-101665.512221`.
Clipping the shifts separately loses this cancellation. Odd shifts use the
exact `SS(h)=0`; actual odd-shift contributions from powers of two remain
present. No parity correction is discarded.

The actual and model off-diagonals are additionally partitioned into the
six unordered lower/bulk/upper packet blocks. Each actual block is summed
with its sign; each model block integrates `W_X(t,t+h)` over the matching
continuous block. The same partition of R is recorded, alongside the
diagonal in each packet region. Thus both boundary caps are retained in the
arithmetic comparison and in its model.

## Model constants without numerical differentiation

The singular series is zero for odd h. For even h the script uses

```
SS(h)=2 C2 product_(p|h,p>2) (p−1)/(p−2),
C2=0.660161815846869.
```

The decimal is tabulated with the Euler-product definition in the
[University of Tokyo computing report](https://www.itc.u-tokyo.ac.jp/Annual_Report/no12/AnnualReportNo12.pdf).
It is a floating input, not an enclosed infinite product. The analytic
singular-series main and its scope are established in
[program 08](../../notes/selective-loss-program/08_dyadic_shifted_correlations_20261003.md);
that main concerns the explicit model, not actual prime correlations.

Let `C_w(z)=integral w(t)w(t+z)dt`, `R0=b0-a0`, `F0=3/2`,
`C_D=2log2−3/4`, and `A_SS=2−gamma−log(2pi)`. The regularized identity

```
K_C = log R0 + integral_0^R0 [C_w(z)−1]dz/z,
J_C = integral_0^infinity z log z C_w''(z)dz = 1+K_C,
I_F = integral_0^infinity q log q F''(q)dq = F0*J_C+C_D,
c_F = A_SS*F0/2−I_F/2,
beta_model = C_D+2c_F−F0 = F0*(−gamma−log(2pi)−K_C)
```

avoids differentiating sampled kernels. It follows by integration by parts
with a lower cutoff tending to zero; `C_w(0)=1`, `C_w'(0)=0` make the
regularized integrand continuous with value zero at the origin. The script
independently applies the corresponding identity directly to F,

```
I_F=F0*(1+log Q)+integral_0^Q [F(q)−F0]dq/q,
Q=2*R0.
```

Quadrature orders 32, 48, and 64 give stable values:

```
K_C        = −3.88203276391979...
c_F        =  1.53205784389674...
beta_model =  2.20041004891337...
```

The direct-F and C_w identities differ by `4.14e-14` at order 64. The
log-density diagonal model is exactly
`D_log=X²[(3/2)log X+C_D]`, because `integral w²=1` and
`integral log(t)w(t)²dt=0`. Combining that model diagonal with the
singular-series main yields the coefficient beta_model. The record stores
both `D_log+C_SS` and `D_actual+C_SS`; neither calculation bounds R.

## Verification and reproduction

The actual variance is independently integrated by squaring the complete
signal in x, splitting at every packet endpoint. The signed pair expansion
uses centered log coordinates. Independently, F is evaluated by additive
autocorrelation quadrature, and its H weights are checked against the sum
of the separately integrated continuous cap blocks. Orders 32 and 40 are
compared for F and the cap blocks.

The maximum absolute direct-variance decomposition residual is `1.03e-8`,
at the largest shell. Dividing by X² gives less than `4.1e-14` there.
The maximum cap-partition versus shifted-remainder residual is `1.11e-9`;
the maximum normalized H cap-sum versus F discrepancy is `2.73e-15`.
These floating comparisons do not certify arithmetic, logarithmic, or
rounding error.

Run with the existing NumPy dependency:

```
OPENBLAS_NUM_THREADS=1 python3 diagnostic.py
```

The exact executable used is
`/Library/Frameworks/Python.framework/Versions/3.10/bin/python3`, with
NumPy 1.25.1. Runtime is about 1.2 seconds. `record.json` is approximately
240 KiB and includes all shifts, signed cap blocks, numerical checks,
quadrature orders, the current script hash and imported script hash, and
the execution environment. No new dependency is installed.

The remaining theorem is still an upper bound for the **combined signed
actual remainder** on the `X² log(2X)` scale, uniformly for sufficiently
large real X. A finite favorable sign, a small residual in these shells,
or the positive model coefficient does not establish that theorem.

## Four-direction fitted Chebyshev discrepancy

The separate `fitted_psi.py` and `fitted_psi_record.json` check the proposed
selective comparison without changing the arithmetic remainder script:

```
epsilon_X(u)=psi(Xu)−Xu,  a0<=u<=2*b0,
T epsilon(s)=−(1/s) integral epsilon(u)w_prime(u/s)du=V(Xs), 1<=s<=2,
epsilon_projected=epsilon_X−Proj_span{1,u,sqrt(u),log(u)} epsilon_X.
```

Integration by parts gives the four zero responses from `integral w'=0`,
`integral w=0`, `integral t^(-1/2)w(t)dt=integral g=0`, and
`integral w(t)dt/t=integral exp(v/2)g(v)dv=0`. Thus the fit preserves the
exact arithmetic signal. The derivative is evaluated from the factored
polynomial derivative of g, using
`w_prime(t)=−t^(-3/2)[g_prime(−log t)+g(−log t)/2]`.

All integer breakpoints `n/X` are included, including those with no prime
power jump. Fit quadrature orders 16 and 24 use the full u interval;
response orders 24 and 32 additionally split at each kernel cap. The
coefficients are computed by weighted SVD least squares, using
`numpy.linalg.lstsq`. No inverse Gram matrix is formed. The Gram condition
number, recovered from the design singular values, is approximately
`1.75983e7`; the record retains the singular values, coefficients, and
orthogonality residuals.

| Real X | Raw squared discrepancy norm | Projected squared discrepancy norm |
|---:|---:|---:|
| 19.375 | 8.486894324 | 2.439658252 |
| 53.625 | 13.712407123 | 7.865886924 |
| 101.3 | 22.940029880 | 15.236466346 |
| 201.75 | 25.828450712 | 20.243307097 |
| 501.125 | 62.243717163 | 55.908926482 |

These norms use du in the scaled coordinate. Multiplying the projected
norm by X gives the physical fitted error H(X) defined in
[program 09](../../notes/selective-loss-program/09_actual_error_projection_and_frequency_20261003.md).

The raw norms are also independently checked by the exact affine-piece
formula: for a piece of length d and midpoint m, the contribution is
`d*epsilon(m)^2+X²*d³/12`. Its floating difference from the quadrature is
below `2.85e-14`. Projected norms at orders 16 and 24 differ by less than
`7.82e-14`. The maximum Pythagorean residual is `6.70e-11`; the maximum
residual orthogonality moment is `3.27e-11`, with the recorded basis
conditioning taken into account.

At each sample, direct prime-power values of `V(Xs)` are compared with
`T epsilon_X` and `T epsilon_projected` at s=1, 1.3, 1.7, and 2. The largest
absolute direct-versus-raw response difference is `3.56e-13`, the largest
direct-versus-projected difference `4.20e-13`, and the largest individual
null-basis response `3.69e-14`. These are point checks, with no interval
or global implication.

Run the additional diagnostic with:

```
OPENBLAS_NUM_THREADS=1 python3 fitted_psi.py
```

It takes approximately 0.03 seconds and saves its own script hash, imported
definition hash, both fit orders, all response checks, and environment in
`fitted_psi_record.json`. No bound for the fitted norm at unbounded real X,
or for RH, is inferred from the displayed samples.
