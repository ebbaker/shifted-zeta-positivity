#!/usr/bin/env python3
"""Fresh interval replay, closed-cover checks and adversarial controls.
Prepared for Edward Baker,18October2026,with substantial LLM assistance.
Authoring gpt-6.1-sol,actualeffortultra. Same-model internal verification.
"""
from __future__ import annotations
import argparse,copy,hashlib,json,platform,time
from pathlib import Path
from fractions import Fraction as F
from flint import arb,acb,ctx
import flint
import high_height_consumer as base
import compare_high_height_real as real


def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def cover(rows,axis,ts,lo,hi):
 allowed={(str(a),str(b))for a,b in zip(ts,ts[1:])}
 base.check(rows and all(tuple(r['t'])in allowed for r in rows),'unexpected time slab')
 for a,b in zip(ts,ts[1:]):
  cells=sorted([r for r in rows if r['t']==[str(a),str(b)]],key=lambda r:F(r[axis][0]))
  base.check(cells and F(cells[0][axis][0])==lo and F(cells[-1][axis][1])==hi,'closed cover endpoints')
  base.check(all(lo<=F(r[axis][0])<F(r[axis][1])<=hi for r in cells),'invalid cell orientation/domain')
  base.check(all(F(x[axis][1])==F(y[axis][0])for x,y in zip(cells,cells[1:])),'closed cover gap or overlap')
 return True

