#!/usr/bin/env python3
"""Exact bookkeeping for OG Note10, not a replay of the OC windings.

2026-11-10. Prepared for Edward Baker with OpenAI Codex LLM assistance.
Actual backend/effort unavailable. Uses only the Python standard library.
Prints the small record to stdout; redirect to the named record to save.
"""

from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import re


ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "result-summaries/README.md").is_file())
BASE = ROOT / ("papers/investigations-5/08_theta_observables_newman_dynamics/"
               "03_operator_imaginary_time_evolution")
OG = BASE / "01_green_potential_resolvent"
OC = BASE / "02_localized_zero_correlations"
OA = BASE / "03_collision_constraints"


def identity(path):
    raw = path.read_bytes()
    return {"path": str(path.relative_to(ROOT)), "bytes": len(raw),
            "sha256": hashlib.sha256(raw).hexdigest()}


def main():
    geometry_path = OC / "numerics/19_TND_OC_B10_R3_EXACT_GEOMETRY_20261109.json"
    note_path = OC / "notes/22_TND_OC_B10_R3_CELL_RANGES_AND_GAUSSIAN_WIDTH_20261109.md"
    geometry = json.loads(geometry_path.read_text())
    note_text = note_path.read_text()
    assert geometry["geometry"]["labels"] == 388
    assert geometry["geometry"]["occupied_cells"] == 388
    assert "Every imaginary interval is \\([-3/32768,3/131072]\\)" in note_text
    assert "(988,2012)" in note_text
    assert geometry["trace_check"]["status"] == (
        "passed_structure_only_inherits_E13_outward_windings")

    labels, y_upper = geometry["geometry"]["labels"], F(3, 131072)
    core = labels * y_upper / 2
    tail = F(1, 2**157)
    geometric_sum = (1 + F(4, 5)) / (1 - F(4, 5))**3
    checks = {
        "kernel_constant": F(10, 21) < F(1, 2),
        "core_exact": core == F(291, 65536),
        "distance_both_sides": 1500 - 988 == 2012 - 1500 == 512,
        "shell_base": 1503 + 512 == 2015 < 2**11,
        "geometric_sum_at_four_fifths": geometric_sum == 225 < 2**8,
        "tail_exponent": 5 + 22 - 192 + 8 == -157,
        "final_strict_threshold": core + tail < F(1, 200),
        "consumer_lower_comparison": F(1, 200) < F(1, 16),
    }
    assert all(checks.values()), checks

    manuscript_sources = []
    manuscript_sections = {}
    for branch in (OG, OC, OA):
        main_path = branch / "manuscript/main.tex"
        includes = re.findall(r"\\input\{(sections/[^}]+)\}", main_path.read_text())
        section_paths = [
            main_path.parent / (name if name.endswith(".tex") else name + ".tex")
            for name in includes
        ]
        manuscript_sections[branch.name] = len(section_paths)
        manuscript_sources.extend([main_path, *section_paths])
    assert list(manuscript_sections.values()) == [9, 18, 7]

    additional = [
        geometry_path, note_path,
        OC / "notes/25_TND_OC_E13_R2_CERTIFIED_GAUSSIAN_PROJECTION_20261109.md",
        OC / "reviews/17_TND_OC_E13_R1_PROOF_AND_IMPLEMENTATION_CHECK_20261109.md",
        OC / "reviews/20_TND_OC_E15_R1_MANUSCRIPT_CLAIM_ASSESSMENT_20261109.md",
        OC / "reviews/21_TND_OC_E13_R2_CELL_RANGE_EXECUTION_ASSESSMENT_20261109.md",
        OC / "numerics/23_TND_OC_E13_R2_EXECUTION_20261109.json",
        OC / "research-progress/02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PROGRESS_20261108.md",
        OA / "research-progress/01_TND_OA_COLLISION_CONSTRAINTS_PROGRESS_20261108.md",
        OA / "reviews/03_TND_OA_E01_R1_REGULAR_DEFLATION_ASSESSMENT_20261109.md",
        OA / "reviews/06_TND_OA_E02_R1_LEHMER_SCREEN_ASSESSMENT_20261109.md",
        OA / "notes/11_TND_OA_AFTER_E02_CONTINUATION_AND_MODEL_CHANGE_20261109.md",
        OG / "notes/05_TND_OG_B03_HDA_HIERARCHY_LOG_TRANSFER_20261108.md",
        OG / "notes/06_TND_OG_E03_COMPLETE_SIGNED_LOG_ACQUISITION_20261108.md",
        OG / "notes/07_TND_OG_E05_ASSESSMENT_CALCULATIONS_20261108.md",
        OG / "notes/09_TND_OG_B04_GREEN_MASS_RESOLUTION_AND_VALUE_DECISION_20261108.md",
        OG / "reviews/06_TND_OG_E05_CLAIM_LEVEL_ASSESSMENT_20261108.md",
        OG / "research-progress/handoffs/18_TND_OG_E06_SINGLE_TUPLE_FEASIBILITY_REQUEST_20261108.md",
        OG / "research-progress/handoffs/18_TND_OG_E06_INPUTS_20261108.json",
        ROOT / "result-summaries/README.md",
        ROOT / "result-summaries/11_newman_heat_flow_reductions_and_certificates.md",
        ROOT / "result-summaries/12_collision_controls_and_screening.md",
        ROOT / "result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md",
        ROOT / "avoid/README.md",
        ROOT / "avoid/01_restating_the_target.md",
        ROOT / "avoid/02_shape_only_arguments_and_the_controls.md",
        ROOT / "avoid/07_scoped_exclusions_read_as_universal.md",
    ]
    record = {
        "task": "TND-OG-B06",
        "date_local": "2026-11-10",
        "timezone": "America/New_York",
        "recorded_at_utc": datetime.now(timezone.utc).isoformat(),
        "prepared_for": "Edward Baker",
        "llm_assistance": "OpenAI Codex",
        "actual_model": None,
        "actual_effort": None,
        "configuration_note": "Unavailable in accessible current-chat capture metadata.",
        "status": "exact_rational_bookkeeping_passed_inherited_census_not_recertified",
        "canonical_source_calls": 0,
        "green_kernel_calls": 0,
        "external_trace_read": False,
        "external_trace_identity_as_recorded_by_OC": geometry["trace_check"],
        "inherited_scope": (
            "Uses the complete OC outward-winding census and the common vertical "
            "interval stated in Note22. Hashes identify small source files; they "
            "do not validate the windings or prove the analytical tail."),
        "proof_location": str((OG / "notes/10_TND_OG_B06_SIBLING_RESULTS_AND_GREEN_CENSUS_TRANSFER_20261110.md").relative_to(ROOT)),
        "X": 1500,
        "inherited_count": labels,
        "inherited_y_upper": str(y_upper),
        "core_upper": str(core),
        "strict_tail_upper": "2^-157",
        "strict_total_upper": str(core + tail),
        "comparison_threshold": "1/200",
        "comparison_slack": str(F(1, 200) - core - tail),
        "consumer_lower_bound": "1/16",
        "checks": checks,
        "manuscript_section_counts": manuscript_sections,
        "source_files": [identity(p) for p in manuscript_sources + additional],
        "script": identity(Path(__file__).resolve()),
    }
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
