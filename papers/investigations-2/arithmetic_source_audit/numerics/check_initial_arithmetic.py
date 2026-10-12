#!/usr/bin/env python3
"""Finite diagnostics of the pinned initial arithmetic reduction.

Prepared for Edward Baker with substantial LLM assistance, 2026-10-12.
Model: GPT-6 (Codex), inherited configuration. Exact serving variant and
configured reasoning effort are not exposed and are not inferred.
No finite test proves the analytic Poisson reduction or an infinite identity.

The Eisenstein arithmetic and residue-field representation are adapted from
check_upstream_reflection_interfaces.py (2026-10-09); this script is standalone.
Exact checks use integers/Fraction and residue-character exponents. Complex
Gauss sums are independently evaluated finite sums with tolerance 1e-10.
"""

import argparse
import cmath
from fractions import Fraction
import hashlib
from itertools import product, combinations
import json
from pathlib import Path
import platform

ONE, ZERO, LAM = (1, 0), (0, 0), (1, 2)
UNITS = [(1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (1, 1)]
PRIME_DATA = [((-2, -3), 7, False), ((1, -3), 13, False),
              ((-2, 3), 19, False), ((1, 6), 31, False),
              ((7, 3), 37, False), ((7, 6), 43, False),
              ((-5, 0), 5, True), ((-11, 0), 11, True)]
COUNTS, ERRORS, NEGATIVE = {}, {}, {}
TOL = 1e-10
EXPECTED_SOURCE_SHA256 = "d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d"


def exact(ok, label):
    assert ok, label
    COUNTS[label] = COUNTS.get(label, 0) + 1


def near(a, b, label):
    err = abs(a - b)
    assert err < TOL, (label, a, b, err)
    n, old = ERRORS.get(label, (0, 0.0))
    ERRORS[label] = (n + 1, max(old, err))


def negative(ok, label, example=None):
    if ok:
        rec = NEGATIVE.setdefault(label, {"detected": 0, "example": example})
        rec["detected"] += 1


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def sub(a, b):
    return a[0] - b[0], a[1] - b[1]


def mul(a, b):
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0] - a[1] * b[1]


def norm(a):
    return a[0] ** 2 - a[0] * a[1] + a[1] ** 2


def powe(a, n):
    ans = ONE
    while n:
        if n & 1:
            ans = mul(ans, a)
        a, n = mul(a, a), n // 2
    return ans


def quot(a, b):
    t, n = mul(a, (b[0] - b[1], -b[1])), norm(b)
    return Fraction(t[0], n), Fraction(t[1], n)


def exactdiv(a, b):
    q = quot(a, b)
    assert all(x.denominator == 1 for x in q), (a, b, q)
    return tuple(int(x) for x in q)


def divides(a, b):
    return all(x.denominator == 1 for x in quot(b, a))


def divrem(a, b):
    x, y = quot(a, b)
    aa, bb = x.numerator // x.denominator, y.numerator // y.denominator
    q = min(((aa+i, bb+j) for i in (-1, 0, 1, 2) for j in (-1, 0, 1, 2)),
            key=lambda q: norm(sub(a, mul(q, b))))
    r = sub(a, mul(q, b))
    assert norm(r) < norm(b)
    return q, r


def primary(a):
    return a[0] % 3 == 1 and a[1] % 3 == 0


def gcd(a, b):
    while b != ZERO:
        a, b = b, divrem(a, b)[1]
    candidates = [mul(u, a) for u in UNITS if primary(mul(u, a))]
    assert len(candidates) == 1
    return candidates[0]


def prod_ring(seq):
    ans = ONE
    for x in seq:
        ans = mul(ans, x)
    return ans


def mu(mask):
    return (-1) ** sum(mask)


