# Shared setup records

13 November 2026. Prepared for Edward Baker with OpenAI Codex assistance;
actual backend model and effort unavailable in recorded configurations.

The [branch setup manifest](01_BRANCH_SETUP_INPUT_MANIFEST_20261113.json)
records inherited file identities for branches 02–04. It is housekeeping,
not a computation of the Newman flow. Future branch computations belong
in their branch and require their own defined scope. Follow
[LARGE_FILES](../../../LARGE_FILES.md).

The [parent-plan input manifest](02_PROGRAM_PLAN_INPUT_MANIFEST_20261113.json)
records pre-edit sources for the subsequent collection planning setup.
It is a provenance record, not a new numerical experiment or proof check.

The [branch-planning input manifest](03_BRANCH_PLAN_INPUT_MANIFEST_20261113.json)
records pre-edit identities for creating the JCH/VCD/ITP plans/registers
and refreshing QTT and parent navigation. It does not record a research run.

## Finite acquisition records, 14 November 2026

Prepared for Edward Baker with OpenAI Codex assistance. B02 used Astra/Ultra; E02/E03 use Sol 6.1/Ultra; coordinator backend/effort unavailable.

- [07 — actual runtime inventory](07_TN6_B02_RUNTIME_INVENTORY_20261114.json).
- [08 — E02 frozen source identities](08_TN6_E02_R1_INPUT_MANIFEST_20261114.json).
- [09 — exact-rational E02 certificate](09_TN6_E02_R1_CERTIFICATE_20261114.json) and [generator](execute_tn6_e02_r1.py).
- [10 — E03 assessment input identities](10_TN6_E03_R1_INPUT_MANIFEST_20261114.json).
- [11 — E03 exact validation and replay receipt](11_TN6_E03_R1_ASSESSMENT_RECORD_20261114.json) and [rational validator](assess_tn6_e03_r1.py).

The certificate preserves the failed 128-bit allowance and successful 256-bit attempt. The [execution note](../notes/06_TN6_E02_CERTIFIED_COEFFICIENT_ACQUISITION_20261114.md) gives scope and replay requirements.

After the assessed summary update, the live cluster 18 has an appended
finite-acquisition result. The frozen generator correctly rejects changed
input bytes. The [editorial receipt](12_TN6_POST_ACQUISITION_GUIDANCE_UPDATE_20261114.json)
and [staging helper](prepare_tn6_e02_replay.py) restore its exact historical
input in a new temporary directory, verifying all 25 frozen files. No
scientific source or generator guard is weakened. Metadata preflight is
recorded in [13](13_TN6_FINAL_RECORD_CHECK_20261114.json).

```sh
tn6_replay_root=$(python3 papers/investigations-6/numerics/prepare_tn6_e02_replay.py)
# Use a Python containing python-flint 0.9.0 / FLINT 3.6.0 for the numerical replay.
python3 "$tn6_replay_root/papers/investigations-6/numerics/execute_tn6_e02_r1.py" \
  --output "$tn6_replay_root/replay-certificate.json"
```

Staging does not run the numerical calculation. Original E02 outputs are
never overwritten. Future scientific runs still require their applicable
bounded contract; this command explains replay, not a new campaign.

## Analytical manuscript records, 14 November 2026

For Edward Baker with OpenAI Codex assistance; manuscript/review workers
Sol 6.1/Ultra, coordinator backend/effort unavailable. These are document
and provenance checks, not new numerical experiments.

- [14 — thirty frozen proof sources](14_TN6_E04_MANUSCRIPT_INPUTS_20261114.json).
- [15 — combined external build](15_TN6_ANALYTICAL_MANUSCRIPT_BUILD_20261114.json), with [builder](build_analytical_manuscripts.py).
- [16 — cross-manuscript analytical assessment identities](16_TN6_MANUSCRIPT_CROSS_REVIEW_20261114.json).
- [17 — exact manuscript-summary append receipt](17_TN6_MANUSCRIPT_GUIDANCE_UPDATE_20261114.json).
- [18 — final source, document and layout checks](18_TN6_MANUSCRIPT_FINAL_CHECK_20261114.json).

The staging helper now verifies the two registered summary appends in
reverse order (17, then 12), restoring the unchanged E02 input. The
manuscript map needs only receipt17 to restore its frozen summary version.
Build reading PDFs into a new external directory, for example:

```sh
python3 papers/investigations-6/numerics/build_analytical_manuscripts.py \
  --output-dir /private/tmp/tn6-reading-copies \
  --record /private/tmp/tn6-reading-copies-build.json
```

The helper rejects an output directory inside the repository. The current
reading copies and previews are temporary; retained TeX supplies the rebuild.
