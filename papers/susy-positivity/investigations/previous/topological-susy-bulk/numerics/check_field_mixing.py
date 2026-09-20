"""Check a positive two-field gamma channel and its exact residual.

NumPy only. Exact coefficient algebra uses fractions.Fraction. Floating-point
checks are diagnostics, not interval certificates. No zeta data are used.
"""
from pathlib import Path
from fractions import Fraction as F
from math import comb
import argparse
import hashlib
import json
import platform
import numpy as np
from numpy.polynomial.legendre import leggauss


PSI0 = -np.euler_gamma - np.pi / 2 - 3 * np.log(2)
W0 = PSI0 - np.log(np.pi)


def bernoulli_numbers(n):
    values = [F(1)]
    for j in range(1, n + 1):
        values.append(-sum(F(comb(j + 1, k)) * values[k]
                           for k in range(j)) / (j + 1))
    return values


BERN = bernoulli_numbers(20)


def gamma_coefficient(n):
    degree = 2 * n
    poly = sum(F(comb(degree, k)) * BERN[k] * F(1, 4)**(degree-k)
               for k in range(degree + 1))
    return (-1)**(n+1) * F(2**degree, degree) * poly


COEFFICIENTS = [float(gamma_coefficient(n)) for n in range(1, 9)]


def kinetic(tau):
    tau = np.asarray(tau, dtype=float)
    z = .25 + .5j * tau
    shifted = z + 20
    psi = np.log(shifted) - 1 / (2 * shifted)
    for k in range(1, 9):
        psi -= float(BERN[2*k]) / (2*k * shifted**(2*k))
    for j in range(20):
        psi -= 1 / (z+j)
    return psi.real - PSI0


def gamma_regular(tau):
    """B(tau^2)-log|tau|+log(2)+psi(1/4), for nonzero real tau.

    The large argument branch avoids subtracting two logarithms. Its finite
    asymptotic series is used only for diagnostics, never as an enclosure.
    """
    tau = np.asarray(tau, dtype=float)
    out = np.empty_like(tau)
    high = np.abs(tau) >= 50
    inv = 1 / tau[high]**2
    poly = np.zeros_like(inv)
    for coefficient in reversed(COEFFICIENTS):
        poly = (poly + coefficient) * inv
    out[high] = poly
    out[~high] = (kinetic(tau[~high]) - np.log(np.abs(tau[~high]))
                  + np.log(2) + PSI0)
    return out


def generator(tau, contact=W0, length=np.log(2), reflection=2**(-.5),
              weight=np.log(2)):
    z = reflection * np.exp(-1j * length * np.asarray(tau))
    return contact - 2 * weight * z / (1-z)


def channel(tau, compliance, a=.5):
    return (2/a) * tau**2 / (tau**2 + a*a*compliance)


def channel_change(tau, q, a=.5, delta=1/24):
    X = (1-delta)*q + delta
    return (2*a*delta*(q-1)*tau**2
            / ((tau**2+a*a*X)*(tau**2+a*a*q)))


def residuals(tau, contact=W0):
    v = generator(tau, contact).real
    q = np.exp(-2*v)
    rho = gamma_regular(tau*np.exp(v))-gamma_regular(tau)
    return rho, rho + channel_change(tau, q)


def exact_algebra():
    b2, b4 = gamma_coefficient(1), gamma_coefficient(2)
    delta = F(1, 24)
    # Ascending powers of q for b4(q^2-1)+(X^2-q^2)/4.
    inverse4 = [-b4+delta**2/4, delta*(1-delta)/2,
                b4+((1-delta)**2-1)/4]
    assert b2 == -F(1,24)
    assert b4 == -F(7,960)
    assert b2 + delta == 0
    assert inverse4 == [F(89,11520), F(230,11520), -F(319,11520)]
    assert sum(inverse4) == 0
    return dict(b2=str(b2), b4=str(b4), delta=str(delta),
                inverse4_ascending=[str(x) for x in inverse4],
                factorization='-(q-1)*(319*q+89)/11520',
                all_fraction_checks_passed=True)


