"""Independent numerical re-verification of selected manuscript items
(run while preparing the preprint, 5 Sept 2026).

Items: A1 (Prop 4.1 proof steps), A2 (endpoint lemma), A3 (sec 6.3 row-max
analysis + item 0.6), A4 (Volterra identities), 0.3 (block-Schur constant),
C1 partial (Suzuki's g_omega -> transfer normalization).
"""
from mpmath import (mp, mpf, gamma, digamma, quad, exp, cosh, sinh, log, pi,
                    sqrt, euler, inf, findroot, diff, beta, betainc, re, im,
                    mpc, matrix, polyroots)
import numpy as np

mp.dps = 40
out = []
def rep(label, ok, detail=""):
    out.append((label, ok, detail))
    print(("PASS " if ok else "FAIL ") + label + ("  " + detail if detail else ""))

# ---------------------------------------------------------------- helpers
def Gamma_inf(s):
    return mpf(1)/2 * s*(s-1) * pi**(-s/2) * gamma(s/2)

def K(omega, p):
    return Gamma_inf(mpf(1)/2 + p - omega) / Gamma_inf(mpf(1)/2 + p + omega)

def a_mult(omega, p):
    al = mpf(1)/2 - omega; be = mpf(1)/2 + omega
    return (1/(p+al) + 1/(p-al) + 1/(p+be) + 1/(p-be) - log(pi)
            + digamma((p+al)/2)/2 + digamma((p+be)/2)/2)

def R(t):
    return exp(t/2) - exp(-5*t/2)/(1-exp(-2*t))

# ================================================================ A1: Prop 4.1
print("\n=== A1: Proposition 4.1 proof steps ===")
p = mpf('2.3'); omega = mpf('0.3')
al = mpf(1)/2 - omega; be = mpf(1)/2 + omega

# step 0: a_omega = l'(p-omega) + l'(p+omega) with l = log Gamma_inf(1/2 + .)
ell = lambda x: log(Gamma_inf(mpf(1)/2 + x))
lhs = diff(ell, p-omega) + diff(ell, p+omega)
rep("a_omega(p) = l'(p-w)+l'(p+w) closed form", abs(lhs - a_mult(omega,p)) < mpf(10)**-30,
    f"diff={abs(lhs - a_mult(omega,p))}")

# step 0b: d/dw K_w(p) = -a_w(p) K_w(p)
dK = diff(lambda w: K(w, p), omega)
rep("dK/dw = -a K", abs(dK + a_mult(omega,p)*K(omega,p)) < mpf(10)**-28,
    f"diff={abs(dK + a_mult(omega,p)*K(omega,p))}")

# step 1: digamma integral representation
c = al
rhs = -euler/2 + quad(lambda t: (exp(-2*t) - exp(-(p+c)*t))/(1-exp(-2*t)), [0, inf])
rep("1/2 psi((p+c)/2) = -gamma/2 + int (e^{-2t}-e^{-(p+c)t})/(1-e^{-2t})",
    abs(digamma((p+c)/2)/2 - rhs) < mpf(10)**-30, f"diff={abs(digamma((p+c)/2)/2 - rhs)}")

# step 2: combination formed before splitting
comb = digamma((p+al)/2)/2 + digamma((p+be)/2)/2 - digamma((p+mpf(1)/2)/2)
integ = quad(lambda t: -2*exp(-p*t)*exp(-t/2)*(cosh(omega*t)-1)/(1-exp(-2*t)), [0, inf])
rep("digamma combination = int -2 e^{-pt} e^{-t/2}(cosh wt -1)/(1-e^{-2t})",
    abs(comb - integ) < mpf(10)**-30, f"diff={abs(comb-integ)}")

# step 3: rational terms
rat = (1/(p+al) + 1/(p-al) + 1/(p+be) + 1/(p-be)) - (2/(p+mpf(1)/2) + 2/(p-mpf(1)/2))
rat_int = quad(lambda t: exp(-p*t)*4*cosh(t/2)*(cosh(omega*t)-1), [0, inf])
rep("rational difference = L[4 cosh(t/2)(cosh wt - 1)]", abs(rat - rat_int) < mpf(10)**-30,
    f"diff={abs(rat-rat_int)}")

