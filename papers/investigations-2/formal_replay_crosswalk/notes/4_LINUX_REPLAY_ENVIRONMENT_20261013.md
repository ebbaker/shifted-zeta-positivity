# Linux replay environment prepared

13 October 2026. Setup began 12 October. Prepared for Edward Baker with substantial LLM assistance. Model: GPT-6 (Codex), inherited session configuration; exact serving variant and reasoning effort are not exposed and are not inferred. These are operational preparation checks, not independent mathematical validation.

Ubuntu 26.04.1 LTS is running locally in Multipass as `rh-replay`, with six CPU cores, 16 GB RAM and a 150 GB virtual disk. The host was updated from macOS 14.5 to 27.0.1; the reproduced QEMU `strchrnul` crash now passes its image create/amend/check test. Multipass remains stable version 1.16.4; no release candidate was installed. No Mac folders are mounted into this VM.

## Evidence completed

- Linux kernel `7.0.0-34-generic`, ARM64, ordinary user `ubuntu`/UID 1000, user systemd manager running, Landlock ABI 8.
- Official Lean 4.34.1 ARM64 archive checksum verified; compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`. Pinned comparator, exporter and Landrun source builds passed on Linux. Direct toolchain binaries are used; elan is not installed in the guest.
- All 2,959 critical upstream inputs were fetched from `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` and compared to the saved hashes. The sparse checkout also includes the original pinned `lean/.gitignore` so build output stays separate from source changes. Unrelated OAI source files are omitted; no critical source or original project configuration changed.
- All 42 original dependency commits and all 23 prescribed compatibility patches verified. Actual complete source trees equal independently constructed expected patched trees. No `lake update` or dependency post-update hooks were run.
- Landrun operates in best-effort mode at ABI 8, which does not provide ABI 9 pathname UNIX-socket controls. The tested systemd guard denies new AF_UNIX socket creation; inherited descriptors and every IPC mechanism were not exhaustively tested.
- All 16 Linux operational controls passed, checking allowed and denied file writes, native execution, TCP bind/connect, and AF_UNIX socket creation under the actual systemd guard. Denials require the operation's explicit errno; startup failure cannot pass. This tests these permission profiles, not every possible kernel/sandbox exploit.
- The unchanged comparator accepted its pinned `simple_match` commutativity fixture through the default Lean kernel. This is a small integration check, not a seven-eighths theorem replay.
- Official Mathlib master cache preparation passed for `d13f23b723b8a846827a245b89c10fc7d3f11612`, downloading/decompressing 8,908 artifacts. The source manifest hash remained unchanged. The cache is trusted as a distribution artifact, as permitted by the comparator README; source-input keys do not independently validate cached contents. No fork cache, alternative scope or unsafe history search was selected.

The [environment record](../numerics/linux_vm_environment_20261013.json) binds the individual [tool build](../numerics/linux_tool_build_20261013.json), [dependency](../numerics/linux_dependencies_20261013.json), [isolation](../numerics/linux_isolation_20261013.json), [cache](../numerics/trusted_mathlib_cache_20261013.json), and [integration](../numerics/comparator_smoke_20261013.json) records. Scripts and the VM bootstrap package list are in `numerics/`. Full logs remain external under the lane archive guide.

## Checking layout and remaining work

The guest uses `/home/ubuntu/rh-replay-tools` for trusted auxiliary tools, `/home/ubuntu/rh-replay-source` for pinned mathematical sources/dependencies, and `/home/ubuntu/rh-replay-preparation` for small records. Linux binaries and third-party sources remain outside the research repository.

The mathematical OAI and challenge build trees were absent when the stopped-VM baseline `rh-replay.pre-math-replay-20261013` was preserved before mathematical compilation. Zeta has now started from this baseline; Dirichlet and Hecke must also use fresh baselines under `RestrictAddressFamilies=~AF_UNIX` and Landrun. Preserve each result externally before any baseline restoration. At this checkpoint the zeta target is running; its outcome and all actual axiom lists remain unset. The other targets have not run.

The pinned comparator checks that dependencies use only permitted axioms, but does not print the exact used set and retains its accepted JSON exports only in memory. A later export's dependency report is supplementary; it cannot be asserted byte-identical to the accepted export. The permitted list must not be relabelled as an actual-use report. The original checker remains unchanged.

Even successful target replay will not close the arithmetic application's U1–U7 ledger in [note 2](2_ARITHMETIC_APPLICATION_CROSSWALK_20261012.md). Those quantitative specializations remain separate work.

## One-off continuation launched

At 05:19 UTC on 13 October, the reviewed host queue adopted the existing zeta001 attempt. The [immutable launch checkpoint](../numerics/replay_queue_launch_20261013.json) records its state and source identities; the [queue guide](../numerics/REPLAY_QUEUE_GUIDE.md) describes continuation. Dirichlet and Hecke are scheduled sequentially from the clean baseline after accepted preceding attempts, with six-hour runtime bounds. Only a confirmed runtime cutoff of the initial zeta attempt permits one fresh-baseline zeta002 retry. Other failures halt after preserving evidence. All 34 internal and 20 separate offline controls passed. No final target acceptance was available at launch. Idle system sleep is inhibited only while this one-off process runs.
