#!/usr/bin/env python3
"""Refresh an opted-in, public-text Codex chat archive without rewriting its past."""
from __future__ import annotations

import argparse
import contextlib
from dataclasses import dataclass
from datetime import datetime, timezone
import fcntl
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import tempfile
import time
import types

MAX_BYTES = 1024 * 1024
LOCK_NAME = ".chat-history-refresh.lock"
TRANSACTION_NAME = ".chat-history-transaction"
TRANSACTION_FILES = {"journal.json", "old_chat", "old_index", "new_chat", "new_index", "restore_chat", "restore_index"}
PUBLIC_PHASES = {"commentary", "final_answer"}
PRIVATE_PHASES = {"analysis", "reasoning", "summary"}
INTERRUPTED_EVENTS = {"turn_aborted", "task_aborted", "task_interrupted", "task_cancelled", "task_canceled"}
_FAULT_POINT = None  # Synthetic transaction fault injection; never set by the CLI.


class HistoryError(RuntimeError):
    """A failed integrity or source check; do not replace a registered capture."""


class SourcePending(HistoryError):
    """The source has not yet flushed a complete requested snapshot."""


@dataclass
class SourceSnapshot:
    conversation: dict
    completed_turns: set[str]
    interrupted_turns: set[str]
    final_turns: set[str]


def sha(data):
    return hashlib.sha256(data).hexdigest()


