#!/usr/bin/env python3
"""Central finite-horizon coercivity with full-output, all-Arb arithmetic.

The only approximation not enclosed during construction is truncating the
analytic profile; its explicit operator-norm remainder is subtracted at the
final Schur test. No empirical rounding allowance or floating-point sign test.
See RESEARCH_REPORT.md for the analytic reduction.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse, gzip, hashlib, json, math, platform, sys, time
import flint
from flint import arb as A, arb_mat as AM, fmpq, ctx


def rat(x):
    x = F(x)
    return A(fmpq(x.numerator, x.denominator))


def pack(x):
    """Dyadic midpoint/radius; reloading may inflate the radius outwards."""
    v = [[str(m), int(e)] for m, e in (x.mid().man_exp(), x.rad().man_exp())]
    y = unpack(v)
    assert y.contains(x)
    return v


def unpack(v):
    return A((int(v[0][0]), v[0][1]), (int(v[1][0]), v[1][1]))


def show(x):
    return x.str(35)


def ident(n):
    return AM([[int(i == j) for j in range(n)] for i in range(n)])


def block(x, ids):
    return AM([[x[i, j] for j in ids] for i in ids])


def sym(x):
    assert (x-x.transpose()).contains(AM(x.nrows(), x.ncols()))
    return (x+x.transpose())/2


def profile(M):
    # G(t) = exp(t/2) t/sinh(t) - 4t cosh(t/2), exact rationals.
    den = [F(1, math.factorial(j+1)) if j % 2 == 0 else F(0) for j in range(M+1)]
    inv = [F(1)] + [F(0)]*M
    for n in range(1, M+1):
        inv[n] = -sum((den[k]*inv[n-k] for k in range(1, n+1)), F(0))
    g = [sum((inv[k]*F(1, 2**(n-k)*math.factorial(n-k)) for k in range(n+1)), F(0)) for n in range(M+1)]
    for n in range(1, M+1, 2):
        g[n] -= F(4, 2**(n-1)*math.factorial(n-1))
    assert g[:3] == [F(1), F(-7, 2), F(-1, 24)]
    return g


def prime_powers(L, log_horizon=None):
    if log_horizon:
        cut = log_horizon  # exact integer comparison handles threshold equality
    else:
        cut = 2
        while A(cut).log() < L:
            cut += 1
        assert A(cut).log() > L  # fail closed on an unresolved comparison
    active = []
    for n in range(2, cut):
        p = next(d for d in range(2, n+1) if n % d == 0)
        rem, k = n, 0
        while rem % p == 0:
            rem //= p
            k += 1
        if rem == 1:
            active.append((n, p, k))
    return active


def chain_norm(n, L, log_horizon=None):
    if log_horizon:
        if n*n >= log_horizon:
            return A(1)
        if n**3 >= log_horizon:
            return A(2).sqrt()
    else:
        d = A(n).log()
        if 2*d > L:
            return A(1)
        if 3*d > L:
            return A(2).sqrt()
    return A(2)


def moment(rows, cols, kind, delta=None, upper=None):
    vals = []
    hn, hn2, ds = A(0), A(0), A(0)
    for k in range(rows+cols-1):
        s = A(k+1)
        hn += 1/s
        hn2 += 1/s**2
        if kind == 'plain': v = 1/s
        elif kind == 'log': v = -1/s**2
        elif kind == 'log2': v = 2/s**3
        elif kind == 'tail': v = (1-delta**(k+1))/s
        elif kind == 'tail_log': v = -(1-delta**(k+1))/s**2-delta**(k+1)*delta.log()/s
        elif kind == 'log1': v = -hn/s
        elif kind == 'loglog': v = hn/s**2-(A.pi()**2/6-hn2)/s
        elif kind == 'tail_log1':
            ds += delta**(k+1)/s
            v = ((1-delta**(k+1))*(1-delta).log()-hn+ds)/s
        elif kind == 'window': v = (upper**(k+1)-delta**(k+1))/s
        else: raise ValueError(kind)
        vals.append(v)
    return AM([[vals[i+j] for j in range(cols)] for i in range(rows)])


def reflect(q):
    K = q.ncols()
    r = AM([[math.comb(k, j)*(-1)**j if j <= k else 0 for j in range(K)] for k in range(K)])
    return q*r


def ldl(mat):
    n = mat.nrows()
    low = [[A(0) for _ in range(n)] for _ in range(n)]
    piv = []
    for i in range(n):
        v = mat[i, i]
        for k in range(i):
            v -= low[i][k]**2*piv[k]
        if not v > 0:
            return {'positive': False, 'failed_pivot': i, 'pivot': show(v), 'pivot_ball': pack(v)}
        piv.append(v)
        for j in range(i+1, n):
            w = mat[j, i]
            for k in range(i):
                w -= low[j][k]*low[i][k]*piv[k]
            low[j][i] = w/v
    mn = min(x.lower() for x in piv)
    return {'positive': True, 'minimum_pivot_lower': show(mn), 'pivots': [pack(x) for x in piv]}


def analytic(L, g, N, active, log_horizon):
    # Cauchy majorant on |z|=3, verified as strict ball inequalities.
    assert A(3).sin() > rat(F(1, 8)) and rat(F(3, 2)).exp() < 5
    assert 5*(24+12) < 256
    M = len(g)-1
    ratio = L/3
    assert 0 < L and L < 3
    eta = 256*ratio**(M+1)/((M+1)*(1-ratio))
    K = sum((rat(abs(g[j]))*L**(j-1) for j in range(1, M+1)), A(0))
    K += rat(F(256, 3))*ratio**M/(1-ratio)
    arithmetic = sum((A(p).log()/A(n).sqrt()*chain_norm(n, L, log_horizon) for n,p,k in active), A(0))
    floor = sum((rat(F(1, j)) for j in range(1, N+1)), A(0))-A.const_euler()-(A.pi()*L).log()
    floor -= K*L/(2*A(N*(N+1)).sqrt())+arithmetic
    change = (L/2).cosh()*((L/2).exp()*L**3/3+L**2/4)
    for n,p,k in active:
        d = A(n).log()
        change += A(p).log()/A(n).sqrt()*d**2*(d/2).cosh()*chain_norm(n, L, log_horizon)/2
    return {'tail_floor': floor, 'profile_remainder': eta, 'smooth_variation': K,
            'arithmetic_norm_bound': arithmetic, 'generator_change_constant': change}


def build(args):
    start = time.time()
    N, M = args.N, args.M
    K = N+M
    L = A(args.log_horizon).log() if args.log_horizon else rat(args.horizon)
    assert 1 < L and L < 2 and N >= 2 and M >= 1
    active = prime_powers(L, args.log_horizon)
    for n,p,k in active:
        assert A(n).log() < L
    g = profile(M)
    p = AM([[(-1)**(n+k)*math.comb(n,k)*math.comb(n+k,k) if k <= n else 0 for k in range(N)] for n in range(N)])
    ell = A.const_euler()+(2*A.pi()*L).log()
    b = AM(N, K)
    h = F(0)
    for k in range(N):
        if k: h += F(1, k)
        b[k,k] = ell-rat(h)
        beta = F(1, k+1)
        for j in range(1, M+1):
            if j > 1: beta *= F(j-1, j+k)
            b[k,k+j] = rat(g[j]*beta)*L**j
    q = p*b
    delays = []
    for n,prime,kpower in active:
        delta = A(n).log()/L
        bd = 2*A(prime).log()/A(n).sqrt()
        tr = AM([[math.comb(k,r)*(-delta)**(k-r) if r<=k else 0 for r in range(N)] for k in range(N)])
        delays.append((delta, (p*tr)*bd))
    print('Profiles built', round(time.time()-start, 3), flush=True)
    # Unnormalized causal derivative matrix and its complete output Gram.
    dmat = p*moment(N,K,'plain')*q.transpose()+p*moment(N,N,'log')*p.transpose()
    gram = q*moment(K,K,'plain')*q.transpose()+p*moment(N,N,'log2')*p.transpose()
    c = p*moment(N,K,'log')*q.transpose()
    gram += c+c.transpose()
    for delta,v in delays:
        dmat += p*moment(N,N,'tail',delta)*v.transpose()
        c = q*moment(K,N,'tail',delta)*v.transpose()+p*moment(N,N,'tail_log',delta)*v.transpose()
        gram += c+c.transpose()
    for i,(delta,v) in enumerate(delays):
        for j,(deltaj,vj) in enumerate(delays):
            # The active prime powers, hence deltas, are sorted exactly.
            gram += v*moment(N,N,'tail',delays[max(i,j)][0])*vj.transpose()
    print('Full causal Gram built', round(time.time()-start, 3), flush=True)
    pr, qr = reflect(p), reflect(q)
    cross = q*moment(K,K,'plain')*qr.transpose()+p*moment(N,K,'log')*qr.transpose()
    cross += q*moment(K,N,'log1')*pr.transpose()+p*moment(N,N,'loglog')*pr.transpose()
    for delta,v in delays:
        c = v*moment(N,K,'tail',delta)*qr.transpose()+v*moment(N,N,'tail_log1',delta)*pr.transpose()
        cross += c+c.transpose()
    overlaps = []
    for i,((ni,_,_),(delta,v)) in enumerate(zip(active,delays)):
        for j,((nj,_,_),(deltaj,vj)) in enumerate(zip(active,delays)):
            yes = ni*nj < args.log_horizon if args.log_horizon else A(ni*nj).log() < L
            if yes:
                cross += v*moment(N,N,'window',delta,1-deltaj)*reflect(vj).transpose()
                overlaps.append([ni,nj])
            else:
                assert ni*nj >= args.log_horizon if args.log_horizon else A(ni*nj).log() > L
    scales = [A(2*n+1).sqrt() for n in range(N)]
    for i in range(N):
        for j in range(N):
            for mat in (dmat, gram, cross):
                mat[i,j] *= scales[i]*scales[j]
    gram, cross = sym(gram), sym(cross)
    Q = -(dmat+dmat.transpose())/2
    for i in range(N):
        for j in range(N):
            if (i+j)%2:
                assert Q[i,j].contains(0)
                Q[i,j] = 0  # exact reflection symmetry of the model
    Q = sym(Q)
    tr = sum((gram[i,i] for i in range(N)), A(0))
    assert tr < 10**7  # in particular ||U_tilde P|| < 10000
    eq = AM(N,N)
    for parity in [0,1]:
        ids = list(range(parity,N,2))
        head = block(Q,ids)
        e = (block(gram,ids)+(-1)**parity*block(cross,ids))/2-head*head
        for i,ii in enumerate(ids):
            for j,jj in enumerate(ids): eq[ii,jj]=e[i,j]
    eq = sym(eq)
    bounds = analytic(L,g,N,active,args.log_horizon)
    matrices = {'Q':Q,'Gram_causal':gram,'ReflectedGram_causal':cross,'E_central':eq}
    maximum_radius = max(x.rad() for mat in matrices.values() for x in mat.entries())
    data = {'N':N,'M':M,'precision_bits':ctx.prec,'horizon':args.horizon,
            'log_horizon':args.log_horizon,'active_prime_powers':active,'reflected_delay_overlaps':overlaps,
            'arithmetic':'Direct Arb enclosures throughout; no aggregate rounding allowance',
            'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'flint':flint.__FLINT_VERSION__},
            'bounds':{k:pack(v) for k,v in bounds.items()},'bound_display':{k:show(v) for k,v in bounds.items()},
            'full_gram_trace':show(tr),'maximum_matrix_radius':show(maximum_radius),
            'elapsed_build_seconds':time.time()-start,
            'matrices':{k:[[pack(mat[i,j]) for j in range(N)] for i in range(N)] for k,mat in matrices.items()}}
    print('Full reflected Gram and exact parity leakage built',round(time.time()-start,3),flush=True)
    return data


def validate(data, floor):
    N = data['N']
    mats = {k:AM([[unpack(x) for x in row] for row in mat]) for k,mat in data['matrices'].items()}
    b = {k:unpack(v) for k,v in data['bounds'].items()}
    a, eta, m = b['tail_floor'].lower(), b['profile_remainder'].upper(), rat(floor)
    assert a > m
    modelerr = ((a-m).abs_upper()+40000)*eta+2*eta**2
    checks=[]
    for parity in [0,1]:
        ids = list(range(parity,N,2))
        head, leakage = block(mats['Q'],ids), block(mats['E_central'],ids)
        test = (head-ident(len(ids))*m)*(a-m)-leakage-ident(len(ids))*modelerr.upper()
        check=ldl(test)
        check['parity']=parity
        checks.append(check)
        print('Parity',parity,{k:v for k,v in check.items() if k not in ['pivots','pivot_ball']},flush=True)
    return {'status':'PASS' if all(c['positive'] for c in checks) else 'NOT CERTIFIED',
            'N':N,'M':data['M'],'precision_bits':data['precision_bits'],
            'horizon':data['horizon'],'log_horizon':data['log_horizon'],'central_coercivity':floor,
            'bound_display':data['bound_display'],'model_error':show(modelerr),
            'maximum_matrix_radius':data['maximum_matrix_radius'],
            'checks':checks,'scope':'Full operator via analytic tail and full-output exact-parity Gram; all finite arithmetic enclosed by Arb. Subject to independent mathematical/code review.'}


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--N',type=int,default=128)
    ap.add_argument('--M',type=int,default=180)
    ap.add_argument('--bits',type=int,default=1536)
    ap.add_argument('--horizon',default='9/5')
    ap.add_argument('--log-horizon',type=int)
    ap.add_argument('--floor',default='1e-26')
    ap.add_argument('--output',default='output/length_1p8_N128')
    ap.add_argument('--reuse',action='store_true')
    args=ap.parse_args()
    ctx.prec=args.bits
    out=Path(args.output);out.mkdir(parents=True,exist_ok=True)
    archive=out/'central_matrices.json.gz'
    if args.reuse:
        with gzip.open(archive,'rt') as f:data=json.load(f)
        assert ctx.prec>=data['precision_bits']
    else:
        data=build(args)
        with gzip.open(archive,'wt') as f:json.dump(data,f)
    result=validate(data,args.floor)
    result['matrix_archive_sha256']=hashlib.sha256(archive.read_bytes()).hexdigest()
    (out/'central_certificate.json').write_text(json.dumps(result,indent=2)+'\n')
    print('FINAL',result['status'],flush=True)


if __name__=='__main__':main()
