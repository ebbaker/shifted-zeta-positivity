"""HDA-R05-N01 exact-Fraction gamma certificates; no research runs on import.

Prepared for Edward Baker with substantial LLM assistance, gpt-6.1-sol,
reasoning effort ultra, 26 October 2026.  Formula sources: recurrence
Notes09--11, especially Note10 C1--7; DLMF 5.11(i)--(ii).

Replay checks exact finite arithmetic and the declared analytic premises;
it is not an independent proof of those classical premises or of Python.
"""
from __future__ import annotations

import argparse
from fractions import Fraction as F
from hashlib import sha256
import json
import math
from pathlib import Path
import resource
import sys
import time

MODEL = {"author": "Edward Baker", "assistance": "gpt-6.1-sol",
         "effort": "ultra", "date": "2026-10-26"}
CAPS = {"gamma_terms_plus_shifts": 4096, "scalar_series_terms": 4096,
        "primitive_requested_bits": 8192}
SCHEMA = "HDA-R05-N01-gamma-v1"
_METRICS = None


class CertificateError(ValueError):
    pass


def require(test, message):
    if not test:
        raise CertificateError(message)


def _finite_json(value):
    if isinstance(value, float):
        require(math.isfinite(value), "nonfinite certificate metadata")
    elif isinstance(value, dict):
        for item in value.values():
            _finite_json(item)
    elif isinstance(value, (list, tuple)):
        for item in value:
            _finite_json(item)


class Metrics:
    def __init__(self):
        self.values = {"max_observed_fraction_numerator_bits": 0,
                       "max_observed_fraction_denominator_bits": 0,
                       "primitive_requested_bits_max": 0,
                       "scalar_series_terms_total": 0,
                       "scalar_series_terms_max": 0,
                       "complex_log_calls": 0,
                       "coefficient_terms": 0}

    def see(self, x):
        x = F(x)
        self.values["max_observed_fraction_numerator_bits"] = max(
            self.values["max_observed_fraction_numerator_bits"],
            abs(x.numerator).bit_length())
        self.values["max_observed_fraction_denominator_bits"] = max(
            self.values["max_observed_fraction_denominator_bits"],
            x.denominator.bit_length())
        return x


def obs(x):
    return _METRICS.see(x) if _METRICS is not None else F(x)


def enc(x):
    x = F(x)
    return f"{x.numerator}/{x.denominator}"


def dec(x):
    require(isinstance(x, str), "rational field must be a string")
    return obs(F(x))


def cenc(z):
    return [enc(z[0]), enc(z[1])]


def cdec(z):
    require(isinstance(z, list) and len(z) == 2, "bad complex pair")
    return dec(z[0]), dec(z[1])


def ca(z, w):
    return obs(z[0] + w[0]), obs(z[1] + w[1])


def cs(z, a):
    return obs(z[0] * a), obs(z[1] * a)


def cm(z, w):
    a, b, c, d = z[0], z[1], w[0], w[1]
    ac, bd, ad, bc = obs(a*c), obs(b*d), obs(a*d), obs(b*c)
    return obs(ac-bd), obs(ad+bc)


def ci(z):
    denominator = obs(obs(z[0]*z[0]) + obs(z[1]*z[1]))
    require(denominator > 0, "zero reciprocal denominator")
    return obs(z[0]/denominator), obs(-z[1]/denominator)


def cabs1(z):
    return obs(abs(z[0]) + abs(z[1]))


def grid(tolerance):
    require(tolerance > 0, "nonpositive tolerance")
    bits, step = 0, F(1)
    while step > tolerance:
        bits += 1
        require(bits <= CAPS["primitive_requested_bits"],
                "primitive requested-bit cap reached")
        step /= 2
    if _METRICS is not None:
        _METRICS.values["primitive_requested_bits_max"] = max(
            _METRICS.values["primitive_requested_bits_max"], bits)
    return bits, obs(step)


def nearest(x, bits):
    require(isinstance(bits, int) and 0 <= bits <= CAPS["primitive_requested_bits"],
            "dyadic precision cap")
    if _METRICS is not None:
        _METRICS.values["primitive_requested_bits_max"] = max(
            _METRICS.values["primitive_requested_bits_max"], bits)
    n, r = divmod(x.numerator << bits, x.denominator)
    if 2*r > x.denominator or (2*r == x.denominator and n & 1):
        n += 1
    result = obs(F(n, 1 << bits))
    require(abs(result-x) <= F(1, 1 << (bits+1)), "rounding failed")
    return result


