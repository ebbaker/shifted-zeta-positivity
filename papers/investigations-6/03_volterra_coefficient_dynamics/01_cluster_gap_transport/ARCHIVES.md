# Regenerable canonical field archives

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex assistance; lead actual model/effort unavailable. Numerical acquisition
explicitly dispatched gpt-6.1-sol/ultra. Follow
[LARGE_FILES](../../../../LARGE_FILES.md). These arrays are regenerable
working data, not independently reviewed mathematical certificates.

The [diagnostic script](numerics/vcd_gt_lehmer_diagnostic.py) generates the
two fixed grids and the [small record](numerics/04_VCD_GT_LEHMER_DIAGNOSTIC_20261116.json)
owns their acquisition parameters, dependencies and hashes. Arrays contain
gauged complete-source field balls before source-tail padding: direct xi
values in the time-zero row, and finite-lattice values at positive times,
serialized as exact integer midpoint/radius/exponent triples. The fine grid
is the input to the separately assessed certification attempt.

| File | Gzip bytes | Stored SHA-256 | Decompressed-content SHA-256 |
| --- | ---: | --- | --- |
| `E04-r1-coarse-fields.json.gz` | 40,925 | `2b720914937d2afe46e5a4913d75057097a79f271c1ad81389a19b5d0ecffa70` | `223c09d08b46d0381b430a17e41d38026464422dfcc0e19d9bc32c85d9e07c1b` |
| `E04-r1-fine-fields.json.gz` | 192,793 | `033f83cb4a8d6bd411e4861380a78e054ab70f7c60079b98a75bd159644a078a` | `508d0feec6655524f1927d5b2877b1171c92a5a553053b7ef428fc680eb6f816` |

The generation-time copies are under `/private/tmp/vcd-gt-lehmer/`.
Temporary storage is not a promise of long-term availability. No archive
has been deposited or published. The source code and parameters permit
reconstruction with Python 3.10 and python-flint 0.9.0 / FLINT 3.6.0:

```sh
python3 papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/numerics/vcd_gt_lehmer_diagnostic.py --cache-dir /private/tmp/vcd-gt-lehmer --output /private/tmp/vcd-gt-lehmer/E04-r1-record.json
```

For the certificate consumer, the normal location is this branch's
`numerics-archives/FILE`. The alternate location is
`VCD_GT_ARCHIVES/numerics-archives/FILE`; that environment directory mirrors
the branch. An explicit `--cache-dir` may select an existing cache directly.
The consumer must reject absent or hash-mismatched data and give the
regeneration instruction. It checks both stored and decompressed bytes
before use. Root `.gitignore` already excludes `numerics-archives/`.

Hashes establish the identity of acquired data in the recorded environment;
they do not establish mathematical inequalities or bitwise portability
across software versions. The certificate must recompute its inequalities
from enclosed values and complete analytical errors. Keep additional
regenerable polynomial/cell output outside Git and record its parameters
and hashes if consumed; keep third-party PDFs outside Git as documented
in [references](references/README.md).

The revised B06 geometry consumer reuses only the fine array, checks the
original consumer source hash, and evaluates no drift kernel or new xi
values. It preserves the same archive lookup and fixed 60-second cap:

```sh
python3 papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport/numerics/vcd_gt_joint_strip_geometry.py --cache-dir /private/tmp/vcd-gt-lehmer --output /private/tmp/vcd-gt-joint-geometry-replay.json
```

[Record09](numerics/09_VCD_GT_JOINT_STRIP_GEOMETRY_20261116.json) records the
initial geometry run; use a distinct output for replay. The same recorded
Python/python-flint environment is required for the stated replay. No new
source archive was generated. [Note22](notes/22_VCD_GT_E04_JOINT_STRIP_GEOMETRY_20261116.md)
explains the separate widened disk error and original-collar moments.

## Exterior real-bracket acquisition, 16 November 2026

