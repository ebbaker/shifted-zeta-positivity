"""E04 joined path certificate for the first counted theta gap.

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance,
gpt-6.2-sol/ultra execution and gpt-6.2-astra/ultra lead.
Run with Python 3 and python-flint 0.9.0.
"""

from hashlib import sha256
import json
from pathlib import Path

import flint
from flint import arb, ctx


HERE = Path(__file__).resolve().parent
E03 = "03_SIGNED_PATH_999_1000_20261120.json"
INPUTS = {
    E03: "41f46ec89f32a5e5d30e66fa3d3c714c8580cf748c40fbfd7a7630091d98408e",
    "ez_signed_transport.py": "4b703d8371bef5e49de1a4e828ab21587d59e9a9a619db380d5af40eb6ebe383",
    "ez_direct_endpoint.py": "83420fc2b33e6810542fba5094365d55c8c7bd67ea81d5e886d8001b7b3965b6",
    "ez_direct_velocity.py": "2658a6d7f6e48a9de339779ad848b52690a4ffd9c77c27d33fbba934de493eba",
}
MESH = 1024
OVERLAP_FIRST = MESH // 2
JOIN = MESH
END = 16 * MESH


class GateFailure(ArithmeticError):
    def __init__(self, gate, **details):
        super().__init__(gate)
        self.details = details


def require(condition, gate, **details):
    if not condition:
        raise GateFailure(gate, **details)


def verified_e03():
    for name, digest in INPUTS.items():
        data = (HERE / name).read_bytes()
        actual = sha256(data).hexdigest()
        require(actual == digest, "pinned input digest", name=name, expected=digest, actual=actual)
        if name == E03:
            e03 = json.loads(data)
    return e03


def from_bounds(bounds):
    # Parsing either number incurs its own outward decimal error.
    return arb(bounds["lower"]).union(arb(bounds["upper"]))


def old_direct_D(endpoint):
    return arb(endpoint["D_lower"]).union(arb(endpoint["D_upper"]))


def exact_counted_roots(transport, moments, s):
    d = transport.tilted_moments(moments, arb(s))
    b = transport.center()
    q1 = arb.pi() / 2
    w = transport.difference_moments(d, b)[1]
    return transport.counted_roots(d, b, q1, 3 * q1, transport.SPATIAL_CAP, w)[:2]


def first_normalized_sign_loss(transport, summary, records, first_cell):
    if summary["normalized_log_gap_drift_sign"] == "positive":
        return None
    b = transport.center()
    q1 = arb.pi() / 2
    for index, (s, _, _, d) in enumerate(records, start=first_cell):
        row = transport.bound_cell(d, b, q1, 3 * q1, transport.SPATIAL_CAP)
        if not row["normalized_drift"] > 0:
            return {
                "absolute_cell": index,
                "s": s.str(25),
                "normalized_log_gap_drift": transport.bounds([row["normalized_drift"]]),
                "fourth_cumulant": transport.bounds([row["fourth_cumulant"]]),
            }
    raise GateFailure("inconsistent normalized sign audit", first_cell=first_cell)


def direct_path_record(direct_path, records, first_cell):
    report = direct_path(records)
    failure = report["first_fail"]
    if failure is not None:
        failure["absolute_cell"] = first_cell + failure["cell"]
    return report


