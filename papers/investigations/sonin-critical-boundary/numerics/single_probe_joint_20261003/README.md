# Joint translated-probe Gram certificate

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and effort not exposed to this agent.
Internal same-model audit, not independent specialist refereeing.

## Preflight recorded before the package runs

This bounded continuation uses the same exact polynomial source as
`../all_window_mechanism_20261003/certify_translated_probe.py`, seven translates
at 0, 2, 4, 6, 8, 10, 12, and only the six positive differences 2,4,6,8,10,12.
The source support width is 1/2, so the entire source span fits in width 25/2.
The maximum prime-power cutoff remains 268338; the new difference 2 adds
only five nonzero prime-power terms. No larger-window full-source certificate
or separation sweep is attempted.

Budget: sieve limit <=300000; six scalar differences; a 7x7 real symmetric
Toeplitz matrix; two runs, at 192 and 256 bits; at most 60 seconds per run;
no floating eigenvalues, bisection, or adaptive searches. The predetermined
certificate margin is the exact rational 1/20. An exploratory preliminary
check established feasibility before this package was prepared. All
archimedean off-diagonal remainders are retained as symmetric outward balls.

The exact polynomial and source norm are regenerated from the previous
package. The diagonal uses its same validated integration with the removable
origin resolved analytically. The prime sums include every prime power.
An interval LDL factorization of G-(1/20)I must have seven strictly positive
pivot enclosures. Failure at any stage causes a nonzero exit; no approximate
matrix positivity can decide the result.

## Reproduce

The base script is located relative to this package by default. Its SHA-256
is pinned in the extension; any mismatch stops execution. An alternate
`--base-script` path is available only to locate that same hash-bound source.

```sh
python3 -B certify_joint_gram.py --bits 192 --output /tmp/joint_192.json
python3 -B certify_joint_gram.py --bits 256 --output /tmp/joint_256.json
python3 -B replay_check.py --first /tmp/joint_192.json --second /tmp/joint_256.json --output /tmp/joint_replay.json
```

Dependencies: Python with python-flint. The originating environment used
Python 3.10.0, python-flint 0.9.0, FLINT 3.6.0; its temporary dependency path
is not a required repository location.

## Recorded result

Both [192-bit](joint_192.json) and [256-bit](joint_256.json) runs pass
in about 0.3 seconds. The [replay record](joint_replay.json) verifies
source bindings, exact pivot signs, invariant data, and interval overlap.
The smallest lower endpoint among the seven shifted LDL pivots exceeds
0.01286159. This pivot value is not itself an eigenvalue bound; the proved
eigenvalue lower bound is the predetermined shift 1/20.

For comparison, the elementary Gershgorin bound
`min_i (G_ii-sum_(j!=i)|G_ij|)` is enclosed between -1.511672 and
-1.495987. Thus this row-sum test cannot prove positivity even for this
matrix, while the signed joint factorization succeeds. A negative
Gershgorin bound does not imply a negative eigenvalue.

The [single-probe theorem](../../notes/SINGLE_PROBE_GROWTH_THEOREM_20261003.md)
identifies the global analytic obligation for the same polynomial probe.
The [review](../../reviews/ALL_WINDOW_OUTCOME_REVIEW_AND_CONTINUATION_20261003.md)
states how the finite joint check and that theorem differ in scope.

## Meaning of the certificate

For the exact normalized source g from the base package and arbitrary complex
coefficients a_0,...,a_6, this certifies

    Q[sum_(j=0)^6 a_j tau_(2j) g] > (1/20) sum_(j=0)^6 |a_j|^2

when the coefficient vector is nonzero. The translates are disjoint and
orthonormal in L2, so this is also a form lower bound on this specific
seven-dimensional source subspace. Positive pivots for a real symmetric
matrix prove its Hermitian inequality for complex coefficients as well.

Each interval LDL operation encloses its exact counterpart for the actual
Gram matrix. Forgetting the shared Toeplitz-entry dependencies only widens
the enclosures, so it does not weaken the validity of the positive result.
The records store the six signed prime sums, all gamma remainder bounds,
the complete first row of the Toeplitz matrix, and the seven LDL pivots as
exact rational interval endpoints.

This checks an actual joint signed covariance matrix rather than only its
2x2 principal blocks. It does not prove the desired inequality on all sources
of width 25/2, all translates of this probe, a complete probe family, or any
unbounded sequence of windows. The source is C4 and lies in the logarithmic
form closure; preparation and all three moments hold exactly.

## Independent matrix algebra audit

The standard-library [rational interval audit](audit_joint_saved_matrix.py)
independently reconstructs the LDL factorization from the saved first-row
enclosures, with directed rounding to a grid of size 2^-128 after every
operation. The [audit record](joint_independent_matrix_audit.json) confirms
seven positive shifted pivots for both records. This validates the matrix
algebra independently; it relies on the generator's entry enclosures and
does not independently reconstruct the prime sums or diagonal integral.

```sh
python3 -B audit_joint_saved_matrix.py --output /tmp/joint_independent_matrix_audit.json
```

## Companion scalar reference calculation

This folder also contains a separate small certificate for the centered
reference, supporting the [negative-index note](../../notes/CENTERED_NEGATIVE_INDEX_SHARPENING_20261003.md).
It is independent of the seven-source Gram calculation. The generator
checks opposite digamma signs at 6 and 7 and performs 64 rational
bisections at 192-bit precision. It certifies the unique positive zero
`t_*` of `Re psi(5/4+it/2)-log pi`, including
`1.94992548206433579713 < t_*/pi < 1.94992548206433579715`.

```sh
python3 -B certify_centered_reference_zero.py --bits 192 --output /tmp/centered_reference_zero_192.json
```

The [record](centered_reference_zero_192.json) stores exact rational
endpoints and the generator hash. The proof of uniqueness and the
negative-index consequence are analytic, in the linked note.
