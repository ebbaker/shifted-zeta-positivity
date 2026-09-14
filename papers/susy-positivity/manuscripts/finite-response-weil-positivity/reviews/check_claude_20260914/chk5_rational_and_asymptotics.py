"""
Check 5: exact rational checks (Sections 12-13 of the companion) and the elementary
tail/asymptotic constants, implemented independently.
"""
from fractions import Fraction as Fr
import mpmath as mp, json
mp.mp.dps = 40
out = {}

# ---- Section 13: beta_1 bound and the 64-term sum ---------------------------------
beta1_bound = Fr(58,100) + Fr(11,7) + Fr(21,10) + Fr(23,20) + Fr(43,1000) + Fr(1,2)
assert beta1_bound == Fr(41611, 7000)
S64 = sum(Fr(2, 1)/(2*k+Fr(1,2)) * Fr(144,1)/((2*k+Fr(1,2))**2 + 144) for k in range(64))
assert S64 > Fr(3007, 500)
margin = Fr(3007,500) - (Fr(41611,7000) + Fr(1,16))
assert margin == Fr(99, 14000)
out['sec13'] = dict(beta1_bound=str(beta1_bound), S64=float(S64), S64_gt_3007_500=S64 > Fr(3007,500), margin=str(margin))
print("Sec 13: beta_1 < 41611/7000 =", float(beta1_bound), "; 64-term sum =", float(S64), "> 3007/500; margin =", margin)
# actual values
gamma, pi, l2, lpi = mp.euler, mp.pi, mp.log(2), mp.log(mp.pi)
beta1 = gamma + pi/2 + 3*l2 + lpi + 2*mp.sinh(mp.mpf(1)/2) - 1 + l2/mp.sqrt(2)
psi14 = mp.digamma(mp.mpf(1)/4)
b = lambda s: mp.re(mp.digamma(mp.mpf(1)/4 + 1j*mp.sqrt(s)/2)) - psi14
print("   actual beta_1 =", mp.nstr(beta1, 12), "; b_3 =", mp.nstr(b((3*pi)**2), 8), "; b_4 =", mp.nstr(b((4*pi)**2), 8),
      "; b(144) =", mp.nstr(b(144), 8), "; beta_1 + 1/16 =", mp.nstr(beta1 + mp.mpf(1)/16, 8))
assert b((3*pi)**2) < beta1 + mp.mpf(1)/16 < b((4*pi)**2)
out['sec13']['N_min_1_is_4'] = True
# auxiliary rational inequalities used
checks = {
 'gamma<0.58': gamma < mp.mpf('0.58'), 'pi<22/7': pi < mp.mpf(22)/7, 'log2<0.7': l2 < mp.mpf('0.7'),
 'logpi<23/20': lpi < mp.mpf(23)/20, '2sinh(1/2)-1<43/1000': 2*mp.sinh(mp.mpf(1)/2)-1 < mp.mpf(43)/1000,
 'log2/sqrt2<1/2': l2/mp.sqrt(2) < mp.mpf(1)/2,
 'H256-log256<0.58 using log2>6931/10000': sum(Fr(1,k) for k in range(1,257)) - 8*Fr(6931,10000) < Fr(58,100),
 '22/7-pi = int x^4(1-x)^4/(1+x^2)': abs(mp.quad(lambda x: x**4*(1-x)**4/(1+x*x), [0,1]) - (mp.mpf(22)/7 - pi)) < mp.mpf(10)**-30,
}
print("   auxiliary:", checks); assert all(checks.values()); out['sec13']['aux'] = {k: bool(v) for k, v in checks.items()}

# ---- Section 12: density control -------------------------------------------------
c = Fr(2,1)/Fr(5,2)**3 + Fr(1,1)/(2*Fr(5,2)**2)
assert c == Fr(26,125)
val = -1 + Fr(26,125)*Fr(22,7)**2/4
assert val == Fr(-2979, 6125)
actual_sum = mp.nsum(lambda k: 2/(2*k+mp.mpf(1)/2)**3, [1, mp.inf])
assert actual_sum < mp.mpf(26)/125
H8 = sum(Fr(1,k) for k in range(1,9)); assert H8 - Fr(11,5) == Fr(29,56) and Fr(29,56) > Fr(1,2)
from math import factorial
six = sum(Fr(11,10)**n / factorial(n) for n in range(6))
assert six > 3
w0 = psi14 - lpi
assert w0 < -5
print("Sec 12: sum_{k>=1} 2/a_k^3 =", mp.nstr(actual_sum, 10), "< 26/125 =", float(Fr(26,125)), "; bound value =", val, "=", float(val))
print("   H_8 - 11/5 =", H8 - Fr(11,5), "; six-term e^{1.1} partial sum =", float(six), "> 3 ;  w0 =", mp.nstr(w0, 10), "< -5")
# actual value of Q_2^dens on the sine input, with exact t_{>=1}
L = mp.mpf(2)
t_ge1 = mp.nsum(lambda k: (2/(2*k+mp.mpf(1)/2))*mp.quad(lambda t: (t*t/((2*k+mp.mpf(1)/2)**2+t*t))*abs((mp.pi/L)*(1+mp.e**(-1j*t*L))/((mp.pi/L)**2-t*t))**2 if abs(t-mp.pi/L)>mp.mpf('1e-12') else 0, [0, mp.pi/L, 10, 100, mp.inf])/mp.pi, [1, 40]) \
        if False else None
