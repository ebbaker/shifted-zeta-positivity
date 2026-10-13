# Arithmetic source audit numerics

12 October 2026. Prepared for Edward Baker using GPT-6-astra (Codex;
`gpt-6-astra`), reasoning effort **ultra**, with substantial LLM assistance.

Place reproducible scripts, parameter records, and small certificates here.
Record software versions, precision, error bounds, and what each check
establishes. Keep large regenerable output outside Git with stored-file and
content hashes and a documented lookup, following
[LARGE_FILES.md](../../../../../LARGE_FILES.md).
See the [project scope](../README.md).

## Exact transfer regrouping

[check_transfer_regrouping.py](check_transfer_regrouping.py) enumerates the
signed preimages in the second Poisson transfer using three distinct
primary Eisenstein primes of norms 7, 13, and 19. It checks common column
scales, Fourier parameters, normalization, exclusion removal, and strict
row decrease with exact integers and rational numbers. A negative control
shows why taking absolute values before the signed regrouping can leave
an inadmissible column scale.

From the repository root:

```sh
python3 papers/investigations-2/inactive/arithmetic_source_audit/numerics/check_transfer_regrouping.py
```

The default output is [the small replay record](transfer_regrouping_record_20261012.json).
Use `--output /path/to/replay.json` to leave the saved record unchanged.
Optionally pass `--source /path/to/paper2.tex`; the script then refuses a
source whose SHA-256 differs from the [pinned provenance](../notes/source_provenance_20261012.json).
The immutable download URL is in that record. No third-party source file
is required for the finite arithmetic checks themselves.

The script uses only the Python standard library. Its record includes the
checker and source hashes, Python version, exact parameters, case counts,
and limitations. These are finite identity and support checks; they do not
evaluate Gauss sums, prove Poisson or theta identities, verify derivative
estimates, or validate the unbounded induction. The analytic argument and
assumptions are in the [branch ledger](../notes/CUBE_TAIL_BRANCH_AUDIT_20261012.md)
and [scoped review](../reviews/FIRST_BRANCH_REVIEW_20261012.md).

## Theta version comparison and reused checks

The [theta version record](theta_version_crosswalk_record_20261012.json)
pins both manuscripts at the same repository revision and confirms that
the September 30 PDF matches the artifact used in the earlier audit.
The source-formula correspondence is a mathematical read-through,
documented in the [theta review](../reviews/THETA_TRANSFORMATION_REVIEW_20261012.md).
It is not an automated assertion that the two source texts are identical.

The existing upstream checker was replayed unchanged, without overwriting
its historical record:

```sh
python3 papers/quasi-rh-character-amplification/numerics/check_upstream_reflection_interfaces.py --output /tmp/theta-interface-replay.json
```

All 69,881 assertions passed and the result agrees with the saved
historical JSON. The suite also contains primitive-Poisson checks; the
total is not a new count of theta obligations. It checks finite local
Fourier identities, cusp congruences and additive CRT phases. It does
not evaluate the global cubic multiplier, prove automorphy or reciprocity,
or establish the analytic kernel estimates. Those calculations are in
the new proof notes, under their stated imports.

The legacy checker records a fixed historical PDF hash without reading
the PDF. This audit separately downloaded and hashed the pinned artifact;
the new version record distinguishes that verification from the replay.
It records both source hashes, the checker hash, the replay result hash,
and the exact finite coverage.


## Initial arithmetic and Poisson bookkeeping

The new [check_initial_arithmetic.py](check_initial_arithmetic.py) is a
standalone standard-library diagnostic. It tests the exact shared-column
Möbius cancellation, the mask-preserving change of variables with
`e=gcd(f,k)`, norm identities, the full primary ray group modulo 12,
and exact cubic Jacobi sums. It also directly evaluates finite Gauss
sums across six split and two inert primes and 28 distinct prime pairs.
Those ordinary floating calculations are not interval certificates.

From the repository root:

```sh
python3 papers/investigations-2/inactive/arithmetic_source_audit/numerics/check_initial_arithmetic.py --output /tmp/initial-arithmetic-replay.json
```

No third-party file is needed for the finite checks. To verify the source
version as well, add `--source /path/to/paper2.tex`, using the immutable
URL and SHA-256 in [the provenance record](../notes/source_provenance_20261012.json).
A mismatched supplied file is rejected before computations or output.
A run without a source explicitly sets `source_hash_verified` to false.
The default output is [initial_arithmetic_record_20261012.json](initial_arithmetic_record_20261012.json);
use `--output` for a replay that preserves the saved record.

