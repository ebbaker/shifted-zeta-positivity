#!/usr/bin/env python3
"""Build the maintained ansatz draft; generated PDFs stay in root output/.

Prepared for Edward Baker with LLM assistance, gpt-6-astra, effort max,
25 October 2026. Production only; no mathematical computation.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess

source = Path(__file__).resolve().parent
repo = source.parents[4]
out = repo / "output/pdf/heat_density_ansatz"
build = out / ".build"
build.mkdir(parents=True, exist_ok=True)
job = "heat_density_ansatz"
latexmk = shutil.which("latexmk") or "/Library/TeX/texbin/latexmk"
result = subprocess.run(
    [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error",
     "-jobname=" + job, "-outdir=" + str(build), "main.tex"],
    cwd=source, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
)
(build / "build.stdout").write_text(result.stdout)
if result.returncode:
    print(result.stdout[-10000:])
    raise SystemExit(result.returncode)
log = (build / (job + ".log")).read_text(errors="replace")
warnings = [line for line in log.splitlines()
            if re.search(r"Overfull|Underfull|LaTeX Warning|Package .* Warning", line)]
target = out / (job + ".pdf")
shutil.copy2(build / (job + ".pdf"), target)
print(json.dumps({
    "pdf": str(target), "bytes": target.stat().st_size,
    "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
    "warnings": warnings
}, indent=2))