# step 4: bridge identity and full multiplier identity
tt = mpf('0.37')
rep("2cosh(t/2) - e^{-t/2}/(1-e^{-2t}) = R(t)",
    abs(2*cosh(tt/2) - exp(-tt/2)/(1-exp(-2*tt)) - R(tt)) < mpf(10)**-35)
full = quad(lambda t: exp(-p*t)*2*(cosh(omega*t)-1)*R(t), [0, inf])
rep("a_w(p) - a_0(p) = L[2 (cosh wt - 1) R(t)]",
    abs(a_mult(omega,p) - a_mult(0,p) - full) < mpf(10)**-30,
    f"diff={abs(a_mult(omega,p) - a_mult(0,p) - full)}")
# endpoint omega = 1/2 (alpha = 0): multiplier identity still holds for Re p large
omega2 = mpf(1)/2
full2 = quad(lambda t: exp(-p*t)*2*(cosh(omega2*t)-1)*R(t), [0, inf])
rep("same identity at omega = 1/2", abs(a_mult(omega2,p) - a_mult(0,p) - full2) < mpf(10)**-30,
    f"diff={abs(a_mult(omega2,p) - a_mult(0,p) - full2)}")
# small-t behaviour of the kernel: c_w = O(t)
rep("R(t) = -1/(2t) + O(1) near 0", abs(R(mpf('1e-6')) + 1/(2*mpf('1e-6'))) < 5,
    f"R(1e-6)+1/(2e-6) = {R(mpf('1e-6')) + 1/(2*mpf('1e-6'))}")

# ================================================================ A2: endpoint lemma
print("\n=== A2: endpoint lemma ===")
L = log(2); T0 = L/2
# delta-mass check: int 1/2 Re psi((alpha+i tau)/2) - 1/2 Re psi(i tau /2) d tau -> -pi as alpha -> 0
for alv in [mpf('1e-2'), mpf('1e-3')]:
    val = quad(lambda tau: re(digamma((alv+1j*tau)/2))/2 - re(digamma(1j*tau/2))/2, [-inf, -1, -alv, 0, alv, 1, inf])
    print(f"   alpha={alv}: int(diff) = {val}  (target -pi = {-pi})")
rep("delta mass -> -pi", abs(val + pi) < mpf('2e-3'), f"at alpha=1e-3: {val}")

# quadratic-form check with f = 1 on I_L:  Q_{1/2}[f] via endpoint lemma  vs  Q_0[f] + C_{1/2}[f]
def fhat_one(tau):  # Fourier transform of indicator of (-T0,T0)
    return 2*sinh(1j*tau*T0)/(1j*tau) if tau != 0 else 2*T0
def w(omega, tau):
    al = mpf(1)/2 - omega; be = mpf(1)/2 + omega
    return re(digamma((al+1j*tau)/2))/2 + re(digamma((be+1j*tau)/2))/2 - log(pi)
def Cc(cst): return quad(lambda x: cosh(cst*x), [-T0, T0])   # C_c(1)
def Ss(cst): return quad(lambda x: sinh(cst*x), [-T0, T0])   # S_c(1) = 0 by symmetry
mp.dps = 25
def fourier_part(omega):
    # even integrand; multiplier ~ log tau, |fhat|^2 ~ 1/tau^2 : converge with tail splitting
    g = lambda tau: w(omega, tau)*abs(fhat_one(tau))**2
    return 2*quad(g, [0, 1, 10, 100, 1000, inf], maxdegree=10)/(2*pi)
Q0 = fourier_part(0) + 2*Cc(mpf(1)/2)**2 - 2*Ss(mpf(1)/2)**2
Qhalf_lemma = fourier_part(mpf(1)/2) + Cc(0)**2/2 + Cc(1)**2 - Ss(1)**2
Qhalf_naive = fourier_part(mpf(1)/2) + Cc(0)**2 + Cc(1)**2 - Ss(1)**2
Chalf = quad(lambda x, y: (cosh(abs(x-y)/2)-1)*R(abs(x-y)) if x != y else mpf(0), [-T0, T0], [-T0, T0])
print(f"   Q_0[1]              = {Q0}")
print(f"   C_1/2[1]            = {Chalf}")
print(f"   Q_0 + C_1/2         = {Q0 + Chalf}")
print(f"   endpoint lemma      = {Qhalf_lemma}")
print(f"   uncorrected formula = {Qhalf_naive}")
rep("endpoint lemma agrees with Q_0 + C_{1/2} (f=1)", abs(Q0 + Chalf - Qhalf_lemma) < mpf('1e-6'),
    f"diff={abs(Q0 + Chalf - Qhalf_lemma)}; uncorrected off by {abs(Q0 + Chalf - Qhalf_naive)}")
