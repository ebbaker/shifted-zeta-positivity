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

## Completed zeta replay: 13 October 2026

Zeta attempt 001 completed at 01:49:40 EDT (05:49:40 UTC), with exit 0, no timeout, statement agreement, permitted-axiom compliance and acceptance by the Lean default kernel. Its [small result record](numerics/replay_zeta_001_20261013.json) binds the exact original configuration, source pin, tool binaries, dependency and cache records, guarded command and preserved evidence. The attempt took 4,715.627372 seconds. The full comparator transcript is external because it exceeds the repository size limit. This result does not close the October 5 arithmetic application crosswalk.

The immutable attempt prefix, relative to this archive root, is:

`linux-replay-20261013/replay-queue-20261013T051902Z-3d320a39/attempts/zeta-001/`

| File under that prefix | Bytes | Stored SHA-256 | Canonical SHA-256, when structured |
| --- | ---: | --- | --- |
| `guest_record.json` | 3,168 | `022eb7d09a69058bce40fe3102fafffd099be09bd034f278134c8cde0695236a` | `ffda8403d752bdb4ffdd527dec73da418b3a6a9b46b346bf99824a8e6dfafb7d` |
| `comparator.log` | 3,722,529 | `c7f3ff3211e2d1d6a03dcad9c03c421d751acc042d593dec4b3d4977708ac3ff` | — |
| `source_preflight.log` | 1,613 | `ffdcb9e7c9aabe07be9e4a451fa042844b74d4ebc5a922f3e226281ec8ff3001` | `6bab698586b3fa2816b492da3ed205ac07c6a03abceed86494419adf01d90737` |
| `guest_final_probe.json` | 5,710 | `dd526295810762bcf0e8bbf6196497053e80e028c92d8170d7197cefab586296` | `e06cf272a4203d29f58e6641d3e3b00555eb116bb9ed7e11a28bdc75bc1603d6` |
| `host_result.json` | 16,694 | `1ac689d5179812ac3d6df9d2efee2c985f6a3e9861a426467ebe5de68114f1b3` | `f46447cb74864f56b07a7861fd0a39ff27a41a0003ea51a66e54ed8db44809bf` |
| `SHA256SUMS.txt` | 424 | `3cb0250749b63a594f87fdfd188c99b07eee7fc9add34af7bc986b977b45a73c` | — |

All five entries in the per-attempt checksum list were checked before integration. The root checksum list includes these immutable files and that checksum list itself; it continues to exclude changing live queue state, queue console, orchestration and active attempt console files. Structured hashes use the UTF-8 canonical JSON serialization defined above, including every field; the source-preflight log also contains one JSON object and has a canonical hash. Preparation context copies retain their earlier dates and not-run outcome fields; the zeta attempt supplies the newer replay outcome.

The preserved host result and guest record establish allowed-set compliance only. The exact used-axiom set and accepted-export digest remain null. The final probe found no active mathematical processes or live replay unit; its not-found unit properties alone are not acceptance evidence. The durable guarded command exit and complete comparator/kernel success output supply that outcome.

To inspect another copy, apply the normal ignored `numerics-archives` lookup followed by `FORMAL_REPLAY_ARCHIVES`, then verify the per-attempt checksum list and the small record’s stored/canonical bindings before using any outcome. Regenerate an attempt with the pinned preparation scripts, clean saved baseline, original target configuration and [guarded queue procedure](numerics/REPLAY_QUEUE_GUIDE.md). A new attempt can have different timings and transcript bytes; retain its own immutable evidence rather than overwriting this attempt. These hashes identify this preserved execution, not portable byte-identical logs from future runs.

## Completed Dirichlet and Hecke replays: 13 October 2026

The original three-target queue finished at 04:01:53 EDT (08:01:53 UTC). Both subsequent attempts were accepted by the unchanged pinned comparator and the Lean default kernel, with exit 0 and no timeout, after restoration of the same clean mathematical baseline. Dirichlet took 4,258.699506 seconds and finished at 03:01:39 EDT (07:01:39 UTC); Hecke took 3,518.721108 seconds and finished at 04:01:14 EDT (08:01:14 UTC). The [Dirichlet record](numerics/replay_dirichlet_001_20261013.json) and [Hecke record](numerics/replay_hecke_001_20261013.json) preserve the original exact target configurations and statements, source/tool/dependency bindings, guarded commands and result evidence. These accepted universal targets do not compile the new October 5 arithmetic applications.

Immutable Dirichlet attempt prefix, relative to this archive root:

`linux-replay-20261013/replay-queue-20261013T051902Z-3d320a39/attempts/Dirichlet-001/`

