"""Read-only verification of this research chat's existing formal replay identity.

15 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model gpt-6-astra; reasoning effort ultra. No history writer is used.
"""
from pathlib import Path
from datetime import datetime,timezone
import argparse,fcntl,hashlib,importlib.util,json,os,stat,sys

def digest(data): return hashlib.sha256(data).hexdigest()

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    repo=args.repo.resolve()
    helper=repo/'tools/refresh_chat_history.py'
    spec=importlib.util.spec_from_file_location('history_read_audit',helper)
    module=importlib.util.module_from_spec(spec)
    sys.modules[spec.name]=module
    spec.loader.exec_module(module)
    thread='01a14023-1225-7d00-8dde-fe9135fa4ca1'
    turn='01a1404e-1e65-72c2-a54a-83092c11165a'
    prior='01a14035-d45f-71e2-bfbb-cb014784eef0'
    relative='papers/investigations-2/formal_replay_crosswalk/chat-histories'
    folder=repo/relative
    checks=[]
    def check(name,condition):
        if not condition: raise AssertionError(name)
        checks.append(name)
    check('sole registration is the existing formal replay lane',module.find_registered(repo,thread)==folder)
    lock=folder/module.LOCK_NAME
    check('existing registry lock is regular and not a symlink',lock.is_file() and not lock.is_symlink())
    fd=os.open(lock,os.O_RDONLY|getattr(os,'O_NOFOLLOW',0))
    try:
        fcntl.flock(fd,fcntl.LOCK_SH|fcntl.LOCK_NB)
        check('lock descriptor is a regular file',stat.S_ISREG(os.fstat(fd).st_mode))
        check('no pending paired history transaction',not (folder/module.TRANSACTION_NAME).exists())
        before_index=(folder/'index.json').read_bytes()
        index=module.read_index(folder)
        entries=[e for e in index['chats'] if e['conversation_id']==thread]
        check('exactly one registry entry in lane',len(entries)==1)
        entry=entries[0]
        expected='0020_2026-10-15T15-16-42Z_brainstorm-theta-geometry-paths.json'
        check('history number and filename preserved',entry['number']==20 and entry['file']==expected)
        check('original title and creation time preserved',entry['title']=='Brainstorm theta geometry paths' and entry['created_at_utc']=='2026-10-15T15:16:42.662Z')
        data,conversation=module.read_registered(folder,entry)
        checks.append('stored bytes and canonical content hashes validate')
        archive=module.ordered_messages(conversation)
        metadata=conversation['archive_metadata']
        check('first capture provenance preserved',entry['first_captured_at_utc']==metadata['first_captured_at_utc']=='2026-10-15T15:18:50.066Z')
        check('archive and registry preserve history number',metadata['history_number']==entry['number'])
        check('registered count equals public archive length',entry['message_count']==len(archive))
        source=module.resolve_rollout(thread)
        snapshot=module.read_public_source(source,thread,entry['title'],module.load_recorder(repo))
        public=module.ordered_messages(snapshot.conversation)
        check('all completed public source text is refreshed',len(public)==len(archive))
        check('every archived public message matches source exactly',all(module.public_signature(a)==module.public_signature(b) for a,b in zip(archive,public)))
        check('source creation time preserved',conversation['create_time']==snapshot.conversation['create_time'])
        final_records=[]
        for final_turn in sorted(snapshot.final_turns & snapshot.completed_turns):
            records=[(n,m) for n,m in enumerate(archive,1) if m['metadata'].get('source_turn_id')==final_turn and m['metadata'].get('phase')=='final_answer']
            check('completed final captured exactly once: '+final_turn,len(records)==1)
            n,m=records[0]
            text=''.join(m['content']['parts'])
            final_records.append({'turn_id':final_turn,'message_id':m['id'],'position':n,'text_sha256':digest(text.encode()),'characters':len(text)})
        check('preceding turn has final and completion',prior in snapshot.final_turns and prior in snapshot.completed_turns)
        check('archive marks preceding turn completed',metadata['turns'][prior]['status']=='completed')
        check('current user request captured',any(m['author']['role']=='user' and m['metadata'].get('source_turn_id')==turn for m in archive))
        check('public-only content validation passes',all(m['author']['role'] in {'user','assistant'} for m in archive))
        deferred_path=Path('/var/folders/xp/y2qq4y8j2zz9j1v35d82dpgw0000gn/T/chat-history-refresh-result-aaa66i0d/result.json')
        deferred=json.loads(deferred_path.read_text())
        check('preceding deferred result preserves identity',deferred['thread_id']==thread and deferred['number']==20 and deferred['file']==expected and deferred['status'] in {'refreshed','unchanged'})
        prior_final=next(x for x in final_records if x['turn_id']==prior)
        check('preceding final lies within deferred captured prefix',prior_final['position']<=deferred['messages']<=len(archive))
        check('registry bytes stable during read-only audit',before_index==(folder/'index.json').read_bytes())
        check('archive bytes stable during read-only audit',data==(folder/entry['file']).read_bytes())
        result={'status':'PASS','date':'2026-10-15','prepared_for':'Edward Baker','llm_assistance':'Substantial LLM assistance; read-only audit.',
                'model':'gpt-6-astra','reasoning_effort':'ultra','verified_at_utc':datetime.now(timezone.utc).isoformat(),
                'thread_id':thread,'current_turn_id':turn,'number':20,'file':entry['file'],'history_dir':relative,'title':entry['title'],
                'created_at_utc':entry['created_at_utc'],'first_captured_at_utc':entry['first_captured_at_utc'],'captured_at_utc':entry['captured_at_utc'],
                'message_count':len(archive),'archive_bytes':len(data),'archive_sha256':digest(data),
                'canonical_content_sha256':entry['conversation_content_sha256'],'index_sha256':digest(before_index),
                'helper_sha256':digest(helper.read_bytes()),'audit_script_sha256':digest(Path(__file__).read_bytes()),
                'source_rollout':str(source),'source_completed_public_message_count_at_audit':len(public),
                'completed_finals':final_records,'prior_deferred_result':deferred,
                'current_turn_has_final_in_source':turn in snapshot.final_turns,
                'current_turn_completed_in_source':turn in snapshot.completed_turns,
                'assertions_passed':len(checks),'checks':checks,
                'scope':'Read-only shared-lock registry, archive, and source snapshot. No registration, history edits, recovery or hook-trust changes. Current unsent final is excluded; exact-turn deferred capture is arranged separately. Hashes identify content, not mathematical validity.'}
    finally:
        fcntl.flock(fd,fcntl.LOCK_UN)
        os.close(fd)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','number','message_count','assertions_passed','archive_sha256','current_turn_has_final_in_source')}))

if __name__=='__main__': main()
