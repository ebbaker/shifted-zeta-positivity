#!/usr/bin/env python3
"""Save a visible chat or import conversations without changing existing numbers."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

UTC = timezone.utc
LOCAL = ZoneInfo("America/New_York")
MAX_BYTES = 1024 * 1024


def iso(value):
    return datetime.fromtimestamp(value, UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def epoch(value):
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if parsed.tzinfo is None:
        raise ValueError("ISO timestamp must include Z or an explicit UTC offset")
    return parsed.timestamp()


def codex_chat(path, title, thread_id, created_at):
    mapping = {"root": {"id": "root", "message": None, "parent": None, "children": []}}
    parent = "root"
    turns = {}
    configurations = []
    source_count = 0
    for line in path.open(encoding="utf-8"):
        row = json.loads(line)
        payload = row.get("payload", {})
        if row.get("type") == "turn_context":
            config = {"model": payload.get("model"), "reasoning_effort": payload.get("effort")}
            if config not in configurations:
                configurations.append(config)
        if row.get("type") != "event_msg":
            continue
        kind = payload.get("type")
        if kind == "task_started":
            turns[payload["turn_id"]] = {"status": "in_progress", "started_at": payload.get("started_at")}
        elif kind == "task_complete":
            turns.setdefault(payload["turn_id"], {}).update(status="completed", completed_at=payload.get("completed_at"))
        if kind != "item_completed" or payload.get("thread_id") != thread_id:
            continue
        item = payload.get("item", {})
        if item.get("type") not in ("UserMessage", "AgentMessage"):
            continue
        source_count += 1
        message_id = item["id"]
        if message_id in mapping:
            continue
        parts = []
        for part in item.get("content", []):
            if part.get("type", "").lower() != "text":
                raise ValueError("Non-text public content needs an explicit attachment-preserving exporter")
            parts.append(part["text"])
        started = payload.get("started_at_ms")
        completed = payload.get("completed_at_ms")
        created = started / 1000 if started is not None else epoch(row["timestamp"])
        updated = completed / 1000 if completed is not None else epoch(row["timestamp"])
        role = "user" if item["type"] == "UserMessage" else "assistant"
        mapping[message_id] = {
            "id": message_id,
            "message": {
                "id": message_id,
                "author": {"role": role, "name": None, "metadata": {}},
                "create_time": created,
                "update_time": updated,
                "content": {"content_type": "text", "parts": parts},
                "status": "finished_successfully",
                "end_turn": item.get("phase") == "final_answer" if role == "assistant" else None,
                "metadata": {
                    "source": "Codex completed public message",
                    "source_turn_id": payload["turn_id"],
                    "phase": item.get("phase"),
                    "created_at_utc": iso(created),
                    "completed_at_utc": iso(updated),
                    "created_at_local": datetime.fromtimestamp(created, LOCAL).isoformat(timespec="milliseconds"),
                },
                "recipient": "all",
            },
            "parent": parent,
            "children": [],
        }
        mapping[parent]["children"].append(message_id)
        parent = message_id
    if parent == "root":
        raise ValueError("No completed public messages found for this thread")
    latest = mapping[parent]["message"]["update_time"]
    return {
        "title": title,
        "create_time": epoch(created_at),
        "update_time": latest,
        "mapping": mapping,
        "current_node": parent,
        "conversation_id": thread_id,
        "id": thread_id,
        "archive_metadata": {
            "format": "ChatGPT-style conversation mapping; local conversion, not an official provider export",
            "source_kind": "Codex local session completed public messages",
            "message_timestamps": "Recorded source start/completion times, in seconds since Unix epoch and ISO 8601",
            "coverage": "All completed user and assistant text messages recorded through capture, including commentary; current response may still be in progress",
            "omitted_record_types": ["system and developer instructions", "internal reasoning", "tool calls and outputs", "subagent messages", "binary and runtime state"],
            "source_public_message_records": source_count,
            "model_configurations": configurations,
            "turns": turns,
        },
    }


def save_chat(folder, conversation, captured, allow_shorter_refresh=False):
    index_path = folder / "index.json"
    index = json.loads(index_path.read_text()) if index_path.exists() else {
        "schema_version": 1,
        "timezone": "America/New_York",
        "numbering": "Stable capture/import order within this folder; historical imports retain their original dates and receive the next unused number",
        "next_number": 1,
        "chats": [],
    }
    chat_id = conversation.get("conversation_id") or conversation.get("id")
    if not chat_id or not isinstance(conversation.get("mapping"), dict):
        raise ValueError("Expected a conversation id and ChatGPT-style mapping")
    created = conversation.get("create_time")
    if not isinstance(created, (int, float)):
        raise ValueError("Expected a numeric original conversation create_time")
    existing = next((entry for entry in index["chats"] if entry["conversation_id"] == chat_id), None)
    number = existing["number"] if existing else index["next_number"]
    if existing:
        filename = existing["file"]
        previous = folder / filename
        if hashlib.sha256(previous.read_bytes()).hexdigest() != existing["sha256"]:
            raise ValueError("Existing chat changed outside the registry; inspect it before refreshing")
        message_count = sum(node.get("message") is not None for node in conversation["mapping"].values())
        latest = conversation.get("update_time")
        previous_latest = existing.get("last_message_at_utc")
        shorter = message_count < existing["message_count"]
        older = isinstance(latest, (int, float)) and previous_latest and latest < epoch(previous_latest)
        if (shorter or older) and not allow_shorter_refresh:
            raise ValueError("Refusing a shorter or older refresh; inspect the import and use --allow-shorter-refresh only for an intentional replacement")
    else:
        slug = re.sub(r"[^a-z0-9]+", "-", conversation.get("title", "chat").lower()).strip("-")[:80] or "chat"
        stamp = datetime.fromtimestamp(created, UTC).strftime("%Y-%m-%dT%H-%M-%SZ")
        filename = f"{number:04d}_{stamp}_{slug}.json"
        if (folder / filename).exists():
            raise ValueError("Refusing to replace an unregistered chat")
    metadata = conversation.setdefault("archive_metadata", {})
    metadata.update(history_number=number, captured_at_utc=iso(captured), captured_at_local=datetime.fromtimestamp(captured, LOCAL).isoformat(timespec="milliseconds"))
    data = (json.dumps([conversation], ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    if len(data) >= MAX_BYTES:
        raise ValueError("Chat exceeds the repository's small-file limit; archive it externally with a small hash record")
    canonical = json.dumps({key: value for key, value in conversation.items() if key != "archive_metadata"},
                           ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    entry = {
        "number": number, "file": filename, "conversation_id": chat_id,
        "title": conversation.get("title"), "created_at_utc": iso(created),
        "created_at_local": datetime.fromtimestamp(created, LOCAL).isoformat(timespec="milliseconds"),
        "captured_at_utc": iso(captured), "captured_at_local": datetime.fromtimestamp(captured, LOCAL).isoformat(timespec="milliseconds"),
        "last_message_at_utc": iso(conversation["update_time"]) if isinstance(conversation.get("update_time"), (int, float)) else None,
        "message_count": sum(node.get("message") is not None for node in conversation["mapping"].values()),
        "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
        "conversation_content_sha256": hashlib.sha256(canonical).hexdigest(),
        "model_configurations": metadata.get("model_configurations", []),
    }
    if existing:
        index["chats"][index["chats"].index(existing)] = entry
    else:
        index["chats"].append(entry)
        index["next_number"] = number + 1
    folder.mkdir(parents=True, exist_ok=True)
    target = folder / filename
    temporary = target.with_suffix(".json.tmp")
    temporary.write_bytes(data)
    temporary.replace(target)
    index_tmp = index_path.with_suffix(".json.tmp")
    index_tmp.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n")
    index_tmp.replace(index_path)
    print(json.dumps({"number": number, "file": filename, "messages": entry["message_count"], "next_number": index["next_number"]}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument("--codex-rollout", type=Path)
    source.add_argument("--import-json", type=Path)
    parser.add_argument("--thread-id")
    parser.add_argument("--title")
    parser.add_argument("--created-at", help="Original thread creation time, ISO 8601 with timezone")
    parser.add_argument("--conversation-id", help="For a multi-chat data export, import only this id")
    parser.add_argument("--allow-shorter-refresh", action="store_true", help="Explicitly permit replacing an existing chat with a shorter or older source")
    parser.add_argument("--folder", type=Path, default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    captured = datetime.now(UTC).timestamp()
    if args.codex_rollout:
        if not all((args.thread_id, args.title, args.created_at)):
            parser.error("Codex capture requires --thread-id, --title, and --created-at")
        conversations = [codex_chat(args.codex_rollout, args.title, args.thread_id, args.created_at)]
    else:
        data = json.loads(args.import_json.read_text(encoding="utf-8"))
        conversations = data if isinstance(data, list) else [data]
        if args.conversation_id:
            conversations = [chat for chat in conversations if (chat.get("conversation_id") or chat.get("id")) == args.conversation_id]
            if not conversations:
                parser.error("Requested conversation id was not found")
        for chat in conversations:
            chat.setdefault("archive_metadata", {}).setdefault("source_kind", "Imported JSON export; original conversation fields preserved")
    for conversation in conversations:
        save_chat(args.folder, conversation, captured, args.allow_shorter_refresh)


if __name__ == "__main__":
    main()
