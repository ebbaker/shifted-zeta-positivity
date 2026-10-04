# Signed arithmetic/discrepancy pilot

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and effort are not exposed and are not
inferred. Floating diagnostic only; no outward certificate or global rate.

This extends the earlier response pilot by separating the actual causal
diagonal, signed off-diagonal, reflected convolution, moment projection,
and complete continuum-discrepancy terms. [THEORY.md](THEORY.md) supplies
the exact identities and two unconditional facts: the direct diagonal is
asymptotic to `Y^2/2`, while absolute off-diagonal pair mass is exponentially
large. The missing bound is on the signed aggregate.

With `Y=r+1/4`, the script uses

```
p(y)=sum Lambda(n)/sqrt(n) g(y-log n),
J=integral_0^Y p(y)^2dy, D=the direct diagonal, Theta=J-D,
C=(p*p)(r), M=the exact odd-moment projection subtraction,
R_ar=D+Theta-C-M.
```

It also evaluates the complete continuum cap response `w0` and the projected
discrepancy `w-w0`, retaining both moment projections. All active prime
powers and all polynomial/cap breakpoints are included. Sixteen-node Gauss
integration is exact for the polynomial pieces in ideal real arithmetic;
orders 16/24 and separate moment orders 24/32 are floating comparisons.
Their agreement does not enclose logarithmic or rounding errors.

| r | Powers | Pieces | D | Theta | C | Projected norm squared |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 8 | 29 | 1.995767 | -0.112990 | -0.092997 | 1.974356 |
| 3 | 18 | 63 | 4.502902 | -0.635469 | -0.301284 | 4.163647 |
| 4 | 34 | 119 | 8.037057 | -3.182372 | -0.738910 | 5.591572 |
| 5 | 68 | 233 | 12.632599 | -6.203762 | -1.436012 | 7.861879 |
| 6 | 143 | 485 | 18.187000 | -10.110604 | -2.649412 | 10.721339 |
| 7 | 308 | 1037 | 24.877903 | -15.476821 | -1.132857 | 10.531140 |
| 8 | 698 | 2329 | 32.569689 | -20.942976 | -4.260120 | 15.886787 |
| 9 | 1642 | 5423 | 41.286417 | -29.386571 | -1.835301 | 13.734126 |
| 10 | 3932 | 12931 | 51.002978 | -37.110718 | 4.814616 | 9.077570 |

The off-diagonal cancellation is directly measured, rather than inferred
from a polynomial fit. The reflected convolution changes sign and must
remain signed. These nine samples establish no growth rate or bound over
continuous separation intervals.

The initial full run took 3.36 seconds (the root replay took about 3.32 seconds) with the existing NumPy dependency and
single-threaded BLAS. No dependency is installed and no large matrix or
data cache is written. Run:

```
OPENBLAS_NUM_THREADS=1 python3 diagnostic.py
```

`record.json` stores all pieces/counts, both polynomial quadrature orders,
moment checks, continuum centering, diagonal projection details, and exact
script SHA-256. Maximum raw-order relative difference was `7.7e-15`;
the signed causal identity residual across both orders was below `1.8e-13`. These are floating
stability diagnostics, not error intervals.

No known-reference inverse A, Sonin/source inverse B, full dual energy X,
safe complement, or selective-loss certificate was computed.

See the [research reduction](../../notes/selective-loss-program/04_complete_response_and_signed_pairs_20261003.md) and [internal audit](../../reviews/SELECTIVE_LOSS_SIGNED_PAIRS_REVIEW_20261003.md) for the exact targets and proof scope.
