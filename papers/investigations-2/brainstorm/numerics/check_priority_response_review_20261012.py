#!/usr/bin/env python3
"""Checks behind the 12 October 2026 Claude review of the Codex priority response.

Prepared for Edward Baker. Model: Claude Opus 5.5 (configured identifier
claude-opus-5-5; the serving model may differ), Claude Cowork.

Standard library only, deterministic, JSON output. The inputs are pinned
third-party files that stay outside the repository (LARGE_FILES.md). Fetch
them with --fetch, or place them by hand in the layout documented in
README.md, then run with --inputs.

Checks
  A  Gomila barrier transcript: per-prism identity
       min_mesh = spatial + time + eps + margin,
     spatial = 2 Dz / mesh, the adaptive rule time == margin, and the
     smallest factor by which the derivative majorants Dz, Dt (jointly or
     singly) would have to be too small for a prism to fail.
  B  Gomila tail Arb log: D = P + TR + OV + Mmax*AB and the slacks
     1 - D and 1 - (D - OV).
  C  E_max against the certified weakest-row floor of note 3.
  D  Liu's pinned upstream closure (adc7f124): git blob SHA-1 of every
     listed module recomputed from openai/math at fd4aeeb2.
  E  Comparator, scope, toolchain and lake manifest files byte-identical
     at adc7f124 and fd4aeeb2.
  F  (optional, --row-record) tolerance of the weakest finite row: from the
     repository's certified replay record, Q = 1 - g_N - S_N and the
     relative error in the triangle sum S_N that would erase L_N - E_max.
"""
import argparse
import hashlib
import json
import os
import re
import sys
import urllib.request
from fractions import Fraction

GOMILA = ("https://raw.githubusercontent.com/judegomila/"
          "dbn-lambda-01787854-candidate-audit/"
          "a74738deb6d5e0f76887cb36901da08b68dca705/")
LIU = ("https://raw.githubusercontent.com/liubaiying101/"
       "Slightly-improved-zero-free-half-planes-for-the-quasi-Riemann-hypothesis/"
       "7d10420de90efa2f082a06a342fc7accbd57ab37/")
OAI = "https://raw.githubusercontent.com/openai/math/{rev}/"
FD4 = "fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb"
ADC = "adc7f1241b42e322a6451854ab7e4b4c146bf78a"

PINNED = {
    "gomila/barrier/certificates/barrier_target_closed.log":
        "2d010f70902dca1627f40ddcd68f3954b37fd9596f7840787415eeafb20805f4",
    "gomila/logs/tail_arb_256.log":
        "bd189e5095d1e62f061f9606e7547793e5cee2f086d41be6e03c53f7744a7a66",
    "gomila/logs/prop410_arb_256.log":
        "995651e49112928472d6511a191d727783b0abdf77c20f2f6c32ec814986b244",
    "liu/upstream/closure_manifest.json":
        "b34b902e4d8141ac6bee3a10761439246bc7262ffb342aa83f79e02f295f043f",
}
SAME_FILES = [
    "lean/docs/003.md",
    "lean/ComparatorChallenges/QuasiRiemannHypothesis.lean",
    "lean/ComparatorChallenges/QuasiRiemannHypothesis.json",
    "lean/ComparatorChallenges/DirichletSevenEighths.lean",
    "lean/ComparatorChallenges/DirichletSevenEighths.json",
    "lean/ComparatorChallenges/HeckeSevenEighths.lean",
    "lean/ComparatorChallenges/HeckeSevenEighths.json",
    "lean/lean-toolchain",
    "lean/lake-manifest.json",
]
# Certified lower end of L_690988(t0, y0), note 3 section 3.2 and
# CERTIFIED_ROW_REPLAY_RECORD_20261012.json.
L_WEAKEST = Fraction("7.9136674559412e-7")


def sha256(path):
    with open(path, "rb") as handle:
        return hashlib.sha256(handle.read()).hexdigest()


