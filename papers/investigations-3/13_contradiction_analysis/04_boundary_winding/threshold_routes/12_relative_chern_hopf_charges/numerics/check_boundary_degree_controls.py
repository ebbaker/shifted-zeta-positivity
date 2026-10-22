#!/usr/bin/env python3
"""Exact boundary degree controls for BW12 Note 02, 21 October 2026.
Prepared for Edward Baker with substantial LLM assistance.
Actual authoring model gpt-6-astra (Codex), effort max.
Standard library only. No theta acquisition or numerical Hopf quadrature.
"""
from fractions import Fraction as Q
from itertools import product, permutations
from math import isqrt
from pathlib import Path
import argparse, hashlib, json, platform, signal, time


def require(condition,message):
    if not condition: raise ArithmeticError(message)


def norm2(v): return sum((x*x for x in v),Q(0))


def sqrt_lower(q,scale=10**9):
    require(q>=0,'negative norm square')
    return Q(isqrt(q.numerator*scale*scale//q.denominator),scale)


def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1


def linear_solve(A,b):
    """Exact 4x4 solve with determinant. Nonregular cases are explicit."""
    m=[list(row)+[rhs] for row,rhs in zip(A,b)]
    pivots=[]; determinant=Q(1); sign=1; r=0
    for col in range(4):
        rows=[i for i in range(r,4) if m[i][col]]
        if not rows: continue
        k=rows[0]
        if k!=r:m[k],m[r]=m[r],m[k];sign=-sign
        pivot=m[r][col];determinant*=pivot
        m[r]=[v/pivot for v in m[r]]
        for i in range(4):
            if i!=r and m[i][col]:
                c=m[i][col];m[i]=[v-c*w for v,w in zip(m[i],m[r])]
        pivots.append(col);r+=1
    if r<4:
        if any(all(v==0 for v in row[:4]) and row[4]!=0 for row in m):
            return 'inconsistent',None,None
        return 'singular_consistent',None,None
    return 'regular',[m[i][4] for i in range(4)],sign*determinant


def value(kind,x):
    tr,ti,zr,zi=x
    if kind=='identity':return x
    if kind=='orientation_reverse':return (tr,-ti,zr,zi)
    constant=Q(1) if kind=='two_root_heat' else Q(0)
    return (zr*zr-zi*zi-constant-2*tr,2*zr*zi-2*ti,2*zr,2*zi)


def boundary_tetrahedra(N):
    for axis in range(4):
        others=[k for k in range(4) if k!=axis]
        for side in (-1,1):
            fixed=0 if side==-1 else N
            for cell in product(range(N),repeat=3):
                for perm in permutations(range(3)):
                    idx=[0]*4;idx[axis]=fixed
                    for k,c in zip(others,cell):idx[k]=c
                    vertices=[tuple(idx)]
                    for p in perm:
                        idx[others[p]]+=1;vertices.append(tuple(idx))
                    sign_x=side*((-1)**axis)*parity(perm)
                    yield axis,vertices,sign_x


def coordinate_floor_squared(vs):
    result=Q(0)
    for j in range(4):
        lo=min(v[j] for v in vs);hi=max(v[j] for v in vs)
        distance=lo if lo>0 else -hi if hi<0 else Q(0)
        result+=distance*distance
    return result


def run_case(kind,N,T,R,expected):
    start=time.monotonic();lengths=(T,T,R,R)
    cache={};tetra=[];minimum_pl=None;minimum_gap=None;max_error=Q(0)
    for axis,ids,sign_x in boundary_tetrahedra(N):
        vs=[]
        for idx in ids:
            if idx not in cache:
                x=tuple(L*Q(2*k-N,N) for k,L in zip(idx,lengths))
                cache[idx]=value(kind,x)
            vs.append(cache[idx])
        floor2=coordinate_floor_squared(vs)
        # Only z^2 is nonlinear: each free real z coordinate has variance
        # <= (2R/N)^2/4. Both components of the derivative are affine.
        error=Q(0) if kind in ('identity','orientation_reverse') else (2-int(axis in (2,3)))*R*R/(N*N)
        require(floor2>error*error,f'{kind}: unpaid tetrahedron boundary interpolation')
        floor=sqrt_lower(floor2)
        require(floor>error,'outward rational floor')
        gap=floor-error
        minimum_pl=floor if minimum_pl is None else min(minimum_pl,floor)
        minimum_gap=gap if minimum_gap is None else min(minimum_gap,gap)
        max_error=max(max_error,error)
        tetra.append((vs,sign_x))
    # An artificial cone value 0 is used only for the PL extension. The
    # true field is never evaluated at the interior cone point.
    target=tuple(Q(1,k) for k in (10007,10009,10037,10039))
    require(norm2(target)<minimum_pl*minimum_pl,'target outside PL boundary clearance')
    positive=negative=outside=singular_empty=0
    for vs,sign_x in tetra:
        A=[[v[j] for v in vs] for j in range(4)]
        status,lam,det=linear_solve(A,target)
        require(status!='singular_consistent','chosen target is not proved regular')
        if status=='inconsistent':singular_empty+=1;continue
        weights=[1-sum(lam),*lam]
        if any(x<0 for x in weights):outside+=1;continue
        require(all(x>0 for x in weights),'target hits an image of an internal simplex face')
        sign_y=1 if det>0 else -1
        contribution=sign_y*sign_x
        if contribution>0:positive+=1
        else:negative+=1
    degree=positive-negative
    require(degree==expected,'boundary degree control failed')
    expected_vertices=(N+1)**4-(N-1)**4
    require(len(cache)==expected_vertices,'complete boundary vertex coverage')
    require(len(tetra)==48*N**3,'complete boundary tetrahedron coverage')
    return {'field':kind,'grid_subintervals_per_axis':N,
            'domain':'(-T,T)^2 in complex time times (-R,R)^2 in complex position',
            'T':str(T),'R':str(R),'source_vertex_error':'0 exact rational values',
            'cached_boundary_vertices':len(cache),'boundary_tetrahedra':len(tetra),
            'actual_interior_field_evaluations':0,
            'PL_boundary_floor_lower':str(minimum_pl),
            'interpolation_error_maximum':str(max_error),
            'uniform_homotopy_gap_lower':str(minimum_gap),
            'artificial_cone_value':['0']*4,'regular_target':[str(x) for x in target],
            'positive_preimages':positive,'negative_preimages':negative,
            'outside_image_simplices':outside,'singular_simplices_with_empty_target_fiber':singular_empty,
            'degree':degree,'expected_degree':expected,'seconds':time.monotonic()-start,
            'degree_status':'exact oriented simplex count; continuous boundary homotopy paid',
            'holomorphic':kind!='orientation_reverse'}


def sharpness_and_scope():
    T=Q(1,10);R=Q(3,2);b=1-2*T;eta=Q(1,10)
    require(b==Q(4,5) and b-eta==Q(7,10),'sharp constant perturbation gap')
    # H=z^2-1-2t+eta has its event at (eta-1)/2, z=0.
    event=(eta-1)/2
    require(abs(event)>T,'sharp model must be event-free')
    require(abs((b-1)/2)==T,'equality puts the event on the boundary')
    require(abs((Q(9,10)-1)/2)<T,'over-budget perturbation has an interior event')
    # Two components genuinely needed: H(0,+/-1)=0 and Hz(0,0)=0.
    require(all(value('two_root_heat',(Q(0),Q(0),z,Q(0)))[0]==0 for z in (Q(-1),Q(1))), 'two roots')
    require(value('two_root_heat',(Q(0),Q(0),Q(0),Q(0)))[2:]==(Q(0),Q(0)), 'stationary point')
    require(Q(1)<R,'both roots are interior')
    return {'square_holomorphic_reference':'F=(z^2-1-2t,2z)',
            'domain_radii':{'time':'1/10','position':'3/2'},
            'exact_reference_floor':'4/5',
            'attainment':'t=-1/10,z=0 on the boundary',
            'two_real_roots':['-1','1'],'stationary_point':'0',
            'sharp_heat_perturbation':{'H':'z^2-1-2t+1/10','uniform_vector_error':'1/10',
                'exact_joint_floor':'7/10','event_time':str(event)},
            'strictness_controls':{'error_equal_floor':'event at boundary t=-1/10',
                'error_9_10':'event at interior t=-1/20, local charge 1'},
            'scope_counterexamples':{
                'target_dimension_too_large':'(1,t,z): C^2 to C^3 on the unit ball; interior min=1, boundary min=sqrt(2)',
                'reference_not_holomorphic':'(1+|t|^2+|z|^2,0) on the unit ball; interior min=1, boundary min=2',
                'zero_free_hypothesis_missing':'(t,z) on the unit ball; boundary min=1, interior min=0',
                'unbounded_domain':'(exp(t),z) on Re(t)<0; boundary inf=1, interior inf=0'},
            'scope':'Exact model algebra and comparisons; analytic minimum principle is proved in the note, not certified by these examples.'}


def main():
    signal.alarm(180)
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
    start=time.monotonic()
    cases=[run_case('identity',1,Q(1),Q(1),1),
           run_case('orientation_reverse',1,Q(1),Q(1),-1),
           run_case('quadratic_collision',2,Q(1,10),Q(1,4),1),
           run_case('two_root_heat',6,Q(1,10),Q(3,2),0)]
    result={'schema':'rch12-boundary-degree-controls-v1','date':'2026-10-21',
        'prepared_for':'Edward Baker','authoring_model':'gpt-6-astra','actual_effort':'max',
        'LLM_assistance':'substantial; same-assistant derivation and checks',
        'python':platform.python_version(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'arithmetic':'Python fractions.Fraction; square-root bounds by integer square root',
        'status':'exact polynomial/linear boundary-degree controls; no new theta certificate or theta cost comparison',
        'seconds':time.monotonic()-start,'cases':cases,'sharpness_and_scope':sharpness_and_scope()}
    args.out.write_text(json.dumps(result,indent=2)+'\n')
    for r in cases:print(r['field'],r['degree'],r['uniform_homotopy_gap_lower'],r['cached_boundary_vertices'],r['positive_preimages'],r['negative_preimages'],round(r['seconds'],3))

if __name__=='__main__':main()
