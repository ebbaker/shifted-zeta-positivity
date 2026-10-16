import mpmath as mp, weil_sine_basis as wf2, sys
N = 80
print("arch+pole with the prime comb DELETED  (continuum control C1)")
print("   L    lam_min(true)      lam_min(no comb)    lam_min(no comb, even/odd)")
for Lf in [0.6,0.8,0.9,1.0,1.2,1.6,2.0]:
    L = mp.mpf(Lf); mp.mp.dps = max(40, int(abs(17.68-5.731*2*mp.e**L)/mp.log(10))+40)
    comb = wf2.prime_comb(L); W = wf2.WeilForm(L, N)
    tv, av = [], []
    for par in (0,1):
        M,_ = W.matrix(comb, par);  tv.append(wf2.lam_min(M))
        M0,_ = W.matrix(comb, par, arch_only=True)
        av.append(min(mp.eigsy(M0, eigvals_only=True)))
    print("%5.2f   %s   %s   (%s / %s)" % (Lf, mp.nstr(min(tv),7), mp.nstr(min(av),7),
                                            mp.nstr(av[0],5), mp.nstr(av[1],5)))
    sys.stdout.flush()

print()
print("comb strength homotopy  Q_s = arch + pole - s*primes,  L = 1.6")
L = mp.mpf('1.6'); mp.mp.dps = 60; comb = wf2.prime_comb(L); W = wf2.WeilForm(L, 120)
for s in ['0','0.25','0.5','0.75','0.9','1','1.1','1.25','1.5']:
    vals = []
    for par in (0,1):
        M,_ = W.matrix(comb, par, scale=mp.mpf(s))
        vals.append(min(mp.eigsy(M, eigvals_only=True)))
    print("   s=%5s   lam_min = %s" % (s, mp.nstr(min(vals), 8)))
