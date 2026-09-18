"""
The phase-matched lattice controls of the Wilson-lines review, in the basis the transfer is
compressed to, against the transfer's own margin.  Unregistered (mpmath).

THE COMPARISON.  Under RH the localized Weil form is the absorption
    Q_{0,L}[f] = sum_rho |F(gamma_rho)|^2,   F(t) = int f(x) e^{i t x} dx, supp f in I_L,
so its margin m_L is how well a function supported in an interval can avoid the Riemann zeros
in frequency.  Replacing the zeros by an unfolded lattice of the same density gives a control;
the review of 17 September (../../wilson-lines/reviews/review_claude-fable-5-1_2026-09-17.md,
Section 3) showed the control is PHASE-dependent, the half-shifted lattice theta(t) = (k-1/2)pi
(Gram's-law idealisation, counting function equal to N_sm on average) tracking the zeros while
the Gram points themselves sit one half-integer off in either direction and miss by orders of
magnitude.

The transfer has NO lattice analogue: k_omega is assembled from Gamma, sinh and the integers,
and its compression knows the zeros only through the poles of Khat_omega.  So this control lives
on the form side alone, and putting it beside lambda_min(D_{omega,L})/(2 omega) measures what the
transfer knows that a lattice does not.

Every lattice value is a trial-space Rayleigh quotient in the SAME N-mode even block, an upper
bound on its own infimum; truncating the point set at T lowers it slightly.  Nothing here is a
positivity certificate.

Usage:  python3 gram_control_vs_transfer.py [T_cutoff] [N] [dps]     (defaults 3000, 24, 50)
"""
import sys, os, json, time
import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '../../../wilson-lines/numerics/exploratory'))
import weil_sine_basis as wsb

# lambda_min(D_{omega,L})/(2 omega) at omega = 0.01 in the same N = 24 basis, from the records
# cmgj_om0.01_log{3,5,7}_N24.json of contraction_margin_gj.py (40-70 digits).
TRANSFER = {"log3": mp.mpf("6.2813855951291e-8"),
            "log5": mp.mpf("2.5749661266817e-17"),
            "log7": mp.mpf("2.1456039609203e-22")}


def gram_points(T):
    out, n = [], -1
    while True:
        g = mp.grampoint(n)
        if g > T:
            return out
        out.append(g)
        n += 1


def half_shift_points(GR, T):
    """theta(t) = (k - 1/2) pi: the lattice one half-step from the Gram points."""
    dth = lambda t: mp.re(mp.digamma(mp.mpf(1)/4 + 1j*t/2))/2 - mp.log(mp.pi)/2
    out = []
    for i in range(len(GR) - 1):
        g = (GR[i] + GR[i+1])/2
        tgt = (i - 1)*mp.pi + mp.pi/2            # theta(GR[i]) = (i-1) pi
        for _ in range(8):
            g = g - (mp.siegeltheta(g) - tgt)/dth(g)
        if g > T:
            break
        out.append(g)
    return out


def lam_pts(L, N, pts, parity=0):
    """lambda_min of sum_t |F(t)|^2 in the orthonormal sine basis, one parity block."""
    al = mp.pi/L
    idx = [j for j in range(1, N+1) if (j-1) % 2 == parity]
    n = len(idx)
    s2L = mp.sqrt(2/L)
    ja = [j*al for j in idx]
    sg = [(-1)**j for j in idx]
    M = [[mp.mpf(0)]*n for _ in range(n)]
    for t in pts:
        cs, sn, tt = mp.cos(t*L), mp.sin(t*L), t*t
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


def main():
    T = mp.mpf(sys.argv[1]) if len(sys.argv) > 1 else mp.mpf(3000)
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 24
    mp.mp.dps = int(sys.argv[3]) if len(sys.argv) > 3 else 50
    t0 = time.time()
    GR = gram_points(T)
    HS = half_shift_points(GR, T)
    rows = {}
    for name, nn in (("log3", 3), ("log5", 5), ("log7", 7)):
        L = mp.log(nn)
        W = wsb.WeilForm(L, N)
        Me, _ = W.matrix(wsb.prime_comb(L), 0)
        zeros = min(mp.eigsy(Me, eigvals_only=True))
        vals = {"zeros (exact Weil form)": zeros,
                "gram n >= -1": lam_pts(L, N, GR),
                "gram n >= 0": lam_pts(L, N, GR[1:]),
                "half-shifted": lam_pts(L, N, HS),
                "transfer lambda_min(D)/(2 omega), omega = 0.01": TRANSFER[name]}
        rows[name] = {k: mp.nstr(v, 10) for k, v in vals.items()}
        rows[name]["log10 gaps to the zeros"] = {
            k: mp.nstr(mp.log10(v/zeros), 6) for k, v in vals.items() if k != "zeros (exact Weil form)"}
        rows[name]["transfer / zeros"] = mp.nstr(vals["transfer lambda_min(D)/(2 omega), omega = 0.01"]/zeros, 10)
        rows[name]["half-shifted / zeros"] = mp.nstr(vals["half-shifted"]/zeros, 10)
    print(json.dumps({
        "programme": "gram_control_vs_transfer.py", "N": N, "even_block": True,
        "T_cutoff": mp.nstr(T, 8), "dps": mp.mp.dps,
        "gram_points": len(GR), "half_shift_points": len(HS),
        "lowest points": {"gram n >= -1": mp.nstr(GR[0], 8), "gram n >= 0": mp.nstr(GR[1], 8),
                          "half-shifted": mp.nstr(HS[0], 8), "gamma_1": "14.134725"},
        "horizons": rows,
        "scope": "trial-space Rayleigh quotients in a fixed basis; not a positivity certificate",
        "seconds": round(time.time()-t0, 1)}, indent=1))


if __name__ == "__main__":
    main()