mp.dps = 40

# ================================================================ A3: section 6.3
print("\n=== A3: section 6.3 row-maximum analysis ===")
h = lambda t: (cosh(t/2)-1)*R(t)
hq = lambda q: (q-1)*(q**6-q**2-1)/(2*q**2*(q+1)*(q**2+1))
tt = mpf('0.5')
rep("closed form h(t) with q=e^{t/2}", abs(h(tt) - hq(exp(tt/2))) < mpf(10)**-35)
rho = polyroots([1, 0, -1, -1])[0].real  # rho^3 = rho + 1
rep("plastic number rho^3 = rho + 1", abs(rho**3 - rho - 1) < mpf(10)**-35, f"rho={rho}")
t0 = log(rho)
rep("t0 = log rho = 0.28119957432296184...", abs(t0 - mpf('0.2811995743229618465')) < mpf(10)**-18, f"t0={t0}")
rep("R changes sign at t0", abs(R(t0)) < mpf(10)**-30)
N = lambda q: q**10+q**9+q**8+q**7-q**6-q**5+q**4-2*q**3-q**2-q-1
Np_group = lambda q: (10*q**9-6*q**5)+(9*q**8-5*q**4)+(8*q**7-6*q**2)+(7*q**6-2*q)+(4*q**3-1)
rep("N'(q) grouping is the derivative of N", abs(diff(N, mpf('1.3')) - Np_group(mpf('1.3'))) < mpf(10)**-30)
rep("N'(q) > 0 for q>=1 (each group nonneg at q=1, increasing)", all(Np_group(mpf(1)+mpf(k)/10) > 0 for k in range(0, 10)))
rep("N(1) = -2 < 0", N(mpf(1)) == -2, f"N(1)={N(mpf(1))}")
rep("N(sqrt rho) = 3 rho^2 - 1 > 0", abs(N(sqrt(rho)) - (3*rho**2-1)) < mpf(10)**-30 and N(sqrt(rho)) > 0,
    f"N(sqrt rho)={N(sqrt(rho))}")
# sign(dh/dt) = sign(N(q)) at several points
ok = True
for tv in ['0.05', '0.1', '0.14', '0.2', '0.3', '0.5', '0.69']:
    tv = mpf(tv); q = exp(tv/2)
    ok &= (diff(h, tv) > 0) == (N(q) > 0)
rep("sign(dh/dt) = sign(N(q)) at 7 sample points", ok)
tm = findroot(lambda t: diff(h, t), mpf('0.14'))
rep("t_m = 0.1416454811943886...", abs(tm - mpf('0.1416454811943886')) < mpf(10)**-15, f"t_m={tm}")
rep("h(t_m) = -0.0044442714714077...", abs(h(tm) - mpf('-0.0044442714714077')) < mpf(10)**-15, f"h(t_m)={h(tm)}")
rep("h(log2 - t0) = 0.0126146638556245...", abs(h(L-t0) - mpf('0.0126146638556245')) < mpf(10)**-15, f"{h(L-t0)}")
rep("h(log2-t0) + h(t_m) > 0.00817039", h(L-t0)+h(tm) > mpf('0.00817039'), f"sum={h(L-t0)+h(tm)}")
Ih = quad(lambda t: -h(t), [0, t0]) + quad(h, [t0, L])
rep("int_0^{log2} |h| = 0.012293050401142320 < 0.012294", abs(Ih - mpf('0.012293050401142320')) < mpf(10)**-17 and Ih < mpf('0.012294'), f"{Ih}")
# item 0.6
rep("item 0.6: a >= L/2 = 0.3466 > t0 = 0.2812, so a <= t0 cannot occur", L/2 > t0, f"L/2={L/2}, t0={t0}")
# row-sum monotonicity: F(a)+F(b) decreasing in b on [0, L/2]
F = lambda r: quad(lambda t: abs(h(t)), [0, min(r, t0), r]) if r > 0 else mpf(0)
rows = [F(L-b)+F(b) for b in [mpf(k)*L/20 for k in range(0, 11)]]
rep("absolute row integral F(L-b)+F(b) is decreasing in b in [0,L/2]",
    all(rows[i] >= rows[i+1] for i in range(len(rows)-1)), f"max={rows[0]}, at L/2={rows[-1]}")
