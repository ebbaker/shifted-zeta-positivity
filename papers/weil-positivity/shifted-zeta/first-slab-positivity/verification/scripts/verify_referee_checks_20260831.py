#!/usr/bin/env python3
"""
Independent verification of the numerical claims in
WORKING_DRAFT_first_slab_positivity (31 Aug 2026).

Written from the definitions in the draft's sections 4.2, 5.1, 5.2, 6.2 only;
no code from the primary or clean-room implementations was consulted.
Requires: mpmath, numpy, scipy.   Run:  python3 verify_referee_checks_20260831.py

NOTE (5 Sept 2026): the constants 0.024587, 1.5053999819194765 and the
"draft certified minima" below are those of the 31 Aug draft and are
superseded in preprint v1.0 (kernel bound 0.012294, d_tail 1.5176929819194764,
margins 6.116350109501e-4 / 5.261670009275e-2). The script is kept as the
record of the round-1 recomputation.
"""
import numpy as np, mpmath as mp
from scipy.special import spherical_jn, spherical_in, eval_legendre
mp.mp.dps = 30
LOG2 = float(np.log(2.0)); LOGPI = float(np.log(np.pi))
LAM = 30.0; BSTAR = float(np.log(LAM/(2*np.pi)) - 1/LAM)

# ---------------------------------------------------------------- profiles
def Rprof(t):  return np.exp(t/2) - np.exp(-5*t/2)/(1-np.exp(-2*t))
def Rmp(t):    return mp.e**(t/2) - mp.e**(-5*t/2)/(1-mp.e**(-2*t))

_wc = {}
def w0(tau):                              # archimedean Weil multiplier
    k = round(tau, 12)
    if k not in _wc:
        _wc[k] = float(mp.re(mp.digamma(mp.mpf(0.25)+1j*mp.mpf(tau)/2))) - LOGPI
    return _wc[k]

def panels(a, b, npan, nq):
    x, w = np.polynomial.legendre.leggauss(nq); e = np.linspace(a, b, npan+1)
    T, W = [], []
    for u, v in zip(e[:-1], e[1:]):
        T.append((v-u)/2*x + (u+v)/2); W.append((v-u)/2*w)
    return np.concatenate(T), np.concatenate(W)

