#!/usr/bin/env python3
"""One-off host queue for the owned formal-replay VM; no recurring scheduling.

Adopts zeta/001, preserves evidence before baseline restoration, and runs
Dirichlet/001 then Hecke/001. Only a confirmed runtime cutoff of zeta/001
permits one zeta/002 retry. All ambiguity halts without resetting the VM.
Use --selftest for fake-response tests; it never calls Multipass.
"""
from __future__ import annotations

import argparse
import datetime as dt
import fcntl
import hashlib
import inspect
import json
import os
from pathlib import Path
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
import uuid


DISCLOSURE = {"prepared_for": "Edward Baker", "model": "GPT-6 (Codex); exact serving variant not exposed",
              "effort": "not exposed; not inferred", "llm_assistance": "Substantial LLM assistance; no independent mathematical validation."}
PINS = {"math": "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb",
        "comparator": "d03acab154d269c06e60e4de7e4cc85deebff94b",
        "lean4export": "076e8e57707e813375e8f9da8bf989799ace9680",
        "landrun": "811cfff51ceaf3d9843708aa6d22e9b84ccac8b4"}


def normalize_runner_cli(argv):
    """Only the known pinned runner's absent --attempt has the default 001."""
    if not any(Path(value).name == 'run_guarded_comparator.py' for value in argv):
        return None
    def value(flag):
        index = argv.index(flag) if flag in argv else -1
        return argv[index + 1] if index >= 0 and index + 1 < len(argv) else None
    return {'target': value('--target'), 'attempt': value('--attempt') if '--attempt' in argv else '001'}


GUEST_PROBE = r'''
import os,json,hashlib,subprocess,sys
from pathlib import Path
''' + inspect.getsource(normalize_runner_cli) + r'''
base=Path(sys.argv[1]);root=Path(sys.argv[2]);target=sys.argv[3];attempt=sys.argv[4]
path=base/('replay_'+target+'_'+attempt+'.json');out={'record':None,'record_error':None,'record_file':None,'running_records':[],'runners':[],'math_processes':[],'other_record_errors':[],'uid':os.getuid()}
if path.exists():
 try:
  if path.stat().st_size>=1000000:raise ValueError('guest target record exceeds one megabyte')
  b=path.read_bytes();out['record_file']={'sha256':hashlib.sha256(b).hexdigest(),'bytes':len(b)};out['record']=json.loads(b)
 except Exception as e:out['record_error']=repr(e)
for p in base.glob('replay_*.json'):
 try:
  if p.stat().st_size>=1000000:raise ValueError('record exceeds one megabyte')
  d=json.loads(p.read_text())
  if d.get('status')=='running':out['running_records'].append({'target':d.get('target'),'attempt':d.get('attempt'),'path':str(p)})
 except Exception as e:
  if p!=path:out['other_record_errors'].append({'path':str(p),'error':repr(e)})
for p in Path('/proc').iterdir():
 if not p.name.isdigit() or int(p.name)==os.getpid():continue
 try:
  argv=[x.decode(errors='replace') for x in (p/'cmdline').read_bytes().split(b'\0') if x]
  if not argv:continue
  identified=normalize_runner_cli(argv)
  if identified is not None:out['runners'].append({'pid':int(p.name),**identified})
  cwd=str((p/'cwd').resolve());exe=(p/'exe').resolve().name
  if (cwd==str(root) or cwd.startswith(str(root)+'/')) and exe in {'lean','lake','comparator','lean4export','landrun'}:
   out['math_processes'].append({'pid':int(p.name),'executable':exe,'cgroup':(p/'cgroup').read_text()})
 except (OSError,ValueError):pass
def call(argv):
 try:
  r=subprocess.run(argv,capture_output=True,text=True,timeout=10);return {'argv':argv,'exit_code':r.returncode,'stdout':r.stdout,'stderr':r.stderr}
 except Exception as e:return {'argv':argv,'error':repr(e)}
listing=call(['systemctl','--user','list-units','--all','--plain','--no-legend','--no-pager','rh-replay-*.service']);out['unit_listing']=listing;out['active_units']=[]
for line in listing.get('stdout','').splitlines():
 parts=line.split()
 if len(parts)>=4 and parts[2] in {'active','activating','deactivating','reloading'}:out['active_units'].append(parts[0])
unit='rh-replay-'+target.lower()+'-'+attempt+'.service'
properties=call(['systemctl','--user','show',unit,'--no-pager','--property=LoadState','--property=ActiveState','--property=SubState','--property=Result','--property=ExecMainCode','--property=ExecMainStatus','--property=RuntimeMaxUSec','--property=ActiveEnterTimestampMonotonic','--property=ActiveExitTimestampMonotonic'])
out['unit_properties_command']=properties;out['unit_properties']=dict(line.split('=',1) for line in properties.get('stdout','').splitlines() if '=' in line)
if out.get('record') and out['record'].get('status')!='running':out['unit_journal']=call(['journalctl','--user','-u',unit,'--no-pager','-n','40'])
out['fresh_OAI_absent']=not(root/'.lake/build/lib/lean/OAI').exists();out['fresh_challenge_absent']=not(root/'.lake/build/lib/lean/ComparatorChallenges').exists()
out['compiled_OAI_modules']=sum(1 for _ in (root/'.lake/build/lib/lean/OAI').rglob('*.olean')) if not out['fresh_OAI_absent'] else 0
runner=base/'run_guarded_comparator.py';out['runner_sha256']=hashlib.sha256(runner.read_bytes()).hexdigest() if runner.exists() else None
print(json.dumps(out))
'''


class Refusal(RuntimeError):
    pass


def require(condition, message):
    if not condition:
        raise Refusal(message)


def utc():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1 << 20), b''):
            h.update(block)
    return h.hexdigest()


def identity(path):
    path = Path(path)
    return {'path': str(path), 'bytes': path.stat().st_size, 'sha256': digest(path)}


def read_small_json(path):
    path=Path(path)
    require(path.is_file() and not path.is_symlink() and path.stat().st_size<1_000_000,
            'small JSON record is missing, symlinked or exceeds one megabyte: '+str(path))
    value=json.loads(path.read_text())
    require(isinstance(value,dict),'small JSON record must be an object: '+str(path))
    return value