# Taylor remainder sanity: sup over omega<=1/2 of |sum_{k>=5} w^{2k} t^{2k}/(2k)! * |R|| on [0,log2], crude
rem = quad(lambda t: (cosh(t/2)-1 - sum((t/2)**(2*k)/mp.factorial(2*k) for k in range(1,5)))*abs(R(t)), [0, t0, L])
rep("degree-4 Taylor remainder row bound is tiny (< 1.54e-12)", rem < mpf('1.54e-12'), f"crude row bound={rem}")

# ================================================================ A4: Volterra identities
print("\n=== A4: Volterra identities (discretised) ===")
mp.dps = 15
n = 400; Lf = float(L); hstep = Lf/n
x = (np.arange(n)+0.5)*hstep
om = 0.3
alf = 0.5-om
def kappa(t):  # regular impulse, sec 3.2, omega = 0.3 (mpmath betainc for B_q(omega, alpha))
    if t <= 0: return 0.0
    q = 1-np.exp(-2*t)
    B = float(betainc(om, alf, 0, q))
    return float(pi**om)*(2*np.exp(-alf*t)*q**(om-1)/float(gamma(om)) - 4*alf*om*np.exp(alf*t)*B/float(gamma(om))
                          - 4*(0.5+om)*om*np.exp(-alf*t)*q**om/float(gamma(om+1)))
Kv = np.array([[kappa(xi-yj)*hstep if xi > yj else 0.0 for yj in x] for xi in x])   # V (strictly lower + diag ~0)
Rm = np.fliplr(np.eye(n))                                                            # reflection
Hm = np.array([[kappa(xi+yj-Lf)*hstep if xi+yj > Lf else 0.0 for yj in x] for xi in x])
e1 = np.abs(Hm - Kv@Rm).max(); e2 = np.abs(Hm - Rm@Kv.T).max(); e3 = np.abs(Rm@Kv@Rm - Kv.T).max()
e4 = np.abs(Hm@Hm - Kv@Kv.T).max(); e5 = np.abs(Hm - Hm.T).max()
print(f"   |H - VR|={e1:.2e}  |H - RV*|={e2:.2e}  |RVR - V*|={e3:.2e}  |H^2 - VV*|={e4:.2e}  |H-H^T|={e5:.2e}")
rep("H = VR = RV*, RVR = V*, H^2 = VV*, H symmetric (grid-exact)", max(e1,e2,e3,e4,e5) < 1e-12)
sv = np.linalg.svd(Kv, compute_uv=False); ev = np.linalg.eigvalsh(Hm)
print(f"   ||V||={sv[0]:.6f}  max|eig H|={np.abs(ev).max():.6f}  (omega=0.3, L=log2, midpoint grid n={n})")
rep("||H|| = ||V|| numerically and < 1 at omega=0.3", abs(sv[0]-np.abs(ev).max()) < 1e-9 and sv[0] < 1)
# Laplace transform of kappa vs K_omega(p) (already checked by third party; quick re-check)
mp.dps = 30
pv = mpf('1.7')
lap = quad(lambda t: kappa(float(t))*exp(-pv*t), [0, 0.01, 0.1, 1, 10, inf])
print(f"   L[kappa](1.7)={lap}   K_0.3(1.7)={K(mpf('0.3'), pv)}")
rep("Laplace of explicit impulse = K_omega(p) (float-precision impulse)", abs(lap - K(mpf('0.3'), pv)) < mpf('1e-9'))

# ================================================================ 0.3: block-Schur constant
print("\n=== Item 0.3: block-Schur coercivity constant ===")
mp.dps = 30
beta_star = log(mpf(30)/(2*pi)) - mpf(1)/30
d_even = beta_star - mpf('9.7777e-24') - mpf('0.012294')
d_odd  = beta_star - mpf('2.4269e-25') - mpf('0.012294')
print(f"   beta* = {beta_star};  d_tail(even) = {d_even};  d_tail(odd) = {d_odd}")
rep("tail lower bound 1.5176929819194764 reproduced", abs(d_even - mpf('1.5176929819194764')) < mpf('1e-15'))
kap_e = mpf('0.012294') + mpf('1.4084884e-9'); kap_o = mpf('0.012294') + mpf('2.2191643e-10')
print(f"   Schur loss even = {kap_e**2/d_even}  (reported 9.95869865858903e-5)")
print(f"   Schur loss odd  = {kap_o**2/d_odd}  (reported 9.95869673623490e-5)")
rep("Schur loss = kappa^2/d_tail reproduces both reported values",
    abs(kap_e**2/d_even - mpf('9.95869865858903e-5')) < mpf('1e-18') and abs(kap_o**2/d_odd - mpf('9.95869673623490e-5')) < mpf('1e-18'))
