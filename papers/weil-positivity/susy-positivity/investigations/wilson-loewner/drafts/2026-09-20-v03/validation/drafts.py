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
import math
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
CHECKS = {
    "check_smooth_variation.py": "smooth-variation-checks.json",
    "check_defect_endpoints.py": "defect-endpoint-checks.json",
    "check_reflected_junction.py": "reflected-junction-checks.json",
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


def tex_sources(base, entry="manuscript.tex"):
    pending = [entry]
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


def verify_document(base, document, entry):
    expected_sources = tex_sources(base, entry)
    require(sorted(document["source_sha256"]) == expected_sources,
            f"TeX dependency list differs for {entry} in {base}")
    for name, want in document["source_sha256"].items():
        require(digest(local_path(base, name)) == want,
                f"Changed recorded file: {base / name}")
    pdf = local_path(base, document["pdf"])
    require(digest(pdf) == document["pdf_sha256"], f"PDF hash differs: {pdf}")
    require(pdf.stat().st_size == document["pdf_bytes"], f"PDF size differs: {pdf}")


def verify_record(base):
    record = json.loads((base / "BUILD_RECORD.json").read_text())
    require(record["schema"] in (1, 2), "Unsupported build-record schema")
    verify_document(base, record, "manuscript.tex")
    companions = record.get("companions", {})
    expected = {"supplementary-information"} if (base / "supplementary-information.tex").exists() else set()
    require(set(companions) == expected, "Companion document inventory differs")
    for name, document in companions.items():
        require(document["entry"] == name + ".tex", "Companion entry point differs")
        require(document["version"] == record["version"], "Document versions differ")
        verify_document(base, document, document["entry"])
    for name, want in record["supporting_sha256"].items():
        require(digest(local_path(base, name)) == want,
                f"Changed recorded file: {base / name}")
    return record


def reviewed_document(entry, pages):
    require(pages is not None and pages > 0, f"Page count must be positive: {entry}")
    stem = Path(entry).stem
    source = local_path(ROOT, entry).read_text()
    version = re.search(r"\\newcommand\{\\draftversion\}\{([^}]+)\}", source)
    require(version is not None, f"Missing draft version: {entry}")
    pdf = local_path(ROOT, stem + ".pdf")
    built_pdf = local_path(ROOT, "build/" + stem + ".pdf")
    require(digest(pdf) == digest(built_pdf), f"Deliverable differs from build: {pdf}")
    log = local_path(ROOT, "build/" + stem + ".log").read_text(errors="replace")
    require(not re.search(r"undefined|Overfull|multiply defined", log, re.I),
            f"Build log has unresolved references or overflow warnings: {entry}")
    require(re.search(rf"Output written.*\({pages} pages?[,)]", log) is not None,
            f"Supplied page count differs from the build log: {entry}")
    sources = tex_sources(ROOT, entry)
    for name in sources:
        require(local_path(ROOT, name).stat().st_mtime <= built_pdf.stat().st_mtime,
                f"Source changed after the PDF build: {name}")
    inputs = local_path(ROOT, "build/" + stem + ".fls").read_text().splitlines()
    manuscript_inputs = {str((ROOT / name).resolve()) for name in sources}
    for line in inputs:
        if line.startswith("INPUT ") and line[6:].endswith(".tex"):
            path = (ROOT / line[6:]).resolve()
            if path.is_relative_to(ROOT):
                require(str(path) in manuscript_inputs,
                        f"Unrecorded local TeX input: {path}")
    return {
        "entry": entry,
        "version": version.group(1),
        "pages": pages,
        "pdf": pdf.name,
        "pdf_bytes": pdf.stat().st_size,
        "pdf_sha256": digest(pdf),
        "source_sha256": {name: digest(local_path(ROOT, name)) for name in sources},
        "build_command": f"latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build {entry}",
        "engine": log.splitlines()[0],
    }


def record_build(args):
    date.fromisoformat(args.date)
    require(args.review_note.strip(), "Describe the completed visual review")
    document = reviewed_document("manuscript.tex", args.pages)
    companions = {}
    if (ROOT / "supplementary-information.tex").exists():
        companion = reviewed_document("supplementary-information.tex", args.supplement_pages)
        require(companion["version"] == document["version"], "Document versions differ")
        companions["supplementary-information"] = companion
    supported = ["BUILD.md", "validation/drafts.py", "MANUSCRIPT_SOURCES.json"]
    for program, result in CHECKS.items():
        supported.extend([f"numerics/{program}", f"numerics/records/{result}"])
        validate_result(json.loads((ROOT / "numerics/records" / result).read_text()))
    record = {
        "schema": 2,
        "title": "Shifted-zeta evolution and Wilson lines",
        **document,
        "review_date": args.date,
        "companions": companions,
        "supporting_sha256": {name: digest(local_path(ROOT, name)) for name in supported},
        "visual_review": args.review_note.strip(),
        "scope": "Visual build review and file identity; not independent mathematical review or a proof certificate.",
        "authoring": "OpenAI GPT-6 (Codex), for Edward Baker",
        "numerical_replay": "Same parameters, cases, thresholds and passing inequalities; floating values may differ.",
    }
    (ROOT / "BUILD_RECORD.json").write_text(json.dumps(record, indent=2) + "\n")
    counts = [document["pages"]] + [d["pages"] for d in companions.values()]
    print(f"Recorded reviewed version {record['version']} (page counts: {counts}).")


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
    names = set(record["source_sha256"]) | set(record["supporting_sha256"])
    names.update({"BUILD_RECORD.json", record["pdf"], ".gitignore"})
    for document in record.get("companions", {}).values():
        names.update(document["source_sha256"])
        names.add(document["pdf"])
    names = sorted(names)
    with tempfile.TemporaryDirectory(prefix="draft-stage-") as temporary:
        prepared = Path(temporary)
        for name in names:
            source = local_path(ROOT, name)
            require(source.stat().st_size <= 1048576, f"File exceeds 1 MiB: {name}")
            target = prepared / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, target)
        companion_link = (
            "The [supplementary PDF](supplementary-information.pdf) and "
            "[its TeX entry point](supplementary-information.tex) are included.\n\n"
            if record.get("companions") else "")
        (prepared / "README.md").write_text(
            f"# Draft {record['version']} - {record['review_date']}\n\n"
            "Historical snapshot of the Wilson--Loewner manuscript package.\n\n"
            "The [exposition](manuscript.pdf), [TeX entry point](manuscript.tex), "
            "[build guide](BUILD.md), sources, checks and records form a standalone package.\n\n"
            + companion_link
            + "Copy this directory elsewhere before rebuilding; preserve this snapshot unchanged.\n\n"
            "SNAPSHOT.json pins the saved files. BUILD_RECORD.json identifies the "
            "reviewed sources and PDFs. These records establish identity, not correctness.\n"
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


def validate_result(data):
    cases = data["cases"]
    require(data["case_count"] == len(cases) and data["all_pass"],
            "Invalid case count or failing recorded run")
    require(len({c["name"] for c in cases}) == len(cases), "Duplicate case names")
    for case in cases:
        value, threshold = case["value"], case["threshold"]
        require(math.isfinite(value) and math.isfinite(threshold), "Nonfinite diagnostic")
        direction = case["comparison"]
        require(direction in ("<=", ">="), "Unknown comparison")
        passed = value <= threshold if direction == "<=" else value >= threshold
        require(passed and case["passed"], f"Failed case: {case['name']}")


def case_identity(data):
    return (data["parameters"], data["case_count"],
            [(c["name"], c["threshold"], c["comparison"]) for c in data["cases"]])


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
            validate_result(expected)
            validate_result(actual)
            require(case_identity(actual) == case_identity(expected),
                    f"Replay case identities differ: {program}")
            total += actual["case_count"]
    print(json.dumps({"status": "passed", "version": record["version"],
                      "snapshots": len(snapshots), "replayed_cases": total,
                      "scope": "Package identity and optional tolerance-based finite diagnostics; not a proof checker."}, indent=2))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    build = commands.add_parser("record", help="Record a build after actual visual review")
    build.add_argument("--date", required=True)
    build.add_argument("--pages", type=int, required=True)
    build.add_argument("--supplement-pages", type=int,
                       help="Required when the supplementary entry point is present")
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
