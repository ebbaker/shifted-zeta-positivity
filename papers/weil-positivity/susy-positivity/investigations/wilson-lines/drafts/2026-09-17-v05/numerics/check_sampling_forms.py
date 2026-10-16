#!/usr/bin/env python3
"""
Closed forms for the localized Weil form in the sine basis, and the sampling
budget at the crossover.  Standard library only; prints JSON to stdout.

WHAT IS CHECKED (nothing here is a positivity certificate):

  A. Basis algebra.  For the orthonormal sine basis of L^2(-L/2, L/2),
     psi_j(x) = sqrt(2/L) sin(j pi (x + L/2)/L), the closed forms used to
     assemble Q_{0,L} are checked against direct quadrature:
       S_{jk}(u) = g_{jk}(u) + g_{jk}(-u),  g_{jk}(u) = int psi_j(x) psi_k(x-u) dx
       E_j^{pm}  = int psi_j(x) e^{pm x/2} dx
     and the parity rule S_{jk} = 0 for j-k odd.

  B. Archimedean integrals.  n(r) = e^{-r/2}/(1-e^{-2r}).  The three families
       A_m = int_0^L sin(m alpha r) n(r) dr
       B_k = int_0^L [(L-r) cos(k alpha r) - L] n(r) dr
       C   = int_0^L (e^{-r/2} - 1) n(r) dr
     are summed in closed form by n(r) = sum_{q>=0} e^{-(2q+1/2) r}, splitting
     each q-term into a piece that telescopes into digamma/trigamma at 1/4 and
     a piece carrying e^{-beta L} that is geometric in q.  Checked against
     quadrature.  Also  int_L^inf e^{-r/2} n(r) dr = artanh(e^{-L}).

  C. Matrix elements against the zeros.  Q_{jk} assembled from A and B is
     compared with  2 sum_{gamma>0} Re[psihat_j(gamma) conj(psihat_k(gamma))]
     over hard-coded published ordinates, plus the smooth tail beyond the last
     one.  Agreement is limited by that tail, so the tolerance is loose; this
     checks the assembly, not the arithmetic of zeta.

  D. The sampling budget.  tau_c = 2 pi e^L (density crossover), T_* = 2 pi
     e^{L+1} (count crossover), and the exact maximal deficit
     D(L) = Nyquist count - 2N(tau_c) = 2 e^L - 7/4, against the
     Riemann-von Mangoldt main term at several horizons.

  E. Units.  The wilson-lines / shifted-zeta convention supports f in
     (-L/2, L/2) and sums primes over n < e^L; Zhu (arXiv:2608.24827) supports
     f in (-L, L) and sums over n < e^{2L}.  The two prime sets are compared,
     which is the content of the factor of two between the two L's.

Every tolerance below is a numerical agreement threshold, not a theorem.
"""
import cmath, json, math

# ---------------------------------------------------------------- utilities
BERN = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510]

def digamma_c(z):
    """psi(z) for complex z, Re z > 0: recurrence up to |z|>12 then Stirling."""
    s = 0j
    while abs(z) < 12:
        s -= 1/z
        z += 1
    r = cmath.log(z) - 1/(2*z)
    z2 = z*z
    p = z2
    for k, b in enumerate(BERN, start=1):
        r -= b/(2*k*p)
        p *= z2
    return s + r

def trigamma_c(z):
    s = 0j
    while abs(z) < 12:
        s += 1/(z*z)
        z += 1
    r = 1/z + 1/(2*z*z)
    z2 = z*z
    p = z2*z
    for k, b in enumerate(BERN, start=1):
        r += b/p
        p *= z2
    return s + r

def gauss_legendre(n):
    """Nodes/weights on [-1,1] by Newton on the Legendre polynomial."""
    xs, ws = [], []
    for i in range(1, n+1):
        x = math.cos(math.pi*(i-0.25)/(n+0.5))
        for _ in range(100):
            p0, p1 = 1.0, 0.0
            for j in range(1, n+1):
                p0, p1 = ((2*j-1)*x*p0 - (j-1)*p1)/j, p0
            dp = n*(x*p0 - p1)/(x*x - 1)
            dx = -p0/dp
            x += dx
            if abs(dx) < 1e-16:
                break
        xs.append(x); ws.append(2/((1-x*x)*dp*dp))
    return xs, ws

GLX, GLW = gauss_legendre(80)

def quad(f, a, b, panels=40):
    tot = 0.0
    for p in range(panels):
        lo = a + (b-a)*p/panels
        hi = a + (b-a)*(p+1)/panels
        c, h = (lo+hi)/2, (hi-lo)/2
        tot += h*sum(w*f(c + h*x) for x, w in zip(GLX, GLW))
    return tot

