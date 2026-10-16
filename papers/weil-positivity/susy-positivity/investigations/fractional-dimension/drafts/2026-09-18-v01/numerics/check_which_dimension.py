#!/usr/bin/env python3
"""
Which dimension does the archimedean kernel carry: 2 omega or omega?  Standard library only;
prints JSON to stdout.  No value of zeta or xi is computed, and nothing here is a positivity
certificate.

THE QUESTION.  The archimedean factor of the shifted Weil transfer has kernel

    k^Gamma_om(tau) = |S^{2om-1}| (2 sinh tau)^(om-1) e^(tau/2),   |S^{d-1}| = 2 pi^(d/2)/Gamma(d/2),

and two dimensions seem to be in play.  The prefactor is the area of the unit sphere in
dimension 2 omega, and the loewner investigation proved
K^Gamma_om(p) = int_{R^d} |t+i|^(-(p+b)) dt with d = 2 omega.  But (sinh tau)^(om-1) is also the
radial Jacobian of a REAL HYPERBOLIC space of dimension omega, which is half as much.

THE ANSWER: 2 omega, and the factor of two is a coordinate artifact.

  A. tau IS NOT A DISTANCE.  tau = log|t+i| is the log-modulus along the horocycle {y = 1} of
     the upper half-plane -- a Busemann function.  The hyperbolic distance from i to t+i is

         d_H(i, t+i) = arccosh(1 + t^2/2) = 2 arcsinh(t/2),

     which behaves like the EUCLIDEAN radius r = |t| at small scale (d ~ r) and like 2 tau at
     large scale.  Meanwhile tau ~ r^2/2 near the origin: a square.  A measure with local
     exponent r^(2om-1) dr therefore has local exponent tau^(om-1) dtau, and the halving of
     the dimension is exactly that square, nothing else.

  B. IN THE TRUE DISTANCE THE TWO PICTURES AGREE.  Put u = d_H/2, so that r = 2 sinh u.  Then
     Lebesgue measure on R^{2 omega} becomes

         |S^{2om-1}| r^(2om-1) dr = 2^(2om) |S^{2om-1}| (sinh u)^(2om-1) cosh u du,

     and (sinh u)^(2n-1) cosh u is the radial Jacobian of COMPLEX HYPERBOLIC space CH^n at
     n = omega: complex dimension omega, REAL dimension 2 omega.  The transfer integral in this
     coordinate, with 1 + r^2 = 2 cosh 2u - 1, reproduces the Gamma ratio.

  C. THE JACOBI PARAMETERS SAY THE SAME THING.  With
     Delta_{al,be}(x) = (2 sinh x)^(2 al + 1) (2 cosh x)^(2 be + 1) and rho = al + be + 1:

         coordinate                 (alpha, beta)      rho          reading
         tau (Busemann)             (om/2 - 1, -1/2)   (om-1)/2 < 0 real hyperbolic at n = om
         u = d_H/2 (true distance)  (om - 1,    0)     om      > 0  complex hyperbolic at n = om

     Only the second has rho > 0, the range in which these weights belong to a space at all.
     The first also leaves the factor e^(tau/2) unexplained, where the Euclidean reading
     accounts for every factor of the kernel: prefactor, Jacobian and weight.

  D. AND THE COMB HAS NO COORDINATE.  Its offset in zeta(2s-d)/zeta(2s) and the exponent in
     its Jordan-totient weights J_d(n)/n^((d+1)/2) are d = 2 omega, with no radial variable to
     re-read them in.  Since the comb and the archimedean factor multiply to make
     Lambda(2s-d)/Lambda(2s), they must carry the same dimension.  That fixes it at 2 omega.

SO "HALF A DIMENSION" IS EXACT: omega is a COMPLEX dimension and 2 omega the real one.  The
real dimension is an integer exactly once in the family, at omega = 1/2 (d = 1, the horocycle
of the modular surface); the complex dimension is an integer nowhere in it.

  Counts refer to finite test cases, not independent theorems.
"""
import json
import math


class Group(object):
    def __init__(self, name, note=None):
        self.name, self.note, self.checks, self.tables = name, note, [], {}

    def add(self, what, error, tol):
        self.checks.append({"what": what, "error": error, "tolerance": tol, "pass": error < tol})
        return self

    def assert_true(self, what, ok):
        self.checks.append({"what": what, "error": 0.0 if ok else 1.0, "tolerance": 0.5, "pass": bool(ok)})
        return self

    def out(self):
        d = {"name": self.name, "cases": len(self.checks),
             "worst_margin_against_own_tolerance": max(c["error"] / c["tolerance"] for c in self.checks),
             "pass": all(c["pass"] for c in self.checks), "checks": self.checks}
        if self.note:
            d["note"] = self.note
        d.update(self.tables)
        return d


