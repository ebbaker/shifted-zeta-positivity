# Internal scope review of the first formal-replay crosswalk milestone

12 October 2026, client date. Prepared for Edward Baker with substantial
LLM assistance. Reviewer: GPT-6 (Codex), inherited session configuration;
the exact serving variant and configured reasoning effort are not exposed
and are not inferred.

This is a same-family internal review. The reviewer also authored note 3
and its statement-contract record; that portion is a self-review. This is
neither an independent mathematical review nor a review by Claude.

**Finding.** The revised artifacts are suitable to save as a partial,
source-inspection first milestone. I found and reproduced a small-record
verification gap during review; the current consumer repairs it, and the
repaired command rejects the corresponding tampering. I found no remaining
scope blocker in the reviewed versions. Mathematical comparator replay,
actual axiom reports, and the October 5 application ledger remain open.

## Scope and evidence examined

I read the environment note, arithmetic crosswalk, formal-statement/Hecke
note, their three JSON records, source-inventory record and consumer,
portable replay guide, and external-archive guide. I inspected relevant
pinned Lean definitions and declarations and the pinned comparator README.
The mathematical source pin is openai/math
`fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`; the comparator README inspected
is at `d03acab154d269c06e60e4de7e4cc85deebff94b`.

I ran only source-inventory verification and its small negative controls.
I did not build a mathematical solution, run a target through comparator,
execute the future Linux commands, inspect every proof in the closure, or
independently repeat the auxiliary-tool builds. Native Mac build success
is recorded by the root task; it is appropriately separated from target
replay in the environment note and JSON.

The reviewed source consumer has SHA-256
`d71f0cafdf6457da7a5a19b4f0e4a5000b30e219fcbdeb3b6e81cc3b334ebd50`;
the revised small source record has SHA-256
`122c153264c38a40f1af9674deec329026c432c8f12992536d9def529168cfcf`.
The external full manifest remains 1,958,471 bytes, with stored SHA-256
`b0bd1f6b77e23bec0a78811a644114eb12dea6e55138620c82ef76a00af77c48`
and canonical SHA-256
`b376fb72817e7bc0bd88c1de0bffb7eedde6f7dd670781c3b593d39fd3f00862`.

## Repaired finding: source identity did not bind saved evidence fields

The initial `--verify-record` consumer verified the external closure
manifest but did not compare the saved small record's substantive evidence
or generator identity against a regenerated small record. A fixture with
the correct closure binding and current generator identity, but with
`scope.proof_checked=true` and fabricated `reported_axioms`, returned
success. Those fields could therefore contradict the actual source-only
operation while being presented as a verified record.

The revised consumer compares the complete deterministic small record and
its schema, including generator bytes/hash. It masks only named incidental
timestamp, machine availability, absolute paths, and package-presence
values. Unknown evidence keys survive that projection and cause refusal.

I independently reran the revised CLI against the pinned checkout and the
external manifest, with these results:

| Input | Exit | Observed result |
| --- | ---: | --- |
| Authentic committed-candidate source record | 0 | `source_record_and_manifest_identity_verified; formal_replay_not_run`, 2,929 local modules |
| Correct current generator, altered proof/axiom evidence only | 2 | Deterministic mismatch in `scope, targets` |
| Altered saved generator hash | 2 | Deterministic mismatch in `generator` |
| Added proof-evidence key inside `environment` | 2 | Deterministic mismatch in `environment` |
| Changes limited to explicitly incidental paths/environment/presence values | 0 | Same source-only verification status and manifest hash |

The consumer's ten small controls also passed, including wrong pin,
changed source, missing source, missing/changed external manifest,
comment/string import handling, unsupported import syntax, changed
proof/axiom evidence, generator identity and unexpected evidence keys.
These are meaningful source-consumer checks, not end-to-end comparator
tests or a proof-integrity audit. Keep these controls with future consumer
changes; do not reinterpret the exit-zero source status as formal success.

## Mathematical and formal scope

The arithmetic note distinguishes source deductions, read Lean contracts,
and newly compiled applications. Its terminal raw-moment exponent and
sixth-power extraction comparison are useful source deductions. The note
preserves two important limitations: a fixed-test existence constant does
not establish uniform quadratic `C^k` dependence, and an endpoint stated
for eventual large `U` with `D=U^r` cannot be specialized to `U=1` to cover
arbitrary large `D`.

