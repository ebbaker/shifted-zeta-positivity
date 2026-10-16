# Manuscript and draft checks

[drafts.py](drafts.py) records reviewed builds, saves complete dated snapshots,
verifies current and historical file hashes, and replays every program in its
`CHECKS` dictionary against the preserved records in
[`../numerics/records/`](../numerics/README.md). See the
[build guide](../BUILD.md) for the workflow.

```sh
python3 validation/drafts.py check --replay
```

The save operation refuses to overwrite an existing version, and `record`
refuses a build whose log shows undefined references, multiply-defined labels or
overfull boxes, or whose `manuscript.pdf` differs from `build/manuscript.pdf`.
None of this compiles TeX, inspects page layout, or proves a mathematical claim:
it establishes file identity, build provenance and reproducibility of the finite
checks. Historical snapshots carry the same tool so they can be checked in
isolation.
