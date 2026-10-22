#!/usr/bin/env python3
"""Complete-theta two-zero boundary/direct comparison, BW12 Note 03.
21 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual authoring model gpt-6-astra (Codex), effort max.
Requires python-flint 0.9.0 and the two companion BW12 scripts.
No RH assumption, global exclusion or independent validation.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from pathlib import Path
import argparse, hashlib, importlib.util, json, platform, signal, sys, time
sys.dont_write_bytecode=True
import flint
from flint import arb, acb, ctx


def require(ok,message):
    if not ok:raise ArithmeticError(message)


def A(v):
    q=Q(v);return arb(q.numerator)/q.denominator


def rec(v):return v.str(40,more=True)


def load_module(folder,name):
    p=folder/(name+'.py')
    spec=importlib.util.spec_from_file_location(name,p)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m)
    return m,hashlib.sha256(p.read_bytes()).hexdigest()


def geometry(Ns):
    for axis in range(4):
        free=[j for j in range(4) if j!=axis]
        for side in (-1,1):
            fixed=0 if side==-1 else Ns[axis]
            for cell in product(*(range(Ns[j]) for j in free)):
                for perm in permutations(range(3)):
                    idx=[0]*4;idx[axis]=fixed
                    for j,k in zip(free,cell):idx[j]=k
                    ids=[tuple(idx)]
                    for p in perm:
                        idx[free[p]]+=1;ids.append(tuple(idx))
                    parity=-1 if sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))%2 else 1
                    yield axis,ids,side*((-1)**axis)*parity


def floor_of(vs,degree):
    return degree.sqrt_lower(degree.coordinate_floor_squared(vs),scale=10**18)


def degree_count(tetra,values,bmin,degree):
    start=time.monotonic()
    target=tuple(Q(1,p) for p in (1000000000039,1000000000061,1000000000063,1000000000091))
    require(sum(v*v for v in target)<bmin*bmin,'regular target inside boundary clearance')
    counts={'positive':0,'negative':0,'outside':0,'singular_empty':0}
    for axis,ids,sx in tetra:
        vs=[values[i] for i in ids]
        Y=[[v[j] for v in vs] for j in range(4)]
        status,lam,det=degree.linear_solve(Y,target)
        require(status!='singular_consistent','unproved regular target: singular consistent system')
        if status=='inconsistent':counts['singular_empty']+=1;continue
        weights=[1-sum(lam),*lam]
        if any(w<0 for w in weights):counts['outside']+=1;continue
        require(all(w>0 for w in weights),'target lies on an actual simplex face')
        counts['positive' if sx*(1 if det>0 else -1)>0 else 'negative']+=1
    counts.update({'degree':counts['positive']-counts['negative'],
                   'target':[str(v) for v in target],
                   'seconds':time.monotonic()-start})
    require(sum(counts[k] for k in ('positive','negative','outside','singular_empty'))==len(tetra),'all cone simplices counted')
    return counts


def anisotropic_controls(degree):
    out=[]
    for kind,Ns,Ts,Rs,Ys,expected in [('identity',(1,1,4,1),Q(1),Q(1),Q(1),1),
                                    ('time_conjugation',(1,1,4,1),Q(1),Q(1),Q(1),-1),
                                    ('quadratic_collision',(1,1,8,1),Q(1,100),Q(1,8),Q(1,100),1)]:
        lengths=(Ts,Ts,Rs,Ys);tetra=list(geometry(Ns));values={};bmin=None;gapmin=None
        for axis,ids,sx in tetra:
            for idx in ids:
                if idx not in values:
                    x=tuple(L*Q(2*k-N,N) for k,N,L in zip(idx,Ns,lengths))
                    if kind=='identity':values[idx]=x
                    elif kind=='time_conjugation':values[idx]=(x[0],-x[1],x[2],x[3])
                    else:values[idx]=degree.value('quadratic_collision',x)
            b=floor_of([values[i] for i in ids],degree)
            err=Q(0) if kind!='quadratic_collision' else sum(lengths[j]**2/Ns[j]**2 for j in (2,3) if j!=axis)
            require(b>err,'anisotropic control boundary error')
            bmin=b if bmin is None else min(bmin,b)
            gapmin=b-err if gapmin is None else min(gapmin,b-err)
        count=degree_count(tetra,values,bmin,degree)
        require(count['degree']==expected,'anisotropic control degree')
        out.append({'field':kind,'mesh':list(Ns),'radii':[str(q) for q in lengths],
                    'vertices':len(values),'tetrahedra':len(tetra),'boundary_gap_lower':str(gapmin),**count})
    return out


def clusters(indices):
    groups=[]
    for k in indices:
        if not groups or k>groups[-1][-1]+1:groups.append([k])
        else:groups[-1].append(k)
    return groups


def real_coverage(nodes,delta,M,h):
    N=len(nodes)-1
    error=[(delta[j]+A(h*h)*M[j+2]/8).upper() for j in (0,1)]
    def endpoints(j,k):
        lo=(A(min(nodes[k][j],nodes[k+1][j]))-error[j]).lower()
        hi=(A(max(nodes[k][j],nodes[k+1][j]))+error[j]).upper()
        return lo,hi
    def sign_at(j,k):
        b=arb(A(nodes[k][j]),delta[j])
        return 1 if b>0 else -1 if b<0 else 0
    results={}
    for j,label in ((0,'zeros'),(1,'stationary_points')):
        uncertain=[k for k in range(N) if not (endpoints(j,k)[0]>0 or endpoints(j,k)[1]<0)]
        group_rows=[]
        for group in clusters(uncertain):
            left=group[0];right=group[-1]+1
            sl,sr=sign_at(j,left),sign_at(j,right)
            require(sl*sr==-1,'opposite signs at uncertain-cluster ends')
            slope_lowers=[]
            for k in group:
                if j==0:
                    lo,hi=endpoints(1,k)
                    slope=lo if lo>0 else -hi if hi<0 else arb(0)
                    direction=1 if lo>0 else -1 if hi<0 else 0
                else:
                    # H'' at the left anchor plus a complete H''' bound.
                    slope=(A(nodes[k][2])-delta[2]-A(h)*M[3]).lower()
                    direction=1 if slope>0 else 0
                require(slope>0 and direction==(sr-sl)//2,'monotonicity on the full uncertain cluster')
                slope_lowers.append(slope)
            brackets=[(k,k+1) for k in range(left,right) if sign_at(j,k)*sign_at(j,k+1)==-1]
            require(len(brackets)==1,'one narrow sign bracket in each cluster')
            k,l=brackets[0]
            group_rows.append({'cluster_indices':[left,right],
                'cluster_x':[str(Q(28)+h*left),str(Q(28)+h*right)],
                'bracket_indices':[k,l],'bracket_x':[str(Q(28)+h*k),str(Q(28)+h*l)],
                'left_value':rec(arb(A(nodes[k][j]),delta[j])),
                'right_value':rec(arb(A(nodes[l][j]),delta[j])),
                'monotonic_derivative_floor_lower':rec(min(slope_lowers)),
                'uniqueness':'entire uncertain cluster monotone; all other segments exclude zero'})
        results[label]=group_rows
    require(len(results['zeros'])==2 and len(results['stationary_points'])==1,'exactly two neighboring roots and one stationary point')
    require(Q(results['zeros'][0]['bracket_x'][1])<Q(results['stationary_points'][0]['bracket_x'][0]) and
            Q(results['stationary_points'][0]['bracket_x'][1])<Q(results['zeros'][1]['bracket_x'][0]),'stationary point between roots')
    results['real_interpolation_errors']=[rec(e) for e in error]
    return results


def acquire_boundary_jet(j,x,T,pi,pilot):
    """Acquire at real time -T, on the boundary face. Tail majorant uses t=0."""
    calls=0;start=time.monotonic()
    def integrand(u,analytic):
        nonlocal calls
        calls+=1
        q=(4*u).exp();v=acb(0)
        for n in range(1,5):
            lam=pi*n*n
            v+=(2*lam*lam*q*q-3*lam*q)*(-lam*q).exp()
        phase=A(x)*u
        trig=(phase.cos,phase.sin,phase.cos,phase.sin)[j%4]()
        if j%4 in (1,2):trig=-trig
        return (u-A(T)*u*u).exp()*v*u**j*trig
    core=acb.integral(integrand,0,1,abs_tol=arb('1e-32'),rel_tol=arb('1e-28'),eval_limit=100000,depth_limit=30)
    require(core.is_finite() and core.imag.contains(0),'finite real boundary-anchor integral')
    require(core.real.rad()<arb('1e-28'),'boundary-anchor quadrature budget')
    omitted,exterior=pilot.tails(j,arb(0),arb(0),pi)
    err=(core.real.rad()+omitted+exterior).upper()
    return (core.real.mid(),err),{'callbacks':calls,'seconds':time.monotonic()-start,
        'quadrature_radius':rec(core.real.rad().upper()),'omitted_modes_upper':rec(omitted),
        'retained_exterior_upper':rec(exterior)}


def run(pilot,degree):
    start=time.monotonic();T=Q(1,100);Y=Q(1,100);N=256;h=Q(15,N);Ns=(1,1,N,1)
    pi=arb.pi();mom_rows=[];M={}
    for j in range(2,6):
        M[j],row=pilot.acquire('moment',j,arb(0),A(T),A(Y),pi);mom_rows.append(row)
    nodes=[];delta=[arb(0)]*4;jet_callbacks=0;jet_seconds=0;max_quad=arb(0)
    tail_max=[arb(0)]*4
    for k in range(N+1):
        x=Q(28)+h*k;vals=[]
        for j in range(4):
            (c,d),row=acquire_boundary_jet(j,x,T,pi,pilot)
            # A float chooses a rational dyadic approximant only. The complete
            # discrepancy from the returned ball is included in its error.
            q=Q(float(c));err=(abs(A(q)-c)+d).upper()
            delta[j]=max(delta[j],err);vals.append(q)
            jet_callbacks+=row['callbacks'];jet_seconds+=row['seconds']
            max_quad=max(max_quad,arb(row['quadrature_radius']))
            tail_max[j]=max(tail_max[j],arb(row['omitted_modes_upper'])+arb(row['retained_exterior_upper']))
        nodes.append(vals)
    acquisition_seconds=time.monotonic()-start
    require(4*(N+1)+len(M)<=1100,'declared acquisition budget')
    # Transfer the boundary source anchors to time zero for real coverage.
    real_nodes=[[c[0]-T*c[2],c[1]-T*c[3],c[2]] for c in nodes]
    real_delta=[(delta[j]+A(T)*delta[j+2]+A(T*T)*M[j+4]/2).upper() for j in (0,1)]
    real_delta.append((delta[2]+A(T)*M[4]).upper())
    coverage=real_coverage(real_nodes,real_delta,M,h)
    coverage['time_zero_anchor_transfer_errors']=[rec(e) for e in real_delta]
    tnorm=(A(T)*arb(5).sqrt()).upper()
    vertex_errors=[]
    for j in (0,1):
        e=delta[j]+A(Y)*delta[j+1]+tnorm*delta[j+2]
        e+=(A(Y*Y)*M[j+2]+2*A(Y)*tnorm*M[j+3]+tnorm*tnorm*M[j+4])/2
        vertex_errors.append(e.upper())
    values={}
    for it,iu,ix,iy in product(range(2),range(2),range(N+1),range(2)):
        tr=(2*it-1)*T;ti=(2*iu-1)*T;y=(2*iy-1)*Y
        c=nodes[ix]
        values[(it,iu,ix,iy)]=(c[0]-(tr+T)*c[2],y*c[1]-ti*c[2],c[1]-(tr+T)*c[3],y*c[2]-ti*c[3])
    require(len(values)==8*(N+1),'all cached boundary vertices')
    tetra=list(geometry(Ns));require(len(tetra)==36*N+12,'all boundary tetrahedra')
    # Pure coordinate variances. The fixed face coordinate contributes zero.
    variances=(T*T,T*T,h*h/4,Y*Y)
    face_errors=[]
    for axis in range(4):
        vt=sum(variances[j] for j in (0,1) if j!=axis)
        vz=sum(variances[j] for j in (2,3) if j!=axis)
        es=[]
        for j in (0,1):
            interp=(M[j+4]*A(vt)+2*M[j+3]*(A(vt)*A(vz)).sqrt()+M[j+2]*A(vz))/2
            es.append((vertex_errors[j]+interp).upper())
        face_errors.append((es,(es[0]**2+es[1]**2).sqrt().upper()))
    begin=time.monotonic();bmin=None;bgap=None;bworst=None
    for i,(axis,ids,sx) in enumerate(tetra):
        b=floor_of([values[k] for k in ids],degree)
        gap=(A(b)-face_errors[axis][1]).lower()
        require(gap>0,'unpaid theta boundary tetrahedron '+str(i))
        bmin=b if bmin is None else min(bmin,b)
        if bgap is None or gap<bgap:bgap=gap;bworst={'tetrahedron_index':i,'axis':axis,'vertex_indices':[list(k) for k in ids],'floor':str(b),'gap':rec(gap)}
    boundary_floor_seconds=time.monotonic()-begin
    count=degree_count(tetra,values,bmin,degree)
    require(count['degree']==0,'computed theta degree zero')
    # Direct tensor-product interpolation on full 4D cells. Its one-variable
    # interpolation remainders sum; no mixed Hessian bound is required.
    direct_components=[(vertex_errors[j]+A(T*T)*M[j+4]+A(h*h/8+Y*Y/2)*M[j+2]).upper() for j in (0,1)]
    direct_error=(direct_components[0]**2+direct_components[1]**2).sqrt().upper()
    begin=time.monotonic();dgap=None;dworst=None;dfloor=None
    for k in range(N):
        ids=[(it,iu,ix,iy) for it,iu,ix,iy in product(range(2),range(2),(k,k+1),range(2))]
        b=floor_of([values[i] for i in ids],degree);gap=(A(b)-direct_error).lower()
        require(gap>0,'unpaid full-dimensional direct cell '+str(k))
        dfloor=b if dfloor is None else min(dfloor,b)
        if dgap is None or gap<dgap:dgap=gap;dworst={'cell':k,'x':[str(Q(28)+h*k),str(Q(28)+h*(k+1))],'floor':str(b),'gap':rec(gap)}
    direct_seconds=time.monotonic()-begin
    require(dgap>bgap,'recorded comparison has direct margin strictly stronger')
    raw=json.dumps([[str(q) for q in row] for row in nodes],separators=(',',':')).encode()
    require(time.monotonic()-start<180,'declared elapsed budget')
    return {'domain':{'Re_t':['-1/100','1/100'],'Im_t':['-1/100','1/100'],
            'Re_z':['28','43'],'Im_z':['-1/100','1/100'],'orientation':'Re(t), Im(t), Re(z), Im(z)',
            'boundary':'piecewise smooth box; Brouwer degree, no smoothing'},
        'mesh_subintervals':list(Ns),'anchor_spacing':str(h),'bits':ctx.prec,
        'source':{'retained_modes':4,'source_cutoff':'1','complete_moment_rows':mom_rows,
            'real_anchor_count':N+1,'anchor_time':'-1/100','anchor_boundary_face':'Re(t)=-1/100',
            'actual_interior_field_anchors':0,'jet_orders':[0,1,2,3],'jet_scalar_integrals':4*(N+1),
            'total_scalar_integrals':4*(N+1)+len(M),'jet_callbacks':jet_callbacks,
            'total_callbacks':jet_callbacks+sum(r['callbacks'] for r in mom_rows),
            'jet_quad_seconds':jet_seconds,'acquisition_elapsed_seconds':acquisition_seconds,
            'uniform_anchor_errors':[rec(d) for d in delta],
            'maximum_quadrature_radius':rec(max_quad),'maximum_source_tails_by_order':[rec(t) for t in tail_max],
            'rational_anchor_midpoints_sha256':hashlib.sha256(raw).hexdigest(),
            'arrays':'regenerated in memory; the hash identifies approximants, not a proof'},
        'real_slice':coverage,
        'vertex_lift':{'formula':'G_j=c_j+i*y*c_(j+1)-(t+T)*c_(j+2), c_j=H_j(-T,x), j=0,1',
            'component_error_upper':[rec(e) for e in vertex_errors],
            'boundary_vertices':len(values),'direct_complex_source_integrals':0},
        'boundary':{'tetrahedra':len(tetra),'PL_floor_lower':str(bmin),
            'face_component_errors':[[rec(e) for e in pair[0]] for pair in face_errors],
            'face_vector_errors':[rec(pair[1]) for pair in face_errors],
            'homotopy_gap_lower':rec(bgap),'worst':bworst,
            'floor_check_seconds':boundary_floor_seconds,**count},
        'direct':{'full_dimensional_cells':N,'vertices_per_cell':16,'same_vertex_set':True,
            'tensor_floor_lower':str(dfloor),'component_error_upper':[rec(e) for e in direct_components],
            'vector_error_upper':rec(direct_error),'joint_floor_lower':rec(dgap),
            'worst':dworst,'check_seconds':direct_seconds},
        'comparison':{'same_source_integrals':True,'same_domain':True,'actual_interior_field_evaluations_both':0,
            'direct_gap_strictly_larger':bool(dgap>bgap),'gap_difference_lower':rec((dgap-bgap).lower()),
            'boundary_total_consumer_seconds':boundary_floor_seconds+count['seconds'],
            'direct_total_consumer_seconds':direct_seconds,
            'time_scope':'one shared acquisition; consumer passes timed sequentially; not an optimal-complexity benchmark',
            'structural_scope':'one mesh interval in each transverse coordinate puts every direct cell vertex on the outer boundary'},
        'run_seconds':time.monotonic()-start}


def main():
    signal.alarm(180)
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--out',type=Path,required=True)
    p.add_argument('--support-dir',type=Path,default=Path(__file__).resolve().parent)
    args=p.parse_args();ctx.prec=192
    pilot,h1=load_module(args.support_dir,'certify_relative_charge_pilot')
    degree,h2=load_module(args.support_dir,'check_boundary_degree_controls')
    controls=anisotropic_controls(degree)
    result={'schema':'rch12-two-zero-theta-comparison-v1','date':'2026-10-21','timezone':'America/New_York',
        'prepared_for':'Edward Baker','authoring_model':'gpt-6-astra','actual_effort':'max',
        'LLM_assistance':'substantial; same-assistant derivation and computation',
        'status':'finite full-theta certificate and matched direct comparison; no global simplicity conclusion',
        'python':platform.python_version(),'python_flint':flint.__version__,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'dependency_sha256':{'certify_relative_charge_pilot.py':h1,'check_boundary_degree_controls.py':h2},
        'declared_budget':{'source_integrals_max':1100,'wall_seconds_max':180,'bits':192,
            'retained_modes':4,'source_cutoff':'1','abs_quad_tolerance':'1e-32','rel_quad_tolerance':'1e-28'},
        'anisotropic_controls':controls,'run':run(pilot,degree)}
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    r=result['run'];print(json.dumps({'degree':r['boundary']['degree'],'boundary_gap':r['boundary']['homotopy_gap_lower'],
        'direct_gap':r['direct']['joint_floor_lower'],'comparison':r['comparison'],
        'coverage':r['real_slice'],'seconds':r['run_seconds']},indent=2))

if __name__=='__main__':main()
