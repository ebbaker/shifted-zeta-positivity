"""
The causal kernel of the shifted Weil transfer, assembled from elementary pieces.
Unregistered (mpmath).  Written by Claude Fable 5.1, 17 September 2026, for
the Wilson-lines note notes/LOEWNER_AND_THE_MARKOV_DECOMPOSITION_20260917.md, from which this investigation was opened;
the living copy is this one, in investigations/loewner/numerics/exploratory/.

With s = 1/2 + p, Lambda(u) = pi^{-u/2} Gamma(u/2) zeta(u), xi(u) = u(u-1)Lambda(u)/2:

  K_omega(p) = xi(s-om)/xi(s+om) = R(p) * Ktilde(p),
  Ktilde(p)  = Lambda(s-om)/Lambda(s+om) = KGamma(p) * Kzeta(p),
  KGamma(p)  = pi^om Gamma((s-om)/2)/Gamma((s+om)/2)
             = Laplace transform of  kGamma(x) = (2 pi^om / Gamma(om)) (2 sinh x)^om n_gamma(x),  x > 0,
               n_gamma(x) = e^{-x/2}/(1-e^{-2x});   a Beta-type probability kernel up to normalisation,
  Kzeta(p)   = zeta(s-om)/zeta(s+om) = sum_n c_n n^{-s},   c_n = n^om prod_{p|n} (1 - p^{-2 om}) > 0,
             = Laplace transform (in p, s = 1/2+p) of the comb  sum_n ct_n delta_{log n},  ct_n = c_n n^{-1/2},
  R(p)       = (p+a)(p-b)/((p+b)(p-a)) = 1 - 4 om b/(p+b) - 4 om a/(p-a),   a = 1/2-om, b = 1/2+om,
             = Laplace transform of  r = delta_0 - 4 om b e^{-b x} - 4 om a e^{a x}.

So ktilde = kGamma * (sum_n ct_n delta_{log n}) is a POSITIVE measure (Ktilde is completely
monotone on p > 1/2+om), and k_omega = r * ktilde is that positive measure minus two
exponential convolutions of it: the whole non-Markov part of the transfer is the rank-two
pole factor R, i.e. the s(s-1) of xi.

Checks (JSON to stdout):
  A  kGamma integrates to KGamma(p) at real p (quadrature vs Gamma ratio);
  B  Dirichlet coefficients c_n are positive and sum to Kzeta(p) (against mpmath zeta);
  C  R(p) Ktilde(p) = K_omega(p) at complex p (algebraic identity, mpmath xi);
  D  complete monotonicity of Ktilde: (-1)^k d^k/dp^k Ktilde(p) > 0, k <= 6;
  E  the first-order law k_omega(x)/om -> 2 n_gamma(x) - 4 cosh(x/2) off the atoms, and the
     sign structure of k_omega on (0, L): positive near 0, negative beyond x_0 ~ 0.281 at small om,
     positive atoms at log n;
  F  table of k_omega on a grid for the note.

Usage: python3 transfer_kernel.py [omega=0.1] [L=2.5]
"""
import sys, json, math
import mpmath as mp
mp.mp.dps = 30

om = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf('0.1')
Lf = float(sys.argv[2]) if len(sys.argv) > 2 else 2.5
a, b = mp.mpf(1)/2 - om, mp.mpf(1)/2 + om

def Lam(u):  return mp.pi**(-u/2)*mp.gamma(u/2)*mp.zeta(u)
def xi(u):   return u*(u-1)/2*Lam(u)
def K(p):    return xi(mp.mpf(1)/2+p-om)/xi(mp.mpf(1)/2+p+om)
def Ktilde(p): return Lam(mp.mpf(1)/2+p-om)/Lam(mp.mpf(1)/2+p+om)
def KGamma(p): s = mp.mpf(1)/2+p; return mp.pi**om*mp.gamma((s-om)/2)/mp.gamma((s+om)/2)
def Kzeta(p):  s = mp.mpf(1)/2+p; return mp.zeta(s-om)/mp.zeta(s+om)
def R(p):    return (p+a)*(p-b)/((p+b)*(p-a))
def ngam(x):
    x = mp.mpf(x)
    return mp.e**(-x/2)/(-mp.expm1(-2*x)) if x > 0 else mp.mpf(0)
