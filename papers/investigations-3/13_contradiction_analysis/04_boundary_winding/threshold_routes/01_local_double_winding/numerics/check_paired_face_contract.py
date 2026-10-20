#!/usr/bin/env python3
"""Exact finite controls for the BW-01 paired-face payment.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Actual model gpt-6-astra (Codex), effort max. Same-assistant verification.
No theta quadrature, actual theta event, or RH exclusion is computed.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import platform
import subprocess


def require(test, message):
    if not test:
        raise AssertionError(message)


def clean(p):
    return {k: F(v) for k, v in p.items() if v}


def add(*ps):
    out = {}
    for p in ps:
        for k, v in p.items():
            out[k] = out.get(k, F(0)) + v
    return clean(out)


def scale(p, c):
    return clean({k: c*v for k, v in p.items()})


def derivative(p, axis):
    out = {}
    for k, v in p.items():
        if k[axis]:
            key = list(k)
            key[axis] -= 1
            out[tuple(key)] = k[axis]*v
    return clean(out)


def restrict_time(p, t):
    out = {}
    for (i, j), v in p.items():
        out[(0, j)] = out.get((0, j), F(0)) + v*t**i
    return clean(out)


def power_interval(lo, hi, n):
    if not n:
        return F(1), F(1)
    if n % 2:
        return lo**n, hi**n
    return (F(0) if lo <= 0 <= hi else min(lo**n, hi**n),
            max(lo**n, hi**n))


def enclose(p, start, end, error=F(0)):
    require(error >= 0, 'negative uncertainty')
    bounds = [(min(a,b), max(a,b)) for a,b in zip(start,end)]
    lo, hi = -error, error
    for (i,j), c in p.items():
        ti, yj = power_interval(*bounds[0], i), power_interval(*bounds[1], j)
        vals = [c*a*b for a in ti for b in yj]
        lo += min(vals)
        hi += max(vals)
    return lo, hi


def halfplane(p, px, start, end, error):
    for axis, poly in enumerate((p,px)):
        lo, hi = enclose(poly,start,end,error)
        if lo > 0:
            return axis, 1
        if hi < 0:
            return axis, -1
    return None


def polygon_winding(vertices):
    require(all(x or y for x,y in vertices), 'origin vertex')
    winding = 0
    for (ax,ay),(bx,by) in zip(vertices,vertices[1:]+vertices[:1]):
        cross = ax*by-ay*bx
        require(cross or ax*bx+ay*by > 0, 'edge meets origin')
        if ay <= 0 < by and cross > 0:
            winding += 1
        elif by <= 0 < ay and cross < 0:
            winding -= 1
    return winding


def certify(p, error=F(0), reverse=False, omit_wall=False):
    corners = [(F(-1),F(-1)),(F(1),F(-1)),
               (F(1),F(1)),(F(-1),F(1))]
    if reverse:
        corners = [corners[0]] + list(reversed(corners[1:]))
    edges = list(zip(corners,corners[1:]+corners[:1]))
    if omit_wall:
        edges.pop()
    require(len(edges)==4 and all(edges[i][1]==edges[(i+1)%4][0]
                                for i in range(4)), 'incomplete boundary')
    px = derivative(p,1)
    accepted = []
    calls = 0

    def cover(start,end,depth):
        nonlocal calls
        calls += 1
        if calls > 2048:
            return False
        hp = halfplane(p,px,start,end,error)
        if hp is not None:
            accepted.append((start,end,hp))
            return True
        if depth == 12:
            return False
        mid = tuple((a+b)/2 for a,b in zip(start,end))
        return cover(start,mid,depth+1) and cover(mid,end,depth+1)

    for start,end in edges:
        if not cover(start,end,0):
            return {'status':'inconclusive','complete_cover':False,
                    'calls':calls,'accepted_segments':len(accepted)}
    require(all(accepted[i][1]==accepted[(i+1)%len(accepted)][0]
                for i in range(len(accepted))), 'segment cover gap')
    vertices = []
    for i in range(len(accepted)):
        v = [0,0]
        for axis,sign in (accepted[i-1][2],accepted[i][2]):
            require(v[axis] in (0,sign), 'incompatible incident halfplanes')
            v[axis] = sign
        vertices.append(tuple(v))
    raw = polygon_winding(vertices)
    physical = -raw if reverse else raw
    return {'status':'certified','complete_cover':True,'calls':calls,
            'accepted_segments':len(accepted),'traversal_winding':raw,
            'physical_winding':physical,'collision_exclusion':physical==0,
            'polygon':vertices,
            'segments':[{'from':list(map(str,a)), 'to':list(map(str,b)),
                         'strict_component':hp[0], 'sign':hp[1]}
                        for a,b,hp in accepted]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo',type=Path,required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    base = Path('papers/investigations-3/13_contradiction_analysis/04_boundary_winding')
    route = base/'threshold_routes/01_local_double_winding'
    q = {(0,2):F(1,2),(1,0):F(-1)}
    z = F(1,8)
    quartic = add(q,scale({(0,3):1,(1,1):-6},z/2),
                  scale({(0,4):1,(1,2):-12,(2,0):12},z*z/8))
    for name,p in [('quadratic',q),('quartic',quartic)]:
        require(not add(derivative(p,0),derivative(derivative(p,1),1)),
                name+': heat equation')
        require(p.get((0,0),0)==0 and derivative(p,1).get((0,0),0)==0,
                name+': exact center event')
        require(derivative(derivative(p,1),1).get((0,0),0)==1,
                name+': exact normalized curvature')
    # The complete pair for a quartic equals its threshold second derivative.
    odd_pair = scale(add(restrict_time(quartic,-1),
                         scale(restrict_time(quartic,1),-1)),F(1,2))
    require(odd_pair==restrict_time(derivative(derivative(quartic,1),1),0),
            'quartic odd time pair')
    # Own physical source: a=1, r=1/8, h2=8, M3=24(a+r)=27, M4=24.
    e0 = F(7,6)*F(27,8)*z + F(1,2)*F(24,8)*z*z
    e1 = F(3,2)*F(27,8)*z
    require(e0==F(33,64) and e1==F(81,128), 'quartic allowances')
    eps2 = e0*e0+e1*e1
    require(eps2==F(10917,16384) and eps2 < F(41,50)**2,
            'quartic complete homotopy allowance below 0.82')
    require(2*24**2-3*8*24==9*8**2,'quartic mirror equality')
    cases = {}
    for name,p,w in [('quadratic',q,-1),('quartic',quartic,-1),
                     ('negative_quartic',scale(quartic,-1),-1),
                     ('constant',{(0,0):F(1)},0)]:
        result = certify(p)
        require(result['status']=='certified' and result['physical_winding']==w,
                name+': wrong winding')
        cases[name] = result
    reversed_result = certify(quartic,reverse=True)
    require(reversed_result['traversal_winding']==1 and
            reversed_result['physical_winding']==-1,'orientation transfer')
    cases['reversed_quartic'] = reversed_result
    for name,p,error in [('boundary_event',add(q,{(0,0):F(1)}),F(0)),
                         ('uncertain_constant',{(0,0):F(1)},F(1))]:
        result = certify(p,error=error)
        require(result['status']=='inconclusive',name+': false certificate')
        cases[name] = result
    try:
        certify(q,omit_wall=True)
    except AssertionError as e:
        require(str(e)=='incomplete boundary','wrong coverage rejection')
        cases['omitted_wall'] = {'status':'rejected','reason':str(e)}
    else:
        raise AssertionError('omitted wall accepted')
    source_paths = [route/'notes/02_PAIRED_FACE_CONTRACT_20261019.md',
                    route/'numerics/check_paired_face_contract.py',
                    base/'research-overview/01_THRESHOLD_BOUNDARY_WINDING_RESEARCH_PROGRAM_20261019.md',
                    Path('papers/quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex'),
                    Path('papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/04_SPACETIME_INDEX_AND_MARKED_TOPOLOGY_20261015.md'),
                    Path('papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/06_WALL_FLUX_AND_CERTIFIED_THETA_WINDING_20261015.md')]
    receipt = {'status':'PASS','prepared_for':'Edward Baker',
               'llm_assistance':'Substantial; same-assistant checks',
               'model':'gpt-6-astra','reasoning_effort':'max',
               'scope':'Finite exact polynomial controls only; no theta event or theta integration.',
               'created_utc':datetime.now(timezone.utc).isoformat(),
               'python':platform.python_version(),
               'git_head':subprocess.check_output(['git','rev-parse','HEAD'],cwd=args.repo,text=True).strip(),
               'source_sha256':{str(p):hashlib.sha256((args.repo/p).read_bytes()).hexdigest()
                                for p in source_paths},
               'arithmetic':'Python Fraction; whole-segment interval bounds and exact polygon degree',
               'quartic_parameters':{'T':'1/4','a':'1','r':'1/8','h2':'8','M3':'27','M4':'24'},
               'quartic_bound':{'epsilon0':str(e0),'epsilon1':str(e1),
                                'epsilon_squared':str(eps2),
                                'epsilon_strict_upper':'41/50',
                                'scaled_boundary_margin_strict_lower':'9/50'},
               'identities':['heat PDE','exact center cancellation','nonzero curvature',
                             'quartic odd time pair','quartic mirror equality'],
               'cases':cases}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps({'status':'PASS','cases':len(cases),'output':str(args.output),
                      'quartic_epsilon_squared':str(eps2),
                      'scope':receipt['scope']},sort_keys=True))


if __name__=='__main__':
    main()
