# Validation and provenance

[drafts.py](drafts.py) records a visually inspected exposition and supplementary build,
preserves new dated snapshots without overwriting them, and verifies current
and archived source/PDF identity for both documents. Historical single-document
records remain supported. Its `check --replay` mode runs the 268
standard-library diagnostics with the original parameters and thresholds.
It is portable with each saved manuscript. See [BUILD.md](../BUILD.md) and
[BUILD_RECORD.json](../BUILD_RECORD.json).

[check_package.py](check_package.py) is the broader live-repository inventory.
It records every current package file except its own record and temporary
build/cache files, including the dated snapshots. It also pins inherited
research inputs in neighboring investigations. The current inventory is
[PACKAGE_RECORD.json](../PACKAGE_RECORD.json).

From the investigation directory:

```sh
python3 validation/drafts.py check --replay
python3 validation/check_package.py check --replay
```

Both replay modes require identical parameters, case names, thresholds and
comparison directions and require every inequality to pass. Floating
diagnostic values may vary by runtime. Hash checks establish file identity,
not correctness; finite replay neither proves the written mathematics nor
certifies quantum reflection positivity, supersymmetric protection or RH.

[MANUSCRIPT_SOURCES.json](../MANUSCRIPT_SOURCES.json) records the research
inputs at assembly and the primary literature used for conventions. Its
paths describe provenance, not additional TeX build dependencies.
