#!/usr/bin/env python3
"""Build the working PDF strictly outside the repository.

Prepared for Edward Baker with OpenAI Codex assistance, 13 November 2026.
Actual lead model/effort unavailable in the recorded configuration.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import subprocess


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    source = Path(__file__).resolve().parent
    repo = next(p for p in source.parents if (p / "LARGE_FILES.md").is_file())
    output = args.output_dir.expanduser().resolve()
    if output == repo or repo in output.parents:
        parser.error("PDF and compilation products must be outside this repository.")
    output.mkdir(parents=True, exist_ok=True)
    if shutil.which("latexmk") is None:
        parser.error("latexmk and a LaTeX installation are required.")
    subprocess.run([
        "latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
        "-file-line-error", f"-outdir={output}",
        "-jobname=gnp_boundary_bootstrap_20261113", "main.tex",
    ], cwd=source, check=True)
    print(output / "gnp_boundary_bootstrap_20261113.pdf")


if __name__ == "__main__":
    main()
