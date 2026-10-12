# Arithmetic source audit numerics

12 October 2026. Prepared for Edward Baker using GPT-6-astra (Codex;
`gpt-6-astra`), reasoning effort **ultra**, with substantial LLM assistance.

Place reproducible scripts, parameter records, and small certificates here.
Record software versions, precision, error bounds, and what each check
establishes. Keep large regenerable output outside Git with stored-file and
content hashes and a documented lookup, following
[LARGE_FILES.md](../../../../LARGE_FILES.md).
See the [project scope](../README.md).

## Exact transfer regrouping

[check_transfer_regrouping.py](check_transfer_regrouping.py) enumerates the
signed preimages in the second Poisson transfer using three distinct
primary Eisenstein primes of norms 7, 13, and 19. It checks common column
scales, Fourier parameters, normalization, exclusion removal, and strict
row decrease with exact integers and rational numbers. A negative control
shows why taking absolute values before the signed regrouping can leave
an inadmissible column scale.

From the repository root:

```sh
python3 papers/investigations-2/arithmetic_source_audit/numerics/check_transfer_regrouping.py
```

The default output is [the small replay record](transfer_regrouping_record_20261012.json).
Use `--output /path/to/replay.json` to leave the saved record unchanged.
Optionally pass `--source /path/to/paper2.tex`; the script then refuses a
source whose SHA-256 differs from the [pinned provenance](../notes/source_provenance_20261012.json).
The immutable download URL is in that record. No third-party source file
is required for the finite arithmetic checks themselves.

The script uses only the Python standard library. Its record includes the
checker and source hashes, Python version, exact parameters, case counts,
and limitations. These are finite identity and support checks; they do not
evaluate Gauss sums, prove Poisson or theta identities, verify derivative
estimates, or validate the unbounded induction. The analytic argument and
assumptions are in the [branch ledger](../notes/CUBE_TAIL_BRANCH_AUDIT_20261012.md)
and [scoped review](../reviews/FIRST_BRANCH_REVIEW_20261012.md).

## Theta version comparison and reused checks

The [theta version record](theta_version_crosswalk_record_20261012.json)
pins both manuscripts at the same repository revision and confirms that
the September 30 PDF matches the artifact used in the earlier audit.
The source-formula correspondence is a mathematical read-through,
documented in the [theta review](../reviews/THETA_TRANSFORMATION_REVIEW_20261012.md).
It is not an automated assertion that the two source texts are identical.

The existing upstream checker was replayed unchanged, without overwriting
its historical record:

```sh
python3 papers/quasi-rh-character-amplification/numerics/check_upstream_reflection_interfaces.py --output /tmp/theta-interface-replay.json
```

All 69,881 assertions passed and the result agrees with the saved
historical JSON. The suite also contains primitive-Poisson checks; the
total is not a new count of theta obligations. It checks finite local
Fourier identities, cusp congruences and additive CRT phases. It does
not evaluate the global cubic multiplier, prove automorphy or reciprocity,
or establish the analytic kernel estimates. Those calculations are in
the new proof notes, under their stated imports.

The legacy checker records a fixed historical PDF hash without reading
the PDF. This audit separately downloaded and hashed the pinned artifact;
the new version record distinguishes that verification from the replay.
It records both source hashes, the checker hash, the replay result hash,
and the exact finite coverage.
