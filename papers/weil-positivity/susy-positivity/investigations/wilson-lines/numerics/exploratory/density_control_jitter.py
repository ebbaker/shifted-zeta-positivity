"""Controls at matched density: Gram points, jittered Gram (jitter applied in the
unfolded variable theta/pi, so the counting function is preserved), and the true
zeros.  Same sine basis, same truncation T, same precision."""
import mpmath as mp, json, sys, random, time
PTS = json.load(open('gramT3000_d220.json'))
ZR  = json.load(open('zeros1001.json'))

def unfold_jitter(sigma, seed):
    """g_n -> theta^{-1}(pi (n + sigma*(U-1/2))) computed by one Newton step."""
    random.seed(seed)
    dth = lambda t: mp.re(mp.digamma(mp.mpf(1)/4+1j*t/2))/2 - mp.log(mp.pi)/2
    out = []
    for i, s in enumerate(PTS):
        g = mp.mpf(s)
        d = mp.pi*sigma*(mp.mpf(random.random())-mp.mpf(1)/2)
        for _ in range(4):
            g = g + (((i-1)*mp.pi + d) - mp.siegeltheta(g))/dth(g)
        out.append(g)
    return out

def lam(Lf, N, pts):
    L = mp.mpf(Lf); al = mp.pi/L
    idx = [j for j in range(1, N+1) if (j-1) % 2 == 0]
    n = len(idx); s2L = mp.sqrt(2/L); ja=[j*al for j in idx]; sg=[(-1)**j for j in idx]
    M = [[mp.mpf(0)]*n for _ in range(n)]
    for t in pts:
        cs, sn = mp.cos(t*L), mp.sin(t*L); tt=t*t
        re=[s2L*a*(1-s*cs)/(a*a-tt) for a,s in zip(ja,sg)]
        im=[s2L*a*(s*sn)/(a*a-tt) for a,s in zip(ja,sg)]
        for p in range(n):
            rp,ip,Mp=re[p],im[p],M[p]
            for q in range(p,n): Mp[q]+=2*(rp*re[q]+ip*im[q])
    for p in range(n):
        for q in range(p,n): M[q][p]=M[p][q]
    return min(mp.eigsy(mp.matrix(M), eigvals_only=True))

for Lf in [float(x) for x in sys.argv[1].split(',')]:
    L = mp.mpf(Lf)
    mp.mp.dps = max(50, int(abs(17.68-5.731*2*mp.e**L)/mp.log(10))+50)
    N = max(60, int(2.8*2*L*mp.e**L)); N += N % 2
    gram = [mp.mpf(s) for s in PTS]
    zeros = [mp.mpf(s) for s in ZR if mp.mpf(s) < 3000]
    rows = [("Gram (S=0)      ", gram),
            ("Gram jitter 0.15", unfold_jitter(0.15, 1)),
            ("Gram jitter 0.40", unfold_jitter(0.40, 2)),
            ("Gram jitter 1.00", unfold_jitter(1.00, 3))]
    print("L=%4.2f  N=%d  dps=%d" % (Lf, N, mp.mp.dps))
    for name, pts in rows:
        t0=time.time(); v = lam(Lf, N, pts)
        print("   %s  log10 lam = %s   [%.0fs]" % (name, mp.nstr(mp.log10(v), 9), time.time()-t0))
        sys.stdout.flush()