def json_bytes(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def load_recorder(repo):
    path = repo / "papers/investigations-2/record_chat.py"
    if not path.is_file() or path.is_symlink():
        raise HistoryError("The repository's existing chat recorder is missing or a symbolic link")
    module = types.ModuleType("_public_chat_recorder")
    module.__file__ = str(path)
    exec(compile(path.read_text(encoding="utf-8"), str(path), "exec"), module.__dict__)
    return module


def safe_directory(repo, relative):
    path = Path(relative)
    if path.is_absolute() or not path.parts or any(p in {".", ".."} for p in path.parts):
        raise HistoryError("--history-dir must be a repository-relative history directory")
    target = repo / path
    if target.name not in {"chat-histories", "chat_histories"}:
        raise HistoryError("--history-dir must name a chat-histories or chat_histories directory")
    current = repo
    for part in path.parts:
        current = current / part
        if current.is_symlink():
            raise HistoryError("History paths must not contain symbolic links")
    if not target.parent.is_dir():
        raise HistoryError("The history's parent directory must already exist")
    if target.exists() and not target.is_dir():
        raise HistoryError("The history destination is not a directory")
    if not target.resolve().is_relative_to(repo):
        raise HistoryError("The history destination leaves the repository")
    return target


def validate_filename(filename):
    if not isinstance(filename, str) or not re.fullmatch(r"[0-9]{4,}_[A-Za-z0-9_.-]+\.json", filename):
        raise HistoryError("Registered chat filenames must be numbered JSON basenames")
    if Path(filename).name != filename or filename in {".", ".."}:
        raise HistoryError("A registered filename leaves the history directory")


def validate_index(folder, index):
    if not isinstance(index, dict) or not isinstance(index.get("chats"), list):
        raise HistoryError("Malformed history index")
    ids, files = set(), set()
    for entry in index["chats"]:
        if not isinstance(entry, dict):
            raise HistoryError("Malformed registered chat entry")
        ident, filename, number = entry.get("conversation_id"), entry.get("file"), entry.get("number")
        if not isinstance(ident, str) or not ident or ident in ids:
            raise HistoryError("Duplicate or missing conversation id in history index")
        validate_filename(filename)
        if filename in files:
            raise HistoryError("Duplicate registered filename in history index")
        if not isinstance(number, int) or isinstance(number, bool) or number < 1:
            raise HistoryError("Invalid registered chat number")
        if int(filename.split("_", 1)[0]) != number:
            raise HistoryError("Registered number disagrees with its filename")
        if (folder / filename).is_symlink():
            raise HistoryError("A registered chat is a symbolic link")
        if not isinstance(entry.get("sha256"), str) or not re.fullmatch(r"[0-9a-f]{64}", entry["sha256"]):
            raise HistoryError("Missing registered chat hash")
        ids.add(ident)
        files.add(filename)
    # Existing merged histories can contain duplicate numbers, but never duplicate IDs/files.
    value = index.get("next_number", 1)
    if not isinstance(value, int) or isinstance(value, bool) or value < 1:
        raise HistoryError("Invalid next-number registry value")
    return index


def read_index(folder):
    path = folder / "index.json"
    if path.is_symlink():
        raise HistoryError("The history index is a symbolic link")
    if not path.exists():
        return {"schema_version": 1, "timezone": "America/New_York", "numbering": "Stable capture/import order within this folder; historical imports retain their original dates and receive the next unused number", "next_number": 1, "chats": []}
    if not path.is_file() or path.stat().st_size >= MAX_BYTES:
        raise HistoryError("The history index is not a small regular file")
    try:
        return validate_index(folder, json.loads(path.read_text(encoding="utf-8")))
    except (ValueError, OSError) as exc:
        raise HistoryError("Cannot read a valid history index") from exc


def find_registered(repo, thread_id, preferred=None):
    matches = []
    papers = repo / "papers"
    if not papers.is_dir():
        raise HistoryError("The repository has no papers directory")
    for path in papers.rglob("index.json"):
        if path.parent.name not in {"chat-histories", "chat_histories"}:
            continue
        folder = safe_directory(repo, str(path.parent.relative_to(repo)))
        index = read_index(folder)
        if any(e["conversation_id"] == thread_id for e in index["chats"]):
            matches.append(folder)
    if preferred is not None and preferred in matches:
        return preferred
    if len(matches) > 1:
        raise HistoryError("The conversation is registered in multiple history directories; resolve the ambiguity explicitly")
    return matches[0] if matches else None


def resolve_rollout(thread_id, supplied=None):
    if supplied is not None:
        path = Path(supplied).expanduser()
        if not path.is_file() or path.is_symlink():
            raise HistoryError("The supplied rollout is not a regular session file")
        return path.resolve()
    sessions = Path(os.environ.get("CODEX_HOME", str(Path.home() / ".codex"))) / "sessions"
    candidates = [p for p in sessions.rglob("*.jsonl") if (p.stem == thread_id or p.name.endswith("-" + thread_id + ".jsonl")) and p.is_file() and not p.is_symlink()]
    if len(candidates) != 1:
        raise HistoryError("Expected one exact-id Codex session file; supply --rollout if discovery is absent or ambiguous")
    return candidates[0].resolve()


def read_public_source(path, thread_id, title, recorder):
    safe_rows, seen = [], {}
    completed, interrupted, finals = set(), set(), set()
    session_seen = False
    created_at = None
    try:
        with Path(path).open("rb") as stream:
            for raw in stream:
                if not raw.endswith(b"\n"):
                    raise SourcePending("The session has an unfinished trailing row; waiting for its real flush")
                try:
                    row = json.loads(raw)
                except (ValueError, UnicodeError) as exc:
                    raise HistoryError("Malformed completed JSONL row in the session") from exc
                if not isinstance(row, dict) or not isinstance(row.get("payload", {}), dict):
                    raise HistoryError("Malformed session row structure")
                payload = row.get("payload", {})
                kind = row.get("type")
                if kind == "session_meta":
                    if payload.get("id") != thread_id:
                        raise HistoryError("The rollout's exact session id does not match the requested chat")
                    stamp = payload.get("timestamp") or row.get("timestamp")
                    if not isinstance(stamp, str):
                        raise HistoryError("The session has no recorded original creation timestamp")
                    if session_seen and stamp != created_at:
                        raise HistoryError("Conflicting session creation metadata")
                    session_seen, created_at = True, stamp
                    safe_rows.append({"type": "session_meta", "timestamp": row.get("timestamp"), "payload": {"id": thread_id}})
                    continue
                if payload.get("thread_id") not in (None, thread_id):
                    continue
                if kind == "turn_context":
                    if any(payload.get(key) is not None and not isinstance(payload.get(key), str) for key in ("model", "effort")):
                        raise HistoryError("Session model and effort provenance must be simple names")
                    safe_rows.append({"type": kind, "timestamp": row.get("timestamp"), "payload": {"model": payload.get("model"), "effort": payload.get("effort")}})
                    continue
                if kind != "event_msg":
                    continue
                event = payload.get("type")
                turn = payload.get("turn_id")
                if event in INTERRUPTED_EVENTS or (event == "task_complete" and payload.get("status") in {"interrupted", "cancelled", "canceled", "aborted"}):
                    if isinstance(turn, str):
                        interrupted.add(turn)
                    continue
                if event in {"task_started", "task_complete"}:
                    if not isinstance(turn, str):
                        raise HistoryError("A turn event has no exact turn id")
                    if event == "task_complete":
                        completed.add(turn)
                    safe_payload = {"type": event, "thread_id": thread_id, "turn_id": turn}
                    for key in ("started_at", "completed_at"):
                        if key in payload:
                            value = payload[key]
                            if value is not None and (not isinstance(value, (str, int, float)) or isinstance(value, bool) or (isinstance(value, (int, float)) and not math.isfinite(value))):
                                raise HistoryError("Invalid turn timestamp provenance")
                            safe_payload[key] = payload[key]
                    safe_rows.append({"type": kind, "timestamp": row.get("timestamp"), "payload": safe_payload})
                    continue
                if event != "item_completed" or payload.get("thread_id") != thread_id:
                    continue
                item = payload.get("item", {})
                if not isinstance(item, dict) or item.get("type") not in {"UserMessage", "AgentMessage"}:
                    continue
                if item["type"] == "AgentMessage":
                    phase = item.get("phase")
                    if phase in PRIVATE_PHASES:
                        continue
                    if phase not in PUBLIC_PHASES:
                        raise HistoryError("An assistant message has an unknown public phase; refusing to export it")
                ident = item.get("id")
                if not isinstance(ident, str) or not ident or ident == "root" or not isinstance(turn, str):
                    raise HistoryError("A public message lacks a valid message or turn id")
                content = item.get("content")
                if not isinstance(content, list):
                    raise HistoryError("Malformed public message content")
                parts = []
                for part in content:
                    if not isinstance(part, dict) or str(part.get("type", "")).lower() != "text" or not isinstance(part.get("text"), str):
                        raise HistoryError("Non-text public content requires an attachment-preserving exporter")
                    parts.append({"type": "text", "text": part["text"]})
                safe_item = {"type": item["type"], "id": ident, "content": parts}
                if "phase" in item:
                    safe_item["phase"] = item["phase"]
                safe_payload = {"type": event, "thread_id": thread_id, "turn_id": turn, "item": safe_item}
                for key in ("started_at_ms", "completed_at_ms"):
                    if key in payload:
                        val = payload[key]
                        if val is not None and (not isinstance(val, (int, float)) or isinstance(val, bool) or not math.isfinite(val)):
                            raise HistoryError("Invalid public message timestamp")
                        safe_payload[key] = val
                safe_row = {"type": "event_msg", "timestamp": row.get("timestamp"), "payload": safe_payload}
                try:
                    start = safe_payload.get("started_at_ms")
                    end = safe_payload.get("completed_at_ms")
                    created = start / 1000 if start is not None else recorder.epoch(row["timestamp"])
                    updated = end / 1000 if end is not None else recorder.epoch(row["timestamp"])
                except (ValueError, KeyError, TypeError, OverflowError) as exc:
                    raise HistoryError("Invalid completed public message times") from exc
                if created > updated:
                    raise HistoryError("A public message starts after its own completion")
                signature = json.dumps({"item": safe_item, "turn_id": turn, "create_time": created, "update_time": updated}, sort_keys=True, ensure_ascii=False)
                if ident in seen:
                    if seen[ident] != signature:
                        raise HistoryError("Conflicting duplicate completed public message id")
                    continue
                seen[ident] = signature
                safe_rows.append(safe_row)
                if item["type"] == "AgentMessage" and item.get("phase") == "final_answer":
                    finals.add(turn)
    except OSError as exc:
        raise HistoryError("Cannot read the requested session file") from exc
    if not session_seen:
        raise HistoryError("The session has no exact session_meta identity")
    if not seen:
        raise SourcePending("No completed public messages have been flushed yet")
    # Only whitelisted public text and safe provenance enter this temporary adapter input.
    with tempfile.TemporaryDirectory(prefix="public-chat-refresh-") as temp:
        filtered = Path(temp) / "public.jsonl"
        filtered.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in safe_rows), encoding="utf-8")
        try:
            conversation = recorder.codex_chat(filtered, title, thread_id, created_at)
        except (ValueError, KeyError, TypeError, OverflowError) as exc:
            raise HistoryError("The public source cannot be converted by the existing recorder") from exc
    return SourceSnapshot(conversation, completed, interrupted, finals)


