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

The [octonion jet checker](check_octonion_jet_identities.py) and
[small record](OCTONION_JET_IDENTITY_CHECKS_20261014.json) verify 248 exact
identities using standard-library rational polynomial arithmetic. They
cover Cayley--Dickson multiplication, norm composition, associators,
physical energy and stationary signs, the transverse derivative, the
eight-dimensional differential extension, and polynomial collision
controls. Replay from this directory:

```sh
python3 check_octonion_jet_identities.py --output /tmp/inv21-octonion-replay.json
```

The [derivation](../notes/15_OCTONIONIC_LIFT_AND_ASSOCIATOR_SIGN_TARGET_20261014.md)
and [internal review](../reviews/10_OCTONIONIC_LIFT_AND_ASSOCIATOR_INTERNAL_REVIEW_20261014.md)
separate these algebra checks from the analytic positive-source control
and the unproved theta-specific estimate. Added 14 October 2026, prepared
for Edward Baker with substantial LLM assistance, **gpt-6-astra**, effort
**ultra**. This is not a new theta sign certificate.

The [centered residual driver](certify_phase_centered_residual.py) and
[certificate](THETA_CENTERED_RESIDUAL_100_104_20261014.json) prove the
complete-source relative bound C0²+C1²<E/9 and mu>=2/5 on 32 closed
cells covering [0,1/2] x [100,104]. Shared centered coefficients are
formed before time/space Taylor transport, with all source and parameter
remainders paid. Both genuine stationary signs and |F|>4e-16 are also
certified on this band. With python-flint available, replay:

```sh
python3 certify_phase_centered_residual.py --output /tmp/theta-residual-replay.json
python3 check_theta_centered_residual_identities.py --output /tmp/theta-residual-identities.json
```

The [exact algebra checker](check_theta_centered_residual_identities.py)
and [record](THETA_CENTERED_RESIDUAL_IDENTITY_CHECKS_20261014.json) check
nine identities using standard-library rational polynomial arithmetic.
The [retained record auditor](audit_theta_centered_residual_record.py)
and [audit record](THETA_CENTERED_RESIDUAL_RECORD_AUDIT_20261014.json)
bind the generating sources and independently verify the exact cover,
outward endpoints, cone and stationary decisions, and stated norm floors.
Replay with the standard library:

```sh
python3 audit_theta_centered_residual_record.py --record THETA_CENTERED_RESIDUAL_100_104_20261014.json --output /tmp/theta-residual-audit.json
```

The [derivation](../notes/16_THETA_CENTERED_RESIDUAL_AND_SHARED_ARITHMETIC_20261014.md)
and [internal review](../reviews/11_THETA_CENTERED_RESIDUAL_INTERNAL_REVIEW_20261014.md)
state the source representation, complete payments, independent replay,
and remaining all-height obligation. Added 14 October 2026, prepared for
Edward Baker with substantial LLM assistance, **gpt-6-astra**, effort
**ultra**.

The [outer-region algebra and phase diagnostic](check_outer_cusp_and_phase_obstructions.py)
and [record](OUTER_CUSP_AND_PHASE_OBSTRUCTION_CHECKS_20261014.json)
check the exact four-jet perturbation algebra, reject a phase-independent
positivity condition for two exact shared-carrier arithmetic sums, and
retain selected complete-source point enclosures and staircase identities.
These computations do not prove the uniform asymptotic theorem; its proof
is in [Note 17](../notes/17_UNIFORM_OUTER_CUSP_SIGNS_AND_THRESHOLD_FOUR_20261014.md).
They give no new finite height cover. Prepared 14 October 2026 with
substantial LLM assistance, **gpt-6-astra**, effort **ultra**. Replay with
python-flint available:

```sh
python3 check_outer_cusp_and_phase_obstructions.py --output /tmp/outer-cusp-checks.json
```

## Manuscript rewrite checks, 14 October 2026

The [rewrite check receipt](MANUSCRIPT_REWRITE_CHECKS_20261014.json) records
6682 higher-height record checks, 547 centered-band record checks, 248
exact octonion identities, and nine centered-residual identities freshly
replayed for the rewritten manuscript. No full interval quadratures were
rerun in this editorial pass; the earlier independent replays remain in
Reviews 6, 9, and 11. Prepared for Edward Baker with substantial LLM
assistance, **gpt-6-astra**, reasoning effort **ultra**.

## Oscillatory continuation checks, 14 October 2026

The [pair/block checker](check_signed_carrier_pair_identities.py) and
[receipt](SIGNED_CARRIER_PAIR_IDENTITY_CHECKS_20261014.json) verify 34 exact
rational identities and exponent checks for the paired observations,
stationary correction, tail expansions, threshold-three block proof,
staircase recurrence, and entry-phase cancellation. The
[constant checker](check_explicit_outer_constants.py) and
[receipt](EXPLICIT_OUTER_CONSTANT_CHECKS_20261014.json) verify 52 rational
budgets and half-line polynomial inequalities for the explicit
threshold-five height 4 pi exp(10^9). Both use the Python standard library:

