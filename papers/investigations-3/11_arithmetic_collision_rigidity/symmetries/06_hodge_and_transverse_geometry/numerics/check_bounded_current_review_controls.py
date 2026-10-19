#!/usr/bin/env python3
"""Fresh-source control interpretation and actual S06-T2 API challenges.

19 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Actual model gpt-6.1-sol (Codex), effort ultra. Same-model internal review.
"""
import argparse
from fractions import Fraction as F
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
from flint import arb,ctx

def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def load(path,name):
    spec=importlib.util.spec_from_file_location(name,path);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod);return mod

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--repo',type=Path,required=True);p.add_argument('--producer',type=Path,required=True)
    p.add_argument('--contract',type=Path,required=True)
    p.add_argument('--source-control-replay',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args();REPO=args.repo;PRODUCER=args.producer;CONTRACT=args.contract
    ctx.prec=192;prod=load(PRODUCER,'s06_t2_review_controls');base=prod.load_base(REPO)
    vals=[arb(1),arb(1),arb(-1),arb(0)]
    domain=[F(1,100),F(1,5),F(999),F(1001)]
    def ledger(v):return {'polynomial_image':v,'quadrature':arb(0),'taylor':arb(0),'mode':arb(0),'source':arb(0),'total':arb(0)}
    validledgers=[ledger(v)for v in vals];rejected=[]
    def reject(label,fn):
        try:fn()
        except (ArithmeticError,KeyError,ValueError,TypeError):rejected.append(label)
        else:raise ArithmeticError('actual helper accepted invalid fixture: '+label)
    reject('three jets',lambda:prod.measure(base,vals[:3],*domain))
    reject('five jets',lambda:prod.measure(base,vals+[arb(0)],*domain))
    reject('NaN jet',lambda:prod.measure(base,[arb('nan')]+vals[1:],*domain))
    reject('infinite jet',lambda:prod.measure(base,[arb('inf')]+vals[1:],*domain))
    reject('reversed time',lambda:prod.measure(base,vals,domain[1],domain[0],*domain[2:]))
    reject('reversed space',lambda:prod.measure(base,vals,*domain[:2],domain[3],domain[2]))
    reject('time outside pilot',lambda:prod.measure(base,vals,F(0),*domain[1:]))
    reject('space outside pilot',lambda:prod.measure(base,vals,*domain[:3],F(1002)))
    reject('three error ledgers',lambda:prod.measure(base,vals,*domain,validledgers[:3]))
    bad=[dict(v)for v in validledgers];bad[0]['total']=arb(-1)
    reject('negative total allowance',lambda:prod.measure(base,vals,*domain,bad))
    bad2=[dict(v)for v in validledgers];bad2[0]['source']=arb(-1)
    reject('negative component allowance',lambda:prod.measure(base,vals,*domain,bad2))
    bad3=[dict(v)for v in validledgers];bad3[0]['total']=arb('nan')
    reject('nonfinite total allowance',lambda:prod.measure(base,vals,*domain,bad3))
    bad4=[dict(v)for v in validledgers];bad4[0]['polynomial_image']=arb('nan')
    reject('nonfinite nominal image',lambda:prod.measure(base,vals,*domain,bad4))
    reject('unsupported run precision',lambda:prod.run(REPO,160,'gpt-6.1-sol','ultra',CONTRACT))
    reject('blank run model',lambda:prod.run(REPO,192,'','ultra',CONTRACT))
    reject('blank run effort',lambda:prod.run(REPO,192,'gpt-6.1-sol','',CONTRACT))
    with tempfile.TemporaryDirectory(prefix='s06-t2-bad-contract-')as temporary:
        fake=Path(temporary)/CONTRACT.name;fake.write_text(CONTRACT.read_text()+'\nchanged\n')
        reject('altered same-name comparison contract',lambda:prod.run(REPO,192,'gpt-6.1-sol','ultra',fake))
    # This challenges the actual finite helper at its declared pilot domain.
    # Curvatures and third derivatives below are synthetic exact event jets;
    # they are not silently labeled as source-specific h3 certificates.
    synthetic=[]
    for h2,h3 in ((2,0),(7,-2),(5,91)):
        row,C,D=prod.measure(base,[arb(0),arb(0),arb(h2),arb(h3)],*domain)
        if row['independently_signed']or not C.is_zero()or not D.is_zero():raise ArithmeticError('exact event accepted')
        synthetic.append({'H':'0','Hx':'0','Hxx':str(h2),'Hxxx':str(h3),'strict_r_rejected':True,'current_radius':'0','direct_radius':'0','domain':'declared B geometry; synthetic event jets, not theta/control acquisition'})
    source_path=args.source_control_replay;fresh=json.loads(source_path.read_text())
    screen=fresh['screen']
    if len(screen['event_rejections'])!=5 or not screen['euler_witness']['strict_signed_margin_rejected']:raise ArithmeticError('fresh inherited controls failed')
    actual=[]
    for event in screen['event_rejections']:
        if not(event['strict_first_jet_rejected']and event['strict_signed_margin_rejected']and not event['theta_error_constants_used']):raise ArithmeticError('inherited event screen')
        polynomial=event['control']=='polynomial backward-heat event'
        actual.append({'control':event['control'],'event_domain':event['event_domain'],'fresh_own_source_event_certificate':not polynomial,'source_status':'exact backward-heat polynomial; no integrable source asserted'if polynomial else'fresh own-source event data','event_rejection_basis':'At the exact event h0=h1=0, so r=h0*(-h2+beta*h3)+h1*(h1-beta*h2)=0 for every finite own-data h2,h3. No h3 enclosure is needed for this exact substitution.','new_four_jet_control_quadrature_claimed':False,'theta_error_constants_used':False})
    result={'status':'pass','date':'2026-10-19','prepared_for':'Edward Baker','actual_model':'gpt-6.1-sol (Codex)','actual_effort':'ultra','llm_assistance':'substantial; separate same-model internal control review; no human specialist review','producer_sha256':digest(PRODUCER),'control_helper_sha256':digest(__file__),'fresh_source_control_replay_sha256':digest(source_path),'source_replay_script_sha256':fresh['script_sha256'],'source_receipt_identities':screen['receipt_identities'],'interface_precision_bits':192,'source_precision_scope':'fresh interface arithmetic at192; each original source certificate retains its explicitly recorded own precision','actual_source_event_rejection':actual,'synthetic_exact_event_helper_challenges':synthetic,'actual_producer_invalid_input_rejections':rejected,'Euler_negative_Laguerre_witness':screen['euler_witness'],'Euler_new_current_sign_claimed':False,'Euler_scope':'The fresh negative-L0 witness rejects inherited Laguerre positivity. Its nonzero first jet permits a noncollision certificate; no implication L0<0=>r<=0 is asserted.','analytic_premise_screen':screen['analytic_premise_screen'],'scope':'Four fresh own-source event replays plus one exact heat-polynomial event, exact all-finite-higher-jets event substitution and actual helper/contract challenges. No imported theta tail constants or new control h3 quadratures.'}
    output=args.output;output.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'status':'pass','fresh_events':len(actual),'synthetic_helper_event_rejections':len(synthetic),'actual_api_guard_rejections':len(rejected),'output':str(output)}))
if __name__=='__main__':main()
