# Formal replay preparation and execution

Initialized 12 October 2026; updated 13 October 2026. Prepared for Edward
Baker with substantial LLM assistance. Model: GPT-6 (Codex), inherited
session configuration; exact serving variant and reasoning effort are not
exposed and are not inferred.

Linux setup is complete in the local Multipass VM `rh-replay`. The guarded
zeta attempt is running from the saved clean baseline; no target outcome
is available yet. Dirichlet and Hecke have not run. See the
[Linux environment note](../notes/4_LINUX_REPLAY_ENVIRONMENT_20261013.md)
and [bound record](linux_vm_environment_20261013.json). The
[12 October note](../notes/1_REPLAY_ENVIRONMENT_AND_TOOL_PREPARATION_20261012.md)
and [native record](replay_environment_20261012.json) describe the earlier
Mac preparation milestone.

## Pins and checking layout

Keep third-party sources, dependencies, binaries, caches and full logs
outside this research repository. Use a fresh mathematical checking
baseline for each target.

| Repository | Commit |
| --- | --- |
| [openai/math](https://github.com/openai/math) | `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` |
| [leanprover/comparator](https://github.com/leanprover/comparator) | `d03acab154d269c06e60e4de7e4cc85deebff94b` |
| [leanprover/lean4export](https://github.com/leanprover/lean4export) | `076e8e57707e813375e8f9da8bf989799ace9680` |
| [Zouuup/landrun](https://github.com/Zouuup/landrun) | `811cfff51ceaf3d9843708aa6d22e9b84ccac8b4` |

The guest paths are:

| Purpose | Path |
| --- | --- |
| Trusted auxiliary tools | `/home/ubuntu/rh-replay-tools` |
| Direct Lean 4.34.1 prefix | `/home/ubuntu/rh-replay-tools/toolchain/lean-4.34.1-linux_aarch64` |
| Comparator, exporter and Landrun | `/home/ubuntu/rh-replay-tools/bin` |
| Pinned mathematical checkout | `/home/ubuntu/rh-replay-source` |
| Lake project | `/home/ubuntu/rh-replay-source/lean` |
| Preparation and attempt records | `/home/ubuntu/rh-replay-preparation` |
| Clean stopped-VM baseline | `rh-replay.pre-math-replay-20261013` |

The guest has no elan installation. Commands put the direct Lean and
auxiliary-tool binaries first on `PATH`; no guest `ELAN_HOME` is required.
The recorded commands also set `ELAN_TOOLCHAIN=leanprover/lean4:v4.34.1`.
Comparator/exporter advertise 4.34.0 in their unchanged source release
configuration and were successfully built using 4.34.1. Their Linux source
and binary identities, Lean release checksum and Landrun Go/module
identities are recorded in [linux_tool_build_20261013.json](linux_tool_build_20261013.json).

## Completed operational preparation

The VM runs Ubuntu 26.04.1 LTS, ARM64 kernel `7.0.0-34-generic`, as ordinary
user `ubuntu`/UID 1000. Its user systemd manager is available. All sixteen
actual permission controls passed, including explicitly permitted and
denied file writes, native execution, TCP bind/connect and new AF_UNIX
socket creation. The comparator's small commutativity integration fixture
also passed its default-kernel replay. These checks establish operational
behavior for the tested profiles, not seven-eighths theorem acceptance.

Landlock ABI is 8. Comparator's `--best-effort` mode therefore lacks ABI 9
pathname UNIX-socket controls; the actual systemd
`RestrictAddressFamilies=~AF_UNIX` guard separately denies new AF_UNIX
sockets. Inherited descriptors and all other IPC mechanisms were not
exhaustively tested. Record the effective policy rather than inferring it
from version numbers or successful sandbox startup.

All 2,959 critical mathematical inputs match the upstream pin. The sparse
checkout includes those exact paths and the original `lean/.gitignore`.
All 42 original dependency commits and 23 prescribed patches were verified
against their complete expected patched source trees. Original project
configuration and manifest are preserved. Dependency preparation did not
run Lean, Lake or post-update hooks. The original Lake configuration's
eleven pre-resolution patch operations and twelve post-update patches
remain part of the trust review.

Official Mathlib cache preparation used
`--repo=leanprover-community/mathlib4 --cache-from=master` for Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. It completed successfully with
unchanged source manifest. Cache contents are explicitly trusted as a
distribution artifact; source-input keys do not independently verify those
contents. The full cache, smoke and tool-build logs are archived externally
under [ARCHIVES.md](../ARCHIVES.md). A cache hit is not target kernel replay.

## Source preflight

For a supplied checkout, set `LANE` to the lane's absolute path,
`CHECK_ROOT` to the detached mathematical checkout, and
`FORMAL_REPLAY_ARCHIVES` to the external manifest location documented in
[ARCHIVES.md](../ARCHIVES.md). The guest's supplied manifest is under
`/home/ubuntu/rh-replay-preparation/archive`.

```sh
python3 "$LANE/numerics/check_replay_inputs.py" --selftest
python3 "$LANE/numerics/check_replay_inputs.py" \
  --checkout "$CHECK_ROOT" \
  --verify-record "$LANE/numerics/source_inventory_20261012.json"
```

The source checker does not invoke Lean, Lake, network downloads or proof
checking; dependency validation and isolation have separate records. Its
original external import frontier remains unexpanded in that source
inventory. The original default Lake target is the whole OAI library,
with over 123,000 source files. Use nominated comparator targets and avoid
an unqualified `lake build`. Keep mathematical solution compilation inside
the guarded comparator attempt.

If a later preparation changes source pins, patches or manifest, record
and resolve the difference before claiming a pinned replay. A reduced
Lake configuration is a separately recorded experiment.

## Guarded target attempt

| Target | Configuration | Solution module |
| --- | --- | --- |
| zeta | `ComparatorChallenges/QuasiRiemannHypothesis.json` | `OAI.NumberTheory.DirichletL.Nonvanishing` |
| Dirichlet | `ComparatorChallenges/DirichletSevenEighths.json` | `OAI.NumberTheory.DirichletL.Nonvanishing` |
| Hecke | `ComparatorChallenges/HeckeSevenEighths.json` | `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing` |

The [guarded runner](run_guarded_comparator.py) checks source input and
tool identities, requires absence of OAI/challenge build trees, and gives
systemd its own controlling PTY. Its baseline-name argument records the
supplied label; snapshot preservation/restoration is recorded separately.
The first zeta attempt is already running with this interface:

```sh
python3 /home/ubuntu/rh-replay-preparation/run_guarded_comparator.py \
  --target zeta --attempt 001 \
  --baseline-name pre-math-replay-20261013 \
  --timeout 7200
```

The runner uses the tested `systemd-run --user --pty` guard with
`RestrictAddressFamilies=~AF_UNIX`, a named service and runtime bound. It
sets the direct-toolchain `PATH`, then runs
`lake env comparator "$CONFIG"` in the pinned `lean` project. Comparator
applies its unchanged Landrun build/export profiles. The target's final
acceptance remains a separate result from the earlier integration check.

The runner preserves a running JSON record before compilation. On
completion it writes the combined raw log, process result and source
preflight log identities. Acceptance requires exit zero, no timeout,
default-kernel acceptance and final comparator success output. An
unsuccessful attempt requires classification; job submission or partial
build success is not a mathematical result.

## Preserve an attempt and restore the baseline

Zeta and Dirichlet share a solution module, so each still requires a fresh
checking baseline. For each completed attempt:

1. Copy its completed JSON record, raw comparator log, source preflight
   log and any supplementary reports to a new external host archive
   directory. Check each recorded SHA-256 and available log-size field. Preserve
   failed attempts as well as accepted ones. Resolve missing or incomplete
   evidence before stopping or restoring the VM.
2. After the external copies and hashes are verified, stop `rh-replay`
   and restore `rh-replay.pre-math-replay-20261013`. Record the restore
   result and baseline identity. Restoration discards the guest state
   accumulated since that baseline, including attempt records and builds.
3. Start the restored VM and transfer the current target runner again.
   It was created after the baseline snapshot. The baseline already
   contains the other preparation inputs, tools, dependencies, cache and
   guest record `linux_isolation_001.json`.
4. Recheck fresh source/build state and tool identities through the runner,
   then select the next target and a distinct attempt identifier. Keep
   each completed host record independently of later restorations.

For the completed `zeta`/`001` attempt, the host transfer pattern is below.
Set `ATTEMPT_ARCHIVE` to the new external destination before use:

```sh
multipass transfer \
  rh-replay:/home/ubuntu/rh-replay-preparation/replay_zeta_001.json \
  rh-replay:/home/ubuntu/rh-replay-preparation/replay_zeta_001.log \
  rh-replay:/home/ubuntu/rh-replay-preparation/replay_zeta_001_source_preflight.log \
  "$ATTEMPT_ARCHIVE/"
shasum -a 256 "$ATTEMPT_ARCHIVE/replay_zeta_001.log" \
  "$ATTEMPT_ARCHIVE/replay_zeta_001_source_preflight.log"
```

Only after completed-record and raw-log preservation and hash checks, use
the installed Multipass 1.16.4 stop/restore/start syntax verified from its
command help:

```sh
multipass stop rh-replay
multipass restore --destructive rh-replay.pre-math-replay-20261013
multipass start rh-replay
multipass transfer "$LANE/numerics/run_guarded_comparator.py" \
  rh-replay:/home/ubuntu/rh-replay-preparation/run_guarded_comparator.py
```

Check each command's success before the next. Consult
`multipass help restore`, `multipass help transfer`, `multipass help stop`
and `multipass help start` for the installed version. The saved snapshot
is already established; an actual restoration remains an operation to
record when moving to the next attempt.

## Result and axiom boundaries

Record target configuration/signatures, definition names, permitted axioms,
source/tool/dependency/patch identities, command, environment, exit status,
statement-comparison result, allowed-axiom compliance and kernel outcome.
The three configurations permit `propext`, `Quot.sound`, `Classical.choice`,
have no definition holes and set `enable_nanoda=false`. An additional
kernel is a separate experiment.

The unchanged pinned comparator checks allowed-set compliance but does not
print the exact used-axiom set or accepted-export digest. Keep actual sets
unset unless supported by explicitly bound evidence. A later export's
dependency report is supplementary and cannot be asserted byte-identical
to the accepted export. Never relabel the permitted list as actual usage.

Comparator success concerns its nominated statement under checker
assumptions. It does not establish every October 5 arithmetic application,
seminorm uniformity or two-Poisson transfer. Those remain in the
[crosswalk's U1–U7 ledger](../notes/2_ARITHMETIC_APPLICATION_CROSSWALK_20261012.md).
