"""Small NumPy-only diagnostics of an independently positive loop evolution.

No zeta zeros, target square root, eigenvalue sweep, or positivity certificate.
Run with --output PATH; all arrays are transient and only small records are saved.
"""
from pathlib import Path
import argparse
import hashlib
import json
import math
import platform
import numpy as np
from numpy.polynomial.legendre import leggauss

BERNOULLI = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510]
PSI0 = -np.euler_gamma - np.pi/2 - 3*np.log(2)
W0 = PSI0 - np.log(np.pi)


def kinetic(tau):
    tau = np.asarray(tau, dtype=float)
    z = .25+.5j*tau
    shifted = z+20
    psi = np.log(shifted)-1/(2*shifted)
    tri = 1/shifted+1/(2*shifted**2)
    for k, value in enumerate(BERNOULLI, 1):
        psi -= value/(2*k*shifted**(2*k))
        tri += value/shifted**(2*k+1)
    for j in range(20):
        psi -= 1/(z+j)
        tri += 1/(z+j)**2
    return psi.real-PSI0, -.5*tau*tri.imag


def potential(tau, primes, contact=0.):
    tau = np.asarray(tau)
    generator = np.zeros_like(tau, dtype=complex)+contact
    for p in primes:
        a, r = np.log(p), p**(-.5)
        z = r*np.exp(-1j*a*tau)
        generator -= 2*a*z/(1-z)
    return generator.real


def bump(x, L, kind):
    y = np.asarray(x)/(.49*L)
    out = np.zeros_like(y, dtype=complex)
    mask = np.abs(y)<1
    out[mask] = np.exp(-1/(1-y[mask]**2))
    if kind == 'complex':
        out *= (1+.3j*np.asarray(x))*np.exp(3j*np.asarray(x))
    elif kind == 'odd':
        out *= np.asarray(x)/L
    return out


def pairings(L, primes, kind, nx, nt, cutoff, panel):
    xn, xw = leggauss(nx)
    x, wx = .49*L*xn, .49*L*xw
    f = bump(x, L, kind)
    tn, tw = leggauss(nt)
    starts = np.arange(-cutoff, cutoff, panel)
    tau = (starts[:, None]+panel/2+panel*tn/2).ravel()
    wt = np.tile(panel*tw/2, len(starts))
    fhat = np.concatenate([np.exp(-1j*np.outer(ts, x))@(wx*f)
                           for ts in np.array_split(tau, math.ceil(len(tau)/1024))])
    density = wt*np.abs(fhat)**2/(2*np.pi)
    norm = float(np.dot(wx, np.abs(f)**2))
    base, _ = kinetic(tau)
    prime = 0.
    active = []
    for p in primes:
        a, r = np.log(p), p**(-.5)
        n = 1
        while n*a < L:
            # Integrate on the true overlap, not a grid-smeared cap.
            lo, hi = -.49*L+n*a, .49*L
            if lo < hi:
                xx = (lo+hi)/2+(hi-lo)*xn/2
                ww = (hi-lo)*xw/2
                overlap = np.dot(ww, np.conj(bump(xx,L,kind))*bump(xx-n*a,L,kind))
            else:
                overlap = 0j
            value = float(-2*a*r**n*np.real(overlap))
            prime += value
            active.append(dict(p=p, n=n, pairing=value))
            n += 1
    C = np.dot(wx, f*np.cosh(x/2))
    S = np.dot(wx, f*np.sinh(x/2))
    poles = float(2*abs(C)**2-2*abs(S)**2)
    K = float(np.dot(density,base))
    Q = K+W0*norm+prime+poles
    rows=[]
    for contact in [0., float(W0)]:
        v = potential(tau, primes, contact)
        deformed, _ = kinetic(tau*np.exp(v))
        residual = deformed-base-v
        Z = float(np.dot(density,deformed))
        R = float(np.dot(density,residual))
        target_principal = contact*norm+prime
        rows.append(dict(contact=contact, Z=Z, R=R,
                         principal_pairing_fourier=float(np.dot(density,v)),
                         principal_pairing_overlap=target_principal,
                         identity_error=Z-(K+target_principal+R),
                         full_Q_minus_Z=Q-Z,
                         normalized_R=R/norm))
    return dict(L=L, primes=primes, kind=kind, nx=nx, nt=nt, cutoff=cutoff,
                panel=panel, norm=norm, fourier_norm=float(density.sum()),
                K=K, prime_pairing=prime, active=active, pole_pairing=poles,
                full_Q_diagnostic=Q, variants=rows)


