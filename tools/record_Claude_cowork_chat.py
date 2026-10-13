#!/usr/bin/env python3
"""Record a Claude Cowork conversation in one of the repository's chat histories.

Prepared for Edward Baker with LLM assistance. Model: Claude Opus 5.5
(configured identifier claude-opus-5-5), Claude Cowork, 12 October 2026.
Revised 13 October 2026 (same model, reasoning effort max): moved to tools/;
`locate` and `capture` let a session refresh its own record at the end of
every turn through files staged to and from the cloud workspace; a refresh
merges into the registered record; a spool keeps the transcript's records
when a context compaction rewrites the transcript; continuation summaries are
skipped.

The chat registries are written by `record_chat.py`
(papers/investigations-2/record_chat.py, and an older copy in
papers/quasi-rh-exponent-descent/chat-histories/). That recorder captures
Codex sessions directly and imports ChatGPT-style JSON with --import-json.
This script supplies the Cowork side:

  spool        Add the transcript's new records to the session's spool and
               print the session id.
  session-id   Print the session id of the newest transcript (the
               conversation id of its record).
  locate       On the computer: find the registry that already holds a
               session, or inspect a chosen one, and list what to stage.
  capture      In the cloud workspace: convert the session, merge it into its
               staged record and import it into a staged copy of the registry;
               write the changed files for committing back. Nothing passes
               through the chat.
  convert      Claude Agent SDK transcript (JSONL) -> one ChatGPT-style
               conversation JSON, under the coverage rules below.
  register     Import a converted conversation with a chosen record_chat.py
               (base64 or gzip+base64 input, for transfer through the chat).
  record       convert + register, when the transcript and the repository are
               on the same machine (for example Claude Code run locally).
  readme-stub  Print a draft registry README entry for a registered chat.

Coverage, as in the earlier Cowork captures. Kept:
  - messages typed by the person, including messages sent while a reply was
    in progress and interruption markers the person triggered;
  - the assistant's text shown in the chat: progress lines between tool calls
    (phase commentary) and the reply ending each completed turn (phase
    final_answer);
  - chat-visible items that travel through tools, rendered as text and
    labelled in message metadata: question cards (AskUserQuestion) with the
    options the person selected, notes sent with SendUserMessage, and file-card
    captions (SendUserFile).
Omitted: system, developer and harness instructions (<system-reminder> blocks
included), the continuation summaries that resume a compacted session,
internal reasoning, other tool calls and outputs, permission prompts, subagent
records, attachments and runtime state. The raw transcript is never copied
into the repository; archive_metadata records its SHA-256.

Compaction and the spool. A context compaction can rewrite the transcript so
that it begins at the compaction, and the records written since the last read
are then gone from it. So every command that reads a transcript first adds its
new records to a spool (default ~/.cache/cowork-chat-spool/SESSION.jsonl, on
the machine that holds the transcript, never in the repository) and converts
the spool; and capture, register and record merge the conversion into the
chat's registered record, keeping the messages the spool no longer covers, so
a refresh never shortens the record. A window that no read covered is listed
in archive_metadata.gaps, and the turns it cuts are marked (end_in_gap,
start_in_gap, gap_inside). Running `spool` at the start of every turn narrows
such a window to the part of one turn before a compaction. The session's event
log on claude.ai stays complete; tools/record_Claude_export_chat.py reads it.

Per-turn Cowork procedure. The transcript lives in the cloud workspace and the
repository on the person's computer; the registry's files make the round trip
with the device tools. STAGED is the staged repository root,
/mnt/user-data/uploads/REPO.

  1. Start of the turn, cloud workspace (once the script has been staged):
       python3 STAGED/tools/record_Claude_cowork_chat.py spool
     It prints the session id.
  2. End of the turn, on the computer, from the repository root:
       python3 tools/record_Claude_cowork_chat.py locate --conversation-id ID \\
           [--registry PATH]
     It prints the registry that already holds the session (for a first
     capture, give the registry: the project's chat-histories/claude-cowork,
     or the portfolio's), the files to stage (this script and record_chat.py
     among them) and the numbered file names the capture must reserve.
  3. Stage the listed files (device_stage_files), keeping each one's mtimeMs.
  4. Cloud workspace:
       python3 STAGED/tools/record_Claude_cowork_chat.py capture --registry PATH \\
           [--reserve NAME ...] [--delivered PATH ...] [--new-registry]
     It converts the spool, merges the result into the staged record, imports
     it into a scratch copy of the staged registry with the staged
     record_chat.py, and writes the changed files under
     /mnt/user-data/outputs/chat-capture/, printing for each the path to commit
     to. Pass --delivered for the files the session wrote with shell commands
     (files committed with the device tools and project documents are
     detected); --new-registry is for a registry without index.json.
  5. Write those files back with device_commit_files, passing expectedMtimeMs
     from step 3 for the files that already existed.
  6. First capture only: add the printed README entry, with its Work sentence
     written, to the registry's README.

A capture made during a turn holds everything up to that point; the reply
being written enters with the next refresh. Repeating the steps refreshes the
same chat number, since the conversation id is the session id. record_chat.py
refuses a shorter or older refresh unless --allow-shorter-refresh is given.

Alternative transfer through the chat (convert, then register on the computer
with the printed base64, optionally gzipped with --gzip):
       python3 STAGED/tools/record_Claude_cowork_chat.py convert --output conv.json \\
           --b64-output conv.b64 [--gzip]
       python3 tools/record_Claude_cowork_chat.py register --input-b64 - \\
           --expect-sha256 HEX [--project NAME | --folder PATH] <<'EOF'
       ...base64...
       EOF
The default recorder and registry are those of papers/investigations-2; use
--recorder and --folder for another registry.

Standard library only (Python 3.9+).
"""
from __future__ import annotations

import argparse
import base64
import glob
import gzip
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo


def find_root(start):
    """The repository root: the nearest folder holding papers/ beside tools/ or .git.

    Works for the script in tools/ of a clone, and for a staged copy whose
    papers/investigations-2/record_chat.py was staged with it.
    """
    for folder in (start, *start.parents):
        if (folder / "papers").is_dir() and ((folder / "tools").is_dir() or (folder / ".git").exists()):
            return folder
    return start.parent if start.name == "tools" else start


ROOT = find_root(Path(__file__).resolve().parent)
BASE = ROOT / "papers" / "investigations-2"
DEFAULT_RECORDER = BASE / "record_chat.py"
SCRIPTS = ("tools/record_Claude_cowork_chat.py", "papers/investigations-2/record_chat.py")
DEFAULT_SPOOL_DIR = "~/.cache/cowork-chat-spool"
DEFAULT_OUT_DIR = "/mnt/user-data/outputs/chat-capture"
UTC = timezone.utc
LOCAL = ZoneInfo("America/New_York")
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
PROJECT_NOTE = re.compile(r'attached to the Project \*\*"([^"*]+)"\*\*')
SKIP_PREFIXES = ("<system-reminder>", "<command-name>", "<command-message>",
                 "<command-args>", "<local-command")
