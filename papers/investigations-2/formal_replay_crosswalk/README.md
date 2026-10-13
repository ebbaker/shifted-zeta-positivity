# Formal replay and arithmetic crosswalk

Initialized 12 October 2026; updated 13 October 2026. Prepared for Edward
Baker with substantial LLM assistance. Owner: ChatGPT and Codex lane.
Model: GPT-6 (Codex), inherited session configuration; exact serving variant
and reasoning effort are not exposed and are not inferred. Internal model
assessments are not independent mathematical validation.

Current replay status, 13 October 2026: the one-off queue completed at 04:01:53 EDT. All three pinned targets were accepted by the unchanged comparator and the Lean default kernel: [zeta](numerics/replay_zeta_001_20261013.json) in 78 minutes 36 seconds, [Dirichlet](numerics/replay_dirichlet_001_20261013.json) in 70 minutes 59 seconds, and [Hecke](numerics/replay_hecke_001_20261013.json) in 58 minutes 39 seconds. Each record binds its exact configuration, guarded fresh-baseline execution, statement agreement, permitted-axiom compliance and preserved raw evidence. The arithmetic crosswalk remains partial; new applications are uncompiled.

The [completion checkpoint](numerics/replay_queue_completion_20261013.json) binds all three result records and the immutable final queue state. Total wall time from the first zeta attempt through final preservation was 3 hours 30 minutes 49 seconds, including baseline resets. At the later VM check, Multipass was running with zero load and no reported errors.

This lane checks the pinned seven-eighths formal statements and builds an
application crosswalk from the October 5 arithmetic argument to the
September 30 source and its Lean constants. Claude's parallel lane is
[Newman certificate auditing](../newman_certificate_audit/README.md).
The [strategy assessment](../brainstorm/reviews/STRATEGY_AND_PARALLEL_LAYOUT_REVIEW_CODEX_20261012.md)
gives the agreed order and remaining qualifications.

## Linux checkpoint: 13 October 2026

The [Linux environment note](notes/4_LINUX_REPLAY_ENVIRONMENT_20261013.md)
and [bound environment record](numerics/linux_vm_environment_20261013.json)
document Ubuntu 26.04.1 LTS in the local Multipass VM `rh-replay`, pinned
Linux tool builds, all sixteen passing operational isolation controls,
42 verified dependency pins, 23 verified prescribed patches, the trusted
official Mathlib master cache and the comparator's small commutativity
integration check.

The guest uses direct Lean 4.34.1 binaries and has no elan installation.
Landrun operates at ABI 8 in best-effort mode; the tested systemd guard
denies new AF_UNIX sockets. The controls establish their recorded
permission-profile behavior, not comprehensive operating-system isolation.
The cache remains an explicitly trusted distribution artifact.

The stopped-VM baseline `rh-replay.pre-math-replay-20261013` was saved before
mathematical compilation. Each of the three accepted attempts started
from that baseline; every completed record, full raw log, source preflight
and final probe was preserved externally before a subsequent restoration. The [replay guide](numerics/REPLAY_GUIDE.md)
describes the checked command syntax, direct tool paths and restoration
protocol.

The three preserved acceptances establish statement agreement,
permitted-axiom compliance and the default-kernel outcome under the checker
assumptions. The pinned checker does not emit an exact used-axiom set or
the digest of its accepted export. Actual axiom sets remain unset, and a
later supplementary export cannot be presumed identical to the accepted
one. All three exact nominated targets were accepted; this does not compile
the new October 5 application terms.

The reviewed [one-off replay queue](numerics/REPLAY_QUEUE_GUIDE.md) completed its sequence of zeta, Dirichlet and Hecke attempts, preserving each result and restoring the clean baseline between targets. All 54 offline controls passed before launch. The [historical launch checkpoint](numerics/replay_queue_launch_20261013.json) and [archive guide](ARCHIVES.md) locate the preparation and completed evidence. An immutable copy of the final phase-complete queue state is bound in both final target records. The recorded temporary keep-awake process was no longer present at the 07:49 EDT observation; no other processes were stopped.

## Arithmetic source continuation: 13 October 2026

The [smooth-weight source pass](notes/5_SMOOTH_WEIGHT_UNIFORMITY_SOURCE_PASS_20261013.md) gives a conditional paper-level derivation of the uniform quadratic seminorm bound. It preserves the derivative-order quantifiers, central scale normalization, positive capacity margin and bounded scales. The new profile, partition and dilation applications remain uncompiled, and transfer to the October 5 arithmetic family still requires U1.

The [unit-row source pass](notes/6_UNIT_ROW_AMPLIFICATION_SOURCE_PASS_20261013.md) locates the arbitrary-column-scale amplification declaration and derives the unit-row exponent with exact cutoffs and losses. [Smooth-weight](reviews/SMOOTH_WEIGHT_SOURCE_SCOPE_REVIEW_20261013.md) and [unit-row](reviews/UNIT_ROW_SOURCE_SCOPE_REVIEW_20261013.md) scope assessments found no concrete defect in these conditional derivations; they remain same-family reviews and new applications remain uncompiled.

