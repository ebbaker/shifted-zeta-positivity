# Creation metadata revision: verified chat refresh repair

16 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex assistance. Actual model and reasoning effort are unavailable in
the recorded configuration. Same-assistant implementation and checks.

The author requested repair of chat `01a1e55a-1a2c-71d0-87ca-bc9fe6ad675c`.
Its first capture recorded creation at `2026-11-16T17:14:09.839Z`; the
current paginated source records `2026-11-16T17:14:09.878Z`. The 39 ms
difference is not a timezone or calendar-date conversion. The exact-id
rollout's session metadata corroborates the latter timestamp. The entire
17-message archived public prefix, including its message identities and
timestamps, still matches the paginated source.

The recorder incorrectly required the original archive creation value to
remain identical to a current database metadata value. The upstream
[metadata upsert implementation](https://github.com/openai/codex/blob/main/codex-rs/state/src/runtime/threads.rs)
explicitly updates `created_at` and `created_at_ms` on an existing thread
(inspected 16 November 2026). This establishes that the current schema
does not promise immutability of those fields. It is consistent with the
observed revision; the exact background write that caused this local
change was not observed, and the live upstream branch is not an attestation
of the installed binary.

The repair separates the preserved original archive creation time from
the last verified source creation time. A new explicit immediate command,
`--reconcile-creation-time OLD_ISO NEW_ISO`, records one precisely pinned
within-second source revision. It requires automatic canonical paginated
selection, a registered archive, matching exact-id paginated session
metadata in the retained rollout, creation before the archived messages,
and all normal hash, public-prefix, turn-provenance, size, lock and
transaction checks. It is unavailable to hooks, deferred workers and
explicit source overrides. The rollout supplies corroborating metadata
only; it never replaces the paginated public-message source.

The audit records both exact timestamps, the checked prefix count/hash
and the metadata path. Future refreshes compare against that verified
source value, preserving original creation and first-capture provenance.
There is no automatic rounding or timestamp tolerance: a subsequent
unreviewed change, even within the same second, is rejected. Larger
calendar/timezone discrepancies require a separate diagnosis.

All 100 recorder tests passed, including seven new reconciliation tests.
The real repair recovered nine public messages, taking this archive from
17 to 26. A normal refresh and an exact prior completed-turn refresh then
returned unchanged. Original creation, first capture, number, filename
and all preceding public messages were verified unchanged. Other registry
entries were unchanged during this repair. Source databases, hook trust
and registered history JSON were not hand-edited.

The [small repair receipt](../papers/investigations-6/03_volterra_coefficient_dynamics/numerics/13_VCD_CHAT_CREATION_METADATA_REPAIR_20261116.json)
records the actual before/after identities and tests. Backups are outside
the repository. Subsequent capture times/counts belong to the live registry;
the receipt describes this repair, not future successful captures.
