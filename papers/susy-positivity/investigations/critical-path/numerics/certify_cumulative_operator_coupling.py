#!/usr/bin/env python3
"""Outward-rational four-block certificate for cumulative append coupling.

The accompanying note proves the forward/backward energy transference.
All signs use exact integers or inherited outward rational intervals.
No floating matrix eigensolver, output projection, or enlarged-window
central certificate is used. Decimal displays do not decide inequalities.
"""
import argparse,hashlib,importlib.util,json,math,platform,time
from fractions import Fraction as F
from pathlib import Path

N,M,J=32,128,2048
FEATURE_SCALE=10**20
MATRIX_SCALE=10**12
ENTRY_ERROR=F(1,10**12)
BERNOULLI=list(map(F,['1/6','-1/30','1/42','-1/30','5/66','-691/2730','7/6','-3617/510']))

def load(path):
 s=importlib.util.spec_from_file_location('anchor_intervals',path)
 a=importlib.util.module_from_spec(s);s.loader.exec_module(a);return a

def dot(x,y):return sum(a*b for a,b in zip(x,y))

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--repository',type=Path)
 ap.add_argument('--digits',type=int,default=40)
 ap.add_argument('--output',type=Path,required=True)
 args=ap.parse_args()
 root=args.repository or Path(__file__).resolve().parents[5]
 src=root/'papers/susy-positivity/investigations/critical-path/numerics/certify_ema_original_anchor.py'
 a=load(src);I=a.I;I.scale=10**args.digits
 assert args.digits>=40
 pi=16*a.atan_reciprocal(5)-4*a.atan_reciprocal(239)
 hn=I(sum((F(1,j) for j in range(1,1001)),F(0)))-a.log_interval(1000)
 gamma=I.raw((hn-F(1,2000)).lo,(hn-F(1,2002)).hi)
 w0=-gamma-pi/2-3*a.log_interval(2)-a.log_interval(pi)
 w0_lower=F(-5372184,1000000)
 assert w0.lower()>w0_lower
 audit={}
 def progress(s):print(s,flush=True)
 def center(x,scale):
  q=(x.lower()+x.upper())/2
  z=(q.numerator*scale+q.denominator//2)//q.denominator
  return z,max(abs(x.lower()-F(z,scale)),abs(x.upper()-F(z,scale)))
 def feature(x):
  z,err=center(x,FEATURE_SCALE)
  assert err<=F(1,FEATURE_SCALE)
  return z
 def rounded_matrix_entry(x):
  z,err=center(x,MATRIX_SCALE)
  assert err<=ENTRY_ERROR,('entry enclosure too wide',float(err))
  return z
 def mat_intervals(mat,diagonal_loss=F(0)):
  return [[I(F(v,MATRIX_SCALE)-(diagonal_loss if i==j else 0)) for j,v in enumerate(row)] for i,row in enumerate(mat)]
 def ldl(name,mat):
  piv=a.ldl_positive(mat)
  audit[name]={'size':len(mat),'minimum_pivot_lower':str(min(x.lower() for x in piv))}
 def scalar_upper(x):return x.upper() if isinstance(x,I) else x
 def cosdata(ell):
  rr=[(1/I(ell)).sqrt()]+[(2/I(ell)).sqrt()]*(J-1)
  k=[j*pi/ell for j in range(J)]
  return rr,k
 def fourth_tail(ell,j):return (2/I(ell))*(I(ell)/pi)**4/(3*(j-1)**3)
 data={}
 def tower(ell,name,min_head,high_floor,r2):
  rr,k=cosdata(ell)
  ep=a.exp_interval(ell/4);sh=(ep-1/ep)/2;ch=(ep+1/ep)/2
  cc=[sh*rr[j]/(F(1,4)+k[j]*k[j]) if j%2==0 else I(0) for j in range(J)]
  ss=[-ch*rr[j]/(F(1,4)+k[j]*k[j]) if j%2 else I(0) for j in range(J)]
  # Positive Robin correction as rank-one feature sums, one parity at a time.
  features=[[] for _ in range(J)]
  d=[I(w0_lower) for _ in range(N+1)]
  env=[I(0) for _ in range(N)]
  for n in range(M):
   rate=I(F(4*n+1,2));ex=1/a.exp_interval(rate*ell)
   factors=[(2*rate*rate*(1-ex)).sqrt(),(2*rate*rate*(1+ex)).sqrt()]
   for j in range(J):
    v=factors[j%2]*rr[j]/(rate*rate+k[j]*k[j])
    assert v.abs().upper()<27
    features[j].append(feature(v))
   for j in range(N+1):
    d[j]+=2/rate*k[j]*k[j]/(rate*rate+k[j]*k[j])
   for j in range(N):
    env[j]+=2*rr[j]*rate*rate*(1+ex)/(rate*rate+k[j]*k[j])
  # Each feature error <=1e-20; every feature magnitude <27.
  rank_error=F(M)*(54/F(FEATURE_SCALE)+1/F(FEATURE_SCALE**2))
  matrix=[]
  for i in range(N):
   row=[]
   for j in range(J):
    if (i-j)%2:
     entry=I(0)
    else:
     entry=I(F(dot(features[i],features[j]),FEATURE_SCALE**2))
     entry=I.raw((entry-rank_error).lo,(entry+rank_error).hi)
     entry+=2*cc[i]*cc[j]-2*ss[i]*ss[j]
    if i==j:entry+=d[i]
    row.append(rounded_matrix_entry(entry))
   matrix.append(row)
  head=[row[:N] for row in matrix]
  # A0 is an exact rational lower head, including every entry error.
  ahead=mat_intervals(head,N*ENTRY_ERROR)
  ldl(name+'_head_floor',[[ahead[i][j]-(min_head if i==j else 0) for j in range(N)] for i in range(N)])
  high=d[N]-2*ch*ch*fourth_tail(ell,N)
  assert high.lower()>high_floor
  for i in range(N):env[i]+=2*(cc[i].abs()*sh+ss[i].abs()*ch)
  tail=fourth_tail(ell,J)*sum((v*v for v in env),I(0))
  body=[row[N:] for row in matrix]
  gram,guard=exact_gram(body)
  ldl(name+'_metric_cross',[[r2*ahead[i][j]-I(gram[i][j])-
       (tail+guard if i==j else 0) for j in range(N)] for i in range(N)])
  audit[name+'_metric']={'head_floor':str(min_head),'complement_floor':str(high_floor),
       'relative_cross_squared_upper':str(r2),'uncomputed_columns_squared_upper':tail.record(),
       'finite_gram_error':str(guard),'finite_high_lower':high.record()}
  data[name]={'ell':ell,'rr':rr,'k':k,'A':ahead,'min':min_head}
  progress(name+' tower: all-input metric checks passed')
 def exact_gram(rows):
  cols=len(rows[0]);n=len(rows)
  g=[[F(dot(rows[i],rows[j]),MATRIX_SCALE**2) for j in range(n)] for i in range(n)]
  fnorm=I(sum((g[i][i] for i in range(n)),F(0))).sqrt().upper()
  # Dimension product below 256^2 for N=32, J-N=2016.
  assert n*cols<=256**2
  eps=256*ENTRY_ERROR
  return g,2*fnorm*eps+eps*eps

 tower(F(1,2),'old',F(4,125),F(161,50),F(11,1000))
 tower(F(1,20),'new',F(31,20),F(369,100),F(13,1000000))

 # Only Im psi and Re psi' are needed. Exact recurrence and Euler--Maclaurin
 # at Re z=33.25, with |B_16({t})|<=8, bound both remainders explicitly.
 def cmul(z,v):return (z[0]*v[0]-z[1]*v[1],z[0]*v[1]+z[1]*v[0])
 def cinv(z):
  den=z[0]*z[0]+z[1]*z[1];return(z[0]/den,-z[1]/den)
 def atan_positive(x):
  flip=x.lower()>1
  if flip:x=1/x
  else:assert x.upper()<1
  z=x/(1+(1+x*x).sqrt());power=z;total=I(0)
  for j in range(64):
   total+=((-1)**j)*power/(2*j+1);power*=z*z
  error=(2*power/129).abs().upper()
  ans=2*total
  ans=I.raw((ans-error).lo,(ans+error).hi)
  return pi/2-ans if flip else ans
 cache={}
 def pfun(index):
  if index in cache:return cache[index]
  k=2*index*pi;imag=k/2
  p_im=I(0);t_re=I(0)
  for j in range(32):
   u=cinv((I(F(5,4)+j),imag))
   p_im-=u[1];t_re+=cmul(u,u)[0]
  u=cinv((I(F(133,4)),imag));u2=cmul(u,u)
  p_im+=(atan_positive(imag/F(133,4)) if index else I(0))-u[1]/2
  t_re+=u[0]+u2[0]/2
  power=u2
  for j,b in enumerate(BERNOULLI,1):
   p_im-=b*power[1]/(2*j)
   t_re+=b*cmul(power,u)[0]
   power=cmul(power,u2)
  ep=F(8,16*33**16);et=F(8,33**17)
  p_im=I.raw((p_im-ep).lo,(p_im+ep).hi)
  t_re=I.raw((t_re-et).lo,(t_re+et).hi)
  value=k*p_im/2
  deriv=(p_im/(4*k)+t_re/8) if index else t_re/4
  cache[index]=(value,deriv)
  return value,deriv

 # Exponential correction represented by 256 rational rank-one features.
 exp_count=256
 ef={};weights=[]
 for n in range(1,exp_count+1):
  rate=F(4*n+1,2)
  weights.append(tuple(feature(1/a.exp_interval(rate*l)) for l in [F(1,20),F(1,2),F(11,20)]))
 for name in ['old','new']:
  d=data[name];table=[]
  for j in range(J):
   line=[]
   for n in range(1,exp_count+1):
    rate=F(4*n+1,2)
    value=d['rr'][j]*rate/(rate*rate+d['k'][j]*d['k'][j])
    assert value.abs().upper()<(1 if name=='old' else 3)
    line.append(feature(value))
   table.append(line)
  ef[name]=table
  progress(name+' mixed exponential features prepared')
 exp_feature_error=F(exp_count*40,FEATURE_SCALE)
 first=F(4*(exp_count+1)+1,2)
 exp_tail=I(13)*3/(a.exp_interval(first/F(20))*first*first*(1-1/a.exp_interval(F(1,10))))
 assert exp_tail.upper()<F(1,10**13)
 def mixed_entry(inew,iold):
  kn=data['new']['k'][inew];ko=data['old']['k'][iold]
  pn,dn=pfun(10*inew);po,do=pfun(iold)
  pure=dn if 10*inew==iold else (po-pn)/(ko*ko-kn*kn)
  pure*=data['new']['rr'][inew]*data['old']['rr'][iold]
  sn=(-1)**inew;so=(-1)**iold
  coeff=[-sn*v[0]-so*v[1]+sn*so*v[2] for v in weights]
  num=sum(x*y*c for x,y,c in zip(ef['new'][inew],ef['old'][iold],coeff))
  pure+=I(F(num,FEATURE_SCALE**3))
  en=a.exp_interval(F(1,40));eo=a.exp_interval(F(1,4))
  pole_n=-F(1,2)*(1-sn*en)/(F(1,4)+kn*kn)*data['new']['rr'][inew]
  pole_o=-F(1,2)*(1-so*eo)/(F(1,4)+ko*ko)*data['old']['rr'][iold]
  pure-=pole_n*pole_o
  error=exp_feature_error+exp_tail.upper()
  return rounded_matrix_entry(I.raw((pure-error).lo,(pure+error).hi))
 # Independent enclosure of the pure infinite series: positive finite sum
 # plus monotone integral bounds, without digamma or Euler--Maclaurin.
 series_controls=[]
 for ni,oi in [(0,0),(0,1),(1,0),(1,10),(2,20),(7,1),(31,31),(31,310),(0,2047),(2047,0)]:
  kn=data['new']['k'][ni];ko=data['old']['k'][oi]
  xn=kn*kn;xo=ko*ko
  pn,dn=pfun(10*ni);po,_=pfun(oi)
  exact=dn if 10*ni==oi else (po-pn)/(xo-xn)
  cutoff=4096
  partial=I(0)
  for n in range(1,cutoff+1):
   rate=F(4*n+1,2);rr=rate*rate
   partial+=rr/((rr+xn)*(rr+xo))
  def integral(start):
   if ni==0 and oi==0:return 1/I(start)
   if 10*ni==oi:
    return atan_positive(kn/start)/(2*kn)+start/(2*(start*start+xn))
   vn=kn*atan_positive(kn/start) if ni else I(0)
   vo=ko*atan_positive(ko/start) if oi else I(0)
   return (vo-vn)/(xo-xn)
  first=F(4*(cutoff+1)+1,2);last=F(4*cutoff+1,2)
  assert (xn*xo).upper()<last**4
  lo=(partial+integral(first)/2).lower()
  hi=(partial+integral(last)/2).upper()
  assert lo<exact.lower() and exact.upper()<hi
  series_controls.append({'new_mode':ni,'old_mode':oi,'independent_width':str(hi-lo)})
 progress('Ten independent infinite-series enclosures passed')
 h_new_head=[]
 for i in range(N):
  h_new_head.append([mixed_entry(i,j) for j in range(J)])
  if i%8==7:progress('mixed new head rows '+str(i+1)+'/'+str(N))
 h_old_head=[]
 for j in range(N):
  h_old_head.append([h_new_head[i][j] if i<N else mixed_entry(i,j) for i in range(J)])
  if j%8==7:progress('mixed old head rows '+str(j+1)+'/'+str(N))
 an=data['new']['A'];ao=data['old']['A'];q=F(171,200)
 head_error=N*ENTRY_ERROR
 block=[]
 for i in range(2*N):
  row=[]
  for j in range(2*N):
   if i<N and j<N:v=q*an[i][j]
   elif i>=N and j>=N:v=q*ao[i-N][j-N]
   elif i<N:v=I(F(h_new_head[i][j-N],MATRIX_SCALE))
   else:v=I(F(h_new_head[j][i-N],MATRIX_SCALE))
   row.append(v-(head_error if i==j else 0))
  block.append(row)
 ldl('mixed_head_norm',block)
 def mixed_tail(name,rows,ellout,bound):
  din=data[name];ellin=din['ell']
  c=sum((1/a.exp_interval(F(5,2)*l)/(1-1/a.exp_interval(2*l)) for l in [ellout,ellin,ellout+ellin]),I(0))
  c+=F(1,2)*(1+a.exp_interval(ellout/2))*2*(a.exp_interval(ellin/2)-1)
  alpha=I(ellout/4);beta=c*(I(ellout)/pi)**2
  tail=2/I(ellout)*F(2*N-1,ellin)*(alpha*alpha/(J-1)+alpha*beta/(J-1)**2+beta*beta/(3*(J-1)**3))
  g,guard=exact_gram([row[N:] for row in rows])
  ldl('mixed_'+name+'_head_to_complement',[[bound*din['A'][i][j]-I(g[i][j])-(tail+guard if i==j else 0) for j in range(N)] for i in range(N)])
  audit['mixed_'+name+'_tail']={'relative_squared_upper':str(bound),'uncomputed_rows_HS_squared_upper':tail.record(),'gram_error':str(guard)}
 mixed_tail('old',h_old_head,F(1,20),F(23,1000))
 mixed_tail('new',h_new_head,F(1,2),F(19,100))
 # The omitted/omitted gamma corner uses its Carleman OPERATOR norm pi/2.
 pole_tail=I(1)
 for ell in [F(1,2),F(1,20)]:
  pole_tail*=F(1,2)*(1+a.exp_interval(ell/2))*fourth_tail(ell,N).sqrt()
 corner=pi/2+pole_tail
 el,eh=F(1,40),F(1,200)
 dl=F(161,50)-F(11,1000)/el
 dh=F(369,100)-F(13,1000000)/eh
 four=[[(I(q*q)/((1-el)*(1-eh))).sqrt(),(I(F(19,100))/((1-eh)*dl)).sqrt()],
       [(I(F(23,1000))/((1-el)*dh)).sqrt(),corner/(I(dl*dh).sqrt())]]
 comparison=[[F(87,100),F(53,200)],[F(81,1000),F(493,1000)]]
 for i in range(2):
  for j in range(2):assert four[i][j].upper()<comparison[i][j]
 gram2=[[sum(comparison[k][i]*comparison[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
 kappa0=F(19,20)
 aa=kappa0*kappa0-gram2[0][0];dd=kappa0*kappa0-gram2[1][1]
 assert aa>0 and dd>0 and aa*dd>gram2[0][1]**2
 # Shift perturbation: Q_s >= T_lower -w^2/8 >=(1-eps/m)T_lower.
 # Here T_lower has the inherited m=1/40 minus the scalar w0 rounding.
 # To avoid borrowing a sharp m for T_lower, the certified diagonal lower
 # metric has min >= min((1-el)*.032,(1-eh)*1.55,dl,dh) > .03.
 m=F(3,100);w=F(1,1000);eps=w*w/8
 assert min((1-el)*F(4,125),(1-eh)*F(31,20),dl,dh)>m
 # |H_s-H_0| <= (w R)^2 cosh(wR)/2 * (pi/2+||pole||).
 R=F(11,20);ex=a.exp_interval(w*R)
 raw=pi/2+((a.exp_interval(F(1,2))-1)*(a.exp_interval(F(1,20))-1)).sqrt()
 difference=w*w*R*R/2*(ex+1/ex)/2*raw
 shift_bound=(I(kappa0)+difference/m)/(1-eps/m)
 target=F(951,1000)
 assert shift_bound.upper()<target
 out={'schema':1,'date':'2026-09-20','model':'OpenAI GPT-6 (Codex; developer-provided identity)',
      'reasoning_effort':'Not exposed in this session; not inferred','digits':args.digits,
      'parameters':{'L':'1/2','h':'1/20','omega':'1/1000','M':M,'N':N,'J':J,'exponential_terms':exp_count},
      'arithmetic':'Exact fixed-point integer matrix products; explicit entry/Gram errors; outward rational interval LDL sign checks',
      'w0_lower':str(w0_lower),'entry_error':str(ENTRY_ERROR),'checks':audit,
      'independent_series_controls':series_controls,
      'control_H_first8_integer_matrix':[row[:8] for row in h_new_head[:8]],
      'control_H_matrix_denominator':MATRIX_SCALE,
      'metric_cross_parameters':[str(el),str(eh)],'complement_metric_floors':[str(dl),str(dh)],
      'four_operator_blocks':[[x.record() for x in row] for row in four],
      'comparison_matrix':[[str(x) for x in row] for row in comparison],
      'comparison_norm_upper':str(kappa0),'comparison_determinant_slack':str(aa*dd-gram2[0][1]**2),
      'shift_perturbation_norm':difference.record(),'shifted_relative_coupling_upper':shift_bound.record(),
      'cumulative_coupling_upper':str(target),'certificate_pass':True,
      'analytic_dependencies':['The note\'s Fourier/EMA decomposition and infinite complement bounds','The forward/backward energy transference on the original causal flow'],
      'scope':'All-input cumulative coupling at the fixed append; internal computer-assisted proof subject to specialist review; no new depth horizon or physical realization',
      'python':platform.python_version(),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'inherited_interval_source_sha256':hashlib.sha256(src.read_bytes()).hexdigest()}
 args.output.parent.mkdir(parents=True,exist_ok=True)
 args.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 progress(json.dumps({'certificate_pass':True,'cumulative_coupling_upper':str(target),'output':str(args.output)}))

if __name__=='__main__':
 if not __debug__:raise SystemExit('Do not disable assertions with python -O.')
 main()
