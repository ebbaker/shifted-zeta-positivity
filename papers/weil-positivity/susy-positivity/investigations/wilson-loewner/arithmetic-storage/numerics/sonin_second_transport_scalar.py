#!/usr/bin/env python3
"""Certified B_infinity[D2**2 F] for the two exact A17 sources.

Prepared for Edward Baker with GPT-6 (Codex), 29 September 2026.
Exact serving variant and effort not exposed. Extends the existing audited
gamma/epsilon methods to one extra transport factor; it is NOT Tr(AH).
Requires python-flint 0.9.0 and the existing arithmetic-storage numerics.
"""
import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from fractions import Fraction as Q
from flint import arb, acb, arb_poly, fmpz_poly, ctx


def require(test, message):
    if not test:
        raise ArithmeticError(message)


def rat(q):
    q=Q(q)
    return arb(q.numerator)/q.denominator


def pack(v):
    require(v.is_finite(), 'Nonfinite enclosure')
    return {'display':v.str(25), 'rational_lower':str(v.lower().fmpq()),
            'rational_upper':str(v.upper().fmpq())}


def inflate(v,e):
    return v+arb(0,e.abs_upper())


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def gamma(source, record, bits=128):
    ctx.prec=bits
    count=2**18
    period=rat(48)
    dx=period/count
    dt=2*arb.pi()/period
    max_n=int((rat(5000)/dt).floor().unique_fmpz())
    cutoff=max_n*dt
    omega=2*arb.pi()/dx
    require(omega>2*cutoff and max_n<count//2,'Invalid alias separation')
    norms=[source.record_ball(row['normalizer']) for row in record['sources']]
    max_j=int((rat('9/20')/dx).floor().unique_fmpz())
    values=[acb(0)]*count
    for j in range(-max_j,max_j+1):
        x=j*dx
        values[j%count]=acb(source.source_value(0,x,normalizer=norms[0]),
                           source.source_value(1,x,normalizer=norms[1]))
    transformed=acb.dft(values)
    del values
    a4=[source.record_ball(row['normalized_derivative_L1_cauchy_bounds'][4]) for row in record['sources']]
    alias=[v*arb.pi()**4/(45*(omega-cutoff)**4) for v in a4]
    accum=[arb(0),arb(0)]
    log2=arb(2).log()
    root2=arb(2).sqrt()
    logpi=arb.pi().log()
    for n in range(max_n+1):
        t=n*dt
        positive=transformed[n]
        negconj=transformed[-n%count].conjugate()
        f0=(positive+negconj)/2
        f1=(positive-negconj)/acb(0,2)
        require(f0.imag.contains(0) and f1.real.contains(0),'Parity lost')
        g=acb(rat('1/4'),t/2).digamma().real-logpi
        transport=rat('3/2')-root2*(t*log2).cos()
        require(transport>0,'Nonpositive transport multiplier')
        factor=(1 if n==0 else 2)/period
        for sid,f in enumerate((f0.real,f1.imag)):
            fv=inflate(dx*f,alias[sid])
            accum[sid]+=factor*g*(transport*transport)*(fv*fv)
            require(accum[sid].is_finite(), 'Nonfinite Fourier sum at source '+str(sid)+' node '+str(n)+' source value '+str(fv))
    del transformed
    u=1+1/root2
    width=rat('9/10')+2*log2
    result=[]
    for sid,row in enumerate(record['sources']):
        l1=u**2*source.record_ball(row['normalized_L1'])
        tail=(u**2*a4[sid])**2/arb.pi()*cutoff**(-7)/7*(6+rat('29/25').log()/2+cutoff.log()+rat('1/7'))
        quadrature=2*l1**2*((width-period)/2).exp()/((1-(-period/2).exp())*(1-(-2*(period-width)).exp()))
        value=inflate(accum[sid],tail+quadrature)
        require(2*value.rad()<rat('1e-4'),'Gamma target missed: '+str(value))
        result.append({'source':sid,'Gamma_D2_squared_F':pack(value),
                       'frequency_tail_bound':pack(tail),'frequency_alias_bound':pack(quadrature),
                       'source_alias_per_value':pack(alias[sid])})
        print(json.dumps({'stage':'gamma','source':sid,'value':str(value)}),flush=True)
    return result


def epsilon(source,prolate,base,record,N,K,bits):
    ctx.prec=bits
    h=arb(2).log()/N
    r=1/arb(2).sqrt()
    radius=math.ceil(float(source.B)/float(h))+1
    require(radius*h>source.ball(source.B),'Source support missed')
    tmax=(2*radius+2*N+2)*h
    terms,kernel_error,eps_sup,_,_=base.exponential_model(prolate,K,bits,tmax.exp())
    require(kernel_error<rat('1e-20'),'Kernel approximation inadequate')
    scale=2**80
    rows=[]
    for sid,row in enumerate(record['sources']):
        normalizer=source.record_ball(row['normalizer'])
        l1=source.record_ball(row['normalized_L1'])
        l1d2=source.record_ball(row['normalized_derivative_L1_cauchy_bounds'][2])
        values=[]
        rounding=arb(0)
        for j in range(-radius,radius+1):
            v,e=base.quantize(source.source_value(sid,j*h,normalizer=normalizer),scale)
            values.append(v)
            rounding=rounding.max(e)
        require(values[0]==values[-1]==0,'Nonzero source exterior')
        eta=h*h*l1d2/8+(2*radius+2)*h*rounding
        product=(fmpz_poly(values)*fmpz_poly(values[::-1])).coeffs()
        mid=len(values)-1
        aa=[int(product[mid+j]) if mid+j<len(product) else 0 for j in range(mid+1)]
        def ac(j):
            return aa[abs(j)] if abs(j)<len(aa) else 0
        # |1-r exp(-ita)|^4 = 13/4 - 3r(U_a+U_-a) + (U_2a+U_-2a)/2.
        coeff=[rat('13/4')*ac(j)-3*r*(ac(j-N)+ac(j+N))
               +rat('1/2')*(ac(j-2*N)+ac(j+2*N)) for j in range(len(aa)+2*N)]
        poly=arb_poly(coeff)
        value=sum((c*base.integrate_exponential_correlation(poly,coeff[0],coeff[1],h,lam,scale)
                   for lam,c in terms),arb(0))
        source_error=eps_sup*(1+r)**4*eta*(2*l1+eta)
        operator_error=kernel_error*(1+r)**4*(l1+eta)**2
        value=inflate(value,source_error+operator_error)
        rows.append({'source':sid,'E_D2_squared_F':pack(value),
                     'source_L1_error':pack(eta),'source_integral_error':pack(source_error),
                     'kernel_integral_error':pack(operator_error),
                     'coefficient_sha256':hashlib.sha256(json.dumps(values,separators=(',',':')).encode()).hexdigest()})
        print(json.dumps({'stage':'epsilon','source':sid,'value':str(value),'error':str(source_error)}),flush=True)
    return rows,{'grid_N':N,'precision_bits':bits,'cosine_terms':K,
                 'rho_max':pack(tmax.exp()),'uniform_kernel_error':pack(kernel_error)}


def unpack(obj):
    lo,hi=rat(obj['rational_lower']),rat(obj['rational_upper'])
    return arb((lo+hi)/2,((hi-lo)/2).abs_upper())


def run(args):
    sys.path.insert(0,str(args.numerics))
    import source_norm_enclosures as source
    import prolate_certificate as prolate
    import sonin_scalar_epsilon as base
    record_path=args.numerics/'records/source_norm_enclosures.json'
    record=json.loads(record_path.read_text())
    require(record['script_sha256']==digest(args.numerics/'source_norm_enclosures.py'),'Source provenance mismatch')
    grows=gamma(source,record)
    erows,parameters=epsilon(source,prolate,base,record,args.grid,args.cosine_terms,args.precision_bits)
    rows=[]
    for g,e in zip(grows,erows):
        require(g['source']==e['source'],'Source mismatch')
        h2=unpack(g['Gamma_D2_squared_F'])+unpack(e['E_D2_squared_F'])
        require(h2>0,'Positive trace not resolved')
        require(2*h2.rad()<rat(args.max_width),'Trace accuracy target missed')
        rows.append({**g,**e,'h2_B_infinity_D2_squared_F':pack(h2)})
    return {'status':'CERTIFIED','date':'2026-09-29','model':'GPT-6 (Codex)',
            'serving_variant':'not exposed','reasoning_effort':'not exposed',
            'scope':'Real-place trace B_infinity[D2**2 F]; NOT the compressed first moment or arithmetic residual.',
            'parameters':parameters,'gamma_parameters':{'fft_power':18,'period':48,'frequency_cutoff':5000,'bits':128},
            'script_sha256':digest(Path(__file__)),
            'dependency_sha256':{name:digest(args.numerics/name) for name in
              ['source_norm_enclosures.py','prolate_certificate.py','sonin_scalar_epsilon.py','records/source_norm_enclosures.json']},
            'sources':rows}


if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--numerics',type=Path,default=Path(__file__).resolve().parent)
    p.add_argument('--grid',type=int,default=65536)
    p.add_argument('--cosine-terms',type=int,default=144)
    p.add_argument('--precision-bits',type=int,default=768)
    p.add_argument('--max-width',default='0.001')
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    require(args.grid>512 and args.cosine_terms>=128 and args.precision_bits>=640,'Insufficient parameters')
    result=run(args)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':result['status'],'traces':[x['h2_B_infinity_D2_squared_F']['display'] for x in result['sources']]}),flush=True)
