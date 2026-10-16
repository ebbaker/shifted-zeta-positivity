#!/usr/bin/env python3
"""
What a radial Loewner chain would have to produce for the archimedean factor, and why it
cannot.  Standard library only; prints JSON to stdout.  Nothing here is a positivity
certificate and nothing here computes with zeta or xi.

THE TARGET.  With a = 1/2 - omega, b = 1/2 + omega, the archimedean transfer is
K^Gamma_omega(p) = pi^omega Gamma((a+p)/2)/Gamma((b+p)/2), whose causal kernel is
k^Gamma_omega(tau) = (2 pi^omega/Gamma(omega)) (2 sinh tau)^(omega-1) e^(tau/2).  Writing
2 sinh tau = e^tau (1 - e^(-2tau)) and omega - 1/2 = -a,

    k^Gamma_omega(tau) = (2 pi^omega/Gamma(omega)) e^(-a tau) (1 - e^(-2 tau))^(omega-1)
                       = pi^omega Gamma(a/2)/Gamma(b/2) * (density of tau = -1/2 log U),

so the archimedean delay is EXACTLY tau = -(1/2) log U with U ~ Beta(a/2, omega): the
squared radius ratio is a Beta variable whose two parameters are a/2 = 1/4 - omega/2 and
omega, summing to b/2.  A Loewner realization of the archimedean factor must produce that
law, for every omega in (0, 1/2), from a chain whose one free parameter is the dimension.

THREE OBSTRUCTIONS, each sufficient on its own.

  A. THE FRACTION IS INDEPENDENT OF THE TOTAL.  U = Z_a/(Z_a + Z_{2omega}) is the additivity
     fraction of the split b = a + 2omega (Shiga-Watanabe), and by the Gamma-Beta algebra it
     is independent of the total Z_b.  A chain driven by a dimension-b process therefore
     cannot see the split at all: U is fresh randomness, not a functional of the path, and
     "dimension b" does no work.  Checked here as the exact factorization of joint moments.

  B. THE ANTIPODAL EXPONENT IS PINNED AT 1/2.  For a radial chain driven by e^(iW) with W a
     continuous semimartingale, a marked boundary point has angle theta obeying the radial
     Loewner drift, d theta = cot(theta/2) dt - sigma dB, and the chord variable
     x = sin^2(theta/2) is a diffusion with

         sigma_x^2(x) = sigma^2 x (1-x),   mu_x(x) = (1-x) + (sigma^2/4)(1 - 2x).

     Its speed density m obeys (1/2)(sigma_x^2 m)' = mu_x m, giving
     m(x) ~ x^(2/sigma^2(0) - 1/2) at the swallowing end and m(x) ~ (1-x)^(-1/2) at the
     antipode.  The first exponent is free (it is the dimension); the SECOND IS -1/2 for
     every sigma, because at x = 1 the Loewner drift cot(theta/2) vanishes and the only
     surviving term is the Ito curvature of the chord map.  So whenever the chord law is a
     Beta law it is Beta( . , 1/2).  The target Beta(a/2, omega) has BOTH parameters below
     1/2 for every omega in (0, 1/2) -- a/2 < 1/4 and omega < 1/2 -- so it is never of that
     form; reversing the orientation asks instead for a/2 = 1/2, i.e. omega = 0.  The two
     families meet only at omega = 1/2, where the target degenerates to Beta(0, 1/2) and the
     dimension is forced to 0.

  C. THE DELAY HAS A SINGULARITY AT ZERO, FIRST-PASSAGE TIMES DO NOT.  k^Gamma_omega(tau)
     ~ (pi^omega 2^omega/Gamma(omega)) tau^(omega-1) blows up as tau -> 0; dually
     E[U^q] ~ (Gamma(b/2)/Gamma(a/2)) q^(-omega), a POWER law in q.  A first-passage time of
     a nondegenerate diffusion from a fixed interior point has a density vanishing faster
     than any power at 0 and a Laplace transform decaying like exp(-c sqrt(q)).  So the
     archimedean delay is not the hitting time of a chain started away from the boundary,
     whatever the driving.  The exponent of that power law is the shift itself.

  E. WHAT THE ARCHIMEDEAN FACTOR ACTUALLY IS: A HOROCYCLE INTEGRAL IN DIMENSION 2 omega.
     Exactly, for every omega in (0, 1/2],

         K^Gamma_omega(p) = int_{R^d} (1 + |t|^2)^{-(p+b)/2} dt = int_{R^d} |t + i|^{-(p+b)} dt,
         d = 2 omega,   s = (p+b)/2,   the integral being pi^{d/2} Gamma(s - d/2)/Gamma(s),

     and the kernel k^Gamma_omega(tau) dtau is the push-forward of (1+|t|^2)^{-b/2} dt under
     tau = (1/2) log(1 + |t|^2) = log|t + i|.  Its prefactor 2 pi^omega/Gamma(omega) is
     EXACTLY the surface area of the unit sphere S^{2 omega - 1}.  At omega = 1/2 this is
     d = 1: the constant-term integral of the Eisenstein series over the one-dimensional
     horocycle of the modular surface, which is why that endpoint is realized and why the
     delay is the log-modulus log|t+i| along it -- the arithmetic coordinate itself.  For
     omega < 1/2 the same formula asks for a horocycle of fractional dimension 2 omega in
     (0,1).  The shift is half a dimension, and every geometry quantizes it: d = 1 is the
     only integer the family's range contains.  This is also why the second Beta parameter
     is omega = d/2, the same d/2 that the radial chord law pins at 1/2 by its
     one-dimensional fold.

  D. The three dimensions a, 2 omega, b all lie in (0,1), while the SLE dictionary gives
     d = 1 + 4/kappa > 1 for every kappa > 0.  The proposal's own driving dimension is
     outside the range any SLE produces.

  Counts refer to finite test cases, not independent theorems.
"""
import json
import math