def relerr(a, b):
    d = max(abs(a), abs(b), 1e-300)
    return abs(a-b)/d

# ---------------------------------------------------------------- the forms
def psi_basis(L, j, x):
    return math.sqrt(2/L)*math.sin(j*math.pi*(x + L/2)/L)

def S_closed(L, j, k, u):
    al = math.pi/L
    if (j-k) % 2:
        return 0.0
    if j == k:
        return 2/L*((L-u)*math.cos(k*al*u) + math.sin(k*al*u)/(k*al))
    sj, sk = math.sin(j*al*u), math.sin(k*al*u)
    return 2/math.pi*((sk-sj)/(j-k) + (sj+sk)/(j+k))

def E_closed(L, j, sign):
    al, beta = math.pi/L, sign*0.5
    I = j*al*(1 - (-1)**j*math.exp(beta*L))/(beta*beta + (j*al)**2)
    return math.sqrt(2/L)*math.exp(-beta*L/2)*I

def n_arch(r):
    return math.exp(-r/2)/(-math.expm1(-2*r))

def geo(term, L, tol=1e-18):
    tot, q = 0.0, 0
    while True:
        t = term(2*q + 0.5)
        tot += t
        if q > 3 and abs(t) < tol*max(abs(tot), 1.0):
            return tot
        q += 1
        if q > 100000:
            return tot

PSI14 = digamma_c(0.25+0j).real

def A_closed(L, m):
    c = m*math.pi/L
    head = digamma_c(0.25 + 0.5j*c).imag/2
    tail = -(-1)**m*c*geo(lambda b: math.exp(-b*L)/(b*b + c*c), L)
    return head + tail

def B_closed(L, k):
    c = k*math.pi/L
    head = (-L/2*(digamma_c(0.25+0.5j*c).real - PSI14)
            - trigamma_c(0.25+0.5j*c).real/4)
    sub = geo(lambda b: math.exp(-b*L)*(-(-1)**k*(b*b-c*c)/(b*b+c*c)**2 - L/b), L)
    return head - sub

def C_closed(L):
    head = (PSI14 - digamma_c(0.5+0j).real)/2
    sub = geo(lambda b: math.exp(-(b+0.5)*L)/(b+0.5) - math.exp(-b*L)/b, L)
    return head - sub

def Sint_closed(L, j, k, A, B):
    if (j-k) % 2:
        return 0.0
    if j == k:
        return 2/L*(B[k] + A[k]/(k*math.pi/L))
    return 2/math.pi*((A[k]-A[j])/(j-k) + (A[j]+A[k])/(j+k))

