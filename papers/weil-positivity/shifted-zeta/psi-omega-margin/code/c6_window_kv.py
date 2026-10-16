"""Step 1: push the unconditional window using explicit zero-free regions (MTY 2024).

Beyond Tv = 3e12 (Platt-Trudgian), every zero has beta <= 1 - nu(tau) with
  nu_cl(tau) = 1/(5.558691 log tau)                       [MTY classical shape, |t|>=2]
  nu_kv(tau) = 1/(55.241 (log tau)^{2/3} (loglog tau)^{1/3})  [MTY Korobov-Vinogradov, |t|>=3]
and nu = max of the two is admissible. Hence b = beta - 1/2 <= 1/2 - nu(tau), and the
high-zero part of the remainder satisfies

  |R_high(t)| <= e^{(1/2-w)t} E(t),
  E(t) = (1/pi) \int_{Lv}^\infty (L - log 2pi) exp(-L - nu~(L) t) dL,   L = log u.

E(0) = S = 2.96e-12 recovers the old bound. New window: root of
  wA t + B - A e^{-wt} - e^{(1/2-w)t} E(t) = 0.
"""
import mpmath as mp
mp.mp.dps = 25

def xilog(s):
    return 1/s + 1/(s-1) - mp.log(mp.pi)/2 + mp.digamma(s/2)/2 + mp.zeta(s, derivative=1)/mp.zeta(s)
def xilogp(s):
    return mp.diff(xilog, s)

Lv = mp.log(mp.mpf('3e12'))
log2pi = mp.log(2*mp.pi)
c_cl = mp.mpf('5.558691')
a_kv = mp.mpf('55.241')

def nu(L):
    return max(1/(c_cl*L), 1/(a_kv * L**mp.mpf('2')/L**mp.mpf('4/3') * mp.log(L)**mp.mpf('1/3')))  # placeholder

# careful: nu_kv = 1/(a_kv * L^{2/3} * (log L)^{1/3})
def nu_cl(L):  return 1/(c_cl*L)
def nu_kv(L):  return 1/(a_kv * L**(mp.mpf(2)/3) * mp.log(L)**(mp.mpf(1)/3))
def nu_max(L): return max(nu_cl(L), nu_kv(L))

# crossover
Lx = mp.findroot(lambda L: nu_cl(L)-nu_kv(L), 9000)
print("crossover L_x =", mp.nstr(Lx,6), " (u = e^L_x = 10^%s)" % mp.nstr(Lx/mp.log(10),4))

def E(t):
    t = mp.mpf(t)
    f = lambda L: (L - log2pi)*mp.e**(-L - nu_max(L)*t)
    return mp.quad(f, [Lv, 60, 200, 1000, Lx, 5*Lx, mp.inf])/mp.pi

print("E(0) =", mp.nstr(E(0),6), " (old S = 2.9594e-12)")
for t in [50, 100, 300, 1000, 3000, 10000]:
    print("E(%d) = %s   damping vs S: %s" % (t, mp.nstr(E(t),4), mp.nstr(E(t)/E(0),4)))

def window_top(w):
    w = mp.mpf(w)
    A = xilog(mp.mpf('0.5')+w)/w; B = xilogp(mp.mpf('0.5')+w)
    F = lambda t: w*A*t + B - A*mp.e**(-w*t) - mp.e**((mp.mpf('0.5')-w)*t)*E(t)
    lo, hi = mp.mpf(30), mp.mpf(30)
    while F(hi) > 0: hi *= 2
    for _ in range(60):
        mid = (lo+hi)/2
        if F(mid) > 0: lo = mid
        else: hi = mid
    return lo

print("\nw | t_plus (old, S only) | t_plus (new, zero-free damped)")
old = {'0.05':55.06,'0.1':63.67,'0.2':87.98,'0.25':107.19,'0.3':136.02,'0.4':282.06,
       '0.45':580.82,'0.49':3079.08,'0.494':None,'0.497':None,'0.499':None}
for w in ['0.05','0.1','0.2','0.25','0.3','0.4','0.45','0.49','0.494','0.497','0.499']:
    tp = window_top(w)
    print(w, old[w], mp.nstr(tp,6), " x=10^%s" % mp.nstr(tp/mp.log(10),4))
