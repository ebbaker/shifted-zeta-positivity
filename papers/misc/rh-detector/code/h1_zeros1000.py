"""h1_zeros1000.py -- cache the first 1001 nontrivial zeta zero ordinates.

Output: zeros1001.json, ordinates gamma_1..gamma_1001 as 25-digit strings
(computed at 30 dps).  Runtime ~ a few minutes.
"""
import json, time
from mpmath import mp, zetazero

mp.dps = 30
K = 1001
t0 = time.time()
zs = []
for n in range(1, K + 1):
    zs.append(mp.nstr(zetazero(n).imag, 25))
    if n % 100 == 0:
        print(n, zs[-1], round(time.time() - t0, 1), "s", flush=True)

with open("zeros1001.json", "w") as f:
    json.dump(zs, f)
print("done", round(time.time() - t0, 1), "s")
