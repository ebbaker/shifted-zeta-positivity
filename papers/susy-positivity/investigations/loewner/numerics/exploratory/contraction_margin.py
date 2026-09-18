"""
The compressed transfer V_{omega,L} assembled from the elementary kernel, and its contraction data.
Unregistered (mpmath).  Written by Claude Fable 5.1, 17 September 2026, for the opening note of the
Loewner investigation (item 1 of its plan) -- a first, exploratory version of the registered assembly.

Galerkin matrix in the orthonormal sine basis e_j(x) = sqrt(2/L) sin(j pi (x + L/2)/L) on I_L:
    V_jk = <e_j, V e_k> = int_0^L k_omega(t) S_jk(t) dt,   S_jk(t) = int_{-L/2+t}^{L/2} e_j(x) e_k(x-t) dx  (closed form),
because V is a causal convolution.  k_omega is assembled as in transfer_kernel.py (R-form); the t-integral is
done with a fixed double-exponential (tanh-sinh) rule on each interval between consecutive atoms log n, after the
substitution t = t_0 + u^{1/omega} that removes the (t - t_0)^{omega-1} singularity at the left endpoint, with the kernel
evaluated in the local coordinate so that the spike's mass at t - t_0 ~ 1e-100 is not lost to cancellation.

Outputs: ||V||, lambda_min(D) with D = I - V^T V, the ratio lambda_min(D)/(2 omega) against m_L = lambda_min(Q_{0,L})
computed in the same basis by weil_sine_basis.py (from the Wilson-lines exploratory folder), and the first-order
check (||f||^2 - ||V f||^2)/(2 omega) -> Q_{0,L}[f] on f = e_1.

Usage: python3 contraction_margin.py omega L N [1/h] [Nbig]   e.g.  python3 contraction_margin.py 0.01 log3 16 16   (L = log 3 exactly; atoms with log n < L)
With Nbig > N the matrix is assembled at Nbig and, besides the plain N x N Galerkin defect I - V_N^T V_N, the NESTED defect
I_N - (V_Nbig^T V_Nbig)[:N,:N] = P_N (I - V^* P_Nbig V) P_N is reported: it approximates the exact compressed defect P_N D P_N
better than the plain one (which overestimates it by P_N V^*(I-P_N)V P_N, a term of first order in omega on the minimizer).
"""
import sys, json, time, math
import mpmath as mp
sys.path.insert(0, '../../../wilson-lines/numerics/exploratory')
import weil_sine_basis as wsb

mp.mp.dps = 40
om = mp.mpf(sys.argv[1]); Lf = mp.log(int(sys.argv[2][3:])) if sys.argv[2].startswith('log') else mp.mpf(sys.argv[2]); N = int(sys.argv[3]); NGL = int(sys.argv[4]) if len(sys.argv) > 4 else 16; Nbig = int(sys.argv[5]) if len(sys.argv) > 5 else N
half = mp.mpf(1)/2; a, b = half - om, half + om; L = Lf; al = mp.pi/L

# ---- kernel (as transfer_kernel.py) ----
def ngam(x):   x = mp.mpf(x); return mp.e**(-x/2)/(-mp.expm1(-2*x)) if x > 0 else mp.mpf(0)
def kGamma(x): x = mp.mpf(x); return 2*mp.pi**om/mp.gamma(om)*(2*mp.sinh(x))**om*ngam(x) if x > 0 else mp.mpf(0)
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
atoms = [n for n in range(1, 10**6) if mp.log(n) < L]       # n = 1 is the atom at 0
CT = {n: ct(n) for n in atoms}
def J(cc, t): return quad_sing(lambda u: mp.e**(cc*(t-u))*kGamma(u), t) if t > 0 else mp.mpf(0)
def k_full(x):
    x = mp.mpf(x); tot = mp.mpf(0)
    for n in atoms:
        t = x - mp.log(n)
        if t <= 0: break
        tot += CT[n]*(kGamma(t) - 4*om*b*J(-b, t) - 4*om*a*J(a, t))
    return tot

# ---- closed-form one-sided autocorrelations of the sine basis ----
def S(j, k, t):
    t = mp.mpf(t)
    if j == k:
        return ((L-t)*mp.cos(k*al*t) + mp.sin(k*al*t)/(k*al))/L
    sg = (-1)**(j+k)
    A = (sg*mp.sin(k*al*t) - mp.sin(j*al*t))/((j-k)*al)
    B = (-sg*mp.sin(k*al*t) - mp.sin(j*al*t))/((j+k)*al)
    return (A - B)/L
# spot-check S against quadrature
def e(j, x): return mp.sqrt(2/L)*mp.sin(j*al*(x+L/2))
chkS = 0
for (j, k, t) in ((1, 1, mp.mpf('0.3')), (1, 2, mp.mpf('0.5')), (3, 5, mp.mpf('0.2')), (4, 4, mp.mpf('0.9'))):
    direct = mp.quad(lambda x: e(j, x)*e(k, x-t), [-L/2+t, L/2])
    chkS = max(chkS, abs(direct - S(j, k, t)))

