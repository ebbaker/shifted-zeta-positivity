"""HDA-R05-N01 r1: exact Legendre/Gauss provider, not an RH evaluator.

Prepared for Edward Baker with LLM assistance: gpt-6.1-sol, ultra.
run_case(s, P) returns a JSON-serializable finite certificate.  Importing this
module does not execute a research case.  All mathematical operations use
integers/Fraction; floats occur only in elapsed-time measurements.

Recorded stopping refinement: C8--C14 Sturm isolation and C13 weights are
unchanged.  Exact interval J/P' certificates allow stopping before the very
conservative global C12 depth.  Note09's interval-provider argument justifies
this refinement.  The global depth is retained as diagnostic metadata.
"""

from fractions import Fraction as F
from math import comb, factorial
import json
import resource
import sys
import time

MAX_DEPTH = 8192
MAX_SIGN_QUERIES = 250000
SCHEMA = "hda-r05-n01-gauss-v1"
INTERVALS = ((F(-1), F(1)), (F(0), F(1, 2)),
             (F(3, 8), F(3, 8) + F(1, 4096)))


def enc(x):
    x = F(x)
    return {"n": hex(x.numerator), "d": hex(x.denominator)}


def certificate_args(cert):
    """Mathematical inputs bound to the precision target, not label metadata."""
    s, p = cert["input"]["s"], cert["input"]["P"]
    if type(s) is not int or type(p) is not int or s < 1 or p < 1:
        raise ValueError("invalid mathematical input")
    if _dec(cert["target_base_node_and_total_weight_error"]) != F(1, 1 << p):
        raise ValueError("precision/target mismatch")
    return [s, p]


class Tracking:
    def __init__(self):
        self.sign_queries = 0
        self.integer_recurrence_steps = 0
        self.max_depth = 0
        self.max_integer_bits = 0
        self.max_fraction_numden_bits = 0

    def note(self, x):
        if isinstance(x, F):
            self.max_fraction_numden_bits = max(
                self.max_fraction_numden_bits,
                abs(x.numerator).bit_length(), x.denominator.bit_length())
        elif isinstance(x, int):
            self.max_integer_bits = max(self.max_integer_bits,
                                        abs(x).bit_length())
        return x


def _mul(a, b, tr):
    return tr.note(a * b)


def _add(a, b, tr):
    return tr.note(a + b)


def _ival_mul(a, b, tr):
    vals = [_mul(x, y, tr) for x in a for y in b]
    return min(vals), max(vals)


def _ival_poly(coeff, x, tr):
    ans = (F(0), F(0))
    for c in reversed(coeff):
        ans = _ival_mul(ans, x, tr)
        ans = (_add(ans[0], c, tr), _add(ans[1], c, tr))
    return ans


def _ival_div(a, b, tr):
    if b[0] <= 0 <= b[1]:
        return None
    inv = (tr.note(1 / b[1]), tr.note(1 / b[0]))
    return _ival_mul(a, inv, tr)


def _eval(coeff, x, tr):
    ans = F(0)
    for c in reversed(coeff):
        ans = _add(_mul(ans, x, tr), c, tr)
    return ans


