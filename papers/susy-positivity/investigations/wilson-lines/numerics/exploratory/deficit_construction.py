"""(b) The literal deficit construction, even block.
Even real f  =>  Fhat real; one real constraint per zero below tau_c.
Trial space: sine modes with j*pi/L <= tau_c  (dimension = Nyquist count),
intersected with {Fhat(gamma)=0 : 0<gamma<tau_c}.  Any such f gives an upper
bound on lambda_min.  Null-space dimension = the sample deficit D(L)/2."""
import mpmath as mp, weil_sine_basis as wf2, json, sys

zeros = [mp.mpf(z) for z in json.load(open('zeros1001.json'))]

def nullspace(rows, n):
    """orthonormal basis (list of mp vectors, length n) of the null space of `rows`."""
    basis = []
    # Gram-Schmidt the constraint rows, then complete
    orth = []
    for r in rows:
        v = mp.matrix(r)
        for u in orth: v -= (u.T*v)[0]*u
        nv = mp.norm(v)
        if nv > mp.mpf(10)**(-mp.mp.dps//2): orth.append(v/nv)
    for i in range(n):
        e = mp.zeros(n, 1); e[i] = 1
        for u in orth + basis: e -= (u.T*e)[0]*u
        ne = mp.norm(e)
        if ne > mp.mpf(10)**(-mp.mp.dps//3): basis.append(e/ne)
    return basis

print(" L     tau_c   m=#g<tau_c  Nyq   D(L)  dim(null) | log10:  true      band     band+vanish")
for Lf in [float(x) for x in sys.argv[1].split(',')]:
    L = mp.mpf(Lf)
    mp.mp.dps = max(60, int(abs(17.68-5.731*2*mp.e**L)/mp.log(10))+60)
    tc = 2*mp.pi*mp.e**L; nyq = 2*L*mp.e**L; D = 2*mp.e**L-mp.mpf(7)/4
    al = mp.pi/L; comb = wf2.prime_comb(L)
    zl = [g for g in zeros if g < tc]
    Nb = max(4, int(nyq)); Nb += Nb % 2
    Nf = max(80, int(2.8*nyq)); Nf += Nf % 2

    Wf = wf2.WeilForm(L, Nf); Mf, _ = Wf.matrix(comb, 0); true = wf2.lam_min(Mf)
    Wb = wf2.WeilForm(L, Nb); Mb, idxb = Wb.matrix(comb, 0); band = wf2.lam_min(Mb)
    n = len(idxb)
    rows = [[(j*al)/((j*al)**2-g*g) for j in idxb] for g in zl]
    B = nullspace(rows, n)
    if B:
        k = len(B)
        R = mp.zeros(k, k)
        for a in range(k):
            Mv = Mb*B[a]
            for b in range(a, k):
                R[a,b] = (B[b].T*Mv)[0]; R[b,a] = R[a,b]
        bv = min(mp.eigsy(R, eigvals_only=True))
    else:
        k = 0; bv = mp.nan
    print("%5.2f %7.2f %7d %9.1f %7.2f %8d   | %9.3f %9.3f %9.3f" %
          (Lf, float(tc), len(zl), float(nyq), float(D), k,
           float(mp.log10(true)), float(mp.log10(band)),
           float(mp.log10(bv)) if (bv==bv and bv>0) else float('nan')))
    sys.stdout.flush()
