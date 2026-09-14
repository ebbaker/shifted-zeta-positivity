#!/usr/bin/env python3
"""Independent numerical checks; the checks themselves are not certificates."""
import json
from pathlib import Path
import mpmath as mp
from flint import arb as A, ctx
import certify_vector_storage as c

mp.mp.dps = 65
ctx.prec = 3072

def mid(x):
    a,b = x.mid().man_exp()
    return mp.mpf(int(a))*mp.mpf(2)**int(b)

def run():
    w = mp.mpf(1)/4
    L = mp.log(3)
    p = c.gamma_output([A(1)],A(3).log(),A(1)/4,160)
    coef = [mid(x) for x in reversed(p.coeffs())]
    def model(t):
        return (t/L)**w*mp.polyval(coef,t/L) if t else mp.mpf(0)
    # This expression comes directly from the gamma-ratio beta kernel and
    # the rational impulse, without using the analytic-profile recurrence.
    def beta_integral(t):
        alpha,beta = mp.mpf(1)/2-w,mp.mpf(1)/2+w
        def integrand(r):
            v = t*r**(1/w)
            g = mp.exp(v/2)*(mp.sinh(v)/v)**(w-1) if v else mp.mpf(1)
            return g*(1-4*w*(mp.exp(alpha*(t-v))-mp.exp(-beta*(t-v))))
        return (2*mp.pi*t)**w/mp.gamma(1+w)*mp.quad(integrand,[0,1])
    kernel_errors = [abs(model(t)-beta_integral(t)) for t in [L/10,L/2,L]]
    ds = c.delays(3,A(3).log(),A(1)/4)
    matrix_norm = mid(c.full_norm_sq(p,ds,A(1)/4))
    delay = mp.log(2)/L
    b = mp.power(2,w-mp.mpf(1)/2)*(1-mp.power(2,-2*w))
    def out(u):
        return model(L*u)+(b*model(L*(u-delay)) if u>delay else 0)
    quad_norm = mp.quad(lambda u:out(u)**2,[0,delay,1])
    norm_error = abs(matrix_norm-quad_norm)
    assert max(kernel_errors)<mp.mpf('1e-55')
    assert norm_error<mp.mpf('1e-55')
    # Algebra check on a genuinely noncommuting block example.
    X=mp.matrix([[0,0],[mp.mpf('.3'),0]])
    Z=mp.matrix([[0,0,0],[mp.mpf('-.2'),0,0],[mp.mpf('.1'),mp.mpf('.4'),0]])
    Y=mp.matrix([[mp.mpf('.1'),mp.mpf('-.2')],[mp.mpf('.15'),mp.mpf('.1')],[mp.mpf('-.05'),mp.mpf('.12')]])
    V=mp.matrix(5)
    V[:2,:2],V[2:,:2],V[2:,2:]=X,Y,Z
    I=mp.eye(5)
    cayley=(I-V)*(I+V)**-1
    P=(cayley+cayley.T)/w
    defect=I-V.T*V
    congruence=defect-w/2*(I+V.T)*P*(I+V)
    Ablock,F,B=P[:2,:2],P[2:,2:],P[2:,:2]
    def invsqrt(a):
        es,vs=mp.eigsy(a)
        assert min(es)>0
        return vs*mp.diag([1/mp.sqrt(t) for t in es])*vs.T
    cc=invsqrt(F)*B*invsqrt(Ablock)
    dc=invsqrt(mp.eye(3)-Z*Z.T)*Y*invsqrt(mp.eye(2)-X.T*X)
    cayley_c=mp.sqrt(mp.eigsy(cc.T*cc,eigvals_only=True)[-1,0])
    storage_c=mp.sqrt(mp.eigsy(dc.T*dc,eigvals_only=True)[-1,0])
    algebra_error=max(abs(x) for x in congruence)
    coupling_error=abs(cayley_c-storage_c)
    assert algebra_error<mp.mpf('1e-60') and coupling_error<mp.mpf('1e-60')
    data={'scope':'Independent numerical checks, not an all-operator certificate.',
          'beta_kernel_profile_max_abs_difference':mp.nstr(max(kernel_errors),12),
          'full_scalar_norm_moments_vs_quadrature_abs_difference':mp.nstr(norm_error,12),
          'full_scalar_norm_squared_constant_input_log3_quarter_shift':mp.nstr(quad_norm,35),
          'cayley_defect_congruence_max_abs_residual':mp.nstr(algebra_error,12),
          'storage_vs_cayley_relative_coupling_abs_difference':mp.nstr(coupling_error,12),
          'mpmath_digits':mp.mp.dps,'arb_bits':ctx.prec,'all_checks_pass':True}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__':
    run()
