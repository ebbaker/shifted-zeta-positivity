"""Independent exact replay for HDA-R05-N01 Gauss certificates.

Prepared for Edward Baker with LLM assistance: gpt-6.1-sol, ultra.
This module deliberately does not import gauss_provider.  It regenerates
Legendre coefficients from Rodrigues' formula and evaluates its entire sign
chain by Fraction Horner evaluation, independently of provider integer C10.
Moment diagnostics share the exact Gauss theorem and are consistency checks.
Timing/RSS/visible-bit measurements are observational, not mathematical proof.
"""

from fractions import Fraction
from math import factorial, comb, isfinite
import json
import sys

R = Fraction


class ReplayError(ValueError):
    pass


def need(condition, message):
    if not condition:
        raise ReplayError(message)


def readq(obj):
    need(isinstance(obj, dict) and set(obj) == {"n", "d"},
         "invalid rational encoding")
    need(type(obj["n"]) is str and type(obj["d"]) is str,
         "rational components must be strings")
    try:
        n, d = int(obj["n"], 0), int(obj["d"], 0)
    except (ValueError, TypeError) as error:
        raise ReplayError("invalid rational integer") from error
    need(d > 0 and hex(n) == obj["n"] and hex(d) == obj["d"],
         "noncanonical rational encoding")
    value = R(n, d)
    need(value.numerator == n and value.denominator == d,
         "unreduced rational encoding")
    return value


def _finite_tree(obj):
    if isinstance(obj, float):
        need(isfinite(obj), "nonfinite JSON number")
    elif isinstance(obj, list):
        for value in obj:
            _finite_tree(value)
    elif isinstance(obj, dict):
        for value in obj.values():
            _finite_tree(value)


def certificate_args(cert):
    try:
        s, p = cert["input"]["s"], cert["input"]["P"]
    except (KeyError, TypeError) as error:
        raise ReplayError("missing mathematical input") from error
    need(type(s) is int and type(p) is int and s >= 1 and p >= 1,
         "invalid order/precision")
    need(readq(cert["target_base_node_and_total_weight_error"]) == R(1, 2**p),
         "precision target does not bind P")
    return [s, p]


