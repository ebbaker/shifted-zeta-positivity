import sys, json, time, argparse, mpmath as mp
from pathlib import Path
from spatial import *
from flint import ctx
sys.path.insert(0,str(HISTORY/'quarter-step-closure-20260910'))
import close_complement as old
ctx.prec=2048
geo=Geometry([logn(7),(logn(8)-logn(7))/4],[8,4],48)
a,h=[l.value() for l in geo.lengths]
g=geo.g
start=time.monotonic()
B,*_=residual.cg.cross(8,4,a,h,48,g)
for target,source,reference in [(1,0,B),(0,1,B.transpose()),(1,1,residual.cg.gamma_head(4,h,48,g))]:
 delta=geo.head_block(target,source)-reference
 bound=frob2(delta).sqrt()
 assert bound<A('1e-100'),bound
 print('head',target,source,bound.str(8),flush=True)
op=old.OldOutput(8,4,a,h,48,g)
xb,bb=op.build()
for left,right,ref in [(0,1,xb),(1,1,bb)]:
 delta=geo.gram_block(0,left,right)-ref
 bound=frob2(delta).sqrt()
 assert bound<A('1e-100'),bound
 print('old gram',left,right,bound.str(8),flush=True)
# The previous new-output series has an explicit remainder, unlike this builder.
bp,bl,be=residual.cross_output(8,a,h,48,g,100)
fp,fl=residual.gamma_output(4,h,48,g)
k=max(bp.ncols(),fp.ncols());kl=max(bl.ncols(),fl.ncols())
poly=AM(residual.pad(bp,k).tolist()+residual.pad(fp,k).tolist())
left=AM(residual.pad(bl,kl).tolist()+residual.pad(fl,kl).tolist())
right=AM(AM(8,4).tolist()+fl.tolist())
ref=residual.gram(poly,left,right)
for i,j,rr,ss in [(0,0,range(8),range(8)),(0,1,range(8),range(8,12)),(1,1,range(8,12),range(8,12))]:
 delta=geo.gram_block(1,i,j)-sub(ref,rr,ss)
 bound=frob2(delta).sqrt()
 assert bound<A('1e-100'),bound
 print('new gram',i,j,bound.str(8),flush=True)


mp.mp.dps=75
moment_errors=[]
for cs,ds in [('0','0'),('0','1'),('1','1'),('0','1.03'),('1','1.03'),('1.03','1.03'),('1.03','1.07'),('-58','0'),('-58','1'),('-58','-1'),('-1','1.03'),('-1','-1'),('2','2')]:
 cc=A(cs,A('1e-100')) if cs in ['-1','2'] else A(cs);dd=cc if cs==ds else A(ds)
 vals=lm.pair(12,cc,dd)
 assert all(v.is_finite() for v in vals)
 for k in [0,1,5,11]:
  ref=mp.quad(lambda x:x**k*mp.log(abs(x-mp.mpf(cs)))*mp.log(abs(x-mp.mpf(ds))),[0,mp.mpf('.5'),1])
  moment_errors.append(abs(ref-residual.ex.mid(vals[k])))
assert max(moment_errors)<mp.mpf('1e-60')
three=Geometry([logn(7),(logn(8)-logn(7))/4,(logn(8)-logn(7))/4],[4,3,3],160)
assert active_powers(logn(7))==[(2,2,1),(3,3,1),(4,2,2),(5,5,1)]
assert active_powers(three.L)==[(2,2,1),(3,3,1),(4,2,2),(5,5,1),(7,7,1)]
head_errors=[];kernel_errors=[]
gamma_geo=Geometry(three.lengths,three.modes,three.degree);gamma_geo.active=[]
def midpoint(x):return residual.ex.mid(x)
def gamma_value(out,target,i,v):
 value=mp.polyval([midpoint(x) for x in reversed(out.poly.tolist()[i])],v)
 for point,mat in out.logs.items():
  value+=mp.polyval([midpoint(x) for x in reversed(mat.tolist()[i])],v)*mp.log(abs(v-midpoint(three.pos(target,point))))
 return value
for target,source in [(0,2),(2,0),(1,2),(2,1)]:
 err=frob2(three.head_block(target,source)-three.head_block(source,target).transpose()).sqrt()
 assert err<A('1e-100');head_errors.append(err)
 out=gamma_geo.output(target,source)
 aa=midpoint(three.starts[target].value());bb=midpoint(three.starts[source].value())
 ll=midpoint(three.lengths[target].value());li=midpoint(three.lengths[source].value())
 for i,v in [(0,mp.mpf('.2')),(2,mp.mpf('.7'))]:
  def kernel(u):
   t=abs(aa+ll*v-bb-li*u)
   q=mp.exp(t/2)-mp.exp(-5*t/2)/(-mp.expm1(-2*t))
   return mp.sqrt(li*ll)*q*mp.sqrt(2*i+1)*mp.legendre(i,2*u-1)
  ref=mp.quad(kernel,[0,1]);kernel_errors.append(abs(ref-gamma_value(out,target,i,v)))
assert max(kernel_errors)<mp.mpf('1e-28')
gram_errors=[]
for target,source in [(1,2),(2,0),(2,1)]:
 out=three.output(target,source);gg=three.gram_block(target,source,source)
 assert all(x.is_finite() for x in gg.entries())
 for i in [0,1]:
  def value(v):
   result=gamma_value(out,target,i,v)
   for lo,hi,mat in out.translations:
    if midpoint(three.pos(target,lo))<v<midpoint(three.pos(target,hi)):
     result+=mp.polyval([midpoint(x) for x in reversed(mat.tolist()[i])],v)
   return result
  points=sorted(set([mp.mpf(0),mp.mpf('.5'),mp.mpf(1)]+[midpoint(three.pos(target,z)) for lo,hi,_ in out.translations for z in [lo,hi]]))
  ref=mp.quad(lambda v:value(v)**2,points)
  gram_errors.append(abs(ref-midpoint(gg[i,i])))
assert max(gram_errors)<mp.mpf('1e-50')
eps=A(0,A('1e-100'))
assert ldl(AM([[1,eps],[eps,1]]))['positive']
assert not ldl(AM([[1,0],[0,-1]]))['positive']
assert not ldl(AM([[A('nan')]]))['positive']
record={'scope':'Implementation consistency checks; quadrature is diagnostic, not a positivity certificate.',
 'all_checks_pass':True,'precision_bits':ctx.prec,'mpmath_digits':mp.mp.dps,
 'endpoint_and_exterior_log_moment_cases':52,
 'log_moment_max_error':mp.nstr(max(moment_errors),20),
 'three_interval_adjoint_head_error_upper':max(head_errors).str(40),
 'three_interval_squared_output_gram_max_error':mp.nstr(max(gram_errors),20),
 'zero_crossing_square_and_nonfinite_ldl_checks_pass':True,
 'original_gamma_kernel_max_error':mp.nstr(max(kernel_errors),20),
 'first_step_legacy_head_and_gram_comparison_pass':True,
 'active_set_endpoint_checks_pass':True,'source_sha256':source_hashes(),'seconds':time.monotonic()-start}
p=argparse.ArgumentParser();p.add_argument('--output',required=True)
args=p.parse_args();Path(args.output).write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
