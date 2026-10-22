# Relative charge computations

21 October 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance. Actual model **gpt-6-astra (Codex)**,
reasoning effort **max**.

## First theta pilot

[The script](certify_relative_charge_pilot.py) replays the complete
bounded theta acquisition and direct comparison in [Note 01][note].
It requires Python 3.10 or later and `python-flint==0.9.0`.

From this directory, in an environment containing that dependency:

```sh
python3 certify_relative_charge_pilot.py --out /tmp/RCH12_REPLAY.json
```

The default precision is 192 bits. The script enforces a 180-second
budget, finite returned balls, source-tail admissibility, strict gaps,
a real-root sign bracket, and exact quadratic/cubic control checks.
Failure of a certificate assertion stops execution before writing a
success record. No external dataset is needed.

The small [recorded receipt](RELATIVE_CHARGE_PILOT_20261021.json) includes
all eight integral enclosures, source tails, the script hash, package
version, domains, gaps and acquisition counts. Elapsed times vary by run;
no byte-for-byte receipt reproducibility is asserted. Its analytic
validity depends on the tail and Taylor proofs in Note 01 and Acb's ball
arithmetic. It is not a formal proof or an independent review.

The boundary method uses eight scalar integrals and 2,208 callbacks in
the recorded run; the direct method uses a six-integral subset with
1,656 callbacks. Neither needs a boundary or interior mesh. This is the
cost of the specified consumers, not an optimal-complexity claim.

[note]: ../notes/01_BOUNDED_THETA_CHARGE_AND_DIRECT_COMPARISON_20261021.md

## Exact boundary-degree controls

[The second script](check_boundary_degree_controls.py) replays the
piecewise affine boundary construction in [Note 02][note02]. It uses
only the Python 3 standard library (on a POSIX system for its 180-second
execution budget). From this directory:

```sh
python3 check_boundary_degree_controls.py --out /tmp/RCH12_BOUNDARY_REPLAY.json
```

The [small receipt](BOUNDARY_DEGREE_CONTROLS_20261021.json) records rational
control parameters, interpolation bounds, signed degree results,
counts, a rational regular target and the script hash. The four controls
return degrees +1, −1, +1 and 0. The last uses 1,776 boundary vertices and
10,368 tetrahedra, with whole-boundary homotopy gap at least 17/40.
No actual interior field values are sampled. No theta source values are
acquired by this script.

The script rejects an unpaid boundary simplex, ambiguous regular target,
wrong expected degree or incomplete boundary count before writing a
success receipt. Fractions decide signs exactly; rational square-root
lower bounds use integer square roots. Large vertex/simplicial arrays
are regenerated in memory rather than stored in the repository.
Elapsed times vary. These controls are not an interval theta run,
formal proof or independent validation. See the [self-review][review02]
for the analytic and implementation checks and their limits.

[note02]: ../notes/02_HOLOMORPHIC_REFERENCE_TRANSFER_AND_BOUNDARY_DEGREE_20261021.md
[review02]: ../reviews/02_REFERENCE_TRANSFER_AND_BOUNDARY_DEGREE_REVIEW_20261021.md

## Complete theta: two neighboring zeros

[The third script](certify_two_zero_boundary_comparison.py) executes the
[declared experiment](TWO_ZERO_EXPERIMENT_PLAN_20261021.json) and
[Note 03][note03]. It requires `python-flint==0.9.0` and the two earlier
scripts in this directory. From this directory:

```sh
python3 certify_two_zero_boundary_comparison.py --out /tmp/RCH12_TWO_ZERO_REPLAY.json
```

The 192-bit run acquires four jets at each of 257 anchors on the boundary
face `Re(t)=-1/100`, plus four complete moments: 1,032 scalar integrals.
Validated source tails, Taylor lifting, real-root counts and all
interpolation errors are included. The 2,056 rational boundary vertices
feed both the 9,228-tetrahedron degree consumer and the 256-cell direct
tensor consumer. No actual interior field anchor is used by either.

The [receipt](TWO_ZERO_THETA_COMPARISON_20261021.json) reports charge zero,
boundary gap >3.5683e−7, direct joint floor >3.9348e−7, exact two-root
and one-stationary-point brackets, fresh anisotropic controls and cost
counts. It binds this script and both companion scripts by SHA-256.
Arrays are regenerated in memory; their hash is an identity check, not a
mathematical proof. Elapsed times depend on the run. The script enforces
the declared acquisition and 180-second limits, strict payments, regular
target checks and coverage assertions before writing a success record.

A development audit replaced interior time-zero anchors with boundary
negative-time anchors; the saved receipt and script use the corrected
version. The [self-review][review03] describes that change and the
analytic verification. The finite comparison favors direct interpolation;
this does not establish a universal cost ordering or global simplicity.

