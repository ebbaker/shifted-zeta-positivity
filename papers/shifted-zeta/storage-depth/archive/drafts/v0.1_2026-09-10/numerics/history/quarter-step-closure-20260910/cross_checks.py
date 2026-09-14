"""Independent numerical quadrature checks; these are not sign proofs."""
import hashlib
import json
from pathlib import Path
import mpmath as mp
from flint import arb as A,ctx
import close_complement as z

def run():
    ctx.prec=3072;mp.mp.dps=65
    r=z.r;a=A(7).log();h=(A(8).log()-a)/4;M=160;g=r.c.profile(M)
    model=z.OldOutput(4,3,a,h,M,g)
    cross,bb=model.build()
    phi=r.matrix([r.ex.legendre(i,A(0),A(1),A(1)) for i in range(4)])
    projected=model.inner(phi,model.bp)+model.inner(phi,model.br,'right')+model.inner(phi,model.bo,'outer')
    for lo,hi,bt in model.bt:projected+=model.inner(phi,bt,window=(lo,hi))
    original_cross,*_=r.cg.cross(4,3,a,h,M,g)
    difference=projected-original_cross.transpose()
    projection_error=sum((difference[i,j].abs_upper()**2 for i in range(4) for j in range(3)),A(0)).sqrt()
    assert projection_error<A('1e-100')
    def mid(x):return r.ex.mid(x)
    aa,hh=mid(a),mid(h)
    def rows(mat):return [[mid(mat[i,j]) for j in reversed(range(mat.ncols()))] for i in range(mat.nrows())]
    ap,al,bp,br,bo=map(rows,[model.ap,model.al,model.bp,model.br,model.bo])
    ats=[(mid(model.pos(lo)),mid(model.pos(hi)),rows(p)) for lo,hi,p in model.at]
    bts=[(mid(model.pos(lo)),mid(model.pos(hi)),rows(p)) for lo,hi,p in model.bt]
    def aval(i,u):
        val=mp.polyval(ap[i],u)+mp.polyval(al[i],u)*(mp.log(u)+mp.log1p(-u))
        return val+sum(mp.polyval(p[i],u) for lo,hi,p in ats if lo<u<hi)
    def bval(j,u):
        val=mp.polyval(bp[j],u)+mp.polyval(br[j],u)*mp.log1p(-u)+mp.polyval(bo[j],u)*mp.log(1+hh/aa-u)
        return val+sum(mp.polyval(p[j],u) for lo,hi,p in bts if lo<u<hi)
    points=sorted(set([mp.mpf(0),mp.mpf(1)]+[x for lo,hi,_ in ats+bts for x in [lo,hi]]))
    errors=[]
    for i,j in [(0,0),(3,2)]:
        val=mp.quad(lambda u:aval(i,u)*bval(j,u),points)
        errors.append(abs(val-mid(cross[i,j])))
    for i,j in [(0,0),(0,2),(2,2)]:
        val=mp.quad(lambda u:bval(i,u)*bval(j,u),points)
        errors.append(abs(val-mid(bb[i,j])))
    assert max(errors)<mp.mpf('1e-48')
    def q(x):return mp.exp(x/2)-mp.exp(-5*x/2)/(-mp.expm1(-2*x))
    point_errors=[]
    for i,u in [(0,mp.mpf('.2')),(1,mp.mpf('.5')),(2,mp.mpf('.98'))]:
        actual=mp.sqrt(aa*hh)*mp.quad(lambda v:q(aa*(1-u)+hh*v)*mp.sqrt(2*i+1)*mp.legendre(i,2*v-1),[0,1])
        pred=mp.polyval(bp[i],u)+mp.polyval(br[i],u)*mp.log1p(-u)+mp.polyval(bo[i],u)*mp.log(1+hh/aa-u)
        point_errors.append(abs(actual-pred))
    assert max(point_errors)<mp.mpf('1e-40')
    vals=z.sm.exterior(10,A('1.017'));cc=mp.mpf('1.017')
    fun={'outer':lambda x:mp.log(cc-x),'outer2':lambda x:mp.log(cc-x)**2,
         'left_outer':lambda x:mp.log(x)*mp.log(cc-x),'right_outer':lambda x:mp.log(1-x)*mp.log(cc-x)}
    moment_errors=[]
    for name in vals:
        for k in [0,1,3,9]:
            val=mp.quad(lambda u:u**k*fun[name](u),[0,mp.mpf('.5'),1])
            moment_errors.append(abs(val-mid(vals[name][k])))
    assert max(moment_errors)<mp.mpf('1e-55')
    record={'scope':'Numerical cross-checks, not positivity certificates.','all_checks_pass':True,'mpmath_digits':mp.mp.dps,
            'old_output_gram_vs_quadrature_max_error':mp.nstr(max(errors),18),
            'adjoint_cross_gamma_vs_original_kernel_max_error':mp.nstr(max(point_errors),18),
            'exterior_log_moments_vs_quadrature_max_error':mp.nstr(max(moment_errors),18),
            'adjoint_projection_vs_original_cross_block_error':projection_error.str(35),
            'source_sha256':{str(p.relative_to(z.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(z.__file__),Path(z.sm.__file__)]}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(record,indent=2)+'\n')
    print(json.dumps(record,indent=2))

if __name__=='__main__':run()
