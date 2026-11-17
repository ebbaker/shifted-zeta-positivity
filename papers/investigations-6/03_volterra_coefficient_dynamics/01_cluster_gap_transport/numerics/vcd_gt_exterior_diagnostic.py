#!/usr/bin/env python3
"""Fixed E04-r4 Stage A candidate diagnostic, 16 November 2026.

Prepared for Edward Baker with OpenAI Codex assistance; actual model and
effort unavailable. This is sampled candidate evidence, not a uniform-time
root-count or lower-mass certificate. Raw samples remain outside Git.
"""

import argparse
from fractions import Fraction as Q
from hashlib import sha256
import json
from math import inf, nextafter
from pathlib import Path
import platform
from time import perf_counter

import flint
from flint import arb, acb, ctx, fmpq


A = Q(140101, 10)
TIMES = (Q(0), Q(1, 20), Q(1, 10))
GRID = tuple(Q(k, 4) for k in range(-640, 641))
MAX_CALLS = 300000
MAX_SECONDS = 360
BITS = 160
PAD = Q(1, 256)


def exact(q):
    q = Q(q)
    return arb(fmpq(q.numerator, q.denominator))


def qstr(q):
    return str(Q(q))


def up(x):
    return nextafter(float(x.upper()), inf)


def low(x):
    return nextafter(float(x.lower()), -inf)


class Stop(RuntimeError):
    pass


class Source:
    def __init__(self):
        self.pi = arb.pi()
        self.logpi = self.pi.log()
        self.rs = [exact(Q(k, 3)) for k in range(37)]
        self.weights = [(-r*r).exp() for r in self.rs]
        self.scale = {t: 2*exact(t).sqrt() for t in TIMES}
        self.prefactor = 1/(3*self.pi.sqrt())
        self.zero = {}
        self.cache = {}
        self.calls = 0
        self.source_seconds = 0.0
        self.last_report = perf_counter()
        alpha, beta = exact(Q(9999, 10000)), exact(Q(131, 100))
        self.lattice = (4*10**13*(4+beta**2/(4*alpha)).exp()
                        / (alpha.sqrt()*(12*self.pi).expm1()))
        self.tail = (2*10**13*(-144*alpha+12*beta).exp()
                     / (self.pi.sqrt()*(24*alpha-beta)))
        self.error = (self.lattice+self.tail).upper()

    def xi(self, offset, shift):
        if self.calls >= MAX_CALLS or self.source_seconds >= MAX_SECONDS:
            raise Stop('fixed source resource cap reached')
        start = perf_counter()
        b = exact(A+offset)
        s = acb((1-shift)/2, b/2)
        result = (self.pi*b/8 + (s/2).lgamma() - s*self.logpi/2).exp()
        result *= s*(s-1)*s.zeta()/16
        self.calls += 1
        self.source_seconds += perf_counter()-start
        if not result.is_finite():
            raise Stop('nonfinite complete-xi finite-arithmetic ball')
        if perf_counter()-self.last_report > 30:
            print(json.dumps({'progress':'source','xi_calls':self.calls,
                              'source_seconds':self.source_seconds}), flush=True)
            self.last_report = perf_counter()
        return result

    def value(self, t, offset):
        key=(t,offset)
        if key in self.cache:
            return self.cache[key]
        if offset not in self.zero:
            self.zero[offset] = self.xi(offset, arb(0)).real
        value = self.zero[offset]
        if t:
            total = acb(value)
            for k in range(1,37):
                total += 2*self.weights[k]*self.xi(offset,self.scale[t]*self.rs[k]).real
            value = (self.prefactor*total).real
        error = self.error if t else arb(0)
        padded = value+arb(0,error)
        sign = 1 if padded>0 else -1 if padded<0 else 0
        row={'offset':qstr(offset),'time':qstr(t), 'finite_ball':str(value),
             'source_error_upper':str(error), 'padded_lower':low(padded),
             'padded_upper':up(padded),'sign':sign}
        self.cache[key]=row
        return row


def exterior(l,r):
    return r < -Q(8,5) or l > Q(8,5)


def bracket_record(l,r,sl,sr,steps,ambiguous):
    return {'left':qstr(l),'right':qstr(r),'left_sign':sl,'right_sign':sr,
            'bisections':steps,'unresolved_midpoint':ambiguous,
            'midpoint':float((l+r)/2),'width':float(r-l)}