The [fixed-character source pass](notes/7_FIXED_CHARACTER_ROW_DICTIONARY_SOURCE_PASS_20261013.md) gives the explicit RowData dictionary, conditional on a residue presentation agreeing with the supplied character and its original zeros. Its [scope review](reviews/FIXED_CHARACTER_SOURCE_SCOPE_REVIEW_20261013.md) found no concrete defect. The classical-character presentation, arbitrary finite mask and combined Lean application remain uncompiled.

The [canonical-energy crosswalk](notes/8_CANONICAL_ENERGY_CROSSWALK_20261013.md) gives a conditional source route for U4 with exact row support, unit-label weight domination, the dyadic factor four, finite restoration of extra excluded primes and derivative order chosen before arbitrary support intervals. Its [source-contract record](numerics/canonical_energy_crosswalk_20261013.json) identifies 38 Lean files and 43 anchors; all 2,926 copied OAI source files were verified against the preserved manifest. The [scope review](reviews/CANONICAL_ENERGY_SOURCE_SCOPE_REVIEW_20261013.md) found no concrete mathematical defect in this conditional derivation. The genuine character presentation and new assembled Lean applications remain uncompiled.

## First source milestone: 12 October 2026

- [Environment and tool preparation](notes/1_REPLAY_ENVIRONMENT_AND_TOOL_PREPARATION_20261012.md): exact source/tool pins, native Lean 4.34.1 tool builds, Linux requirements and the execution limits at that milestone.
- [Arithmetic application crosswalk](notes/2_ARITHMETIC_APPLICATION_CROSSWALK_20261012.md): October 5 to September 30 substitutions, 26 exact Lean declarations, and unresolved application ledger U1–U7.
- [Formal statements and Hecke bridge](notes/3_FORMAL_STATEMENTS_AND_HECKE_BRIDGE_20261012.md): all three universal target contracts, ideal-series normalization, ray-character interpretation and principal exceptions.
- [Source checker and records](numerics/README.md), [replay guide](numerics/REPLAY_GUIDE.md), and [external archive guide](ARCHIVES.md).
- [Internal scope review](reviews/FIRST_MILESTONE_SCOPE_REVIEW_20261012.md): same-family assessment; a Claude review remains outstanding.

The source checker verified 2,926 OAI modules plus three challenge modules,
and 2,959 critical files, against the exact pin. Its source graph left
252 external imports as an unexpanded frontier. All ten source-fixture
controls passed, as did the native comparator/exporter builds. Mathematical
comparator replay had not run at that historical milestone.

Source algebra supports the two terminal moment/extraction correspondences
identified by Claude. Exact Lean applications still require the fixed-data
dictionary, smooth-weight uniformity and arbitrary-scale unit-row
amplification. A weighted Fourier transfer theorem provides a concrete
route to the uniformity obligation. The compressed October 5 proof route
and its two-Poisson transfer remain separately unresolved.

## Next bounded tasks

1. Obtain a scoped review of the three completed replay records, including
   exact configurations, source/tool/dependency bindings, permitted-axiom
   compliance, kernel outcomes and trust assumptions. The original checker
   does not emit exact used-axiom sets or accepted-export digests.
2. Continue the October 5 to September 30 to Lean application crosswalk.
   Preserve normalization, signs, zero extensions, exclusions,
   smooth-profile classes, parameter ranges and uniformity. Classify each
   link as identical, justified specialization or unresolved. Successful
   formal target replay does not close U1–U7.
3. Obtain a Claude review of the deliverables and write a ChatGPT review
   of Claude's first Newman supplier report. Each is a new uniquely named
   review; the project owner maintains the indexes.

The upstream replay pin is `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`,
inherited from the arithmetic source audit. Liu's verifier pins
`adc7f1241b42e322a6451854ab7e4b4c146bf78a`; its extension is an optional
separately recorded target. The brainstorm record reports matching upstream
closure source blobs. Source correspondence alone does not establish
successful formal replay.

## Research records and ownership

- `notes/`: statement reading, contracts, crosswalk and derivations.
- `numerics/`: replay scripts, small execution records and source hashes.
- `reviews/`: scoped assessments of this lane.
- `chat-histories/`: selected conversations with a single recorder.

Treat the existing [arithmetic source audit](../inactive/arithmetic_source_audit/README.md)
as reference material. Cite its records without copying, renaming or
rewriting its history. Keep shared portfolio and brainstorm indexes for a
single integration writer. Separate folders do not isolate Git operations;
concurrent workers should use separate clones or worktrees.

Follow [LARGE_FILES.md](../../../LARGE_FILES.md) and [ARCHIVES.md](ARCHIVES.md).
Keep large logs, caches, dependencies and regenerable output external.
The source manifest is reached through `FORMAL_REPLAY_ARCHIVES`. Maintain
any future manuscript at a stable path, identify Edward Baker or state
drafted for him, acknowledge LLM assistance, and record milestones in
`DRAFT_HISTORY.md`. Create no draft snapshot folders.
