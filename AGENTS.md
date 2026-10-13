# Shifted zeta positivity project instructions

Follow the investigation's instructions and `LARGE_FILES.md`. Save incremental
research in its `notes/`, computations and small execution records in
`numerics/`, and assessments in `reviews/`. Include dates, the intended
author, LLM assistance, and the actual recorded model and effort when
available; do not infer unavailable settings. Manuscripts name Edward Baker
or state they were drafted for him and acknowledge LLM assistance. Maintain
concise milestone entries in the investigation's `DRAFT_HISTOR.md`; create
no new manuscript snapshot folders.

## Automatic research chat history

The user authorizes ongoing capture and refresh of research conversations
for this repository once their investigation destination is known. Routine
captures and refreshes do not need renewed approval. Keep each chat in its
investigation's `chat-histories/`; use a base history only for a conversation
about the shared portfolio. Resolve an ambiguous destination from the task
and existing registry before creating a new entry.

Use `tools/refresh_chat_history.py` and follow `tools/CHAT_HISTORY.md`.
For a new research chat, register its actual thread id, source transcript,
actual title and selected history folder. For an already registered chat,
refresh at the start of a new turn to catch any unsaved preceding response.
Before finishing each reply, refresh completed public text and arrange the
bounded exact-turn follow-up with `--after-turn` and `--defer`, unless an
active trusted completion hook already supplies that capture. Make that
follow-up the last tool action and then send the final answer promptly.
The worker must wait for the real final message and completed turn; never
write a planned answer into a transcript. A trusted completion hook is the
preferred automatic mechanism and captures after the reply is recorded.

Preserve original creation time, number, filename, first-capture provenance
and all earlier public messages. Read current capture times, counts, sizes,
model configurations and hashes from the registry. Use one recorder at a
time for a history folder; automatic writers must use the new tool's shared
lock. Do not run a legacy recorder concurrently with it or hand-edit a
registered JSON history. Do not bypass integrity, shorter/older source,
unsupported content, size or transaction-recovery checks. Surface a failed
capture and leave its prior verified record intact whenever possible.

Archive completed public user and assistant text, including visible
commentary. Exclude private instructions, internal reasoning, tool traffic,
subagent correspondence and binary runtime data. Keep raw session exports
outside the repository. Source capture preserves provenance and does not
validate mathematical claims.

If a native hook needs one-time platform review and trust, explain the
requirement and point to the concrete hook definition. Never bypass hook
trust or overwrite an existing notification integration. Standing
instructions and bounded follow-ups provide the explicit tool workflow;
do not claim that a native hook is active until that activation is verified.
