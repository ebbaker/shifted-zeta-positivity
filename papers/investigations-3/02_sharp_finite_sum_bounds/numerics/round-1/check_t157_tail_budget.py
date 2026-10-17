#!/usr/bin/env python3
"""Bounded, hash-pinned adaptation of the inherited directed Decimal checker.
Prepared for Edward Baker with LLM assistance; Codex research subagent; actual serving model/effort are not exposed here.
See PLAN.md for pre-run scope; this is an analytic-budget pilot only.
"""
import argparse, hashlib, json, resource, signal, sys, time
from fractions import Fraction as F
from pathlib import Path

SOURCE_REL='papers/investigations-2/newman_certificate_audit/numerics/check_tail_and_uniform_error_budget.py'
SOURCE_SHA256='c48c737e75baa70e9d59b22f1d71a32eb84ee1c16826df122eb9f6036311fed4'
CANDIDATES=(153814,600000)
T=F(157,1000); Y0SQ=F(87677,2500000); YMAXSQ=F(343,500)
YLO=F(1872719,10**7); YHI=F(23409,125000); EXTHI=F(8282512,10**7)

# These old application/regression gates are not the new acceptance criteria.
NONREQUIRED={
 'prop410.exact.target_identity':'historical target; replaced by new exact target gate',
 'prop410.exact.tbox':'historical time box; replaced by exact t=157/1000',
 'prop410.exact.floor>coarse_budget':'historical plain triangle floor; no new sharp row floor supplied',
 'prop410.decisive.eAB<206/10^14':'historical numeric regression corridor',
 'prop410.decisive.eC0<stated':'historical numeric regression corridor',
 'prop410.decisive.Emax<stated':'historical numeric regression corridor',
 'prop410.decisive.Emax<234/10^9':'historical numeric regression corridor',
 'prop410.decisive.Tmin-Emax>557/10^9':'historical row floor is not transferred to the new time',
 'tail.exact.target_identity':'historical target; replaced by new exact target gate',
 'tail.GN-AB.ext_hull(as_in_package)':'reverse y-then-N contraction proof only needs y-box; full-hull error gates retained',
 'tail.decisive.D<1':'contains redundant OV; replaced by OV-free contraction',
 'tail.decisive.D<0.999721':'historical OV-containing regression corridor',
 'tail.P_width<1-D':'historical OV-containing reserve; replaced by OV-free reserve test',
 'tail.decisive.flow>err>0':'historical OV-containing margin; replaced by OV-free margin',
 'tail.decisive.flow-err>0.00017352':'historical OV-containing regression corridor',
}

def replace_once(s,a,b):
    if s.count(a)!=1: raise RuntimeError('source splice no longer unique: '+repr(a))
    return s.replace(a,b)