def upper_grid(x, bits):
    require(isinstance(bits, int) and 0 <= bits <= CAPS["primitive_requested_bits"],
            "dyadic radius precision cap")
    if _METRICS is not None:
        _METRICS.values["primitive_requested_bits_max"] = max(
            _METRICS.values["primitive_requested_bits_max"], bits)
    n, r = divmod(x.numerator << bits, x.denominator)
    return obs(F(n + bool(r), 1 << bits))


def cq(z, bits):
    result = nearest(z[0], bits), nearest(z[1], bits)
    require(cabs1(ca(result, cs(z, -1))) <= F(1, 1 << bits),
            "complex dyadic rounding failed")
    return result


def _series(kind, t, terms):
    require(0 <= terms <= CAPS["scalar_series_terms"], "series term cap")
    require(abs(t) <= (F(1, 3) if kind == "log" else F(1, 2)),
            "series argument outside certified disk")
    total, power, square = F(0), t, obs(t*t)
    for j in range(terms):
        term = obs(power / (2*j+1))
        total = obs(total + (term if kind == "log" or j % 2 == 0 else -term))
        power = obs(power*square)
    if kind == "log":
        total = obs(2*total)
        tail = obs(2*abs(power)/((2*terms+1)*(1-square)))
    else:
        tail = obs(abs(power)/(2*terms+1))
    if _METRICS is not None:
        _METRICS.values["scalar_series_terms_total"] += terms
        _METRICS.values["scalar_series_terms_max"] = max(
            _METRICS.values["scalar_series_terms_max"], terms)
    return total, tail


def _choose_series(kind, t, tolerance):
    square, power, terms = obs(t*t), abs(t), 0
    while True:
        tail = (2*power/((2*terms+1)*(1-square)) if kind == "log"
                else power/(2*terms+1))
        obs(tail)
        if tail <= tolerance:
            return terms
        terms += 1
        require(terms <= CAPS["scalar_series_terms"], "scalar series cap")
        power = obs(power*square)


def _log_reduction(x):
    require(x > 0, "positive logarithm input required")
    k, y = 0, x
    while y < 1:
        y = obs(y*2)
        k -= 1
    while y >= 2:
        y = obs(y/2)
        k += 1
    return k, obs((y-1)/(y+1))


def log_positive(x, tolerance):
    k, t = _log_reduction(x)
    local = obs(tolerance/(16*(1+abs(k))))
    my = _choose_series("log", t, local)
    m2 = _choose_series("log", F(1, 3), local) if k else 0
    sy, ry = _series("log", t, my)
    s2, r2 = _series("log", F(1, 3), m2) if k else (F(0), F(0))
    partial, tail = obs(sy+k*s2), obs(ry+abs(k)*r2)
    bits, step = grid(tolerance/16)
    value = nearest(partial, bits)
    radius = upper_grid(obs(tail+abs(value-partial)), bits)
    require(radius <= tolerance, "log delivery bound")
    cert = {"kind": "positive_log", "x": enc(x), "tolerance": enc(tolerance),
            "k": k, "terms_y": my, "terms_2": m2, "bits": bits,
            "value": enc(value), "radius": enc(radius)}
    return value, radius, cert


def replay_log_positive(cert):
    require(cert["kind"] == "positive_log", "wrong log certificate")
    x, tolerance = dec(cert["x"]), dec(cert["tolerance"])
    k, t = _log_reduction(x)
    require(k == cert["k"], "log range-reduction mismatch")
    sy, ry = _series("log", t, cert["terms_y"])
    if k:
        s2, r2 = _series("log", F(1, 3), cert["terms_2"])
    else:
        require(cert["terms_2"] == 0, "unused log2 terms")
        s2, r2 = F(0), F(0)
    partial, tail = obs(sy+k*s2), obs(ry+abs(k)*r2)
    bits = cert["bits"]
    require(0 <= bits <= CAPS["primitive_requested_bits"], "log bits cap")
    value, radius = dec(cert["value"]), dec(cert["radius"])
    require(value == nearest(partial, bits), "log dyadic value mismatch")
    require(radius == upper_grid(tail+abs(value-partial), bits),
            "log radius mismatch")
    require(0 <= radius <= tolerance, "log tail/delivery inequality")
    return value, radius


