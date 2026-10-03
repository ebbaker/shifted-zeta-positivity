#!/usr/bin/env python3
"""Reproduce independent quadrature crosschecks of the floating extension pilot.

Prepared with substantial LLM assistance, GPT-6 (Codex), 2026-10-03.
Serving variant and reasoning effort are not exposed. No outward certificate.
"""
import importlib.util,json,hashlib,numpy as np
from pathlib import Path
path=Path(__file__).with_name('pilot_extension.py')
spec=importlib.util.spec_from_file_location('p',path);p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
record=json.loads(path.with_name('pilot_10000.json').read_text());results=[]
for case in record['cases']:
 proj=p.Projection(case['rank']);sources=[np.array(x['finite_polynomial_legendre_coefficients']) for x in case['raw_worst_directions']]+[np.array(case['signed_worst_direction']['finite_polynomial_legendre_coefficients'])]
 alt=p.actual_q_diagnostics(proj,sources,order=24)
 prior=case['actual_q_diagnostics']['quadrature'];diff=max(abs(x-y) for a,b in zip(alt['quadrature'],prior) for x,y in zip(a['finite_q_values'],b['finite_q_values']))
 z,w=np.polynomial.legendre.leggauss(256);y=z/2;w=w/2
 constraints=np.array([np.ones_like(y),np.sinh(proj.alpha*y)/np.sqrt(proj.ns),(np.cosh(proj.alpha*y)-proj.mean)/np.sqrt(proj.nc)])
 leg=np.polynomial.legendre.legvander(z,proj.rank-1).T*np.sqrt(2*proj.n[:,None]+1)
 times=np.array([.01,.5,10,99.999]);planes=np.exp(1j*p.L*y[:,None]*times[None,:]);projected=planes-constraints.T@(constraints@(w[:,None]*planes))
 direct=leg@(w[:,None]*projected);direct[1::2]/=1j
 analytic=proj.planes(times)
 coefferr=float(np.max(abs(direct-analytic)))
 results.append(dict(lambda_=case['lambda_'],rank=proj.rank,actual_q_GL16_vs_GL24_max_difference=diff,projected_plane_vs_direct_spatial_gauss_max_difference=coefferr,spatial_gauss_nodes=256,frequencies=times.tolist(),q_GL24=alt['quadrature']))
assert all(x['actual_q_GL16_vs_GL24_max_difference']<1e-8 and x['projected_plane_vs_direct_spatial_gauss_max_difference']<1e-9 for x in results)
result=dict(check_script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), status='FLOATING_CROSSCHECK_NOT_A_CERTIFICATE',pilot_script_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),input_record_sha256=hashlib.sha256(path.with_name('pilot_10000.json').read_bytes()).hexdigest(),checks=results)
path.with_name('pilot_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