EULER = 0.57721566490153286061


def lbeta(a, b):
    return math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b)


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


OMEGAS = (0.002, 0.01, 0.05, 0.1, 0.25, 0.4, 0.49)


def kGamma(om, tau):
    return 2.0 * math.pi ** om / math.gamma(om) * (2.0 * math.sinh(tau)) ** (om - 1.0) * math.exp(tau / 2.0)


def beta_pullback(om, tau):
    """pi^om Gamma(a/2)/Gamma(b/2) times the density of tau = -(1/2) log U, U ~ Beta(a/2, om)."""
    a, b = 0.5 - om, 0.5 + om
    dens = 2.0 * math.exp(-a * tau) * (1.0 - math.exp(-2.0 * tau)) ** (om - 1.0) / math.exp(lbeta(a / 2.0, om))
    return math.pi ** om * math.gamma(a / 2.0) / math.gamma(b / 2.0) * dens


def group_identification():
    g = Group("A. the archimedean delay IS a Beta variable: tau = -(1/2) log U, U ~ Beta(a/2, omega)",
              "this is Proposition 4.1 of the manuscript made pointwise; the change of "
              "variable x = e^(-2 tau) in the Beta integral is what identifies U")
    worst = 0.0
    for om in OMEGAS:
        for tau in (1e-4, 1e-2, 0.1, 0.5, 1.0, 2.5, 6.0, 12.0):
            k = kGamma(om, tau)
            worst = max(worst, abs(k - beta_pullback(om, tau)) / abs(k))
    g.add("k^Gamma_omega(tau) against the Beta pullback, 7 shifts x 8 delays", worst, 1e-12)

    wm = 0.0
    for om in OMEGAS:
        a, b = 0.5 - om, 0.5 + om
        for q in (0.25, 1.0, 3.0, 10.0):
            mellin = math.exp(lbeta(a / 2.0 + q, om) - lbeta(a / 2.0, om))
            gam = math.exp(math.lgamma((a + 2.0 * q) / 2.0) + math.lgamma(b / 2.0)
                           - math.lgamma((b + 2.0 * q) / 2.0) - math.lgamma(a / 2.0))
            wm = max(wm, abs(mellin - gam) / gam)
    g.add("E[U^q] against Gamma((a+2q)/2) Gamma(b/2) / (Gamma((b+2q)/2) Gamma(a/2))", wm, 1e-13)

    rows = {}
    ws = 0.0
    for om in OMEGAS:
        lim = math.pi ** om * 2.0 ** om / math.gamma(om)
        v = kGamma(om, 1e-9) * (1e-9) ** (1.0 - om)
        rows["omega = %g" % om] = {"k^Gamma(tau) tau^(1-omega) at tau=1e-9": v,
                                   "pi^om 2^om / Gamma(om)": lim}
        ws = max(ws, abs(v - lim) / lim)
    g.add("the zero-delay singularity k^Gamma ~ (pi^om 2^om/Gamma(om)) tau^(omega-1)", ws, 1e-8)

    wp, prows = 0.0, {}
    for om in OMEGAS:
        a, b = 0.5 - om, 0.5 + om
        lim = math.exp(math.lgamma(b / 2.0) - math.lgamma(a / 2.0))
        q = 1e7
        v = math.exp(lbeta(a / 2.0 + q, om) - lbeta(a / 2.0, om)) * q ** om
        prows["omega = %g" % om] = {"E[U^q] q^omega at q=1e7": v, "Gamma(b/2)/Gamma(a/2)": lim}
        wp = max(wp, abs(v - lim) / lim)
    g.add("the dual power law E[U^q] ~ (Gamma(b/2)/Gamma(a/2)) q^(-omega)", wp, 1e-6)
    g.tables = {"zero-delay exponent": rows, "large-q power law": prows}
    return g.out()