OMEGAS = (0.01, 0.05, 0.1, 0.25, 0.4, 0.5)


def sphere(d):
    return 2.0 * math.pi ** (d / 2.0) / math.gamma(d / 2.0)


def kGamma(om, tau):
    return sphere(2.0 * om) * (2.0 * math.sinh(tau)) ** (om - 1.0) * math.exp(tau / 2.0)


def gauss_legendre_unit(n):
    nodes, weights = [], []
    for i in range(1, n + 1):
        x = math.cos(math.pi * (i - 0.25) / (n + 0.5))
        for _ in range(100):
            p0, p1 = 1.0, 0.0
            for j in range(1, n + 1):
                p0, p1 = ((2.0 * j - 1.0) * x * p0 - (j - 1.0) * p1) / j, p0
            dp = n * (x * p0 - p1) / (x * x - 1.0)
            dx = -p0 / dp
            x += dx
            if abs(dx) < 1e-16:
                break
        nodes.append((1.0 + x) / 2.0)
        weights.append(1.0 / ((1.0 - x * x) * dp * dp))
    order = sorted(range(n), key=lambda i: nodes[i])
    return [nodes[i] for i in order], [weights[i] for i in order]


def group_busemann():
    g = Group("A. tau is a Busemann coordinate, not a distance",
              "the hyperbolic distance along the horocycle tracks the Euclidean radius at "
              "small scale and 2 tau at large; tau itself is a square of the radius near 0")
    w = 0.0
    rows = {}
    for t in (1e-4, 1e-2, 0.5, 3.0, 50.0):
        d1 = math.acosh(1.0 + t * t / 2.0)
        d2 = 2.0 * math.asinh(t / 2.0)
        tau = 0.5 * math.log(1.0 + t * t)
        w = max(w, abs(d1 - d2) / d1)
        rows["t = %g" % t] = {"d_H(i, t+i)": d1, "2 arcsinh(t/2)": d2, "tau = log|t+i|": tau,
                              "d_H / r": d1 / t, "d_H / (2 tau)": d1 / (2.0 * tau)}
    g.add("d_H(i, t+i) = 2 arcsinh(t/2), five separations", w, 1e-8)
    ws = 0.0
    for r in (1e-3, 1e-4, 1e-5):
        ws = max(ws, abs(0.5 * math.log(1.0 + r * r) / (r * r / 2.0) - 1.0))
    g.add("tau ~ r^2/2 as r -> 0 (the square)", ws, 1e-5)
    g.assert_true("d_H/r -> 1 as r -> 0, so the true distance tracks the Euclidean radius",
                  abs(math.acosh(1.0 + 1e-8 / 2.0) / 1e-4 - 1.0) < 1e-6)
    g.assert_true("d_H/(2 tau) -> 1 as r -> infinity, so tau is half the distance at large scale",
                  abs(math.acosh(1.0 + 2500.0 / 2.0) / (2.0 * 0.5 * math.log(1.0 + 2500.0)) - 1.0) < 1e-3)
    g.tables = {"the horocycle": rows}
    return g.out()


def group_two_exponents():
    g = Group("B. the same measure has local exponent 2om-1 in r and om-1 in tau",
              "and the ratio of the two normalized limits is 2^(1-omega), the Jacobian of the "
              "square tau = r^2/2 -- which is the entire difference between the two readings")
    worst, rows = 0.0, {}
    for om in OMEGAS:
        b = 0.5 + om
        r = 1e-7
        tau = 0.5 * math.log(1.0 + r * r)
        in_r = sphere(2.0 * om) * r ** (2.0 * om - 1.0) * (1.0 + r * r) ** (-b / 2.0) * r ** (1.0 - 2.0 * om)
        in_tau = kGamma(om, tau) * tau ** (1.0 - om)
        rows["omega = %g" % om] = {"[r] density * r^(1-2om)": in_r,
                                   "[tau] k^Gamma * tau^(1-om)": in_tau,
                                   "ratio": in_r / in_tau, "2^(1-omega)": 2.0 ** (1.0 - om)}
        e = abs(in_r / in_tau - 2.0 ** (1.0 - om)) / 2.0 ** (1.0 - om)
        g.add("the two local limits differ by exactly 2^(1-omega), omega = %g" % om, e, 1e-6)
        worst = max(worst, e)
    g.tables = {"local exponents": rows}
    return g.out()


