"""
Checks for the opening note of the Loewner investigation
(notes/MARKOV_PART_AND_REALIZATIONS_20260917.md).  Unregistered (mpmath, 30 digits).
Written by Claude Fable 5.1, 17 September 2026.

  s = 1/2 + p,  a = 1/2 - om,  b = 1/2 + om,  Lambda(u) = pi^{-u/2} Gamma(u/2) zeta(u).
  Ktilde = Lambda(s-om)/Lambda(s+om)          (completely monotone on p > b)
  Khat   = (p+a)/(p-a) * Ktilde               (also completely monotone on p > b)
  K      = B_b * Khat,   B_b = (p-b)/(p+b)    (one first-order all-pass section at the pole of zeta)
so the transfer kernel is  k = khat - 2 EMA_b[khat],  EMA_b[g](x) = b int_0^x e^{-b(x-y)} g(y) dy,
with khat >= 0.

Groups: 1 Khat completely monotone;  2 K = B_b Khat at complex p;  3 the omega = 1/2 endpoint:
Ktilde_{1/2}(p) = Lambda(p)/Lambda(p+1) is the Eisenstein scattering matrix phi((p+1)/2) of
PSL(2,Z), Khat_{1/2} = Ktilde_{1/2}, and the comb weights are Euler's totient over n;
4 the BESQ/Beta reading KGamma = pi^om Gamma(a/2)/Gamma(b/2) E[U^{p/2}], U ~ Beta(a/2, om);
5 the EMA identity at the kernel level against the assembled k of transfer_kernel.py;
6 first-order comb weights.
Usage: python3 decomposition_checks.py [omega=0.1]
"""
import sys, json, math
import mpmath as mp
from fractions import Fraction
mp.mp.dps = 30
om = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf('0.1')
a, b = mp.mpf(1)/2 - om, mp.mpf(1)/2 + om
half = mp.mpf(1)/2

def Lam(u):  return mp.pi**(-u/2)*mp.gamma(u/2)*mp.zeta(u)
def xi(u):   return u*(u-1)/2*Lam(u)
def K(p, w=om):      return xi(half+p-w)/xi(half+p+w)
def Ktilde(p, w=om): return Lam(half+p-w)/Lam(half+p+w)
def Khat(p, w=om):
    aa = half - w
    return (p+aa)/(p-aa)*Ktilde(p, w) if aa != 0 else Ktilde(p, w)
def Bb(p, w=om):     bb = half + w; return (p-bb)/(p+bb)
def KGamma(p, w=om): s = half+p; return mp.pi**w*mp.gamma((s-w)/2)/mp.gamma((s+w)/2)
def phi_eis(sp):     return Lam(2*sp-1)/Lam(2*sp)          # Eisenstein scattering matrix, PSL(2,Z)

out = {"omega": float(om), "a": float(a), "b": float(b)}

# 1. complete monotonicity of Khat on p > b
rows = {}; ok = True
for p in (b + mp.mpf('0.2'), mp.mpf(1), mp.mpf(2)):
    row = []
    for k in range(7):
        d = (-1)**k*mp.diff(lambda q: Khat(q), p, k); row.append(float(d)); ok = ok and d > 0
    rows[str(float(p))] = row
out["1_Khat_completely_monotone"] = {"signed_derivatives": rows, "all_positive": ok}

# 2. K = B_b Khat
worst = 0
for p in (mp.mpc(2, 0), mp.mpc(1, 5), mp.mpc(0.2, 30), mp.mpc(0, 14.1), mp.mpc(3, -2)):
    worst = max(worst, abs(Bb(p)*Khat(p)/K(p) - 1))
out["2_K_equals_Bb_Khat"] = {"worst_rel": float(worst), "pass": worst < 1e-20}