def coefficient_controls():
    theta = 2*np.pi*np.arange(8192)/8192
    rows=[]
    for p in [2,3,5]:
        a,r=np.log(p),p**(-.5)
        z=r*np.exp(-1j*theta)
        real_log=(-2*a*z/(1-z)).real
        for n in [1,2,3]:
            value=float(2*np.mean(real_log*np.cos(n*theta)))
            rows.append(dict(p=p,n=n,cosine_coefficient=value,
                             expected=float(-2*a*r**n),error=float(value+2*a*r**n)))
    th=2*np.pi*np.arange(128)/128
    zp=2**(-.5)*np.exp(-1j*th[:,None])
    zq=3**(-.5)*np.exp(-1j*th[None,:])
    v=(-2*np.log(2)*zp/(1-zp)-2*np.log(3)*zq/(1-zq)).real
    mixed=[float(2*np.mean(v*np.cos(th[:,None]+sign*th[None,:]))) for sign in [1,-1]]
    return dict(single_prime=rows,mixed_sum_and_difference=mixed,
                rational_control_second_cosine=float(-(.4**2)/2),
                old_required_alpha3=float(2*np.log(3)/np.sqrt(3)))


def analytic_controls():
    masses=2*np.arange(200000)+.5
    series=[]
    for t in [0.,.1,1.,5.,20.]:
        B,h=kinetic(t)
        s=t*t
        series.append(dict(tau=t,B_difference=float(B-np.sum(2/masses*s/(masses*masses+s))),
                           h_difference=float(h-np.sum(4*masses*s/(masses*masses+s)**2))))
    # Integral of the exact coupling derivative, not its value at coupling zero.
    ln,lw=leggauss(192)
    lam=(ln+1)/2
    frequencies=np.array([0.,.3,1.,3.,10.,50.,200.])
    v=potential(frequencies,[2,3],float(W0))
    b0,_=kinetic(frequencies)
    b1,_=kinetic(frequencies*np.exp(v))
    _,h=kinetic(frequencies[:,None]*np.exp(v[:,None]*lam))
    integrated=(v[:,None]*(h-1))@(lw/2)
    direct=b1-b0-v
    evolution_error=float(np.max(np.abs(integrated-direct)))
    # Check the first inverse-square term of the digamma expansion.
    high=[]
    for t in [1e3,3e3,1e4]:
        b,_=kinetic(t)
        high.append(dict(tau=t,scaled_error=float(t*t*(b-np.log(t)+np.log(2)+PSI0)),
                         expected=-1/24))
    # A non-arithmetic control: the construction works for any assigned delay.
    t=np.linspace(-40,40,1201)
    a,r,weight=.81,.37,.62
    z=r*np.exp(-1j*a*t)
    g=-2*weight*z/(1-z)
    m=np.exp(g)
    arbitrary_delay_error=float(np.max(np.abs(np.log(np.abs(m))-g.real)))
    theta=2*np.pi*np.arange(32768)/32768
    one_prime=-2*np.log(2)*(2**(-.5)*np.exp(-1j*theta)/(1-2**(-.5)*np.exp(-1j*theta))).real
    cusps=[]
    for contact in [0., float(W0)]:
        a0=float(np.mean(np.exp(-2*(contact+one_prime)))-1)
        cusps.append(dict(contact=contact,mean_exponential_minus_one=a0,
                          predicted_derivative_jump=a0/24))
    # A true rational transfer controls the logarithmic-derivative obstruction:
    # (1-alpha*z)'/(1-alpha*z) has a simple pole, not the target double pole.
    rational_alpha=.4
    rational=np.log(np.abs(1-rational_alpha*np.exp(-1j*theta)))
    rational_error=float(2*np.mean(rational*np.cos(2*theta))+rational_alpha**2/2)
    return dict(series=series,evolution_integral_max_error=evolution_error,
                asymptotic=high,arbitrary_delay_log_identity_error=arbitrary_delay_error,
                one_prime_cusp=cusps,rational_second_coefficient_error=rational_error)


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    records=[]
    for resolution in [(192,32,140.,1.),(288,48,210.,.5)]:
        for L,primes,kind in [(1.,[2],'complex'),(1.25,[2,3],'complex'),
                              (1.5,[2,3],'complex'),(1.25,[2,3],'odd'),
                              (1.,[2,3],'complex')]:
            records.append(pairings(L,primes,kind,*resolution))
    output=dict(status='Floating-point diagnostics, not error enclosures or a positivity proof.',
                python=platform.python_version(),numpy=np.__version__,
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                w0=float(W0),coefficient_controls=coefficient_controls(),
                analytic_controls=analytic_controls(),pairings=records)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(output,indent=2)+'\n')
    summary=dict(output=str(args.output),record_bytes=args.output.stat().st_size,
                 max_coefficient_error=max(abs(x['error']) for x in output['coefficient_controls']['single_prime']),
                 max_pairing_identity_error=max(abs(v['identity_error']) for row in records for v in row['variants']),
                 max_evolution_error=output['analytic_controls']['evolution_integral_max_error'])
    print(json.dumps(summary,indent=2))


if __name__=='__main__':
    main()
