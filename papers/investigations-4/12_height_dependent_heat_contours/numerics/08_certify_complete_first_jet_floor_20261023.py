#!/usr/bin/env python3
"""Bounded full-volume complete-theta first-jet floor on the original pilot box.

Prepared for Edward Baker, 2026-10-23. Substantial LLM assistance:
gpt-6-astra (Codex), effort ultra. No root disks or root data are used.
Stdout JSON unless --output; source core must be an importable sibling.
"""
import argparse,hashlib,json,time
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb
import hdc13_theta_core as source_module
from hdc13_theta_core import ActualHeatCore,rec

def A(x):
    x=F(x);return arb(x.numerator)/x.denominator

def cell(x0,x1,y0,y1):
    return acb(arb(A((x0+x1)/2),A((x1-x0)/2)),arb(A((y0+y1)/2),A((y1-y0)/2)))

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path)
    args=ap.parse_args();start=time.monotonic();core=ActualHeatCore();leaves=[];calls=0;rejected=0;checks=[]
    def check(name,ok):
        if not ok:raise AssertionError(name)
        checks.append(name)
    target=arb(1)/10**13
    def cover(x0,x1,y0,y1,depth=0):
        nonlocal calls,rejected
        calls+=1
        if calls>4096 or depth>22:raise RuntimeError('bounded full-volume budget exceeded')
        z=cell(x0,x1,y0,y1);jets=core.jets(z,1)
        floor=sum((v.abs_lower()**2 for v in jets),arb(0)).abs_lower()
        if floor>target:
            leaves.append({'bounds':[x0,x1,y0,y1],'floor':floor,
                'H_upper':jets[0].abs_upper(),'Hz_upper':jets[1].abs_upper(),'depth':depth})
            return
        rejected+=1
        if x1-x0>=y1-y0:
            mid=(x0+x1)/2;cover(x0,mid,y0,y1,depth+1);cover(mid,x1,y0,y1,depth+1)
        else:
            mid=(y0+y1)/2;cover(x0,x1,y0,mid,depth+1);cover(x0,x1,mid,y1,depth+1)
    cover(F(26),F(46),F(-2),F(2))
    check('full-volume area exactly80',sum(((v['bounds'][1]-v['bounds'][0])*(v['bounds'][3]-v['bounds'][2]) for v in leaves),F(0))==80)
    # Binary subdivisions of a box already guarantee disjoint interiors and
    # coverage; independently audit all leaf intersections and their bounds.
    check('all leaf boxes lie in original spatial rectangle',all(F(26)<=v['bounds'][0]<v['bounds'][1]<=46 and F(-2)<=v['bounds'][2]<v['bounds'][3]<=2 for v in leaves))
    overlap=False
    for i,v in enumerate(leaves):
        x0,x1,y0,y1=v['bounds']
        for w in leaves[:i]:
            a,b,c,d=w['bounds']
            if max(x0,a)<min(x1,b) and max(y0,c)<min(y1,d):overlap=True
    check('leaf interiors pairwise disjoint',not overlap)
    floor=min(v['floor'] for v in leaves)
    check('uniform complete first-jet norm floor positive',floor>target)
    check('bounded number of cell calls',calls<=4096)
    rows=[{'spatial_bounds':[str(x) for x in v['bounds']],
        'first_jet_squared_norm_lower':rec(v['floor']),
        'H_upper':rec(v['H_upper']),'Hz_upper':rec(v['Hz_upper']),'depth':v['depth']} for v in leaves]
    data={'status':'PASS','date':'2026-10-23','prepared_for':'Edward Baker',
        'model':'gpt-6-astra (Codex)','reasoning_effort':'ultra','llm_assistance':True,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'core_sha256':hashlib.sha256(Path(source_module.__file__).read_bytes()).hexdigest(),
        'exact_box':{'x':['26','46'],'y':['-2','2'],'Re_tau':['-1/10000','1/10000'],'Im_tau':['-1/10000','1/10000']},
        'source_oracle':core.metadata(),'accepted_spatial_cells':len(leaves),'cell_calls':calls,
        'rejected_parents':rejected,'maximum_depth':max(v['depth'] for v in leaves),
        'uniform_first_jet_squared_norm_lower':rec(floor),'target_floor':'1/10000000000000',
        'uniform_H_upper':rec(max(v['H_upper'] for v in leaves)),
        'uniform_Hz_upper':rec(max(v['Hz_upper'] for v in leaves)),
        'leaf_records':rows,'assertions':len(checks),'checks':checks,'elapsed_seconds':time.monotonic()-start,
        'establishes':['The complete first jet (H_tau,H_tau,z) is nonzero throughout the entire original closed spatial rectangle times the original complex time square.',
            'A quantitative uniform positive denominator floor is supplied without internal root isolation or omitted root disks.'],
        'does_not_establish':['The actual cap/complement integrals or any height-uniform estimate.',
            'An advantage over a direct complete-source interior method; this computation is itself such an interior check.']}
    text=json.dumps(data,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    else:print(text,end='')
if __name__=='__main__':main()
