# Automatic research chat history

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded session configuration: `gpt-6.1-sol`, reasoning effort **ultra**.

The [refresh tool](refresh_chat_history.py) updates a registered research
conversation after new public messages are recorded. It retains the chat's
original number and filename, checks its stored and canonical identities,
and requires the earlier messages to remain an unchanged prefix. An
unchanged capture leaves the files byte-identical. The existing
[recorder](../papers/investigations-2/record_chat.py) supplies the archive
format; the wrapper adds source checks, serialized writes and recoverable
installation of the conversation and its registry.

The project standing policy is [AGENTS.md](../AGENTS.md). Raw transcripts
remain outside the repository. Only completed public user and assistant
text is archived, including visible progress messages. Private instructions,
reasoning, tools and subagent traffic are excluded. Unsupported public
attachments or source formats are reported; they are not silently removed.

## Refresh an existing chat

Run from the repository root, using the actual thread id. The tool locates
its unique registered history and the exact local source session. Supply
`--rollout /path/to/rollout.jsonl` when the source is elsewhere or discovery
is ambiguous.

```sh
python3 tools/refresh_chat_history.py --thread-id ACTUAL_THREAD_ID
```

An unregistered chat is skipped. To register a new research conversation,
choose its investigation and use its actual title:

```sh
python3 tools/refresh_chat_history.py \
  --thread-id ACTUAL_THREAD_ID \
  --rollout /path/to/rollout.jsonl \
  --history-dir papers/investigations-2/PROJECT/chat-histories \
  --title 'Actual chat title'
```

The original creation timestamp is read from the source. The destination
must stay within the repository and be a history folder. A chat registered
in multiple folders needs an explicit destination. The default session
location is `$CODEX_HOME/sessions`, or `~/.codex/sessions` when unset.
The exact recorded session id must match the requested id.

## Move an existing chat to another investigation

Procedure added 14 October 2026. Prepared for Edward Baker with substantial
LLM assistance; recorded model `gpt-6.1-sol`, reasoning effort **ultra**.

When the user requests a different investigation destination, relocate the
existing registration rather than importing the conversation again. Keep
one canonical registration. The user's explicit destination authorizes
the move; clarify only if the destination itself is ambiguous. Preserve
the original conversation id, number, filename, title, creation times,
first-capture fields, every earlier public message, and all other existing
entry metadata. Relocation time is separate from first-capture time.

**The refresh CLI has no relocation command.** Passing a new
`--history-dir` for an already registered conversation is rejected. The
flag selects a refresh or initial registration destination; it does not
move an archive. Do not re-register the conversation, edit its public
transcript, or use the flag to conceal duplicate registrations. Preserve its
number unless the user explicitly requests renumbering.

### Explicitly requested renumbering

17 October 2026. Prepared for Edward Baker with substantial LLM assistance;
recorded model `gpt-6.1-sol`, reasoning effort **ultra**.

The ordinary relocation procedure below preserves numbers and filenames.
When the user explicitly requests renumbering, choose the destination's next
unused number, respecting its counter and every reserved numbered file.
Update the registry number and filename and only the archive's
`archive_metadata.history_number`; preserve all other parsed archive fields.
The canonical conversation-content hash must remain unchanged. Recompute the
stored-byte hash and size, and verify embedded and registry numbers agree.
Record old/new numbers, filenames and stored hashes, preserved creation and
first-capture times, and the explicit authorization in the relocation receipt.
Use the same locks, durable backups, transactions and rollback gates below.
The [17 October affiliation correction](../papers/investigations-2/formal_replay_crosswalk/CHAT_HISTORY_RELOCATION_20261017.json)
is a checked precedent, not a script to replay. Routine refreshes retain
the resulting number and filename.

### Prepare and validate

1. Refresh completed public text at the current destination using the
   ordinary refresh command. Finish any outstanding bounded final-capture
   worker before starting the transfer. Identify the exact thread id and
   current registry entry; use the requested investigation's existing
   `chat-histories/` folder or create that folder under its existing parent.
