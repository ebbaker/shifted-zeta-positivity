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
