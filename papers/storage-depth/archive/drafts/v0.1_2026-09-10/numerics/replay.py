#!/usr/bin/env python3
"""Supported replay/regeneration entry point; original research is immutable.

Inputs are checked and staged in a temporary copy. Only changed results are
exported. Generated data receive byte and canonical matrix-content hashes.
"""
import argparse
import datetime
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import archive_io as io

HERE = Path(__file__).resolve().parent
HISTORY = HERE / "history"
CLOSURE = "quarter-step-closure-20260910"
MATRIX = f"history/{CLOSURE}/closure_256_32.matrices.json.gz"
ACTIONS = ("verify", "checks", "relative", "spatial-sign", "shift",
           "rebuild", "rebuild-initial", "residual", "generator", "storage",
           "whole-step", "global", "new-slab")

def verify_history():
    expected = json.loads((HERE / "HISTORY_RECORD.json").read_text())["sha256"]
    for rel, digest in expected.items():
        if io.file_hash(HISTORY / rel) != digest:
            raise ValueError(f"Historical file hash mismatch: {rel}")
    return expected

def command_list(action):
    if action == "checks":
        return [(CLOSURE, ["verify_arithmetic_partition.py"]),
                (CLOSURE, ["cross_checks.py"])]
    if action == "relative":
        return [(CLOSURE, ["relative_closure.py", "--archive",
                "closure_256_32.matrices.json.gz", "--theta", "0.9",
                "--output", "relative_256_32.json"])]
    if action == "spatial-sign":
        return [(CLOSURE, ["spatial_sign.py", "--archive",
                "closure_256_32.matrices.json.gz", "--output", "spatial_sign_replay.json"])]
    if action == "shift":
        return [(CLOSURE, ["path_corollary.py"])]
    if action in ("rebuild", "rebuild-initial"):
        old = "256" if action == "rebuild" else "128"
        script = "close_complement.py" if old == "256" else "close_complement_initial.py"
        return [(CLOSURE, [script, "--old", old, "--new", "32", "--degree", "320",
                "--log-degree", "100", "--bits", "6144", "--cells", "512",
                "--floor", "1e-33", "--output", f"closure_{old}_32.json"])]
    if action == "residual":
        return [("quarter-step-20260910", ["central_residual.py",
                "--output", "residual_128_32.json"])]
    if action == "generator":
        return [("critical-path-20260910", ["certify_generator_witness.py",
                "--vector-record", "generator_witness_log7.json", "--bits", "2048",
                "--output", "generator_witness_log7_replay.json"])]
    if action == "storage":
        return [("cumulative-path-20260910", ["certify_vector_storage.py",
                "--degree", "240", "--bits", "7168",
                "--output", "storage_log7_1em11_replay.json"])]
    if action == "whole-step":
        return [("log7-log8-extension-20260910", ["extension_storage.py",
                "--old", "128", "--new", "32", "--degree", "280",
                "--bits", "6144", "--shift", "1e-11",
                "--output", "extension_128_32_1em11.json"])]
    if action == "global":
        return [("quarter-step-20260910", ["reference_check.py",
                "--n", "256", "--degree", "260", "--bits", "3072",
                "--floor", "1e-31", "--output", "reference_256.json"])]
    if action == "new-slab":
        return [("log7-log8-extension-20260910", ["new_slab_bound.py"])]
    return []

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("action", choices=ACTIONS)
    p.add_argument("--output-dir", type=Path,
                   help="A new folder for results; required except for verify")
    p.add_argument("--archives", action="store_true",
                   help="For verify: also check all three external matrix archives")
    p.add_argument("--use-cache", action="store_true",
                   help="For rebuild only: verify and stage the historical old-depth cache")
    args = p.parse_args()
    if not __debug__ or os.environ.get("PYTHONOPTIMIZE"):
        p.error("Python assertions must remain enabled; do not use -O or PYTHONOPTIMIZE")
    expected = verify_history()
    report = {"action": args.action, "utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
              "historical_files_verified": len(expected), "archives_verified": [],
              "commands": [], "exit_success": False,
              "scope": "Integrity and/or arithmetic replay; no independent normalization audit."}
    if args.action == "verify":
        if args.archives:
            for record in io.catalog():
                io.verify(record["path"])
                report["archives_verified"].append(record["path"])
        report["exit_success"] = True
        print(json.dumps(report, indent=2))
        return
    if args.output_dir is None:
        p.error("--output-dir is required for a replay; choose a new folder")
    output = args.output_dir.resolve()
    if output.exists():
        p.error("Output folder already exists; choose a new folder to preserve prior results")
    output.mkdir(parents=True)
    with tempfile.TemporaryDirectory(prefix="storage-depth-replay-") as temp:
        work = Path(temp)
        shutil.copytree(HISTORY, work / "history",
                        ignore=shutil.ignore_patterns("*.json.gz", "__pycache__", "*.pyc"))
        selected = []
        if args.action in ("relative", "spatial-sign", "shift"):
            selected = [MATRIX]
        elif args.action in ("rebuild", "rebuild-initial") and args.use_cache:
            old = 256 if args.action == "rebuild" else 128
            selected = [f"history/{CLOSURE}/old_{old}_320_6144.json.gz"]
        staged = {}
        for rel in selected:
            source = io.verify(rel)
            destination = work / rel
            shutil.copy2(source, destination)
            # Verify the staged bytes too, before any historical consumer runs.
            digest = io.file_hash(source)
            if io.file_hash(destination) != digest:
                raise ValueError("Staged archive hash mismatch")
            staged[rel] = digest
            report["archives_verified"].append(rel)
        if args.action == "spatial-sign":
            shutil.copy2(HERE / "spatial_sign.py", work / "history" / CLOSURE / "spatial_sign.py")
        try:
            with (output / "run.log").open("w") as log:
                for folder, argv in command_list(args.action):
                    cmd = [sys.executable, "-B", *argv]
                    report["commands"].append({"cwd": f"history/{folder}", "argv": cmd[1:]})
                    result = subprocess.run(cmd, cwd=work / "history" / folder,
                                            stdout=log, stderr=subprocess.STDOUT, check=False)
                    if result.returncode:
                        raise RuntimeError(f"Replay exited {result.returncode}; see {output / 'run.log'}")
            report["exit_success"] = True
        finally:
            changed = []
            generated_archives = []
            for src in sorted((work / "history").rglob("*")):
                if not src.is_file() or "__pycache__" in src.parts or src.suffix == ".pyc":
                    continue
                rel = src.relative_to(work).as_posix()
                historical_rel = src.relative_to(work / "history").as_posix()
                digest = io.file_hash(src)
                if digest == expected.get(historical_rel) or digest == staged.get(rel):
                    continue
                if src.suffix == ".py":
                    # Sources are already supplied; the extra validator lives at numerics/.
                    continue
                dest = output / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dest)
                changed.append({"path": rel, "sha256": digest, "bytes": src.stat().st_size})
                if src.name.endswith(".json.gz"):
                    generated_archives.append(io.describe(src, rel))
            report["exported_files"] = changed
            report["generated_archives"] = generated_archives
            if generated_archives:
                (output / "ARCHIVE_RECORDS.json").write_text(json.dumps({
                    "canonicalization": json.loads(io.CATALOG.read_text())["canonicalization"],
                    "archives": generated_archives}, indent=2) + "\n")
            (output / "RUN_RECORD.json").write_text(json.dumps(report, indent=2) + "\n")
            (output / "SHA256SUMS.txt").write_text("".join(
                f"{io.file_hash(path)}  {path.relative_to(output).as_posix()}\n"
                for path in sorted(output.rglob("*")) if path.is_file()
                and path.name != "SHA256SUMS.txt"))
    print(f"Replay completed: {output}")
    print("Read the result record for its mathematical PASS/FAIL and domain scope.")

if __name__ == "__main__":
    main()
