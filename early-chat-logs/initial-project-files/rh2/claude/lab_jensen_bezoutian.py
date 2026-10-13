import mpmath as mp
mp.mp.dps = 140
_cache = {}
def Phi(u):
    key = mp.nstr(u, 45)
    if key in _cache: return _cache[key]
    tot = mp.mpf(0)
    for n in range(1, 200):
        t = (2*mp.pi**2*n**4*mp.e**(mp.mpf(9)*u/2) - 3*mp.pi*n**2*mp.e**(mp.mpf(5)*u/2)) \
            * mp.e**(-mp.pi*n**2*mp.e**(2*u))
        tot += t
        if n > 4 and abs(t) < mp.mpf('1e-160')*max(abs(tot), mp.mpf(1)): break
    _cache[key] = tot
    return tot

NM = 24
seg = [0, mp.mpf('0.5'), 2, 6, 12, 20]
M = [mp.quad(lambda u, k=k: Phi(u)*u**k, seg) for k in range(2*NM+2)]
print(f"  4*M_0 = {mp.nstr(4*M[0],16)}   vs  xi(1/2) = 0.49712071737")
b = [4*M[2*m]/mp.factorial(2*m) for m in range(NM+1)]
print(f"  all b_m > 0 : {all(x>0 for x in b)}   (m <= {NM});  Phi evals cached: {len(_cache)}")
gam = [mp.factorial(m)*b[m] for m in range(NM+1)]

def bez(rts):
    d = len(rts); s = [sum((mp.mpmathify(r)**k for r in rts), mp.mpf(0)) for k in range(2*d-1)]
    H = mp.matrix(d, d)
    for i in range(d):
        for j in range(d): H[i,j] = mp.re(s[i+j])
    return H

print(f"\n{'d':>3s} {'sig':>4s} {'rank':>5s} {'hyperbolic?':>12s} {'|lam_min|/||H||':>18s} {'log10':>9s} {'digits needed':>14s}")
for d in [2,4,6,8,10,12,14,16,18,20,22,24]:
    co = [mp.binomial(d,j)*gam[j] for j in range(d+1)]
    co = [x/co[-1] for x in co]
    rts = mp.polyroots(list(reversed(co)), maxsteps=3000, extraprec=3000)
    mx = max(abs(r) for r in rts); rts = [r/mx for r in rts]
    ev = [mp.re(x) for x in mp.eigsy(bez(rts), eigvals_only=True)]
    nrm = max(abs(x) for x in ev); tol = nrm*mp.mpf('1e-115')
    pos = sum(1 for x in ev if x > tol); neg = sum(1 for x in ev if x < -tol)
    lmin = min(abs(x) for x in ev)/nrm
    print(f"{d:3d} {pos-neg:4d} {pos+neg:5d} {str(pos-neg==d):>12s} {mp.nstr(lmin,6):>18s}"
          f" {mp.nstr(mp.log10(lmin),6):>9s} {int(-mp.log10(lmin))+1:>14d}")
