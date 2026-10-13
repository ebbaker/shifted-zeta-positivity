# Linux setup checkpoint scope review

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred.

This is an internal evidence and scope review by the agent that prepared
the isolation fixtures. It is not an independent mathematical review or
an independent execution of the Linux commands. No VM commands, theorem
builds, new isolation tests, or repository edits were performed here.

## Assessment

The saved operational evidence supports proceeding to the first guarded
zeta comparator attempt after preserving the fresh VM baseline. No
blocking scope or evidence error was found in the setup checkpoint.
Statements of theorem execution, exact theorem axiom usage and seven-eighths
kernel acceptance must remain unset until the relevant target is checked.

The reviewed checkpoint is `notes/4_LINUX_REPLAY_ENVIRONMENT_20261013.md`
with the five small records bound by
`numerics/linux_vm_environment_20261013.json`. All five referenced records
match their recorded SHA-256 and byte count: tool build, dependencies,
isolation, trusted Mathlib cache and comparator integration.

## Isolation evidence

The Linux record contains sixteen distinct controls. The recorded operation
identities, operation success values, explicit errno, process exit status,
timeout status and expected file states agree in every control. The four
file-write/execution denials and two TCP denials yield `EACCES` (13), and
the AF_UNIX creation denial yields `EAFNOSUPPORT` (97). Each denied
operation exits 13. Permitted operations exit zero, including explicit-port
TCP controls and `.lake` build writes/execution; the denied writes leave
their files unchanged. No command timed out, and no startup failure was
misclassified as a successful denial.

The recorded runner SHA-256 is
`ed78b80c3b548a271896f46d331dc3f48d62287709d8c478ad4b816aae630cbe`,
matching both the staged fixture source and the proposed tracked copy.
The Landrun binary SHA-256 is
`d89541d39126a33f0eca4a676594533ed6da95d7f1183fe317b9f7de2354f887`,
matching the pinned Linux tool-build record and environment record.
The recorded UID is 1000, architecture is AArch64, and queried Landlock
ABI is 8. Guarded commands contain the pinned comparator's Landrun base
flags, project/build/export permission profiles, and the actual
`systemd-run --user --pty` AF_UNIX guard. Named units and service runtime
bounds only manage fixture lifetime.

One scope refinement should accompany this checkpoint: `--best-effort`
on ABI 8 does not provide the ABI 9 pathname UNIX-socket protections.
The tested systemd guard separately denies new AF_UNIX socket creation.
Do not describe this as ABI 9 isolation or comprehensive IPC isolation;
the fixture record already excludes inherited-descriptor and general
kernel attack claims. This distinction does not block the planned replay
under the stated comparator/operating-system assumptions.

## Toolchain, integration and source freshness

The tool-build record names the intended comparator, exporter and Landrun
commits, clean tracked tool sources and Lean 4.34.1 as the actual comparator
and exporter build toolchain. Both tools' configured 4.34.0 release remains
recorded as an override distinction. Linux binary identities agree across
the relevant records.

The integration log is 1,563 bytes and matches SHA-256
`4f83b45e15afb1cf691277c47a2d9c9b7b54f77ec31801db25d244b04bbc050a`.
It includes `Lean default kernel accepts the solution` and final comparator
success, with outer process exit zero and no timeout. Its challenge's
intentional `sorry` is consistent with a statement-comparison fixture:
the solution is exported and replayed separately. This establishes a small
commutativity integration check only. It provides no zeta, Dirichlet or
Hecke result.

The dependency preparation record reports all 42 original package pins,
all 23 prescribed patches, unchanged original manifest, and no Lean/Lake
execution during that stage. The source preparation script hashes all
2,959 critical inputs at the intended upstream commit and checks a clean
sparse source checkout. The cache-preparation script requires absence of
the main mathematical build directory before preparation and checks absence
of the OAI build tree afterwards. These checks, plus the planned stopped-VM
baseline, support the stated fresh-checking-environment policy. Preserve
and identify the completed baseline before launching comparator, and use
fresh baselines for each target.

## Cache and theorem evidence boundaries

The recorded cache invocation explicitly uses the official Mathlib
repository and `--cache-from=master` at Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. Its exit is zero, and source
manifest SHA-256 before and after is unchanged. The preparation script
removes inherited cache-scope overrides. The saved policy explicitly
trusts cache contents as a distribution artifact rather than independently
validating them from their source-input keys. The checkpoint communicates
that trust correctly.

Preserve the actual `trusted_mathlib_cache.log`, with the recorded size and
hash, before restoring the VM. Its reported 8,908-artifact count is an
execution-log fact; it is not present in the small cache record reviewed
here. At this review time the host staging directory exposed the wrapper
preparation log but not that full cache log. This is a preservation detail
to resolve before finalizing the archive, not grounds to claim cache
failure or to repeat the download.

All three investigation target records currently leave actual axioms,
exit status and kernel result null. That is correct. The unchanged pinned
comparator checks the permitted-axiom restriction but does not print an
exact used set or preserve its accepted export. A supplementary later
export must not be presented as byte-identical to that accepted export.
Even later comparator success will leave the arithmetic U1–U7 application
ledger separate from the nominated formal theorem statement.

The VM baseline was accurately labelled `pending_snapshot` in the reviewed
environment record. Update it to the actual completed snapshot identity
once preservation succeeds; do not infer success from requesting a snapshot.
