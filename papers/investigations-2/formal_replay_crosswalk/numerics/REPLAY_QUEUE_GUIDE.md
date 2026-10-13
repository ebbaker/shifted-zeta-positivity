# One-off replay queue

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and reasoning effort are not
exposed and are not inferred.

`run_replay_queue.py` is an ordinary long-lived host process. It adopts the
existing zeta/001 attempt, including the pinned runner's default `001` when
its original command omitted `--attempt`. It never launches another initial
zeta build. After verified preservation of a completed attempt, it restores
the owned clean VM baseline, transfers the unchanged target runner, and
runs Dirichlet/001 and Hecke/001 sequentially with six-hour bounds.

Only a confirmed runtime cutoff of zeta/001 permits one fresh-baseline
zeta/002 retry with a six-hour bound. Resource errors, compilation errors,
statement/axiom/kernel failures and unclassified outcomes halt after
preservation. A generic killed process or client timeout is insufficient to
authorize that retry. Runtime classification binds the named unit's timeout
result and actual runtime limit to its recorded command and duration or
explicit runtime-limit message.

Set `LANE`, `ARCHIVE_ROOT` and optionally `SAVED_BASELINE_INFO` to their
absolute host paths. The archive must be outside the research checkout.
The VM and full baseline arguments must match the saved lane environment.
The optional seed is the already saved Multipass snapshot-info JSON.

```sh
python3 run_replay_queue.py --selftest
python3 run_replay_queue.py \
  --lane "$LANE" --archive-root "$ARCHIVE_ROOT" \
  --vm rh-replay --baseline rh-replay.pre-math-replay-20261013 \
  --baseline-info "$SAVED_BASELINE_INFO" --poll-seconds 60
```

The parent agent may run this once as a detached process with idle-sleep
inhibition. This package has not launched the queue and has made no VM
operation. There is no scheduler, recurring automation or messaging.

The queue stores a small atomic `replay_queue_state.json` at the archive
root, and a uniquely named run directory with immutable preparation-context
copies, append-only full orchestration output and per-attempt evidence.
Its fixed per-host/UID/VM exclusive lock is independent of archive choice
and `TMPDIR`; the lock directory and file require private ownership and
no-follow checks. The guest probes refuse competing or duplicate runners,
unknown mathematical processes and failed service inventories.

Each attempt preserves its guest JSON, raw comparator log and source
preflight log, checking SHA-256 and available byte counts before any VM
stop or restore. Its small host result binds source/tool/dependency/cache
identities, baseline creation metadata and current runner/queue hashes.
`SHA256SUMS.txt` covers immutable evidence, the final probe and host result;
it excludes live state, orchestration and potentially still-changing runner
console output. The queue writes entirely to the external archive.

Normal interruption while waiting or copying can resume with the same
arguments and state file. Explicit failure or a crash at an ambiguous
stop/restore/start/launch boundary halts for state reconciliation; the queue
does not guess whether a destructive action happened. Preserve the named
state and full orchestration log when investigating such a halt.

Comparator acceptance still records permitted-axiom compliance and kernel
outcome, with the exact actual axiom set unset. A still-loaded final unit
must report success; an explicitly collected unit can instead use the
unchanged runner's bound systemd-run exit-zero and complete checker success.
The host result distinguishes those evidence sources.

All 34 internal controls passed without VM calls, including actual exclusive
lock refusal and fake-queue checks that mismatched or missing evidence
causes no reset and that adopting the active attempt causes no duplicate
launch. An additional offline integration fixture used the actual saved
lane records and a fake snapshot client: all context hashes, 42 dependency
identities and the zeta/Dirichlet/Hecke target keys passed. The test record
is `replay_queue_controls_20261013.json`. These tests check orchestration
guards; they are not mathematical theorem validation.
