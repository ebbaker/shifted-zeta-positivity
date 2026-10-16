"""
Lattice-phase robustness test for the density control of manuscript 8.6 /
frame-bound note 5.  Unregistered (mpmath).  Written by Claude Fable 5.1 for
reviews/review_claude-fable-5-1_2026-09-17.md.

The Gram points theta(g_n) = n pi, n >= -1, used in density_control_gram.py are
one phase of the unfolded lattice {theta(t)/pi + 1 in Z + c}; they have c = 0,
lowest point 9.67 (below gamma_1 = 14.13) and a counting function that exceeds
the smooth N_sm(T) = theta(T)/pi + 1 by 1/2 on average.  This programme computes
the even-block lambda_min, in the same sine basis and truncation, for

  zeros       exact Weil form, closed-form assembler (weil_sine_basis.py);
  gram_nm1    Gram points n >= -1            (phase c = 0,   as in the note);
  gram_n0     Gram points n >= 0             (lowest 17.85; count low by 1/2);
  half        half-shifted lattice theta(t) = (k - 1/2) pi, k >= 0
              (phase c = 1/2; lowest 14.52; counting function averages to
              N_sm exactly -- the Gram's-law idealisation of the zeros).

Usage:  python3 gram_phase_control.py 0.6,0.8,1.0 [T_cutoff]
Needs gram_T3000.json in the working directory (make it with:
  python3 -c "import mpmath as mp,json; mp.mp.dps=40; out=[]; n=-1
  while True:
      g=mp.grampoint(n)
      if g>3000: break
      out.append(mp.nstr(g,35)); n+=1
  json.dump(out,open('gram_T3000.json','w'))").
Every value is a trial-space Rayleigh quotient, an upper bound on its infimum;
truncating the point set at T_cutoff lowers the three control values slightly.
Results recorded in the review: |half - zeros| <= 0.12 in log10 for
L in {0.6,...,2.8}, against gaps of +1.1 to +3.6 for gram_nm1 and -0.9 to -2.7
for gram_n0.
"""
import sys, json, time
import mpmath as mp, weil_sine_basis as wf2

TCUT = float(sys.argv[2]) if len(sys.argv) > 2 else 3000.0
GR = [mp.mpf(s) for s in json.load(open("gram_T3000.json"))]

def half_shift_points(T):
    dth = lambda t: mp.re(mp.digamma(mp.mpf(1)/4 + 1j*t/2))/2 - mp.log(mp.pi)/2
    out = []
    for i in range(len(GR) - 1):
        g = (GR[i] + GR[i+1])/2; tgt = (i-1)*mp.pi + mp.pi/2   # theta(GR[i]) = (i-1) pi
        for _ in range(6):
            g = g - (mp.siegeltheta(g) - tgt)/dth(g)
        if g > T: break
        out.append(g)
    return out

def lam_pts(Lf, N, pts):
    """even-block lambda_min of sum_t |F^(t)|^2 over the point set, sine basis"""
    L = mp.mpf(Lf); al = mp.pi/L
    idx = [j for j in range(1, N+1) if (j-1) % 2 == 0]
    n = len(idx); s2L = mp.sqrt(2/L); ja = [j*al for j in idx]; sg = [(-1)**j for j in idx]
    M = [[mp.mpf(0)]*n for _ in range(n)]
    for t in pts:
        cs, sn = mp.cos(t*L), mp.sin(t*L); tt = t*t
        re = [s2L*a*(1 - s*cs)/(a*a - tt) for a, s in zip(ja, sg)]
        im = [s2L*a*(s*sn)/(a*a - tt) for a, s in zip(ja, sg)]
        for p in range(n):
            rp, ip, Mp = re[p], im[p], M[p]
            for q in range(p, n):
                Mp[q] += 2*(rp*re[q] + ip*im[q])
    for p in range(n):
        for q in range(p, n):
            M[q][p] = M[p][q]
    return min(mp.eigsy(mp.matrix(M), eigvals_only=True))

mp.mp.dps = 50
HS = half_shift_points(TCUT)
G1 = [g for g in GR if g < TCUT]
print("lowest points: gram_nm1 %s  gram_n0 %s  half %s   (gamma_1 = 14.1347)"
      % (mp.nstr(G1[0], 6), mp.nstr(G1[1], 6), mp.nstr(HS[0], 6)))
res = {}
for Lf in [float(x) for x in sys.argv[1].split(',')]:
    L = mp.mpf(Lf)
    mp.mp.dps = max(50, int(abs(17.68 - 5.731*2*mp.e**L)/mp.log(10)) + 50)
    N = max(60, int(2.8*2*L*mp.e**L)); N += N % 2
    t0 = time.time()
    W = wf2.WeilForm(L, N); M, _ = W.matrix(wf2.prime_comb(L), 0); lz = wf2.lam_min(M)
    row = dict(zeros=float(mp.log10(lz)),
               gram_nm1=float(mp.log10(lam_pts(Lf, N, G1))),
               gram_n0=float(mp.log10(lam_pts(Lf, N, G1[1:]))),
               half=float(mp.log10(lam_pts(Lf, N, HS))), N=N, dps=mp.mp.dps, T_cutoff=TCUT)
    res[Lf] = row
    print("L=%.2f N=%d dps=%d  zeros %.3f | gram(n>=-1) %.3f | gram(n>=0) %.3f | half-shift %.3f"
          "   gaps %.2f %.2f %.2f  [%.0fs]" % (Lf, N, mp.mp.dps, row['zeros'], row['gram_nm1'],
          row['gram_n0'], row['half'], row['gram_nm1']-row['zeros'], row['gram_n0']-row['zeros'],
          row['half']-row['zeros'], time.time()-t0))
    sys.stdout.flush()
    json.dump(res, open('gram_phase_control.json', 'w'), indent=1)
