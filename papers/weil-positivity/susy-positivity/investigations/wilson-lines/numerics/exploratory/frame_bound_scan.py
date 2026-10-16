"""
Converged lambda_min(Q_{0,L}) over a range of L.  Requires mpmath (unregistered).

Basis size: the minimiser is not resolved until the trial space reaches about
2.5 times the Nyquist count 2 L e^L of the deficit band |tau| < tau_c = 2 pi e^L,
so N is set to 2.8 times that.  Precision is set from the value itself.
The minimum always sits in the even block.

Usage:  python3 frame_bound_scan.py 0.6,0.8,...,3.0
"""
import mpmath as mp, weil_sine_basis as wf2, sys, time, json

res = {}
for Lf in [float(x) for x in sys.argv[1].split(',')]:
    L = mp.mpf(Lf)
    mp.mp.dps = max(40, int(abs(17.68 - 5.731*2*mp.e**L)/mp.log(10)) + 60)
    N = max(160, int(2.8*2*L*mp.e**L)); N += N % 2
    comb = wf2.prime_comb(L); t0 = time.time()
    W = wf2.WeilForm(L, N)
    M, _ = W.matrix(comb, 0)
    lam = wf2.lam_min(M)
    print("%5.2f  N=%5d dps=%4d nprimes=%2d  log10 lam_min = %s  [%.0fs]"
          % (Lf, N, mp.mp.dps, len(comb), mp.nstr(mp.log10(lam), 12), time.time()-t0))
    sys.stdout.flush()
    res[Lf] = [float(mp.log10(lam)), N, int(mp.mp.dps)]
    json.dump(res, open('frame_bound_scan.json', 'w'))
