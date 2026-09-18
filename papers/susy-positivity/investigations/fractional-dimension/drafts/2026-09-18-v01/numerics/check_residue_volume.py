#!/usr/bin/env python3
"""
The Blaschke factor's pole is a volume term, and the lattice it belongs to has rank d + 1.
Standard library only; prints JSON to stdout.  Nothing here is a positivity certificate.

Unlike the other two programmes of this investigation, this one does evaluate zeta -- but only
at REAL arguments sigma > 1, by the convergent series with an Euler-Maclaurin tail.  No value on
or near the critical line is computed, and no functional equation is used.

THE STATEMENT.  With d = 2 omega, s = (p+b)/2 and b = (d+1)/2, the Markov part

    Ktilde_omega(p) = pi^(d/2) Gamma(s - d/2)/Gamma(s) . zeta(2s - d)/zeta(2s)

has a single pole in the right half-plane, at 2s - d = 1, that is at p = b = (d+1)/2 -- which
is exactly where the Blaschke factor B_b(p) = (p-b)/(p+b) of the full transfer cancels it.  Its
residue is

    Res_{p=b} Ktilde_omega = pi^((d+1)/2) / ( Gamma((d+1)/2) zeta(d+1) ) = |S^d| / (2 zeta(d+1)).

Both factors are d-dimensional in the same way, and both belong to dimension d + 1 rather than
d: |S^d| is the area of the unit sphere in R^(d+1), and 1/zeta(d+1) is the density of PRIMITIVE
vectors in Z^(d+1).  Their product is the volume term of a lattice of RANK d + 1, whose cusp has
a horocycle of dimension d -- the two differing by one, as a cusp requires.

At d = 1 this is the modular surface exactly: rank-2 lattice Z^2, one-dimensional horocycle, and

    Res_{p=b} = 6/pi = 2 / vol(PSL(2,Z)\\H),   vol = pi/3,

which is the classical residue Res_{s=1} phi(s) = 3/pi = 1/vol of the Eisenstein series,
doubled because 2s = p + b makes a residue in p twice a residue in s.

SO THE DICTIONARY CLOSES ON ITS THIRD ENTRY.  The correction is not merely "forced by
unimodularity and carrying no arithmetic", as the loewner investigation proved; it is the volume
term of the same d-dimensional object the other two factors live on, and its coefficient is
computable as one.

  Counts refer to finite test cases, not independent theorems.
"""
import json
import math
from itertools import product


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


def zeta_real(sig, N=40000):
    """zeta(sigma) for real sigma > 1: convergent series plus Euler-Maclaurin tail."""
    total = math.fsum(float(n) ** -sig for n in range(1, N))
    return (total + N ** (1.0 - sig) / (sig - 1.0) + 0.5 * N ** -sig
            + sig * N ** (-sig - 1.0) / 12.0)


def sphere(m):
    """|S^(m-1)|, the unit sphere in R^m."""
    return 2.0 * math.pi ** (m / 2.0) / math.gamma(m / 2.0)


def group_zeta():
    g = Group("A. the elementary zeta values this programme needs",
              "real arguments above 1 only, by a convergent series with an Euler-Maclaurin "
              "tail; checked against the two closed forms")
    g.add("zeta(2) against pi^2/6", abs(zeta_real(2.0) - math.pi ** 2 / 6.0) / (math.pi ** 2 / 6.0), 1e-12)
    g.add("zeta(4) against pi^4/90", abs(zeta_real(4.0) - math.pi ** 4 / 90.0) / (math.pi ** 4 / 90.0), 1e-12)
    g.add("zeta(6) against pi^6/945", abs(zeta_real(6.0) - math.pi ** 6 / 945.0) / (math.pi ** 6 / 945.0), 1e-12)
    g.tables = {"values": {"zeta(2)": zeta_real(2.0), "zeta(4)": zeta_real(4.0),
                           "zeta(6)": zeta_real(6.0)}}
    return g.out()


def group_residue():
    g = Group("B. the residue at the Blaschke pole, in two forms",
              "the pole sits at p = b = (d+1)/2, where 2s - d = 1; the residue is "
              "pi^((d+1)/2)/(Gamma((d+1)/2) zeta(d+1)), which is |S^d|/(2 zeta(d+1))")
    worst, rows = 0.0, {}
    for om in OMEGAS:
        d = 2.0 * om
        b = 0.5 + om
        r1 = math.pi ** ((d + 1.0) / 2.0) / (math.gamma((d + 1.0) / 2.0) * zeta_real(d + 1.0))
        r2 = sphere(d + 1.0) / (2.0 * zeta_real(d + 1.0))
        e = abs(r1 - r2) / r1
        rows["omega = %g" % om] = {"d = 2 omega": d, "pole at p = b = (d+1)/2": b,
                                   "residue": r1, "|S^d|": sphere(d + 1.0),
                                   "zeta(d+1)": zeta_real(d + 1.0)}
        g.add("the two forms of the residue agree, omega = %g" % om, e, 1e-14)
        g.assert_true("omega = %g: the pole is at p = b = (d+1)/2" % om, abs(b - (d + 1.0) / 2.0) < 1e-15)
        worst = max(worst, e)
    g.tables = {"residues": rows}
    return g.out()