def run(repo, M):
    start=time.monotonic()
    def timeout(signum, frame): raise TimeoutError('120 second per-candidate wall budget exceeded')
    signal.signal(signal.SIGALRM,timeout);signal.alarm(120)
    p=repo/SOURCE_REL; raw=p.read_bytes(); digest=hashlib.sha256(raw).hexdigest()
    if digest!=SOURCE_SHA256: raise RuntimeError('inherited checker hash mismatch')
    substitutions=[
      ('T_LO = F(129, 800)','T_LO = F(157, 1000)'),
      ('T_HI = F(161250001, 10 ** 9)','T_HI = F(157, 1000)'),
      ('YMAXSQ = F(271, 400)','YMAXSQ = F(343, 500)'),
      ('    M = 153814\n',f'    M = {M}\n'),
      ('F(8231039, 10 ** 7)','F(8282512, 10 ** 7)'),
      ('    return ln_lo(d), ln_hi(d)',
       '    v = CN.ln(d)\n    pad = CC.multiply(ETA, max(ONE, v.copy_abs()))\n    return CF.subtract(v, pad), CC.add(v, pad)')]
    src=raw.decode()
    for a,b in substitutions: src=replace_once(src,a,b)
    ns={'__name__':'t157_inherited_checker','__file__':str(p)}
    exec(compile(src,'hash_pinned_t157_adapter','exec'),ns)
    results={};raw_gates={};ns['prop410'](results,raw_gates);ns['tail'](results,raw_gates)
    D=ns['Dc']; rf=ns['CF']; ONE=ns['ONE']
    dp=D(results['tail.Dprime_hi(without_OV)']); flow=D(results['tail.flowprime_lo(without_OV)']); err=D(results['tail.err_hi'])
    # Results are formatted outward enclosure values to 30 digits. A one-last-digit
    # guard preserves outward direction when reading that display serialization.
    def upper_display(s):
        d=D(s); return ns['CC'].add(d,D(1).scaleb(d.adjusted()-29))
    def lower_display(s):
        d=D(s); return rf.subtract(d,D(1).scaleb(d.adjusted()-29))
    dp=upper_display(str(dp));flow=lower_display(str(flow));err=upper_display(str(err))
    pw=upper_display(results['tail.P_t_interval_width_contribution_hi'])
    emax=upper_display(results['prop410.Emax_hi'])
    new_gates={
      'new.exact.target_872677_over_5000000':T+Y0SQ/2==F(872677,5000000),
      'new.exact.t_point_157_over_1000':ns['T_LO']==T==ns['T_HI'],
      'new.exact.ymaxsq_equals_1_minus_2t':YMAXSQ==1-2*T==ns['YMAXSQ'],
      'new.exact.y_box_contains_y0':YLO**2<Y0SQ<YHI**2,
      'new.exact.ext_hi_covers_ymax':EXTHI**2>=YMAXSQ,
      'new.exact.ext_previous_grid_below_ymax':(EXTHI-F(1,10**7))**2<YMAXSQ,
      'new.exact.tail_index_unchanged_and_head_larger_than_error_head':3840000>M>3000,
      'new.tail.OV_free_Dprime_less_than_one':dp<1,
      'new.tail.OV_free_width_less_than_reserve':pw<rf.subtract(ONE,dp),
      'new.tail.OV_free_flow_greater_than_error':flow>err>0,
      'new.error.Emax_below_3e_minus_7':0<emax<D('3e-7'),
    }
    required={k:bool(v) for k,v in raw_gates.items() if k not in NONREQUIRED}
    required.update(new_gates)
    elapsed=time.monotonic()-start
    # macOS ru_maxrss is bytes; Linux ru_maxrss is KiB.
    rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    peak_bytes=rss if sys.platform=='darwin' else rss*1024
    required['resource.wall_seconds_below_120']=elapsed<120
    required['resource.peak_resident_bytes_below_512MiB']=peak_bytes<512*1024**2
    signal.alarm(0)
    return {'status':'directed enclosure pilot; no finite-row or complete Newman certificate',
      'source_relative_path':SOURCE_REL,'source_sha256':digest,
      'adapter_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'substitutions':[{'from':a,'to':b} for a,b in substitutions],
      'parameters':{'t':'157/1000','X':6000000185827,'y0_squared':'87677/2500000','ymax_squared':'343/500',
                    'N_star':3840000,'M':M,'M_err':3000,'N0':690988,'m0':2000},
      'raw_inherited_gates':raw_gates,'nonrequired_inherited_gate_reasons':NONREQUIRED,
      'new_gates':new_gates,'required_gates':required,'all_required_gates_pass':all(required.values()),
      'results':results,'runtime_seconds':elapsed,'peak_resident_bytes':peak_bytes,
      'limitations':['source theorem and reverse-order reduction imported from inherited audit note 4',
       'required error gate Emax<3e-7 is a budget declaration, not a claim that any new sharp row exceeds it',
       'no external primary-source freshness or byte-identity check is performed',
       'no new finite-row replay, complete window coverage, or y-transfer certificate is supplied']}

def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument('--repo',type=Path,required=True)
    ap.add_argument('--head',type=int,choices=CANDIDATES,required=True);ap.add_argument('--output',type=Path,required=True)
    a=ap.parse_args(); rec=run(a.repo,a.head); a.output.write_text(json.dumps(rec,indent=2)+'\n')
    print(json.dumps({'head':a.head,'all_required_gates_pass':rec['all_required_gates_pass'],
       'failed_required_gates':[k for k,v in rec['required_gates'].items() if not v],
       'false_raw_gates':[k for k,v in rec['raw_inherited_gates'].items() if not v],
       'runtime_seconds':rec['runtime_seconds'],'peak_resident_bytes':rec['peak_resident_bytes']},indent=2))
if __name__=='__main__': main()
