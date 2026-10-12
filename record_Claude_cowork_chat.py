#!/usr/bin/env python3
"""Record a Claude Cowork conversation in one of the repository's chat histories.

Prepared for Edward Baker with LLM assistance. Model: Claude Opus 5.5
(configured identifier claude-opus-5-5), Claude Cowork, 12 October 2026.

The chat registries are written by `record_chat.py`
(papers/investigations-2/record_chat.py, and an older copy in
papers/quasi-rh-exponent-descent/chat-histories/). That recorder captures
Codex sessions directly and imports ChatGPT-style JSON with --import-json.
This script supplies the Cowork side:

  convert      Claude Agent SDK transcript (JSONL) -> one ChatGPT-style
               conversation JSON, under the coverage rules below.
  register     Import a converted conversation with a chosen record_chat.py.
  record       convert + register, when the transcript and the repository are
               on the same machine (for example Claude Code run locally).
  readme-stub  Print a draft guide paragraph for a registered chat.

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
included), internal reasoning, other tool calls and outputs, permission
prompts, subagent records, attachments and runtime state. The raw transcript is
never copied into the repository; archive_metadata records its SHA-256.

Cowork procedure. The transcript lives in the cloud workspace and the
repository on the person's computer, so the two steps run in different places:

  1. Cloud workspace (get this file there, e.g. by staging it from the repo):
       python3 record_cowork_chat.py convert --output conv.json --b64-output conv.b64
     The newest transcript under ~/.claude/projects is used unless
     --transcript is given. The chosen path and the output SHA-256 are printed.
     Add --delivered PATH for files written by shell commands, which are not
     detected automatically.
  2. Computer, from the repository root (the base64 text comes from conv.b64):
       python3 record_cowork_chat.py register --input-b64 - --expect-sha256 HEX \\
           [--project NAME | --folder PATH] <<'EOF'
       ...base64...
       EOF
  3. Draft the guide paragraph, edit its first sentence, and add it to that
     registry's README:
       python3 record_cowork_chat.py readme-stub [--project NAME | --folder PATH]

Repeating the steps later refreshes the same chat number, since the
conversation id is the session id. record_chat.py refuses a shorter or older
refresh unless --allow-shorter-refresh is given. The default recorder and
registry are those of papers/investigations-2; use --recorder and --folder
for another registry.

Standard library only (Python 3.9+).
"""
from __future__ import annotations

import argparse
import base64
import glob
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import textwrap
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parent
BASE = ROOT / "papers" / "investigations-2"
DEFAULT_RECORDER = BASE / "record_chat.py"
UTC = timezone.utc
LOCAL = ZoneInfo("America/New_York")
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
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
    "internal reasoning",
    "tool calls and outputs, except the chat-visible items named in coverage",
    "permission and folder-access prompts",
    "subagent messages",
    "attachments and runtime state",
]


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


def note(message):
    print(message, file=sys.stderr)


# ------------------------------------------------------------ transcript I/O

def find_transcript(projects_dir):
    pattern = str(Path(projects_dir).expanduser() / "*" / "*.jsonl")
    candidates = [Path(path) for path in glob.glob(pattern)]
    if not candidates:
        sys.exit("No transcript found under %s; pass --transcript" % projects_dir)
    return max(candidates, key=lambda path: path.stat().st_mtime)


def read_transcript(path):
    raw = Path(path).read_bytes()
    complete = raw[:raw.rfind(b"\n") + 1] if b"\n" in raw else raw
    rows = [json.loads(line) for line in complete.decode("utf-8").splitlines() if line.strip()]
    return complete, rows


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