```sh
python3 check_signed_carrier_pair_identities.py --output /tmp/inv21-pair-checks.json
python3 check_explicit_outer_constants.py --output /tmp/inv21-outer-constants.json
```

The [integration receipt](OSCILLATORY_CONTINUATION_CHECKS_20261014.json)
binds these small sources and records. The [internal review](../reviews/14_OSCILLATORY_BLOCKS_AND_EXPLICIT_HEIGHT_REVIEW_20261014.md)
independently checks the analytic arguments and replays both drivers.
The finite algebra does not replace the proofs in Notes 19 and 20; no new
interval quadrature or finite-height cover is asserted. Prepared for
Edward Baker with substantial LLM assistance, **gpt-6-astra**, effort
**ultra**.


The [signed-curvature split checker](check_signed_curvature_split.py) and
[receipt](SIGNED_CURVATURE_SPLIT_IDENTITY_CHECKS_20261014.json) check 14
exact polynomial identities and controls. The [genuine-branch pilot](check_stationary_favorable_curvature_pilot.py)
and [receipt](STATIONARY_FAVORABLE_CURVATURE_PILOT_20261014.json) extract
eight paid time slabs from the existing 100--104 certificate. They prove
a prescribed zero-loss signed estimate on a genuine h1=0 branch in
101<x<102, with a deliberate alternative centering for which every norm
cone eta<=mu fails. The original saddle-centered eta=1/3 cone still passes.
No new quadrature, height extension, or proper finite-block filter is
claimed. [Note 21](../notes/21_ONE_SIDED_STATIONARY_ESTIMATES_AND_THETA_PILOT_20261014.md)
gives the formulas, limitations, and standard-library replay commands;
[Review 15](../reviews/15_ONE_SIDED_STATIONARY_ESTIMATES_REVIEW_20261014.md)
records independent checks. Prepared 14 October 2026 for Edward Baker
with substantial LLM assistance, **gpt-6-astra**, effort **ultra**.


The [proper-source-filter driver](certify_predetermined_source_filter_pilot.py)
and [compact record](PREDETERMINED_SOURCE_FILTER_PILOT_20261014.json)
retain all 64 predeclared filter/branch/time cases. Fixed two-index filters
absorb an adverse complement with lambda=1/2 and zero loss on both genuine
stationary branches; one-index filters fail the same condition. The
[Gaussian checker](check_gaussian_source_filter_pilot.py) and
[record](GAUSSIAN_SOURCE_FILTER_PILOT_20261014.json) certify positive retained
and complementary products in 14 cases using the exact full-source
identity G_j=C_j(t-1/16,x). New partial quadratures use python-flint 0.9.0
at 192 bits; the Gaussian extraction uses the Python standard library.
[Note 22](../notes/22_PROPER_SOURCE_FILTERS_AND_THETA_CORRELATIONS_20261014.md)
gives definitions, errors, analytic limitations, and replay commands.
[Review 16](../reviews/16_SOURCE_FILTERS_AND_THETA_CORRELATIONS_REVIEW_20261014.md)
independently reproduces all classifications and numerical bounds. No
height extension or global correlation estimate. Prepared 14 October 2026
for Edward Baker with substantial LLM assistance, **gpt-6-astra**, **ultra**.


## Manuscript integration audit, 14 October 2026

[MANUSCRIPT_CONTINUATION_CHECKS_20261014.json](MANUSCRIPT_CONTINUATION_CHECKS_20261014.json)
records 100 fresh exact checks (34 paired/block, 52 outer constants,
14 signed-split/control) and hash identity of the three previously
independently replayed finite pilots. This integration does not repeat
interval quadrature or extend height coverage. See
[Review 17](../reviews/17_MANUSCRIPT_CONTINUATION_INTEGRATION_REVIEW_20261014.md)
and [Note 23](../notes/23_MANUSCRIPT_INTEGRATION_AND_CROSS_TIME_CONTINUATION_20261014.md).
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra**, reasoning effort **ultra**.

## Proportional Gaussian delay checks 14 October 2026

The [half-time pilot](check_proportional_gaussian_source_filter_pilot.py)
and [16-case record](PROPORTIONAL_GAUSSIAN_SOURCE_FILTER_PILOT_20261014.json)
certify retained and absorption products on both current stationary
branches for all eight closed time slabs covering [0,1/2]. The protocol
fixes delta=t/2, lambda=1/2, a=pi/16, b=1/4, and zero loss before testing.
Exact common-variable binomial transport preserves cross-time polynomial
correlation and pays all original complete-source errors. The separate
complement is undecided on four cases and positive on the other twelve.
The [20-check algebra driver](check_proportional_delay_identities.py)
and [receipt](PROPORTIONAL_DELAY_IDENTITY_CHECKS_20261014.json) include
complex conjugation controls, moving-delay derivatives, and pair-tail
payments. These standard-library replays do not repeat quadrature or
extend height coverage. [Note 24](../notes/24_PROPORTIONAL_DELAY_PHASE_OBSTRUCTION_AND_CONTINUATION_20261014.md)
proves the all-height phase obstruction to this rule despite finite
success; [Review 18](../reviews/18_PROPORTIONAL_DELAY_PHASE_OBSTRUCTION_REVIEW_20261014.md)
records independent replay and 1,200 additional exact affine evaluations.
Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol**, reasoning effort **ultra**.

