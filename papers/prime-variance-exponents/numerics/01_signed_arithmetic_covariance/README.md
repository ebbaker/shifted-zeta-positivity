# Signed arithmetic covariance continuation checks

4 October 2026. Prepared with substantial LLM assistance; GPT-6 (Codex),
inherited configuration; exact serving variant and effort not inferred.

[check_cutoff_transport.py](check_cutoff_transport.py) uses standard-library
integer vectors of prime logarithms and rational continuum coefficients.
It checks full Vaughan coefficients, both cutoff annuli and their mixed
rectangle, including noninteger cutoff choices and prime powers. Run:

```sh
python3 papers/prime-variance-exponents/numerics/01_signed_arithmetic_covariance/check_cutoff_transport.py
```

[centered_sector_pilot.py](centered_sector_pilot.py) uses NumPy and the
established probe/sieve from [the original pilot](../mobius_reduction_20261004/pilot.py).
It independently assembles the semiprime coefficient from unordered prime
pairs, the smooth-outer/prime-inner sector, and the inner higher-prime-power
sector. Their sum is checked against the complete capped Vaughan coefficient.
The large-prime classification of the outer factor is checked with exact
integer arithmetic. The continuum, all prime powers, signed cross terms and
the scalar mismatch are retained.

```sh
OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 python3 \
  papers/prime-variance-exponents/numerics/01_signed_arithmetic_covariance/centered_sector_pilot.py \
  --output /tmp/centered_sector_record_20261004.json
```

Defaults are X=10000.5 and 100000.25, U=V=floor(X^(11/24)), and 128/256
Gauss–Legendre nodes. The small [record](centered_sector_record_20261004.json)
includes parameters, source hashes and library versions. No sieve, Gram
matrix or other large array is stored.

Across the four runs the floating coefficient-decomposition residual was
zero and the energy-split residual/X² was below 3.23e-16. The maximum
128→256 change across the listed sector, shape, scalar, complete and
semiprime/smooth cross energies divided by X² was below 3.51e-8.
These are numerical diagnostics, not outward error certificates.

At 256 nodes:

| X | Semiprime scalar | Smooth-outer scalar | Inner-prime-power scalar | Continuum scalar | Centered total energy/X² |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 10000.5 | −7.37917e-4 | 3.82064e-5 | 1.57796e-4 | −4.91814e-8 | 2.39844582 |
| 100000.25 | −4.41565e-5 | −9.89092e-5 | 3.70953e-6 | 7.87221e-7 | 1.96407700 |

The semiprime scalars still have the opposite sign to their eventual
positive leading asymptotic. The probe's logarithmic moment is small and
finite fluctuations dominate these samples. Thus these runs verify
bookkeeping, not the asymptotic semiprime main term, eventual negative
cross covariance, a first exponent, or any fitted convergence rate.

See the [arithmetic-overlap derivation](../../notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_OVERLAP_20261004.md),
[cutoff transport](../../notes/programs/01_signed_arithmetic_covariance/CUTOFF_TRANSPORT_20261004.md),
and [scalar detector](../../notes/programs/01_signed_arithmetic_covariance/SCALAR_DETECTOR_20261004.md).

## Exact checks for the one-sided arithmetic investigation

[check_prime_discrepancy_centering.py](check_prime_discrepancy_centering.py)
checks the density/divisor identity, full continuum cancellation, and
Stieltjes integration by parts with the strict lower cutoff. Its compact
polynomial kernel has zero ordinary moment, and its prime atoms carry
rational weights p, allowing exact fraction arithmetic. These are
synthetic inputs for the algebraic identities, not the fixed probe or
the actual log-prime measure. The [record](prime_discrepancy_centering_record_20261004.json)
contains 386 successful comparisons over 32 rational cases; omitting
the lower-cutoff boundary fails in 28 cases, as intended.

[check_smooth_sign_obstruction.py](check_smooth_sign_obstruction.py)
checks short-cofactor and complementary-divisor identities, the
roughness/parity identity including a strict endpoint, and formally
grouped coefficients with a unique retained large prime. It includes
exact comparisons at algebraic U=X^(11/24) for noninteger X by raising
to the 24th power. Its [record](smooth_sign_obstruction_record_20261004.json)
contains 81,043 successful finite comparisons. Prime logarithms are
formal coefficient dictionaries; no floating sign decision is used.

Both scripts use only the Python standard library. Run:

```sh
python3 papers/prime-variance-exponents/numerics/01_signed_arithmetic_covariance/check_prime_discrepancy_centering.py
python3 papers/prime-variance-exponents/numerics/01_signed_arithmetic_covariance/check_smooth_sign_obstruction.py
```

Each accepts `--output PATH` for a small JSON record and reports its source
hash. The analytic derivative bounds, kernel-lobe existence and PNT box
asymptotics are proved in the associated notes; these finite checks do
not certify their constants or asymptotic onset. See the
[investigation summary](../../notes/programs/01_signed_arithmetic_covariance/ONE_SIDED_ARITHMETIC_ATTEMPT_20261004.md)
and [internal review](../../reviews/01_signed_arithmetic_covariance/ONE_SIDED_ATTEMPT_REVIEW_20261004.md).
