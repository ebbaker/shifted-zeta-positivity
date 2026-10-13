#!/usr/bin/env python3
"""Read-only source inventory for the three pinned seven-eighths comparators.

Prepared 12 October 2026 with GPT-6 (Codex); exact serving variant and
reasoning effort are not exposed and are not inferred. Substantial LLM
assistance. This is a source-level inventory, NOT a Lean build, comparator
replay, axiom audit, or proof of correspondence to an arithmetic argument.

Generate (all output must be outside the upstream checkout):
  python3 check_replay_inputs.py --checkout /path/to/openai-math \
    --output source_inventory_20261012.json \
    --closure-manifest /external/archive/source_closure_manifest.json

Check an existing record and its external manifest, without writing:
  FORMAL_REPLAY_ARCHIVES=/external/archive python3 check_replay_inputs.py \
    --checkout /path/to/openai-math --verify-record source_inventory_20261012.json

The external manifest is looked up first at the lane's
numerics-archives/source_closure_manifest.json, then at the same relative
path under FORMAL_REPLAY_ARCHIVES. A missing/mismatched manifest fails closed.
Record verification also compares all regenerated deterministic evidence,
including the generator's own hash. Only explicitly named timestamps,
environment availability, and absolute output/checkout paths are incidental.
Only imports reachable from the configured challenge/solution roots
are scanned. External package and core imports form a frontier; they are
listed but not recursively expanded or validated. No tools are installed,
downloaded, or executed except read-only Git queries. In particular, Lean,
Lake, and elan wrappers are never invoked.
"""

from __future__ import annotations

import argparse
from collections import deque
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import subprocess
import sys
import tempfile

EXPECTED_PIN = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"
EXPECTED_TOOLCHAIN = "leanprover/lean4:v4.34.1"
MANIFEST_RELATIVE = Path("source_closure_manifest.json")
SMALL_RECORD_MAX = 1_000_000
TARGETS = {
    "QuasiRiemannHypothesis": (
        "OAI.NumberTheory.DirichletL.Nonvanishing",
        "OAI.riemannZeta_ne_zero_of_seven_eighths_lt_re",
    ),
    "DirichletSevenEighths": (
        "OAI.NumberTheory.DirichletL.Nonvanishing",
        "OAI.DirichletCharacter.LFunction_ne_zero_of_seven_eighths_lt_re",
    ),
    "HeckeSevenEighths": (
        "OAI.NumberTheory.DirichletL.Hecke.Nonvanishing",
        "OAI.SevenEighths.HeckeFamily.LFunction_ne_zero_of_seven_eighths_lt_re",
    ),
}
PERMITTED_AXIOMS = ["propext", "Quot.sound", "Classical.choice"]
PRE_RESOLUTION_PATCHES = [
    "iut", "tate-curves-theta", "genl", "heights", "pi1", "orbicurve-cores",
    "oka", "tempered-fundamental-groups", "elliptic-curves", "formal-schemes", "belyi",
]
POST_UPDATE_PATCHES = [
    "fixed-point-theorems", "PrimeNumberTheoremAnd", "Zeta3Irrational",
    "rellich-kondrachov", "carleson", "StrongPNT", "AbsorptionCutoff", "AINTLIB",
    "ClassFieldTheory", "schoenflies-lean", "SphereEversion", "gromov",
]
MODULE_RE = re.compile(r"[A-Za-z_][A-Za-z_0-9']*(?:\.[A-Za-z_][A-Za-z_0-9']*)*")


class PreflightError(RuntimeError):
    pass


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical(data: object) -> bytes:
    return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")


