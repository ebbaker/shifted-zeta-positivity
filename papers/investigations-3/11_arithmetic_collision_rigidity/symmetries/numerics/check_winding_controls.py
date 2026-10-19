#!/usr/bin/env python3
"""Own-source interval controls for the GEO-T1 winding acceptance helpers.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Actual model gpt-6.1-sol (Codex), actual effort ultra. Internal same-model
controls, not an independent specialist review. No theta error is assigned
to a polynomial control: its own exact H and Hx are evaluated on each cell.
"""
import argparse
import copy
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import importlib.util
import json
import platform
from pathlib import Path
import sys

import flint
from flint import arb, ctx


def require(ok, message):
    if not bool(ok):
        raise ValueError(message)


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_helpers(path, name="geo_t1_winding_helpers"):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def r(value):
    value = F(value)
    return arb(value.numerator) / value.denominator


def interval(lo, hi):
    lo, hi = F(lo), F(hi)
    require(lo <= hi, "interval endpoints reversed")
    return r((lo+hi)/2) + arb(0, 1)*r((hi-lo)/2)


def polynomial_jet(name, t, x):
    if name == "quadratic":
        return [x*x-2*t, 2*x]
    if name == "cubic":
        return [x*x*x-6*t*x, 3*x*x-6*t]
    if name == "quartic":
        x2=x*x
        return [x2*x2-12*t*x2+12*t*t, 4*x2*x-24*t*x]
    if name == "linear":
        return [x, arb(1)]
    if name == "constant":
        return [arb(1), arb(0)]
    if name == "boundary_event":
        return [x*x-2*(t+1), 2*x]
    if name == "uncertain_constant":
        return [arb(1)+arb(0,1), arb(0)]
    raise ValueError("unknown control polynomial")


def encloser(name):
    def evaluate(t0,t1,x0,x1):
        return polynomial_jet(name, interval(t0,t1), interval(x0,x1))
    return evaluate


def expect_raises(fn, message):
    try:
        fn()
    except (ValueError, TypeError):
        return True
    raise ValueError("missing interface rejection: "+message)


