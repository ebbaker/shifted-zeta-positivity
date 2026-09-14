"""
Check 2: boundary representation T_L = b(H_N) + K_L (Theorem 3.1 / D (5.3)), the
image-sum closed form of the kernel of K_L, the column formula (3.3), the entry
formula (3.4), the compressed and full-column tails (6.2)-(6.3), and the pole /
shift entries (6.4)-(6.6).

Independent implementation (mpmath / scipy), not derived from the paper's scripts.
"""
import mpmath as mp, numpy as np
from scipy import integrate, special
mp.mp.dps = 20
out = {}

def a(k): return 2*k + mp.mpf(1)/2
psi14 = mp.digamma(mp.mpf(1)/4)
def b_tau2(t):  # b(tau^2)
    return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*mp.mpf(t)/2)) - psi14
def nfun(t):    # n(t) = sum_k e^{-a_k t}
    return mp.e**(-t/2)/(1-mp.e**(-2*t))

# ---- 2a: kernel of K_L by images  vs  direct mass sum -------------------------
L = mp.mpf('1.3')
def K_images(x, y, M=40):
    return sum(nfun(x+y+2*m*L) + nfun((2*m+2)*L-x-y) + nfun((2*m+2)*L+x-y) + nfun((2*m+2)*L-x+y)
               for m in range(M))
def K_mass(x, y, kmax=4000):
    tot = mp.mpf(0)
    for k in range(kmax):
        ak = a(k); r = mp.e**(-ak*L)
        u = lambda z: mp.e**(-ak*z); v = lambda z: mp.e**(-ak*(L-z))
        tot += (u(x)*u(y)+v(x)*v(y)+r*(u(x)*v(y)+v(x)*u(y)))/(1-r*r)
    # tail of sum_k e^{-a_k(x+y)} etc. beyond kmax is < e^{-a_kmax * min path}; report it
    return tot
pts = [(mp.mpf('0.2'), mp.mpf('0.5')), (mp.mpf('0.9'), mp.mpf('1.1')), (mp.mpf('0.05'), mp.mpf('0.07'))]
err = max(abs(K_images(x, y) - K_mass(x, y)) for x, y in pts)
out['kernel_images_vs_mass_sum_maxerr'] = float(err)
print("2a kernel image-sum vs direct mass sum, max err:", mp.nstr(err, 3))

# ---- 2b: T_L = b(H_N) + K_L on a smooth compactly supported f ------------------
# f = bump exp(-1/(x(L-x))) scaled; use f(x) = x^4 (L-x)^4 (C^3 at ends; cosine coeffs ~ j^-6) instead for speed
def f(x): return (x*(L-x))**4
def Fhat(t):
    return mp.quad(lambda x: f(x)*mp.e**(-1j*t*x), [0, L/2, L])
# Fourier side (with analytic Fhat via repeated integration would be nicer; numeric fine)
pts_t = mp.linspace(0, 80, 161) + [120, 200, 400, 800, mp.inf]
tL_fourier = 2*mp.quad(lambda t: b_tau2(t)*abs(Fhat(t))**2, pts_t)/(2*mp.pi)
# cosine side
def e(j, x):
    nu = 1/mp.sqrt(L) if j == 0 else mp.sqrt(2/L)
    return nu*mp.cos(j*mp.pi*x/L)
J = 60
fj = [mp.quad(lambda x: f(x)*e(j, x), [0, L/2, L]) for j in range(J)]
bj = [b_tau2(j*mp.pi/L) for j in range(J)]
diag_part = sum(bj[j]*fj[j]**2 for j in range(J))
# <f, K_L f> by 2-D quadrature of the image kernel
Kff = mp.quad(lambda x: mp.quad(lambda y: K_images(x, y, M=25)*f(x)*f(y), [0, x, L]), [0, L])
normf2 = mp.quad(lambda x: f(x)**2, [0, L])
cos_side = diag_part + Kff
out['boundary_identity'] = dict(L=float(L), tL_fourier=float(tL_fourier), b_HN_part=float(diag_part),
                                Kff=float(Kff), cosine_side=float(cos_side), diff=float(tL_fourier-cos_side),
                                normf2=float(normf2), cosine_coeff_truncation=float(sum(fj[j]**2 for j in range(J))/normf2-1))
print("2b  t_L[f] (Fourier) =", mp.nstr(tL_fourier, 15))
print("    <f,b(H_N)f> + <f,K_L f> =", mp.nstr(cos_side, 15), " (b part", mp.nstr(diag_part, 10), ", K part", mp.nstr(Kff, 10), ")")
print("    difference =", mp.nstr(tL_fourier-cos_side, 3), "  [cosine coefficient mass missing:", mp.nstr(1-sum(fj[j]**2 for j in range(J))/normf2, 3), "]")

# ---- 2c: column formula K_a e_j and entries -----------------------------------
def Ka_apply_num(aa, j, x):   # (K_a e_j)(x) by quadrature of the kernel
    r = mp.e**(-aa*L)
    u = lambda z: mp.e**(-aa*z); v = lambda z: mp.e**(-aa*(L-z))
    ker = lambda y: (u(x)*u(y)+v(x)*v(y)+r*(u(x)*v(y)+v(x)*u(y)))/(1-r*r)
    return mp.quad(lambda y: ker(y)*e(j, y), [0, L])
def Ka_apply_formula(aa, j, x):
    nu = 1/mp.sqrt(L) if j == 0 else mp.sqrt(2/L); w = j*mp.pi/L
    return nu*aa/(aa*aa+w*w)*(mp.e**(-aa*x) + (-1)**j*mp.e**(-aa*(L-x)))
