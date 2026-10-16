"""Check 3: prime-side formula eq:Psiomegaprimes vs paper Table tab:asym and Check 0.
Lambda(n) sieved to e^15 ~ 3.27e6."""
import numpy as np, mpmath as mp
mp.mp.dps = 25

LIM = int(np.exp(15)) + 1
print("sieving to", LIM)
lam = np.zeros(LIM, dtype=np.float64)   # log p at prime powers
is_comp = np.zeros(LIM, dtype=bool)
primes = []
for p in range(2, LIM):
    if not is_comp[p]:
        primes.append(p)
        is_comp[p*p::p] = True
primes = np.array(primes)
logp = np.log(primes.astype(np.float64))
# mark prime powers
pp_n, pp_l = [], []
for p, lp in zip(primes, logp):
    q = p
    while q < LIM:
        pp_n.append(q); pp_l.append(lp)
        q *= p
pp_n = np.array(pp_n, dtype=np.int64); pp_l = np.array(pp_l)
order = np.argsort(pp_n); pp_n = pp_n[order]; pp_l = pp_l[order]
logn = np.log(pp_n.astype(np.float64))
print("prime powers:", len(pp_n))

def psi_omega_primes(w, t):
    w_ = mp.mpf(w); t_ = mp.mpf(t)
    term1 = 4*( mp.e**((mp.mpf('0.5')-w_)*t_)/(1-2*w_)**2 + mp.e**(-(mp.mpf('0.5')+w_)*t_)/(1+2*w_)**2
                - (4 - 2*(1-w_*t_)*(1-4*w_**2))/(1-4*w_**2)**2 )
    term2 = t_/2*( mp.digamma(mp.mpf('0.25')+w_/2) - mp.log(mp.pi) )
    term3 = mp.mpf('0.25')*( mp.polygamma(1, mp.mpf('0.25')+w_/2)
                - mp.e**(-(mp.mpf('0.5')+w_)*t_)*mp.lerchphi(mp.e**(-2*t_), 2, mp.mpf('0.25')+w_/2) )
    # prime sum with numpy (double precision is plenty: differences ~1e-5 scale)
    mask = logn <= float(t)
    n = pp_n[mask].astype(np.float64); l = pp_l[mask]; ln = logn[mask]
    s = np.sum(l * n**(-(0.5+float(w))) * (float(t)-ln))
    return term1 + term2 + term3 - mp.mpf(s)

def xilog(s):
    return 1/s + 1/(s-1) - mp.log(mp.pi)/2 + mp.digamma(s/2)/2 + mp.zeta(s, derivative=1)/mp.zeta(s)
def xilogp(s):
    return mp.diff(xilog, s)

print("\nCheck 0: Psi(0.464002) =", mp.nstr(psi_omega_primes(0, 0.464002), 10), " (paper: 0.03966175656)")
print("Psi(0) =", mp.nstr(psi_omega_primes(0, 1e-30), 6))

print("\nw | t | Psi_w primes | main term | diff | A(w)e^{-wt}")
rows = [(0.20,6),(0.20,15),(0.30,6),(0.30,15),(0.40,6),(0.40,15)]
for w,t in rows:
    w_ = mp.mpf(str(w))
    val = psi_omega_primes(w, t)
    main = xilog(mp.mpf('0.5')+w_)*t + xilogp(mp.mpf('0.5')+w_)
    env = (xilog(mp.mpf('0.5')+w_)/w_)*mp.e**(-w_*t)
    print(w, t, mp.nstr(val,9), mp.nstr(main,9), mp.nstr(val-main,3), mp.nstr(env,3))