def _polynomials(s, tr):
    # A_s = (d/dx)^s (x^2-1)^s = 2^s s! P_s.
    aa = [0] * (s + 1)
    for j in range((s + 1) // 2, s + 1):
        aa[2*j-s] = tr.note(((-1) ** (s-j)) * comb(s, j)
                           * (factorial(2*j) // factorial(2*j-s)))
    scale = (1 << s) * factorial(s)
    pp = [tr.note(F(c, scale)) for c in aa]
    dp = [tr.note(j * pp[j]) for j in range(1, s + 1)]
    # Q_s = s! integral [A_s(t)-A_s(a)]/(t-a) dt.
    qq = [0] * s
    sf = factorial(s)
    for r in range(s):
        qq[r] = tr.note(sum(2 * aa[j] * (sf // (j-r))
                            for j in range(r+1, s+1)
                            if (j-r) % 2 == 1))
    jj = [tr.note(F(c, sf * scale)) for c in qq]
    return aa, pp, dp, qq, jj


def _depth_for_width(delta):
    # Exact smallest h>=0 with 2^(1-h)<=delta; no floating logarithm.
    h = max(0, delta.denominator.bit_length()
            - abs(delta.numerator).bit_length())
    while F(2, 1 << h) > delta:
        h += 1
    while h and F(2, 1 << (h-1)) <= delta:
        h -= 1
    return h


def _global_depth(s, target, pp, jj, tr):
    lead_a = factorial(2*s) // factorial(s)
    sigma = tr.note(F(1, lead_a ** (2*s-1)
                     * (1 << (s*(s-1)))))
    dd = tr.note(pp[-1] * sigma ** (s-1))
    s1 = tr.note(sum(j * abs(pp[j]) for j in range(s+1)))
    s2 = tr.note(sum(j*(j-1) * abs(pp[j]) for j in range(s+1)))
    j0 = tr.note(sum(abs(c) for c in jj))
    j1 = tr.note(sum(j * abs(jj[j]) for j in range(s)))
    lw = tr.note(2*j1/dd + 4*j0*s2/(dd*dd))
    mu = tr.note(1 / (4 * max(F(1), 2*s*s1/dd)))
    delta = min(F(1, 8), sigma/4, dd/(4*max(F(1), s2)),
                target, target/(2*s*max(F(1), lw)),
                mu/(2*max(F(1), lw)))
    tr.note(delta)
    return {"depth": _depth_for_width(delta),
            "conditioning_visible_operand_bits": max(
                max(abs(v.numerator).bit_length(), v.denominator.bit_length())
                for v in (sigma, dd, s1, s2, j0, j1, lw, mu, delta)),
            "used_as_mandatory_stopping_depth": False}


def _variation(s, x, tr):
    if tr.sign_queries >= MAX_SIGN_QUERIES:
        raise RuntimeError("sign_query_cap")
    tr.sign_queries += 1
    c, q = x.numerator, x.denominator
    if q & (q-1):
        raise ValueError("Sturm points must be dyadic")
    b0, b1 = 1, tr.note(2*c)
    last = 1
    variations = 0
    if b1:
        sign = 1 if b1 > 0 else -1
        variations += sign != last
        last = sign
    if s == 1:
        return int(variations), b1 == 0
    q2 = tr.note(q*q)
    for k in range(1, s):
        t1 = tr.note(2*(2*k+1)*c*b1)
        t2 = tr.note(4*k*k*q2*b0)
        bn = tr.note(t1-t2)
        tr.integer_recurrence_steps += 1
        if bn:
            sign = 1 if bn > 0 else -1
            variations += sign != last
            last = sign
        b0, b1 = b1, bn
    return int(variations), b1 == 0


def _ceil_dyadic(x, bits):
    scale = 1 << bits
    return F((x.numerator*scale + x.denominator-1)
             // x.denominator, scale)


def _local_root_record(s, a, b, depth, va, vb, za, zb,
                       aa, dp, qq, jj, target, grid, tr):
    singleton = a == b
    xx = (a, b)
    deriv = _ival_poly(dp, xx, tr)
    if deriv[0] <= 0 <= deriv[1]:
        return None
    numerator = _ival_poly(jj, xx, tr)
    wi = _ival_div(numerator, deriv, tr)
    if wi is None or wi[0] <= 0:
        return None
    node = (a+b)/2
    da = [j*aa[j] for j in range(1, s+1)]
    den = _eval(da, node, tr)
    weight = tr.note(_eval(qq, node, tr)/(factorial(s)*den))
    rawerr = tr.note(max(abs(weight-wi[0]), abs(wi[1]-weight)))
    ne = (b-a)/2
    if ne > target/2 or rawerr > target/(2*s):
        return None
    we = _ceil_dyadic(rawerr, grid)
    if we > target/s or weight <= 0:
        return None
    return {"left": enc(a), "right": enc(b),
            "singleton": singleton, "depth": depth,
            "variations_left": va, "variations_right": vb,
            "left_is_root": za, "right_is_root": zb,
            "root_count_open": 0 if singleton else 1,
            "node": enc(node), "node_error": enc(ne),
            "weight": enc(weight),
            "derivative_interval": [enc(v) for v in deriv],
            "denominator_separation": enc(min(abs(v) for v in deriv)),
            "weight_interval": [enc(v) for v in wi],
            "weight_error": enc(we)}


def _dec(x):
    return F(int(x["n"], 0), int(x["d"], 0))


def _moments(nodes, weights, left, right, eu, ew, precision, tr):
    out = []
    powers = [F(1)] * len(nodes)
    mm = max(abs(left), abs(right))
    length = right-left
    for k in range(2*len(nodes)):
        approx = F(0)
        for w, v in zip(weights, powers):
            approx = _add(approx, _mul(w, v, tr), tr)
        expected = (right ** (k+1) - left ** (k+1))/(k+1)
        error = tr.note(abs(approx-expected))
        bound = ew if k == 0 else (
            ew*mm**k + length*k*mm**(k-1)*eu)
        out.append({"degree": k, "exact_integral": enc(expected),
                    "absolute_error_upper_dyadic": enc(
                        _ceil_dyadic(error, precision+16)),
                    "propagated_bound": enc(bound),
                    "within_propagated_bound": error <= bound})
        powers = [_mul(v, x, tr) for v, x in zip(powers, nodes)]
    return out


def run_case(s, P):
    """Deliver one bounded case; caller coordinates global 900s/512MiB caps."""
    if type(s) is not int or type(P) is not int or s < 1 or P < 1:
        raise ValueError("positive integer order and precision required")
    start = time.perf_counter()
    tr = Tracking()
    target = F(1, 1 << P)
    grid = P + (max(2, s)-1).bit_length() + 8
    cert = {"schema": SCHEMA, "input": {"s": s, "P": P},
            "metadata": {"model": "gpt-6.1-sol", "effort": "ultra",
                         "author": "Edward Baker",
                         "llm_assistance": True,
                         "python": sys.version.split()[0]},
            "limits": {"max_depth": MAX_DEPTH,
                       "max_sign_queries": MAX_SIGN_QUERIES},
            "algorithm": "C8-C14 integer Sturm/C13 rational weights",
            "stopping_refinement":
                "exact-local-interval-J-over-Pprime; Note09 interval provider",
            "target_base_node_and_total_weight_error": enc(target),
            "weight_radius_grid_bits": grid,
            "status": "running", "roots": [], "pending": [],
            "mapped_rules": []}
    aa, pp, dp, qq, jj = _polynomials(s, tr)
    cert["global_C12_reference"] = _global_depth(s, target, pp, jj, tr)
    cert["global_C12_reference"]["exceeds_depth_cap"] = (
        cert["global_C12_reference"]["depth"] > MAX_DEPTH)
    # (a,b,V(a),V(b),P_s(a)==0,P_s(b)==0,depth); endpoints known.
    active = [(F(-1), F(1), s, 0, False, False, 0)]
    done = []
    reason = None
    while active and reason is None:
        nxt = []
        for index, item in enumerate(active):
            a, b, va, vb, za, zb, depth = item
            tr.max_depth = max(tr.max_depth, depth)
            count = va-vb-int(zb)
            if count <= 0:
                raise AssertionError("nonpositive active count")
            record = None
            if count == 1:
                record = _local_root_record(
                    s, a, b, depth, va, vb, za, zb,
                    aa, dp, qq, jj, target, grid, tr)
            if record is not None:
                done.append(record)
                continue
            if depth >= MAX_DEPTH:
                reason = "depth_cap"
                nxt.extend(active[index:])
                break
            if tr.sign_queries >= MAX_SIGN_QUERIES:
                reason = "sign_query_cap"
                nxt.extend(active[index:])
                break
            mid = (a+b)/2
            vm, zm = _variation(s, mid, tr)
            child_depth = depth+1
            tr.max_depth = max(tr.max_depth, child_depth)
            if zm:
                sr = _local_root_record(
                    s, mid, mid, child_depth, vm, vm, True, True,
                    aa, dp, qq, jj, target, grid, tr)
                if sr is None:
                    raise AssertionError("exact root lacks positive weight")
                done.append(sr)
            lc, rc = va-vm-int(zm), vm-vb-int(zb)
            if lc < 0 or rc < 0 or lc+rc+int(zm) != count:
                raise AssertionError("Sturm split count mismatch")
            if lc:
                nxt.append((a, mid, va, vm, za, zm, child_depth))
            if rc:
                nxt.append((mid, b, vm, vb, zm, zb, child_depth))
        active = nxt
    done.sort(key=lambda rr: _dec(rr["node"]))
    cert["roots"] = done
    if reason:
        cert["status"] = "capped"
        cert["stop_reason"] = reason
        cert["pending"] = [
            {"left": enc(a), "right": enc(b), "depth": depth,
             "root_count_open": va-vb-int(zb),
             "variations_left": va, "variations_right": vb,
             "left_is_root": za, "right_is_root": zb}
            for a, b, va, vb, za, zb, depth in active]
    else:
        if len(done) != s:
            raise AssertionError("wrong number of delivered roots")
        nodes = [_dec(r["node"]) for r in done]
        weights = [_dec(r["weight"]) for r in done]
        eu = max(_dec(r["node_error"]) for r in done)
        ew = sum((_dec(r["weight_error"]) for r in done), F(0))
        if eu > target or ew > target:
            raise AssertionError("base delivery tolerance failed")
        cert["base_max_node_error"] = enc(eu)
        cert["base_total_weight_error"] = enc(ew)
        diag_ok = True
        for left, right in INTERVALS:
            hh, cc = (right-left)/2, (right+left)/2
            nn = [tr.note(cc+hh*x) for x in nodes]
            ww = [tr.note(hh*w) for w in weights]
            du, dw = hh*eu, hh*ew
            diagnostics = _moments(nn, ww, left, right, du, dw, P, tr)
            diag_ok = diag_ok and all(d["within_propagated_bound"]
                                      for d in diagnostics)
            cert["mapped_rules"].append({
                "left": enc(left), "right": enc(right),
                "nodes": [enc(v) for v in nn],
                "weights": [enc(v) for v in ww],
                "max_node_error": enc(du),
                "total_weight_error": enc(dw),
                "requested_mapped_node_error": enc(hh*target),
                "requested_mapped_total_weight_error": enc(hh*target),
                "diagnostic_label":
                    "moment consistency; shares exact Gauss premises",
                "moment_diagnostics": diagnostics})
        cert["status"] = "pass" if diag_ok else "failure"
        if not diag_ok:
            cert["stop_reason"] = "polynomial_moment_diagnostic_mismatch"
    usage = resource.getrusage(resource.RUSAGE_SELF)
    rss = int(usage.ru_maxrss) * (1 if sys.platform == "darwin" else 1024)
    cert["stats"] = {
        "elapsed_seconds": time.perf_counter()-start,
        "sign_count_queries": tr.sign_queries,
        "integer_recurrence_steps": tr.integer_recurrence_steps,
        "max_isolation_depth": tr.max_depth,
        "tracked_max_integer_bits": tr.max_integer_bits,
        "tracked_max_fraction_numden_bits": tr.max_fraction_numden_bits,
        "operand_measurement":
            "visible exact operands/results, not Python hidden temporaries",
        "peak_rss_bytes": rss,
        "rss_measurement":
            "getrusage process-lifetime high-water; not case-exclusive",
        "primitive_series_terms": 0,
        "primitive_internal_bits": 0}
    return cert


def replay_case(cert):
    """Harness-compatible dispatch to the separate, independently coded replay."""
    import importlib.util
    from pathlib import Path
    location = Path(__file__).with_name("gauss_replay.py")
    spec = importlib.util.spec_from_file_location("hda_n01_gauss_replay", location)
    if spec is None or spec.loader is None:
        raise RuntimeError("independent Gauss replay module is unavailable")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.replay_case(cert)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--order", type=int, required=True)
    parser.add_argument("--precision", type=int, required=True)
    parser.add_argument("--output")
    args = parser.parse_args()
    result = run_case(args.order, args.precision)
    data = json.dumps(result, sort_keys=True, separators=(",", ":"),
                      allow_nan=False) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as stream:
            stream.write(data)
    else:
        print(data, end="")
