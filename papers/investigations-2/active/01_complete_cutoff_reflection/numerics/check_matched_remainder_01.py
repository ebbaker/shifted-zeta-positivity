#!/usr/bin/env python3
"""Bounded complete A+B-C error-floor screen for the matched 01/18 pilot.
Prepared for Edward Baker with substantial LLM assistance, gpt-6-astra, ultra.
The retained Polymath theorem and source proofs are imported, not formalized.
"""
import argparse, hashlib, json, math, platform, time
from pathlib import Path
from flint import arb, acb, acb_series, ctx

ROOT = Path.cwd()
BASELINE_SHA256 = 'e98a91f7c3abe8e8e9302ca3cf4c372329ec84d8668a5777eaf68bf86e0a0e47'
SOURCE_NOTES = [
'papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/20_EXPLICIT_THETA_CORRECTION_AND_CORRELATED_PHYSICAL_JETS_20261011.md',
'papers/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/22_THETA_CUTOFF_MATCHING_AND_UNIFORM_PHYSICAL_JETS_20261011.md',
'papers/investigations-2/active/01_complete_cutoff_reflection/notes/COMPLETE_REFLECTED_BLOCK_AND_ENDPOINT_OBSTRUCTION_20261013.md',
]
def pack(x):
    return {'ball':x.str(70), 'diagnostic_midpoint_binary64':float(x.mid())}
def upper(x):return x.upper()
def maxabs(a,b):return a.abs_upper().max(b.abs_upper())
def pad(x,e):return x+arb(0,e.abs_upper())
def m0(s):
    pi=arb.pi()
    return s*(s-1)/16 * ((-s/2)*pi.log()).exp() * (2*pi).sqrt() * ((s/2-arb(1)/2)*(s/2).log()-s/2).exp()
def alpha(s):return 1/(2*s)+1/(s-1)+(s/(2*arb.pi())).log()/2

def physical_model(x,t,N):
    # x is an interval of REAL centers; the formal variable supplies physical x jets.
    s=acb_series([acb(arb(1)/2,x/2),acb(0,arb(1)/2)],4)
    al=alpha(s)
    mt=m0(s)*(t*al*al/4).exp()
    wave=acb_series([0],4)
    for n in range(1,N+1):
        ln=arb(n).log()
        wave+= (t*ln*ln/4-(s+t*al/2)*ln).exp()
    gs=mt*wave
    A=abs(mt[0])
    assert A>0
    gj=[2*gs[j].real*math.factorial(j)/A for j in range(4)]
    pi=arb.pi(); tau=x/2+pi*t/8; a=(tau/(2*pi)).sqrt();p=1-2*(a-N)
    phase=pi*(p*p/2+arb(3)/8)
    den=2*(pi*p).cos()
    assert not den.contains(0) # selected cells avoid the removable profile points
    u=phase.cos()/den
    v=(phase.sin()-arb(2).sqrt()*(pi*p/2).cos())/den
    C=(-1)**(N+1)*pi.sqrt()/4 * (-pi*x/8-t*pi*pi/64).exp()*tau**arb('1.5')*(u-v/tau)
    return A,gj,C/A,p

