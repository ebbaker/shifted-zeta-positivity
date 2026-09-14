"""Check 4: per-gamma identity: integral definition (eq:Psiomegadef applied to a single
term f(u)=(1-cos(gamma u))/gamma^2, gamma possibly complex) equals the bracket in
eq:Psiomegaseries. Also check the exponential decomposition of the remainder used in the
revised proof: (g^2-w^2)cos(gt)+2gw sin(gt) = (1/2)[e^{igt}(g-iw)^2 + e^{-igt}(g+iw)^2]."""
import mpmath as mp
mp.mp.dps = 30

def series_term(g, w, t):
    return ( w*t*(g**2+w**2) + (g**2-w**2)
             - mp.e**(-w*t)*(g**2-w**2)*mp.cos(g*t)
             - mp.e**(-w*t)*2*g*w*mp.sin(g*t) ) / (g**2+w**2)**2

def def_term(g, w, t):
    f = lambda u: (1-mp.cos(g*u))/g**2
    I1 = mp.quad(lambda u: mp.e**(-w*u)*f(u), [0, t])
    I2 = mp.quad(lambda u: (t-u)*mp.e**(-w*u)*f(u), [0, t])
    return mp.e**(-w*t)*f(t) + 2*w*I1 + w**2*I2

for g in [mp.mpf('14.1347'), mp.mpc('14.1347','0.2'), mp.mpc('-3.7','-0.45')]:
    for (w, t) in [(mp.mpf('0.3'), mp.mpf('2.0')), (mp.mpf('0.05'), mp.mpf('7.5'))]:
        a = series_term(g, w, t); b = def_term(g, w, t)
        print("g=",mp.nstr(g,6),"w=",mp.nstr(w,3),"t=",mp.nstr(t,3)," series:",mp.nstr(a,12)," defn:",mp.nstr(b,12)," diff:",mp.nstr(abs(a-b),3))

print()
# exponential decomposition
for g in [mp.mpc('14.1','0.3'), mp.mpc('-7.2','-0.1')]:
    w, t = mp.mpf('0.27'), mp.mpf('3.3')
    lhs = (g**2-w**2)*mp.cos(g*t) + 2*g*w*mp.sin(g*t)
    rhs = ( mp.e**(1j*g*t)*(g-1j*w)**2 + mp.e**(-1j*g*t)*(g+1j*w)**2 )/2
    print("decomp diff:", mp.nstr(abs(lhs-rhs),3))

# A*-B identity: A*-B = sum (b-w)^2/|g-iw|^4 + (b+w)^2/|g+iw|^4 per zero
g = mp.mpc('21.02','0.18'); w = mp.mpf('0.31')
Astar = (1/abs(g-1j*w)**2 + 1/abs(g+1j*w)**2)/2
Bterm = mp.re((g**2-w**2)/(g**2+w**2)**2)  # use re: pairing with conjugate
b = mp.im(g)
ident = (b-w)**2/abs(g-1j*w)**4 + (b+w)**2/abs(g+1j*w)**4
print("A*-B per-zero identity diff:", mp.nstr(abs((Astar-Bterm)-ident),3))
