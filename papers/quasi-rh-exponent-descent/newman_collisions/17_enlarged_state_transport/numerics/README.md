# Enlarged-state algebra checks and future experiments

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex), reasoning effort ultra, verified from the
recorded drafting-turn configuration. Internal replays are not independent
mathematical validation.

The initial manuscript uses the existing
[exact enlarged-state checker](../../13_microlocal_phase_space/numerics/check_enlarged_state_identities.py)
and [small identity record](../../13_microlocal_phase_space/numerics/ENLARGED_STATE_IDENTITY_RECORD_20261010.json).
They remain in their original location so one source defines the common
controls. The standard-library replay checks the anchored graph and Schur
example, the Gaussian collision control, chord commutator, and score-to-jet
quadratic with exact rational arithmetic. It does not establish a theta
sign, useful transport multipliers, or interval coverage.

From the repository root, replay without replacing the shared record:

```sh
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_enlarged_state_identities.py /tmp/project17_enlarged_state_replay.json
```

## Continuation checks

10 October 2026 continuation: GPT-6 (Codex), reasoning effort unavailable
to this session and not inferred; internal LLM checks.

- [Exact adjoint checker](check_adjoint_transport_optimality.py) and
  [record](ADJOINT_TRANSPORT_OPTIMALITY_RECORD_20261010.json): 1,878 exact
  Fraction assertions for full and restricted trees, support geometry,
  source cancellations and disconnected-sector payments.
- [Regular cell checker](check_regular_adjoint_cell.py) and
  [record](REGULAR_ADJOINT_CELL_RECORD_20261010.json): complete N=22066
  outward enclosure on t0 to t0+0.000008 and x0+0.3 to x0+0.7. The paid
  directional margin is greater than 0.5552583, conditional on the
  imported complete disk interface. The same forty subcells also exclude
  by separate paid tests, 38 by value and two by derivative.
- [Heat transversality checker](check_heat_transversality.py) and
  [record](HEAT_TRANSVERSALITY_RECORD_20261010.json): 1,819 exact rational
  and quadratic-field assertions. These check implicit fold jets, full
  Jacobians, stationary precursor coefficients for both parities,
  positive Gaussian double/triple/quadruple controls, frozen-beta score targets,
  physical normalization through order three and product error payments.
  The analytic stationary-sign theorem is proved in Note 5; the replay
  establishes no genuine theta sign or stationary-set coverage.

- [Physical stationary cell checker](check_theta_stationary_cell.py) and
  [record](THETA_STATIONARY_CELL_RECORD_20261010.json): eighty complete
  height subcells certify one physical Hx zero per time in [0.590,0.605]
  relative to x0, with HHxx/normalizer² < -90.3133241620. The imported
  complete holomorphic disk is assumed; all physical derivatives and
  third-jet costs are restored. Hxx has no zeros in this cell.
- [Direct full-theta inflection checker](check_theta_stationary_low_height.py)
  and [record](THETA_STATIONARY_LOW_HEIGHT_RECORD_20261010.json): on all
  0≤t≤0.05, 8≤x≤12, exactly one Hxx zero per time lies in [9.4,9.6],
  with HxHxxx < -3.78300454912e-7. Uses 2,048 outward integration cells,
  eighty height cells, all theta terms and complete integral tails;
  no finite-sum approximation disk. Also certifies L1(H)>2.43219610004e-7
  on the whole rectangle. Hx never vanishes there.
- [Complete theta kernel checker](check_theta_laguerre_kernel.py) and
  [record](THETA_LAGUERRE_KERNEL_RECORD_20261010.json): complete directed
  source integration proves J1,t(0.3)<-1.683363e-9 for 0≤t≤0.05.
  Negative source values do not refute positive definiteness or Fourier
  nonnegativity. The coordinate 0.3 is not a physical stationary height.
- [Exact Laguerre kernel algebra](check_laguerre_kernel_algebra.py) and
  [record](LAGUERRE_KERNEL_ALGEBRA_RECORD_20261010.json): 167 exact
  assertions for heat hierarchy, cubic/triple controls, autocorrelation
  symbols and full/half Fourier normalization. These do not verify the
  analytic remainder proof or establish any uniform theta sign.

Replay from the repository root without replacing the saved records:

```sh
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_adjoint_transport_optimality.py /tmp/project17_adjoint_algebra_replay.json
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_regular_adjoint_cell.py /tmp/project17_regular_cell_replay.json
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_heat_transversality.py --record /tmp/project17_heat_transversality_replay.json
```

All four new checkers write a record only when `--record` is explicitly
provided. Replay into temporary paths from the repository root:

```sh
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_theta_stationary_cell.py --record /tmp/project17_stationary_cell_replay.json
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_theta_stationary_low_height.py --record /tmp/project17_stationary_low_height_replay.json
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_theta_laguerre_kernel.py --record /tmp/project17_theta_kernel_replay.json
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_laguerre_kernel_algebra.py --record /tmp/project17_laguerre_algebra_replay.json
```

