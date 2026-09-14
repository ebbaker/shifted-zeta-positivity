# Verification, part 1: the analytic identities behind Theorems 1.1 and 1.2
# of "The shifted zeta string" (residue lemma, Fourier block, constants).
# Referenced in the paper's Section 7 and in the ROUND15 audit record.
from mpmath import mp, mpf, mpc, zeta, digamma, log, pi, sqrt, quad, cos, exp, mpmathify, im, re

mp.dps = 40

def xilogd(s):
    s = mpmathify(s)
    if s == 1: s = mpf(1)+mpf('1e-22')   # the 1/(s-1) and zeta'/zeta poles cancel at s=1
    return 1/s + 1/(s-1) - log(pi)/2 + digamma(s/2)/2 + zeta(s, derivative=1)/zeta(s)

print("=== (a) per-pair residue identity  T(z) = I_pair(z)  [Lemma 3.1] ===")
# T(z) = (1/w)[1/(a+w-i g) + 1/(a+w+i g)],  w = -i sqrt(z)  (Im sqrt(z) > 0 off [0,inf))
# I_pair(z) = int_R (1/pi)[a/(a^2+(u-g)^2) + a/(a^2+(u+g)^2)] / (u^2 - z) du
for (a, g, z) in [(mpf('0.7'), mpf('14.13'), mpc(2,3)), (mpf('0.5'), mpf('21.02'), mpc(-5,'0.001')),
                  (mpf('1.3'), mpf('3.7'),  mpc('0.5','-2')), (mpf('0.5'), mpf('50'), mpc(100,1))]:
    v = sqrt(z)
    if im(v) < 0: v = -v
    w = -1j*v
    T = (1/w)*(1/(a+w-1j*g) + 1/(a+w+1j*g))
    f = lambda u: ((a/(a**2+(u-g)**2) + a/(a**2+(u+g)**2))/pi) / (u**2 - z)
    # split points at the Lorentzian centres and, for near-cut z, near Re sqrt(z)
    r = abs(re(v))
    pts = sorted(set([-g, 0, g] + ([-r, r] if r > 1 else [])))
    I = quad(f, [-mp.inf] + pts + [mp.inf], maxdegree=12)
    print("a=%s g=%s z=%s   |T-I| = %.3e" % (a, g, str(z), abs(T-I)))

print()
print("=== (b) Fourier block:  int_0^inf (1-cos ut) e^{izt} dt = -i u^2/(z(z^2-u^2)) ===")
for (u, z, tmax) in [(mpf(3), mpc(1,'0.8'), 400), (mpf('0.4'), mpc(-2,'1.1'), 300)]:
    lhs = quad(lambda t: (1-cos(u*t))*exp(1j*z*t), [0, tmax])
    rhs = -1j*u**2/(z*(z**2-u**2))
    print("u=%s z=%s   |lhs-rhs| = %.3e" % (u, str(z), abs(lhs-rhs)))

print()
print("=== (c) constants ===")
gamma_ = mp.euler
sl_closed = gamma_/2 + 1 - log(4*pi)/2
sl_direct = xilogd(1)
print("xi'/xi(1) closed form g/2+1-log(4pi)/2 =", mp.nstr(sl_closed, 16))
print("xi'/xi(1) direct (regularized)         =", mp.nstr(sl_direct, 16))
print("rho_inf = slope^-2                     =", mp.nstr(1/sl_closed**2, 12))
print("rho(0)  = slope/pi                     =", mp.nstr(sl_closed/pi, 8))