def ledger(x,t,r,N):
    pi=arb.pi(); xm=x.lower()-r;xp=x.upper()+r
    assert xm>=200 and 0<t<=arb('0.5') and 0<r<=1
    natlo=xm/(4*pi)+t/16;nathi=xp/(4*pi)+t/16
    assert natlo>=N*N and nathi<(N+1)**2
    qm=xm/(4*pi);qp=xp/(4*pi);V=xm/2
    S=(xp*xp+(1+r)**2).sqrt()/2
    amin=qm.log()/2-1/(V*V)
    astar=3/(2*V)+((S/(2*pi)).log()**2+pi*pi/4).sqrt()/2
    dstar=3/(2*V*V)+1/(2*V)
    K=(r*astar*(1+t*dstar/2)/2).exp()
    kap=t*r/(2*(xm-6));EAB=arb(0)
    for n in range(1,N+1):
        ln=arb(n).log()
        vn=(-ln/2+t*(ln*ln/4-amin*ln/2)).exp()
        ell=maxabs((qm/(n*n)).log(),(qp/(n*n)).log())
        un=((t*t*ell*ell/16+arb('.626'))/(xm-arb('6.66'))).exp()-1
        EAB+=(1+(kap*arb(N).log()+r*ln).exp())*vn*un
    Z=(-qm.log()/4-t*qm.log()**2/16+(3*(qp.log()**2+pi*pi/4).sqrt()+arb('3.58'))/(xm-arb('8.52'))).exp()
    BC=arb('1.24')*((r*arb(3).log()).exp()+(-r*arb(3).log()).exp())/(N-arb('.125'))+arb('6.92')/(xm-12)
    taulo=xm/2+pi*t/8; tauhi=xp/2+pi*t/8;alo=(taulo/(2*pi)).sqrt();ahi=(tauhi/(2*pi)).sqrt()
    pbox=(1-2*(alo-N)).union(1-2*(ahi-N))
    assert pbox.abs_upper()<arb('1.01')
    # Uniform profile constants from Note20 section1.1, all natural phases.
    J=3/taulo+1/(taulo*taulo)+(17+17/taulo)/(4*pi*alo)
    W=(tauhi/taulo)**arb('1.5')
    source=K*(EAB+Z*BC); surrogate=K*Z*2*r*W*J
    eta=source+surrogate
    err=[math.factorial(j)*eta/r**j for j in range(4)]
    return eta,err,{'r':pack(r),'expanded_x_range':[pack(xm),pack(xp)],'natural_cutoff_squared':[pack(natlo),pack(nathi)],
      'profile_p_range':pack(pbox),'K':pack(K),'E_AB':pack(EAB),'Z':pack(Z),'B_C':pack(BC),
      'J_all':pack(J),'source_error':pack(source),'surrogate_error':pack(surrogate),'eta':pack(eta)}

def rational(text):
    from fractions import Fraction
    q=Fraction(text)
    return arb(q.numerator)/q.denominator

def retained_ball(item):
    lo=item['lower_dyadic'];hi=item['upper_dyadic']
    return (arb(int(lo['mantissa']))*arb(2)**lo['exponent']).union(arb(int(hi['mantissa']))*arb(2)**hi['exponent'])