def primes_below(x):
    n = int(x)+2
    s = [True]*(n+1); s[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if s[i]:
            s[i*i::i] = [False]*len(s[i*i::i])
    return [i for i, v in enumerate(s) if v]

def prime_comb(L):
    out = []
    for p in primes_below(math.exp(L)):
        m = 1
        while m*math.log(p) < L:
            out.append((m*math.log(p), math.log(p)*p**(-m/2))); m += 1
    return out

def Q_entry(L, j, k, A, B, C, comb):
    d = 1.0 if j == k else 0.0
    pole = E_closed(L, j, +1)*E_closed(L, k, -1) + E_closed(L, j, -1)*E_closed(L, k, +1)
    const = -(math.log(4*math.pi) + 0.5772156649015328606)*d
    arch = -(Sint_closed(L, j, k, A, B) - 2*d*C) + 2*d*math.atanh(math.exp(-L))
    pr = sum(w*S_closed(L, j, k, dd) for dd, w in comb)
    return pole + const + arch - pr

def psihat2_pair(L, j, k, t):
    """psihat_j(t) conj(psihat_k(t)), real part, for the two-sided zero sum."""
    al = math.pi/L
    nj = (j*al)*(1 - (-1)**j*cmath.exp(-1j*t*L))/((j*al)**2 - t*t)
    nk = (k*al)*(1 - (-1)**k*cmath.exp(-1j*t*L))/((k*al)**2 - t*t)
    return (2/L)*(nj*nk.conjugate()).real

# first 100 ordinates of the zeros of zeta on the critical line (published data)
ZEROS = [
 14.134725142, 21.022039639, 25.010857580, 30.424876126, 32.935061588,
 37.586178159, 40.918719012, 43.327073281, 48.005150881, 49.773832478,
 52.970321478, 56.446247697, 59.347044003, 60.831778525, 65.112544048,
 67.079810529, 69.546401711, 72.067157674, 75.704690699, 77.144840069,
 79.337375020, 82.910380854, 84.735492981, 87.425274613, 88.809111208,
 92.491899271, 94.651344041, 95.870634228, 98.831194218, 101.317851006,
 103.725538040, 105.446623052, 107.168611184, 111.029535543, 111.874659177,
 114.320220915, 116.226680321, 118.790782866, 121.370125002, 122.946829294,
 124.256818554, 127.516683880, 129.578704200, 131.087688531, 133.497737203,
 134.756509753, 138.116042055, 139.736208952, 141.123707404, 143.111845808,
 146.000982487, 147.422765343, 150.053520421, 150.925257612, 153.024693811,
 156.112909294, 157.597591818, 158.849988171, 161.188964138, 163.030709687,
 165.537069188, 167.184439978, 169.094515416, 169.911976479, 173.411536520,
 174.754191523, 176.441434298, 178.377407776, 179.916484020, 182.207078484,
 184.874467848, 185.598783678, 187.228922584, 189.416158656, 192.026656361,
 193.079726604, 195.265396680, 196.876481841, 198.015309676, 201.264751944,
 202.493594514, 204.189671803, 205.394697202, 207.906258888, 209.576509717,
 211.690862595, 213.347919360, 214.547044783, 216.169538508, 219.067596349,
 220.714918839, 221.430705555, 224.007000255, 224.983324670, 227.421444280,
 229.337413306, 231.250188700, 231.987235253, 233.693404179, 236.524229666]

def main():
    out = {"groups": [], "note": "counts are finite test cases, not theorems"}

    # ---- A. basis algebra -------------------------------------------------
    cases, worst = 0, 0.0
    for L in (1.0, 1.6, 2.5, 3.0):
        for (j, k) in [(1,1),(2,2),(3,3),(1,3),(2,4),(3,5),(1,5),(4,6),(1,2),(2,3)]:
            for u in (0.0, 0.17*L, 0.5*L, 0.83*L):
                num = (quad(lambda x: psi_basis(L,j,x)*psi_basis(L,k,x-u), -L/2+u, L/2)
                       + quad(lambda x: psi_basis(L,j,x)*psi_basis(L,k,x+u), -L/2, L/2-u))
                worst = max(worst, abs(num - S_closed(L,j,k,u))); cases += 1
        for j in range(1, 8):
            for s in (+1, -1):
                num = quad(lambda x: psi_basis(L,j,x)*math.exp(s*x/2), -L/2, L/2)
                worst = max(worst, relerr(num, E_closed(L,j,s))); cases += 1
    out["groups"].append({"name": "A. sine-basis closed forms S_jk and E_j^pm",
                          "cases": cases, "worst_error": worst, "tolerance": 1e-11,
                          "pass": worst < 1e-11})

    # ---- B. archimedean integrals ----------------------------------------
    cases, worst = 0, 0.0
    for L in (1.0, 1.6, 2.5, 3.0):
        al = math.pi/L
        for m in (1, 2, 3, 5, 8, 13, 21):
            num = quad(lambda r: (math.sin(m*al*r)*n_arch(r) if r > 1e-14 else m*al/2), 0.0, L)
            worst = max(worst, relerr(num, A_closed(L, m))); cases += 1
        for k in (1, 2, 3, 5, 8, 13):
            num = quad(lambda r: (((L-r)*math.cos(k*al*r)-L)*n_arch(r) if r > 1e-14 else -0.5), 0.0, L)
            worst = max(worst, relerr(num, B_closed(L, k))); cases += 1
        num = quad(lambda r: (math.expm1(-r/2)*n_arch(r) if r > 1e-14 else -0.25), 0.0, L)
        worst = max(worst, relerr(num, C_closed(L))); cases += 1
        num = quad(lambda r: math.exp(-r/2)*n_arch(r), L, L+120, panels=200)
        worst = max(worst, relerr(num, math.atanh(math.exp(-L)))); cases += 1
        A = [0.0]+[A_closed(L,m) for m in range(1, 17)]
        B = [0.0]+[B_closed(L,k) for k in range(1, 9)]
        for (j,k) in [(1,1),(2,2),(1,3),(2,4),(3,5),(1,5)]:
            num = quad(lambda r: ((S_closed(L,j,k,r)-S_closed(L,j,k,0.0))*n_arch(r)
                                  if r > 1e-12 else 0.0), 1e-12, L)
            worst = max(worst, relerr(num, Sint_closed(L,j,k,A,B))); cases += 1
    out["groups"].append({"name": "B. archimedean integrals in closed form",
                          "cases": cases, "worst_error": worst, "tolerance": 1e-9,
                          "pass": worst < 1e-9})

    # ---- C. matrix elements against the zeros ----------------------------
    cases, worst = 0, 0.0
    T = ZEROS[-1]
    for L in (1.0, 1.6, 2.5):
        A = [0.0]+[A_closed(L,m) for m in range(1, 17)]
        B = [0.0]+[B_closed(L,k) for k in range(1, 9)]
        C = C_closed(L); comb = prime_comb(L)
        for (j,k) in [(1,1),(2,2),(3,3),(1,3),(2,4),(1,5),(3,5)]:
            ef = Q_entry(L, j, k, A, B, C, comb)
            zs = 2*sum(psihat2_pair(L,j,k,g) for g in ZEROS)
            tail = 2*quad(lambda t: psihat2_pair(L,j,k,t)*math.log(t/(2*math.pi))/(2*math.pi),
                          T, T+4000, panels=400)
            worst = max(worst, relerr(ef, zs+tail)); cases += 1
    out["groups"].append({"name": "C. Q_jk (explicit formula) vs the zero sum, 100 ordinates + smooth tail",
                          "cases": cases, "worst_error": worst, "tolerance": 3e-3,
                          "pass": worst < 3e-3,
                          "scope": "checks the assembly; accuracy is limited by the truncated tail"})

    # ---- D. the sampling budget ------------------------------------------
    cases, worst, rows = 0, 0.0, []
    for L in (math.log(3), math.log(5), math.log(7), 2.0, 3.0, 4.0):
        tc = 2*math.pi*math.exp(L)
        nyq = L*tc/math.pi                               # 2 L e^L
        twoN = tc/math.pi*math.log(tc/(2*math.pi*math.e)) + 7/4
        d_meas, d_exact = nyq - twoN, 2*math.exp(L) - 7/4
        worst = max(worst, abs(d_meas - d_exact)); cases += 1
        # T_* : cumulative counts cross where 2N(T) = L T / pi
        Tstar = 2*math.pi*math.exp(L+1)
        worst = max(worst, abs(Tstar/math.pi*math.log(Tstar/(2*math.pi*math.e)) + 7/4
                               - (L*Tstar/math.pi) - 7/4)); cases += 1
        rows.append({"L": L, "tau_c": tc, "nyquist_count": nyq,
                     "two_N_tau_c": twoN, "deficit": d_meas, "2e^L-7/4": d_exact,
                     "T_star": Tstar})
    out["groups"].append({"name": "D. D(L) = 2 e^L - 7/4 exactly, and T_* = 2 pi e^{L+1}",
                          "cases": cases, "worst_error": worst, "tolerance": 1e-9,
                          "pass": worst < 1e-9, "rows": rows})

    # ---- E. the factor of two between the two conventions ----------------
    cases, worst, rows = 0, 0.0, []
    for Lz in (0.8, 1.0, 2.0):
        # Zhu: f supported in [-L_z, L_z], autocorrelation in [-2L_z, 2L_z],
        #      A_{L_z} = sum_{log n < 2 L_z} 2 Lambda(n)/sqrt(n) ~ 4 e^{L_z}
        A_zhu = 0.0
        for p_ in primes_below(math.exp(2*Lz)):
            m = 1
            while m*math.log(p_) < 2*Lz:
                A_zhu += 2*math.log(p_)*p_**(-m/2); m += 1
        # here: f supported in (-L/2, L/2), autocorrelation in (-L, L),
        #       comb over n < e^L.  The two coincide iff L = 2 L_z.
        A_here = sum(2*w for _, w in prime_comb(2*Lz))
        worst = max(worst, relerr(A_zhu, A_here)); cases += 1
        rows.append({"L_zhu": Lz, "L_here": 2*Lz, "A_L": A_zhu,
                     "identical_to_comb_here_at_L=2L_zhu": relerr(A_zhu, A_here) < 1e-14,
                     "4 e^{L_zhu} (PNT)": 4*math.exp(Lz)})
    out["groups"].append({"name": "E. conventions: f in (-L/2,L/2) here, f in (-L,L) in arXiv:2608.24827",
                          "cases": cases, "worst_error": worst, "tolerance": 1e-14,
                          "pass": worst < 1e-14,
                          "scope": "bookkeeping: Zhu's prime mass A_L at L_zhu is this comb at L = 2 L_zhu"})

    out["all_pass"] = all(g.get("pass", False) for g in out["groups"])
    out["total_checks"] = sum(g.get("cases", 0) for g in out["groups"])
    print(json.dumps(out, indent=2))

if __name__ == "__main__":
    main()