class Field:
    """O/(a+b omega) for split prime; O/(-p) for an inert prime."""

    def __init__(self, element, p, inert):
        self.element, self.p, self.inert = element, p, inert
        self.q = p * p if inert else p
        self.values = [(a, b) for a in range(p) for b in range(p)] if inert else list(range(p))
        self.zero, self.one = ((0, 0), (1, 0)) if inert else (0, 1)
        self.root6 = (1, 1) if inert else (1 - element[0] * pow(element[1], -1, p)) % p
        roots = [self.power(self.root6, j) for j in range(6)]
        assert len(set(roots)) == 6
        self.chars = {x: None if x == self.zero else roots.index(self.power(x, (self.q-1)//6)) for x in self.values}

    def reduce(self, x):
        if self.inert:
            return x[0] % self.p, x[1] % self.p
        return (x[0] - x[1] * self.element[0] * pow(self.element[1], -1, self.p)) % self.p

    def product(self, a, b):
        if self.inert:
            t = mul(a, b)
            return t[0] % self.p, t[1] % self.p
        return a * b % self.p

    def plus(self, a, b):
        if self.inert:
            return (a[0]+b[0]) % self.p, (a[1]+b[1]) % self.p
        return (a+b) % self.p

    def minus(self, a, b):
        if self.inert:
            return (a[0]-b[0]) % self.p, (a[1]-b[1]) % self.p
        return (a-b) % self.p

    def power(self, a, n):
        ans = self.one
        while n:
            if n & 1:
                ans = self.product(ans, a)
            a, n = self.product(a, a), n // 2
        return ans

    def additive_exponent(self, x):
        # e(a+b omega)=exp(2 pi i b); conjugate of denominator is used.
        return (-x[1] if self.inert else -self.element[1] * x) % self.p

    def additive(self, x):
        return cmath.exp(2j * cmath.pi * self.additive_exponent(x) / self.p)

    def char(self, x, j=1):
        exponent = self.chars[x]
        return 0j if exponent is None else cmath.exp(2j * cmath.pi * (j*exponent % 6) / 6)

    def char_ring(self, x, j=1):
        return self.char(self.reduce(x), j)

    def gauss(self, j, scale=None):
        if scale is None:
            scale = self.one
        return sum(self.char(x, j) * self.additive(self.product(scale, x)) for x in self.values) / self.q**0.5


def gamma_quad_exp(c):
    """Exact phase t in Gamma_quad(c)=i^t from Appendix A.1."""
    iroots = [(1,0), (0,1), (-1,0), (0,-1)]
    a, b = c
    terms = [iroots[j % 4] for j in (0, -b, a, b-a)]
    z = tuple(sum(t[k] for t in terms) for k in (0,1))
    assert all(v % 2 == 0 for v in z)
    return iroots.index(tuple(v//2 for v in z))


def cubic_mod2_exp(c):
    # (c/(-2))_3 in F4 is c itself, with omega exponent 0,1,2.
    return {(1,0): 0, (0,1): 1, (1,1): 2}[(c[0] % 2, c[1] % 2)]


def gexp(c):
    return (3 * gamma_quad_exp(c) - 4 * cubic_mod2_exp(c)) % 12


def ray(c):
    return c[0] % 12, c[1] % 12


def rayinv(c):
    answers = [(a,b) for a in range(12) for b in range(12) if ray(mul(c,(a,b))) == ONE]
    assert len(answers) == 1
    return answers[0]


def root12(j):
    return cmath.exp(2j * cmath.pi * (j % 12) / 12)


def check_bookkeeping():
    # Actual primary Eisenstein primes, including one inert prime.
    ps = [PRIME_DATA[i][0] for i in (0,1,6)]
    masks = list(product((0,1), repeat=len(ps)))
    sqfree = {s: prod_ring(p for p, present in zip(ps,s) if present) for s in masks}
    for s, t in product(masks, repeat=2):
        g = gcd(sqfree[s], sqfree[t])
        common = tuple(a and b for a,b in zip(s,t))
        exact(g == sqfree[common], "gcd_common_column")
        divisors = [v for v in masks if all(a <= b for a,b in zip(v,common))]
        exact(sum(mu(v) for v in divisors) == int(g == ONE), "mobius_common_column")
        negative(len(divisors) != int(g == ONE), "drop_common_column_mobius_sign", {"s":s,"t":t})
    images = set()
    for bs, fs in product(masks, repeat=2):
        if any(a and b for a,b in zip(bs,fs)):
            continue
        b, f = sqfree[bs], sqfree[fs]
        for ks in product(range(3), repeat=len(ps)):
            basek = prod_ring(powe(p,n) for p,n in zip(ps,ks))
            for unit in UNITS:
                k = mul(unit,basek)
                e = gcd(f,k)  # Euclidean gcd, independent of factor-list inverse.
                es = tuple(int(present and exponent>0) for present,exponent in zip(fs,ks))
                exact(e == sqfree[es], "inverse_e_is_actual_gcd")
                v, h, g = exactdiv(f,e), exactdiv(k,e), mul(b,e)
                exact(gcd(g,v) == ONE and gcd(h,v) == ONE, "inverse_coprimality")
                exact(all(not divides(powe(p,2),g) and not divides(powe(p,2),v) for p in ps), "inverse_squarefree")
                exact(exactdiv(g,e) == b and mul(e,v) == f and mul(e,h) == k, "bijection_forward_inverse")
                key = (g,v,e,h)
                exact(key not in images, "bijection_injective")
                images.add(key)
                exact(mul(g,v) == mul(b,f), "column_product_identity")
                exact(mul(h,mul(powe(e,5),powe(v,4))) == mul(k,powe(f,4)), "twist_argument_identity")
                vs = tuple(a-b for a,b in zip(fs,es))
                exact(mu(es)*mu(vs) == mu(fs), "mobius_factor_identity")
                exact(Fraction(norm(g),norm(e)) == norm(b), "norm_coefficient_identity")
                # Use m1,m2=1 here: equality is independent of their common factor.
                exact(Fraction(norm(h),norm(e)*norm(v)**2) == Fraction(norm(k),norm(f)**2), "poisson_norm_argument_identity")
                negative(gcd(f,k) != f, "incorrect_inverse_e_equals_f", {"f":f,"k":k})
                negative(mul(h,mul(powe(e,4),powe(v,4))) != mul(k,powe(f,4)), "drop_one_e_twist_power", {"e":e,"h":h,"v":v})
                # A surviving m may share primes with k; only f is discarded here.
                for ms,m in sqfree.items():
                    mask_before = int(gcd(m,f) == ONE)
                    mask_after = int(all(not divides(p,mul(k,powe(f,4))) for p in ps if divides(p,m)))
                    mask_k = int(gcd(m,k) == ONE)
                    exact(mask_after == mask_before*mask_k, "zero_extension_f_mask")
                    negative(mask_after != mask_k, "omit_chi_m_f_fourth_power", {"m":m,"f":f,"k":k})
    # Scales are exact rational identities; no numerical rounding is used.
    for D,B,F,nd in product((100,1000),(1,2,8),(1,3,7),(1,7,13)):
        X = Fraction(D,B*F)
        exact(X*F == Fraction(D,B), "scale_XF")
        exact((X/nd)*(F*nd) == X*F, "exclusion_shift_scale")
    # If the common-column character mask (h,v)=1 is lost, the claimed
    # inverse really fails: e=1, v=p, h=p gives gcd(f,k)=p, not e.
    for p in ps:
        negative(gcd(p,p) != ONE,"drop_h_v_coprimality_breaks_inverse", {"g":ONE,"v":p,"e":ONE,"h":p})
        # Without (g,v)=1, e=g=p and v=p instead produce nonsquarefree f.
        negative(divides(powe(p,2),mul(p,p)),"drop_g_v_coprimality_breaks_squarefree_f", {"g":p,"v":p,"e":p,"h":ONE})


def check_ray_classes():
    units4 = [(a,b) for a in range(4) for b in range(4) if norm((a,b)) % 2]
    reduce4 = lambda z: (z[0] % 4,z[1] % 4)
    squares4 = {reduce4(mul(u,u)) for u in units4}
    exact(len(units4) == 12 and len(squares4) == 3,"mod4_square_subgroup_count")
    representatives = [ONE,(-1,0),LAM,(-LAM[0],-LAM[1])]
    cosets = [{reduce4(mul(c,s)) for s in squares4} for c in representatives]
    exact(len({frozenset(s) for s in cosets}) == 4,"mod4_square_cosets_distinct")
    exact(set.union(*cosets) == set(units4),"mod4_square_cosets_cover")
    for c,s in product(units4,squares4):
        exact(gamma_quad_exp(c) == gamma_quad_exp(mul(c,s)),"mod4_quadratic_square_invariance")
    for c,expected in zip(representatives,(0,0,1,3)):
        exact(gamma_quad_exp(c) == expected,"mod4_quadratic_representative_table")
    classes = [(a,b) for a in range(12) for b in range(12) if primary((a,b)) and norm((a,b)) % 2]
    exact(len(classes) == 12, "ray_class_count")
    def R(a,b):
        exponent = (gexp(mul(a,b))-gexp(a)-gexp(b)) % 12
        exact(exponent in (0,6), "ray_R_sign")
        return exponent
    for a,b in product(classes, repeat=2):
        exact(R(a,b) == R(b,a), "ray_R_symmetric")
        exact((gexp(mul(b,rayinv(a)))-gexp(b)+gexp(a)+R(a,a)+R(a,b)) % 12 == 0, "ray_G_quotient")
        for c in classes:
            exact(R(mul(a,c),b) == (R(a,b)+R(c,b)) % 12, "ray_R_multiplicative_first")
            exact(R(a,mul(b,c)) == (R(a,b)+R(a,c)) % 12, "ray_R_multiplicative_second")
    for e,f,g,h in product((0,1),repeat=4):
        a,b = mul(powe((-1,0),e),powe(LAM,f)), mul(powe((-1,0),g),powe(LAM,h))
        actual = (gamma_quad_exp(mul(a,b))-gamma_quad_exp(a)-gamma_quad_exp(b)) % 4
        exact(actual == 2*((e*h+f*g+f*h) % 2), "four_square_classes_sign_table")
        negative(actual != 2*((e*h+f*g) % 2), "omit_fh_bicharacter_sign", {"e":e,"f":f,"g":g,"h":h})


def check_gauss():
    fields = [Field(*data) for data in PRIME_DATA]
    prime_reports = []
    for f in fields:
        p = f.element
        alpha = complex(p[0]-p[1]/2, p[1]*3**0.5/2)/f.q**0.5
        gam = {j:f.gauss(j) for j in (-1,0,1,2,3,4,5)}
        G = f.char_ring((4,0)).conjugate()*gam[3]
        rayG = root12(gexp(p))
        near(gam[2]**3,-alpha,"prime_gamma2_cube")
        near(gam[1]*gam[2],-alpha*G,"prime_gamma1_gamma2")
        near(gam[1]*gam[-1],f.char_ring((-1,0)),"prime_inverse_gauss")
        near(-gam[-1],f.char_ring((-1,0))/G*alpha.conjugate()*gam[2],"prime_convert2")
        near(G,rayG,"prime_G_ray_evaluation")
        near(gam[3],root12(3*gamma_quad_exp(p)),"prime_quadratic_gauss")
        near(gam[0],-1/f.q**0.5,"principal_gauss_unit_mask")
        # Check Jacobi evaluation from its defining finite sum, using exact roots.
        coeff = [0,0,0]
        for x in f.values:
            y = f.minus(f.one,x)
            if x != f.zero and y != f.zero:
                j = (2*(f.chars[x]+f.chars[y]) % 6)//2
                coeff[j] += 1
        J = (coeff[0]-coeff[2],coeff[1]-coeff[2])
        exact(J == (-p[0],-p[1]),"prime_cubic_jacobi_exact")
        # Test the common-column character mask on every residue h and unit e.
        for h,e in product(f.values,[x for x in f.values if x!=f.zero]):
            he5 = f.product(h,f.power(e,5))
            exact(int(f.chars[he5] is not None) == int(h!=f.zero),"common_column_character_mask")
            near(abs(alpha.conjugate()*gam[2]*f.char(he5))**2,int(h!=f.zero),"common_column_absolute_square")
        for x in f.values:
            exact((f.chars[x] is None) == (x==f.zero),"character_zero_extension")
            negative(f.char(x,0) != 1,"principal_power_zero_must_be_mask", {"prime":p,"x":x})
        negative(abs(gam[2]**3-alpha)>1e-7,"omit_prime_mobius_sign",{"prime":p})
        negative(abs(-gam[-1]-1/G*alpha.conjugate()*gam[2])>1e-7,"omit_chi_minus_one_convert2",{"prime":p})
        prime_reports.append({"primary_prime":p,"rational_prime":f.p,"norm":f.q,"type":"inert" if f.inert else "split"})
    # Paired Gauss conversion uses a direct CRT character sum, not its formula.
    paired_reports = []
    for fa,fb in combinations(fields,2):
        a,b = fa.element,fb.element
        if not norm(gcd(a,b)) == 1:
            continue
        binv = fa.power(fa.reduce(b),fa.q-2)
        ainv = fb.power(fb.reduce(a),fb.q-2)
        direct = sum(fa.char(x,-1)*fb.char(y)*fa.additive(fa.product(x,binv))*fb.additive(fb.product(y,ainv))
                     for x in fa.values for y in fb.values)/(fa.q*fb.q)**0.5
        aa = complex(a[0]-a[1]/2,a[1]*3**0.5/2)/fa.q**0.5
        ab = complex(b[0]-b[1]/2,b[1]*3**0.5/2)/fb.q**0.5
        A,B = aa.conjugate()*fa.gauss(2),ab.conjugate()*fb.gauss(2)
        ray_factor = root12(gexp(mul(b,rayinv(a))))
        expected = A*B.conjugate()*ray_factor
        near(direct,expected,"paired_gauss_direct_CRT")
        R = root12(gexp(mul(a,b))-gexp(a)-gexp(b))
        near(fb.char_ring(a),R*fa.char_ring(b),"prime_pair_sextic_reciprocity")
        # Independently evaluate gamma2(ab) with its own direct CRT sum.
        direct2 = sum(fa.char(x,2)*fb.char(y,2)*fa.additive(fa.product(x,binv))*fb.additive(fb.product(y,ainv))
                      for x in fa.values for y in fb.values)/(fa.q*fb.q)**0.5
        alphab = aa*ab
        near(alphab.conjugate()*direct2,A*B*fb.char_ring(a,4),"coefficient_CRT_direct")
        negative(abs(direct-A*B.conjugate()*ray_factor.conjugate())>1e-7,"conjugate_paired_ray_factor",{"a":a,"b":b})
        negative(abs(direct-A*B.conjugate())>1e-7,"omit_paired_ray_factor",{"a":a,"b":b})
        paired_reports.append({"a":a,"b":b,"modulus_norm":fa.q*fb.q})
    return prime_reports,paired_reports


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source",type=Path,default=None,
                        help="Optional pinned TeX file; if supplied its SHA256 must equal the audited source hash")
    parser.add_argument("--output",type=Path,default=Path(__file__).with_name("initial_arithmetic_record_20261012.json"))
    args = parser.parse_args()
    actual_source_sha256 = None
    if args.source is not None:
        actual_source_sha256 = hashlib.sha256(args.source.read_bytes()).hexdigest()
        if actual_source_sha256 != EXPECTED_SOURCE_SHA256:
            parser.error("source hash mismatch; expected " + EXPECTED_SOURCE_SHA256 + "; observed " + actual_source_sha256)
    check_bookkeeping()
    check_ray_classes()
    primes,pairs = check_gauss()
    required_negatives = ["drop_common_column_mobius_sign","incorrect_inverse_e_equals_f","drop_one_e_twist_power",
                          "omit_chi_m_f_fourth_power","omit_fh_bicharacter_sign","principal_power_zero_must_be_mask",
                          "omit_prime_mobius_sign","omit_chi_minus_one_convert2","conjugate_paired_ray_factor","omit_paired_ray_factor",
                          "drop_h_v_coprimality_breaks_inverse","drop_g_v_coprimality_breaks_squarefree_f"]
    assert all(NEGATIVE.get(k,{}).get("detected",0)>0 for k in required_negatives)
    record = {"date":"2026-10-12","prepared_for":"Edward Baker","model":"GPT-6 (Codex); inherited configuration",
              "effort":"configured reasoning effort not exposed; not inferred",
              "source_path":None if args.source is None else str(args.source),
              "expected_source_sha256":EXPECTED_SOURCE_SHA256,"source_sha256":actual_source_sha256,
              "source_hash_verified":args.source is not None,
              "script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              "python_version":platform.python_version(),"python_implementation":platform.python_implementation(),
              "source_physical_lines":[[1040,1220],[2690,2890]],"status":"pass",
              "exact_check_count":sum(COUNTS.values()),"exact_checks":COUNTS,
              "floating_tolerance":TOL,"floating_check_count":sum(n for n,_ in ERRORS.values()),
              "floating_checks":{k:{"count":n,"max_abs_error":err} for k,(n,err) in ERRORS.items()},
              "negative_controls":NEGATIVE,"primes":primes,"paired_CRT_moduli":pairs,
              "coverage":{"bookkeeping":"3 primary primes (2 split, 1 inert), all disjoint squarefree b/f, k valuations 0..2, all 6 units; 4374 bijection inputs",
                          "ray_group":"all 12 primary unit classes modulo 12, all pairs and triples; square subgroup modulo 4 computed by ring operations, all four cosets, Gamma square invariance and table",
                          "characters":"all residues and every nonzero exclusion e at 8 primes; principal powers explicitly zero-extended",
                          "paired":"28 unordered pairs of distinct chosen primary primes, direct finite CRT sums, trivial original ray twist nu",
                          "limits":"finite diagnostics only; no analytic Poisson, smoothing, norm-range estimates, asymptotics, general reciprocity proof, or family baseline certified"}}
    args.output.write_text(json.dumps(record,indent=2)+"\n")
    print(json.dumps({"status":record["status"],"source_sha256":record["source_sha256"],
                      "exact_check_count":record["exact_check_count"],"floating_check_count":record["floating_check_count"],
                      "max_abs_error":max(e for _,e in ERRORS.values()),"negative_controls":len(NEGATIVE),"record":str(args.output)},indent=2))


if __name__ == "__main__":
    main()
