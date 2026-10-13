# Portable replay preparation

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred.

This handoff requires a suitable Linux environment. Source preflight and
native Mac auxiliary-tool builds passed; Linux commands and mathematical
comparator targets have not run here. See [environment note](../notes/1_REPLAY_ENVIRONMENT_AND_TOOL_PREPARATION_20261012.md)
and [record](replay_environment_20261012.json).

## Pins and directories

Keep clones, dependencies, binaries, caches and full logs outside this
research repository. Use a separate tool directory and a fresh mathematical
checking baseline for each target.

| Repository | Commit |
| --- | --- |
| [openai/math](https://github.com/openai/math) | `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb` |
| [leanprover/comparator](https://github.com/leanprover/comparator) | `d03acab154d269c06e60e4de7e4cc85deebff94b` |
| [leanprover/lean4export](https://github.com/leanprover/lean4export) | `076e8e57707e813375e8f9da8bf989799ace9680` |
| [Zouuup/landrun](https://github.com/Zouuup/landrun) | `811cfff51ceaf3d9843708aa6d22e9b84ccac8b4` |

Lean is `leanprover/lean4:v4.34.1`. Comparator/exporter advertise 4.34.0;
use a 4.34.1 build override. Both passed that source compatibility test
on the Mac. Build Linux binaries separately, recording commands, compiler
versions, source and binary identities. Build Landrun from pinned source
with its required Go version and record module checksums.

## Source preflight

Set `LANE` to this lane's absolute path, `CHECK_ROOT` to a clean detached
math checkout at the exact commit, and `FORMAL_REPLAY_ARCHIVES` to the
external archive documented in [ARCHIVES.md](../ARCHIVES.md).

```sh
python3 "$LANE/numerics/check_replay_inputs.py" --selftest
python3 "$LANE/numerics/check_replay_inputs.py" \
  --checkout "$CHECK_ROOT" \
  --verify-record "$LANE/numerics/source_inventory_20261012.json"
```

This read-only check does not invoke Lake, build proofs, validate downloaded
dependency sources or test isolation. The external frontier remains
unexpanded. The original default Lake target is the whole OAI library,
with over 123,000 Lean source files. Avoid an unqualified `lake build`.
Do not compile mathematical solution modules outside comparator in a
checking baseline.

## Linux and dependency preparation

Before replay, record and check:

1. Linux kernel/distribution/architecture, unprivileged identity, user
   systemd and effective Landlock support. Test the actual Landrun write,
   execution and network restrictions, plus the systemd AF_UNIX guard,
   using harmless fixtures. Record denied and permitted operations.
   Version numbers and `--best-effort` startup do not prove isolation.
2. Auxiliary tools built under isolated Lean 4.34.1, including binary
   identities and exit status. Keep tool compilation separate from the
   mathematical checking environments.
3. Trust review of the original executable Lake configuration before
   elaborating it. Its 11 pre-resolution patches can execute during a
   Lake command before theorem compilation; 12 more run in `post_update`.
4. All 42 manifest package pins, actual checkout commits, prescribed patch
   identities and applied diffs. Preserve `lake-manifest.json`. If
   preparation changes it, stop, record differences and resolve drift
   before claiming a pinned replay. Do not change the preflight pin to
   bless a mismatch. Audit the resolved external imports, including PNTA
   and Rellich patch effects.
5. An explicit source/cache trust policy. The comparator permits a trusted
   Mathlib cache before checking; record provenance if used. Prepare
   dependencies without compiling solution modules. A cache hit is not
   target kernel replay.

Use the original configuration for the initial reproducibility attempt.
A reduced dependency configuration is a separate recorded experiment;
do not silently remove packages or patches from the original setup.

## Guarded invocation

Set `PATH` to the Linux comparator/exporter/Landrun and Lean binaries,
`ELAN_HOME` to the isolated installation, and
`ELAN_TOOLCHAIN=leanprover/lean4:v4.34.1`. For each row, use a fresh
`CHECK_ROOT`, recheck source identity after preparation, and set `CONFIG`:

| Target | `CONFIG` | Solution module |
| --- | --- | --- |
| zeta | `ComparatorChallenges/QuasiRiemannHypothesis.json` | `OAI.NumberTheory.DirichletL.Nonvanishing` |
| Dirichlet | `ComparatorChallenges/DirichletSevenEighths.json` | `OAI.NumberTheory.DirichletL.Nonvanishing` |
| Hecke | `ComparatorChallenges/HeckeSevenEighths.json` | `OAI.NumberTheory.DirichletL.Hecke.Nonvanishing` |

Adapted from the pinned comparator README, untested on Linux here:

```sh
systemd-run --property='RestrictAddressFamilies=~AF_UNIX' --user --pty \
  -E PATH="$PATH" -E ELAN_HOME="$ELAN_HOME" \
  -E ELAN_TOOLCHAIN="$ELAN_TOOLCHAIN" \
  --working-directory="$CHECK_ROOT/lean" -- \
  bash -c 'lake env comparator "$1"' bash "$CONFIG"
```

Keep full logs external. Record the service result and comparator result
separately; inspect documented success output, not just job-submission
status. Distinguish operational errors from statement mismatch, excess
axioms or kernel rejection. Never call development `fake-landrun.sh` a
guarded replay.

Per target record full signatures, challenge/solution identities,
definition names, permitted and reported axioms, built dependency/patch
identities, command, environment, exit status and kernel result. These
configurations permit `propext`, `Quot.sound`, `Classical.choice`, have
no definition holes, and set `enable_nanoda=false`. Additional-kernel
verification is a separate experiment.

Comparator success concerns its nominated statement under checker
assumptions. It does not establish every October 5 arithmetic application,
seminorm uniformity or two-Poisson transfer. Those are tracked in the
[crosswalk](../notes/2_ARITHMETIC_APPLICATION_CROSSWALK_20261012.md).
