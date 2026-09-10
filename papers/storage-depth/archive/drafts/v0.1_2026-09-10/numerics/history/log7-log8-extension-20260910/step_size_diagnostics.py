#!/usr/bin/env python3
"""Compare shorter first steps, keeping old depth and input dimensions fixed."""
import json
import hashlib
from pathlib import Path
import mpmath as mp
from flint import arb as A,ctx
import central_geometry as c

def run():
    ctx.prec=4096
    mp.mp.dps=100
    no,nn,M=128,32,320
    a=A(7).log()
    hmax=A(8).log()-a
    g=c.c.profile(M)
    Ao=c.old.head(c.c,7,no,M,return_balls=True)
    aa=c.ex.tomp(Ao)
    out=[]
    for denominator in [4,2,1]:
        h=hmax/denominator
        F=c.gamma_head(nn,h,M,g)
        B,*_=c.cross(no,nn,a,h,M,g)
        c2,_=c.coupling(c.ex.tomp(B),aa,c.ex.tomp(F))
        eta=c.c.rat({4:'1e-7',2:'1e-11',1:'1e-17'}[denominator])
        def error(t): return 256*(t/3)**(M+1)/((M+1)*(1-t/3))
        joint=c.ex.AM(no+nn,no+nn)
        for i in range(no+nn):
            for j in range(no+nn):
                joint[i,j]=(1-eta)*Ao[i,j] if i<no and j<no else F[i-no,j-no] if i>=no and j>=no else B[i-no,j] if i>=no else B[j-no,i]
        guarded=joint-c.ex.ident(no+nn)*(error(a+h)+eta*error(a)).upper()
        check=c.c.ldl(guarded)
        assert check['positive']
        out.append({'fraction_of_log8_over7':f'1/{denominator}',
                    'h':mp.nstr(c.ex.mid(h),25),
                    'central_finite_relative_slack':mp.nstr(1-c2,35),
                    'proved_finite_relative_slack_lower':{4:'1e-7',2:'1e-11',1:'1e-17'}[denominator],
                    'finite_relative_slack_with_profile_error_pass':True})
    data={'scope':'Finite-input central diagnostics and relative-slack lower bounds with profile error. No full-coupling upper bound or unrestricted extension.',
          'old_input_modes':no,'new_input_modes':nn,'profile_degree':M,'precision_bits':ctx.prec,
          'results':out,'source_sha256':{str(p.relative_to(c.ex.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(c.__file__),Path(c.ex.__file__),Path(c.old.__file__),Path(c.c.__file__)]}}
    Path(__file__).with_suffix('.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2),flush=True)

if __name__=='__main__':run()
