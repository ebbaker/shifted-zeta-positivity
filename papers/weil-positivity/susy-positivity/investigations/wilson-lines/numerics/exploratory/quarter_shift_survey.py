# UNREGISTERED exploratory programme (requires mpmath). Claude Opus 5, 17 Sep 2026.
"""Survey of reflection amplitudes by the dictionary-free invariants."""
import mpmath as mp
mp.mp.dps = 40
B = lambda n,a: mp.bernpoly(n, a)
q = mp.mpf(1)/4; h = mp.mpf(1)/2

def inv(factors, M=3):
    lam = 2*mp.fsum(n*b for n,a,b in factors)
    return lam, [lam**(2*m-1)*mp.fsum(n*B(2*m,a)/b**(2*m-1) for n,a,b in factors) for m in range(1,M+1)]

TG = [mp.mpf(2)**(2*m-1)*B(2*m,q) for m in range(1,4)]
print("target   I_2=%s  I_4=%s  I_6=%s" % tuple(mp.nstr(x,12) for x in TG))
print()
print("0.  the exact degeneracy:  B_{2m}(1/2) = 2^{2m} B_{2m}(1/4)   (multiplication theorem)")
for m in range(1,6):
    print("    m=%d  B_%d(1/2)=%s   2^%d B_%d(1/4)=%s   diff=%s"
          % (m,2*m,mp.nstr(B(2*m,h),12),2*m,2*m,mp.nstr(2**(2*m)*B(2*m,q),12),
             mp.nstr(abs(B(2*m,h)-2**(2*m)*B(2*m,q)),3)))
print("    => (a=1/4, b, n) and (a=1/2, 2b, n/2) have identical Lambda and all Sigma_2m.")
print()

rows = []
def add(name, f):
    lam, I = inv(f)
    ok = all(abs(I[k]-TG[k]) < mp.mpf('1e-25') for k in range(3))
    rows.append((name, lam, I, ok))

add("TARGET  Gamma_R(s)            a=1/4 b=1/2 n=1",        [(1,q,h)])
add("        Gamma_R(s+1) odd      a=3/4 b=1/2 n=1",        [(1,3*q,h)])
add("inv.osc. half-line, even      a=1/4 b=1/2 n=-1",       [(-1,q,h)])
add("inv.osc. half-line, odd       a=3/4 b=1/2 n=-1",       [(-1,3*q,h)])
add("inv.osc. FULL line            a=1/2 b=1  n=-1",        [(-1,h,mp.mpf(1))])
add("c=1 matrix model (MPR sqrt)   a=1/2 b=1  n=-1/2",      [(-h,h,mp.mpf(1))])
add("modular surface, Gamma part   a=1/2 b=1/2 n=1",        [(1,h,h)])
add("JT / Liouville-QM wall        a=1   b=2  n=1",         [(1,mp.mpf(1),mp.mpf(2))])
add("H_3^+ (m-basis), any level    a=1   b=2/t n=-1",       [(-1,mp.mpf(1),mp.mpf(2)/3)])
for bb in ['1.0','0.7']:
    b=mp.mpf(bb); Q=b+1/b
    add("Liouville bulk  b=%s" % bb,  [(1,mp.mpf(1),2*b),(1,mp.mpf(1),2/b)])
    add("FZZT boundary   b=%s" % bb,  [(h,mp.mpf(1),2*b),(h,mp.mpf(1),2/b)])
add("Gauss duplication of target   a=1/8,5/8 b=1/4",        [(1,mp.mpf(1)/8,q),(1,mp.mpf(5)/8,q)])

print("%-46s %10s %14s %14s %14s  %s" % ("amplitude","Lambda","I_2","I_4","I_6","match"))
for name, lam, I, ok in rows:
    print("%-46s %10s %14s %14s %14s  %s"
          % (name, mp.nstr(lam,5), mp.nstr(I[0],8), mp.nstr(I[1],8), mp.nstr(I[2],8),
             "ALL THREE" if ok else ""))

