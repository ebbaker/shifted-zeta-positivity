# Numerical programs and diagnostic records

All numerical material for this attempt lives here. The four manuscript programs
need Python 3 and NumPy. They generate their own inputs and require no data
download, external working note, zero database, or target spectral factor.
The manuscript's Section 14 describes the methods and their evidentiary limits.

| Program | Retained record | Main checks |
| --- | --- | --- |
| [check_relative_and_delay_models.py](check_relative_and_delay_models.py) | [supplied-model-diagnostics.json](records/supplied-model-diagnostics.json) | Relative harmonic projection and exterior energy; finite toy complex; exact integer delays; true logarithmic delays; derivative controls; comparison models |
| [check_finite_coupling.py](check_finite_coupling.py) | [finite-coupling-diagnostics.json](records/finite-coupling-diagnostics.json) | Scalar coefficients, gamma-series controls, exact finite coupling versus the tangent |
| [check_loop_evolution.py](check_loop_evolution.py) | [loop-evolution-diagnostics.json](records/loop-evolution-diagnostics.json) | Prime coefficients, full compact-input pairing, evolution identity, cutoff and rational controls |
| [check_field_mixing.py](check_field_mixing.py) | [field-mixing-diagnostics.json](records/field-mixing-diagnostics.json) | Exact rational coefficients; independent field elimination; derivative penalty; high-frequency packets; modified compact-input response |

The toy matrix eigensystem in the first program is a check of a small explicitly
given relative complex. It is not a factorization of the Weil form.

## Replay the four manuscript calculations

```sh
python3 -m pip install -r numerics/requirements.txt
python3 numerics/replay.py --output-dir /tmp/topological-susy-bulk-replay
```

Run from the attempt root. The output directory must be outside this attempt;
this protects the small historical records and keeps derived outputs out of
the repository. It receives four JSON outputs, logs, and `replay-summary.json`.
No output is fetched from or written into another project folder.

The replay checks every scientific field against the retained JSON, with
absolute tolerance `5e-9` plus relative tolerance `5e-8`. Environment metadata
are reported separately. Key sets, list lengths, text, booleans, and integers
must agree exactly. The unchanged loop and field programs must also match
their historical source hashes. Additional checks enforce the loop identity
and coefficient thresholds, the field elimination error threshold, and the
field program's refusal to run with assertions disabled. The programs' own
internal checks also remain active.

These tolerances test reproduction, not mathematical error bounds. Exact
`Fraction` algebra in the field program establishes only the displayed finite
rational identities. Floating-point quadrature, frequency truncation, and
packet asymptotics are not interval certificates. A matching replay is not an
independent mathematical proof.

The delivered replay was run with Python 3.12 and NumPy 2.3.5; full version
strings and hashes are in [records/manuscript-replay.json](records/manuscript-replay.json).
The runner limits common BLAS/OpenMP thread pools to one thread per program
for a predictable local workload. Cross-platform bitwise equality is not
required.

## Individual commands

```sh
python3 numerics/check_relative_and_delay_models.py --output /tmp/relative-models.json
python3 numerics/check_finite_coupling.py --output /tmp/finite-coupling.json
python3 numerics/check_loop_evolution.py --output /tmp/loop-evolution.json
python3 numerics/check_field_mixing.py --output /tmp/field-mixing.json
```

Do not run the field checker with `-O`; it explicitly rejects disabled assertions.

## Preserved and adapted material

The loop and field scripts and all five pre-existing diagnostic JSON files were
moved without changing their bytes. Both
[loop-evolution-replay.json](records/loop-evolution-replay.json) and the original
loop record are retained, even though they are byte-identical. The old
finite-coupling program is frozen in
[archive/check_finite_coupling_before_cli.py](archive/check_finite_coupling_before_cli.py);
the current version changes only output argument handling. The relative/delay
generator is now present locally; only its opening explanatory docstring was
adapted when it was incorporated. See the
[relocation and provenance record](../REORGANIZATION_20260912.json).

