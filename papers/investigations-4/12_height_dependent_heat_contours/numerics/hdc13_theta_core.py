"""Complete canonical theta heat oracle on the physical pilot box.

Prepared for Edward Baker, 2026-10-23. Substantial LLM assistance:
gpt-6-astra (Codex), reasoning effort ultra. Requires python-flint 0.9.
This is a physical-cell range oracle, NOT an analytic integration callback.
No root location, simplicity, discriminant, RH, or zero-count premise is used.
"""
from math import factorial
from time import perf_counter
from flint import arb, acb, acb_series, ctx


def canonical_h0(z):
    s=acb(arb(1)/2)+acb(0,arb(1)/2)*acb(z)
    return s*(s-1)/16*(-s/2*arb.pi().log()).exp()*(s/2).gamma()*s.zeta()


def rec(v):
    return v.str(32,more=True)


class ActualHeatCore:
    """Range over z-cell intersected with |z-36|<=11, |Im z|<=2.

    Default time cell contains the exact square [-1e-4,1e-4]^2. All
    source errors are paid on the larger disk |tau|<=1/5000, avoiding
    reliance on exact endpoint representation of interval radii.
    """
    def __init__(self,bits=192,terms=96,heat_terms=6,cell_order=6,max_jet=3):
        ctx.prec=int(bits); self.bits=int(bits); self.N=int(terms)
        self.A=int(heat_terms);self.J=int(cell_order);self.max_jet=int(max_jet)
        self.center=arb(36);self.radius=arb(11);self.collar=arb(12);self.R=arb(24)
        self.T=arb(1)/5000;self.time_radius=self.T
        self.tau=acb(arb(0,arb(1)/10000),arb(0,arb(1)/10000))
        assert self.tau.abs_upper()<self.time_radius
        self.counts={'cell_jet_calls':0,'point_jet_calls':0}
        start=perf_counter();old_cap=ctx.cap;ctx.cap=self.N
        try:
            s=acb_series([acb(arb(1)/2,self.center/2),acb(0,arb(1)/2)])
            h=s*(s-1)/16*(-s/2*arb.pi().log()).exp()*(s/2).gamma()*s.zeta()
            assert all(h[k].is_finite() and h[k].imag.contains(0) for k in range(self.N))
            self.coeff=[h[k].real for k in range(self.N)]
        finally:ctx.cap=old_cap
        m=canonical_h0(acb(0,self.R)); low=canonical_h0(acb(0,2))
        assert m.is_finite() and m.real>0 and m.imag.contains(0)
        assert low.is_finite() and low.real>0 and low.imag.contains(0)
        self.cauchy_majorant=m.real.abs_upper();self.low_source=low.real.abs_upper()
        self.spatial_tail=(2*self.cauchy_majorant/arb(2)**self.N).abs_upper()
        self.Cphi=2*arb.pi()**2/(1-16*(-3*arb.pi()).exp())
        assert 16*(-3*arb.pi()).exp()<1
        self.max_order=2*(self.A-1)+self.J+self.max_jet
        self.factorials=[factorial(j) for j in range(self.max_order+2*self.A+4)]
        self.bounds=[]
        for j in range(self.max_order+1):
            self.bounds.append(sum((abs(self.coeff[l])*(factorial(l)//factorial(l-j))*self.radius**(l-j)
                for l in range(j,self.N)),arb(0)).abs_upper())
        self.errors=[]; self.moments=[]
        for j in range(self.max_jet+1):
            moment=self.moment(2*self.A+j);self.moments.append(moment)
            spatial=self.spatial_tail*sum((self.time_radius**k*factorial(j+2*k)/factorial(k)
                for k in range(self.A)),arb(0))
            heat=self.time_radius**self.A*moment/factorial(self.A)
            self.errors.append((spatial+heat).abs_upper())
        self.setup_seconds=perf_counter()-start

    def moment(self,j):
        # [0,1]: u^j e^(T u²) cosh(2u) <= e^T cosh(2u).
        # [1,infty): u^j<=e^(ju), Phi<=Cphi exp(9u-pi exp4u).
        # T u²+(11+j)u <= B exp2u, then complete the square.
        pi=arb.pi();B=self.T/arb(2).exp()+(11+j)/(2*arb(1).exp())
        x=pi*arb(4).exp()/2
        tail=self.Cphi/4*(B*B/(2*pi)-x).exp()/x
        return (self.T.exp()*self.low_source+tail).abs_upper()

    def _normalized_poly_jets(self,x,order):
        # Exact derivative/factorial recurrence for the finite spatial polynomial.
        v=[acb(0) for _ in range(order+1)]
        for c in reversed(self.coeff):
            for j in range(order,0,-1):v[j]=v[j]*x+v[j-1]
            v[0]=v[0]*x+c
        return v

    def polynomial_coefficients(self,tau,derivative=0):
        """Ascending centered coefficients of finite analytic G_tau^(derivative)."""
        tau=acb(tau)
        if not hasattr(self,'_poly_cache'):self._poly_cache={}
        key=tuple(str(v) for x in (tau.real,tau.imag) for v in (x.mid().fmpq(),x.rad().fmpq()))+(int(derivative),)
        if key not in self._poly_cache:
            d=int(derivative); out=[]
            for m in range(self.N-d):
                out.append(sum((self.coeff[m+d+2*k]*(factorial(m+d+2*k)//factorial(m))
                    *((-tau)**k)/factorial(k)
                    for k in range(min(self.A,(self.N-1-m-d)//2+1))),acb(0)))
            self._poly_cache[key]=out
        return self._poly_cache[key]

    def evaluate_poly(self,z,tau,derivative=0):
        """Globally analytic finite polynomial only; suitable integration callback."""
        v=acb(0);x=acb(z)-self.center
        for c in reversed(self.polynomial_coefficients(tau,derivative)):v=v*x+c
        return v

    def point_jets(self,z,max_order=0,tau=None,start_heat=0):
        """Finite heat polynomial derivatives only; no source tail added."""
        tau=self.tau if tau is None else acb(tau)
        assert tau.abs_upper()<=self.time_radius
        self.counts['point_jet_calls']+=1
        v=self._normalized_poly_jets(acb(z)-self.center,max_order+2*(self.A-1))
        powers=[(-tau)**k/factorial(k) for k in range(self.A)]
        return [sum((powers[k]*factorial(j+2*k)*v[j+2*k] for k in range(start_heat,self.A)),acb(0))
            for j in range(max_order+1)]

    def jets(self,z,max_order=1,tau=None,difference=False):
        """Complete H_tau derivatives on the physical portion of z-cell.

        The z rectangle itself must lie in |z-36|<=11, |Im z|<=2.
        Inputs are outward interval supersets; requested exact cells are
        intersections with these stated physical bounds if radii round out.
        """
        if not 0<=max_order<=self.max_jet:raise ValueError('jet order exceeds source budget')
        tau=self.tau if tau is None else acb(tau);z=acb(z)
        assert tau.abs_upper()<=self.time_radius and z.is_finite()
        x=z-self.center
        assert x.abs_upper()<=self.radius
        mid=acb(z.real.mid(),z.imag.mid());delta=z-mid;rho=delta.abs_upper()
        assert abs(mid.imag)<=2
        self.counts['cell_jet_calls']+=1
        start_heat=1 if difference else 0
        pv=self.point_jets(mid,max_order+self.J-1,tau,start_heat=start_heat)
        result=[]
        for j in range(max_order+1):
            value=sum((pv[j+l]*delta**l/factorial(l) for l in range(self.J)),acb(0))
            bound=sum((self.time_radius**k*self.bounds[j+self.J+2*k]/factorial(k)
                for k in range(start_heat,self.A)),arb(0))
            source_error=2*self.errors[j] if difference else self.errors[j]
            err=(rho**self.J*bound/factorial(self.J)+source_error).abs_upper()
            result.append(acb(value.real+arb(0,err),value.imag+arb(0,err)))
        return result

    def cell(self,z,derivative=0,tau=None):
        return self.jets(z,derivative,tau)[derivative]

    def difference_cell(self,z,derivative=0,tau=None):
        """Complete H_tau-H_0, preserving cancellation before interval evaluation."""
        return self.jets(z,derivative,tau,difference=True)[derivative]

    def metadata(self):
        return {'bits':self.bits,'spatial_terms':self.N,'heat_terms':self.A,'cell_order':self.J,
          'center':36,'physical_radius':11,'physical_imaginary_bound':2,'cauchy_radius':24,'collar_radius':12,
          'source_time_disk_radius':'1/5000','target_time_square':['-1/10000','1/10000'],
          'source_Cphi':rec(self.Cphi),'cauchy_majorant_H0_i24':rec(self.cauchy_majorant),
          'low_source_H0_i2':rec(self.low_source),'spatial_collar_remainder':rec(self.spatial_tail),
          'moment_bounds':[rec(x) for x in self.moments],
          'uniform_source_errors':[rec(x) for x in self.errors],
          'setup_seconds':self.setup_seconds,'counts':self.counts}
