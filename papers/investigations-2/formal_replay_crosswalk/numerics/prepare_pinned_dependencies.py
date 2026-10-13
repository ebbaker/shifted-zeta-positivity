#!/usr/bin/env python3
"""Prepare original pinned Lake dependencies without executing Lake or Lean.

Only Python's standard library and Git are used. Preparation checks out the 42
saved manifest commits and applies the 23 original compatibility patches. It
does not update manifests, resolve new revisions, run dependency hooks, obtain
caches, or compile mathematical modules. All outputs are provenance evidence,
not proof verification. Run --selftest before using --prepare.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import uuid

UPSTREAM_PIN = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"
INVENTORY_SHA256 = "122c153264c38a40f1af9674deec329026c432c8f12992536d9def529168cfcf"
TOOLCHAIN = "leanprover/lean4:v4.34.1"
HEX40 = re.compile(r"[0-9a-f]{40}\Z")
SAFE_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]*\Z")
PACKAGE_KEYS = ("url", "type", "subDir", "scope", "rev", "name",
                "manifestFile", "inputRev", "inherited", "configFile")
GIT_SETTINGS = ["-c", "core.hooksPath=/dev/null", "-c", "core.fsmonitor=false",
                "-c", "protocol.file.allow=never", "-c", "fetch.writeCommitGraph=false"]


class PreparationError(RuntimeError):
    pass


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def git(directory: Path, *args: str, extra_env=None, check=True) -> subprocess.CompletedProcess:
    env = os.environ.copy()
    # Do not inherit user-supplied alternate repositories, indexes or global Git
    # filters. This recipe owns its fresh dependency repository configurations.
    for key in list(env):
        if key.startswith("GIT_"):
            env.pop(key)
    env.update({"GIT_CONFIG_NOSYSTEM": "1", "GIT_CONFIG_GLOBAL": os.devnull,
                "GIT_ATTR_NOSYSTEM": "1", "GIT_TERMINAL_PROMPT": "0"})
    if extra_env:
        env.update(extra_env)
    result = subprocess.run(["git", *GIT_SETTINGS, "-C", str(directory), *args],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            env=env, timeout=1200)
    if check and result.returncode:
        raise PreparationError(f"Git failed in {directory}: {' '.join(args)}\n"
                               + result.stderr.decode("utf-8", "replace")[-6000:])
    return result


def git_text(directory: Path, *args: str, **kwargs) -> str:
    return git(directory, *args, **kwargs).stdout.decode("utf-8").strip()


def require(condition: bool, message: str):
    if not condition:
        raise PreparationError(message)


def safe_child(parent: Path, name: str) -> Path:
    require(bool(SAFE_NAME.fullmatch(name)), f"Unsafe package name: {name!r}")
    path = parent / name
    require(not path.is_symlink(), f"Refusing symlink: {path}")
    require(path.resolve().parent == parent.resolve(), f"Path escape: {path}")
    return path


def normalize_name(name: str) -> str:
    if name.startswith("«") and name.endswith("»"):
        name = name[1:-1]
    require(bool(SAFE_NAME.fullmatch(name)), f"Unsupported package name: {name!r}")
    return name


def verified_file(path: Path, identity: dict) -> bytes:
    require(path.is_file() and not path.is_symlink(), f"Missing or linked source: {path}")
    data = path.read_bytes()
    require(len(data) == identity["bytes"] and sha(data) == identity["sha256"],
            f"Source identity mismatch: {path}")
    return data


def source_preflight(checkout: Path, inventory_path: Path) -> dict:
    require(checkout.is_dir(), f"Missing upstream checkout: {checkout}")
    raw_inventory = inventory_path.read_bytes()
    require(sha(raw_inventory) == INVENTORY_SHA256, "Saved inventory hash mismatch")
    inventory = json.loads(raw_inventory)
    require(git_text(checkout, "rev-parse", "HEAD") == UPSTREAM_PIN,
            "Wrong upstream checkout commit")
    require(git_text(checkout, "rev-parse", "--show-toplevel") == str(checkout),
            "Checkout must be the repository root")
    require(not git_text(checkout, "status", "--porcelain=v1", "--untracked-files=all"),
            "Unexpected changes or untracked files in mathematical source checkout")
    root = checkout / "lean"
    require(not (root / ".lake/build").exists(),
            "Mathematical build output exists; use a fresh checking baseline")
    manifest_bytes = verified_file(root / "lake-manifest.json", inventory["lake_manifest"])
    verified_file(root / "lakefile.lean", inventory["compatibility_patches"]["lakefile"])
    require((root / "lean-toolchain").read_text().strip() == TOOLCHAIN,
            "Wrong proof toolchain")
    manifest = json.loads(manifest_bytes)
    require(manifest["packagesDir"] == ".lake/packages" and manifest["name"] == "OAI",
            "Unexpected manifest package layout")
    expected = inventory["lake_manifest"]["packages"]
    actual = manifest["packages"]
    require(len(expected) == len(actual) == 42, "Expected exactly 42 manifest packages")
    require([{k: p[k] for k in PACKAGE_KEYS} for p in actual]
            == [{k: p[k] for k in PACKAGE_KEYS} for p in expected],
            "Manifest packages differ from saved inventory")
    packages = []
    names = set()
    for p in actual:
        require(p["type"] == "git" and p["subDir"] is None,
                f"Unsupported dependency source: {p['name']}")
        require(bool(HEX40.fullmatch(p["rev"])), f"Non-exact commit: {p['name']}")
        require(p["url"].startswith("https://github.com/"), f"Unsupported origin: {p['name']}")
        label = normalize_name(p["name"])
        require(label not in names, f"Duplicate package label: {label}")
        names.add(label)
        packages.append(dict(p, label=label))
    patches = inventory["compatibility_patches"]["patches"]
    require(len(patches) == inventory["compatibility_patches"]["count"] == 23,
            "Expected exactly 23 original compatibility patches")
    patch_names = set()
    by_label = {p["label"]: p for p in packages}
    for p in patches:
        label = p["dependency"]
        require(label in by_label and label not in patch_names, f"Invalid patch owner: {label}")
        require(p["dependency_commit"] == by_label[label]["rev"], f"Patch pin mismatch: {label}")
        require(p["path"] == f"lean/patches/{label}-lean4341.patch", f"Unexpected patch path: {label}")
        data = verified_file(checkout / p["path"], p)
        require(git_text(checkout, "rev-parse", f"HEAD:{p['path']}") == p["git_blob_sha1"],
                f"Patch Git object mismatch: {label}")
        require(hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
                == p["git_blob_sha1"], f"Patch blob content mismatch: {label}")
        patch_names.add(label)
    return {"inventory": inventory, "manifest": manifest, "packages": packages,
            "patches": patches, "manifest_sha256": sha(manifest_bytes),
            "root": root, "checkout": checkout}


def assert_repository(directory: Path, package: dict):
    require(directory.is_dir() and not directory.is_symlink(), f"Missing or linked dependency: {directory}")
    require((directory / ".git").is_dir() and not (directory / ".git").is_symlink(),
            f"Dependency must be a standalone Git checkout: {directory}")
    require(git_text(directory, "rev-parse", "--show-toplevel") == str(directory.resolve()),
            f"Unexpected Git root: {directory}")
    require(git_text(directory, "rev-parse", "HEAD") == package["rev"],
            f"Wrong dependency commit: {package['label']}")
    require(git_text(directory, "remote", "get-url", "origin") == package["url"],
            f"Wrong dependency origin: {package['label']}")
    require(git(directory, "diff", "--cached", "--quiet", "HEAD", check=False).returncode == 0,
            f"Unexpected staged dependency changes: {package['label']}")


def obtain_package(packages_dir: Path, package: dict, prepare: bool) -> Path:
    label = package["label"]
    directory = safe_child(packages_dir, label)
    if not directory.exists():
        require(prepare, f"Dependency absent: {label}")
        staging = packages_dir / f".{label}-preparation-{uuid.uuid4().hex}"
        staging.mkdir()
        print(f"Fetching {label} at {package['rev']}", flush=True)
        try:
            git(staging, "init", "--quiet")
            git(staging, "remote", "add", "origin", package["url"])
            git(staging, "fetch", "--depth=1", "--no-tags", "origin", package["rev"])
            git(staging, "checkout", "--detach", "--quiet", "FETCH_HEAD")
            assert_repository(staging, package)
            require(not git_text(staging, "status", "--porcelain=v1", "--untracked-files=all"),
                    f"Fresh dependency checkout is dirty: {label}")
            staging.rename(directory)
        except Exception:
            # Preserve interrupted staging for inspection; never delete or
            # reset a checkout supplied by the caller.
            print(f"Failed staging retained: {staging}", file=sys.stderr, flush=True)
            raise
    assert_repository(directory, package)
    return directory


def temporary_index_tree(directory: Path, patch: Path | None, actual=False) -> str:
    with tempfile.TemporaryDirectory(prefix="replay-index-") as temp:
        index_env = {"GIT_INDEX_FILE": str(Path(temp) / "index")}
        git(directory, "read-tree", "HEAD", extra_env=index_env)
        if actual:
            git(directory, "add", "--all", "--", ".", extra_env=index_env)
        elif patch:
            git(directory, "apply", "--cached", "--check", str(patch), extra_env=index_env)
            git(directory, "apply", "--cached", str(patch), extra_env=index_env)
        return git_text(directory, "write-tree", extra_env=index_env)


def diff_bytes(directory: Path, tree: str) -> bytes:
    return git(directory, "diff", "--binary", "--full-index", "--no-ext-diff",
               "--no-textconv", "--no-renames", "HEAD", tree, "--").stdout


def patch_plan(directory: Path, package: dict, patch: Path | None) -> dict:
    assert_repository(directory, package)
    base_tree = git_text(directory, "rev-parse", "HEAD^{tree}")
    expected_tree = temporary_index_tree(directory, patch)
    actual_tree = temporary_index_tree(directory, None, actual=True)
    require(actual_tree in {base_tree, expected_tree},
            f"Unexpected dependency diff (not exactly original source or prescribed patch): {package['label']}")
    return {"directory": directory, "package": package, "patch": patch,
            "base_tree": base_tree, "expected_tree": expected_tree,
            "initial_tree": actual_tree,
            "state": "already_applied" if actual_tree == expected_tree else "needs_apply"}


def plan_record(plan: dict, patch_identity: dict | None) -> dict:
    directory = plan["directory"]
    expected = plan["expected_tree"]
    actual = temporary_index_tree(directory, None, actual=True)
    require(actual == expected, f"Applied source differs from exact expected tree: {plan['package']['label']}")
    expected_diff = diff_bytes(directory, expected)
    actual_diff = diff_bytes(directory, actual)
    require(actual_diff == expected_diff, f"Canonical patch diff mismatch: {plan['package']['label']}")
    changed = []
    paths = git(directory, "diff", "--name-only", "-z", "--no-renames", "HEAD", expected, "--").stdout
    for encoded in paths.split(b"\0"):
        if not encoded:
            continue
        relative = encoded.decode("utf-8")
        file = directory / relative
        require(file.resolve().is_relative_to(directory.resolve()), f"Patched path escape: {file}")
        require(not file.is_symlink(), f"Unexpected symlink in patch: {file}")
        if file.is_file():
            data = file.read_bytes()
            expected_blob = git(directory, "cat-file", "blob", f"{expected}:{relative}").stdout
            require(data == expected_blob, f"Patched file differs from expected Git blob: {file}")
            changed.append({"path": relative, "bytes": len(data), "sha256": sha(data),
                            "git_blob_sha1": git_text(directory, "rev-parse", f"{expected}:{relative}")})
        else:
            changed.append({"path": relative, "deleted": True})
    config = directory / plan["package"]["configFile"]
    require(config.is_file() and not config.is_symlink(), f"Missing package config: {config}")
    return {**plan["package"], "checkout_path": str(directory),
            "actual_head": git_text(directory, "rev-parse", "HEAD"),
            "actual_origin": git_text(directory, "remote", "get-url", "origin"),
            "base_tree": plan["base_tree"], "expected_patched_tree": expected,
            "actual_source_tree": actual, "initial_patch_state": plan["state"],
            "patch": patch_identity, "expected_diff_sha256": sha(expected_diff),
            "actual_diff_sha256": sha(actual_diff), "diff_bytes": len(actual_diff),
            "changed_files": changed, "config_sha256": sha(config.read_bytes()),
            "dependency_build_directory_present": (directory / ".lake/build").exists(),
            "status": "exact_source_and_prescribed_patch_verified"}


def ownership_audit(packages_dir: Path) -> dict:
    rellich = packages_dir / "rellich-kondrachov"
    config = (rellich / "lakefile.lean").read_text()
    # A direct textual check at the pinned configuration, not a claim to have
    # executed Lake's module ownership resolver.
    mathlib_ext = bool(re.search(r"lean_lib\s+«?MathlibExtensions»?\s+where", config))
    rellich_lib = bool(re.search(r"lean_lib\s+«?RellichKondrachov»?\s+where", config))
    require(mathlib_ext and rellich_lib, "Expected both pinned Rellich libraries are missing")
    require((rellich / "RellichKondrachov/Analysis/FunctionalSpaces/Sobolev/Euclidean/Rellich.lean").is_file(),
            "Rellich source root is missing")
    return {"config": str(rellich / "lakefile.lean"), "config_sha256": sha(config.encode()),
            "MathlibExtensions_declared": mathlib_ext,
            "RellichKondrachov_declared": rellich_lib,
            "interpretation": "Both libraries are present in the exact pinned configuration. Earlier truncated-excerpt ownership concern is withdrawn. Lake resolution has not run."}


def prepare_sources(preflight: dict, jobs: int, prepare: bool) -> dict:
    root = preflight["root"]
    packages_dir = root / ".lake/packages"
    require(not packages_dir.is_symlink() and not (root / ".lake").is_symlink(), "Linked Lake directory")
    if prepare:
        packages_dir.mkdir(parents=True, exist_ok=True)
    require(packages_dir.is_dir(), "Dependency directory does not exist")
    labels = {p["label"] for p in preflight["packages"]}
    extras = [p.name for p in packages_dir.iterdir() if p.name not in labels]
    require(not extras, f"Unexpected dependency directory entries: {extras}")
    locations = {}
    # Fetching separate standalone Git repositories is independent; patch
    # preflight and mutations are performed sequentially only after every fetch.
    with concurrent.futures.ThreadPoolExecutor(max_workers=jobs) as pool:
        tasks = {pool.submit(obtain_package, packages_dir, p, prepare): p["label"]
                 for p in preflight["packages"]}
        failures = []
        for task in concurrent.futures.as_completed(tasks):
            label = tasks[task]
            try:
                locations[label] = task.result()
            except Exception as error:
                failures.append(f"{label}: {error}")
        require(not failures, "Dependency fetch/preflight failures:\n" + "\n".join(failures))
    patch_by_label = {p["dependency"]: p for p in preflight["patches"]}
    plans = []
    for package in preflight["packages"]:
        identity = patch_by_label.get(package["label"])
        patch = preflight["checkout"] / identity["path"] if identity else None
        plans.append(patch_plan(locations[package["label"]], package, patch))
    if not prepare:
        require(all(p["state"] == "already_applied" for p in plans),
                "Some prescribed patches have not been applied")
    for plan in plans:
        if plan["state"] == "needs_apply":
            print(f"Applying original patch: {plan['package']['label']}", flush=True)
            git(plan["directory"], "apply", "--check", str(plan["patch"]))
            git(plan["directory"], "apply", str(plan["patch"]))
            git(plan["directory"], "apply", "--reverse", "--check", str(plan["patch"]))
    records = [plan_record(p, patch_by_label.get(p["package"]["label"])) for p in plans]
    after = source_preflight(preflight["checkout"], preflight["inventory_path"])
    require(after["manifest_sha256"] == preflight["manifest_sha256"], "Original manifest changed")
    return {"packages": records, "package_count": len(records),
            "verified_original_patch_count": len(patch_by_label),
            "original_manifest_sha256_before": preflight["manifest_sha256"],
            "original_manifest_sha256_after": after["manifest_sha256"],
            "rellich_configuration_audit": ownership_audit(packages_dir)}


def selftest() -> dict:
    controls = []
    with tempfile.TemporaryDirectory(prefix="replay-dependency-selftest-") as temp:
        root = Path(temp).resolve()
        git(root, "init", "--quiet")
        git(root, "config", "user.name", "Replay fixture")
        git(root, "config", "user.email", "fixture@example.invalid")
        git(root, "remote", "add", "origin", "https://github.com/example/fixture.git")
        (root / "base.lean").write_text("-- original source\n")
        git(root, "add", "base.lean")
        git(root, "commit", "--quiet", "-m", "fixture")
        package = {"label": "fixture", "rev": git_text(root, "rev-parse", "HEAD"),
                   "url": "https://github.com/example/fixture.git", "configFile": "base.lean"}
        patch = Path(temp) / "fixture.patch"
        # Keep the patch outside the repository so it is not an untracked
        # change in the source-tree identity test.
        with tempfile.TemporaryDirectory(prefix="replay-patch-selftest-") as patch_temp:
            patch = Path(patch_temp) / "fixture.patch"
            (root / "base.lean").write_text("-- patched source\n")
            (root / "new.lean").write_text("-- patch-added source\n")
            git(root, "add", "--all")
            patch.write_bytes(git(root, "diff", "--cached", "--binary", "--full-index", "HEAD").stdout)
            git(root, "reset", "--quiet", "HEAD")
            git(root, "checkout", "--", "base.lean")
            (root / "new.lean").unlink()
            plan = patch_plan(root, package, patch)
            require(plan["state"] == "needs_apply", "Fresh patch fixture misclassified")
            controls.append({"control": "clean_exact_source_acceptance", "passed": True})
            git(root, "apply", str(patch))
            plan = patch_plan(root, package, patch)
            require(plan["state"] == "already_applied", "Patched fixture misclassified")
            record = plan_record(plan, {"fixture": True})
            require(len(record["changed_files"]) == 2, "Added-file identity was not recorded")
            controls.append({"control": "exact_patch_including_added_file_acceptance", "passed": True})
            (root / "base.lean").write_text("-- unexpected change\n")
            try:
                patch_plan(root, package, patch)
            except PreparationError:
                controls.append({"control": "unexpected_tracked_diff_rejection", "passed": True})
            else:
                raise PreparationError("Unexpected tracked diff accepted")
            (root / "base.lean").write_text("-- patched source\n")
            (root / "extra.lean").write_text("-- unexpected extra\n")
            try:
                patch_plan(root, package, patch)
            except PreparationError:
                controls.append({"control": "unexpected_untracked_file_rejection", "passed": True})
            else:
                raise PreparationError("Unexpected untracked file accepted")
            (root / "extra.lean").unlink()
            git(root, "add", "base.lean")
            try:
                patch_plan(root, package, patch)
            except PreparationError:
                controls.append({"control": "unexpected_staged_diff_rejection", "passed": True})
            else:
                raise PreparationError("Unexpected staged diff accepted")
            git(root, "reset", "--quiet", "HEAD")
            for key, value in (("rev", "0" * 40), ("url", "https://github.com/example/wrong.git")):
                bad = dict(package, **{key: value})
                try:
                    patch_plan(root, bad, patch)
                except PreparationError:
                    controls.append({"control": f"wrong_{key}_rejection", "passed": True})
                else:
                    raise PreparationError(f"Wrong {key} accepted")
            bad_patch = Path(patch_temp) / "bad.patch"
            bad_patch.write_text("diff --git a/absent b/absent\n--- a/absent\n+++ b/absent\n@@ -1 +1 @@\n-x\n+y\n")
            try:
                patch_plan(root, package, bad_patch)
            except PreparationError:
                controls.append({"control": "nonapplicable_patch_rejection", "passed": True})
            else:
                raise PreparationError("Nonapplicable patch accepted")
    return {"status": "passed", "controls": controls, "control_count": len(controls),
            "scope": "Small Git/Python provenance fixtures only; no Lean execution or proof verification."}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, help="Exact detached openai/math repository root")
    parser.add_argument("--inventory", type=Path, help="Saved source_inventory_20261012.json")
    parser.add_argument("--output", type=Path, help="External JSON provenance record")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--prepare", action="store_true", help="Fetch and apply original pinned sources")
    modes.add_argument("--verify-only", action="store_true", help="Verify existing exactly patched sources")
    modes.add_argument("--plan-only", action="store_true", help="Verify recipe inputs; no dependency downloads")
    parser.add_argument("--jobs", type=int, default=3, choices=range(1, 5), help="Independent Git fetches (default 3)")
    parser.add_argument("--selftest", action="store_true", help="Run harmless local Git fixture controls")
    args = parser.parse_args()
    record = {"schema": "formal-replay-pinned-dependencies-v1", "record_date": "2026-10-12",
              "generated_at_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
              "prepared_for": "Edward Baker", "model": "GPT-6 (Codex)",
              "effort": "Inherited session configuration; exact serving variant and reasoning effort are not exposed.",
              "llm_acknowledgement": "Prepared with substantial LLM assistance; not an independent mathematical review.",
              "script_sha256": sha(Path(__file__).read_bytes()), "upstream_pin": UPSTREAM_PIN,
              "inventory_sha256": INVENTORY_SHA256, "toolchain": TOOLCHAIN,
              "lake_executed": False, "lean_executed": False, "mathlib_cache_downloaded": False,
              "mathematical_verification": "not_run", "status": "started"}
    try:
        if args.selftest:
            record["controls"] = selftest()
        if not any((args.prepare, args.verify_only, args.plan_only)):
            require(args.selftest, "Choose --prepare, --verify-only, --plan-only, or --selftest")
            record["status"] = "selftest_passed"
        else:
            require(args.checkout and args.inventory and args.output,
                    "--checkout, --inventory and --output are required for recipe modes")
            checkout = args.checkout.resolve()
            inventory_path = args.inventory.resolve()
            output = args.output.resolve()
            require(not output.is_relative_to(checkout), "Provenance output must be outside the upstream checkout")
            preflight = source_preflight(checkout, inventory_path)
            preflight["inventory_path"] = inventory_path
            record.update({"checkout": str(checkout), "mode": "prepare" if args.prepare else
                           "verify_only" if args.verify_only else "plan_only", "jobs": args.jobs,
                           "original_manifest_sha256": preflight["manifest_sha256"]})
            if args.plan_only:
                record["planned_packages"] = preflight["packages"]
                record["planned_patches"] = preflight["patches"]
                record["status"] = "recipe_inputs_verified_dependencies_not_fetched"
            else:
                record.update(prepare_sources(preflight, args.jobs, args.prepare))
                record["status"] = "all_42_pins_and_23_prescribed_patches_verified"
    except Exception as error:
        record["status"] = "failed_closed"
        record["error"] = str(error)
        print(str(error), file=sys.stderr)
    if args.output:
        output = args.output.resolve()
        if args.checkout and output.is_relative_to(args.checkout.resolve()):
            print("Refusing to write output inside upstream source checkout", file=sys.stderr)
            return 2
        output.parent.mkdir(parents=True, exist_ok=True)
        data = json.dumps(record, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
        temp = output.with_name(output.name + ".tmp-" + uuid.uuid4().hex)
        temp.write_text(data)
        temp.replace(output)
        print(f"Record: {output} ({len(data.encode())} bytes)", flush=True)
    print(f"Status: {record['status']}", flush=True)
    return 2 if record["status"] == "failed_closed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
