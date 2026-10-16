#!/usr/bin/env python3
"""Bounded actual-orbit numerical pilot; not interval arithmetic or a proof.

Requires NumPy; Decimal is used to protect the large common-height phases.
No counting-error constant is chosen. Gamma is retained symbolically as
Gamma0 + density_coefficient/(4*C_count+1)**2. Outputs are small records.
"""
import argparse
from decimal import Decimal as D, localcontext, ROUND_HALF_EVEN
from pathlib import Path
import hashlib
import json
import math
import time
import numpy as np


def decimal_pi():
    def atan(z):
        total = D(0)
        power = z
        for k in range(130):
            total += (-1 if k % 2 else 1)*power/D(2*k+1)
            power *= z*z
        return total
    return 16*atan(D(1)/5)-4*atan(D(1)/239)


def decimal_trig(angle, pi):
    period = 2*pi
    angle -= (angle/period).to_integral_value(rounding=ROUND_HALF_EVEN)*period
    square = angle*angle
    st, ct = angle, D(1)
    sn, cs = st, ct
    for k in range(1, 36):
        st *= -square/D((2*k)*(2*k+1))
        ct *= -square/D((2*k-1)*(2*k))
        sn += st
        cs += ct
    return cs, sn


def decimal_center(M, h, precision):
    """Scalar exact formulas evaluated at finite Decimal precision."""
    with localcontext() as ctx:
        ctx.prec = precision
        pi = decimal_pi()
        lm = D(M).ln()
        t = 1/(2*lm)
        x0 = 4*pi*M*M
        x = x0+D(str(h))
        L = (x/(4*pi)).ln()
        lc = (1+1/(x*x)).ln()
        # Reciprocal arctangent is tiny; four terms are ample here.
        y = 1/x
        atanx = pi/2-(y-y**3/3+y**5/5-y**7/7)
        ar = L/2+lc/4-1/(1+x*x)
        ai = 3*x/(1+x*x)-atanx/2
        U = (7*x*x-5)/(1+x*x)**2
        V = x*(x*x+5)/(1+x*x)**2
        c = (1+t*U/2)/2
        Omega = (ar*(1+t*U/2)-ai*t*V/2)/2
        mu = Omega/c
        aN = D('0.5')+t*ar/2-t*lm/2
        T = (x-t*ai)/2
        wN = (t*lm*lm/4-(D('0.5')+t*ar/2)*lm).exp()
        # Remove the exact integer pi*M**2 before reducing the phase.
        carrier = pi*(M % 2)-pi+atanx/4+D(str(h))/4 \
            -x*(x/x0).ln()/4-x*lc/8+t*ai*(ar-lm)/2
        return {'pi': pi, 'logM': lm, 't': t, 'x0': x0, 'x': x,
                'L': L, 'ar': ar, 'ai': ai, 'c': c, 'mu': mu,
                'aN': aN, 'T': T, 'wN': wN, 'carrier': carrier}


def decimal_complete(M, h, precision, return_array=False):
    """All summands, common physical height; optional complete moments 0..6."""
    with localcontext() as ctx:
        ctx.prec = precision
        data = decimal_center(M, h, precision)
        qr = np.empty(M) if return_array else None
        qi = np.empty(M) if return_array else None
        logs = np.empty(M) if return_array else None
        moments = [[D(0), D(0)] for _ in range(7)]
        for n in range(1, M+1):
            ell = D(n).ln()
            delta = data['logM']-ell
            amp = data['wN']*(data['aN']*delta+data['t']*delta*delta/4).exp()
            cs, sn = decimal_trig(data['carrier']-data['T']*delta, data['pi'])
            real, imag = amp*cs, amp*sn
            if return_array:
                qr[n-1], qi[n-1], logs[n-1] = float(real), float(imag), float(ell)
            else:
                rho = ell-data['mu']
                power = D(1)
                for pair in moments:
                    pair[0] += power*real
                    pair[1] += power*imag
                    power *= rho
        if return_array:
            return qr+1j*qi, logs
        return [complex(float(a), float(b)) for a,b in moments]


