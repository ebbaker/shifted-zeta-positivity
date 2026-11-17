#!/usr/bin/env python3
"""VCD-GT E04-r4 exterior real-bracket certificate, for Edward Baker.

16 November 2026. OpenAI Codex assistance; inherited actual model/effort
unavailable. Note30 pays the complete source, affine chain rule and signs.
Acquisition requires the frozen manifest and its externally supplied hash.
No routine in this module evaluates the target curvature K.
"""

import argparse
from fractions import Fraction
import gzip
from hashlib import sha256
import json
from math import comb, factorial
import os
from pathlib import Path
import platform
import signal
import sys
from time import perf_counter
from types import ModuleType
from tempfile import TemporaryDirectory

import flint
from flint import acb, arb, ctx, fmpq


BITS = 224
DEGREE = 12
LATTICE_DENOMINATOR = 3
CUTOFF = 12
SIGN_SCHEDULE = (16, 64, 256, 1024)
WEIGHT_CELLS = 512
XI_CALL_CAP = 200000
SOURCE_SECONDS_CAP = 360
TOTAL_SECONDS_CAP = 420
ARCHIVE_NAME = "E04-r4-exterior-boundary-fields.json.gz"
GEOMETRY_SHA256 = "8353074c4db8b15e10fbbafcaaf097b1241d0d27b21a0bfae047323cda154122"
NOTE30_SHA256 = "6ec2849f855e1ee4eeffd3fb26c955e1c1c357ebb5945d1fd3204c8bd78cc872"
CENTER = Fraction(140101, 10)
HALF_TIME = Fraction(1, 20)
TARGET = Fraction(59, 100)


class GateFailure(RuntimeError):
    pass


def q(value, denominator=None):
    value = Fraction(value, denominator) if denominator is not None else Fraction(value)
    return arb(fmpq(value.numerator, value.denominator))


def digest(data):
    return sha256(data).hexdigest()


def verified_bytes(path, expected, label):
    raw = path.read_bytes()
    if digest(raw) != expected:
        raise GateFailure(f"{label} SHA-256 mismatch")
    return raw


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":")).encode()


def bound_ball(lo, hi):
    lo, hi = q(lo), q(hi)
    return (lo + hi) / 2 + arb(0, ((hi - lo) / 2).upper())


def ball_parts(value):
    return list(map(int, value.mid_rad_10exp()))


def restored_ball(parts):
    if not (isinstance(parts, list) and len(parts) == 3
            and all(isinstance(v, int) and not isinstance(v, bool) for v in parts)):
        raise GateFailure("invalid decimal ball triple")
    mid, radius, exponent = parts
    if radius < 0 or abs(exponent) > 100000:
        raise GateFailure("invalid decimal ball radius/exponent")
    unit = arb(10) ** exponent
    value = mid * unit + arb(0, (radius * unit).upper())
    if not value.is_finite():
        raise GateFailure("nonfinite restored source ball")
    return value


def parse_rational(value, name):
    if not isinstance(value, str):
        raise GateFailure(f"{name} must be an exact rational string")
    try:
        return Fraction(value)
    except (ValueError, ZeroDivisionError) as error:
        raise GateFailure(f"invalid rational {name}") from error


def read_manifest(path, expected):
    data = json.loads(verified_bytes(path, expected, "manifest"))
    if parse_rational(data.get("center"), "center") != CENTER:
        raise GateFailure("unexpected target center")
    if not isinstance(data.get("groups"), list) or not data["groups"]:
        raise GateFailure("manifest requires a nonempty groups array")
    groups, seen = [], set()
    for row in data["groups"]:
        ident = row.get("id")
        if not isinstance(ident,(str,int)) or isinstance(ident,bool):
            raise GateFailure("group ids must be strings or integers")
        ident = str(ident)
        if not ident or ident in seen:
            raise GateFailure("group ids must be distinct after string normalization")
        seen.add(ident)
        group = {"id": ident}
        for name in ("mid_offset", "slope", "half_width"):
            group[name] = parse_rational(row.get(name), name)
        if group["half_width"] <= 0:
            raise GateFailure("nonpositive bracket half-width")
        groups.append(group)
    return groups


