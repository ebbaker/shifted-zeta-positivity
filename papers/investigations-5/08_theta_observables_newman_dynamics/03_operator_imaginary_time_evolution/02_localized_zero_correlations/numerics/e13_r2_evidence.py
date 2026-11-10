"""Verify the frozen E13 r2 inputs and import the assessed winding census.

9 November 2026, America/New_York. Prepared for Edward Baker with OpenAI
Codex assistance. This source-free step must run inside the r2 worker's
elapsed-time budget. It checks trace identity and the accepted count tree.
"""

from fractions import Fraction
import hashlib
import json
from pathlib import Path
from types import ModuleType


OC = Path(__file__).resolve().parent.parent
REPO = OC.parents[4]
HANDOFFS = OC / "research-progress/handoffs"
REFRESH = HANDOFFS / "33_TND_OC_E13_R2_ROUTING_REFRESH_AFTER_E15_20261109.json"
REFRESH_SHA256 = "28accd4d7c29cb0544bd7e9cda0ec443b165cbef4862b455466f5d194635551d"
PROGRESS = str((OC / "research-progress/02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PROGRESS_20261108.md").relative_to(REPO))
CHECKER = OC / "numerics/check_b10_r3_cell_geometry.py"
GEOMETRY_RECORD = OC / "numerics/19_TND_OC_B10_R3_EXACT_GEOMETRY_20261109.json"


class EvidenceError(ValueError):
    """A named pre-evaluation evidence failure."""

    def __init__(self, gate, detail):
        super().__init__(f"{gate}: {detail}")
        self.gate = gate
        self.detail = detail


def require(condition, gate, detail):
    if not condition:
        raise EvidenceError(gate, detail)


