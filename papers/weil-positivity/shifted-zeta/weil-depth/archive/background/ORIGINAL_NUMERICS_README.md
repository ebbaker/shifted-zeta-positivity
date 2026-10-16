# Central coercivity at total horizon 9/5: reproducible Arb certificate

The result is Q_(0,9/5) >= 1e-26 I, with all finite construction arithmetic
enclosed by Arb, and an analytic infinite-tail plus profile-remainder argument.
Read RESEARCH_REPORT.md first. This is a research certificate requiring
mathematical/code review, not a formally verified or independently audited paper.

## Contents

- `certify_arb.py`: standalone full-output exact-parity construction and ball LDL.
- `analyze_certificate.py`: small-shift consequence, rational display bounds,
  optional legacy comparison, and clearly labelled spectral diagnostics.
- `output/length_1p8_N128/central_matrices.json.gz`: all four matrix enclosures,
  analytic-bound balls, arithmetic metadata, and checked dyadic export format.
- `output/length_1p8_N128/central_certificate.json`: both complete LDL results,
  all pivot enclosures, target margin, and matrix-archive SHA256.
- `output/length_1p8_N128/analysis.json`: relative-coupling diagnostics and
  exact/rational continuation validation.
- `run_N128.log`, `replay_N128.log`, `analysis_N128.log`: recorded execution logs.
- `background/`: preceding strategy and research report. These explain project
  normalization and history; their numerical archives are not certificate inputs.
- `SOURCE_HASHES.json`, `SHA256SUMS.txt`: provenance and final file checksums.

## Environment

Recorded versions: Python 3.12.14, python-flint 0.9.0, FLINT 3.6.0,
NumPy 2.3.5. The builder requires only python-flint and the Python standard
library. NumPy is used only for ordinary floating-point diagnostic eigenvalues.

Install into your preferred Python environment:

```bash
python -m pip install -r requirements.txt
```

Keep assertions enabled. Do not run with `python -O`.

## Rebuild the full certificate

From this directory:

```bash
python certify_arb.py --N 128 --M 180 --bits 1536 --horizon 9/5 --floor 1e-26 --output output/rebuilt
```

The recorded construction took about 64 seconds before archive compression and
the final LDL checks; machine-dependent runtimes vary. Both parity sectors must
print `positive: True`, followed by `FINAL PASS`.

The program encloses every finite operation; there is no aggregate 1e-45
rounding budget. The uncomputed analytic profile tail is still subtracted as
an explicit norm error, as explained in the report. Increasing precision does
not eliminate the need for that analytic remainder.

## Replay the saved matrix enclosures

```bash
python certify_arb.py --reuse --bits 1536 --floor 1e-26 --output output/length_1p8_N128
python analyze_certificate.py output/length_1p8_N128
```

Replay rechecks the final matrix signs from the saved construction enclosures;
a complete rebuild also checks the construction and analytic bounds themselves.
The analyzer's rounded-bound assertions and default continuation constants are
specific to this 9/5, 128-mode certificate. Its final floating-point eigenvalues
are diagnostics, never positivity decision inputs.

The recorded legacy comparison can be repeated if the older supplement is
available:

```bash
python analyze_certificate.py output/length_1p8_N128 --legacy /absolute/path/to/length_1p8_N96/central_matrices.json
```

That optional archive is not needed for the new result. The archived diagnostic
records retain the path used in the original run; future machines should supply
their own actual path.

## Ball encoding and conventions

Each scalar is `[[midpoint_mantissa, midpoint_binary_exponent],
[radius_mantissa, radius_binary_exponent]]`, where mantissas are decimal strings
encoding exact integers. This preserves the original dyadic midpoint and radius;
the Arb constructor may enlarge the radius outward. Export asserts containment
after reconstructing every ball. Midpoint-only decimal strings are never used
to reload certificate enclosures.

The matrices use the causal derivative U, whereas the previous report stored
the reflected derivative H1=UR. Within either reflection sector the full Gram
and reflected Gram agree under these conventions; off-sector entries acquire
the appropriate (-1)^(i+j) sign. Q and the central leakage are unchanged.

The program certifies a positive central lower bound using an analytic tail
floor and exact central-parity omitted-output coupling. A positive retained
head alone is insufficient. LDL pivots are not spectral lower bounds.

## Next handoff

Attach this ZIP and the standalone report. The next depth target is L=log(7).
The builder accepts `--log-horizon 7`; choose a new output directory and decide
head size/profile degree from the new Schur test and remainder budget. No claim
at log(7) has been computed in this packet. A strict horizon above log(7)
activates a new prime delay. The second-slab shift gap and all-depth induction
remain unresolved.

No license is newly imposed by this research packaging step.