The [independent affine audit](audit_proportional_delay_affine_transport.py)
and [receipt](PROPORTIONAL_DELAY_AFFINE_AUDIT_20261014.json) reproduce all
1,200 rational Taylor comparisons cited in Review 18, with four input
source-hash checks. They check the finite transport polynomial, with no
quadrature, analytic-tail, or new theta-sign claim.

## Phase controlled delay and cusp cover through 112

14 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol**, reasoning effort **ultra**.

The [new generator](certify_fixed_cusp_band_extension.py) runs the unchanged
full-source driver on [104–108](FIXED_CUSP_BAND_104_108_20261014.json) and
[108–112](FIXED_CUSP_BAND_108_112_20261014.json), using python-flint 0.9.0
at 192 bits. All 64 whole-cell norm tests and 128 stationary implications
pass. The original uniform 1/9 cone remains INCOMPLETE in the saved records
and is reported separately.

The [exact auditor](audit_fixed_cusp_band_extension.py) and
[1,321-check receipt](FIXED_CUSP_BAND_EXTENSION_AUDIT_20261014.json) certify
both genuine stationary branches, the half-time products, and positive
retained/absorption products at **every earlier time** s in [0,t]. They
preserve a common spatial coordinate while separately paying both time
ranges. All old coarse undecided verdicts are retained. This includes the
proposed smooth delay on these finite cells, with no fitted losses.

The [symbolic driver](check_phase_controlled_delay_identities.py) and
[21-check record](PHASE_CONTROLLED_DELAY_IDENTITY_CHECKS_20261014.json)
verify moving-delay derivatives and rational budgets for the analytic
outer theorem. [Note 25](../notes/25_PHASE_CONTROLLED_DELAY_AND_CUSP_EXTENSION_20261014.md)
contains the complete proof and reproduction commands; the
[validation receipt](PHASE_CONTROLLED_CUSP_CONTINUATION_CHECKS_20261014.json)
records fresh exact replay plus two complete 192-bit quadrature replays,
matching every field except elapsed time. The analytic comparison adds no
asymptotic coverage, and the unbounded inner cusp remains open.

## Poisson identity and remainder continuation of 15 October 2026

- [Poisson checker](check_poisson_parity_heat_obstruction.py) and [receipt](POISSON_PARITY_HEAT_OBSTRUCTION_CHECKS_20261015.json): 27 exact/sensitivity assertions and 12 paid primitive-identity comparisons. The unbounded heat obstruction is proved analytically in Note 38.
- [Convex dyadic checker](check_convex_dyadic_weighted_remainder.py) and [receipt](CONVEX_DYADIC_WEIGHTED_REMAINDER_CHECKS_20261015.json): 129 exact rational assertions supporting Note 39, with imported constants unevaluated.
- [Fixed-theta baseline driver](certify_theta_stationary_baseline.py) and [receipt](THETA_STATIONARY_BASELINE_20261015.json): six fresh unique full-stationary roots in their final brackets, all with positive signed products at theta 1/2, 3/4, and 1. Complete source and transport errors are paid. No new sign domain or Poisson-mechanism validation.

Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra**, effort **ultra**. [Review 27](../reviews/27_POISSON_OBSTRUCTION_AND_WEIGHTED_REMAINDER_REVIEW_20261015.md) records the proof and computation boundaries.

## Localized Poisson and explicit weighted budgets, 15 October 2026

Prepared for Edward Baker with substantial LLM assistance; **gpt-6.1-sol**, effort **ultra**. `check_poisson_mode_cutoff_obstructions.py` records 260 exact assertions in `POISSON_MODE_CUTOFF_OBSTRUCTIONS_20261015.json`; `check_explicit_weighted_budget.py` records 50 exact assertions in `EXPLICIT_WEIGHTED_BUDGET_CHECKS_20261015.json`. Both use the Python standard library and accept `--output /tmp/replay.json`. Independent replay is byte-identical. These are finite algebraic audits, not stationary-root or sign certificates. `LOCALIZED_POISSON_CONTINUATION_VALIDATION_20261015.json` records final hashes, links, sizes, manuscript identity, and scope.

## Exact local manifold geometry

[check_theta_manifold_geometry.py](check_theta_manifold_geometry.py) verifies the semi-flat closed triple, inverse metric, Ricci-flatness, nonzero horizontal sectional curvature, totally geodesic base slices and formal source operator using rational Laurent polynomials. [Execution receipt](THETA_MANIFOLD_GEOMETRY_CHECKS_20261015.json): 55 exact assertions, independently replayed. Run `python3 check_theta_manifold_geometry.py` from this directory. It is not a theta sign certificate. Updated 15 October 2026 for Edward Baker with substantial LLM assistance, **gpt-6-astra**, effort **ultra**.
