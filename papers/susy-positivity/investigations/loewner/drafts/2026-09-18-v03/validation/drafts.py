#!/usr/bin/env python3
"""Record reviewed manuscript builds and preserve complete draft snapshots.

Standard library only. Hash checks establish identity, not mathematical or
visual correctness. No command rewrites an existing historical snapshot.
"""
from pathlib import Path
import argparse
from datetime import date
import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CHECKS = {
    "check_contraction_margin.py": "contraction-margin-checks.json",
    "check_beta_realization.py": "beta-realization-checks.json",
}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition, message):
    if not condition:
        raise ValueError(message)


def local_path(base, name):
    path = (base / name).resolve()
    require(path.is_relative_to(base.resolve()), f"Path escapes package: {name}")
    require(path.is_file(), f"Missing package file: {name}")
    return path


def tex_sources(base):
    pending = ["manuscript.tex"]
    seen = set()
    while pending:
        name = pending.pop()
        if name in seen:
            continue
        path = local_path(base, name)
        seen.add(name)
        text = re.sub(r"(?m)(?<!\\)%.*$", "", path.read_text())
        for dep in re.findall(r"\\(?:input|include)\{([^}]+)\}", text):
            if not Path(dep).suffix:
                dep += ".tex"
            require(Path(dep).name.lower() not in {"background.tex", "background_section.tex"},
                    f"Shared background dependency is not allowed: {dep}")
            pending.append(dep)
    return sorted(seen)


def verify_record(base):
    record = json.loads((base / "BUILD_RECORD.json").read_text())
    expected_sources = tex_sources(base)
    require(sorted(record["source_sha256"]) == expected_sources,
            f"TeX dependency list differs in {base}")
    for group in ("source_sha256", "supporting_sha256"):
        for name, want in record[group].items():
            require(digest(local_path(base, name)) == want,
                    f"Changed recorded file: {base / name}")
    pdf = local_path(base, record["pdf"])
    require(digest(pdf) == record["pdf_sha256"], f"PDF hash differs in {base}")
    require(pdf.stat().st_size == record["pdf_bytes"], f"PDF size differs in {base}")
    return record


def record_build(args):
    date.fromisoformat(args.date)
    require(args.pages > 0, "Page count must be positive")
    require(args.review_note.strip(), "Describe the completed visual review")
    source = (ROOT / "manuscript.tex").read_text()
    version = re.search(r"\\newcommand\{\\draftversion\}\{([^}]+)\}", source)
    require(version is not None, "Missing manuscript draft version")
    pdf = local_path(ROOT, "manuscript.pdf")
    built_pdf = local_path(ROOT, "build/manuscript.pdf")
    require(digest(pdf) == digest(built_pdf), "Deliverable differs from build PDF")
    log = local_path(ROOT, "build/manuscript.log").read_text(errors="replace")
    require(not re.search(r"undefined|Overfull|multiply defined", log, re.I),
            "Build log has unresolved references or overflow warnings")
    require(re.search(rf"Output written.*\({args.pages} pages?[,)]", log) is not None,
            "Supplied page count differs from the build log")
    sources = tex_sources(ROOT)
    for name in sources:
        require(local_path(ROOT, name).stat().st_mtime <= built_pdf.stat().st_mtime,
                f"Source changed after the PDF build: {name}")
    inputs = (ROOT / "build/manuscript.fls").read_text().splitlines()
    manuscript_inputs = {str((ROOT / name).resolve()) for name in sources}
    for line in inputs:
        if line.startswith("INPUT ") and line[6:].endswith(".tex"):
            path = (ROOT / line[6:]).resolve()
            # System TeX support files may be outside the package.
            if path.is_relative_to(ROOT):
                require(str(path) in manuscript_inputs,
                        f"Unrecorded local TeX input: {path}")
    supported = ["BUILD.md", "validation/drafts.py"]
    for program, result in CHECKS.items():
        supported.extend([f"numerics/{program}", f"numerics/records/{result}"])
    record = {
        "schema": 1,
        "title": "The Markov part of the shifted Weil transfer",
        "version": version.group(1),
        "review_date": args.date,
        "pages": args.pages,
        "pdf": "manuscript.pdf",
        "pdf_bytes": pdf.stat().st_size,
        "pdf_sha256": digest(pdf),
        "source_sha256": {name: digest(local_path(ROOT, name)) for name in sources},
        "supporting_sha256": {name: digest(local_path(ROOT, name)) for name in supported},
        "build_command": "latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build manuscript.tex",
        "engine": log.splitlines()[0],
        "visual_review": args.review_note.strip(),
        "scope": "Reviewed file identity and build provenance; not a proof certificate.",
    }
    (ROOT / "BUILD_RECORD.json").write_text(json.dumps(record, indent=2) + "\n")
    print(f"Recorded reviewed version {record['version']} ({args.pages} pages).")


