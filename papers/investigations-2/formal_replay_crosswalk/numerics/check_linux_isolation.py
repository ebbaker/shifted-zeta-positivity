#!/usr/bin/env python3
"""Harmless operational controls for the pinned comparator's Linux sandbox.

This checks restrictions, not Lean statements or proofs. The JSON preserves
complete command output and independent observations; startup failure never
counts as a denial. No root privileges, network downloads, or proof builds.
"""

from __future__ import annotations

import argparse
import ctypes
import datetime as dt
import errno
import hashlib
import json
import os
from pathlib import Path
import platform
import pty
import select
import shutil
import signal
import socket
import subprocess
import sys
import tempfile
import time


MARKER = "SZP_ISOLATION_RESULT="
WRITE_BYTES = b"formal-replay-isolation-fixture\n"
COMPARATOR_PIN = "d03acab154d269c06e60e4de7e4cc85deebff94b"
LANDRUN_PIN = "811cfff51ceaf3d9843708aa6d22e9b84ccac8b4"
MODEL_DISCLOSURE = {
    "model": "GPT-6 (Codex), inherited session configuration",
    "reasoning_effort": "not exposed; not inferred",
    "exact_serving_variant": "not exposed; not inferred",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def file_state(path: Path | None) -> dict | None:
    if path is None:
        return None
    if not path.exists():
        return {"exists": False}
    return {"exists": True, "size": path.stat().st_size, "sha256": sha256(path)}


def probe(operation: str, target: str) -> int:
    """One operation, with its own errno and process status as independent data."""
    result = {
        "schema_version": 1, "operation": operation, "target": target,
        "operation_success": False, "errno": None, "error_type": None,
        "message": "", "native_returncode": None,
    }
    status = 17
    try:
        if operation == "write":
            Path(target).write_bytes(WRITE_BYTES)
        elif operation == "exec":
            # Target is a byte-for-byte local copy of /usr/bin/true, not a shell.
            native = subprocess.run([target], capture_output=True, timeout=10)
            result["native_returncode"] = native.returncode
            if native.returncode != 0:
                raise RuntimeError(f"harmless native fixture exited {native.returncode}")
        elif operation == "tcp_bind":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.bind(("127.0.0.1", int(target)))
        elif operation == "tcp_connect":
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(5)
                sock.connect(("127.0.0.1", int(target)))
        elif operation == "unix_socket":
            with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM):
                pass
        else:
            raise ValueError(f"unknown probe operation: {operation}")
        result["operation_success"] = True
        status = 0
    except OSError as error:
        result.update(errno=error.errno, error_type=type(error).__name__, message=str(error))
        status = 13
    except Exception as error:
        result.update(error_type=type(error).__name__, message=str(error))
    print(MARKER + json.dumps(result, sort_keys=True), flush=True)
    return status