def interval_at(group, t):
    middle = group["mid_offset"] + group["slope"] * (t - HALF_TIME)
    return middle - group["half_width"], middle + group["half_width"]


def geometry_checks(groups):
    for t in (Fraction(0), Fraction(1, 10)):
        last_upper = None
        for group in groups:
            lo, hi = interval_at(group, t)
            if not lo < hi:
                raise GateFailure("empty bracket")
            if not (hi < -Fraction(8, 5) or lo > Fraction(8, 5)):
                raise GateFailure(f"target exclusion fails: {group['id']}")
            if last_upper is not None and not last_upper < lo:
                raise GateFailure("manifest order/disjointness fails")
            if not (13840 <= CENTER + lo < CENTER + hi <= 14180):
                raise GateFailure("moving boundary leaves source center range")
            last_upper = hi
    return {"endpoint_times": ["0", "1/10"], "positive_ordered_disjoint": True,
            "target_radius_excluded": "8/5", "all_boundary_centers": [13840, 14180],
            "affine_endpoint_checks_pay_full_time": True}


def boundary_list(groups):
    answer = []
    for group in groups:
        for side, direction in (("left", -1), ("right", 1)):
            answer.append({"id": f"{group['id']}:{side}", "group_id": group["id"],
                           "side": side, "B": CENTER + group["mid_offset"]
                           + direction * group["half_width"], "v": group["slope"]})
    return answer


def source_parameters():
    return {"precision_bits": BITS, "time_degree": DEGREE,
            "lattice_denominator": LATTICE_DENOMINATOR, "cutoff": CUTOFF,
            "gauge": "constant exp(pi*B/8) on each affine boundary",
            "time_order": "ascending Lobatto nodes x=cos(pi*(n-l)/n)",
            "sample_content": "finite-source arithmetic balls before analytic source padding",
            "component_format": "[midpoint_integer,radius_integer,decimal_exponent]"}


def load_geometry_module():
    path = Path(__file__).resolve().with_name("vcd_gt_joint_strip_geometry.py")
    source = verified_bytes(path, GEOMETRY_SHA256, "geometry consumer")
    module = ModuleType("pinned_exterior_geometry")
    module.__file__ = str(path)
    sys.modules[module.__name__] = module
    exec(compile(source, str(path), "exec"), module.__dict__)
    note = path.parents[1] / "notes/30_VCD_GT_E03_REAL_BRACKETS_AND_MOVING_BOUNDARIES_20261116.md"
    verified_bytes(note, NOTE30_SHA256, "Note30 proof")
    return module


def mass_on_cell(groups, center_offset, d_lower, tlo, thi):
    total = q(5000, 1962848636289)
    for group in groups:
        left0, right0 = interval_at(group, tlo)
        left1, right1 = interval_at(group, thi)
        lo, hi = min(left0, left1), max(right0, right1)
        distance = max(abs(q(lo) - center_offset).upper(), abs(q(hi) - center_offset).upper())
        denominator = distance**2 - d_lower
        if not denominator > 0:
            raise GateFailure("nonpositive real-weight denominator")
        total += 1 / denominator
    return total.lower()