# 3. the omega = 1/2 endpoint
w = half; worst3 = 0
for p in (mp.mpc(2, 0), mp.mpc(0, 6.0), mp.mpc(0.3, 17.5)):
    worst3 = max(worst3, abs(Ktilde(p, w)/phi_eis((p+1)/2) - 1))
    worst3 = max(worst3, abs(Khat(p, w)/Ktilde(p, w) - 1))
    worst3 = max(worst3, abs(K(p, w)/(Bb(p, w)*phi_eis((p+1)/2)) - 1))
def c_frac(n, wq):   # c_n = n^w prod_{p|n}(1 - p^{-2w}) at w = 1/2 in exact rationals: n^{1/2} prod (1-1/p)
    # tilde c_n = c_n n^{-1/2} = prod_{p|n}(1-1/p)  at w=1/2
    v = Fraction(1); m = n; d = 2
    while d*d <= m:
        if m % d == 0:
            v *= Fraction(d-1, d)
            while m % d == 0: m //= d
        d += 1
    if m > 1: v *= Fraction(m-1, m)
    return v
def totient(n):
    r = n; m = n; d = 2
    while d*d <= m:
        if m % d == 0:
            r = r//d*(d-1)
            while m % d == 0: m //= d
        d += 1
    if m > 1: r = r//m*(m-1)
    return r
tot_ok = all(c_frac(n, half) == Fraction(totient(n), n) for n in range(1, 200))
out["3_omega_half_endpoint"] = {"Ktilde_is_Eisenstein_phi_worst_rel": float(worst3), "pass": worst3 < 1e-20,
                                "comb_weights_are_totient_over_n_to_199": tot_ok}

# 4. BESQ / Beta reading
worst4 = 0
for p in (mp.mpf('0.5'), mp.mpf(1), mp.mpf(3)):
    EU = mp.beta(a/2 + p/2, om)/mp.beta(a/2, om)              # E[U^{p/2}], U ~ Beta(a/2, om)
    worst4 = max(worst4, abs(mp.pi**om*mp.gamma(a/2)/mp.gamma(b/2)*EU/KGamma(p) - 1))
    # and as a Gamma ratio: U = G_{a/2}/(G_{a/2}+G_{om}), i.e. BESQ(a)/(BESQ(a)+BESQ(2 om)) at a common time
    EU2 = mp.gamma(a/2+p/2)*mp.gamma(a/2+om)/(mp.gamma(a/2+om+p/2)*mp.gamma(a/2))
    worst4 = max(worst4, abs(EU2/EU - 1))
# the Beta density in u = e^{-2x} pulls back to kGamma(x) dx: check at three x
for x in (mp.mpf('0.1'), mp.mpf('0.7'), mp.mpf('2.0')):
    u = mp.e**(-2*x)
    dens = u**(a/2-1)*(1-u)**(om-1)/mp.beta(a/2, om)*2*u          # density in x (du = -2u dx)
    kG = 2*mp.pi**om/mp.gamma(om)*(2*mp.sinh(x))**om*mp.e**(-x/2)/(-mp.expm1(-2*x))
    norm = mp.pi**om*mp.gamma(a/2)/mp.gamma(b/2)                    # total mass KGamma(0)
    worst4 = max(worst4, abs(norm*dens/kG - 1))
out["4_BESQ_Beta_reading"] = {"worst_rel": float(worst4), "pass": worst4 < 1e-20,
                              "dimensions": {"a": float(a), "2omega": float(2*om), "sum_b": float(b)}}

# 5. EMA identity at the kernel level: k = khat - 2 EMA_b[khat], khat = ktilde + 2a e^{a.} * ktilde
def ngam(x):
    x = mp.mpf(x); return mp.e**(-x/2)/(-mp.expm1(-2*x)) if x > 0 else mp.mpf(0)
def kGamma(x):
    x = mp.mpf(x); return 2*mp.pi**om/mp.gamma(om)*(2*mp.sinh(x))**om*ngam(x) if x > 0 else mp.mpf(0)