def atomic_json(path, value):
    path = Path(path)
    encoded = (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()
    require(len(encoded) < 1_000_000, 'small state/result exceeded one megabyte')
    temporary = path.with_name(path.name + '.new-' + uuid.uuid4().hex)
    with temporary.open('xb') as stream:
        stream.write(encoded); stream.flush(); os.fsync(stream.fileno())
    os.replace(temporary, path)


def snapshot_metadata(response, vm, baseline):
    require(not response.get('errors'), 'Multipass snapshot info reports errors')
    name = baseline[len(vm) + 1:]
    try:
        metadata = response['info'][vm]['snapshots'][name]
    except (KeyError, TypeError) as error:
        raise Refusal('named saved baseline is missing from snapshot info') from error
    require(isinstance(metadata, dict) and metadata.get('created'), 'baseline creation metadata is missing')
    return metadata


def match_snapshot(actual, expected):
    # Children/size are observational; preserve them but do not infer stability.
    for key in ('created', 'comment', 'cpu_count', 'disk_space', 'memory_size', 'mounts', 'parent'):
        if key in expected:
            require(actual.get(key) == expected[key], 'saved baseline metadata drift: ' + key)


def ensure_quiescent(probe, allowed=None):
    require(probe.get('unit_listing', {}).get('exit_code') == 0, 'cannot establish active systemd units')
    require(not probe.get('other_record_errors'), 'another guest attempt record is unreadable')
    require(len(probe.get('runners', [])) <= 1, 'duplicate runner processes are active')
    allowed_tuple = tuple(allowed) if allowed else None
    allowed_unit = f'rh-replay-{allowed[0].lower()}-{allowed[1]}.service' if allowed else None
    for item in probe.get('running_records', []) + probe.get('runners', []):
        require((item.get('target'), item.get('attempt')) == allowed_tuple,
                'another or unidentified target attempt is active')
    require(all(unit == allowed_unit for unit in probe.get('active_units', [])), 'another guarded service is active')
    for item in probe.get('math_processes', []):
        require(allowed_unit is not None and allowed_unit in item.get('cgroup', ''), 'unowned mathematical process is active')


def validate_record(record, observed_file, context, target, attempt):
    require(isinstance(record, dict), 'completed target record missing')
    require(record.get('schema') == 'guarded-mathematical-replay-v1', 'unexpected target record schema')
    require((record.get('target'), record.get('attempt')) == (target, attempt), 'target/attempt identity mismatch')
    require(record.get('baseline_name') in {context['baseline'], context['baseline_label']}, 'attempt baseline label mismatch')
    require(record.get('fresh_OAI_and_challenge_build_trees_absent') is True, 'fresh-baseline assertion missing')
    require(record.get('untrusted_solution_compilation_outside_guard') is False, 'unguarded compilation recorded')
    expected = context['targets'][target]
    require(record.get('configuration') == expected['configuration'], 'configuration content mismatch')
    require(record.get('configuration_sha256') == expected['configuration_sha256'], 'configuration SHA mismatch')
    require(record.get('status') != 'running' and record.get('finished_utc'), 'target record is incomplete')
    command = record.get('command', [])
    require('--property=RestrictAddressFamilies=~AF_UNIX' in command and '--user' in command and '--pty' in command,
            'required systemd guard is missing')
    require('--unit=rh-replay-' + target.lower() + '-' + attempt in command, 'named service does not match attempt')
    require(command[-4:] == ['-c', 'lake env comparator "$1"', 'bash', expected['config_guest_path']], 'checker invocation changed')
    timeout_flags = [part for part in command if part.startswith('--property=RuntimeMaxSec=')]
    require(len(timeout_flags) == 1 and re.fullmatch(r'--property=RuntimeMaxSec=\d+s', timeout_flags[0]), 'runtime bound missing')
    bound = int(timeout_flags[0].split('=')[-1][:-1])
    require(60 <= bound <= 21600, 'runtime bound outside approved range')
    if (target, attempt) != ('zeta', '001'):
        require(bound == 21600, 'queued target did not use six-hour runtime bound')
    expected_command = ['systemd-run','--property=RestrictAddressFamilies=~AF_UNIX','--user','--pty',
                        '--unit=rh-replay-'+target.lower()+'-'+attempt,'--property=RuntimeMaxSec='+str(bound)+'s',
                        '-E','PATH='+context['replay_PATH'],'-E','ELAN_TOOLCHAIN=leanprover/lean4:v4.34.1',
                        '--working-directory='+context['guest_project'],'--','bash','-c','lake env comparator "$1"','bash',expected['config_guest_path']]
    require(command == expected_command, 'actual target command differs from unchanged runner/guard')
    require(record.get('process_result',{}).get('argv') == command, 'process result argv differs from target command')
    require(isinstance(observed_file, dict) and observed_file.get('sha256'), 'guest record identity missing')
    require(isinstance(observed_file.get('bytes'),int) and observed_file['bytes']<1_000_000,'guest target record exceeds small-record bound')
    for key, suffix in [('log', '.log'), ('source_preflight_log', '_source_preflight.log')]:
        item = record.get(key, {})
        expected_path = context['guest_records'] + f'/replay_{target}_{attempt}' + suffix
        require(item.get('path') == expected_path, 'unexpected evidence path: ' + key)
        require(re.fullmatch('[0-9a-f]{64}', item.get('sha256', '')) is not None, 'missing evidence SHA: ' + key)
    require(isinstance(record['log'].get('bytes'), int) and record['log']['bytes'] >= 0, 'raw log size missing')
    return bound


def systemd_seconds(text):
    if not isinstance(text,str):return None
    if re.fullmatch(r'\d+',text):return int(text)/1_000_000
    scale={'w':604800,'d':86400,'h':3600,'min':60,'s':1,'ms':0.001,'us':0.000001,'µs':0.000001}
    token=r'(\d+(?:\.\d+)?)\s*(min|ms|us|µs|w|d|h|s)'
    parts=re.findall(token,text)
    if not parts or re.sub(token,'',text).strip():return None
    return sum(float(value)*scale[unit] for value,unit in parts)


def classify(record, log_text, probe, bound):
    process = record.get('process_result', {})
    accepted = (record.get('status') == 'comparator_accepted' and process.get('exit_code') == 0
                and process.get('timed_out') is False and record.get('kernel_result') == 'accepted'
                and record.get('axiom_allowed_set_compliance') == 'passed' and record.get('statement_comparison') == 'passed'
                and 'Lean default kernel accepts the solution' in log_text and 'Your solution is okay!' in log_text)
    props = probe.get('unit_properties', {})
    property_query_ok = probe.get('unit_properties_command',{}).get('exit_code') == 0
    if accepted:
        if props.get('LoadState')=='not-found':return 'comparator_accepted'
        if property_query_ok and props.get('LoadState')=='loaded' and props.get('Result')=='success':return 'comparator_accepted'
        return 'unclassified_unsuccessful_attempt'
    lower = re.sub(r'\x1b\[[0-?]*[ -/]*[@-~]','',log_text).lower()
    if (property_query_ok and props.get('Result') == 'oom-kill') or any(word in lower for word in ('out of memory', 'cannot allocate memory', 'no space left on device', 'oom-kill')):
        return 'operational_resource_failure'
    if any(word in lower for word in ('kernel rejects the solution', 'kernel rejected the solution', 'quotient post-check rejects', 'unpermitted axiom', 'illegal axiom', 'statement mismatch', 'declaration mismatch')):
        return 'statement_axiom_or_kernel_failure'
    if any(word in lower for word in ('error:', 'fatal:', 'traceback (most recent call last)', 'build failed', 'some required targets logged failures', 'some required builds logged failures', 'failed to build')):
        return 'compilation_or_operational_error'
    journal = probe.get('unit_journal', {}).get('stdout', '').lower()
    runtime_duration = None
    try:
        runtime_duration = (int(props['ActiveExitTimestampMonotonic']) - int(props['ActiveEnterTimestampMonotonic'])) / 1_000_000
    except (KeyError, TypeError, ValueError):
        pass
    runtime_proven = (property_query_ok and props.get('Result') == 'timeout' and systemd_seconds(props.get('RuntimeMaxUSec'))==bound and
                      ('runtime time limit' in journal or (runtime_duration is not None and runtime_duration >= bound - 2)))
    if runtime_proven:
        return 'operational_runtime_timeout'
    # A client timeout alone does not establish why the guarded service stopped.
    return 'unclassified_unsuccessful_attempt'


class Client:
    def __init__(self, executable, logger):
        self.executable = executable; self.logger = logger

    def call(self, arguments, timeout=120, check=True):
        command = [self.executable] + list(arguments)
        started = utc()
        try:
            result = subprocess.run(command, capture_output=True, text=True, errors='replace', timeout=timeout)
            evidence = {'started_utc': started, 'finished_utc': utc(), 'argv': command,
                        'exit_code': result.returncode, 'stdout': result.stdout, 'stderr': result.stderr}
        except subprocess.TimeoutExpired as error:
            evidence = {'started_utc': started, 'finished_utc': utc(), 'argv': command, 'exit_code': None,
                        'timed_out': True, 'stdout': str(error.stdout or ''), 'stderr': str(error.stderr or '')}
        self.logger('command', evidence)
        if check:
            require(evidence.get('exit_code') == 0, 'host command failed or timed out: ' + ' '.join(arguments[:2]))
        return evidence

    def transfer(self, vm, guest_path, local_path):
        return self.call(['transfer', vm + ':' + guest_path, str(local_path)])

    def probe(self, context, target, attempt):
        result = self.call(['exec', context['vm'], '--', 'python3', '-c', GUEST_PROBE,
                            context['guest_records'], context['guest_project'], target, attempt])
        try:
            require(len(result['stdout'].encode()) < 1_000_000, 'guest probe exceeds one-megabyte record bound')
            return json.loads(result['stdout'])
        except (ValueError, TypeError) as error:
            raise Refusal('invalid guest probe response') from error

    def snapshot(self, vm, baseline):
        result = self.call(['info', baseline, '--format', 'json'])
        require(len(result['stdout'].encode())<1_000_000,'snapshot info exceeds small-record bound')
        response = json.loads(result['stdout'])
        return snapshot_metadata(response, vm, baseline), response

    def launch(self, context, target, attempt, console_path):
        command = [self.executable, 'exec', context['vm'], '--', 'python3',
                   context['guest_records'] + '/run_guarded_comparator.py', '--target', target,
                   '--attempt', attempt, '--baseline-name', context['baseline_label'], '--timeout', '21600']
        with Path(console_path).open('ab', buffering=0) as stream:
            process = subprocess.Popen(command, stdin=subprocess.DEVNULL, stdout=stream, stderr=subprocess.STDOUT,
                                       close_fds=True, start_new_session=True)
        self.logger('runner_launch', {'argv': command, 'host_pid': process.pid, 'console_log': str(console_path)})
        return process


def verify_evidence_files(directory, record, observed_file):
    directory = Path(directory)
    checks = [('guest_record.json', observed_file['sha256'], observed_file.get('bytes')),
              ('comparator.log', record['log']['sha256'], record['log']['bytes']),
              ('source_preflight.log', record['source_preflight_log']['sha256'], None)]
    identities = {}
    for filename, expected_sha, expected_size in checks:
        path = directory / filename
        require(path.is_file() and not path.is_symlink(), 'missing or symlinked preserved evidence: ' + filename)
        actual = identity(path)
        require(actual['sha256'] == expected_sha, 'preserved evidence SHA mismatch: ' + filename)
        if expected_size is not None:
            require(actual['bytes'] == expected_size, 'preserved evidence size mismatch: ' + filename)
        identities[filename] = {'bytes': actual['bytes'], 'sha256': actual['sha256']}
    require(read_small_json(directory/'guest_record.json') == record, 'preserved record contents changed')
    return identities


def preserve(client, context, probe, target, attempt, directory):
    record = probe.get('record'); observed_file = probe.get('record_file')
    bound = validate_record(record, observed_file, context, target, attempt)
    directory = Path(directory); directory.mkdir(parents=True, exist_ok=True)
    paths = [('guest_record.json', context['guest_records'] + f'/replay_{target}_{attempt}.json'),
             ('comparator.log', record['log']['path']), ('source_preflight.log', record['source_preflight_log']['path'])]
    for filename, guest_path in paths:
        final = directory / filename
        if final.exists():
            continue  # Resumption verifies existing bytes; it never silently replaces them.
        temporary = directory / (filename + '.incoming-' + uuid.uuid4().hex)
        client.transfer(context['vm'], guest_path, temporary)
        os.replace(temporary, final)
    evidence = verify_evidence_files(directory, record, observed_file)
    if (directory/'host_result.json').exists():
        previous=read_small_json(directory/'host_result.json')
        require(previous.get('preserved_files')==evidence and previous.get('target')==target and previous.get('attempt')==attempt,
                'existing host result does not bind these immutable files')
        verify_sums(directory)
        return previous,identity(directory/'host_result.json')
    atomic_json(directory / 'guest_final_probe.json', probe)
    outcome = classify(record, (directory / 'comparator.log').read_text(errors='replace'), probe, bound)
    host = {'schema': 'formal-replay-host-attempt-v1', **DISCLOSURE, 'preserved_utc': utc(),
            'target': target, 'attempt': attempt, 'classification': outcome, 'baseline': context['baseline'],
            'baseline_metadata': context['baseline_metadata'], 'host_runner_sha256': context['runner_sha256'],
            'queue_script_sha256': context['queue_script_sha256'], 'source_tool_dependency_identities': context['identities'],
            'preserved_files': evidence, 'actual_axioms': None,
            'service_completion_evidence': 'durable unchanged systemd-run exit and complete comparator/kernel output; live unit explicitly not-found' if probe.get('unit_properties',{}).get('LoadState')=='not-found' else 'durable runner result plus observed live unit properties',
            'actual_axiom_note': 'Unchanged checker establishes permitted-set compliance only; no exact accepted-export axiom set is emitted.',
            'kernel_result': record.get('kernel_result') if outcome == 'comparator_accepted' else None,
            'statement_comparison': record.get('statement_comparison') if outcome == 'comparator_accepted' else None,
            'axiom_allowed_set_compliance': record.get('axiom_allowed_set_compliance') if outcome == 'comparator_accepted' else None}
    atomic_json(directory / 'host_result.json', host)
    names=['guest_record.json','comparator.log','source_preflight.log','guest_final_probe.json','host_result.json']
    sums=''.join(digest(directory/name)+'  '+name+'\n' for name in names)
    with (directory/'SHA256SUMS.txt').open('x') as stream:stream.write(sums)
    return host, identity(directory / 'host_result.json')


def verify_sums(directory):
    directory=Path(directory)
    expected={'guest_record.json','comparator.log','source_preflight.log','guest_final_probe.json','host_result.json'}
    seen=[]
    for line in (directory/'SHA256SUMS.txt').read_text().splitlines():
        checksum,name=line.split('  ',1)
        require('/' not in name and name in expected and re.fullmatch('[0-9a-f]{64}',checksum),'unexpected checksum path/hash')
        require(digest(directory/name)==checksum,'immutable evidence checksum mismatch: '+name)
        seen.append(name)
    require(set(seen)==expected and len(seen)==len(expected),'checksum manifest is incomplete or duplicates a file')


def reset_authority(directory, result_identity):
    directory = Path(directory)
    result_path = directory / 'host_result.json'
    require(result_path.exists() and digest(result_path) == result_identity['sha256'], 'preserved host-result identity mismatch')
    host = read_small_json(result_path)
    record = read_small_json(directory/'guest_record.json')
    require(host.get('classification') in {'comparator_accepted', 'operational_runtime_timeout'}, 'unsuccessful evidence does not authorize reset')
    expected = host['preserved_files']['guest_record.json']
    verify_evidence_files(directory, record, expected)
    verify_sums(directory)
    return host


def verify_context(context, run_directory):
    root=Path(run_directory)/'context'
    for name,item in {**context['identities']['input_records'],**context['context_artifacts']}.items():
        path=root/name
        require(path.is_file() and not path.is_symlink() and path.stat().st_size==item['bytes'] and digest(path)==item['sha256'],
                'preserved queue context drift: '+name)


class HostLock:
    def __init__(self,vm):
        fixed=Path('/private/tmp') if sys.platform=='darwin' else Path('/tmp')
        directory=fixed/f'formal-replay-queue-locks-{os.getuid()}'
        try:directory.mkdir(mode=0o700)
        except FileExistsError:pass
        info=directory.lstat()
        require(stat.S_ISDIR(info.st_mode) and info.st_uid==os.getuid() and not stat.S_IMODE(info.st_mode)&0o077,
                'host lock directory must be owned, private and nonsymlinked')
        self.path=directory/(vm+'.lock')
        fd=os.open(self.path,os.O_CREAT|os.O_RDWR|os.O_NOFOLLOW,0o600)
        info=os.fstat(fd)
        if not(stat.S_ISREG(info.st_mode) and info.st_uid==os.getuid() and not stat.S_IMODE(info.st_mode)&0o077):
            os.close(fd);raise Refusal('host lock file is not owned/private/regular')
        self.stream=os.fdopen(fd,'r+')
    def __enter__(self):
        try:fcntl.flock(self.stream,fcntl.LOCK_EX|fcntl.LOCK_NB)
        except BlockingIOError:self.stream.close();raise Refusal('another host queue owns this VM lock')
        return self.stream
    def __exit__(self,*_):self.stream.close()


class Queue:
    def __init__(self, client, state_path, state, poll):
        self.client = client; self.path = Path(state_path); self.state = state; self.poll = poll; self.children = {}
        self.context = state['context']; self.root = Path(state['run_directory'])

    def save(self, **changes):
        self.state.update(changes); self.state['updated_utc'] = utc(); atomic_json(self.path, self.state)

    def event(self, name, fields=None):
        payload = {'timestamp_utc': utc(), 'event': name, **(fields or {})}
        with (self.root / 'orchestration.jsonl').open('a', encoding='utf-8') as stream:
            stream.write(json.dumps(payload, sort_keys=True) + '\n'); stream.flush()
        print(json.dumps({'timestamp_utc': payload['timestamp_utc'], 'event': name,
                          **{k: v for k, v in (fields or {}).items() if k in {'target','attempt','phase','classification','compiled_OAI_modules','reason'}}}), flush=True)

    def next_attempt(self, target, attempt, outcome):
        if outcome == 'comparator_accepted':
            return {'zeta': ['Dirichlet','001'], 'Dirichlet': ['Hecke','001'], 'Hecke': None}[target]
        if outcome == 'operational_runtime_timeout' and (target, attempt) == ('zeta','001') and not self.state.get('zeta_retry_used'):
            self.save(zeta_retry_used=True)
            return ['zeta','002']
        raise Refusal('halt after preserved ' + outcome + '; no automatic retry is authorized')

    def run(self):
        require(self.state['phase'] not in {'halted','stop_requested','restore_requested','start_requested','launch_committed'},
                'queue stopped at an ambiguous action or explicit failure; inspect state/evidence before reconciliation')
        while self.state['phase'] != 'complete':
            phase = self.state['phase']
            target, attempt = self.state['current']
            directory = self.root / 'attempts' / (target + '-' + attempt)
            if phase == 'waiting':
                probe = self.client.probe(self.context, target, attempt)
                ensure_quiescent(probe, [target, attempt])
                require(probe.get('runner_sha256') == self.context['runner_sha256'], 'guest target runner changed')
                record = probe.get('record')
                if probe.get('record_error'):
                    failures = self.state.get('record_read_failures', 0) + 1
                    self.save(record_read_failures=failures)
                    require(failures < 3, 'guest target record remains invalid JSON')
                elif record and record.get('status') != 'running':
                    # Final writer may still be exiting. Wait for complete quiescence.
                    try:
                        ensure_quiescent(probe)
                    except Refusal:
                        time.sleep(self.poll); continue
                    host, result_identity = preserve(self.client, self.context, probe, target, attempt, directory)
                    self.event('attempt_preserved', {'target':target,'attempt':attempt,'classification':host['classification']})
                    self.save(last_preserved={'directory':str(directory),'host_result':result_identity,'target':target,'attempt':attempt}, record_read_failures=0)
                    following = self.next_attempt(target, attempt, host['classification'])
                    if following is None:
                        self.save(phase='complete', completed_utc=utc()); self.event('queue_complete'); return
                    self.save(phase='ready_to_reset', following=following)
                    continue
                else:
                    active = bool(probe.get('runners') or probe.get('active_units') or probe.get('math_processes'))
                    if not active:
                        launched=self.state.get('launched_utc')
                        elapsed=(dt.datetime.now(dt.timezone.utc)-dt.datetime.fromisoformat(launched)).total_seconds() if launched else 1000
                        require(record is None and elapsed<120, 'expected attempt has no live runner/service and no completed record')
                    self.save(last_progress={'observed_utc':utc(),'target':target,'attempt':attempt,
                                             'compiled_OAI_modules':probe.get('compiled_OAI_modules'),'guest_status':record.get('status') if record else 'starting'}, record_read_failures=0)
                    self.event('waiting_for_attempt', {'target':target,'attempt':attempt,'compiled_OAI_modules':probe.get('compiled_OAI_modules')})
                time.sleep(self.poll)
                continue
            previous = self.state['last_preserved']
            reset_authority(previous['directory'], previous['host_result'])
            verify_context(self.context,self.root)
            require(digest(self.context['runner_path']) == self.context['runner_sha256'], 'current host target runner changed before baseline transition')
            saved_environment=read_small_json(Path(self.context['lane'])/'numerics/linux_vm_environment_20261013.json')
            require(saved_environment.get('vm_name') == self.context['vm'] and
                    saved_environment.get('clean_vm_baseline',{}).get('name') == self.context['baseline'],
                    'current saved environment no longer identifies this owned VM/baseline')
            live_metadata, raw_info = self.client.snapshot(self.context['vm'], self.context['baseline'])
            match_snapshot(live_metadata, self.context['baseline_metadata'])
            if phase == 'ready_to_reset':
                probe = self.client.probe(self.context, target, attempt); ensure_quiescent(probe)
                require(probe.get('record_file', {}).get('sha256') == read_small_json(Path(previous['directory'])/'host_result.json')['preserved_files']['guest_record.json']['sha256'],
                        'guest completion record changed after preservation')
                self.save(phase='stop_requested'); self.client.call(['stop',self.context['vm']]); self.save(phase='vm_stopped')
                continue
            if phase == 'vm_stopped':
                self.save(phase='restore_requested')
                self.client.call(['restore','--destructive',self.context['baseline']]); self.save(phase='baseline_restored', restore_completed_utc=utc())
                continue
            if phase == 'baseline_restored':
                self.save(phase='start_requested'); self.client.call(['start',self.context['vm']]); self.save(phase='vm_started')
                continue
            if phase == 'vm_started':
                require(digest(self.context['runner_path']) == self.context['runner_sha256'], 'host target runner changed')
                self.client.call(['transfer',self.context['runner_path'],self.context['vm']+':'+self.context['guest_records']+'/run_guarded_comparator.py'])
                self.save(phase='runner_transferred'); continue
            if phase == 'runner_transferred':
                following_target, following_attempt = self.state['following']
                probe = self.client.probe(self.context, following_target, following_attempt); ensure_quiescent(probe)
                require(probe.get('record') is None and probe.get('record_file') is None, 'next attempt already exists; refuse duplicate launch')
                require(probe.get('fresh_OAI_absent') is True and probe.get('fresh_challenge_absent') is True, 'restored mathematical build tree is not fresh')
                require(probe.get('runner_sha256') == self.context['runner_sha256'], 'retransferred guest runner SHA mismatch')
                directory = self.root/'attempts'/(following_target+'-'+following_attempt); directory.mkdir(parents=True,exist_ok=True)
                self.save(phase='launch_committed',current=[following_target,following_attempt],launched_utc=utc())
                child = self.client.launch(self.context,following_target,following_attempt,directory/'runner_console.log')
                self.children[(following_target,following_attempt)] = child
                self.save(phase='waiting',launched_host_pid=child.pid,record_read_failures=0)
                continue
            raise Refusal('unknown queue phase: ' + phase)


def build_context(args, run_directory, client):
    lane = Path(args.lane).resolve(strict=True); records = lane/'numerics'
    environment = read_small_json(records/'linux_vm_environment_20261013.json')
    require(args.vm == environment['vm_name'], 'VM argument does not match saved owned environment')
    require(args.baseline == environment['clean_vm_baseline']['name'], 'baseline argument does not match saved environment')
    require(environment['clean_vm_baseline']['status'] == 'snapshot_saved_before_mathematical_compilation', 'saved clean baseline is not established')
    values={}
    bindings={'tool_build_record':'linux_tool_build_20261013.json','dependency_record':'linux_dependencies_20261013.json',
              'isolation_record':'linux_isolation_20261013.json','trusted_cache_record':'trusted_mathlib_cache_20261013.json','integration_record':'comparator_smoke_20261013.json'}
    files=['linux_vm_environment_20261013.json','source_inventory_20261012.json','formal_statement_contracts_20261012.json']+list(bindings.values())
    context_directory=Path(run_directory)/'context';context_directory.mkdir()
    input_identities={}
    for name in files:
        path=records/name;require(path.stat().st_size<1_000_000,'input record exceeds one megabyte: '+name);item=identity(path);input_identities[name]={'bytes':item['bytes'],'sha256':item['sha256']}
        values[name]=read_small_json(path);shutil.copyfile(path,context_directory/name)
    for key,name in bindings.items():
        require(environment[key]['sha256']==input_identities[name]['sha256'] and environment[key]['bytes']==input_identities[name]['bytes'], 'saved environment binding mismatch: '+name)
    tools=values['linux_tool_build_20261013.json'];deps=values['linux_dependencies_20261013.json'];inventory=values['source_inventory_20261012.json'];contracts=values['formal_statement_contracts_20261012.json']
    require(inventory['upstream']['actual_head']==PINS['math'] and deps['upstream_pin']==PINS['math'], 'mathematical source pin mismatch')
    require(deps['package_count']==42 and deps['verified_original_patch_count']==23 and deps['status']=='all_42_pins_and_23_prescribed_patches_verified', 'dependency preparation incomplete')
    for name in ('comparator','lean4export','landrun'):
        require(tools['sources'][name]['commit']==PINS[name], 'tool source pin mismatch: '+name)
        require(tools['binaries'][name]['sha256']==environment['tool_binaries'][name]['sha256'], 'tool binary binding mismatch: '+name)
    require(values['linux_isolation_20261013.json']['all_controls_passed'] and values['linux_isolation_20261013.json']['passed_count']==16, 'isolation controls incomplete')
    runner=records/'run_guarded_comparator.py';runner_sha=digest(runner)
    metadata,raw_info=client.snapshot(args.vm,args.baseline)
    if args.baseline_info:
        require(Path(args.baseline_info).stat().st_size<1_000_000,'baseline seed record exceeds one megabyte')
        expected=snapshot_metadata(read_small_json(args.baseline_info),args.vm,args.baseline);match_snapshot(metadata,expected)
    atomic_json(context_directory/'saved_baseline_info.json',raw_info)
    shutil.copyfile(runner,context_directory/'run_guarded_comparator.py')
    shutil.copyfile(Path(__file__).resolve(),context_directory/'run_replay_queue.py')
    artifacts={name:{'bytes':(context_directory/name).stat().st_size,'sha256':digest(context_directory/name)} for name in ('saved_baseline_info.json','run_guarded_comparator.py','run_replay_queue.py')}
    targets={}
    for item in contracts['targets']:
        family={'zeta':'zeta','dirichlet':'Dirichlet','hecke':'Hecke'}[item['family']];path=item['configuration_path'];targets[family]={'configuration':item['configuration'],
          'configuration_sha256':contracts['source_files'][path]['sha256'],'config_guest_path':path.removeprefix('lean/')}
    packages=[{'name':x['name'],'commit':x['actual_head'],'patched_tree':x['actual_source_tree'],'diff_sha256':x['actual_diff_sha256']} for x in deps['packages']]
    return {'vm':args.vm,'baseline':args.baseline,'baseline_label':args.baseline.split('.',1)[1],
            'baseline_metadata':metadata,'lane':str(lane),'runner_path':str(runner),'runner_sha256':runner_sha,
            'queue_script_sha256':digest(Path(__file__).resolve()),'guest_records':environment['guest_paths']['records'],
            'context_artifacts':artifacts,
            'guest_project':environment['guest_paths']['sources']+'/lean','replay_PATH':tools['replay_PATH'],'targets':targets,
            'identities':{'upstream_commit':PINS['math'],'toolchain':environment['toolchain'],'tool_source_commits':{k:PINS[k] for k in ('comparator','lean4export','landrun')},
                          'tool_binaries':environment['tool_binaries'],'dependencies':packages,'original_manifest_sha256':deps['original_manifest_sha256'],
                          'prescribed_patch_count':23,'input_records':input_identities,'cache_trust_policy':environment['mathlib_cache_trust_policy']}}


def selftest():
    tests=[]
    def trial(name,function,refuses=False):
        try:function();passed=not refuses
        except Refusal:passed=refuses
        except Exception:passed=False
        tests.append({'name':name,'passed':passed})
    quiet={'unit_listing':{'exit_code':0},'running_records':[],'runners':[],'active_units':[],'math_processes':[]}
    running={**quiet,'runners':[{'target':'zeta','attempt':'001'}],'running_records':[{'target':'zeta','attempt':'001'}],'active_units':['rh-replay-zeta-001.service'],'math_processes':[{'cgroup':'rh-replay-zeta-001.service'}]}
    trial('adopt same active attempt without competing launch',lambda:ensure_quiescent(running,['zeta','001']))
    trial('initial runner default attempt is recognized',lambda:require(normalize_runner_cli(['python3','/home/ubuntu/rh-replay-preparation/run_guarded_comparator.py','--target','zeta','--baseline-name','pre-math-replay-20261013'])=={'target':'zeta','attempt':'001'},'default attempt not recognized'))
    trial('explicit retry attempt is retained',lambda:require(normalize_runner_cli(['python3','run_guarded_comparator.py','--target','zeta','--attempt','002'])=={'target':'zeta','attempt':'002'},'explicit attempt lost'))
    trial('active attempt forbids reset',lambda:ensure_quiescent(running),True)
    trial('different active attempt forbids adoption',lambda:ensure_quiescent(running,['Dirichlet','001']),True)
    trial('unknown compiler forbids reset',lambda:ensure_quiescent({**quiet,'math_processes':[{'cgroup':'other.service'}]}),True)
    trial('failed service inventory cannot authorize reset',lambda:ensure_quiescent({**quiet,'unit_listing':{'exit_code':1}}),True)
    with tempfile.TemporaryDirectory(prefix='replay-queue-selftest-') as directory:
        root=Path(directory);data=b'raw harmless fixture\n';pre=b'preflight\n'
        class AdoptClient:
            def __init__(self):self.probes=0;self.mutations=[]
            def probe(self,*_):
                self.probes+=1
                if self.probes>1:raise Refusal('fixture polling stopped')
                return {**running,'record':{'status':'running'},'runner_sha256':'known','compiled_OAI_modules':1}
            def call(self,*arguments,**_):self.mutations.append(arguments);raise AssertionError('mutation during adoption')
            def launch(self,*arguments):self.mutations.append(arguments);raise AssertionError('duplicate launch during adoption')
        def adoption_fixture():
            client=AdoptClient();state={'phase':'waiting','current':['zeta','001'],'context':{'runner_sha256':'known'},'run_directory':str(root)}
            queue=Queue(client,root/'adopt_state.json',state,0)
            queue.event=lambda *_:None
            try:queue.run()
            except Refusal:
                require(client.probes==2 and not client.mutations,'adoption launched/reset or refused valid initial attempt');return
            raise AssertionError('fixture failed to stop')
        trial('fake queue adopts and polls without duplicate launch',adoption_fixture)
        record={'log':{'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data)},'source_preflight_log':{'sha256':hashlib.sha256(pre).hexdigest()}}
        (root/'guest_record.json').write_text(json.dumps(record));(root/'comparator.log').write_bytes(data);(root/'source_preflight.log').write_bytes(pre)
        observed={'sha256':digest(root/'guest_record.json'),'bytes':(root/'guest_record.json').stat().st_size}
        trial('matching preserved evidence accepted',lambda:verify_evidence_files(root,record,observed))
        preserved=verify_evidence_files(root,record,observed)
        host={'classification':'comparator_accepted','preserved_files':preserved};atomic_json(root/'host_result.json',host)
        result_identity=identity(root/'host_result.json')
        class FakeClient:
            def __init__(self):self.calls=[]
            def call(self,*args,**kwargs):self.calls.append(args);raise AssertionError('a VM mutation was attempted')
        def refusal_prevents_reset():
            fake=FakeClient();state={'phase':'ready_to_reset','current':['zeta','001'],'context':{'identities':{'input_records':{}},'context_artifacts':{}},'run_directory':str(root),
                                   'last_preserved':{'directory':str(root),'host_result':result_identity}}
            q=Queue(fake,root/'state.json',state,60)
            try:q.run()
            except Refusal:
                require(not fake.calls,'reset occurred despite invalid evidence');return
            raise AssertionError('invalid evidence was accepted')
        (root/'comparator.log').write_bytes(b'wrong')
        trial('mismatched log SHA forbids reset authority',lambda:verify_evidence_files(root,record,observed),True)
        trial('fake queue never resets after SHA mismatch',refusal_prevents_reset)
        (root/'comparator.log').unlink()
        trial('missing raw log forbids reset authority',lambda:verify_evidence_files(root,record,observed),True)
        trial('fake queue never resets with missing raw log',refusal_prevents_reset)
        (root/'comparator.log').write_bytes(data)
        wrong_record=json.loads(json.dumps(record));wrong_record['log']['bytes']+=1
        trial('wrong recorded log size rejected',lambda:verify_evidence_files(root,wrong_record,observed),True)
        trial('wrong copied guest JSON hash rejected',lambda:verify_evidence_files(root,record,{'sha256':'0'*64}),True)
    failed={'status':'unsuccessful_attempt_requires_classification','process_result':{'exit_code':143,'timed_out':False}}
    timeout={'unit_properties_command':{'exit_code':0},'unit_properties':{'Result':'timeout','RuntimeMaxUSec':'2h','ActiveEnterTimestampMonotonic':'1000000','ActiveExitTimestampMonotonic':'7201000000'}}
    trial('explicit runtime cutoff classification',lambda:require(classify(failed,'',timeout,7200)=='operational_runtime_timeout','bad timeout classification'))
    trial('generic kill is not automatically timeout',lambda:require(classify(failed,'',quiet,7200)=='unclassified_unsuccessful_attempt','generic exit treated as timeout'))
    trial('resource failure takes precedence over timeout',lambda:require(classify(failed,'Out of memory',timeout,7200)=='operational_resource_failure','bad resource classification'))
    trial('kernel failure takes precedence over timeout',lambda:require(classify(failed,'Lean default kernel rejects the solution',timeout,7200)=='statement_axiom_or_kernel_failure','bad proof classification'))
    trial('compilation error before runtime cutoff never retries',lambda:require(classify(failed,'error: unsolved goals',timeout,7200)=='compilation_or_operational_error','compilation error treated as timeout'))
    trial('Lake build-failure summary prevents runtime-only retry',lambda:require(classify(failed,'Some required builds logged failures',timeout,7200)=='compilation_or_operational_error','build failure summary treated as timeout'))
    trial('wrong live runtime bound cannot authorize retry',lambda:require(classify(failed,'',{**timeout,'unit_properties':{**timeout['unit_properties'],'RuntimeMaxUSec':'6h'}},7200)=='unclassified_unsuccessful_attempt','wrong runtime bound accepted'))
    duplicate={**running,'runners':[{'pid':1,'target':'zeta','attempt':'001'},{'pid':2,'target':'zeta','attempt':'001'}]}
    trial('two identical attempt runners are rejected',lambda:ensure_quiescent(duplicate,['zeta','001']),True)
    accepted={'status':'comparator_accepted','process_result':{'exit_code':0,'timed_out':False},'kernel_result':'accepted','axiom_allowed_set_compliance':'passed','statement_comparison':'passed'}
    okay_log='Lean default kernel accepts the solution\nYour solution is okay!\n'
    trial('loaded successful unit confirms accepted durable result',lambda:require(classify(accepted,okay_log,{'unit_properties_command':{'exit_code':0},'unit_properties':{'LoadState':'loaded','Result':'success'}},7200)=='comparator_accepted','acceptance rejected'))
    trial('explicitly collected unit retains durable accepted result',lambda:require(classify(accepted,okay_log,{'unit_properties':{'LoadState':'not-found'}},7200)=='comparator_accepted','collected unit acceptance rejected'))
    trial('loaded failed unit prevents acceptance',lambda:require(classify(accepted,okay_log,{'unit_properties':{'LoadState':'loaded','Result':'timeout'}},7200)=='unclassified_unsuccessful_attempt','failed unit treated as acceptance'))
    trial('failed property query cannot authorize runtime retry',lambda:require(classify(failed,'',{**timeout,'unit_properties_command':{'exit_code':1}},7200)=='unclassified_unsuccessful_attempt','failed property query accepted'))
    fake_state={'phase':'waiting','current':['zeta','001'],'context':{},'run_directory':'/unused'}
    queue=Queue(None,'/unused',fake_state,60);queue.save=lambda **changes:fake_state.update(changes)
    trial('only initial explicit timeout gets retry',lambda:require(queue.next_attempt('zeta','001','operational_runtime_timeout')==['zeta','002'],'retry missing'))
    trial('second zeta timeout halts',lambda:queue.next_attempt('zeta','002','operational_runtime_timeout'),True)
    trial('unknown failure never retries',lambda:queue.next_attempt('zeta','001','unclassified_unsuccessful_attempt'),True)
    trial('proof rejection never retries',lambda:queue.next_attempt('zeta','001','statement_axiom_or_kernel_failure'),True)
    trial('missing named baseline rejected',lambda:snapshot_metadata({'info':{},'errors':[]},'rh-replay','rh-replay.clean'),True)
    trial('changed baseline creation rejected',lambda:match_snapshot({'created':'new'},{'created':'old'}),True)
    name='selftest-'+uuid.uuid4().hex[:12]
    def lock_fixture():
        first=HostLock(name)
        try:
            with first:
                second=HostLock(name)
                try:
                    with second:raise AssertionError('second queue acquired VM lock')
                except Refusal:pass
        finally:
            first.path.unlink(missing_ok=True)
    trial('exclusive VM lock rejects a second owner',lock_fixture)
    print(json.dumps({'selftest':tests,'all_passed':all(x['passed'] for x in tests),'VM_commands_executed':False},indent=2))
    return 0 if all(x['passed'] for x in tests) else 1


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lane',help='absolute formal_replay_crosswalk lane path')
    parser.add_argument('--archive-root',help='external host directory for durable queue state and logs')
    parser.add_argument('--vm',help='owned VM name, must match saved environment')
    parser.add_argument('--baseline',help='full instance.snapshot reference, must match saved environment')
    parser.add_argument('--baseline-info',help='optional previously saved Multipass snapshot JSON for metadata comparison')
    parser.add_argument('--poll-seconds',type=int,default=60)
    parser.add_argument('--multipass',default='multipass',help='Multipass executable path')
    parser.add_argument('--selftest',action='store_true')
    args=parser.parse_args()
    if args.selftest:return selftest()
    for name in ('lane','archive_root','vm','baseline'):
        if not getattr(args,name):parser.error('--'+name.replace('_','-')+' is required')
    require(re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,63}',args.vm) is not None,'invalid VM name')
    require(args.baseline.startswith(args.vm+'.') and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9-]{0,63}',args.baseline.split('.',1)[1]) is not None,'invalid full baseline name')
    require(15<=args.poll_seconds<=300,'poll interval must be 15–300 seconds')
    lane=Path(args.lane).resolve(strict=True);archive=Path(args.archive_root).resolve()
    protected=[lane]+[p for p in lane.parents if (p/'.git').exists() or (p/'LARGE_FILES.md').exists()]
    require(not any(archive==p or p in archive.parents for p in protected),'archive must be outside the research checkout')
    archive.mkdir(parents=True,exist_ok=True)
    with HostLock(args.vm) as lock:
        lock.seek(0);lock.truncate();lock.write(json.dumps({'pid':os.getpid(),'vm':args.vm,'archive':str(archive),'started_utc':utc()}));lock.flush()
        state_path=archive/'replay_queue_state.json'
        if state_path.exists():
            state=read_small_json(state_path);context=state['context']
            require((context['vm'],context['baseline'],context['lane'])==(args.vm,args.baseline,str(lane)),'resume arguments do not match saved queue')
            require(digest(context['runner_path'])==context['runner_sha256'],'host runner changed since queue creation')
            require(digest(Path(__file__).resolve())==context['queue_script_sha256'],'queue source changed; reconcile state before resuming')
            verify_context(context,state['run_directory'])
        else:
            run_directory=archive/('replay-queue-'+dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:8]);run_directory.mkdir()
            def initial_logger(event,evidence):
                with (run_directory/'orchestration.jsonl').open('a') as log:log.write(json.dumps({'timestamp_utc':utc(),'event':event,**evidence})+'\n')
            initial_client=Client(args.multipass,initial_logger)
            context=build_context(args,run_directory,initial_client)
            initial_probe=initial_client.probe(context,'zeta','001');ensure_quiescent(initial_probe,['zeta','001'])
            require(initial_probe.get('record') is not None,'initial zeta/001 record is absent; queue must adopt an existing attempt')
            require(initial_probe.get('runner_sha256') == context['runner_sha256'],'initial guest runner SHA mismatch')
            state={'schema':'one-off-formal-replay-queue-v1',**DISCLOSURE,'created_utc':utc(),'phase':'waiting','current':['zeta','001'],
                   'context':context,'run_directory':str(run_directory),'zeta_retry_used':False}
            atomic_json(state_path,state)
        queue=Queue(None,state_path,state,args.poll_seconds);queue.client=Client(args.multipass,queue.event)
        queue.event('queue_resumed',{'target':state['current'][0],'attempt':state['current'][1],'phase':state['phase']})
        try:queue.run()
        except Exception as error:
            queue.event('queue_halted',{'reason':str(error),'phase':queue.state['phase']})
            queue.save(phase='halted',halt_reason=str(error),halt_phase=queue.state['phase'],halted_utc=utc())
            return 1
        return 0


if __name__=='__main__':
    try:raise SystemExit(main())
    except Refusal as error:print('Queue refused: '+str(error),file=sys.stderr);raise SystemExit(1)
