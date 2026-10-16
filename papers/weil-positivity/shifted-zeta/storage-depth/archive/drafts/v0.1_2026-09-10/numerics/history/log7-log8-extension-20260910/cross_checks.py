#!/usr/bin/env python3
"""Independent low-dimensional checks of both extension constructions."""
import json
from pathlib import Path
import mpmath as mp
from flint import arb as A,ctx
import extension_storage as e
import central_geometry as cg

def run():
    mp.mp.dps=65
    ctx.prec=4096
    aa,LL=A(7).log(),A(8).log()
    hh=LL-aa
    a,L=mp.log(7),mp.log(8)
    h=L-a
    M=240
    B,*_=cg.cross(1,1,aa,hh,M,cg.c.profile(M))
    def q(s):
        return mp.exp(s/2)-mp.exp(-5*s/2)/(-mp.expm1(-2*s))
    gamma=(mp.quad(lambda s:s*q(s),[0,h])+mp.quad(lambda s:h*q(s),[h,a])
           +mp.quad(lambda s:(L-s)*q(s),[a,L]))/mp.sqrt(a*h)
    arithmetic=-mp.sqrt(h/a)*sum(mp.log(p)/mp.sqrt(n) for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7)])
    central_error=abs(e.mid(B[0,0])-gamma-arithmetic)
    assert central_error<mp.mpf('1e-45')
    # Constant inputs on the two intervals, quarter shift. Compare the exact
    # moment construction against direct quadrature of its output functions.
    w=A(1)/4
    ca,ct=e.input_coefficients(1,1,LL,aa,hh)
    G=e.gamma_operator(1,LL,w,M)
    Q,T=ca*G,ct*G
    ds=e.core.delays(8,LL,w)
    gram=e.gram(Q,ds,w,A(1),tail=T,label='quadrature cross-check')
    p=[e.mid(x) for x in reversed(e.core.gamma_output([A(1)],LL,w,M).coeffs())]
    def g(u): return u**mp.mpf('.25')*mp.polyval(p,u) if u>0 else mp.mpf(0)
    delays=[(e.mid(d),e.mid(b)) for d,b,_ in ds]
    def old(u): return mp.sqrt(L/a)*(sum(b*g(u-d) for d,b in delays)-g(u-a/L))
    def new(u): return mp.sqrt(L/h)*g(u-a/L)
    cuts=[d for d,_ in delays]+[mp.mpf(1)]
    funcs=[old,new]
    quad=mp.matrix([[mp.quad(lambda u:funcs[i](u)*funcs[j](u),cuts) for j in range(2)] for i in range(2)])
    moment_error=max(abs(e.mid(gram[i,j])-quad[i,j]) for i in range(2) for j in range(2))
    assert moment_error<mp.mpf('1e-50')
    data={'scope':'Independent numerical checks, not full-operator certificates.',
          'central_constant_cross_form_vs_original_kernel_error':mp.nstr(central_error,15),
          'piecewise_constant_full_output_gram_vs_quadrature_error':mp.nstr(moment_error,15),
          'all_checks_pass':True,'digits':mp.mp.dps,'bits':ctx.prec}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2),flush=True)

if __name__=='__main__':run()
