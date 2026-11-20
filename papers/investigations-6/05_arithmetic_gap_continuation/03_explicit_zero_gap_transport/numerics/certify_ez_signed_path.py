"""Issue-specific path and endpoint comparisons for the explicit-gap branch.

20 November 2026. Prepared for Edward Baker with OpenAI Codex assistance.
Integration gpt-6.2-astra/ultra, mathematical components gpt-6.2-sol/ultra.
Run with Python 3 and python-flint 0.9.0.
"""
from hashlib import sha256
import json
from pathlib import Path

import flint
from flint import arb, ctx

from ez_direct_endpoint import direct_endpoint
from ez_direct_velocity import direct_path
from ez_signed_transport import load_anchor, run_transport

HERE = Path(__file__).resolve().parent
OPENING = "01_BACKWARD_GAP_999_1000_20261120.json"


def opening_receipt():
    data = (HERE / OPENING).read_bytes()
    if sha256(data).hexdigest() != "cc7a443c2ac8ceb06826bc31905e4a0b2024f64c43394b85a4e383748e924a32":
        raise ValueError("Opening comparison receipt changed")
    return json.loads(data)


def e03(moments, anchors):
    historical = opening_receipt()
    transport, propagated, cells, integral = run_transport(moments, anchors, 0, 256, 256)
    direct, endpoint, _ = direct_endpoint(moments, 1, 3, cells[-1][1:3])
    holdout = arb(historical["full_endpoint_D"])
    path = direct_path(cells)
    if not (propagated.contains(endpoint) and holdout.overlaps(endpoint)
            and len(cells) == 256):
        raise ArithmeticError("E03 endpoint, holdout, or cell cover consistency failed")
    return {
        "physical_times": [999, 1000], "precision_bits": ctx.prec,
        "historical_transport_width": historical["transport_width"],
        "historical_six_moment_direct_width": historical["matched_width"],
        "opening_full_source_holdout": historical["full_endpoint_D"],
        "holdout_overlaps_direct": True,
        "integrated_transport_contains_direct": True,
        "transport": transport, "direct_endpoint": direct, "direct_path": path,
    }


def main():
    ctx.prec = 224
    moments, anchors = load_anchor()
    return {
        "date": "2026-11-20", "prepared_for": "Edward Baker",
        "assistance": "OpenAI Codex, gpt-6.2-astra/ultra lead, gpt-6.2-sol/ultra component execution",
        "python_flint": flint.__version__, "packet": "AGC-EZ-E03 R1",
        "positive_zero_indices": [1, 2], "spatial_cap": 4,
        "anchor": {"time": 1000, "center": "671/500", "highest_moment": 28,
                   "moment_28": moments[28].str(35), "initial_root_balls": [x.str(52) for x in anchors]},
        "result": e03(moments, anchors),
    }


if __name__ == "__main__":
    print(json.dumps(main(), indent=2))
