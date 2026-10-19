#!/usr/bin/env python3
"""GEO-T1 fixed B comparison, complete physical first jet and exact degree.

Prepared for Edward Baker,19October2026,with substantial LLM assistance.
Actual model gpt-6.1-sol (Codex),effort ultra. Requires python-flint.
The frozen contract specifies source/precision/budgets and cold-cost gate.
"""
from __future__ import annotations
import argparse,copy,hashlib,importlib.util,json,math,platform,sys,time
from fractions import Fraction as F
from pathlib import Path
import flint
from flint import arb,ctx

SYM=Path('papers/investigations-3/11_arithmetic_collision_rigidity/symmetries')
BASE=Path('papers/investigations-3/11_arithmetic_collision_rigidity/numerics/high_height_consumer/high_height_consumer.py')
CONTRACT=SYM/'notes/05_GEO_T1_MATCHED_WINDING_COMPARISON_CONTRACT_20261019.md'
CONTRACT_HASH='4ec9cb2f49bde49a0e1236b493d928b35d315c95681e754c7f49e65d93b445ba'
BASE_HASH='e96feb2b4c3e84de3025713b486fb8cf99fdd810f61366b79a0da188eb12535f'
BOX=(F(1,100),F(1,5),F(999),F(1001))
def check(v,msg):
 if not bool(v):raise ArithmeticError(msg)
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(p,name):
 s=importlib.util.spec_from_file_location(name,p);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
def text(v):return v.str(38,more=True)
def canon(v):return json.dumps(v,sort_keys=True,separators=(',',':')).encode()
def exact(v):
 check(v.is_exact() and v.is_finite(),'exact finite dyadic required');m,e=v.man_exp();return {'mantissa':str(m),'exponent':int(e)}
def record(v):return {'enclosure':text(v),'midpoint_dyadic':exact(v.mid()),'radius_dyadic':exact(v.rad())}

class MatchedEvaluator:
 def __init__(self,source,base):
  self.ev=copy.copy(source);self.ev.coeff_cache={};self.ev.calls=0;self.base=base;self.calls=0
  self.maximum_errors=[arb(0)for _ in range(3)];self.log=[];self.start=time.monotonic()
 def enclose(self,t0,t1,x0,x1):
  check(self.calls<512,'consumer512callbudget');check(time.monotonic()-self.start<60,'consumer60secondbudget')
  vals,budgets=self.ev.enclose(t0,t1,x0,x1);self.calls+=1
  dt=self.base.box(t0,t1)-self.base.A(self.ev.tc);dx=self.base.box(x0,x1)-self.base.A(self.ev.xc)
  # Each is a valid evaluation of the SAME midpoint polynomial. The same
  # quadrature/Taylor/mode/source error is already included in vals.
  out=[]
  for j in range(3):
   cs=[self.base.poly([self.ev.values[j+l+2*k]/self.ev.fact[l]for l in range(self.ev.L+1)],dx)/self.ev.fact[k]for k in range(self.ev.K+1)]
   alternate=self.base.poly(cs,-dt)+arb(0,budgets[j]['total'])
   check(vals[j].overlaps(alternate),'disjoint valid Hornerimages')
   both=vals[j].intersection(alternate);check(both.is_finite(),'nonfinite complete jet')
   out.append(both);self.maximum_errors[j]=max(self.maximum_errors[j],budgets[j]['total'])
  self.log.append({'t':[str(t0),str(t1)],'x':[str(x0),str(x1)],'complete_jets':[text(v)for v in out],
   'complete_added_errors':[text(b['total'])for b in budgets]})
  return out
 def metadata(self):return {'complete_enclosure_calls':self.calls,'maximum_complete_added_errors':[text(v)for v in self.maximum_errors],
  'cache_entries':len(self.ev.coeff_cache),'Horner_orders':'intersection of complete t-first and x-first evaluations; identical full errors','source_vertex_calls':0}

