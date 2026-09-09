# Clean-environment rerun of the first-slab certificate code — 9 September 2026

**What this is.** A record of one regeneration of the Investigation 12/13/14
result tables from the recovered certificate code, in a fresh, version-pinned
environment on a machine that had never run them. It is evidence for checklist
item **D4** (pinned rerun with archived logs), and for nothing else: byte
identity of outputs establishes repeatability of the computation, not the
correctness of the inherited analytic bounds (D1), the interval `LDLᵀ` and
box construction (D2), or the write-ups (D5). D3 (full primary-vs-audit row
diff) is not addressed here.

**Where the code is.** Not in this repository. The recovered code, tables,
verifiers, pins and hash manifest are packaged as a review candidate held by
the author (`code/README.md`, "Not here yet, and why"). Source files run, by
SHA-256:

| File | SHA-256 |
|---|---|
| `investigation12_offcenter_weil_generator.py` | `b04321e6263fddb80c7da1213ebd10f5b17222f6d12e1d89c5d26e09480b8afc` |
| `project_support/investigation7_first_slab_certificate.py` | `3d8ea53a73d3332d3ad074273476f0c1305b14c47d484b40a2db2250635b93b9` |
| `investigation13_operator_diagnostics.py` | `6a8135be5a467db30933e92a9b00ace2511f43772aded79fcad0bd370c59ac15` |
| `investigation14_independent_generator_audit.py` | `c3e896e2a0d0761591b936b81ae62198d55f29a89d18809f671912c25c5c128c` |
| `verify_investigation12_results.py` | `42c99a9dd5de642cba9cb4dfb8d0ecb2c9c3d7e75eefb4c85ff773c96b80b183` |
| `verify_investigation13_results.py` | `93c4696c26cf349cfd193287da8abcb9c69318dd8dbfb5ef3597a07edaff9257` |
| `verify_investigation14_results.py` | `7f18b45b4ed8e9ebacea2ed0f054a47c622d13dd9237083ef95baf6f1048a8d4` |

## Environment

CPython 3.12.3, Linux x86_64 (glibc 2.39), fresh `venv`, packages installed
from the candidate's `INVESTIGATION_12_requirements.txt` and nothing else:

```
mpmath==1.4.1
numpy==2.3.5
python-flint==0.9.0
scipy==1.17.0
```

This is the same pin set as the author's 5 September 2026 regeneration record
(CPython 3.12; NumPy 2.3.5; SciPy 1.17.0; mpmath 1.4.1; python-flint 0.9.0).

## Commands and wall-clock

Run from the candidate's root directory, outputs into a fresh `rerun/`:

```bash
PYTHONPATH=project_support .venv/bin/python investigation12_offcenter_weil_generator.py --certify --output rerun/INVESTIGATION_12_results.csv        # ~1 min
.venv/bin/python investigation13_operator_diagnostics.py --output rerun/INVESTIGATION_13_results.csv                                                 # 39 s
.venv/bin/python investigation14_independent_generator_audit.py --primary rerun/INVESTIGATION_12_results.csv \
    --output rerun/INVESTIGATION_14_results.csv --matrices rerun/INVESTIGATION_14_matrices.csv                                                       # 1 min 54 s
```

All three exited 0.

## Printed summaries

Investigation 12 (`--certify`):

```
kernel norm enclosure: [0.012293050401142319 +/- 6.84e-19]
Taylor remainder enclosure: [1.532967865231399199978994309467059193393135328338029429604221955775e-12 +/- 2.56e-79]
floating minimum ranges: {0: (0.0007338295497901536, 0.0011544688066373147), 1: (0.052724939643018394, 0.05813994388714404)}
certified boxes: 512
minimum interval LDL pivot: 0.023268119148861763
maximum Schur loss: 9.958698658589029e-05
minimum certified Weyl margin: 0.0006116350109501362
wrote 724 rows
```

Investigation 13: `wrote 90 rows`, `maximum transfer-derivative residual: 4.2168792e-81`.

Investigation 14: `wrote 783 audit rows`, `maximum central quadrature
discrepancy: 1.693e-15`, `maximum primary floating discrepancy: 4.375e-13`,
`maximum direct-kernel discrepancy: 1.593e-13`, `minimum directed-interval
margin: 6.116514636999e-04`, `minimum directed-interval pivot: 2.326829938890e-02`.

These agree with the constants used in the preprint: kernel-norm bound
`0.012293050401142320 < 0.012294`, Taylor remainder `< 1.54e-12`, even/odd
512-box margins `6.116350109501e-4` / `5.261670009275e-2`.

## Output identity

Every regenerated table is byte-identical (`cmp`) to the archived table in the
candidate, and to the hashes in the 5 September 2026 record:

| Output | SHA-256 (regenerated = archived) |
|---|---|
| `INVESTIGATION_12_results.csv` (724 rows) | `29d2a8a01d9570544607294ac57de512b1f550f30940490dea6a2b9179aa092f` |
| `INVESTIGATION_13_results.csv` (90 rows) | `56446c9b35058fc820108de07bb99905f1db13db1bca1e8ea1dfd216f37b3849` |
| `INVESTIGATION_14_results.csv` (783 rows) | `76eb4072144afffacce4aa02ffcf73f86308ce7c4d6c8e0344168183318e48e1` |
| `INVESTIGATION_14_matrices.csv` (1,360 rows) | `278d1f373558c1ab78a4fbe90638922e2dc512311fdd25c7c7bfd08b653a46e1` |

The three `verify_investigation*_results.py` structural verifiers pass on the
regenerated tables (exit 0), reporting the row counts and margins above.

## What remains for the code gate

D1 (rederive the Investigation 7 tail majorants), D2 (a second reader for the
interval `LDLᵀ` and box construction), D3 (complete primary-vs-audit row
diff), D5 (reconcile the stale passages in the Investigation 12/14 write-ups
with the preprint's block-Schur argument; the candidate's own README lists
them). Note also that the primary even margin `6.116350109501e-4` is the
Weyl–Schur box margin; the preprint's full-form coercivity constant
`6.1159e-4` additionally applies the block-Schur argument of its Lemma 7.1.

*Run performed with language-model assistance in a cloud sandbox during the
9 September 2026 repository-review session; the author is responsible for the
record.*
