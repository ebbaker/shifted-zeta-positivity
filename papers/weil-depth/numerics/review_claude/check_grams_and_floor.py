"""Independent quadrature check of full-output Gram entries F_ij = <U phi_i, U phi_j>
    and C_ij = <U phi_i, R U phi_j> at L=9/5, using the (now validated) output
    formula U phi_n = p_n(u) log u + q_n(u) + sum 2 Lambda(k)/sqrt(k) 1_{u>delta_k} p_n(u-delta_k),
    with g_j from mp.taylor rather than the code's rational recursion.
Convention: the archives store Grams in the unitary coordinate u = x/L with the basis
sqrt(2n+1) p_n(u) and inner product int_0^1 du, so no factor L appears.
(E_r PSD checks, head spectra and the floor sweep are in check_floor.py.)
"""
import os as _os
ARCHIVE_1P8 = _os.environ.get('ARCHIVE_1P8', 'output/length_1p8_N128/central_matrices.json.gz')
ARCHIVE_LOG7 = _os.environ.get('ARCHIVE_LOG7', 'output/log7_N128/central_matrices.json.gz')
import sys, gzip, json, math
import mpmath as mp
sys.path.insert(0, '.')  # run from numerics/
import certify_arb as c

mp.mp.dps = 25
L = mp.mpf(9)/5; N = 128; M = 180
G0 = lambda t: t*mp.exp(t/2)/mp.sinh(t) - 4*t*mp.cosh(t/2) if t != 0 else mp.mpf(1)
g = mp.taylor(G0, 0, M)
ell = mp.euler + mp.log(2*mp.pi*L)
active = [(2,2),(3,3),(4,2),(5,5)]
deltas = [(k, mp.log(k)/L, 2*mp.log(p)/mp.sqrt(k)) for k,p in active]

def legcoef(n):  # coefficients of shifted Legendre p_n(u) = sum_k a_k u^k
    return [(-1)**(n+k)*math.comb(n,k)*math.comb(n+k,k) if k<=n else 0 for k in range(n+1)]

def Uphi(n):
    a = legcoef(n); s = mp.sqrt(2*n+1)
    H = [mp.mpf(0)]
    for k in range(1, n+M+2): H.append(H[-1]+mp.mpf(1)/k)
    def p(u): return sum(a[k]*u**k for k in range(n+1))
    def q(u):
        tot = mp.mpf(0)
        for k in range(n+1):
            if a[k]==0: continue
            tot += a[k]*u**k*(ell-H[k])
            beta = mp.mpf(1)/(k+1)
            for j in range(1, M+1):
                if j>1: beta *= mp.mpf(j-1)/(j+k)
                tot += a[k]*g[j]*beta*L**j*u**(j+k)
        return tot
    def out(u):
        v = p(u)*mp.log(u) + q(u)
        for k, d, coef in deltas:
            if u > d: v += coef*p(u-d)
        return v
    return lambda u: s*out(u)   # normalized basis sqrt(2n+1) p_n(u) in the unitary coordinate

brk = sorted(set([mp.mpf(0), mp.mpf(1)] + [d for _,d,_ in deltas] + [1-d for _,d,_ in deltas]))
def ip(f, h):   # <f, h> in the unitary coordinate: int_0^1 f h du
    return mp.quad(lambda u: f(u)*h(u), brk)

with gzip.open(ARCHIVE_1P8,'rt') as fh:
    data = json.load(fh)
def entry(name,i,j):
    m,e = data['matrices'][name][i][j][0]; return mp.mpf(int(m))*mp.mpf(2)**int(e)

print("Gram entries by direct quadrature vs archived Arb Grams, L=9/5")
Us = {n: Uphi(n) for n in (0,1,2,3,5,8)}
for (i,j) in [(0,0),(1,1),(2,2),(0,2),(1,3),(3,5),(2,8),(5,5)]:
    Fq = ip(Us[i], Us[j])
    Cq = ip(Us[i], lambda u: Us[j](1-u))
    print(f"  F[{i},{j}]: quad {mp.nstr(Fq,14):>20s}  Arb {mp.nstr(entry('Gram_causal',i,j),14):>20s}  diff {mp.nstr(Fq-entry('Gram_causal',i,j),2)}"
          f"   | C[{i},{j}]: quad {mp.nstr(Cq,14):>20s}  Arb {mp.nstr(entry('ReflectedGram_causal',i,j),14):>20s}  diff {mp.nstr(Cq-entry('ReflectedGram_causal',i,j),2)}")