# ---- double-exponential rule on each inter-atom interval, in the local coordinate tau = t - log n0 ----
# Substitution tau = u^{1/omega} removes the tau^{omega-1} singularity at the left endpoint; the kernel is
# evaluated in LOCAL coordinates so that the spike's mass at tau ~ 1e-100 is not lost to cancellation.
t0 = time.time()
def de_rule(lo, hi, h, M):
    out = []; c = (hi-lo)/2; m = (lo+hi)/2
    for kk in range(-M, M+1):
        sh = mp.pi/2*mp.sinh(kk*h); x = mp.tanh(sh); w = h*mp.pi/2*mp.cosh(kk*h)/mp.cosh(sh)**2
        out.append((m + c*x, c*w))
    return out
def kern1(tau):              # single-atom kernel at local separation tau > 0
    return kGamma(tau) - 4*om*b*J(-b, tau) - 4*om*a*J(a, tau)
def k_local(n0, tau):        # k(log n0 + tau): atom n0 at tau exactly, earlier atoms at (log n0 - log m) + tau
    tot = CT[n0]*kern1(tau)
    for m in atoms:
        if m >= n0: break
        tot += CT[m]*kern1((mp.log(n0) - mp.log(m)) + tau)
    return tot
H = mp.mpf(1)/NGL                                        # DE step; NGL is reused as 1/h (e.g. 16)
M = int(4.5*NGL)
tvals, wvals, kvals = [], [], []
for i, n0 in enumerate(atoms):
    lo = mp.log(n0); hi = mp.log(atoms[i+1]) if i+1 < len(atoms) else L
    U = (hi-lo)**om
    for (u, w) in de_rule(mp.mpf(0), U, H, M):
        if u <= 0 or u >= U or w < mp.mpf(10)**(-mp.mp.dps-5): continue
        tau = u**(1/om); jac = u**(1/om-1)/om
        tvals.append(lo + tau); wvals.append(w*jac); kvals.append(k_local(n0, tau))
t_kernel = time.time()-t0
mass = mp.fsum(w*kv for (w, kv) in zip(wvals, kvals))

# ---- V matrix ----
Vbig = mp.zeros(Nbig, Nbig)
for j in range(1, Nbig+1):
    for k in range(1, Nbig+1):
        Vbig[j-1, k-1] = mp.fsum(w*kv*S(j, k, t) for (t, w, kv) in zip(tvals, wvals, kvals))
V = Vbig[0:N, 0:N]                                        # plain N x N Galerkin block
VtV = V.T*V
D = mp.eye(N) - VtV
ev_VtV = mp.eigsy(VtV, eigvals_only=True)
normV = mp.sqrt(max(ev_VtV)); lam_min_D = min(1 - x for x in ev_VtV)
nested = None
if Nbig > N:                                              # nested defect P_N (I - V^* P_Nbig V) P_N
    VtVbig = (Vbig.T*Vbig)[0:N, 0:N]
    ev_nested = mp.eigsy(VtVbig, eigvals_only=True)
    lam_min_nested = min(1 - x for x in ev_nested)
    nested = {"Nbig": Nbig, "lambda_min_nested_D": float(lam_min_nested),
              "lambda_min_nested_D_over_2omega": float(lam_min_nested/(2*om))}

# ---- Q_{0,L} in the same basis (even and odd blocks) ----
W = wsb.WeilForm(L, N)
comb = wsb.prime_comb(L)
Me, idxe = W.matrix(comb, 0); Mo, idxo = W.matrix(comb, 1)
mL_even = min(mp.eigsy(Me, eigvals_only=True)); mL_odd = min(mp.eigsy(Mo, eigvals_only=True))
Q_e1 = Me[0, 0]                                           # e_1 is the first even mode
f = mp.zeros(N, 1); f[0] = 1
Vf = V*f; nVf2 = mp.fsum(Vf[i]**2 for i in range(N))
first_order = (1 - nVf2)/(2*om)

out = {"omega": float(om), "L": float(L), "N": N, "de_step_inverse": NGL, "mass_on_0_L": float(mass), "atoms": atoms,
       "S_closed_form_vs_quadrature_worst": float(chkS),
       "kernel_evaluations": len(tvals), "kernel_time_s": round(t_kernel, 1),
       "norm_V": float(normV), "one_minus_norm_V": float(1 - normV),
       "lambda_min_D": float(lam_min_D), "lambda_min_D_over_2omega": float(lam_min_D/(2*om)),
       "m_L_even_block_same_basis": float(mL_even), "m_L_odd_block_same_basis": float(mL_odd),
       "ratio_lamD_over_2om_to_mL": float(lam_min_D/(2*om)/min(mL_even, mL_odd)),
       "first_order_check_e1": {"(1-||Ve1||^2)/(2omega)": float(first_order), "Q[e1]": float(Q_e1), "ratio": float(first_order/Q_e1)},
       "nested_defect": (dict(nested, ratio_to_mL=float(nested["lambda_min_nested_D"]/(2*om)/min(mL_even, mL_odd))) if nested else None),
       "total_time_s": round(time.time()-t0, 1)}
print(json.dumps(out, indent=1))