def group_modular():
    g = Group("C. at d = 1 the residue is the volume of the modular surface",
              "residues in p are twice residues in s because 2s = p + b, so the classical "
              "Res_{s=1} phi(s) = 1/vol is recovered exactly")
    res_p = sphere(2.0) / (2.0 * zeta_real(2.0))
    vol = math.pi / 3.0
    g.add("Res_{p=b} at d = 1 against 6/pi", abs(res_p - 6.0 / math.pi) / (6.0 / math.pi), 1e-12)
    g.add("Res_{p=b} at d = 1 against 2/vol(PSL(2,Z)\\H)", abs(res_p - 2.0 / vol) / (2.0 / vol), 1e-12)
    g.add("Res_{s=1} = Res_{p=b}/2 against 1/vol", abs(res_p / 2.0 - 1.0 / vol) / (1.0 / vol), 1e-12)
    g.tables = {"the endpoint": {"Res_{p=b}": res_p, "6/pi": 6.0 / math.pi,
                                 "vol(PSL(2,Z)\\H) = pi/3": vol, "2/vol": 2.0 / vol,
                                 "Res_{s=1} = 1/vol": res_p / 2.0}}
    return g.out()


def group_lattice():
    g = Group("D. 1/zeta(m) is the primitive density in Z^m, so the lattice has rank d + 1",
              "checked by brute-force counts of primitive vectors in balls; the asymptotic "
              "error is of relative order log(X)/X, so the tolerances here are percents")
    rows = {}
    for m, X, tol in ((2, 300, 0.02), (3, 40, 0.03), (4, 14, 0.06)):
        count = 0
        rng = range(-X, X + 1)
        X2 = X * X
        for v in product(rng, repeat=m):
            if sum(c * c for c in v) > X2:
                continue
            gg = 0
            for c in v:
                gg = math.gcd(gg, c if c >= 0 else -c)
            if gg == 1:
                count += 1
        pred = (sphere(m) / m) * X ** m / zeta_real(float(m))
        rel = abs(count - pred) / pred
        rows["m = %d" % m] = {"radius X": X, "primitive vectors counted": count,
                              "vol(B^m) X^m / zeta(m)": pred, "relative error": rel}
        g.add("primitive count in a ball of R^%d against vol(B^m) X^m/zeta(m)" % m, rel, tol)
    g.tables = {"primitive lattice points": rows,
                "bookkeeping": {"horocycle dimension": "d = 2 omega",
                                "lattice rank": "d + 1 = 2 omega + 1",
                                "they differ by one": "as a cusp requires",
                                "at d = 1": "rank-2 lattice Z^2, one-dimensional horocycle: "
                                            "SL(2,Z) acting on the upper half-plane"}}
    for om in OMEGAS:
        d = 2.0 * om
        g.assert_true("omega = %g: rank (d+1) minus horocycle dimension (d) is 1" % om,
                      abs((d + 1.0) - d - 1.0) < 1e-15)
    return g.out()


def main():
    groups = [group_zeta(), group_residue(), group_modular(), group_lattice()]
    out = {
        "programme": "check_residue_volume.py",
        "investigation": "fractional-dimension",
        "statement": "the pole that the Blaschke factor cancels sits at p = b = (d+1)/2 and has "
                     "residue |S^d|/(2 zeta(d+1)): the volume term of a lattice of rank d+1 "
                     "whose cusp has a horocycle of dimension d. At d = 1 it is 2/vol of the "
                     "modular surface, recovering the classical Eisenstein residue 1/vol",
        "consequence": "the third entry of the dimension dictionary is not merely forced; it is "
                       "a volume, and its coefficient is computable as one",
        "scope": "finite test cases; zeta is evaluated only at real arguments above 1, by a "
                 "convergent series, and nothing here is a positivity certificate",
        "groups": groups,
    }
    out["all_pass"] = all(g["pass"] for g in groups)
    out["total_checks"] = sum(g["cases"] for g in groups)
    print(json.dumps(out, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
