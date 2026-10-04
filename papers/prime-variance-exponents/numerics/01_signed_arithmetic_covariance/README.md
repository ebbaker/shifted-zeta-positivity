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


## Aggregated kernel and signed divisor localization

[check_aggregated_kernel.py](check_aggregated_kernel.py) imports the exact
polynomial kernel and arithmetic helpers from the adjacent centering checker.
It tests global aggregate/divisor identities including the singleton term,
a signed divisor split, Stieltjes integration on partial intervals with prime
and noninteger endpoints, centering E by E(U), and the terminal Möbius-shell
identity. All calculations use exact fractions and synthetic prime atom
weights p. Run:

```sh
python3 papers/prime-variance-exponents/numerics/01_signed_arithmetic_covariance/check_aggregated_kernel.py
```

The [record](aggregated_kernel_record_20261004.json) contains 1,279 exact
comparisons across 28 cases, with source hashes for both the checker and its
shared kernel module. It detects 277 instances where endpoint deletion
changes a tested expression, 15 cases where using the terminal identity
globally fails, and 28 nonzero singleton controls outside its deletion range.
Counts of controls are diagnostic instances, not independent asymptotic tests.
The script accepts `--output PATH`. No large arrays or derived sweeps are saved.

See the [research continuation](../../notes/programs/01_signed_arithmetic_covariance/AGGREGATED_KERNEL_CONTINUATION_20261004.md)
and [review](../../reviews/01_signed_arithmetic_covariance/AGGREGATED_KERNEL_REVIEW_20261004.md).
The Poisson derivative constants, mixed Mellin moments and residue arguments
are analytic deductions reviewed separately; the checker does not certify
those statements or any fixed-power estimate.


## Localized target and finite spectrum continuation

[check_localized_target.py](check_localized_target.py) checks the cofactor
identity underlying the spectral representation, exact mu/von-Mangoldt
coefficient closure, additive smoothing with zero-extended band endpoints,
centered covariance, shifted autocorrelation, and a synthetic triple
integration-by-parts identity. Run:

```sh
python3 papers/prime-variance-exponents/numerics/01_signed_arithmetic_covariance/check_localized_target.py
```

The [record](localized_target_record_20261004.json) reports 2,592 exact
comparisons and source hashes for the new checker and both shared kernel
modules. Formal prime logarithms are coefficient dictionaries; the kernel
checks use rational polynomial data and synthetic prime weights p. The
primitive tests use R(v)=v^8, not the fixed probe. Negative controls expose
38 missing low/low terms, 18 omitted shifted endpoint residuals, and 16
incorrect primitive coefficients. The script accepts `--output PATH`.

The [analytic note](../../notes/programs/01_signed_arithmetic_covariance/FINITE_CROSS_SPECTRUM_20261004.md)
and [review](../../reviews/01_signed_arithmetic_covariance/LOCALIZED_TARGET_ATTEMPT_REVIEW_20261004.md)
separate these finite checks from the Fourier inversion, spectral-tail
bound, mode estimate, and unproved central arithmetic inequality. No
asymptotic exponent fit or large numerical sweep is included.