The saved verified-source run passes 113,748 exact assertions and 19,868
floating comparisons at tolerance `1e-10`; maximum observed absolute error
is about `4.092e-15`. Twelve negative-control families detect omitted
signs, masks, coprimality restrictions, and a reversed conjugation.
The record identifies Python, script hash, pinned source hash, and all
coverage counts. The exact count includes repeated checks inside finite
enumerations, not distinct proof obligations. No claim of bit-identical
floating portability is made.

The checker does not prove analytic Poisson, the bandlimited majorant,
smooth norms, asymptotic estimates, or general reciprocity. Arbitrary
fixed Hecke twists are handled by the algebraic character expansion, while
the paired numerical tests use the trivial original twist. The analytic
argument and its conditions are in [the combined review](../reviews/INITIAL_POISSON_AND_ARITHMETIC_REVIEW_20261012.md)
and its linked derivations.

## Completed mean-square bookkeeping

[check_completed_bookkeeping.py](check_completed_bookkeeping.py) is a
standalone standard-library diagnostic of the exceptional local branches,
conductor ledger, and general-row reduction in `prop:R`.
This continuation used GPT-6 (Codex); its exact serving variant and
configured effort are not exposed and are not inferred.

From the repository root:

```sh
python3 papers/investigations-2/inactive/arithmetic_source_audit/numerics/check_completed_bookkeeping.py --output /tmp/completed-bookkeeping-replay.json
```

No third-party file is needed for the finite checks. Add
`--source /path/to/paper2.tex` to verify the source version using the
immutable URL and SHA-256 in [the provenance record](../notes/source_provenance_20261012.json).
A supplied file with a mismatched hash is rejected before arithmetic or
output, with exit status 2. A run without a source explicitly records
`source_hash_verified=false`. The default output is
[completed_bookkeeping_record_20261012.json](completed_bookkeeping_record_20261012.json);
use `--output` to preserve the saved record during replay.

The saved verified-source run uses CPython 3.10.0 and passes 198,323 exact
assertions, with zero floating comparisons and eleven negative-control
families. Coverage includes 7,776 actual Eisenstein elements with shared
squarefree/square factors and character zeros, 40 exact local collision
sums, every local branch at valuations through 18, simultaneous
three-prime products, polynomial length bounds, and the exact inverse-square
normalization. The local tests use rational arithmetic or
`Q(sqrt(q))`; square norms are reduced to canonical rational form.
Counts include repeated enumerations rather than distinct theorem
validations. The records identify the script and pinned source hashes,
software version, finite coverage, and limitations.

The [CLI validation record](completed_bookkeeping_cli_validation_20261012.json)
also confirms source-mismatch rejection without output and a successful
portable run without a source file. The mathematical arguments and
imported inputs are in [the completed mean-square review](../reviews/COMPLETED_MEAN_SQUARE_REVIEW_20261012.md)
and its linked notes. The checker does not prove the theta transformation,
moving-prime uniformity, coefficient or weight bounds, the quadratic large
sieve, infinite summation, or an unbounded mean-square estimate.

## Full two Poisson transfer bookkeeping

[check_full_transfer_bookkeeping.py](check_full_transfer_bookkeeping.py)
extends the earlier regrouping diagnostic to all sampled local
placements, actual Eisenstein row elements, character zeros, first-map
fibers, returned children, short ranges, and finite descent bookkeeping.
It uses only the Python standard library. This continuation used GPT-6
(Codex); the exact serving variant and configured effort are not exposed
and are not inferred.

From the repository root:

```sh
python3 papers/investigations-2/inactive/arithmetic_source_audit/numerics/check_full_transfer_bookkeeping.py --output /tmp/full-transfer-replay.json
```

No third-party file is needed for the finite arithmetic. Add
`--source /path/to/paper2.tex` to verify the pinned source version,
using the immutable URL and SHA-256 in
[the provenance record](../notes/source_provenance_20261012.json).
A supplied source with a mismatched hash is rejected before arithmetic
or output, with exit status 2. Without a supplied source, the record
explicitly sets `source_hash_verified=false`.
The default output is
[full_transfer_bookkeeping_record_20261012.json](full_transfer_bookkeeping_record_20261012.json);
use `--output` during replay to preserve the saved record.

The verified-source run uses CPython 3.10.0 and passes 4,186,781 exact
assertions, zero floating comparisons, and eleven negative-control
families. Coverage includes:

- 62,208 signed regrouping cases and 438,012 actual preimages over primes
  of norms 7, 13, and 19, with row valuations 0–3, ramified valuations
  0/1/3, norm-4 prime valuations 0/2, and all six units. Independent
  forward/inverse local enumeration covers valuations through six.
- Exact sextic character masks at residue-field norms 7, 13, 19, and 25,
  including zero values; first-map fibers through valuation six; common
  prefactors, individual lengths, and Fourier parameters.
- 271 retained scale cases, 309 divisor-shifted children, and 1,311
  eligible cube-tail parameter cases. These test necessary ranges and
  contraction, rather than nonzero Möbius coefficients or actual kernels.
- An admitted positive-form example with intermediate scale \(Y=32/49\),
  its unit column, the zero lattice row, short columns, the unit cube
  for a cutoff below one, and composition of derivative orders.

Arithmetic uses exact integers, ring pairs, residue-field exponents,
and `fractions.Fraction`. Assertion totals include repeated checks,
not independent theorem validations. Negative controls detect premature
absolute values, incorrectly retained first-stage signs, omitted
character masks, invalid assumptions on short scales, lost normalization,
and incorrect derivative-order composition.

The [CLI validation record](full_transfer_bookkeeping_cli_validation_20261012.json)
also confirms source-mismatch rejection with no output and successful
portable execution without a source file. The main record identifies
the source and script hashes, software version, parameters, finite
coverage and limitations. The inverse/norm formulas adapt
[check_transfer_regrouping.py](check_transfer_regrouping.py); the new
forward enumeration and extended checks do not turn that adaptation
into an independent proof.

The checker evaluates no Gauss sum, theta sum, or actual smooth Fourier
kernel. It does not establish analytic Poisson, unbounded divisor
estimates, smooth derivative norms, the transfer inequality, the
canonical estimate, or quasi-RH. The analytic arguments and their inputs
are in [the full transfer review](../reviews/TWO_POISSON_TRANSFER_REVIEW_20261012.md)
and its three linked derivations.

## Final assembly bookkeeping

[check_final_assembly.py](check_final_assembly.py) is a compact
standard-library diagnostic of the last normalization, exponent,
scale-boundary and Euler-factor calculations. This continuation used
GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

From the repository root:

```sh
python3 papers/investigations-2/inactive/arithmetic_source_audit/numerics/check_final_assembly.py --output /tmp/final-assembly-replay.json
```

No third-party file is needed. Add
`--source /path/to/paper2.tex` to verify the pinned source,
using the immutable URL and SHA-256 in
[the provenance record](../notes/source_provenance_20261012.json).
A mismatched supplied source is rejected before diagnostic arithmetic
or output, with exit status 2. A run without a source explicitly records
`source_hash_verified=false`. The default output is
[final_assembly_record_20261012.json](final_assembly_record_20261012.json);
use the output option for a replay that preserves the saved record.

The saved verified-source run uses CPython 3.10.0 and passes **622 exact
assertions**, **zero floating comparisons**, and **thirteen negative-control
families**. Coverage includes seven explicit rational final-loss choices,
twelve fixed-constant large-D thresholds, 81 initial scale combinations,
a divisor shift below column length one, all sixth roots and the character
zero, and formal split/inert/ramified Euler polynomials. A separate
finite series inversion checks those polynomials through degree six.
The norm-7 sixth-power boundary is exact norm algebra; the checker does
not enumerate actual prime ideals or evaluate their characters.

Negative controls detect omission of the outside D or b-shell count,
incorrect sixth-root scaling, erased character zeros, overspent losses,
substitution of theta zero into a positive-gap theorem, dropping a fixed
constant before the large-D threshold, treating every shifted length as
at least one, the missing inert character square, and erased ramified or
imprimitive corrections. The explicit quadratic norm-lift example at
three shows why the source's finite-Euler-factor qualification is needed.
Counts include repeated arithmetic checks rather than independent theorem
validations.

The [CLI validation record](final_assembly_cli_validation_20261012.json)
confirms mismatch rejection with no output and portable execution without
a supplied source. The main record identifies the script and source
hashes, software version, exact finite coverage, and limitations.

These checks do not establish prime-ideal counting, a mean-square or
canonical estimate, smooth-kernel nonvanishing, analytic Poisson, theta
automorphy, the quadratic large sieve, Mellin holomorphy, Hecke
continuation, or quasi-RH. They supply no uniform quantitative estimates
as a character conductor or alleged zero's height varies. The analytical
ledger, imported facts and scoped decision are in
[the final assembly review](../reviews/FINAL_ASSEMBLY_REVIEW_20261012.md)
and its three linked notes.
