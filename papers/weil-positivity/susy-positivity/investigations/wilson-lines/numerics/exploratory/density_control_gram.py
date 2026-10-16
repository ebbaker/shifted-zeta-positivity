import mpmath as mp, sys, time, json
PTS_RAW = json.load(open('gramT3000_d220.json'))
def lam_gram(Lf, N, pts):
    L = mp.mpf(Lf); al = mp.pi/L
    idx = [j for j in range(1, N+1) if (j-1) % 2 == 0]
    n = len(idx); s2L = mp.sqrt(2/L); ja = [j*al for j in idx]; sg = [(-1)**j for j in idx]
    M = [[mp.mpf(0)]*n for _ in range(n)]
    for t in pts:
        cs, sn = mp.cos(t*L), mp.sin(t*L); tt = t*t
        re = [s2L*a*(1-s*cs)/(a*a-tt) for a, s in zip(ja, sg)]
        im = [s2L*a*(s*sn)/(a*a-tt) for a, s in zip(ja, sg)]
        for p in range(n):
            rp, ip, Mp = re[p], im[p], M[p]
            for q in range(p, n): Mp[q] += 2*(rp*re[q]+ip*im[q])
    for p in range(n):
        for q in range(p, n): M[q][p] = M[p][q]
    return min(mp.eigsy(mp.matrix(M), eigvals_only=True))
res = {}
for Lf in [float(x) for x in sys.argv[1].split(',')]:
    L = mp.mpf(Lf)
    mp.mp.dps = min(210, max(50, int(abs(17.68-5.731*2*mp.e**L)/mp.log(10))+50))
    pts = [mp.mpf(s) for s in PTS_RAW]
    N = max(60, int(2.8*2*L*mp.e**L)); N += N % 2
    t0 = time.time(); lam = lam_gram(Lf, N, pts)
    print("L=%4.2f N=%4d dps=%4d  lam_Gram=%s  log10=%s  [%.0fs]" %
          (Lf, N, mp.mp.dps, mp.nstr(lam,8), mp.nstr(mp.log10(lam),10), time.time()-t0))
    sys.stdout.flush(); res[Lf] = float(mp.log10(lam)); json.dump(res, open('gram_conv.json','w'))
print("DONE")
