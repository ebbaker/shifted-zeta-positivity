# Small finite arithmetic-response diagnostic

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and configured reasoning effort are
not exposed and are not inferred. This is a floating diagnostic, not an
outward certificate or independent specialist review.

The script computes the actual finite prime-power response `W_L F_r`
for `r=2,3,4,5,6`, on the centered interval of length `L=r+1/2`, then
projects it onto the three-moment source space. The centered source is
`F_r=(g(x+r/2)+g(x-r/2))/sqrt(2)`. It uses the exact factored polynomial

```
g0(x)=-64*x*(1-16*x^2)^5*(2689-215072*x^2+256*x^4), |x|<1/4,
||g0||^2=146640624550936576/37921101075,
g=g0/||g0||.
```

All active prime powers, including powers of old primes, are included.
The response is odd. Its mean and cosh moment vanish, leaving the sinh
projection with squared subtraction
`|<sinh(x/2),W_L F_r>|^2/[sinh(L/2)-L/2]`.

Every translated-polynomial breakpoint is included. The squared response
has degree at most 30 on each piece, so 16-node Gauss integration is exact
in ideal real arithmetic. Orders 24 and 32 provide floating stability
comparisons; the sinh moment uses their same piece boundaries. Agreement
between these orders is not a rigorous rounding or truncation enclosure.

| r | Active prime powers | Pieces | Raw squared norm | Projected squared norm | Retained fraction |
|---:|---:|---:|---:|---:|---:|
| 2 | 8 | 27 | 1.97577390749 | 1.97435617326 | 0.999282441057 |
| 3 | 18 | 61 | 4.16871633939 | 4.16364676257 | 0.998783899789 |
| 4 | 34 | 117 | 5.59359493402 | 5.59157184769 | 0.999638320909 |
| 5 | 68 | 231 | 7.86484835070 | 7.86187878967 | 0.999622426156 |
| 6 | 143 | 483 | 10.7258071987 | 10.7213391696 | 0.999583431907 |

The probe norm-squared check was `1.0000000000000002`. Raw squared norms
at orders 16/24/32 agreed within `9.0e-16` relatively, and moments at
orders 24/32 within `7.6e-15` relatively. The complete run took about
0.06 seconds after import; the root replay took about 0.09 seconds.
These small windows show that three-moment
projection removes little of this arithmetic response here. They establish
no polynomial or asymptotic growth rate.

No `B` inverse, Sonin correction, Schur inverse, boundary inverse, or full
Weil form was computed. In particular these response norms alone do not
certify a selective-loss bound or a safe complement.

Run with an existing Python/NumPy environment:

```
python3 diagnostic.py
```

No dependency is installed. The script writes `record.json`, which records
all three quadrature orders, raw and projected norms, retained and growth
ratios, order differences, prime-power/piece counts, versions, runtime,
and the SHA-256 of the exact script. No large data file is generated.

## Exact continuum constants

[continuum_constants.py](continuum_constants.py) separately regenerates
the fixed-profile constants with standard-library rational arithmetic:

```sh
python3 continuum_constants.py
```

Its [small exact record](continuum_record.json) gives the complete
smooth-density response squared norm `917180/580421327`, independent
of separation, and the kernel comparison constant
`Dg=1950415853039/2321685308`. These are exact polynomial integrals.
They do not prove a bound on the remaining prime discrepancy.

The [centered dual energy note](../../notes/selective-loss-program/03_centered_dual_energy_20261003.md)
derives the complete response, its continuum cancellation, the sharp-cutoff
edge, and its relation to the sufficient polynomial-loss target. The
[program overview](../../notes/selective-loss-program/overview.md) records
the changed complement obligation. The floating pilot and exact constants
have distinct scopes; only the latter have exact rational sign checks.
