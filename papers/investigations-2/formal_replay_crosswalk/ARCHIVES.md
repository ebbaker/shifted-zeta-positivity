# Formal replay external archive

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred.

Follow [LARGE_FILES.md](../../../LARGE_FILES.md). Tracked scripts and small
records reproduce and identify the external source manifest. Third-party
source trees, binaries, toolchains and caches remain external.

## Data and lookup

| Relative archive path | Bytes | Stored SHA-256 |
| --- | ---: | --- |
| `source_closure_manifest.json` | 1,958,471 | `b0bd1f6b77e23bec0a78811a644114eb12dea6e55138620c82ef76a00af77c48` |

Canonical SHA-256:
`b376fb72817e7bc0bd88c1de0bffb7eedde6f7dd670781c3b593d39fd3f00862`.
Canonical serialization is UTF-8 JSON, sorted keys, no ASCII escaping,
separators `(',', ':')`, no final newline. Stored serialization uses sorted
keys, two-space indentation, no ASCII escaping, and a final newline.

The manifest enumerates local module identities/imports and critical inputs
at openai/math `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`. Regenerate it
with [check_replay_inputs.py](numerics/check_replay_inputs.py). Matching
hashes establish identity under this scanner; they are not proof steps or
external-dependency validation.

Lookup first uses this lane's ignored
`numerics-archives/source_closure_manifest.json`, then
`$FORMAL_REPLAY_ARCHIVES/source_closure_manifest.json`. The consumer checks
stored and canonical hashes against the [small record](numerics/source_inventory_20261012.json)
and rebuilds the graph from the supplied checkout. It fails closed on
missing, modified or inconsistent data.

The current local archive is
`/Users/Shared/szp-archive/formal_replay_crosswalk/numerics-archives`.
This is a convenience, not a public deposit or hardcoded consumer path.
Move/copy it anywhere and set:

```sh
export FORMAL_REPLAY_ARCHIVES=/absolute/path/to/numerics-archives
```

The folder includes `README.md` (copy of this canonical guide),
`SHA256SUMS.txt` and native tool-build logs under `logs/`, whose identities
are in [replay_environment_20261012.json](numerics/replay_environment_20261012.json).
Repeating tool builds can regenerate logs with different timings/bytes.
Those logs record auxiliary builds, not mathematical replay.

## Regeneration and verification

Obtain a clean checkout at the exact pin with `lean/`, including challenge
configurations and patches. The scanner uses Python 3.10+ and Git and
does not invoke Lean, Lake or a downloader. Set `LANE`, `CHECK_ROOT` and
`ARCHIVE` to the lane, checkout and an empty external destination:

```sh
python3 "$LANE/numerics/check_replay_inputs.py" \
  --checkout "$CHECK_ROOT" \
  --expected-pin fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb \
  --output "$ARCHIVE/regenerated_source_inventory.json" \
  --closure-manifest "$ARCHIVE/source_closure_manifest.json" --selftest

FORMAL_REPLAY_ARCHIVES="$ARCHIVE" \
  python3 "$LANE/numerics/check_replay_inputs.py" \
  --checkout "$CHECK_ROOT" \
  --verify-record "$LANE/numerics/source_inventory_20261012.json" --selftest
```

Generation writes named outputs. Preserve the committed record and use an
empty external destination to avoid overwriting a reviewer's copy. The
full manifest is deterministic for the same pinned inputs/scanner. Small
records have incidental dates/paths/environment fields; their bytes can
differ. Deterministic evidence and generator identity are verified
separately from incidental fields.

To request or supply data, provide this archive folder with its checksums,
or regenerate the manifest. From inside the folder verify `SHA256SUMS.txt`
with `sha256sum -c` on Linux or `shasum -a 256 -c` on macOS. Do not commit
full manifests or logs.

## Linux setup logs: 13 October 2026

Full operational logs are preserved under `linux-vm-setup-20261013/` in this archive: `tool-build-logs/` contains the complete numbered commands from the Linux tool-build record; `trusted_mathlib_cache.log` and `comparator_smoke.log` are the raw cache and integration logs. The tracked [Linux environment record](numerics/linux_vm_environment_20261013.json) gives the mapping and binds individual small records, which carry log sizes and SHA-256 identities. The folder's `SHA256SUMS.txt` identifies every archived file. These logs establish the recorded preparation outcomes, not the seven-eighths conclusions. The Linux VM, source clones, toolchain, binaries and caches remain external and can be reconstructed from the tracked scripts and pins. Mathematical target attempt logs will be archived separately when each attempt completes.

## Live mathematical replay queue: 13 October 2026

The [launch checkpoint](numerics/replay_queue_launch_20261013.json) binds the reviewed queue/runner and immutable launch/initial-state files. Current state is `linux-replay-20261013/replay_queue_state.json`; it changes atomically and is not itself proof evidence. The relative run directory is recorded there, with immutable context copies, an append-only orchestration log and `attempts/<target>-<attempt>/` folders. Each completed attempt contains exact guest JSON, full comparator log, source-preflight log, final probe, small `host_result.json` and `SHA256SUMS.txt`. The host result and checksums bind the observed outcome to the exact preserved files and preparation inputs. No exact used-axiom set is inferred from allowed-set compliance.

The queue writes entirely outside the research checkout. Its committed source and [guide](numerics/REPLAY_QUEUE_GUIDE.md) reproduce the sequence from the preserved clean VM baseline and original preparation. Live queue state, console and orchestration logs are excluded from the root archive checksum list while changing; immutable launch/context files are included. Future completed attempt folders carry their own checksum lists. Refresh the root manifest after the run finishes, excluding still-mutable files; do not describe an initial progress hash as final result evidence.

To inspect results, resolve these relative paths first under the lane’s ignored `numerics-archives`, then under `FORMAL_REPLAY_ARCHIVES`. Check the per-attempt SHA256SUMS before relying on a copied host result. Preserve failed attempts as well as accepted ones. The current local archive root above remains a convenience, not a hardcoded consumer path or public deposit.
