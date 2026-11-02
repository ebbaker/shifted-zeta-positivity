"""MC03-B01: four bounded exact Gaussian polynomial checks; no theta sampling."""
from fractions import Fraction as F
import itertools,json,hashlib

def add(a,b):
 c=a.copy()
 for k,v in b.items(): c[k]=c.get(k,F(0))+v
 return {k:v for k,v in c.items() if v}
def mul(a,b):
 c={}
 for i,v in a.items():
  for j,w in b.items():
   k=tuple(i[t]+j[t] for t in range(3));c[k]=c.get(k,F(0))+v*w
 return {k:v for k,v in c.items() if v}
one={(0,0,0):F(1)}; x=[{tuple(int(i==j) for i in range(3)):F(1)} for j in range(3)]
v=one
for i in range(3):
 for j in range(i+1,3):v=mul(v,add(x[j],{k:-a for k,a in x[i].items()}))
v2=mul(v,v);S={};Q={}
for a in x:S=add(S,a);Q=add(Q,mul(a,a))
def gm(n):
 if n%2:return F(0)
 z=F(1)
 for j in range(1,n,2):z*=j
 return z
def avg(p):
 z=F(0)
 for k,v in p.items():
  for n in k:v*=gm(n)
  z+=v
 return z
norm=avg(v2)
values={'vandermonde_squared_normalization_over_three_independent_normals':norm,'trace_mean':avg(mul(v2,S))/norm,'trace_second_moment':avg(mul(v2,mul(S,S)))/norm,'quadratic_norm_mean':avg(mul(v2,Q))/norm,'trace_squared_times_quadratic_norm':avg(mul(v2,mul(mul(S,S),Q)))/norm}
expected=[F(12),F(0),F(3),F(9),F(33)]
assert list(values.values())==expected
print(json.dumps({'scope':'bounded exact Gaussian polynomial normalization and four moments; no theta evaluation','values':{k:str(v) for k,v in values.items()},'fixed_box_L':12,'gaussian_mass_outside_bound':str(F(9,144)),'gaussian_trace_squared_outside_bound':str(F(33,144)),'passed':True},indent=2))
