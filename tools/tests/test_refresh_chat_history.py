#!/usr/bin/env python3
"""Meaningful isolated fixtures for automatic research-history refresh.

Installed under tools/tests, this resolves the repository renderer and tools
wrapper relatively. Scratch runs may set REFRESH_SCRIPT and
CHAT_HISTORY_RECORDER to explicit existing files.
All source text is synthetic. The real recorder is copied read-only into a
temporary fixture repository; actual project histories and sessions are unused.
"""
from __future__ import annotations

import contextlib
import copy
from datetime import datetime, timezone
import hashlib
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
import warnings
from unittest import mock

HERE = Path(__file__).resolve().parent
SCRIPT = Path(os.environ.get('REFRESH_SCRIPT', HERE.parent / 'refresh_chat_history.py')).resolve()
LEGACY = Path(os.environ.get('CHAT_HISTORY_RECORDER', HERE.parents[1] / 'papers/investigations-2/record_chat.py')).resolve()
THREAD = '11111111-1111-1111-1111-111111111111'
OTHER = '22222222-2222-2222-2222-222222222222'
HISTORY_REL = 'papers/investigations-2/fixture_project/chat-histories'
START = datetime(2026, 10, 13, 1, 0, tzinfo=timezone.utc).timestamp()
FIRST_CAPTURE = START + 100


