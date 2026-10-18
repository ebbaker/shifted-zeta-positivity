# Fixed source measurement replay

17 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model **gpt-6.1-sol (Codex)**, reasoning effort **ultra**.

This directory contains the code and small records for
[Note 02](../../notes/round-1/02_EXPLICIT_THETA_JET_AND_ENDPOINT_BOUNDS_CODEX_20261017.md)
and [Note 03](../../notes/round-1/03_BOUNDED_REPLAY_AND_POSITIVE_FEASIBILITY_CODEX_20261017.md).
The fixed replay has six observations, 24 conditioning combinations and
32 equality/nonnegative-feasibility combinations. No height threshold or
support sweep is included. Formal review occurs at the investigation round
boundary; these are the current computational records.

## Reproduce

Requires Python, `mpmath` and `python-flint`. The recorded environment used
Python 3.10.0, mpmath 1.4.1 and python-flint 0.9.0. Run from this directory,
choosing a working output directory outside the checkout:

```sh
python3 run_replay.py --output-dir /tmp/source-measurement-replay \
  --original-record ../../../../brainstorm/investigations-3/numerics/CHECK_CODEX_RESPONSE_REPLY_CLAUDE_20261016.json
```

The original floating record is read only for comparison after the independent
implementation. It is not an arithmetic input to the new solves. Omitting
`--original-record` omits that comparison. No machine-specific dependency
path is embedded in the code; use a Python environment containing the two
libraries.

The producer runs one 80/120-decimal-digit comparison with thin QR/SVD and
enumerates the declared small active sets. Separate 448-bit Arb computations
enclose the integrals and analytic tails, verify rank/inverse identities,
check Farkas signs and bound Euclidean optima. The recorded run took about
29 seconds; the largest child process used about 32 MiB peak RSS, within the
1800-second and 1-GiB contract. Full floating outputs are regenerable working
data and are not versioned here. No large archive is required.

## Retained records

| Record | What it establishes or records |
| --- | --- |
| [CERTIFIED_EVALUATION.json](CERTIFIED_EVALUATION.json) | Complete-integral jet enclosures, individual numerical tail allowances and the omitted coefficient tail |
| [CERTIFIED_MEASUREMENTS.json](CERTIFIED_MEASUREMENTS.json) | Injective measurements, rank-two jets, optimal operator constants, sufficient radii and actual unconstrained measurement distances |
| [FEASIBILITY_WITNESSES.json](FEASIBILITY_WITNESSES.json) | Compact candidate decimal separating multipliers and augmented-minor specifications |
| [CERTIFIED_FEASIBILITY.json](CERTIFIED_FEASIBILITY.json) | Interval verification of 26 nonnegative infeasibility witnesses, 6 feasible first-N-coordinate Euclidean optima and all 32 equality classifications |
| [ANALYTIC_BOUND_CHECKS.json](ANALYTIC_BOUND_CHECKS.json) | Finite constants for the complete-theta bound, exact carrier normalization and five independent time-zero jet checks |
| [REPLAY_SUMMARY.json](REPLAY_SUMMARY.json) | Environment, precision comparison, runtime, scope, source and code hashes |

The interval producers bind their inputs by SHA-256 in the records. The
summary binds all retained records and code. Hashes establish identity,
not the validity of a mathematical argument; a regenerated certificate
must pass its arithmetic checks. Runtime-dependent summary bytes may change
on a replay. The analytic contour and infinite-tail proofs are in Note 02
and Note 03, not supplied by successful finite checks alone.

The fixed theta-tail coefficient class preserves exact primitive
normalization; the zero-tail class has its separate affine normalization.
A finite coordinate distance for a zero-tail source is not a finite full
raw distance from theta. Weighted distances are values at Euclidean optima,
not weighted optima. All errors in the conditioning table are absolute in
the declared raw row units.

Follow [LARGE_FILES.md](../../../../../LARGE_FILES.md). Each retained record
is small; regenerable full floating output stays outside the checkout.

## Concrete analytic onset budget

[Note 05](../../notes/round-1/05_CONCRETE_NORMALIZED_ONSET_BUDGET_CODEX_20261017.md)
uses a separate fixed-pair calculation, not an expansion of the six-point
replay. The [producer](concrete_onset_budget.py) and
[interval record](CONCRETE_ONSET_BUDGET.json) evaluate derivative majorants,
the determinant threshold and coefficient/measurement upper bounds.
The record binds its producer by SHA-256 and carries the fixed contract,
environment and resource record. The original replay summary continues to
identify the original replay; it is not relabelled as this later calculation.

```sh
python3 concrete_onset_budget.py --output /tmp/CONCRETE_ONSET_BUDGET.json
```

The prescribed rounding rule gives x at least 3915, uniformly in heat time
from zero through one quarter. The coefficient change bound is below
4e-307; this is a sufficient construction, not an optimal distance or a
measured first event. No new physical integrals, grid or support search run.


## Round-two record-hygiene correction

17 October 2026, prepared for Edward Baker with substantial LLM assistance,
gpt-6.1-sol, effort ultra. The runner now reports stored-file and canonical
mathematical-content hashes separately, using
[replay_record_hygiene.py](replay_record_hygiene.py), and converts Linux KiB
and macOS byte RSS values explicitly. The canonical projection retains
serialized enclosures, witnesses, precision, scope and mathematical hash
references. It removes only its documented execution/environment and
stored-file/code provenance fields. This is identity in the tested
environments, not arithmetic portability or mathematical validity.
The [two-run verification](../round-2/REPLAY_HYGIENE_CHECKS_CODEX_20261017.json)
confirms all five historical retained records' mathematical contents.
Historical certificates and their original summary remain unchanged.
See [round two](../round-2/README.md) for reproduction.