def check_join(transport, moments, anchors, old):
    direct = old["direct_endpoint"]
    old_roots = [from_bounds(bounds) for bounds in direct["root_brackets"]]
    tubes = exact_counted_roots(transport, moments, 1)
    tube_bounds = [transport.bounds([root]) for root in tubes]
    contained = [tube.contains(bracket) for tube, bracket in zip(tubes, old_roots)]
    require(all(contained), "t=999 marked root join", counted_roots=tube_bounds,
            E03_direct_roots=direct["root_brackets"], contained=contained)
    I1 = from_bounds(old["transport"]["integrated_normalized_drift"])
    joined_D, _, _, _ = transport.endpoint_discriminant(moments, anchors, arb(1), I1)
    direct_D = old_direct_D(direct)
    e03_transport_D = from_bounds(old["transport"]["endpoint_D"])
    joined_bounds = transport.bounds([joined_D])
    require(joined_D.contains(direct_D) and joined_D.overlaps(e03_transport_D),
            "t=999 discriminant join", joined=joined_bounds,
            E03_transport=old["transport"]["endpoint_D"],
            E03_matched_direct=transport.bounds([direct_D]))
    return I1, old_roots, {
        "counted_roots": tube_bounds,
        "contains_E03_direct_roots": contained,
        "transported_D": joined_bounds,
        "overlaps_E03_transport_D": True,
        "contains_E03_matched_direct_D": True,
        "stored_integral_0_to_1": transport.bounds([I1]),
    }


def joined_margins(transport, old, overlap, added, anchor_D):
    charts = [old["transport"], overlap, added]
    drift_lowers = [arb(chart["physical_backward_log_gap_drift"]["lower"]).lower()
                    for chart in charts]
    strict_rate = min(drift_lowers)
    require(strict_rate > 0 and anchor_D > 0, "joined strict physical path margin",
            log_gap_rates=[c.str(24) for c in drift_lowers], anchor_D=anchor_D.str(50))
    result = {
        "physical_backward_log_gap_drift": transport.bounds([
            from_bounds(chart["physical_backward_log_gap_drift"]) for chart in charts
        ]),
        "normalized_log_gap_drift": transport.bounds([
            from_bounds(chart["normalized_log_gap_drift"]) for chart in charts
        ]),
        "current_floor_lower": min(arb(c["current_floor_min"]).lower() for c in charts).str(24),
        "phase_reach_margin_lower": min(
            arb(c["phase_reach_margin_min"]).lower() for c in charts
        ).str(24),
        "spatial_gap_lower": min(
            arb(c["spatial_gap_lower_min"]).lower() for c in charts
        ).str(24),
        "whole_path_D_lower": anchor_D.lower().str(50),
        "partial_path_exponential_rate_lower": (2 * strict_rate).lower().str(24),
    }
    return result


