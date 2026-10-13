#!/usr/bin/env python3
"""Build auxiliary replay tools, never mathematical solution modules.

Prepared 2026-10-12 for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration; serving variant and
reasoning effort are not exposed and are not inferred.

Run as an ordinary Linux ARM64 user. Dependencies supplied by the VM owner:
Python >=3.12, git, gcc, make, zstd, Go >=1.24, libc development headers,
libcap development headers, ca-certificates. Full logs stay in --root/logs.
The JSON result records tool preparation only, not sandbox or theorem success.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
from pathlib import Path
import platform
import re
import shutil
import struct
import subprocess
import sys
import tarfile
import tempfile
import time
import urllib.request


LEAN_VERSION = "4.34.1"
LEAN_COMMIT = "5045d0056413266e57c625dcd7c365b10e377c52"
LEAN_ASSET = "lean-4.34.1-linux_aarch64.tar.zst"
LEAN_ASSET_SHA256 = "fdb974c2cdb4627e090d5d4007b913e09d13c4868720fb5594e22808b3de9e37"
LEAN_ASSET_SIZE = 581946052
LEAN_ASSET_ID = 586761736
LEAN_RELEASE_ID = 396051688
LEAN_ASSET_URL = "https://github.com/leanprover/lean4/releases/download/v4.34.1/" + LEAN_ASSET
LEAN_RELEASE_API = "https://api.github.com/repos/leanprover/lean4/releases/tags/v4.34.1"
PINS = {
    "comparator": ("https://github.com/leanprover/comparator.git", "d03acab154d269c06e60e4de7e4cc85deebff94b"),
    "lean4export": ("https://github.com/leanprover/lean4export.git", "076e8e57707e813375e8f9da8bf989799ace9680"),
    "landrun": ("https://github.com/Zouuup/landrun.git", "811cfff51ceaf3d9843708aa6d22e9b84ccac8b4"),
}
MAX_RESULT_BYTES = 1_000_000


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def file_identity(path: Path) -> dict:
    require(path.is_file(), f"Required regular file absent: {path}")
    return {"path": str(path), "size_bytes": path.stat().st_size, "sha256": sha256(path)}


def validate_release(data: dict) -> dict:
    require(data.get("id") == LEAN_RELEASE_ID, "Lean release ID changed")
    require(data.get("tag_name") == "v" + LEAN_VERSION, "Lean release tag mismatch")
    require(data.get("draft") is False and data.get("prerelease") is False, "Unexpected release status")
    matches = [asset for asset in data.get("assets", []) if asset.get("name") == LEAN_ASSET]
    require(len(matches) == 1, "Expected one official Linux ARM64 archive")
    asset = matches[0]
    for key, expected in {
        "id": LEAN_ASSET_ID,
        "size": LEAN_ASSET_SIZE,
        "browser_download_url": LEAN_ASSET_URL,
        "digest": "sha256:" + LEAN_ASSET_SHA256,
    }.items():
        require(asset.get(key) == expected, f"Lean asset {key} mismatch")
    return {key: asset[key] for key in ("id", "name", "size", "digest", "browser_download_url")}


def validate_comparator_manifest(data: dict) -> dict:
    require(data.get("name") == "Comparator", "Comparator manifest package name mismatch")
    packages = data.get("packages")
    require(isinstance(packages, list) and len(packages) == 1, "Unexpected comparator dependencies")
    package = packages[0]
    for key, expected in {
        "name": "lean4export", "type": "git", "rev": PINS["lean4export"][1],
        "url": "https://github.com/leanprover/lean4export", "subDir": None,
    }.items():
        require(package.get(key) == expected, f"Comparator dependency {key} mismatch")
    return package


def verify_arm64_elf(path: Path) -> dict:
    with path.open("rb") as handle:
        head = handle.read(20)
    require(len(head) == 20 and head[:4] == b"\x7fELF", f"Not an ELF binary: {path}")
    require(head[4] == 2 and head[5] == 1, f"Expected little-endian ELF64: {path}")
    machine = struct.unpack("<H", head[18:20])[0]
    require(machine == 183, f"Expected AArch64 ELF binary: {path}")
    return {"elf_class": 64, "elf_machine": machine, "architecture": "aarch64"}


class Bootstrap:
    def __init__(self, root: Path):
        self.root = root
        self.logs = root / "logs"
        self.sources = root / "sources"
        self.bin = root / "bin"
        self.record = {
            "schema_version": 1,
            "purpose": "Auxiliary proof-tool preparation only",
            "mathematical_replay_run": False,
            "sandbox_functional_tests_run": False,
            "model": "GPT-6 (Codex)",
            "reasoning_effort": "Inherited session setting; exact level is not exposed",
            "started_utc": now(), "root": str(root), "status": "running",
            "commands": [], "sources": {}, "binaries": {}, "runtime_versions": {},
            "bootstrap_script": file_identity(Path(__file__).resolve()),
        }
        self.env = dict(os.environ)
        # Prevent an ambient Lean search path/compiler override from changing the build.
        for key in ("LEAN_PATH", "LEAN_SRC_PATH", "LEAN_SYSROOT", "LEAN_CC", "LAKE", "LAKE_HOME",
                    "GOFLAGS", "GOWORK", "GOINSECURE", "GOPRIVATE", "GONOSUMDB", "GONOPROXY"):
            self.env.pop(key, None)
        self.env.update({
            "ELAN_TOOLCHAIN": "leanprover/lean4:v" + LEAN_VERSION,
            "GOTOOLCHAIN": "local", "CGO_ENABLED": "1",
            "GOCACHE": str(root / "cache/go-build"),
            "GOPATH": str(root / "cache/go-path"),
            "GOSUMDB": "sum.golang.org", "GOPROXY": "https://proxy.golang.org,direct",
            "GOENV": "off", "GOWORK": "off", "GOFLAGS": "",
            "GIT_CONFIG_NOSYSTEM": "1", "GIT_TERMINAL_PROMPT": "0",
            "GIT_CONFIG_GLOBAL": "/dev/null", "GIT_OPTIONAL_LOCKS": "0",
        })
        self.command_index = 0

    def save(self) -> None:
        data = (json.dumps(self.record, indent=2, sort_keys=True) + "\n").encode()
        require(len(data) < MAX_RESULT_BYTES, "Tool result exceeds repository small-record limit")
        destination = self.root / "bootstrap_linux_tools_result.json"
        temporary = destination.with_suffix(".json.tmp")
        temporary.write_bytes(data)
        temporary.replace(destination)

    def run(self, label: str, argv: list[str], cwd: Path | None = None,
            capture: bool = False, timeout: int = 3600) -> str:
        self.command_index += 1
        log = self.logs / f"{self.command_index:02d}_{label}.log"
        item = {"label": label, "argv": argv, "cwd": str(cwd or self.root), "started_utc": now()}
        self.record["commands"].append(item)
        print(f"[{label}] started", flush=True)
        start = time.monotonic()
        with log.open("wb") as handle:
            handle.write((json.dumps({"argv": argv, "cwd": item["cwd"]}) + "\n").encode())
            handle.flush()
            try:
                result = subprocess.run(argv, cwd=cwd or self.root, env=self.env,
                                        stdout=handle, stderr=subprocess.STDOUT,
                                        timeout=timeout, check=False)
                item["exit_code"] = result.returncode
            except BaseException as error:
                item["exception"] = str(error)
                item["exit_code"] = None
                raise
            finally:
                item["finished_utc"] = now()
                item["elapsed_seconds"] = round(time.monotonic() - start, 3)
                handle.flush()
                item["log"] = file_identity(log)
                self.save()
        require(result.returncode == 0, f"{label} failed (exit {result.returncode}); inspect {log}")
        print(f"[{label}] passed", flush=True)
        if capture:
            # The first log line is the structured command header, not command output.
            return log.read_text(errors="replace").split("\n", 1)[1].strip()
        return ""

    def source_identity(self, name: str, path: Path, expected: str) -> dict:
        commit = self.run(name + "_commit", ["git", "-c", "core.fsmonitor=false", "rev-parse", "HEAD"], path, True)
        require(commit == expected, f"{name}: source commit mismatch")
        status = self.run(name + "_clean", ["git", "-c", "core.fsmonitor=false", "status", "--porcelain=v1", "--untracked-files=all"], path, True)
        require(not status, f"{name}: source checkout is not clean")
        remote = self.run(name + "_remote", ["git", "remote", "get-url", "origin"], path, True)
        require(remote.removesuffix(".git").lower() == PINS[name][0].removesuffix(".git").lower(),
                f"{name}: source origin mismatch")
        return {"path": str(path), "commit": commit, "origin": remote, "tracked_source_clean": True}

    def checkout(self, name: str) -> Path:
        url, pin = PINS[name]
        path = self.sources / name
        require(not path.is_symlink(), f"Refusing symlink checkout: {path}")
        if not path.exists():
            path.mkdir()
            self.run(name + "_init", ["git", "init", "--quiet"], path)
            self.run(name + "_remote_add", ["git", "remote", "add", "origin", url], path)
            self.run(name + "_fetch", ["git", "fetch", "--depth=1", "origin", pin], path)
            self.run(name + "_checkout", ["git", "checkout", "--detach", pin], path)
        self.record["sources"][name] = self.source_identity(name, path, pin)
        self.save()
        return path

    def lean(self) -> Path:
        request = urllib.request.Request(LEAN_RELEASE_API, headers={
            "Accept": "application/vnd.github+json", "User-Agent": "rh-formal-replay-bootstrap/1",
            "X-GitHub-Api-Version": "2022-11-28",
        })
        with urllib.request.urlopen(request, timeout=60) as handle:
            metadata_bytes = handle.read(2_000_001)
        require(len(metadata_bytes) <= 2_000_000, "Unexpectedly large release metadata")
        metadata = json.loads(metadata_bytes)
        asset = validate_release(metadata)
        metadata_file = self.root / "downloads/lean_release_metadata.json"
        metadata_file.write_bytes(metadata_bytes)
        self.record["lean_release"] = {
            "metadata_url": LEAN_RELEASE_API, "retrieved_utc": now(),
            "metadata_file": file_identity(metadata_file), "asset": asset,
            "verification": "Hard-pinned SHA256 equals official GitHub release API digest",
        }
        archive = self.root / "downloads" / LEAN_ASSET
        if not archive.exists():
            partial = archive.with_suffix(archive.suffix + ".partial")
            require(not partial.is_symlink(), "Refusing a symlink archive staging path")
            request = urllib.request.Request(LEAN_ASSET_URL, headers={"User-Agent": "rh-formal-replay-bootstrap/1"})
            print("[lean_archive] downloading pinned official ARM64 asset", flush=True)
            downloaded = 0
            with urllib.request.urlopen(request, timeout=120) as response, partial.open("wb") as output:
                for chunk in iter(lambda: response.read(1024 * 1024), b""):
                    downloaded += len(chunk)
                    require(downloaded <= LEAN_ASSET_SIZE, "Lean archive exceeds pinned size")
                    output.write(chunk)
            require(downloaded == LEAN_ASSET_SIZE, "Lean archive truncated")
            require(sha256(partial) == LEAN_ASSET_SHA256, "Lean archive checksum mismatch")
            partial.replace(archive)
        require(not archive.is_symlink(), "Refusing a symlink Lean archive")
        require(archive.stat().st_size == LEAN_ASSET_SIZE and sha256(archive) == LEAN_ASSET_SHA256,
                "Cached Lean archive differs from pinned official asset")
        self.record["lean_release"]["archive"] = file_identity(archive)
        unpack_root = self.root / "toolchain"
        prefix = unpack_root / "lean-4.34.1-linux_aarch64"
        marker = unpack_root / ".verified-release-sha256"
        if not marker.exists():
            require(not any(unpack_root.iterdir()), "Partial toolchain present; inspect it before retrying")
            require(hasattr(tarfile, "data_filter"), "Python >=3.12 tar data filter is required")
            stderr_log = self.logs / "lean_extract_zstd.log"
            with stderr_log.open("wb") as errors:
                process = subprocess.Popen(["zstd", "--decompress", "--stdout", str(archive)], stdout=subprocess.PIPE, stderr=errors)
                try:
                    with tarfile.open(fileobj=process.stdout, mode="r|") as contents:
                        for member in contents:
                            require(member.name == prefix.name or member.name.startswith(prefix.name + "/"),
                                    "Unexpected archive top-level path")
                            contents.extract(member, path=unpack_root, filter="data")
                    process.stdout.close()
                    require(process.wait() == 0, "zstd archive decoder failed")
                except BaseException:
                    process.kill()
                    process.wait()
                    raise
            self.record["lean_release"]["extraction_log"] = file_identity(stderr_log)
            marker.write_text(LEAN_ASSET_SHA256 + "\n")
        require(marker.read_text().strip() == LEAN_ASSET_SHA256, "Toolchain marker digest mismatch")
        require(not prefix.is_symlink(), "Refusing a symlink toolchain prefix")
        self.env["PATH"] = str(prefix / "bin") + ":/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        version = self.run("lean_version", [str(prefix / "bin/lean"), "--version"], capture=True)
        require(re.search(r"\bversion 4\.34\.1,", version) is not None, "Wrong Lean version")
        require(LEAN_COMMIT in version, "Wrong Lean compiler commit")
        commit = self.run("lean_githash", [str(prefix / "bin/lean"), "--githash"], capture=True)
        require(commit == LEAN_COMMIT, "Lean --githash does not match pinned compiler")
        lake_version = self.run("lake_version", [str(prefix / "bin/lake"), "--version"], capture=True)
        require(LEAN_VERSION in lake_version, "Lake does not report required Lean version")
        self.record["runtime_versions"].update({"lean": version, "lean_githash": commit, "lake": lake_version})
        self.record["lean_invocation"] = {
            "method": "Direct official toolchain bin PATH; no elan installation or wrapper",
            "prefix": str(prefix), "PATH": self.env["PATH"],
            "ELAN_TOOLCHAIN": self.env["ELAN_TOOLCHAIN"],
            "lean_binary": file_identity(prefix / "bin/lean"),
            "lake_binary": file_identity(prefix / "bin/lake"),
        }
        verify_arm64_elf(prefix / "bin/lean")
        verify_arm64_elf(prefix / "bin/lake")
        self.save()
        return prefix

    def install_binary(self, name: str, source: Path) -> None:
        destination = self.bin / name
        require(not destination.is_symlink(), f"Refusing symlink binary destination: {destination}")
        if source != destination:
            shutil.copy2(source, destination)
        identity = file_identity(destination)
        identity.update(verify_arm64_elf(destination))
        identity["source_build_path"] = str(source)
        self.record["binaries"][name] = identity
        self.save()

    def execute(self) -> None:
        require(platform.system() == "Linux", "This bootstrap runs only on Linux")
        require(platform.machine() in ("aarch64", "arm64"), "This bootstrap pins the Linux ARM64 archive")
        require(os.getuid() != 0 and os.geteuid() != 0, "Run as an ordinary user, not root")
        require(sys.version_info >= (3, 12), "Python >=3.12 is required for safe archive extraction")
        for executable in ("git", "gcc", "make", "zstd", "go"):
            require(shutil.which(executable) is not None, f"Required system dependency missing: {executable}")
        self.record["host"] = {"system": platform.system(), "release": platform.release(),
                               "machine": platform.machine(), "uid": os.getuid(), "euid": os.geteuid(),
                               "python": sys.version, "platform": platform.platform()}
        self.record["runtime_versions"]["git"] = self.run("git_version", ["git", "--version"], capture=True)
        self.record["runtime_versions"]["gcc"] = self.run("gcc_version", ["gcc", "--version"], capture=True)
        self.record["runtime_versions"]["zstd"] = self.run("zstd_version", ["zstd", "--version"], capture=True)
        go_version = self.run("go_version", ["go", "version"], capture=True)
        match = re.search(r"\bgo(\d+)\.(\d+)(?:\.\d+)?\b", go_version)
        require(match is not None and tuple(map(int, match.groups())) >= (1, 24), "Go >=1.24 required; automatic toolchain downloads disabled")
        self.record["runtime_versions"]["go"] = go_version
        prefix = self.lean()
        comparator = self.checkout("comparator")
        exporter = self.checkout("lean4export")
        landrun = self.checkout("landrun")
        lake = str(prefix / "bin/lake")
        for name, source in (("comparator", comparator), ("lean4export", exporter)):
            configured = (source / "lean-toolchain").read_text().strip()
            require(configured == "leanprover/lean4:v4.34.0", f"Unexpected configured {name} toolchain")
            self.record["sources"][name]["configured_toolchain"] = configured
            self.record["sources"][name]["actual_build_toolchain"] = "leanprover/lean4:v" + LEAN_VERSION
            self.record["sources"][name]["build_configuration_files"] = {
                relative: file_identity(source / relative)
                for relative in ("lean-toolchain", "lakefile.toml", "lake-manifest.json")
                if (source / relative).exists()
            }
        manifest_file = comparator / "lake-manifest.json"
        manifest_hash = sha256(manifest_file)
        dependency = validate_comparator_manifest(json.loads(manifest_file.read_text()))
        self.record["comparator_dependency_manifest"] = {"file": file_identity(manifest_file), "package": dependency}
        self.run("exporter_build", [lake, "build", "lean4export"], exporter)
        self.run("comparator_build", [lake, "build", "comparator", "lean4export"], comparator)
        require(sha256(manifest_file) == manifest_hash, "Comparator build changed its pinned dependency manifest")
        dependency_path = comparator / ".lake/packages/lean4export"
        self.record["comparator_dependency_checkout"] = self.source_identity("lean4export", dependency_path, PINS["lean4export"][1])
        for name, source in (("comparator", comparator), ("lean4export", exporter)):
            identity = self.source_identity(name, source, PINS[name][1])
            self.record["sources"][name].update(identity)
        embedded_exporter = dependency_path / ".lake/build/bin/lean4export"
        self.record["comparator_dependency_exporter_binary"] = file_identity(embedded_exporter)
        self.record["comparator_dependency_exporter_binary"].update(verify_arm64_elf(embedded_exporter))
        self.install_binary("comparator", comparator / ".lake/build/bin/comparator")
        self.install_binary("lean4export", exporter / ".lake/build/bin/lean4export")
        go_files_before = {name: sha256(landrun / name) for name in ("go.mod", "go.sum")}
        self.run("landrun_modules_download", ["go", "mod", "download"], landrun)
        self.run("landrun_modules_verify", ["go", "mod", "verify"], landrun)
        module_listing = self.run("landrun_modules_list", ["go", "list", "-mod=readonly", "-m", "-json", "all"], landrun, True)
        decoder = json.JSONDecoder()
        remaining = module_listing.strip()
        modules = []
        while remaining:
            module, length = decoder.raw_decode(remaining)
            modules.append(module)
            remaining = remaining[length:].lstrip()
        self.record["landrun_go_modules"] = modules
        self.record["landrun_go_environment"] = self.run("landrun_go_env", ["go", "env", "-json", "GOVERSION", "GOARCH", "GOOS", "CGO_ENABLED", "GOTOOLCHAIN", "GOSUMDB", "GOPROXY", "GOCACHE", "GOPATH", "CC"], landrun, True)
        self.run("landrun_build", ["go", "build", "-trimpath", "-mod=readonly", "-o", str(self.bin / "landrun"), "./cmd/landrun"], landrun)
        for name, before in go_files_before.items():
            require(sha256(landrun / name) == before, f"Landrun preparation changed pinned {name}")
        self.record["sources"]["landrun"].update(self.source_identity("landrun", landrun, PINS["landrun"][1]))
        self.record["sources"]["landrun"]["go_configuration_files"] = {
            name: file_identity(landrun / name) for name in ("go.mod", "go.sum")
        }
        self.install_binary("landrun", self.bin / "landrun")
        self.run("landrun_help", [str(self.bin / "landrun"), "--help"])
        self.record["replay_PATH"] = str(self.bin) + ":" + self.env["PATH"]
        self.record["status"] = "auxiliary_tools_built"
        self.record["finished_utc"] = now()
        self.save()
        print("Auxiliary tools built. No mathematical replay or sandbox functional check was run.", flush=True)


def self_test() -> None:
    fixture = {"id": LEAN_RELEASE_ID, "tag_name": "v" + LEAN_VERSION,
               "draft": False, "prerelease": False, "assets": [{
                   "id": LEAN_ASSET_ID, "name": LEAN_ASSET, "size": LEAN_ASSET_SIZE,
                   "browser_download_url": LEAN_ASSET_URL, "digest": "sha256:" + LEAN_ASSET_SHA256,
               }]}
    validate_release(fixture)
    tests = 1
    for field, wrong in (("digest", "sha256:" + "0" * 64), ("size", 1),
                         ("browser_download_url", "https://example.invalid/archive"), ("id", 1)):
        changed = json.loads(json.dumps(fixture))
        changed["assets"][0][field] = wrong
        try:
            validate_release(changed)
        except RuntimeError:
            tests += 1
        else:
            raise AssertionError(f"Failed to reject altered asset {field}")
    package = {"name": "lean4export", "type": "git", "rev": PINS["lean4export"][1],
               "url": "https://github.com/leanprover/lean4export", "subDir": None}
    validate_comparator_manifest({"name": "Comparator", "packages": [package]})
    tests += 1
    package["rev"] = "0" * 40
    try:
        validate_comparator_manifest({"name": "Comparator", "packages": [package]})
    except RuntimeError:
        tests += 1
    else:
        raise AssertionError("Failed to reject drifted exporter dependency")
    with tempfile.TemporaryDirectory(prefix="rh-tool-bootstrap-test-") as directory:
        path = Path(directory) / "binary"
        good = bytearray(20)
        good[:6] = b"\x7fELF\x02\x01"
        good[18:20] = struct.pack("<H", 183)
        path.write_bytes(good)
        verify_arm64_elf(path)
        tests += 1
        good[18:20] = struct.pack("<H", 62)
        path.write_bytes(good)
        try:
            verify_arm64_elf(path)
        except RuntimeError:
            tests += 1
        else:
            raise AssertionError("Failed to reject x86-64 tool binary")
    print(json.dumps({"self_test": "passed", "controls": tests, "network_used": False,
                      "tool_builds_run": False, "mathematical_replay_run": False}, sort_keys=True))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path("/home/ubuntu/rh-replay-tools"))
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        self_test()
        return 0
    raw = args.root.absolute()
    require(not raw.is_symlink(), "Refusing symlink tool root")
    root = raw.resolve()
    require(root != Path("/") and root != Path.home(), "Use a dedicated auxiliary tool root")
    root.mkdir(parents=True, exist_ok=True)
    for relative in ("logs", "sources", "bin", "downloads", "toolchain", "cache"):
        directory = root / relative
        require(not directory.is_symlink(), f"Refusing symlink tool subdirectory: {directory}")
        directory.mkdir(exist_ok=True)
    bootstrap = Bootstrap(root)
    try:
        bootstrap.execute()
        return 0
    except BaseException as error:
        bootstrap.record.update({"status": "failed", "finished_utc": now(), "error": str(error)})
        bootstrap.save()
        print(f"Tool bootstrap stopped: {error}", file=sys.stderr, flush=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
