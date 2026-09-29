#!/usr/bin/env python3
"""Small eigenbasis/precision summary of already saved floating observations.

GPT-6 (Codex); exact variant and effort not exposed. 2026-09-28. No new eigenvalue calculation.
"""
import hashlib
import json
from decimal import Decimal,localcontext
from pathlib import Path

HERE=Path(__file__).resolve().parent
paths=[HERE/'xi-ground-comparison-90.json',HERE/'xi-ground-comparison-130.json']
data=[json.loads(p.read_text()) for p in paths]
if data[0]['source_hashes']!=data[1]['source_hashes']:
    raise ValueError('Source identity changed between precision runs.')
resolved_sources={}
for path,digest in data[0]['source_hashes'].items():
    candidates=(HERE/'run-sources'/Path(path).name,HERE/Path(path).name,Path(path))
    match=next((p for p in candidates if p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==digest),None)
    if match is None:
        raise ValueError('Missing original run source '+path)
    resolved_sources[path]=str(match.resolve())
def mapping(record):return {(r['X'],r['N']):r for r in record['cases']}
low,high=map(mapping,data)
selected={**low,**high}
out=dict(date='2026-09-28',model='GPT-6 (Codex)',exact_serving_variant='not exposed',reasoning_effort='not exposed',
    status='derived floating diagnostics; not interval certification',
    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    input_sha256={p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
    source_bindings_verified=True,original_run_source_resolution=resolved_sources,
    precision_comparisons=[],eigenbasis_cases=[])
with localcontext() as ctx:
    ctx.prec=90
    for key in sorted(low.keys() & high.keys()):
        a,b=low[key],high[key]
        fields=('candidate_rayleigh','finite_candidate_residual','second_even_minus_rayleigh',
                'overlap','full_candidate_ground_distance','candidate_projection_tail_norm',
                'ground_signed_half_second_moment','finite_even_ground_gap')
        differences={name:abs(Decimal(a[name])-Decimal(b[name]))/max(abs(Decimal(a[name])),abs(Decimal(b[name])))
                     for name in fields}
        eigen_diffs=[abs(Decimal(x)-Decimal(y))/max(abs(Decimal(x)),abs(Decimal(y)))
                     for x,y in zip(a['even_eigenvalues'],b['even_eigenvalues'])]
        out['precision_comparisons'].append(dict(X=key[0],N=key[1],
            observable_relative_differences=differences,even_eigenvalue_relative_differences=eigen_diffs,
            gate_sign_agrees=a['residual_gate_positive']==b['residual_gate_positive']))
        if max(list(differences.values())+eigen_diffs)>Decimal('1e-20'):
            raise ArithmeticError('The requested 20-digit relative agreement failed.')
    for key,row in sorted(selected.items()):
        if key[1] not in (32,64):continue
        lam=list(map(Decimal,row['even_eigenvalues']))
        weight=list(map(Decimal,row['retained_candidate_even_spectral_weights']))
        rho=Decimal(row['candidate_rayleigh'])
        r2=Decimal(row['finite_candidate_residual'])**2
        residual=[(e-rho)**2*w for e,w in zip(lam,weight)]
        energy=[e*w for e,w in zip(lam,weight)]
        cumulative=[sum(weight[:j+1]) for j in range(len(weight))]
        out['eigenbasis_cases'].append(dict(X=key[0],N=key[1],
            first_four_weights=weight,cumulative_weight_first_one_to_four=cumulative,
            weight_outside_first_four=1-sum(weight),
            residual_squared_first_four=residual,
            fraction_residual_squared_first_four=sum(residual)/r2,
            fraction_residual_squared_remainder=1-sum(residual)/r2,
            rayleigh_contributions_first_four=energy,
            fraction_rayleigh_first_four=sum(energy)/rho,
            candidate_excited_mass=1-weight[0],
            comment='These are finite even eigenspace weights. The remainder includes retained modes 4..N, not the uncomputed infinite Fourier complement.'))
def serialize(x):
    if isinstance(x,Decimal):return str(x)
    if isinstance(x,dict):return {k:serialize(v) for k,v in x.items()}
    if isinstance(x,list):return [serialize(v) for v in x]
    return x
dest=HERE/'xi-ground-comparison-summary.json'
dest.write_text(json.dumps(serialize(out),indent=2)+'\n')
print(json.dumps(serialize(out),indent=2))