def _rod(k):
    ans = [R(0)] * (k+1)
    for j in range((k+1)//2, k+1):
        ans[2*j-k] = R((-1)**(k-j) * comb(k, j)
                       * factorial(2*j),
                       2**k * factorial(k) * factorial(2*j-k))
    return ans


def _point(poly, x):
    total = R(0)
    for value in poly[::-1]:
        total = total*x+value
    return total


def _interval(poly, a, b):
    lower = upper = R(0)
    for value in poly[::-1]:
        cross = (lower*a, lower*b, upper*a, upper*b)
        lower, upper = min(cross)+value, max(cross)+value
    return lower, upper


def _quotient(numer, denom):
    lo, hi = denom
    need(not (lo <= 0 <= hi), "unseparated derivative denominator")
    vals = tuple(x/y for x in numer for y in denom)
    return min(vals), max(vals)


def _chain(chain, x):
    signs = []
    zero = False
    for index, poly in enumerate(chain):
        value = _point(poly, x)
        if value:
            signs.append(1 if value > 0 else -1)
        if index == len(chain)-1:
            zero = value == 0
    changes = sum(a != b for a, b in zip(signs, signs[1:]))
    return changes, zero


def _ceil(value, bits):
    n, d = value.numerator * 2**bits, value.denominator
    return R((n+d-1)//d, 2**bits)


def _global_reference(s, p, pp, jj):
    a = factorial(2*s)//factorial(s)
    sigma = R(1, a**(2*s-1) * 2**(s*(s-1)))
    dd = pp[-1]*sigma**(s-1)
    s1 = sum(j*abs(c) for j, c in enumerate(pp))
    s2 = sum(j*(j-1)*abs(c) for j, c in enumerate(pp))
    j0 = sum(abs(c) for c in jj)
    j1 = sum(j*abs(c) for j, c in enumerate(jj))
    lw = 2*j1/dd+4*j0*s2/dd**2
    mu = 1/(4*max(R(1), 2*s*s1/dd))
    target = R(1, 2**p)
    delta = min(R(1, 8), sigma/4, dd/(4*max(R(1), s2)), target,
                target/(2*s*max(R(1), lw)), mu/(2*max(R(1), lw)))
    h = max(0, delta.denominator.bit_length()
            - abs(delta.numerator).bit_length())
    while R(2, 2**h) > delta:
        h += 1
    while h and R(2, 2**(h-1)) <= delta:
        h -= 1
    bits = max(max(abs(v.numerator).bit_length(), v.denominator.bit_length())
               for v in (sigma, dd, s1, s2, j0, j1, lw, mu, delta))
    return h, bits


def _mesh_and_ancestors(a, b, depth, singleton, split_nodes):
    need(type(depth) is int and 0 <= depth <= 8192, "invalid root depth")
    need(-1 <= a <= b <= 1, "root interval outside base domain")
    factor = R(2**depth, 2)
    j = (a+1)*factor
    need(j.denominator == 1, "left endpoint is not on depth mesh")
    if singleton:
        need(a == b and depth >= 1 and j.numerator % 2 == 1,
             "singleton is not a newly encountered midpoint")
        parent_index = (j.numerator-1)//2
        for level in range(depth):
            split_nodes.add((level, parent_index >> (depth-1-level)))
    else:
        need(a < b and b-a == R(2, 2**depth),
             "bracket width/depth mismatch")
        cell_index = j.numerator
        for level in range(depth):
            split_nodes.add((level, cell_index >> (depth-level)))


def _record(rec, chain, pp, dp, jj, s, p, grid, pending, split_nodes):
    a, b = readq(rec["left"]), readq(rec["right"])
    singleton = False if pending else rec["singleton"]
    need(type(singleton) is bool, "invalid singleton flag")
    _mesh_and_ancestors(a, b, rec["depth"], singleton, split_nodes)
    va, za = _chain(chain, a)
    vb, zb = _chain(chain, b)
    need(type(rec["variations_left"]) is int
         and type(rec["variations_right"]) is int
         and rec["variations_left"] == va
         and rec["variations_right"] == vb,
         "stored endpoint variations mismatch")
    need(type(rec["left_is_root"]) is bool
         and type(rec["right_is_root"]) is bool
         and rec["left_is_root"] == za and rec["right_is_root"] == zb,
         "stored exact endpoint-zero flags mismatch")
    count = va-vb-int(zb)
    if singleton:
        need(za and zb and rec["root_count_open"] == 0,
             "invalid exact singleton root")
        contribution = 1
    else:
        need(type(rec["root_count_open"]) is int
             and count == rec["root_count_open"] and count > 0,
             "open-interval root count mismatch")
        contribution = count
    if pending:
        return (a, b, False, contribution), None
    need(contribution == 1, "delivered bracket contains multiple roots")
    node = readq(rec["node"])
    ne = readq(rec["node_error"])
    weight = readq(rec["weight"])
    we = readq(rec["weight_error"])
    need(node == (a+b)/2 and ne == (b-a)/2, "node center/radius mismatch")
    deriv = _interval(dp, a, b)
    need(tuple(readq(v) for v in rec["derivative_interval"]) == deriv,
         "derivative interval mismatch")
    need(not (deriv[0] <= 0 <= deriv[1]), "derivative contains zero")
    need(readq(rec["denominator_separation"])
         == min(abs(v) for v in deriv) > 0, "bad denominator separation")
    wi = _quotient(_interval(jj, a, b), deriv)
    need(tuple(readq(v) for v in rec["weight_interval"]) == wi,
         "true-weight interval mismatch")
    need(weight == _point(jj, node)/_point(dp, node),
         "rational C13 weight mismatch")
    raw = max(abs(weight-wi[0]), abs(wi[1]-weight))
    need(we == _ceil(raw, grid), "weight-radius quantization mismatch")
    target = R(1, 2**p)
    need(wi[0] > 0 and weight > 0, "weight positivity failed")
    need(ne <= target/2 and raw <= target/(2*s) and 0 <= we <= target/s,
         "local delivery certificate failed")
    return (a, b, singleton, 1), (node, weight, ne, we)


def _diagnostics(record, nodes, weights, a, b, eu, ew, p):
    data = record["moment_diagnostics"]
    need(len(data) == 2*len(nodes), "missing polynomial-moment channels")
    need(record["diagnostic_label"]
         == "moment consistency; shares exact Gauss premises",
         "missing shared-premise diagnostic label")
    powers = [R(1)]*len(nodes)
    mm = max(abs(a), abs(b))
    for k, item in enumerate(data):
        need(type(item["degree"]) is int and item["degree"] == k,
             "moment degree mismatch")
        exact = (b**(k+1)-a**(k+1))/(k+1)
        val = sum(w*v for w, v in zip(weights, powers))
        err = abs(val-exact)
        bound = ew if k == 0 else ew*mm**k+(b-a)*k*mm**(k-1)*eu
        need(readq(item["exact_integral"]) == exact, "moment target mismatch")
        need(readq(item["absolute_error_upper_dyadic"])
             == _ceil(err, p+16), "moment error report mismatch")
        need(readq(item["propagated_bound"]) == bound,
             "moment propagated bound mismatch")
        need(type(item["within_propagated_bound"]) is bool
             and item["within_propagated_bound"] == (err <= bound),
             "moment consistency boolean mismatch")
        need(err <= bound, "polynomial-moment diagnostic failed")
        powers = [value*x for value, x in zip(powers, nodes)]


def replay_case(cert):
    """Validate exact proof data; raises ReplayError at first mismatch."""
    _finite_tree(cert)
    need(cert["schema"] == "hda-r05-n01-gauss-v1", "unknown schema")
    metadata = cert["metadata"]
    need(set(metadata) == {"model", "effort", "author", "llm_assistance", "python"}
         and metadata["model"] == "gpt-6.1-sol"
         and metadata["effort"] == "ultra"
         and metadata["author"] == "Edward Baker"
         and metadata["llm_assistance"] is True
         and metadata["python"] == sys.version.split()[0],
         "metadata or producer/replay Python-version mismatch")
    s, p = certificate_args(cert)
    need(cert["algorithm"] == "C8-C14 integer Sturm/C13 rational weights",
         "wrong algorithm declaration")
    need(cert["stopping_refinement"]
         == "exact-local-interval-J-over-Pprime; Note09 interval provider",
         "wrong stopping declaration")
    need(cert["limits"] == {"max_depth": 8192, "max_sign_queries": 250000},
         "limits changed")
    need(all(type(v) is int for v in cert["limits"].values()),
         "limits must have integer encoding")
    grid = p+(max(2, s)-1).bit_length()+8
    need(cert["weight_radius_grid_bits"] == grid, "radius grid mismatch")
    chain = [_rod(k) for k in range(s+1)]
    pp = chain[-1]
    dp = [j*pp[j] for j in range(1, s+1)]
    jj = [sum(2*pp[j]/(j-r) for j in range(r+1, s+1)
              if (j-r) % 2 == 1) for r in range(s)]
    ref_depth, ref_bits = _global_reference(s, p, pp, jj)
    ref = cert["global_C12_reference"]
    need(ref["depth"] == ref_depth
         and ref["conditioning_visible_operand_bits"] == ref_bits
         and ref["used_as_mandatory_stopping_depth"] is False
         and ref["exceeds_depth_cap"] == (ref_depth > 8192),
         "global conditioning diagnostic mismatch")
    regions, delivered, splits = [], [], set()
    for item in cert["roots"]:
        region, output = _record(item, chain, pp, dp, jj, s, p, grid,
                                 False, splits)
        regions.append(region)
        delivered.append(output)
    for item in cert["pending"]:
        region, _ = _record(item, chain, pp, dp, jj, s, p, grid,
                             True, splits)
        regions.append(region)
    regions.sort()
    for previous, current in zip(regions, regions[1:]):
        need(previous[1] <= current[0], "overlapping root regions")
        need(not (previous[2] and current[2]
                  and previous[0] == current[0]), "duplicated singleton")
    need(sum(region[3] for region in regions) == s,
         "root regions do not account for all s roots")
    stats = cert["stats"]
    need(type(stats["sign_count_queries"]) is int
         and stats["sign_count_queries"] == len(splits) <= 250000,
         "sign-query count not bound to subdivision tree")
    need(type(stats["integer_recurrence_steps"]) is int
         and stats["integer_recurrence_steps"] == (s-1)*len(splits),
         "integer recurrence operation count mismatch")
    depths = [r["depth"] for r in cert["roots"]+cert["pending"]]
    need(type(stats["max_isolation_depth"]) is int
         and stats["max_isolation_depth"] == max(depths, default=0) <= 8192,
         "isolation-depth measurement mismatch")
    for key in ("elapsed_seconds", "peak_rss_bytes", "tracked_max_integer_bits",
                "tracked_max_fraction_numden_bits"):
        need(type(stats[key]) in (int, float) and stats[key] >= 0,
             "invalid observational measurement")
    need(type(stats["primitive_series_terms"]) is int
         and type(stats["primitive_internal_bits"]) is int
         and stats["primitive_series_terms"] == 0
         and stats["primitive_internal_bits"] == 0,
         "Gauss provider should have no transcendental primitive")
    status = cert["status"]
    if status == "capped":
        need(cert["pending"] and not cert["mapped_rules"],
             "capped record has inconsistent completion fields")
        reason = cert["stop_reason"]
        need((reason == "depth_cap" and any(r["depth"] == 8192
                                            for r in cert["pending"]))
             or (reason == "sign_query_cap" and len(splits) == 250000),
             "unsubstantiated cap reason")
        return {"replay_status": "pass", "delivery_status": "capped",
                "delivered": False, "certificate_args": [s, p],
                "checked_root_records": len(delivered),
                "checked_pending_records": len(cert["pending"]),
                "checked_mapped_rules": 0,
                "observational_measurements_replayed": False}
    need(status == "pass" and not cert["pending"] and len(delivered) == s,
         "record does not assert a successful complete delivery")
    nodes, weights, en, ew = map(list, zip(*delivered))
    need(nodes == sorted(nodes), "base nodes are not sorted")
    eu, total_w = max(en), sum(ew)
    target = R(1, 2**p)
    need(readq(cert["base_max_node_error"]) == eu <= target
         and readq(cert["base_total_weight_error"]) == total_w <= target,
         "aggregate base delivery mismatch")
    intervals = ((R(-1), R(1)), (R(0), R(1, 2)),
                 (R(3, 8), R(3, 8)+R(1, 4096)))
    need(len(cert["mapped_rules"]) == len(intervals), "missing mapped rules")
    for record, (a, b) in zip(cert["mapped_rules"], intervals):
        need(readq(record["left"]) == a and readq(record["right"]) == b,
             "mapping endpoints changed")
        h, c = (b-a)/2, (b+a)/2
        nn = [c+h*x for x in nodes]
        ww = [h*w for w in weights]
        need([readq(v) for v in record["nodes"]] == nn
             and [readq(v) for v in record["weights"]] == ww,
             "mapped centers/weights mismatch")
        need(all(a < x < b for x in nn) and all(w > 0 for w in ww),
             "mapped geometry or positivity failed")
        need(readq(record["max_node_error"]) == h*eu <= h*target
             and readq(record["total_weight_error"]) == h*total_w <= h*target,
             "mapped delivered errors mismatch")
        need(readq(record["requested_mapped_node_error"]) == h*target
             and readq(record["requested_mapped_total_weight_error"]) == h*target,
             "mapped tolerance mismatch")
        _diagnostics(record, nn, ww, a, b, h*eu, h*total_w, p)
    return {"replay_status": "pass", "delivery_status": "pass",
            "delivered": True, "certificate_args": [s, p],
            "checked_root_records": s, "checked_pending_records": 0,
            "checked_mapped_rules": 3,
            "checked_moment_diagnostics": 6*s,
            "observational_measurements_replayed": False,
            "independence":
                "separate Rodrigues/Horner implementation; shared Gauss theorems"}


if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise SystemExit("usage: gauss_replay.py certificate.json")
    with open(sys.argv[1], encoding="utf-8") as stream:
        certificate = json.load(stream)
    print(json.dumps(replay_case(certificate), sort_keys=True, allow_nan=False))
