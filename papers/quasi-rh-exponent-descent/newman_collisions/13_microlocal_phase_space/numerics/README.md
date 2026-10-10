# Numerical and algebraic replay

10 October 2026. Latest continuation: GPT-6.1-sol (Codex), configured
reasoning effort ultra, verified from the parent chat recording. Earlier
retained records keep their original metadata. Checks are internal, not
independent mathematical review.

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_phase_space.py
```

The script requires only Python 3 and the standard library. It prints a small JSON record; [the run record](SCOUT_CHECK_RECORD_20261010.json) was produced on 10 October 2026 with Python 3.10.0. Status: **PASS**.

The four Gaussian jet polynomials were verified exactly over rational numbers. A Gaussian wave amplitude checks the full Husimi generator by finite differences; a finite complex block checks doubled value, derivative and positive-matrix observed squares. Those finite floating-point controls are not a genuine arithmetic sign certificate.

The source note supplies the analytic arguments. Floating-point checks are not rigorous numerical enclosures and are not independent mathematical validation. No large generated data are stored. Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md) if later computations need an archive.

## Genuine block-current continuation

Run the bounded interval checker from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_block_current.py
```

The default parameters are `M=N=22066`, `kappa=1`, and 60-digit Decimal
arithmetic. All 11033 terms in the actual relative block are enclosed with
outward rounding, Taylor/alternating-series trigonometric bounds and full
physical derivative drift. Unlike the initial replay above, this calculation
is an outward interval sign enclosure. It uses only Python 3's standard
library and takes a few seconds in the recorded environment.

[The certificate](BLOCK_CURRENT_CERTIFICATE_20261010.json) encloses
`J_B/w_N^2` strictly between `-181.169106` and `-181.169105`; its status is
**PASS**. [The build record](BLOCK_CURRENT_BUILD_RECORD_20261010.json) identifies
the exact source/certificate by SHA-256. Replaying computes the sign afresh;
hashes alone do not decide it.

This is a genuine finite-block current certificate, not a complete-sum sign,
candidate collision, threshold exclusion, or RH result. The checker asserts
a negative current at its default height; another `--M` is a separate
experiment and may fail that particular assertion. See Note 2 and Review 2
for the complete recombination and candidate-current tolerance.

## Complete current and genuine simple-zero rectangle

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_complete_current_rectangle.py
```

The new checker uses the exact `M=N=22066` center and all 22066 genuine
terms. It imports the preserved Note 2 arithmetic source after checking its
retained SHA-256, and evaluates integer powers locally by repeated outward
multiplication. A changed dependency fails closed before import.

The [complete certificate](COMPLETE_CURRENT_RECTANGLE_CERTIFICATE_20261010.json)
reports the block, complement and full current, the cross current, and
both difference-phase and reflected sum-phase energy interference.
It then certifies a positive-area rectangle with time increments
`0 <= t - t0 <= 8e-6` and height offsets `0.3 <= x - x0 <= 0.4`.
All spatial normalizer/drift corrections, physical fixed-height time
derivatives, coherent midpoint jets, sixth-moment remainders, and full
holomorphic value/derivative payments are retained.

Status: **PASS**. The paid endpoint values have opposite signs and the paid
normalized derivative `Q_t'` exceeds `10.20` throughout the rectangle. Therefore every time
in that interval has one unique simple genuine `H_t` zero in the specified
height interval; `H_t` and `H_t'` are jointly nonvanishing on the entire
rectangle. The uniform paid full-current reverse candidate inequality
also passes. This is a finite rectangle theorem, not sectorwide current
positivity, threshold exclusion, or an RH result.

The [build record](COMPLETE_CURRENT_RECTANGLE_BUILD_RECORD_20261010.json)
binds the new source, its preserved imported source and the certificate.
The replay decides each sign by arithmetic; hashes identify files. No
large data or nonstandard Python dependencies are required.

## Complete candidate-current atlas and thirteen genuine zero branches

Run from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_candidate_current_atlas.py
```

To write a fresh replay without changing the retained certificate:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_candidate_current_atlas.py --output /tmp/candidate-current-atlas-replay.json
```

The new standard-library source checks the unchanged Note 3 source hash
before import; that source checks the unchanged Note 2 interval source.
It computes all 22066 genuine terms once into 64 signed midpoint jets and
the complete 64th absolute frequency moment. A degree-63 coherent
polynomial with its real-variable remainder covers the full height width
eight; exact polynomial shifts allow adaptive local enclosures without
dropping signed cancellation. Physical spatial residuals and fixed-height
time/mixed derivatives are paid on the whole rectangle.