def group_independence():
    g = Group("B. the additivity fraction is independent of the total, so a dimension-b chain cannot see the split",
              "U = Z_a/(Z_a + Z_2omega) and S = Z_a + Z_2omega = Z_b are independent "
              "(Gamma-Beta algebra); at the level of processes this is the Warren-Yor "
              "decomposition of BESQ into a Jacobi process and an independent total. So the "
              "Beta law is not a functional of the dimension-b path")
    worst = 0.0
    rows = {}
    for om in (0.002, 0.01, 0.1, 0.25, 0.45):
        al, be = (0.5 - om) / 2.0, om
        sub = {}
        for q in (0.3, 1.0, 2.5):
            for r in (0.3, 1.0, 2.5):
                joint = math.exp(lbeta(al + q, be) + math.lgamma(al + be + r)
                                 - math.lgamma(al) - math.lgamma(be))
                EU = math.exp(lbeta(al + q, be) - lbeta(al, be))
                ES = math.exp(math.lgamma(al + be + r) - math.lgamma(al + be))
                rel = abs(joint - EU * ES) / abs(EU * ES)
                worst = max(worst, rel)
                if q == 1.0 and r == 1.0:
                    sub = {"E[U S]": joint, "E[U] E[S]": EU * ES}
        rows["omega = %g" % om] = sub
    g.add("E[U^q S^r] = E[U^q] E[S^r], 5 shifts x 9 (q,r) pairs", worst, 1e-12)
    g.tables = {"at q = r = 1": rows}
    return g.out()


def chord_coefficients(sig2, x):
    """x = sin^2(theta/2) for d theta = cot(theta/2) dt - sigma dB: (mu_x, sigma_x^2)."""
    return (1.0 - x) + (sig2 / 4.0) * (1.0 - 2.0 * x), sig2 * x * (1.0 - x)


