# Desktop chat-history compatibility diagnosis

7 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Author-selected Sol6.1/ultra; code
helpers explicitly dispatched as gpt-6.1-sol/ultra. Root exact backend and
effort were not independently exposed.

## What failed

Repository writing works. The E02 research files were saved successfully.
Automatic capture failed while looking for the source of environment
thread **01a1b947-0215-7566-a1a4-34f4a8d8d0e5**, before an archive could be
registered. No source transcript, actual title or exact turn id was
fabricated.

The pre-repair recorder searched only exact-ID legacy JSONL files under
`$CODEX_HOME/sessions`, or `~/.codex/sessions`. It had no paginated-history
adapter. Missing-source discovery raised an immediate error, so even the
configured five- or sixty-second wait did not wait for a source file to
appear. Deferred capture also resolved the source before creating its
worker.

## What changed in the installed client

The installed app is **26.1103.41825**, with bundled CLI
**0.167.0-alpha.3.2**. Read-only inspection of installed code, generated
protocol definitions and CLI help establishes:

| Contract | Verified installed behavior | Recorder consequence |
| --- | --- | --- |
| Local history mode | Thread metadata permits legacy or paginated, with a nullable legacy path | JSONL-only discovery is incomplete |
| Local paginated store | thread_history_1.sqlite contains turn and item tables | An exact read-only database adapter is needed |
| Hook transcript path | Stop and SessionStart schemas permit a null transcript_path | A null path is valid; it cannot be assumed to name a JSONL |
| Stop identity | Stop still supplies exact session_id and turn_id | Keep exact-turn final/completion gates |
| Hook feature | The bundled CLI still reports hooks enabled | The feature was not simply removed |
| Conversation and execution placement | The app has separate local and durable conversation-host paths with attached execution environments | Local file-writing ability does not prove local transcript storage |

The existing branch conversation
`01a1b91b-2fc3-7da3-aad7-18c2890c8cac` is marked **paginated** and has
public message records in the new database. Its stored schema was
inspected to fix the adapter, without printing or exporting unrelated
conversation contents.

These observations establish a compatibility gap. They do **not** prove
that this current conversation moved to a cloud host, or that its Stop
hook ran. An update date alone is not a causal test of those claims.

## Current conversation availability

For the exact current thread, inspection found:

- no matching source in local active or archived session files;
- no entry in the local state_5.sqlite thread metadata;
- no turn or item rows in thread_history_1.sqlite;
- no matching current thread in the local desktop catalog/timeline;
- failures from the app's supported thread-reading and listing tools,
  including the explicit durable-host attempt.

The app-tools socket exists. The configured repository and mirror hook
definitions and trust entries remain present. Local logs show the hook
listing facility working for the local app server, but provide no verified
current-turn hook execution. This separates a source-access problem from
repository permissions and from an unproved hook-trust diagnosis.

The missing exact source remains an app/runtime-side limitation. A safe
recorder cannot recreate its original metadata from a partial Markdown
record or substitute another chat's history.

## Repair and evidence

The repair adds bounded waiting for an absent source, allows a deferred
worker to discover the source after launch, and adds explicit read-only
diagnostics. It also adds a read-only adapter for the verified local
paginated-history schema while retaining legacy support. Exact source
identity, public-message prefix, timestamps, phases, final-turn completion,
attachment refusal, size limits, archive hashes, locking and transaction
recovery remain required.

Default selection follows the exact thread's declared history mode. An
old JSONL file retained after migration must not override newer paginated
history or make a capture silently appear unchanged. Explicit rollout
selection remains an intentional exact-source override. Database reads
use guarded read-only transactions; the approximately 927 MB history
store is not copied or exported for each capture.

The two hook definitions, stored trust hashes, app files, local databases
and computer-use notification integration are not changed. No new trust
exception or background research automation is installed. A null
transcript path is handled through actual local source discovery, not
through the hook's last_assistant_message.

The accompanying [repair receipt](../papers/investigations-5/08_theta_observables_newman_dynamics/03_operator_imaginary_time_evolution/01_green_potential_resolvent/research-progress/handoffs/07_TND_OG_CHAT_CAPTURE_COMPATIBILITY_20261107.json)
records the actual test and dry-run results and the remaining current-chat
capture status. Passing synthetic fixtures or an older local-source
crosscheck is not represented as successful capture of this conversation.

Earlier research manifests keep their original tooling/documentation
hashes. This author-requested repair supersedes those tooling versions;
it does not rewrite the issued manifests or change the mathematical
inputs/results. Future research should consult the repair receipt for
these deliberate tooling changes.

## Completed validation

The final recorder suite passed **64 tests** (44 existing and 20 added),
and the paginated-source suite passed **24 tests**. An additional read-only
live comparison selected the declared paginated source for the existing
branch chat and matched all **eight** archived public-message signatures
and the original creation timestamp exactly. Its recorded turn metadata
also merged without changing prior nonnull values. The genuine final item
and completed turn were both present. No real archive was rewritten by
this comparison.

The source-reader fixtures cover incomplete public-message gaps, changed
source snapshots, main/WAL/SHM preservation, unsupported public structures,
attachments and unknown phases. Recorder regressions cover late source
creation, bounded timeout, delayed deferred capture, null hook transcript
paths, source-mode precedence over stale JSONL, exact timestamp conflicts,
and preserved original archive provenance. An additional read-only code
review found no unresolved blocking issue. These checks do not establish
that the current Work conversation invoked a native hook.

The repaired diagnostic still reports this current thread as unregistered
with source_unavailable. Full current-chat recovery is therefore **not
complete**. The existing registered history remains intact.

## Continuation

Use the repaired diagnostic to distinguish a supported local source from
an absent one. If the client exposes the real source later, register the
current chat once at its existing investigation destination, using the
actual title, creation metadata and exact source. Then arm the bounded
exact-turn final capture. Preserve the old branch registration and
unregistered partial records.

If the source remains unavailable, use a supported app export/read path
or resume research in a verified local Codex session. Do not migrate
databases, restart active work, modify hook trust or reconstruct an
authoritative transcript from manually copied prose merely to make a
capture appear successful.
