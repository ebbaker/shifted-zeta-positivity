#!/usr/bin/env python3
"""Record earlier Claude conversations in the repository's chat histories.

Prepared for Edward Baker with LLM assistance. Model: Claude Opus 5.5
(configured identifier claude-opus-5-5), Claude Cowork, 13 October 2026.
Moved to tools/ the same day (same model).

tools/record_Claude_cowork_chat.py captures a Cowork session from inside that
session, using the session's own transcript. This script recovers the
conversations from before that practice began, from two sources kept outside
the repository:

  cowork  A Cowork cloud session, from a session-events file written in the
          signed-in browser by the extractor that `extractor` prints. The
          extractor reads the session's event log from claude.ai
          (GET /v1/code/sessions/{id}/events, an internal endpoint of the web
          app) and keeps only the fields the coverage rules below use. The
          session list (GET /v1/code/sessions?tags=cowork-remote) supplies
          the title, model, effort and chat_project_id. That id is
          "claude_proj_01" followed by the project UUID in base 58; the
          conversion decodes it and refuses a mismatch with the stated
          project UUID.
  chat    A claude.ai chat, from the account data export (conversations.json).
          The export records neither project nor model, so both come from
          claude.ai's chat list for the project
          (GET /api/organizations/{org}/projects/{uuid}/conversations_v2)
          and are passed in with --project-name, --project-uuid and --model.

Each source becomes one ChatGPT-style conversation of the shape used by every
registry, registered with record_chat.py --import-json --folder (default
recorder: papers/investigations-2/record_chat.py).

Coverage, as for the Cowork captures. Kept:
  - messages typed by the person, including messages sent while a reply was in
    progress, with the names (not contents) of files sent with them, and the
    interruption markers the person triggered;
  - the assistant's text shown in the chat: progress lines (phase commentary)
    and the text ending each completed turn (phase final_answer);
  - Cowork items that travel through tools, rendered as text and labelled in
    message metadata: question cards (AskUserQuestion) with the selected
    options, notes sent with SendUserMessage, and file-card captions
    (SendUserFile).
Omitted: system and harness text (reminders, date notes, memory snapshots,
continuation summaries after context compaction, hook feedback, skill text,
local command output), internal reasoning, other tool calls and outputs,
permission prompts, control and environment events, usage and cost figures,
subagent messages, and the contents of attachments. A claude.ai chat keeps its
message tree, so a reply left behind by an edited prompt stays on its own
branch; current_node is the end of the most recent branch.

Usage, from the repository root:
  python3 tools/record_Claude_export_chat.py list --events FILE
  python3 tools/record_Claude_export_chat.py cowork --events FILE --session-id cse_... --folder DIR
  python3 tools/record_Claude_export_chat.py chat --export conversations.json \\
      --conversation-id UUID --project-name NAME --project-uuid UUID --model ID --folder DIR
  python3 tools/record_Claude_export_chat.py readme-stub --folder DIR [--number N]
  python3 tools/record_Claude_export_chat.py extractor
Add --dry-run --output PATH to write a conversion without registering it.
Neither the export nor the events file is copied into the repository; each
record stores their SHA-256 instead.

Standard library only (Python 3.9+).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import textwrap
import uuid as uuidlib
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

def find_root(start):
    """The repository root: the nearest folder holding papers/ beside tools/ or .git."""
    for folder in (start, *start.parents):
        if (folder / "papers").is_dir() and ((folder / "tools").is_dir() or (folder / ".git").exists()):
            return folder
    return start.parent if start.name == "tools" else start


ROOT = find_root(Path(__file__).resolve().parent)
DEFAULT_RECORDER = ROOT / "papers" / "investigations-2" / "record_chat.py"
UTC = timezone.utc
LOCAL = ZoneInfo("America/New_York")
BASE58 = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
PROJECT_TAG = "claude_proj_01"
ROOT_SENTINEL = "00000000-0000-4000-8000-000000000000"
REMINDER = re.compile(r"<system-reminder>.*?</system-reminder>", re.S)
UPLOADED = re.compile(r"<uploaded_files>(.*?)</uploaded_files>", re.S)
UPLOADED_PATH = re.compile(r"<file_path>(.*?)</file_path>", re.S)
SKIP_PREFIXES = ("<system-reminder>", "<command-name>", "<command-message>",
                 "<command-args>", "<local-command")
INTERRUPTED = "[Request interrupted by user"
RENDERED_TOOLS = ("AskUserQuestion", "SendUserMessage", "SendUserFile")
RENDERING = {
    "AskUserQuestion": "header, question and options of the card, as text",
    "answer": "the option the person selected in the question card",
    "SendUserMessage": "verbatim message shown to the person between tool calls",
    "SendUserFile": "caption of a file card shown to the person",
}
OMITTED = [
    "system, developer and harness text (reminders, date notes, memory snapshots, "
    "continuation summaries, hook feedback, skill text, local command output)",
    "internal reasoning",
    "tool calls and outputs, except the chat-visible items named in coverage",
    "permission prompts, control and environment events, usage and cost figures",
    "subagent messages",
    "attachment contents (file names are kept in message metadata)",
]
FORMAT = "ChatGPT-style conversation mapping; local conversion, not an official provider export"

EXTRACTOR_JS = r'''async function (id) {
  const H = {headers: {'anthropic-version': '2023-06-01'}};
  const KEEP_INPUT = new Set(['AskUserQuestion', 'SendUserMessage', 'SendUserFile']);
  const KEEP_RESULT = new Set(['AskUserQuestion', 'mcp__remote-devices__device_commit_files']);
  const strip = (t) => typeof t === 'string' ? t.replace(/<system-reminder>[\s\S]*?<\/system-reminder>/g, '').trim() : t;
  let events = [], cursor = null, pages = 0, seen = new Set();
  while (true) {
    const url = `/v1/code/sessions/${id}/events?limit=100` + (cursor ? '&cursor=' + encodeURIComponent(cursor) : '');
    let r, tries = 0;
    while (true) { r = await fetch(url, H); if (r.status !== 429 && r.status < 500) break; if (++tries > 6) throw new Error('fetch failed ' + r.status); await new Promise(res => setTimeout(res, 2000 * tries)); }
    if (!r.ok) throw new Error('HTTP ' + r.status + ' for ' + id);
    const b = await r.json();
    const fresh = (b.data || []).filter(e => !seen.has(e.event_id));
    fresh.forEach(e => seen.add(e.event_id));
    events = events.concat(fresh); pages++;
    if (!fresh.length || !b.next_cursor || b.next_cursor === cursor || pages > 2000) break;
    cursor = b.next_cursor;
  }
  events.sort((a, b) => Number(a.sequence_num) - Number(b.sequence_num));
  const raw = JSON.stringify(events);
  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(raw));
  const sha = Array.from(new Uint8Array(digest)).map(x => x.toString(16).padStart(2, '0')).join('');
  const names = {};
  for (const e of events) { const p = e.payload || {}; if (p.type === 'assistant' && p.message && Array.isArray(p.message.content)) for (const k of p.message.content) if (k.type === 'tool_use') names[k.id] = k.name; }
  const counts = {}, sdkIds = new Set(), records = [];
  let subagent = 0;
  for (const e of events) {
    const p = e.payload || {};
    const t = p.type || e.event_type;
    counts[t] = (counts[t] || 0) + 1;
    if (p.session_id) sdkIds.add(p.session_id);
    const base = {seq: Number(e.sequence_num), created_at: e.created_at, source: e.source, type: t};
    if (t === 'user' || t === 'assistant') {
      if (p.parent_tool_use_id) { subagent++; continue; }
      const m = p.message || {};
      const c = m.content;
      const blocks = typeof c === 'string' ? [{type: 'text', text: strip(c)}] : (c || []).map(k => {
        if (k.type === 'text') return {type: 'text', text: strip(k.text)};
        if (k.type === 'tool_use') return KEEP_INPUT.has(k.name) ? {type: 'tool_use', id: k.id, name: k.name, input: k.input} : {type: 'tool_use', id: k.id, name: k.name};
        if (k.type === 'tool_result') { const n = names[k.tool_use_id]; const o = {type: 'tool_result', tool_use_id: k.tool_use_id, name: n || null, is_error: !!k.is_error}; if (KEEP_RESULT.has(n)) o.content = k.content; return o; }
        return {type: k.type};
      });
      const rec = Object.assign(base, {uuid: p.uuid, timestamp: p.timestamp, blocks});
      if (t === 'assistant') { rec.model = m.model || null; rec.message_id = m.id || null; rec.stop_reason = m.stop_reason || null; }
      if (t === 'user') {
        for (const k of ['isMeta', 'isSynthetic', 'shouldQuery', 'priority', 'isReplay', 'isCompactSummary', 'origin']) if (p[k] !== undefined) rec[k] = p[k];
        const rn = blocks.filter(k => k.type === 'tool_result').map(k => k.name);
        if (p.tool_use_result && rn.some(n => KEEP_RESULT.has(n))) rec.tool_use_result = p.tool_use_result;
      }
      records.push(rec);
    } else if (t === 'result') {
      records.push(Object.assign(base, {subtype: p.subtype, is_error: p.is_error, stop_reason: p.stop_reason, terminal_reason: p.terminal_reason, user_message_uuids: p.user_message_uuids || [], origin: p.origin || null, uuid: p.uuid}));
    } else if (t === 'system' && ['init', 'compact_boundary'].includes(p.subtype)) {
      records.push(Object.assign(base, {subtype: p.subtype, model: p.model || null, permissionMode: p.permissionMode || null}));
    } else if (t === 'control_request' && p.request && p.request.subtype === 'interrupt') {
      records.push(Object.assign(base, {subtype: 'interrupt'}));
    }
  }
  return {id, events_read: events.length, pages, first_seq: events.length ? Number(events[0].sequence_num) : null, last_seq: events.length ? Number(events[events.length - 1].sequence_num) : null, sha256_of_events_json: sha, events_json_bytes: new TextEncoder().encode(raw).length, event_counts: counts, subagent_messages_omitted: subagent, sdk_session_ids: [...sdkIds], records};
}'''


# ---------------------------------------------------------------- utilities

def epoch(stamp):
    return datetime.fromisoformat(stamp.replace("Z", "+00:00")).timestamp()


def iso(value):
    return datetime.fromtimestamp(value, UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def local(value):
    return datetime.fromtimestamp(value, LOCAL).isoformat(timespec="milliseconds")


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def note(message):
    print(message, file=sys.stderr)


def project_uuid_from_tag(tag):
    """Decode a chat_project_id ("claude_proj_01" + base-58 UUID)."""
    if not isinstance(tag, str) or not tag.startswith(PROJECT_TAG):
        return None
    number = 0
    for char in tag[len(PROJECT_TAG):]:
        if char not in BASE58:
            return None
        number = number * 58 + BASE58.index(char)
    if number >= 1 << 128:
        return None
    return str(uuidlib.UUID(int=number))


def repo_relative(path, repo_name="shifted-zeta-positivity"):
    marker = "/%s/" % repo_name
    return path.split(marker, 1)[1] if marker in path else path


def question_text(questions):
    lines = []
    for question in questions or []:
        lines.append("%s: %s" % (question.get("header", ""), question.get("question", "")))
        for option in question.get("options", []):
            lines.append("- %s — %s" % (option.get("label", ""), option.get("description", "")))
    return "\n".join(lines)


def answer_text(result):
    if not isinstance(result, dict):
        return None
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


def written_paths(block, record):
    """Paths a device_commit_files call reports as written."""
    candidates = [record.get("tool_use_result"), block.get("content")]
    for candidate in candidates:
        if isinstance(candidate, list):
            candidate = "".join(part.get("text", "") for part in candidate if isinstance(part, dict))
        if isinstance(candidate, str):
            try:
                candidate = json.loads(candidate)
            except ValueError:
                continue
        if isinstance(candidate, dict) and isinstance(candidate.get("written"), list):
            return candidate["written"]
    return []


def model_name(identifier):
    parts = (identifier or "").split("-")
    words = [p.capitalize() for p in parts if not p.isdigit()]
    digits = [p for p in parts if p.isdigit()]
    return " ".join(words) + (" " + ".".join(digits) if digits else "")


class Ids:
    def __init__(self):
        self.used = set()

    def claim(self, preferred, fallback):
        ident = preferred if preferred and preferred not in self.used else fallback
        while ident in self.used:
            ident += "+"
        self.used.add(ident)
        return ident


def node(ident, role, created, updated, text, metadata, phase=None):
    meta = dict(metadata)
    meta.setdefault("phase", phase)
    return {
        "id": ident,
        "message": {
            "id": ident,
            "author": {"role": role, "name": None, "metadata": {}},
            "create_time": created,
            "update_time": updated,
            "content": {"content_type": "text", "parts": [text]},
            "status": "finished_successfully",
            "end_turn": (phase == "final_answer") if role == "assistant" else None,
            "metadata": meta,
            "recipient": "all",
        },
        "parent": None,
        "children": [],
    }


def stamps(created, updated):
    return {"created_at_utc": iso(created), "completed_at_utc": iso(updated),
            "created_at_local": local(created)}


# ------------------------------------------------------------ Cowork sessions

COWORK_SOURCE = "Claude Cowork session event, completed public message"
COWORK_COVERAGE = (
    "Messages typed by the person (including any sent while a reply was in progress, with the names "
    "of files sent with them) and interruption markers; the options the person selected in question "
    "cards; the assistant text shown in the chat: progress lines between tool calls, question cards "
    "rendered as text, notes and file-card captions sent through tools (phase commentary), and the "
    "text ending each completed turn (phase final_answer); recorded through the event log as read")


def load_events(path):
    data = Path(path).read_bytes()
    doc = json.loads(data)
    if not str(doc.get("format", "")).startswith("rh-cowork-session-events/"):
        raise SystemExit("Not a session-events file: %s" % path)
    return doc, data


def cowork_conversation(doc, data, path, session_id, options):
    session = next((s for s in doc["sessions"] if s["session"]["id"] == session_id), None)
    if session is None:
        raise SystemExit("Session %s is not in %s" % (session_id, path))
    meta = session["session"]
    decoded = project_uuid_from_tag(meta.get("chat_project_id"))
    if decoded != meta.get("project_uuid"):
        raise SystemExit("chat_project_id %s decodes to %s, not the stated project %s"
                         % (meta.get("chat_project_id"), decoded, meta.get("project_uuid")))
    records = sorted(session["records"], key=lambda r: r["seq"])
    ids = Ids()

    def when(record):
        return epoch(record.get("timestamp") or record["created_at"])

    tools = {}
    for record in records:
        if record["type"] == "assistant":
            for block in record["blocks"]:
                if block["type"] == "tool_use":
                    tools[block["id"]] = (block["name"], block.get("input") or {})

    items, delivered, models = [], [], set()
    for record in records:
        kind = record["type"]
        if kind == "user":
            text = "\n\n".join(b.get("text") or "" for b in record["blocks"] if b["type"] == "text").strip()
            text = REMINDER.sub("", text).strip()
            for block in record["blocks"]:
                if block["type"] != "tool_result":
                    continue
                name, _ = tools.get(block.get("tool_use_id"), (block.get("name"), {}))
                if name == "AskUserQuestion":
                    answer = answer_text(record.get("tool_use_result"))
                    if answer:
                        items.append({"t": when(record), "seq": record["seq"], "role": "user", "kind": "answer",
                                      "id": ids.claim(record["uuid"], block.get("tool_use_id")), "text": answer,
                                      "extra": {"rendered_from_tool": "AskUserQuestion",
                                                "rendering": RENDERING["answer"]}})
                elif name and name.endswith("device_commit_files"):
                    delivered.extend(repo_relative(p) for p in written_paths(block, record))
            if record.get("source") == "client":
                if record.get("shouldQuery") is False or record.get("isMeta") or record.get("isSynthetic"):
                    continue
                if text.lstrip().startswith(SKIP_PREFIXES):
                    continue
                extra = {}
                uploaded = UPLOADED.search(text)
                if uploaded:
                    extra["attachments"] = [Path(p.strip()).name for p in UPLOADED_PATH.findall(uploaded.group(1))]
                    text = UPLOADED.sub("", text).strip()
                others = [b["type"] for b in record["blocks"] if b["type"] not in ("text", "tool_result")]
                if others:
                    extra["attachment_types"] = others
                if not text and not extra:
                    continue
                items.append({"t": when(record), "seq": record["seq"], "role": "user", "kind": "prompt",
                              "id": ids.claim(record["uuid"], "%s-prompt" % record["uuid"]),
                              "uuid": record["uuid"], "text": text, "extra": extra})
            elif text.startswith(INTERRUPTED):
                items.append({"t": when(record), "seq": record["seq"], "role": "user", "kind": "interrupt",
                              "id": ids.claim(record["uuid"], "%s-interrupt" % record["uuid"]),
                              "text": text, "extra": {}})
        elif kind == "assistant":
            if record.get("model"):
                models.add(record["model"])
            for number, block in enumerate(record["blocks"]):
                if block["type"] == "text" and (block.get("text") or "").strip():
                    items.append({"t": when(record), "seq": record["seq"], "role": "assistant", "kind": "text",
                                  "id": ids.claim(record["uuid"], "%s-%d" % (record["uuid"], number)),
                                  "text": block["text"], "extra": {}})
                elif block["type"] == "tool_use" and block["name"] in RENDERED_TOOLS:
                    name, tool_input = block["name"], block.get("input") or {}
                    if name == "SendUserMessage":
                        text = tool_input.get("message")
                    elif name == "AskUserQuestion":
                        text = question_text(tool_input.get("questions"))
                    else:
                        text = tool_input.get("caption")
                    extra = {"rendered_from_tool": name, "rendering": RENDERING[name]}
                    if name == "SendUserFile":
                        files = [Path(f).name for f in tool_input.get("files", []) if isinstance(f, str)]
                        extra["files"] = files
                        delivered.extend("file card: %s" % f for f in files)
                    if not text:
                        continue
                    items.append({"t": when(record), "seq": record["seq"], "role": "assistant", "kind": "tool",
                                  "id": ids.claim(block.get("id"), "%s-%d" % (record["uuid"], number)),
                                  "text": text, "extra": extra})
        elif kind == "result":
            items.append({"t": epoch(record["created_at"]), "seq": record["seq"], "kind": "result",
                          "record": record})
        elif kind == "control_request" and record.get("subtype") == "interrupt":
            items.append({"t": epoch(record["created_at"]), "seq": record["seq"], "kind": "interrupt_request"})
    items.sort(key=lambda item: item["seq"])

    # Turns: a typed prompt opens one; a prompt sent before the open turn's closing
    # result joins it; the closing result is the first one that names the turn's
    # prompts, or (older sessions, where results name none) the first after output.
    turns, current = [], None
    for item in items:
        kind = item["kind"]
        if kind == "prompt":
            if current is not None and current["result"] is None:
                item["kind"] = "queued"
                item["extra"]["sent_while_reply_in_progress"] = True
                current["prompts"].append(item)
                item["turn"] = current["key"]
                continue
            current = {"key": item["uuid"], "start": item["t"], "prompts": [item], "result": None,
                       "output": False, "interrupted_at": None, "continued": False, "results": 0}
            turns.append(current)
            item["turn"] = current["key"]
        elif kind == "result":
            if current is None:
                continue
            record = item["record"]
            named = set(record.get("user_message_uuids") or [])
            own = {p["uuid"] for p in current["prompts"]}
            if named and not named & own:
                continue
            if not named and not current["output"] and record.get("subtype") == "success":
                continue
            if current["result"] is None:
                current["result"] = record
                current["result_t"] = item["t"]
                current["results"] += 1
        elif kind == "interrupt_request":
            if current is not None and current["interrupted_at"] is None:
                current["interrupted_at"] = item["t"]
        else:
            if current is None:
                current = {"key": "session-start", "start": item["t"], "prompts": [], "result": None,
                           "output": False, "interrupted_at": None, "continued": False, "results": 0}
                turns.append(current)
            if current["result"] is not None and item["role"] == "assistant":
                current["result"] = None
                current["continued"] = True
            if item["role"] == "assistant":
                current["output"] = True
            if kind == "interrupt" and current["interrupted_at"] is None:
                current["interrupted_at"] = item["t"]
            item["turn"] = current["key"]
    messages = [item for item in items if "turn" in item]
    if not any(item["kind"] == "prompt" for item in messages):
        raise SystemExit("Session %s has no typed prompt" % session_id)

    status_bucket = meta.get("status_bucket")
    turn_records = {}
    for index, turn in enumerate(turns):
        members = [m for m in messages if m["turn"] == turn["key"]]
        texts = [m for m in members if m["role"] == "assistant" and m["kind"] == "text"]
        result = turn["result"]
        record = {"started_at": iso(turn["start"])}
        if result is not None:
            aborted = result.get("subtype") != "success"
            if turn["interrupted_at"] is not None or str(result.get("terminal_reason") or "").startswith("aborted"):
                record = {"status": "interrupted", **record}
                if turn["interrupted_at"] is not None:
                    record["interrupted_at"] = iso(turn["interrupted_at"])
                record["ended_at"] = iso(turn["result_t"])
            elif aborted:
                record = {"status": "error", **record, "ended_at": iso(turn["result_t"]),
                          "result_subtype": result.get("subtype")}
            else:
                final = texts[-1] if texts else None
                if final:
                    final["phase"] = "final_answer"
                record = {"status": "completed", **record,
                          "completed_at": iso(final["t"] if final else turn["result_t"])}
        else:
            last = index == len(turns) - 1
            state = "no_result_recorded"
            if last and status_bucket == "blocked":
                state = "awaiting_permission_when_read"
            record = {"status": state, **record}
            if turn["interrupted_at"] is not None:
                record["interrupted_at"] = iso(turn["interrupted_at"])
        if len(turn["prompts"]) > 1:
            record["prompts_in_turn"] = len(turn["prompts"])
        if turn["continued"]:
            record["continued_after_result"] = True
        turn_records[turn["key"]] = record

    mapping = {"root": {"id": "root", "message": None, "parent": None, "children": []}}
    parent = "root"
    for item in messages:
        phase = item.get("phase") or ("commentary" if item["role"] == "assistant" else None)
        metadata = {"source": COWORK_SOURCE, "source_turn_id": item["turn"], "source_event_seq": item["seq"]}
        metadata.update(stamps(item["t"], item["t"]))
        if item["kind"] in ("queued", "interrupt", "answer"):
            metadata["kind"] = item["kind"]
        metadata.update(item["extra"])
        entry = node(item["id"], item["role"], item["t"], item["t"], item["text"], metadata, phase)
        entry["parent"] = parent
        mapping[item["id"]] = entry
        mapping[parent]["children"].append(item["id"])
        parent = item["id"]

    title = options.get("title") or meta.get("title")
    folders = [Path(str(f).rstrip("/")).name for f in meta.get("user_selected_folders") or []]
    configured = {"model": meta.get("model"), "reasoning_effort": meta.get("effort_level")}
    delivered = list(dict.fromkeys(delivered + list(options.get("delivered") or [])))
    script = Path(__file__).resolve()
    return {
        "title": title,
        "create_time": epoch(meta["created_at"]),
        "update_time": messages[-1]["t"],
        "mapping": mapping,
        "current_node": parent,
        "conversation_id": session_id,
        "id": session_id,
        "archive_metadata": {
            "format": FORMAT,
            "source_kind": "Claude Cowork cloud session event log (claude.ai GET /v1/code/sessions/{id}/events), "
                           "read in the signed-in browser and reduced to completed public messages",
            "message_timestamps": "Event times, in seconds since Unix epoch and ISO 8601: the session's own "
                                  "timestamp where the event carries one, otherwise the server's event time "
                                  "(typed messages); the conversation create_time is the session's creation "
                                  "time in the session list",
            "coverage": COWORK_COVERAGE,
            "omitted_record_types": OMITTED,
            "source_public_message_records": len(messages),
            "model_configurations": [configured] if configured["model"] else [],
            "serving_models_per_events": sorted(models),
            "turns": turn_records,
            "session": {
                "app": "Claude Cowork (cloud session)",
                "session_id": session_id,
                "claude_ai_session": meta.get("url") or "https://claude.ai/cowork/%s" % session_id,
                "title_source": "set at conversion; the session list shows %r" % meta.get("title")
                                if options.get("title") else "the session's title in the Cowork session list",
                "project": {"name": meta.get("project_name"), "uuid": meta.get("project_uuid"),
                            "chat_project_id": meta.get("chat_project_id"),
                            "chat_project_id_decodes_to_uuid": True},
                "created_at_utc": meta.get("created_at"),
                "last_event_at_utc": meta.get("last_event_at"),
                "status_bucket_when_read": status_bucket,
                "origin": meta.get("origin"),
                "permission_mode": meta.get("permission_mode"),
                "user_selected_folders": folders,
                "sdk_session_ids": session.get("sdk_session_ids", []),
            },
            "source_events": {
                "events_file": Path(path).name,
                "events_file_sha256": sha256(data),
                "events_read": session.get("events_read"),
                "event_pages": session.get("pages"),
                "first_sequence_num": session.get("first_seq"),
                "last_sequence_num": session.get("last_seq"),
                "sha256_of_events_json": session.get("sha256_of_events_json"),
                "events_json_bytes": session.get("events_json_bytes"),
                "event_counts": session.get("event_counts"),
                "subagent_messages_omitted": session.get("subagent_messages_omitted"),
                "reduced_session_sha256": sha256(canonical(session)),
                "read_by": doc.get("fetched_by"),
                "read_between_utc": [doc.get("started_at"), doc.get("finished_at")],
                "note": "sha256_of_events_json is the SHA-256 of JSON.stringify(events sorted by sequence_num) "
                        "computed in the browser; neither the event log nor the events file is stored in the "
                        "repository, since they hold instructions, reasoning and tool traffic that the coverage "
                        "rules exclude",
            },
            "delivered_files_not_embedded": delivered,
            "delivered_files_note": "Paths reported by device_commit_files and names of file cards; files "
                                    "written by shell commands or saved as project documents are not detected",
            "converter": {"script": script.name, "sha256": sha256(script.read_bytes())},
        },
    }


# ---------------------------------------------------------- claude.ai chats

CHAT_SOURCE = "claude.ai data export, completed public message"
CHAT_COVERAGE = (
    "Messages typed by the person, with the names of attached files; the assistant text shown in the "
    "chat, one message per text block: progress lines between tool calls (phase commentary) and the text "
    "ending each response (phase final_answer); the export's message tree, including any side branch "
    "left by an edited prompt")


def chat_conversation(export_path, conversation_id, options):
    data = Path(export_path).read_bytes()
    conversations = json.loads(data)
    chat = next((c for c in conversations if c.get("uuid") == conversation_id), None)
    if chat is None:
        raise SystemExit("Conversation %s is not in %s" % (conversation_id, export_path))
    messages = sorted(chat["chat_messages"], key=lambda m: m["created_at"])
    by_id = {m["uuid"]: m for m in messages}
    children = {}
    for message in messages:
        children.setdefault(message.get("parent_message_uuid"), []).append(message["uuid"])
    leaves = [m for m in messages if not children.get(m["uuid"])]
    leaf = max(leaves, key=lambda m: (m["created_at"], m["updated_at"]))
    current_path = set()
    walk = leaf
    while walk is not None:
        current_path.add(walk["uuid"])
        walk = by_id.get(walk.get("parent_message_uuid"))

    ids = Ids()
    mapping = {"root": {"id": "root", "message": None, "parent": None, "children": []}}
    last_node, turns, delivered, block_counts = {}, {}, [], {}
    for message in messages:
        for block in message.get("content") or []:
            block_counts[block.get("type")] = block_counts.get(block.get("type"), 0) + 1
    for message in messages:
        parent_message = message.get("parent_message_uuid")
        parent = "root"
        walk = parent_message
        while walk and walk not in last_node and walk in by_id:
            walk = by_id[walk].get("parent_message_uuid")
        if walk in last_node:
            parent = last_node[walk]
        blocks = message.get("content") or []
        branch = "current" if message["uuid"] in current_path else "side"
        if message["sender"] == "human":
            text = "\n\n".join(b.get("text") or "" for b in blocks if b.get("type") == "text").strip()
            if not text:
                text = (message.get("text") or "").strip()
            names = [a.get("file_name") for a in message.get("attachments") or [] if a.get("file_name")]
            names += [f.get("file_name") for f in message.get("files") or [] if f.get("file_name")]
            extra = {"branch": branch}
            if names:
                extra["attachments"] = list(dict.fromkeys(names))
            created = epoch(message["created_at"])
            ident = ids.claim(message["uuid"], "%s-prompt" % message["uuid"])
            entry = node(ident, "user", created, created, text,
                         {"source": CHAT_SOURCE, "source_turn_id": message["uuid"], **stamps(created, created),
                          **extra})
            entry["parent"] = parent
            mapping[ident] = entry
            mapping[parent]["children"].append(ident)
            last_node[message["uuid"]] = ident
            turns[message["uuid"]] = {"started_at": iso(created), "status": "no_response_recorded", "branch": branch}
            continue
        visible = [(n, b) for n, b in enumerate(blocks) if b.get("type") not in ("token_budget",)]
        closing = visible[-1][1] if visible else None
        ends_on_text = bool(closing and closing.get("type") == "text" and (closing.get("text") or "").strip())
        texts = [(n, b) for n, b in enumerate(blocks) if b.get("type") == "text" and (b.get("text") or "").strip()]
        for block in blocks:
            if block.get("type") == "tool_use" and block.get("name") == "present_files":
                for path in (block.get("input") or {}).get("filepaths", []) or []:
                    delivered.append("file card: %s" % Path(path).name)
        for position, (n, block) in enumerate(texts):
            final = ends_on_text and position == len(texts) - 1
            start = epoch(block.get("start_timestamp") or message["created_at"])
            stop = epoch(block.get("stop_timestamp") or message["updated_at"])
            ident = ids.claim(message["uuid"] if position == 0 else None, "%s-%d" % (message["uuid"], n))
            entry = node(ident, "assistant", start, stop, block["text"],
                         {"source": CHAT_SOURCE, "source_turn_id": parent_message, "branch": branch,
                          **stamps(start, stop)},
                         "final_answer" if final else "commentary")
            entry["parent"] = parent
            mapping[ident] = entry
            mapping[parent]["children"].append(ident)
            parent = ident
        last_node[message["uuid"]] = parent
        turn = turns.get(parent_message)
        if turn is not None:
            turn["status"] = "response_ends_with_text" if ends_on_text else "response_ends_without_text"
            turn["completed_at"] = iso(epoch(message["updated_at"]))
            turn["closing_block"] = closing.get("type") if closing else None
    current_node = last_node[leaf["uuid"]]
    created = [mapping[k]["message"]["update_time"] for k in mapping if mapping[k]["message"]]
    script = Path(__file__).resolve()
    selected = canonical(chat)
    return {
        "title": options.get("title") or chat.get("name"),
        "create_time": epoch(chat["created_at"]),
        "update_time": max(created),
        "mapping": mapping,
        "current_node": current_node,
        "conversation_id": chat["uuid"],
        "id": chat["uuid"],
        "archive_metadata": {
            "format": FORMAT,
            "source_kind": "claude.ai chat from the account data export (conversations.json), public text messages",
            "message_timestamps": "Export times, in seconds since Unix epoch and ISO 8601: a typed message carries "
                                  "its message time and an assistant text block the start and stop times of that "
                                  "block; the conversation create_time is the export's created_at",
            "coverage": CHAT_COVERAGE,
            "omitted_record_types": [
                "platform-injected prompt blocks (date notes, memory snapshots)",
                "internal reasoning (thinking blocks)",
                "tool calls and outputs (code execution, file creation, web search and fetch, project knowledge "
                "search); the names of files presented as file cards are kept",
                "token-budget markers",
                "attachment contents (file names are kept in message metadata)",
                "the message-level text field, which flattens tool blocks into placeholder lines; the content "
                "blocks are used instead",
            ],
            "source_public_message_records": sum(1 for v in mapping.values() if v["message"]),
            "model_configurations": [{"model": options.get("model"), "reasoning_effort": None}]
                                    if options.get("model") else [],
            "turns": turns,
            "session": {
                "app": "Claude (claude.ai chat)",
                "conversation_uuid": chat["uuid"],
                "claude_ai_url": "https://claude.ai/chat/%s" % chat["uuid"],
                "title_source": "set at conversion" if options.get("title") else "the export's conversation name",
                "project": {"name": options.get("project_name"), "uuid": options.get("project_uuid")},
                "model_source": "claude.ai project chat list (conversations_v2); the export records no model or "
                                "reasoning effort",
                "platform": options.get("platform"),
                "branches": "current_node ends the most recent branch; nodes marked branch=side belong to a reply "
                            "left behind by an edited prompt",
                "turn_status_note": "The export records no stop or interruption markers; a turn status says only "
                                    "whether the recorded response ends with visible text",
            },
            "source_export": {
                "file": Path(export_path).name,
                "file_bytes": len(data),
                "file_sha256": sha256(data),
                "conversation_sha256": sha256(selected),
                "chat_messages": len(messages),
                "content_block_counts": block_counts,
                "note": "conversation_sha256 is the SHA-256 of the exported conversation object serialized with "
                        "sorted keys and compact separators; the export is not stored in the repository",
            },
            "delivered_files_not_embedded": list(dict.fromkeys(delivered + list(options.get("delivered") or []))),
            "converter": {"script": script.name, "sha256": sha256(script.read_bytes())},
        },
    }


# ----------------------------------------------------------------- commands

def register(conversation, args):
    text = (json.dumps(conversation, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if args.output:
        Path(args.output).write_bytes(text)
        note("wrote %s  sha256 %s  (%d bytes)" % (args.output, sha256(text), len(text)))
    if args.dry_run:
        return
    if not args.folder:
        raise SystemExit("--folder is required unless --dry-run is given")
    recorder = Path(args.recorder).resolve() if args.recorder else DEFAULT_RECORDER
    with tempfile.TemporaryDirectory(prefix="claude-export-") as folder:
        path = Path(folder) / "conversation.json"
        path.write_bytes(text)
        command = [sys.executable, str(recorder), "--import-json", str(path),
                   "--folder", str(Path(args.folder).resolve())]
        if args.allow_shorter_refresh:
            command.append("--allow-shorter-refresh")
        result = subprocess.run(command)
    if result.returncode:
        raise SystemExit(result.returncode)


def cmd_list(args):
    doc, _ = load_events(args.events)
    for session in sorted(doc["sessions"], key=lambda s: s["session"]["created_at"]):
        meta = session["session"]
        prompts = sum(1 for r in session["records"] if r["type"] == "user" and r.get("source") == "client"
                      and r.get("shouldQuery") is not False
                      and any((b.get("text") or "").strip() for b in r["blocks"] if b["type"] == "text"))
        print("%s  %-18s %-6s %-30s %3d prompts  %s" % (
            meta["created_at"][:16], meta["project_name"], meta.get("effort_level") or "",
            meta["id"], prompts, meta["title"]))


def cmd_cowork(args):
    doc, data = load_events(args.events)
    conversation = cowork_conversation(doc, data, args.events, args.session_id,
                                       {"title": args.title, "delivered": args.delivered})
    register(conversation, args)


def cmd_chat(args):
    conversation = chat_conversation(args.export, args.conversation_id, {
        "title": args.title, "delivered": args.delivered, "project_name": args.project_name,
        "project_uuid": args.project_uuid, "model": args.model, "platform": args.platform})
    register(conversation, args)


def cmd_readme_stub(args):
    folder = Path(args.folder)
    index = json.loads((folder / "index.json").read_text(encoding="utf-8"))
    entries = index["chats"] if args.number is None else [e for e in index["chats"] if e["number"] == args.number]
    for entry in entries:
        conversation = json.loads((folder / entry["file"]).read_text(encoding="utf-8"))[0]
        meta = conversation.get("archive_metadata", {})
        session = meta.get("session", {})
        project = (session.get("project") or {}).get("name")
        config = (entry.get("model_configurations") or [{}])[0]
        started = datetime.fromisoformat(entry["created_at_local"])
        turns = meta.get("turns", {})
        statuses = {}
        for turn in turns.values():
            statuses[turn.get("status")] = statuses.get(turn.get("status"), 0) + 1
        nodes = [n["message"] for n in conversation["mapping"].values() if n.get("message")]
        prompts = [m for m in nodes if m["author"]["role"] == "user" and not m["metadata"].get("kind")]
        opening = re.sub(r"\s+", " ", prompts[0]["content"]["parts"][0]).strip() if prompts else ""
        if len(opening) > 220:
            opening = opening[:217].rsplit(" ", 1)[0] + " …"
        app = "Claude Cowork cloud session" if session.get("app", "").startswith("Claude Cowork") else "claude.ai chat"
        effort = config.get("reasoning_effort")
        model = "%s (`%s`%s)" % (model_name(config.get("model")), config.get("model"),
                                 ", reasoning effort %s" % effort if effort else "")
        status_text = ", ".join("%d %s" % (n, s.replace("_", " ")) for s, n in sorted(statuses.items()))
        print("%d. **%s** — [%s](%s)" % (entry["number"], entry["title"], entry["file"], entry["file"].replace(" ", "%20")))
        bullets = [
            "*Session.* A %s in project %s with %s, started %d %s %d at %s America/New_York."
            % (app, project, model, started.day, started.strftime("%B"), started.year, started.strftime("%H:%M")),
            "*Record.* %d messages over %d turns (%s). Opening request: “%s”"
            % (entry["message_count"], len(turns), status_text, opening),
        ]
        for bullet in bullets:
            print(textwrap.fill("- " + bullet, width=78, initial_indent="   ", subsequent_indent="     ",
                                break_on_hyphens=False, break_long_words=False))
        print()


def cmd_extractor(args):
    print(EXTRACTOR_JS)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    def output_options(p):
        p.add_argument("--folder", help="Chat-history registry folder to register into")
        p.add_argument("--recorder", help="record_chat.py to use (default: %s)" % DEFAULT_RECORDER.relative_to(ROOT))
        p.add_argument("--title", help="Override the recorded title")
        p.add_argument("--delivered", action="append", metavar="PATH", help="Delivered file not detected automatically")
        p.add_argument("--output", help="Also write the converted conversation here")
        p.add_argument("--dry-run", action="store_true", help="Convert only; do not register")
        p.add_argument("--allow-shorter-refresh", action="store_true")

    p = sub.add_parser("list", help="List the sessions in a session-events file")
    p.add_argument("--events", required=True)
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("cowork", help="Convert and register a Cowork session from a session-events file")
    p.add_argument("--events", required=True)
    p.add_argument("--session-id", required=True)
    output_options(p)
    p.set_defaults(func=cmd_cowork)

    p = sub.add_parser("chat", help="Convert and register a claude.ai chat from the account data export")
    p.add_argument("--export", required=True, help="conversations.json from the account data export")
    p.add_argument("--conversation-id", required=True)
    p.add_argument("--project-name")
    p.add_argument("--project-uuid")
    p.add_argument("--model", help="Model from the project chat list")
    p.add_argument("--platform", default="CLAUDE_AI")
    output_options(p)
    p.set_defaults(func=cmd_chat)

    p = sub.add_parser("readme-stub", help="Draft guide entries for a registry folder")
    p.add_argument("--folder", required=True)
    p.add_argument("--number", type=int)
    p.set_defaults(func=cmd_readme_stub)

    p = sub.add_parser("extractor", help="Print the browser extractor used for session-events files")
    p.set_defaults(func=cmd_extractor)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
