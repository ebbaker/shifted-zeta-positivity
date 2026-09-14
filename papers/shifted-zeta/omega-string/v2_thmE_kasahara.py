# Verification, part 2: Theorem 1.6 convergence + the Kasahara dual-curve table
# (Remark 5.1) + the endpoint length L_xi = B(0) (Remark 6.3).
from mpmath import mp, mpf, mpc, zeta, digamma, log, pi, sqrt, quad, exp, mpmathify, im, re

mp.dps = 25

def xilogd(s):
    s = mpmathify(s)
    return 1/s + 1/(s-1) - log(pi)/2 + digamma(s/2)/2 + zeta(s, derivative=1)/zeta(s)

def q(om, z):
    v = sqrt(mpc(z))
    if im(v) < 0: v = -v
    w = -1j*v
    return xilogd(mpf('0.5')+om+w)/w

print("=== (d) Weyl-function convergence q_omega -> q_xi  [Thm 1.6(i)] ===")
for z in [mpc(0,1), mpc(-1,2)]:
    q0 = q(mpf(0), z)
    for om in ['0.5','0.2','0.1','0.05','0.02','0.01']:
        d = abs(q(mpf(om), z) - q0)
        print("z=%s  om=%s  |q_om - q_xi| = %.4e  (/om = %.4f)" % (str(z), om, float(d), float(d/mpf(om))))
    print()

print("=== (e) vague convergence: J(om) = int rho_om(u) f(u) du -> f(gamma_1) = 1  [Thm 1.6(ii)] ===")
g1 = mp.zetazero(1).imag
print("gamma_1 =", mp.nstr(g1,12))
f = lambda u: exp(-(u-g1)**2)
def rho(om, u):
    return re(xilogd(mpc(mpf('0.5')+om, u)))/pi
for om in ['0.5','0.2','0.1','0.05','0.02']:
    omv = mpf(om)
    J = quad(lambda u: rho(omv,u)*f(u), [g1-8, g1-1, g1-5*omv, g1, g1+5*omv, g1+1, g1+7])
    print("om=%s   J = %.6f" % (om, float(J)))

print()
print("=== (f) Kasahara dual curve (omega=1/2): M(y)/[4x/log^2 x], x=q(-y)  [Rem 5.1] ===")
for y in ['1e-6','1','1e3','1e6','1e9','1e12','1e15']:
    yv = mpf(y)
    qq = xilogd(1+sqrt(yv))/sqrt(yv)
    ratio = (1/(yv*qq)) / (4*qq/(log(qq))**2)
    print("y=%7s  x=%.4e  ratio=%.5f" % (y, float(qq), float(ratio)))

print()
print("=== (g) endpoint length: q_xi(-s) -> B(0) = (xi'/xi)'(1/2)  [Rem 6.3] ===")
for s in ['1e-2','1e-4','1e-6','1e-10']:
    sv = mpf(s)
    print("s=%7s  q_xi(-s) = %.12f" % (s, float(xilogd(mpf('0.5')+sqrt(sv))/sqrt(sv))))
h = mpf('1e-8')
B0 = (xilogd(mpf('0.5')+h)-xilogd(mpf('0.5')-h))/(2*h)
print("B(0) = (xi'/xi)'(1/2) =", mp.nstr(B0, 12))
