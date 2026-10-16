import mpmath as mp, weil_sine_basis as wf2, sys
"""Rayleigh minimum restricted to bandwidth W = N pi / L, i.e. W/tau_c = N/(2 L e^L)."""
for Lf in [float(x) for x in sys.argv[1].split(',')]:
    L = mp.mpf(Lf)
    mp.mp.dps = max(40, int(abs(17.68-5.731*2*mp.e**L)/mp.log(10))+60)
    nyq = 2*L*mp.e**L
    comb = wf2.prime_comb(L)
    print("\nL=%.2f  tau_c=2 pi e^L=%s  Nyquist count 2Le^L=%s  deficit 2e^L-7/4=%s"
          % (Lf, mp.nstr(2*mp.pi*mp.e**L,7), mp.nstr(nyq,7), mp.nstr(2*mp.e**L-mp.mpf(7)/4,7)))
    print("    N     W/tau_c    log10 lam_min(band)")
    prev=None
    for frac in [0.5,0.75,1.0,1.25,1.5,2.0,2.5,3.0,3.5]:
        N = max(4, int(frac*nyq)); N += N % 2
        W = wf2.WeilForm(L, N)
        M,_ = W.matrix(comb, 0)
        try: lam = wf2.lam_min(M)
        except Exception: lam = min(mp.eigsy(M, eigvals_only=True))
        print("  %5d    %5.2f      %s" % (N, float(N/nyq), mp.nstr(mp.log10(lam),10)))
        sys.stdout.flush()