def bare_energy_checks():
    rows = []
    a, delta = .5, 1/24
    for contact in [0., float(W0)]:
        for tau in [.1, 1., 7., 30., 100.]:
            m = np.exp(generator(tau, contact))
            q = 1 / abs(m)**2
            X = (1-delta)*q+delta
            c1, c2 = 1/(a*np.sqrt(1-delta)), 1/(a*np.sqrt(delta))
            D = np.array([[1, 0], [c1*m*1j*tau, -c1*m], [0,c2]], complex)
            J = np.array([1,0,0], complex)
            solution = np.linalg.solve(D.conj().T@D, D.conj().T@J)
            state = J-D@solution
            numerical = (2/a)*float(np.vdot(state,state).real)
            expected = float(channel(tau, X))
            u = a*a*X/(tau*tau+a*a*X)
            w = delta/X*1j*tau*u
            rows.append(dict(contact=contact,tau=tau,
                             energy=numerical,formula=expected,
                             error=abs(numerical-expected),
                             equilibrium_error=float(np.linalg.norm(solution-[u,w])),
                             harmonic_error=float(np.linalg.norm(D.conj().T@state))))
    assert max(x['error'] for x in rows) < 1e-11
    assert max(x['harmonic_error'] for x in rows) < 1e-10
    # A genuine pure relaxation control: E=|F-u-w|^2+s|u|^2+b|w|^2.
    s, b = 2., 3.
    H = np.array([[1+s,1],[1,1+b]])
    sol = np.linalg.solve(H,np.ones(2))
    relaxed = (1-sol.sum())**2+s*sol[0]**2+b*sol[1]**2
    expected = 1/(1+1/s+1/b)
    assert abs(relaxed-expected) < 1e-14
    assert 0 < relaxed < s/(1+s)
    return dict(two_field=rows,
                relaxation_control=dict(old=s/(1+s),new=relaxed,formula=expected))


def derivative_field_checks():
    a,delta,mu=.5,1/24,2.
    rows=[]
    for tau in [.1,1.,7.,30.,100.]:
        m=np.exp(generator(tau))
        q=1/abs(m)**2
        X=(1-delta)*q+delta/(1+a*a*mu*delta*tau*tau)
        c1,c2=1/(a*np.sqrt(1-delta)),1/(a*np.sqrt(delta))
        D=np.array([[1,0],[c1*m*1j*tau,-c1*m],[0,c2],
                    [0,np.sqrt(mu)*1j*tau]],complex)
        J=np.array([1,0,0,0],complex)
        sol=np.linalg.solve(D.conj().T@D,D.conj().T@J)
        state=J-D@sol
        actual=(2/a)*float(np.vdot(state,state).real)
        expected=float(channel(tau,X))
        rows.append(dict(tau=tau,energy=actual,formula=expected,
                         error=abs(actual-expected)))
    assert max(x['error'] for x in rows)<1e-11
    # For delta=1/(48a), the nonconstant q coefficient vanishes,
    # but the residual constant inverse-square coefficient is exactly 1/24.
    assert 2*F(1,2)*F(1,24)-F(1,24)==0
    theta=2*np.pi*np.arange(32768)/32768
    q=np.exp(-2*generator(theta/np.log(2)).real)
    q1=float(np.mean(q*np.cos(theta)))
    assert q1>0
    return dict(mu=mu,rows=rows,q_first_complex_fourier_coefficient=q1,
                residual_inverse2_after_active_shift_cancellation='1/24',
                resulting_diagonal_derivative_jump='-1/24')


def asymptotic_checks():
    theta = 2*np.pi*np.arange(32768)/32768
    length = np.log(2)
    q = np.exp(-2*generator(theta/length).real)
    d4 = -(q-1)*(319*q+89)/11520
    beta0 = float(np.mean(q)-1)
    gamma0 = float(np.mean(d4))
    assert beta0 > 0 and np.max(d4) < 0
    rows = []
    for angle in [0., .4, 1.2, np.pi]:
        for cycles in [100000,300000,1000000]:
            tau = (2*np.pi*cycles+angle)/length
            qvalue = float(np.exp(-2*generator(tau).real))
            rho, corrected = [float(x) for x in residuals(tau)]
            expected2 = -(qvalue-1)/24
            expected4 = -(qvalue-1)*(319*qvalue+89)/11520
            rows.append(dict(angle=angle,cycles=cycles,tau=tau,
                             original_scaled=tau*tau*rho,expected2=expected2,
                             corrected_scaled=tau**4*corrected,expected4=expected4,
                             corrected_ratio=tau**4*corrected/expected4))
    # Cancellation limits the final digits; the exact fraction proof is primary.
    assert max(abs(x['corrected_ratio']-1) for x in rows) < .003
    controls=[]
    for value in [50.,100.,300.]:
        direct = kinetic(value)-np.log(value)+np.log(2)+PSI0
        controls.append(dict(tau=value,asymptotic_vs_recurrence_error=
                             float(abs(gamma_regular(value)-direct))))
    assert max(x['asymptotic_vs_recurrence_error'] for x in controls) < 1e-13
    return dict(beta0=beta0,original_first_derivative_jump=beta0/24,
                gamma0=gamma0,corrected_third_derivative_jump=gamma0,
                q_min=float(q.min()),q_max=float(q.max()),
                scaled_checks=rows,regular_evaluation_controls=controls)