def kGamma(x):
    x = mp.mpf(x)
    if x <= 0: return mp.mpf(0)
    return 2*mp.pi**om/mp.gamma(om)*(2*mp.sinh(x))**om*ngam(x)


def quad_sing(f, T):
    """int_0^T f(x) dx for f ~ x^(om-1) at 0: substitute x = t^(1/om) on [0, min(T,1)]."""
    T = mp.mpf(T)
    if T <= 0: return mp.mpf(0)
    T1 = min(T, mp.mpf(1))
    g = lambda t: f(t**(1/om))*t**(1/om-1)/om
    val = mp.quad(g, [0, T1**om])
    if T > 1: val += mp.quad(f, [1, T])
    return val

def factor(n):
    f = {}; d = 2
    while d*d <= n:
        while n % d == 0: f[d] = f.get(d, 0)+1; n //= d
        d += 1
    if n > 1: f[n] = f.get(n, 0)+1
    return f
def c(n):
    v = mp.mpf(n)**om
    for p in factor(n): v *= (1 - mp.mpf(p)**(-2*om))
    return v

out = {"omega": float(om), "L": Lf, "a": float(a), "b": float(b), "checks": {}}

# A: Laplace transform of kGamma
worstA = 0
for p in (mp.mpf('0.7'), mp.mpf(1), mp.mpf(2), mp.mpf(3.5)):
    lhs = quad_sing(lambda x: mp.e**(-p*x)*kGamma(x), 60)
    rel = abs(lhs/KGamma(p)-1); worstA = max(worstA, rel)
out["checks"]["A_kGamma_laplace"] = {"worst_rel": float(worstA), "pass": worstA < 1e-20}

# B: Dirichlet coefficients positive, Dirichlet series = Kzeta
N = 20000
cs = [None] + [c(n) for n in range(1, N+1)]
allpos = all(cs[n] > 0 for n in range(1, N+1))
worstB = 0
for p in (mp.mpf(2), mp.mpf(3), mp.mpf(4)):
    s = mp.mpf(1)/2+p
    ser = mp.fsum(cs[n]*mp.mpf(n)**(-s) for n in range(1, N+1))
    tail = float(N**(1+om-s.real)/(s.real-1-om))   # crude tail bound sum_{n>N} n^{om-s}
    rel = abs(ser/Kzeta(p)-1); worstB = max(worstB, rel)
    out["checks"].setdefault("B_dirichlet", {})[str(float(p))] = {"rel": float(rel), "tail_bound": tail}
out["checks"]["B_dirichlet"]["all_c_n_positive_to_N"] = allpos
out["checks"]["B_dirichlet"]["N"] = N
out["checks"]["B_dirichlet"]["c_n_first_12"] = [float(cs[n]) for n in range(1, 13)]
out["checks"]["B_dirichlet"]["ct_n_first_12_x_weights"] = [float(cs[n]/mp.sqrt(n)) for n in range(1, 13)]
out["checks"]["B_dirichlet"]["first_order_atom_masses_2omLambda_n_sqrt"] = [float(2*om*(mp.log(list(factor(n))[0]) if len(factor(n))==1 else 0)/mp.sqrt(n)) for n in range(2, 13)]

# C: R * Ktilde = K at complex p, and the partial fractions of R
worstC = 0
for p in (mp.mpc(2, 0), mp.mpc(2, 7), mp.mpc(0.3, 25), mp.mpc(1.1, -3), mp.mpc(0, 14.1)):
    worstC = max(worstC, abs(R(p)*Ktilde(p)/K(p)-1))
    pf = 1 - 4*om*b/(p+b) - 4*om*a/(p-a)
    worstC = max(worstC, abs(pf/R(p)-1))
out["checks"]["C_R_times_Ktilde_equals_K"] = {"worst_rel": float(worstC), "pass": worstC < 1e-20}

# D: complete monotonicity of Ktilde on p > 1/2 + om
cm_ok = True; dvals = {}
for p in (mp.mpf(1), mp.mpf('1.5'), mp.mpf(3)):
    row = []
    for k in range(0, 7):
        d = mp.diff(Ktilde, p, k) * (-1)**k
        row.append(float(d)); cm_ok = cm_ok and d > 0
    dvals[str(float(p))] = row
out["checks"]["D_complete_monotonicity"] = {"signed_derivatives": dvals, "all_positive": cm_ok}

