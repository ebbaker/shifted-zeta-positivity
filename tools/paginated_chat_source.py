#!/usr/bin/env python3
"""Read the verified local Codex paginated history schema without source writes.

The return value is ``(legacy_public_rows, metadata)``.  Rows contain only
canonical user text, assistant commentary/final text and recorded lifecycle
metadata.  They are adapter input for the existing strict history reader,
not a provider export or a reconstruction of omitted model settings.

Supported schema: state_5.sqlite threads and thread_history_1.sqlite
thread_turns/thread_items, as shipped with Codex 0.167.0-alpha.3.2. Read-only
transactions are guarded by before/after metadata checks on both databases
and sidecars. A no-WAL/no-SHM/no-journal database can be read immutable;
an existing WAL requires an existing SHM and an ordinary read-only view.
Any detected change fails closed. This does not copy or export whole stores.
"""
from __future__ import annotations

import contextlib
from datetime import datetime, timezone
import json
import math
from pathlib import Path
import sqlite3
import stat


SOURCE_KIND = "Local Codex paginated SQLite history; canonical public-text adapter"
PUBLIC_PHASES = {"commentary", "final_answer"}
PRIVATE_PHASES = {"analysis", "reasoning", "summary"}
# The non-public alternatives of the installed generated v2/ThreadItem type.
# An unfamiliar kind must not silently disappear from the public transcript.
NONPUBLIC_TYPES = {
    "hookPrompt", "functionCallOutput", "plan", "reasoning",
    "commandExecution", "fileChange", "mcpToolCall", "dynamicToolCall",
    "collabAgentToolCall", "subAgentActivity", "webSearch", "imageView",
    "sleep", "imageGeneration", "enteredReviewMode", "exitedReviewMode",
    "contextCompaction",
}
PUBLIC_TYPES = {"userMessage", "agentMessage"}
# Terminal strings were observed in the verified local DB; inProgress is
# explicitly documented by the installed generated v2/TurnStatus protocol.
# No alternate pending spelling is inferred from that protocol.
TURN_STATUSES = {"completed", "inProgress", "interrupted", "failed"}
DATABASES = {"state": "state_5.sqlite", "history": "thread_history_1.sqlite"}
TIMESTAMP_SCHEMA = {
    "thread_created_at": "threads.created_at_ms: Unix milliseconds",
    "turn_started_at": "thread_turns.started_at: Unix seconds",
    "turn_completed_at": "thread_turns.completed_at: Unix seconds",
    "item_started_at": "thread_items.started_at_ms: Unix milliseconds",
    "item_completed_at": "thread_items.completed_at_ms: Unix milliseconds",
}


class SourceError(RuntimeError):
    """Unsupported or inconsistent canonical source; not a retryable absence."""

    retryable = False

    def __init__(self, message, *, code="source_invalid", details=None):
        super().__init__(message)
        self.code = code
        # Fixed diagnostic labels/counts only; never message text or private data.
        self.details = {"source_selection": "paginated_sqlite"}
        if details:
            self.details.update(details)


class SourceUnavailable(SourceError):
    """A missing, incomplete or changing source may become available later."""

    retryable = True

    def __init__(self, message, *, code="source_unavailable", details=None):
        super().__init__(message, code=code, details=details)


def _identity(value, label):
    if not isinstance(value, str) or not value or value == "root" or "\x00" in value:
        raise SourceError("Invalid recorded " + label, code="source_identity_mismatch")
    return value


def _number(value, label, *, integer=False):
    if (not isinstance(value, (int, float)) or isinstance(value, bool)
            or not math.isfinite(value) or value < 0
            or (integer and not isinstance(value, int))):
        raise SourceError("Invalid recorded " + label, code="source_timestamp_invalid")
    return value


