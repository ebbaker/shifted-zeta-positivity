"""
Re-examination of the four qualifications raised in response_claude_20260914.md.
Reuses the chk3 cosine-basis assembly (independent of the paper's scripts).
"""
import numpy as np, json
src=open('chk3_operator_and_schur.py').read(); s=src.index('def assemble'); e=src.index('def active_powers'); ns={}
exec("import numpy as np, mpmath as mp\nfrom scipy.special import digamma\nmp.mp.dps=30\npsi14=float(mp.digamma(0.25)); w0=psi14-np.log(np.pi)\ndef a_k(k): return 2*k+0.5\n"+src[s:e], ns)
assemble=ns['assemble']
out={}

# ---------- (2) inertia vs eigenvalues: lambda_min(W_K) vs lambda_min(U_K) ----------
L=1.0; N=4; beta=5.904503101954
print("L=1: compression lambda_min(W_K)  vs  Schur upper lambda_min(U_K)")
rows=[]
for K in [200, 800, 2000, 4000]:
    M=assemble(L,K,[(2,1)]); W=M['W']
    lamW=np.linalg.eigvalsh(W)[0]
    A=W[:N,:N]; HK=W[N:K,N:K]; BK=W[N:K,:N]
    U=A-BK.T@np.linalg.solve(HK,BK); lamU=np.linalg.eigvalsh((U+U.T)/2)[0]
    rows.append((K,float(lamW),float(lamU),float(lamU/lamW)))
    print(f"  K={K:5d}   lambda_min(W_K)={lamW:.6e}   lambda_min(U_(1,4,K))={lamU:.6e}   ratio={lamU/lamW:.5f}")
out['inertia_vs_eigenvalues']=rows

# ---------- (1) truncated residual Gram is not a lower enclosure ----------
# reproduce the response's exact counterexample
A0=np.zeros((1,1)); H0=np.eye(2); B0=np.array([[0.],[1.]]); Y0=np.zeros((2,1))
R0=B0-H0@Y0
exact=float((A0-B0.T@np.linalg.solve(H0,B0))[0,0])
row0_only=float((A0-B0.T@Y0-(R0[0:1,:].T@R0[0:1,:]))[0,0])
full=float((A0-B0.T@Y0-(R0.T@R0))[0,0])
print(f"\nResponse counterexample: exact Schur={exact}, row-0-only 'lower'={row0_only}, full Gram lower={full}")
out['truncated_gram_counterexample']=dict(exact=exact, row0_only=row0_only, full=full,
    verdict="row-0-only value 0 exceeds the exact Schur value -1; truncated Gram is not a lower bound")

# ---------- (5) zero-side sampling vs continuous out-of-band mass ----------
zeros=np.array([float(z) for z in json.load(open('zeros_300.json'))]); g1=zeros[0]
from scipy import integrate
K=400; M=assemble(L,K,[(2,1)]); W=M['W']; nu=M['nu']; om=M['om']
ev,V=np.linalg.eigh(W)
def Fhat(c,t):
    t=np.atleast_1d(t)[:,None]
    def E(al): return L*np.exp(1j*al*L/2)*np.sinc(al*L/(2*np.pi))
    return ((c*nu)[None,:]*(E(om[None,:]-t)+E(-om[None,:]-t))/2).sum(1)
c=V[:,0]
zero_sum=float(2*np.sum(np.abs(Fhat(c,zeros))**2))
out_of_band=2*integrate.quad(lambda t: abs(Fhat(c,t)[0])**2, g1, 200, limit=600)[0]/(2*np.pi)
out_of_band+=2*integrate.quad(lambda t: abs(Fhat(c,t)[0])**2, 200, np.inf, limit=600)[0]/(2*np.pi)
in_band=2*integrate.quad(lambda t: abs(Fhat(c,t)[0])**2, 0, g1, limit=600)[0]/(2*np.pi)
print(f"\nNear-null eigenvector at L=1 (eigenvalue {ev[0]:.6e}):")
print(f"  zero-side sum  2*sum_gamma |Fhat|^2 (300 zeros) = {zero_sum:.6e}")
print(f"  continuous OUT-OF-BAND mass  (1/2pi)int_{{|t|>g1}}|Fhat|^2 = {out_of_band:.6e}")
print(f"  continuous IN-BAND mass                                   = {in_band:.6e}")
print(f"  ratio zero_sum / out_of_band = {zero_sum/out_of_band:.4f}   <-- NOT ~1: the two quantities differ by a large factor")
out['sampling_vs_mass']=dict(eigenvalue=float(ev[0]), zero_sum=zero_sum, out_of_band=float(out_of_band),
    in_band=float(in_band), ratio=float(zero_sum/out_of_band))
json.dump(out, open('recheck.json','w'), indent=1)
