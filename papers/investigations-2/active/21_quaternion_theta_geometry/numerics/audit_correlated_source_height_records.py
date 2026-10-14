#!/usr/bin/env python3
"""Hash-bound exact semantic audit of the three final height-100 records.

2026-10-14. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: gpt-6.1-sol (Codex); reasoning effort: ultra.
Standard library only. This checks 6,682 exact-rational algebra, coverage,
classification, payment-consistency, branch, and norm conditions. It does not
replace the analytic source bounds or validated quadrature replay.
"""
import argparse
from collections import Counter, defaultdict
from fractions import Fraction as Q
from hashlib import sha256
from math import isqrt
import json
from pathlib import Path
import platform

EXPECTED_RECORDS = {
    '40_60': '7e32b3f4c0ec7e26157bccb5a7248f5f7693f9dee11cfff40527f5a7e308ad66',
    '60_80': 'c69ee97e476e44f54b75e320be4665132ab2a6aaa00ad454887bdb2155dad020',
    '80_100': '3d2c63e5b669843417f2324d26c4ba88de219b636c0bfe81d203c2ac25c5b6f3',
}
EXPECTED_SOURCE_NAMES = {
    'checker': 'certify_correlated_source_height_extension.py',
    'imported_reviewed_source': 'certify_compensated_stationary_theta.py',
}

checks=0
def need(ok,what):
    global checks
    checks+=1
    if not ok: raise AssertionError(what)
def lo(a):return Q(int(a[0][0]))*Q(2)**int(a[0][1])
def hi(a):return Q(int(a[1][0]))*Q(2)**int(a[1][1])
def separated(a):return lo(a)>0 or hi(a)<0
def sign(a):return 1 if lo(a)>0 else -1 if hi(a)<0 else 0
def dist(a):return max(Q(0),lo(a),-hi(a))