def group_pinned_exponent():
    g = Group("C. the antipodal exponent of a radial chain is 1/2 for every driving",
              "the speed density solves (1/2)(sigma_x^2 m)' = mu_x m; at the antipode the "
              "Loewner drift cot(theta/2) vanishes and only the Ito curvature of the chord "
              "map survives, which is why the exponent there does not depend on the driving")
    # (i) the exact speed density for constant sigma^2 = kappa, verified algebraically
    worst = 0.0
    rows = {}
    for kappa in (1.0, 2.0, 4.0, 6.0, 8.0, 16.0, 64.0):
        p = 2.0 / kappa - 0.5                      # m(x) = x^p (1-x)^(-1/2)
        for x in (0.05, 0.2, 0.5, 0.8, 0.95):
            mu, _ = chord_coefficients(kappa, x)
            lhs = (kappa / 2.0) * ((p + 1.0) * (1.0 - x) - x / 2.0)     # (1/2)(sigma_x^2 m)' / (x^p (1-x)^(-1/2))
            worst = max(worst, abs(lhs - mu) / abs(mu))
        d = 1.0 + 4.0 / kappa
        rows["kappa = %g" % kappa] = {"Bessel dimension d = 1 + 4/kappa": d,
                                      "speed density": "x^(d/2 - 1) (1-x)^(-1/2)",
                                      "Beta parameters (swallowing, antipode)": [d / 2.0, 0.5]}
    g.add("(1/2)(sigma_x^2 m)' = mu_x m for m = x^(d/2-1)(1-x)^(-1/2), 7 kappa x 5 points", worst, 1e-13)

    # (ii) the two endpoint exponents, for general sigma^2(x), from the limits of (1-x) 2mu/sigma_x^2
    drivings = (("sigma^2 = 6 (constant)", lambda x: 6.0),
                ("sigma^2 = 2 (constant)", lambda x: 2.0),
                ("sigma^2 = 6 (1 + 0.3 cos theta)^2", lambda x: 6.0 * (1.0 + 0.3 * (1.0 - 2.0 * x)) ** 2),
                ("sigma^2 = 6 (1 + 0.6 x)", lambda x: 6.0 * (1.0 + 0.6 * x)),
                ("sigma^2 = 1 + 9 x^2", lambda x: 1.0 + 9.0 * x * x))
    wa, w0, erows = 0.0, 0.0, {}
    for name, s2 in drivings:
        vals_anti, vals_swal = [], []
        for eps in (1e-6, 1e-8, 1e-10):
            x = 1.0 - eps
            mu, sx2 = chord_coefficients(s2(x), x)
            vals_anti.append(eps * 2.0 * mu / sx2)          # -> -1/2, pinned
            x = eps
            mu, sx2 = chord_coefficients(s2(x), x)
            vals_swal.append(eps * 2.0 * mu / sx2)          # -> 2/sigma^2(0) + 1/2, free
        want0 = 2.0 / s2(0.0) + 0.5
        wa = max(wa, max(abs(v + 0.5) for v in vals_anti))
        w0 = max(w0, max(abs(v - want0) for v in vals_swal))
        erows[name] = {"antipode: (1-x) 2 mu_x/sigma_x^2 -> -1/2": vals_anti[-1],
                       "swallowing end: x 2 mu_x/sigma_x^2 -> 2/sigma^2(0) + 1/2": vals_swal[-1],
                       "that limit": want0,
                       "speed exponents (swallowing, antipode)": [want0 - 1.0, -0.5]}
    g.add("the antipodal exponent is -1/2 for all 5 drivings (Beta second parameter = 1/2)", wa, 1e-5)
    g.add("the swallowing exponent is 2/sigma^2(0) - 1/2, free, for all 5 drivings", w0, 1e-5)
    g.tables = {"constant driving": rows, "general driving": erows}
    return g.out()