print()
print("1.  the modular surface, from scratch.  NOTE the completion: the Eisenstein")
print("    scattering matrix is Lam(2s-1)/Lam(2s) with Lam(u) = pi^{-u/2} Gamma(u/2) zeta(u),")
print("    NOT xi(2s-1)/xi(2s) for the manuscript's xi(u) = u(u-1)/2 Lam(u).  They differ by")
print("    (2s-2)/(2s), unimodular, whose delay is -2/tau^2 -- enough to move I_2 to +11/6.")
Lam = lambda u: mp.pi**(-u/2)*mp.gamma(u/2)*mp.zeta(u)
xi  = lambda u: u*(u-1)/2*Lam(u)
iwa = lambda s: mp.sqrt(mp.pi)*mp.gamma(s-h)*mp.zeta(2*s-1)/(mp.gamma(s)*mp.zeta(2*s))
for r in ['2.4','9.1','40']:
    r = mp.mpf(r); s = h + 1j*r
    print("    r=%5s  |phi|=%s  |phi - Lam-ratio|=%s  |phi - xi-ratio|=%s  |phi - (s/(s-1)) xi-ratio|=%s"
          % (mp.nstr(r,5), mp.nstr(abs(iwa(s)),10), mp.nstr(abs(iwa(s)-Lam(2*s-1)/Lam(2*s)),3),
             mp.nstr(abs(iwa(s)-xi(2*s-1)/xi(2*s)),3),
             mp.nstr(abs(iwa(s)-(s/(s-1))*xi(2*s-1)/xi(2*s)),3)))
    print("           arg phi + 2 arg Lam(1+2ir) mod 2pi = %s"
          % mp.nstr(abs(mp.arg(iwa(s)) + 2*mp.arg(Lam(1+2j*r))) % (2*mp.pi), 3))
print("    the ARCHIMEDEAN part of the delay in tau = 2r is -log(tau/2pi) + 1/(6 tau^2):")
for t in ['60','200','800']:
    t = mp.mpf(t); r = t/2
    arch = -(mp.re(mp.digamma(h+1j*r)) - mp.log(mp.pi))
    print("      tau=%5s   tau^2 (arch + log(tau/2pi)) = %s    +1/6 = %s   (I_2 = Lambda Sigma_2 = (-1)(1/6) = -1/6)"
          % (mp.nstr(t,4), mp.nstr((arch + mp.log(t/(2*mp.pi)))*t*t, 10), mp.nstr(mp.mpf(1)/6,10)))
print("    the ARITHMETIC part 2 Re (zeta'/zeta)(1+i tau) does NOT decay -- it is")
print("    -2 sum_n Lambda(n) n^{-1} cos(tau log n), mean zero and oscillatory:")
for t in ['100','1000','10000']:
    t = mp.mpf(t)
    v = 2*mp.diff(lambda x: mp.arg(mp.zeta(1+1j*x)), t)
    print("      tau=%7s   2 d/dtau arg zeta(1+i tau) = %-16s   tau^-4 = %s"
          % (mp.nstr(t,6), mp.nstr(v,10), mp.nstr(t**-4,3)))
print("    so the displayed expansion is of the archimedean factor alone; the zeros,")
print("    which are the poles of phi at s = rho/2, are OFF the line and enter it not at all.")

print()
print("2.  the cigar: shifts 1/2 + (|n| -+ k w)/2 are tunable; can it hit I_2 and then I_4?")
def cigar(k, nn, w):
    t = k-2
    return [(-1,mp.mpf(1),2/t), (-1,mp.mpf(1),mp.mpf(2)),
            (1, h+(abs(nn)-k*w)/2, mp.mpf(1)), (1, h+(abs(nn)+k*w)/2, mp.mpf(1))]
for (k,nn,w) in [(mp.mpf(14)/3,1,0), (mp.mpf(782)/3,7,0), (mp.mpf(5),0,0), (mp.mpf(3),0,0)]:
    lam, I = inv(cigar(k,nn,w))
    print("    k=%-8s n=%d w=%d   Lambda=%-10s I_2=%-14s I_4=%-14s (target %s, %s)"
          % (mp.nstr(k,6), nn, w, mp.nstr(lam,6), mp.nstr(I[0],8), mp.nstr(I[1],8),
             mp.nstr(TG[0],6), mp.nstr(TG[1],6)))