def convert(rows, transcript_bytes, options):
    records_read = len(rows)
    rows = [row for row in rows if not row.get("isSidechain")]
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
    if not prompts:
        raise SystemExit("No typed prompt found in the transcript")

    # Turns: each typed prompt opens one; everything until the next belongs to it.
    starts = [e["t"] for e in events if e["kind"] == "prompt"]
    keys = [e.get("prompt_id") or e["id"] for e in events if e["kind"] == "prompt"]
    stops = sorted(epoch(r["timestamp"]) for r in rows
                   if r.get("type") == "system" and r.get("subtype") in STOP_SUBTYPES and r.get("timestamp"))
    assistant_times = sorted(epoch(r["timestamp"]) for r in rows
                             if r.get("type") == "assistant" and r.get("timestamp"))
    skipped_prompt_ids = {r.get("promptId") for r in rows if r.get("type") == "user"
                          and r.get("promptId") and isinstance(r.get("message", {}).get("content"), str)
                          and r["message"]["content"].lstrip().startswith(SKIP_PREFIXES)}

    turns = {}
    for index, (start, key) in enumerate(zip(starts, keys)):
        end = starts[index + 1] if index + 1 < len(starts) else float("inf")
        members = [e for e in events if start <= e["t"] < end]
        for e in members:
            e["turn"] = key
        interrupt = next((e for e in members if e["kind"] == "interrupt"), None)
        last_assistant = max((t for t in assistant_times if start <= t < end), default=start)
        stop = [t for t in stops if last_assistant <= t < end]
        texts = [e for e in members if e["role"] == "assistant" and e["kind"] == "text"]
        record = {"started_at": iso(start)}
        if interrupt:
            record = {"status": "interrupted", **record, "interrupted_at": iso(interrupt["t"])}
        elif stop or end != float("inf"):
            final = texts[-1] if texts else None
            if final:
                final["phase"] = "final_answer"
            done = final["t"] if final else (stop[0] if stop else last_assistant)
            record = {"status": "completed", **record, "completed_at": iso(done)}
        else:
            record = {"status": "in_progress", **record}
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

    mapping = {"root": {"id": "root", "message": None, "parent": None, "children": []}}
    parent = "root"
    for e in events:
        phase = e.get("phase") or ("commentary" if e["role"] == "assistant" else None)
        metadata = {"source": SOURCE, "source_turn_id": e["turn"], "phase": phase,
                    "created_at_utc": iso(e["t"]), "completed_at_utc": iso(e["t"]),
                    "created_at_local": local(e["t"])}
        metadata.update(e["extra"])
        mapping[e["id"]] = {
            "id": e["id"],
            "message": {
                "id": e["id"],
                "author": {"role": e["role"], "name": None, "metadata": {}},
                "create_time": e["t"],
                "update_time": e["t"],
                "content": {"content_type": "text", "parts": [e["text"]]},
                "status": "finished_successfully",
                "end_turn": (phase == "final_answer") if e["role"] == "assistant" else None,
                "metadata": metadata,
                "recipient": "all",
            },
            "parent": parent,
            "children": [],
        }
        mapping[parent]["children"].append(e["id"])
        parent = e["id"]

    session_id = next(r["sessionId"] for r in rows if r.get("sessionId"))
    titles = [r.get("aiTitle") for r in rows if r.get("type") == "ai-title" and r.get("aiTitle")]
    stamps = [epoch(r["timestamp"]) for r in rows if r.get("timestamp")]
    attachments = [r.get("attachment") or {} for r in rows if r.get("type") == "attachment"]
    urls = [a.get("url") for a in attachments if a.get("type") == "remote_session_change" and a.get("url")]
    identity = [a.get("identity", {}).get("modelId") for a in attachments if a.get("type") == "model"]
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
    session.update(options.get("session_notes") or {})
    delivered = list(dict.fromkeys(delivered + list(options.get("delivered") or [])))
    script = Path(__file__).resolve()
    return {
        "title": options.get("title") or (titles[-1] if titles else "Cowork session %s" % session_id[:8]),
        "create_time": min(stamps),
        "update_time": events[-1]["t"],
        "mapping": mapping,
        "current_node": parent,
        "conversation_id": session_id,
        "id": session_id,
        "archive_metadata": {
            "format": "ChatGPT-style conversation mapping; local conversion, not an official provider export",
            "source_kind": "Claude Cowork session transcript (Claude Agent SDK JSONL), completed public text messages",
            "message_timestamps": "Transcript record times, in seconds since Unix epoch and ISO 8601; the conversation create_time is the first transcript event; a message typed while a reply was in progress carries its queue time, with its delivery time in metadata",
            "coverage": COVERAGE,
            "omitted_record_types": OMITTED,
            "source_public_message_records": len(events),
            "model_configurations": [{"model": m, "reasoning_effort": e} for m, e in models],
            "turns": turns,
            "session": session,
            "source_transcript": {
                "records_read": records_read,
                "bytes_read": len(transcript_bytes),
                "sha256_of_bytes_read": sha256(transcript_bytes),
                "last_record_utc": iso(max(stamps)),
                "note": "The transcript is not stored in the repository; it contains instructions, reasoning and tool traffic that the coverage rules exclude",
            },
            "delivered_files_not_embedded": delivered,
            "converter": {"script": script.name, "sha256": sha256(script.read_bytes())},
        },
    }


