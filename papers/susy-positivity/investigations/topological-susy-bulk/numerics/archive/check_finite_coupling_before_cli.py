"""Additional review diagnostics from the printed model, using NumPy only.

These computations do not certify a sign or a quadrature error bound.
The scalar coefficient obstruction is elementary exact algebra; its decimals
and the finite-coupling pairing checks are recorded for inspection.
"""
from pathlib import Path
import json
import math
import numpy as np
from numpy.polynomial.legendre import leggauss


BERNOULLI = [1/6, -1/30, 1/42, -1/30, 5/66, -691/2730, 7/6, -3617/510]


def psi_and_trigamma(z):
    z = np.asarray(z, dtype=complex)
    shifted = z + 20
    psi = np.log(shifted) - 1/(2*shifted)
    tri = 1/shifted + 1/(2*shifted**2)
    for k, value in enumerate(BERNOULLI, 1):
        psi -= value/(2*k*shifted**(2*k))
        tri += value/shifted**(2*k+1)
    for j in range(20):
        psi -= 1/(z+j)
        tri += 1/(z+j)**2
    return psi, tri


def kinetic(tau):
    psi, tri = psi_and_trigamma(.25+.5j*np.asarray(tau))
    psi0 = -np.euler_gamma - np.pi/2 - 3*np.log(2)
    return psi.real-psi0, -.5*np.asarray(tau)*tri.imag


def pairing_comparison(nx, nt, cutoff, panel):
    # A complex C-infinity bump supported strictly inside I_1.
    nodes, weights = leggauss(nx)
    x, wx = .49*nodes, .49*weights
    f = np.exp(-1/(1-(x/.49)**2))*(1+.3j*x)*np.exp(3j*x)
    tn, tw = leggauss(nt)
    starts = np.arange(-cutoff, cutoff, panel)
    tau = (starts[:, None]+panel/2+panel*tn/2).ravel()
    wt = np.tile(panel*tw/2, len(starts))
    fhat = np.concatenate([np.exp(-1j*np.outer(ts, x))@(wx*f)
                           for ts in np.array_split(tau, math.ceil(len(tau)/1024))])
    density = wt*np.abs(fhat)**2/(2*np.pi)
    base, h = kinetic(tau)
    d = np.log(2)
    rows = []
    norm = float(np.dot(wx, np.abs(f)**2))
    for alpha in [.001, .01, .1, 2*d/np.sqrt(2)]:
        m = 1-alpha*np.exp(-1j*d*tau)
        changed, _ = kinetic(tau*np.abs(m))
        actual = float(np.dot(density, changed-base))
        tangent = float(np.dot(density, -alpha*h*np.cos(d*tau)))
        rows.append(dict(alpha=float(alpha),
                         actual_change=actual,
                         first_order_prediction=tangent,
                         difference=actual-tangent,
                         difference_per_input_norm=(actual-tangent)/norm))
    return dict(nx=nx, nt=nt, cutoff=cutoff, panel=panel,
                spatial_norm=norm, fourier_norm=float(density.sum()),
                comparisons=rows)


def main():
    alpha2 = 2*math.log(2)/math.sqrt(2)
    scalar = dict(
        required_alpha2=alpha2,
        required_alpha3=2*math.log(3)/math.sqrt(3),
        single_factor_first_coefficient_supremum=1,
        predicted_second2=alpha2**2/2,
        target_second2=math.log(2),
        exact_regular_remainder_at_zero=-math.log(1-alpha2),
        first_order_regular_remainder_at_zero=alpha2,
    )
    # Independent check of the digamma implementation against positive series.
    masses=2*np.arange(200000)+.5
    controls=[]
    for t in [0., .1, 1., 5., 20.]:
        b,h=kinetic(t)
        s=t*t
        b_series=np.sum(2/masses*s/(masses*masses+s))
        h_series=np.sum(4*masses*s/(masses*masses+s)**2)
        controls.append(dict(tau=t, B_difference=float(b-b_series),
                             h_difference=float(h-h_series)))
    output=dict(status='Floating-point diagnostics; analytic coefficient comparison is exact.',
                scalar_obstructions=scalar,
                digamma_series_controls=controls,
                pairings=[pairing_comparison(256,48,160,1.),
                          pairing_comparison(384,64,240,.5)])
    dest=Path(__file__).with_name('finite-coupling-diagnostics.json')
    dest.write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))


if __name__=='__main__':
    main()
