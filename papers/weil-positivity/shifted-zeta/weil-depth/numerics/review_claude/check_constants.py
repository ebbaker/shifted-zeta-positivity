"""Independent recomputation (mpmath, 60 digits) of the analytic constants
reported in the manuscript, without using any of the supplied code."""
import mpmath as mp
mp.mp.dps = 60

def G0_taylor(M):
    # G0(t) = t e^{t/2}/sinh t - 4 t cosh(t/2); Taylor coefficients via mpmath
    f = lambda t: t*mp.exp(t/2)/mp.sinh(t) - 4*t*mp.cosh(t/2) if t != 0 else mp.mpf(1)
    return mp.taylor(f, 0, M)

def chain_norm(d, L):
    q = int(mp.ceil(L/d))
    return 2*mp.cos(mp.pi/(q+1))

def constants(L, N, M, active):
    g = G0_taylor(M)
    assert abs(g[0]-1) < 1e-40 and abs(g[1]+mp.mpf(7)/2) < 1e-40 and abs(g[2]+mp.mpf(1)/24) < 1e-40
    ratio = L/3
    eta = 256*ratio**(M+1)/((M+1)*(1-ratio))
    K = sum(abs(g[j])*L**(j-1) for j in range(1, M+1)) + mp.mpf(256)/3*ratio**M/(1-ratio)
    arith = sum(mp.log(p)/mp.sqrt(n)*chain_norm(mp.log(n), L) for n, p in active)
    HN = sum(mp.mpf(1)/j for j in range(1, N+1))
    a = HN - mp.euler - mp.log(mp.pi*L) - K*L/(2*mp.sqrt(N*(N+1))) - arith
    CL = mp.cosh(L/2)*(mp.exp(L/2)*L**3/3 + L**2/4)
    CL += sum(mp.log(p)/mp.sqrt(n)*mp.log(n)**2*mp.cosh(mp.log(n)/2)*chain_norm(mp.log(n), L)/2 for n, p in active)
    return dict(a=a, K=K, eta=eta, arith=arith, CL=CL, gmax=max(abs(g[j])*3**j for j in range(M+1)))

active = [(2,2),(3,3),(4,2),(5,5)]
for label, L, N, M, m in [('9/5', mp.mpf(9)/5, 128, 180, mp.mpf('1e-26')),
                          ('log7', mp.log(7), 128, 220, mp.mpf('1e-34'))]:
    c = constants(L, N, M, active)
    eps = (abs(c['a']-m) + 40000)*c['eta'] + 2*c['eta']**2
    print(f"--- L = {label} = {mp.nstr(L, 12)}, N={N}, M={M}")
    print("  tail floor a      =", mp.nstr(c['a'], 16))
    print("  K_L               =", mp.nstr(c['K'], 10))
    print("  eta_M             =", mp.nstr(c['eta'], 6))
    print("  epsilon           =", mp.nstr(eps, 6))
    print("  arithmetic term   =", mp.nstr(c['arith'], 14))
    print("  C_L               =", mp.nstr(c['CL'], 10))
    print("  max |g_j| 3^j     =", mp.nstr(c['gmax'], 6), "(Cauchy majorant used: 256; true sup on |z|=3 bounded by 180)")
    for n in (2,3,4,5,7):
        print(f"    chain norm n={n}:", mp.nstr(chain_norm(mp.log(n), L), 8) if mp.log(n) < L else "inactive/endpoint")

# Continuation rational checks
print("9/5:  1e-26 - 11/3*(3e-14)^2 =", mp.nstr(mp.mpf('1e-26') - mp.mpf(11)/3*mp.mpf('3e-14')**2, 6))
print("log7: 1e-34 - 14/3*(3e-18)^2 =", mp.nstr(mp.mpf('1e-34') - mp.mpf(14)/3*mp.mpf('3e-18')**2, 6))

# Cauchy majorant check on |z|=3 directly
G0 = lambda z: z*mp.exp(z/2)/mp.sinh(z) - 4*z*mp.cosh(z/2)
sup = max(abs(G0(3*mp.exp(1j*mp.mpf(k)/400*2*mp.pi))) for k in range(400))
print("numerical sup |G0| on |z|=3 ~", mp.nstr(sup, 8))
print("3/sin(3) =", mp.nstr(3/mp.sin(3), 8), " e^{3/2} =", mp.nstr(mp.exp(1.5), 8))

# Tail floor at log 8 for various N (prospective)
L8 = mp.log(8); active8 = [(2,2),(3,3),(4,2),(5,5),(7,7)]
for N in (128, 256, 512, 1024, 2048):
    c = constants(L8, N, 220, active8)
    print(f"log8 N={N}: tail floor a = {mp.nstr(c['a'], 8)}, arith={mp.nstr(c['arith'],8)}, K={mp.nstr(c['K'],6)}")