# ----------------------------------------------------------------- commands

def parse_notes(pairs):
    notes = {}
    for pair in pairs or []:
        if "=" not in pair:
            raise SystemExit("--session-note expects KEY=VALUE, got %r" % pair)
        key, value = pair.split("=", 1)
        notes[key.strip()] = value.strip()
    return notes


def run_convert(args):
    transcript = Path(args.transcript) if args.transcript else find_transcript(args.projects_dir)
    data, rows = read_transcript(transcript)
    conversation = convert(rows, data, {
        "title": args.title, "claude_session_url": args.claude_session_url,
        "session_notes": parse_notes(args.session_note), "delivered": args.delivered,
        "repo_name": args.repo_name,
    })
    text = (json.dumps(conversation, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    note("transcript: %s (%d records)" % (transcript, len(rows)))
    node = conversation["mapping"]["root"]
    while node["children"]:
        node = conversation["mapping"][node["children"][0]]
        message = node["message"]
        preview = message["content"]["parts"][0].replace("\n", " ")[:70]
        note("  %s %-9s %-12s %s" % (message["metadata"]["created_at_utc"], message["author"]["role"],
                                     message["metadata"]["phase"] or "", preview))
    for key, turn in conversation["archive_metadata"]["turns"].items():
        note("  turn %s: %s" % (key[:8], turn["status"]))
    return conversation, text


def cmd_convert(args):
    _, text = run_convert(args)
    Path(args.output).write_bytes(text)
    if args.b64_output:
        Path(args.b64_output).write_text(base64.b64encode(text).decode("ascii") + "\n")
    print("wrote %s  sha256 %s  (%d bytes)" % (args.output, sha256(text), len(text)))


def import_with_recorder(data, args):
    try:
        conversation = json.loads(data)
    except ValueError as error:
        raise SystemExit("Input is not JSON: %s" % error)
    chats = conversation if isinstance(conversation, list) else [conversation]
    if len(chats) != 1 or not isinstance(chats[0].get("mapping"), dict):
        raise SystemExit("Expected one ChatGPT-style conversation")
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
            command += ["--folder", str(Path(args.folder).resolve())]
        if args.allow_shorter_refresh:
            command.append("--allow-shorter-refresh")
        result = subprocess.run(command)
    if result.returncode:
        raise SystemExit(result.returncode)
    note("Next: draft the guide paragraph with `readme-stub` and add it to the registry README.")


def cmd_register(args):
    if bool(args.input) == bool(args.input_b64):
        raise SystemExit("Give exactly one of --input and --input-b64")
    if args.input_b64:
        source = sys.stdin.read() if args.input_b64 == "-" else Path(args.input_b64).read_text()
        data = base64.b64decode("".join(source.split()), validate=True)
    else:
        data = Path(args.input).read_bytes()
    digest = sha256(data)
    if args.expect_sha256 and digest != args.expect_sha256.lower():
        raise SystemExit("SHA-256 mismatch: got %s, expected %s" % (digest, args.expect_sha256))
    note("input sha256 %s" % digest)
    import_with_recorder(data, args)


def cmd_record(args):
    _, text = run_convert(args)
    note("converted sha256 %s" % sha256(text))
    import_with_recorder(text, args)


def model_name(identifier):
    parts = (identifier or "").split("-")
    words = [p.capitalize() for p in parts if not p.isdigit()]
    digits = [p for p in parts if p.isdigit()]
    return " ".join(words) + (" " + ".".join(digits) if digits else "")


def cmd_readme_stub(args):
    if args.folder:
        folder = Path(args.folder)
    elif args.project:
        folder = BASE / args.project / "chat-histories"
    else:
        folder = BASE / "chat-histories"
    index = json.loads((folder / "index.json").read_text(encoding="utf-8"))
    entries = index["chats"]
    if args.number is not None:
        entries = [e for e in entries if e["number"] == args.number]
    elif args.conversation_id:
        entries = [e for e in entries if e["conversation_id"] == args.conversation_id]
    if not entries:
        raise SystemExit("No matching chat in %s" % (folder / "index.json"))
    entry = entries[-1]
    conversation = json.loads((folder / entry["file"]).read_text(encoding="utf-8"))[0]
    meta = conversation.get("archive_metadata", {})
    config = (entry.get("model_configurations") or [{}])[0]
    started = datetime.fromisoformat(entry["created_at_local"])
    captured = datetime.fromisoformat(entry["captured_at_local"])
    when = "the same day" if captured.date() == started.date() else \
        "on %d %s" % (captured.day, captured.strftime("%B %Y"))
    turns = meta.get("turns", {})
    open_turn = any(t.get("status") == "in_progress" for t in turns.values())
    tool_items = any((node.get("message") or {}).get("metadata", {}).get("rendered_from_tool")
                     for node in conversation["mapping"].values())
    count = entry["message_count"]
    bullets = [
        "- *Session.* A Claude Cowork session with %s (`%s`, reasoning effort %s per the transcript), "
        "started %d %s at %s America/New_York."
        % (model_name(config.get("model")), config.get("model"), config.get("reasoning_effort"),
           started.day, started.strftime("%B %Y"), started.strftime("%H:%M")),
        "- *Capture.* It was captured at %s %s and holds %d messages over %d turns%s."
        % (captured.strftime("%H:%M"), when, count, len(turns),
           "; the reply to the last request was still in progress and enters only on a refresh"
           if open_turn else ""),
    ]
    if tool_items:
        bullets.append("- *Coverage.* As for the earlier Cowork captures, plus chat-visible items that "
                       "travel through tools, labelled in each message's metadata.")
    print("[Chat %d — %s](%s)" % (entry["number"], entry["title"], entry["file"]))
    print("records TODO: one sentence on what the conversation did, with links to its saved outputs.")
    print()
    for bullet in bullets:
        print(textwrap.fill(bullet, width=76, subsequent_indent="  ", break_on_hyphens=False))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    def conversion_options(p):
        p.add_argument("--transcript", help="Claude Agent SDK transcript (default: newest under --projects-dir)")
        p.add_argument("--projects-dir", default="~/.claude/projects")
        p.add_argument("--title", help="Override the session's recorded title")
        p.add_argument("--claude-session-url", help="Override the claude.ai session link")
        p.add_argument("--session-note", action="append", metavar="KEY=VALUE",
                       help="Extra archive_metadata.session field (repeatable)")
        p.add_argument("--delivered", action="append", metavar="PATH",
                       help="Delivered file not detected automatically (repeatable)")
        p.add_argument("--repo-name", default=ROOT.name if (ROOT / "papers").is_dir() else "shifted-zeta-positivity",
                       help="Folder name used to shorten device paths to repository paths")

    def registry_options(p):
        p.add_argument("--recorder", help="record_chat.py to use (default: %s)" % DEFAULT_RECORDER.relative_to(ROOT))
        target = p.add_mutually_exclusive_group()
        target.add_argument("--project", help="Project folder name under papers/investigations-2")
        target.add_argument("--folder", help="Explicit chat-history folder")
        p.add_argument("--allow-shorter-refresh", action="store_true")

    p = sub.add_parser("convert", help="Transcript -> conversation JSON")
    conversion_options(p)
    p.add_argument("--output", required=True)
    p.add_argument("--b64-output", help="Also write the JSON as base64, for transfer between machines")
    p.set_defaults(func=cmd_convert)

    p = sub.add_parser("register", help="Import a converted conversation with record_chat.py")
    p.add_argument("--input", help="Conversation JSON file")
    p.add_argument("--input-b64", help="Base64 of the conversation JSON: a file, or - for stdin")
    p.add_argument("--expect-sha256", help="Refuse unless the decoded JSON has this SHA-256")
    registry_options(p)
    p.set_defaults(func=cmd_register)

    p = sub.add_parser("record", help="convert + register on one machine")
    conversion_options(p)
    registry_options(p)
    p.set_defaults(func=cmd_record)

    p = sub.add_parser("readme-stub", help="Draft a guide paragraph for a registered chat")
    target = p.add_mutually_exclusive_group()
    target.add_argument("--project")
    target.add_argument("--folder")
    p.add_argument("--number", type=int)
    p.add_argument("--conversation-id")
    p.set_defaults(func=cmd_readme_stub)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