The exact theorem domain is `t0=1/(2*log(22066)) <= t <= 1/20` and
`x0=4*pi*22066^2 <= x <= x0+8`. Numerical outer hulls bound computations;
the certificate distinguishes them from the exact domain at the sector
edge. The natural cutoff is always 22066. The full holomorphic value and
derivative payments satisfy `eta < 0.009642`, `L*eta < 0.192864`.

Status: **PASS**. The [retained certificate](CANDIDATE_CURRENT_ATLAS_CERTIFICATE_20261010.json)
has 46 closed height strips covering every exact allowed time. It proves
29 value-away strips and 17 candidate strips with simultaneously positive
paid derivative and full-current margins. The minimum normalized joint
vector norm is greater than `0.03728`; the candidate current gap is greater
than `0.11934`. All thirteen connected candidate bands have strict
opposite all-time endpoint signs and a strict all-time derivative sign.
Consequently there are exactly thirteen simple genuine heat zeros at each
time, with no other zero and no joint `H_t,H_t'` zero in the rectangle.

The [build record](CANDIDATE_CURRENT_ATLAS_BUILD_RECORD_20261010.json) binds
the final source, preserved dependencies and the approximately 122 KB
certificate. A separate internal agent's complete replay was byte
identical. Both candidate tolerances and every cell adjacency/endpoint are
checked; no ordinary float enters a proof assertion. The correlated
holomorphic candidate quantity from Heat Note 18 is also reported, but
the acceptance rules already prove the result using the older rectangular
payments. See Note 4 and Review 4 for the finite scope; no uniform-sector
or RH conclusion follows from this bounded atlas.

## Finite multi-cutoff family with direct Schur checks

Run the new generic checker from the repository root:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_multi_cutoff_candidate_family.py --M 22067
```

The retained cases are `M=22067`, `22068` and `22080`. To replay all three
without changing their retained certificates:

```bash
for task_M in 22067 22068 22080; do
  python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_multi_cutoff_candidate_family.py --M "$task_M" --output "/tmp/current-family-M$task_M.json"
done
```

For each selected cutoff the exact domain is
`1/(2*log(M)) <= t <= 1/20`, `4*pi*M^2 <= x <= 4*pi*M^2+8`.
The windows are disconnected, have their own constant natural cutoff,
and do not cover entire cutoff cells or the gaps between them. The source
hash-checks the preserved Note 4 source before import and inherits its
preserved dependency chain. Every genuine term and physical spatial/time
payment is rebuilt at the new actual common orbit.

All three cases are **PASS**. Their complete records are
[22067](MULTI_CUTOFF_M22067_CERTIFICATE_20261010.json),
[22068](MULTI_CUTOFF_M22068_CERTIFICATE_20261010.json) and
[22080](MULTI_CUTOFF_M22080_CERTIFICATE_20261010.json). They have 29, 28 and
32 closed strips and prove exactly 12, 12 and 13 simple genuine heat
zeros per time. Their normalized joint-vector floors exceed `0.03117`,
`0.02205` and `0.0032919`, respectively. No unresolved strip is omitted.

Every value-screen survivor actively passes the first-jet Schur candidate
condition in reverse and a strict fully paid derivative test. The
derivative test already implies that Schur predicate for these particular
records; additional curved-body exclusion is not demonstrated here.
Only two retained strips per cutoff also pass the coarse rectangular
complete-current test. Other current enclosures are inconclusive, with
no negative actual-current assertion. Full `eta`, `L*eta`, all complete
coherent interference, endpoint signs, derivative signs and exact closed
coverage remain retained.

The [family build record](MULTI_CUTOFF_CANDIDATE_FAMILY_BUILD_RECORD_20261010.json)
binds the generic source, preserved dependencies and three small
certificates. Separate internal full replays were byte identical to all
three. Other `--M` values are separate experiments and may fail acceptance
or counting assertions; no uniform cutoff theorem is encoded by the three
retained successes. See Note 5 and Review 5 for scope and the remaining
signed arithmetic obligation.

## Manuscript certificate summary

The read-only checker [check_manuscript_certificate_summary.py](check_manuscript_certificate_summary.py)
uses exact rational arithmetic to audit the stored enclosures and coverage:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_manuscript_certificate_summary.py
```

