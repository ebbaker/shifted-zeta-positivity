#!/usr/bin/env python3
"""Bounded S07 option screens; proofs and scope are in Note05.

Prepared for Edward Baker, 19 October 2026, with substantial LLM assistance.
Actual model gpt-6.1-sol (Codex), effort ultra. Requires python-flint.
Evaluates assigned-payment floors, not actual-error lower bounds.
"""
import argparse
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib,json,math,platform
from pathlib import Path
import flint
from flint import arb,ctx

LANE=Path('papers/investigations-3/11_arithmetic_collision_rigidity/symmetries/07_geometric_duality_and_quaternionic_symmetry')
NAMES=['03_CONSTRAINED_THETA_JET_SPACE_AND_RESIDUAL_CONTRACT_20261019.md','04_PAID_PROFILE_TRACE_AND_DIRECT_TAIL_COMPARISON_20261019.md','05_OBSERVATION_OPTIONS_AND_BOUNDED_FEASIBILITY_SCREENS_20261019.md']
def require(ok,msg):
 if not bool(ok):raise ValueError(msg)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(repo,bits):
 require(128<=bits<=4096,'precision outside bounded range')
 require((repo/'AGENTS.md').is_file(),'research repository missing')
 require(all((repo/LANE/'notes'/n).is_file() for n in NAMES[:2]),'required source notes missing')
 ctx.prec=bits
 R=lambda a,b=1:arb(a)/b
 pi=arb.pi();U=arb(4).log()/4
 lam=9*pi-R(1,80);r=R(256,81)*(-7*pi).exp();r4=R(256,81)*(-28*pi).exp()
 def J2(Q):return(-lam*Q).exp()*(Q**2/lam+2*Q/lam**2+2/lam**3)
 def JD(Q):return(-lam*Q).exp()*((Q**3-Q**2)/lam+(3*Q**2-2*Q)/lam**2+(6*Q-2)/lam**3+6/lam**4)
 D=[81*pi*pi/2*((J2(1)-J2(4))/(1-r)+J2(4)/(1-r4)),81*pi*pi/8*((JD(1)-JD(4))/(1-r)+JD(4)/(1-r4))]
 c=[(U/2-R(1,4*999)).sqrt(),(U**3/6-U**2/(4*999)-U/(4*999**2)-R(1,8*999**3)).sqrt()]
 def a(q,y):
  w=pi*q*y*y
  return (q.log()/4).exp()*w*(w-R(3,2))*(-w).exp()
 # Any cutoff preserving samples chi(+/-3)=0, with residual in X.
 q0=R(65,64)
 Xcut=(R(29,16)*q0.log()*a(q0,arb(3))**2).sqrt()
 Gcut=[arb(20).sqrt()*Xcut*v for v in c]
 # Original chi2 with finite V4 projection and old X for complement.
 M={0:(-8*pi).exp()/(8*pi)}
 for k in (2,4,6,8):M[k]=arb(2)**(k-1)*(-8*pi).exp()/(4*pi)+(k-1)*M[k-2]/(4*pi)
 root2=(arb(2).log()/4).exp();Q=R(17,16);b=R(5,2);alow=R(9,4)
 C=[2*root2*pi*pi*M[4],2*root2*pi*pi*4*pi/arb(2).sqrt()*M[6],2*root2*pi*pi*16*pi*pi/arb(24).sqrt()*M[8]]
 common=root2*(Q.log()/4).exp()*(-pi*alow**2).exp()
 B=[common,common*4*pi*Q*b*b/arb(2).sqrt(),common*16*pi*pi*Q*Q*b**4/arb(24).sqrt()]
 projection=sum((v*w for v,w in zip(C,B)),arb(0))
 m=a(Q,b)/(1+R(8,3).exp())
 require(m>projection and projection>0,'complement witness not positive')
 Xcomp=(R(97,64)*Q.log()).sqrt()*(m-projection)
 Gcomp=[arb(20).sqrt()*Xcomp*v for v in c]
 require(F(29,4)*F(1,4)==F(29,16),'cutoff trace witness coefficient')
 require(F(1)+F(5,2)**2==F(29,4),'sample interval weight')
 checks={
 'cutoff_value_loss_ratio_exceeds_10.23':Gcut[0]/D[0]>arb('10.23'),
 'cutoff_derivative_loss_ratio_exceeds_215.9':Gcut[1]/D[1]>arb('215.9'),
 'projected_witness_bound_below_2.30508e-11':projection<arb('2.30508e-11'),
 'complement_value_loss_ratio_exceeds_1617':Gcomp[0]/D[0]>1617,
 'complement_derivative_loss_ratio_exceeds_34118':Gcomp[1]/D[1]>34118,
 'tail_ratios_valid':0<r4<r<1,
 }
 for name,v in checks.items():require(v,name)
 vals={'U':U,'X_cutoff_family_floor_expression':Xcut,'projection_absolute_witness_upper_expression':projection,'original_profile_witness_lower_expression':m,'X_complement_floor_expression':Xcomp}
 for j in (0,1):
  vals.update({f'direct_complete_upper_{j}':D[j],f'cutoff_family_assigned_floor_{j}':Gcut[j],f'cutoff_family_loss_ratio_{j}':Gcut[j]/D[j],f'projection_complement_assigned_floor_{j}':Gcomp[j],f'projection_complement_loss_ratio_{j}':Gcomp[j]/D[j]})
 for n,v in vals.items():require(v.is_finite() and v>0,'nonpositive/nonfinite '+n)
 digits=max(30,int(bits*math.log10(2))-8)
 pins={str(LANE/'notes'/n):sha(repo/LANE/'notes'/n) for n in NAMES if (repo/LANE/'notes'/n).is_file()}
 return {'date':'2026-10-19','generated_at_utc':datetime.now(timezone.utc).isoformat(),'prepared_for':'Edward Baker','actual_model':'gpt-6.1-sol (Codex)','actual_effort':'ultra','llm_assistance':'substantial; separate same-model review','status':'pass: two scoped option screens','runtime':{'python':platform.python_version(),'python_flint':flint.__version__,'precision_bits':bits},'scope':['All admissible cutoffs with unchanged physical N2 samples and same X/sqrt20/Cauchy rule; cutoff-family lower floor is independent of annulus placement.','Original chi2, orthogonal V4 projection, separate triangle payment with unchanged X/sqrt20/Cauchy complement; projected component cost need not be lower bounded.','These are lower floors for assigned allowances, never actual-error lower bounds.','Observation-adapted signed/dual/complement estimates remain outside these screens.','Continuous universal proofs are in Note05; intervals certify their closed constants.'],'checks':{k:bool(v) for k,v in checks.items()},'interval_values':{k:v.str(digits) for k,v in vals.items()},'source_sha256':pins,'checker_sha256':sha(Path(__file__))}
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--repo',required=True,type=Path);p.add_argument('--precision',type=int,default=192);p.add_argument('--output',required=True,type=Path);a=p.parse_args();d=run(a.repo.resolve(),a.precision);a.output.parent.mkdir(parents=True,exist_ok=True);a.output.write_text(json.dumps(d,indent=2,sort_keys=True)+'\n');print(json.dumps({'status':d['status'],'precision':a.precision,'output':str(a.output)}))
if __name__=='__main__':main()