Prepared for Edward Baker with OpenAI Codex assistance; actual settings
unavailable, inherited helper dispatch. [Diagnostic15](numerics/15_VCD_GT_EXTERIOR_CANDIDATE_DIAGNOSTIC_20261116.json)
records the bounded three-time candidate selection. Its raw canonical JSON
is `/private/tmp/vcd-gt-exterior/stage-a-raw.json`, 1,846,244 bytes,
SHA-256 `10fa691c116a96f223c194ba04235f1c811ac560a1b7f491c24d5407b5fb1b38`.
The canonical-content hash is the same because this is uncompressed,
sorted compact JSON. It contains samples and execution metadata; new
timings can change a regenerated full-file hash. This raw diagnostic is
not consumed by the final certificate, whose exact rational groups are
fixed in [Manifest16](numerics/16_VCD_GT_EXTERIOR_BRACKET_MANIFEST_20261116.json).
The diagnostic script's later planning-only reprocessing and zero-source-call
provenance are recorded in Diagnostic15; its original source-execution hash
is preserved. Regenerate into a separate temporary folder with
`vcd_gt_exterior_diagnostic.py --raw-dir DESTINATION --record RECORD_PATH`.

The certificate's independent boundary-source archive contains 352 rows
of 13 real finite-arithmetic balls, before analytical source padding.
Each ball is stored as exact integer midpoint, radius and decimal exponent.
Metadata binds the exact manifest, acquisition code, precision, source
lattice, time nodes, constant gauges and boundary coefficients.

| File | Gzip bytes | Stored SHA-256 | Canonical-content SHA-256 |
| --- | ---: | --- | --- |
| `E04-r4-exterior-boundary-fields.json.gz` | 196,166 | `d96fc38052655a5fd566581c6a0a39be54c316c05cd6a2263b0fbe330640ab14` | `de2abfa688e86776468718045db8d992c00527ae1655db23a109153f75ac248a` |

The canonical uncompressed payload is 436,970 bytes. Acquisition-time copy:
`/private/tmp/vcd-gt-exterior/E04-r4-exterior-boundary-fields.json.gz`.
Temporary storage is not a promise of permanent availability; no deposit
or publication is claimed. The [consumer](numerics/vcd_gt_exterior_certificate.py)
checks both hashes and the complete metadata before replay. It also checks
the original target source cache and geometry programs; those inputs are
listed above and in the [certificate input pins](research-progress/handoffs/VCD-GT-E04-r4-certificate-input-pins.json).

Normal lookup is this branch's `numerics-archives/FILE`, then the same
relative path under `VCD_GT_ARCHIVES`; `--cache-dir` explicitly selects
another existing directory. The target cache has its separate
`--target-cache-dir`, otherwise the inherited normal/environment lookup.
Use Python 3.10 with python-flint0.9.0/FLINT3.6.0 for the recorded environment.
From the repository root, a bounded replay with the acquisition-time copies is:

```sh
vcd_gt_branch=papers/investigations-6/03_volterra_coefficient_dynamics/01_cluster_gap_transport
python3 "$vcd_gt_branch/numerics/vcd_gt_exterior_certificate.py" --replay \
  --manifest "$vcd_gt_branch/numerics/16_VCD_GT_EXTERIOR_BRACKET_MANIFEST_20261116.json" \
  --manifest-sha256 c068fda3ec1b36fd1b14e949e484fbfe32f4f8f6670d10f90cc6be93c0932cff \
  --cache-dir /private/tmp/vcd-gt-exterior \
  --target-cache-dir /private/tmp/vcd-gt-lehmer \
  --expected-stored-sha256 d96fc38052655a5fd566581c6a0a39be54c316c05cd6a2263b0fbe330640ab14 \
  --expected-content-sha256 de2abfa688e86776468718045db8d992c00527ae1655db23a109153f75ac248a \
  --output /private/tmp/vcd-gt-exterior-replay.json
```

To reconstruct boundary source data, use `--acquire` instead of `--replay`,
omit the two expected archive hashes, and choose a **new empty** cache
directory and new output record. The program refuses to overwrite an
existing boundary archive. The same frozen source, precision, refinement
and resource caps apply; regeneration is not a scan extension. The
original target cache must remain available or be reconstructed by the
earlier instructions. Both acquisition and replay consume serialized
source balls through the same guarded decoding path.

[Record17](numerics/17_VCD_GT_EXTERIOR_BRACKET_CERTIFICATE_20261116.json)
is the small certificate. Its c,D strings are outward display summaries;
replay recomputes the working coordinate balls from the original cache,
then checks each lower-mass predicate before formatting. The hashes identify
the source data, not the truth of an inequality or cross-version bitwise
portability. Actual bounds are recomputed by interval arithmetic and the
written analytical payments. Generated source arrays remain outside Git.