def identity(data):
    return {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def expected_identity(entry):
    return {"bytes": entry["bytes"], "sha256": entry["sha256"]}


def read_bytes(path, gate):
    try:
        return path.read_bytes()
    except OSError as exc:
        raise EvidenceError(gate, f"Cannot read {path}: {exc}") from exc


def check_identity(data, expected, gate, path):
    found = identity(data)
    require(found == expected_identity(expected), gate,
            f"Digest or size mismatch at {path}: expected {expected_identity(expected)}, found {found}")
    return found


def bound_input(entry, gate):
    data = read_bytes(REPO / entry["path"], gate)
    check_identity(data, entry, gate, entry["path"])
    return data


def validate_progress_override(override, expected):
    gate = "routing_context"
    require(isinstance(override, dict), gate, "Progress02 override is not a JSON object")
    require(override.get("refresh33_sha256") == REFRESH_SHA256
            and override.get("path") == PROGRESS
            and override.get("previous") == expected,
            gate, "Progress02 override does not bind the exact refresh33 routing version")
    require(override.get("mathematical_or_execution_contract_changes") == []
            and isinstance(override.get("reason"), str) and override["reason"].strip(),
            gate, "Progress02 override lacks a routing-only reason")
    current = override.get("current")
    require(isinstance(current, dict) and type(current.get("bytes")) is int
            and current["bytes"] > 0 and isinstance(current.get("sha256"), str)
            and len(current["sha256"]) == 64 and current != expected,
            gate, "Progress02 override lacks a distinct exact size and SHA-256")
    return current


def verify_frozen_inputs(progress_override=None):
    """Return frozen bytes without rereading mutable navigation afterward."""
    gate = "frozen_input_digests"
    refresh_bytes = read_bytes(REFRESH, gate)
    require(identity(refresh_bytes)["sha256"] == REFRESH_SHA256, gate,
            f"Routing refresh33 digest mismatch at {REFRESH}")
    refresh = json.loads(refresh_bytes)
    manifest_bytes = bound_input(refresh["original_manifest"], gate)
    manifest = json.loads(manifest_bytes)
    request_bytes = bound_input(refresh["original_request"], gate)
    bound_input(refresh["supersedes_routing_refresh"], "routing_context")

    amendments = {a["path"]: a for a in refresh["amendments"]}
    entries = {row["path"]: row for row in manifest["files"]}
    require(len(entries) == len(manifest["files"]) == 41 and len(amendments) == 2
            and PROGRESS in amendments, gate, "Unexpected frozen manifest or amendment counts")
    require(entries[refresh["original_request"]["path"]]["role"] == "mathematical_contract",
            gate, "Request29 is missing its mathematical-contract row")
    checked = {}
    originals = {}
    verified = []
    for path, row in entries.items():
        role = row["role"]
        row_gate = role if role in {"routing_context", "policy_context"} else gate
        expected = expected_identity(row)
        if path in amendments:
            amendment = amendments[path]
            require(role == amendment["role"] == "routing_context"
                    and expected == amendment["previous"], row_gate,
                    f"Routing amendment does not bind original row: {path}")
            expected = amendment["current"]
        if path == PROGRESS and progress_override is not None:
            expected = validate_progress_override(progress_override, expected)
        data = (request_bytes if path == refresh["original_request"]["path"]
                else read_bytes(REPO / path, row_gate))
        actual = check_identity(data, expected, row_gate, path)
        checked[REPO / path] = data
        originals[path] = row
        verified.append({"path": path, "role": role, **actual})
    receipt = {
        "frozen_manifest": refresh["original_manifest"],
        "frozen_request": refresh["original_request"],
        "routing_refresh": {"path": str(REFRESH.relative_to(REPO)), **identity(refresh_bytes)},
        "routing_amendments": [a["path"] for a in refresh["amendments"]],
        "additional_progress_override": progress_override,
        "original_input_hashes_matched": 39,
        "verified_inputs": verified,
    }
    return manifest, checked, originals, receipt


def _verified_checker(data):
    checker = ModuleType("e13_frozen_geometry_checker")
    checker.__file__ = str(CHECKER)
    exec(compile(data, str(CHECKER), "exec"), checker.__dict__)
    return checker


def verify_evidence(*, relocated_trace=None, progress_override=None, stage=None):
    """Return sorted (exact box, count) rows and a JSON-ready evidence receipt."""
    manifest, checked, originals, receipt = verify_frozen_inputs(progress_override)
    if stage is not None:
        stage("frozen_inputs_verified")

    gate = "inherited_geometry"
    checker = _verified_checker(checked[CHECKER])
    return_bytes = checked[checker.RETURN]
    execution_bytes = checked[checker.EXECUTION]
    returned = json.loads(return_bytes)
    execution = json.loads(execution_bytes)
    require(identity(return_bytes)["sha256"] == checker.RETURN_SHA, gate,
            "Return27 does not match the frozen checker")
    require(REPO / returned["execution_record"] == checker.EXECUTION
            and identity(execution_bytes)["sha256"] == returned["execution_record_sha256"],
            gate, "Return27 and execution18 evidence link")
    require(set(execution["code_sha256"]) == {"e13_contours.py", "e13_gaussian_pilot.py"},
            gate, "Execution18 code set")
    for name, digest in execution["code_sha256"].items():
        require(identity(checked[OC / "numerics" / name])["sha256"] == digest, gate,
                f"Execution18 source-code digest mismatch: {name}")

    recorded_geometry = json.loads(checked[GEOMETRY_RECORD])
    cells = returned["certified_cell_census"]["cells"]
    try:
        geometry = checker.geometry(cells)
    except (KeyError, TypeError, ValueError) as exc:
        raise EvidenceError(gate, str(exc)) from exc
    gates = manifest["gates"]
    require(geometry == recorded_geometry["geometry"]
            and geometry["labels"] == gates["N"] == gates["singleton_cells"]
            and geometry["x_width_max"] == gates["u"]
            and geometry["y_width_max"] == gates["v"]
            and geometry["min_horizontal_gap"] == gates["adjacent_horizontal_gap_min"]
            and geometry["unordered_pairs"] == 75078,
            gate, "Exact geometry differs from the frozen census, widths, gap or pair count")
    rows = sorted((checker.coordinates(cell["box"]), cell["count"]) for cell in cells)
    require(all(box[2:] == (Fraction(-3, 32768), Fraction(3, 131072)) for box, _ in rows),
            gate, "Imaginary cell intervals differ from the acquired census")
    if stage is not None:
        stage("inherited_geometry_verified")

    gate = "trace_evidence"
    binding = manifest["external_evidence"]
    original = Path(binding["original_path"])
    trace = Path(relocated_trace) if relocated_trace is not None else original
    trace_record = execution["contour_log"]
    require(OC / binding["location_record"] == checker.EXECUTION
            and Path(execution["evidence_directory"]) / "contours.jsonl" == original
            and returned["certified_cell_census"]["source_log_sha256"] == binding["stored_sha256"]
            and all(binding[k] == trace_record[k]
                    for k in ("bytes", "stored_sha256", "canonical_content_sha256")),
            gate, "External trace bindings disagree")
    require(trace.is_file(), gate, f"Required inherited trace is missing: {trace}")
    try:
        require(trace.stat().st_size == binding["bytes"], gate, f"Trace size mismatch: {trace}")
        trace_check = checker.tree_check(trace, returned, execution)
    except EvidenceError:
        raise
    except (OSError, ValueError, KeyError, TypeError, RecursionError) as exc:
        raise EvidenceError(gate, str(exc)) from exc
    require(trace_check == recorded_geometry["trace_check"], gate,
            "Trace identity or accepted-tree receipt differs from record19")
    if stage is not None:
        stage("trace_and_tree_verified")

    gate = "evidence_negative_controls"
    try:
        rejections = checker.rejection_checks(cells)
    except ValueError as exc:
        raise EvidenceError(gate, str(exc)) from exc
    require(rejections == recorded_geometry["geometry_rejection_checks"]
            and len(rejections) == 6, gate, "Frozen malformed-census controls differ")
    noninteger = [{**cells[0], "count": 1.0}, *cells[1:]]
    try:
        checker.geometry(noninteger)
    except ValueError as exc:
        require(str(exc) == "singleton count", gate, "Noninteger control failed at the wrong predicate")
    else:
        raise EvidenceError(gate, "Noninteger count accepted")
    rejections.append("noninteger_count")

    return_row = originals[str(checker.RETURN.relative_to(REPO))]
    corrupted_return = bytes([return_bytes[0] ^ 1]) + return_bytes[1:]
    try:
        check_identity(corrupted_return, return_row, "frozen_input_digests", return_row["path"])
    except EvidenceError as exc:
        require(exc.gate == "frozen_input_digests", gate, "Corrupted bytes failed at the wrong gate")
    else:
        raise EvidenceError(gate, "Corrupted census bytes accepted")
    rejections.append("corrupted_census_bytes")
    if stage is not None:
        stage("evidence_negative_controls_verified")

    receipt.update({
        "geometry": geometry,
        "trace": {"path": str(trace.resolve()), "relocation_requested": relocated_trace is not None,
                  **trace_check},
        "evidence_controls": rejections,
        "evidence_fixtures": len(rejections),
        "winding_scope": "Inherited assessed E13 r1 outward windings and replayed count structure.",
    })
    return rows, receipt
