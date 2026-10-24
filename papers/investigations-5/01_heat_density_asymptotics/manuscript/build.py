#!/usr/bin/env python3
"""Build the maintained manuscript into the repository's ignored output tree.

Prepared for Edward Baker with substantial LLM assistance.
gpt-6-astra, recorded effort max, 24 October 2026.
"""
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess

source = Path(__file__).resolve().parent
repo = source.parents[3]
out = repo / "output/pdf/heat_density_asymptotics"
build = out / ".build"
build.mkdir(parents=True, exist_ok=True)
driver = build / "driver.tex"
driver.write_text(
    "\\def\\researchroot{\\detokenize{" + str(repo) + "}}\n"
    "\\input{main.tex}\n"
)
latexmk = shutil.which("latexmk") or "/Library/TeX/texbin/latexmk"
job = "heat_density_asymptotics"
result = subprocess.run(
    [latexmk, "-pdf", "-interaction=nonstopmode", "-halt-on-error",
     "-jobname="+job, "-outdir="+str(build), str(driver)],
    cwd=source, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
)
(build / "build.stdout").write_text(result.stdout)
if result.returncode:
    print(result.stdout[-12000:])
    raise SystemExit(result.returncode)
log = (build / (job+".log")).read_text(errors="replace")
warnings = [line for line in log.splitlines()
            if re.search(r"Overfull|Underfull|LaTeX Warning|Package .* Warning", line)]
if warnings:
    raise SystemExit("Build needs review:\n"+"\n".join(warnings))
target = out / (job+".pdf")
shutil.copy2(build / (job+".pdf"), target)
print(json.dumps({
    "pdf": str(target),
    "bytes": target.stat().st_size,
    "sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
    "warnings": warnings
}, indent=2))
