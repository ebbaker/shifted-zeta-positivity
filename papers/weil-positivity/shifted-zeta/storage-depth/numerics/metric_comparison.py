"""Additional review experiment: full-old H_J >= mu A, with archived enclosures.

This is a new validator, not a reconstruction of the supplied spatial matrices.
Its reduction is documented in the accompanying review. Assertions required.
"""
import hashlib
import argparse
import json
import gzip
import sys
import os
from pathlib import Path
from flint import arb as A, arb_mat as AM, ctx

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--paper', type=Path, required=True)
parser.add_argument('--archives', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--bits', type=int, default=2048)
parser.add_argument('--mu', nargs='+', default=['1e-7','1e-8'])
args = parser.parse_args()
BASE = args.paper.resolve()
assert not args.output.exists(), 'Choose a new output file.'
os.environ['STORAGE_DEPTH_ARCHIVES'] = str(args.archives.resolve())
sys.path.insert(0, str(BASE/'numerics'))
import archive_io
sys.path.insert(0, str(BASE/'numerics/history/quarter-step-closure-20260910'))
import close_complement as z
c = z.c

def frob2(m):
    return sum((x.abs_upper()**2 for x in m.entries()), A(0)).upper()

assert __debug__
history = json.loads((BASE/'numerics/HISTORY_RECORD.json').read_text())['sha256']
for rel,digest in history.items():
    assert archive_io.file_hash(BASE/'numerics/history'/rel) == digest, rel
path = archive_io.verify('history/quarter-step-closure-20260910/closure_256_32.matrices.json.gz')
with gzip.open(path, 'rt') as stream:
    data = json.load(stream)
for rel, digest in data['source_sha256'].items():
    assert hashlib.sha256((z.ROOT/rel).read_bytes()).hexdigest() == digest
ctx.prec = args.bits
no, nn = data['old_modes'], data['new_modes']
n = no+nn
H = AM([[c.unpack(x) for x in row] for row in data['matrices']['head']])
Go = AM([[c.unpack(x) for x in row] for row in data['matrices']['gram_old']])
proposal_path = z.ROOT/'quarter-step-20260910/residual_128_32.json'
proposal = json.loads(proposal_path.read_text())
T = AM(n,no)
for i in range(no): T[i,i] = 1
for i,row in enumerate(proposal['continuation_rational_coefficients']):
    for j,value in enumerate(row): T[no+i,j] = c.rat(value)
J = AM([[T[no+i,j] for j in range(no)] for i in range(nn)])
Ho = AM([[H[i,j] for j in range(n)] for i in range(no)])
Ao = AM([[H[i,j] for j in range(no)] for i in range(no)])
HJ = c.sym(T.transpose()*H*T)
KoGram = c.sym(Go-Ho.transpose()*Ho)
eta = c.unpack(data['eta']).upper()
e = c.unpack(data['leakage_error']).upper()
betaA = (A(data['tail_bounds']['old_gamma_tail']).lower()
         - A(data['tail_bounds']['arithmetic_norm_upper']).upper()).lower()
assert betaA>0
results=[]
for mu_text in args.mu:
    mu = c.rat(mu_text)
    assert 0 < mu < 1
    U = AM(T.tolist())
    for i in range(no): U[i,i] = 1-mu
    head = c.sym(HJ-mu*Ao)
    leakage = c.sym(U.transpose()*KoGram*U)
    beta = ((1-mu)*betaA).lower()
    herr = eta*(frob2(T)+mu)
    eerr = e*frob2(U)
    budget = (beta*herr+eerr).upper()
    sign = c.ldl(c.sym(beta*head-leakage-budget*c.ident(no)))
    item = {'mu':mu_text,'positive':sign['positive'],
            'tail_floor':beta.str(40),'error_budget':budget.str(40),
            'schur_check':sign}
    results.append(item)
    print(json.dumps({k:v for k,v in item.items() if k!='schur_check'}),flush=True)
    if sign['positive']: break
record = {'scope':'Additional full-old form comparison H_J >= mu A for the original rational continuation; archive-based validation, inherited analytic enclosures, not an independent full reconstruction.',
          'precision_bits':ctx.prec,'old_modes':no,'new_modes':nn,
          'historical_files_verified':len(history),
          'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'archive_sha256':archive_io.file_hash(path),
          'proposal_sha256':hashlib.sha256(proposal_path.read_bytes()).hexdigest(),
          'old_complement_floor':betaA.str(40),'J_frobenius_squared_upper':frob2(J).str(40),
          'attempts':results}
args.output.parent.mkdir(parents=True,exist_ok=True)
args.output.write_text(json.dumps(record,indent=2)+'\n')