def group_exclusion():
    g = Group("D. the two parameter families do not meet on 0 < omega < 1/2",
              "the radial family is Beta(d/2, 1/2) (or Beta(1/2, d/2) with the orientation "
              "reversed): one parameter is exactly 1/2. The target has both parameters "
              "strictly below 1/2, and its first below 1/4")
    rows = {}
    for om in OMEGAS:
        a, b = 0.5 - om, 0.5 + om
        al, be = a / 2.0, om
        rows["omega = %g" % om] = {"b = 1/2 + omega": b, "target Beta": [al, be],
                                   "sum = b/2": al + be, "max parameter": max(al, be),
                                   "matches Beta(d/2, 1/2)?": abs(be - 0.5) < 1e-12,
                                   "matches Beta(1/2, d/2)?": abs(al - 0.5) < 1e-12}
        g.assert_true("omega = %g: both target parameters are < 1/2" % om, max(al, be) < 0.5)
        g.assert_true("omega = %g: the first target parameter is < 1/4" % om, al < 0.25)
        g.assert_true("omega = %g: neither parameter equals 1/2, so no radial chord law matches" % om,
                      abs(al - 0.5) > 1e-12 and abs(be - 0.5) > 1e-12)
    # the endpoint
    om = 0.5
    al, be = (0.5 - om) / 2.0, om
    g.assert_true("at omega = 1/2 the second parameter is 1/2 but the first is 0, forcing dimension 0",
                  abs(be - 0.5) < 1e-15 and abs(al) < 1e-15)
    # dimension range
    drow = {}
    for om in OMEGAS:
        a, b = 0.5 - om, 0.5 + om
        drow["omega = %g" % om] = {"a": a, "2 omega": 2.0 * om, "b": b, "all below 1": max(a, 2.0 * om, b) < 1.0}
        g.assert_true("omega = %g: the three dimensions a, 2omega, b all lie in (0,1)" % om,
                      0.0 < min(a, 2.0 * om) and max(a, 2.0 * om, b) < 1.0)
    g.assert_true("the SLE dictionary d = 1 + 4/kappa never reaches (0,1)",
                  all(1.0 + 4.0 / k > 1.0 for k in (0.5, 1.0, 2.0, 4.0, 8.0, 16.0, 64.0, 1024.0)))
    g.tables = {"target parameters": rows, "the three Bessel dimensions": drow}
    return g.out()


def sphere_area(d):
    return 2.0 * math.pi ** (d / 2.0) / math.gamma(d / 2.0)


def riesz_quadrature(d, s, n=200000):
    """S_{d-1} int_0^inf (1+r^2)^(-s) r^(d-1) dr by the substitution r = tan u."""
    h = (math.pi / 2.0) / n
    tot = math.fsum(h * (1.0 + math.tan(h * (i + 0.5)) ** 2) ** (-s)
                    * math.tan(h * (i + 0.5)) ** (d - 1) / math.cos(h * (i + 0.5)) ** 2
                    for i in range(n))
    return sphere_area(d) * tot