2. Use a reviewed, single-purpose migration built on the validation,
   locking and transaction helpers in
   [refresh_chat_history.py](refresh_chat_history.py). Historical temporary
   migration scripts are evidence of earlier moves, not reusable or
   idempotent command-line tools. Do not perform a manual file move or
   hand-edit registered JSON. Acquire `registry_lock` for **both** source
   and destination, in sorted path order, and hold both through the transfer
   and its integrity checks. Legacy recorders must not run concurrently.
3. Under those locks, call `recover_transaction` for both folders before
   reading their indexes. Use `safe_directory`, `read_index`, and
   `read_registered` to validate paths, registry identity, stored-byte and
   canonical-content hashes. Check the other registered files against
   their hashes and save their digests for the final comparison. Reject
   unexpected duplicates, filename collisions, symbolic links, altered
   captures, or unrecognized pending state before changing files.
4. Prepare the new indexes without re-rendering the conversation. Transfer
   its archive bytes and complete registry entry unchanged. Remove only
   that entry from the source index. Preserve the source `next_number` so
   its historical number is not reused. Set the destination `next_number`
   above the moved number and all existing registered or reserved numbered
   filenames, without reducing its previous counter. A moved chat can
   therefore remain number 7 in a newly created registry. A destination
   without `index.json` starts from `read_index`'s empty-registry default;
   keep its preexisting README and unrelated files.
5. Before mutation, write durable rollback copies outside the repository
   of both original indexes and the conversation bytes. Explicitly record
   an originally absent destination index. Write a separate relocation
   journal containing the paths, id, filename, expected old/new index
   hashes, archive hash and operation phase. Flush the backups and journal
   before the first install. Do not place raw session exports in Git.

### Install and verify

1. Validate the proposed indexes with `validate_index`. Install the copied
   archive and destination index through `_install_transaction`, retaining
   the wrapper's paired-file recovery checks. Read the destination back
   with `read_registered` and verify byte identity **before** removing the
   source registration or archive.
2. Replace the source index atomically using `write_sync`, `os.replace`
   and `fsync_dir`, retaining all other entries and metadata. Remove the
   old archive only after rechecking that its hash matches the verified
   destination. Never remove another chat or an unexpected file.
3. Verify that `find_registered` discovers exactly the destination, the
   source no longer registers the chat, and the old archive is absent.
   Recheck archive bytes, all preserved identity and provenance fields,
   unrelated archive hashes, and both numbering counters. Finish the
   relocation journal as committed only after these checks succeed.
4. Save a small permanent relocation record in the destination
   investigation, such as `CHAT_HISTORY_RELOCATION_YYYYMMDD.json`. Record
   the reason, exact identity, old/new paths, preserved number and
   filename, creation and first-capture times, stored and canonical hashes
   **at the move**, message count, counters, verification time, integrity
   results, and rollback-backup location. Include the actual model and
   effort when recorded. Later refreshes legitimately change the capture
   hash and count; this receipt identifies the transfer snapshot.
5. Update the old and new history READMEs and investigation links to point
   to the sole new archive. Leave a historical pointer at the old location,
   not another registration or transcript copy. Resume ordinary refresh
   and arrange the current turn's bounded final capture at the new home:

   ```sh
   python3 tools/refresh_chat_history.py \
     --thread-id ACTUAL_THREAD_ID \
     --history-dir papers/investigations-2/DESTINATION/chat-histories

   python3 tools/refresh_chat_history.py \
     --thread-id ACTUAL_THREAD_ID \
     --history-dir papers/investigations-2/DESTINATION/chat-histories \
     --after-turn ACTUAL_CURRENT_TURN_ID --wait-seconds 60 --defer
   ```

   Run the deferred capture as the last tool action, then send the real
   final reply promptly. Automatic discovery also works once registration
   is unique. The explicit path shown here verifies the intended home.

### Rollback and interrupted moves

A cross-folder relocation is **not one atomic transaction**. The wrapper
recovers each folder's paired chat/index install; it does not automatically
recover the whole move, the source-index replacement, or source deletion.
After an interruption, inspect and recover the separate relocation journal
under both shared locks before another refresh or migration. Temporary
duplicate registrations can be an interrupted install; selecting one with
`--history-dir` does not repair that condition.