The located `rawMoment_reference` transfer genuinely supplies a quadratic
weighted-Fourier constant. Ordinary derivative control, fixed-annulus
dilation/partition and October 5's order of quantifiers (`k` before the
arbitrary support interval) are still application work. The exact
additive-character dictionary retains `paperE(z)=breveE(z/eisLam)`; this
avoids silently equating the two normalizations.

The completed-sum identity is kept separate from its cutoff bound, and
the reflected-row declarations retain controlled arithmetic, simultaneous
geometry, margin and small-completion hypotheses. The note does not claim
that the generic canonical completion estimate is the all-row October 5
`prop:R` contract. Its U1–U7 ledger therefore identifies substantive
remaining applications instead of treating matching theorem names or
imports as sufficient evidence.

The statement/Hecke note correctly preserves strict `Re(s)>7/8`, universal
modulus/character/height coverage, the principal-pole conjunction, the
totalized zeta convention at one, and the distinction between nominated
and reported axioms. The finite residue/ray interface, unit quotient,
element-to-ideal factor six, defining-modulus zero masks and positive-real-
part Euler-factor nonvanishing are supported by named source contracts.
The abstract idelic interpretation and conventional completed-factor
comparison are labelled semantic inferences. The inspected source has a
concrete ray-family corollary; a generic abstract idelic equivalence was
not established in this milestone.

This review does not promote any source declaration to accepted proof.
Permitting `propext`, `Quot.sound` and `Classical.choice` is not an actual
axiom-dependency report. `definition_names=[]` nominates no additional
definition holes; it does not independently validate semantic definitions.

## Command and archive boundaries

The source consumer uses argument-list Git queries, compares reached file
bytes to pinned Git blobs, rejects symlink/escape paths, checks relevant
worktree/index changes, and rechecks reads for concurrent modification.
It invokes no Lean/Lake/elan wrapper and writes only explicitly named
outputs outside the upstream checkout after validation. Its lexical import
scanner is a reproducible navigation/identity mechanism. It does not
elaborate Lean, validate the 252 external imports, materialize all 42
packages, or apply the 23 compatibility patches.

The replay guide's shell arguments are quoted, and the configuration is
passed as a positional argument to the inner shell. The invocation retains
the pinned comparator README's unprivileged user service and
`RestrictAddressFamilies=~AF_UNIX` guard. It also passes the isolated Lean
environment explicitly. I did not execute this command; effective Linux
sandboxing remains a required operational check. The guide explicitly
requires harmless denied/permitted-operation fixtures and separate service
and comparator outcomes, so a startup or job-submission success is not
presented as replay success.

Dependency preparation is correctly treated as executable configuration
requiring trust review, and future mathematical solution compilation is
reserved for comparator in a fresh checking baseline. Zeta and Dirichlet
share the same solution module; the guide correctly requires separate
fresh baselines. Native Mac executables are not presented as Linux tools.
Trusted cache provenance, package/patch audit and manifest drift are left
explicit rather than hidden by a reduced dependency configuration.

The large full manifest, binaries, caches and full logs are external.
The consumer checks normal-lane lookup before the environment override and
fails closed on missing or mismatched manifest data. The archive guide
keeps regeneration output separate from the saved source record. These
boundaries match the first milestone's source-only claims.

## Required next actions and limits

1. Select a suitable Linux destination, validate effective isolation,
   prepare and audit pinned dependencies, and replay each target in a
   fresh baseline. Record actual exit status, checker result and reported
   axioms; keep the current null result fields until then.
2. Complete U1–U2 before claiming the October 5 moment's full quantified
   contract, then U3–U4 for arbitrary-scale extraction and canonical energy
   specialization. A newly compiled application should preserve all
   masks, row multiplicity, seminorm dependence and parameter ranges.
3. Treat U5–U7 as separate proof-route work. Even successful replay of all
   three universal conclusions will not by itself discharge the all-row
   reflected bound, complete two-Poisson transfer or the simultaneous
   theta dictionary needed by that route.
4. Obtain an independent mathematical or cross-family review before
   describing this internal source pass as independent validation.

No remaining artifact change is required by this scoped review. The
milestone is preparation plus source crosswalk, with operational replay
and specific arithmetic applications still pending.