def main():
    ctx.prec = 224
    result = {
        "date": "2026-11-20",
        "prepared_for": "Edward Baker",
        "assistance": "OpenAI Codex, gpt-6.2-sol/ultra execution, gpt-6.2-astra/ultra lead",
        "python_flint": flint.__version__,
        "precision_bits": ctx.prec,
        "packet": "AGC-EZ-E04 R1",
        "positive_zero_indices": [1, 2],
        "spatial_cap": 4,
        "anchor_time": 1000,
        "anchor_center": "671/500",
        "anchor_moment_degree": 28,
        "new_chart_time": [984, 999.5],
        "joined_time": [984, 1000],
        "new_cells_per_unit": MESH,
        "input_sha256": INPUTS,
    }
    stage = "verify E03 inputs"
    try:
        old = verified_e03()["result"]
        import ez_signed_transport as transport
        from ez_direct_endpoint import direct_endpoint
        from ez_direct_velocity import direct_path

        stage = "load pinned anchor"
        moments, anchors = transport.load_anchor()
        stage = "verify exact join at t=999"
        I1, old_roots, result["join"] = check_join(transport, moments, anchors, old)
        stage = "transport over the overlap"
        overlap, _, overlap_records, _ = transport.run_transport(
            moments, anchors, OVERLAP_FIRST, JOIN, MESH
        )
        result["overlap_audit"] = overlap
        result["overlap_audit_contributes_to_endpoint_integral"] = False
        stage = "transport through the earlier cells"
        added, _, added_records, I_new = transport.run_transport(
            moments, anchors, JOIN, END, MESH
        )
        result["earlier_transport"] = added
        stage = "verify adjacent-cell guards at t=999"
        overlap_tubes = overlap_records[-1][1:3]
        added_tubes = added_records[0][1:3]
        both_contain = [left.contains(root) and right.contains(root)
                        for left, right, root in zip(overlap_tubes, added_tubes, old_roots)]
        result["join"]["adjacent_cell_tubes_contain_E03_direct_roots"] = both_contain
        require(all(both_contain), "t=999 adjacent-cell root join",
                later_tubes=[transport.bounds([x]) for x in overlap_tubes],
                earlier_tubes=[transport.bounds([x]) for x in added_tubes],
                E03_direct_roots=old["direct_endpoint"]["root_brackets"])

        stage = "accumulate joined transport"
        I = I1 + I_new
        D, ratio, mean, anchor_D = transport.endpoint_discriminant(moments, anchors, arb(16), I)
        old_terms = old["transport"]["velocity_terms"]
        new_terms = added["velocity_terms"]
        integrated_terms = {}
        for degree, term in old_terms.items():
            name = "integrated_divided_difference_term"
            integrated_terms[degree] = transport.bounds([
                from_bounds(term[name]) + from_bounds(new_terms[degree][name])
            ])
        paid_remainder = sum(arb(record["integrated_spatial_remainder_upper"]).upper()
                             for record in (old["transport"], added))
        result["joined_transport"] = {
            "integral_0_to_16": transport.bounds([I]),
            "integral_parts_s": [[0, 1], [1, 16]],
            "integrated_signed_velocity_terms": integrated_terms,
            "integrated_spatial_remainder_upper": paid_remainder.upper().str(24),
            "endpoint_mean": transport.bounds([mean]),
            "endpoint_mean_ratio": transport.bounds([ratio]),
            "endpoint_mean_ratio_width_upper": (2 * ratio.rad()).upper().str(24),
            "anchor_D": transport.bounds([anchor_D]),
            "anchor_D_width_upper": (2 * anchor_D.rad()).upper().str(24),
            "endpoint_D": transport.bounds([D]),
            "endpoint_D_width_upper": (2 * D.rad()).upper().str(24),
            **joined_margins(transport, old, overlap, added, anchor_D),
        }
        loss = first_normalized_sign_loss(transport, overlap, overlap_records, OVERLAP_FIRST)
        if loss is None:
            loss = first_normalized_sign_loss(transport, added, added_records, JOIN)
        result["joined_transport"]["first_normalized_sign_loss"] = loss
        result["joined_transport"]["normalized_drift_strictly_positive"] = (
            loss is None and old["transport"]["normalized_log_gap_drift_sign"] == "positive"
        )

        stage = "matched direct implicit velocities"
        result["direct_path"] = {
            "old_slab_from_E03": old["direct_path"],
            "overlap": direct_path_record(direct_path, overlap_records, OVERLAP_FIRST),
            "earlier": direct_path_record(direct_path, added_records, JOIN),
        }
        result["direct_path"]["strict_on_all_joined_cells"] = all(
            row["strict"] for row in result["direct_path"].values()
        )
        stage = "matched direct endpoint at t=984"
        hints = exact_counted_roots(transport, moments, 16)
        endpoint, direct_D, _ = direct_endpoint(moments, 16, 1, hints)
        result["direct_endpoint"] = endpoint
        result["direct_endpoint"]["cauchy_radius"] = 1
        result["transport_contains_direct_endpoint"] = D.contains(direct_D)
        result["transport_overlaps_direct_endpoint"] = D.overlaps(direct_D)
        require(D.overlaps(direct_D), "t=984 transport and direct endpoint intersection",
                transport=transport.bounds([D]), direct=transport.bounds([direct_D]))
        result["status"] = "certified"
    except ArithmeticError as error:
        result["status"] = "required gate failed"
        result["failure"] = {
            "stage": stage,
            "gate": str(error),
            **getattr(error, "details", {}),
        }
    return result


if __name__ == "__main__":
    receipt = main()
    print(json.dumps(receipt, indent=2))
    raise SystemExit(receipt["status"] != "certified")