def ordered_messages(conversation):
    mapping = conversation.get("mapping")
    if not isinstance(mapping, dict) or "root" not in mapping:
        raise HistoryError("The registered capture is not a linear Codex conversation")
    node, visited, result = "root", set(), []
    while True:
        if node in visited or node not in mapping or not isinstance(mapping[node], dict):
            raise HistoryError("Malformed or cyclic archived conversation mapping")
        visited.add(node)
        record = mapping[node]
        message = record.get("message")
        if node == "root":
            if message is not None or record.get("parent") is not None:
                raise HistoryError("Malformed archive root")
        else:
            if not isinstance(message, dict) or message.get("id") != node:
                raise HistoryError("Malformed archived public message")
            role = message.get("author", {}).get("role")
            if role not in {"user", "assistant"}:
                raise HistoryError("The registered capture contains a non-public author")
            if role == "assistant" and message.get("metadata", {}).get("phase") not in PUBLIC_PHASES:
                raise HistoryError("The registered capture has an unsupported assistant phase")
            content = message.get("content", {})
            if content.get("content_type") != "text" or not isinstance(content.get("parts"), list) or not all(isinstance(p, str) for p in content["parts"]):
                raise HistoryError("The registered capture contains unsupported public content")
            for field in ("create_time", "update_time"):
                if not isinstance(message.get(field), (int, float)) or not math.isfinite(message[field]):
                    raise HistoryError("Malformed archived public message times")
            if message["create_time"] > message["update_time"]:
                raise HistoryError("An archived message starts after its own completion")
            result.append(message)
        children = record.get("children")
        if not isinstance(children, list) or len(children) > 1:
            raise HistoryError("Automatic refresh requires one linear public-message branch")
        if not children:
            if conversation.get("current_node") != node:
                raise HistoryError("The archive's current node is inconsistent")
            break
        child = children[0]
        if child not in mapping or mapping[child].get("parent") != node:
            raise HistoryError("The archive's parent/child links are inconsistent")
        node = child
    if visited != set(mapping):
        raise HistoryError("The registered capture has orphaned conversation nodes")
    return result