def quad_sing(f, T):
    T = mp.mpf(T)
    if T <= 0: return mp.mpf(0)
    T1 = min(T, mp.mpf(1)); g = lambda t: f(t**(1/om))*t**(1/om-1)/om
    v = mp.quad(g, [0, T1**om])
    if T > 1: v += mp.quad(f, [1, T])
    return v
def factor(n):
    f = {}; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
def ct(n):
    v = mp.mpf(n)**(om-half)
    for q in factor(n): v *= (1 - mp.mpf(q)**(-2*om))
    return v
NMAX = 20; CT = [None] + [ct(n) for n in range(1, NMAX+1)]
def ktilde(x):
    x = mp.mpf(x); tot = mp.mpf(0); n = 1
    while n <= NMAX and mp.log(n) < x: tot += CT[n]*kGamma(x - mp.log(n)); n += 1
    return tot
def J(cc, t): return quad_sing(lambda u: mp.e**(cc*(t-u))*kGamma(u), t) if t > 0 else mp.mpf(0)
def conv_exp(cc, x):       # (e^{cc .} * ktilde)(x) = sum_n ct_n J(cc, x - log n)
    x = mp.mpf(x); tot = mp.mpf(0); n = 1
    while n <= NMAX and mp.log(n) < x: tot += CT[n]*J(cc, x - mp.log(n)); n += 1
    return tot
def k_R(x):     # k = ktilde - 4 om b e^{-b.}*ktilde - 4 om a e^{a.}*ktilde   (the R decomposition)
    return ktilde(x) - 4*om*b*conv_exp(-b, x) - 4*om*a*conv_exp(a, x)
def khat(x):    # khat = ktilde + 2a e^{a.}*ktilde
    return ktilde(x) + 2*a*conv_exp(a, x)
def k_B(x):     # k = khat - 2 EMA_b[khat] = khat - 2b e^{-b.}*khat
    x = mp.mpf(x)
    # e^{-b.} * khat = e^{-b.}*ktilde + 2a e^{-b.}*e^{a.}*ktilde ;  e^{-b.}*e^{a.} = (e^{a.} - e^{-b.})/(a+b)
    ema = conv_exp(-b, x) + 2*a*(conv_exp(a, x) - conv_exp(-b, x))/(a+b)
    return khat(x) - 2*b*ema
worst5 = 0; pts = {}
for x in (mp.mpf('0.2'), mp.mpf('0.5'), mp.mpf('0.9'), mp.mpf('1.3')):
    kr, kb, kh = k_R(x), k_B(x), khat(x)
    worst5 = max(worst5, abs(kb - kr)); pts[str(float(x))] = {"k_via_R": float(kr), "k_via_Bb": float(kb), "khat": float(kh)}
out["5_EMA_identity_kernel_level"] = {"worst_abs_diff": float(worst5), "pass": worst5 < 1e-24, "khat_positive": all(v["khat"] > 0 for v in pts.values()), "points": pts}

# 6. first-order comb weights at small omega
w0 = mp.mpf('0.01'); rat = {}
def ct_w(n, w):
    v = mp.mpf(n)**(w-half)
    for q in factor(n): v *= (1 - mp.mpf(q)**(-2*w))
    return v
for n in (2, 3, 4, 5, 7, 8, 9):
    Lam_n = mp.log(list(factor(n))[0]) if len(factor(n)) == 1 else mp.mpf(0)
    rat[n] = float(ct_w(n, w0)/(2*w0*Lam_n/mp.sqrt(n)))
rat6 = float(ct_w(6, w0)/(w0**2))
out["6_first_order_comb"] = {"ratio_ct_n_over_2omLambda_n_sqrt_at_om_0.01": rat, "ct_6_over_omega_squared": rat6,
                             "note": "ratios -> 1 as omega -> 0; c_6 is O(omega^2), coefficient 4 log2 log3 6^{-1/2} = %.4f" % float(4*mp.log(2)*mp.log(3)/mp.sqrt(6))}
print(json.dumps(out, indent=1))