[The summary](MANUSCRIPT_CERTIFICATE_SUMMARY_20261010.json) reports **PASS**:
12 build-record hash/size entries, all 135 closed atlas leaves and all
50 zero bands. It verifies conservative normalized joint floors, the
correct L-up derivative denominator, conservative Schur lower bounds,
acceptance predicates, exact closed adjacency and strict all-time
endpoint/derivative signs. It requires only the standard library and
performs no writes. `--numerics-dir` can select another copy of the records.

This is an exact-rational logical inspection of retained outward intervals;
use the original sources above for fresh interval-sum replays. Those fresh
replays were also performed for the working manuscript and were
byte-identical to the retained certificates. Neither operation re-proves
the imported full holomorphic approximation. The
[manuscript review](../reviews/6_MANUSCRIPT_INTERNAL_REVIEW_20261010.md)
records these checks and their limits. New review metadata: GPT-6 (Codex),
exact serving variant and effort not exposed and not inferred.

## Curvature and sharp candidate-null support controls

The new read-only exact checker uses only the Python standard library:

```bash
python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/check_candidate_localization_and_support.py
```

[The small record](CANDIDATE_LOCALIZATION_SUPPORT_RECORD_20261010.json)
reports PASS with 6914 Fraction controls for the curvature complete square,
physical candidate-null identity, sharp support, golden-ratio comparison
and monotone upper endpoints. These are finite algebra/support controls,
not a proof of the imported analytic interface or an actual arithmetic sign.
Optional `--output` writes a specified replay record; omit it for no writes.

## Bounded complete-orbit and Möbius pilots

These numerical diagnostics require NumPy. Tested environment: Python
3.10.0, NumPy 1.25.1; no dependencies were installed. Decimal protects the
large common-height phases before complex128 operations. Run from the
repository root, writing replays outside the repository:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/pilot_complete_centered_jets.py --output /tmp/complete-centered-pilot-replay.json --calibration-certificate papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/COMPLETE_CURRENT_RECTANGLE_CERTIFICATE_20261010.json
PYTHONDONTWRITEBYTECODE=1 python3 papers/quasi-rh-exponent-descent/newman_collisions/13_microlocal_phase_space/numerics/pilot_coupled_mobius_frontier.py --output /tmp/coupled-mobius-pilot-replay.json
```

[The primary source](pilot_complete_centered_jets.py) and
[record](PILOT_COMPLETE_CENTERED_JETS_20261010.json) retain all terms at
M=22066,50000,100000 and nine height offsets, physical raw jets through
order four, complete centered moments through degree six, block/complement
interference, current and candidate-null payments. The counting constant
remains symbolic. Selected 75-digit complete sums, raw derivative controls
and retained-certificate midpoint calibration pass. Its critical-point
scan makes no root-completeness or interval-coverage claim. No sampled
joint candidate is found. The available fourth Cauchy upper payment remains
about 25295–37050, despite tiny Bell residuals; this is an upper payment,
not a measured genuine approximation error.

[The coupled source](pilot_coupled_mobius_frontier.py) and
[record](PILOT_COUPLED_MOBIUS_FRONTIER_20261010.json) retain every nonzero
c_J(q), both phase channels and BB/CC/BC terms at N=100000,J=100 and two
heights. They check the exact divisor identity for every integer through N,
and 234 formal Fraction controls through N=12. Singleton Jdagger terms
q>N/2 vanish identically and are optimized exactly. The first active band
has coefficients -1 and contributes negatively at both heights; the full
frontier stays positive because q=1 dominates. Candidate equations are
never imposed separately on a sublattice. The source checks the preserved
primary source hash before import. Use `--N` only for a separate experiment.

[The build/summary record](PILOT_SUMMARY_BUILD_RECORD_20261010.json) binds
both sources and records and reports their scope. Separate full internal
replays match every retained field except elapsed time. Neither diagnostic
is an outward enclosure, verifies the all-real/counting hypotheses, or
supplies the missing uniform signed threshold inequality. See
[Heat Note 24](../../notes/24_CURVATURE_CONES_SHARP_NULL_PAYMENTS_AND_LOCALIZED_POISSON_20261010.md)
and [Review 7](../reviews/7_CANDIDATE_LOCALIZATION_AND_SIGNED_PILOT_INTERNAL_REVIEW_20261010.md).
New metadata: GPT-6 (Codex); exact serving variant and effort not exposed
and not inferred. Internal LLM validation only.
