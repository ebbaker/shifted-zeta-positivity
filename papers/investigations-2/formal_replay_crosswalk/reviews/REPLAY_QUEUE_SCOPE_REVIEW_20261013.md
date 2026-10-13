# Replay queue scope and preservation review

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Reviewer: GPT-6 (Codex), inherited session configuration. Exact serving variant
and reasoning effort are not exposed and are not inferred.

This is a separate same-family source review of the host one-off queue; it is not external independent mathematical validation. No VM command,
snapshot operation, theorem compilation or queue launch was performed by the
reviewer. The frozen final script passed the author's offline controls and
the reviewer's independent response fixtures. No remaining launch blocker
was identified within the owned-VM scope described below.

## Initial review findings

The first frozen review copy was 42,649 bytes with SHA256
`1da74ab5f4a7a245e6bf6e10bb65a93ac653212ebb770d5e92260c6a87cb1784`.
The author was still editing. The following findings were sent to the author
before execution, and the first two were also sent immediately to the
coordinating agent:

1. The per-VM lock used `tempfile.gettempdir()`, allowing different `TMPDIR`
   values to create independent locks for the same VM. A fixed lock directory,
   independent of archive and environment, is required.
2. Runtime-only retry classification excluded a small catalogue of proof
   errors. A generic Lean/Lake compilation error followed by a timeout in a
   still-running parallel job could therefore trigger the automatic retry.
   Generic compilation/error markers must halt conservatively before the
   runtime-only branch.
3. Same-attempt runner duplicates were accepted by the quiescence predicate.
   A duplicate runner PID list must be refused, even when names match.
4. The nested process command needs to equal the exact recorded guarded
   command; observed timeout properties need to match its bound. Final loaded
   unit failure must not be overridden by success markers.
5. Preserved context records/scripts need rehashing on resume. Small record
   limits should be enforced when reading/copying, not only when serializing
   the final state.

Full command equality and initial/current guest runner SHA checks were already
present in that frozen copy; these corrected weaknesses observed during the
earlier live read. The review follows the final bytes, not an assumed filename.

## Required evidence boundary

An accepted target means that the unchanged pinned comparator reached its
complete acceptance markers with zero guarded-run exit status. It reports
permitted-set compliance, not an exact used axiom set; `actual_axioms` must
remain null. A successful transient unit can be garbage-collected before the
next poll, so explicit `LoadState=not-found` after quiescence may use the
durable runner/exit/acceptance evidence. A still-loaded unit must report
success. Other absent or failed property observations must halt. The host
record should state which evidence was observed.

The queue may adopt the existing zeta/001 process, and may launch only the
approved following attempts from a verified clean snapshot. Only a confirmed
runtime limit of the initial zeta attempt permits its one six-hour retry.
Resource failures, proof errors, failed preservation, ambiguous process
state and ambiguous interrupted mutation states must stop before a restore
or another launch.

## Final reviewed identity and validation

Reviewed final script: `run_replay_queue.py`, 52,659 bytes, SHA256
`a2468085fb8369994c561c8536307c0a6f2ff774d926fb91c20c819236b9cb11`.
The coordinating agent should verify that identity before launch; this review
does not apply automatically to later edits.

The reviewer reran all **34** author-provided offline controls and all **20**
independent controls in `queue_scope_review_checks.py`; both suites exited
zero with every control passing. The independent suite covers duplicate
same-attempt runners, reset while active, generic compile/build errors before
runtime expiration, resource failures, mismatched timeout bounds, failed
property queries, failed loaded units despite success markers, complete
guarded command equality, nested process-argv drift, four interrupted
mutation phases and the one-megabyte small-JSON boundary. These controls use
local harmless fixtures and fake responses. They never call Multipass.
The independent harness is 7,648 bytes with SHA256
`29359af2555b06f42c10ad1f3e21e64bc48b32238f5d1759d68f6482ef37e4d4`.
The author's saved checked result is 4,626 bytes with SHA256
`8fb0591cf744acaee6fda75aec8cc61c7f72b6c1565ce7a01663c1f3dcff8de9`.

An intermediate frozen candidate passed all 32 author controls but failed
the independent failure-summary variation `Some required builds logged
failures`. The author added that variation and explicit property-query
success requirements; the final suites confirm both corrections. The
earlier findings are resolved in the final bytes rather than waived.

## Final behavior assessed

- **Preserve before restore.** Completion requires quiescence, exact target,
  baseline, configuration, guarded command and process-command bindings.
  Guest JSON, full comparator log and source-preflight log are transferred
  to the external host archive, then checked against recorded SHA256 values
  and available sizes. The preserved JSON must equal the observed record.
  An immutable checksum list includes these files, the final probe and host
  result. Every baseline transition rechecks the host-result identity and
  all evidence checksums; corrupt or missing evidence refuses reset.
- **Exclusive ownership and adoption.** A fixed private directory under
  `/private/tmp` on macOS is independent of `TMPDIR` and archive arguments.
  The per-UID/per-VM lock uses no-follow file opening, ownership/mode checks
  and an exclusive nonblocking lock. Initial execution requires the existing
  zeta/001 record and matching guest runner identity. It polls that attempt;
  it does not launch another copy. Unknown attempts, duplicate runners,
  unowned mathematical processes and failed service inventory halt.
- **Fresh attempts.** The saved owned-VM baseline metadata is checked before
  each transition. After restoration and restart, the unchanged runner is
  transferred and hashed. The next record must be absent and both OAI and
  challenge compiled trees must be absent before launch. The runner itself
  repeats source preflight and freshness assertions under the established
  preparation contract.
- **Narrow retry rule.** Only an initial zeta/001 runtime timeout can select
  zeta/002. Runtime classification requires a successful live property
  query, `Result=timeout`, the exact live runtime limit, and supporting time
  duration or an explicit runtime-limit journal message. Generic compiler,
  build, proof and resource errors take precedence. Client timeout or a
  generic signal alone cannot authorize retry. Later timeouts halt. Queued
  runs use the existing six-hour runner bound.
- **Conservative resumption.** State writes use atomic replacement and a
  small-record limit. Saved input records, baseline information and both
  scripts are rehashed on resume and before baseline transitions; changed
  queue or runner bytes refuse resumption. Interrupted stop/restore/start/
  launch commitment phases halt for reconciliation rather than infer that
  an action did or did not finish. Host evidence is not silently replaced
  on resumption.
- **CLI and output scope.** Host subprocess calls use argument arrays,
  constrained VM/snapshot names and no host shell interpolation. The guest
  checker invocation preserves the quoted positional configuration argument.
  The archive must be outside the research checkout. Small inputs, probes,
  state and JSON results are bounded below one megabyte; full logs remain
  external and are allowed to be larger.

The review does not establish actual snapshot restoration behavior or target
acceptance: those require the real controlled run. The final queue relies on
the previously prepared owned snapshot, pinned tool/dependency records,
tested isolation and the trusted host/VM services. No exact axiom-set claim
or broader mathematical conclusion is added by this orchestration review.
