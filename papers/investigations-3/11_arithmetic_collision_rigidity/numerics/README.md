# Arithmetic constraints at collision scale: numerics

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model: **gpt-6-astra (Codex)**; reasoning effort:
**max**, verified from the authoring turn metadata.

## Opening round checks

[check_packets_and_orbits.py](check_packets_and_orbits.py) and its
[execution record](PACKET_AND_ORBIT_CHECKS_20261018.json) use python-flint
at 384 bits for two bounded tasks:

- Check complete d=2,3,6 packet formulas and their first two derivatives at
  t=1/4, z=30+i/3, including reflected signs and analytic source/integration tails.
- Certify the invertibility, coefficient bound, and nonzero third source
  endpoint for one exactly defined infinite-orbit direction on rough seeds
  5,7,11. Primitive normalization and the first odd source endpoint vanish
  by the complete-sum definitions.

The retained run took under one second. These are same-assistant checks.
No collision location or theta positivity is numerically certified. The
[analytic theorem](../notes/03_FINITE_PRIME_COMPATIBLE_COLLISION_CONTROLS_CODEX_20261018.md)
supplies existence at unspecified sufficiently high gaps.

Requires Python with python-flint. To replay without replacing the retained
record:

```sh
python3 check_packets_and_orbits.py --output /tmp/inv11-packet-orbit-replay.json
```

The script records its source hash, precision, runtime, parameters and scope.
Runtime fields can change on replay; a matching hash is provenance, not
mathematical validation.

## Positive packet bounds

[check_positive_packets.py](check_positive_packets.py) and the
[retained record](POSITIVE_PACKET_BOUNDS_20261018.json) certify constants in
[Note 04](../notes/04_POSITIVE_ARITHMETIC_PACKETS_AND_MODULAR_CANCELLATION_CODEX_20261018.md)
using 384-bit Arb/Acb arithmetic. The all-height sign and relative estimates
are proved analytically. The checker verifies scalar constants, the first
modular endpoint with an infinite tail bound, and eight finite-interval
integration identities with their upper boundaries. Omitting the boundary
is rejected. It certifies no theta sign or collision. The recorded run took
about 0.023 seconds; assessment is by the same assistant.

```sh
python3 check_positive_packets.py --output /tmp/inv11-positive-packets-replay.json
```

## Manuscript constant enclosures

[certify_manuscript_constants.py](certify_manuscript_constants.py) uses only
Python's standard library and exact fractions. Machin's formula, an
alternating arctangent remainder, a positive exponential-series remainder,
and outward dyadic interval rounding certify every printed table interval
and headline constant in the manuscript. The [record](MANUSCRIPT_CONSTANTS_20261018.json)
contains exact rational endpoints, outward decimal endpoints, the script
hash, and the bounds checked. All checks passed. This is an additional
arithmetic implementation by the same assistant, not independent review.

```sh
python3 certify_manuscript_constants.py --output /tmp/inv11-manuscript-constants-replay.json
```

No oscillatory integral, event height, all-height theta sign, or analytic
proof is certified by this scalar calculation. The manuscript derives the
uniform estimates separately.

Keep reproducible code and small records here, with parameters, precision,
method, errors, source identities and the exact bounded claim checked. Label
floating-point diagnostics separately from certificates. Favorable finite
checks do not support the all-event criterion in the [shared plan][overview].
Follow the [large-file policy][large] for derived data; no large outputs or
third-party PDFs belong in this folder.

[overview]: ../../research-overview/02_EXPLORATORY_FIXED_FUNCTION_RESEARCH_PLAN_20261018.md
[large]: ../../../../LARGE_FILES.md

## Strip-carrier continuation, 18 October 2026

[certify_strip_carriers.py](certify_strip_carriers.py) and
[STRIP_CARRIER_CHECKS_20261018.json](STRIP_CARRIER_CHECKS_20261018.json)
replay all original scalar checks and certify the improved real remainder
derivatives, the complex ratio below 8.5e-25, and example shifted-mode tail
constants. The checker reuses the original exact-rational interval code;
it is not an independent implementation. No quadrature or nonzero physical
margin is certified. Prepared for Edward Baker with substantial LLM
assistance, **gpt-6-astra, ultra**.

