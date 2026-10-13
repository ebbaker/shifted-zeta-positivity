#!/usr/bin/env python3
"""Independent offline response fixtures for the reviewed queue; no VM calls."""
from pathlib import Path
import importlib.util
import json
import sys
import tempfile

source = Path(sys.argv[1]).resolve()
spec = importlib.util.spec_from_file_location("reviewed_replay_queue", source)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
results = []

def check(name, action, refusal=False):
    try:
        action()
        passed = not refusal
        observed = "returned"
    except m.Refusal as error:
        passed = refusal
        observed = str(error)
    except Exception as error:
        passed = False
        observed = type(error).__name__ + ": " + str(error)
    results.append({"control": name, "passed": passed, "observation": observed})

quiet = {"unit_listing": {"exit_code": 0}, "running_records": [], "runners": [],
         "active_units": [], "math_processes": []}
one = {**quiet, "runners": [{"pid": 100, "target": "zeta", "attempt": "001"}],
       "active_units": ["rh-replay-zeta-001.service"]}
two = {**one, "runners": one["runners"] + [{"pid": 101, "target": "zeta", "attempt": "001"}]}
check("one matching runner may be adopted", lambda: m.ensure_quiescent(one, ["zeta", "001"]))
check("two matching runners are ambiguous", lambda: m.ensure_quiescent(two, ["zeta", "001"]), True)
check("adopted runner prevents reset", lambda: m.ensure_quiescent(one), True)

failure = {"status": "unsuccessful_attempt_requires_classification", "process_result": {"exit_code": 143, "timed_out": False}}
timeout = {"unit_properties_command": {"exit_code": 0}, "unit_properties": {
    "LoadState": "loaded", "Result": "timeout", "RuntimeMaxUSec": "2h",
    "ActiveEnterTimestampMonotonic": "1000000", "ActiveExitTimestampMonotonic": "7201000000"}}
check("pure recorded runtime cutoff", lambda: m.require(m.classify(failure, "", timeout, 7200) == "operational_runtime_timeout", "runtime not classified"))
check("compile error plus timeout never retries", lambda: m.require(m.classify(failure, "error: type mismatch in solution", timeout, 7200) != "operational_runtime_timeout", "earlier compile failure was masked"))
check("failed build plus timeout never retries", lambda: m.require(m.classify(failure, "Some required builds logged failures", timeout, 7200) != "operational_runtime_timeout", "earlier build failure was masked"))
check("resource error plus timeout never retries", lambda: m.require(m.classify(failure, "Out of memory", timeout, 7200) == "operational_resource_failure", "resource failure was masked"))
wrong_bound = json.loads(json.dumps(timeout))
wrong_bound["unit_properties"]["RuntimeMaxUSec"] = "1h"
check("different service timeout cannot authorize retry", lambda: m.require(m.classify(failure, "", wrong_bound, 7200) != "operational_runtime_timeout", "service limit mismatch was ignored"))

success = {"status": "comparator_accepted", "process_result": {"exit_code": 0, "timed_out": False},
           "kernel_result": "accepted", "axiom_allowed_set_compliance": "passed", "statement_comparison": "passed"}
success_log = "Lean default kernel accepts the solution\nYour solution is okay!\n"
failed_unit = {"unit_properties_command": {"exit_code": 0}, "unit_properties": {"LoadState": "loaded", "Result": "oom-kill"}}
check("loaded service failure beats success markers", lambda: m.require(m.classify(success, success_log, failed_unit, 7200) != "comparator_accepted", "failed unit accepted"))
failed_properties = {"unit_properties_command": {"exit_code": 1}, "unit_properties": {"LoadState": "loaded", "Result": "success"}}
check("failed property observation cannot confirm loaded success", lambda: m.require(m.classify(success, success_log, failed_properties, 7200) != "comparator_accepted", "failed property observation was trusted"))
failed_timeout_query = json.loads(json.dumps(timeout)); failed_timeout_query["unit_properties_command"]["exit_code"] = 1
check("failed property observation cannot confirm timeout", lambda: m.require(m.classify(failure, "", failed_timeout_query, 7200) != "operational_runtime_timeout", "failed property observation authorized retry"))

