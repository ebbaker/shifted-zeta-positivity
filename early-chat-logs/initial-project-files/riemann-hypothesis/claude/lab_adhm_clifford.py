import numpy as np, sympy as sp, itertools
# real symmetric anticommuting triples: T_a T_b + T_b T_a = 2 delta_ab I.
# k=4: use real symmetric Clifford generators.
X=np.array([[0,1],[1,0]]); Z=np.array([[1,0],[0,-1]]); Y=np.array([[0,-1],[1,0]])  # Y antisym
kr=np.kron
G=[kr(X,np.eye(2)), kr(Z,np.eye(2)), kr(Y,Y)]   # all real; check symmetry & Clifford
for a,A in enumerate(G): assert np.allclose(A,A.T), a
for a in range(3):
    for b in range(3):
        assert np.allclose(G[a]@G[b]+G[b]@G[a], 2*(a==b)*np.eye(4)), (a,b)
print('k=4: found real symmetric anticommuting triple  T_a^2=I:', True)
T=[np.zeros((4,4))]+[g.astype(float) for g in G]
lam=np.zeros((4,4))
C=sum(t@t for t in T)
print('C = %s * I'%(C[0,0]))
x0,x1,x2,x3=sp.symbols('x0 x1 x2 x3',real=True)
M=sp.Matrix(C)+ (x0**2+x1**2+x2**2+x3**2)*sp.eye(4) - 2*(x0*sp.Matrix(T[0])+x1*sp.Matrix(T[1])+x2*sp.Matrix(T[2])+x3*sp.Matrix(T[3]))
d=sp.factor(sp.expand(sp.det(M)))
print('det M =',d)
# is det M a polynomial in x0 and r^2 ?  test rotation invariance in the imaginary part
r=sp.sqrt(x1**2+x2**2+x3**2)
print('det M with (x1,x2,x3)->(r,0,0):', sp.factor(sp.expand(d.subs({x1:sp.Symbol("R"),x2:0,x3:0}))))
print('det M with (x1,x2,x3)->(0,0,r):', sp.factor(sp.expand(d.subs({x1:0,x2:0,x3:sp.Symbol("R")}))))