out['sec12'] = dict(sum_2_over_ak3=mp.nstr(actual_sum, 12), bound=str(val), w0=mp.nstr(w0, 12))

# ---- elementary tail constants -------------------------------------------------------
aJ = lambda J: 2*J + mp.mpf(1)/2
for J in [1, 5, 40]:
    t3 = mp.nsum(lambda k: 2/aJ(k)**3, [J, mp.inf]); assert t3 <= 2/aJ(J)**3 + 1/(2*aJ(J)**2)
    t2 = mp.nsum(lambda k: 1/aJ(k)**2, [J, mp.inf]); assert t2 <= 1/aJ(J)**2 + 1/(2*aJ(J))
    t32 = mp.nsum(lambda k: aJ(k)**(-mp.mpf(3)/2), [J, mp.inf]); assert t32 <= aJ(J)**(-mp.mpf(3)/2) + aJ(J)**(-mp.mpf(1)/2)
print("tail constants (3.2),(6.2),(6.3) hold at J=1,5,40")
out['tail_constants'] = 'ok'

# ---- gamma series identity and asymptotic ------------------------------------------
for s in [mp.mpf('0.3'), 7, 144, 10**4]:
    ser = mp.nsum(lambda k: (2/aJ(k))*s/(aJ(k)**2+s), [0, mp.inf])
    assert abs(ser - b(s)) < mp.mpf(10)**-25
asym = [(t, mp.nstr((b(t*t) - (mp.log(t) - mp.log(2) - psi14))*t*t, 8)) for t in [10, 100, 1000, 10**4]]
print("gamma series = Re psi identity OK;  tau^2 * [b(tau^2) - (log tau - log 2 - psi(1/4))] ->", asym, " (should tend to a constant: -1/2 + ... )")
out['asymptotic_tau2_times_remainder'] = asym
# w0 closed form
assert abs(w0 - (-mp.euler - mp.pi/2 - 3*mp.log(2) - mp.log(mp.pi))) < mp.mpf(10)**-35
# psi(1/2)-psi(1/4) identity for the contact integral
I = mp.quad(lambda r: (1-mp.e**(-r/2))*mp.e**(-r/2)/(1-mp.e**(-2*r)), [0, 1, mp.inf])
assert abs(I - (mp.digamma(mp.mpf(1)/2) - psi14)/2) < mp.mpf(10)**-30
print("contact integral = (psi(1/2)-psi(1/4))/2 OK; w0 closed form OK")

# ---- remainder kernel bound in D 5.1 ---------------------------------------------------
n = lambda t: mp.e**(-t/2)/(1-mp.e**(-2*t))
for L in [mp.mpf('0.5'), mp.mpf(1), mp.mpf(3)]:
    bound = 2*(n(2*L)+n(L))/(1-mp.e**(-L))
    worst = 0
    for x in mp.linspace(0, L, 7):
        for y in mp.linspace(0, L, 7):
            rem = sum(n(x+y+2*m*L) + n((2*m+2)*L-x-y) for m in range(1, 60)) + sum(n((2*m+2)*L+x-y) + n((2*m+2)*L-x+y) for m in range(0, 60))
            worst = max(worst, rem/bound)
    print(f"L={L}: max (non-leading image kernel)/(stated bound) = {mp.nstr(worst,4)}  (<=1 required)")
    assert worst <= 1
    # n(t) - 1/(2t) bounded on (0,2L]
    m = max(abs(n(t) - 1/(2*t)) for t in mp.linspace(mp.mpf('1e-6'), 2*L, 200))
    print(f"      max |n(t)-1/(2t)| on (0,2L] = {mp.nstr(m,4)}")
out['remainder_kernel_bound'] = 'ok'
json.dump(out, open('chk5.json', 'w'), indent=1, default=str)
