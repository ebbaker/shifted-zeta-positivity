#!/usr/bin/env python3
"""Outward interval certificate for a real simple heat zero at every time.

Uses the existing stdlib Decimal interval backend and analytic disk error in
check_fixed_heat_checkpoint. Every rectangle cell is covered, with strict
endpoint sign and derivative inequalities. No sampled floating result enters
the certificate. The imported Polymath theorem and Note 3 disk lemma remain
analytic inputs. Run from this directory or with it on PYTHONPATH.
"""
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path
import check_fixed_heat_checkpoint as h


def real_formula(t, x, nmax):
    """Differentiate the real finite formula before interval evaluation.

    This eliminates the cancellation of the normalizer derivative in G'/A-bF.
    Here ar_x=aip/2, ai_x=-arp/2 and theta_x=-Re(m'_t)/2.
    """
    d = 1 + x.square()
    ar = (d.ln()/2-(4*h.PI).ln())/2 - 1/d
    at = h.atan_small(1/x, terms=20)
    ai = -h.PI/4 + at/2 + 3*x/d
    theta = -7*h.PI/8 - at/4 + x*(1-(d.ln()/2-(4*h.PI).ln()))/4 + t*ar*ai/2
    arp = 6*(x.square()-1)/d.square() + 1/d
    aip = 4*x/d.square() + x/d
    f = h.I(0)
    fp = h.I(0)
    for n in range(1, nmax+1):
        l = h.logn(n)
        amp = (t*l.square()/4-(h.I('.5')+t*ar/2)*l).exp()
        sn, cs = h.sin_cos(theta+(x-t*ai)*l/2)
        lr = (ar-l)*(1+t*arp/2)-ai*t*aip/2
        f = f + 2*amp*cs
        fp = fp + amp*(lr*sn-t*aip*l*cs/2)
    return f, fp


def derivative_algebra_checks():
    count = 0
    for x in (Q(2011), Q(40053, 10), Q(40055, 10), Q(40058, 10)):
        d = 1+x*x
        arx = x/(2*d)+2*x/(d*d)
        aix = -1/(2*d)+3*(1-x*x)/(d*d)
        arp = 6*(x*x-1)/(d*d)+1/d
        aip = 4*x/(d*d)+x/d
        assert arx == aip/2 and aix == -arp/2
        for t in (Q(1, 5), Q(1, 4), Q(3, 10)):
            for ar in (Q(-1), Q(0), Q(3)):
                for ai in (Q(-4, 5), Q(1, 7)):
                    for l in (Q(0), Q(1), Q(5, 3)):
                        li = (ar-l)*t*aip/2 + ai*(1+t*arp/2)
                        b = (ai*(1+t*arp/2)+ar*t*aip/2)/2
                        assert li-2*b == -t*aip*l/2
                        count += 1
    return count


def certificate():
    X, R, a = h.I('4005.5'), h.I('.7'), h.I('.3')
    ep, ta = h.I('.2'), h.I('.3')
    N = 17
    eta, cutoffs = h.heat_error(X, ep, ta, R, N)
    derivative_error = eta/(R-a)
    assert cutoffs == [17, 17]
    assert X.lo-R.hi > 200 and R.hi <= 1
    assert eta.hi < h.D('.554')
    assert derivative_error.hi < h.D('1.385')
    nx, nt = 30, 20
    x0, x1, t0, t1 = map(h.D, ('4005.2', '4005.8', '.2', '.3'))
    xmin = None
    left_upper = None
    right_lower = None
    overlap_checks = 0
    for k in range(nt):
        tlo = h.DOWN.add(t0, h.DOWN.divide(h.D(k)*h.D('.1'), h.D(nt)))
        thi = h.UP.add(t0, h.UP.divide(h.D(k+1)*h.D('.1'), h.D(nt)))
        tv = h.I(tlo, thi)
        left, _ = real_formula(tv, h.I(x0), N)
        right, _ = real_formula(tv, h.I(x1), N)
        assert left.hi+eta.hi < 0, (k, left.endpoints())
        assert right.lo-eta.hi > 0, (k, right.endpoints())
        left_upper = left.hi if left_upper is None else max(left_upper, left.hi)
        right_lower = right.lo if right_lower is None else min(right_lower, right.lo)
        for j in range(nx):
            xlo = h.DOWN.add(x0, h.DOWN.divide(h.D(j)*h.D('.6'), h.D(nx)))
            xhi = h.UP.add(x0, h.UP.divide(h.D(j+1)*h.D('.6'), h.D(nx)))
            xv = h.I(xlo, xhi)
            _, fp = real_formula(tv, xv, N)
            assert fp.lo > derivative_error.hi, (j, k, fp.endpoints())
            xmin = fp.lo if xmin is None else min(xmin, fp.lo)
        # A check against the earlier analytic G'/A-bF representation at
        # exact points, separate from the whole-cell inequalities.
        f, fp = real_formula(h.I(tlo), X, N)
        old_f, old_fp = h.finite_heat(h.I(tlo), X, N)
        assert max(f.lo, old_f.lo) <= min(f.hi, old_f.hi)
        assert max(fp.lo, old_fp.lo) <= min(fp.hi, old_fp.hi)
        overlap_checks += 2
    qprime = h.DOWN.subtract(xmin, derivative_error.hi)
    qleft = h.UP.add(left_upper, eta.hi)
    qright = h.DOWN.subtract(right_lower, eta.hi)
    assert qprime > h.D('2.3') and qleft < h.D('-.44') and qright > h.D('.59')
    return {
        'status': 'outward interval certificate passed',
        'date': '2026-10-09',
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'interval_backend_sha256': hashlib.sha256(Path(h.__file__).read_bytes()).hexdigest(),
        'precision': h.PREC,
        'backend': 'stdlib Decimal; directed arithmetic, widened exp/ln/sqrt, Machin pi, explicit Taylor remainders',
        'rectangle': {'x': [str(x0), str(x1)], 't': [str(t0), str(t1)]},
        'outer_disk': {'center': '4005.5', 'radius': '.7', 'inner_radius': '.3'},
        'fixed_N': N,
        'natural_cutoffs': cutoffs,
        'spatial_cells': nx, 'time_cells': nt,
        'derivative_cells': nx*nt, 'endpoint_time_cells': 2*nt,
        'exact_derivative_algebra_checks': derivative_algebra_checks(),
        'point_formula_overlap_checks': overlap_checks,
        'pi_interval': h.PI.endpoints(),
        'eta_interval': eta.endpoints(),
        'derivative_error_interval': derivative_error.endpoints(),
        'finite_Fprime_lower_bound': str(xmin),
        'finite_left_F_upper_bound': str(left_upper),
        'finite_right_F_lower_bound': str(right_lower),
        'normalized_Qprime_lower_bound': str(qprime),
        'normalized_left_Q_upper_bound': str(qleft),
        'normalized_right_Q_lower_bound': str(qright),
        'source': 'Polymath, arXiv:1904.12438v2, Theorem 1.3; repository Newman Note 3, equations (14)-(17)',
        'scope': 'For every t in [1/5,3/10], exactly one real zero of H_t lies in (4005.2,4005.8), and it is simple. No real multiple zero occurs on the full rectangle. Imported source theorem, analytic disk lemma and Decimal runtime guarantees are proof inputs. No RH or Newman bound is established.'
    }


if __name__ == '__main__':
    print(json.dumps(certificate(), indent=2))