def _atan_terms(t):
    """Finite exact angle identities; every returned argument is <=1/2."""
    sign = -1 if t < 0 else 1
    t = abs(t)
    terms = []
    if t > 1:
        terms.extend([(2*sign, F(1, 2)), (2*sign, F(1, 3))])
        sign = -sign
        t = obs(1/t)
    if t > F(1, 2):
        terms.append((sign, F(1, 2)))
        t = obs((t-F(1, 2))/(1+t/2))
    if t:
        terms.append((sign, t))
    return terms


def atan_linear(terms, tolerance, kind="atan", argument=None):
    total_coeff = sum(abs(c) for c, _ in terms)
    local = obs(tolerance/(16*(1+total_coeff)))
    partial, tail, witnesses = F(0), F(0), []
    for coefficient, argument_i in terms:
        count = _choose_series("atan", argument_i, local)
        s, r = _series("atan", argument_i, count)
        partial = obs(partial+coefficient*s)
        tail = obs(tail+abs(coefficient)*r)
        witnesses.append({"coefficient": coefficient, "argument": enc(argument_i),
                          "terms": count})
    bits, step = grid(tolerance/16)
    value = nearest(partial, bits)
    radius = upper_grid(obs(tail+abs(value-partial)), bits)
    require(radius <= tolerance, "atan delivery inequality")
    cert = {"kind": kind, "tolerance": enc(tolerance), "witnesses": witnesses,
            "bits": bits, "value": enc(value), "radius": enc(radius)}
    if argument is not None:
        cert["argument"] = enc(argument)
    return value, radius, cert


def replay_atan(cert):
    kind, tolerance = cert["kind"], dec(cert["tolerance"])
    if kind == "pi":
        expected = [(4, F(1, 2)), (4, F(1, 3))]
    else:
        require(kind == "atan", "wrong angle certificate")
        expected = _atan_terms(dec(cert["argument"]))
    actual = [(w["coefficient"], dec(w["argument"])) for w in cert["witnesses"]]
    require(actual == expected, "angle identity/reduction mismatch")
    partial, tail = F(0), F(0)
    for (coefficient, argument), witness in zip(actual, cert["witnesses"]):
        s, r = _series("atan", argument, witness["terms"])
        partial = obs(partial+coefficient*s)
        tail = obs(tail+abs(coefficient)*r)
    bits = cert["bits"]
    require(0 <= bits <= CAPS["primitive_requested_bits"], "atan bits cap")
    value, radius = dec(cert["value"]), dec(cert["radius"])
    require(value == nearest(partial, bits), "angle dyadic value mismatch")
    require(radius == upper_grid(tail+abs(value-partial), bits),
            "angle radius mismatch")
    require(0 <= radius <= tolerance, "angle tail/delivery inequality")
    return value, radius


def complex_log(z, tolerance):
    require(z[0] > 0, "complex Log requires positive real part")
    if _METRICS is not None:
        _METRICS.values["complex_log_calls"] += 1
    real, rr, rc = log_positive(obs(z[0]*z[0]+z[1]*z[1]), tolerance/4)
    argument = obs(z[1]/z[0])
    imag, ri, ic = atan_linear(_atan_terms(argument), tolerance/4,
                              argument=argument)
    bits, step = grid(tolerance/16)
    value = cq((obs(real/2), imag), bits)
    qerr = cabs1(ca(value, cs((real/2, imag), -1)))
    radius = upper_grid(obs(rr/2+ri+qerr), bits)
    require(radius <= tolerance, "complex log delivery inequality")
    cert = {"kind": "complex_log", "z": cenc(z), "tolerance": enc(tolerance),
            "real_log": rc, "angle": ic, "bits": bits,
            "value": cenc(value), "radius": enc(radius)}
    return value, radius, cert