def main():
    global checks
    checks = 0
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    base = Path(__file__).resolve().parent
    # Identity checks fail before writing any output. The two source hashes
    # are verified against each exact-byte-bound certificate below, as part
    # of the 6,682 semantic checks. No wildcard or self-allowing hash is used.
    input_bindings = []
    for band, expected in EXPECTED_RECORDS.items():
        path = base / f'CORRELATED_SOURCE_HEIGHT_{band}_20261014.json'
        actual = sha256(path.read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f'Certificate byte hash mismatch: {path.name}')
        data = json.loads(path.read_text())
        for field, name in EXPECTED_SOURCE_NAMES.items():
            if data[field]['file'] != name:
                raise RuntimeError(f'Unexpected source binding in {path.name}: {field}')
        input_bindings.append({'file': path.name, 'sha256': actual})
    # Universal polynomial check independent of the imported three-channel controls.
    for n in (3,4,5):
     for j in (0,1):
      whole,paired=defaultdict(int),defaultdict(int)
      def add(d,a,b,c):d[tuple(sorted((a,b)))]+=c
      for r in range(n):
       for s in range(n):
        add(whole,(r,j+1),(s,j+1),1);add(whole,(r,j),(s,j+2),-1)
       add(paired,(r,j+1),(r,j+1),1);add(paired,(r,j),(r,j+2),-1)
       for s in range(r+1,n):
        add(paired,(r,j+1),(s,j+1),2)
        add(paired,(r,j),(s,j+2),-1);add(paired,(s,j),(r,j+2),-1)
      need(whole==paired,'General N D/X identity')

    results=[]
    for band in ('40_60','60_80','80_100'):
     p=base/f'CORRELATED_SOURCE_HEIGHT_{band}_20261014.json'
     d=json.loads(p.read_text());cells=d['cells'];n=d['parameters']['N']
     need(d['status']=='PASS' and n==4,'PASS/N4')
     for field in ('checker','imported_reviewed_source'):
      need(sha256((base/d[field]['file']).read_bytes()).hexdigest()==d[field]['sha256'],'Source hash')
     need(d['cell_count']==len(cells),'Cell count')
     need(d['domain']['t']==['0','1/2'],'Full possible positive threshold time')
     need(d['precision_bits']==256,'256 bits')
     for key in ('unresolved_sign_cells','unresolved_direct_norm_cells','unresolved_branch_windows'):
      need(not d[key],'No unresolved '+key)
     tl,tr=map(Q,d['domain']['t']);xl,xr=map(Q,d['domain']['x'])
     times=sorted({Q(v) for c in cells for v in c['t']})
     need(times[0]==tl and times[-1]==tr,'Time endpoints')
     for a,b in zip(times,times[1:]):
      mid=(a+b)/2
      spans=sorted((Q(c['x'][0]),Q(c['x'][1])) for c in cells if Q(c['t'][0])<mid<Q(c['t'][1]))
      need(spans[0][0]==xl and spans[-1][1]==xr,'Exact spatial endpoints')
      need(all(u<v for u,v in spans) and all(spans[k][1]==spans[k+1][0] for k in range(len(spans)-1)),'Exact gap-free cover')
     totals={str(j):dict(Counter(c['observations'][j]['classification'] for c in cells)) for j in (0,1)}
     need(totals==d['observation_totals'],'Observation totals')
     minima={str(j):[] for j in(0,1)}
     sq=[]
     for c in cells:
      need(tl<=Q(c['t'][0])<Q(c['t'][1])<=tr and xl<=Q(c['x'][0])<Q(c['x'][1])<=xr,'Cell containment')
      need(all(Q(v).denominator&(Q(v).denominator-1)==0 for v in c['t']+c['x']),'Dyadic endpoints')
      pay=d['shared_complete_index_payments'][c['complete_index_payment_reference']]
      need(pay['x_left']==c['x'][0],'All-index reference left height')
      eps=pay['complete_compensated_four_jet_errors']
      for k in range(4):
       C=d['complete_index_tail']['norm_constants_C_j'][k]
       need(max(lo(eps[k]),lo(C)/Q(c['x'][0])**4)<=min(hi(eps[k]),hi(C)/Q(c['x'][0])**4),'Index payment agrees scale')
      par=d['shared_parameter_Taylor_payments'][c['parameter_Taylor_payment_reference']]
      need(par['t']==c['t'] and Q(par['space_radius'])==(Q(c['x'][1])-Q(c['x'][0]))/2,'Taylor payment references')
      need(len(par['raw_source_parameter_Taylor_payments'])==4,'Four retained raw-channel payments')
      sq.append(sum(dist(v)**2 for v in c['genuine_four_jets'][:2]))
      for j,o in enumerate(c['observations']):
       need(o['j']==j and o['genuine_stationary_derivative']==c['genuine_four_jets'][j+1],'Genuine derivative storage')
       cl=o['classification']
       if cl=='stationarity_excluded':
        if not separated(o['genuine_stationary_derivative']):
         need(separated(o['genuine_next_derivative']) and sign(o['left_stationary_derivative'])==sign(o['right_stationary_derivative'])!=0,'Monotone same-sign endpoint exclusion')
       else:
        need(cl.startswith('stationary_signed'),'Resolved signed cell')
        need(len(o['diagonal_terms'])==n and len(o['cross_terms'])==n*(n-1)//2,'All N4 D/X terms')
        need(o['cross_index_pairs']==[[r,s] for r in range(1,n+1) for s in range(r+1,n+1)],'All six N4 cross pairs')
        need(lo(o['correlated_cross_term_surplus_L_P_minus_payment'])>0,'Strict paid stationary surplus')
        minima[str(j)].append(lo(o['correlated_cross_term_surplus_L_P_minus_payment']))
        pp=c['compensated_aggregate_jets']
        maxabs=lambda a:max(abs(lo(a)),abs(hi(a)))
        fee_upper=hi(eps[j+1])**2+maxabs(pp[j])*hi(eps[j+2])+maxabs(pp[j+2])*hi(eps[j])+hi(eps[j])*hi(eps[j+2])
        # Strict exact-rational upper-fee comparison: no tolerance enters this audit.
        need(hi(o['stationary_error_payment'])>=fee_upper,'Complete stationary fee')
     for j in(0,1):
      v=min(minima[str(j)])
      need(v==Q(d['minimum_stationary_surplus_exact_rational'][str(j)]),'Exact stationary minimum')
      need(v>Q(1 if j==0 else 2,10**(30 if j==0 else 32)),'Convenient strict stationary floor')
     gap=d['uniform_genuine_norm_gap'];minsq=min(sq);g=Q(gap['rational_norm_lower_bound'])
     need(Q(gap['minimum_cellwise_squared_lower_bound'])==minsq,'Exact physical norm square')
     need(g==Q(isqrt(minsq.numerator*2**256//minsq.denominator),2**128),'Directed rational square root')
     need(g*g<=minsq and g>Q(1,4*10**15),'Positive direct norm floor')
     branches=[]
     for a,b in zip(times,times[1:]):
      mid=(a+b)/2
      slab=sorted((c for c in cells if Q(c['t'][0])<mid<Q(c['t'][1])),key=lambda c:Q(c['x'][0]))
      for j in(0,1):
       groups=[];group=[]
       for c in slab:
        if c['observations'][j]['classification'].startswith('stationary_signed'):group.append(c)
        elif group:groups.append(group);group=[]
       if group:groups.append(group)
       for group in groups:
        signs={sign(c['genuine_four_jets'][j+2]) for c in group}
        need(len(signs)==1 and 0 not in signs,'Strict common next derivative on branch window')
        s=next(iter(signs));ls=group[0]['observations'][j]['left_stationary_derivative'];rs=group[-1]['observations'][j]['right_stationary_derivative']
        need(sign(ls)==-s and sign(rs)==s,'Opposite endpoint branch signs')
        branches.append(([str(a),str(b)],j,[group[0]['x'][0],group[-1]['x'][1]],len(group),s))
     stored=[(v['t'],v['j'],v['x_window'],v['member_cell_count'],v['next_derivative_sign']) for v in d['regular_stationary_branch_windows']]
     need(branches==stored and all(v['uniform_unique_regular_branch'] for v in d['regular_stationary_branch_windows']),'Complete branch-window replay')
     results.append({'band':band,'cells':len(cells),'totals':totals,'branch_windows':len(branches),'minimum_surplus':[str(min(minima[str(j)])) for j in(0,1)],'norm_floor':str(g),'record_sha256':sha256(p.read_bytes()).hexdigest()})
    if checks != 6682:
        raise RuntimeError(f'Unexpected semantic check count: {checks}')
    source_bindings = [{'file': name, 'sha256': sha256((base/name).read_bytes()).hexdigest()}
                       for name in EXPECTED_SOURCE_NAMES.values()]
    record = {
        'schema': 'inv21-higher-height-record-audit-v1',
        'date': '2026-10-14',
        'provenance': {'prepared_for': 'Edward Baker', 'llm_assistance': 'substantial',
                       'recorded_model': 'gpt-6.1-sol (Codex)', 'reasoning_effort': 'ultra'},
        'runtime': {'python': platform.python_version(), 'arithmetic': 'exact fractions; standard library only'},
        'auditor': {'file': Path(__file__).name, 'sha256': sha256(Path(__file__).read_bytes()).hexdigest()},
        'bound_inputs': input_bindings,
        'bound_generating_sources': source_bindings,
        'semantic_checks_passed': checks,
        'status': 'PASS',
        'band_results': results,
        'combined': {'cell_count': sum(v['cells'] for v in results),
                     'stationarity_excluded_observations': sum(v['totals'][str(j)].get('stationarity_excluded',0)
                                                             for v in results for j in (0,1)),
                     'strict_signed_observations': sum(sum(count for classification,count in v['totals'][str(j)].items()
                                                          if classification.startswith('stationary_signed'))
                                                      for v in results for j in (0,1)),
                     'regular_time_slab_branch_windows': sum(v['branch_windows'] for v in results),
                     'unresolved_sign_cells': 0, 'unresolved_direct_norm_cells': 0, 'unresolved_branch_windows': 0,
                     'exact_stationary_floors': {'0': str(Q(1,10**30)),
                                                  '1': str(Q(2,10**32))},
                     'exact_strict_norm_floor': str(Q(1,4*10**15))},
        'limitations': ['A semantic audit complements the independently replayed validated quadrature and analytic source bounds.',
                        'The certified rectangle is bounded; no all-height nonvanishing or RH conclusion.'],
    }
    payload = json.dumps(record, sort_keys=True, indent=2)+'\n'
    if len(payload.encode()) >= 1048576:
        raise RuntimeError('Audit record must stay below one MiB')
    args.output.write_text(payload)
    print(json.dumps({'status': 'PASS', 'semantic_checks_passed': checks,
                      'cells': record['combined']['cell_count'],
                      'regular_time_slab_branch_windows': record['combined']['regular_time_slab_branch_windows'],
                      'record_bytes': len(payload.encode())}, indent=2))


if __name__ == '__main__':
    main()
