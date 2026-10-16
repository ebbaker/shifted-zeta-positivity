"""Check 2: zero sums. S4 = sum over all rho of (Im rho)^-4; A,B direct vs closed form;
A* and the new threshold bound; tail beyond zero #N via Riemann-von Mangoldt density."""
import mpmath as mp
mp.mp.dps = 25

N = 120
gam = [mp.im(mp.zetazero(n)) for n in range(1, N+1)]   # positive ordinates
print("first/last ordinate:", mp.nstr(gam[0],10), mp.nstr(gam[-1],10))

def dens(t):  # dN/dt ~ (1/2pi) log(t/2pi)
    return mp.log(t/(2*mp.pi))/(2*mp.pi)

T = gam[-1]
# S4 over all zeros (both signs of ordinate): 2*sum tau^-4  + tail
S4_head = 2*mp.fsum(g**-4 for g in gam)
S4_tail = 2*mp.quad(lambda t: dens(t)*t**-4, [T, mp.inf])
print("S4 head:", mp.nstr(S4_head,8), " tail:", mp.nstr(S4_tail,4), " total ~", mp.nstr(S4_head+S4_tail,8))

# S2 = 2*sum tau^-2 (for A* under RH etc.), and check B(0)=S2? B(0)=sum gamma^-2 (all) = 2 sum_{tau>0} tau^-2
S2_head = 2*mp.fsum(g**-2 for g in gam)
S2_tail = 2*mp.quad(lambda t: dens(t)*t**-2, [T, mp.inf])
print("S2 head+tail:", mp.nstr(S2_head+S2_tail,8), " vs B(0)=0.04620999")

def xilog(s):
    return 1/s + 1/(s-1) - mp.log(mp.pi)/2 + mp.digamma(s/2)/2 + mp.zeta(s, derivative=1)/mp.zeta(s)
def xilogp(s):
    return mp.diff(xilog, s)

# A,B direct sums (RH zeros real) vs closed forms; and paper's Table tab:AB with 250-zero style tail
print("\nw | A direct+tail | A closed | B direct+tail | B closed")
for w in ['0.10','0.25','0.40']:
    w_ = mp.mpf(w)
    A_h = 2*mp.fsum(1/(g**2+w_**2) for g in gam) + 2*mp.quad(lambda t: dens(t)/(t**2+w_**2), [T, mp.inf])
    B_h = 2*mp.fsum((g**2-w_**2)/(g**2+w_**2)**2 for g in gam) + 2*mp.quad(lambda t: dens(t)*(t**2-w_**2)/(t**2+w_**2)**2, [T, mp.inf])
    A_c = xilog(mp.mpf('0.5')+w_)/w_
    B_c = xilogp(mp.mpf('0.5')+w_)
    print(w, mp.nstr(A_h,8), mp.nstr(A_c,8), mp.nstr(B_h,8), mp.nstr(B_c,8),
          " relA:", mp.nstr((A_h-A_c)/A_c,3), " relB:", mp.nstr((B_h-B_c)/B_c,3))

# New threshold: t0 <= (A*-B)/(wA) <= 8 w^2 S4 / (xi'/xi)(1/2+w)
S4 = S4_head + S4_tail
print("\nNew threshold bound t0(w) <= 8 w^2 S4 / (xi'/xi)(.5+w):")
for w in ['0.001','0.01','0.05','0.1','0.2','0.3','0.4','0.49','0.4999']:
    w_ = mp.mpf(w)
    sl = xilog(mp.mpf('0.5')+w_)
    t0 = 8*w_**2*S4/sl
    print(w, " t0 <=", mp.nstr(t0,6), "  t0/w =", mp.nstr(t0/w_,6))

# RH-case exact (A*-B)/(wA) = (A-B)/(wA) = (1-r)/w
print("\nRH case t0 = (1-r)/w:")
for w in ['0.1','0.3','0.49']:
    w_ = mp.mpf(w)
    sl = xilog(mp.mpf('0.5')+w_); B = xilogp(mp.mpf('0.5')+w_)
    r = w_*B/sl
    print(w, mp.nstr((1-r)/w_, 6))

# check (xi'/xi)(1/2+w)/w minimum on (0,1/2]
ws = [mp.mpf(k)/1000 for k in range(1,501,10)]
vals = [xilog(mp.mpf('0.5')+w)/w for w in ws]
print("\nmin slope/w on grid:", mp.nstr(min(vals),9), " at w=", mp.nstr(ws[vals.index(min(vals))],4))
print("monotone decreasing?", all(vals[i]>vals[i+1] for i in range(len(vals)-1)))
