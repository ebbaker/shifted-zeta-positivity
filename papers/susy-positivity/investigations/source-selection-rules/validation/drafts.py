#!/usr/bin/env python3
"""Replay the investigation's check programmes against their preserved records.

Standard library only. Hash and replay checks establish identity and
reproducibility, not mathematical correctness.

This investigation has no manuscript yet, so the `record` and `save` commands of
the sibling investigations are not available here; they will be added, with the
same interface, when a manuscript exists. Until then `check --replay` is the
whole tool: it runs every programme registered in CHECKS and requires its output
to equal the preserved record byte for byte after JSON parsing.
"""
from pathlib import Path
import argparse
import hashlib
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKS = {
    "check_density_symbol.py": "density-symbol-checks.json",
    "check_symbol_split.py": "symbol-split-checks.json",
    "check_qweyl_relations.py": "qweyl-relations-checks.json",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def check_package(args):
    total, records = 0, {}
    for program, result in CHECKS.items():
        record_path = ROOT / "numerics/records" / result
        require(record_path.is_file(), f"Missing preserved record: {result}")
        expected = json.loads(record_path.read_text())
        records[result] = digest(record_path)
        if args.replay:
            output = subprocess.check_output(
                [sys.executable, str(ROOT / "numerics" / program)], cwd=ROOT, text=True)
            actual = json.loads(output)
            require(actual == expected, f"Replay differs from preserved record: {program}")
        total += expected["total_checks"]
    print(json.dumps({
        "status": "passed",
        "programs": len(CHECKS),
        "replayed": bool(args.replay),
        "recorded_cases": total,
        "record_sha256": records,
        "scope": "Reproducibility of the finite checks. Not a proof certificate, "
                 "and not a statement about the Weil criterion.",
    }, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("check", help="Verify the preserved records")
    check.add_argument("--replay", action="store_true")
    check.set_defaults(action=check_package)
    args = parser.parse_args()
    try:
        args.action(args)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
