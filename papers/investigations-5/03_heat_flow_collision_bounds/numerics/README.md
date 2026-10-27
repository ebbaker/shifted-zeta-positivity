# Numerical work

26 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort max**.

No research computation accompanies setup. Before a numerical task freeze
finite cases, complete populations, source versions, encodings, continuous
error allocation, comparator and stop rules in the HCB register.
Distinguish floating exploration from interval/rational certification.
Keep code and small records here; large data and working PDFs follow
[LARGE_FILES.md](../../../../LARGE_FILES.md). Add an archive guide and
hash-bound loader when external derived data are first introduced.

## Fixed endpoint/count pilot and retained-data witness

26 October 2026. Prepared for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), actual recorded effort ultra**.

The [protocol](../notes/05_ENDPOINT_COUNT_PILOT_PROTOCOL_20261026.md) fixed
one source case, m=16, before execution. Python3 and **python-flint 0.9.0**
at 192 bits are required. [Source script](01_certify_frozen_endpoint_count_20261026.py)
uses exact initial xi factors and conditional real-zero Gaussian transport.
Its [raw record](FROZEN_ENDPOINT_COUNT_RECORD_20261026.json) remains
**stopped** at the first nonfinite capped contour integral; no retry or
other finite case was run.

A separate [verifier](02_verify_retained_endpoint_count_20261026.py) makes
zero source calls. Its [witness](RETAINED_ENDPOINT_COUNT_WITNESS_20261026.json)
proves under RH uniform endpoint floors 0.8144/0.2789, complete count 1
including multiplicity, and full canonical wall floor 0.0697 for this case.
It does not certify F_N mismatch/coefficient errors or a uniform-m result.
The count is a post hoc deduction from retained data, not a successful
continuous-integration stage. See [Note06](../notes/06_REAL_ENDPOINT_TRANSPORT_AND_FINITE_COUNT_20261026.md)
and [Review04](../reviews/04_REAL_ENDPOINT_AND_FINITE_COUNT_INTERNAL_REVIEW_20261026.md).

From this investigation's root, verify the preserved witness without new
source evaluations:

```sh
python3 numerics/02_verify_retained_endpoint_count_20261026.py \
  --record numerics/FROZEN_ENDPOINT_COUNT_RECORD_20261026.json \
  --expected-sha256 2acb74e40eb7344bc7f2343782ecfda6a251b8a6e01d81a4fdefa7b79df27188 \
  --source-script numerics/01_certify_frozen_endpoint_count_20261026.py \
  --output /tmp/hcb-retained-witness-replay.json
```

The source script's failed protocol is preserved for inspection. Repeating
source values or changing its cases/tolerances needs a new explicit bounded
protocol; do not overwrite the historical raw record. These files are small
and introduce no external derived archive or generated PDF.
