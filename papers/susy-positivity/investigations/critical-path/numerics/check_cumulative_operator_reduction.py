#!/usr/bin/env python3
"""Independent floating quadrature checks of the certified mixed coefficients.

The sign certificate is certify_cumulative_operator_coupling.py, not this
diagnostic. Reuses the earlier physical-delay quadrature, which does not use
the certificate's digamma/Euler--Maclaurin matrix construction.
"""
import argparse,hashlib,importlib.util,json,platform
from pathlib import Path
import numpy as np

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--repository',type=Path)
    ap.add_argument('--certificate',type=Path,required=True)
    ap.add_argument('--output',type=Path,required=True)
    args=ap.parse_args()
    root=args.repository or Path(__file__).resolve().parents[5]
    folder=root/'papers/susy-positivity/investigations/critical-path/numerics'
    pilot=load('earlier_ema_pilot',folder/'adaptive_ema_pilot.py')
    diag=load('earlier_append_diagnostic',folder/'diagnose_cumulative_append.py')
    cert=json.loads(args.certificate.read_text())
    assert cert['certificate_pass'] and cert['cumulative_coupling_upper']=='951/1000'
    certificate_source=Path(__file__).with_name('certify_cumulative_operator_coupling.py')
    assert cert['source_sha256']==hashlib.sha256(certificate_source.read_bytes()).hexdigest(), 'Certificate source hash mismatch; regenerate it with the current source.'
    target=np.array(cert['control_H_first8_integer_matrix'],dtype=float)/cert['control_H_matrix_denominator']
    runs=[]
    for order,inner in [(96,64),(144,96)]:
        _,central=diag.mixed(pilot,pilot.parent.Kernel(.001,24),8,order,inner)
        # Earlier mixed() uses physical old coordinate y; the certificate
        # reflects to r=L-y. Cosine reflection contributes (-1)^j.
        direct=-central*((-1.)**np.arange(8))[None,:]
        error=float(np.max(np.abs(direct-target)))
        assert error<1e-9
        runs.append({'delay_order':order,'cross_section_order':inner,
                     'maximum_coefficient_error':error})
    out={'date':'2026-09-20','model':'OpenAI GPT-6 (Codex; developer-provided identity)',
         'reasoning_effort':'Not exposed in this session; not inferred',
         'status':'Floating reduction check, not an interval sign certificate',
         'python':platform.python_version(),'numpy':np.__version__,'runs':runs,
         'certificate_sha256':hashlib.sha256(args.certificate.read_bytes()).hexdigest(),
         'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'inherited_source_sha256':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()
             for p in (folder/'adaptive_ema_pilot.py',folder/'diagnose_cumulative_append.py',pilot.PARENT)},
         'check_pass':True}
    args.output.parent.mkdir(parents=True,exist_ok=True)
    args.output.write_text(json.dumps(out,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'check_pass':True,'runs':runs},indent=2))

if __name__=='__main__':
    if not __debug__:raise SystemExit('Do not disable diagnostic assertions with python -O.')
    main()
