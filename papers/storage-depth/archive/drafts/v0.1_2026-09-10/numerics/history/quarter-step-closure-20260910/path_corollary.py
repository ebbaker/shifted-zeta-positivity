"""Positive-shift consequences of the spatial closure certificate alone."""
import hashlib
import json
from pathlib import Path
from flint import arb as A,ctx
import close_complement as z

def run():
    ctx.prec=1024
    here=Path(__file__).resolve().parent
    path=here/'closure_256_32.json'
    record=json.loads(path.read_text())
    assert record['full_operator_certificate_pass']
    for rel,digest in record['source_sha256'].items():
        assert hashlib.sha256((z.ROOT/rel).read_bytes()).hexdigest()==digest
    assert hashlib.sha256((here/record['matrix_archive']).read_bytes()).hexdigest()==record['matrix_archive_sha256']
    L=A(7).log()+(A(8).log()-A(7).log())/4
    m=z.c.rat(record['requested_full_coercivity'])
    g=z.c.profile(record['profile_degree'])
    C=z.c.analytic(L,g,record['old_modes'],z.c.prime_powers(L),None)['generator_change_constant']
    omega=z.c.rat('5e-18')
    assert C*omega**2<m/2
    storage=-(-m*omega).expm1()
    assert storage>z.c.rat('4.99e-51')
    data={'scope':'Full-operator positive-shift consequences of the spatial central certificate. Working v0.3 normalization.',
          'quarter_depth':L.str(40),'central_coercivity':record['requested_full_coercivity'],
          'generator_change_constant_upper':C.upper().str(40),'safe_shift_interval':'0 < omega <= 5e-18',
          'shift_change_at_upper_endpoint_upper':(C*omega**2).upper().str(40),'uniform_shifted_generator_floor':'5e-34',
          'transfer_norm_bound':'||V_{omega,L}|| <= exp(-5e-34*omega) for L <= L_quarter',
          'cumulative_defect_bound':'D_{omega,L} >= (1-exp(-1e-33*omega)) I',
          'cumulative_relative_coupling_squared_bound':'c_D(omega)^2 <= exp(-1e-33*omega)',
          'storage_floor_at_upper_shift_endpoint':storage.lower().str(40),'all_checks_pass':True,
          'spatial_certificate_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
          'source_sha256':{str(p.relative_to(z.ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__).resolve(),Path(z.__file__),Path(z.c.__file__)]}}
    (here/'path_corollary.json').write_text(json.dumps(data,indent=2)+'\n')
    print(json.dumps(data,indent=2))

if __name__=='__main__':run()
