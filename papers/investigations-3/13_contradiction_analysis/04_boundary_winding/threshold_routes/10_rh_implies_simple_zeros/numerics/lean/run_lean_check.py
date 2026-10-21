"""Run one scratch-only Lean check using the existing pinned VM cache.

This does not invoke lake, download dependencies, or modify the replay project.
"""
import glob
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

project = Path("/home/ubuntu/rh-replay-source/lean")
scratch = Path("/tmp/bw10-round20-lean")
lean = Path("/home/ubuntu/rh-replay-tools/toolchain/lean-4.34.1-linux_aarch64/bin/lean")
source = scratch / "FlatTaperTradeoff.lean"
output = scratch / "FlatTaperTradeoff.olean"
environment = os.environ.copy()
library_paths = sorted(glob.glob(str(project / ".lake/packages/*/.lake/build/lib/lean")))
library_paths.append(str(project / ".lake/build/lib/lean"))
environment["LEAN_PATH"] = ":".join(library_paths)
version = subprocess.run([str(lean), "--version"], capture_output=True, text=True, check=True)
pin = subprocess.run(
    ["git", "-C", str(project / ".lake/packages/mathlib"), "rev-parse", "HEAD"],
    capture_output=True, text=True, check=True,
)
command = [str(lean), "-o", str(output), str(source)]
result = subprocess.run(command, cwd=scratch, env=environment, capture_output=True, text=True)
report = {
    "lean_version": version.stdout.strip(),
    "mathlib_commit": pin.stdout.strip(),
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "command": command,
    "cwd": str(scratch),
    "lean_path": library_paths,
    "returncode": result.returncode,
    "stdout": result.stdout,
    "stderr": result.stderr,
    "scope": "Abstract real inner-product implication only; analytic taper and zeta premises are not formalized.",
    "project_changes": "None requested: existing project/cache only read; all outputs explicitly routed to scratch.",
}
if result.returncode == 0:
    report["olean_sha256"] = hashlib.sha256(output.read_bytes()).hexdigest()
log = scratch / "lean_check.json"
log.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
sys.exit(result.returncode)
