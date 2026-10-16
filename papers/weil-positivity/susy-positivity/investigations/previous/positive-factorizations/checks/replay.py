#!/usr/bin/env python3
"""Replay historical checkers and round-4 Markdown programs without overwriting records.

Run from any directory with Python 3 and NumPy, without -O. The output
directory must not exist; all paths in the saved record are portable.
"""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile

ATTEMPT = Path(__file__).resolve().parents[1]


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    if not __debug__:
        raise RuntimeError('Do not run certificate dependencies with Python -O.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    output = args.output_dir.resolve()
    output.mkdir(parents=True, exist_ok=False)
    historical = {str(p.relative_to(ATTEMPT)): digest(p)
                  for p in (ATTEMPT/'checks').glob('round*/diagnostics.json')}
    record = {'kind': 'fresh replay; historical outputs preserved',
              'python': platform.python_version(),
              'started_at_utc': datetime.now(timezone.utc).isoformat(), 'checks': {}}
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
    with tempfile.TemporaryDirectory(prefix='susy-replay-') as tmp:
        scratch = Path(tmp)
        shutil.copytree(ATTEMPT/'checks', scratch/'checks',
                        ignore=shutil.ignore_patterns('__pycache__', '*.pyc'))

        def run(name, argv, expected=0):
            result = subprocess.run([sys.executable, *map(str, argv)], cwd=scratch,
                                    env=env, capture_output=True, text=True)
            (output/(name+'.txt')).write_text(
                (result.stdout+result.stderr).replace(str(scratch), '<temporary-replay>'))
            ok = result.returncode == expected if expected == 0 else result.returncode != 0
            if expected != 0:
                ok = ok and 'Do not run certificate dependencies with Python -O.' in result.stderr
            record['checks'][name] = {'exit_code': result.returncode, 'passed': ok}
            if not ok:
                raise RuntimeError(f'{name} failed; see saved output')
            print(f'PASS: {name}', flush=True)

        try:
            for name, script in [('round1','check_structural_identities.py'),
                                 ('round2','check_round2.py'),('round3','check_round3.py')]:
                run(name,[scratch/'checks'/name/script])
                shutil.copy2(scratch/'checks'/name/'diagnostics.json',output/(name+'-diagnostics.json'))
            run('optimized-control',['-O',scratch/'checks/round3/check_round3.py',
                                     '--certificate-only'],expected=1)
            note=ATTEMPT/'archive/progress-reports/REPRODUCIBILITY_round4_20260911.md'
            blocks=re.findall(r'^```python\n(.*?)^```',note.read_text(),re.M|re.S)
            if len(blocks)!=2:
                raise RuntimeError('Expected two round-4 Python blocks')
            for name,source in zip(['round4-certificates','round4-diagnostics'],blocks):
                script=scratch/(name+'.py')
                script.write_text(source)
                run(name,[script,scratch])
            current={name:digest(ATTEMPT/name) for name in historical}
            if current!=historical:
                raise RuntimeError('Historical diagnostics changed')
            record['historical_diagnostics_sha256']=historical
            record['passed']=True
        finally:
            record.setdefault('passed',False)
            record['output_sha256']={p.name:digest(p) for p in sorted(output.iterdir()) if p.is_file()}
            (output/'RUN_RECORD.json').write_text(json.dumps(record,indent=2)+'\n')


if __name__=='__main__':
    main()
