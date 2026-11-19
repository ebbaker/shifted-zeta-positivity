"""Illustrative readout of an existing certificate, for Edward Baker.

19 November 2026; OpenAI Codex assistance, actual model/effort unavailable.
Uses binary floating point for rounded exposition, not interval certification.
No new source evaluations or changes to the inherited certificate.
"""
from pathlib import Path
import hashlib
import json
import math
import re

base = Path(__file__).resolve().parents[2]
source = base / "numerics/16_VCD_GT_CM_EXTENDED_SOURCE_CERTIFICATE_20261118.json"
source_data = json.loads(source.read_text())
source_rows = source_data["canonical"]["inherited_endpoint_rows_with_new_geometry"]


def midpoint(s):
    return float(re.fullmatch(r"\[([^\s]+) \+/- ([^\]]+)\]", s).group(1))


rows = []
for label, t in [("time_zero", 0.0), ("positive_anchor", 0.1)]:
    v = source_rows[label]
    d_value = (midpoint(v["D_lower"]) + midpoint(v["D_upper"])) / 2
    m_value = midpoint(v["M"])
    center = 14010.1 + midpoint(v["center_offset"])
    density = math.log(center / (4 * math.pi)) / (4 * math.pi) + t / (16 * center)
    scale = 1 / density
    gap = 2 * math.sqrt(d_value)
    rows.append({
        "source_row": "canonical/inherited_endpoint_rows_with_new_geometry/" + label,
        "physical_time": t,
        "source_values": {k: v[k] for k in ["center_offset", "D_lower", "D_upper", "M"]},
        "approximate": {
            "center": center, "D": d_value, "M": m_value,
            "reference_spacing": scale, "gap": gap,
            "gap_over_reference_spacing": gap / scale,
            "reference_spacing_squared_times_M": scale * scale * m_value,
            "Dprime_from_pair_law": 2 - 4 * d_value * m_value,
        },
    })

record = {
    "date_local": "2026-11-19", "timezone": "America/New_York",
    "prepared_for": "Edward Baker", "llm_assistance": "OpenAI Codex",
    "actual_recorded_model": None, "actual_recorded_effort": None,
    "status": "rounded illustrative readout of inherited enclosures; not a new certificate",
    "source": str(source.relative_to(base)),
    "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
    "reference_spacing_definition": "1 / [log(center/(4*pi))/(4*pi) + physical_time/(16*center)]",
    "reference_scope": "smooth density scale; no claim that the high-clock localization onset is met here",
    "arithmetic": "Python binary floating point; source bound strings preserved; derived values are not outward enclosures",
    "rows": rows,
}
dest = Path(__file__).with_name("04_HEIGHT_DENSITY_AND_PAIR_READOUT_20261119.json")
dest.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps({"record": str(dest), "rows": [x["approximate"] for x in rows]}, indent=2))