configuration = {"fixture": True}
context = {"baseline": "rh-replay.clean", "baseline_label": "clean", "guest_records": "/guest/records",
           "guest_project": "/guest/source/lean", "replay_PATH": "/trusted/bin:/trusted/lean/bin:/usr/bin",
           "targets": {"zeta": {"configuration": configuration, "configuration_sha256": "a" * 64,
                                "config_guest_path": "ComparatorChallenges/QuasiRiemannHypothesis.json"}}}
command = ["systemd-run", "--property=RestrictAddressFamilies=~AF_UNIX", "--user", "--pty", "--unit=rh-replay-zeta-001",
           "--property=RuntimeMaxSec=7200s", "-E", "PATH=" + context["replay_PATH"], "-E", "ELAN_TOOLCHAIN=leanprover/lean4:v4.34.1",
           "--working-directory=" + context["guest_project"], "--", "bash", "-c", "lake env comparator \"$1\"", "bash",
           context["targets"]["zeta"]["config_guest_path"]]
record = {"schema": "guarded-mathematical-replay-v1", "target": "zeta", "attempt": "001", "baseline_name": "clean",
          "fresh_OAI_and_challenge_build_trees_absent": True, "untrusted_solution_compilation_outside_guard": False,
          "configuration": configuration, "configuration_sha256": "a" * 64, "status": "comparator_accepted",
          "finished_utc": "2026-10-13T01:00:00+00:00", "command": command, "process_result": {"argv": command, "exit_code": 0, "timed_out": False},
          "log": {"path": "/guest/records/replay_zeta_001.log", "sha256": "b" * 64, "bytes": 10},
          "source_preflight_log": {"path": "/guest/records/replay_zeta_001_source_preflight.log", "sha256": "c" * 64}}
observed = {"sha256": "d" * 64, "bytes": len(json.dumps(record))}
check("record matches exact guarded command", lambda: m.validate_record(record, observed, context, "zeta", "001"))
bad = json.loads(json.dumps(record)); bad["command"][0] = "echo"
check("guard-like echo arguments are rejected", lambda: m.validate_record(bad, observed, context, "zeta", "001"), True)
bad = json.loads(json.dumps(record)); bad["process_result"]["argv"] = ["echo", "fake"]
check("nested process argv drift is rejected", lambda: m.validate_record(bad, observed, context, "zeta", "001"), True)

class FakeClient:
    def __init__(self): self.calls = []
    def call(self, *args, **kwargs):
        self.calls.append(args)
        raise AssertionError("A VM command was attempted by a refusal fixture")

with tempfile.TemporaryDirectory(prefix="queue-scope-review-") as temp:
    root = Path(temp)
    for phase in ("stop_requested", "restore_requested", "start_requested", "launch_committed"):
        fake = FakeClient()
        state = {"phase": phase, "current": ["zeta", "001"], "context": {}, "run_directory": str(root)}
        def interrupted(state=state, fake=fake):
            try: m.Queue(fake, root / "state.json", state, 60).run()
            finally: m.require(not fake.calls, "ambiguous state issued a VM command")
        check("interrupted " + phase + " halts before mutation", interrupted, True)
    check("oversized small JSON is refused", lambda: m.atomic_json(root / "oversized.json", {"data": "x" * 1_000_000}), True)
    check("refused oversized JSON was not written", lambda: m.require(not (root / "oversized.json").exists(), "oversized output was created"))

output = {"reviewed_queue_sha256": m.digest(source), "controls": results,
          "all_passed": all(item["passed"] for item in results), "VM_commands_executed": False}
print(json.dumps(output, indent=2))
sys.exit(0 if output["all_passed"] else 1)