def gather(source,t):
    vals=[source.value(t,x) for x in GRID]
    brackets=[]
    for i in range(len(GRID)-1):
        l,r=GRID[i],GRID[i+1]
        sl,sr=vals[i]['sign'],vals[i+1]['sign']
        if not exterior(l,r) or not sl or not sr or sl==sr:
            continue
        ambiguous=False
        steps=0
        for _ in range(6):
            mid=(l+r)/2
            sm=source.value(t,mid)['sign']
            if not sm:
                ambiguous=True
                break
            if sm==sl:
                l=mid
            else:
                r=mid
            steps+=1
        brackets.append(bracket_record(l,r,sl,sr,steps,ambiguous))
    return {'time':qstr(t),'brackets':brackets,
            'quarter_grid_ambiguous_offsets':[x['offset'] for x in vals if not x['sign']],
            'selected_sign_intervals':len(brackets)}


def mids(rows):
    return [(Q(r['left'])+Q(r['right']))/2 for r in rows]


def ordered_match(left,right):
    """Finite planning alignment: maximize pairs, then minimize displacement.

    This is neither tracked root identity nor a proof between sampled times.
    Each permitted edge has midpoint displacement at most one.
    """
    a,b=mids(left),mids(right)
    n,m=len(a),len(b)
    score=[[(0,Q(0)) for _ in range(m+1)] for _ in range(n+1)]
    move=[['' for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1,n+1): move[i][0]='a'
    for j in range(1,m+1): move[0][j]='b'
    for i in range(1,n+1):
        for j in range(1,m+1):
            options=[(score[i-1][j],'a'),(score[i][j-1],'b')]
            dist=abs(a[i-1]-b[j-1])
            if dist<=1:
                prev=score[i-1][j-1]
                options.append(((prev[0]+1,prev[1]-dist),'p'))
            score[i][j],move[i][j]=max(options,key=lambda v:v[0])
    pairs=[]
    i,j=n,m
    while i or j:
        step=move[i][j]
        if step=='p': pairs.append((i-1,j-1)); i-=1; j-=1
        elif step=='a': i-=1
        else: j-=1
    pairs.reverse()
    return pairs


def weight(l,r,cmin,cmax,dmin):
    u=max(abs(l-cmin),abs(l-cmax),abs(r-cmin),abs(r-cmax))
    denominator=u*u-dmin
    if denominator<=0:
        raise Stop('candidate mass has nonpositive denominator')
    return 1/denominator


MIRROR=Q(5000,1962848636289)
COORDINATES={
    'original_C_0.07_D_abs_0.2':(Q(-7,100),Q(7,100),Q(-1,5)),
    'paid_geometry09_uniform':(Q('0.0594957328'),Q('0.0637631130'),Q('0.0007983892')),
}


def manifest(samples):
    rows=[s['brackets'] for s in samples]
    pairs01=ordered_match(rows[0],rows[1]); pairs02=ordered_match(rows[0],rows[2])
    map1=dict(pairs01);map2=dict(pairs02)
    groups=[]
    ambiguous=[]
    mm=[mids(rr) for rr in rows]
    for i in sorted(set(map1)&set(map2)):
        indices=(i,map1[i],map2[i])
        selected=[rows[k][idx] for k,idx in enumerate(indices)]
        centers=[(Q(r['left'])+Q(r['right']))/2 for r in selected]
        halfs=[(Q(r['right'])-Q(r['left']))/2 for r in selected]
        candidates=[[j for j,x in enumerate(mm[k]) if abs(x-centers[0])<=1]
                    for k in (1,2)]
        is_ambiguous=any(len(c)>1 for c in candidates)
        if is_ambiguous:
            ambiguous.append({'t0_index':i,'candidate_indices_t05_t1':candidates,
                              'chosen_indices':list(indices)})
        static_l=min(Q(r['left']) for r in selected)-PAD
        static_r=max(Q(r['right']) for r in selected)+PAD
        slope=10*(centers[2]-centers[0])
        midpoint_defect=abs(centers[1]-(centers[0]+centers[2])/2)
        width=max(halfs[0],halfs[2],halfs[1]+midpoint_defect)+PAD
        groups.append({'id':len(groups)+1,'sample_indices':list(indices),
                       'sample_brackets':selected,
                       'planning_alignment_ambiguous':is_ambiguous,
                       'static_left':qstr(static_l),'static_right':qstr(static_r),
                       'affine_center_at_zero':qstr(centers[0]),
                       'affine_slope_per_t':qstr(slope),'affine_half_width':qstr(width),
                       'sampled_midpoint_line_defect':qstr(midpoint_defect),
                       'extra_padding':qstr(PAD)})
    overlaps=[]
    for left,right in zip(groups,groups[1:]):
        if Q(left['static_right'])>=Q(right['static_left']):
            overlaps.append([left['id'],right['id'],'static'])
        for t in (Q(0),Q(1,10)):
            lhi=Q(left['affine_center_at_zero'])+t*Q(left['affine_slope_per_t'])+Q(left['affine_half_width'])
            rlo=Q(right['affine_center_at_zero'])+t*Q(right['affine_slope_per_t'])-Q(right['affine_half_width'])
            if lhi>=rlo:
                overlaps.append([left['id'],right['id'],'affine',qstr(t)])
    mass={}
    for name,(cmin,cmax,dmin) in COORDINATES.items():
        static=MIRROR+sum((weight(Q(g['static_left']),Q(g['static_right']),cmin,cmax,dmin) for g in groups),Q(0))
        cells=[]
        for i in range(64):
            tlo=Q(i,640); thi=Q(i+1,640)
            total=MIRROR
            for g in groups:
                intercept=Q(g['affine_center_at_zero']);slope=Q(g['affine_slope_per_t']); half=Q(g['affine_half_width'])
                endpoints=(intercept+slope*tlo,intercept+slope*thi)
                total+=weight(min(endpoints)-half,max(endpoints)+half,cmin,cmax,dmin)
            cells.append(total)
        mass[name]={'static_mass_decimal':float(static),'affine_64_cell_minimum_decimal':float(min(cells)),
                    'static_reaches_0.59':static>=Q(59,100),'affine_reaches_0.59':min(cells)>=Q(59,100),
                    'coordinate_offset_min':qstr(cmin),'coordinate_offset_max':qstr(cmax),'D_lower':qstr(dmin),
                    'status':'exact rational calculation on hypothetical candidate tubes; locations are sampled only'}
    unmatched={str(k):[i for i in range(len(rows[k])) if i not in [g['sample_indices'][k] for g in groups]] for k in range(3)}
    rough_D=(Q('0.00142117673'),Q('0.09542258705'),Q('0.17873685257'))
    point_planning=[]
    cmin,cmax,_=COORDINATES['paid_geometry09_uniform']
    for t,dapprox in zip(TIMES,rough_D):
        total=MIRROR
        for g in groups:
            center=Q(g['affine_center_at_zero'])+t*Q(g['affine_slope_per_t'])
            half=Q(g['affine_half_width'])
            total+=weight(center-half,center+half,cmin,cmax,dapprox)
        point_planning.append({'time':qstr(t),'approximate_D_not_proof_input':qstr(dapprox),
                               'affine_point_mass_decimal':float(total)})
    minimum_distance=min(abs(Q(g['affine_center_at_zero'])+t*Q(g['affine_slope_per_t']))
                         -Q(g['affine_half_width']) for g in groups for t in (Q(0),Q(1,10)))
    return {'groups':groups,'aligned_groups':len(groups),'alignment_rule':'maximum ordered matches then minimum sum displacement, each displacement <=1; no identity claim',
            'alignment_ambiguities':ambiguous,'unmatched_indices':unmatched,'candidate_overlaps':overlaps,
            'mass_estimates':mass,'full_time_signs_verified':False,
            'affine_geometry':{'minimum_endpoint_distance_from_a':qstr(minimum_distance),
                               'maximum_absolute_slope':qstr(max(abs(Q(g['affine_slope_per_t'])) for g in groups)),
                               'maximum_half_width':qstr(max(Q(g['affine_half_width']) for g in groups)),
                               'all_affine_tubes_exterior':minimum_distance>Q(8,5)},
            'three_time_D_planning':{'status':'floating planning only; approximate historical D values are not new coordinate enclosures or proof premises',
                                    'provenance':'numerics/04_VCD_GT_LEHMER_DIAGNOSTIC_20261116.json, levels[0].D_by_time indices 0,8,16, rounded to eleven decimal places; midpoint is an existing floating sample, not a linear interpolation',
                                    'values':point_planning}}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--raw-dir',type=Path,default=Path('/private/tmp/vcd-gt-exterior'))
    parser.add_argument('--record',type=Path,required=True)
    parser.add_argument('--reprocess-raw',action='store_true',help='verify existing raw hash and recompute planning only; no source calls')
    args=parser.parse_args()
    if args.reprocess_raw:
        record=json.loads(args.record.read_text())
        raw_bytes=Path(record['raw']['path']).read_bytes()
        if sha256(raw_bytes).hexdigest()!=record['raw']['sha256']:
            raise Stop('raw source record hash mismatch')
        raw=json.loads(raw_bytes)
        if raw['status']!='complete':
            raise Stop('planning reprocessing needs the complete original diagnostic')
        record.setdefault('source_execution_script_sha256',record['script_sha256'])
        record['script_sha256']=sha256(Path(__file__).read_bytes()).hexdigest()
        record['planning_manifest']=manifest(raw['bracket_slices'])
        extra_input='numerics/04_VCD_GT_LEHMER_DIAGNOSTIC_20261116.json'
        record['input_sha256'][extra_input]=sha256((Path(__file__).resolve().parents[1]/extra_input).read_bytes()).hexdigest()
        record['postprocessing']={'source_calls':0,'raw_hash_verified':True,
                                  'scope':'exact affine exterior/disjointness summaries and explicitly floating three-time D planning; original source data and performance retained'}
        args.record.write_text(json.dumps(record,indent=2)+'\n')
        print(json.dumps({'reprocessed_without_source_calls':True,
                          'point_planning':record['planning_manifest']['three_time_D_planning']}),flush=True)
        return
    args.raw_dir.mkdir(parents=True,exist_ok=True)
    ctx.prec=BITS
    start=perf_counter();source=Source();samples=[];failure=None;planning=None
    benchmark={}
    try:
        bstart=perf_counter()
        for offset in GRID[:16]: source.value(Q(1,20),offset)
        elapsed=perf_counter()-bstart
        mean=source.source_seconds/source.calls
        projected_grid=mean*(len(GRID)*(1+72))
        benchmark={'points':16,'time':'1/20','xi_calls':source.calls,
                   'wall_seconds':elapsed,'source_seconds':source.source_seconds,
                   'seconds_per_xi':mean,'projected_grid_source_seconds':projected_grid}
        print(json.dumps({'benchmark':benchmark}),flush=True)
        if projected_grid>MAX_SECONDS: raise Stop('benchmark projects grid alone beyond source cap')
        for t in TIMES:
            result=gather(source,t);samples.append(result)
            print(json.dumps({'time_complete':qstr(t),'sign_intervals':result['selected_sign_intervals'],
                              'ambiguous_grid':len(result['quarter_grid_ambiguous_offsets']),
                              'xi_calls':source.calls,'source_seconds':source.source_seconds}),flush=True)
        planning=manifest(samples)
    except Stop as e:
        failure=str(e)
    raw={'status':'partial' if failure else 'complete','samples':list(source.cache.values()),
         'bracket_slices':samples,'benchmark':benchmark,'failure':failure}
    payload=json.dumps(raw,sort_keys=True,separators=(',',':')).encode()
    raw_path=args.raw_dir/'stage-a-raw.json'
    raw_path.write_bytes(payload)
    inputs=['notes/12_VCD_GT_E08_CANONICAL_XI_ORACLE_20261116.md',
            'notes/14_VCD_GT_E09_TENSOR_CERTIFICATE_BOUNDS_20261116.md',
            'numerics/04_VCD_GT_LEHMER_DIAGNOSTIC_20261116.json',
            'numerics/09_VCD_GT_JOINT_STRIP_GEOMETRY_20261116.json',
            'brainstorm/notes/09_VCD_GT_B06_EXTERIOR_BRACKET_ACQUISITION_DECISION_20261116.md',
            'research-progress/handoffs/VCD-GT-E04-r4-diagnostic.md']
    branch=Path(__file__).resolve().parents[1]
    record={'request':'VCD-GT-E04-r4-stage-A','date':'2026-11-16 America/New_York',
            'prepared_for':'Edward Baker','llm_assistance':'OpenAI Codex; inherited helper; actual model and effort unavailable',
            'status':'failed bounded diagnostic' if failure else 'completed sampled candidate diagnostic; not a uniform-time certificate',
            'script_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
            'input_sha256':{f:sha256((branch/f).read_bytes()).hexdigest() for f in inputs},
            'versions':{'python':platform.python_version(),'platform':platform.platform(),
                        'python_flint':flint.__version__},
            'precision_bits':BITS,'center':qstr(A),'offset_window':[-160,160],
            'grid_step':'1/4','times':[qstr(t) for t in TIMES],'maximum_bisections':6,
            'gaussian_step':'1/3','gaussian_cutoff':12,'source_constant_C':10**13,
            'source_lattice_error_upper':str(source.lattice.upper()),'source_tail_error_upper':str(source.tail.upper()),
            'source_error_scope':'complete-source sampled signs conditional on the extended-center E03-r7 majorant; no full-time assertion',
            'source_xi_calls':source.calls,'source_seconds':source.source_seconds,'wall_seconds':perf_counter()-start,
            'caps':{'xi_calls':MAX_CALLS,'source_seconds':MAX_SECONDS},'benchmark':benchmark,
            'sampled_slice_summary':[{k:v for k,v in row.items() if k!='brackets'} for row in samples],
            'failure':failure,'planning_manifest':planning,
            'raw':{'path':str(raw_path),'bytes':len(payload),'sha256':sha256(payload).hexdigest(),
                   'canonical_content_sha256':sha256(payload).hexdigest()},
            'measured_K_used_as_premise':False,'uniform_time_count_acquired':False,
            'historical_arrays_changed':False}
    args.record.write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps({'finished':record['status'],'calls':source.calls,'seconds':source.source_seconds,
                      'groups':planning['aligned_groups'] if planning else None,
                      'mass':planning['mass_estimates'] if planning else None,'failure':failure}),flush=True)


if __name__=='__main__':
    main()
