#!/usr/bin/env python3
"""Independent quadrature checks of the residual output and full norm."""
import json
from pathlib import Path
import mpmath as mp
from flint import arb as A,ctx
import central_residual as r

def run():
    ctx.prec=3072;mp.mp.dps=80
    a=A(7).log();h=(A(8).log()-a)/4
    no,nn,M,T=4,3,160,70
    g=r.c.profile(M)
    B,*_=r.cg.cross(no,nn,a,h,M,g);F=r.cg.gamma_head(nn,h,M,g)
    J,_=r.rational_matrix(-F.solve(B),100)
    bp,bl,_=r.cross_output(no,a,h,M,g,T)
    fp,fl=r.gamma_output(nn,h,M,g)
    k=max(bp.ncols(),fp.ncols())
    rp=r.pad(bp,k)+J.transpose()*r.pad(fp,k)
    ra=r.pad(bl,no)+J.transpose()*r.pad(fl,no)
    rb=J.transpose()*fl
    gram=r.gram(rp,ra,rb)
    def mppolys(mat):return [[r.ex.mid(p[j]) for j in reversed(range(mat.ncols()))] for p in r.rows(mat)]
    pp,pa,pb=mppolys(rp),mppolys(ra),mppolys(rb)
    def model(i,v):return mp.polyval(pp[i],v)+mp.polyval(pa[i],v)*mp.log(v)+mp.polyval(pb[i],v)*mp.log1p(-v)
    norm_error=mp.mpf(0)
    for i,j in [(0,0),(0,2),(3,3)]:
        val=mp.quad(lambda v:model(i,v)*model(j,v),[0,mp.mpf('.5'),1])
        norm_error=max(norm_error,abs(val-r.ex.mid(gram[i,j])))
    assert norm_error<mp.mpf('1e-65')
    aa,hh=r.ex.mid(a),r.ex.mid(h)
    ell=mp.euler+mp.log(2*mp.pi*hh)
    def profile(t):return mp.exp(t/2)*t/mp.sinh(t)-4*t*mp.cosh(t/2) if t else mp.mpf(1)
    def w(t):return (profile(t)-1)/t if t else -mp.mpf(7)/2
    def q(t):return mp.exp(t/2)-mp.exp(-5*t/2)/(-mp.expm1(-2*t))
    def phi(n,v):return mp.sqrt(2*n+1)*mp.legendre(n,2*v-1)
    jj=r.ex.tomp(J)
    point_error=mp.mpf(0)
    for i,v in [(0,mp.mpf('.2')),(2,mp.mpf('.5')),(3,mp.mpf('.8'))]:
        cross=mp.sqrt(aa*hh)*mp.quad(lambda u:q(aa+hh*v-aa*u)*phi(i,u),[0,1])
        cross-=mp.sqrt(hh/aa)*sum(mp.log(p)/mp.sqrt(n)*phi(i,1+hh/aa*v-mp.log(n)/aa) for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7)])
        def continuation(u):return sum(jj[n,i]*phi(n,u) for n in range(nn))
        gv=continuation(v)
        rowsum=-ell-mp.log(v*(1-v))/2-(mp.quad(w,[0,hh*v])+mp.quad(w,[0,hh*(1-v)]))/2
        def difference(u):
            if u==v:return mp.mpf(0)
            return profile(hh*abs(v-u))/(2*abs(v-u))*(gv-continuation(u))
        applied=rowsum*gv+mp.quad(difference,[0,v,1])
        point_error=max(point_error,abs(cross+applied-model(i,v)))
    assert point_error<mp.mpf('1e-35')
    data={'scope':'Independent numerical checks, not positivity certificates.',
          'full_residual_gram_vs_quadrature_error':mp.nstr(norm_error,15),
          'residual_output_vs_original_kernel_error':mp.nstr(point_error,15),
          'all_checks_pass':True,'mpmath_digits':mp.mp.dps,'arb_bits':ctx.prec}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2),flush=True)

if __name__=='__main__':run()