The high checker also validates and regenerates the retained regular-cell
source. `--project17-numerics` and `--interval-source-dir` support staged
replays. Defaults resolve relative to the source location; no machine
paths are required. The direct and paired theta checkers validate the two
retained program 13 interval source hashes. Kernel, integral and high-cell
replays use 60-digit directed Decimal arithmetic. Neither bounded
stationary calibration adds collision coverage or proves a predecessor
buffer, uniform positive definiteness or RH.

The cell checker validates both retained program 13 source hashes before
importing them. Its default source directory is relative to its location;
`--interval-source-dir` permits a staged replay. No extra dependencies
are required. Runtime metadata can vary; the small records include source
hashes, all directed endpoints and explicit complete error payments.

Future experiments should test a uniform correlated direction or source
estimate on a growing family, or the complete signed stationary-set
targets in Note 5, retaining all physical, residual and boundary costs.
Every claimed visibility margin requires outward enclosures on a stated
parameter domain. Store source code and small records; keep large derived
data outside Git under the repository's
[large-file policy](../../../../../LARGE_FILES.md).

## Paired contour and quasi RH continuation

- [Raw endpoint checker](check_paired_boundary_derivative.py) and
  [record](PAIRED_BOUNDARY_DERIVATIVE_RECORD_20261010.json): 4,096 outward
  interval cells and a complete analytic tail certify
  0.00474119 < J0,P=1 prime at zero < 0.00500393 at time zero.
  This is a nonzero raw-channel boundary source, not a complete Fourier sign.
  Uses the same two hash-checked program 13 interval sources as above.
- [Conditional cofactor transfer checks](check_quasi_rh_cofactor_transfer.py)
  and [record](QUASI_RH_COFACTOR_TRANSFER_RECORD_20261010.json): 43 exact
  rational exponent and finite divisor-coefficient checks. The prime-counting
  premise, asymptotic transfer and lattice count remain analytic inputs;
  the checker does not establish a bound for the complete actual moment.

Replay without replacing the saved records:

```sh
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_paired_boundary_derivative.py --record /tmp/project17_paired_boundary_replay.json
python3 papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/numerics/check_quasi_rh_cofactor_transfer.py --record /tmp/project17_cofactor_transfer_replay.json
```

The complex-contour growth and product-index remainder estimates are proved
analytically in [Note 9](../notes/9_PAIRED_CONTOUR_BOUNDS_ON_THE_SHRINKING_SECTOR_20261010.md).
The endpoint calculation tests a distinct source issue described in
[Note 10](../notes/10_MATCHED_MELLIN_BESSEL_TRANSFORM_AND_RAW_CHANNEL_OBSTRUCTION_20261010.md).
Model: GPT-6 (Codex); effort not exposed and not inferred. Internal LLM
checks are not independent mathematical validation.

## Nonempty high-height second stationary branch

- [High stationary S1 checker](check_high_stationary_s1_cell.py) and
  [record](HIGH_STATIONARY_S1_CELL_RECORD_20261010.json): all 22,066 terms,
  twelve height subcells, and all physical derivatives through order three
  certify exactly one genuine Hxx zero per time on
  t=t0+[0,1e-8], x=x0+[87.38,87.44]. Five candidate subcells confine it
  to x-x0 in [87.400,87.425], with Hx Hxxx/A squared < -13941.95.
  The imported complete disk is assumed. Its third physical-jet error
  472.218960 is fully paid. The first derivative is nonzero throughout,
  so this is a sign calibration without additional collision coverage.

Replay from this directory without overwriting the retained record:

```sh
python3 check_high_stationary_s1_cell.py
```

Use `--record PATH` to save a fresh record. The standard-library checker
regenerates the new midpoint and validates the same two program 13 interval
source hashes. The earlier .5 midpoint is not reused at 87.41. Detailed
bounds and scope appear in [Note 15](../notes/15_NONVACUOUS_HIGH_HEIGHT_SECOND_STATIONARY_SIGN_20261010.md).

## Bounded loss and correlated disk continuation

- [Exact correlated-jet checker](check_correlated_jet_geometry.py) and
  [record](CORRELATED_JET_GEOMETRY_RECORD_20261010.json): exact Fraction
  controls for Schur coefficients, conditional intervals, physical drift,
  degenerate parameter faces and disk-only failure models. No theta values.
- [Small-first-jet survey](survey_stationary.py) and
  [summary record](STATIONARY_SMALL_JET_SURVEY_RECORD_20261010.json): exploratory
  connected windows at N=22066 and N=100000. The summary retains parameters,
  root counts, weakest rows, validation, source hashes and raw/canonical data
  hashes. Floating sign-change detection is not complete root isolation or
  certification of a genuine stationary branch. Full root arrays are generated
  outside the repository; NumPy is required only for this survey.
- [Outward disk-ambiguity checker](check_stationary_disk_ambiguity.py) and
  [record](STATIONARY_DISK_AMBIGUITY_RECORD_20261010.json): complete finite
  N=22066 physical jets at offset58.57 admit two strict coarse-disk
  perturbations with the same value/slope and opposite Hx Hxxx signs on exact
  Hxx=0. The result concerns alternative observations, not genuine theta.

Replay the exact and outward checks from this numerics directory:

```sh
python3 check_correlated_jet_geometry.py
python3 check_stationary_disk_ambiguity.py
```

The outward checker validates the two retained interval-source hashes and
uses only the standard library. Both write new records only with `--record`.
Regenerate the detailed floating sweeps to locations outside the repository:

```sh
python3 survey_stationary.py --N 22066 --record /tmp/project17_survey_n22066.json
python3 survey_stationary.py --N 22066 --time-shift 0.00000001 --record /tmp/project17_survey_n22066_tplus.json
python3 survey_stationary.py --N 100000 --record /tmp/project17_survey_n100000.json
```

The canonical data hash is SHA-256 of the UTF-8 compact JSON serialization
of `all_detected_roots`, with sorted object keys and no trailing newline.
This omits timing but is not a portability guarantee for floating arithmetic.
No mathematical claim depends on a hash. The full proofs and numerical scope
are in [Note 18](../notes/18_CORRELATED_ERROR_JETS_AND_LOCAL_HEAT_AMBIGUITY_20261010.md)
and [Note 19](../notes/19_STATIONARY_SURVEY_AND_CERTIFIED_DISK_AMBIGUITY_20261010.md).
Model: GPT-6 (Codex); effort not exposed and not inferred. Internal LLM work.


## Explicit theta correction and weak stationary cell

`check_theta_corrected_stationary_cell.py` retains the leading correction
from Polymath Corollary 6.4, uses Proposition 6.6 to bound the complete
residual, and pays the replacement of the printed nonholomorphic correction
by a local holomorphic exponential. It uses the same hash-checked directed
interval modules and finite-moment transport method as the retained high
stationary checker. The source theorem and new comparison argument are
stated in [Note 20](../notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md).

From this directory, replay with:

```sh
python3 check_theta_corrected_stationary_cell.py --record /tmp/THETA_CORRECTED_STATIONARY_CELL_RECORD_20261011.json
```

The default shared-source directory resolves to investigation 13's
`numerics/`; an explicit `--interval-source-dir` is also supported.
The [retained small record](THETA_CORRECTED_STATIONARY_CELL_RECORD_20261011.json)
certifies the whole time interval `[t0,t0+1e-8]`, `t0=1/(2 log 22066)`,
and spatial offsets `[58.567,58.571]` from `4 pi 22066^2`. Every time has
one genuine Hxx zero, in offsets `[58.5690,58.5695]`, with strictly negative
Hx Hxxx. Conditional derivative combinations also verify the sign after
eliminating the leading correction amplitude algebraically.

The analytic remainder is divided by the holomorphic normalizer before
Cauchy estimates; all normalizer derivatives through order three are paid.
The physical third derivative error is below 0.015346692, compared with
about 472.219 in Note 19's particular coarse disk payment. This is a sharper
source estimate and a genuine stationary-sign calibration, not new
collision coverage: the earlier interface already separates the slope.
The checker verifies its fixed-cutoff and local profile hypotheses; the
broader analytic profile corollary in Note 20 is not used numerically.
All outputs are small; no new large derived archive is retained.

## Complete theta correction across a cutoff change

The [cutoff matching checker](check_theta_cutoff_matching.py) and
[record](THETA_CUTOFF_MATCHING_RECORD_20261011.json) verify the complete
corrected disk error on `t=t0+[0,1e-8]`, `t0=1/(2 log 22066)`, for all
centers in `4 pi 22066^2+[-0.1,0.1]`, with radius 0.05. The enclosing
rectangle has natural cutoffs 22065 and 22066; the fixed reference cutoff
is 22066 even for individual disks wholly to the left of the moving edge.
Both reflected entering waves and the complete source remainder are paid.

The added matching cost is below 1.484686e-12 and the complete disk
residual is below 3.135204e-7. Direct normalization by the constant
positive center value `A_t(X)` gives physical derivative payments
`j! eta/r^j`; the third is below 0.015048978. These parameters and the
normalization convention differ from the preceding stationary checker.
No genuine first-jet lower bound or stationary product is evaluated here.

A separate real-edge finite-term evaluation finds a positive discrepancy
of about 3.920037e-13, within the full complex matching allowance. The
natural piecewise leading approximation is therefore not exactly
continuous; all derivative bounds use the frozen holomorphic expression.
The general analytic proof and candidate localization are in
[Note 22](../notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md),
and a separate-agent replay and original-carrier phase audit are in the
[review](../reviews/11_THETA_CUTOFF_MATCHING_REVIEW_20261011.md).

Replay from this directory without overwriting the saved record:

```sh
python3 check_theta_cutoff_matching.py --record /tmp/THETA_CUTOFF_MATCHING_RECORD_20261011.json
```

The standard-library script uses the same two hash-checked interval modules,
60-digit directed arithmetic and optional `--interval-source-dir` as above.
The published source theorem is an imported analytic input. This bounded
numerical record does not verify the theorem formally or establish uniform
stationary loss or collision exclusion. All retained files are small.
Preparation: GPT-6 (Codex), 11 October 2026; effort unavailable and not
inferred. Internal LLM checks are not independent mathematical validation.