INTERRUPTED = "[Request interrupted by user"
STOP_SUBTYPES = {"stop_hook_summary", "turn_duration"}
SOURCE = "Claude Cowork completed public message"
RENDERING = {
    "AskUserQuestion": "header, question and options of the card, as text",
    "answer": "the option the person selected in the question card",
    "SendUserMessage": "verbatim message shown to the person between tool calls",
    "SendUserFile": "caption of a file card shown to the person",
}
COVERAGE = (
    "Messages typed by the person (including any sent while a reply was in progress, and "
    "interruption markers the person triggered) and the options the person selected in question "
    "cards; the assistant text shown in the chat: progress lines between tool calls, question "
    "cards rendered as text, notes and file-card captions sent through tools (phase commentary), "
    "and the reply ending each completed turn (phase final_answer); recorded through capture. "
    "A reply still in progress at capture enters only on a refresh")
OMITTED = [
    "system, developer and harness instructions (including <system-reminder> blocks)",
    "the continuation summaries that resume a compacted session",
    "internal reasoning",
    "tool calls and outputs, except the chat-visible items named in coverage",
    "permission and folder-access prompts",
    "subagent messages",
    "attachments and runtime state",
]
TRANSCRIPT_NOTE = ("The transcript is not stored in the repository; it contains instructions, reasoning "
                   "and tool traffic that the coverage rules exclude")
SPOOL_NOTE = ("Every transcript record read so far for this session, kept outside the repository so "
              "that a transcript rewritten at a compaction loses nothing already read; the conversion "
              "reads the spool")
GAP_CAUSE = ("A context compaction rewrote the transcript to begin at the compaction; records written "
             "in this window had not been read by any capture, so their messages are missing")
WINDOW_CAUSE = ("The records of this window were read by no capture: the earlier read ends before the "
                "first record of the later one")


# ---------------------------------------------------------------- utilities

def epoch(stamp):
    return datetime.fromisoformat(stamp.replace("Z", "+00:00")).timestamp()


