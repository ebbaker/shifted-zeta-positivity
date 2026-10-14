# Quaternion theta computations

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.

Save reproducible computations and small execution records here. The first
formula task is specified in the [research program](../notes/2_INITIAL_RESEARCH_PROGRAM_20261014.md).
The [exact polynomial checker](check_fueter_boundary_identities.py) and
[small execution record](FUETER_BOUNDARY_IDENTITY_CHECKS_20261014.json)
check Fueter regularity, the first three spherical boundary moments,
and polynomial control observations using rational arithmetic.
Run `python3 check_fueter_boundary_identities.py --output /tmp/fueter-checks.json`.
These are algebra consistency checks, not a theta numerical certificate.

The [central constant checker](check_theta_central_moment_bound.py) and
[record](THETA_CENTRAL_MOMENT_BOUND_20261014.json) verify the elementary
core, entire-tail, and signed moment constants. The
[gluing constant checker](check_theta_gluing_defect_constants.py) and
[record](THETA_GLUING_DEFECT_CHECKS_20261014.json) verify the four
defect-transfer constants, central robust gap, and endpoint determinant.
Both use exact rational arithmetic and finite exponential-series bounds;
no quadrature or finite theta truncation decides these analytic claims.

The [coordinate algebra audit](check_quaternion_coordinate_algebra.py) and
[record](QUATERNION_COORDINATE_ALGEBRA_CHECKS_20261014.json) add 58 exact
checks at rational complex coordinates, including Hamilton multiplication,
Fueter and heat identities, signed Laguerre components, and the negative
real Jacobian orientation. It imports the polynomial utility above.

The [compensated stationary checker](certify_compensated_stationary_theta.py)
and [certificate](COMPENSATED_STATIONARY_THETA_CERTIFICATE_20261014.json)
cover \([1/200,3/50]\times[7,41]\) with 34 closed cells. They retain
K=2, N=3 compensated channels and every arithmetic cross term, pay the
complete index and integration tails, and use validated quadrature and
parameter Taylor enclosures to decide both genuine stationary signs.
The run uses python-flint 0.9.0 at 256-bit precision. From this directory,
with python-flint available to the chosen Python interpreter, replay:

```sh
python3 certify_compensated_stationary_theta.py --output /tmp/inv21-stationary-replay.json
```

The [rational tail and overlap checker](check_compensated_tail_and_signed_overlap.py)
and [record](COMPENSATED_TAIL_AND_SIGNED_OVERLAP_20261014.json)
replay the explicit all-index constants and a separate analytic signed
estimate using the Python standard library. Their
[derivation](../notes/8_COMPENSATED_STATIONARY_SIGN_DERIVATION_20261014.md)
and [internal review](../reviews/5_COMPENSATED_STATIONARY_SIGN_INTERNAL_REVIEW_20261014.md)
state the bounded claim and remaining all-height obligation.

The [full-time extension driver](certify_compensated_stationary_time_extension.py)
and [compact certificate](COMPENSATED_STATIONARY_TIME_EXTENSION_20261014.json)
cover [0,1/2] x [7,41] with 272 cells, retaining the same complete error
payments. They certify both stationary signs, all regular branch windows,
and a direct norm gap greater than 1.89e-6. The record binds both the new
driver and its imported source. Replay with python-flint available:

```sh
python3 certify_compensated_stationary_time_extension.py --output /tmp/inv21-full-time-replay.json
```

The [forward-collar checker](check_forward_stationary_collars.py) and
[record](FORWARD_STATIONARY_COLLAR_CHECKS_20261014.json) use exact rational
arithmetic to audit branch identities, the quartic control, and a concrete
short continuation from the earlier certificate. Their
[derivation](../notes/10_FORWARD_STATIONARY_COLLARS_AND_BRANCH_CREATION_20261014.md)
explains the necessary branch-creation and edge guards. These checks do
not establish a uniform all-height gap.

The [correlated-source driver](certify_correlated_source_height_extension.py)
and its [band guide](CORRELATED_SOURCE_HEIGHT_README_20261014.md) extend
full-time coverage through height100 with three records below one MiB.
They sum theta center jets before common Taylor evaluation and retain
all previous errors. The 510 new cells have no unresolved signs, direct
norms, or merged branch windows.

The [shifted-contour checker](check_shifted_contour_payments.py) and
[record](SHIFTED_CONTOUR_PAYMENT_CHECKS_20261014.json) check analytic
payment hypotheses at five selected heights and eight paid shifted/direct
jet comparisons. These are implementation checks; the
[derivation](../notes/12_SHIFTED_CONTOUR_FOUR_JET_PAYMENTS_20261014.md)
proves the universal absolute bounds, with no global sign assertion.

For each future computation, identify the formula and source version,
parameters, domain, arithmetic method, approximation and tail bounds,
and the exact claim established. Keep numerical claims in dedicated
notes that link to the code and records. Use the polynomial control in the
[criteria note](../notes/1_RH_CRITERIA_AND_QUATERNION_SETUP_20261014.md)
and the [existing stationary certificates](../../20_constrained_operator_squares/notes/2_CERTIFIED_STATIONARY_THETA_AND_EULER_CONTROLS_20261014.md)
as scoped references.

Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md). Keep tracked
files below about 1 MiB and large regenerable outputs outside Git.
Introduce a documented archive lookup and stored/content hashes when
the first large derived dataset is produced.

The [retained higher-height auditor](audit_correlated_source_height_records.py)
and [small audit record](HIGHER_HEIGHT_RECORD_AUDIT_20261014.json) replay
6682 exact semantic decisions after binding all three certificate bytes
and their generating/imported sources. It uses only the standard library:

```sh
python3 audit_correlated_source_height_records.py --output /tmp/inv21-height-audit.json
```

This complements the independent validated-quadrature replay; it does not
replace the analytic source bounds or establish an all-height sign.
