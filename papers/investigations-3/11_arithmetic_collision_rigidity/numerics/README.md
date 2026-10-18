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
