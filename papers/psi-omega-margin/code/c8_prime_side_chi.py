"""Prime-side (arithmetic) formula for Psi_{omega,chi}, real primitive chi mod q, parity a:

  Psi_{w,chi}(t) = (t/2)[psi(alpha) + log(q/pi)]
                 + (1/4)[psi'(alpha) - e^{-2 alpha t} Phi(e^{-2t}, 2, alpha)]
                 - sum_{n<=e^t} Lambda(n) chi(n) n^{-1/2-w} (t - log n),
  alpha = (1/2 + w + a)/2.

Laplace check (the one nontrivial block, verified numerically here; algebra done by hand):
  int_0^inf (1/4)[psi'(a) - e^{-2 a t} Phi(e^{-2t},2,a)] e^{izt} dt
      = -(1/2 z^2)[psi(a - iz/2) - psi(a)],  Im z > 0.

End-to-end test: prime side vs the margin main term slope*t + B_chi(w); the difference must
sit inside A_chi(w) e^{-wt} (GRH is verified for these q well beyond any relevant height).
Uses NO zeros.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 20

# ---------- transform identity check ----------
for alpha, z in [(mp.mpf('0.6'), mp.mpc('0.3','0.9')), (mp.mpf('0.95'), mp.mpc('-1.1','0.7'))]:
    f = lambda t: mp.mpf('0.25')*(mp.polygamma(1,alpha) - mp.e**(-2*alpha*t)*mp.lerchphi(mp.e**(-2*t),2,alpha))*mp.e**(1j*z*t)
    lhs = mp.quad(f, [0, 1, 5, 20, mp.inf])
    rhs = -(mp.digamma(alpha - 1j*z/2) - mp.digamma(alpha))/(2*z**2)
    print("alpha=%s z=%s  |LHS-RHS| = %s" % (mp.nstr(alpha,3), mp.nstr(z,3), mp.nstr(abs(lhs-rhs),3)))

# ---------- characters ----------
CHARS = {
  3: {'a':1, 'vals':[0,1,-1]},
  4: {'a':1, 'vals':[0,1,0,-1]},
  5: {'a':0, 'vals':[0,1,-1,-1,1]},
}

def L(s, q):
    ch = CHARS[q]['vals']
    return mp.mpf(q)**(-s) * mp.fsum(ch[r]*mp.zeta(s, mp.mpf(r)/q) for r in range(1, q) if ch[r] != 0)

def xilog_chi(s, q):
    a = CHARS[q]['a']
    Lp = mp.diff(lambda z_: L(z_, q), s)
    return mp.log(mp.mpf(q)/mp.pi)/2 + mp.digamma((s+a)/2)/2 + Lp/L(s, q)

def xilogp_chi(s, q):
    return mp.diff(lambda z_: xilog_chi(z_, q), s)

# ---------- sieve Lambda(n) to e^15, with chi values ----------
LIM = int(np.exp(15)) + 1
is_comp = np.zeros(LIM, dtype=bool)
primes = []
for p in range(2, LIM):
    if not is_comp[p]:
        primes.append(p)
        is_comp[p*p::p] = True
primes = np.array(primes); logp = np.log(primes.astype(np.float64))
pp_n, pp_l = [], []
for p, lp in zip(primes, logp):
    m = p
    while m < LIM:
        pp_n.append(m); pp_l.append(lp)
        m *= p
pp_n = np.array(pp_n, dtype=np.int64); pp_l = np.array(pp_l)
order = np.argsort(pp_n); pp_n, pp_l = pp_n[order], pp_l[order]
logn = np.log(pp_n.astype(np.float64))
print("prime powers:", len(pp_n))

def psi_omega_chi(q, w, t):
    a = CHARS[q]['a']; ch = np.array(CHARS[q]['vals'])
    w_ = mp.mpf(str(w)); t_ = mp.mpf(str(t))
    alpha = (mp.mpf('0.5') + w_ + a)/2
    term_t   = t_/2*( mp.digamma(alpha) + mp.log(mp.mpf(q)/mp.pi) )
    term_gam = mp.mpf('0.25')*( mp.polygamma(1, alpha)
               - mp.e**(-2*alpha*t_)*mp.lerchphi(mp.e**(-2*t_), 2, alpha) )
    mask = logn <= float(t)
    n = pp_n[mask]; l = pp_l[mask]; ln = logn[mask]
    chi_n = ch[n % q]
    s = np.sum(chi_n * l * n.astype(np.float64)**(-(0.5+float(w))) * (float(t)-ln))
    return term_t + term_gam - mp.mpf(float(s))

print("\nq | w | t | Psi_{w,chi} (primes) | main term | diff | A_chi(w) e^{-wt}")
for q in (3,4,5):
    for (w,t) in [(0.2,6),(0.2,15),(0.3,15),(0.4,15)]:
        w_ = mp.mpf(str(w))
        val  = psi_omega_chi(q, w, t)
        sl   = xilog_chi(mp.mpf('0.5')+w_, q)
        B    = xilogp_chi(mp.mpf('0.5')+w_, q)
        main = sl*t + B
        env  = (sl/w_)*mp.e**(-w_*t)
        print(q, w, t, mp.nstr(val,9), mp.nstr(main,9), mp.nstr(val-main,3), mp.nstr(env,3))
    # value at t=0 must be 0
    print("  q=%d: Psi_{0.3,chi}(1e-12) =" % q, mp.nstr(psi_omega_chi(q, 0.3, 1e-12),3))