def target_geometry_and_mass(groups, cache_dir):
    """Replay only target count/collar and c,D moments, never K methods."""
    geometry = load_geometry_module()
    consumer = geometry.load_verified_consumer()
    samples = consumer.archived_fields(cache_dir)
    coefficients, sample_radius = consumer.tensor_coefficients(samples)
    wide_error, wide_record = geometry.disk_error(sample_radius, q(8, 5))
    narrow_error, _, narrow_record = consumer.tensor_error(sample_radius)
    wide = consumer.FieldPolynomial(coefficients, wide_error)
    narrow = consumer.FieldPolynomial(coefficients, narrow_error)
    if wide.sign != narrow.sign:
        raise GateFailure("inconsistent true-field signs")
    record = {"source_archive": {"filename": consumer.ARCHIVE,
              "stored_sha256": consumer.STORED_SHA256,
              "content_sha256": consumer.CONTENT_SHA256},
              "source_hashes_verified": True,
              "auxiliary_disk_error": wide_record, "original_disk_error": narrow_record,
              "auxiliary_geometry": {}, "original_collar": {}}
    if geometry.certify_boundaries(wide, q(8, 5), record["auxiliary_geometry"]) is None:
        raise GateFailure("auxiliary target-only disk failed")
    original = geometry.certify_boundaries(narrow, q(21, 20), record["original_collar"])
    if original is None:
        raise GateFailure("target collar failed")
    boundaries, data = original
    target = narrow.circle(q(9, 10), consumer.N)
    collar = consumer.ContourCertificate(narrow, target, boundaries, data)
    record["log_moment_collar"] = collar.geometry_record(data)
    pads = collar.padding(q(1, WEIGHT_CELLS))
    record["cells"] = []
    coordinate_balls = []
    floor = coarse_floor = global_floor = None
    coarse_center = arb(0, q(7, 100))
    global_center = bound_ball("0.0594957328", "0.0637631130")
    for i in range(WEIGHT_CELLS):
        c, d = geometry.cell_moments(target, pads, collar.center, collar.moment_errors, i)
        if not (abs(c) < q(7, 100) and abs(d) < q(1, 5)):
            raise GateFailure("inherited c,D magnitude gate failed")
        if not (c >= q("0.0594957328") and c <= q("0.0637631130")
                and d >= q("0.0007983892") and d <= q("0.1791166200")):
            raise GateFailure("replayed cells leave the recorded global coordinate bounds")
        coordinate_balls.append((c,d))
        tlo, thi = Fraction(i, 10 * WEIGHT_CELLS), Fraction(i + 1, 10 * WEIGHT_CELLS)
        lower = mass_on_cell(groups, c, d.lower(), tlo, thi)
        coarse = mass_on_cell(groups, coarse_center, -q(1, 5), tlo, thi)
        global_bound = mass_on_cell(groups, global_center, q("0.0007983892"), tlo, thi)
        floor = lower if floor is None else min(floor, lower)
        coarse_floor = coarse if coarse_floor is None else min(coarse_floor, coarse)
        global_floor = global_bound if global_floor is None else min(global_floor, global_bound)
        record["cells"].append({"cell": i, "c_offset": str(c), "D": str(d),
                                "conditional_lower_mass": str(lower)})
    record.update({"cell_count": WEIGHT_CELLS, "minimum_conditional_mass": str(floor),
                   "coarse_coordinate_minimum": str(coarse_floor),
                   "record09_global_coordinate_minimum": str(global_floor),
                   "threshold": "59/100", "conditional_mass_pass": bool(floor >= q(TARGET)),
                   "mirror_retained": "target reflection only; 5000/1962848636289",
                   "selected_negative_reflections_retained": False,
                   "K_calls": 0, "coordinate_inputs_are_independent_of_K": True,
                   "count_condition": "exterior lower counts remain to be certified by boundary signs"})
    if not record["conditional_mass_pass"]:
        return record, False, coordinate_balls
    return record, True, coordinate_balls


