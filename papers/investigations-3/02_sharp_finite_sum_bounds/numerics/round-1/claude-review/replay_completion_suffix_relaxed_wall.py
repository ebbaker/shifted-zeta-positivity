#!/usr/bin/env python3
"""Replay of the round's completion suffix with the wall budget relaxed.

Prepared for Edward Baker with LLM assistance, 17 October 2026. Model:
Claude Opus 5.5 (configured identifier claude-opus-5-5), Claude Cowork,
reasoning effort max; the serving model may differ. Standard library only.

The round's completion wrapper, complete_sharp_y_transfer_gate.py, calls
certify_leg(0, 45, 30000, 36) on patterns 172..242 of leg 0 and requires the
run to finish within 45 seconds. This script makes the same call on the same,
hash-checked engine with the same box cap (30000) and depth (36), and raises
only the wall budget, so that a slower host can reproduce the recorded
accepted-leaf digest. It changes no engine code and writes only --output.

Usage, from the repository root:
  python3 -I papers/investigations-3/02_sharp_finite_sum_bounds/numerics/round-1/claude-review/replay_completion_suffix_relaxed_wall.py --output /tmp/suffix.json
"""
import argparse, hashlib, importlib.util, json, sys
from pathlib import Path

ENGINE_SHA = 'aa6c73e0aa6672b5e6706f704b0a8dda42f1a572d9cd2a3766c91a61bebf6792'
RECORDED_DIGEST = 'f222a5c9364eb63b1c4232addb817d6197f59a334b41c78f27c1a37888f69c3b'
START = 172


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--seconds', type=float, default=5000)
    ap.add_argument('--output', type=Path, required=True)
    a = ap.parse_args()
    engine = Path(__file__).resolve().parent.parent / 'check_sharp_y_transfer_gate.py'
    if hashlib.sha256(engine.read_bytes()).hexdigest() != ENGINE_SHA:
        raise SystemExit('engine hash mismatch')
    spec = importlib.util.spec_from_file_location('gate_engine_suffix_replay', engine)
    core = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = core
    spec.loader.exec_module(core)
    original = core.Leg

    class SuffixLeg(original):
        def __init__(self, idx):
            super().__init__(idx)
            self.patterns = self.patterns[START:]

    core.Leg = SuffixLeg
    r = core.certify_leg(0, a.seconds, 30000, 36)
    summary = {k: r[k] for k in ('evaluated', 'accepted', 'unresolved_leaf_count', 'stop_reason', 'seconds',
                                 'passed', 'accepted_leaf_sha256', 'all_patterns_completed')}
    summary['matches_recorded_digest'] = r['accepted_leaf_sha256'] == RECORDED_DIGEST
    summary['wall_budget_seconds'] = a.seconds
    a.output.write_text(json.dumps(dict(summary=summary, result=r), indent=1) + '\n')
    print(json.dumps(summary))
    return 0 if summary['matches_recorded_digest'] and r['passed'] else 1


if __name__ == '__main__':
    sys.exit(main())
