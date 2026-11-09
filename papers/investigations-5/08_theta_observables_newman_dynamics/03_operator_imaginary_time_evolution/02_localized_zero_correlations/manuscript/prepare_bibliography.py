"""Select canonical records; write only the regenerable build bibliography.

8 November 2026. For Edward Baker, with substantial OpenAI Codex assistance.
Actual recorded model and effort unavailable. No canonical bibliography is edited.
"""
from pathlib import Path
import re
import subprocess
import sys

HERE = Path(__file__).resolve().parent
ROOT = Path(subprocess.check_output(['git', '-C', str(HERE), 'rev-parse', '--show-toplevel'], text=True).strip())
SOURCES = {
    HERE.parent / 'references/localized_comparison_sources.bib':
        {'Tao2020LocalZeros', 'Tao2016Harnack', 'DLMFReciprocalGammaOC', 'DLMFEulerProductOC'},
    HERE.parent / 'references/pair_marginal_sources.bib':
        {'BGST2026PairI', 'TaoVu2014LocalZeros'},
    HERE.parent.parent / 'references/complex_statistics_sources.bib': {'Montgomery1973'},
    HERE.parent.parent / 'references/correlation_hierarchy_sources.bib': {'Borodin2009DPP'},
    HERE.parent / 'references/manuscript_internal_sources.bib': None,
    HERE.parent / 'references/manuscript_e14_sources.bib': None,
}

def main():
    output = Path(sys.argv[1]).resolve()
    if ROOT / 'output/pdf' not in output.parents:
        raise SystemExit('Build bibliography must be under the repository output/pdf directory.')
    records, seen = [], set()
    for source, selected in SOURCES.items():
        parsed = re.findall(r'(?ms)^(@\w+\{([^,\s]+),.*?)(?=^@\w+\{|\Z)', source.read_text())
        keyed = {key: record for record, key in parsed}
        needed = set(keyed) if selected is None else selected
        if needed - keyed.keys():
            raise SystemExit(f'Missing keys in {source}: {needed - keyed.keys()}')
        for key in sorted(needed):
            if key in seen:
                raise SystemExit(f'Duplicate citation key: {key}')
            seen.add(key)
            records.append(keyed[key].strip())
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text('% Generated from canonical source records. Do not edit.\n\n' + '\n\n'.join(records) + '\n')
    print(f'Prepared {len(records)} bibliography entries.')

if __name__ == '__main__':
    main()
