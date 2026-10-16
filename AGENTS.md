# Shifted zeta positivity project instructions

Follow the investigation's instructions and `LARGE_FILES.md`. Save incremental
research in its `notes/`, computations and small execution records in
`numerics/`, and assessments in `reviews/`. Include dates, the intended
author, LLM assistance, and the actual recorded model and effort when
available; do not infer unavailable settings. Manuscripts name Edward Baker
or state they were drafted for him and acknowledge LLM assistance. Maintain
concise milestone entries in the investigation's `DRAFT_HISTORY.md`; create
no new manuscript snapshot folders.

## Read first: established results and patterns to avoid

Before opening a new direction or continuing one, read
[`result-summaries/README.md`](result-summaries/README.md) (short summaries
of what the repository has established, in the sources' own status words,
routing to the files that hold them) and
[`avoid/README.md`](avoid/README.md) (recurring patterns that have cost this
project retractions and wasted work, each with evidence). Cite both in
research overviews and continuation notes, and point at the specific
cluster or pattern file rather than restating it.

Before writing up a proposed criterion, estimate or mechanism: classify it
as in [`avoid/01`](avoid/01_restating_the_target.md) (an RH-equivalent
reformulation is stated once and not supported by checks; a milestone is
judged by its number); run the collision controls listed in
[`result-summaries/12`](result-summaries/12_collision_controls_and_screening.md)
and name the premise each control fails, as in
[`avoid/02`](avoid/02_shape_only_arguments_and_the_controls.md); and state
every negative result with the class it was proved for, as in
[`avoid/07`](avoid/07_scoped_exclusions_read_as_universal.md).

When an investigation closes or a manuscript reaches a milestone, add or
amend the `result-summaries/` entry for what it established and an `avoid/`
entry for what it learned, with a path and a quotation; keep the source's
status words, never upgrade them, and mark superseded entries instead of
deleting them. Keep both folders short; detail belongs in the sources.

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