def main():
 p=argparse.ArgumentParser();p.add_argument('--repo',type=Path,required=True);p.add_argument('--records',type=Path,required=True);p.add_argument('--output',type=Path,required=True);p.add_argument('--execution-model',required=True);p.add_argument('--execution-effort',required=True);a=p.parse_args()
 started=time.monotonic();paths={k:a.records/(k+'.json')for k in ['SETUP','SIGNED_CONSUMER','VERTICAL_WALL','REAL_COMPARISON']}
 data={k:json.loads(path.read_text())for k,path in paths.items()};setup=data['SETUP'];signed=data['SIGNED_CONSUMER'];wall=data['VERTICAL_WALL'];comparison=data['REAL_COMPARISON']
 base.validate_setup(setup,a.repo)
 for obj in [signed,wall]:base.check(obj['source_sha256']==digest(base.__file__),'consumer code hash mismatch')
 base.check(comparison['script_sha256']==digest(real.__file__),'real comparator code hash mismatch')
 for key,name in [('setup','SETUP'),('signed','SIGNED_CONSUMER'),('wall','VERTICAL_WALL')]:
  base.check(comparison['input_sha256'][key]==digest(paths[name]),'comparison input hash mismatch')
 signedtimes=list(map(F,['1/100','23/400','21/200','61/400','1/5']));walltimes=[F(k,20)for k in range(5)]
 cover(signed['repair_cells'],'x',signedtimes,F(999),F(1001));cover(wall['cells'],'y',walltimes,F(0),F(1))
 # Reintegrate at a new precision; do not accept cached PASS labels.
 ctx.prec=256;fresh=base.bounded(lambda:base.WholeCellEvaluator(256),60)
 fresh_signed=[]
 for r in signed['repair_cells']:
  ta,tb=map(F,r['t']);xa,xb=map(F,r['x']);values,budgets=fresh.enclose(ta,tb,xa,xb)
  E=base.square(values[0])+base.square(values[1]);excess=base.square(values[1])-values[0]*values[2]-E/100
  base.check(excess>arb('8.26087e-5'),'fresh signed excess lower bound')
  base.check(all(values[j].overlaps(arb(r['jet'][j]))for j in range(3)),'fresh saved signed jets disjoint')
  fresh_signed.append({'t':r['t'],'x':r['x'],'excess_norm2':base.s(excess),'added_errors_norm':[base.s(q['total'])for q in budgets]})
 wc=base.prepare_wall(fresh);fresh_wall=[]
 for r in wall['cells']:
  ta,tb=map(F,r['t']);ya,yb=map(F,r['y']);values,budgets=base.wall_enclose(fresh,ta,tb,ya,yb,wc)
  margin=max(values[0].real.abs_lower(),values[0].imag.abs_lower())
  base.check(margin>arb('0.00425'),'fresh complex wall margin')
  base.check(all(values[j].real.overlaps(arb(r['jet'][j]['real'])) and values[j].imag.overlaps(arb(r['jet'][j]['imag']))for j in range(3)),'fresh saved wall jets disjoint')
  fresh_wall.append({'t':r['t'],'y':r['y'],'margin_norm':base.s(margin),'added_errors_norm':[base.s(q['total'])for q in budgets]})
 fresh_seconds=time.monotonic()-started
 # Independent real-contour midpoint integrals from the matched run pay
 # their own physical tails. Recompute every signed and wall lower margin.
 raw=comparison['attempts'][-1];base.check(raw['status']=='pass','real midpoint accuracy gate failed')
 rev,hm=real.attach_real(setup,raw,768);real_signed=real.replay_cells(rev,signed);real_wall=real.replay_wall(rev,wall)
 negatives=[]
 def reject(name,fn):
  try:fn()
  except (ArithmeticError,ValueError,KeyError,FileNotFoundError)as exc:negatives.append({'case':name,'rejected':True,'reason':str(exc)})
  else:raise ArithmeticError('negative control accepted: '+name)
 bad=copy.deepcopy(setup);bad['source_sha256']='0'*64;reject('altered evaluator hash',lambda:base.load_setup(bad))
 bad=copy.deepcopy(setup);bad['frozen_parameters']['first_omitted_mode']=13;reject('foreign mode cutoff',lambda:base.load_setup(bad))
 bad=copy.deepcopy(setup);bad['domain']['x']=[998,1001];reject('foreign physical domain',lambda:base.load_setup(bad))
 bad=copy.deepcopy(setup);bad['setup']['midpoint_jets'].pop();reject('incomplete midpoint cache',lambda:base.load_setup(bad))
 bad=copy.deepcopy(setup);bad['setup']['midpoint_jets'][0]['quadrature_radius_dyadic']['mantissa']='-1';reject('negative quadrature radius',lambda:base.load_setup(bad))
 bad=copy.deepcopy(signed['repair_cells']);bad.pop();reject('missing signed cell',lambda:cover(bad,'x',signedtimes,F(999),F(1001)))
 bad=copy.deepcopy(wall['cells']);bad.pop();reject('missing wall cell',lambda:cover(bad,'y',walltimes,F(0),F(1)))
 reject('missing input file',lambda:json.loads((a.records/'INTENTIONALLY_ABSENT_INPUT.json').read_text()))
 base.check(not(arb(0)>0)and not(arb('0.001')>arb('0.001')),'strict equality accepted')
 negatives.append({'case':'strict equality at zero and wall allowance','rejected':True})
 # Exact polynomial backward-heat event in this same cached-polynomial lane.
 toy=base.load_setup(setup);ctx.prec=192
 toy.values=[arb(0)for _ in range(51)];toy.values[0]=-arb(1)/100;toy.values[2]=arb(2)
 toy.radii=[arb(0)for _ in range(51)];toy.majorant=arb(2);toy.uniform_tails=([arb(0)]*3,[arb(0)]*3);toy.coeff_cache={}
 v,b=toy.enclose(F(99,1000),F(101,1000),F(999999,1000),F(1000001,1000))
 excess=base.square(v[1])-v[0]*v[2]-(base.square(v[0])+base.square(v[1]))/100
 base.check(v[0].contains(0)and v[1].contains(0)and not excess>0,'polynomial event passed signed gate')
 toywall={'M':arb(2),'mode':[arb(0)]*3,'source':[arb(0)]*3,'calls':0,'coeff_cache':{}}
 values,b=base.wall_enclose(toy,F(99,1000),F(101,1000),F(0),F(1,1000),toywall)
 base.check(values[0].real.contains(0)and values[0].imag.contains(0),'polynomial wall event not enclosed')
 base.check(not max(values[0].real.abs_lower(),values[0].imag.abs_lower())>arb('1e-3'),'polynomial event passed wall gate')
 negatives.append({'case':'exact polynomial heat event','field':'(z-1000)^2-2(t-1/10)','event':['1/10','1000'],'signed_rejected':True,'wall_rejected':True,'initial_reality_premise':'fails: initial roots1000 +/- i/sqrt(5)','theta_truncation_constants_used':False})
 report={'date':'2026-10-18','timezone':'America/New_York','prepared_for':'Edward Baker','actual_model':a.execution_model,'actual_effort':a.execution_effort,'llm_assistance':'substantial; fresh same-model interval replay','python':platform.python_version(),'python_flint':flint.__version__,'script_sha256':digest(__file__),'evaluator_sha256':digest(base.__file__),'real_comparator_sha256':digest(real.__file__),'input_sha256':{k:digest(p)for k,p in paths.items()},'fresh_shifted_precision_bits':256,'fresh_shifted_setup_seconds':fresh.setup_seconds,'fresh_shifted_callbacks':fresh.callbacks,'fresh_signed_cells':fresh_signed,'fresh_wall_cells':fresh_wall,'fresh_minimum_signed_excess_norm2':base.s(min(arb(r['excess_norm2']).lower()for r in fresh_signed)),'fresh_minimum_wall_margin_norm':base.s(min(arb(r['margin_norm']).lower()for r in fresh_wall)),'fresh_shifted_replay_seconds':fresh_seconds,'real_midpoint_precision_bits':768,'real_signed_minimum_excess_norm2':base.s(min(arb(r['excess_norm2']).lower()for r in real_signed)),'real_wall_replay':real_wall,'negative_controls':negatives,'exact_closed_coverages_verified':True,'global_Newman_bound':False,'status':'pass','total_replay_seconds':time.monotonic()-started}
 a.output.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':'pass','signed_cells':len(fresh_signed),'wall_cells':len(fresh_wall),'negative_controls':len(negatives),'seconds':report['total_replay_seconds']}))
if __name__=='__main__':main()
