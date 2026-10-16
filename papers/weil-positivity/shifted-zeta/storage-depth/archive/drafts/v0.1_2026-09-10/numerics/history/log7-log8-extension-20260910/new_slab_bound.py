#!/usr/bin/env python3
"""Full-operator gamma-only new-slab contraction by a positive kernel bound."""
import hashlib
import json
from pathlib import Path
from flint import arb as A, ctx
import extension_storage as ex

def run():
    if not __debug__: raise RuntimeError('Assertions must remain enabled')
    ctx.prec=768
    M=64
    h=A(8).log()-A(7).log()
    out=[]
    assert 0<h<A(2).log()
    assert A(3).sin()>A(1)/8 and (A(3)/2).exp()<5
    assert 120+1440*A(3).exp()<32768
    for ws in ['4e-15','1e-11','1e-7']:
        w=ex.core.rat(ws)
        g=ex.core.profile(w,M)
        tail=32768*(h/3)**(M+1)/(1-h/3)
        variation=sum((abs(g[j])*h**j for j in range(1,M+1)),A(0))+tail
        assert variation<1
        # The exact real kernel is positive on (0,h). Its L1 norm is its
        # response to constant input, evaluated at the endpoint.
        p=ex.core.gamma_output([A(1)],h,w,M)
        kernel_integral_upper=(p(A(1))+ex.gamma_error(h,w,M).upper()).upper()
        assert 0<kernel_integral_upper<1
        floor=(1-kernel_integral_upper**2).lower()
        assert floor>0
        out.append({'shift_rational':ws,'positive_profile_floor':(1-variation).lower().str(35),
                    'transfer_norm_upper':kernel_integral_upper.str(50),
                    'input_and_output_storage_floor':floor.str(45),
                    'storage_floor_divided_by_2omega':(floor/(2*w)).lower().str(40),
                    'full_new_slab_contraction_pass':True})
    # Uniform bound, including the limit at zero without dividing balls by
    # omega. Each interval is exactly specified by decimal midpoint/radius.
    uniform_decay_lower=None
    uniform_profile_lower=None
    for i in range(50):
        w=A(f'0.{10*i+5:03d}','0.005')
        assert w.contains(A(i)/100) and w.contains(A(i+1)/100)
        g=ex.core.profile(w,M)
        assert g[1].contains(A(-7)/2)
        g[1]=A(-7)/2  # exact identity avoids alpha+beta interval dependency
        tail=32768*(h/3)**(M+1)/(1-h/3)
        variation=sum((abs(g[j])*h**j for j in range(1,M+1)),A(0))+tail
        assert variation<1
        J=sum((g[j]*h**j/(j+w) for j in range(1,M+1)),A(0))+tail/(M+1)
        # log Gamma(1+w) >= -EulerGamma*w+(pi^2/4-2)*w^2
        # follows by integrating trigamma(t)>=trigamma(3/2) on [1,3/2].
        decay=-((2*A.pi()*h).log()+A.const_euler()-(A.pi()**2/4-2)*w+J)
        dl,pl=decay.lower(),(1-variation).lower()
        uniform_decay_lower=dl if uniform_decay_lower is None else min(uniform_decay_lower,dl)
        uniform_profile_lower=pl if uniform_profile_lower is None else min(uniform_profile_lower,pl)
    assert uniform_decay_lower>A('0.06') and uniform_profile_lower>0
    data={'scope':'Unrestricted new slab only, length log(8/7), in the working v0.3 normalization.',
          'profile_degree':M,'precision_bits':ctx.prec,'results':out,
          'uniform_result':{'shift_range':'0 < omega <= 1/2','interval_cells':50,
              'profile_positive_floor':uniform_profile_lower.str(40),
              'decay_coefficient_lower':uniform_decay_lower.str(40),
              'rounded_norm_bound':'||Z_omega|| <= exp(-0.06*omega)',
              'rounded_storage_bound':'I-Z*Z and I-ZZ* >= (1-exp(-0.12*omega))*I',
              'pass':True},
          'source_sha256':{str(p.relative_to(ex.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(ex.__file__),Path(ex.core.__file__)]}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2),flush=True)

if __name__=='__main__': run()
