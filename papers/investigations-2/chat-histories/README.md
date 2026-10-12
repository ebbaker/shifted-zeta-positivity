# Investigation chat histories

12 October 2026. Prepared for Edward Baker using GPT-6-astra (Codex;
`gpt-6-astra`), reasoning effort **ultra**, with substantial LLM assistance.

This folder stores conversations about the complete investigations-2
portfolio. Each project has its own `chat-histories/` directory and
`index.json`. Numbering is local to each history folder; it starts at one,
remains stable on refresh, and is distinct from historical chronology.

The initial conversation, **Review brainstorm directions**, is archived
here as chat 1. It contains the request to review the brainstorm folder,
the ranked recommendations, and the request to create all six projects,
along with completed public progress messages through capture. Project
histories refer to this shared context instead of duplicating the file.
Consult [index.json](index.json) for the filename, dates, message count,
capture time, hashes, and next number.

## Capture a Codex conversation

Run the recorder from the investigations-2 base folder. Supply the actual
session file and its recorded conversation metadata:

```sh
python3 record_chat.py \
  --codex-rollout /path/to/rollout.jsonl \
  --thread-id ACTUAL_THREAD_ID \
  --title 'Actual chat title' \
  --created-at 'ACTUAL_ISO_TIMESTAMP_WITH_TIMEZONE'
```

The example values are placeholders. The default destination is this base
history. To record a project conversation, add its exact folder name:

```sh
python3 record_chat.py \
  --project arithmetic_source_audit \
  --codex-rollout /path/to/rollout.jsonl \
  --thread-id ACTUAL_THREAD_ID \
  --title 'Actual chat title' \
  --created-at 'ACTUAL_ISO_TIMESTAMP_WITH_TIMEZONE'
```

`--project` accepts an existing direct project directory with `README.md`,
`notes/`, `numerics/`, and `reviews/`. The six names are listed in the
[overview](../README.md). Alternatively, `--folder /explicit/history/path`
sets a history directory directly; it cannot be combined with `--project`.
The recorder uses only Python's standard library. Run one writer at a time
for each registry.

## Import a selected conversation

```sh
python3 record_chat.py \
  --project function_field_covariance \
  --import-json /path/to/conversations.json \
  --conversation-id ACTUAL_CONVERSATION_ID
```

A single-conversation JSON can be imported without selecting its ID. A
multi-conversation export requires `--conversation-id`; the recorder does
not import an entire account by default. Original conversation fields are
preserved, with local archive metadata added. Do not put raw account exports
or raw Codex session files in the repository.

## Coverage and provenance

Each stored file is a JSON array containing one conversation in the familiar
ChatGPT mapping format. This is a local export-style record, not an official
provider export or a guarantee of compatibility with another importer.
Original dates and recorded message times are distinct from the capture
time. UTC and America/New_York timestamps are recorded where available.

Codex capture includes completed user and assistant text messages, including
commentary and final answers recorded through capture. It excludes system
and developer instructions, internal reasoning, tool calls and outputs,
subagent correspondence, and binary runtime data. Unsupported non-text
public content is rejected rather than silently discarded. Session model
and reasoning-effort settings are retained as provenance.

The capture is a snapshot. A final answer sent after capture is included
only by refreshing the same conversation later. The recorder preserves the
conversation's number and filename; it refuses shorter or older refreshes
unless `--allow-shorter-refresh` is intentionally supplied. A hash mismatch
in an existing registered history also prevents an automatic refresh.
Unregistered numbered JSON files reserve their numbers.

## File integrity and size

`index.json` records the file SHA-256 and a canonical conversation-content
SHA-256, excluding local archive metadata. These identify the data; they do
not validate its mathematical claims. Do not hand-edit a registered history
and then treat the old index as authoritative.

The recorder refuses individual conversation files of 1 MiB or more.
Follow [LARGE_FILES.md](../../../LARGE_FILES.md) for large non-regenerable
histories: preserve them externally with a small dated hash and lookup
record. Keep source exports outside the repository.