def physical_data(M, h):
    lm = math.log(M)
    t = 1/(2*lm)
    x0 = 4*math.pi*M*M
    x = x0+h
    L = 2*lm+math.log1p(h/x0)
    ar = L/2+math.log1p(1/(x*x))/4-1/(1+x*x)
    ai = 3*x/(1+x*x)-math.atan(x)/2
    s = complex(.5,-x/2)
    alpha = complex(ar,ai)
    ad = [alpha]
    for k in range(1,5):
        ad.append((-1)**k*math.factorial(k)/(2*s**(k+1))
                  +(-1)**k*math.factorial(k)/(s-1)**(k+1)
                  +.5*(-1)**(k-1)*math.factorial(k-1)/s**k)
    c, d = .5+t*ad[1].real/4, t*ad[1].imag/4
    Omega = (alpha*(1+t*ad[1]/2)).real/2
    mu = Omega/c
    dk, ck, ok = [],[],[]
    for k in range(4):
        ax = (-.5j)**k*ad[k+1]
        dk.append(t*ax.imag/4)
        ck.append((.5 if k==0 else 0)+t*ax.real/4)
        fs = ad[k]+t/2*sum(math.comb(k,j)*ad[j]*ad[k+1-j] for j in range(k+1))
        ok.append(((-.5j)**k*fs).real/2)
    logA2 = -.25*(ad[1]+t/2*(ad[1]**2+alpha*ad[2])).real
    gamma0 = 18*logA2+9/x**2
    Gamma0 = gamma0/c**2
    density = 9*math.log(x)/(2*(8*math.pi)**2*c**2)
    eta = 5*math.exp(-t*L*L/16-L/4)
    return dict(M=M,h=h,t=t,x0=x0,x=x,L=L,c=c,d=d,mu=mu,ar=ar,ai=ai,
                dk=dk,ck=ck,ok=ok,eta=eta,Gamma0=Gamma0,density=density,
                gamma0=gamma0,A=-d*mu,epsilon=d/c)


def transported_q(q0, logs, data):
    """Stable physical q(x0+h)/q(x0), retaining carrier and weight motion."""
    x0, x, h, t = data['x0'],data['x'],data['h'],data['t']
    lc0,lc = math.log1p(1/x0**2),math.log1p(1/x**2)
    dar = .5*math.log1p(h/x0)+(lc-lc0)/4 \
        -(1/(1+x*x)-1/(1+x0*x0))
    da = math.atan(h/(1+x*x0))
    dai = 3*h*(1-x*x0)/((1+x*x)*(1+x0*x0))-.5*da
    arml0 = lc0/4-1/(1+x0*x0)
    arml = arml0+dar
    ai0 = 3*x0/(1+x0*x0)-math.atan(x0)/2
    carrier_delta = h/4-x*math.log1p(h/x0)/4+da/4 \
        -(x*lc-x0*lc0)/8+t/2*((ai0+dai)*arml-ai0*arml0)
    delta = math.log(data['M'])-logs
    phase = carrier_delta-(h/2-t*dai/2)*delta
    return q0*np.exp(-t*dar*logs/2+1j*phase)


def raw_rows(logs, data):
    gamma = [-data['dk'][k]*logs-1j*(data['ok'][k]-data['ck'][k]*logs)
             for k in range(4)]
    v,v1,v2,v3 = gamma
    rows = [np.ones_like(v),v,v*v+v1,v**3+3*v*v1+v2,
            v**4+6*v*v*v1+3*v1*v1+4*v*v2+v3]
    return rows,gamma


def affine_K(m):
    return [2*m[3].imag**2+3*m[2].real*m[4].real,-m[2].real**2]


