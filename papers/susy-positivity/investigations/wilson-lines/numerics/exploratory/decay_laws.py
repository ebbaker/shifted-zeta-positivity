import math
# converged true values (program units: f supported in (-L/2, L/2))
T = {0.6:-2.110692136, 0.8:-3.72642152254, 1.0:-6.00789844279, 1.2:-8.76388092477,
     1.4:-12.3472871991, 1.6:-16.7535864074, 1.8:-22.3527238503, 2.0:-29.167851883,
     2.2:-37.622775153, 2.4:-48.0423794919, 2.6:-60.9741780119, 2.8:-76.7471627877,
     3.0:-96.2463231944}
LN10 = math.log(10)
print(" L    -ln lam    D=2e^L-7/4   Nyq=2Le^L   u=1-D/Nyq |  /D     /Nyq    Zhu     G=ratio/pi")
for L in sorted(T):
    y = -T[L]*LN10
    D = 2*math.exp(L) - 1.75
    nyq = 2*L*math.exp(L)
    u = 1 - D/nyq
    tc = 2*math.pi*math.exp(L)
    NT = tc/(2*math.pi)*math.log(tc/(2*math.pi*math.e)) + 0.875   # N(tau_c)
    zhu = y/(NT/math.log(NT)) if NT > 1.2 else float('nan')
    print("%4.1f %10.3f %10.3f %11.3f %9.3f | %6.3f %6.3f %7.2f %8.4f"
          % (L, y, D, nyq, u, y/D, y/nyq, zhu, y/(math.pi*nyq)))

print("\nleast-squares over L in [1.4, 3.0], model -ln lam = a * X(L):")
Ls = [L for L in sorted(T) if L >= 1.4]
def fit(name, X):
    xs = [X(L) for L in Ls]; ys = [-T[L]*LN10 for L in Ls]
    a = sum(x*y for x,y in zip(xs,ys))/sum(x*x for x in xs)
    r = [abs(a*x-y)/y for x,y in zip(xs,ys)]
    print("  %-34s a=%9.4f   max rel resid = %5.1f%%" % (name, a, 100*max(r)))
fit("D(L) = 2e^L - 7/4", lambda L: 2*math.exp(L)-1.75)
fit("Nyq(L) = 2 L e^L", lambda L: 2*L*math.exp(L))
fit("Nyq/ln Nyq", lambda L: 2*L*math.exp(L)/math.log(2*L*math.exp(L)))
fit("N(tau_c)/ln N(tau_c)  [Zhu]", lambda L: (math.exp(L)*(L-1)+0.875)/math.log(math.exp(L)*(L-1)+0.875))
fit("D/ln(2 Nyq/D)  [Kulikov order]", lambda L: (2*math.exp(L)-1.75)/math.log(2*2*L*math.exp(L)/(2*math.exp(L)-1.75)))
fit("Nyq * (1 - 0.75 u)", lambda L: 2*L*math.exp(L)*(1-0.75*(1-(2*math.exp(L)-1.75)/(2*L*math.exp(L)))))
