"""
Checks for the 1 October revision (commit 5a431c1) of manuscript.tex.

 A. Finite Blaschke energy identity  E(Theta) = 4 pi^2 m  (revised Lemma energy) for m = 1,2,3 zeros in
    one half-plane, with unequal widths; and the energy of mixed-orientation products against the
    manuscript's bound 8 pi^2 (m_+ + m_-) and against the sharper 4 pi^2 (m_+ + m_-).
    E(u) is computed as  int |xi| |FT(u - u(inf))(xi)|^2 dxi  by FFT on a long fine grid
    (the constant does not change E).
 B. Interpolation bound  E(f) <= 2 pi ||f||_2 ||f'||_2  on a few test functions.
 C. The sharpened unit-window bound: E(b_j v_sigma) for the actual zeta phase at heights
    j = 10 ... 30000, sigma = 0.6 and 0.51, compared with log(2+j) and with the number of
    critical zeros in the window (sign changes of Hardy's Z).  The old lemma allowed log^2;
    the revision claims C log.  Ratios E/log(2+j) should stay bounded.
"""
import numpy as np, mpmath as mp, time, sys
mp.mp.dps = 15
pi = np.pi

def energy_from_samples(fvals, dt, pad_factor=4):
    """E(f) = int |xi| |fhat(xi)|^2 dxi for f sampled on a uniform grid (f -> 0 off the grid)."""
    n = len(fvals)
    M = 1
    while M < pad_factor*n:
        M *= 2
    F = np.fft.fft(fvals, n=M) * dt            # fhat(xi_k) with the manuscript's convention
    xi = 2*pi*np.fft.fftfreq(M, d=dt)
    dxi = 2*pi/(M*dt)
    return float(np.sum(np.abs(xi)*np.abs(F)**2)*dxi)

print("=== A. Blaschke energies (grid T=4000, dt=0.004) ===")
T, dt = 4000.0, 0.004
t = np.arange(-T, T, dt)
def blaschke(zeros_lower):
    """product over zeros z0 in the LOWER half-plane of (t - z0)/(t - conj z0): analytic in C_-, |.|=1 on R"""
    u = np.ones_like(t, dtype=complex)
    for z0 in zeros_lower:
        u *= (t - z0)/(t - np.conj(z0))
    return u
cases = {
    "m=1, zero at 0-0.1i":                [0-0.1j],
    "m=2, zeros 3-0.1i, -5-2i":           [3-0.1j, -5-2j],
    "m=3, zeros 0-0.05i, 0.3-0.05i, 7-1i": [0-0.05j, 0.3-0.05j, 7-1j],
    "m=3, triple zero at 1-0.2i":          [1-0.2j, 1-0.2j, 1-0.2j],
}
for name, zs in cases.items():
    u = blaschke(zs)
    E = energy_from_samples(u - 1.0, dt)      # u(inf) = 1
    print(f"  {name:40s}  E/(4pi^2) = {E/(4*pi**2):.5f}   (claim: {len(zs)})")
# mixed orientation: u_+ (zeros in upper half-plane) times u_- (zeros in lower half-plane)
def blaschke_upper(zeros_upper):
    u = np.ones_like(t, dtype=complex)
    for z0 in zeros_upper:
        u *= (t - z0)/(t - np.conj(z0))
    return u
mixed = {
    "m+=1 (0+0.1i), m-=1 (0-10i)  [rational model eps=0.1]": ([0+0.1j], [0-10j]),
    "m+=1 (0+0.1i), m-=1 (0-0.1i)":                           ([0+0.1j], [0-0.1j]),
    "m+=2 (0+0.1i, 2+0.3i), m-=1 (-1-0.5i)":                 ([0+0.1j, 2+0.3j], [-1-0.5j]),
}
for name, (zu, zl) in mixed.items():
    u = blaschke_upper(zu)*blaschke(zl)
    E = energy_from_samples(u - 1.0, dt)
    mp_, mm = len(zu), len(zl)
    print(f"  {name:55s} E/(4pi^2) = {E/(4*pi**2):.5f}; manuscript bound 2(m+ + m-) = {2*(mp_+mm)}; sharper bound (m+ + m-) = {mp_+mm}")