def affine_J(m, epsilon):
    k = affine_K(m)
    z1 = m[1].imag+epsilon*m[1].real
    return [k[0]+m[0].real*(-3*m[6].real+2*epsilon*m[6].imag)-2*z1*m[5].imag,
            k[1]+m[0].real*m[4].real]


def eval_affine(a, Gamma):
    return a[0]+Gamma*a[1]


def support(A,B):
    return A+B*B/(4*A) if A>0 and B<=2*A else B


def features(q0, logs, M, h):
    data = physical_data(M,h)
    q = transported_q(q0,logs,data)
    rho = logs-data['mu']
    powers = [np.ones_like(logs)]
    for _ in range(6): powers.append(powers[-1]*rho)
    moments = [complex(np.sum(q*p)) for p in powers]
    split = M//2
    mb = [complex(np.sum((q*p)[split:])) for p in powers]
    mc = [complex(np.sum((q*p)[:split])) for p in powers]
    rows, gamma = raw_rows(logs,data)
    raw = [float(2*np.sum(q*p).real) for p in rows]
    S,Sprime = moments[0],complex(np.sum(q*rows[1]))
    current = -(Sprime*S.conjugate()).imag
    DB,DC = complex(np.sum((q*rows[1])[split:])),complex(np.sum((q*rows[1])[:split]))
    JB,JC = -(DB*mb[0].conjugate()).imag,-(DC*mc[0].conjugate()).imag
    crossJ = -(DB*mc[0].conjugate()+DC*mb[0].conjugate()).imag
    c,d,mu,L,eta = (data[k] for k in ('c','d','mu','L','eta'))
    eps = d/c
    leading = [-2*c*c*moments[2].real,2*c**3*moments[3].imag,2*c**4*moments[4].real]
    b = 1j*c*rho
    drift = -d*logs
    v,v1,v2,v3 = gamma
    residual_rows = [2*b*drift+drift**2+v1,
        3*b*b*drift+3*b*drift**2+drift**3+3*v*v1+v2,
        4*b**3*drift+6*b*b*drift**2+4*b*drift**3+drift**4
        +6*v*v*v1+3*v1*v1+4*v*v2+v3]
    E = [float(2*np.sum(np.abs(q)*np.abs(r))) for r in residual_rows]
    residual_check = [abs(raw[j+2]-leading[j]) for j in range(3)]
    K,J = affine_K(moments),affine_J(moments,eps)
    KB,KC = affine_K(mb),affine_K(mc)
    Kcross = [4*mb[3].imag*mc[3].imag+3*(mb[2].real*mc[4].real+mc[2].real*mb[4].real),
              -2*mb[2].real*mc[2].real]
    Jb,Jc = affine_J(mb,eps),affine_J(mc,eps)
    zB,zC = mb[1].imag+eps*mb[1].real,mc[1].imag+eps*mc[1].real
    Jcross = [Kcross[0]-3*(mb[0].real*mc[6].real+mc[0].real*mb[6].real)
              +2*eps*(mb[0].real*mc[6].imag+mc[0].real*mb[6].imag)
              -2*(zB*mc[5].imag+zC*mb[5].imag),
              Kcross[1]+mb[0].real*mc[4].real+mc[0].real*mb[4].real]
    candidate = abs(raw[0])<=eta and abs(raw[1])<=L*eta
    schur = (raw[0]/eta)**2+abs(raw[1])/(L*eta)
    slope = -moments[0].real*moments[4].real
    intercept = moments[0].real*(3*moments[6].real-2*eps*moments[6].imag) \
        +2*(moments[1].imag+eps*moments[1].real)*moments[5].imag
    Acarrier = data['A']
    def payments(Gamma):
        Dcoef = 3*moments[6].real-Gamma*moments[4].real-2*eps*moments[6].imag
        Zbound = (L+abs(Acarrier))*eta/(2*c)
        box = eta/2*abs(Dcoef)+2*Zbound*abs(moments[5].imag)
        slab = eta/2*abs(Dcoef+2*Acarrier/c*moments[5].imag) \
            +L*eta/c*abs(moments[5].imag)
        curved = eta/2*support(2*L*abs(moments[5].imag)/c,
                              abs(Dcoef+2*Acarrier/c*moments[5].imag))
        gam = c*c*Gamma
        ds = [math.factorial(j)*L**j*eta+E[j-2] for j in (2,3,4)]
        g2,g3,g4 = leading;d2,d3,d4=ds
        Delta = 4*abs(g3)*d3+2*d3*d3+3*(abs(g2)*d4+abs(g4)*d2+d2*d4) \
            +abs(gam)*(2*abs(g2)*d2+d2*d2)
        return {'box':box,'slab':slab,'curved':curved,'complete_threshold_payment':Delta/(4*c**6)}
    gamma_range = [data['Gamma0'],data['Gamma0']+data['density']]
    pay = [payments(g) for g in gamma_range]
    abs_diff = [abs(eval_affine(K,g)-eval_affine(J,g)) for g in gamma_range]
    current_box = eta/2*(L*abs(S.imag)+abs(Sprime.imag))
    current_curved = eta/2*support(L*abs(S.imag),abs(Sprime.imag))
    identity_errors = {
       'current_B_C_cross':abs(current-JB-JC-crossJ),
       'K_B_C_cross':max(abs(K[i]-KB[i]-KC[i]-Kcross[i]) for i in (0,1)),
       'Jdagger_B_C_cross':max(abs(J[i]-Jb[i]-Jc[i]-Jcross[i]) for i in (0,1)),
       'candidate_slab_identity':abs(raw[1]/2-(Acarrier*moments[0].real
                  -d*moments[1].real-c*moments[1].imag)),
       'K_minus_Jdagger_affine':max(abs(K[i]-J[i]-[intercept,slope][i]) for i in (0,1)),
       'raw_leading_K_scaling':abs((2*leading[1]**2-3*leading[0]*leading[2])/(4*c**6)-K[0])}
    record = {'M':M,'height_offset':h,'time':data['t'],'L':L,'eta':eta,
       'moments_0_to_6':[[z.real,z.imag] for z in moments], 'raw_jets_0_to_4':raw,
       'current':current,'current_B_C_cross':[JB,JC,crossJ],
       'current_candidate_payment_box':current_box,'current_candidate_payment_curved':current_curved,
       'Gamma0':data['Gamma0'],'density_coefficient':data['density'],
       'Gamma_formula':'Gamma0+density_coefficient/(4*C_count+1)^2, C_count>=0',
       'K_affine_in_Gamma':K,'Jdagger_affine_in_Gamma':J,
       'K_B_C_cross_affine':[KB,KC,Kcross],'Jdagger_B_C_cross_affine':[Jb,Jc,Jcross],
       'K_minus_Jdagger_affine':[intercept,slope],
       'leading_jets_2_to_4':leading,'absolute_Bell_residual_payments':E,
       'complete_jet_error_payments_2_to_4':[math.factorial(j)*L**j*eta+E[j-2] for j in (2,3,4)],
       'observed_raw_leading_differences':residual_check,
       'candidate_null_slab':{'X0':moments[0].real,'e1':raw[1]/2,
              'Z1':moments[1].imag+eps*moments[1].real,
              'value_allowance':eta/2,'derivative_allowance':L*eta/2,
              'Z1_box_allowance':(L+abs(Acarrier))*eta/(2*c),
              'curved_predicate':schur,'joint_box_candidate':candidate},
       'conditional_payment_at_Gamma_range_endpoints':pay,
       'actual_K_minus_J_at_Gamma_range_endpoints':abs_diff,
       'payment_applicability':'Only at a genuine joint candidate; unrestricted actual differences need not obey payments.',
       'identity_errors':identity_errors}
    return record,raw,moments


