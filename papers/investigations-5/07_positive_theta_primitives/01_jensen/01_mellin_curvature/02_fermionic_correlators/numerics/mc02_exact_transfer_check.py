"""MC02-B01 finite exact transfer checks: no theta acquisition or scans."""
from fractions import Fraction as Q
import itertools,json
c=[Q(1),Q(1),Q(2)];v=Q(1);Z=sum(a*v**i for i,a in enumerate(c))
def coeff(n):return c[n] if 0<=n<len(c) else Q(0)
def K(i,j):return coeff(j-i)*v**(j-i)/Z
def det2(a):return a[0][0]*a[1][1]-a[0][1]*a[1][0]
I=[0,1];J=[1,2]
amp=det2([[K(i,j) for j in J]for i in I]);minor=det2([[coeff(j-i)for j in J]for i in I]);scale=v**(sum(J)-sum(I))/Z**2
assert amp==scale*minor==Q(-1,16)
assert sum(a*v**i/Z for i,a in enumerate(c))==1
# For B=[[d,b],[0,d]], coefficient of alpha in (GB-B^T G)_(0,1) is b.
d=K(0,0);b=K(0,1);alpha=Q(3);z=Q(7);delta=Q(11)
G=[[alpha,z],[z,delta]];B=[[d,b],[Q(0),d]]
def mul(A,B):return [[sum(A[i][k]*B[k][j]for k in range(2))for j in range(2)]for i in range(2)]
GB=mul(G,B);BtG=mul([[B[j][i]for j in range(2)]for i in range(2)],G)
assert GB[0][1]-BtG[0][1]==alpha*b
print(json.dumps({'scope':'one explicit coefficient-transfer relaxation and an illustrative exact commutator check; symbolic metric proof is in the note','coefficients':[str(a)for a in c],'v':str(v),'normalizer':str(Z),'one_particle_weights':[str(a*v**i/Z)for i,a in enumerate(c)],'rows':I,'columns':J,'unscaled_minor':str(minor),'positive_rescaling':str(scale),'fermion_amplitude':str(amp),'commutator_01':str(GB[0][1]-BtG[0][1]),'alpha_times_b':str(alpha*b),'passed':True},indent=2))
