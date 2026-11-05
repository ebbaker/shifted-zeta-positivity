#!/usr/bin/env python3
"""Build the canonical RGD draft into the repository's ignored PDF output."""
from pathlib import Path
import datetime
import hashlib
import json
import shutil
import subprocess

here = Path(__file__).resolve().parent
repo = next(p for p in here.parents if (p / 'LARGE_FILES.md').is_file())
out = repo / 'output/pdf/radial-green-determinants'
out.mkdir(parents=True, exist_ok=True)
latexmk = shutil.which('latexmk')
if latexmk is None:
    raise SystemExit('Install a TeX distribution with latexmk and pdflatex, then retry.')
command = [latexmk, '-pdf', '-interaction=nonstopmode', '-halt-on-error',
           '-file-line-error', f'-outdir={out}', 'radial_green_determinants.tex']
subprocess.run(command, cwd=here, check=True)
log = (out / 'radial_green_determinants.log').read_text(errors='replace')
bad = [line for line in log.splitlines() if any(marker in line for marker in
       ('Overfull \\hbox', 'Overfull \\vbox', 'There were undefined references',
        'Citation `', 'Label(s) may have changed'))]
pdf = out / 'radial_green_determinants.pdf'
sources = sorted([here / 'radial_green_determinants.tex', here / 'references.bib',
                  here / 'build.py', *list((here / 'sections').glob('*.tex'))])
def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
record = {
    'built_at_utc': datetime.datetime.now(datetime.timezone.utc).isoformat(),
    'task': 'RGD-E01 r3', 'prepared_for': 'Edward Baker',
    'consolidation_model': 'gpt-6-astra', 'effort': 'ultra',
    'command': command, 'return_code': 0,
    'sources': [{'path': str(p.relative_to(here)), 'bytes': p.stat().st_size,
                 'sha256': digest(p)} for p in sources],
    'reading_copy': {'path_from_repo': str(pdf.relative_to(repo)),
                     'bytes': pdf.stat().st_size, 'sha256': digest(pdf),
                     'generated_and_git_ignored': True},
    'layout_or_reference_warnings': bad,
    'validation_limit': 'Successful TeX build and log checks do not validate mathematical claims. Visual review is recorded separately.'
}
(here / 'BUILD_RECORD.json').write_text(json.dumps(record, indent=2) + '\n')
print(pdf)
if bad:
    raise SystemExit('Inspect layout/reference warnings in BUILD_RECORD.json.')
