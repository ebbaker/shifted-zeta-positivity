"""
Check 2b (redo): T_L = b(H_N) + K_L tested on f(x) = sin^4(pi x/L), which is the finite
cosine sum (3/8) - (1/2)cos(2 pi x/L) + (1/8) cos(4 pi x/L).  Its zero extension is C^3,
|Fhat|^2 ~ tau^{-10}, and Fhat is analytic (sinc's).  The Fourier side is the closed
logarithmic form t_L[f]; the cosine side is sum_j b_j |<e_j,f>|^2 + <f, K_L f> with the
kernel of K_L evaluated by the method of images and integrated by scipy dblquad.
"""
import mpmath as mp, numpy as np, json
from scipy import integrate
mp.mp.dps = 25
res = {}
for Lf in ['1.0', '1.3', '2.5']:
    L = mp.mpf(Lf); Ld = float(L)
    coef = [(mp.mpf(3)/8, 0), (-mp.mpf(1)/2, 2*mp.pi/L), (mp.mpf(1)/8, 4*mp.pi/L)]
    def E(alpha): return L*mp.e**(1j*alpha*L/2)*mp.sinc(alpha*L/2)
    def Fhat(t): return sum(cc*(E(w-t)+E(-w-t))/2 for cc, w in coef)
    psi14 = mp.digamma(mp.mpf(1)/4)
    def b_tau2(t): return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*mp.mpf(t)/2)) - psi14
    pts = mp.linspace(0, 120, 481) + [160, 240, 400, 800, 2000, mp.inf]
    tL = 2*mp.quad(lambda t: b_tau2(t)*abs(Fhat(t))**2, pts)/(2*mp.pi)
    # cosine side: coefficients  <e_0,f> = (3/8) sqrt(L),  <e_2,f> = -(1/2) sqrt(L/2),  <e_4,f> = (1/8) sqrt(L/2)
    f0, f2, f4 = mp.mpf(3)/8*mp.sqrt(L), -mp.mpf(1)/2*mp.sqrt(L/2), mp.mpf(1)/8*mp.sqrt(L/2)
    bpart = b_tau2(0)*f0**2 + b_tau2(2*mp.pi/L)*f2**2 + b_tau2(4*mp.pi/L)*f4**2
    # <f, K_L f> with image kernel (double precision)
    def nfun(t): return np.exp(-t/2)/(1-np.exp(-2*t))
    def Kimg(x, y, M=30):
        m = np.arange(M)
        return (nfun(x+y+2*m*Ld) + nfun((2*m+2)*Ld-x-y) + nfun((2*m+2)*Ld+x-y) + nfun((2*m+2)*Ld-x+y)).sum()
    fd = lambda x: np.sin(np.pi*x/Ld)**4
    Kff, err = integrate.dblquad(lambda y, x: Kimg(x, y)*fd(x)*fd(y), 0, Ld, 0, Ld, epsabs=1e-13, epsrel=1e-13)
    cos_side = bpart + mp.mpf(Kff)
    res[Lf] = dict(tL_fourier=float(tL), b_HN_part=float(bpart), Kff=Kff, Kff_quad_err=err,
                   cosine_side=float(cos_side), diff=float(tL-cos_side))
    print(f"L={Lf}: t_L[f]={mp.nstr(tL,14)}  b-part={mp.nstr(bpart,12)}  <f,K_L f>={Kff:.12f} (+-{err:.1e})  diff={mp.nstr(tL-cos_side,3)}")
json.dump(res, open('chk2b.json', 'w'), indent=1)