def replay_complex_log(cert):
    require(cert["kind"] == "complex_log", "wrong complex-log certificate")
    z, tolerance = cdec(cert["z"]), dec(cert["tolerance"])
    require(z[0] > 0, "unseparated complex-log branch")
    require(dec(cert["real_log"]["x"]) == z[0]*z[0]+z[1]*z[1],
            "complex-log modulus argument")
    require(cert["angle"]["kind"] == "atan", "complex-log angle must certify atan")
    require(dec(cert["angle"]["argument"]) == z[1]/z[0],
            "complex-log angle argument")
    real, rr = replay_log_positive(cert["real_log"])
    imag, ri = replay_atan(cert["angle"])
    bits = cert["bits"]
    require(0 <= bits <= CAPS["primitive_requested_bits"], "complex-log bits cap")
    raw = (real/2, imag)
    value = cq(raw, bits)
    radius = upper_grid(rr/2+ri+cabs1(ca(value, cs(raw, -1))), bits)
    require(value == cdec(cert["value"]), "complex-log value mismatch")
    require(radius == dec(cert["radius"]) and radius <= tolerance,
            "complex-log error inequality")
    return value, radius


def log_2pi(epsilon):
    pi, rp, pc = atan_linear([(4, F(1, 2)), (4, F(1, 3))], epsilon/256,
                             kind="pi")
    require(pi-rp > 3, "pi lower separation")
    value, rv, lc = log_positive(obs(2*pi), epsilon/256)
    bits, step = grid(epsilon/1024)
    radius = upper_grid(obs(rv+rp/(pi-rp)), bits)
    require(radius <= epsilon/32, "log2pi error inequality")
    return value, radius, {"kind": "log_2pi", "pi": pc, "log": lc,
                           "bits": bits, "value": enc(value),
                           "radius": enc(radius)}


def replay_log_2pi(cert, epsilon):
    require(cert["kind"] == "log_2pi", "wrong log2pi certificate")
    require(cert["pi"]["kind"] == "pi", "log2pi must use a pi certificate")
    pi, rp = replay_atan(cert["pi"])
    require(pi-rp > 3, "pi denominator separation")
    require(dec(cert["log"]["x"]) == 2*pi, "log2pi input mismatch")
    value, rv = replay_log_positive(cert["log"])
    bits = cert["bits"]
    require(0 <= bits <= CAPS["primitive_requested_bits"], "log2pi bits cap")
    radius = upper_grid(rv+rp/(pi-rp), bits)
    require(value == dec(cert["value"]), "log2pi value mismatch")
    require(radius == dec(cert["radius"]) and radius <= epsilon/32,
            "log2pi radius inequality")
    return value, radius


def bernoulli_table(degree):
    values = [F(1)]
    for n in range(1, degree+1):
        total = F(0)
        for k, value in enumerate(values):
            total = obs(total+obs(math.comb(n+1, k)*value))
        values.append(obs(-total/(n+1)))
    return values


def bernoulli_digest(values):
    return sha256("\n".join(map(enc, values)).encode("ascii")).hexdigest()