def coercivity(m, kap, d):
    # largest c with c + kap^2/(d-c) <= m + kap^2/d  (i.e. Q >= c I from head >= (m+kap^2/d) I, tail >= d I, |B|<=kap)
    lam = m + kap**2/d
    return findroot(lambda c: c + kap**2/(d-c) - lam, m)
for sec, m, kap, d in [("even", mpf('6.116350109501e-4'), kap_e, d_even), ("odd", mpf('5.261670009275e-2'), kap_o, d_odd),
                       ("even-audit", mpf('6.116514636999e-4'), kap_e, d_even), ("odd-audit", mpf('5.261670255041e-2'), kap_o, d_odd)]:
    cst = coercivity(m, kap, d)
    print(f"   {sec}: margin m={m}  ->  exact coercivity c={cst}   m-c={m-cst}   kap^2 m/(d(d-m))={kap**2*m/(d*(d-m))}")
c_even = coercivity(mpf('6.116350109501e-4'), kap_e, d_even)
rep("Q >= c_* I with c_* = 6.1159e-4 is safe (c_even > 6.1159e-4)", c_even > mpf('6.1159e-4'), f"c_even={c_even}")
rep("naive reading Q >= m I is NOT implied (c_even < m by ~4e-8)", c_even < mpf('6.116350109501e-4'))

# ================================================================ C1 partial: Suzuki's g_omega
print("\n=== C1 (partial): Suzuki g_omega (as extracted from arXiv:1204.1827) -> Mellin transform ===")
mp.dps = 30
def g_suz(x, om, variant):
    pref = 2*pi**om/gamma(om)
    I = quad(lambda t: t**(mpf(1)/2-om)*(1-t)**(om-1), [x**2, 1])   # = -int_1^{x^2}
    lead = x**(2-om) if variant == 'A' else x**(-om)
    return pref*(lead*(1-x**2)**(om-1) + om*x**(om-1)*I)
def mellin_g(om, s, variant):
    return quad(lambda x: g_suz(x, om, variant)*x**(s-1), [0, mpf('0.5'), 1])
for om in [mpf('0.3'), mpf('0.45')]:
    for s in [mpf('2.0'), mpf('2.7')]:
        target = Gamma_inf(s-om)/Gamma_inf(s+om)
        target_noPoly = (pi**(-(s-om)/2)*gamma((s-om)/2))/(pi**(-(s+om)/2)*gamma((s+om)/2))
        mA = mellin_g(om, s, 'A'); mB = mellin_g(om, s, 'B')
        print(f"   om={om} s={s}: variantA={mA}  variantB={mB}")
        print(f"        Gamma_inf ratio={target}   Gamma-only ratio={target_noPoly}")
# compare kappa built from Suzuki's g (variant B) with the manuscript's explicit impulse
om = mpf('0.3'); alf = mpf(1)/2-om
def kappa_ms(t):
    q = 1-exp(-2*t)
    return pi**om*(2*exp(-alf*t)*q**(om-1)/gamma(om) - 4*alf*om*exp(alf*t)*betainc(om, alf, 0, q)/gamma(om)
                   - 4*(mpf(1)/2+om)*om*exp(-alf*t)*q**om/gamma(om+1))
for tv in [mpf('0.1'), mpf('0.4'), mpf('0.69')]:
    kB = exp(-tv/2)*g_suz(exp(-tv), om, 'B'); kA = exp(-tv/2)*g_suz(exp(-tv), om, 'A')
    print(f"   t={tv}: kappa_manuscript={kappa_ms(tv)}  from Suzuki g (B)={kB}  (A)={kA}")

print("\n=== SUMMARY ===")
for lab, ok, det in out:
    print(("PASS" if ok else "FAIL"), lab)
print(f"{sum(1 for _,ok,_ in out if ok)}/{len(out)} passed")