| File under that prefix | Bytes | Stored SHA-256 | Canonical SHA-256, when structured |
| --- | ---: | --- | --- |
| `guest_record.json` | 3,209 | `aa7dac44398a65ef522c6e550eda8042301d113ab09792ff056f9c81f0576971` | `1d3c26da0b63178e89257c0f6121cf9358b3d833883b86ad6d1d512f52165834` |
| `comparator.log` | 3,413,044 | `4896aaf441aa18498de0203b40555073fac7fadc120d162021e209a9f7d59a35` | — |
| `source_preflight.log` | 1,613 | `ffdcb9e7c9aabe07be9e4a451fa042844b74d4ebc5a922f3e226281ec8ff3001` | `6bab698586b3fa2816b492da3ed205ac07c6a03abceed86494419adf01d90737` |
| `guest_final_probe.json` | 5,771 | `af966c4e6b0e23f15015cf0a4027af97414993a7d3854631bf89d0c4cefec56e` | `7c9c778aa157908e07a6f156fce27ead86174c3bff835a4a568ce3cd794f78e0` |
| `host_result.json` | 16,699 | `74a6b267edc8a5e3eb4348d04aea019f4b536f9925db6dce0d2033e936ef727a` | `12282bc557e3e242f07f693d477f065dcb66cc3ce460ad1f0b9cf31d70fe1006` |
| `SHA256SUMS.txt` | 424 | `83c6a609d372b460183164d5d22cf5750d117db52f5db25bd94c1681746f1b0d` | — |

Immutable Hecke attempt prefix, relative to this archive root:

`linux-replay-20261013/replay-queue-20261013T051902Z-3d320a39/attempts/Hecke-001/`

| File under that prefix | Bytes | Stored SHA-256 | Canonical SHA-256, when structured |
| --- | ---: | --- | --- |
| `guest_record.json` | 3,189 | `d3e77fd3bb9c9436936e97ca9b769e98ef0b07c322f3cc4973d4cedaf6171e95` | `5757668ccbdbe5f7100896c39b50d2c39282ad5b7641135b590cc130e08d8058` |
| `comparator.log` | 2,730,124 | `f90ee76da77ffbe0a8d953f93b39a1330435521f46e869374ec7628f8c837dbd` | — |
| `source_preflight.log` | 1,613 | `ffdcb9e7c9aabe07be9e4a451fa042844b74d4ebc5a922f3e226281ec8ff3001` | `6bab698586b3fa2816b492da3ed205ac07c6a03abceed86494419adf01d90737` |
| `guest_final_probe.json` | 5,728 | `bad0a5b4be14dccdd87e748c3ec6d88095213a7c3445bd49d1f05bc079919f72` | `bf8f6916a7a583cf85b011d609524d5b35e3d0b299cb79ab4c663af9a9ea7bca` |
| `host_result.json` | 16,695 | `30f34c5dc88c5bf8051ff2a213ce61a9fe5b60baa4a001743e974ea9155c6598` | `131bb60eb70d516ca93a3106dbcd31ceaa1797d2d869800b9fd95954401efca0` |
| `SHA256SUMS.txt` | 424 | `49ab760efc8981af591680d8de0217f1d273a677363b05d4aa14d5f55e4660c2` | — |

An exact immutable copy of the completed queue state is preserved separately from the original live-state filename:

| Relative archive path | Bytes | Stored SHA-256 | Canonical SHA-256 |
| --- | ---: | --- | --- |
| `linux-replay-20261013/replay-queue-20261013T051902Z-3d320a39/queue_final_state_20261013.json` | 21,008 | `1440ea1bcaf676c943878606f7f4b58c00515a08d2b98dc496a4c60b89765eba` | `bc22a1b48a557056354f6f6c832e059a2a8ae5fe57721b49f6003c188bbc0987` |

All five checksum entries for each attempt and the raw default-kernel success markers were verified before integration. The root manifest now includes the immutable Dirichlet and Hecke attempt files, their per-attempt checksum lists and this final-state snapshot. The original live-state path, orchestration and console files remain excluded. The queue itself was not modified. Structured hashes use the canonical UTF-8 JSON encoding defined above. Full comparator logs remain external.

Exact used-axiom sets and accepted-export digests remain null in both small records; allowed-set compliance is not an exact axiom report. The final queue state is an operational completion checkpoint, not kernel acceptance evidence. Each target’s durable exit and preserved full comparator output supply its recorded result. Check the normal relative archive lookup and the bound stored/canonical hashes before relying on a copied record. Regenerate separate attempts with the original pinned preparation, baseline and [guarded queue procedure](numerics/REPLAY_QUEUE_GUIDE.md); preserve new evidence without overwriting these completed attempts.