# E/F: the kernel on (0, L)
def ktilde(x):
    x = mp.mpf(x); tot = mp.mpf(0); n = 1
    while mp.log(n) < x:
        u = x - mp.log(n)
        tot += cs[n]*mp.mpf(n)**(-mp.mpf(1)/2)*kGamma(u); n += 1
    return tot
def J(cc, t):   # int_0^t e^{cc (t-u)} kGamma(u) du   (endpoint singularity u^{om-1})
    if t <= 0: return mp.mpf(0)
    return quad_sing(lambda u: mp.e**(cc*(t-u))*kGamma(u), t)
def k_full(x):
    x = mp.mpf(x); tot = ktilde(x); n = 1
    while mp.log(n) < x:
        t = x - mp.log(n)
        tot -= cs[n]*mp.mpf(n)**(-mp.mpf(1)/2)*(4*om*b*J(-b, t) + 4*om*a*J(a, t)); n += 1
    return tot
def first_order(x):
    x = mp.mpf(x); return 2*ngam(x) - 4*mp.cosh(x/2)

grid = [0.05, 0.1, 0.2, 0.281, 0.3, 0.4, 0.5, 0.6, 0.65, 0.72, 0.8, 0.9, 1.0, 1.05, 1.15, 1.3, 1.35, 1.45, 1.55, 1.65, 1.75, 1.85, 1.9, 1.98, 2.1, 2.3, 2.5, 2.8, 3.0]
grid = [x for x in grid if x < Lf]
table = []
for x in grid:
    kv = k_full(x); kt = ktilde(x)
    table.append({"x": x, "k": float(kv), "ktilde": float(kt), "k_over_omega": float(kv/om), "first_order": float(first_order(x))})
out["F_kernel_table"] = table
# sign changes of k on the continuous part
signs = [(row["x"], row["k"] > 0) for row in table]
changes = [(signs[i][0], signs[i+1][0]) for i in range(len(signs)-1) if signs[i][1] != signs[i+1][1]]
out["E_sign_changes_of_k_between"] = changes
# root of the first-order continuous kernel: u^3 + u^2 = 1, x0 = -log u
u0 = mp.findroot(lambda u: u**3+u**2-1, 0.75); out["E_first_order_root_x0"] = float(-mp.log(u0))
# mass checks: int_0^L of ktilde and of k against the truncated Laplace transform at p=0 is not
# meaningful (infinite mass); instead record the small-x law k ~ (2pi)^om/Gamma(om) x^{om-1}
xs = mp.mpf('1e-3'); out["E_small_x_ratio"] = float(k_full(xs)/((2*mp.pi)**om/mp.gamma(om)*xs**(om-1)))

# G: kernel-level check.  Truncated Laplace transform of the assembled k on [0, X] against K(p);
#    the difference is the tail int_X^inf e^{-px} k, which must shrink with X.  Uses
#    T_q(X) = int_0^X e^{-qy} ktilde(y) dy = sum_{n<e^X} c_n n^{-q} Phi_q(X - log n),
#    and int_0^X e^{-px} (e^{c.} * ktilde)(x) dx = [T_p(X) - e^{-(p-c)X} T_c(X)]/(p-c).
def Phi(q, t):
    return quad_sing(lambda u: mp.e**(-q*u)*kGamma(u), t) if t > 0 else mp.mpf(0)
def T(q, X):
    tot = mp.mpf(0); n = 1
    while mp.log(n) < X:
        tot += cs[n]*mp.mpf(n)**(-q-mp.mpf(1)/2)*Phi(q, X - mp.log(n)); n += 1
    return tot
G = {}
for pp in (mp.mpf(3), mp.mpf(5)):
    row = {}
    for X in (mp.mpf(2), mp.mpf(3), mp.mpf(4)):
        Tp = T(pp, X)
        val = Tp
        for cc, gam in ((-b, 4*om*b), (a, 4*om*a)):
            val -= gam*(Tp - mp.e**(-(pp-cc)*X)*T(cc, X))/(pp-cc)
        row[str(float(X))] = {"truncated_transform": float(val), "K": float(K(pp)), "diff": float(val - K(pp))}
    G[str(float(pp))] = row
out["checks"]["G_kernel_laplace_truncated"] = G

print(json.dumps(out, indent=1))
