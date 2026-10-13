"""Quaternionic matrix algebra over sympy, for the ADHM check.

A quaternionic matrix X is represented as a list of four REAL sympy matrices
[X0, X1, X2, X3] meaning  X = X0 + X1 i + X2 j + X3 k.  This is legitimate
because real matrices commute with the units e_a, so

    X Y = sum_{a,b} (X_a Y_b) (e_a e_b)

with X_a Y_b an ordinary matrix product.  Conjugate transpose:

    X^dag = X0^T - X1^T i - X2^T j - X3^T k .
"""
import sympy as sp

# quaternion multiplication table: MUL[a][b] = (sign, index) for e_a e_b
MUL = [[(1, 0), (1, 1), (1, 2), (1, 3)],
       [(1, 1), (-1, 0), (1, 3), (-1, 2)],
       [(1, 2), (-1, 3), (-1, 0), (1, 1)],
       [(1, 3), (1, 2), (-1, 1), (-1, 0)]]


def qzeros(r, c):
    return [sp.zeros(r, c) for _ in range(4)]


def qmul(X, Y):
    """Quaternionic matrix product."""
    r, c = X[0].rows, Y[0].cols
    Z = [sp.zeros(r, c) for _ in range(4)]
    for a in range(4):
        if X[a].is_zero_matrix:
            continue
        for b in range(4):
            if Y[b].is_zero_matrix:
                continue
            s, idx = MUL[a][b]
            Z[idx] = Z[idx] + s * (X[a] * Y[b])
    return [sp.expand(M) for M in Z]


def qdag(X):
    """Conjugate transpose."""
    return [X[0].T, -X[1].T, -X[2].T, -X[3].T]


def qadd(X, Y):
    return [X[a] + Y[a] for a in range(4)]


def qsub(X, Y):
    return [X[a] - Y[a] for a in range(4)]


def qscalar_times_I(xs, k):
    """The quaternionic matrix q*I_k for q = sum xs[a] e_a."""
    return [xs[a] * sp.eye(k) for a in range(4)]


def qsimp(X):
    return [sp.expand(sp.simplify(M)) for M in X]


def sym_matrix(name, k, symmetric=False):
    """A general real k x k sympy matrix of symbols."""
    if symmetric:
        E = sp.zeros(k, k)
        for i in range(k):
            for j in range(i, k):
                s = sp.Symbol(f"{name}{i}{j}", real=True)
                E[i, j] = s
                E[j, i] = s
        return E
    return sp.Matrix(k, k, lambda i, j: sp.Symbol(f"{name}{i}{j}", real=True))


def qsym_matrix(name, k, symmetric=False):
    """General quaternionic k x k matrix: four real blocks."""
    return [sym_matrix(f"{name}{a}_", k, symmetric) for a in range(4)]


def qsym_row(name, k):
    """General quaternionic 1 x k row."""
    return [sp.Matrix(1, k, lambda i, j: sp.Symbol(f"{name}{a}_{j}", real=True))
            for a in range(4)]


def verify_table():
    """Sanity check the multiplication table against the quaternion relations."""
    def unit(a):
        M = [sp.zeros(1, 1) for _ in range(4)]
        M[a] = sp.eye(1)
        return M
    names = "1ijk"
    out = {}
    for a in range(4):
        for b in range(4):
            P = qmul(unit(a), unit(b))
            nz = [(c, P[c][0, 0]) for c in range(4) if P[c][0, 0] != 0]
            assert len(nz) == 1
            c, v = nz[0]
            out[(names[a], names[b])] = ("" if v == 1 else "-") + names[c]
    return out
