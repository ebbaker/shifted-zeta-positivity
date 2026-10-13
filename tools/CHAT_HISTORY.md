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