def norm_lower(v):return (v[0].abs_lower()**2+v[1].abs_lower()**2).sqrt().lower()
def direct_consumer(view):
 accepted=[];failed=[];calls_before=view.calls;first_failures=[];rejected=0;midpoint_calls=0
 def cell(t0,t1,x0,x1,depth,cap,stage):
  nonlocal rejected,midpoint_calls
  vals=view.enclose(t0,t1,x0,x1);lower=norm_lower(vals);method='Cartesian first-jet norm'
  if not lower>0:
   xm=(x0+x1)/2;mv=view.enclose(t0,t1,xm,xm);midpoint_calls+=1
   derivative=(vals[1].abs_upper()**2+vals[2].abs_upper()**2).sqrt().upper()
   propagated=(norm_lower(mv)-view.base.A((x1-x0)/2)*derivative).lower()
   if propagated>lower:lower=propagated;method='paid spatial-midpoint propagation'
  if lower>0:
   accepted.append({'t':[str(t0),str(t1)],'x':[str(x0),str(x1)],'radius_lower':text(lower),'method':method,'depth':depth,'stage':stage});return True
  rejected+=1
  if depth>=cap:
   failed.append((t0,t1,x0,x1,depth));return False
  xm=(x0+x1)/2;a=cell(t0,t1,x0,xm,depth+1,cap,stage);b=cell(t0,t1,xm,x1,depth+1,cap,stage);return a and b
 tlo,thi,xlo,xhi=BOX
 cell(tlo,thi,xlo,xhi,0,6,'full-time')
 first_failures=list(failed);failed=[]
 for _,_,xa,xb,d in first_failures:
  for k in range(4):
   ta=tlo+(thi-tlo)*F(k,4);tb=tlo+(thi-tlo)*F(k+1,4)
   cell(ta,tb,xa,xb,d,9,'four-time-slab fallback')
 # Verify every exact horizontal elementary strip is covered for every
 # elementary time slab; a boundary-only or partial cover cannot pass.
 times=sorted({tlo,thi}|{F(v)for r in accepted for v in r['t']});xs=sorted({xlo,xhi}|{F(v)for r in accepted for v in r['x']})
 coverage=not failed
 for ta,tb in zip(times,times[1:]):
  pieces=sorted((F(r['x'][0]),F(r['x'][1]))for r in accepted if F(r['t'][0])<=ta and tb<=F(r['t'][1]))
  cursor=xlo
  for xa,xb in pieces:
   if xa>cursor:coverage=False
   cursor=max(cursor,xb)
  if cursor<xhi:coverage=False
 check(coverage or bool(failed),'unexplained direct coverage gap')
 return {'status':'pass'if coverage else'inconclusive','coverage_verified':coverage,'accepted_cells':accepted,
  'unresolved_cells':[[str(v)for v in r]for r in failed],'initial_unresolved_strips':[[str(v)for v in r]for r in first_failures],
  'rejected_parent_cells':rejected,'midpoint_calls':midpoint_calls,'calls':view.calls-calls_before,
  'minimum_physical_radius_over_Gc':text(min(arb(r['radius_lower']).lower()for r in accepted))if accepted else'0',
  'normalization':'physical sqrt(H^2+Hx^2)/fixed positive Gc; winding margin is a separate boundary quantity'}

def mathematical(record):
 def clean(v):
  if isinstance(v,dict):return {k:clean(x)for k,x in v.items()if k not in ('timing_seconds','setup_seconds','jet_seconds','seconds','callbacks','jet_callbacks','mathematical_content_sha256')}
  if isinstance(v,list):return[clean(x)for x in v]
  return v
 return clean(record)