def run(helper_path, bits=192, comparison_path=None):
    require(128 <= bits <= 4096, "precision outside bounded range")
    ctx.prec = bits
    h = load_helpers(helper_path)
    box = [F(-1),F(1),F(-1),F(1)]
    expected = {"quadratic":-1,"cubic":-1,"quartic":-2,
                "linear":0,"constant":0}
    records = {}
    boundaries = {}
    checks = {}
    for name, degree in expected.items():
        result = h.boundary_acceptance(encloser(name),box,
                                       max_depth=9,max_calls=512)
        require(result.get("degree") == degree,
                name+" exact own-source degree")
        require(result.get("status") == ("pass" if degree == 0 else "nonzero_degree"),
                name+" actual acceptance status")
        adaptive = h.adaptive_boundary(encloser(name),box,
                                       max_depth=9,max_calls=512)
        require(adaptive.get("status") == "complete",name+" complete cover")
        polygon = h.polygon_from_halfplanes(adaptive,box)
        require(h.polygon_winding(polygon) == degree,name+" actual polygon degree")
        require(h.polygon_winding(list(reversed(polygon))) == -degree,
                name+" reverse orientation")
        records[name] = result
        boundaries[name] = adaptive["boundary"]
        checks[name+"_whole_boundary_own_jet"] = True
        checks[name+"_orientation_reversal"] = True

    for name in ("boundary_event","uncertain_constant"):
        result = h.boundary_acceptance(encloser(name),box,
                                       max_depth=9,max_calls=512)
        require(result.get("status") == "inconclusive" and result.get("degree") is None,
                name+" must fail strict boundary acceptance")
        records[name] = result
        checks[name+"_rejects_strict_acceptance"] = True

    good = boundaries["constant"]
    require(len(good)>=4,"four boundary faces must be represented")
    checks["omitted_wall_rejected"] = expect_raises(
        lambda:h.polygon_from_halfplanes(good[1:],box),"omitted wall/segment")
    broken = copy.deepcopy(good)
    broken[0]["to"][0] = "0"
    checks["broken_contiguity_rejected"] = expect_raises(
        lambda:h.polygon_from_halfplanes(broken,box),"broken contiguity")
    checks["reversed_boundary_orientation_rejected"] = expect_raises(
        lambda:h.polygon_from_halfplanes(list(reversed(good)),box),
        "reversed boundary orientation")
    conflict = copy.deepcopy(good)
    conflict[1]["component"] = conflict[0]["component"]
    conflict[1]["sign"] = -conflict[0]["sign"]
    conflict[1]["margin_lower"] = "1"
    checks["conflicting_incident_halfplanes_rejected"] = expect_raises(
        lambda:h.polygon_from_halfplanes(conflict,box),"conflicting incident halfplanes")
    checks["polygon_origin_vertex_rejected"] = expect_raises(
        lambda:h.polygon_winding([(F(0),F(0)),(F(1),F(0)),(F(1),F(1))]),
        "origin polygon vertex")
    checks["polygon_origin_crossing_rejected"] = expect_raises(
        lambda:h.polygon_winding([(F(-1),F(0)),(F(1),F(0)),(F(0),F(1))]),
        "origin crossing polygon edge")
    require(h.polygon_winding([(F(1),F(0))]*4)==0,"nonzero constant polygon")
    checks["nonzero_constant_polygon_degree_zero"] = True
    require(h.polygon_winding([(F(1),F(0)),(F(0),F(1)),(F(-1),F(0)),(F(0),F(-1))])==1,
            "unit diamond positive degree")
    checks["unit_diamond_degree_positive_one"] = True

    checks["separator_zero_uncertainty_rejected"] = h.strict_separator([arb(0),arb(0)]) is None
    checks["separator_uncertainty_touching_zero_rejected"] = h.strict_separator([arb(1)+arb(0,1),arb(0)]) is None
    require(checks["separator_zero_uncertainty_rejected"] and
            checks["separator_uncertainty_touching_zero_rejected"],"strictness at zero")
    checks["separator_missing_component_guard"] = expect_raises(
        lambda:h.strict_separator([arb(1)]),"missing second component")
    checks["separator_nonfinite_guard"] = expect_raises(
        lambda:h.strict_separator([arb('nan'),arb(1)]),"nonfinite component")
    checks["degenerate_box_guard"] = expect_raises(
        lambda:h.boundary_acceptance(encloser("constant"),[F(0),F(0),F(-1),F(1)]),
        "degenerate box")
    checks["reversed_box_guard"] = expect_raises(
        lambda:h.boundary_acceptance(encloser("constant"),[F(1),F(-1),F(-1),F(1)]),
        "reversed box")
    checks["negative_depth_guard"] = expect_raises(
        lambda:h.boundary_acceptance(encloser("constant"),box,max_depth=-1),
        "negative maximum depth")
    checks["zero_call_budget_guard"] = expect_raises(
        lambda:h.boundary_acceptance(encloser("constant"),box,max_calls=0),
        "zero call budget")
    partial=h.boundary_acceptance(encloser("constant"),box,max_calls=1)
    require(partial.get("status")=="inconclusive" and partial.get("degree") is None
            and partial.get("calls")==1 and not partial.get("accepts_zero_degree"),
            "an exhausted partial boundary must never acquire a degree")
    checks["exhausted_partial_boundary_is_inconclusive"] = True
    checks["incomplete_boundary_record_cannot_form_polygon"] = expect_raises(
        lambda:h.polygon_from_halfplanes(partial,box),"incomplete boundary record")
    records["partial_budget_constant"] = partial
    checks["binary_float_box_guard"] = expect_raises(
        lambda:h.boundary_acceptance(encloser("constant"),[-1.0,1,-1,1]),
        "inexact binary-float domain")
    checks["unknown_limits_key_guard"] = expect_raises(
        lambda:h.boundary_acceptance(encloser("constant"),box,limits={"unrecognized":1}),
        "unknown limits key")
    result_from_limits=h.boundary_acceptance(encloser("constant"),box,
                                             limits={"max_calls":4,"max_depth":0})
    require(result_from_limits.get("status")=="pass" and
            result_from_limits.get("degree")==0 and result_from_limits.get("calls")==4,
            "supported limits dictionary")
    checks["supported_limits_dictionary"] = True
    direct_records={}
    if comparison_path is None:
        candidate=helper_path.with_name("compare_winding_direct.py")
        comparison_path=candidate if candidate.is_file() else None
    if comparison_path is not None:
        comparison=load_helpers(comparison_path,"geo_t1_actual_direct_comparison")
        class DirectBase:
            A=staticmethod(r)
        class DirectOwnSource:
            def __init__(self,name):
                self.name=name;self.calls=0;self.base=DirectBase
            def enclose(self,t0,t1,x0,x1):
                require(self.calls<512,"own-source direct consumer 512-call limit")
                self.calls+=1
                t=interval(t0,t1)-r(F(21,200));x=interval(x0,x1)-1000
                if self.name=="shifted_quadratic_event":
                    return[x*x-2*t,2*x,arb(2)]
                if self.name=="uncertain_constant":
                    return[arb(1)+arb(0,1),arb(0),arb(0)]
                return[arb(1),arb(0),arb(0)]
        for name in ("shifted_quadratic_event","constant","uncertain_constant"):
            view=DirectOwnSource(name)
            try:
                result=comparison.direct_consumer(view)
            except (ArithmeticError,RuntimeError,ValueError) as error:
                result={"status":"inconclusive","coverage_verified":False,
                        "failure":str(error),"calls":view.calls}
            expected_status="pass" if name=="constant" else "inconclusive"
            require(result.get("status")==expected_status and
                    bool(result.get("coverage_verified"))==(name=="constant"),
                    "actual direct own-source acceptance: "+name)
            if name=="shifted_quadratic_event":
                require(result.get("midpoint_calls",0)>0,
                        "event must exercise paid midpoint propagation")
            if name=="uncertain_constant":
                require(view.calls==512,"persistent uncertainty reaches declared bound")
            direct_records[name]=result
            checks["actual_direct_own_"+name]=True
    require(all(checks.values()),"all winding controls")
    output={
        "date":"2026-10-19","generated_at_utc":datetime.now(timezone.utc).isoformat(),
        "prepared_for":"Edward Baker","actual_model":"gpt-6.1-sol (Codex)",
        "actual_effort":"ultra","llm_assistance":"substantial; separate same-model controls",
        "status":"pass: own-source exact-polynomial winding acceptance controls",
        "runtime":{"python":platform.python_version(),"python_flint":flint.__version__,
                   "precision_bits":bits},
        "box_t0_t1_x0_x1":[str(v) for v in box],
        "scope":["Arb outward intervals evaluate each polynomial control's own exact H,Hx on every requested boundary segment.",
                 "Interior quadratic/cubic/quartic heat collisions have nonzero degrees -1,-1,-2; actual zero-degree acceptance must reject them.",
                 "Linear and constant nonvanishing first jets have degree zero; boundary event and uncertainty touching zero remain inconclusive.",
                 "These are controls for the actual new winding acceptance helpers, not a theta certificate or validation by assertion count."],
        "checks":checks,"control_records":records,"actual_direct_own_source_controls":direct_records,
        "helper_sha256":sha(helper_path),"control_checker_sha256":sha(Path(__file__)),
    }
    if comparison_path is not None:
        output["direct_control_comparison_sha256"]=sha(comparison_path)
        output["scope"].append("The actual direct-consumer implementation is separately exercised on frozen B by its own shifted quadratic heat event, exact constant, and a true constant with uniform value uncertainty reaching zero; all three physical derivatives are supplied without theta error constants.")
    return output


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--helpers",type=Path,default=Path(__file__).with_name("winding_helpers.py"))
    parser.add_argument("--precision",type=int,default=192)
    parser.add_argument("--comparison",type=Path)
    parser.add_argument("--output",type=Path,required=True)
    args=parser.parse_args()
    result=run(args.helpers.resolve(),args.precision,
               args.comparison.resolve() if args.comparison is not None else None)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({"status":result["status"],"output":str(args.output),"checks":len(result["checks"])}))


if __name__=="__main__":
    main()