def public_signature(message):
    # Ignore newly added child links, but preserve every field of the completed message itself.
    return json.dumps(message, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def read_registered(folder, entry):
    path = folder / entry["file"]
    if path.is_symlink() or not path.is_file() or path.stat().st_size >= MAX_BYTES:
        raise HistoryError("The registered capture is not a small regular file")
    data = path.read_bytes()
    if sha(data) != entry["sha256"] or ("bytes" in entry and entry["bytes"] != len(data)):
        raise HistoryError("Existing capture changed outside its hash registry")
    try:
        values = json.loads(data)
    except ValueError as exc:
        raise HistoryError("Malformed registered capture JSON") from exc
    if not isinstance(values, list) or len(values) != 1 or not isinstance(values[0], dict):
        raise HistoryError("Expected one registered conversation")
    conversation = values[0]
    if conversation.get("conversation_id") != entry["conversation_id"] or conversation.get("id") != entry["conversation_id"]:
        raise HistoryError("Registered capture id does not match its index")
    ordered_messages(conversation)
    canonical = json.dumps({k: v for k, v in conversation.items() if k != "archive_metadata"}, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    if sha(canonical) != entry.get("conversation_content_sha256"):
        raise HistoryError("The registered canonical conversation-content hash does not match")
    return data, conversation


@contextlib.contextmanager
def registry_lock(folder, wait_seconds):
    folder.mkdir(exist_ok=True)
    path = folder / LOCK_NAME
    if path.is_symlink():
        raise HistoryError("The history lock is a symbolic link")
    flags = os.O_CREAT | os.O_RDWR | getattr(os, "O_NOFOLLOW", 0)
    fd = os.open(path, flags, 0o600)
    try:
        if not stat.S_ISREG(os.fstat(fd).st_mode):
            raise HistoryError("The history lock is not a regular file")
        deadline = time.monotonic() + max(0, wait_seconds)
        while True:
            try:
                fcntl.flock(fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
                break
            except BlockingIOError:
                if time.monotonic() >= deadline:
                    raise SourcePending("Another history writer still holds the registry lock")
                time.sleep(0.05)
        yield
    finally:
        fcntl.flock(fd, fcntl.LOCK_UN)
        os.close(fd)


def fsync_dir(path):
    fd = os.open(path, os.O_RDONLY)
    try:
        os.fsync(fd)
    finally:
        os.close(fd)


def write_sync(path, data):
    if path.is_symlink():
        raise HistoryError("A transaction file is a symbolic link")
    with path.open("wb") as stream:
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def current_hash(path):
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise HistoryError("A transaction destination is not a regular file")
    return sha(path.read_bytes()) if path.exists() else None


def transaction_directory(folder):
    path = folder / TRANSACTION_NAME
    if path.is_symlink() or (path.exists() and not path.is_dir()):
        raise HistoryError("The transaction directory is unsafe")
    if path.exists():
        for child in path.iterdir():
            if child.name not in TRANSACTION_FILES or child.is_symlink() or not child.is_file():
                raise HistoryError("Unexpected file in the history transaction directory")
    return path


def clean_transaction(folder, transaction):
    for child in transaction.iterdir():
        child.unlink()
    transaction.rmdir()
    fsync_dir(folder)


def rollback_transaction(folder, transaction, journal):
    plans = []
    for label, target in (("chat", folder / journal["filename"]), ("index", folder / "index.json")):
        actual = current_hash(target)
        old, new = journal[f"old_{label}_sha256"], journal[f"new_{label}_sha256"]
        if actual not in {old, new}:
            raise HistoryError("Transaction recovery found an unexpected destination hash; manual recovery is required")
        backup = None
        if old is not None and actual != old:
            backup = transaction / f"old_{label}"
            if not backup.is_file() or sha(backup.read_bytes()) != old:
                raise HistoryError("Transaction recovery backup is missing or altered")
        plans.append((label, target, old, actual, backup))
    # Check every destination and required backup before changing either registered file.
    for label, target, old, actual, backup in plans:
        if old is None:
            if target.exists():
                target.unlink()
        elif actual != old:
            restore = transaction / f"restore_{label}"
            write_sync(restore, backup.read_bytes())
            os.replace(restore, target)
        fsync_dir(folder)


def recover_transaction(folder):
    transaction = transaction_directory(folder)
    if not transaction.exists():
        return None
    journal_path = transaction / "journal.json"
    if not journal_path.exists():
        # A journal is flushed before the first destination mutation.
        clean_transaction(folder, transaction)
        return "discarded_uninstalled_stage"
    try:
        journal = json.loads(journal_path.read_text(encoding="utf-8"))
        if journal.get("schema_version") != 1:
            raise ValueError("schema")
        validate_filename(journal["filename"])
        for label in ("chat", "index"):
            for state in ("old", "new"):
                value = journal[f"{state}_{label}_sha256"]
                if value is not None and not re.fullmatch(r"[0-9a-f]{64}", value):
                    raise ValueError("hash")
            if journal[f"new_{label}_sha256"] is None:
                raise ValueError("new hash")
    except (ValueError, KeyError, TypeError) as exc:
        raise HistoryError("Malformed transaction journal; manual recovery is required") from exc
    both_new = current_hash(folder / journal["filename"]) == journal["new_chat_sha256"] and current_hash(folder / "index.json") == journal["new_index_sha256"]
    if both_new:
        clean_transaction(folder, transaction)
        return "completed_commit"
    rollback_transaction(folder, transaction, journal)
    clean_transaction(folder, transaction)
    return "rolled_back_incomplete_commit"


def _install_transaction(folder, filename, chat_bytes, index_bytes):
    validate_filename(filename)
    transaction = transaction_directory(folder)
    if transaction.exists():
        raise HistoryError("A previous transaction must be recovered before writing")
    targets = {"chat": folder / filename, "index": folder / "index.json"}
    for path in targets.values():
        current_hash(path)
    old = {key: path.read_bytes() if path.exists() else None for key, path in targets.items()}
    journal = {"schema_version": 1, "filename": filename}
    transaction.mkdir(mode=0o700)
    try:
        for label, data in (("chat", chat_bytes), ("index", index_bytes)):
            if old[label] is not None:
                write_sync(transaction / f"old_{label}", old[label])
            write_sync(transaction / f"new_{label}", data)
            journal[f"old_{label}_sha256"] = sha(old[label]) if old[label] is not None else None
            journal[f"new_{label}_sha256"] = sha(data)
        write_sync(transaction / "journal.json", json_bytes(journal))
        fsync_dir(transaction)
        fsync_dir(folder)
        os.replace(transaction / "new_chat", targets["chat"])
        fsync_dir(folder)
        if _FAULT_POINT == "after_chat_replace":
            raise RuntimeError("Synthetic failure after chat replacement")
        os.replace(transaction / "new_index", targets["index"])
        fsync_dir(folder)
        if _FAULT_POINT == "after_index_replace":
            raise RuntimeError("Synthetic failure after index replacement")
        clean_transaction(folder, transaction)
    except Exception as exc:
        if (transaction / "journal.json").exists():
            try:
                rollback_transaction(folder, transaction, journal)
                clean_transaction(folder, transaction)
            except Exception as recovery:
                raise HistoryError("Installation failed and rollback is unresolved; preserve the transaction directory for recovery") from recovery
        elif transaction.exists():
            clean_transaction(folder, transaction)
        raise HistoryError("Installation failed; the original registered capture and index were preserved") from exc


def refresh_once(repo, thread_id, rollout=None, history_dir=None, title=None, after_turn=None, lock_wait_seconds=10, user_turn=None):
    repo = Path(repo).expanduser().resolve()
    if not isinstance(thread_id, str) or not re.fullmatch(r"[A-Za-z0-9_-]{1,128}", thread_id):
        raise HistoryError("A valid exact conversation id is required")
    explicit_folder = safe_directory(repo, history_dir) if history_dir is not None else None
    registered = find_registered(repo, thread_id, preferred=explicit_folder)
    if history_dir is None:
        if registered is None:
            return {"status": "skipped_unregistered", "thread_id": thread_id}
        folder = registered
    else:
        folder = explicit_folder
        if registered is not None and registered != folder:
            raise HistoryError("The conversation is already registered in another history folder")
    recorder = load_recorder(repo)
    source = resolve_rollout(thread_id, rollout)
    # Lock all reads, prefix checks and both writes in this one registry.
    with registry_lock(folder, lock_wait_seconds):
        recovery = recover_transaction(folder)
        index = read_index(folder)
        entry = next((e for e in index["chats"] if e["conversation_id"] == thread_id), None)
        previous = None
        if entry:
            _, previous = read_registered(folder, entry)
            capture_title = previous.get("title")
            if title is not None and title != capture_title:
                raise HistoryError("Automatic refresh cannot rename a registered conversation")
        else:
            if history_dir is None or not isinstance(title, str) or not title.strip():
                raise HistoryError("A new capture requires explicit --history-dir and --title")
            capture_title = title
        snapshot = read_public_source(source, thread_id, capture_title, recorder)
        if after_turn:
            if after_turn in snapshot.interrupted_turns:
                return {"status": "skipped_interrupted_turn", "thread_id": thread_id, "turn_id": after_turn}
            if after_turn not in snapshot.completed_turns or after_turn not in snapshot.final_turns:
                raise SourcePending("Waiting for the exact turn's real public final answer and task_complete record")
        conversation = snapshot.conversation
        new_messages = ordered_messages(conversation)
        if user_turn and not any(message["author"]["role"] == "user" and message.get("metadata", {}).get("source_turn_id") == user_turn for message in new_messages):
            raise SourcePending("Waiting for the exact prompt turn's real completed user message")
        if previous:
            old_messages = ordered_messages(previous)
            if len(new_messages) < len(old_messages) or any(public_signature(a) != public_signature(b) for a, b in zip(old_messages, new_messages)):
                raise HistoryError("The refreshed public messages do not preserve the exact archived prefix")
            if conversation["create_time"] != previous["create_time"]:
                raise HistoryError("The session creation timestamp disagrees with the registered capture")
            conversation["create_time"] = previous["create_time"]
            if len(new_messages) == len(old_messages):
                return {"status": "unchanged", "thread_id": thread_id, "number": entry["number"], "file": entry["file"], "messages": len(new_messages), "recovery": recovery}
            if new_messages[len(old_messages)]["update_time"] < old_messages[-1]["update_time"]:
                raise HistoryError("A new public message is backdated before the archived prefix")
        for earlier, later in zip(new_messages, new_messages[1:]):
            if later["update_time"] < earlier["update_time"]:
                raise HistoryError("Completed public message times are not monotone")
        captured = datetime.now(timezone.utc).timestamp()
        archive_meta = conversation["archive_metadata"]
        prior_meta = previous.get("archive_metadata", {}) if previous else {}
        archive_meta["first_captured_at_utc"] = prior_meta.get("first_captured_at_utc", prior_meta.get("captured_at_utc", recorder.iso(captured)))
        archive_meta["first_captured_at_local"] = prior_meta.get("first_captured_at_local", prior_meta.get("captured_at_local", datetime.fromtimestamp(captured, recorder.LOCAL).isoformat(timespec="milliseconds")))
        with tempfile.TemporaryDirectory(prefix="render-public-chat-") as temp:
            stage = Path(temp)
            (stage / "index.json").write_bytes(json_bytes(index))
            for old_entry in index["chats"]:
                if old_entry["conversation_id"] == thread_id:
                    (stage / old_entry["file"]).write_bytes((folder / old_entry["file"]).read_bytes())
            # Preserve reservations from unregistered numbered files, without copying their bodies.
            used = [e["number"] for e in index["chats"]]
            for path in folder.iterdir():
                match = re.fullmatch(r"(\d+)_.*\.json", path.name)
                if match:
                    used.append(int(match[1]))
            index["next_number"] = max(index.get("next_number", 1), max(used, default=0) + 1)
            (stage / "index.json").write_bytes(json_bytes(index))
            try:
                with contextlib.redirect_stdout(io.StringIO()):
                    recorder.save_chat(stage, conversation, captured)
            except (ValueError, OSError, KeyError, TypeError) as exc:
                raise HistoryError("The existing renderer refused the public capture; no registered data were changed") from exc
            rendered_index = json.loads((stage / "index.json").read_text(encoding="utf-8"))
            rendered_entry = next(e for e in rendered_index["chats"] if e["conversation_id"] == thread_id)
            rendered_entry["first_captured_at_utc"] = archive_meta["first_captured_at_utc"]
            rendered_entry["first_captured_at_local"] = archive_meta["first_captured_at_local"]
            validate_index(stage, rendered_index)
            filename = rendered_entry["file"]
            chat_bytes, index_bytes = (stage / filename).read_bytes(), json_bytes(rendered_index)
            if len(chat_bytes) >= MAX_BYTES or len(index_bytes) >= MAX_BYTES:
                raise HistoryError("The public capture or registry reaches the repository's 1 MiB limit")
            if not entry and (folder / filename).exists():
                raise HistoryError("Refusing to overwrite an unregistered chat filename")
            if entry and current_hash(folder / filename) != entry["sha256"]:
                raise HistoryError("The registered capture changed during refresh")
            _install_transaction(folder, filename, chat_bytes, index_bytes)
        return {"status": "refreshed" if previous else "registered", "thread_id": thread_id, "number": rendered_entry["number"], "file": filename, "messages": rendered_entry["message_count"], "recovery": recovery}


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--repo", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--thread-id")
    p.add_argument("--rollout", type=Path)
    p.add_argument("--history-dir", help="Explicit repository-relative destination; needed with --title to opt in a new chat")
    p.add_argument("--title")
    p.add_argument("--hook", action="store_true", help="Read a Stop or UserPromptSubmit hook input from stdin; never block the conversation")
    p.add_argument("--after-turn", help="Require the real public final answer and completion record of this exact turn")
    p.add_argument("--wait-seconds", type=float, default=60)
    p.add_argument("--defer", action="store_true", help="Launch a single bounded, detached exact-turn refresh worker")
    p.add_argument("--result-file", type=Path, help=argparse.SUPPRESS)
    return p


def run_bounded(args):
    deadline = time.monotonic() + args.wait_seconds
    while True:
        try:
            return refresh_once(args.repo, args.thread_id, args.rollout, args.history_dir, args.title, args.after_turn, lock_wait_seconds=min(5, max(0, deadline - time.monotonic())), user_turn=getattr(args, "user_turn", None))
        except SourcePending:
            if time.monotonic() >= deadline:
                raise SourcePending("The bounded refresh ended before the requested real source records were fully flushed")
            time.sleep(min(0.25, max(0, deadline - time.monotonic())))


def main(argv=None):
    args = parser().parse_args(argv)
    hook = args.hook
    try:
        if not math.isfinite(args.wait_seconds) or not 0 <= args.wait_seconds <= 120:
            raise HistoryError("--wait-seconds must lie between 0 and 120")
        if hook:
            try:
                payload = json.load(sys.stdin)
            except ValueError as exc:
                raise HistoryError("The hook input is not valid JSON") from exc
            if not isinstance(payload, dict) or payload.get("hook_event_name") not in {"Stop", "UserPromptSubmit"}:
                raise HistoryError("Only Stop and UserPromptSubmit hook events are supported")
            ident = payload.get("session_id")
            if not isinstance(ident, str) or not ident:
                raise HistoryError("The hook has no exact session id")
            if args.thread_id and args.thread_id != ident:
                raise HistoryError("The hook session id disagrees with --thread-id")
            args.thread_id = ident
            supplied = payload.get("transcript_path")
            if args.rollout and supplied and args.rollout.resolve() != Path(supplied).expanduser().resolve():
                raise HistoryError("The hook transcript path disagrees with --rollout")
            if supplied:
                if not isinstance(supplied, str):
                    raise HistoryError("The hook transcript path is invalid")
                args.rollout = Path(supplied)
            if payload["hook_event_name"] == "Stop":
                turn = payload.get("turn_id")
                if not isinstance(turn, str) or not turn:
                    raise HistoryError("The Stop hook has no exact turn id")
                if args.after_turn and args.after_turn != turn:
                    raise HistoryError("The hook turn disagrees with --after-turn")
                args.after_turn = turn
            else:
                turn = payload.get("turn_id")
                if not isinstance(turn, str) or not turn:
                    raise HistoryError("The UserPromptSubmit hook has no exact turn id")
                args.user_turn = turn
            # last_assistant_message is deliberately never used or synthesized.
        if not args.thread_id:
            raise HistoryError("--thread-id is required outside hook mode")
        if args.defer:
            if hook or not args.after_turn:
                raise HistoryError("--defer requires an exact --after-turn outside hook mode")
            source = resolve_rollout(args.thread_id, args.rollout)
            directory = Path(tempfile.mkdtemp(prefix="chat-history-refresh-result-"))
            result_file = directory / "result.json"
            command = [sys.executable, str(Path(__file__).resolve()), "--repo", str(args.repo.resolve()), "--thread-id", args.thread_id, "--rollout", str(source), "--after-turn", args.after_turn, "--wait-seconds", str(args.wait_seconds), "--result-file", str(result_file)]
            for flag, value in (("--history-dir", args.history_dir), ("--title", args.title)):
                if value is not None:
                    command.extend([flag, value])
            child = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, start_new_session=True, close_fds=True)
            result = {"status": "deferred", "pid": child.pid, "thread_id": args.thread_id, "turn_id": args.after_turn, "result_file": str(result_file), "wait_seconds": args.wait_seconds}
        else:
            result = run_bounded(args)
        if args.result_file:
            if args.result_file.is_symlink():
                raise HistoryError("The worker result file is a symbolic link")
            args.result_file.write_bytes(json_bytes(result))
        print("{}" if hook else json.dumps(result, ensure_ascii=False))
        return 0
    except Exception as exc:
        detail = str(exc) if isinstance(exc, (HistoryError, OSError, ValueError, TypeError)) else "Unexpected refresh failure (" + type(exc).__name__ + ")"
        result = {"status": "failed", "error": detail}
        if args.result_file and not args.result_file.is_symlink():
            try:
                args.result_file.write_bytes(json_bytes(result))
            except OSError:
                pass
        if hook:
            print(json.dumps({"systemMessage": "Chat-history refresh warning: " + detail}))
            return 0
        print(json.dumps(result), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