For an exception, verify every destination against the journal's expected
old/new hashes before rollback. Restore the original archive and source
index, restore the previous destination index, and remove only the exact
verified copy created by this move. If the destination index was originally
absent, remove the newly created index rather than inventing an empty
original. Preserve unrelated files and recheck unique original
registration. Keep the rollback copies and journal until recovery is
verified. Unexpected bytes or an unresolved rollback require stopping and
reporting the condition; do not overwrite them or delete transaction state
to make the refresh proceed.

Three completed precedents record this procedure:

- [Portfolio relocation, 13 October 2026](../papers/investigations-2/CHAT_HISTORY_RELOCATION_20261013.json).
- [Investigation 21 relocation, 14 October 2026](../papers/investigations-2/active/21_quaternion_theta_geometry/CHAT_HISTORY_RELOCATION_20261014.json).
- [Repository-root registry to the early Codex logs, 16 October 2026](../early-chat-logs/chatgpt-codex/CHAT_HISTORY_RELOCATION_20261016.json).
  The destination is outside `papers/`, which `find_registered` does not
  scan, so unique registration was checked across every `index.json`; the
  emptied root registry was then removed at the user's request.

Their receipts describe past moves. Use the current helpers and current
registry state for a future move; never replay old ids, paths, hashes,
counters or temporary scripts as though they described the new operation.

## Capture the final reply after it is sent

A normal save inside a turn cannot contain that turn's unsent final reply.
For the direct standing workflow, make this the final tool action before
sending the answer:

```sh
python3 tools/refresh_chat_history.py \
  --thread-id ACTUAL_THREAD_ID \
  --after-turn ACTUAL_CURRENT_TURN_ID --wait-seconds 60 --defer
```

The detached worker waits for the actual public final message and completion
of that exact turn, refreshes the same registered conversation and exits.
It is bounded and does not schedule future model work. A timeout or source
failure must not be presented as a successful capture. Check its returned
status location or the registry on the next turn. Refresh at the next turn's
start to catch a response missed by a stopped or interrupted worker.

## Native completion hooks

The repository [hook definitions](../.codex/hooks.json) call the same tool
for submitted prompts and completed replies. The current local ChatGPT
project mirror has a matching bridge to this repository tool. Existing
computer-use notifications are preserved.

The installed CLI reports lifecycle hooks enabled. New hook definitions
still require the user's one-time platform review and trust. Open `/hooks`
in the Codex CLI for this workspace to review them, then resume or reopen
the conversation if needed to reload configuration. Do not use a hook-trust
bypass or add a managed-hook exception. Until native activation is verified,
use the direct standing workflow above.

The completion hook runs in the background so the turn can finish while
its transcript is being saved. Progress messages are included at the next
capture; streaming fragments are not separately archived. Local command
hooks depend on a locally accessible session and repository. These are the
[official hook lifecycle and trust rules](https://learn.chatgpt.com/docs/hooks);
[project instruction discovery](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
explains the local override used by the mirror.

## Integrity and recovery

The tool holds `.chat-history-refresh.lock` for each registry and uses an
ignored `.chat-history-transaction/` to stage paired archive/index updates.
It checks recovery state before a later save. Do not delete those runtime
files to bypass a reported inconsistency. A manual legacy capture must be
serialized with automatic writers; use this wrapper for Codex refreshes.

The first capture time remains historical provenance. `captured_at` records
the latest successful refresh. Consult `index.json` for current counts,
times, models, sizes and hashes. Hashes identify the data and do not certify
its mathematical statements. Conversation and registry files remain below
1 MiB; an oversized source needs the external archive procedure in
[LARGE_FILES.md](../LARGE_FILES.md), rather than an automatic truncated save.

The tool uses the Python standard library and POSIX file locks; it runs on macOS and Linux without a network dependency. Existing legacy writers remain unlocked and must be serialized manually with the wrapper. A first registration interrupted before its registry exists may need the same explicit history destination on retry. Older records that had already been refreshed before first-capture fields existed preserve their earliest available capture timestamp. Run the focused checks with:

```sh
python3 -m unittest discover -s tools/tests -p 'test_refresh_chat_history.py'
```