def run(baseline_path):
    ctx.prec=256;ctx.cap=4
    start=time.perf_counter();t=arb(1)/20
    if hashlib.sha256(baseline_path.read_bytes()).hexdigest()!=BASELINE_SHA256:
        raise RuntimeError('Retained shared baseline record hash mismatch')
    baseline=json.loads(baseline_path.read_text())
    assert baseline['status']=='PASS'
    cells=baseline['cells']
    records=[]
    for bc in cells:
        jtarget=bc['j'];name='j'+str(jtarget)
        assert bc['unique_stationary_root'] and bc['t']=='1/20'
        x=rational(bc['stationary_root_bracket'][0]).union(rational(bc['stationary_root_bracket'][1]))
        initial=rational(bc['initial_x_cell'][0]).union(rational(bc['initial_x_cell'][1]))
        A,g,c,p=physical_model(x,t,4); k=arb.pi()/8
        truth=retained_ball(bc['conditional_laguerre'])
        actual_jets=[retained_ball(v)/A for v in bc['stationary_jets']]
        measured_residuals=[actual_jets[j]-(g[j]-c*(-k)**j) for j in range(4)]
        qmax=initial.upper()/(4*arb.pi())
        eta_floor=(-qmax.log()/4-t*qmax.log()**2/16).exp()*(arb('2.48')/(4-arb('.125'))+arb('6.92')/(initial.upper()-12))
        d=-k
        lower_center=g[jtarget]-g[jtarget+1]/d
        upper_center=g[jtarget+2]-d*g[jtarget+1]
        lower_error_floor=(math.factorial(jtarget)+math.factorial(jtarget+1)/k)*eta_floor
        upper_error_floor=(math.factorial(jtarget+2)+k*math.factorial(jtarget+1))*eta_floor
        all_radius_failure=bool(lower_center.abs_upper()<lower_error_floor and upper_center.abs_upper()<upper_error_floor)
        floor_record={'eta_lower_bound_for_all_0_lt_r_le_1':pack(eta_floor),
            'conditional_lower_jet_error_allowance_floor':pack(lower_error_floor),
            'conditional_upper_jet_error_allowance_floor':pack(upper_error_floor),
            'conditional_finite_lower_jet':pack(lower_center),'conditional_finite_upper_jet':pack(upper_center),
            'both_conditional_jet_boxes_contain_zero_for_every_allowed_radius':all_radius_failure,
            'meaning':'Lower bound on this theorem error ALLOWANCE, not on the true approximation error.'}
        if jtarget==1: assert all_radius_failure
        attempts=[]
        for rs in ['.25','.5','.75','1']:
            r=arb(rs);eta,err,led=ledger(x,t,r,4)
            raw=[pad(g[j]-c*(-k)**j,err[j]) for j in range(4)]
            # At physical stationarity h_{j+1}=0, eliminate the entire leading
            # correction amplitude, retaining BOTH analytic residual payments.
            d=-k; jj=jtarget
            lower=pad(g[jj]-g[jj+1]/d,err[jj]+err[jj+1]/abs(d))
            upperjet=pad(g[jj+2]-d*g[jj+1],err[jj+2]+abs(d)*err[jj+1])
            sign=-lower*upperjet
            separate=-raw[jj]*raw[jj+2]
            attempts.append({'ledger':led,'physical_errors_over_A':[pack(e) for e in err],
              'paid_physical_jets_over_A':[pack(v) for v in raw],
              'separate_stationary_product_over_A_squared':pack(separate),
              'leading_correction_eliminated':{'conditional_lower_jet':pack(lower),'conditional_upper_jet':pack(upperjet),
                 'stationary_sign_over_A_squared':pack(sign),'strict_sign_proved':bool(sign>0)},
              'complete_first_jet_excluded':bool(not raw[0].contains(0) or not raw[1].contains(0)),
              'arithmetic_width_target_1e_minus40_met':all((A*e)<arb('5e-41') for e in err)})
        records.append({'target':name,'stationary_derivative_order':jtarget+1,'time':'1/20','initial_x_cell':bc['initial_x_cell'],'baseline_stationary_bracket':bc['stationary_root_bracket'],'x_interval':pack(x),
          'baseline_reconstructed_residuals_over_A':[pack(v) for v in measured_residuals],
          'residual_scope':'Computed by subtracting the finite model from the complete direct-source baseline; this is not an independent signed remainder certificate.',
          'baseline_laguerre':bc['conditional_laguerre'],'baseline_laguerre_over_A_squared':pack(truth/A**2),
          'all_radius_allowance_floor':floor_record,
          'A_positive':pack(A),'finite_physical_G_jets_over_A':[pack(v) for v in g],
          'C_over_A':pack(c),'profile_p':pack(p),'attempts':attempts})
    return {'date':'2026-10-14','prepared_for':'Edward Baker','model':'gpt-6-astra','reasoning_effort':'ultra',
       'acknowledgment':'Substantial LLM assistance; internal bounded research, not independent validation.',
       'status':'COMPLETE_ERROR_FLOOR_SCREEN','precision_bits':ctx.prec,'runtime_seconds':time.perf_counter()-start,
       'source': 'Polymath Corollary6.4/Proposition6.6 via retained Notes20/22; entire physical A+B-C bound, not a newly derived signed Mordell estimate.',
       'normalization':'A_t(X)=abs(M_t((1+iX)/2)) at each real center, held fixed when taking physical derivatives.',
       'work_counters':{'finite_source_terms_per_cell':4,'cell_count':2,'ledger_radii_per_cell':4,'source_quadrature_evaluations':0,
          'primitive_ball_operations':'not instrumented; no claim of operation-count timing equivalence'},
       'records':records,'source_hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in SOURCE_NOTES},
       'baseline_record_sha256':hashlib.sha256(baseline_path.read_bytes()).hexdigest(),
       'baseline_checker_sha256':baseline['checker_sha256'],
       'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'python_version':platform.python_version(),
       'limitations':['Published source theorem imported, not formally verified.',
       'Interval arithmetic encloses all center values and all complete source/Cauchy errors; primitive operation counts are not benchmarked.',
       'The r<=1 Cauchy theorem does not license a larger optimization disk.',
       'No exact signed contour remainder has been bounded independently here.',
       'Failed sign separation is failure of this retained estimate, not a negative stationary value of genuine theta.']}
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--record',type=Path,required=True);ap.add_argument('--baseline-record',type=Path,required=True);args=ap.parse_args()
    result=run(args.baseline_record);args.record.write_text(json.dumps(result,indent=2)+'\n')
    for cell in result['records']:
        print(cell['target'],'A',cell['A_positive']['ball'],'Gjets',[x['diagnostic_midpoint_binary64'] for x in cell['finite_physical_G_jets_over_A']])
        for a in cell['attempts']:
            print('r',a['ledger']['r']['diagnostic_midpoint_binary64'],'eta',a['ledger']['eta']['diagnostic_midpoint_binary64'],
               'errors',[e['diagnostic_midpoint_binary64'] for e in a['physical_errors_over_A']],
               'sign',a['leading_correction_eliminated']['strict_sign_proved'],'firstjet',a['complete_first_jet_excluded'])
    print('seconds',result['runtime_seconds'])