## Quantum covariance follow-up, 13 September 2026

The separate [quantum ground-state investigation](../archive/notes/QUANTUM_GROUND_STATE_CORRELATIONS_20260913.md)
adds [check_quantum_covariance.py](check_quantum_covariance.py). Run it with:

```sh
python3 numerics/check_quantum_covariance.py --output /tmp/quantum-covariance-check.json
```

Run this command from the investigation root. The delivered record is
[quantum-covariance-diagnostics.json](records/quantum-covariance-diagnostics.json).
The program uses NumPy, standard-library rational arithmetic, and Decimal.
It verifies exact cancellation and positivity polynomials, a shifted moment
obstruction, the normal-mode vacuum covariances of the two- and three-field
models, and their high-frequency residuals. The arithmetic certificates are
exact; the floating-point and Decimal checks are not interval enclosures.
This program is separate from the four historical replay jobs described above.

## Covariance audit and larger blocks, 13 September 2026

The [independent audit and finite-block obstruction](../archive/notes/QUANTUM_COVARIANCE_AUDIT_AND_FINITE_BLOCK_OBSTRUCTION_20260913.md)
adds [check_quantum_block_obstruction.py](check_quantum_block_obstruction.py).
Run from the investigation root:

    python3 numerics/check_quantum_block_obstruction.py --output /tmp/quantum-block-check.json
    python3 validation/check_package.py

The checker needs only Python 3 and NumPy. It replays the preceding quantum
program in a temporary directory, derives gamma coefficients independently
from the short-distance kernel, and recomputes the earlier Gram determinants.
It lists complete exact rational moment matrices and determinant sign
certificates for one through four replaced channels, verifies the general
annihilator identity in those cases, constructs the new Jacobi models, and
compares their entire response with quantum normal modes and classical
minimization. Conservative negative odd-moment certificates support the
separate interval obstruction proof in the note.

The delivered [diagnostic record](records/quantum-block-obstruction-diagnostics-20260913.json)
and [audit validation record](records/quantum-block-audit-validation-20260913.json)
are new; historical files are preserved. Rational identities and polynomial
coefficient signs are exact. Normal-mode comparisons are floating-point
diagnostics, and replay is not independent proof of the analytic claims.
The all-finite-block and interval conclusions are proved in the note; this
calculation establishes no norm estimate or positivity of the complete Weil
operator. It remains separate from the four historical manuscript replay jobs.

## Superspace boundary pairing, 13 September 2026

The [superspace action and preparation note](../archive/notes/SUPERSPACE_RELATIVE_BOUNDARY_ACTION_20260913.md)
adds [check_superspace_boundary_pairing.py](check_superspace_boundary_pairing.py).
Run from the investigation root with Python 3.10 or later and NumPy:

    python3 numerics/check_superspace_boundary_pairing.py --output /tmp/superspace-boundary-check.json
    python3 validation/check_package.py

The [delivered diagnostics](records/superspace-boundary-pairing-diagnostics-20260913.json)
use exact rational polynomial and Grassmann algebra for the superspace
component action, kinetic and endpoint invariance, and projection variation.
Canonical Fock matrices on complete invariant excitation sectors check both
charge anticommutators. Heat kernels check complex boundary pairings, gluing,
the protected Ward identity, and the nonzero variation of a raw insertion.
First-prime matrices check the change of the harmonic source projection.
Tower sums sample the uniform analytic preparation bound.
Common-rate sums also check the logarithmic cutoff divergence and the
alternative of increasing preparation time as the number of channels grows.

Floating-point checks are diagnostics, not interval enclosures. The general
domain, convergence, Ward, and residual statements are proved in the note.
The [validation record](records/superspace-boundary-validation-20260913.json)
also records preservation of the earlier package, brainstorming material,
and background. These additions leave every preceding diagnostic and the
four historical manuscript replay jobs unchanged.
