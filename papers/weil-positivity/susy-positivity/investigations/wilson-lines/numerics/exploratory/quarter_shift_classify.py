# UNREGISTERED exploratory programme (requires mpmath). Claude Opus 5, 17 Sep 2026.
"""Single-factor classification and the two-factor family at a common shift a=1."""
import mpmath as mp
mp.mp.dps = 50
B = lambda n,a: mp.bernpoly(n,a)
q = mp.mpf(1)/4

def inv(factors, M=4):
    lam = 2*mp.fsum(n*b for n,a,b in factors)
    return lam, [lam**(2*m-1)*mp.fsum(n*B(2*m,a)/b**(2*m-1) for n,a,b in factors) for m in range(1,M+1)]

TG = [mp.mpf(2)**(2*m-1)*B(2*m,q) for m in range(1,5)]
print("targets  I_2=%s  I_4=%s  I_6=%s  I_8=%s" % tuple(mp.nstr(x,14) for x in TG))
print("exact:   -1/24=%s  7/480=%s  -31/2688=%s"
      % (mp.nstr(-mp.mpf(1)/24,14), mp.nstr(mp.mpf(7)/480,14), mp.nstr(-mp.mpf(31)/2688,14)))
print()

print("A. SINGLE FACTOR:  I_2m = 2^{2m-1} n^{2m} B_2m(a), independent of b.")
for (n,a,b) in [(1,q,mp.mpf(1)/2),(1,q,mp.mpf(3)),(1,q,mp.mpf('0.137'))]:
    lam,I = inv([(mp.mpf(n),a,b)])
    print("   (n=%s,a=1/4,b=%s)  Lambda=%s  I_2=%s I_4=%s I_6=%s"
          % (n, mp.nstr(b,5), mp.nstr(lam,6), mp.nstr(I[0],12), mp.nstr(I[1],12), mp.nstr(I[2],12)))
for (n,a,b) in [(1,q,mp.mpf(1)/2),(-1,q,mp.mpf(1)/2),(1,3*q,mp.mpf(1)/2),
                (mp.mpf(1)/2,mp.mpf(1)/2,mp.mpf(1)),(-mp.mpf(1)/2,mp.mpf(1)/2,mp.mpf(1))]:
    lam,I = inv([(mp.mpf(n),a,b)])
    d = max(abs(I[k]-TG[k]) for k in range(4))
    print("   claimed solution n=%-5s a=%-5s  max|I-target| over m=1..4 : %s"
          % (mp.nstr(mp.mpf(n),4), mp.nstr(a,4), mp.nstr(d,3)))
print()
print("   the classification: n^2 B_2(a) = -1/48 and n^4 B_4(a) = 7/3840")
print("   with u=B_2(a): B_4(a)=u^2-u/3-1/180, giving 576u^2+60u+1=0, u=-1/48 or -1/12")
for u,lab in [(-mp.mpf(1)/48,'u=-1/48'),(-mp.mpf(1)/12,'u=-1/12')]:
    t = -1/(48*u)                       # = n^2
    disc = 1-4*(mp.mpf(1)/6-u)
    print("      %s : n^2=%s  a=(1+-sqrt(%s))/2 = %s , %s ; check B_4 eq: %s"
          % (lab, mp.nstr(t,6), mp.nstr(disc,6), mp.nstr((1+mp.sqrt(disc))/2,8),
             mp.nstr((1-mp.sqrt(disc))/2,8),
             mp.nstr(abs(t*t*((u-mp.mpf(1)/6)**2-mp.mpf(1)/30) - mp.mpf(7)/3840),3)))
print("   a>=1 impossible: B_2(a)>=1/6>0 there, and I_2 = 2 n^2 B_2(a) has the sign of B_2(a).")