def _assemble(u, J, P, logw, logw_radius, shiftlogs, l2pi, l2pi_radius,
              bernoulli, bits):
    epsilon, m = F(1, 1 << P), P+2*J+4
    a, W = m+1, (F(m+1)+F(1, 4), obs(u/4))
    wpowers = [(F(1), F(0))]
    inverse = ci(W)
    for _ in range(2*m+J):
        wpowers.append(cm(wpowers[-1], inverse))
    jets, primitive_error, counts = [], [], []
    for j in range(J+1):
        if j == 0:
            term = ca(cm(ca(W, (F(-1, 2), F(0))), logw),
                      ca(cs(W, -1), (l2pi/2, F(0))))
            err = obs(cabs1(ca(W, (F(-1, 2), F(0))))*logw_radius+l2pi_radius/2)
        elif j == 1:
            lj = wpowers[1]
            term = ca(cm(ca(W, (F(-1, 2), F(0))), lj),
                      ca(logw, (F(-1), F(0))))
            err = logw_radius
        else:
            lj = cs(wpowers[j], F((-1)**(j-1), j))
            lp = cs(wpowers[j-1], F((-1)**(j-2), j-1))
            term = ca(cm(ca(W, (F(-1, 2), F(0))), lj), lp)
            err = F(0)
        jets.append(cq(term, bits)); primitive_error.append(err); counts.append(1)
    for k in range(1, m):
        coefficient = obs(bernoulli[2*k]/(2*k*(2*k-1)))
        for j in range(J+1):
            term = cs(wpowers[2*k+j-1],
                      obs(coefficient*((-1)**j)*math.comb(2*k+j-2, j)))
            jets[j] = ca(jets[j], cq(term, bits)); counts[j] += 1
    for h in range(a):
        value, radius = shiftlogs[h]
        jets[0] = ca(jets[0], cq(cs(value, -1), bits)); counts[0] += 1
        primitive_error[0] = obs(primitive_error[0]+radius)
        power, inverse_h = (F(1), F(0)), ci((F(1, 4)+h, u/4))
        for j in range(1, J+1):
            power = cm(power, inverse_h)
            term = cs(power, F((-1)**j, j))
            jets[j] = ca(jets[j], cq(term, bits)); counts[j] += 1
    channels = []
    step = F(1, 1 << bits)
    for j, value in enumerate(jets):
        analytic = obs(F(8**j, (4**m)*m))
        rounding = obs(counts[j]*step)
        radius = upper_grid(obs(analytic+primitive_error[j]+rounding), bits)
        require(analytic <= epsilon/256, "C4 analytic remainder inequality")
        require(radius <= epsilon, "gamma delivery inequality")
        channels.append({"j": j, "value": cenc(value), "radius": enc(radius),
                         "analytic_radius": enc(analytic),
                         "primitive_radius": enc(primitive_error[j]),
                         "rounding_radius": enc(rounding), "term_count": counts[j]})
    if _METRICS is not None:
        _METRICS.values["coefficient_terms"] = sum(counts)
    return channels


def _measure_end(start, metrics):
    usage = resource.getrusage(resource.RUSAGE_SELF)
    peak = usage.ru_maxrss * (1 if sys.platform == "darwin" else 1024)
    result = dict(metrics.values)
    observed = max(result["max_observed_fraction_numerator_bits"],
                   result["max_observed_fraction_denominator_bits"])
    result.update({"elapsed_seconds": time.perf_counter()-start,
                   "peak_rss_bytes_process_lifetime": peak,
                   "conservative_fraction_raw_crossproduct_bits": 2*observed+2,
                   "measurement_scope": "Instrumented Fraction results and powers; "
                   "Fraction/gcd internal transient objects are not directly measured. "
                   "The raw crossproduct bound is conservative, not a measurement."})
    return result


def run_case(u, J, P):
    """Produce a JSON-serializable finite certificate; no external backend."""
    global _METRICS
    start, metrics = time.perf_counter(), Metrics()
    _METRICS = metrics
    try:
        require(isinstance(J, int) and not isinstance(J, bool) and
                isinstance(P, int) and not isinstance(P, bool), "integer J/P required")
        u = obs(F(u))
        require(u > 0 and J >= 0 and P >= 1, "invalid gamma input")
        m = P+2*J+4
        a = m+1
        require(a+m-1 <= CAPS["gamma_terms_plus_shifts"], "gamma term/shift cap")
        epsilon = F(1, 1 << P)
        W = (F(a)+F(1, 4), u/4)
        upper_w = obs(cabs1(W)+1)
        logw, rw, cw = complex_log(W, epsilon/(64*(1+upper_w)))
        l2p, r2p, c2p = log_2pi(epsilon)
        shift_data, shift_certificates = [], []
        for h in range(a):
            value, radius, witness = complex_log((F(h)+F(1, 4), u/4),
                                                epsilon/(64*a))
            shift_data.append((value, radius)); shift_certificates.append(witness)
        bernoulli = bernoulli_table(2*m-2)
        bits, step = grid(epsilon/(256*(a+m+J+10)))
        jets = _assemble(u, J, P, logw, rw, shift_data, l2p, r2p, bernoulli, bits)
        return {"schema": SCHEMA, "metadata": MODEL, "input": {"u": enc(u), "J": J, "P": P},
                "caps": CAPS, "m": m, "a": a, "gamma_terms_plus_shifts": a+m-1,
                "dyadic_fraction_bits": bits, "bernoulli_degree": 2*m-2,
                "bernoulli_sha256": bernoulli_digest(bernoulli),
                "log_W": cw, "log_2pi": c2p, "shift_logs": shift_certificates,
                "jets": jets, "metrics": _measure_end(start, metrics),
                "premises": ["Note10 C1-C7 and DLMF5.11 finite remainder",
                             "Note09 P5 and arctangent alternating-series tails",
                             "Right-half-plane analytic log Gamma branch"],
                "cap_interpretation": "4096 gamma expansion terms plus recurrence shifts; "
                "aggregate underlying elementary-series terms are reported separately"}
    finally:
        _METRICS = None