```sh
python3 certify_strip_carriers.py --output /tmp/inv11-strip-carriers-replay.json
```

## Revised manuscript table, 18 October 2026

[certify_updated_manuscript.py](certify_updated_manuscript.py) verifies all
nine current table rows and eight headline bounds and replays the original
checks. [The record](UPDATED_MANUSCRIPT_CONSTANTS_20261018.json) retains
exact rational endpoints and source identities. The final three intervals
enclose conservative shifted constants using cos(pi/4) > 7/10. This wrapper
reuses the original interval engine; it is not an independent implementation.
Prepared for Edward Baker with substantial LLM assistance, **gpt-6-astra,
ultra**, coordinating the Sol manuscript integration.

```sh
python3 certify_updated_manuscript.py --output /tmp/inv11-updated-manuscript-replay.json
```

This is the current manuscript table certificate. Earlier records retain
their historical scopes. No retained-mode quadrature or positive physical
jet margin is certified.

## Overview 02 evaluator and bounded program

18 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort max**. Requires Python with python-flint 0.9.0;
recorded runtime Python 3.12.14. This is same-assistant internal interval
verification on already covered territory, not a new global Newman bound.

- [Stage 0 replay](STRENGTHENED_MANUSCRIPT_REPLAY_20261018.json) pins the strengthened manuscript and all three exact scalar replays.
- [Baseline summary](BASELINE_REPLAY_SUMMARY_20261018.json) binds the original 786-check winding/interior replay and unchanged geometry hashes.
- [Evaluator](certify_shifted_theta_jet.py) and [validation](SHIFTED_EVALUATOR_VALIDATION_20261018.json) supply complete finite errors and 128-strip first-jet coverage.
- [Predeclared parameters](PREDECLARED_STAGE2_STAGE3_20261018.json), [pilot driver](run_plan02_pilot.py) and [comparison](SHIFTED_PILOT_COMPARISON_20261018.json) record source-specific control event rejection and the failed performance gate.
- [Signed certificate](COMPLETE_MODULAR_SIGNED_ESTIMATE_20261018.json) gives L0>E/100 on [1/100,1/5] × [25,45], with 314 full-time strips.
- [Replay script](replay_plan02_certificates.py) and [claim ledger](FINAL_CLAIM_LEDGER_20261018.json) recalculate every signed cell at 256 bits and run fifteen failure/regression checks.
- [Global budget](GLOBAL_CONSUMER_BUDGET_20261018.json) records the unclosed finite bridge. It establishes no new Newman bound.

From the repository root, use a fresh external output directory. The model
and effort arguments below reproduce the recorded configuration labels;
future runs must use their actual recorded settings. The pilot driver
executes the original source checkers itself into the temporary receipt
folder, binds the fresh output bytes, and rejects changed data or sources.
The final replay checks source/code and validation hashes before reuse.

```sh
mkdir -p /tmp/inv11-plan02-replay
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/certify_shifted_theta_jet.py --output /tmp/inv11-plan02-replay/SHIFTED_EVALUATOR_VALIDATION_20261018.json --execution-model gpt-6.1-sol --execution-effort max
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/run_plan02_pilot.py --repo . --receipts /tmp/inv11-plan02-replay --validation /tmp/inv11-plan02-replay/SHIFTED_EVALUATOR_VALIDATION_20261018.json --declaration papers/investigations-3/11_arithmetic_collision_rigidity/numerics/PREDECLARED_STAGE2_STAGE3_20261018.json --output /tmp/inv11-plan02-replay/SHIFTED_PILOT_COMPARISON_20261018.json --signed-output /tmp/inv11-plan02-replay/COMPLETE_MODULAR_SIGNED_ESTIMATE_20261018.json --execution-model gpt-6.1-sol --execution-effort max
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_plan02_certificates.py --repo . --records /tmp/inv11-plan02-replay --output /tmp/inv11-plan02-replay/FINAL_CLAIM_LEDGER_20261018.json --budget-output /tmp/inv11-plan02-replay/GLOBAL_CONSUMER_BUDGET_20261018.json --execution-model gpt-6.1-sol --execution-effort max
```

