# Exact checks and collision reconnaissance

Prepared for Edward Baker, 8 October 2026, with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred.

Run `python3 check_initial_identities.py` with Python 3.10 or later; no
third-party packages are required. It writes the small
[retained record](initial_identity_record_20261008.json).

The checks use exact rational arithmetic for the positive-kernel polynomial
and its positivity and monotonicity identities, the off-real quartic roots,
three cases of the fixed-scale geometric iteration, the factor-scale
logarithmic counterexample, and the scalar remainder exponents. Analytic
convergence, the Bessel argument, heat-flow
theorems, and actual-prime estimates are outside the script's scope.

The script and record are small. No zero cache, external PDF, or large
derived dataset is stored here. Follow [LARGE_FILES.md](../../../LARGE_FILES.md)
if later experiments require large outputs.

## Second continuation

Run these from this directory with Python 3.10 or later. They use only
the standard library.

| Script | Scope | Output behavior |
| --- | --- | --- |
| [check_mixed_conductor_refinement.py](check_mixed_conductor_refinement.py) | Exact rational intervals and automatic differentiation cover 1,024 closed cells; checks buffered cutoff extrema and the new plain-conductor sector | Prints JSON; saved as [mixed_conductor_refinement_certificate_20261008.json](mixed_conductor_refinement_certificate_20261008.json) |
| [check_short_family_refinement.py](check_short_family_refinement.py) | Five exact rational extraction chains and twelve finite prime-mask identities | Writes [short_family_refinement_check.json](short_family_refinement_check.json) |
| [check_integer_quadratic_lift.py](check_integer_quadratic_lift.py) | 51,657 integer Jacobi-mask comparisons, exact root counts, prime-power deletion, Gram/grouping identities and rational exponents | Writes [integer_quadratic_lift_record_20261008.json](integer_quadratic_lift_record_20261008.json) |
| [zeta_collision_arithmetic_check.py](zeta_collision_arithmetic_check.py) | Floating Simpson quadrature, panel doubling, and evaluations of analytic tail formulas; no interval quadrature enclosure or rectangle certification | Prints JSON; saved as [zeta_collision_arithmetic_record_20261008.json](zeta_collision_arithmetic_record_20261008.json) |

To compare a stdout record without overwriting it, redirect the script to
a temporary file and compare that file with the saved JSON. The rational
certificates support the finite algebra only. The collision record is
reconnaissance, including its numerical evaluations of proved tail formulas.
None supplies a new asymptotic arithmetic moment or all-height conclusion.

See the [results summary](../notes/SECOND_CONTINUATION_RESULTS_20261008.md)
for the mathematical deductions and their separate scoped reviews.

## Third continuation

These standard-library checks use Python 3.10 or later. Their records remain
small; none evaluates the missing asymptotic signed moments.

| Script | Scope | Output behavior |
| --- | --- | --- |
| [check_short_family_small_cofactor.py](check_short_family_small_cofactor.py) | 51,040 local ratio/mask checks, 56 complete-period sums, and exact second-Poisson and residual exponent identities | Writes [short_family_small_cofactor_check.json](short_family_small_cofactor_check.json) |
| [check_selected_inverse_distribution.py](check_selected_inverse_distribution.py) | 819 finite-field Gauss sums over orders 3, 9 and 27; 504 local sextic phase/mask checks; exact frame identities; continuous rational repeated-character margin on 1,024 cells | Prints JSON; saved as [selected_inverse_distribution_certificate_20261008.json](selected_inverse_distribution_certificate_20261008.json) |
| [check_quadratic_moment_barrier.py](check_quadratic_moment_barrier.py) | 13,065 exact masked coefficient identities, a canceled-prime counterexample, positive-Gram identities and rational envelope budgets | Writes [quadratic_moment_barrier_record_20261008.json](quadratic_moment_barrier_record_20261008.json) |
| [check_normalized_heat_constants.py](check_normalized_heat_constants.py) | Exact rational implications of the final analytic heat bounds; no floating heat values, disk enclosure computation or compact rectangle certificate | Prints JSON; saved as [normalized_heat_constant_record_20261008.json](normalized_heat_constant_record_20261008.json) |

The [third results note](../notes/THIRD_CONTINUATION_RESULTS_20261008.md)
states the analytic deductions and links the scoped reviews. In particular,
the effective large-height conclusion is proved analytically from the
imported approximation theorem; its rational constant script alone does
not prove that conclusion.

## Focused short-family continuation

Run [check_short_family_continuation.py](check_short_family_continuation.py)
with Python 3.10 or later. It prints JSON and writes no files. The retained
[record](short_family_continuation_record_20261008.json) contains 9,356
passing exact assertions and replays byte-for-byte.

The checks cover rational block budgets and inherited family exponents,
324 rational heights for the generic sieve comparison, 780 complex weight
vectors, a nonconstant Eisenstein angular-phase witness, and exact finite
Gauss/Fourier identities over the fields of sizes 7, 13, and 19. Complex
profiles and nonreal characters detect the wrong conjugation orientations.
All arithmetic uses fractions and finite cyclotomic polynomial rings;
there is no floating-point tolerance.

These checks certify only the displayed finite identities and exponent
bookkeeping. They do not prove the number-field Poisson formula, the
imported sextic large sieve, the prime ideal theorem, or the missing
asymptotic signed estimate. See the
[continuation](../short_families/notes/7_SHORT_FAMILY_CONTINUATION_20261008.md) and
[scoped review](../reviews/SHORT_FAMILY_CORE_AND_OVERLAP_REVIEW_20261008.md).
