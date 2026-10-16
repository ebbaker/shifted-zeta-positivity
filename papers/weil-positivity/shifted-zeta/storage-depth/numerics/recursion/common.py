"""Pinned arithmetic dependencies and exact logarithmic geometry."""
from fractions import Fraction
from pathlib import Path
import hashlib
import json
import sys
from flint import arb as A, arb_mat as AM, arb_poly as AP, fmpq

PAPER = Path(__file__).resolve().parents[2]
V01 = PAPER/'archive/drafts/v0.1_2026-09-10'
HISTORY = V01/'numerics/history'
sys.path.insert(0,str(V01/'numerics'))
import archive_io as legacy_io
sys.path.insert(0,str(HISTORY/'quarter-step-20260910'))
import central_residual as residual
c = residual.c

def verify_legacy():
    records=json.loads((V01/'numerics/HISTORY_RECORD.json').read_text())['sha256']
    for rel,digest in records.items():
        assert hashlib.sha256((HISTORY/rel).read_bytes()).hexdigest()==digest,rel
    return len(records)

def rat(x):
    q=Fraction(x)
    return A(fmpq(q.numerator,q.denominator))

class LogPoint:
    """A rational linear combination of prime logarithms; equality is exact."""
    def __init__(self,terms=()):
        d={}
        for p,v in (terms.items() if isinstance(terms,dict) else terms):
            d[int(p)]=d.get(int(p),Fraction(0))+Fraction(v)
        self.terms=tuple(sorted((p,v) for p,v in d.items() if v))
    def __add__(self,other): return LogPoint(self.terms+other.terms)
    def __neg__(self): return LogPoint((p,-v) for p,v in self.terms)
    def __sub__(self,other): return self+-other
    def __mul__(self,x): return LogPoint((p,v*Fraction(x)) for p,v in self.terms)
    __rmul__=__mul__
    def __truediv__(self,x): return self*Fraction(1,x)
    def __eq__(self,other): return isinstance(other,LogPoint) and self.terms==other.terms
    def __hash__(self): return hash(self.terms)
    def value(self): return sum((rat(v)*A(p).log() for p,v in self.terms),A(0))
    def __lt__(self,other):
        if self==other:return False
        delta=(other-self).value()
        assert delta>0 or delta<0, 'Unresolved logarithmic endpoint ordering'
        return delta>0
    def json(self):return [[p,str(v)] for p,v in self.terms]
    @classmethod
    def read(cls,data):return cls((p,Fraction(v)) for p,v in data)

ZERO=LogPoint()
def logn(n):
    d={};p=2
    while p*p<=n:
        while n%p==0:d[p]=d.get(p,0)+1;n//=p
        p+=1
    if n>1:d[n]=d.get(n,0)+1
    return LogPoint(d)

def active_powers(L):
    active=[];n=2
    while logn(n)<L:
        d=logn(n).terms
        if len(d)==1:active.append((n,d[0][0],int(d[0][1])))
        n+=1
    return active

def ident(n):return c.ident(n)
def frob2(m):return sum((x.abs_upper()**2 for x in m.entries()),A(0)).upper()
def matrix(polys):
    k=max(1,max(p.degree()+1 for p in polys))
    return AM([[p[j] for j in range(k)] for p in polys])
def rows(m):return [AP([m[i,j] for j in range(m.ncols())]) for i in range(m.nrows())]
def legendre(n):
    return [residual.ex.legendre(i,A(0),A(1),A(1)) for i in range(n)]
def sub(m,rows,cols):return AM([[m[i,j] for j in cols] for i in rows])
def setblock(m,block,i,j):
    for r in range(block.nrows()):
        for s in range(block.ncols()):m[i+r,j+s]=block[r,s]
def source_hashes():
    return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(Path(__file__).parent.glob('*.py'))}

def ldl(mat):
    """Guarded LDL with finite failure records and safe real-ball squares."""
    n=mat.nrows();low=[[A(0) for _ in range(n)] for _ in range(n)];piv=[]
    for i in range(n):
        v=mat[i,i]
        for k in range(i):v-=low[i][k]*low[i][k]*piv[k]
        if not v.is_finite():
            return {'positive':False,'failed_pivot':i,'reason':'Non-finite interval pivot','pivot':v.str(35)}
        if not v>0:
            return {'positive':False,'failed_pivot':i,'pivot':v.str(35),'pivot_ball':c.pack(v)}
        piv.append(v)
        for j in range(i+1,n):
            w=mat[j,i]
            for k in range(i):w-=low[j][k]*low[i][k]*piv[k]
            low[j][i]=w/v
    return {'positive':True,'minimum_pivot_lower':min(x.lower() for x in piv).str(35),
            'pivots':[c.pack(x) for x in piv]}
