"""Build the working manuscript into the ignored repository PDF directory."""
import os
from pathlib import Path
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "LARGE_FILES.md").is_file())
JOB = "explicit_zero_gap_transport"
OUTPUT = ROOT / "output" / "pdf" / "explicit-zero-gap-transport"


def main():
    OUTPUT.mkdir(parents=True, exist_ok=True)
    env = os.environ.copy()
    refs = [str(HERE.parent / "references"), str(HERE.parent.parent / "references")]
    env["BIBINPUTS"] = os.pathsep.join(refs + [env.get("BIBINPUTS", "")])
    with tempfile.TemporaryDirectory(dir=OUTPUT) as temp:
        subprocess.run(["latexmk", "-pdf", "-interaction=nonstopmode", "-halt-on-error",
                        "-file-line-error", f"-jobname={JOB}", f"-outdir={temp}", "main.tex"],
                       cwd=HERE, env=env, check=True)
        os.replace(Path(temp) / f"{JOB}.pdf", OUTPUT / f"{JOB}.pdf")
    print(OUTPUT / f"{JOB}.pdf")


if __name__ == "__main__":
    main()
