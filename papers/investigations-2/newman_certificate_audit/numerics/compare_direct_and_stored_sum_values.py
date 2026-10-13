#!/usr/bin/env python3
"""Compare two evaluations of the Polymath finite sum f_t at the same barrier
mesh points (corroboration for note 5 of the Newman certificate audit).

Inputs, per prism:
  * a dump of the package's barrier program, instrumented to print, for every
    mesh point of its first prism, the line
        DUMP t re_s im_s re_f im_f rad_re rad_im rad_s_re rad_s_im
    (midpoints and radii of the stored-sum Taylor enclosure of f_t, including
    the 1e-20 serialization and truncation allowances; s = (1 - y + ix)/2);
  * the output of direct_ft_arb (direct summation over n <= N, no stored
    sums) on the points "t re_s im_s" selected from that dump, one line
        t re_s im_s re_f im_f rad_re rad_im.

For each point the script records both values, the differences of the
midpoints and the ratios of the differences to the stored-sum radii, and
checks that every direct value lies inside the stored-sum ball (enlarged by
the direct value's own radius).  Only the comparison is done here, in exact
decimal arithmetic; both evaluations come from FLINT/Arb programs.

Prepared for Edward Baker with LLM assistance (Claude Opus 5.5,
claude-opus-5-5), 13 October 2026.  Internal corroboration, not a
certificate and not independent review.

Usage:
    python3 compare_direct_and_stored_sum_values.py \\
        --pair 882 dump882.txt direct882.txt --pair 1 dump1.txt direct1.txt \\
        --evaluator-source direct_ft_arb.c --patch barrier_dump_instrumentation.patch \\
        --output DIRECT_SUM_CORROBORATION_RECORD_20261013.json
"""
import argparse
import hashlib
import json
import sys
from decimal import Decimal as D, getcontext

getcontext().prec = 60


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def load_dump(path):
    out = {}
    order = []
    for line in open(path):
        if not line.startswith("DUMP "):
            continue
        f = line.split()
        key = (f[1], f[2], f[3])
        if key not in out:
            out[key] = [D(v) for v in f[4:10]]
            order.append(key)
    return out, order


def compare(prism, dump, direct):
    dd, order = load_dump(dump)
    points = []
    for line in open(direct):
        f = line.split()
        if len(f) < 7:
            continue
        key = (f[0], f[1], f[2])
        if key not in dd:
            raise SystemExit("direct point not found in dump: %r" % (key,))
        re_s, im_s, r_re, r_im, _, _ = dd[key]
        re_d, im_d, q_re, q_im = D(f[3]), D(f[4]), D(f[5]), D(f[6])
        d_re, d_im = abs(re_d - re_s), abs(im_d - im_s)
        points.append({
            "mesh_index": order.index(key),
            "t": f[0], "re_s": f[1], "im_s": f[2],
            "stored_sum": {"re": str(re_s), "im": str(im_s), "rad_re": str(r_re), "rad_im": str(r_im)},
            "direct_sum": {"re": f[3], "im": f[4], "rad_re": f[5], "rad_im": f[6]},
            "abs_diff_re": format(d_re, ".4E"), "abs_diff_im": format(d_im, ".4E"),
            "diff_over_radius_re": format(d_re / r_re, ".4E"), "diff_over_radius_im": format(d_im / r_im, ".4E"),
            "direct_inside_stored_ball": bool(d_re <= r_re + q_re and d_im <= r_im + q_im),
            "abs_f_direct": format((re_d * re_d + im_d * im_d).sqrt(), ".19f"),
        })
    mods = [((D(v[0]) ** 2 + D(v[1]) ** 2).sqrt(), k) for k, v in dd.items()]
    mmin = min(mods)
    summary = {
        "prism_of_sealed_transcript": prism,
        "mesh_points_in_dump": len(order),
        "points_compared": len(points),
        "dump_minimum_modulus_point_index": order.index(mmin[1]),
        "dump_minimum_modulus_point_compared": any(p["mesh_index"] == order.index(mmin[1]) for p in points),
        "dump_minimum_modulus_midpoint": format(mmin[0], ".19f"),
        "all_direct_values_inside_stored_balls": all(p["direct_inside_stored_ball"] for p in points),
        "max_abs_diff_re": max(D(p["abs_diff_re"]) for p in points).__format__(".4E"),
        "max_abs_diff_im": max(D(p["abs_diff_im"]) for p in points).__format__(".4E"),
        "max_diff_over_radius": max(max(D(p["diff_over_radius_re"]), D(p["diff_over_radius_im"])) for p in points).__format__(".4E"),
        "dump_sha256": sha(dump), "direct_output_sha256": sha(direct),
    }
    return summary, points


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--pair", nargs=3, action="append", metavar=("PRISM", "DUMP", "DIRECT"), required=True)
    ap.add_argument("--evaluator-source", help="direct_ft_arb.c, whose SHA-256 is recorded")
    ap.add_argument("--patch", help="barrier_dump_instrumentation.patch, whose SHA-256 is recorded")
    ap.add_argument("--output")
    args = ap.parse_args()
    rec = {"title": "Direct-summation corroboration of the barrier's stored-sum values of f_t",
           "date": "2026-10-13", "model": "Claude Opus 5.5 (claude-opus-5-5)",
           "source_package": {"repository": "https://github.com/judegomila/dbn-lambda-01787854-candidate-audit",
                              "commit": "a74738deb6d5e0f76887cb36901da08b68dca705"},
           "kind": "corroboration (both evaluations FLINT/Arb); not a certificate",
           "prisms": []}
    ok = True
    for prism, dump, direct in args.pair:
        summary, points = compare(int(prism), dump, direct)
        ok = ok and summary["all_direct_values_inside_stored_balls"]
        rec["prisms"].append({"summary": summary, "points": points})
        print("prism %s: %d of %d mesh points compared; all inside: %s; max |diff|/radius = %s; "
              "min-modulus point compared: %s" % (prism, summary["points_compared"], summary["mesh_points_in_dump"],
                                                  summary["all_direct_values_inside_stored_balls"],
                                                  summary["max_diff_over_radius"],
                                                  summary["dump_minimum_modulus_point_compared"]))
    rec["all_direct_values_inside_stored_balls"] = ok
    if args.evaluator_source:
        rec["evaluator_source_sha256"] = sha(args.evaluator_source)
        rec["evaluator_note"] = ("the outputs were produced by this source before its header comment was edited "
                                 "(output format and timing only); the code is unchanged")
    if args.patch:
        rec["instrumentation_patch_sha256"] = sha(args.patch)
    with open(__file__, "rb") as fh:
        rec["script_sha256"] = hashlib.sha256(fh.read()).hexdigest()
    if args.output:
        with open(args.output, "w") as fh:
            fh.write(json.dumps(rec, indent=1) + "\n")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
