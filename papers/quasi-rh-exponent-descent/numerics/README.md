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

## Centered short-family factorization

Run [check_short_family_factorization.py](check_short_family_factorization.py)
with Python 3.10 or later. It uses exact standard-library arithmetic,
prints a deterministic small JSON record, and writes no files. The
[retained record](short_family_factorization_record_20261008.json) lists
the 24,245 exact assertions across 33 groups. Two coordinating runs
reproduced the record byte-for-byte.

The checks cover truncated ideal-style convolution and its endpoint,
complex completely multiplicative twists with deletion zeros,
nonsquarefree cancellation, principal centering algebra, signed gcd
recombination, Euler deletion identities, divisor-mean algebra, and
rational completion, truncation and core-cutoff budgets. Their
scope is finite algebra and exponent bookkeeping. They do not prove
number-field reciprocity, Poisson summation, prime ideal counting,
the imported large sieve, or the missing recombined moment.

See the [continuation](../short_families/notes/10_SHORT_FAMILY_FACTORIZATION_CONTINUATION_20261008.md)
and [scoped review](../reviews/SHORT_FAMILY_FACTORIZATION_REVIEW_20261008.md).

## Zero-integral adaptive short families

Run [check_short_family_mean_zero.py](check_short_family_mean_zero.py)
with Python 3.10 or later. It uses exact standard-library arithmetic,
prints deterministic JSON and writes no files. Two fresh coordinating
runs reproduced the 3,144-byte
[record](short_family_mean_zero_record_20261008.json) byte-for-byte:
4,812 assertions across 28 groups passed.

The checks cover the zero-integral derivative profile, Mellin and
logarithmic integral identities, finite scalar differentiation,
complex adaptive convolution with deletion zeros, an empty cutoff,
the local conductor/mask partition, finite radical-weight geometric
factors including the divisor weight, and rational support and
generic bilinear exponents. The polynomial profile is a finite
calculus diagnostic; it is not a smooth analytic test profile.
Formal monoid twists are not actual residue symbols.

Infinite Euler convergence, primitive Poisson, the quantitative prime
ideal theorem, the imported sextic sieve, and the new adaptive signed
moment are outside the finite checks. See the
[continuation](../short_families/notes/13_SHORT_FAMILY_ADAPTIVE_CONTINUATION_20261008.md)
and [scoped review](../reviews/SHORT_FAMILY_MEAN_ZERO_REVIEW_20261008.md).

## Ideal discrepancy and signed packets

These standalone standard-library scripts print deterministic JSON and write
no files. Two fresh runs reproduced each retained record byte-for-byte.

| Script and record | Finite checks | Scope |
| --- | --- | --- |
| [check_short_family_ideal_discrepancy.py](check_short_family_ideal_discrepancy.py), [record](short_family_ideal_discrepancy_record_20261008.json) | 638 named equalities | Formal logarithmic convolution, complex discrepancy integrals, complete Riesz edge closure and centered Stieltjes endpoints |
| [check_short_family_divisor_packets.py](check_short_family_divisor_packets.py), [record](short_family_divisor_packet_record_20261008.json) | 3,982 assertions in 22 groups | Tuple/product recombination, nonsquarefree packets, masks, strict cutoffs and actual split-prime local sextic symbols |
| [check_short_family_product_barrier.py](check_short_family_product_barrier.py), [record](short_family_product_barrier_record_20261008.json) | 182 assertions in ten groups | Product coefficients, continuum series and partial fractions, polynomial derivative moments and rational exponents |

The actual local packet uses a good-radical proxy rather than a computation
of the primitive combined conductor. It tests the pointwise packet theorem,
not membership in its asymptotic growing-cofactor range. The polynomial bump
is a finite calculus diagnostic, not a smooth analytic test profile.
These checks do not verify reciprocity, conductor comparison, Poisson,
prime ideal asymptotics, the all-profile density argument, or a signed moment.
See the [milestone](../short_families/notes/15_SHORT_FAMILY_DIVISOR_PACKET_CANCELLATION_20261008.md)
and [scoped review](../reviews/SHORT_FAMILY_SIGNED_PACKET_REVIEW_20261008.md).

## Squarefree reduction and further compensation

Each standard-library script prints deterministic JSON and writes no files.
Two fresh coordinating runs reproduced each retained record byte-for-byte.

| Script and record | Finite checks | Scope |
| --- | --- | --- |
| [check_short_family_squarefree_projection.py](check_short_family_squarefree_projection.py), [record](short_family_squarefree_projection_record_20261008.json) | 594,360 exact assertions | Equal-norm distinct ideal symbols, projection signs, overlaps, sixth-root phases and zeros, strict cutoffs, sixth-power sparsity and fixed binary prefixes |
| [check_short_family_cofactor_compensation.py](check_short_family_cofactor_compensation.py), [record](short_family_cofactor_compensation_record_20261008.json) | 18,442 exact assertions | Cofactor inversion, bounded selectors, adaptive split, complex phases, endpoints and asymmetric factorization |
| [check_short_family_edge_compensation.py](check_short_family_edge_compensation.py), [record](short_family_edge_compensation_record_20261008.json) | Five packets, 52 triple terms, 208 phase/deletion checks and 24 rational-log cases | All four logarithmic edges, nonsquarefree cofactors, weak endpoints and the unit exception |

These finite monoid models do not validate reciprocity, primitive conductors,
Poisson, infinite Euler convergence, asymptotic sparse ideal counts, prime
ideal counting, the imported sieve or any unbounded signed moment. See the
[main proof](../short_families/notes/17_SHORT_FAMILY_SQUAREFREE_TAIL_REDUCTION_20261008.md)
and [scoped review](../reviews/SHORT_FAMILY_SQUAREFREE_AND_COFACTOR_REVIEW_20261008.md).