def run(repo,bits):
 check(bits in (192,256),'precision192or256required');check(sha(repo/CONTRACT)==CONTRACT_HASH,'frozen contract changed')
 check(sha(repo/BASE)==BASE_HASH,'source evaluator changed')
 helpers=load(Path(__file__).with_name('winding_helpers.py'),'geo_winding');base=load(repo/BASE,'geo_source')
 ctx.prec=bits;start=time.monotonic();source=base.bounded(lambda:base.WholeCellEvaluator(bits),60)
 setup=base.setup_record(source,base.provenance(repo,'gpt-6.1-sol','ultra',bits))
 results={};timings={}
 # Alternate order between precisions, with independent empty caches.
 order=['winding','direct']if bits==192 else['direct','winding']
 for method in order:
  before=time.monotonic();view=MatchedEvaluator(source,base)
  try:
   if method=='winding':
    r=base.bounded(lambda:helpers.boundary_acceptance(view.enclose,BOX,max_depth=9,max_calls=512),60)
    check(view.calls==r['calls'],'windingcallledger')
    if r['status']=='pass':
     check(r['degree']==0,'nonzero degree accepted');r['minimum_boundary_halfplane_margin_over_Gc']=str(min(F(s['margin_lower'])for s in r['boundary']))
   else:r=base.bounded(lambda:direct_consumer(view),60)
  except (base.BudgetStop,ArithmeticError,RuntimeError) as exc:r={'status':'inconclusive','failure':str(exc),'type':type(exc).__name__}
  r['source_evaluation']=view.metadata();results[method]=r;timings[method]=time.monotonic()-before
 common=source.setup_seconds
 cold={k:common+timings[k]for k in results};speedup=cold['direct']/cold['winding']
 # An already covered box cannot earn coverage. Report actual status and gate,
 # without changing to consumer-only or amortized setup metric afterwards.
 both=results['winding']['status']=='pass'and results['direct']['status']=='pass'
 benefit=both and speedup>=2
 out={'schema':'geo-t1-matched-winding-v1','date':'2026-10-19','timezone':'America/New_York','prepared_for':'Edward Baker',
  'actual_model':'gpt-6.1-sol (Codex)','actual_effort':'ultra','llm_assistance':'substantial; internal same-model research; no specialist review',
  'runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'precision_bits':bits},
  'source_sha256':{str(BASE):sha(repo/BASE),str(CONTRACT):sha(repo/CONTRACT),'winding_helpers.py':sha(Path(__file__).with_name('winding_helpers.py'))},
  'producer_sha256':sha(__file__),'domain':{'t':[str(BOX[0]),str(BOX[1])],'x':[str(BOX[2]),str(BOX[3])]},
  'normalization':'physical(H,Hx,Hxx)/fixed positive Gc; same complete first jet and source acquisition',
  'common_setup':setup,'consumer_order':order,'winding':results['winding'],'direct':results['direct'],
  'timing_seconds':{'common_fresh_setup':common,'consumer':timings,'cold_total':cold,'direct_over_winding_cold_ratio':speedup,
   'best_possible_cold_ratio_if_winding_free':cold['direct']/common,'total_execution':time.monotonic()-start},
  'decision':{'both_certify_closed_B':both,'new_coverage':False,'primary_twofold_cold_cost_gain_observed':benefit,
   'continuation':'stop fixed B comparison; no milestone'if not benefit else'review observed cost gain before continuation',
   'scope':'timing observations only; no uniform hardware claim, new signed estimate, interior winding-radius bound, coverage, Newman or global result'},
  'source_premise':'complete reflected theta contour and all tails; no theta constants substituted in controls'}
 out['mathematical_content_sha256']=hashlib.sha256(canon(mathematical(out))).hexdigest()
 return out

def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',type=Path,required=True);p.add_argument('--precision',type=int,choices=[192,256],required=True);p.add_argument('--output',type=Path,required=True);a=p.parse_args();d=run(a.repo.resolve(),a.precision);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2)+'\n');print(json.dumps({'output':str(a.output),'winding':{k:d['winding'].get(k)for k in ('status','degree','calls','accepted_segments')},'direct':{k:d['direct'].get(k)for k in ('status','calls','minimum_physical_radius_over_Gc')},'timing':d['timing_seconds'],'bytes':a.output.stat().st_size}))
if __name__=='__main__':main()