def replay_case(cert):
    """Check actual witnesses and finite inequalities, without producer refinement."""
    global _METRICS
    start, metrics = time.perf_counter(), Metrics()
    _METRICS = metrics
    try:
        _finite_json(cert)
        require(cert["schema"] == SCHEMA, "unknown gamma schema")
        require(cert["metadata"] == MODEL, "certificate provenance metadata mismatch")
        require(cert["caps"] == CAPS, "caps differ from frozen packet")
        u, J, P = dec(cert["input"]["u"]), cert["input"]["J"], cert["input"]["P"]
        require(isinstance(J, int) and not isinstance(J, bool) and
                isinstance(P, int) and not isinstance(P, bool) and u > 0 and J >= 0 and P >= 1,
                "invalid replay input")
        m, a = P+2*J+4, P+2*J+5
        require(cert["m"] == m and cert["a"] == a, "C1 parameter mismatch")
        require(cert["gamma_terms_plus_shifts"] == a+m-1 <= CAPS["gamma_terms_plus_shifts"],
                "gamma term/shift cap mismatch")
        require(len(cert["shift_logs"]) == a, "missing shift logarithms")
        epsilon = F(1, 1 << P)
        expected_w = (F(a)+F(1, 4), u/4)
        require(cdec(cert["log_W"]["z"]) == expected_w, "wrong shifted gamma argument")
        logw, rw = replay_complex_log(cert["log_W"])
        l2p, r2p = replay_log_2pi(cert["log_2pi"], epsilon)
        shifts = []
        for h, witness in enumerate(cert["shift_logs"]):
            require(cdec(witness["z"]) == (F(h)+F(1, 4), u/4), "shift argument mismatch")
            shifts.append(replay_complex_log(witness))
        bernoulli = bernoulli_table(2*m-2)
        require(cert["bernoulli_degree"] == 2*m-2 and
                cert["bernoulli_sha256"] == bernoulli_digest(bernoulli),
                "Bernoulli recurrence/digest mismatch")
        bits = cert["dyadic_fraction_bits"]
        require(0 <= bits <= CAPS["primitive_requested_bits"], "gamma dyadic bits cap")
        channels = _assemble(u, J, P, logw, rw, shifts, l2p, r2p, bernoulli, bits)
        require(channels == cert["jets"], "gamma coefficient/error replay mismatch")
        return {"ok": True, "schema": SCHEMA, "input": cert["input"],
                "jet_count": J+1, "maximum_radius": enc(max(dec(x["radius"]) for x in channels)),
                "checks": ["positive log branch", "exact range reductions and series tails",
                           "dyadic rounding", "pi separation", "Bernoulli recurrence",
                           "shifted coefficient formulas", "C4 remainder", "all jet delivery bounds"],
                "metrics": _measure_end(start, metrics)}
    finally:
        _METRICS = None


def certificate_args(cert):
    """Bind worker arguments to the same exact input used by replay_case."""
    require(cert.get("schema") == SCHEMA, "unknown gamma schema")
    data = cert["input"]
    u, J, P = F(data["u"]), data["J"], data["P"]
    require(isinstance(J, int) and not isinstance(J, bool) and
            isinstance(P, int) and not isinstance(P, bool) and
            u > 0 and J >= 0 and P >= 1, "invalid mathematical case input")
    return [u.numerator if u.denominator == 1 else enc(u), J, P]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--u", default="1")
    parser.add_argument("--J", type=int, default=0)
    parser.add_argument("--P", type=int, default=32)
    parser.add_argument("--replay", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = replay_case(json.loads(args.replay.read_text())) if args.replay else run_case(args.u, args.J, args.P)
    content = json.dumps(result, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n"
    if args.output:
        args.output.write_text(content)
    else:
        sys.stdout.write(content)


if __name__ == "__main__":
    main()