def times_and_basis():
    n = DEGREE
    basis = [[arb.cos_pi_fmpq(fmpq((n-l)*k, n)) for k in range(n+1)] for l in range(n+1)]
    times = [(1 + row[1]) / 20 for row in basis]
    times[0], times[-1] = arb(0), q(1, 10)
    if n % 2 == 0:
        times[n//2] = q(1, 20)
    return times, basis


class CompleteSource:
    def __init__(self):
        self.pi = arb.pi()
        self.log_pi = self.pi.log()
        self.h = q(1, LATTICE_DENOMINATOR)
        self.r = [self.h*k for k in range(CUTOFF*LATTICE_DENOMINATOR+1)]
        self.weights = [(-r*r).exp() for r in self.r]
        self.prefactor = self.h/self.pi.sqrt()
        self.calls = 0
        self.started = perf_counter()

    def xi(self, b, B, shift):
        if self.calls >= XI_CALL_CAP:
            raise GateFailure("xi-call cap reached")
        if perf_counter()-self.started >= SOURCE_SECONDS_CAP:
            raise GateFailure("source wall-clock cap reached")
        # Reflection to Re(s)>=1/2 is exact for xi and stabilizes the zeta input.
        s = acb((1+shift)/2, -b/2)
        value = (self.pi*q(B)/8 + (s/2).lgamma() - s*self.log_pi/2).exp()
        value *= s*(s-1)*s.zeta()/16
        self.calls += 1
        if not value.is_finite():
            raise GateFailure("nonfinite complete-source xi ball")
        return value.real

    def value(self, boundary, time, t0=False):
        b = q(boundary["B"]) + q(boundary["v"])*(time-q(1, 20))
        value = self.xi(b, boundary["B"], arb(0))
        if t0:
            return value
        scale = 2*time.sqrt()
        for k in range(1, len(self.r)):
            value += 2*self.weights[k]*self.xi(b, boundary["B"], scale*self.r[k])
        return self.prefactor*value


def analytic_errors(v):
    pi = arb.pi()
    alpha, beta = q(9999, 10000), q(131, 100)
    amplitude = (beta**2/(4*alpha)).exp()/alpha.sqrt()
    lattice = 4*arb(10**13)*arb(4).exp()*amplitude/(4*pi*LATTICE_DENOMINATOR).expm1()
    tail = 2*arb(10**13)*(-144*alpha+12*beta).exp()/(pi.sqrt()*(24*alpha-beta))
    gauge = (pi*abs(q(v))/160).exp()
    source = gauge*(lattice+tail)
    m5 = 2*arb(10**16)*amplitude
    m = DEGREE+1
    derivative = gauge*m5*sum(comb(m,j)*abs(q(v))**(m-j)*factorial(m+j)/arb(5)**(m+j)
                              for j in range(m+1))
    time = derivative/factorial(m)*q(1,20)**m/q(2)**(DEGREE-1)
    total = ((2*DEGREE+1)*source+time).upper()
    return total, {"source_lattice": str(lattice.upper()), "source_tail": str(tail.upper()),
                   "constant_gauge_factor": str(gauge.upper()),
                   "uniform_constant_gauge_source": str(source.upper()),
                   "time_chain_rule_derivative": str(derivative.upper()),
                   "time_interpolation_error": str(time.upper()),
                   "sample_operator_norm": 2*DEGREE+1,
                   "complete_analytic_error": str(total)}


def chebyshev_coefficients(samples, basis):
    n = DEGREE
    weights = [q(1,2)] + [arb(1)]*(n-1) + [q(1,2)]
    return [2*weights[k]*sum(weights[l]*samples[l]*basis[l][k] for l in range(n+1))/n
            for k in range(n+1)]


def chebyshev_value(coefficients, x):
    if len(coefficients) == 1:
        return coefficients[0]
    b1, b2 = arb(0), arb(0)
    for coefficient in reversed(coefficients[1:]):
        b0 = coefficient+2*x*b1-b2
        b2,b1 = b1,b0
    return coefficients[0]+x*b1-b2


def certify_sign(coefficients, error, schedule=SIGN_SCHEDULE):
    reference = chebyshev_value(coefficients, arb(0))
    if reference > error:
        sign = 1
    elif reference < -error:
        sign = -1
    else:
        return {"success": False, "failure": "midpoint sign unresolved", "attempts": []}
    derivative = sum(k*k*abs(value).upper() for k,value in enumerate(coefficients)).upper()
    attempts = []
    for cells in schedule:
        floor = None
        failed_at = None
        for k in range(cells):
            x = q(2*k+1-cells, cells)
            lower = (sign*chebyshev_value(coefficients,x)-derivative/cells-error).lower()
            floor = lower if floor is None else min(floor, lower)
            if not lower > 0:
                failed_at = k
                break
        attempts.append({"cells": cells, "floor_checked": str(floor), "failure_cell": failed_at})
        if failed_at is None:
            return {"success": True, "sign": sign, "uniform_sign_floor": str(floor),
                    "derivative_upper": str(derivative), "cells": cells, "attempts": attempts}
    return {"success": False, "sign": sign, "failure": "sign mesh schedule exhausted",
            "derivative_upper": str(derivative), "attempts": attempts}


def control_checks(groups=None):
    # These exact-polynomial controls exercise sign rejection without source calls.
    positive = certify_sign([arb(2), arb(0)], arb(0))
    zero = certify_sign([arb(0)], arb(0))
    interior = certify_sign([q(1,4),arb(0),q(1,2)],arb(0))  # x^2-1/4
    if not positive["success"] or zero["success"] or interior["success"]:
        raise GateFailure("sign control failure")
    # At T=1/20 the quartic is (z^2-a^2)^2; every exterior real point is positive.
    # Equal positive signs at both endpoints cannot establish an extra bracket.
    no_extra_bracket = True
    if groups is not None:
        for group in groups:
            lo,hi = interval_at(group,HALF_TIME)
            for offset in (lo,hi):
                z = CENTER+offset
                if not ((z*z-CENTER*CENTER)**2>0 and offset*offset>0):
                    no_extra_bracket = False
    wrong_hash_rejected = False
    missing_source_rejected = False
    with TemporaryDirectory(prefix="vcd-gt-exterior-controls-") as directory:
        path = Path(directory)/"control"
        path.write_bytes(b"control")
        try:
            verified_bytes(path,"0"*64,"altered source control")
        except GateFailure:
            wrong_hash_rejected = True
        try:
            read_archive(Path(directory)/"missing", "0"*64,"0"*64,{})
        except GateFailure:
            missing_source_rejected = True
    if not no_extra_bracket or not wrong_hash_rejected or not missing_source_rejected:
        raise GateFailure("control predicate failed")
    return {"constant_positive_passes": positive["success"], "zero_sign_rejected": not zero["success"],
            "interior_sign_change_rejected": not interior["success"],
            "quartic_at_double_no_exterior_opposite_sign": no_extra_bracket,
            "altered_hash_refused": wrong_hash_rejected,
            "missing_source_refused": missing_source_rejected,
            "interpretation": "exact algebraic controls, not canonical source samples"}


def archive_path(cache_dir):
    relative = Path("numerics-archives")/ARCHIVE_NAME
    normal = Path(__file__).resolve().parents[1]/relative
    if cache_dir:
        return cache_dir/ARCHIVE_NAME
    if normal.is_file():
        return normal
    if root := os.getenv("VCD_GT_ARCHIVES"):
        return Path(root)/relative
    return normal


def archive_metadata(manifest_hash, script_hash, boundaries):
    return {"manifest_sha256": manifest_hash, "source_script_sha256": script_hash,
            "parameters": source_parameters(),
            "boundaries": [{"id":b["id"],"B":str(b["B"]),"v":str(b["v"])} for b in boundaries]}


def acquire_samples(boundaries, times, metadata, cache_path, record):
    if cache_path.exists():
        raise GateFailure("refusing to overwrite an existing source archive")
    expected_calls = len(boundaries)*(1+DEGREE*(1+CUTOFF*LATTICE_DENOMINATOR))
    if expected_calls > XI_CALL_CAP:
        raise GateFailure("fixed source-call projection exceeds cap")
    source = CompleteSource()
    fields = []
    # First two complete boundary rows are reused, not a discarded benchmark.
    try:
        for index,boundary in enumerate(boundaries):
            row = [source.value(boundary,t,t0=(l==0)) for l,t in enumerate(times)]
            fields.append(row)
            if index == min(1,len(boundaries)-1):
                elapsed = perf_counter()-source.started
                projection = elapsed*expected_calls/source.calls
                record["source_preflight"] = {"rows": index+1, "xi_calls": source.calls,
                      "elapsed_seconds": elapsed,"projected_source_seconds": projection,
                      "expected_total_xi_calls": expected_calls,"cap_seconds": SOURCE_SECONDS_CAP,
                      "gate": projection < SOURCE_SECONDS_CAP}
                print(f"source projection {projection:.2f}s for {expected_calls} xi calls",flush=True)
                if not projection < SOURCE_SECONDS_CAP:
                    raise GateFailure("source preflight projection exceeds frozen cap")
            if (index+1)%32 == 0:
                print(f"boundary rows {index+1}/{len(boundaries)}; xi calls {source.calls}",flush=True)
    finally:
        record["source_xi_calls"] = source.calls
        record["source_seconds"] = perf_counter()-source.started
    if record["source_seconds"] > SOURCE_SECONDS_CAP:
        raise GateFailure("source work exceeded its frozen cap")
    if source.calls != expected_calls:
        raise GateFailure("unexpected complete-source call count")
    archive = {"metadata": metadata, "finite_arithmetic_fields": [[ball_parts(v) for v in row] for row in fields]}
    payload = canonical_json(archive)
    stored = gzip.compress(payload,mtime=0)
    cache_path.parent.mkdir(parents=True,exist_ok=True)
    with cache_path.open("xb") as stream:
        stream.write(stored)
    # Acquisition and replay both consume the serialized balls, not distinct paths.
    info = {"filename": cache_path.name,"stored_sha256":digest(stored),
            "content_sha256":digest(payload),"stored_bytes":len(stored),
            "content_bytes":len(payload),"path_at_acquisition":str(cache_path)}
    return read_archive(cache_path,info["stored_sha256"],info["content_sha256"],metadata),info


def read_archive(path, stored_hash, content_hash, metadata):
    if not path.is_file():
        raise GateFailure(f"missing source archive {path}; regenerate with the frozen --acquire contract")
    stored = verified_bytes(path,stored_hash,"boundary stored archive")
    payload = gzip.decompress(stored)
    if digest(payload) != content_hash:
        raise GateFailure("boundary archive content SHA-256 mismatch")
    decoded = json.loads(payload)
    if decoded.get("metadata") != metadata:
        raise GateFailure("boundary source metadata mismatch")
    fields = decoded.get("finite_arithmetic_fields")
    if not isinstance(fields,list) or len(fields) != len(metadata["boundaries"]):
        raise GateFailure("boundary source row count mismatch")
    if any(not isinstance(row,list) or len(row) != DEGREE+1 for row in fields):
        raise GateFailure("boundary source time count mismatch")
    return [[restored_ball(parts) for parts in row] for row in fields]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--acquire",action="store_true")
    modes.add_argument("--replay",action="store_true")
    modes.add_argument("--self-test",action="store_true")
    parser.add_argument("--manifest",type=Path)
    parser.add_argument("--manifest-sha256")
    parser.add_argument("--cache-dir",type=Path)
    parser.add_argument("--target-cache-dir",type=Path)
    parser.add_argument("--expected-stored-sha256")
    parser.add_argument("--expected-content-sha256")
    parser.add_argument("--output",type=Path)
    args = parser.parse_args()
    ctx.prec = BITS
    if args.self_test:
        print(json.dumps(control_checks(),indent=2))
        return 0
    if not args.manifest or not args.manifest_sha256 or not args.output:
        parser.error("manifest, manifest-sha256 and output are required")
    if args.replay and not (args.expected_stored_sha256 and args.expected_content_sha256):
        parser.error("replay requires both externally supplied archive hashes")
    started = perf_counter()
    script_hash = digest(Path(__file__).read_bytes())
    record = {"request":"VCD-GT-E04-r4", "date":"2026-11-16 America/New_York",
              "prepared_for":"Edward Baker", "llm_assistance":"OpenAI Codex; inherited actual model/effort unavailable",
              "script_sha256":script_hash,"manifest_sha256":args.manifest_sha256,
              "note30_sha256":NOTE30_SHA256,"geometry_script_sha256":GEOMETRY_SHA256,
              "versions":{"python":platform.python_version(),"python_flint":flint.__version__,
                          "flint":flint.__FLINT_VERSION__,"platform":platform.platform()},
              "parameters":source_parameters(),"sign_schedule":SIGN_SCHEDULE,
              "weight_cells":WEIGHT_CELLS,"xi_call_cap":XI_CALL_CAP,
              "source_seconds_cap":SOURCE_SECONDS_CAP,"total_seconds_cap":TOTAL_SECONDS_CAP,
              "mode":"acquire" if args.acquire else "replay",
              "target_K_calls":0,"success":False}
    def timed_out(_signum,_frame):
        raise GateFailure("total certificate wall-clock cap reached")
    signal.signal(signal.SIGALRM,timed_out)
    signal.setitimer(signal.ITIMER_REAL,TOTAL_SECONDS_CAP)
    try:
        pins_path = Path(__file__).resolve().parents[1]/"research-progress/handoffs/VCD-GT-E04-r4-certificate-input-pins.json"
        pins_raw = pins_path.read_bytes()
        pins = json.loads(pins_raw)
        for relative,expected in pins["input_hashes"].items():
            verified_bytes(Path(__file__).resolve().parents[1]/relative,expected,"frozen input "+relative)
        record["input_pins_sha256"] = digest(pins_raw)
        record["frozen_input_hashes"] = pins["input_hashes"]
        groups = read_manifest(args.manifest,args.manifest_sha256)
        record["manifest_geometry"] = geometry_checks(groups)
        record["controls"] = control_checks(groups)
        record["stage"] = "target coordinate replay and hypothetical mass before boundary acquisition"
        record["target_geometry"],mass_pass,coordinates = target_geometry_and_mass(groups,args.target_cache_dir)
        print("hypothetical mass",record["target_geometry"]["minimum_conditional_mass"],"pass",mass_pass,flush=True)
        if not mass_pass:
            raise GateFailure("manifest fails conditional mass threshold before new boundary xi work")
        boundaries = boundary_list(groups)
        times,basis = times_and_basis()
        metadata = archive_metadata(args.manifest_sha256,script_hash,boundaries)
        path = archive_path(args.cache_dir)
        record["stage"] = "boundary source acquisition" if args.acquire else "boundary source replay"
        if args.acquire:
            signal.setitimer(signal.ITIMER_REAL,min(SOURCE_SECONDS_CAP,TOTAL_SECONDS_CAP-(perf_counter()-started)))
            fields,record["source_archive"] = acquire_samples(boundaries,times,metadata,path,record)
            remaining = TOTAL_SECONDS_CAP-(perf_counter()-started)
            if remaining <= 0:
                raise GateFailure("total certificate wall-clock cap reached")
            signal.setitimer(signal.ITIMER_REAL,remaining)
        else:
            fields = read_archive(path,args.expected_stored_sha256,args.expected_content_sha256,metadata)
            record["source_archive"] = {"filename":path.name,"stored_sha256":args.expected_stored_sha256,
                                         "content_sha256":args.expected_content_sha256,"hashes_verified":True}
            record["source_xi_calls"] = 0
        record["stage"] = "complete-time boundary signs"
        record["boundary_signs"] = []
        signs = {}
        for boundary,row in zip(boundaries,fields):
            coefficients = chebyshev_coefficients(row,basis)
            error,budget = analytic_errors(boundary["v"])
            result = certify_sign(coefficients,error)
            result.update({"id":boundary["id"],"B":str(boundary["B"]),"v":str(boundary["v"]),"error_budget":budget})
            record["boundary_signs"].append(result)
            if result["success"]:
                signs[boundary["id"]] = result["sign"]
        retained = []
        record["group_dispositions"] = []
        for group in groups:
            left,right = signs.get(group["id"]+":left"),signs.get(group["id"]+":right")
            passed = left is not None and right is not None and left == -right
            record["group_dispositions"].append({"id":group["id"],"retained":passed,
                 "reason":"opposite complete-time signs" if passed else "boundary sign failed or not opposite"})
            if passed:
                retained.append(group)
        retained_floor = None
        for i,(c,d) in enumerate(coordinates):
            lower = mass_on_cell(retained,c,d.lower(),Fraction(i,10*WEIGHT_CELLS),Fraction(i+1,10*WEIGHT_CELLS))
            record["target_geometry"]["cells"][i]["retained_lower_mass"] = str(lower)
            retained_floor = lower if retained_floor is None else min(retained_floor,lower)
        record["minimum_retained_lower_mass"] = str(retained_floor)
        record["retained_groups"] = len(retained)
        record["omitted_groups"] = len(groups)-len(retained)
        if not retained_floor >= q(TARGET):
            raise GateFailure("retained sign-certified manifest fails full-slab mass threshold")
        record.update({"stage":"complete", "success":True,
                       "exact_singleton_counts_claimed":False,"simplicity_claimed":False,
                       "labels_used":False,"full_slab_threshold":"-K >= 59/100",
                       "selected_real_lower_count":len(retained),
                       "minimum_certified_lower_mass":str(retained_floor)})
    except (OSError,ValueError,RuntimeError,KeyError,TypeError) as error:
        record["failure"] = str(error)
    finally:
        signal.setitimer(signal.ITIMER_REAL,0)
    record["total_seconds"] = perf_counter()-started
    record["status"] = "exterior lower mass acquired pending internal review" if record["success"] else "failed gate"
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(record,indent=2)+"\n")
    print(record["status"],record.get("failure",""),flush=True)
    return 0 if record["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