def run_pty(command: list[str], cwd: Path, environment: dict[str, str], timeout: float) -> dict:
    """Give systemd-run --pty an actual controlling PTY even via multipass exec."""
    started = time.monotonic()
    pid, master = pty.fork()
    if pid == 0:
        try:
            os.chdir(cwd)
            os.execvpe(command[0], command, environment)
        except BaseException as error:
            # This marker intentionally differs from the operation marker.
            os.write(2, ("SZP_FIXTURE_EXEC_FAILURE=" + repr(error) + "\n").encode())
            os._exit(127)
    chunks: list[bytes] = []
    wait_status = None
    timed_out = False
    timeout_cleanup_errors = []
    output_closed = False
    try:
        while not output_closed or wait_status is None:
            remaining = timeout - (time.monotonic() - started)
            if remaining <= 0:
                timed_out = True
                try:
                    os.killpg(pid, signal.SIGTERM)
                except OSError as error:
                    if error.errno != errno.ESRCH:
                        timeout_cleanup_errors.append(repr(error))
                time.sleep(0.1)
                if wait_status is None:
                    finished, status = os.waitpid(pid, os.WNOHANG)
                    if finished:
                        wait_status = status
                if wait_status is None:
                    try:
                        os.killpg(pid, signal.SIGKILL)
                    except OSError as error:
                        if error.errno != errno.ESRCH:
                            timeout_cleanup_errors.append(repr(error))
                        try:
                            os.kill(pid, signal.SIGKILL)
                        except OSError as direct_error:
                            if direct_error.errno != errno.ESRCH:
                                timeout_cleanup_errors.append(repr(direct_error))
                    cleanup_deadline = time.monotonic() + 2
                    while wait_status is None and time.monotonic() < cleanup_deadline:
                        finished, status = os.waitpid(pid, os.WNOHANG)
                        if finished:
                            wait_status = status
                        else:
                            time.sleep(0.01)
                    if wait_status is None:
                        timeout_cleanup_errors.append("client process was not reaped within cleanup bound")
                break
            if not output_closed:
                ready, _, _ = select.select([master], [], [], min(remaining, 0.1))
                if ready:
                    try:
                        block = os.read(master, 65536)
                    except OSError as error:
                        if error.errno != errno.EIO:
                            raise
                        block = b""
                    if block:
                        chunks.append(block)
                    else:
                        output_closed = True
            if wait_status is None:
                finished, status = os.waitpid(pid, os.WNOHANG)
                if finished:
                    wait_status = status
            if output_closed and wait_status is None:
                time.sleep(0.01)
    finally:
        os.close(master)
    return {
        "argv": command, "working_directory": str(cwd),
        "pty_allocated": True, "elapsed_seconds": round(time.monotonic() - started, 6),
        "exit_code": os.waitstatus_to_exitcode(wait_status) if wait_status is not None else None,
        "timed_out": timed_out, "stdout_stderr_combined": b"".join(chunks).decode("utf-8", "replace"),
        "timeout_cleanup_errors": timeout_cleanup_errors,
    }


def judge(observation: dict, operation: str, target: str, allowed: bool,
          permitted_errno: set[int], before: dict | None, after: dict | None) -> dict:
    reasons = []
    candidates = [line[len(MARKER):] for line in observation["stdout_stderr_combined"].splitlines()
                  if line.startswith(MARKER)]
    decoded = None
    if len(candidates) != 1:
        reasons.append(f"expected exactly one operation record; found {len(candidates)}")
    else:
        try:
            decoded = json.loads(candidates[0])
        except (json.JSONDecodeError, TypeError):
            reasons.append("operation record is invalid JSON")
    if observation["timed_out"]:
        reasons.append("command timed out")
    expected_exit = 0 if allowed else 13
    if observation["exit_code"] != expected_exit:
        reasons.append(f"service/process exit {observation['exit_code']}; expected {expected_exit}")
    if decoded is not None:
        if not isinstance(decoded, dict):
            reasons.append("operation record is not an object")
        else:
            if (decoded.get("schema_version"), decoded.get("operation"), decoded.get("target")) != (1, operation, target):
                reasons.append("operation identity does not match requested fixture")
            if decoded.get("operation_success") is not allowed:
                reasons.append("operation success differs from expectation")
            if allowed:
                if decoded.get("errno") is not None or decoded.get("error_type") is not None:
                    reasons.append("permitted operation reported an error")
                if operation == "exec" and decoded.get("native_returncode") != 0:
                    reasons.append("permitted native execution did not exit zero")
            else:
                if type(decoded.get("errno")) is not int or decoded["errno"] not in permitted_errno:
                    reasons.append(f"denial errno {decoded.get('errno')!r} is not one of {sorted(permitted_errno)}")
                if decoded.get("error_type") is None:
                    reasons.append("denial omitted its operation exception")
    if operation == "write":
        if allowed and (not after or after.get("sha256") != hashlib.sha256(WRITE_BYTES).hexdigest()):
            reasons.append("permitted write did not create the exact fixture bytes")
        if not allowed and before != after:
            reasons.append("denied write changed the fixture file")
    return {"passed": not reasons, "reasons": reasons, "operation_record": decoded}