errs = []
for aa in [a(0), a(3), mp.mpf('7.25')]:
    for j in [0, 1, 2, 5]:
        for x in [mp.mpf('0.1'), mp.mpf('0.77')]:
            errs.append(abs(Ka_apply_num(aa, j, x) - Ka_apply_formula(aa, j, x)))
out['column_formula_maxerr'] = float(max(errs))
print("2c  column formula (3.3) max err:", mp.nstr(max(errs), 3))

# entries (3.4) with 60 masses vs numeric double integral of the 60-mass kernel
def entry_formula(i, j, kmax):
    if (i+j) % 2: return mp.mpf(0)
    nui = 1/mp.sqrt(L) if i == 0 else mp.sqrt(2/L); nuj = 1/mp.sqrt(L) if j == 0 else mp.sqrt(2/L)
    wi, wj = i*mp.pi/L, j*mp.pi/L
    return 2*nui*nuj*sum(a(k)**2*(1-(-1)**j*mp.e**(-a(k)*L))/((a(k)**2+wi**2)*(a(k)**2+wj**2)) for k in range(kmax))
def entry_num(i, j, kmax):
    return mp.quad(lambda x: e(i, x)*sum(Ka_apply_formula(a(k), j, x) for k in range(kmax)), [0, L])
errs = [abs(entry_formula(i, j, 12) - entry_num(i, j, 12)) for i in range(4) for j in range(4)]
out['entry_formula_maxerr'] = float(max(errs))
print("2c  entry formula (3.4), 12 masses, max err:", mp.nstr(max(errs), 3))

# ---- 2d: tails (6.2) compressed, (6.3) full column ------------------------------
# full column tail: || (K_L - K^{(J)}) e_j ||  vs  sqrt(2) nu_j (a_J^{-1/2} + a_J^{-3/2})
def col_tail_norm2(j, Jm, kmax=3000):
    # sum_{k>=Jm}^{kmax} K_{a_k} e_j  as a function, then L2 norm; the omitted part beyond kmax is ~ kmax^{-1/2}
    g = lambda x: sum(Ka_apply_formula(a(k), j, x) for k in range(Jm, kmax))
    return mp.sqrt(mp.quad(lambda x: g(x)**2, [0, L/2, L]))
ratios = []
for j in [0, 1, 3]:
    for Jm in [5, 20]:
        nu = 1/mp.sqrt(L) if j == 0 else mp.sqrt(2/L)
        bound = mp.sqrt(2)*nu*(a(Jm)**(-mp.mpf(1)/2) + a(Jm)**(-mp.mpf(3)/2))
        got = col_tail_norm2(j, Jm, kmax=600)
        ratios.append(float(got/bound))
out['column_tail_ratio_max'] = max(ratios)
print("2d  full-column tail (partial, 600 masses) / bound (6.3): max ratio", max(ratios), "(<1 required)")

# ---- 2e: shift entries (6.4) and pole coefficients (6.5) -------------------------
def I_(lam, phi, aa, bb):
    return (bb-aa)*mp.cos(phi) if lam == 0 else (mp.sin(lam*bb+phi)-mp.sin(lam*aa+phi))/lam
def t_formula(i, j, d):
    nui = 1/mp.sqrt(L) if i == 0 else mp.sqrt(2/L); nuj = 1/mp.sqrt(L) if j == 0 else mp.sqrt(2/L)
    wi, wj = i*mp.pi/L, j*mp.pi/L
    return nui*nuj/2*(I_(wi-wj, wj*d, d, L) + I_(wi+wj, -wj*d, d, L))
def t_num(i, j, d):
    return mp.quad(lambda x: e(i, x)*e(j, x-d), [d, L])
d = mp.log(2)
errs = [abs(t_formula(i, j, d)-t_num(i, j, d)) for i in range(5) for j in range(5)]
out['shift_entry_maxerr'] = float(max(errs))
print("2e  shift entries (6.4) max err:", mp.nstr(max(errs), 3))
def Jj(j, sig):
    w = j*mp.pi/L
    return sig*((-1)**j*mp.e**(sig*L)-1)/(sig*sig+w*w)
def cs_formula(j):
    nu = 1/mp.sqrt(L) if j == 0 else mp.sqrt(2/L)
    return (nu/2*(mp.e**(-L/4)*Jj(j, mp.mpf(1)/2)+mp.e**(L/4)*Jj(j, -mp.mpf(1)/2)),
            nu/2*(mp.e**(-L/4)*Jj(j, mp.mpf(1)/2)-mp.e**(L/4)*Jj(j, -mp.mpf(1)/2)))
def cs_num(j):
    return (mp.quad(lambda x: e(j, x)*mp.cosh((x-L/2)/2), [0, L]), mp.quad(lambda x: e(j, x)*mp.sinh((x-L/2)/2), [0, L]))
errs = []
for j in range(6):
    cf, sf = cs_formula(j); cn, sn = cs_num(j); errs += [abs(cf-cn), abs(sf-sn)]
out['pole_coeff_maxerr'] = float(max(errs))
print("2e  pole coefficients (6.5) max err:", mp.nstr(max(errs), 3))
# pole norms
print("    |c|^2 =", mp.nstr(mp.quad(lambda x: mp.cosh((x-L/2)/2)**2, [0, L]), 12), " vs L/2+sinh(L/2) =", mp.nstr(L/2+mp.sinh(L/2), 12))
print("    |s|^2 =", mp.nstr(mp.quad(lambda x: mp.sinh((x-L/2)/2)**2, [0, L]), 12), " vs -L/2+sinh(L/2) =", mp.nstr(-L/2+mp.sinh(L/2), 12))

import json; json.dump(out, open('chk2.json', 'w'), indent=1)