def iso(value):
    return datetime.fromtimestamp(value, UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def local(value):
    return datetime.fromtimestamp(value, LOCAL).isoformat(timespec="milliseconds")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def blocks(record):
    content = record.get("message", {}).get("content")
    return content if isinstance(content, list) else []


def stamp_of(row):
    return epoch(row["timestamp"]) if row.get("timestamp") else None


def note(message):
    print(message, file=sys.stderr)


def dump(conversation):
    return (json.dumps(conversation, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


# ------------------------------------------------------- transcript and spool

def find_transcript(projects_dir):
    pattern = str(Path(projects_dir).expanduser() / "*" / "*.jsonl")
    candidates = [Path(path) for path in glob.glob(pattern)]
    if not candidates:
        sys.exit("No transcript found under %s; pass --transcript" % projects_dir)
    return max(candidates, key=lambda path: path.stat().st_mtime)


def read_lines(path):
    """The complete JSON lines of a transcript or spool; a partly written last line is left out."""
    raw = Path(path).read_bytes()
    complete = raw[:raw.rfind(b"\n") + 1] if b"\n" in raw else raw
    return complete, [line for line in complete.split(b"\n") if line.strip()]


def row_key(row, line):
    return "uuid:" + row["uuid"] if row.get("uuid") else "line:" + sha256(line)


def describe(data, rows, sizes=("records_read", "bytes_read", "sha256_of_bytes_read")):
    stamps = [stamp_of(r) for r in rows if r.get("uuid") and r.get("timestamp")]
    return {sizes[0]: len(rows), sizes[1]: len(data), sizes[2]: sha256(data),
            "first_record_utc": iso(min(stamps)) if stamps else None,
            "last_record_utc": iso(max(stamps)) if stamps else None}


def update_spool(spool_file, sources):
    """Append to the spool every record of the sources that it lacks; return the number added."""
    seen = set()
    if spool_file.exists():
        complete, lines = read_lines(spool_file)
        if len(complete) != spool_file.stat().st_size:
            spool_file.write_bytes(complete)
        seen = {row_key(json.loads(line), line) for line in lines}
    added = []
    for source in sources:
        for line in read_lines(source)[1]:
            key = row_key(json.loads(line), line)
            if key not in seen:
                seen.add(key)
                added.append(line)
    if added:
        spool_file.parent.mkdir(parents=True, exist_ok=True)
        with spool_file.open("ab") as handle:
            handle.write(b"".join(line + b"\n" for line in added))
    return len(added)


def load_session(args):
    """Read the transcript, add its new records to the spool, and return (rows, provenance)."""
    transcript = Path(args.transcript).expanduser() if args.transcript else find_transcript(args.projects_dir)
    data, lines = read_lines(transcript)
    live = [json.loads(line) for line in lines]
    session_id = next((r["sessionId"] for r in live if r.get("sessionId")), transcript.stem)
    provenance = {"session_id": session_id, "live": live,
                  "source_transcript": dict(describe(data, live), note=TRANSCRIPT_NOTE)}
    if args.no_spool:
        if args.spool_from:
            raise SystemExit("--spool-from needs the spool; drop --no-spool")
        note("transcript: %s (%d records); no spool" % (transcript, len(live)))
        return live, provenance
    spool_file = Path(args.spool_dir).expanduser() / ("%s.jsonl" % session_id)
    added = update_spool(spool_file, [Path(p).expanduser() for p in args.spool_from or []] + [transcript])
    spool_data, spool_lines = read_lines(spool_file)
    rows = [json.loads(line) for line in spool_lines]
    provenance["spool"] = dict(describe(spool_data, rows, ("records", "bytes", "sha256")), note=SPOOL_NOTE)
    provenance["spool_file"] = str(spool_file)
    provenance["spool_added"] = added
    note("transcript: %s (%d records); spool: %s (%d records, %d added now)"
         % (transcript, len(live), spool_file, len(rows), added))
    return rows, provenance


# --------------------------------------------------------------- conversion

def typed_text(record):
    """Text the person typed in a user record, or None for anything else."""
    content = record.get("message", {}).get("content")
    attachments = []
    if isinstance(content, str):
        text = content
    elif isinstance(content, list):
        if any(block.get("type") == "tool_result" for block in content):
            return None
        text = "\n\n".join(block.get("text", "") for block in content if block.get("type") == "text")
        attachments = [block.get("type") for block in content
                       if block.get("type") not in ("text", "tool_result")]
    else:
        return None
    if text.lstrip().startswith(SKIP_PREFIXES):
        return None
    if REMINDER.search(text):
        text = REMINDER.sub("", text).strip()
    if not text.strip() and not attachments:
        return None
    return text, attachments


def question_text(questions):
    lines = []
    for question in questions:
        lines.append("%s: %s" % (question.get("header", ""), question.get("question", "")))
        for option in question.get("options", []):
            lines.append("- %s — %s" % (option.get("label", ""), option.get("description", "")))
    return "\n".join(lines)


def answer_text(result):
    answers = result.get("answers") or {}
    if not answers:
        return None
    annotations = result.get("annotations") or {}
    lines = []
    for question, answer in answers.items():
        header = next((q.get("header") for q in result.get("questions", [])
                       if q.get("question") == question), None)
        line = answer if len(answers) == 1 else "%s: %s" % (header or question, answer)
        notes = (annotations.get(question) or {}).get("notes")
        if notes:
            line += "\n(note: %s)" % notes
        lines.append(line)
    return "\n".join(lines)


def repo_relative(path, repo_name):
    marker = "/%s/" % repo_name
    return path.split(marker, 1)[1] if marker in path else path


def tool_result_payload(record):
    result = record.get("toolUseResult")
    if isinstance(result, dict):
        return result
    for block in blocks(record):
        if block.get("type") == "tool_result":
            content = block.get("content")
            if isinstance(content, list):
                content = "".join(part.get("text", "") for part in content if isinstance(part, dict))
            try:
                payload = json.loads(content) if isinstance(content, str) else None
            except ValueError:
                payload = None
            if isinstance(payload, dict):
                return payload
    return {}


def is_compaction_summary(row):
    """The user-role record the harness writes to resume a compacted session."""
    return row.get("type") == "user" and bool(row.get("isCompactSummary"))


def is_registry_file(path):
    """A chat record or registry index: written by the capture itself, not a deliverable."""
    return bool(re.search(r"(^|/)chat-histories/(.*/)?[^/]+\.json$", path))


def transcript_gaps(rows):
    """Compactions, and the windows lost where a compaction rewrote the transcript.

    A rewritten transcript begins at a compact_boundary record whose logical
    parent (the last record before the compaction) is no longer present. The
    window runs from the latest earlier record still held (None if there is
    none) to the boundary; resume_key is the prompt id carried by the
    continuation summary, that of the turn then in progress.
    """
    uuids = {row["uuid"] for row in rows if row.get("uuid")}
    by_uuid = {row["uuid"]: row for row in rows if row.get("uuid")}
    children = {}
    for row in rows:
        if row.get("uuid") and row.get("parentUuid"):
            children.setdefault(row["parentUuid"], []).append(row["uuid"])
    boundaries = [row for row in rows if row.get("type") == "system"
                  and row.get("subtype") == "compact_boundary" and row.get("timestamp")]
    gaps = []
    for boundary in boundaries:
        parent = boundary.get("logicalParentUuid")
        if not parent or parent in uuids or not boundary.get("uuid"):
            continue
        chain, stack = set(), [boundary["uuid"]]
        while stack:
            ident = stack.pop()
            if ident not in chain:
                chain.add(ident)
                stack.extend(children.get(ident, []))
        moment = stamp_of(boundary)
        earlier = [stamp_of(row) for row in rows if row.get("uuid") and row.get("timestamp")
                   and row["uuid"] not in chain and stamp_of(row) < moment]
        resumed = [stamp_of(by_uuid[ident]) for ident in chain if by_uuid[ident].get("timestamp")]
        summary = next((row for row in rows if is_compaction_summary(row)
                        and row.get("parentUuid") == boundary["uuid"]), None)
        gaps.append({"after": max(earlier) if earlier else None, "before": moment,
                     "resume_at": min(resumed + [moment]),
                     "resume_key": summary.get("promptId") if summary else None})
    compaction = {"boundaries_utc": [iso(stamp_of(row)) for row in boundaries],
                  "transcript_rewritten_at_utc": [iso(gap["before"]) for gap in gaps]}
    return compaction, gaps


def convert(rows, provenance, options):
    rows = [row for row in rows if not row.get("isSidechain")]
    compaction, gaps = transcript_gaps(rows)
    rows = [row for row in rows if not is_compaction_summary(row)]
    used_ids = set()

    def claim(preferred, fallback):
        ident = preferred if preferred not in used_ids else fallback
        used_ids.add(ident)
        return ident

    tools = {}
    for row in rows:
        if row.get("type") == "assistant":
            for block in blocks(row):
                if block.get("type") == "tool_use":
                    tools[block["id"]] = (block.get("name"), block.get("input") or {})
    queue = [row for row in rows if row.get("type") == "queue-operation"]

    events = []
    delivered = []
    for row in rows:
        kind = row.get("type")
        if kind == "user":
            for block in blocks(row):
                if block.get("type") != "tool_result":
                    continue
                name, tool_input = tools.get(block.get("tool_use_id"), (None, {}))
                result = row.get("toolUseResult") if isinstance(row.get("toolUseResult"), dict) else {}
                if name == "AskUserQuestion":
                    text = answer_text(result)
                    if text:
                        events.append({"t": epoch(row["timestamp"]), "role": "user",
                                       "id": claim(row["uuid"], block.get("tool_use_id")),
                                       "text": text, "kind": "answer",
                                       "extra": {"rendered_from_tool": "AskUserQuestion",
                                                 "rendering": RENDERING["answer"]}})
                elif name and name.endswith("device_commit_files"):
                    payload = tool_result_payload(row)
                    for path in payload.get("written", []) or []:
                        delivered.append(repo_relative(path, options["repo_name"]))
                elif name == "Projects" and tool_input.get("method") == "project_write":
                    delivered.append("claude.ai project document %s" % tool_input.get("path"))
            parsed = None if row.get("isMeta") else typed_text(row)
            if parsed is None:
                continue
            text, attachments = parsed
            events.append({"t": epoch(row["timestamp"]), "role": "user",
                           "id": claim(row["uuid"], row["uuid"] + "-prompt"),
                           "text": text,
                           "kind": "interrupt" if text.startswith(INTERRUPTED) else "prompt",
                           "prompt_id": row.get("promptId"),
                           "extra": {"attachments": attachments} if attachments else {}})
        elif kind == "assistant":
            stamp = epoch(row["timestamp"])
            for number, block in enumerate(blocks(row)):
                if block.get("type") == "text" and block.get("text", "").strip():
                    events.append({"t": stamp, "role": "assistant",
                                   "id": claim(row["uuid"], "%s-%d" % (row["uuid"], number)),
                                   "text": block["text"], "kind": "text", "extra": {}})
                elif block.get("type") == "tool_use":
                    name, tool_input = block.get("name"), block.get("input") or {}
                    if name == "SendUserMessage" and tool_input.get("message"):
                        text = tool_input["message"]
                    elif name == "AskUserQuestion" and tool_input.get("questions"):
                        text = question_text(tool_input["questions"])
                    elif name == "SendUserFile" and tool_input.get("caption"):
                        text = tool_input["caption"]
                    else:
                        continue
                    extra = {"rendered_from_tool": name, "rendering": RENDERING[name]}
                    if name == "SendUserFile":
                        extra["files"] = [Path(f).name for f in tool_input.get("files", [])]
                    events.append({"t": stamp, "role": "assistant",
                                   "id": claim(row["uuid"], block.get("id")),
                                   "text": text, "kind": "tool", "extra": extra})
        elif kind == "attachment":
            attachment = row.get("attachment") or {}
            if attachment.get("type") != "queued_command":
                continue
            prompt = attachment.get("prompt")
            if not isinstance(prompt, str) or prompt.lstrip().startswith(SKIP_PREFIXES):
                continue
            if (attachment.get("origin") or {}).get("kind", "human") != "human":
                continue
            stamp = epoch(row["timestamp"])
            queued = [epoch(q["timestamp"]) for q in queue
                      if q.get("operation") == "enqueue" and q.get("content") == prompt
                      and epoch(q["timestamp"]) <= stamp + 1]
            removed = [epoch(q["timestamp"]) for q in queue
                       if q.get("operation") in ("remove", "dequeue") and q.get("content") == prompt
                       and epoch(q["timestamp"]) >= stamp - 1]
            events.append({"t": max(queued) if queued else stamp, "role": "user",
                           "id": claim(attachment.get("source_uuid") or row["uuid"], row["uuid"]),
                           "text": prompt,
                           "kind": "queued",
                           "extra": {"sent_while_reply_in_progress": True,
                                     "delivered_to_session_at_utc": iso(min(removed) if removed else stamp)}})

    prompts = [e for e in events if e["kind"] == "prompt"]
    events = [e for e in events if not (e["kind"] == "queued" and any(
        p["text"] == e["text"] and 0 <= p["t"] - e["t"] <= 300 for p in prompts))]
    events.sort(key=lambda e: e["t"])
    if not events and not options.get("allow_empty"):
        raise SystemExit("No public message found in the transcript")

    # Turns: each typed prompt opens one, and so does the first record after a
    # rewrite whose turn's prompt was lost; everything until the next belongs to it.
    segments = [{"start": e["t"], "key": e.get("prompt_id") or e["id"], "gap": None}
                for e in events if e["kind"] == "prompt"]
    for gap in gaps:
        if gap["resume_key"] and gap["resume_key"] not in {s["key"] for s in segments}:
            segments.append({"start": gap["resume_at"], "key": gap["resume_key"], "gap": gap})
    segments.sort(key=lambda s: s["start"])
    stops = sorted(epoch(r["timestamp"]) for r in rows
                   if r.get("type") == "system" and r.get("subtype") in STOP_SUBTYPES and r.get("timestamp"))
    assistant_times = sorted(epoch(r["timestamp"]) for r in rows
                             if r.get("type") == "assistant" and r.get("timestamp"))
    skipped_prompt_ids = {r.get("promptId") for r in rows if r.get("type") == "user"
                          and r.get("promptId") and isinstance(r.get("message", {}).get("content"), str)
                          and r["message"]["content"].lstrip().startswith(SKIP_PREFIXES)}

    turns = {}
    for index, segment in enumerate(segments):
        start, key = segment["start"], segment["key"]
        following = segments[index + 1] if index + 1 < len(segments) else None
        end = following["start"] if following else float("inf")
        cut = following is not None and following["gap"] is not None
        members = [e for e in events if start <= e["t"] < end]
        for e in members:
            e["turn"] = key
        interrupt = next((e for e in members if e["kind"] == "interrupt"), None)
        last_assistant = max((t for t in assistant_times if start <= t < end), default=start)
        stop = [t for t in stops if last_assistant <= t < end]
        texts = [e for e in members if e["role"] == "assistant" and e["kind"] == "text"]
        record = ({"start_in_gap": True, "recorded_from": iso(start)} if segment["gap"]
                  else {"started_at": iso(start)})
        if interrupt:
            record = {"status": "interrupted", **record, "interrupted_at": iso(interrupt["t"])}
        elif cut:
            record = {"status": "ended", **record, "end_in_gap": True}
        elif stop or end != float("inf"):
            final = texts[-1] if texts else None
            if final:
                final["phase"] = "final_answer"
            done = final["t"] if final else (stop[0] if stop else last_assistant)
            record = {"status": "completed", **record, "completed_at": iso(done)}
        else:
            record = {"status": "in_progress", **record}
        if any(g["after"] is not None and start <= g["after"] < end
               and not (cut and g is following["gap"]) for g in gaps):
            record["gap_inside"] = True
        asks = [e for e in members if e["extra"].get("rendered_from_tool") == "AskUserQuestion"
                and e["role"] == "assistant"]
        if asks:
            record["awaited_answer_from"] = iso(asks[0]["t"])
            answers = [e for e in members if e["kind"] == "answer" and e["t"] >= asks[0]["t"]]
            if answers:
                record["resumed_at"] = iso(answers[0]["t"])
        continued = sorted({r.get("promptId") for r in rows if r.get("type") == "user"
                            and r.get("promptId") and r.get("timestamp")
                            and start <= epoch(r["timestamp"]) < end}
                           - {key} - skipped_prompt_ids)
        if continued:
            record["continued_under_prompt_ids"] = continued
        turns[key] = record
    events = [e for e in events if "turn" in e]

    messages = []
    for e in events:
        phase = e.get("phase") or ("commentary" if e["role"] == "assistant" else None)
        metadata = {"source": SOURCE, "source_turn_id": e["turn"], "phase": phase,
                    "created_at_utc": iso(e["t"]), "completed_at_utc": iso(e["t"]),
                    "created_at_local": local(e["t"])}
        metadata.update(e["extra"])
        messages.append({
            "id": e["id"],
            "author": {"role": e["role"], "name": None, "metadata": {}},
            "create_time": e["t"],
            "update_time": e["t"],
            "content": {"content_type": "text", "parts": [e["text"]]},
            "status": "finished_successfully",
            "end_turn": (phase == "final_answer") if e["role"] == "assistant" else None,
            "metadata": metadata,
            "recipient": "all",
        })
    mapping, current = build_mapping(messages)

    session_id = next(r["sessionId"] for r in rows if r.get("sessionId"))
    live = provenance.get("live") or rows
    titles = [r.get("aiTitle") for r in live if r.get("type") == "ai-title" and r.get("aiTitle")] or \
             [r.get("aiTitle") for r in rows if r.get("type") == "ai-title" and r.get("aiTitle")]
    stamps = [epoch(r["timestamp"]) for r in rows if r.get("timestamp")]
    attachments = [r.get("attachment") or {} for r in rows if r.get("type") == "attachment"]
    urls = [a.get("url") for a in attachments if a.get("type") == "remote_session_change" and a.get("url")]
    identity = [a.get("identity", {}).get("modelId") for a in attachments if a.get("type") == "model"]
    projects = [m.group(1) for a in attachments if a.get("type") == "session_context"
                for m in [PROJECT_NOTE.search(str((a.get("context") or {}).get("attachedProject") or ""))] if m]
    models = sorted({(r.get("message", {}).get("model"), r.get("effort")) for r in rows
                     if r.get("type") == "assistant" and r.get("message", {}).get("model")},
                    key=lambda pair: (str(pair[0]), str(pair[1])))
    session = {
        "app": "Claude Cowork (desktop app, cloud session)",
        "session_id": session_id,
        "title_source": "the session's recorded title" if not options.get("title") else "set at conversion",
        "first_event_utc": iso(min(stamps)),
        "claude_ai_session": options.get("claude_session_url") or (urls[-1] if urls else None),
        "configured_model_identifier_reported_by_harness": identity[-1] if identity else None,
        "serving_model_per_transcript": ", ".join(sorted({m for m, _ in models})),
    }
    if projects:
        session["project"] = {"name": projects[-1], "source": "the session context the harness records"}
    session.update(options.get("session_notes") or {})
    delivered = list(dict.fromkeys([path for path in delivered if not is_registry_file(path)]
                                   + list(options.get("delivered") or [])))
    script = Path(__file__).resolve()
    metadata = {
        "format": "ChatGPT-style conversation mapping; local conversion, not an official provider export",
        "source_kind": "Claude Cowork session transcript (Claude Agent SDK JSONL), completed public text messages",
        "message_timestamps": "Transcript record times, in seconds since Unix epoch and ISO 8601; the conversation create_time is the first transcript event; a message typed while a reply was in progress carries its queue time, with its delivery time in metadata",
        "coverage": COVERAGE,
        "omitted_record_types": OMITTED,
        "source_public_message_records": len(messages),
        "model_configurations": [{"model": m, "reasoning_effort": e} for m, e in models],
        "turns": turns,
        "session": session,
        "compaction": compaction,
        "gaps": [{"after_utc": iso(g["after"]) if g["after"] is not None else None,
                  "before_utc": iso(g["before"]), "cause": GAP_CAUSE} for g in gaps],
        "source_transcript": provenance["source_transcript"],
    }
    if provenance.get("spool"):
        metadata["spool"] = provenance["spool"]
    metadata["delivered_files_not_embedded"] = delivered
    metadata["converter"] = {"script": script.name, "sha256": sha256(script.read_bytes())}
    return {
        "title": options.get("title") or (titles[-1] if titles else "Cowork session %s" % session_id[:8]),
        "create_time": min(stamps),
        "update_time": messages[-1]["create_time"] if messages else None,
        "mapping": mapping,
        "current_node": current,
        "conversation_id": session_id,
        "id": session_id,
        "archive_metadata": metadata,
    }


def build_mapping(messages):
    mapping = {"root": {"id": "root", "message": None, "parent": None, "children": []}}
    parent = "root"
    for message in messages:
        mapping[message["id"]] = {"id": message["id"], "message": message, "parent": parent, "children": []}
        mapping[parent]["children"].append(message["id"])
        parent = message["id"]
    return mapping, parent


def chain_messages(conversation):
    mapping, found, node = conversation["mapping"], [], conversation["mapping"]["root"]
    while node["children"]:
        node = mapping[node["children"][-1]]
        if node.get("message"):
            found.append(node["message"])
    return found


def covered(conversation):
    """First and last transcript record behind a conversion or record (spool if one was read)."""
    meta = conversation.get("archive_metadata", {})
    read = meta.get("spool") or meta.get("source_transcript") or {}
    first, last = read.get("first_record_utc"), read.get("last_record_utc")
    return (epoch(first) if first else conversation["create_time"],
            epoch(last) if last else (conversation.get("update_time") or conversation["create_time"]))


def merge_conversations(base, new, title=None):
    """Merge a fresh conversion into the chat's registered record without losing its messages.

    The conversion is authoritative from its first record on; the record keeps
    what came before. Windows that neither covers become gaps.
    """
    if base.get("conversation_id") != new.get("conversation_id"):
        raise SystemExit("The registered record is of %s, not %s" % (base.get("conversation_id"),
                                                                     new.get("conversation_id")))
    bmeta, nmeta = base.get("archive_metadata", {}), new["archive_metadata"]
    new_from, _ = covered(new)
    _, base_to = covered(base)
    fresh = chain_messages(new)
    fresh_ids = {m["id"] for m in fresh}
    kept = [m for m in chain_messages(base) if m["id"] not in fresh_ids and m["create_time"] < new_from]
    messages = sorted(kept + fresh, key=lambda m: m["create_time"])
    kept_turns = {m["metadata"].get("source_turn_id") for m in kept}
    prompted = {m["metadata"].get("source_turn_id") for m in messages if m["author"]["role"] == "user"
                and not m["metadata"].get("rendered_from_tool")
                and not m["metadata"].get("sent_while_reply_in_progress")
                and not m["content"]["parts"][0].startswith(INTERRUPTED)}

    new_turns = nmeta.get("turns", {})
    turns = {}
    for key, record in bmeta.get("turns", {}).items():
        if key in new_turns:
            merged = dict(record)
            merged.update(new_turns[key])
            if "started_at" in record:
                merged = {"status": merged.pop("status"), "started_at": record["started_at"],
                          **{k: v for k, v in merged.items() if k not in ("start_in_gap", "recorded_from")}}
            turns[key] = merged
        elif key in kept_turns:
            turns[key] = dict(record)
            if record.get("status") == "in_progress":
                rest = {k: v for k, v in record.items() if k != "status"}
                turns[key] = {"status": "ended", **rest, "end_in_gap": True}
    for key, record in new_turns.items():
        if key not in turns:
            turns[key] = dict(record)
    for key, record in turns.items():
        if record.get("start_in_gap") and key in prompted:
            record.pop("start_in_gap")
            record.pop("recorded_from", None)

    gaps = [dict(g) for g in bmeta.get("gaps", []) if epoch(g["before_utc"]) <= new_from + 1e-3]
    for gap in nmeta.get("gaps", []):
        gap = dict(gap)
        if gap["after_utc"] is None:
            if base_to >= epoch(gap["before_utc"]):
                continue
            gap["after_utc"] = iso(base_to)
        gaps.append(gap)
    if kept and base_to < new_from - 1e-3 and not any(
            epoch(g["after_utc"]) <= base_to + 1e-3 and epoch(g["before_utc"]) >= new_from - 1.0 for g in gaps):
        gaps.append({"after_utc": iso(base_to), "before_utc": iso(new_from), "cause": WINDOW_CAUSE})
    unique = []
    for gap in sorted(gaps, key=lambda g: g["before_utc"]):
        if gap not in unique:
            unique.append(gap)

    compaction = {}
    for field in ("boundaries_utc", "transcript_rewritten_at_utc"):
        compaction[field] = sorted(set((bmeta.get("compaction") or {}).get(field, []))
                                   | set((nmeta.get("compaction") or {}).get(field, [])))
    earlier = []
    if kept:
        earlier = list(bmeta.get("earlier_reads", []))
        read = {"source_transcript": bmeta.get("source_transcript")}
        if bmeta.get("spool"):
            read["spool"] = bmeta["spool"]
        earlier.append(read)
    configurations = []
    for item in bmeta.get("model_configurations", []) + nmeta.get("model_configurations", []):
        if item not in configurations:
            configurations.append(item)
    create_time = min(base["create_time"], new["create_time"])
    session = dict(bmeta.get("session", {}))
    session.update(nmeta.get("session", {}))
    session["first_event_utc"] = iso(create_time)

    mapping, current = build_mapping(messages)
    meta = dict(nmeta)
    meta.update(source_public_message_records=len(messages), model_configurations=configurations,
                turns=turns, session=session, compaction=compaction, gaps=unique,
                delivered_files_not_embedded=list(dict.fromkeys(
                    bmeta.get("delivered_files_not_embedded", []) + nmeta.get("delivered_files_not_embedded", []))))
    if earlier:
        meta["earlier_reads"] = earlier
    merged = dict(new)
    merged.update(title=title or base.get("title") or new["title"], create_time=create_time,
                  update_time=messages[-1]["create_time"] if messages else base.get("update_time"),
                  mapping=mapping, current_node=current, archive_metadata=meta)
    return merged


# ----------------------------------------------------------------- commands

def parse_notes(pairs):
    notes = {}
    for pair in pairs or []:
        if "=" not in pair:
            raise SystemExit("--session-note expects KEY=VALUE, got %r" % pair)
        key, value = pair.split("=", 1)
        notes[key.strip()] = value.strip()
    return notes


def report(conversation):
    node = conversation["mapping"]["root"]
    while node["children"]:
        node = conversation["mapping"][node["children"][-1]]
        message = node["message"]
        preview = message["content"]["parts"][0].replace("\n", " ")[:70]
        note("  %s %-9s %-12s %s" % (message["metadata"]["created_at_utc"], message["author"]["role"],
                                     message["metadata"]["phase"] or "", preview))
    meta = conversation["archive_metadata"]
    for key, turn in meta["turns"].items():
        flags = [flag for flag in ("start_in_gap", "end_in_gap", "gap_inside") if turn.get(flag)]
        note("  turn %s: %s%s" % (key[:8], turn["status"], " (%s)" % ", ".join(flags) if flags else ""))
    for gap in meta.get("gaps", []):
        note("  gap: %s to %s" % (gap["after_utc"], gap["before_utc"]))


def converted(args, base=None):
    rows, provenance = load_session(args)
    conversation = convert(rows, provenance, {
        "title": args.title, "claude_session_url": args.claude_session_url,
        "session_notes": parse_notes(args.session_note), "delivered": args.delivered,
        "repo_name": args.repo_name, "allow_empty": base is not None,
    })
    if base is not None:
        conversation = merge_conversations(base, conversation, args.title)
    report(conversation)
    return conversation, dump(conversation), provenance


def registry_folder(args):
    if getattr(args, "folder", None):
        return Path(args.folder).expanduser()
    if getattr(args, "project", None):
        return BASE / args.project / "chat-histories"
    return BASE / "chat-histories"


def registered_record(folder, conversation_id):
    """The registry entry and record of a conversation, verified against index.json, or (None, None)."""
    index_path = Path(folder) / "index.json"
    if not conversation_id or not index_path.is_file():
        return None, None
    index = json.loads(index_path.read_text(encoding="utf-8"))
    entry = next((e for e in index.get("chats", []) if e.get("conversation_id") == conversation_id), None)
    if entry is None:
        return None, None
    path = Path(folder) / entry["file"]
    if not path.is_file():
        raise SystemExit("Chat %d is registered but %s is missing; stage it too" % (entry["number"], path))
    data = path.read_bytes()
    if sha256(data) != entry["sha256"]:
        raise SystemExit("%s does not match index.json; restage both, or inspect the record" % path)
    return entry, json.loads(data)[0]


def session_of(args):
    transcript = Path(args.transcript).expanduser() if args.transcript else find_transcript(args.projects_dir)
    for line in read_lines(transcript)[1]:
        row = json.loads(line)
        if row.get("sessionId"):
            return row["sessionId"]
    return transcript.stem


def cmd_convert(args):
    base = None
    if args.base:
        loaded = json.loads(Path(args.base).read_text(encoding="utf-8"))
        base = loaded[0] if isinstance(loaded, list) else loaded
    _, text, _ = converted(args, base)
    Path(args.output).write_bytes(text)
    if args.b64_output:
        payload = gzip.compress(text, compresslevel=9, mtime=0) if args.gzip else text
        Path(args.b64_output).write_text(base64.b64encode(payload).decode("ascii") + "\n")
    print("wrote %s  sha256 %s  (%d bytes)" % (args.output, sha256(text), len(text)))


def cmd_spool(args):
    _, provenance = load_session(args)
    print(json.dumps({"session_id": provenance["session_id"], "spool": provenance.get("spool_file"),
                      "spool_records": (provenance.get("spool") or {}).get("records"),
                      "added_now": provenance.get("spool_added"),
                      "transcript_records": provenance["source_transcript"]["records_read"]}, indent=1))


def cmd_session_id(args):
    print(session_of(args))


# ------------------------------------------------------- per-turn procedure

def history_registries(root):
    """Every chat-history registry index under root, skipping hidden folders."""
    found = []
    for folder, subfolders, files in os.walk(root):
        subfolders[:] = sorted(d for d in subfolders if not d.startswith("."))
        path = Path(folder)
        if "index.json" in files and "chat-histories" in path.relative_to(root).parts:
            found.append(path / "index.json")
    return found


def numbered_files(folder):
    return sorted(p.name for p in Path(folder).iterdir()
                  if p.is_file() and re.fullmatch(r"\d+_.*\.json", p.name)) if Path(folder).is_dir() else []


def clean_registry(value):
    registry = value.strip().strip("/")
    if not registry or Path(registry).is_absolute() or ".." in Path(registry).parts:
        raise SystemExit("--registry must be a repository-relative path, got %r" % value)
    return Path(registry).as_posix()


def cmd_locate(args):
    root = Path(args.root).resolve() if args.root else ROOT
    holders = []
    for index_path in history_registries(root):
        try:
            index = json.loads(index_path.read_text(encoding="utf-8"))
        except ValueError:
            continue
        for entry in index.get("chats", []):
            if entry.get("conversation_id") == args.conversation_id:
                holders.append((index_path.parent.relative_to(root).as_posix(), entry))
    if len(holders) > 1:
        raise SystemExit("The session is registered in several registries: %s" % ", ".join(h[0] for h in holders))
    registered = holders[0] if holders else None
    chosen = clean_registry(args.registry) if args.registry else None
    if chosen and registered and chosen != registered[0]:
        raise SystemExit("The session is already registered in %s, not %s; refresh it there"
                         % (registered[0], chosen))
    registry = registered[0] if registered else chosen
    report_ = {"conversation_id": args.conversation_id, "registry": registry, "registered": None,
               "index_exists": False, "stage": [], "reserve": []}
    if registry is None:
        report_["hint"] = ("Not registered yet: rerun with --registry, the project's chat-histories/claude-cowork "
                           "or papers/investigations-2/chat-histories/claude-cowork")
        print(json.dumps(report_, indent=1))
        return
    folder = root / registry
    index_path = folder / "index.json"
    report_["index_exists"] = index_path.is_file()
    report_["stage"] = [path for path in SCRIPTS if (root / path).is_file()]
    known = set()
    if index_path.is_file():
        index = json.loads(index_path.read_text(encoding="utf-8"))
        known = {entry["file"] for entry in index.get("chats", [])}
        report_["stage"].append("%s/index.json" % registry)
    else:
        report_["hint"] = "No index.json yet: pass --new-registry to capture"
    if registered:
        entry = registered[1]
        report_["registered"] = {key: entry.get(key) for key in
                                 ("number", "file", "message_count", "captured_at_utc", "last_message_at_utc")}
        report_["stage"].append("%s/%s" % (registry, entry["file"]))
    report_["reserve"] = [name for name in numbered_files(folder) if name not in known]
    print(json.dumps(report_, indent=1))


def cmd_capture(args):
    registry = clean_registry(args.registry)
    staged_root = Path(args.staged_root).resolve() if args.staged_root else ROOT
    staged = staged_root / registry
    recorder = Path(args.recorder).resolve() if args.recorder else staged_root / SCRIPTS[1]
    if not recorder.is_file():
        raise SystemExit("Recorder not found: %s (stage %s)" % (recorder, SCRIPTS[1]))
    has_index = (staged / "index.json").is_file()
    if not has_index and not args.new_registry:
        raise SystemExit("No staged index.json at %s. Stage it first, or pass --new-registry for a registry "
                         "that has none yet." % (staged / "index.json"))
    if has_index and args.new_registry:
        raise SystemExit("--new-registry given, but a staged index.json exists at %s" % staged)
    entry, base = registered_record(staged, session_of(args))
    conversation, text, provenance = converted(args, base)
    device_root = (args.device_root or "~/Documents/%s" % args.repo_name).rstrip("/")
    out_root = Path(args.out_dir)
    if (out_root / registry).is_dir():
        shutil.rmtree(out_root / registry)
    with tempfile.TemporaryDirectory(prefix="cowork-capture-") as scratch:
        work = Path(scratch) / "registry"
        work.mkdir()
        if staged.is_dir():
            for path in staged.iterdir():
                if path.is_file() and path.suffix == ".json":
                    shutil.copyfile(path, work / path.name)
        placeholders = set()
        for name in args.reserve or []:
            if "/" in name or not re.fullmatch(r"\d+_.*\.json", name):
                raise SystemExit("--reserve expects a numbered file name, got %r" % name)
            if not (work / name).exists():
                (work / name).write_bytes(b"")
                placeholders.add(name)
        before = {p.name: sha256(p.read_bytes()) for p in work.iterdir() if p.is_file()}
        source = Path(scratch) / "conversation.json"
        source.write_bytes(text)
        command = [sys.executable, str(recorder), "--import-json", str(source), "--folder", str(work)]
        if args.allow_shorter_refresh:
            command.append("--allow-shorter-refresh")
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode:
            sys.stderr.write(result.stdout + result.stderr)
            raise SystemExit(result.returncode)
        summary = json.loads(result.stdout.strip().splitlines()[-1])
        commit = []
        for path in sorted(work.iterdir()):
            if not path.is_file() or path.name in placeholders or path.name.endswith(".tmp"):
                continue
            digest = sha256(path.read_bytes())
            if before.get(path.name) == digest:
                continue
            target = out_root / registry / path.name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(path, target)
            commit.append({"stagedPath": str(target), "devicePath": "%s/%s/%s" % (device_root, registry, path.name),
                           "repoPath": "%s/%s" % (registry, path.name), "existed": path.name in before,
                           "sha256": digest, "bytes": path.stat().st_size})
        stub = None if entry else readme_stub_text(work, number=summary["number"], per_turn=True)
    meta = conversation["archive_metadata"]
    print(json.dumps({
        "conversation_id": conversation["conversation_id"], "registry": registry, "number": summary["number"],
        "file": summary["file"], "message_count": summary["messages"], "new_chat": entry is None,
        "turns": {key[:8]: turn["status"] for key, turn in meta["turns"].items()},
        "gaps": meta.get("gaps", []), "spool": provenance.get("spool_file"),
        "commit": commit, "readme_stub": stub,
        "next": "Write each file back with device_commit_files, passing expectedMtimeMs from staging for "
                "files that existed" + ("; then add readme_stub to the registry README" if entry is None else "")},
        ensure_ascii=False, indent=1))


def import_with_recorder(data, args):
    recorder = Path(args.recorder).resolve() if args.recorder else DEFAULT_RECORDER
    if not recorder.is_file():
        raise SystemExit("Recorder not found: %s" % recorder)
    with tempfile.TemporaryDirectory(prefix="cowork-chat-") as folder:
        path = Path(folder) / "conversation.json"
        path.write_bytes(data)
        command = [sys.executable, str(recorder), "--import-json", str(path)]
        if args.project:
            command += ["--project", args.project]
        if args.folder:
            command += ["--folder", str(Path(args.folder).expanduser().resolve())]
        if args.allow_shorter_refresh:
            command.append("--allow-shorter-refresh")
        result = subprocess.run(command)
    if result.returncode:
        raise SystemExit(result.returncode)
    note("Next, for a new chat: draft its README entry with `readme-stub` and add it to the registry README.")


def cmd_register(args):
    if bool(args.input) == bool(args.input_b64):
        raise SystemExit("Give exactly one of --input and --input-b64")
    if args.input_b64:
        source = sys.stdin.read() if args.input_b64 == "-" else Path(args.input_b64).read_text()
        data = base64.b64decode("".join(source.split()), validate=True)
        if data[:2] == b"\x1f\x8b":
            data = gzip.decompress(data)
    else:
        data = Path(args.input).read_bytes()
    digest = sha256(data)
    if args.expect_sha256 and digest != args.expect_sha256.lower():
        raise SystemExit("SHA-256 mismatch: got %s, expected %s" % (digest, args.expect_sha256))
    note("input sha256 %s" % digest)
    try:
        conversation = json.loads(data)
    except ValueError as error:
        raise SystemExit("Input is not JSON: %s" % error)
    chats = conversation if isinstance(conversation, list) else [conversation]
    if len(chats) != 1 or not isinstance(chats[0].get("mapping"), dict):
        raise SystemExit("Expected one ChatGPT-style conversation")
    _, base = registered_record(registry_folder(args), chats[0].get("conversation_id"))
    if base is not None:
        merged = merge_conversations(base, chats[0])
        report(merged)
        data = dump(merged)
        note("merged into the registered record: sha256 %s" % sha256(data))
    import_with_recorder(data, args)


def cmd_record(args):
    _, base = registered_record(registry_folder(args), session_of(args))
    _, text, _ = converted(args, base)
    note("converted sha256 %s" % sha256(text))
    import_with_recorder(text, args)


def model_name(identifier):
    parts = (identifier or "").split("-")
    words = [p.capitalize() for p in parts if not p.isdigit()]
    digits = [p for p in parts if p.isdigit()]
    return " ".join(words) + (" " + ".".join(digits) if digits else "")


def readme_stub_text(folder, number=None, conversation_id=None, per_turn=False):
    """A draft registry README entry, in the numbered-list form of the claude-cowork registries."""
    folder = Path(folder)
    index = json.loads((folder / "index.json").read_text(encoding="utf-8"))
    entries = index["chats"]
    if number is not None:
        entries = [e for e in entries if e["number"] == number]
    elif conversation_id:
        entries = [e for e in entries if e["conversation_id"] == conversation_id]
    if not entries:
        raise SystemExit("No matching chat in %s" % (folder / "index.json"))
    entry = entries[-1]
    conversation = json.loads((folder / entry["file"]).read_text(encoding="utf-8"))[0]
    meta = conversation.get("archive_metadata", {})
    project = ((meta.get("session") or {}).get("project") or {}).get("name")
    models = " and ".join("%s (`%s`, reasoning effort %s per the transcript)"
                          % (model_name(c.get("model")), c.get("model"), c.get("reasoning_effort"))
                          for c in entry.get("model_configurations") or [{}])
    started = datetime.fromisoformat(entry["created_at_local"])
    captured = datetime.fromisoformat(entry["captured_at_local"])
    when = "the same day" if captured.date() == started.date() else \
        "on %d %s" % (captured.day, captured.strftime("%B %Y"))
    turns = meta.get("turns", {})
    open_turn = any(t.get("status") == "in_progress" for t in turns.values())
    tool_items = any((node.get("message") or {}).get("metadata", {}).get("rendered_from_tool")
                     for node in conversation["mapping"].values())
    compactions = len((meta.get("compaction") or {}).get("boundaries_utc") or [])
    gaps = meta.get("gaps") or []
    count = entry["message_count"]
    session = ("A Claude Cowork cloud session%s with %s, started %d %s at %s America/New_York."
               % (" in project %s" % project if project else "", models, started.day,
                  started.strftime("%B %Y"), started.strftime("%H:%M")))
    if compactions:
        session += " Its context was compacted %s." % {1: "once", 2: "twice"}.get(compactions, "%d times" % compactions)
    if per_turn:
        capture = ("Captured by the session itself with `record_Claude_cowork_chat.py capture`, first at "
                   "%s %s (%d messages over %d turns), and refreshed at the end of every later turn, before "
                   "that turn's reply; [index.json](index.json) gives the current count."
                   % (captured.strftime("%H:%M"), when, count, len(turns)))
    else:
        capture = ("Captured at %s %s; it holds %d messages over %d turns%s."
                   % (captured.strftime("%H:%M"), when, count, len(turns),
                      "; the reply to the last request was still in progress and enters only on a refresh"
                      if open_turn else ""))
    bullets = ["*Work.* TODO: one sentence on what the conversation did, with links to its saved outputs.",
               "*Session.* " + session, "*Capture.* " + capture]
    if gaps:
        bullets.append("*Gaps.* A compaction rewrote the transcript before %s of it had been read; the "
                       "messages of %s are missing, and `archive_metadata.gaps` lists %s."
                       % (("one window", "that window", "it") if len(gaps) == 1
                          else ("%d windows" % len(gaps), "those windows", "them")))
    if tool_items:
        bullets.append("*Coverage.* As for the earlier Cowork captures, plus chat-visible items that travel "
                       "through tools, labelled in each message's metadata.")
    lines = ["%d. **%s** — [%s](%s)" % (entry["number"], entry["title"], entry["file"], entry["file"])]
    for bullet in bullets:
        lines.append(textwrap.fill("- " + bullet, width=78, initial_indent="   ", subsequent_indent="     ",
                                   break_on_hyphens=False, break_long_words=False))
    return "\n".join(lines) + "\n"


def cmd_readme_stub(args):
    sys.stdout.write(readme_stub_text(registry_folder(args), args.number, args.conversation_id, args.per_turn))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    def transcript_options(p):
        p.add_argument("--transcript", help="Claude Agent SDK transcript (default: newest under --projects-dir)")
        p.add_argument("--projects-dir", default="~/.claude/projects")
        p.add_argument("--spool-dir", default=DEFAULT_SPOOL_DIR, help="Folder of the session spools (default: %(default)s)")
        p.add_argument("--spool-from", action="append", metavar="PATH",
                       help="Add the records of an earlier copy of the transcript to the spool (repeatable)")
        p.add_argument("--no-spool", action="store_true", help="Read the transcript alone, without the spool")

    def conversion_options(p):
        transcript_options(p)
        p.add_argument("--title", help="Override the session's recorded title")
        p.add_argument("--claude-session-url", help="Override the claude.ai session link")
        p.add_argument("--session-note", action="append", metavar="KEY=VALUE",
                       help="Extra archive_metadata.session field (repeatable)")
        p.add_argument("--delivered", action="append", metavar="PATH",
                       help="Delivered file not detected automatically (repeatable)")
        p.add_argument("--repo-name", default=ROOT.name if (ROOT / "papers").is_dir() else "shifted-zeta-positivity",
                       help="Folder name used to shorten device paths to repository paths")

    def registry_options(p):
        p.add_argument("--recorder", help="record_chat.py to use (default: %s)" % SCRIPTS[1])
        target = p.add_mutually_exclusive_group()
        target.add_argument("--project", help="Project folder name under papers/investigations-2")
        target.add_argument("--folder", help="Explicit chat-history folder")
        p.add_argument("--allow-shorter-refresh", action="store_true")

    p = sub.add_parser("spool", help="Add the transcript's new records to the session spool")
    transcript_options(p)
    p.set_defaults(func=cmd_spool)

    p = sub.add_parser("session-id", help="Print the session id of the newest transcript")
    p.add_argument("--transcript", help="Claude Agent SDK transcript (default: newest under --projects-dir)")
    p.add_argument("--projects-dir", default="~/.claude/projects")
    p.set_defaults(func=cmd_session_id)

    p = sub.add_parser("locate", help="On the computer: the registry holding a session and the files to stage")
    p.add_argument("--conversation-id", required=True, help="The session id")
    p.add_argument("--registry", help="Repository-relative registry folder, for a first capture")
    p.add_argument("--root", help="Repository root (default: the one holding this script)")
    p.set_defaults(func=cmd_locate)

    p = sub.add_parser("capture", help="Cloud workspace: convert, merge and import into a staged registry")
    conversion_options(p)
    p.add_argument("--registry", required=True, help="Repository-relative registry folder")
    p.add_argument("--staged-root", help="Staged repository root (default: the one holding this script)")
    p.add_argument("--reserve", action="append", metavar="NAME",
                   help="Numbered file name that locate listed under reserve (repeatable)")
    p.add_argument("--new-registry", action="store_true", help="The registry has no index.json yet")
    p.add_argument("--out-dir", default=DEFAULT_OUT_DIR, help="Where to write the files to commit (default: %(default)s)")
    p.add_argument("--device-root", help="Repository root on the computer (default: ~/Documents/REPO_NAME)")
    p.add_argument("--recorder", help="record_chat.py to use (default: the staged %s)" % SCRIPTS[1])
    p.add_argument("--allow-shorter-refresh", action="store_true")
    p.set_defaults(func=cmd_capture)

    p = sub.add_parser("convert", help="Transcript -> conversation JSON")
    conversion_options(p)
    p.add_argument("--output", required=True)
    p.add_argument("--b64-output", help="Also write the JSON as base64, for transfer between machines")
    p.add_argument("--gzip", action="store_true", help="Compress the JSON with gzip before base64")
    p.add_argument("--base", help="A registered record of the session to merge the conversion into")
    p.set_defaults(func=cmd_convert)

    p = sub.add_parser("register", help="Import a converted conversation with record_chat.py")
    p.add_argument("--input", help="Conversation JSON file")
    p.add_argument("--input-b64", help="Base64 (optionally of gzip) of the conversation JSON: a file, or - for stdin")
    p.add_argument("--expect-sha256", help="Refuse unless the decoded JSON has this SHA-256")
    registry_options(p)
    p.set_defaults(func=cmd_register)

    p = sub.add_parser("record", help="convert + register on one machine")
    conversion_options(p)
    registry_options(p)
    p.set_defaults(func=cmd_record)

    p = sub.add_parser("readme-stub", help="Draft a registry README entry for a registered chat")
    target = p.add_mutually_exclusive_group()
    target.add_argument("--project")
    target.add_argument("--folder")
    p.add_argument("--number", type=int)
    p.add_argument("--conversation-id")
    p.add_argument("--per-turn", action="store_true",
                   help="Describe a record the session refreshes at the end of every turn (as printed at its first capture)")
    p.set_defaults(func=cmd_readme_stub)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