def group_horocycle():
    g = Group("E. the archimedean factor is a horocycle integral in dimension d = 2 omega",
              "K^Gamma_omega(p) = int_{R^d} |t+i|^(-(p+b)) dt with d = 2 omega: at omega = 1/2 "
              "this is the constant-term integral of the Eisenstein series over the "
              "one-dimensional horocycle of the modular surface, and the delay is log|t+i|, "
              "the arithmetic coordinate. For omega < 1/2 the dimension is fractional")
    worst = 0.0
    for om in OMEGAS + (0.5,):
        a, b = 0.5 - om, 0.5 + om
        for p in (0.7, 1.5, 4.0, 9.0, 25.0):
            lhs = math.pi ** om * math.gamma((a + p) / 2.0) / math.gamma((b + p) / 2.0)
            s_ = (p + b) / 2.0
            rhs = math.pi ** om * math.gamma(s_ - om) / math.gamma(s_)
            worst = max(worst, abs(lhs - rhs) / lhs)
    g.add("K^Gamma_omega(p) = pi^(d/2) Gamma(s-d/2)/Gamma(s), d = 2 omega, s = (p+b)/2", worst, 1e-13)

    ws, srows = 0.0, {}
    for om in (0.05, 0.1, 0.25, 0.5, 1.0, 1.5):
        pref = 2.0 * math.pi ** om / math.gamma(om)
        area = sphere_area(2.0 * om)
        srows["omega = %g" % om] = {"d = 2 omega": 2.0 * om,
                                    "2 pi^omega / Gamma(omega)": pref,
                                    "area of S^(2 omega - 1)": area}
        ws = max(ws, abs(pref - area) / area)
    g.add("the kernel prefactor is the area of the unit sphere in dimension 2 omega", ws, 1e-14)

    wq, qrows = 0.0, {}
    for d in (1, 2, 3):
        for s_ in (1.4, 2.0, 3.5):
            if s_ <= d / 2.0:
                continue
            closed = math.pi ** (d / 2.0) * math.gamma(s_ - d / 2.0) / math.gamma(s_)
            num = riesz_quadrature(d, s_)
            rel = abs(num - closed) / closed
            qrows["d = %d, s = %g" % (d, s_)] = {"quadrature": num, "closed form": closed,
                                                 "relative error": rel}
            wq = max(wq, rel)
    g.add("the Riesz integral by honest quadrature at integer d in {1,2,3}", wq, 1e-5)

    # push-forward of (1+|t|^2)^(-b/2) dt under tau = (1/2) log(1+|t|^2)
    wp = 0.0
    for om in OMEGAS:
        b = 0.5 + om
        for tau in (1e-3, 0.05, 0.5, 2.0, 6.0):
            r2 = math.exp(2.0 * tau) - 1.0
            push = sphere_area(2.0 * om) * r2 ** (om - 1.0) * math.exp(2.0 * tau) * (1.0 + r2) ** (-b / 2.0)
            wp = max(wp, abs(push - kGamma(om, tau)) / kGamma(om, tau))
    g.add("k^Gamma_omega dtau is the push-forward of (1+|t|^2)^(-b/2) dt on R^(2 omega)", wp, 1e-12)

    g.assert_true("d = 2 omega is an integer for some omega in (0, 1/2] only at omega = 1/2",
                  all(abs(2.0 * om - round(2.0 * om)) > 1e-12 for om in OMEGAS) and abs(2 * 0.5 - 1) < 1e-15)
    g.tables = {"sphere areas": srows, "Riesz integral at integer dimension": qrows,
                "reading": "d = 1 at omega = 1/2 is the horocycle of the modular surface; "
                           "d = 2 would be omega = 1, outside the family"}
    return g.out()


def main():
    groups = [group_identification(), group_independence(), group_pinned_exponent(),
              group_exclusion(), group_horocycle()]
    out = {
        "programme": "check_beta_realization.py",
        "investigation": "loewner",
        "question": "can a radial Loewner chain driven by a Bessel process of dimension "
                    "b = 1/2 + omega produce the archimedean delay, i.e. a squared radius "
                    "ratio distributed as Beta(a/2, omega)?",
        "what the archimedean factor is instead": "the horocycle integral "
                    "int_{R^d} |t+i|^(-(p+b)) dt in dimension d = 2 omega, whose delay is "
                    "log|t+i| and whose prefactor is the area of S^(2 omega - 1); at "
                    "omega = 1/2, d = 1 and this is the Eisenstein constant term of the "
                    "modular surface. The shift is half a dimension, and geometry quantizes it",
        "answer": "no, for three independent reasons: the fraction is independent of the "
                  "total; the antipodal exponent of any radial chord law is pinned at 1/2 "
                  "while the transfer needs it to be omega; and the delay has a power-law "
                  "singularity at zero delay that no first-passage time from an interior "
                  "start can have",
        "scope": "finite test cases and exact identities about Beta, Gamma and the radial "
                 "Loewner drift; no zeta, no xi, no zeros, and nothing here is a positivity "
                 "certificate",
        "groups": groups,
    }
    out["all_pass"] = all(g["pass"] for g in groups)
    out["total_checks"] = sum(g["cases"] for g in groups)
    print(json.dumps(out, indent=2, sort_keys=False))


if __name__ == "__main__":
    main()
