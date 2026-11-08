#!/usr/bin/env python3
"""Isolated synthetic fixtures for the bounded paginated history adapter."""
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path
import sqlite3
import tempfile
import unittest
from unittest import mock

SCRIPT = Path(__file__).resolve().parents[1] / "paginated_chat_source.py"
SPEC = importlib.util.spec_from_file_location("fixture_paginated_source", SCRIPT)
ADAPTER = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(ADAPTER)
THREAD = "11111111-1111-7111-a111-111111111111"
OTHER = "22222222-2222-7222-a222-222222222222"
EPOCH = 1794106000


class PaginatedSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="paginated-source-fixture-")
        self.home = Path(self.temp.name)
        self.state = self.home / "state_5.sqlite"
        self.history = self.home / "thread_history_1.sqlite"
        with sqlite3.connect(self.state) as db:
            db.execute("CREATE TABLE threads(id TEXT PRIMARY KEY,title TEXT,created_at_ms INTEGER,history_mode TEXT)")
            db.execute("INSERT INTO threads VALUES(?,?,?,?)", (THREAD, "Synthetic exact title", EPOCH * 1000, "paginated"))
        with sqlite3.connect(self.history) as db:
            db.execute("""CREATE TABLE thread_turns(thread_id TEXT,turn_id TEXT,rollout_ordinal INTEGER,
                status TEXT,started_at REAL,completed_at REAL,first_user_item_id TEXT,final_agent_item_id TEXT)""")
            db.execute("""CREATE TABLE thread_items(thread_id TEXT,turn_id TEXT,item_id TEXT,
                rollout_ordinal INTEGER,created_at_ms INTEGER,item_json TEXT,item_type TEXT,
                updated_at_ordinal INTEGER,started_at_ms REAL,completed_at_ms REAL)""")
            db.execute("INSERT INTO thread_turns VALUES(?,?,?,?,?,?,?,?)",
                       (THREAD, "turn-1", 1, "completed", EPOCH + 1, EPOCH + 9, "user-1", "answer-1"))
        self.add_item("user-1", "userMessage", 2, content=[{"type": "text", "text": "Synthetic user text.", "text_elements": []}], clientId="client-1")
        self.add_item("progress-1", "agentMessage", 3, text="Synthetic progress.", phase="commentary")
        self.add_item("answer-1", "agentMessage", 5, text="Synthetic final.", phase="final_answer")

    def tearDown(self):
        self.temp.cleanup()

    def add_item(self, ident, kind, ordinal, *, turn="turn-1", thread=THREAD, start=None, end=None, pending=False, **fields):
        data = {"type": kind, "id": ident, **fields}
        if kind == "agentMessage":
            data.update(memoryCitation=None, delivery=None, questions=None)
        start = (EPOCH + ordinal) * 1000 if start is None else start
        end = None if pending else (start + 100 if end is None else end)
        with sqlite3.connect(self.history) as db:
            db.execute("INSERT INTO thread_items VALUES(?,?,?,?,?,?,?,?,?,?)",
                       (thread, turn, ident, ordinal, int(EPOCH * 1000), json.dumps(data), kind, ordinal, start, end))

    def change_json(self, ident, **updates):
        with sqlite3.connect(self.history) as db:
            data = json.loads(db.execute("SELECT item_json FROM thread_items WHERE item_id=?", (ident,)).fetchone()[0])
            data.update(updates)
            db.execute("UPDATE thread_items SET item_json=? WHERE item_id=?", (json.dumps(data), ident))

    def change_turn(self, **updates):
        with sqlite3.connect(self.history) as db:
            db.execute("UPDATE thread_turns SET " + ",".join(k + "=?" for k in updates), tuple(updates.values()))

    def source(self):
        return ADAPTER.load_paginated_rows(self.home, THREAD)

    def messages(self, rows):
        return [r["payload"]["item"] for r in rows if r.get("payload", {}).get("type") == "item_completed"]

    def file_signatures(self):
        return {p.name: (hashlib.sha256(p.read_bytes()).hexdigest(), p.stat().st_size, p.stat().st_mtime_ns)
                for p in self.home.iterdir() if p.is_file()}

    def test_completed_public_rows_exact_identity_time_and_metadata(self):
        rows, metadata = self.source()
        self.assertEqual([m["id"] for m in self.messages(rows)], ["user-1", "progress-1", "answer-1"])
        self.assertEqual(self.messages(rows)[0]["content"], [{"type": "text", "text": "Synthetic user text."}])
        self.assertEqual(metadata["thread_id"], THREAD)
        self.assertEqual(metadata["title"], "Synthetic exact title")
        self.assertEqual(metadata["created_at_ms"], EPOCH * 1000)
        self.assertEqual(metadata["created_at"], "2026-11-08T02:46:40.000Z")
        self.assertEqual(metadata["source_turn_ids"], ["turn-1"])
        self.assertEqual(metadata["source_kind"], ADAPTER.SOURCE_KIND)
        self.assertIn("immutable_no_wal_transaction", metadata["snapshot_mode"])
        self.assertFalse(any(r["type"] == "turn_context" for r in rows))
        final = next(r for r in rows if r.get("payload", {}).get("item", {}).get("id") == "answer-1")
        self.assertEqual(final["payload"]["started_at_ms"], (EPOCH + 5) * 1000)
        complete = [r for r in rows if r.get("payload", {}).get("type") == "task_complete"]
        self.assertEqual(len(complete), 1)
        self.assertEqual(complete[0]["payload"]["completed_at"], EPOCH + 9)

    def test_private_tool_and_other_thread_content_never_output(self):
        self.add_item("private-agent", "agentMessage", 4, text="PRIVATE_ANALYSIS_SENTINEL", phase="analysis")
        self.add_item("private-tool", "commandExecution", 6, command="PRIVATE_TOOL_SENTINEL")
        self.add_item("private-reasoning", "reasoning", 7, content=["PRIVATE_REASONING_SENTINEL"])
        self.add_item("other-user", "userMessage", 8, thread=OTHER, content=[{"type": "text", "text": "OTHER_THREAD_SENTINEL"}])
        with sqlite3.connect(self.history) as db:
            # Its payload is deliberately not JSON: known excluded types must
            # not be read or parsed merely to extract their private content.
            db.execute("UPDATE thread_items SET item_json='NOT_JSON_PRIVATE_SENTINEL' WHERE item_id='private-tool'")
        rows, metadata = self.source()
        self.assertNotIn("SENTINEL", json.dumps((rows, metadata)))
        self.assertEqual(len(self.messages(rows)), 3)

    def test_read_only_main_databases_and_no_new_sidecars(self):
        before = self.file_signatures()
        self.source()
        self.assertEqual(before, self.file_signatures())

    def test_existing_wal_is_read_and_all_source_bytes_preserved(self):
        writer = sqlite3.connect(self.history)
        try:
            writer.execute("PRAGMA journal_mode=WAL")
            writer.execute("UPDATE thread_items SET item_json=item_json WHERE item_id='answer-1'")
            writer.commit()
            before = self.file_signatures()
            rows, metadata = self.source()
            self.assertIn("read_only_wal_transaction", metadata["snapshot_mode"])
            self.assertEqual(before, self.file_signatures())
            self.assertEqual(len(self.messages(rows)), 3)
        finally:
            writer.close()

    def test_missing_exact_identity_is_retryable_without_other_thread_fallback(self):
        with self.assertRaises(ADAPTER.SourceUnavailable) as raised:
            ADAPTER.load_paginated_rows(self.home, OTHER)
        self.assertTrue(raised.exception.retryable)
        self.assertEqual(ADAPTER.probe_paginated_mode(self.home, OTHER), "absent")

    def test_probe_is_authoritative_even_without_history_store(self):
        self.history.unlink()
        self.assertEqual(ADAPTER.probe_paginated_mode(self.home, THREAD), "paginated")
        with self.assertRaises(ADAPTER.SourceUnavailable):
            self.source()
        with sqlite3.connect(self.state) as db:
            db.execute("UPDATE threads SET history_mode='legacy'")
        self.assertEqual(ADAPTER.probe_paginated_mode(self.home, THREAD), "legacy")

    def test_missing_state_probe_is_absent(self):
        self.state.unlink()
        self.assertEqual(ADAPTER.probe_paginated_mode(self.home, THREAD), "absent")

    def test_item_json_identity_and_type_must_match_columns(self):
        for updates in ({"id": "wrong-id"}, {"type": "reasoning"}):
            with self.subTest(updates=updates):
                self.change_json("answer-1", **updates)
                with self.assertRaises(ADAPTER.SourceError) as raised:
                    self.source()
                self.assertEqual(raised.exception.code, "source_identity_mismatch")
                self.change_json("answer-1", id="answer-1", type="agentMessage")

    def test_invalid_item_times_fail_closed(self):
        for start, end in ((None, 5), (float("inf"), 5), (8, 7), (-1, 5), ("bad", 5)):
            with self.subTest(start=start, end=end):
                with sqlite3.connect(self.history) as db:
                    db.execute("UPDATE thread_items SET started_at_ms=?, completed_at_ms=? WHERE item_id='answer-1'", (start, end))
                with self.assertRaises(ADAPTER.SourceError) as raised:
                    self.source()
                self.assertEqual(raised.exception.code, "source_timestamp_invalid")

    def test_invalid_creation_and_turn_times_fail_closed(self):
        with sqlite3.connect(self.state) as db:
            db.execute("UPDATE threads SET created_at_ms=NULL")
        with self.assertRaises(ADAPTER.SourceError):
            self.source()
        with sqlite3.connect(self.state) as db:
            db.execute("UPDATE threads SET created_at_ms=?", (EPOCH * 1000,))
        self.change_turn(started_at=EPOCH + 20, completed_at=EPOCH + 1)
        with self.assertRaises(ADAPTER.SourceError):
            self.source()

    def test_attachments_annotations_and_unknown_user_structures_fail(self):
        for updates in (
            {"content": [{"type": "image", "fileId": "attachment"}]},
            {"content": [{"type": "text", "text": "x", "text_elements": [{"type": "unknown"}]}]},
            {"attachment": {"fileId": "attachment"}},
        ):
            with self.subTest(updates=updates):
                self.change_json("user-1", **updates)
                with self.assertRaises(ADAPTER.SourceError) as raised:
                    self.source()
                self.assertEqual(raised.exception.code, "unsupported_public_content")
                self.change_json("user-1", content=[{"type": "text", "text": "Synthetic user text."}], attachment=None)
                with sqlite3.connect(self.history) as db:
                    data = json.loads(db.execute("SELECT item_json FROM thread_items WHERE item_id='user-1'").fetchone()[0])
                    data.pop("attachment", None)
                    db.execute("UPDATE thread_items SET item_json=? WHERE item_id='user-1'", (json.dumps(data),))

    def test_unknown_assistant_phases_fail(self):
        for phase in (None, "new_public_phase", []):
            with self.subTest(phase=phase):
                self.change_json("answer-1", phase=phase)
                with self.assertRaises(ADAPTER.SourceError) as raised:
                    self.source()
                self.assertEqual(raised.exception.code, "unsupported_source_format")

    def test_structured_assistant_material_is_not_silently_dropped(self):
        self.change_json("answer-1", questions=[{"question": "visible?"}])
        with self.assertRaises(ADAPTER.SourceError) as raised:
            self.source()
        self.assertEqual(raised.exception.code, "unsupported_public_content")

    def test_unknown_item_kind_fails_even_without_public_payload(self):
        self.add_item("future-item", "futurePublicMessage", 8, text="UNSUPPORTED")
        with self.assertRaises(ADAPTER.SourceError) as raised:
            self.source()
        self.assertEqual(raised.exception.code, "unsupported_source_format")

    def test_pending_public_gap_cannot_create_nonprefix_capture(self):
        self.add_item("unfinished-progress", "agentMessage", 4, pending=True, text="Pending", phase="commentary")
        with self.assertRaises(ADAPTER.SourceUnavailable):
            self.source()

    def test_pending_public_tail_in_completed_turn_waits(self):
        self.add_item("unfinished-tail", "agentMessage", 8, pending=True, text="Pending", phase="commentary")
        with self.assertRaises(ADAPTER.SourceUnavailable):
            self.source()

    def test_terminal_failed_turn_does_not_emit_completed_event(self):
        self.change_turn(status="failed")
        rows, _ = self.source()
        events = [r.get("payload", {}).get("type") for r in rows]
        self.assertNotIn("task_complete", events)
        self.assertIn("task_aborted", events)

    def test_inprogress_never_infers_turn_completion_from_final_text(self):
        self.change_turn(status="inProgress", completed_at=None)
        rows, _ = self.source()
        self.assertEqual(self.messages(rows)[-1]["phase"], "final_answer")
        self.assertFalse(any(r.get("payload", {}).get("type") == "task_complete" for r in rows))

    def test_inprogress_public_tail_is_not_exported_before_completion(self):
        self.change_turn(status="inProgress", completed_at=None)
        self.add_item("unfinished-tail", "agentMessage", 8, pending=True, text="Pending", phase="commentary")
        rows, metadata = self.source()
        self.assertNotIn("unfinished-tail", [m["id"] for m in self.messages(rows)])
        self.assertEqual(metadata["pending_item_count"], 1)
        self.assertFalse(any(r.get("payload", {}).get("type") == "task_complete" for r in rows))

    def test_unknown_turn_status_is_not_guessed(self):
        self.change_turn(status="pending-guessed-alias")
        with self.assertRaises(ADAPTER.SourceError) as raised:
            self.source()
        self.assertEqual(raised.exception.code, "unsupported_source_format")

    def test_final_reference_and_actual_final_completion_gate(self):
        for changes in ({"final_agent_item_id": None}, {"final_agent_item_id": "missing-final"},
                        {"final_agent_item_id": "progress-1"}, {"completed_at": None}):
            with self.subTest(changes=changes):
                self.change_turn(final_agent_item_id="answer-1", completed_at=EPOCH + 9, **{})
                self.change_turn(**changes)
                with self.assertRaises(ADAPTER.SourceUnavailable):
                    self.source()

    def test_final_reference_cannot_point_at_user(self):
        self.change_turn(final_agent_item_id="user-1")
        with self.assertRaises(ADAPTER.SourceError) as raised:
            self.source()
        self.assertEqual(raised.exception.code, "source_identity_mismatch")

    def test_live_change_invalidates_cross_database_snapshot(self):
        original = ADAPTER._load
        def changed(*args):
            value = original(*args)
            with sqlite3.connect(self.state) as db:
                db.execute("UPDATE threads SET title='Changed synthetic metadata'")
            return value
        with mock.patch.object(ADAPTER, "_load", side_effect=changed):
            with self.assertRaises(ADAPTER.SourceUnavailable) as raised:
                self.source()
        self.assertEqual(raised.exception.code, "source_snapshot_changed")

    def test_unpaired_wal_and_rollback_journal_fail_without_changes(self):
        for suffix in ("-wal", "-journal"):
            with self.subTest(suffix=suffix):
                sidecar = Path(str(self.history) + suffix)
                sidecar.write_bytes(b"synthetic incomplete sidecar")
                before = self.file_signatures()
                with self.assertRaises(ADAPTER.SourceUnavailable):
                    self.source()
                self.assertEqual(before, self.file_signatures())
                sidecar.unlink()


if __name__ == "__main__":
    unittest.main()