def selftest() -> int:
    """Exercise false-pass defenses without Landrun, Linux, or a VM."""
    def observation(success=True, error=None, code=None, operation="exec", target="/fixture"):
        result = {"schema_version": 1, "operation": operation, "target": target,
                  "operation_success": success, "errno": error,
                  "error_type": None if success else "PermissionError",
                  "native_returncode": 0 if success else None}
        return {"stdout_stderr_combined": MARKER + json.dumps(result) + "\r\n",
                "exit_code": (0 if success else 13) if code is None else code, "timed_out": False}
    cases = []
    def check(name, obs, allowed, expected, operation="exec", target="/fixture", before=None, after=None):
        actual = judge(obs, operation, target, allowed, {errno.EACCES, errno.EPERM}, before, after)["passed"]
        cases.append({"name": name, "passed": actual is expected})
    check("permitted operation", observation(), True, True)
    check("permission denial", observation(False, errno.EACCES), False, True)
    check("missing fixture is not denial", observation(False, errno.ENOENT), False, False)
    check("wrong process status", observation(False, errno.EACCES, 1), False, False)
    check("service failure cannot pass", {"stdout_stderr_combined": "", "exit_code": 13, "timed_out": False}, False, False)
    check("allowed operation cannot count as denial", observation(True, None, 13), False, False)
    check("wrong operation identity", observation(False, errno.EACCES, operation="write"), False, False)
    check("wrong target identity", observation(False, errno.EACCES, target="/wrong"), False, False)
    duplicate = observation(False, errno.EACCES)
    duplicate["stdout_stderr_combined"] *= 2
    check("duplicate record rejected", duplicate, False, False)
    malformed = observation(False, errno.EACCES)
    malformed["stdout_stderr_combined"] = MARKER + "not-json\n"
    check("malformed record rejected", malformed, False, False)
    timeout = observation()
    timeout["timed_out"] = True
    check("timeout rejected", timeout, True, False)
    check("denied write mutation rejected", observation(False, errno.EACCES, operation="write"), False, False,
          operation="write", before={"exists": False}, after={"exists": True})
    check("permitted write independently observed", observation(operation="write"), True, True,
          operation="write", after={"sha256": hashlib.sha256(WRITE_BYTES).hexdigest()})
    check("missing permitted write rejected", observation(operation="write"), True, False,
          operation="write", after={"exists": False})
    print(json.dumps({"selftest": cases, "all_passed": all(case["passed"] for case in cases)}, indent=2))
    return 0 if all(case["passed"] for case in cases) else 1


def tool_version(command: list[str], environment: dict[str, str] | None = None) -> dict:
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=10, env=environment)
        return {"argv": command, "exit_code": result.returncode,
                "stdout": result.stdout, "stderr": result.stderr}
    except Exception as error:
        return {"argv": command, "error": repr(error)}


def landlock_abi() -> dict:
    # NR_landlock_create_ruleset is 444 on these asm-generic/x86_64 architectures.
    if platform.machine() not in {"aarch64", "arm64", "x86_64"}:
        return {"queried": False, "reason": "syscall number not specified for this architecture"}
    library = ctypes.CDLL(None, use_errno=True)
    library.syscall.restype = ctypes.c_long
    ctypes.set_errno(0)
    result = library.syscall(ctypes.c_long(444), ctypes.c_void_p(), ctypes.c_size_t(0), ctypes.c_uint(1))
    return {"queried": True, "abi": result if result >= 0 else None,
            "errno": ctypes.get_errno() if result < 0 else None}


