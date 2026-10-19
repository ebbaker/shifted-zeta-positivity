# External evaluated-jet tables: S02-T2

19 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. **gpt-6.1-sol (Codex), actual reasoning effort ultra**. Internal LLM verification and separate same-model replay; no specialist review.

These regenerable tables contain the complete closed-cell jet images, every error payment, phase/normalizer data and paid tests behind [Note 03](notes/03_COMPLETE_FROZEN_JETS_AND_PAID_CONSUMERS_20261019.md). Each table exceeds 5 MiB and is kept out of Git under [LARGE_FILES.md](../../../../../LARGE_FILES.md). The small canonical record is [S02_COMPLETE_JETS_20261019.json](numerics/S02_COMPLETE_JETS_20261019.json); the generator and loader are [evaluate_complete_frozen_jets.py](numerics/evaluate_complete_frozen_jets.py).

## Location and identity

The normal path is `numerics/` followed by the relative path below, inside this S02 lane. The sole fallback is the same relative path under `S02_JET_ARCHIVES`. The maintainer's saved root is `/Users/Shared/szp-archive/s02-cutoff-jets/numerics-archives`; set `S02_JET_ARCHIVES` to that root, or to another copy's root. The code contains no machine-specific fallback. Missing data fail closed with regeneration guidance. Local output patterns are ignored by this lane's `.gitignore`.

| Relative path under the archive root or local numerics/ | Bits | Stored bytes | Stored SHA-256 | Canonical cell-content SHA-256 |
| --- | ---: | ---: | --- | --- |
| output/S02_T2_B_192_20261019.jsonl.gz | 192 | 6843771 | `b8986713d8a14e2b8f55302eea30694b4c98794ab193523d874b9c8d99b14379` | `9e73d866c3a25ac79d9d6fd18f17e24c787aa2fa862bd155feffc99685829842` |
| output/S02_T2_B_256_20261019.jsonl.gz | 256 | 6845883 | `e5f29e482d8a1416dfb3f88290da9fc7b744360e771e83251ab52eb7b0764208` | `e6cb47e0d6babad36f0da841102023eda7b914f5609f6005d770f169e883b837` |

The stored hash identifies the complete gzip bytes. The canonical content hash covers every sorted-key cell JSON row in fixed time/space order, excluding the header's observational reference-setup times; it is independent of compression and those timings. Fresh mathematical rows matched in a separate 192-bit rebuild even though observed setup time and compressed-file identity differed. This is tested data identity, not proof or guaranteed arithmetic portability. Different precision tables legitimately have different cell hashes.

Each archive starts with a header containing source/producer hashes, the exact-dyadic complete-source setup, fixed domain and derivative semantics. The remaining 4,096 rows are ordered `(time_index, space_index)`. Numeric display strings conservatively re-enclose the intervals when parsed as Arb; do not call them exact dyadic serialization. The source setup retains its exact dyadics separately. The inherited 512-call setup metadata concerns the old adaptive consumer, while this task declares a fixed 4,096-cell replay.

## Regeneration and verification

Use Python with python-flint 0.9.0 and the source identities pinned in the small record. From the repository root, write to a fresh external directory:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/evaluate_complete_frozen_jets.py --repo . --output /tmp/S02_COMPLETE_JETS_REBUILD.json --archive-dir /tmp/S02_JET_REBUILD --bits 192 256 --execution-model ACTUAL_MODEL --execution-effort ACTUAL_EFFORT
```

The rebuild summary supplies its own exact stored-file receipts. Acquisition timing may change its stored hashes; compare canonical cell-content hashes when assessing mathematical identity. Do not overwrite a retained receipt merely to conceal a mismatch. The code performs no network download. The independent review's compressed inspection copy is not a third canonical table: its mathematical cell content agrees with the saved primary 192-bit table, and its distinct observed-header identity remains in the review replay record.

The loader first tries the normal local path and then `S02_JET_ARCHIVES`. Supply an archive receipt from the corresponding run summary to `load_cell_archive(repo, receipt)`. It verifies stored and canonical hashes, producer/source pins, precision and count before exposing rows, then checks each row's declared order before yielding it. Arithmetic decisions use the returned outward intervals; a hash is not a sign proof.

With `S02_JET_ARCHIVES` pointing to the retained root, verify both tables and the fail-closed guards:

```sh
python3 papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/check_jet_archive_integrity.py --repo . --record papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/02_cutoff_reflection/numerics/S02_COMPLETE_JETS_20261019.json --archive-root /path/to/s02-cutoff-jets/numerics-archives --output /tmp/S02_ARCHIVE_CHECKS.json
```

The saved [archive check](numerics/S02_JET_ARCHIVE_CHECKS_20261019.json) loads all 8,192 rows and rejects wrong stored/content hashes, a missing table, and a stale producer with otherwise valid mathematical content before yielding any data in those test cases. The external root also contains `SHA256SUMS.txt` and a copy of this guide as `README.md`. Regenerate source-event replay receipts externally with the control command in the [numerical guide](numerics/README.md).