def value_derivative(q0,logs,M,h):
    data=physical_data(M,h)
    q=transported_q(q0,logs,data)
    v=-data['d']*logs-1j*(data['ok'][0]-data['c']*logs)
    v1=-data['dk'][1]*logs-1j*(data['ok'][1]-data['ck'][1]*logs)
    return [float(2*np.sum(q).real),float(2*np.sum(q*v).real),
            float(2*np.sum(q*(v*v+v1)).real)]


def critical_points(q0,logs,M):
    grid=np.linspace(0,8,65)
    values=[value_derivative(q0,logs,M,float(h))[1] for h in grid]
    roots=[]
    for a,b,va,vb in zip(grid[:-1],grid[1:],values[:-1],values[1:]):
        if va*vb>=0: continue
        left,right=float(a),float(b)
        h=(left+right)/2
        for _ in range(18):
            f,der,sec=value_derivative(q0,logs,M,h)
            if va*der<=0: right=h;vb=der
            else: left=h;va=der
            if abs(der)<1e-9: break
            nxt=h-der/sec if sec else (left+right)/2
            h=nxt if left<nxt<right else (left+right)/2
        f,der,sec=value_derivative(q0,logs,M,h)
        data=physical_data(M,h)
        roots.append({'height_offset':h,'finite_F':f,'finite_Fprime_residual':der,
            'finite_Fsecond':sec,'eta':data['eta'],'value_to_eta_ratio':abs(f)/data['eta'],
            'pointwise_joint_box_candidate':abs(f)<=data['eta'] and abs(der)<=data['L']*data['eta']})
    return {'M':M,'initial_scan_step':.125,'detected_sign_change_critical_points':roots,
            'coverage_claim':'None: sign-change scanning can miss roots and is not an interval isolation.'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--output',required=True)
    parser.add_argument('--cutoffs',type=int,nargs='+',default=[22066,50000,100000])
    parser.add_argument('--precision',type=int,default=55)
    parser.add_argument('--calibration-certificate')
    args=parser.parse_args()
    started=time.time()
    records=[];validation=[];criticals=[]
    offsets=[0,.25,.35,.5,1,2,4,6,8]
    for M in args.cutoffs:
        phase_start=time.time()
        q0,logs=decimal_complete(M,0,args.precision,return_array=True)
        print(f'M={M}: all base phases protected in {time.time()-phase_start:.2f}s',flush=True)
        for h in offsets:
            record,_,_=features(q0,logs,M,h)
            records.append(record)
        critical=critical_points(q0,logs,M)
        if critical['detected_sign_change_critical_points']:
            closest=min(critical['detected_sign_change_critical_points'],key=lambda z:abs(z['finite_F']))
            critical['closest_detected_critical_point_complete_features']=features(q0,logs,M,closest['height_offset'])[0]
        criticals.append(critical)
        # Direct Decimal physical sum at h=.35 is independent of float transport.
        # Recompute all moments to precision75 for the first and last cutoff.
        if M in (args.cutoffs[0],args.cutoffs[-1]):
            hs=.35
            high=decimal_complete(M,hs,75)
            rec,_,ordinary=features(q0,logs,M,hs)
            errors=[abs(a-b) for a,b in zip(ordinary,high)]
            scales=[max(1,abs(z)) for z in high]
            assert max(a/b for a,b in zip(errors,scales))<1e-10
            step=.001
            samples={k:features(q0,logs,M,hs+k*step)[1] for k in (-2,-1,0,1,2)}
            derivative_errors=[]
            for j in range(1,5):
                fd=(samples[-2][j-1]-8*samples[-1][j-1]+8*samples[1][j-1]-samples[2][j-1])/(12*step)
                derivative_errors.append(abs(fd-samples[0][j])/max(1,abs(samples[0][j])))
            assert max(derivative_errors)<1e-7
            validation.append({'M':M,'height_offset':hs,'high_precision_digits':75,
                   'complete_moment_absolute_errors':errors,
                   'complete_moment_relative_errors':[a/b for a,b in zip(errors,scales)],
                   'finite_difference_relative_errors_raw_1_to_4':derivative_errors,
                   'finite_difference_step':step,'finite_difference_stencil':'five point derivative of raw row j-1'})
    identities=max(max(r['identity_errors'].values()) for r in records)
    # Roundoff tolerances scale with each observed complete feature, not eta.
    for r in records:
        scale=max(1,abs(r['K_affine_in_Gamma'][0]),abs(r['Jdagger_affine_in_Gamma'][0]))
        assert max(r['identity_errors'].values())<1e-10*scale
        assert all(err<=budget for err,budget in zip(r['observed_raw_leading_differences'],
                                                    r['absolute_Bell_residual_payments']))
    calibration=None
    if args.calibration_certificate:
        reference=Path(args.calibration_certificate)
        center=json.loads(reference.read_text())['center']
        measured=next(r for r in records if r['M']==22066 and r['height_offset']==0)
        def middle(pair): return (float(pair[0])+float(pair[1]))/2
        expected=[2*middle(center['complete_S']['real']),
                  2*middle(center['complete_Sprime']['real']),middle(center['complete_current'])]
        observed=measured['raw_jets_0_to_4'][:2]+[measured['current']]
        errors=[abs(a-b) for a,b in zip(observed,expected)]
        assert max(errors)<1e-10
        calibration={'reference_sha256':hashlib.sha256(reference.read_bytes()).hexdigest(),
                     'comparison':'Numerical values versus retained certificate midpoints, tolerance1e-10; not interval inclusion.',
                     'quantities':['F','Fprime','current'],'absolute_errors':errors}
    candidates=[(r['M'],r['height_offset']) for r in records if r['candidate_null_slab']['joint_box_candidate']]
    result={'date':'2026-10-10','status':'PASS','scope':'Bounded numerical pilot of complete genuine finite sums; no outward intervals, no genuine heat-zero proof, no uniform theorem.',
        'model':'GPT-6 (Codex); exact serving variant and effort unavailable, not inferred',
        'cutoffs':args.cutoffs,'height_offsets':offsets,'phase_precision_digits':args.precision,
        'complex_summation':'NumPy complex128 after Decimal protected phase reduction',
        'count_constant':'Symbolic; no C_count selected. Kernel coefficients are affine in Gamma.',
        'samples':records,'higher_precision_validation':validation,'finite_critical_point_diagnostics':criticals,
        'calibration':calibration,
        'joint_box_candidates_at_sampled_heights':candidates,
        'minimum_sampled_curved_predicate':min(r['candidate_null_slab']['curved_predicate'] for r in records),
        'maximum_feature_identity_absolute_error':identities,
        'elapsed_seconds':time.time()-started,
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'numpy_version':np.__version__,
        'source_interfaces':['09_prime_phase_torus/prime_phase_torus_signed_reductions.tex equations Jdag, Jdag-payment, Gamma and leading-jets',
             '13_microlocal_phase_space/notes/2_CENTERED_RELATIVE_BLOCK_AND_ADVERSE_COHERENT_CURRENT_20261010.md',
             '13_microlocal_phase_space/notes/3_COMPLETE_CURRENT_AND_PAID_SIMPLE_ZERO_RECTANGLE_20261010.md'],
        'scientific_limits':['Sparse point sampling does not prove coverage between samples.',
             'Conditional null-slab and curved payments apply at joint candidates only.',
             'All-real threshold and counting hypotheses and their finite-height range are not tested.',
             'Large moment absolute differences can arise from complex128 reduction roundoff; selected complete sums were checked at 75 digits.']}
    out=Path(args.output)
    out.write_text(json.dumps(result,indent=2,allow_nan=False)+'\n')
    print(json.dumps({'status':'PASS','output':str(out),'elapsed_seconds':result['elapsed_seconds'],
                      'sampled_joint_candidates':candidates,'maximum_identity_error':identities}),flush=True)


if __name__=='__main__': main()