eps = 0.1; q = (1-eps**2)/(1+eps**2)
print(f"  (rational model prediction from rank-one blocks: E/(4pi^2) = 2 q^2 = {2*q**2:.5f})")

print("\n=== B. E(f) <= 2 pi ||f||_2 ||f'||_2 ===")
tt = np.arange(-60, 60, 0.002)
for name, f in [("gaussian exp(-t^2/2)", np.exp(-tt**2/2)),
                ("chirp bump exp(-t^2/2) e^{i 5 t}", np.exp(-tt**2/2)*np.exp(5j*tt)),
                ("sech(t)", 1/np.cosh(tt))]:
    E = energy_from_samples(f, 0.002)
    fp = np.gradient(f, 0.002)
    rhs = 2*pi*np.sqrt(np.sum(np.abs(f)**2)*0.002)*np.sqrt(np.sum(np.abs(fp)**2)*0.002)
    print(f"  {name:36s} E = {E:9.4f}   2pi||f|| ||f'|| = {rhs:9.4f}   ratio = {E/rhs:.3f}")

print("\n=== C. window energy E(b_j v_sigma) for the zeta phase ===")
def smoothstep(x):
    x = np.clip(x, 0, 1)
    with np.errstate(divide='ignore', over='ignore', invalid='ignore'):
        a = np.where(x > 0, np.exp(-1/np.maximum(x, 1e-300)), 0.0)
        b = np.where(x < 1, np.exp(-1/np.maximum(1-x, 1e-300)), 0.0)
    return a/(a+b)
def b0(x):   # C_c^inf((-2,2)), equal to 1 on [0,1]
    return smoothstep((x+2)/2) * smoothstep((2-x)/1)
dtw = 0.005
xw = np.arange(-2, 2, dtw)
bw = b0(xw)
print(f"  E(b_0)/(4pi^2) = {energy_from_samples(bw.astype(complex), dtw)/(4*pi**2):.4f}  (fixed cutoff energy)")

def v_sigma(sigma, tv):
    tv = mp.mpf(tv)
    z = mp.zeta(sigma + 1j*tv)
    gam = mp.gamma(mp.mpf('0.25') + 1j*tv/2)/mp.gamma(mp.mpf('0.25') - 1j*tv/2)
    return complex(gam*mp.power(mp.pi, -1j*tv)*z/mp.conj(z))

def zeros_in_window(j, lo=-2.0, hi=2.0, step=0.02):
    ts = np.arange(j+lo, j+hi+step, step)
    Z = np.array([float(mp.siegelz(x)) for x in ts])
    return int(np.sum(np.sign(Z[1:]) != np.sign(Z[:-1])))

heights = [10, 30, 100, 300, 1000, 3000, 10000, 30000]
for sigma in [mp.mpf('0.6'), mp.mpf('0.51')]:
    print(f"\n  sigma = {float(sigma)}")
    print(f"  {'j':>6} {'E/(4pi^2)':>10} {'E/log(2+j)':>11} {'E/log^2(2+j)':>13} {'zeros in (j-2,j+2)':>19} {'zeros weighted by b_j^2':>24} {'time':>6}")
    for j in heights:
        t0 = time.time()
        tv = j + xw
        vals = np.array([v_sigma(sigma, x) for x in tv])
        f = bw*vals
        E = energy_from_samples(f, dtw)
        nz = zeros_in_window(j)
        # zeros weighted by b_j^2 (the Poisson-limit prediction for the window mass)
        ts = np.arange(j-2, j+2+0.02, 0.02); Z = np.array([float(mp.siegelz(x)) for x in ts])
        idx = np.where(np.sign(Z[1:]) != np.sign(Z[:-1]))[0]
        wz = float(np.sum(b0(ts[idx]-j)**2))
        lg = np.log(2+j)
        print(f"  {j:6d} {E/(4*pi**2):10.4f} {E/lg:11.4f} {E/lg**2:13.4f} {nz:19d} {wz:24.3f} {time.time()-t0:5.0f}s")