[note03]: ../notes/03_TWO_ZERO_THETA_BOUNDARY_AND_DIRECT_COMPARISON_20261021.md
[review03]: ../reviews/03_TWO_ZERO_THETA_COMPARISON_REVIEW_20261021.md

## Complete theta application of the real cap theorem

[The real-cap verifier](certify_real_cap_application.py) implements
[Note 06](../notes/06_COMPLETE_THETA_WALLS_AND_REAL_CAP_APPLICATION_20261021.md)
under the [predeclared plan](REAL_CAP_APPLICATION_PLAN_20261021.json).
It uses python-flint 0.9.0 and `certify_relative_charge_pilot.py` for
complete moment acquisition and source-tail payments. From this folder:

```sh
python3 -B certify_real_cap_application.py --out /tmp/RCH12_REAL_CAP_REPLAY.json
```

The fixed 192-bit calculation covers |Re t|,|Im t|<=.01 and circles
centered at 71/2 with radii 8 and 10. Sixteen time-zero complex jets at
129 anchors per circle, conjugation and degree-seven joint Taylor
expansion pay whole arcs and all times. Ten complete moments supply the
remainder. Eight real-cap values give two disjoint root brackets per cap.
The total is 4,146 complete source integrals; it does not acquire a
four-dimensional boundary mesh or a complex-time discriminant curve.

The [receipt](REAL_CAP_THETA_APPLICATION_20261021.json) records wall floors
>8.36937e-7 and >7.57583e-7, spatial counts (2,2), |A|<3.489078,
K tau<.034891, both cap discriminants >144, and charge zero. Three exact
quadratic controls pass through the same wall/ratio/winding consumer
and return charges 1,0,0 after their exact cap signs. The script fails
before writing success if any wall, winding, phase, cap or budget check
fails. Limits are 5,000 source integrals and 180 seconds; the final run
took about 16.1 seconds. This is not a matched speed comparison.

Script, helper, plan and regenerated source-array hashes bind the small
record. Arrays are recreated in memory. Times and binary arithmetic
behavior can vary across environments; hashes are identity checks,
not mathematical hypotheses. All original theta modes and exterior
source integrals are paid. The
[review](../reviews/06_COMPLETE_THETA_REAL_CAP_APPLICATION_REVIEW_20261021.md)
is by the producing assistant. The certificate concerns a well-separated
finite pair, without a global or near-event endpoint claim.

## Endpoint-program exact algebra controls, 21 October 2026

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. [ece_exact_controls.py](ece_exact_controls.py)
uses Python's standard library and exact rational arithmetic; run it to
stdout to reproduce [ECE_EXACT_CONTROLS_20261021.json](ECE_EXACT_CONTROLS_20261021.json).
It checks Hermite discriminants for m=2–8, finite clusters retaining
nonzero exterior forcing, cubic forcing and quadratic source response.
These are algebra checks, not new theta source acquisition, interval
certification, or a substitute for the proofs. See the
[opening-round review](../reviews/08_ENDPOINT_CHARGE_OPENING_ROUND_REVIEW_20261021.md).

## Finite-time reconstruction and covariance controls, 21 October 2026

Prepared for Edward Baker with substantial LLM assistance,
**gpt-6-astra, actual effort ultra**. The standard-library rational
[reconstruction script](ftsr_exact_controls.py) checks polynomial Gaussian
transfer, Hermite projection, exact response reduction modulo P²,
nonconstant exterior units, confluent roots and affine heat collisions.
The separate [covariance script](ftsr_covariance_controls.py) imports its
small algebra helpers and checks continuous laws with atoms, signed
covariance errors, exact cell-range containment and deliberate omission
of the mixed correction. From this directory:

```sh
python3 -B ftsr_exact_controls.py --output /tmp/FTSR_REPLAY.json
python3 -B ftsr_covariance_controls.py --output /tmp/FTSR_COVARIANCE_REPLAY.json
```

The [first receipt](FTSR_EXACT_CONTROLS_20261021.json) records 862 exact
algebra checks. The [second receipt](FTSR_COVARIANCE_CONTROLS_20261021.json)
records 96 covariance cases, six strict containment examples and three
rejections of the dropped-mixed-term error. Its mixed-term counts overlap
the covariance cases and must not be counted as extra independent cases.
Receipts bind scripts/helpers by SHA-256; hashes identify the source and
do not prove the mathematics. These controls acquire no theta values and
are not a canonical-source certificate, independent specialist review,
or endpoint exclusion. [Review 12](../reviews/12_FINITE_TIME_SIGNED_RECONSTRUCTION_OPENING_REVIEW_20261021.md)
records the analytic checks and the separate internal rerun.
