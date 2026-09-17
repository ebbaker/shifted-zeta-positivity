import mpmath as mp, json, sys, time
T = mp.mpf(sys.argv[1]); DPS = int(sys.argv[2])
mp.mp.dps = 30
seed = []; n = -1
t0 = time.time()
while True:
    g = mp.grampoint(n)
    if g > T: break
    seed.append(g); n += 1
print("seeds: %d  [%.0fs]" % (len(seed), time.time()-t0)); sys.stdout.flush()
def th(t):  return mp.siegeltheta(t)
def dth(t): return mp.re(mp.digamma(mp.mpf(1)/4 + 1j*t/2))/2 - mp.log(mp.pi)/2
out = []
for i, g0 in enumerate(seed):
    tgt = (i-1)*mp.pi
    g = g0
    for dps in (60, 120, DPS):
        mp.mp.dps = dps + 10
        g = +g
        for _ in range(3):
            g = g - (th(g)-tgt)/dth(g)
    mp.mp.dps = DPS
    out.append(mp.nstr(+g, DPS-3))
json.dump(out, open('gramT%d_d%d.json' % (int(T), DPS), 'w'))
print("cached %d to T=%s dps=%d [%.0fs]" % (len(out), mp.nstr(T,6), DPS, time.time()-t0))