def git_blob(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def fetch(url, dest):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    with urllib.request.urlopen(url, timeout=120) as response:
        data = response.read()
    with open(dest, "wb") as handle:
        handle.write(data)


def fetch_inputs(root):
    for rel in PINNED:
        if rel.startswith("gomila/"):
            fetch(GOMILA + rel[len("gomila/"):], os.path.join(root, rel))
        else:
            fetch(LIU + rel[len("liu/"):], os.path.join(root, rel))
    for rev, tag in ((FD4, "fd4aeeb2"), (ADC, "adc7f124")):
        for rel in SAME_FILES:
            fetch(OAI.format(rev=rev) + rel,
                  os.path.join(root, "openai-math-" + tag, rel))
    manifest = json.load(open(os.path.join(root, "liu/upstream/closure_manifest.json")))
    for record in manifest["modules"].values():
        rel = "lean/" + record["path"][len("vendor/"):]
        fetch(OAI.format(rev=FD4) + rel, os.path.join(root, "openai-math-fd4aeeb2", rel))


def ball_mid(line, key):
    match = re.search(key + r"=\[?\s*([-0-9.e+]+)", line)
    if not match:
        raise ValueError("missing %s in: %s" % (key, line[:80]))
    return Fraction(match.group(1))


def check_barrier(path):
    prisms = []
    for line in open(path, encoding="utf-8"):
        if not line.startswith("Prism("):
            continue
        index = int(re.match(r"Prism\((\d+)\)", line).group(1))
        prisms.append({
            "prism": index,
            "min_mesh": ball_mid(line, "min_mesh"),
            "spatial": ball_mid(line, "spatial"),
            "time": ball_mid(line, "time"),
            "eps": ball_mid(line, "eps"),
            "margin": ball_mid(line, "margin"),
            "Dz": ball_mid(line, "Dz"),
            "mesh": int(re.search(r"mesh=(\d+)", line).group(1)),
            "pass": line.rstrip().endswith("PASS"),
        })
    identity = max(abs(p["min_mesh"] - p["spatial"] - p["time"] - p["eps"] - p["margin"])
                   for p in prisms)
    spatial_rule = max(abs(p["spatial"] - 2 * p["Dz"] / p["mesh"]) for p in prisms)
    adaptive = sum(1 for p in prisms if abs(p["time"] - p["margin"]) < Fraction(1, 10**15))

    def joint(p):
        return (p["min_mesh"] - p["eps"]) / (p["spatial"] + p["time"])

    def dz_only(p):
        return 1 + p["margin"] / p["spatial"]

    def dt_only(p):
        return 1 + p["margin"] / p["time"]

    worst = min(prisms, key=joint)
    worst_dz = min(prisms, key=dz_only)
    worst_dt = min(prisms, key=dt_only)
    worst_margin = min(prisms, key=lambda p: p["margin"])
    p882 = next(p for p in prisms if p["prism"] == 882)
    return {
        "prisms": len(prisms),
        "all_pass": all(p["pass"] for p in prisms),
        "max_abs_identity_residual": float(identity),
        "max_abs_spatial_minus_2Dz_over_mesh": float(spatial_rule),
        "prisms_with_time_equal_margin": adaptive,
        "min_margin": {"prism": worst_margin["prism"], "margin": float(worst_margin["margin"]),
                       "margin_over_eps": float(worst_margin["margin"] / worst_margin["eps"])},
        "min_joint_flip_factor": {"prism": worst["prism"], "factor": float(joint(worst))},
        "min_Dz_only_flip_factor": {"prism": worst_dz["prism"], "factor": float(dz_only(worst_dz))},
        "min_Dt_only_flip_factor": {"prism": worst_dt["prism"], "factor": float(dt_only(worst_dt))},
        "prism_882_margin_after_50pct_increase_of_both_allowances":
            float(p882["margin"] - (p882["spatial"] + p882["time"]) / 2),
    }


def upper_point(text, name):
    match = re.search(name + r" upper point = \[([-0-9.e+]+)", text)
    if not match:
        raise ValueError("missing %s upper point" % name)
    return Fraction(match.group(1))


def check_tail(path):
    text = open(path, encoding="utf-8").read()
    p, tr, ov = upper_point(text, "P"), upper_point(text, "TR"), upper_point(text, "OV")
    mmax, ab, d = upper_point(text, "Mmax"), upper_point(text, "AB"), upper_point(text, "D")
    total = p + tr + ov + mmax * ab
    slack = 1 - d
    return {
        "P": float(p), "TR": float(tr), "OV": float(ov), "Mmax": float(mmax), "AB": float(ab),
        "D_upper": float(d),
        "abs_D_minus_sum_of_parts": float(abs(d - total)),
        "slack_1_minus_D": float(slack),
        "slack_if_OV_is_padding_1_minus_D_plus_OV": float(1 - (d - ov)),
        "relative_tolerance_of_parts": {
            "P": float(slack / p), "TR": float(slack / tr), "Mmax_AB": float(slack / (mmax * ab)),
        },
        "all_checks_pass": "RESULT: ALL ARB TAIL CHECKS PASS" in text,
    }


def check_emax(path):
    text = open(path, encoding="utf-8").read()
    emax = upper_point(text, "Emax")
    return {
        "Emax_upper": float(emax),
        "certified_L_690988_lower": float(L_WEAKEST),
        "Emax_over_L": float(emax / L_WEAKEST),
        "flip_factor_L_over_Emax": float(L_WEAKEST / emax),
    }


def check_closure(root):
    manifest = json.load(open(os.path.join(root, "liu/upstream/closure_manifest.json")))
    same, different, missing = 0, [], []
    for name, record in sorted(manifest["modules"].items()):
        rel = "lean/" + record["path"][len("vendor/"):]
        path = os.path.join(root, "openai-math-fd4aeeb2", rel)
        if not os.path.exists(path):
            missing.append(name)
        elif git_blob(path) == record["git_blob"]:
            same += 1
        else:
            different.append(name)
    return {
        "manifest_upstream_commit": manifest["commit"],
        "modules_listed": len(manifest["modules"]),
        "identical_at_fd4aeeb2": same,
        "different": different,
        "missing": missing,
        "contains_hecke_solution_module":
            "OAI.NumberTheory.DirichletL.Hecke.Nonvanishing" in manifest["modules"],
        "contains_zeta_dirichlet_solution_module":
            "OAI.NumberTheory.DirichletL.Nonvanishing" in manifest["modules"],
    }


def check_weakest_row(path, emax_text_path):
    record = json.load(open(path, encoding="utf-8"))
    row = next(r for r in record["rows"] if r["N"] == 690988)
    g = Fraction(row["g_N"][1])          # upper ends: the conservative direction
    s = Fraction(row["S_N"][1])
    m = Fraction(row["M_N"][1])
    gc = Fraction(row["g_N_C_N_upper"])
    emax = upper_point(open(emax_text_path, encoding="utf-8").read(), "Emax")
    q = 1 - g - s
    room = q - m * (emax + gc)
    return {
        "N": 690988,
        "Q_upper_inputs": float(q),
        "Q_over_S": float(q / s),
        "room_in_S_with_Emax": float(room),
        "relative_room_in_S_with_Emax": float(room / s),
    }


def check_same_files(root):
    result = {}
    for rel in SAME_FILES:
        a = os.path.join(root, "openai-math-fd4aeeb2", rel)
        b = os.path.join(root, "openai-math-adc7f124", rel)
        result[rel] = {"fd4aeeb2": sha256(a), "identical": sha256(a) == sha256(b)}
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", required=True, help="directory holding the pinned inputs")
    parser.add_argument("--fetch", action="store_true", help="download the pinned inputs first")
    parser.add_argument("--output", required=True, help="JSON record to write")
    parser.add_argument("--row-record", help="newman_certificate_audit/numerics/"
                        "CERTIFIED_ROW_REPLAY_RECORD_20261012.json (optional check F)")
    args = parser.parse_args()
    if args.fetch:
        fetch_inputs(args.inputs)
    hashes = {}
    for rel, expected in PINNED.items():
        actual = sha256(os.path.join(args.inputs, rel))
        hashes[rel] = {"sha256": actual, "matches_pin": actual == expected}
        if actual != expected:
            sys.exit("pinned input hash mismatch: " + rel)
    record = {
        "date": "2026-10-12",
        "prepared_for": "Edward Baker",
        "model": "Claude Opus 5.5 (configured identifier claude-opus-5-5; serving model may differ)",
        "scope": "Internal checks for a review of priorities; not independent validation",
        "pins": {
            "gomila": "a74738deb6d5e0f76887cb36901da08b68dca705",
            "liu": "7d10420de90efa2f082a06a342fc7accbd57ab37",
            "openai_math": [FD4, ADC],
        },
        "input_hashes": hashes,
        "A_barrier": check_barrier(os.path.join(
            args.inputs, "gomila/barrier/certificates/barrier_target_closed.log")),
        "B_tail": check_tail(os.path.join(args.inputs, "gomila/logs/tail_arb_256.log")),
        "C_emax": check_emax(os.path.join(args.inputs, "gomila/logs/prop410_arb_256.log")),
        "D_closure": check_closure(args.inputs),
        "E_same_files": check_same_files(args.inputs),
    }
    if args.row_record:
        record["F_weakest_row"] = check_weakest_row(
            args.row_record, os.path.join(args.inputs, "gomila/logs/prop410_arb_256.log"))
        record["F_weakest_row"]["row_record_sha256"] = sha256(args.row_record)
    with open(args.output, "w", encoding="utf-8") as handle:
        json.dump(record, handle, indent=2, sort_keys=True)
        handle.write("\n")
    shown = ("A_barrier", "B_tail", "C_emax", "F_weakest_row")
    print(json.dumps({k: record[k] for k in shown if k in record}, indent=1))
    print("closure:", record["D_closure"]["identical_at_fd4aeeb2"], "/",
          record["D_closure"]["modules_listed"], "identical;",
          "same-file checks:", all(v["identical"] for v in record["E_same_files"].values()))


if __name__ == "__main__":
    main()