def verify_snapshot(base):
    snapshot = json.loads((base / "SNAPSHOT.json").read_text())
    for name, want in snapshot["sha256"].items():
        require(digest(local_path(base, name)) == want,
                f"Historical snapshot changed: {base / name}")
    verify_record(base)


def save_snapshot(args):
    require(re.fullmatch(r"\d{4}-\d{2}-\d{2}-v\d+[a-z0-9-]*", args.name),
            "Use a dated version name such as 2026-09-14-v01")
    date.fromisoformat(args.name[:10])
    record = verify_record(ROOT)
    archive = ROOT / "drafts"
    archive.mkdir(exist_ok=True)
    destination = archive / args.name
    require(not destination.exists(), f"Refusing to overwrite {destination}")
    names = sorted(set(record["source_sha256"]) | set(record["supporting_sha256"])
                   | {"BUILD_RECORD.json", "manuscript.pdf", ".gitignore"})
    with tempfile.TemporaryDirectory(prefix="draft-stage-") as temporary:
        prepared = Path(temporary)
        for name in names:
            source = local_path(ROOT, name)
            require(source.stat().st_size <= 1048576, f"File exceeds 1 MiB: {name}")
            target = prepared / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        (prepared / "README.md").write_text(
            f"# Draft {record['version']} - {record['review_date']}\n\n"
            "Historical snapshot of *The Markov part of the shifted Weil transfer*.\n\n"
            "The [PDF](manuscript.pdf), [TeX entry point](manuscript.tex), sources,\n"
            "[build guide](BUILD.md), checks and records form a standalone package.\n"
            "Copy this directory elsewhere before rebuilding; preserve this snapshot unchanged.\n\n"
            "`SNAPSHOT.json` pins the saved files. `BUILD_RECORD.json` identifies the\n"
            "reviewed source/PDF pair. These records establish identity, not correctness.\n"
        )
        names.append("README.md")
        snapshot = {
            "schema": 1, "name": args.name, "version": record["version"],
            "review_date": record["review_date"],
            "sha256": {name: digest(prepared / name) for name in sorted(names)},
        }
        (prepared / "SNAPSHOT.json").write_text(json.dumps(snapshot, indent=2) + "\n")
        verify_snapshot(prepared)
        shutil.copytree(prepared, destination)
    print(f"Saved {destination.relative_to(ROOT)}; existing versions were preserved.")


def check_package(args):
    record = verify_record(ROOT)
    if (ROOT / "SNAPSHOT.json").exists():
        verify_snapshot(ROOT)
    snapshots = sorted((ROOT / "drafts").glob("*/SNAPSHOT.json"))
    for snapshot in snapshots:
        verify_snapshot(snapshot.parent)
    total = 0
    if args.replay:
        for program, result in CHECKS.items():
            expected = json.loads((ROOT / "numerics/records" / result).read_text())
            output = subprocess.check_output(
                [sys.executable, str(ROOT / "numerics" / program)], cwd=ROOT, text=True)
            actual = json.loads(output)
            require(actual == expected, f"Replay differs from preserved record: {program}")
            total += actual["total_checks"]
    print(json.dumps({"status": "passed", "version": record["version"],
                      "snapshots": len(snapshots), "replayed_cases": total,
                      "scope": "Package identity and optional finite algebra replay."}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build = commands.add_parser("record", help="Record a build after actual visual review")
    build.add_argument("--date", required=True)
    build.add_argument("--pages", type=int, required=True)
    build.add_argument("--review-note", required=True)
    build.set_defaults(action=record_build)
    save = commands.add_parser("save", help="Save a new complete snapshot without overwriting")
    save.add_argument("name")
    save.set_defaults(action=save_snapshot)
    check = commands.add_parser("check", help="Verify current and archived package identity")
    check.add_argument("--replay", action="store_true")
    check.set_defaults(action=check_package)
    args = parser.parse_args()
    try:
        args.action(args)
    except (ValueError, OSError, KeyError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"FAIL: {exc}\n")


if __name__ == "__main__":
    main()