# --------------------------------------------- head matrix of Q_{omega,L}
def head(L, ns, sigma, omega=0.0, floor=False, LB=10000.0):
    """Legendre head block of Q_{omega,L} on I_L=(-L/2,L/2).
       floor=True  -> replace w0 by beta_* for |tau|>LAM (the draft's construction,
                      a rigorous lower bound); floor=False -> integrate to LB."""
    T0 = L/2
    if floor:
        taus, wts = panels(0, LAM, 60, 40); W = np.array([w0(t)-BSTAR for t in taus])
    else:
        t1,w1 = panels(0,60,120,32); t2,w2 = panels(60,LB,400,24)
        taus, wts = np.concatenate([t1,t2]), np.concatenate([w1,w2])
        W = np.array([w0(t) for t in taus])
    B = np.array([np.sqrt(2*T0*(2*n+1))*spherical_jn(n, T0*taus) for n in ns])
    M = (B*(wts*W)) @ B.T * 2/(2*np.pi)
    eps = np.array([(-1)**(n//2) for n in ns], float)
    M = np.outer(eps, eps)*M
    if floor: M = M + BSTAR*np.eye(len(ns))
    p = np.array([np.sqrt(2*T0*(2*n+1))*spherical_in(n, T0/2) for n in ns])
    M = M + 2*sigma*np.outer(p, p)
    if omega > 0: M = M + pert(L, ns, omega)
    return M

def pert(L, ns, omega, nu=300, nr=80, scale=1.0):
    """C_omega block via the exact Legendre-correlation reduction of sec 6.2."""
    xu, wu = np.polynomial.legendre.leggauss(nu); u = (xu+1)/2; wu = wu/2
    xr, wr = np.polynomial.legendre.leggauss(nr)
    t = L*u; g = (np.cosh(omega*t)-1)*Rprof(t)*scale
    P = np.zeros((len(ns), len(ns)))
    for k in range(nu):
        uu = u[k]; a, b = -1.0, 1.0-2*uu
        r = (b-a)/2*xr + (a+b)/2; wg = (b-a)/2*wr
        A  = np.array([eval_legendre(n, r+2*uu) for n in ns])
        Bm = np.array([eval_legendre(n, r)      for n in ns])
        P += wu[k]*g[k]*0.5*((A*wg)@Bm.T + (Bm*wg)@A.T)
    s = np.sqrt(2*np.array(ns)+1.0)
    return np.outer(s, s)*P*L

EV = list(range(0, 32, 2)); OD = list(range(1, 33, 2))
lmin = lambda M: np.linalg.eigvalsh(M)[0]

print("="*74); print("1. sign change of R and the Schur constant"); print("="*74)
t0 = mp.findroot(Rmp, mp.mpf('0.28'))
print(f"   t0 = {mp.nstr(t0,25)}   (draft 0.2811995743229618465)")
print(f"   exp(t0) = {mp.nstr(mp.e**t0,20)}  = plastic number, root of x^3=x+1")
gk = lambda u: (mp.cosh(u/2)-1)*Rmp(u)
S = mp.quad(lambda u: abs(gk(u)), [0, t0, mp.log(2)])
print(f"   sup_x int_I |c_(1/2)(x,y)| dy = {mp.nstr(S,20)}")
print(f"   draft sec 6.3 kernel bound    = 0.02458610080228464  = {mp.nstr(mp.mpf('0.02458610080228464')/S,6)} x")

print("="*74); print("2. tail floor and Schur loss"); print("="*74)
bs = mp.log(30/(2*mp.pi)) - mp.mpf(1)/30
print(f"   beta_* = {mp.nstr(bs,20)}    beta_*-0.024587 = {mp.nstr(bs-mp.mpf('0.024587'),20)}")
print( "   draft d_tail                                  = 1.5053999819194765  (=> delta_central = 0)")
for nm, k in [("even",1.4084884e-9), ("odd",2.2191643e-10)]:
    print(f"   reconstructed Schur loss {nm:<5}= {(0.024587+k)**2/1.5053999819194765:.15e}")
print( "   draft                    even = 4.01568118454612e-04   odd = 4.01568079695150e-04")
sharp = float(S); d2 = float(bs)-sharp
print(f"   with the sharp constant: d_tail={d2:.10f}  loss={(sharp+1.4084884e-9)**2/d2:.6e}")

print("="*74); print("3. independent reconstruction of the certificate (L=log2)"); print("="*74)
for nm, ns, sg in [("even", EV, 1.0), ("odd", OD, -1.0)]:
    Q0 = head(LOG2, ns, sg, floor=True)
    Qh = Q0 + pert(LOG2, ns, 0.5); Qd = Q0 + pert(LOG2, ns, 0.5, scale=2.0)
    print(f"   {nm:<5} lam_min(Q0)={lmin(Q0):.8e}   lam_min(Q0+C_1/2)={lmin(Qh):.8e}")
    print(f"         margin after Schur loss = {lmin(Qh)-4.01568118454612e-4:.6e}"
          f"   |  with kernel doubled: {lmin(Qd)-4.01568118454612e-4:+.6e}")
print( "   draft certified minima: even 3.096538790814e-04   odd 5.231471898041e-02")

print("="*74); print("4. positivity horizon (untruncated frequency integral)"); print("="*74)
print("   window sweep, omega=0:")
for L in [0.60, LOG2, 0.75, 0.80, 0.90, float(np.log(3))]:
    print(f"     L={L:<9.6f} even={lmin(head(L,EV,1.0)):+.5e}  odd={lmin(head(L,OD,-1.0)):+.5e}")
print("   shift sweep, L=log2:")
for om in [0.0, 0.5, 0.75, 0.861, 1.0, 1.8]:
    print(f"     omega={om:<6} even={lmin(head(LOG2,EV,1.0,om)):+.5e}  odd={lmin(head(LOG2,OD,-1.0,om)):+.5e}")

print("="*74); print("5. the omega=1/2 endpoint anomaly in the sec 4.2 representation"); print("="*74)
mp.mp.dps = 20; H = mp.log(2)/2
def compare(f, om):
    fh = lambda t: mp.quad(lambda x: f(x)*mp.cos(t*x), [-H, 0, H])
    Cc = lambda c: mp.quad(lambda x: f(x)*mp.cosh(c*x), [-H, 0, H])
    W  = lambda o,t: (mp.re(mp.digamma((mp.mpf(1)/2-o+1j*t)/2))/2
                    + mp.re(mp.digamma((mp.mpf(1)/2+o+1j*t)/2))/2 - mp.log(mp.pi))
    F = mp.quad(lambda t:(W(om,t)-W(0,t))*fh(t)**2, [0,1,4,15,60,200,1000])*2/(2*mp.pi)
    F += Cc(mp.mpf(1)/2-om)**2 + Cc(mp.mpf(1)/2+om)**2 - 2*Cc(mp.mpf(1)/2)**2
    ck = lambda u: 0 if u < mp.mpf('1e-18') else (mp.cosh(om*u)-1)*Rmp(u)
    rho = lambda u: 2*mp.quad(lambda r: f(r)*f(r+u), [-H, H-u])
    K = mp.quad(lambda u: ck(u)*rho(u), [0, mp.log(2)/2, mp.log(2)])
    return F, K
for om in ['0.3', '0.45', '0.5']:
    F, K = compare(lambda x: mp.mpf(1), mp.mpf(om))
    print(f"   f=1, omega={om:<5} Fourier={mp.nstr(F,12):>14} kernel={mp.nstr(K,12):>14}"
          f"  diff={mp.nstr(F-K,8)}")
print(f"   (int f)^2 / 2 = {mp.nstr((2*H)**2/2,10)}  <- the missing -pi*delta(tau) at omega=1/2")
