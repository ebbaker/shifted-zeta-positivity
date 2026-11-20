"""Build the working PDF in the repository's ignored output folder."""

from pathlib import Path
import os
import subprocess
import tempfile

HERE = Path(__file__).resolve().parent
REPO = next(parent for parent in HERE.parents if (parent / 'LARGE_FILES.md').is_file())
DESTINATION = REPO / 'output/pdf/jacobi-integer-hierarchy'
JOB = 'jacobi_integer_hierarchy'


def main():
    DESTINATION.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(dir=DESTINATION) as temporary:
        subprocess.run(
            ['latexmk', '-pdf', '-interaction=nonstopmode', '-halt-on-error',
             '-file-line-error', f'-jobname={JOB}', f'-outdir={temporary}', 'main.tex'],
            cwd=HERE, check=True,
        )
        pdf = Path(temporary) / f'{JOB}.pdf'
        os.replace(pdf, DESTINATION / pdf.name)
    print(DESTINATION / f'{JOB}.pdf')


if __name__ == '__main__':
    main()
