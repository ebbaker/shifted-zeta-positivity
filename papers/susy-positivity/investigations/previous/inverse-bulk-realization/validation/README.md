# Manuscript and draft checks

[drafts.py](drafts.py) records reviewed builds, saves complete dated snapshots,
and verifies current and historical file hashes. See the [build guide](../BUILD.md)
for the workflow. The save operation refuses to overwrite an existing version.

```sh
python3 validation/drafts.py check --replay
```

The optional replay compares all four algebra programs with the preserved
records. It does not update them, compile TeX, inspect page layout, or prove
the mathematical claims. Historical snapshots carry the same tool so they
can be checked in isolation.