def _iso(value, label, *, milliseconds=False):
    _number(value, label)
    try:
        return datetime.fromtimestamp(value / 1000 if milliseconds else value,
                                      timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z")
    except (ValueError, OverflowError, OSError) as exc:
        raise SourceError("Invalid recorded " + label, code="source_timestamp_invalid") from exc


def _ordinal(value):
    if not isinstance(value, int) or isinstance(value, bool) or value < 0:
        raise SourceError("Invalid source rollout ordering", code="source_order_invalid")
    return value


def _inventory(paths):
    result = {}
    for kind, database in paths.items():
        for suffix in ("", "-wal", "-shm", "-journal"):
            path = Path(str(database) + suffix)
            try:
                info = path.lstat()
            except FileNotFoundError:
                if not suffix:
                    raise SourceUnavailable("A paginated history database is unavailable",
                                            details={"database": kind, "candidate_count": 0})
                result[(kind, suffix)] = None
                continue
            except OSError as exc:
                raise SourceUnavailable("Cannot inspect the paginated source snapshot",
                                        details={"database": kind}) from exc
            if not stat.S_ISREG(info.st_mode):
                raise SourceError("Paginated history sources must be regular files",
                                  code="source_invalid", details={"database": kind})
            result[(kind, suffix)] = (info.st_dev, info.st_ino, info.st_size,
                                      info.st_mtime_ns, info.st_ctime_ns)
    return result


def _unchanged(paths, before):
    if _inventory(paths) != before:
        raise SourceUnavailable("Paginated history changed during source acquisition",
                                code="source_snapshot_changed")


@contextlib.contextmanager
def _snapshot(paths):
    before = _inventory(paths)
    for kind in paths:
        journal = before[(kind, "-journal")]
        if journal is not None and journal[2]:
            raise SourceUnavailable("A database rollback journal prevents stable source acquisition",
                                    code="source_snapshot_changed", details={"database": kind})
        has_wal = before[(kind, "-wal")] is not None
        has_shm = before[(kind, "-shm")] is not None
        if has_wal != has_shm:
            raise SourceUnavailable("An incomplete WAL/SHM pair prevents safe read-only acquisition",
                                    code="source_snapshot_changed", details={"database": kind})
    yield paths, before
    # The guard spans acquisition of both SQLite read transactions and every
    # metadata/item read. Thus cross-database changes also invalidate capture.
    _unchanged(paths, before)


@contextlib.contextmanager
def _read_database(path, *, may_be_immutable):
    connection = None
    mode = "immutable_no_wal_transaction" if may_be_immutable else "read_only_wal_transaction"
    try:
        try:
            uri = path.as_uri() + "?mode=ro" + ("&immutable=1" if may_be_immutable else "")
            connection = sqlite3.connect(uri, uri=True, timeout=0)
            connection.execute("PRAGMA query_only=ON")
            connection.execute("BEGIN")
            connection.execute("SELECT name FROM sqlite_master LIMIT 1").fetchall()
        except sqlite3.OperationalError as exc:
            raise SourceUnavailable("Cannot obtain the guarded read-only paginated view") from exc
        connection.row_factory = sqlite3.Row
        yield connection, mode
    except SourceError:
        raise
    except sqlite3.DatabaseError as exc:
        raise SourceError("Cannot read the supported paginated history schema",
                          code="unsupported_source_format") from exc
    finally:
        if connection is not None:
            connection.close()


def _event(event, thread_id, turn_id, timestamp, **fields):
    return {"type": "event_msg", "timestamp": timestamp,
            "payload": {"type": event, "thread_id": thread_id,
                        "turn_id": turn_id, **fields}}


def _public_item(item, item_type):
    if item_type == "agentMessage":
        phase = item.get("phase")
        if not isinstance(phase, str):
            raise SourceError("Unknown assistant public phase", code="unsupported_source_format")
        if phase in PRIVATE_PHASES:
            return None
        if phase not in PUBLIC_PHASES:
            raise SourceError("Unknown assistant public phase", code="unsupported_source_format")
        allowed = {"type", "id", "text", "phase", "memoryCitation", "delivery", "questions"}
        if set(item) - allowed or not isinstance(item.get("text"), str):
            raise SourceError("Unsupported assistant public structure", code="unsupported_public_content")
        # Structured citations/delivery/questions need an explicit preserving
        # exporter; silently dropping them could omit visible public material.
        if any(item.get(key) is not None for key in ("memoryCitation", "delivery", "questions")):
            raise SourceError("Structured assistant content requires a preserving exporter",
                              code="unsupported_public_content")
        return {"type": "AgentMessage", "id": item["id"], "phase": phase,
                "content": [{"type": "text", "text": item["text"]}]}
    if set(item) - {"type", "id", "clientId", "content"}:
        raise SourceError("Unsupported user public structure", code="unsupported_public_content")
    if item.get("clientId") is not None and not isinstance(item["clientId"], str):
        raise SourceError("Invalid user message identity", code="source_identity_mismatch")
    if not isinstance(item.get("content"), list):
        raise SourceError("Malformed public user content", code="unsupported_public_content")
    parts = []
    for part in item["content"]:
        if (not isinstance(part, dict) or part.get("type") != "text"
                or not isinstance(part.get("text"), str)
                or set(part) - {"type", "text", "text_elements"}
                or part.get("text_elements", []) != []):
            raise SourceError("Non-text or annotated public content requires a preserving exporter",
                              code="unsupported_public_content")
        parts.append({"type": "text", "text": part["text"]})
    return {"type": "UserMessage", "id": item["id"], "content": parts}


def _load(state, history, thread_id):
    records = state.execute("SELECT id, title, created_at_ms, history_mode FROM threads WHERE id = ?",
                            (thread_id,)).fetchall()
    if not records:
        raise SourceUnavailable("No exact paginated thread metadata is available",
                                details={"candidate_count": 0})
    if len(records) != 1 or records[0]["id"] != thread_id:
        raise SourceError("Conflicting exact thread metadata", code="source_identity_mismatch")
    metadata = dict(records[0])
    if metadata["history_mode"] != "paginated":
        raise SourceUnavailable("The exact thread has no paginated history contract",
                                code="source_not_paginated")
    created = _number(metadata["created_at_ms"], "thread creation time", integer=True)
    created_at = _iso(created, "thread creation time", milliseconds=True)
    if metadata["title"] is not None and not isinstance(metadata["title"], str):
        raise SourceError("Invalid recorded thread title", code="source_invalid")
    turns = history.execute("""SELECT thread_id, turn_id, rollout_ordinal, status,
        started_at, completed_at, first_user_item_id, final_agent_item_id
        FROM thread_turns WHERE thread_id = ? ORDER BY rollout_ordinal""", (thread_id,)).fetchall()
    if not turns:
        raise SourceUnavailable("No exact paginated turns are available", details={"candidate_count": 0})
    turn_by_id, turn_ordinals = {}, set()
    rows = [{"type": "session_meta", "timestamp": created_at,
             "payload": {"id": thread_id, "timestamp": created_at}}]
    for turn in turns:
        if turn["thread_id"] != thread_id:
            raise SourceError("A turn belongs to a different thread", code="source_identity_mismatch")
        ident = _identity(turn["turn_id"], "turn id")
        ordinal = _ordinal(turn["rollout_ordinal"])
        if ident in turn_by_id or ordinal in turn_ordinals:
            raise SourceError("Conflicting source turns", code="source_order_invalid")
        turn_ordinals.add(ordinal)
        if turn["status"] not in TURN_STATUSES:
            raise SourceError("Unknown recorded turn status", code="unsupported_source_format")
        start = _iso(turn["started_at"], "turn start time")
        if turn["completed_at"] is not None:
            _iso(turn["completed_at"], "turn completion time")
            if turn["started_at"] > turn["completed_at"]:
                raise SourceError("A turn starts after its completion", code="source_timestamp_invalid")
        for key in ("first_user_item_id", "final_agent_item_id"):
            if turn[key] is not None:
                _identity(turn[key], "turn message reference")
        turn_by_id[ident] = turn
        rows.append(_event("task_started", thread_id, ident, start, started_at=turn["started_at"]))

    kinds = {row[0] for row in history.execute(
        "SELECT DISTINCT item_type FROM thread_items WHERE thread_id = ?", (thread_id,))}
    if any(kind not in PUBLIC_TYPES | NONPUBLIC_TYPES for kind in kinds):
        raise SourceError("Unknown canonical item kind", code="unsupported_source_format")
    # Only public payloads are read. Known private/tool alternatives are
    # excluded by the SQL predicate, not exported and subsequently discarded.
    items = history.execute("""SELECT thread_id, turn_id, item_id, rollout_ordinal,
        item_type, started_at_ms, completed_at_ms, item_json AS public_json
        FROM thread_items WHERE thread_id = ? AND item_type IN ('userMessage', 'agentMessage')
        ORDER BY rollout_ordinal""", (thread_id,)).fetchall()
    seen_ids, seen_ordinals, item_info, public = set(), set(), {}, {}
    pending_count, pending_turns = 0, set()
    public_gap = False
    for item in items:
        ident = _identity(item["item_id"], "item id")
        turn_id = _identity(item["turn_id"], "item turn id")
        if item["thread_id"] != thread_id or turn_id not in turn_by_id:
            raise SourceError("An item has no matching exact source turn", code="source_identity_mismatch")
        ordinal = _ordinal(item["rollout_ordinal"])
        if ident in seen_ids or ordinal in seen_ordinals:
            raise SourceError("Conflicting source item ordering", code="source_order_invalid")
        seen_ids.add(ident)
        seen_ordinals.add(ordinal)
        kind = item["item_type"]
        item_info[ident] = (turn_id, kind)
        try:
            data = json.loads(item["public_json"])
        except (TypeError, ValueError) as exc:
            raise SourceError("Malformed public item JSON", code="unsupported_source_format") from exc
        if not isinstance(data, dict) or data.get("id") != ident or data.get("type") != kind:
            raise SourceError("Item columns disagree with its canonical JSON identity",
                              code="source_identity_mismatch")
        safe = _public_item(data, kind)
        if safe is None:
            continue
        end = item["completed_at_ms"]
        if end is None:
            pending_count += 1
            pending_turns.add(turn_id)
            public_gap = True
            continue
        if public_gap:
            raise SourceUnavailable("An unfinished public item precedes later completed public text",
                                    code="source_pending", details={"pending_item_count": pending_count})
        _iso(item["started_at_ms"], "public item start time", milliseconds=True)
        stamp = _iso(end, "public item completion time", milliseconds=True)
        if item["started_at_ms"] > end:
            raise SourceError("A public item starts after its completion", code="source_timestamp_invalid")
        public[ident] = (turn_id, safe)
        rows.append(_event("item_completed", thread_id, turn_id, stamp,
                           started_at_ms=item["started_at_ms"], completed_at_ms=end, item=safe))
    if not public:
        raise SourceUnavailable("No completed canonical public messages are available",
                                details={"pending_item_count": pending_count})
    for ident, turn in turn_by_id.items():
        first, final = turn["first_user_item_id"], turn["final_agent_item_id"]
        if first is not None and first in item_info and item_info[first] != (ident, "userMessage"):
            raise SourceError("A turn's user reference disagrees with its source item",
                              code="source_identity_mismatch")
        if final is not None and final in item_info and item_info[final] != (ident, "agentMessage"):
            raise SourceError("A turn's final reference disagrees with its source item",
                              code="source_identity_mismatch")
        if turn["status"] == "completed":
            if (ident in pending_turns or turn["completed_at"] is None or final not in public
                    or public[final][0] != ident or public[final][1].get("phase") != "final_answer"):
                raise SourceUnavailable("A completed turn lacks its actual completed public final",
                                        code="source_pending")
            if first is not None and first not in public:
                raise SourceUnavailable("A completed turn lacks its referenced completed user item",
                                        code="source_pending")
            stamp = _iso(turn["completed_at"], "turn completion time")
            rows.append(_event("task_complete", thread_id, ident, stamp,
                               completed_at=turn["completed_at"]))
        elif turn["status"] in {"interrupted", "failed"}:
            stamp = (_iso(turn["completed_at"], "terminal turn time")
                     if turn["completed_at"] is not None else None)
            rows.append(_event("task_interrupted" if turn["status"] == "interrupted" else "task_aborted",
                               thread_id, ident, stamp))
    return rows, {"thread_id": thread_id, "title": metadata["title"],
                  "created_at_ms": created, "created_at": created_at,
                  "source_turn_ids": list(turn_by_id),
                  "pending_item_count": pending_count}


def load_paginated_rows(codex_home, thread_id):
    """Return exact normalized public rows and source metadata, or fail closed.

    A missing exact thread, unfinished source or changing snapshot raises
    SourceUnavailable. Unsupported public structure/identity/time raises
    SourceError. This function never invents model configurations, IDs,
    lifecycle times, final completion, or a provider source location.
    """
    _identity(thread_id, "requested thread id")
    home = Path(codex_home).expanduser().absolute()
    paths = {kind: home / filename for kind, filename in DATABASES.items()}
    with _snapshot(paths) as (copies, before):
        with contextlib.ExitStack() as stack:
            connections, modes = {}, []
            for kind in DATABASES:
                connection, mode = stack.enter_context(_read_database(
                    copies[kind], may_be_immutable=before[(kind, "-wal")] is None
                    and before[(kind, "-journal")] is None))
                connections[kind] = connection
                modes.append(mode)
            try:
                rows, metadata = _load(connections["state"], connections["history"], thread_id)
            except SourceError:
                raise
            except sqlite3.DatabaseError as exc:
                raise SourceError("Unsupported paginated history table or item JSON",
                                  code="unsupported_source_format") from exc
    metadata.update(source_kind=SOURCE_KIND,
                    source_paths={kind: str(path) for kind, path in paths.items()},
            snapshot_mode="guarded_read_transactions:" + ",".join(modes),
                    timestamp_schema=dict(TIMESTAMP_SCHEMA))
    return rows, metadata


def probe_paginated_mode(codex_home, thread_id):
    """Return the exact stored history contract: paginated, legacy, or absent.

    The caller may fall back to discovery of legacy JSONL only for legacy or
    absent. A marked paginated thread's later loading errors are never a
    reason to fall back to a retained, potentially stale JSONL file.
    """
    _identity(thread_id, "requested thread id")
    path = Path(codex_home).expanduser().absolute() / DATABASES["state"]
    try:
        path.lstat()
    except FileNotFoundError:
        return "absent"
    except OSError as exc:
        raise SourceUnavailable("Cannot inspect exact thread history metadata") from exc
    with _snapshot({"state": path}) as (paths, before):
        with _read_database(paths["state"], may_be_immutable=before[("state", "-wal")] is None
                            and before[("state", "-journal")] is None) as (connection, _):
            try:
                records = connection.execute("SELECT id, history_mode FROM threads WHERE id = ?",
                                             (thread_id,)).fetchall()
            except sqlite3.DatabaseError as exc:
                raise SourceError("Unsupported thread history metadata schema",
                                  code="unsupported_source_format") from exc
            if not records:
                mode = "absent"
            elif len(records) != 1 or records[0]["id"] != thread_id:
                raise SourceError("Conflicting exact thread metadata", code="source_identity_mismatch")
            else:
                mode = records[0]["history_mode"]
                if mode not in {"paginated", "legacy"}:
                    raise SourceError("Unknown persisted history contract", code="unsupported_source_format")
    return mode
