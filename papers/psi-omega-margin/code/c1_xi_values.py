"""Check 1: xi'/xi values, B(0), r(omega), old u* roots, and the new threshold quantities."""
import mpmath as mp
mp.mp.dps = 30

def xilog(s):
    # (xi'/xi)(s) = 1/s + 1/(s-1) - (1/2)log pi + (1/2)psi(s/2) + zeta'/zeta(s)
    s = mp.mpf(s) if not isinstance(s, mp.mpc) else s
    return 1/s + 1/(s-1) - mp.log(mp.pi)/2 + mp.digamma(s/2)/2 + mp.zeta(s, derivative=1)/mp.zeta(s)

def xilogp(s):  # derivative of xi'/xi
    return mp.diff(xilog, s)

print("B(0) = (xi'/xi)'(1/2) =", mp.nstr(xilogp(mp.mpf('0.5')), 15))
print("(xi'/xi)(1/2)        =", mp.nstr(xilog(mp.mpf('0.5')), 5))

print("\nomega | slope=(xi'/xi)(.5+w) | B(w)=(xi'/xi)'(.5+w) | r(w)=wB/slope | slope/w")
for w in ['0.49','0.4','0.3','0.2','0.1','0.05','0.01','0.001']:
    w_ = mp.mpf(w)
    sl = xilog(mp.mpf('0.5')+w_); B = xilogp(mp.mpf('0.5')+w_)
    r = w_*B/sl
    print(w, mp.nstr(sl,9), mp.nstr(B,9), mp.nstr(r,10), mp.nstr(sl/w_,9))

# near the endpoint: does u* exceed the paper's claimed upper bound 0.3751475?
def ustar(r, c):   # root of u + r = c*e^{-u}
    return mp.findroot(lambda u: u + r - c*mp.exp(-u), 0.3)
for w in ['0.49','0.499','0.4999']:
    w_ = mp.mpf(w)
    sl = xilog(mp.mpf('0.5')+w_); B = xilogp(mp.mpf('0.5')+w_); r = w_*B/sl
    print("w=",w," r=",mp.nstr(r,10)," u*(2e^-u)=", mp.nstr(ustar(r,2),9), " u*(e^-u)=", mp.nstr(ustar(r,1),6))

# limit r -> 1 root
print("root of u+1=2e^-u:", mp.nstr(ustar(1,2),12))

# (xi'/xi)(1) and 2*(xi'/xi)(1) for the endpoint slope/w check
print("(xi'/xi)(1) =", mp.nstr(xilog(mp.mpf(1)),12), " => slope/w at w=1/2:", mp.nstr(xilog(mp.mpf(1))/mp.mpf('0.5'),9))
