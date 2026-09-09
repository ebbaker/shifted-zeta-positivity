"""Step 2: the margin for real primitive Dirichlet characters (q = 3, 4, 5).

xi(s,chi) = (q/pi)^{(s+a)/2} Gamma((s+a)/2) L(s,chi),  a = (1-chi(-1))/2, eps = +1 for real chi.
Margin slope = (xi'/xi)(1/2+w, chi); intercept = (xi'/xi)'(1/2+w, chi);
A_chi(w) = (1/w)(xi'/xi)(1/2+w,chi) checked against direct sums over computed zeros + RvM tail.
Also: numerical check that a REAL zero pair (Siegel-type) contributes POSITIVELY to Psi_w.
"""
import mpmath as mp
mp.mp.dps = 20

CHARS = {
  3: {'a':1, 'vals':{0:0, 1:1, 2:-1}},                      # Legendre mod 3 (odd)
  4: {'a':1, 'vals':{0:0, 1:1, 2:0, 3:-1}},                 # chi_4 (odd)
  5: {'a':0, 'vals':{0:0, 1:1, 2:-1, 3:-1, 4:1}},           # Legendre mod 5 (even)
}

def L(s, q):
    ch = CHARS[q]['vals']
    return mp.mpf(q)**(-s) * mp.fsum(ch[r]*mp.zeta(s, mp.mpf(r)/q) for r in range(1, q) if ch[r] != 0)

def xichi(s, q):
    a = CHARS[q]['a']
    return (mp.mpf(q)/mp.pi)**((s+a)/2) * mp.gamma((s+a)/2) * L(s, q)

def xilog_chi(s, q):
    a = CHARS[q]['a']
    Lp = mp.diff(lambda z: L(z, q), s)
    return mp.log(mp.mpf(q)/mp.pi)/2 + mp.digamma((s+a)/2)/2 + Lp/L(s, q)

def xilogp_chi(s, q):
    return mp.diff(lambda z: xilog_chi(z, q), s)

# --- sanity: functional equation xi(s)=xi(1-s), and xi(1/2+it) real ---
for q in (3,4,5):
    d1 = xichi(mp.mpf('0.3'), q) - xichi(mp.mpf('0.7'), q)
    z = xichi(mp.mpf('0.5')+1j*mp.mpf('7.7'), q)
    print("q=%d  FE residual %s   Im xi(1/2+7.7i) %s" % (q, mp.nstr(abs(d1),3), mp.nstr(abs(mp.im(z)),3)))

# --- find zeros on the critical line up to T by sign changes of real xi(1/2+it) ---
def zeros_upto(q, T, step=0.05):
    Z = lambda t: mp.re(xichi(mp.mpf('0.5')+1j*t, q))
    zs, t, prev = [], mp.mpf('0.05'), None
    prev = Z(mp.mpf('0.05'))
    while t < T:
        t2 = t + step
        cur = Z(t2)
        if prev*cur < 0:
            zs.append(mp.findroot(Z, (t, t2), solver='bisect'))
        prev, t = cur, t2
    return zs

import time
results = {}
for q in (3,4,5):
    t0 = time.time()
    zs = zeros_upto(q, 60)
    results[q] = zs
    # RvM check: N(T) ~ (T/pi) log(qT/(2 pi e))  for zeros with |Im|<=T (both signs)
    T = 60
    Npred = (T/mp.pi)*mp.log(q*T/(2*mp.pi*mp.e))
    print("q=%d: %d zeros to T=60 (predicted both-signs %s), first: %s   [%.0fs]" %
          (q, 2*len(zs), mp.nstr(Npred,4), ", ".join(mp.nstr(z,6) for z in zs[:4]), time.time()-t0))

# --- closed forms vs zero sums ---
print("\nq | w | A_chi closed | A_chi sum+tail | B_chi closed | B_chi sum+tail")
for q in (3,4,5):
    zs = results[q]
    T = mp.mpf(60)
    dens = lambda u: mp.log(q*u/(2*mp.pi))/(2*mp.pi)
    for w in ['0.10','0.25','0.40']:
        w_ = mp.mpf(w)
        Ac = xilog_chi(mp.mpf('0.5')+w_, q)/w_
        Bc = xilogp_chi(mp.mpf('0.5')+w_, q)
        Ah = 2*mp.fsum(1/(g**2+w_**2) for g in zs) + 2*mp.quad(lambda u: dens(u)/(u**2+w_**2), [T, mp.inf])
        Bh = 2*mp.fsum((g**2-w_**2)/(g**2+w_**2)**2 for g in zs) + 2*mp.quad(lambda u: dens(u)*(u**2-w_**2)/(u**2+w_**2)**2, [T, mp.inf])
        print(q, w, mp.nstr(Ac,7), mp.nstr(Ah,7), mp.nstr(Bc,7), mp.nstr(Bh,7),
              " rel:", mp.nstr((Ah-Ac)/Ac,2))

# --- the margin across conductors ---
print("\nconductor | B_chi(0)=(xi'/xi)'(1/2,chi) | slope at w=0.25 | slope/w at w->0")
print("zeta:", 0.04620999)
for q in (3,4,5):
    B0 = xilogp_chi(mp.mpf('0.5'), q)
    sl = xilog_chi(mp.mpf('0.75'), q)
    s0 = xilog_chi(mp.mpf('0.5'), q)
    print("q=%d:" % q, mp.nstr(B0,7), mp.nstr(sl,7), " (xi'/xi)(1/2,chi) =", mp.nstr(s0,3))

# --- Siegel blindness: a real zero pair contributes POSITIVELY ---
print("\nreal-zero pair (gamma = +-i*delta) contribution to Psi_w series, delta=0.4, w=0.1:")
def term(g, w, t):
    return ( w*t*(g**2+w**2) + (g**2-w**2)
             - mp.e**(-w*t)*(g**2-w**2)*mp.cos(g*t)
             - mp.e**(-w*t)*2*g*w*mp.sin(g*t) ) / (g**2+w**2)**2
for t in [1, 5, 10, 20, 40]:
    val = term(mp.mpc(0,'0.4'), mp.mpf('0.1'), t) + term(mp.mpc(0,'-0.4'), mp.mpf('0.1'), t)
    pred = ((mp.mpf('0.4')+mp.mpf('0.1'))**2)*mp.e**(mp.mpf('0.3')*t)/(mp.mpf('0.4')**2-mp.mpf('0.1')**2)**2
    print("t=%2d: pair term = %s  (asymptotic prediction %s)" % (t, mp.nstr(val,6), mp.nstr(pred,4)))
