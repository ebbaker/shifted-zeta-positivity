# Status-only assistant metadata: chat archive repair

16 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance, recorded authoring configuration
**gpt-6-astra / max**. A read-only code reviewer was explicitly dispatched
**gpt-6.1-sol / ultra**; separate backend attestation was unavailable.
This records an author-requested repair, not a change to hook trust or
permission to discard unsupported public material.

## Cause and verified scope

The registered conversation **Explore induction strategies**, thread
`01a1e2cb-4214-7010-9664-8b2a13fe0a34`, stopped refreshing after five
public messages. Its canonical paginated source remained available.
Four completed assistant finals had the exact metadata
`{"moderated": true, "display": null}`. The adapter recognized the
otherwise identical false/null form but rejected true/null as potentially
structured display content. The complete mathematical replies were still
present in the source; they had not been lost.

Two read-only checks established this particular form's public-text scope:

- The installed app, version **26.1111.21308**, build **27194**, bundles
  CLI **0.169.0-alpha.11.1**. Its generated app-server schema defines
  `AgentMessageModeration` with a Boolean `moderated` field and a nullable
  `AgentMessageDisplay` payload. The generated schema was kept outside
  the repository, with identity recorded in the linked receipt.
- The supported app `read_thread` operation returned the complete public
  text of all four affected finals, with pagination exhausted and no text
  truncation. Each message ID and full text matched its canonical database
  record exactly. Only public final text was saved for comparison outside
  the repository; private/tool payloads were not exported.

These observations support the explicit no-display case. They do not
authorize treating a non-null display instruction as ordinary text or
guessing the meaning of unknown fields.

## Change and validation

[The adapter](paginated_chat_source.py) now accepts an exact two-key
moderation object with an actual Boolean and explicit null display.
Missing/extra keys, numeric or string substitutes for the Boolean, and
every non-null display remain rejected. The existing null-metadata form
is unchanged. Structured questions, citations, delivery data, unknown
public structures and unsupported attachments still require a preserving
exporter.

The normalized text still passes the unchanged refresh tool's identity,
phase, completion, timestamp, earlier-message prefix, hash, file-size,
shared-lock and transaction-recovery checks. No source database, registered
JSON file, hook definition, trust record or legacy-source override was
edited by hand.

The recorder suites passed **93 tests**, including regression coverage
for both Boolean flags, rejection of display replacements, private-content
exclusion and an unfinished final. A separate read-only internal code
review found no substantive issue within this narrow change. This is
LLM code review, not independent specialist assurance.

The normal recorder then recovered all four missing finals and the rest
of the completed public conversation. Original creation/first-capture
times, number, filename, title and earlier public messages were preserved.
The branch's other conversation was not modified. A real prior completed
turn also passed the exact-turn capture path. The current turn's unsent
final is handled only after it is recorded, through the prescribed bounded
follow-up; no future capture is claimed here.

The [repair and planning receipt](../papers/investigations-6/03_volterra_coefficient_dynamics/numerics/06_VCD_ARCHIVE_AND_MIDPOINT_UPDATE_20261116.json)
records before/after identities, public-text comparisons, tests and limits.
Live capture times, counts and hashes belong to the
[branch registry](../papers/investigations-6/03_volterra_coefficient_dynamics/chat-histories/index.json).
This repair addresses the observed format and restores this conversation;
it does not claim support for every structured or multimodal conversation.