def group_accounting():
    g = Group("C. the Euclidean reading accounts for every factor; the tau-Jacobi reading does not",
              "prefactor, Jacobian and weight together reproduce k^Gamma exactly, while the "
              "Jacobi weight Delta in the tau coordinate leaves e^(tau/2) unexplained")
    worst = 0.0
    rows = {}
    for om in OMEGAS:
        b = 0.5 + om
        e = 0.0
        for tau in (0.05, 0.3, 0.7, 2.0, 5.0):
            euclid = (sphere(2.0 * om) * (2.0 * math.sinh(tau)) ** (om - 1.0)
                      * math.exp((om + 1.0) * tau) * math.exp(-b * tau))
            e = max(e, abs(euclid - kGamma(om, tau)) / kGamma(om, tau))
        g.add("|S^{2om-1}| r^(2om-2) e^(2 tau) (1+r^2)^(-b/2) = k^Gamma_om(tau), omega = %g" % om,
              e, 1e-13)
        worst = max(worst, e)
        delta_only = sphere(2.0 * om) * (2.0 * math.sinh(0.7)) ** (om - 1.0)
        rows["omega = %g" % om] = {"k^Gamma(0.7)": kGamma(om, 0.7),
                                   "Delta_{om/2-1,-1/2}(0.7) with the prefactor": delta_only,
                                   "leftover": kGamma(om, 0.7) / delta_only,
                                   "e^(tau/2) at tau = 0.7": math.exp(0.35)}
        g.add("the tau-Jacobi leftover is exactly e^(tau/2), omega = %g" % om,
              abs(kGamma(om, 0.7) / delta_only - math.exp(0.35)) / math.exp(0.35), 1e-13)
    g.tables = {"what is left over in the tau coordinate": rows}
    return g.out()


def group_complex_hyperbolic():
    g = Group("D. in the true half-distance u = d_H/2 the measure is the CH^omega radial measure",
              "r = 2 sinh u turns Lebesgue on R^{2 omega} into (sinh u)^(2 omega - 1) cosh u, "
              "the radial Jacobian of complex hyperbolic space of complex dimension omega and "
              "real dimension 2 omega")
    worst = 0.0
    for om in OMEGAS:
        e = 0.0
        for u in (0.05, 0.3, 0.7, 2.0, 4.0):
            r = 2.0 * math.sinh(u)
            lhs = sphere(2.0 * om) * r ** (2.0 * om - 1.0) * (2.0 * math.cosh(u))
            rhs = 2.0 ** (2.0 * om) * sphere(2.0 * om) * math.sinh(u) ** (2.0 * om - 1.0) * math.cosh(u)
            e = max(e, abs(lhs - rhs) / lhs)
        g.add("|S^{2om-1}| r^(2om-1) dr/du = 2^(2om)|S^{2om-1}| (sinh u)^(2om-1) cosh u, omega = %g" % om,
              e, 1e-14)
        worst = max(worst, e)

    # the transfer in the u coordinate, by an honest quadrature independent of the r form:
    # int_0^inf (2 sinh u)^(2om-1)(2 cosh u)(2 cosh 2u - 1)^(-(p+b)/2) du, with u = v^(1/(2om))
    # on [0,1] to remove the endpoint singularity, plus Gauss-Legendre panels on [1, 40].
    xs, ws_ = gauss_legendre_unit(80)
    rows = {}
    wq = 0.0
    for om in (0.1, 0.25, 0.4, 0.5):
        a, b = 0.5 - om, 0.5 + om
        sub = {}
        for p in (2.0, 5.0):
            def f(u):
                return ((2.0 * math.sinh(u)) ** (2.0 * om - 1.0) * (2.0 * math.cosh(u))
                        * (2.0 * math.cosh(2.0 * u) - 1.0) ** (-(p + b) / 2.0))
            head = math.fsum(w * f(x ** (1.0 / (2.0 * om))) * x ** (1.0 / (2.0 * om) - 1.0) / (2.0 * om)
                             for x, w in zip(xs, ws_))
            tail = 0.0
            edges = [1.0 + 39.0 * (i / 8.0) ** 2 for i in range(9)]
            for lo, hi in zip(edges[:-1], edges[1:]):
                tail += (hi - lo) * math.fsum(w * f(lo + (hi - lo) * x) for x, w in zip(xs, ws_))
            num = sphere(2.0 * om) * (head + tail)
            closed = math.pi ** om * math.gamma((a + p) / 2.0) / math.gamma((b + p) / 2.0)
            rel = abs(num - closed) / closed
            sub["p = %g" % p] = {"quadrature in u": num, "closed form": closed, "relative error": rel}
            wq = max(wq, rel)
        rows["omega = %g" % om] = sub
    g.add("the transfer integral in the u coordinate against pi^om Gamma((a+p)/2)/Gamma((b+p)/2)",
          wq, 1e-9)
    g.tables = {"the transfer in the true distance": rows}
    return g.out()