The analytic derivation and arithmetic-square repair are in the
[overview 02 notes](../notes/02_updated_research_plan/README.md). Quad radii
include internal rounding; subsequent arithmetic is enclosed in the exact
polynomial's outward image. The listed added error is not a license to
discard the radius of a returned cell enclosure. Timing and interval
subdivision details can change across environments; hashes identify the
recorded artifacts, not mathematical truth or bit-for-bit portability.

## Effective near-boundary tail and point evaluation

18 October 2026, for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**. [Note 11](../notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md)
derives the nonstationary estimate and all error contracts;
[Review 10](../reviews/10_EFFECTIVE_NONSTATIONARY_TAIL_AND_POINT_EVALUATOR_REVIEW_20261018.md) records internal same-model checks.

- [Scalar checker](certify_nonstationary_mode_tail.py) and [192-bit record](EFFECTIVE_NONSTATIONARY_TAIL_20261018.json) verify explicit uniform constants, direct frozen-bound comparisons and rejection of invalid contours. The proof, rather than sampled heights, covers the unbounded range.
- [Point evaluator](bounded_near_boundary_evaluator.py) and [160-bit record](NEAR_BOUNDARY_POINT_EVALUATION_20261018.json) pay mode, retained-source, quadrature and arithmetic errors at t=1/10, x=1000 and x=10000; a second frozen contour replays x=1000. Every component error is below 1e-8 G0. These are point evaluations, not whole-cell exclusion or a performance comparison.
- [Control wrapper](replay_nonstationary_controls.py) and [fresh replay](NONSTATIONARY_CONTROL_REPLAY_20261018.json) reuses the pilot's source-specific interface and rejects five event boxes plus the separate Euler-factor negative-Laguerre witness.

Replay from the repository root with Python and python-flint 0.9.0, writing
outside the repository:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/certify_nonstationary_mode_tail.py --repo . --output /tmp/inv11-effective-tail.json --model gpt-6.1-sol --effort ultra
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/bounded_near_boundary_evaluator.py --repo . --output /tmp/inv11-near-boundary-points.json --execution-model gpt-6.1-sol --execution-effort ultra
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/inv11-near-boundary-controls --output /tmp/inv11-near-boundary-controls.json --execution-model gpt-6.1-sol --execution-effort ultra
```

Use actual execution settings in future records. The control wrapper uses the established pilot interface at 192 bits,
with source-specific imported precision and fresh external receipts; code
and receipt hashes are bound in the record. All retained files remain below the large-file limit.

## High height signed and vertical wall consumers

[Reproducible code and records](high_height_consumer/README.md) consume
Note 11's new arithmetic tail in 40 closed signed cells and seven complex
wall cells. [The ledger](high_height_consumer/HIGH_HEIGHT_CONSUMER_LEDGER_20261018.json)
binds the finite-height consequence, published inputs, failed timing gate
and remaining global bridge. Fresh 256-bit and independent real-contour
replays pass. For Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**, 18 October 2026; same-model internal work.

## Final analytic continuation records

[Analytic continuation replay](analytic_continuation/README.md) reproduces
Note 14's exp(20/epsilon) real exterior, constant-distance arithmetic tail
and exact remote polynomial control. It includes source identities,
192/256-bit overlap checks, parameter rejection and measured scalar cost.
The new ledger supersedes the old outer threshold, with the finite
certificates unchanged. For Edward Baker with substantial LLM assistance,
**gpt-6.1-sol, actual effort ultra**, 18 October 2026; same-model checks.
Global coverage remains open.
