#!/usr/bin/env python3
"""Independent checks for the Claude cross-family review of the formal replay
records and source passes 4-8 in papers/investigations-2/formal_replay_crosswalk.

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier claude-opus-5-5; the serving
model may differ), Anthropic, Claude Cowork; reasoning effort max.
Internal model checks are not independent mathematical validation.

What this program checks (it never runs Lean, Lake or the comparator):

  1. replay_records: each committed replay record's configuration, challenge
     and solution identities against an openai/math checkout at the pin, its
     written contract against the solution source, its preparation-context
     bindings against the committed lane files, and the completion
     checkpoint's bindings of the three records.
  2. source_contract_record: the 38 files, 43 anchor excerpts, two TeX
     sources and note binding of canonical_energy_crosswalk_20261013.json.
  3. note_hash_tables: the SHA-256 tables in notes 5 and 7.
  4. note_line_ranges: every pinned GitHub line range in notes 5-8 whose
     preceding back-ticked identifier is a declaration name of the checkout
     contains that name.
  5. invocation_chains: for each listed chain, the source text of every
     declaration mentions the next declaration by name. This is textual
     evidence that the later declaration is used in the proof of the earlier
     one; it is not a Lean dependency query.
  6. exponent_algebra: exact rational checks of the substitutions in notes
     2, 5, 6 and 8 and in the earlier Claude review's U3 route.
  7. comparator_semantics (optional): the pinned comparator exports only the
     dependency closure of the nominated targets, compares the statement's
     definitional cone, checks axioms over the theorem's closure and replays
     the export in the kernel; lean4export dumps dependencies recursively.

Standard library only (Python 3.9+, plus the git executable for blob and
commit identities). Output is deterministic: sorted keys, relative paths,
no timestamps.

Usage:
  python3 CHECKS.py --lane LANE --checkout OPENAI_MATH \
      [--comparator COMPARATOR_SRC --lean4export LEAN4EXPORT_SRC] \
      [--output OUT.json]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from fractions import Fraction

PIN = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"
COMPARATOR_PIN = "d03acab154d269c06e60e4de7e4cc85deebff94b"
LEAN4EXPORT_PIN = "076e8e57707e813375e8f9da8bf989799ace9680"
DL = "lean/OAI/NumberTheory/DirichletL/"


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def blob_sha1(data: bytes) -> str:
    return hashlib.sha1(b"blob %d\0" % len(data) + data).hexdigest()


def canonical_sha256(obj) -> str:
    text = json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return sha256(text.encode("utf-8"))


def read(path: str) -> bytes:
    with open(path, "rb") as handle:
        return handle.read()


def git_head(path: str):
    if not os.path.isdir(os.path.join(path, ".git")):
        return None
    out = subprocess.run(["git", "-C", path, "rev-parse", "HEAD"],
                         capture_output=True, text=True)
    return out.stdout.strip() if out.returncode == 0 else None


# ---------------------------------------------------------------- 1 records
def check_replay_records(lane: str, checkout: str) -> dict:
    result = {}
    numerics = os.path.join(lane, "numerics")
    for target in ("zeta", "dirichlet", "hecke"):
        name = f"replay_{target}_001_20261013.json"
        rec = json.loads(read(os.path.join(numerics, name)).decode("utf-8"))
        entry = {}
        cs = rec["configuration_source"]
        data = read(os.path.join(checkout, cs["path"]))
        entry["configuration_identity"] = (
            len(data) == cs["bytes"] and sha256(data) == cs["sha256"]
            and blob_sha1(data) == cs["git_blob_sha1"])
        entry["configuration_equal_to_pinned_json"] = (
            json.loads(data.decode("utf-8")) == rec["configuration"])
        for key in ("challenge_source", "solution_source"):
            ev = rec["source_evidence"][key]
            data = read(os.path.join(checkout, ev["path"]))
            entry[key + "_identity"] = (
                len(data) == ev["bytes"] and sha256(data) == ev["sha256"]
                and blob_sha1(data) == ev["git_blob_sha1"])
        solution = read(os.path.join(checkout, rec["source_evidence"]["solution_source"]["path"])).decode("utf-8")
        entry["written_contract_in_solution"] = rec["written_contract"]["source_contract"] in solution
        context = {}
        for fname, ev in sorted(rec["preserved_preparation_context"].items()):
            path = os.path.join(numerics, fname)
            if not os.path.exists(path):
                context[fname] = "absent_from_lane"
                continue
            data = read(path)
            ok = len(data) == ev["bytes"] and sha256(data) == ev["stored_sha256"]
            if "canonical_sha256" in ev:
                ok = ok and canonical_sha256(json.loads(data.decode("utf-8"))) == ev["canonical_sha256"]
            context[fname] = ok
        entry["preparation_context_bindings"] = context
        entry["status"] = rec["status"]
        entry["kernel_result"] = rec["kernel_result"]
        entry["actual_axioms_recorded"] = rec["actual_axioms"]
        entry["elapsed_seconds"] = rec["elapsed_seconds"]
        entry["compiled_OAI_modules"] = rec["execution"]["compiled_OAI_modules"]
        result[target] = entry
    completion = json.loads(read(os.path.join(numerics, "replay_queue_completion_20261013.json")).decode("utf-8"))
    bound = {}
    for t in completion["targets"]:
        data = read(os.path.join(lane, t["relative_record_path"]))
        bound[t["target"]] = (
            len(data) == t["bytes"] and sha256(data) == t["stored_sha256"]
            and canonical_sha256(json.loads(data.decode("utf-8"))) == t["canonical_sha256"])
    result["completion_checkpoint_bindings"] = bound
    wall = completion["queue"]["total_replay_wall_seconds_including_baseline_resets"]
    result["completion_total_wall_seconds"] = wall
    result["completion_total_wall_hms"] = "%d:%02d:%02d" % (int(wall) // 3600, int(wall) % 3600 // 60, int(wall) % 60)
    return result


# ------------------------------------------------------- 2 source contracts
def check_source_contract_record(lane: str, checkout: str) -> dict:
    rec = json.loads(read(os.path.join(lane, "numerics", "canonical_energy_crosswalk_20261013.json")).decode("utf-8"))
    files_ok = anchors_ok = anchors = 0
    failures = []
    for c in rec["lean_source_contracts"]:
        data = read(os.path.join(checkout, c["path"]))
        if len(data) == c["bytes"] and sha256(data) == c["sha256"] and blob_sha1(data) == c["git_blob_sha1"]:
            files_ok += 1
        else:
            failures.append(c["path"])
        lines = data.decode("utf-8").split("\n")
        for a in c["anchors"]:
            anchors += 1
            seg = "\n".join(lines[a["line_start"] - 1:a["line_end"]])
            if sha256(seg.encode("utf-8")) == a["excerpt_sha256"] or sha256((seg + "\n").encode("utf-8")) == a["excerpt_sha256"]:
                anchors_ok += 1
            else:
                failures.append("%s#L%d-L%d" % (c["path"], a["line_start"], a["line_end"]))
    papers_ok = all(
        sha256(read(os.path.join(checkout, p["path"]))) == p["sha256"]
        and len(read(os.path.join(checkout, p["path"]))) == p["bytes"]
        for p in rec["paper_sources"])
    note = read(os.path.join(lane, rec["note"]["relative_path"]))
    return {
        "files": len(rec["lean_source_contracts"]), "files_matching": files_ok,
        "anchors": anchors, "anchors_matching": anchors_ok,
        "paper_sources_matching": papers_ok,
        "note_binding_matches_committed_note": sha256(note) == rec["note"]["sha256"] and len(note) == rec["note"]["bytes"],
        "failures": failures,
    }


# ------------------------------------------------------ 3 note hash tables
def check_note_hash_tables(lane: str, checkout: str) -> dict:
    out = {}
    for note in ("5_SMOOTH_WEIGHT_UNIFORMITY_SOURCE_PASS_20261013.md",
                 "7_FIXED_CHARACTER_ROW_DICTIONARY_SOURCE_PASS_20261013.md"):
        text = read(os.path.join(lane, "notes", note)).decode("utf-8")
        rows = re.findall(r"\|\s*`([^`]+\.lean)`\s*\|\s*`([0-9a-f]{64})`\s*\|", text)
        good = sum(sha256(read(os.path.join(checkout, DL, p))) == h for p, h in rows)
        out[note] = {"rows": len(rows), "matching": good}
    return out


# ------------------------------------------------------ 4 note line ranges
DECL_RE = re.compile(r"^(?:@\[[^\]]*\]\s*)*(?:(?:private|protected|noncomputable|nonrec|partial|unsafe)\s+)*"
                     r"(?:theorem|lemma|def|abbrev|instance|structure|class|inductive|opaque)\s+([^\s:({\[]+)")


def declaration_names(checkout: str) -> set:
    names = set()
    root = os.path.join(checkout, DL)
    for dirpath, _dirs, files in os.walk(root):
        for f in files:
            if f.endswith(".lean"):
                for line in read(os.path.join(dirpath, f)).decode("utf-8").split("\n"):
                    m = DECL_RE.match(line)
                    if m:
                        names.add(m.group(1).split(".")[-1])
    return names


def check_note_line_ranges(lane: str, checkout: str, names: set) -> dict:
    link_re = re.compile(r"\]\((https://github\.com/openai/math/blob/" + PIN + r"/([^)#]+)#L(\d+)(?:-L(\d+))?)\)")
    tick_re = re.compile(r"`([^`]+)`")
    out = {}
    for note in ("5_SMOOTH_WEIGHT_UNIFORMITY_SOURCE_PASS_20261013.md",
                 "6_UNIT_ROW_AMPLIFICATION_SOURCE_PASS_20261013.md",
                 "7_FIXED_CHARACTER_ROW_DICTIONARY_SOURCE_PASS_20261013.md",
                 "8_CANONICAL_ENERGY_CROSSWALK_20261013.md"):
        checked = 0
        misses = []
        for line in read(os.path.join(lane, "notes", note)).decode("utf-8").split("\n"):
            for m in link_re.finditer(line):
                path, a = m.group(2), int(m.group(3))
                b = int(m.group(4) or a)
                if not path.endswith(".lean"):
                    continue
                ticks = [t for t in tick_re.findall(line[:m.start()])
                         if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_.'!?]*", t)]
                if not ticks:
                    continue
                name = ticks[-1].split(".")[-1]
                if name not in names:
                    continue
                lines = read(os.path.join(checkout, path)).decode("utf-8").split("\n")
                checked += 1
                seg = "\n".join(lines[a - 1:b])
                if not re.search(r"(?<![A-Za-z0-9_])" + re.escape(name) + r"(?![A-Za-z0-9_'])", seg):
                    misses.append("%s -> %s#L%d-L%d" % (ticks[-1], path, a, b))
        out[note] = {"declaration_links_checked": checked, "misses": misses}
    return out


# ------------------------------------------------------ 5 invocation chains
# Each link (caller, callee): (relative file under DL, declared name as written).
D = {
    "hecke_target": ("Hecke/Nonvanishing.lean", "LFunction_ne_zero_of_seven_eighths_lt_re"),
    "certified_bands": ("Hecke/ConditionalNonvanishing.lean", "LFunction_ne_zero_of_certified_bands"),
    "detector_certified_bands": ("Detector/FinalAssemblyUnconditional.lean", "detector_certified_bands"),
    "chosen_moments_of_certified": ("Detector/FinalAssemblyCertifiedBands.lean", "chosen_moments_of_certified"),
    "fine_moments_of_certified": ("Detector/FinalAssemblyCertifiedBands.lean", "fine_moments_of_certified"),
    "source_moments": ("Detector/FinalAssemblyCertifiedBands.lean", "source_moments"),
    "source_batch_inverse_fields": ("Detector/DetectorInverseFields.lean", "source_batch_inverse_fields"),
    "source_batch_inverse_raw": ("Detector/DetectorInverseRawField.lean", "source_batch_inverse_raw"),
    "fixed_raw_profiles": ("Detector/DetectorInverseRawField.lean", "fixed_raw_profiles"),
    "raw_reference_moment": ("Dictionary/InverseRawReference.lean", "raw_reference_moment"),
    "raw_pair_height_uniform": ("Dictionary/InverseRawUniform.lean", "raw_pair_height_uniform"),
    "raw_pair_uniform": ("Dictionary/InverseRawUniform.lean", "raw_pair_uniform"),
    "raw_family_uniform": ("Dictionary/InverseRawUniform.lean", "raw_family_uniform"),
    "rawMoment_reference": ("Dictionary/InverseRawEnergy.lean", "rawMoment_reference"),
    "chosen_input_of_fine": ("Detector/FinalAssemblyChosenData.lean", "chosen_input_of_fine"),
    "source_count_parameters": ("Detector/FinalAssemblyData.lean", "source_count_parameters"),
    "exists_count_parameters": ("Detector/FinalAssemblyCountParameters.lean", "exists_count_parameters"),
    "balanced_adaptive_count_from_raw_moments": ("PrimeRows/NonfloorCount.lean", "balanced_adaptive_count_from_raw_moments"),
    "fixed_amplitude_count_from_raw_moments": ("Hecke/DetectorFixedAmplitudeCount.lean", "fixed_amplitude_count_from_raw_moments"),
    "count_from_raw_moments": ("Hecke/DetectorCountFromMoments.lean", "count_from_raw_moments"),
    "no_slot_inverse_count": ("Hecke/DetectorNoSlotInverseCount.lean", "no_slot_inverse_count"),
    "no_slot_rowwise_endpoint": ("Hecke/InverseAmplificationRowwise.lean", "no_slot_rowwise_endpoint"),
    "no_slot_endpoint": ("Hecke/InverseAmplificationEndpoint.lean", "no_slot_endpoint"),
    "eventually_fixed_ray_amplification": ("Hecke/InverseAmplificationPrimePool.lean", "eventually_fixed_ray_amplification"),
    "averaged_energy": ("Hecke/InverseAmplificationAggregate.lean", "averaged_energy"),
    "scaleEnergy": ("Hecke/InverseAmplificationRaw.lean", "RawMoment.scaleEnergy"),
    "raw_reference_large": ("Dictionary/InverseRawReference.lean", "raw_reference_large"),
    "raw_input_bound": ("Dictionary/InverseRawInputBound.lean", "raw_input_bound"),
    "original_input_bound": ("Inversion/InitialTotalEnergy.lean", "original_input_bound"),
    "finite_physical_bound": ("Inversion/InitialFiniteEnergy.lean", "finite_physical_bound"),
    "retained_sum_bound": ("Inversion/InitialRetainedSum.lean", "retained_sum_bound"),
    "retained_window_bound": ("Inversion/InitialRetainedWindow.lean", "retained_window_bound"),
    "retained_physical_bound": ("Inversion/InitialRetainedPhysical.lean", "retained_physical_bound"),
    "canonical_marked_energy_exists": ("Descent/CanonicalRankExistence.lean", "canonical_marked_energy_exists"),
    "actual_physical_reference_bound": ("Inversion/InitialEnergyCallerReference.lean", "actual_physical_reference_bound"),
    "initial_raw_uniform": ("Inversion/InitialEnergyCallerUniform.lean", "initial_raw_uniform"),
    "canonical_clipped_uniform": ("Descent/ClippedUniform.lean", "canonical_clipped_uniform"),
    "canonical_clipped_energy": ("Descent/ClippedEnergy.lean", "canonical_clipped_energy"),
    "rawMoment_of_large_rows_ge_one": ("Dictionary/InverseRawCompact.lean", "rawMoment_of_large_rows_ge_one"),
    "reference_energy_linear": ("Dictionary/InverseRawCompact.lean", "reference_energy_linear"),
    "inverse_reference_bound": ("Dictionary/InverseRawCompact.lean", "inverse_reference_bound"),
    "inverse_polynomial_bound": ("Dictionary/InverseRawCompact.lean", "inverse_polynomial_bound"),
    "source_batch_plain_unmarked": ("Detector/DetectorPlainUnmarkedRestrictedField.lean", "source_batch_plain_unmarked"),
    "source_batch_plain_retained": ("Moments/DetectorPlainExceptional.lean", "source_batch_plain_retained"),
    "fiber_plain_energy_eq": ("Moments/DetectorDictionaryFiber.lean", "fiber_plain_energy_eq"),
    "momentData_plain_pair_norm": ("Moments/DetectorDictionaryRows.lean", "momentData_plain_pair_norm"),
    "character_spec": ("Hecke/InverseAmplificationFamily.lean", "RowData.character_spec"),
    "hecke_of_chosen_moments": ("Detector/FinalAssemblyChosenData.lean", "hecke_of_chosen_moments"),
    "hecke_ne_zero_of_common_probe": ("Hecke/CommonProbe.lean", "hecke_ne_zero_of_common_probe"),
    "beta_le_seven_eighths": ("Hecke/CommonProbe.lean", "beta_le_seven_eighths"),
    "nonzero_of_probe_bounds": ("Hecke/SignalIdentity.lean", "nonzero_of_probe_bounds"),
    "LFunction_ne_zero_of_one_lt_re": ("Hecke/Euler.lean", "LFunction_ne_zero_of_one_lt_re"),
    "LFunction_eq_series": ("Hecke/Euler.lean", "LFunction_eq_series"),
    "LFunction_eq_ideal_tsum": ("Hecke/IdealBridge.lean", "LFunction_eq_ideal_tsum"),
    "continuedLattice_eq_six_ideal_tsum": ("Hecke/IdealBridge.lean", "continuedLattice_eq_six_ideal_tsum"),
    "exists_primitive_zero_near_beta": ("Hecke/PrimitiveSupremum.lean", "exists_primitive_zero_near_beta"),
    "beta_eq_primitive_supremum": ("Hecke/PrimitiveSupremum.lean", "beta_eq_primitive_supremum"),
    "exists_primitive_zero": ("Hecke/FiniteDeletion.lean", "exists_primitive_zero"),
    "exists_primitive_character": ("Hecke/IdealOperations.lean", "exists_primitive_character"),
    "zeta_target": ("Nonvanishing.lean", "riemannZeta_ne_zero_of_seven_eighths_lt_re"),
    "zeta_nonzero": ("Detector/FinalAssemblyUnconditional.lean", "zeta_nonzero"),
    "zeta_of_certified": ("Detector/FinalAssemblyCertifiedBands.lean", "zeta_of_certified"),
    "zeta_of_chosen_moments": ("Detector/FinalAssemblyChosenData.lean", "zeta_of_chosen_moments"),
    "zeta_of_common_probe": ("Hecke/CommonProbe.lean", "zeta_of_common_probe"),
    "zeta_seven_eighths_of_hecke": ("Hecke/Dirichlet.lean", "zeta_seven_eighths_of_hecke"),
    "dirichlet_seven_eighths_of_hecke": ("Hecke/Dirichlet.lean", "dirichlet_seven_eighths_of_hecke"),
    "LFunction_eq_dirichlet_product": ("Hecke/Dirichlet.lean", "LFunction_eq_dirichlet_product"),
    "LFunction_differentiableAt": ("Hecke/IdealBridge.lean", "LFunction_differentiableAt"),
    "dirichlet_target": ("Nonvanishing.lean", "LFunction_ne_zero_of_seven_eighths_lt_re"),
    "dirichlet_nonzero": ("Detector/FinalAssemblyUnconditional.lean", "dirichlet_nonzero"),
    "dirichlet_of_certified": ("Detector/FinalAssemblyCertifiedBands.lean", "dirichlet_of_certified"),
    "dirichlet_of_chosen_moments": ("Detector/FinalAssemblyChosenData.lean", "dirichlet_of_chosen_moments"),
    "dirichlet_of_common_probe": ("Hecke/CommonProbe.lean", "dirichlet_of_common_probe"),
}

CHAINS = {
    "A_hecke_to_raw_reference_moment": ["hecke_target", "certified_bands", "chosen_moments_of_certified",
                                        "fine_moments_of_certified", "source_moments", "source_batch_inverse_fields",
                                        "source_batch_inverse_raw", "fixed_raw_profiles", "raw_reference_moment"],
    "A0_hecke_target_uses_detector_certified_bands": ["hecke_target", "detector_certified_bands"],
    "B_to_rawMoment_reference": ["fixed_raw_profiles", "raw_pair_height_uniform", "raw_pair_uniform",
                                 "raw_family_uniform", "rawMoment_reference"],
    "C_to_fixed_ray_amplification": ["chosen_moments_of_certified", "chosen_input_of_fine", "source_count_parameters",
                                     "exists_count_parameters", "balanced_adaptive_count_from_raw_moments",
                                     "fixed_amplitude_count_from_raw_moments", "count_from_raw_moments",
                                     "no_slot_inverse_count", "no_slot_rowwise_endpoint", "no_slot_endpoint",
                                     "eventually_fixed_ray_amplification", "averaged_energy"],
    "C1_no_slot_endpoint_uses_scaleEnergy": ["no_slot_endpoint", "scaleEnergy"],
    "D_to_canonical_marked_energy_exists": ["raw_reference_moment", "raw_reference_large", "raw_input_bound",
                                            "original_input_bound", "finite_physical_bound", "retained_sum_bound",
                                            "retained_window_bound", "retained_physical_bound",
                                            "canonical_marked_energy_exists"],
    "E_to_canonical_clipped_energy": ["retained_physical_bound", "actual_physical_reference_bound",
                                      "initial_raw_uniform", "canonical_clipped_uniform", "canonical_clipped_energy"],
    "F_to_inverse_polynomial_bound": ["raw_reference_moment", "rawMoment_of_large_rows_ge_one",
                                      "reference_energy_linear", "inverse_reference_bound", "inverse_polynomial_bound"],
    "G_to_RowData_character_spec": ["source_moments", "source_batch_plain_unmarked", "source_batch_plain_retained",
                                    "fiber_plain_energy_eq", "momentData_plain_pair_norm", "character_spec"],
    "H_hecke_series_identity": ["certified_bands", "hecke_of_chosen_moments", "hecke_ne_zero_of_common_probe",
                                "beta_le_seven_eighths", "nonzero_of_probe_bounds", "LFunction_ne_zero_of_one_lt_re",
                                "LFunction_eq_series", "LFunction_eq_ideal_tsum", "continuedLattice_eq_six_ideal_tsum"],
    "I_hecke_primitive_reduction": ["beta_le_seven_eighths", "exists_primitive_zero_near_beta",
                                    "beta_eq_primitive_supremum", "exists_primitive_zero", "exists_primitive_character"],
    "J_zeta_to_base_change": ["zeta_target", "zeta_nonzero", "zeta_of_certified", "zeta_of_chosen_moments",
                              "zeta_of_common_probe", "zeta_seven_eighths_of_hecke",
                              "dirichlet_seven_eighths_of_hecke", "LFunction_eq_dirichlet_product"],
    "J1_zeta_shares_hecke_core": ["zeta_of_certified", "chosen_moments_of_certified"],
    "J2_base_change_uses_analyticity": ["LFunction_eq_dirichlet_product", "LFunction_differentiableAt"],
    "K_dirichlet_to_base_change": ["dirichlet_target", "dirichlet_nonzero", "dirichlet_of_certified",
                                   "dirichlet_of_chosen_moments", "dirichlet_of_common_probe",
                                   "dirichlet_seven_eighths_of_hecke", "LFunction_eq_dirichlet_product"],
    "K1_dirichlet_shares_hecke_core": ["dirichlet_of_certified", "chosen_moments_of_certified"],
}

TOP_RE = re.compile(r"^(?:@\[|(?:private|protected|noncomputable|nonrec|partial|unsafe)\s|theorem\s|lemma\s|def\s|abbrev\s|"
                    r"instance\s|structure\s|class\s|inductive\s|opaque\s|end\b|namespace\s|section\b|open\s|variable\s|"
                    r"include\s|omit\s|/-|--)")


def declaration_text(checkout: str, rel: str, name: str) -> str:
    lines = read(os.path.join(checkout, DL, rel)).decode("utf-8").split("\n")
    start = None
    for i, line in enumerate(lines):
        m = DECL_RE.match(line)
        if m and m.group(1) == name:
            start = i
            break
    if start is None:
        raise SystemExit("declaration %s not found in %s" % (name, rel))
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j] and not lines[j][0].isspace() and TOP_RE.match(lines[j]):
            end = j
            break
    return "\n".join(lines[start:end])


def check_invocation_chains(checkout: str) -> dict:
    out = {}
    for chain, keys in sorted(CHAINS.items()):
        links = []
        for a, b in zip(keys, keys[1:]):
            text = declaration_text(checkout, *D[a])
            body = text.split("\n", 1)[1] if "\n" in text else text
            short = D[b][1].split(".")[-1]
            hits = len(re.findall(r"(?<![A-Za-z0-9_])" + re.escape(short) + r"(?![A-Za-z0-9_'])", body))
            links.append({"caller": D[a][1], "callee": D[b][1], "mentions": hits})
        out[chain] = {"links": links, "all_links_mentioned": all(l["mentions"] > 0 for l in links)}
    return out


# ------------------------------------------------------- 6 exponent algebra
def check_exponent_algebra() -> dict:
    grid = [Fraction(n, d) for n in (1, 2, 3, 5, 7) for d in (3, 7, 10, 40)]
    ok = {"T1_raw_to_O5": True, "note5_capacity": True, "note6_exponents": True,
          "note6_budget": True, "claude_U3_route": True, "note8_margins": True,
          "note8_restoration_normalizer": True}
    for theta in grid:  # the identities hold for every theta > 0, including 0 < theta <= 1/10
        for eps in grid:
            # T1: D * H (H D)^eps' with H = D^(1+theta), eps' = eps/(2+theta)
            ok["T1_raw_to_O5"] &= 1 + (1 + theta) + (eps / (2 + theta)) * (2 + theta) == 2 + theta + eps
            # note 6: q=(1+c)/6, |P|^2 exponent and amplitude exponent
            c, kappa, eta = theta, eps / 7, eps / 5
            q = (1 + c) / 6
            p2 = 1 + c + kappa * (2 + c) - q
            ok["note6_exponents"] &= p2 == Fraction(5, 6) * (1 + c) + kappa * (2 + c)
            amp = Fraction(1, 2) + (p2 + eta) / 2
            ok["note6_exponents"] &= amp == Fraction(11, 12) + Fraction(5, 12) * c + kappa * (2 + c) / 2 + eta / 2
            # note 6 budget c=min(1,4eps/5), kappa=2eps/(3(2+c)), eta=2eps/3
            cb = min(Fraction(1), 4 * eps / 5)
            kb = 2 * eps / (3 * (2 + cb))
            eb = 2 * eps / 3
            excess = Fraction(5, 12) * cb + kb * (2 + cb) / 2 + eb / 2
            ok["note6_budget"] &= excess <= eps
            # earlier Claude route: U = D^(1/R), exponent (1+5R)/6 + eps in U
            for R in (Fraction(1), Fraction(2), Fraction(7, 2), Fraction(10)):
                lhs = ((1 + 5 * R) / 6 + eps) / R
                ok["claude_U3_route"] &= lhs == Fraction(5, 6) + (1 + 6 * eps) / (6 * R)
                ok["claude_U3_route"] &= Fraction(1, 2) + lhs / 2 == Fraction(11, 12) + (1 + 6 * eps) / (12 * R)
    # note 5: (lambda D)^(1+c0) <= D^(1+c) once D >= L^((1+c0)/(c-c0)), c0=c/2 (log form)
    for c in grid:
        c0 = c / 2
        for logL in (Fraction(0), Fraction(1), Fraction(5, 2)):
            logD = max(Fraction(1), logL * (1 + c0) / (c - c0))
            ok["note5_capacity"] &= (1 + c0) * (logL + logD) <= (1 + c) * logD
    # note 8: margins after dilation; restoration keeps X'F' = XF
    for kappa in grid:
        for logZ2a in (Fraction(-1, 3) * kappa, Fraction(0), Fraction(1, 2)):
            if logZ2a < -kappa / 2:
                continue
            for M in (Fraction(0), Fraction(1), Fraction(3)):
                F0 = M + kappa + logZ2a  # worst case H = Sigma Z^-kappa
                ok["note8_margins"] &= F0 - M >= kappa / 2 and 4 * F0 - 3 * M >= kappa / 2
        for X, F, Nd in ((Fraction(9), Fraction(4), Fraction(7)), (Fraction(5, 3), Fraction(13), Fraction(13))):
            ok["note8_restoration_normalizer"] &= (X / Nd) * (F * Nd) == X * F
    # note 8 dyadic factor: with V+ = log_Z(2F) the Lean normalizer is 1/(2XF), so
    # E_S = 2 E_Lean, and E_Lean <= C Z^(F0+eps) = C (2XF) Z^eps gives E_S <= 4 C XF Z^eps.
    factor = True
    for X, F in ((Fraction(3), Fraction(5)), (Fraction(7, 2), Fraction(11))):
        ratio = (1 / (X * F)) / (1 / (2 * X * F))
        factor &= ratio == 2 and ratio * (2 * X * F) / (X * F) == 4
    ok["note8_dyadic_factor_four"] = factor
    return ok


# ---------------------------------------------- 7 comparator export semantics
def check_comparator_semantics(comparator: str, lean4export: str) -> dict:
    main = read(os.path.join(comparator, "Main.lean")).decode("utf-8")
    compare = read(os.path.join(comparator, "Comparator", "Compare.lean")).decode("utf-8")
    axioms = read(os.path.join(comparator, "Comparator", "Axioms.lean")).decode("utf-8")
    export_main = read(os.path.join(lean4export, "Main.lean")).decode("utf-8")
    export_lib = read(os.path.join(lean4export, "Export.lean")).decode("utf-8")
    dump = export_lib[export_lib.index("partial def dumpConstant"):]
    dump = dump[:dump.index("\n\n")] if "\n\n" in dump else dump
    return {
        "comparator_head": git_head(comparator) == COMPARATOR_PIN,
        "lean4export_head": git_head(lean4export) == LEAN4EXPORT_PIN,
        "export_called_with_named_targets": 'let baseArgs := #[module.toString, "--"]' in main
                                            and "let exportTargets := (← builtinTargets) ++ (← getTheoremNames)" in main,
        "lean4export_dumps_named_constants_only_when_given": "let constants := match constants.tail? with" in export_main,
        "lean4export_dumps_dependencies_recursively": "dumpDeps val.type" in dump and "dumpDeps val.value" in dump,
        "statement_cone_compared_by_full_constant_equality": "if challengeConst != solutionConst then" in compare
                                                             and "addRelevantConsts solutionConst" in compare,
        "axioms_checked_over_theorem_closure": "Illegal axiom detected" in axioms and "runForUsedConsts info validateConst" in axioms,
        "kernel_replays_solution_export": "kernelEnv ← kernelEnv.replay kernelConstMap" in main,
        "acceptance_line_printed_after_all_checks": main.index("verifyMatch challengeExport solutionExport")
                                                    < main.index('IO.println "Your solution is okay!"'),
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--lane", required=True, help="papers/investigations-2/formal_replay_crosswalk")
    ap.add_argument("--checkout", required=True, help="openai/math checkout at the pin (lean/ and preprints/)")
    ap.add_argument("--comparator", help="leanprover/comparator source at the pin (optional)")
    ap.add_argument("--lean4export", help="leanprover/lean4export source at the pin (optional)")
    ap.add_argument("--output", help="write the JSON record here")
    args = ap.parse_args()
    head = git_head(args.checkout)
    if head is not None and head != PIN:
        print("checkout is at %s, not %s" % (head, PIN), file=sys.stderr)
        return 2
    names = declaration_names(args.checkout)
    record = {
        "schema": "claude-cross-family-replay-and-source-pass-checks-v1",
        "record_date": "2026-10-13",
        "model": "Claude Opus 5.5 (configured identifier claude-opus-5-5; serving model may differ), reasoning effort max",
        "prepared_for": "Edward Baker",
        "llm_acknowledgement": "Prepared with LLM assistance; identity and textual checks, not mathematical validation or a Lean query.",
        "upstream_commit": PIN,
        "checkout_head_verified": head == PIN,
        "replay_records": check_replay_records(args.lane, args.checkout),
        "source_contract_record": check_source_contract_record(args.lane, args.checkout),
        "note_hash_tables": check_note_hash_tables(args.lane, args.checkout),
        "note_line_ranges": check_note_line_ranges(args.lane, args.checkout, names),
        "invocation_chains": check_invocation_chains(args.checkout),
        "exponent_algebra": check_exponent_algebra(),
    }
    if args.comparator and args.lean4export:
        record["comparator_semantics"] = check_comparator_semantics(args.comparator, args.lean4export)
    else:
        record["comparator_semantics"] = "not_run"

    def all_true(obj) -> bool:
        if isinstance(obj, bool):
            return obj
        if isinstance(obj, dict):
            return all(all_true(v) for k, v in obj.items()
                       if k not in ("actual_axioms_recorded", "status", "kernel_result", "elapsed_seconds",
                                    "compiled_OAI_modules", "completion_total_wall_seconds",
                                    "completion_total_wall_hms", "mentions", "caller", "callee"))
        if isinstance(obj, list):
            return all(all_true(v) for v in obj)
        return True

    scr = record["source_contract_record"]
    passed = (all_true({k: v for k, v in record.items() if k not in ("comparator_semantics",)})
              and scr["files_matching"] == scr["files"] and scr["anchors_matching"] == scr["anchors"]
              and not scr["failures"]
              and all(v["rows"] == v["matching"] for v in record["note_hash_tables"].values())
              and all(not v["misses"] for v in record["note_line_ranges"].values()))
    if isinstance(record["comparator_semantics"], dict):
        passed = passed and all(record["comparator_semantics"].values())
    record["all_checks_passed"] = passed
    text = json.dumps(record, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text)
    print(text, end="")
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
