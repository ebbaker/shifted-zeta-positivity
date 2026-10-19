# S07 checks and execution records

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance; **gpt-6.1-sol (Codex), actual effort ultra**.

The opening note reuses the canonical
[S06 geometric checker](../../06_hodge_and_transverse_geometry/numerics/check_geometric_symmetry_coverage.py),
which verifies 61 exact rational identities covering quaternion matrices,
pairing and curvature signs, J/K insertions, diagonal Hessian corrections,
primitive compensation and the pointwise-J closedness counterexample.
Its implementation remains in S06; do not copy or relocate it for S07.

The [fresh S07 replay](GEOMETRIC_SYMMETRY_INITIAL_REPLAY_20261018.json)
records execution against the current sources. The separate
[setup/source record](INITIAL_NOTE_SOURCE_RECORD_20261018.json) pins this
investigation's initial documents and inherited references. Historical
S06 receipts remain unchanged, even where a guide hash later changes.

Reproduce from the repository root:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/06_hodge_and_transverse_geometry/numerics/check_geometric_symmetry_coverage.py --repo . --output /tmp/s07_initial_geometric_replay.json
```

The reused checker retains its original authorship and points to S06
Review 03 for the analytic arguments. The [S07 note](../notes/01_POINCARE_DUALITY_AND_QUATERNIONIC_SYMMETRY_INITIAL_FINDINGS_20261018.md)
consolidates their use here. This is finite algebra, not a new collision
certificate or evidence for a global sign. The interval signed certificate
and inherited event controls were not freshly rerun for this organizational
opening. A future estimating method must execute its applicable controls.

Save new S07-specific code and small replayable records here. Keep bulk
derived data outside Git under the repository large-file policy.


## Zero-form Green and trace round

18 October 2026. For Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), actual effort ultra**. The
[checker](check_green_identity_and_trace.py) and
[exact record](GREEN_IDENTITY_AND_TRACE_CHECKS_20261018.json) verify
93 rational matrix/exterior/polynomial and Gaussian-moment identities.
The polynomial concentration sequence illustrates flat C1 scaling; the
smooth actual-bundle obstruction is proved in [Note 02](../notes/02_ZERO_FORM_GREEN_IDENTITY_AND_PHYSICAL_TRACE_OBSTRUCTION_20261018.md).

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry/numerics/check_green_identity_and_trace.py --repo . --output /tmp/s07_green_identity_checks.json
```

[Fresh canonical control replay](S07_GREEN_SOURCE_CONTROLS_20261018.json)
rejects five event boxes and the separate Euler negative-Laguerre witness.
This validates inherited strict physical interfaces, not a new Green
inequality. The record includes source-specific enclosures and hashes;
small intermediate receipts are regenerable and were kept in temporary
storage. The current execution used Python 3.10 and python-flint 0.9.0;
the interface precision was 192 bits, with imported receipts retaining
their recorded precision.

In an environment with python-flint installed, reproduce the controls
from the repository root:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/numerics/replay_nonstationary_controls.py --repo . --receipts /tmp/s07_control_receipts --output /tmp/s07_source_controls.json --execution-model gpt-6.1-sol --execution-effort ultra
```

The [internal review](../reviews/02_GREEN_IDENTITY_AND_TRACE_OBSTRUCTION_INTERNAL_REVIEW_20261018.md) distinguishes the analytic
proof, finite algebra, control replay and remaining theta-specific gap.
The original setup manifest remains a historical pin, not a hash of later
edited guides. No new physical sign, region or complete-error gain is claimed.
