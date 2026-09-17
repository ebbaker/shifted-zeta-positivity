# UNREGISTERED exploratory programme (requires mpmath). Claude Opus 5, 17 Sep 2026.
"""Two factors at the common shift a=1: the family matching I_2 and I_4, and what I_6 does to it."""
import mpmath as mp
mp.mp.dps = 50
B = lambda n,a: mp.bernpoly(n,a)
q = mp.mpf(1)/4; one = mp.mpf(1)
TG = [mp.mpf(2)**(2*m-1)*B(2*m,q) for m in range(1,5)]

def inv(factors, M=4):
    lam = 2*mp.fsum(n*b for n,a,b in factors)
    return lam, [lam**(2*m-1)*mp.fsum(n*B(2*m,a)/b**(2*m-1) for n,a,b in factors) for m in range(1,M+1)]

print("1. the ratio Gamma(1+i r tau)/Gamma(1+i tau): I_2 = -(r-1)^2/(3r).")
print("   I_2 = -1/24  <=>  8r^2-17r+8 = 0  <=>  r = (17 +- sqrt 33)/16")
r = (17+mp.sqrt(33))/16
lam,I = inv([(one,one,r),(-one,one,one)])
print("   r = %s   Lambda=%s" % (mp.nstr(r,16), mp.nstr(lam,10)))
print("   I_2 = %s   target %s   diff %s" % (mp.nstr(I[0],14), mp.nstr(TG[0],14), mp.nstr(abs(I[0]-TG[0]),3)))
print("   I_4 = %s   claim 5/384 = %s   diff %s" % (mp.nstr(I[1],14), mp.nstr(mp.mpf(5)/384,14), mp.nstr(abs(I[1]-mp.mpf(5)/384),3)))
print("   I_4/target = %s   claim 25/28 = %s" % (mp.nstr(I[1]/TG[1],12), mp.nstr(mp.mpf(25)/28,12)))
print("   other root r' = %s = 1/r ? diff %s" % (mp.nstr((17-mp.sqrt(33))/16,12), mp.nstr(abs((17-mp.sqrt(33))/16 - 1/r),3)))
print()

print("2. two factors, BOTH at a=1, n_1 n_2 and the ratio free: a one-parameter family")
print("   matching I_2 AND I_4 exactly.  P = Lambda/2, s = 1/r^2 = (7-16P^2)/(16P^2(1+8P^2)),")
print("   p = -(1+8P^2)/(8P(s-1)),  q = P-p,  n_1 = p sqrt(s), beta_1 = 1/sqrt(s), n_2 = q, beta_2 = 1.")
def member(P):
    s = (7-16*P**2)/(16*P**2*(1+8*P**2))
    p = -(1+8*P**2)/(8*P*(s-1)); qq = P-p
    r = 1/mp.sqrt(s)
    return [(p/r, one, r), (qq, one, one)], s, r
print("   %-9s %-12s %-12s %-12s %-14s %-14s %-14s" % ("P","s","n_1","beta_1","I_2-tgt","I_4-tgt","I_6-tgt"))
for Pv in ['0.5','0.25','0.6','0.1','0.3','0.45','0.65']:
    P = mp.mpf(Pv)
    if 16*P**2 >= 7:
        print("   P=%-7s  s<0: outside the family" % Pv); continue
    f,s,r = member(P); lam,I = inv(f)
    print("   %-9s %-12s %-12s %-12s %-14s %-14s %-14s"
          % (Pv, mp.nstr(s,7), mp.nstr(f[0][0],7), mp.nstr(f[0][2],7),
             mp.nstr(I[0]-TG[0],4), mp.nstr(I[1]-TG[1],4), mp.nstr(I[2]-TG[2],4)))
print()
print("3. where does I_6 also vanish on the family?  root-find on P in (0, sqrt7/4=%s)"
      % mp.nstr(mp.sqrt(7)/4,8))
def f6(P):
    f,s,r = member(P); lam,I = inv(f); return I[2]-TG[2]
xs = [mp.mpf(k)/400 for k in range(4, 265)]
prev = None
roots = []
for x in xs:
    try: v = f6(x)
    except Exception: continue
    if prev is not None and mp.sign(v) != mp.sign(prev[1]):
        try:
            rt = mp.findroot(f6, (prev[0], x), solver='bisect', tol=mp.mpf('1e-40'))
            roots.append(rt)
        except Exception: pass
    prev = (x, v)
for rt in roots:
    f,s,r = member(rt); lam,I = inv(f)
    print("   P = %-14s  s = %-14s  n_1 = %-10s beta_1 = %-10s  max|I_2m-tgt|, m<=4 : %s"
          % (mp.nstr(rt,12), mp.nstr(s,12), mp.nstr(f[0][0],8), mp.nstr(f[0][2],8),
             mp.nstr(max(abs(I[k]-TG[k]) for k in range(4)),3)))
print("   (s=1/4 and s=4 are the two Legendre-duplication points; nothing else.)")
print()
print("4. the two survivors ARE Legendre duplication, identically:")
print("   Gamma(2z) = 2^{2z-1} pi^{-1/2} Gamma(z)Gamma(z+1/2)  with 2z = 1+2i tau gives")
print("   [Gamma(1+2i tau)/Gamma(1+i tau)]^{1/2} = 2^{i tau} pi^{-1/4} Gamma(1/2+i tau)^{1/2},")
print("   i.e. (n=1/2,a=1,b=2)+(n=-1/2,a=1,b=1) == (n=1/2,a=1/2,b=1) up to a linear phase;")
for tt in ['1.3','7.0']:
    t = mp.mpf(tt)
    lhs = mp.sqrt(mp.gamma(1+2j*t)/mp.gamma(1+1j*t))
    rhs = 2**(1j*t)*mp.pi**mp.mpf('-0.25')*mp.sqrt(mp.gamma(mp.mpf(1)/2+1j*t))
    print("      tau=%-5s |lhs-rhs| = %s" % (tt, mp.nstr(abs(lhs-rhs),3)))
