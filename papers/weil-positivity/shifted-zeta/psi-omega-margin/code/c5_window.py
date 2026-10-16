"""Check 5: unconditional positivity window.
Psi_w(t) >= wA t + B - A e^{-wt} - S e^{(1/2-w)t},  S = sum over zeros with |tau|>Tv of tau^-2,
Tv = 3e12 (Platt-Trudgian). Find the window (t_lo, t_hi) where RHS > 0, per omega."""
import mpmath as mp
mp.mp.dps = 25

def xilog(s):
    return 1/s + 1/(s-1) - mp.log(mp.pi)/2 + mp.digamma(s/2)/2 + mp.zeta(s, derivative=1)/mp.zeta(s)
def xilogp(s):
    return mp.diff(xilog, s)

Tv = mp.mpf('3e12')
# S = 2 * int_{Tv}^inf (1/2pi) log(t/2pi) t^-2 dt  (RvM density; explicit-N(T) correction ~ 0.11logT/T^2 negligible)
S = 2*mp.quad(lambda t: mp.log(t/(2*mp.pi))/(2*mp.pi)/t**2, [Tv, mp.inf])
print("S =", mp.nstr(S,6))

print("\nw | t_lo | t_hi")
for w in ['0.05','0.1','0.15','0.2','0.25','0.3','0.35','0.4','0.45','0.49']:
    w_ = mp.mpf(w)
    A = xilog(mp.mpf('0.5')+w_)/w_; B = xilogp(mp.mpf('0.5')+w_)
    F = lambda t: w_*A*t + B - A*mp.e**(-w_*t) - S*mp.e**((mp.mpf('0.5')-w_)*t)
    # lower root near (1-r)/(2w)
    r = B/A
    t_lo = mp.findroot(F, (1-r)/(2*w_)+mp.mpf('1e-9'))
    # upper root: scan
    t_hi = mp.findroot(F, 26/(mp.mpf('0.5')-w_))
    print(w, mp.nstr(t_lo,4), mp.nstr(t_hi,6), "  e^t_hi ~ 10^%s" % mp.nstr(t_hi/mp.log(10),3))