def load_module(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def timestamp(seconds):
    return datetime.fromtimestamp(START + seconds, timezone.utc).isoformat()


def source_row(kind, payload, seconds=0):
    return {'timestamp': timestamp(seconds), 'type': kind, 'payload': payload}


def public_message(message_id, text, seconds, role='AgentMessage', phase='commentary', turn='turn-1', thread=THREAD):
    item = {'id': message_id, 'type': role, 'content': [{'type': 'text', 'text': text}]}
    if role == 'AgentMessage':
        item['phase'] = phase
    return source_row('event_msg', {
        'type': 'item_completed', 'thread_id': thread, 'turn_id': turn,
        'started_at_ms': int((START + seconds) * 1000),
        'completed_at_ms': int((START + seconds + .1) * 1000), 'item': item,
    }, seconds + .1)


def completed_turn(turn, seconds):
    return source_row('event_msg', {'type': 'task_complete', 'thread_id': THREAD, 'turn_id': turn}, seconds)


def initial_source():
    return [
        source_row('session_meta', {'id': THREAD, 'timestamp': timestamp(0)}, 0),
        source_row('turn_context', {'thread_id': THREAD, 'model': 'fixture-model', 'effort': 'fixture-effort'}, 1),
        source_row('event_msg', {'type': 'task_started', 'thread_id': THREAD, 'turn_id': 'turn-1'}, 2),
        public_message('user-1', 'Synthetic research request.', 3, role='UserMessage'),
        public_message('answer-1', 'Synthetic completed first answer.', 4, phase='final_answer'),
        completed_turn('turn-1', 5),
    ]


def encoded_rows(rows):
    return ''.join(json.dumps(x, ensure_ascii=False) + '\n' for x in rows).encode()


REFRESH = load_module(SCRIPT, 'fixture_history_refresh') if SCRIPT.exists() else None


class RefreshTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if REFRESH is None:
            raise RuntimeError(f'Implementation not yet available: {SCRIPT}')

    def setUp(self):
        # The unchanged legacy renderer predates context-managed file reads.
        warnings.filterwarnings('ignore', category=ResourceWarning)
        self.temp = tempfile.TemporaryDirectory(prefix='history-refresh-fixture-')
        self.root = Path(self.temp.name)
        self.repo = self.root / 'repo'
        self.repo.mkdir()
        legacy_path = self.repo / 'papers/investigations-2/record_chat.py'
        legacy_path.parent.mkdir(parents=True)
        legacy_path.write_bytes(LEGACY.read_bytes())
        self.legacy = load_module(legacy_path, 'fixture_legacy_' + self.root.name.replace('-', '_'))
        project = self.repo / 'papers/investigations-2/fixture_project'
        for name in ['notes', 'numerics', 'reviews', 'chat-histories']:
            (project / name).mkdir(parents=True, exist_ok=True)
        (project / 'README.md').write_text('# Synthetic fixture project\n')
        self.history = self.repo / HISTORY_REL
        self.rollout = self.root / 'source.jsonl'
        self.rows = initial_source()
        self.write_source()
        self.register()

    def tearDown(self):
        self.temp.cleanup()

    def write_source(self):
        self.rollout.write_bytes(encoded_rows(self.rows))

    def register(self):
        conversation = self.legacy.codex_chat(self.rollout, 'Synthetic fixture chat', THREAD, timestamp(0))
        with contextlib.redirect_stdout(io.StringIO()):
            self.legacy.save_chat(self.history, conversation, FIRST_CAPTURE)

    def refresh(self, **kwargs):
        args = {'repo': self.repo, 'thread_id': THREAD, 'rollout': self.rollout}
        args.update(kwargs)
        with contextlib.redirect_stdout(io.StringIO()):
            return REFRESH.refresh_once(**args)

    def append(self, text='Synthetic appended progress.', seconds=10, phase='commentary', turn='turn-2'):
        self.rows.append(public_message('append-' + str(seconds), text, seconds, phase=phase, turn=turn))
        self.write_source()

    def registry(self):
        return json.loads((self.history / 'index.json').read_bytes())

    def entry(self):
        return next(x for x in self.registry()['chats'] if x['conversation_id'] == THREAD)

    def history_path(self):
        return self.history / self.entry()['file']

    def conversation(self):
        return json.loads(self.history_path().read_bytes())[0]

    def texts(self):
        return [n['message']['content']['parts'][0] for n in self.conversation()['mapping'].values() if n.get('message')]

    def data_pair(self):
        return self.history_path().read_bytes(), (self.history / 'index.json').read_bytes()

    def assert_registry_integrity(self):
        entry = self.entry()
        data = self.history_path().read_bytes()
        self.assertEqual(hashlib.sha256(data).hexdigest(), entry['sha256'])
        conversation = json.loads(data)[0]
        canonical = json.dumps({k:v for k,v in conversation.items() if k != 'archive_metadata'}, ensure_ascii=False, sort_keys=True, separators=(',',':')).encode()
        self.assertEqual(hashlib.sha256(canonical).hexdigest(), entry['conversation_content_sha256'])
        self.assertEqual(len(data), entry['bytes'])
        self.assertEqual(sum(n.get('message') is not None for n in conversation['mapping'].values()), entry['message_count'])

    def assert_refusal_preserves(self, expected=None):
        before = self.data_pair()
        with self.assertRaises(expected or REFRESH.HistoryError):
            self.refresh()
        self.assertEqual(self.data_pair(), before)

    def test_append_keeps_identity_creation_and_first_capture(self):
        original = copy.deepcopy(self.entry())
        self.append()
        self.refresh()
        current = self.entry()
        for field in ['number','file','conversation_id','created_at_utc','created_at_local']:
            self.assertEqual(current[field], original[field])
        self.assertEqual(current['message_count'], original['message_count'] + 1)
        for obj in [current, self.conversation()['archive_metadata']]:
            self.assertEqual(obj['first_captured_at_utc'], original['captured_at_utc'])
            self.assertEqual(obj['first_captured_at_local'], original['captured_at_local'])
        self.assert_registry_integrity()
        self.assertEqual(self.texts()[-1], 'Synthetic appended progress.')

    def test_first_capture_survives_multiple_later_refreshes(self):
        first=self.entry()['captured_at_utc']
        self.append(seconds=10);self.refresh()
        self.append(seconds=20);self.refresh()
        self.assertEqual(self.entry()['first_captured_at_utc'],first)
        self.assertEqual(self.conversation()['archive_metadata']['first_captured_at_utc'],first)
        self.assertEqual(self.entry()['message_count'],4)

    def test_unchanged_second_refresh_is_byte_idempotent(self):
        self.refresh()  # May migrate legacy first-capture metadata once.
        before = self.data_pair()
        self.refresh()
        self.assertEqual(self.data_pair(), before)

    def test_original_public_prefix_cannot_be_rewritten(self):
        self.rows[4]['payload']['item']['content'][0]['text'] = 'Rewritten first answer.'
        self.append()
        self.assert_refusal_preserves()

    def test_shorter_source_cannot_replace_registered_chat(self):
        self.rows = self.rows[:4]
        self.write_source()
        self.assert_refusal_preserves()

    def test_original_message_timestamp_cannot_change(self):
        self.rows[4]['payload']['completed_at_ms'] += 1000
        self.append()
        self.assert_refusal_preserves()

    def test_submillisecond_original_creation_change_is_rejected(self):
        self.rows[0]['payload']['timestamp']=timestamp(.0005)
        self.append()
        self.assert_refusal_preserves()

    def test_appended_message_time_cannot_go_backwards(self):
        self.append(seconds=2)
        self.assert_refusal_preserves()

    def test_wrong_source_session_identity_is_rejected(self):
        self.rows[0]['payload']['id'] = OTHER
        self.append()
        self.assert_refusal_preserves()

    def test_source_without_exact_session_metadata_is_rejected(self):
        self.rows=self.rows[1:];self.write_source()
        self.assert_refusal_preserves()

    def test_conflicting_duplicate_public_message_id_is_rejected(self):
        duplicate=copy.deepcopy(self.rows[4]);duplicate['payload']['item']['content'][0]['text']='DUPLICATE_REWRITE_FIXTURE'
        self.rows.append(duplicate);self.write_source()
        self.assert_refusal_preserves()

    def test_nonfinite_public_timestamp_is_rejected(self):
        self.append();self.rows[-1]['payload']['completed_at_ms']=float('nan');self.write_source()
        self.assert_refusal_preserves()

    def test_private_and_other_thread_records_are_not_archived(self):
        forbidden = ['PRIVATE_SYSTEM_FIXTURE','PRIVATE_REASONING_FIXTURE','PRIVATE_TOOL_FIXTURE','OTHER_THREAD_FIXTURE']
        self.rows.extend([
            source_row('response_item', {'type':'message','role':'system','content':[{'type':'text','text':forbidden[0]}]}, 6),
            source_row('event_msg', {'type':'item_completed','thread_id':THREAD,'turn_id':'turn-2','item':{'type':'Reasoning','id':'reasoning','content':[{'type':'text','text':forbidden[1]}]}}, 7),
            source_row('event_msg', {'type':'item_completed','thread_id':THREAD,'turn_id':'turn-2','item':{'type':'ToolCall','id':'tool','content':[{'type':'text','text':forbidden[2]}]}}, 8),
            public_message('other-thread', forbidden[3], 9, thread=OTHER),
        ])
        self.append()
        self.refresh()
        saved = self.history_path().read_text()
        for text in forbidden:
            self.assertNotIn(text, saved)
        self.assertEqual(self.entry()['message_count'], 3)

    def test_unknown_public_assistant_phase_refuses(self):
        self.append(phase='unknown_public_phase')
        self.assert_refusal_preserves()

    def test_private_assistant_phase_is_omitted(self):
        self.rows.append(public_message('private-analysis','PRIVATE_ANALYSIS_FIXTURE',9,phase='analysis'))
        self.append();self.refresh()
        self.assertNotIn('PRIVATE_ANALYSIS_FIXTURE',self.history_path().read_text())
        self.assertEqual(self.entry()['message_count'],3)

    def test_nontext_public_content_refuses_instead_of_dropping(self):
        row = public_message('image-message', 'placeholder', 10)
        row['payload']['item']['content'] = [{'type':'image','image_url':'fixture://image'}]
        self.rows.append(row); self.write_source()
        self.assert_refusal_preserves()

    def test_unregistered_thread_without_opt_in_is_skipped(self):
        before = self.data_pair()
        result = self.refresh(thread_id=OTHER)
        self.assertIn('skip', result['status'])
        self.assertEqual(self.data_pair(), before)
        self.assertEqual(len(self.registry()['chats']), 1)

    def test_explicit_destination_registers_new_chat(self):
        for row in self.rows:
            payload = row['payload']
            if row['type'] == 'session_meta': payload['id'] = OTHER
            if payload.get('thread_id') == THREAD: payload['thread_id'] = OTHER
        self.write_source()
        self.refresh(thread_id=OTHER, history_dir=HISTORY_REL, title='Second synthetic chat')
        entries = self.registry()['chats']
        self.assertEqual(len(entries), 2)
        new = next(x for x in entries if x['conversation_id'] == OTHER)
        self.assertEqual(new['number'], 2)
        self.assertEqual(new['created_at_utc'], self.entry()['created_at_utc'])

    def test_explicit_destination_resolves_duplicate_registered_chat(self):
        other=self.repo/'papers/investigations-2/other_project/chat-histories';other.mkdir(parents=True)
        name=self.entry()['file']
        other_chat=self.history_path().read_bytes();other_index=(self.history/'index.json').read_bytes()
        (other/name).write_bytes(other_chat);(other/'index.json').write_bytes(other_index)
        self.append()
        with self.assertRaises(REFRESH.HistoryError):self.refresh()
        self.refresh(history_dir=HISTORY_REL)
        self.assertEqual(self.entry()['message_count'],3)
        self.assertEqual((other/name).read_bytes(),other_chat)
        self.assertEqual((other/'index.json').read_bytes(),other_index)
        self.assert_registry_integrity()

    def test_source_discovery_rejects_wrong_substring_then_selects_exact_suffix(self):
        fake_home=self.root/'discovery_home';sessions=fake_home/'.codex/sessions';sessions.mkdir(parents=True)
        (sessions/('rollout-'+THREAD+'-extra.jsonl')).write_bytes(encoded_rows(self.rows))
        with mock.patch.object(REFRESH.os,'environ',{}),mock.patch.object(REFRESH.Path,'home',return_value=fake_home):
            with self.assertRaises(REFRESH.HistoryError):REFRESH.resolve_rollout(THREAD)
            exact=sessions/('rollout-date-'+THREAD+'.jsonl');exact.write_bytes(encoded_rows(self.rows))
            self.assertEqual(REFRESH.resolve_rollout(THREAD),exact.resolve())

    def test_source_discovery_refuses_two_exact_candidates(self):
        fake_home=self.root/'discovery_home';sessions=fake_home/'.codex/sessions';sessions.mkdir(parents=True)
        for prefix in ['rollout-one-','rollout-two-']:
            (sessions/(prefix+THREAD+'.jsonl')).write_bytes(encoded_rows(self.rows))
        with mock.patch.object(REFRESH.os,'environ',{}),mock.patch.object(REFRESH.Path,'home',return_value=fake_home):
            with self.assertRaises(REFRESH.HistoryError):REFRESH.resolve_rollout(THREAD)

    def test_incomplete_trailing_json_is_not_archived(self):
        self.append()
        self.rollout.write_bytes(self.rollout.read_bytes() + b'{"type":"event_msg","payload":{"text":"PARTIAL_FIXTURE')
        before = self.data_pair()
        try:
            self.refresh()
        except REFRESH.SourcePending:
            self.assertEqual(self.data_pair(), before)
        self.assertNotIn('PARTIAL_FIXTURE', self.history_path().read_text())
        self.assert_registry_integrity()

    def test_malformed_completed_jsonl_record_is_rejected(self):
        self.rollout.write_bytes(self.rollout.read_bytes() + b'{bad completed JSON}\n')
        self.assert_refusal_preserves()

    def test_registered_filename_cannot_escape_history_folder(self):
        index = self.registry(); index['chats'][0]['file'] = '../outside.json'
        (self.history/'index.json').write_text(json.dumps(index))
        outside = self.history.parent/'outside.json'; outside.write_text('OUTSIDE_FIXTURE')
        with self.assertRaises(REFRESH.HistoryError): self.refresh()
        self.assertEqual(outside.read_text(), 'OUTSIDE_FIXTURE')

    def test_registered_file_symlink_is_rejected(self):
        path = self.history_path(); data = path.read_bytes(); path.unlink()
        outside = self.root/'outside.json'; outside.write_bytes(data); path.symlink_to(outside)
        self.append()
        with self.assertRaises(REFRESH.HistoryError): self.refresh()
        self.assertEqual(outside.read_bytes(), data)

    def test_history_folder_symlink_is_rejected(self):
        outside = self.root/'outside-history'; self.history.rename(outside); self.history.symlink_to(outside, target_is_directory=True)
        before = (outside/'index.json').read_bytes()
        with self.assertRaises(REFRESH.HistoryError): self.refresh(history_dir=HISTORY_REL)
        self.assertEqual((outside/'index.json').read_bytes(), before)

    def test_archive_integrity_mismatch_refuses(self):
        self.history_path().write_bytes(self.history_path().read_bytes() + b'\n')
        self.append()
        self.assert_refusal_preserves()

    def test_canonical_registry_hash_mismatch_refuses(self):
        index=self.registry();index['chats'][0]['conversation_content_sha256']='0'*64
        (self.history/'index.json').write_text(json.dumps(index))
        self.append();self.assert_refusal_preserves()

    def test_large_public_history_is_rejected_without_replacement(self):
        self.append(text='x' * (1024 * 1024))
        self.assert_refusal_preserves()

    def test_concurrent_identical_refreshes_leave_one_consistent_result(self):
        self.append()
        cmd = [sys.executable, str(SCRIPT), '--repo',str(self.repo),'--thread-id',THREAD,'--rollout',str(self.rollout)]
        children = [subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True) for _ in range(4)]
        try:
            outcomes = [p.communicate(timeout=20) for p in children]
        finally:
            for p in children:
                if p.poll() is None: p.kill(); p.wait()
        self.assertEqual([p.returncode for p in children], [0]*4, outcomes)
        self.assertEqual(self.entry()['message_count'], 3)
        self.assertEqual(len(self.registry()['chats']), 1)
        self.assert_registry_integrity()

    def test_transaction_fault_after_chat_replace_rolls_back(self):
        self._check_transaction_fault('after_chat_replace')

    def test_transaction_fault_after_index_replace_rolls_back(self):
        self._check_transaction_fault('after_index_replace')

    def _check_transaction_fault(self, point):
        before = self.data_pair(); self.append()
        original = getattr(REFRESH, '_FAULT_POINT', None)
        REFRESH._FAULT_POINT = point
        try:
            with self.assertRaises((RuntimeError, REFRESH.HistoryError)):
                self.refresh()
        finally:
            REFRESH._FAULT_POINT = original
        self.assertEqual(self.data_pair(), before)
        REFRESH.recover_transaction(self.history)
        self.assertEqual(self.data_pair(), before)
        self.refresh()
        self.assertEqual(self.entry()['message_count'], 3)
        self.assert_registry_integrity()

    def test_final_capture_requires_real_final_and_task_complete(self):
        before = self.data_pair()
        self.rows.append(source_row('event_msg', {'type':'task_started','thread_id':THREAD,'turn_id':'turn-2'}, 9))
        self.append(text='Progress, not a final response.', turn='turn-2')
        with self.assertRaises(REFRESH.SourcePending): self.refresh(after_turn='turn-2')
        self.assertEqual(self.data_pair(), before)
        self.rows.append(completed_turn('turn-2', 11)); self.write_source()
        with self.assertRaises(REFRESH.SourcePending): self.refresh(after_turn='turn-2')
        self.assertEqual(self.data_pair(), before)
        self.rows.append(public_message('final-2','Actual completed synthetic final.',12,phase='final_answer',turn='turn-2'))
        self.rows.append(completed_turn('turn-2', 13)); self.write_source()
        self.refresh(after_turn='turn-2')
        self.assertEqual(self.texts()[-1], 'Actual completed synthetic final.')
        self.assert_registry_integrity()

    def test_deferred_cli_captures_only_after_final_source_is_completed(self):
        self.rows.append(source_row('event_msg', {'type':'task_started','thread_id':THREAD,'turn_id':'turn-2'}, 9))
        self.append(text='Synthetic deferred progress.',turn='turn-2')
        before = self.data_pair()
        cmd = [sys.executable,str(SCRIPT),'--repo',str(self.repo),'--thread-id',THREAD,'--rollout',str(self.rollout),'--after-turn','turn-2','--wait-seconds','4','--defer']
        launcher = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        self.assertEqual(launcher.returncode, 0, (launcher.stdout,launcher.stderr))
        time.sleep(.15)
        self.assertEqual(self.data_pair(), before)
        self.rows.append(public_message('deferred-final','Actually sent deferred synthetic final.',12,phase='final_answer',turn='turn-2'))
        self.rows.append(completed_turn('turn-2',13)); self.write_source()
        deadline = time.monotonic()+6
        while time.monotonic()<deadline:
            if 'Actually sent deferred synthetic final.' in self.history_path().read_text(): break
            time.sleep(.05)
        self.assertEqual(self.texts()[-1], 'Actually sent deferred synthetic final.')
        self.assert_registry_integrity()

    def prepare_crash_journal(self, state='mixed'):
        filename = self.entry()['file']
        old_chat, old_index = self.data_pair()
        self.append(); self.refresh()
        new_chat, new_index = self.data_pair()
        self.history_path().write_bytes(old_chat)
        (self.history/'index.json').write_bytes(old_index)
        transaction = self.history/'.chat-history-transaction'; transaction.mkdir()
        journal = {'schema_version':1,'filename':filename}
        for name,data in [('old_chat',old_chat),('old_index',old_index),('new_chat',new_chat),('new_index',new_index)]:
            (transaction/name).write_bytes(data)
            journal[name+'_sha256']=hashlib.sha256(data).hexdigest()
        (transaction/'journal.json').write_text(json.dumps(journal))
        if state in ['mixed','complete']:
            os.replace(transaction/'new_chat',self.history/filename)
        if state=='complete':
            os.replace(transaction/'new_index',self.history/'index.json')
        return (old_chat,old_index),(new_chat,new_index),transaction

    def test_crash_between_replacements_recovers_original_pair(self):
        old,new,transaction=self.prepare_crash_journal('mixed')
        self.assertEqual(REFRESH.recover_transaction(self.history),'rolled_back_incomplete_commit')
        self.assertEqual(self.data_pair(),old)
        self.assertFalse(transaction.exists())
        self.assert_registry_integrity()

    def test_crash_after_both_replacements_finishes_committed_pair(self):
        old,new,transaction=self.prepare_crash_journal('complete')
        self.assertEqual(REFRESH.recover_transaction(self.history),'completed_commit')
        self.assertEqual(self.data_pair(),new)
        self.assertFalse(transaction.exists())
        self.assert_registry_integrity()

    def test_crash_recovery_refuses_foreign_destination_bytes(self):
        old,new,transaction=self.prepare_crash_journal('mixed')
        self.history_path().write_bytes(b'FOREIGN_EDIT_FIXTURE')
        before=self.data_pair()
        with self.assertRaises(REFRESH.HistoryError):REFRESH.recover_transaction(self.history)
        self.assertEqual(self.data_pair(),before)
        self.assertTrue(transaction.exists())

    def test_crash_recovery_checks_later_index_before_restoring_chat(self):
        old,new,transaction=self.prepare_crash_journal('mixed')
        (self.history/'index.json').write_bytes(b'FOREIGN_INDEX_FIXTURE')
        filename=json.loads(old[1])['chats'][0]['file']
        before_chat=(self.history/filename).read_bytes()
        with self.assertRaises(REFRESH.HistoryError):REFRESH.recover_transaction(self.history)
        self.assertEqual((self.history/filename).read_bytes(),before_chat)
        self.assertEqual((self.history/'index.json').read_bytes(),b'FOREIGN_INDEX_FIXTURE')
        self.assertTrue(transaction.exists())

    def test_crash_recovery_refuses_changed_backup(self):
        old,new,transaction=self.prepare_crash_journal('mixed')
        (transaction/'old_chat').write_bytes(b'BAD_BACKUP_FIXTURE')
        before=self.data_pair()
        with self.assertRaises(REFRESH.HistoryError):REFRESH.recover_transaction(self.history)
        self.assertEqual(self.data_pair(),before)
        self.assertTrue(transaction.exists())

    def test_hook_does_not_synthesize_last_assistant_message(self):
        self.rows.append(source_row('event_msg',{'type':'task_started','thread_id':THREAD,'turn_id':'turn-2'},9))
        self.append(text='Synthetic pending commentary.',turn='turn-2')
        before=self.data_pair()
        hook={'hook_event_name':'Stop','session_id':THREAD,'transcript_path':str(self.rollout),'turn_id':'turn-2','last_assistant_message':'DRAFT_FINAL_NOT_IN_SOURCE'}
        cmd=[sys.executable,str(SCRIPT),'--repo',str(self.repo),'--hook','--wait-seconds','0']
        out=subprocess.run(cmd,input=json.dumps(hook),capture_output=True,text=True,timeout=10)
        self.assertEqual(out.returncode,0)
        self.assertIn('systemMessage',json.loads(out.stdout))
        self.assertEqual(self.data_pair(),before)
        self.assertNotIn('DRAFT_FINAL_NOT_IN_SOURCE',self.history_path().read_text())

    def test_prompt_hook_waits_for_real_user_flush_without_synthesizing_prompt(self):
        before=self.data_pair()
        hook={'hook_event_name':'UserPromptSubmit','session_id':THREAD,'transcript_path':str(self.rollout),'turn_id':'turn-2','prompt':'SYNTHETIC_PROMPT_MUST_NOT_BE_IMPORTED'}
        cmd=[sys.executable,str(SCRIPT),'--repo',str(self.repo),'--hook','--wait-seconds','4']
        child=subprocess.Popen(cmd,stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
        try:
            child.stdin.write(json.dumps(hook)+'\n');child.stdin.close();child.stdin=None
            time.sleep(.15)
            self.assertIsNone(child.poll(),'Old user messages must not satisfy the current-turn gate')
            self.assertEqual(self.data_pair(),before)
            self.rows.append(public_message('user-2','Actual source user prompt.',10,role='UserMessage',turn='turn-2'))
            self.rows.append(source_row('event_msg',{'type':'task_interrupted','thread_id':THREAD,'turn_id':'turn-2'},11))
            self.write_source()
            stdout,stderr=child.communicate(timeout=8)
            self.assertEqual(child.returncode,0,(stdout,stderr))
            self.assertEqual(json.loads(stdout),{})
        finally:
            if child.poll() is None:child.kill();child.wait()
        self.assertEqual(self.texts()[-1],'Actual source user prompt.')
        self.assertNotIn('SYNTHETIC_PROMPT_MUST_NOT_BE_IMPORTED',self.history_path().read_text())
        self.assert_registry_integrity()

    def test_prompt_hook_without_exact_turn_id_warns_without_refresh(self):
        self.append()
        before=self.data_pair()
        hook={'hook_event_name':'UserPromptSubmit','session_id':THREAD,'transcript_path':str(self.rollout),'prompt':'MISSING_TURN_FIXTURE'}
        cmd=[sys.executable,str(SCRIPT),'--repo',str(self.repo),'--hook','--wait-seconds','0']
        out=subprocess.run(cmd,input=json.dumps(hook),capture_output=True,text=True,timeout=8)
        self.assertEqual(out.returncode,0)
        self.assertIn('systemMessage',json.loads(out.stdout))
        self.assertEqual(self.data_pair(),before)

    def test_api_user_turn_gate_requires_current_real_user(self):
        self.append(text='A completed assistant message is not the user prompt.',turn='turn-2')
        before=self.data_pair()
        with self.assertRaises(REFRESH.SourcePending):self.refresh(user_turn='turn-2')
        self.assertEqual(self.data_pair(),before)
        self.rows.append(public_message('user-2','Real current-turn API fixture user.',12,role='UserMessage',turn='turn-2'))
        self.write_source();self.refresh(user_turn='turn-2')
        self.assertEqual(self.texts()[-1],'Real current-turn API fixture user.')
        self.assert_registry_integrity()

    def test_interrupted_turn_is_skipped_without_replacing_history(self):
        self.rows.append(source_row('event_msg',{'type':'task_interrupted','thread_id':THREAD,'turn_id':'turn-2'},9))
        self.append(text='Synthetic interrupted progress.',turn='turn-2')
        before=self.data_pair()
        result=self.refresh(after_turn='turn-2')
        self.assertEqual(result['status'],'skipped_interrupted_turn')
        self.assertEqual(self.data_pair(),before)


if __name__ == '__main__':
    unittest.main(verbosity=2)
