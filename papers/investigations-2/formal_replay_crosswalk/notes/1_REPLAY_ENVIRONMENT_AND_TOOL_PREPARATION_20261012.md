# Replay environment and tool preparation

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred. This is a source
preflight and auxiliary-tool build record, not mathematical validation.

The first milestone establishes a pinned source inventory and compatible
checking-tool sources. Mathematical replay has not run. This Mac has no
configured Linux runtime; the comparator's checking command requires Linux
sandboxing and a user systemd service. An environment choice has been
requested. Source work can proceed independently of that choice.

## Source identity and scope

The clean detached checkout is openai/math
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, using
`leanprover/lean4:v4.34.1`. Mathlib is pinned to
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

The [source inventory](../numerics/source_inventory_20261012.json) follows
local imports from three exact challenge/solution pairs. It verifies 2,926
OAI modules and three challenge modules, with 2,959 critical files and
32,672,977 bytes including configurations and prescribed patch inputs.
Each critical file was compared to its pinned Git blob. The lexical import
scanner is a navigation and identity check, not the Lean parser or a
compiled dependency verifier.

Per-target OAI counts are 2,924 for zeta, 2,924 for Dirichlet, and 2,925 for
Hecke; their union is 2,926. The scanner stops at 252 external imports,
including Mathlib/core, PrimeNumberTheoremAnd and RellichKondrachov. These
are an unexpanded frontier, not demonstrated missing or failed dependencies.

The record includes all 42 manifest packages and 23 prescribed compatibility
patches: 11 before dependency resolution and 12 in `post_update`. Recording
these inputs establishes neither patch application nor that every package
or patch is used by these targets. Project dependencies have not been
materialized or patched here. The full source manifest is external under
[ARCHIVES.md](../ARCHIVES.md); hashes establish identity under this scanner,
not theorem truth.

## Native tool preparation

| Tool | Pinned source | Result on this Mac |
| --- | --- | --- |
| comparator | `d03acab154d269c06e60e4de7e4cc85deebff94b` | Source build passed with Lean 4.34.1; 21 jobs including exporter |
| lean4export | `076e8e57707e813375e8f9da8bf989799ace9680` | Separate source build passed with Lean 4.34.1; six jobs |
| landrun | `811cfff51ceaf3d9843708aa6d22e9b84ccac8b4` | Source retrieved; Linux binary not built or tested |

The compatible comparator/exporter sources advertise Lean 4.34.0. Both
built successfully with an explicit 4.34.1 override matching the proof
project. The newer tool HEADs inspected advertise 4.35.0 and were not used
for these builds. Native source compatibility is established on this host;
Linux builds and runtime integration remain separate checks.

Lean was installed under isolated temporary `ELAN_HOME` at
`/private/tmp/formal-replay-crosswalk-20261012/elan`; the user's default
toolchain was not changed. Actual version output:

```text
Lean (version 4.34.1, arm64-apple-darwin24.6.0,
commit 5045d0056413266e57c625dcd7c365b10e377c52, Release)
```

The builds used `ELAN_TOOLCHAIN=leanprover/lean4:v4.34.1`, the isolated
toolchain binary directory on `PATH`, and respectively
`lake build comparator lean4export` and `lake build lean4export`, in tool
checkouts separate from the mathematical project. The
[environment record](../numerics/replay_environment_20261012.json) includes
pins, executable and log identities, commands and null target result fields.
Native binaries and caches remain external and temporary. Mac binaries
cannot serve as Linux executables.

## Required checking environment

The host is Darwin, arm64, under an unprivileged user. No working Docker,
Podman, Colima, Lima, Multipass, Orb, UTM or qemu runtime was found. The
Docker path entry is a dangling link to an absent application.
`systemd-run` and `landrun` are absent. No VM was installed.

The pinned [comparator instructions](https://github.com/leanprover/comparator/blob/d03acab154d269c06e60e4de7e4cc85deebff94b/README.md)
require a trustworthy challenge closure and Lake configuration, no prior
potentially adversarial solution compilation in the checking environment,
correct Landrun operation, an unprivileged user, and the systemd
`RestrictAddressFamilies=~AF_UNIX` guard. The operating system, sandbox
and Lean kernel remain checker assumptions. A Linux container cannot be
assumed to satisfy them. The comparator uses Landrun's `--best-effort`;
functional isolation tests are necessary, not just startup success.

Use a fresh baseline for each configuration. Zeta and Dirichlet nominate
the same solution module; the first target compiles it, so that used
environment should not be called fresh for the second. Shared dependency
preparation requires an explicit cache/source trust policy.

## Execution status

All targets nominate `propext`, `Quot.sound`, `Classical.choice`, no
definition holes, and no additional kernel. Actual axiom reports,
comparator exit codes and kernel results are `null`. No mathematical
solution was compiled, comparator target run, or fake Landrun used.

The [portable guide](../numerics/REPLAY_GUIDE.md) records source preflight,
dependency preparation boundaries and the guarded invocation. Next select
a suitable Linux environment, verify effective isolation, materialize and
audit dependencies, then replay three targets in fresh baselines. The
[arithmetic crosswalk](2_ARITHMETIC_APPLICATION_CROSSWALK_20261012.md)
tracks separate application obligations.
