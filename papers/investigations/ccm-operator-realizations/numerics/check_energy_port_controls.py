#!/usr/bin/env python3
"""Exact controls: fixed first mass and bounded total mass do not ensure tightness."""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path


def run():
    rows=[]
    for R in (10,100,1000):
        t=F(1,4)
        k2=F(1,R-1)
        K=[[1+k2,-k2],[-k2,k2]]
        M=[F(1),F(2,R)]
        def det(A):
            return A[0][0]*A[1][1]-A[0][1]*A[1][0]
        assert K[0][0]>0 and det(K)>0 and min(M)>0
        polynomial=det([[K[0][0]-t*M[0],K[0][1]],
                        [K[1][0],K[1][1]-t*M[1]]])/det(K)
        expected=1-3*t+2*(1-F(1,R))*t*t
        assert polynomial==expected
        response=(K[1][1]-t*M[1])/(det(K)*polynomial)
        assert response==(1-2*(1-F(1,R))*t)/expected
        rows.append(dict(R=R,total_mass=str(1+F(2,R)),first_position=1,trace=3,
            far_atom_first_moment=2,determinant_at_z_half=str(polynomial),
            response_at_t_quarter=str(response)))
    return dict(date='2026-09-26',status='exact rational arithmetic controls',
        model='GPT-6 (Codex); exact variant and reasoning effort not exposed',
        source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        convention='t=z^2, masses (1,2/R), positions (1,R), first bead mass one',
        formula='P(t)=1-3*t+2*(1-1/R)*t^2; response=(1-2*(1-1/R)*t)/P(t)',
        cases=rows)


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',type=Path,default=Path(__file__).parent/'records'/'energy_port_exact_controls_20260926.json')
    args=p.parse_args()
    result=run()
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(result,indent=2)+'\n')
    print('Exact rational determinant, response, and positivity controls passed.')


if __name__=='__main__':
    main()