def packet_checks():
    # Support diameter .4 < log(2), making every nonzero translated overlap zero.
    xn,xw=leggauss(192)
    x,wx=.2*xn,.2*xw
    f=np.exp(-1/(1-xn*xn))
    norm=float(np.dot(wx,f*f))
    tn,tw=leggauss(16)
    starts=np.arange(-300.,300.,.5)
    eta=(starts[:,None]+.25+.25*tn).ravel()
    wt=np.tile(.25*tw,len(starts))
    ft=np.concatenate([np.exp(-1j*np.outer(ts,x))@(wx*f)
                       for ts in np.array_split(eta,40)])
    density=wt*np.abs(ft)**2/(2*np.pi)
    theta=2*np.pi*np.arange(32768)/32768
    q=np.exp(-2*generator(theta/np.log(2)).real)
    expected2=-float(np.mean(q)-1)*norm/24
    expected4=-float(np.mean((q-1)*(319*q+89)))*norm/11520
    rows=[]
    for carrier in [1e5,3e5,1e6]:
        original,corrected=residuals(carrier+eta)
        value2=float(carrier**2*np.dot(density,original))
        value4=float(carrier**4*np.dot(density,corrected))
        rows.append(dict(carrier=carrier,original_scaled_pairing=value2,
                         expected2=expected2,original_ratio=value2/expected2,
                         corrected_scaled_pairing=value4,expected4=expected4,
                         corrected_ratio=value4/expected4))
    assert abs(rows[-1]['original_ratio']-1) < .001
    assert abs(rows[-1]['corrected_ratio']-1) < .001
    return dict(support_radius=.2,spatial_nodes=192,frequency_nodes_per_panel=16,
                frequency_panel=.5,relative_frequency_cutoff=300,
                norm=norm,fourier_norm=float(density.sum()),rows=rows)


def finite_frequency_checks():
    # The paper's smooth compact complex witness, computed at two resolutions.
    rows=[]
    for nx,nt,cutoff,panel in [(192,24,140.,1.),(288,32,210.,.5)]:
        xn,xw=leggauss(nx)
        x,wx=.49*xn,.49*xw
        f=np.exp(-1/(1-xn*xn))*(1+.3j*x)*np.exp(3j*x)
        tn,tw=leggauss(nt)
        starts=np.arange(-cutoff,cutoff,panel)
        tau=(starts[:,None]+panel/2+panel*tn/2).ravel()
        wt=np.tile(panel*tw/2,len(starts))
        ft=np.concatenate([np.exp(-1j*np.outer(ts,x))@(wx*f)
                           for ts in np.array_split(tau,40)])
        density=wt*np.abs(ft)**2/(2*np.pi)
        norm=float(np.dot(wx,np.abs(f)**2))
        C=np.dot(wx,f*np.cosh(x/2)); S=np.dot(wx,f*np.sinh(x/2))
        poles=float(2*abs(C)**2-2*abs(S)**2)
        rho,corrected=residuals(tau)
        original=float(np.dot(density,rho))
        changed=float(np.dot(density,corrected))
        rows.append(dict(nx=nx,nt=nt,cutoff=cutoff,panel=panel,norm=norm,
                         original_residual=original,modified_residual=changed,
                         positive_energy_increase=changed-original,
                         Q_minus_original_Z=poles-original,
                         Q_minus_modified_Z=poles-changed))
    # These inequalities are numerical controls; the note does not certify them.
    assert abs(rows[-1]['Q_minus_original_Z']+.0008460031093333507) < 1e-9
    return rows


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: this diagnostic requires its assertions.')
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    data=dict(status='Exact rational algebra plus floating-point diagnostics; no interval sign certificate.',
              python=platform.python_version(),numpy=np.__version__,
              source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              model=dict(primes=[2],contact=float(W0),full_primitive_histories=True,
                         mass=.5,delta='1/24',target_length_range='log(2)<L<=log(3)'),
              exact_algebra=exact_algebra(),bare_energy=bare_energy_checks(),
              derivative_field=derivative_field_checks(),
              asymptotics=asymptotic_checks(),packets=packet_checks(),
              finite_frequency=finite_frequency_checks())
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(data,indent=2,allow_nan=False)+'\n')
    print(json.dumps(dict(output=str(args.output),
                          max_bare_energy_error=max(x['error'] for x in data['bare_energy']['two_field']),
                          beta0=data['asymptotics']['beta0'],gamma0=data['asymptotics']['gamma0'],
                          modified_defect=data['finite_frequency'][-1]['Q_minus_modified_Z']),indent=2))


if __name__=='__main__':
    main()
