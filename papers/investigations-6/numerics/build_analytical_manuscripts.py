#!/usr/bin/env python3
"""Build the four analytical manuscripts, keeping every PDF outside the repo.

14 November 2026. Prepared for Edward Baker with OpenAI Codex LLM assistance.
Coordinator model/effort are not exposed. This is a document build helper,
not a numerical experiment. Requires latexmk, pdflatex and pdfinfo on PATH.
"""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
BASE = HERE.parent
BRANCHES = (
    ("01_qtt_newman_flow", "qtt", "qtt_newman_flow"),
    ("02_jacobi_chain_height_flow", "jch", "jacobi_chain_height_flow"),
    ("03_volterra_coefficient_dynamics", "vcd", "volterra_coefficient_dynamics"),
    ("04_exact_infinite_tensor_products", "itp", "exact_infinite_tensor_products"),
)


def identity(path):
    data = path.read_bytes()
    return {"path": str(path), "bytes": len(data),
            "sha256": hashlib.sha256(data).hexdigest()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path,
                        help="External reading-copy directory; default is a new temp directory")
    parser.add_argument("--record", type=Path, required=True,
                        help="Small JSON build record, normally in parent numerics")
    parser.add_argument("--branch", choices=[b[1] for b in BRANCHES],
                        help="Build only one branch, otherwise build all four")
    args = parser.parse_args()
    out = (args.output_dir or Path(tempfile.mkdtemp(prefix="tn6-manuscripts-"))).resolve()
    if out == ROOT or out.is_relative_to(ROOT):
        parser.error("the author requires every PDF and build product outside the repository")
    latexmk, pdfinfo = shutil.which("latexmk"), shutil.which("pdfinfo")
    if not latexmk or not pdfinfo:
        parser.error("latexmk and pdfinfo are required; no dependencies are installed automatically")
    selected = [b for b in BRANCHES if args.branch is None or b[1] == args.branch]
    for name, _, _ in selected:
        if not (BASE / name / "manuscript/main.tex").is_file():
            parser.error(f"manuscript source is missing: {name}")
    out.mkdir(parents=True, exist_ok=True)
    record = {
        "date_utc": datetime.now(timezone.utc).isoformat(),
        "intended_author": "Edward Baker", "assistance": "OpenAI Codex LLM",
        "coordinator_model_and_effort": "unavailable",
        "purpose": "Manuscript compilation and output identities, not mathematical validation",
        "external_output_root": str(out),
        "latexmk_version": subprocess.run([latexmk, "-v"], capture_output=True,
                                           text=True, check=True, timeout=10).stdout.strip(),
        "manuscripts": [],
    }
    for name, short, job in selected:
        source = BASE / name / "manuscript"
        destination = out / short
        destination.mkdir(parents=True, exist_ok=True)
        command = [latexmk, "-norc", "-pdf", "-interaction=nonstopmode",
                   "-halt-on-error", "-file-line-error", f"-outdir={destination}",
                   f"-jobname={job}", "main.tex"]
        run = subprocess.run(command, cwd=source, capture_output=True, text=True,
                             timeout=180)
        console = destination / "build.console.txt"
        console.write_text(run.stdout + "\n" + run.stderr)
        if run.returncode:
            raise SystemExit(f"{short} build failed; see {console}")
        pdf = destination / f"{job}.pdf"
        info = subprocess.run([pdfinfo, str(pdf)], capture_output=True,
                              text=True, check=True, timeout=20).stdout
        log = (destination / f"{job}.log").read_text(errors="replace")
        warnings = [line.strip() for line in log.splitlines()
                    if re.search(r"Overfull|Underfull|undefined|LaTeX Warning|Package .* Warning", line)]
        sources = []
        for p in sorted(source.rglob("*")):
            if p.is_file() and p.suffix in (".tex", ".bib", ".sty", ".cls"):
                item = identity(p)
                item["path"] = str(p.relative_to(ROOT))
                sources.append(item)
        pages = re.search(r"^Pages:\s*(\d+)", info, re.MULTILINE)
        record["manuscripts"].append({
            "branch": name, "sources": sources, "pdf": identity(pdf),
            "pages": int(pages.group(1)) if pages else None,
            "command": command, "working_directory": str(source.relative_to(ROOT)),
            "console_log": str(console), "warnings": warnings,
        })
        print(f"{short}: {pdf}", flush=True)
    args.record.parent.mkdir(parents=True, exist_ok=True)
    args.record.write_text(json.dumps(record, indent=2) + "\n")
    print(f"Build record: {args.record}")


if __name__ == "__main__":
    main()