def suite(args: argparse.Namespace) -> dict:
    if sys.platform != "linux":
        raise RuntimeError("Linux is required for operational checks")
    if os.getuid() == 0:
        raise RuntimeError("run as an unprivileged Linux user; UID 0 is rejected")
    script = Path(__file__).resolve(strict=True)
    landrun = Path(args.landrun).resolve(strict=True)
    lean_prefix = Path(args.lean_prefix).resolve(strict=True)
    if not landrun.is_file() or not os.access(landrun, os.X_OK) or not lean_prefix.is_dir():
        raise RuntimeError("Landrun must be executable and Lean prefix must be a directory")
    systemd = shutil.which("systemd-run")
    true = shutil.which("true")
    git = shutil.which("git")
    if not systemd or not true or not git:
        raise RuntimeError("systemd-run, native true, and git must be available")
    systemd = str(Path(systemd).resolve(strict=True))
    true_path = Path(true).resolve(strict=True)
    git_path = Path(git).resolve(strict=True)
    python = str(Path(sys.executable).resolve(strict=True))
    # Avoid a shell built-in or executable script as the native execution fixture.
    if true_path.read_bytes()[:4] != b"\x7fELF":
        raise RuntimeError("true fixture source is not an ELF native executable")
    environment = dict(os.environ)
    added_environment = {}
    if not environment.get("XDG_RUNTIME_DIR"):
        runtime_dir = Path(f"/run/user/{os.getuid()}")
        if runtime_dir.is_dir() and runtime_dir.stat().st_uid == os.getuid():
            environment["XDG_RUNTIME_DIR"] = str(runtime_dir)
            added_environment["XDG_RUNTIME_DIR"] = str(runtime_dir)
    # lake env normally supplies LEAN_PATH to comparator; make the fixture's
    # exporter environment explicit even if its caller is multipass exec.
    environment.setdefault("LEAN_PATH", str(lean_prefix / "lib" / "lean"))
    record = {
        "schema_version": 1, "kind": "harmless_linux_isolation_controls",
        "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
        "prepared_for": "Edward Baker", "llm_disclosure": MODEL_DISCLOSURE,
        "source_profiles": {
            "comparator_commit": COMPARATOR_PIN, "landrun_commit_expected": LANDRUN_PIN,
            "source_url": f"https://github.com/leanprover/comparator/blob/{COMPARATOR_PIN}/Main.lean",
            "profile_lines": "buildLandrunArgs:73-79, safeLakeBuild:104-121, safeExport:122-137",
            "base_flags": ["--best-effort", "--ro", "/", "--rw", "/dev", "-ldd", "-add-exec"],
            "guard": ["--property=RestrictAddressFamilies=~AF_UNIX", "--user", "--pty"],
            "scope": "permission-profile fixtures; not comparator execution or proof verification",
            "binary_provenance": "binary SHA recorded; caller must separately tie build to expected source pin",
        },
        "host": {"platform": platform.platform(), "kernel": platform.release(),
                 "architecture": platform.machine(), "uid": os.getuid(), "gid": os.getgid(),
                 "landlock": landlock_abi()},
        "tools": {
            "runner": {"path": str(script), "sha256": sha256(script)},
            "landrun": {"path": str(landrun), "sha256": sha256(landrun), "version": tool_version([str(landrun), "--version"])},
            "systemd_run": {"path": systemd, "sha256": sha256(Path(systemd)), "version": tool_version([systemd, "--version"])},
            "python": {"path": python, "sha256": sha256(Path(python)), "version": sys.version},
            "native_fixture_source": {"path": str(true_path), "sha256": sha256(true_path)},
            "lean_prefix": str(lean_prefix), "git": str(git_path),
        },
        "selected_environment": {key: environment.get(key) for key in
                                 ("PATH", "HOME", "LEAN_PATH", "ELAN_HOME", "ELAN_TOOLCHAIN", "XDG_RUNTIME_DIR")},
        "environment_added_for_user_bus": added_environment,
        "controls": [],
    }
    with tempfile.TemporaryDirectory(prefix="szp-isolation-", dir=args.fixture_parent) as root_text:
        root = Path(root_text).resolve()
        project = root / "checking-project"
        lake = project / ".lake"
        lake.mkdir(parents=True)
        # The read-only project itself is the outside-.lake control, so these
        # denials test the same location class as challenge/source files.
        outside_write = project / "fixture-source.txt"
        inside_write = lake / "fixture-write.txt"
        outside_exec = project / "fixture-native-true"
        inside_exec = lake / "fixture-native-true"
        for destination in (outside_exec, inside_exec):
            shutil.copyfile(true_path, destination)
            destination.chmod(0o755)
            if sha256(destination) != sha256(true_path):
                raise RuntimeError("copied native fixture identity mismatch")
        record["fixture_root"] = str(root)
        record["fixtures_deleted_after_run"] = True
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as connector_listener:
            connector_listener.bind(("127.0.0.1", 0))
            connector_listener.listen(8)
            connect_port = str(connector_listener.getsockname()[1])
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as reserve:
                reserve.bind(("127.0.0.1", 0))
                bind_port = str(reserve.getsockname()[1])
            record["network_fixture"] = {"scope": "loopback only; no payload is sent",
                                         "connect_listener_port": int(connect_port), "bind_control_port": int(bind_port)}

            def run(name, operation, target, profile, allowed, extra_flags=None):
                target_text = str(target)
                file_target = Path(target_text) if operation == "write" else None
                before = file_state(file_target)
                child = [python, "-I", "-B", str(script), "--_probe", operation, "--target", target_text]
                command = child
                unit_name = None
                if profile != "baseline":
                    flags = ["--best-effort", "--ro", "/", "--rw", "/dev", "-ldd", "-add-exec"]
                    # Exact order of the comparator's env/read/write/exec flags.
                    passed_environment = ["PATH", "HOME", "LEAN_ABORT_ON_PANIC"]
                    if profile == "export":
                        passed_environment.insert(2, "LEAN_PATH")
                    for key in passed_environment:
                        flags += ["--env", key]
                    flags += ["--ro", str(project)]
                    if profile == "build":
                        flags += ["--rwx", str(lake), "--rox", str(lean_prefix), "--rox", str(git_path)]
                    else:
                        flags += ["--ro", str(lake), "--rox", str(lean_prefix)]
                    flags += list(extra_flags or [])
                    unit_name = f"szp-isolation-{os.getpid()}-{len(record['controls'])}.service"
                    command = [systemd, "--property=RestrictAddressFamilies=~AF_UNIX", "--user", "--pty",
                               "--unit=" + unit_name,
                               "--property=RuntimeMaxSec=" + str(args.timeout) + "s",
                               "-E", "PATH=" + environment.get("PATH", ""),
                               "-E", "HOME=" + environment.get("HOME", ""),
                               "-E", "LEAN_PATH=" + environment["LEAN_PATH"],
                               "-E", "LEAN_ABORT_ON_PANIC=1",
                               "--working-directory=" + str(project), "--", str(landrun)] + flags + ["--"] + child
                try:
                    observation = run_pty(command, project, environment, args.timeout)
                except Exception as error:
                    observation = {"argv": command, "working_directory": str(project),
                                   "pty_allocated": True, "elapsed_seconds": None,
                                   "exit_code": None, "timed_out": False,
                                   "stdout_stderr_combined": "", "operational_error": repr(error)}
                if unit_name and observation["timed_out"]:
                    systemctl = shutil.which("systemctl")
                    observation["timed_out_unit_cleanup"] = tool_version([systemctl, "--user", "stop", unit_name], environment) if systemctl else {"error": "systemctl unavailable; RuntimeMaxSec remains the service bound"}
                after = file_state(file_target)
                denial_errno = {errno.EAFNOSUPPORT} if operation == "unix_socket" else {errno.EACCES, errno.EPERM}
                verdict = judge(observation, operation, target_text, allowed, denial_errno, before, after)
                record["controls"].append({"name": name, "permission_profile": profile,
                                            "operation": operation, "target": target_text,
                                            "expected_allowed": allowed,
                                            "permitted_denial_errno": sorted(denial_errno) if not allowed else [],
                                            "additional_network_control_flags": list(extra_flags or []),
                                            "transient_unit": unit_name,
                                            "file_before": before, "file_after": after,
                                            "command_result": observation, **verdict})

            run("outside_write_baseline_allowed", "write", outside_write, "baseline", True)
            run("build_outside_write_denied", "write", outside_write, "build", False)
            run("build_lake_write_allowed", "write", inside_write, "build", True)
            run("export_lake_write_denied", "write", inside_write, "export", False)
            run("outside_native_exec_baseline_allowed", "exec", outside_exec, "baseline", True)
            run("build_outside_native_exec_denied", "exec", outside_exec, "build", False)
            run("build_lake_native_exec_allowed", "exec", inside_exec, "build", True)
            run("export_lake_native_exec_denied", "exec", inside_exec, "export", False)
            run("tcp_bind_baseline_allowed", "tcp_bind", bind_port, "baseline", True)
            run("build_tcp_bind_denied", "tcp_bind", bind_port, "build", False)
            run("build_tcp_bind_explicit_port_allowed", "tcp_bind", bind_port, "build", True, ["--bind-tcp", bind_port])
            run("tcp_connect_baseline_allowed", "tcp_connect", connect_port, "baseline", True)
            run("build_tcp_connect_denied", "tcp_connect", connect_port, "build", False)
            run("build_tcp_connect_explicit_port_allowed", "tcp_connect", connect_port, "build", True, ["--connect-tcp", connect_port])
            run("unix_socket_baseline_allowed", "unix_socket", "AF_UNIX", "baseline", True)
            run("guarded_build_unix_socket_creation_denied", "unix_socket", "AF_UNIX", "build", False)
    record["all_controls_passed"] = len(record["controls"]) == 16 and all(control["passed"] for control in record["controls"])
    record["passed_count"] = sum(control["passed"] for control in record["controls"])
    record["proof_replay_performed"] = False
    record["limitations"] = [
        "Tests permission profiles with harmless Python/native fixtures, not comparator or theorem execution.",
        "No general proof of kernel, systemd, Landlock, tool-source, or operating-system integrity.",
        "TCP tests cover IPv4 loopback bind/connect. No DNS, UDP, IPv6, inherited-descriptor, or kernel attack tests.",
        "AF_UNIX test checks socket creation under the actual systemd guard, not every IPC mechanism.",
        "The source profile keeps comparator's /dev read/write allowance and .lake execution allowance.",
        "Fixtures are deleted after recording; all command output, identities, and operation errno remain in JSON.",
    ]
    return record


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--landrun", help="absolute path to separately built pinned Landrun")
    parser.add_argument("--lean-prefix", help="actual isolated Lean 4.34.1 prefix")
    parser.add_argument("--output", help="new JSON record path (existing files are rejected)")
    parser.add_argument("--fixture-parent", help="optional writable directory for disposable fixtures")
    parser.add_argument("--timeout", type=float, default=30.0, help="per-control timeout in seconds (default 30)")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--_probe", choices=("write", "exec", "tcp_bind", "tcp_connect", "unix_socket"), help=argparse.SUPPRESS)
    parser.add_argument("--target", help=argparse.SUPPRESS)
    args = parser.parse_args()
    if args._probe:
        if args.target is None:
            parser.error("probe target missing")
        return probe(args._probe, args.target)
    if args.selftest:
        return selftest()
    if not args.landrun or not args.lean_prefix or not args.output:
        parser.error("--landrun, --lean-prefix and --output are required")
    if not 1 <= args.timeout <= 60:
        parser.error("--timeout must be between 1 and 60 seconds")
    output = Path(args.output).absolute()
    if output.exists():
        parser.error("output already exists; preserve prior evidence and select a new filename")
    output.parent.mkdir(parents=True, exist_ok=True)
    try:
        result = suite(args)
    except Exception as error:
        result = {"schema_version": 1, "kind": "harmless_linux_isolation_controls",
                  "timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                  "llm_disclosure": MODEL_DISCLOSURE, "all_controls_passed": False,
                  "proof_replay_performed": False, "operational_error": repr(error)}
    with output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2, sort_keys=True)
        stream.write("\n")
    print(json.dumps({"record": str(output), "all_controls_passed": result["all_controls_passed"],
                      "passed_count": result.get("passed_count", 0), "control_count": len(result.get("controls", [])),
                      "operational_error": result.get("operational_error")}, sort_keys=True))
    return 0 if result["all_controls_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
