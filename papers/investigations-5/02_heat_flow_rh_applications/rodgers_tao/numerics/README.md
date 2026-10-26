# Rodgers–Tao computations and certificates

Updated 26 October 2026 for Edward Baker with substantial LLM assistance,
**gpt-6.1-sol (Codex), actual recorded effort ultra**.

The [r2 checker](certify_rt03_rt04_r2.py) and
[small certificate](R2_CANONICAL_TWO_ROOT_CERTIFICATE_20261026.json)
acquire canonical contour/root data and pay the two-root exterior-force
term on `t in[1/20000,1/10000]`, `z in(26,46)+i(-2,2)`.
See [Note03](../notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md),
[Assessment02](../reviews/02_CANONICAL_TWO_ROOT_ACQUISITION_ASSESSMENT_20261026.md)
and [work record](../notes/03_R2_INPUTS_AND_WORK_RECORD_20261026.json).

This is an interval-certified known-covered compact acquisition pilot,
with same-model checks only. It adds no Newman bound or noncollision
coverage. The contour upper budget loses to the direct actual-root
budget by about 309.53; the paired transfer allowance loses to the
separate-drift allowance by about 6.88721. These compare certified upper
budgets, not true-error lower bounds or runtime speedups.

Replay from a checkout with Python and `python-flint==0.9.0`:

```sh
python3 -B papers/investigations-5/02_heat_flow_rh_applications/rodgers_tao/numerics/certify_rt03_rt04_r2.py \
  --repo-root "$PWD" --output /tmp/rt-r2-replay.json
```

The script uses the existing HDC13 core at its repository-relative
path and checks its recorded SHA256 before import. It regenerates the
canonical coefficient enclosures and performs the arithmetic gates;
no local zero cache or external numerical data is required. A changed
core needs inspection and an explicit input-record update, not removal
of the hash check. Rounding/library versions and script hashes are in
the certificate. Byte hashes identify versions, not proof validity or
cross-platform bitwise reproducibility.

Rejection check: run with a **fresh output path** and
`--inject-wall-error 1/1000000`. The contour margin must fail with a
nonzero exit and no new PASS artifact. The successful run uses injection 0.
Do not interpret an older output file left by another run as success
after a failed process.

Keep generated bulk data, package installations, raw transcripts and
third-party PDFs outside Git, following
[LARGE_FILES.md](../../../../../LARGE_FILES.md). No sweep or manuscript
PDF was produced for this return.