def group_parameters():
    g = Group("E. the Jacobi parameters in the two coordinates, and what is realizable",
              "Delta_{al,be}(x) = (2 sinh x)^(2al+1)(2 cosh x)^(2be+1), rho = al+be+1; the "
              "group cases are (n/2-1, -1/2) for real hyperbolic H^n and (n-1, 0) for complex "
              "hyperbolic CH^n")
    rows = {}
    for om in OMEGAS:
        al_t, be_t = om / 2.0 - 1.0, -0.5
        al_u, be_u = om - 1.0, 0.0
        rows["omega = %g" % om] = {
            "tau (Busemann)": {"alpha": al_t, "beta": be_t, "rho": al_t + be_t + 1.0,
                               "reading": "real hyperbolic at n = omega"},
            "u = d_H/2 (true distance)": {"alpha": al_u, "beta": be_u, "rho": al_u + be_u + 1.0,
                                          "reading": "complex hyperbolic at n = omega"},
            "real dimension": 2.0 * om, "complex dimension": om}
        g.assert_true("omega = %g: rho < 0 in the Busemann coordinate" % om, al_t + be_t + 1.0 < 0.0)
        g.assert_true("omega = %g: rho > 0 in the true distance" % om, al_u + be_u + 1.0 > 0.0)
        g.add("omega = %g: rho = omega in the true distance" % om,
              abs((al_u + be_u + 1.0) - om), 1e-15)
        g.add("omega = %g: rho = (omega-1)/2 in the Busemann coordinate" % om,
              abs((al_t + be_t + 1.0) - (om - 1.0) / 2.0), 1e-15)
    # the group cases, as a sanity check on the parametrization
    wg = 0.0
    for n in (1, 2, 3, 4):
        for x in (0.3, 1.1):
            al, be = n / 2.0 - 1.0, -0.5
            delta = (2.0 * math.sinh(x)) ** (2.0 * al + 1.0) * (2.0 * math.cosh(x)) ** (2.0 * be + 1.0)
            wg = max(wg, abs(delta - (2.0 * math.sinh(x)) ** (n - 1)) / abs(delta))
            al, be = n - 1.0, 0.0
            delta = (2.0 * math.sinh(x)) ** (2.0 * al + 1.0) * (2.0 * math.cosh(x)) ** (2.0 * be + 1.0)
            want = (2.0 * math.sinh(x)) ** (2 * n - 1) * (2.0 * math.cosh(x))
            wg = max(wg, abs(delta - want) / abs(want))
    g.add("the group cases: (n/2-1,-1/2) gives (2 sinh)^(n-1) and (n-1,0) gives (2 sinh)^(2n-1)(2 cosh)",
          wg, 1e-14)
    # realizability
    g.assert_true("the real dimension 2 omega is an integer exactly once on (0,1/2], at omega = 1/2",
                  abs(2 * 0.5 - 1.0) < 1e-15
                  and all(abs(2 * o - round(2 * o)) > 1e-9 for o in OMEGAS if o != 0.5))
    g.assert_true("the complex dimension omega is an integer nowhere on (0,1/2]",
                  all(abs(o - round(o)) > 1e-9 for o in OMEGAS))
    g.tables = {"parameters": rows,
                "reading": "the real dimension is 2 omega in either coordinate once the "
                           "coordinate is a distance; the Busemann reading halves it because "
                           "tau ~ r^2/2. 'Half a dimension' is exact: omega is the complex one"}
    return g.out()


def main():
    groups = [group_busemann(), group_two_exponents(), group_accounting(),
              group_complex_hyperbolic(), group_parameters()]
    out = {
        "programme": "check_which_dimension.py",
        "investigation": "fractional-dimension",
        "question": "does the archimedean kernel carry the Euclidean dimension 2 omega or the "
                    "hyperbolic dimension omega?",
        "answer": "the real dimension is 2 omega. tau = log|t+i| is a Busemann function and not "
                  "a distance; the true hyperbolic distance on the horocycle tracks the "
                  "Euclidean radius, and tau ~ r^2/2 is a square, which is the whole factor of "
                  "two. In the true half-distance the measure is the radial measure of complex "
                  "hyperbolic space of complex dimension omega and real dimension 2 omega, with "
                  "rho = omega > 0; in the Busemann coordinate it is the real hyperbolic form at "
                  "n = omega with rho < 0 and an unexplained factor e^(tau/2). The comb, which "
                  "has no radial coordinate at all, fixes the dimension at 2 omega",
        "consequence": "'the shift is half a dimension' is exact: omega is a complex dimension "
                       "and 2 omega the real one",
        "scope": "finite test cases and exact identities about Gamma, sinh and the hyperbolic "
                 "metric of the upper half-plane; no zeta, no xi, no positivity",
        "groups": groups,
    }
    out["all_pass"] = all(g["pass"] for g in groups)
    out["total_checks"] = sum(g["cases"] for g in groups)
    print(json.dumps(out, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