def stored_json(data: object) -> bytes:
    return (json.dumps(data, sort_keys=True, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def git_blob(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def require_pin(expected: str, actual: str) -> None:
    if not re.fullmatch(r"[0-9a-f]{40}", expected):
        raise PreflightError("Expected pin must be a full lowercase 40-character Git commit.")
    if actual != expected:
        raise PreflightError(f"Wrong source pin: expected {expected}, found {actual}.")


def git(root: Path, args: list[str], input_bytes: bytes | None = None) -> bytes:
    env = os.environ.copy()
    env["GIT_OPTIONAL_LOCKS"] = "0"
    result = subprocess.run(
        ["git", "-c", "core.fsmonitor=false", "-C", str(root), *args],
        input=input_bytes, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env,
        check=False,
    )
    if result.returncode:
        raise PreflightError(f"Read-only Git query failed ({args[0]}): " + result.stderr.decode(errors="replace").strip())
    return result.stdout


def read_source(root: Path, relative: str, contents: dict[str, bytes]) -> bytes:
    if relative in contents:
        return contents[relative]
    path = root / relative
    try:
        path.resolve().relative_to(root)
    except ValueError as exc:
        raise PreflightError(f"Source escapes checkout: {relative}") from exc
    partial = root
    for component in Path(relative).parts:
        partial /= component
        if partial.is_symlink():
            raise PreflightError(f"Source path contains a symlink: {relative}")
    if not path.is_file():
        raise PreflightError(f"Missing critical source input: {relative}")
    contents[relative] = path.read_bytes()
    return contents[relative]


def strip_comments_and_strings(source: str) -> str:
    """Lex enough Lean to find import lines; nested comments are supported.

    Newlines are retained, as are guillemet-quoted identifiers. Unsupported
    import tokens are rejected below rather than silently omitted. This does
    not elaborate Lean; its limits are explicit in the generated record.
    """
    out: list[str] = []
    depth = 0
    in_string = False
    i = 0
    while i < len(source):
        pair = source[i:i + 2]
        ch = source[i]
        if depth:
            if pair == "/-":
                depth += 1
                out.extend("  ")
                i += 2
            elif pair == "-/":
                depth -= 1
                out.extend("  ")
                i += 2
            else:
                out.append("\n" if ch == "\n" else " ")
                i += 1
        elif in_string:
            if ch == "\\":
                out.append(" ")
                i += 1
                if i < len(source):
                    out.append("\n" if source[i] == "\n" else " ")
                    i += 1
            else:
                if ch == '"':
                    in_string = False
                out.append("\n" if ch == "\n" else " ")
                i += 1
        elif pair == "--":
            end = source.find("\n", i)
            if end == -1:
                end = len(source)
            out.extend(" " * (end - i))
            i = end
        elif pair == "/-":
            depth = 1
            out.extend("  ")
            i += 2
        elif ch == '"':
            in_string = True
            out.append(" ")
            i += 1
        else:
            out.append(ch)
            i += 1
    if depth or in_string:
        raise PreflightError("Unterminated comment/string in a reached Lean source.")
    return "".join(out)


def imports(data: bytes, relative: str) -> list[str]:
    try:
        clean = strip_comments_and_strings(data.decode("utf-8"))
    except (UnicodeDecodeError, PreflightError) as exc:
        raise PreflightError(f"Cannot scan {relative}: {exc}") from exc
    found: list[str] = []
    for line in clean.splitlines():
        match = re.match(r"^\s*(?:(?:public|private)\s+)?import\s+(.+?)\s*$", line)
        if not match:
            if re.match(r"^\s*(?:(?:public|private)\s+)?import\b", line):
                raise PreflightError(f"Unsupported empty import syntax in {relative}.")
            continue
        for token in match.group(1).split():
            if not MODULE_RE.fullmatch(token):
                raise PreflightError(f"Unsupported import token {token!r} in {relative}.")
            found.append(token)
    return sorted(set(found))


def module_path(module: str) -> str:
    if not MODULE_RE.fullmatch(module):
        raise PreflightError(f"Invalid configured module name: {module!r}")
    return "lean/" + module.replace(".", "/") + ".lean"


def verify_bytes(relative: str, data: bytes, expected_blob: str, expected_size: int) -> None:
    if len(data) != expected_size or git_blob(data) != expected_blob:
        raise PreflightError(f"Source hash mismatch against pinned Git blob: {relative}")


def verify_git_inputs(root: Path, pin: str, contents: dict[str, bytes]) -> dict[str, dict]:
    paths = sorted(contents)
    queries = "".join(f"{pin}:{path}\n" for path in paths).encode()
    lines = git(root, ["cat-file", "--batch-check=%(objectname) %(objecttype) %(objectsize)"], queries).decode().splitlines()
    if len(lines) != len(paths):
        raise PreflightError("Incomplete Git blob response.")
    records = {}
    for path, line in zip(paths, lines):
        fields = line.split()
        if len(fields) != 3 or fields[1] != "blob":
            raise PreflightError(f"Critical input is not a blob at the expected pin: {path}")
        blob, _, size = fields
        verify_bytes(path, contents[path], blob, int(size))
        records[path] = {"path": path, "bytes": int(size), "sha256": sha256(contents[path]), "git_blob_sha1": blob}
    # Index changes matter even when the working-tree bytes match the pin.
    # Unrelated dirty files do not cause rejection; every reached input does.
    for args in (["diff", "--name-only", "-z"], ["diff", "--cached", "--name-only", "-z", pin]):
        dirty = {p.decode("utf-8") for p in git(root, args).split(b"\0") if p}
        relevant = sorted(dirty.intersection(contents))
        if relevant:
            raise PreflightError("Dirty relevant source/index paths: " + ", ".join(relevant[:10]))
    # Reject a concurrent edit between scanning and verification.
    for path in paths:
        if (root / path).read_bytes() != contents[path]:
            raise PreflightError(f"Source changed during inventory: {path}")
    return records


def provider(module: str) -> str | None:
    prefix = module.split(".", 1)[0]
    return {"Mathlib": "mathlib", "Lean": "Lean toolchain", "Init": "Lean toolchain",
            "Std": "Lean toolchain", "PrimeNumberTheoremAnd": "PrimeNumberTheoremAnd",
            "RellichKondrachov": "rellich-kondrachov"}.get(prefix)


def inventory(root: Path, expected_pin: str) -> tuple[dict, dict]:
    if not root.is_dir():
        raise PreflightError(f"Checkout directory is absent: {root}")
    head = git(root, ["rev-parse", "HEAD"]).decode().strip()
    require_pin(expected_pin, head)
    if git(root, ["rev-parse", "--show-object-format"]).decode().strip() != "sha1":
        raise PreflightError("This pin inventory requires a SHA-1 Git repository.")
    contents: dict[str, bytes] = {}
    toolchain = read_source(root, "lean/lean-toolchain", contents).decode().strip()
    if toolchain != EXPECTED_TOOLCHAIN:
        raise PreflightError(f"Unexpected Lean toolchain: {toolchain!r}")
    lakefile = read_source(root, "lean/lakefile.lean", contents).decode()
    lake_manifest = json.loads(read_source(root, "lean/lake-manifest.json", contents))
    read_source(root, "lean/patches/README.md", contents)
    targets = {}
    all_roots = set()
    for name, (solution, theorem) in TARGETS.items():
        relative = f"lean/ComparatorChallenges/{name}.json"
        config = json.loads(read_source(root, relative, contents))
        expected_config = {"challenge_module": f"ComparatorChallenges.{name}",
                           "solution_module": solution, "theorem_names": [theorem],
                           "definition_names": [], "permitted_axioms": PERMITTED_AXIOMS,
                           "enable_nanoda": False}
        if config != expected_config:
            raise PreflightError(f"Comparator contract differs from expected pinned contract: {relative}")
        targets[name] = {"config_path": relative, **config, "reported_axioms": None,
                         "formal_replay_status": "not_run"}
        all_roots.update([config["challenge_module"], config["solution_module"]])
    graph = {}
    queue = deque(sorted(all_roots))
    while queue:
        module = queue.popleft()
        if module in graph:
            continue
        relative = module_path(module)
        graph[module] = imports(read_source(root, relative, contents), relative)
        for imported in graph[module]:
            if imported == "OAI" or imported.startswith(("OAI.", "ComparatorChallenges.")):
                queue.append(imported)
    target_members = {}
    for name, target in targets.items():
        reached = set()
        queue = deque([target["challenge_module"], target["solution_module"]])
        while queue:
            module = queue.popleft()
            if module in reached:
                continue
            reached.add(module)
            queue.extend(m for m in graph[module] if m in graph)
        target_members[name] = reached
    packages = []
    patch_records = []
    package_by_name = {}
    for package in lake_manifest["packages"]:
        name = package["name"].removeprefix("«").removesuffix("»")
        if package.get("type") != "git" or not re.fullmatch(r"[0-9a-f]{40}", package.get("rev", "")):
            raise PreflightError(f"Unpinned or non-Git lake manifest package: {name}")
        package_by_name[name] = package
        packages.append({**package, "normalized_name": name,
                         "checkout_present": (root / "lean/.lake/packages" / name).is_dir(),
                         "checkout_validated_by_this_scanner": False})
    for phase, names in (("pre_resolution", PRE_RESOLUTION_PATCHES), ("post_update", POST_UPDATE_PATCHES)):
        for name in names:
            if name not in package_by_name or name not in lakefile:
                raise PreflightError(f"Missing expected patched dependency declaration: {name}")
            relative = f"lean/patches/{name}-lean4341.patch"
            read_source(root, relative, contents)
            patch_records.append({"dependency": name, "path": relative, "phase": phase,
                                  "dependency_commit": package_by_name[name]["rev"],
                                  "application_status": "not_checked_not_applied"})
    files = verify_git_inputs(root, expected_pin, contents)
    external = sorted({m for imported in graph.values() for m in imported if m not in graph})
    modules = []
    for module in sorted(graph):
        modules.append({"module": module, **files[module_path(module)], "imports": graph[module],
                        "reached_by": sorted(name for name, members in target_members.items() if module in members)})
    full = {"schema": "formal-replay-source-closure-v1", "expected_commit": expected_pin,
            "toolchain": toolchain, "targets": targets, "modules": modules,
            "critical_nonmodule_files": [files[p] for p in sorted(files) if not p.endswith(".lean") or p == "lean/lakefile.lean"],
            "external_frontier": [{"module": m, "provider_hint": provider(m),
                                   "imported_by": sorted(k for k, v in graph.items() if m in v),
                                   "resolved_by_this_scanner": False} for m in external]}
    for name, target in targets.items():
        members = target_members[name]
        module_rows = [row for row in modules if row["module"] in members]
        target.update({"local_module_count_including_challenge": len(members),
                       "oai_module_count": sum(m == "OAI" or m.startswith("OAI.") for m in members),
                       "local_source_bytes": sum(row["bytes"] for row in module_rows),
                       "local_modules_canonical_sha256": sha256(canonical(module_rows)),
                       "external_import_count": len({m for k in members for m in graph[k] if m not in graph})})
    small = {
        "schema": "formal-replay-source-inventory-v1",
        "prepared_for": "Edward Baker",
        "record_date": "2026-10-12",
        "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "model": "GPT-6 (Codex), inherited session configuration",
        "effort": "not exposed; not inferred",
        "llm_acknowledgement": "Prepared with substantial LLM assistance; not independent mathematical validation.",
        "status": "pinned_source_inputs_verified; formal_replay_not_run",
        "scope": {
            "source_identity_only": True, "proof_checked": False, "axioms_inferred_from_source": False,
            "externals_recursively_expanded": False, "dependencies_built_or_validated": False,
            "import_scanner": "Lexical import-line scanner; nested comments and strings masked; unsupported import tokens fail closed. No Lean elaboration.",
            "source_roots": sorted(all_roots), "read_input_count": len(files),
            "local_module_count_including_challenges": len(graph),
            "oai_module_count": sum(m == "OAI" or m.startswith("OAI.") for m in graph),
            "source_bytes_read": sum(row["bytes"] for row in files.values()),
            "external_frontier_count": len(external),
        },
        "upstream": {"expected_commit": expected_pin, "actual_head": head, "checkout": str(root),
                     "git_object_format": "sha1", "all_relevant_worktree_bytes_match_pin": True,
                     "relevant_index_and_worktree_dirty_check": "passed; unrelated paths excluded"},
        "toolchain": {"expected": EXPECTED_TOOLCHAIN, "observed": toolchain, **files["lean/lean-toolchain"]},
        "targets": targets,
        "source_roots": [{"module": m, **files[module_path(m)]} for m in sorted(all_roots)],
        "environment": {
            "platform": platform.platform(), "system": platform.system(), "machine": platform.machine(),
            "python_version": platform.python_version(),
            "path_availability_only": {name: shutil.which(name) for name in
                                       ["git", "systemd-run", "landrun", "comparator", "lean4export", "lean", "lake", "elan"]},
            "tool_version_probes_run": False,
            "availability_note": "A PATH match does not establish a working tool or sandbox. Lean/Lake/elan wrappers were not invoked.",
        },
        "lake_manifest": {**files["lean/lake-manifest.json"], "version": lake_manifest.get("version"),
                          "package_count": len(packages), "packages": packages,
                          "scope": "Entire OAI environment, not a minimal target dependency closure."},
        "compatibility_patches": {
            "count": len(patch_records), "lakefile": files["lean/lakefile.lean"],
            "readme": files["lean/patches/README.md"],
            "patches": [{**p, **files[p["path"]]} for p in patch_records],
            "scope": "Prescribed whole-project patch files. Recorded source identity only; no claim all are imported by these targets, and no patches applied."},
        "unresolved_external_imports": [{"module": m, "provider_hint": provider(m)} for m in external],
        "external_dependency_hints": sorted({provider(m) for m in external if provider(m)}),
        "external_frontier_note": "Unresolved by this source scanner. Provider mapping is a naming hint, not dependency validation or a compiled import closure.",
    }
    return small, full


def ensure_output_outside_checkout(path: Path, checkout: Path) -> None:
    try:
        path.resolve().relative_to(checkout)
    except ValueError:
        return
    raise PreflightError(f"Refusing to write inside upstream source checkout: {path}")


def locate_manifest() -> Path:
    normal = Path(__file__).resolve().parent.parent / "numerics-archives" / MANIFEST_RELATIVE
    if normal.is_file():
        return normal
    archive_root = os.environ.get("FORMAL_REPLAY_ARCHIVES")
    if archive_root:
        external = Path(archive_root).expanduser() / MANIFEST_RELATIVE
        if external.is_file():
            return external
    raise PreflightError(
        f"External source closure manifest is absent. Looked at {normal} and FORMAL_REPLAY_ARCHIVES/{MANIFEST_RELATIVE}. "
        "Regenerate with --checkout CHECKOUT --output RECORD --closure-manifest ARCHIVE/source_closure_manifest.json, "
        "then set FORMAL_REPLAY_ARCHIVES to ARCHIVE."
    )


def verify_bound_manifest(path: Path, bound: dict, regenerated: dict) -> None:
    if not path.is_file():
        raise PreflightError("External closure manifest is absent; regenerate it and set FORMAL_REPLAY_ARCHIVES.")
    loaded_bytes = path.read_bytes()
    if len(loaded_bytes) != bound["stored_bytes"] or sha256(loaded_bytes) != bound["stored_sha256"]:
        raise PreflightError("Stored external closure manifest hash/size mismatch.")
    loaded = json.loads(loaded_bytes)
    if sha256(canonical(loaded)) != bound["canonical_sha256"]:
        raise PreflightError("Canonical external closure manifest hash mismatch.")
    if sha256(stored_json(regenerated)) != bound["stored_sha256"] or sha256(canonical(regenerated)) != bound["canonical_sha256"]:
        raise PreflightError("Fresh source inventory differs from the hash-bound external manifest.")


def deterministic_record(record: dict) -> dict:
    """Mask only named incidental values; preserve every key and evidence field.

    Unknown fields survive the projection and therefore cause comparison to
    fail. Availability values may vary between machines, but their schemas
    remain bound. Proof/axiom/status fields are never excluded.
    """
    if not isinstance(record, dict):
        raise PreflightError("Small record must be a JSON object.")
    result = json.loads(canonical(record))
    if "generated_at_utc" in result:
        if not isinstance(result["generated_at_utc"], str):
            raise PreflightError("Small record timestamp must be a string.")
        try:
            dt.datetime.fromisoformat(result["generated_at_utc"])
        except ValueError as exc:
            raise PreflightError("Small record timestamp is invalid.") from exc
        result["generated_at_utc"] = "incidental_timestamp"
    if "environment" in result:
        env = result["environment"]
        if not isinstance(env, dict):
            raise PreflightError("Small record environment must be an object.")
        for field in ["platform", "system", "machine", "python_version"]:
            if field in env:
                if not isinstance(env[field], str):
                    raise PreflightError(f"Environment {field} must be a string.")
                env[field] = "incidental_environment"
        if "path_availability_only" in env:
            paths = env["path_availability_only"]
            if not isinstance(paths, dict) or any(value is not None and not isinstance(value, str) for value in paths.values()):
                raise PreflightError("Environment PATH availability must map tool names to paths or null.")
            env["path_availability_only"] = {key: None for key in paths}
    for block, field in [("upstream", "checkout"), ("closure_manifest", "generated_at_path")]:
        if block in result and not isinstance(result[block], dict):
            raise PreflightError(f"Small record {block} must be an object.")
        if block in result and field in result[block]:
            if not isinstance(result[block][field], str):
                raise PreflightError(f"Small record {block}.{field} must be a string.")
            result[block][field] = "incidental_absolute_path"
    if "lake_manifest" in result and not isinstance(result["lake_manifest"], dict):
        raise PreflightError("Small record lake_manifest must be an object.")
    if "lake_manifest" in result and "packages" in result["lake_manifest"]:
        if not isinstance(result["lake_manifest"]["packages"], list):
            raise PreflightError("Small record packages must be an array.")
        for package in result["lake_manifest"]["packages"]:
            if not isinstance(package, dict):
                raise PreflightError("Small record package entry must be an object.")
            if "checkout_present" in package:
                if type(package["checkout_present"]) is not bool:
                    raise PreflightError("Package checkout_present must be Boolean.")
                package["checkout_present"] = None
    return result


def verify_small_record(saved: dict, regenerated: dict) -> None:
    observed = deterministic_record(saved)
    expected = deterministic_record(regenerated)
    if canonical(observed) != canonical(expected):
        changed = sorted(key for key in set(observed) | set(expected)
                         if key not in observed or key not in expected or canonical(observed[key]) != canonical(expected[key]))
        raise PreflightError("Small record deterministic evidence/schema/generator mismatch in: " + ", ".join(changed))


def selftest() -> dict:
    """Small negative controls. No clones, builds, or Git mutations."""
    checks = []
    def rejects(name, fn):
        try:
            fn()
        except PreflightError:
            checks.append({"control": name, "result": "rejected_as_expected"})
        else:
            raise PreflightError(f"Negative control failed: {name}")
    rejects("wrong_commit_pin", lambda: require_pin(EXPECTED_PIN, "0" * 40))
    original = b"import Mathlib\ntheorem target : True := by trivial\n"
    changed = b"import Mathlib\ntheorem target : False := by sorry\n"
    rejects("changed_target_source", lambda: verify_bytes("Target.lean", changed, git_blob(original), len(original)))
    with tempfile.TemporaryDirectory(prefix="formal-replay-input-controls-") as temp:
        rejects("missing_critical_source", lambda: read_source(Path(temp), "lean/Target.lean", {}))
        path = Path(temp) / "source_closure_manifest.json"
        fixture = {"modules": []}
        encoded = stored_json(fixture)
        bound = {"stored_bytes": len(encoded), "stored_sha256": sha256(encoded),
                 "canonical_sha256": sha256(canonical(fixture))}
        rejects("missing_external_manifest", lambda: verify_bound_manifest(path, bound, fixture))
        path.write_bytes(encoded)
        verify_bound_manifest(path, bound, fixture)
        path.write_bytes(stored_json({"modules": ["changed"]}))
        rejects("changed_external_manifest", lambda: verify_bound_manifest(path, bound, fixture))
    sample = '/- outer /- nested -/ import OAI.False -/\nimport OAI.Real -- import OAI.False\n#eval "import OAI.False"\npublic import Mathlib.Real\n'
    if imports(sample.encode(), "fixture.lean") != ["Mathlib.Real", "OAI.Real"]:
        raise PreflightError("Nested-comment/string import control failed.")
    checks.append({"control": "nested_comments_strings_and_public_import", "result": "passed"})
    rejects("unsupported_import_token", lambda: imports(b"import OAI.Real;\n", "fixture.lean"))
    evidence_fixture = {"schema": "fixture", "status": "formal_replay_not_run",
                        "scope": {"proof_checked": False},
                        "targets": {"HeckeSevenEighths": {"reported_axioms": None}},
                        "generator": {"sha256": "a" * 64, "bytes": 123}}
    tampered = json.loads(canonical(evidence_fixture))
    tampered["scope"]["proof_checked"] = True
    tampered["targets"]["HeckeSevenEighths"]["reported_axioms"] = ["fabricated_axiom"]
    rejects("tampered_small_record_proof_and_axiom_evidence", lambda: verify_small_record(tampered, evidence_fixture))
    tampered_generator = json.loads(canonical(evidence_fixture))
    tampered_generator["generator"]["sha256"] = "b" * 64
    rejects("changed_small_record_generator_hash", lambda: verify_small_record(tampered_generator, evidence_fixture))
    extra_evidence = json.loads(canonical(evidence_fixture))
    extra_evidence["scope"]["fabricated_success"] = True
    rejects("unexpected_small_record_evidence_key", lambda: verify_small_record(extra_evidence, evidence_fixture))
    return {"status": "passed", "controls": checks,
            "scope": "Pure small fixtures exercising pin/hash/missing-input/scanner/record-evidence rejection paths; not proof or end-to-end comparator tests."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--checkout", type=Path, help="Explicit upstream repository root; never modified.")
    parser.add_argument("--expected-pin", default=EXPECTED_PIN)
    parser.add_argument("--output", type=Path, help="Small inventory JSON to create outside upstream checkout.")
    parser.add_argument("--closure-manifest", type=Path, help="External full manifest output path, required with --output.")
    parser.add_argument("--verify-record", type=Path, help="Verify an existing small record and normal/environment-located external manifest.")
    parser.add_argument("--selftest", action="store_true", help="With no checkout, run only small controls. Controls also always run before generation/verification.")
    args = parser.parse_args()
    try:
        controls = selftest()
        if args.checkout is None:
            if args.selftest:
                print(json.dumps(controls, indent=2))
                return 0
            parser.error("--checkout is required unless running --selftest alone")
        if bool(args.output) == bool(args.verify_record):
            parser.error("Choose exactly one of --output or --verify-record")
        if args.output and not args.closure_manifest:
            parser.error("--output requires explicit --closure-manifest outside the source checkout")
        if args.verify_record and args.closure_manifest:
            parser.error("--verify-record uses normal path / FORMAL_REPLAY_ARCHIVES lookup; omit --closure-manifest")
        root = args.checkout.expanduser().resolve()
        small, full = inventory(root, args.expected_pin)
        manifest_bytes = stored_json(full)
        manifest_hash = sha256(manifest_bytes)
        canonical_hash = sha256(canonical(full))
        small["closure_manifest"] = {
            "relative_archive_path": MANIFEST_RELATIVE.as_posix(), "generated_at_path": "not yet written",
            "stored_bytes": len(manifest_bytes), "stored_sha256": manifest_hash,
            "canonical_sha256": canonical_hash,
            "canonical_encoding": "UTF-8 json.dumps(sort_keys=True, ensure_ascii=False, separators=(',', ':')); no final newline",
            "stored_encoding": "UTF-8 JSON sorted keys, indent=2, ensure_ascii=False, final newline",
            "lookup": "lane/numerics-archives/source_closure_manifest.json, then FORMAL_REPLAY_ARCHIVES/source_closure_manifest.json",
            "regeneration": {"script": Path(__file__).name, "checkout_pin": args.expected_pin,
                             "arguments": ["--checkout", "CHECKOUT", "--expected-pin", args.expected_pin,
                                           "--output", "RECORD", "--closure-manifest", "ARCHIVE/source_closure_manifest.json", "--selftest"]},
            "meaning": "Source and import-graph identity in this scanner; hashes are not proof steps, compiled dependency checks, or formal validation.",
        }
        small["negative_controls"] = controls
        script_bytes = Path(__file__).read_bytes()
        small["generator"] = {"name": Path(__file__).name, "sha256": sha256(script_bytes), "bytes": len(script_bytes)}
        if args.verify_record:
            saved = json.loads(args.verify_record.read_bytes())
            verify_small_record(saved, small)
            path = locate_manifest()
            verify_bound_manifest(path, saved["closure_manifest"], full)
            print(json.dumps({"status": "source_record_and_manifest_identity_verified; formal_replay_not_run",
                              "manifest": str(path), "local_module_count": len(full["modules"]),
                              "canonical_sha256": canonical_hash, "negative_controls": controls}, indent=2))
            return 0
        output = args.output.expanduser().resolve()
        manifest_path = args.closure_manifest.expanduser().resolve()
        ensure_output_outside_checkout(output, root)
        ensure_output_outside_checkout(manifest_path, root)
        if output == manifest_path:
            raise PreflightError("Small record and external manifest must be different files.")
        small["closure_manifest"]["generated_at_path"] = str(manifest_path)
        record_bytes = stored_json(small)
        if len(record_bytes) >= SMALL_RECORD_MAX:
            raise PreflightError(f"Small record is {len(record_bytes)} bytes, exceeding the lane's 1 MB limit.")
        # All validation precedes writes. Neither output is under the source checkout.
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        output.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_bytes(manifest_bytes)
        output.write_bytes(record_bytes)
        print(json.dumps({"status": small["status"], "record": str(output), "record_bytes": len(record_bytes),
                          "external_manifest": str(manifest_path), "manifest_bytes": len(manifest_bytes),
                          "oai_module_count": small["scope"]["oai_module_count"],
                          "local_module_count_including_challenges": len(full["modules"]),
                          "manifest_canonical_sha256": canonical_hash}, indent=2))
        return 0
    except (PreflightError, OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Preflight refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
