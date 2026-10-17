#!/usr/bin/env python3
"""Labelled numerical checks behind the Claude reply to Codex's response
(papers/brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md).

16 October 2026. Prepared for Edward Baker with LLM assistance. Model:
Claude Fable 5.1 (configured identifier claude-fable-5-1), Claude Cowork,
reasoning effort max. Standard library only; deterministic; prints one JSON
record to stdout. Floats are rounded to 12 significant figures (the
beta-weighted distances to 10) so the record is byte-identical across the
x86-64 and arm64 platforms it was run on.

Everything here is a floating-point diagnostic supporting a remark in the
reply. Nothing is certified and nothing is a theorem about zeta.

Sections
  A. The coefficient-space collision distance of Note 03 Section 9.1,
     repaired as Codex's response asks: nonnegative weights, the primitive
     endpoint normalization sum_n a_n beta_n = 1/2 with
     beta_n = (4 pi n^2 - 1) e^{-pi n^2}, optionally the anchor a_1 = 1,
     in the theta-tail class (a_n = 1 for n > N) and in the zero-tail class
     of the three-square control (a_n = 0 for n > N).  Minimum-norm
     solutions of the constrained linear system; raw and beta-weighted
     distances.
  B. The conditioning constant of Codex's measurement inequality
     ||B delta|| <= C ||M delta|| on the normalized, anchored tangent space,
     for M = recurrence defects and for M = reflection-defect samples, at
     several heights, together with the jet margin |h(t,x)| and the
     resulting admissible measurement error.  This is the scale remark of
     the reply made numerical: the admissible error decays like
     x^A e^{-pi x/8} for every fixed finite measurement design.
  C. Independent replay of the corrected attraction numbers (pair bound
     applied to a count of individual zeros, factor 2).
  D. The shrinking-window energy identity of Codex's Section 1 for the
     double-collision germ, checked against direct quadrature.

Dependency: the term transforms are taken from the earlier Claude script
check_brainstorm_modifications_claude_20261016.py in the same folder (its
composite Simpson rule), with a larger panel count at the greater heights.
"""
import hashlib
import json
import math
import os
import sys

PI = math.pi
HERE = os.path.dirname(os.path.abspath(__file__))
DEP = os.path.join(HERE, "check_brainstorm_modifications_claude_20261016.py")
DEP_SHA256 = "b7249c105ba42bc6e13c9397b837fdf60dab8c130f7c762debbae60683c5cfbc"


def load_dependency():
    data = open(DEP, "rb").read()
    digest = hashlib.sha256(data).hexdigest()
    ns = {"__name__": "dependency"}
    exec(compile(data, DEP, "exec"), ns)
    return ns, digest


DEPNS, DEP_DIGEST = load_dependency()
phi_term = DEPNS["phi_term"]
simpson = DEPNS["simpson"]
U_MAX = DEPNS["U_MAX"]


def panels_for(x):
    """Composite Simpson panels: error ~ (b-a) h^4 x^4 / 180 relative to the
    O(1) integrand near u=0; keep it far below the field at every height used."""
    return 36000 if x <= 50.0 else 180000


def term_transform(n, t, x, deriv=0):
    m = panels_for(x)
    if deriv == 0:
        f = lambda u: math.exp(t * u * u) * phi_term(n, u) * math.cos(x * u)
    else:
        f = lambda u: -u * math.exp(t * u * u) * phi_term(n, u) * math.sin(x * u)
    return simpson(f, 0.0, U_MAX, m)


def beta(n):
    return (4.0 * PI * n * n - 1.0) * math.exp(-PI * n * n)


# ---------------------------------------------------------------------------
# small dense linear algebra (standard library)
# ---------------------------------------------------------------------------

def solve(A, b):
    """Gaussian elimination with partial pivoting for a square system."""
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        if abs(M[p][c]) == 0.0:
            raise ZeroDivisionError("singular")
        M[c], M[p] = M[p], M[c]
        for r in range(n):
            if r != c:
                f = M[r][c] / M[c][c]
                if f != 0.0:
                    for k in range(c, n + 1):
                        M[r][k] -= f * M[c][k]
    return [M[i][n] / M[i][i] for i in range(n)]


def min_norm(rows, rhs):
    """Minimum Euclidean-norm solution of rows . d = rhs (rows: list of m
    vectors of length k, m <= k, independent).  Rows are scaled to unit norm,
    orthonormalized by modified Gram-Schmidt with one reorthogonalization
    pass, and the right-hand side is carried along (forward substitution)."""
    m, k = len(rows), len(rows[0])
    R = []
    c = []
    for r, b in zip(rows, rhs):
        nr = math.sqrt(sum(v * v for v in r))
        if nr == 0.0:
            raise ZeroDivisionError("zero row")
        R.append([v / nr for v in r])
        c.append(b / nr)
    Q, T = [], []          # orthonormal rows and the triangular coefficients
    for i in range(m):
        v = R[i][:]
        coeffs = [0.0] * i
        for _ in range(2):
            for j in range(i):
                dot = sum(a * b for a, b in zip(v, Q[j]))
                coeffs[j] += dot
                v = [a - dot * b for a, b in zip(v, Q[j])]
        nv = math.sqrt(sum(a * a for a in v))
        if nv < 1e-13:
            raise ZeroDivisionError("dependent rows")
        Q.append([a / nv for a in v])
        T.append(coeffs + [nv])
    z = []
    for i in range(m):
        s = c[i] - sum(T[i][j] * z[j] for j in range(i))
        z.append(s / T[i][i])
    return [sum(z[j] * Q[j][i] for j in range(m)) for i in range(k)]


def sym2_eigs(a, b, c):
    """Eigenvalues of [[a,b],[b,c]]."""
    tr, det = a + c, a * c - b * b
    disc = max(tr * tr / 4.0 - det, 0.0)
    return tr / 2.0 + math.sqrt(disc), tr / 2.0 - math.sqrt(disc)


def two_row_norm(R):
    """Largest singular value of a 2 x k matrix R (list of two rows)."""
    a = sum(v * v for v in R[0])
    b = sum(v * w for v, w in zip(R[0], R[1]))
    c = sum(w * w for w in R[1])
    return math.sqrt(sym2_eigs(a, b, c)[0])


def tangent_basis(N, anchored):
    """Orthonormal basis of the normalized tangent space of finite-support
    perturbations: delta_n = 0 for n > N, sum_n beta_n delta_n = 0, and
    delta_1 = 0 when anchored.  Built from the exact kernel vectors
    v_n = e_n - (beta_n/beta_p) e_p (p = 2 if anchored, else p = 1), then
    orthonormalized by modified Gram-Schmidt with reorthogonalization."""
    p = 2 if anchored else 1
    vecs = []
    for n in range(p + 1, N + 1):
        v = [0.0] * N
        v[n - 1] = 1.0
        v[p - 1] = -beta(n) / beta(p)
        vecs.append(v)
    basis = []
    for v in vecs:
        w = v[:]
        for _ in range(2):
            for q in basis:
                dot = sum(a * b for a, b in zip(w, q))
                w = [a - dot * b for a, b in zip(w, q)]
        nw = math.sqrt(sum(a * a for a in w))
        basis.append([a / nw for a in w])
    return basis


# ---------------------------------------------------------------------------
# A. repaired coefficient-space collision distance
# ---------------------------------------------------------------------------

def columns(t, x, N):
    B = [[term_transform(n, t, x, 0) for n in range(1, N + 1)],
         [term_transform(n, t, x, 1) for n in range(1, N + 1)]]
    return B


def section_a():
    out = {"definitions": {
        "beta_n": "(4 pi n^2 - 1) e^{-pi n^2}; sum_{n>=1} beta_n = 1/2 is the theta identity theta'(1) = -theta(1)/4",
        "class": "a_n >= 0, sum_n a_n beta_n = 1/2, a_n fixed for n > N (theta tail: 1; zero tail: 0), optionally a_1 = 1",
        "problem": "minimum Euclidean norm of delta = a - a_theta with H_a(t,x) = d_x H_a(t,x) = 0 and the normalization; a linear system with 3 (or 4) rows in N unknowns",
        "jet_truncation": "theta jet and tail computed from the first 6 square terms; terms beyond n=6 are below 1e-48 on the half-line",
    }, "beta": {str(n): beta(n) for n in range(1, 7)},
        "sum_beta_1_to_6": sum(beta(n) for n in range(1, 7)), "points": []}
    for (t, x) in ((0.25, 44.1303), (0.0, 60.0)):
        B6 = columns(t, x, 6)
        h = [sum(B6[0]), sum(B6[1])]
        entry = {"t": t, "x": x, "theta_jet_h": h, "columns": B6, "solves": []}
        for tail in ("theta", "zero"):
            for anchor in (False, True):
                for N in (2, 3, 4, 6):
                    # unknowns delta_1..delta_N; tail fixed
                    tailB = [sum(B6[j][n - 1] for n in range(N + 1, 7)) if tail == "theta" else 0.0 for j in (0, 1)]
                    tailbeta = sum(beta(n) for n in range(N + 1, 7)) if tail == "theta" else 0.0
                    # rows: jet rows, normalization row, (anchor row)
                    rows = [B6[0][:N], B6[1][:N], [beta(n) for n in range(1, N + 1)]]
                    # H_a = sum_{n<=N} (1+delta_n) b_n + tail = 0  =>  sum delta_n b_n = -(sum_{n<=N} b_n + tail)
                    rhs = [-(sum(B6[0][:N]) + tailB[0]), -(sum(B6[1][:N]) + tailB[1]),
                           0.5 - (sum(beta(n) for n in range(1, N + 1)) + tailbeta)]
                    if anchor:
                        rows.append([1.0] + [0.0] * (N - 1))
                        rhs.append(0.0)
                    if len(rows) > N:
                        entry["solves"].append({"tail": tail, "anchor_a1": anchor, "N": N,
                                                "result": "overdetermined (more constraints than weights); no exact solution in general"})
                        continue
                    try:
                        d = min_norm(rows, rhs)
                    except ZeroDivisionError:
                        entry["solves"].append({"tail": tail, "anchor_a1": anchor, "N": N, "result": "singular"})
                        continue
                    a = [1.0 + v for v in d]
                    resid = [sum(r[j] * d[j] for j in range(N)) - rr for r, rr in zip(rows, rhs)]
                    # the residuals are rounding noise (1e-21 on the jet rows, 1e-16 on the
                    # normalization) and differ between platforms; record only the bound
                    entry["solves"].append({
                        "tail": tail, "anchor_a1": anchor, "N": N,
                        "weights_a": a,
                        "raw_l2_distance": math.sqrt(sum(v * v for v in d)),
                        "beta_weighted_distance": float("%.9e" % sum(beta(n) * abs(d[n - 1]) for n in range(1, N + 1))),
                        "all_weights_nonnegative": all(v >= 0.0 for v in a),
                        "max_abs_constraint_residual_below_1e-14": max(abs(v) for v in resid) < 1e-14,
                    })
        out["points"].append(entry)
    # the strictly anchored class at the first point: two free directions
    # v_3 = e_3 - (beta_3/beta_2) e_2 and v_4 = e_4 - (beta_4/beta_2) e_2
    for p in out["points"]:
        t, x = p["t"], p["x"]
        B6 = p["columns"]
        h = p["theta_jet_h"]
        v3 = [B6[j][2] - (beta(3) / beta(2)) * B6[j][1] for j in (0, 1)]
        v4 = [B6[j][3] - (beta(4) / beta(2)) * B6[j][1] for j in (0, 1)]
        det = v3[0] * v4[1] - v3[1] * v4[0]
        c3 = (-h[0] * v4[1] + h[1] * v4[0]) / det
        c4 = (-v3[0] * h[1] + v3[1] * h[0]) / det
        p["strictly_anchored_two_direction_solve"] = {
            "directions": "v_3 = e_3 - (beta_3/beta_2) e_2, v_4 = e_4 - (beta_4/beta_2) e_2 (delta_1 = 0 exactly, normalization exact)",
            "jets": {"B v_3": v3, "B v_4": v4},
            "coefficients": {"c_3": c3, "c_4": c4},
            "weights": {"a_2": 1.0 - (beta(3) / beta(2)) * c3 - (beta(4) / beta(2)) * c4, "a_3": 1.0 + c3, "a_4": 1.0 + c4},
            "comment": "with the first weight pinned exactly, the second is pinned by the normalization and the collision must be carried by the third and fourth nodes; the fourth needs a weight far beyond any positive control, which is why the general solver reports the anchored systems as numerically singular",
        }
    # sensitivity of the three-weight solution to the collision abscissa inside the control's bracket
    sens = []
    for x in (44.1303, 44.13035, 44.1304):
        B6 = columns(0.25, x, 6)
        N = 3
        rows = [B6[0][:N], B6[1][:N], [beta(n) for n in range(1, N + 1)]]
        tailB = [sum(B6[j][n - 1] for n in range(N + 1, 7)) for j in (0, 1)]
        tailbeta = sum(beta(n) for n in range(N + 1, 7))
        rhs = [-(sum(B6[0][:N]) + tailB[0]), -(sum(B6[1][:N]) + tailB[1]),
               0.5 - (sum(beta(n) for n in range(1, N + 1)) + tailbeta)]
        d = min_norm(rows, rhs)
        sens.append({"x": x, "weights_a": [1.0 + v for v in d]})
    out["three_weight_solution_across_the_control_bracket"] = sens
    raw = (1.0, 0.879175, 57742.5)
    scale = 0.5 / sum(w * beta(n) for w, n in zip(raw, (1, 2, 3)))
    out["three_square_control_reference"] = {
        "normalized_control_weights_from_table_midpoints": [w * scale for w in raw],
        "rescaling_factor": scale,
        "source": "22 Note 05/01 Section 4 table: raw a_1=1, a_2 in (0.87916,0.87919), a_3 in (57740,57745), zero tail, collision at T=1/4, x in (44.1303,44.1304)",
        "comment": "the normalized three-weight solution at (1/4,44.1303) must reproduce these weights up to the positive rescaling that imposes the primitive endpoint, since three weights with two jet conditions and one normalization have a unique solution",
    }
    out["comment"] = ("With the normalization imposed, the trivial near-zero source found by the "
                      "unnormalized solve disappears; the collision is carried by the third node "
                      "at the scale e^{9 pi} beta_3^{-1}-type suppression, as Note 03 Section 1.2 predicted, "
                      "and the solution is the existing control, not new structure.")
    return out


# ---------------------------------------------------------------------------
# B. conditioning of the measurement inequality on the normalized tangent space
# ---------------------------------------------------------------------------

def reflection_defect_rows(N, samples):
    """Rows r_j(n) = phi_n(u_j) - phi_n(-u_j) for the finite-support directions
    e_1..e_N: the defect of the full-line source reflection at sample points.
    phi_n(-u) is the n-th term continued to negative u (no cutoff there)."""
    def phi_full(n, u):
        q = PI * n * n * math.exp(4.0 * u)
        if q > 700.0:
            return 0.0
        return (2.0 * q * q - 3.0 * q) * math.exp(u - q)
    return [[phi_full(n, u) - phi_full(n, -u) for n in range(1, N + 1)] for u in samples]


def recurrence_rows(N):
    """Rows d_k = delta_{k-1} - 2 delta_k + delta_{k+1}, k = 1..N+1, with
    delta_0 = 0 (no zero mode in the physical source) and delta_{N+1} = 0
    (tail fixed): N+1 rows on N unknowns, rank N."""
    rows = []
    for k in range(1, N + 2):
        row = [0.0] * N
        for idx, coeff in ((k - 1, 1.0), (k, -2.0), (k + 1, 1.0)):
            if 1 <= idx <= N:
                row[idx - 1] += coeff
        rows.append(row)
    return rows


def restricted_norm_ratio(Brows, Mrows, basis):
    """sup over the tangent space (orthonormal basis columns) of
    ||B delta|| / ||M delta||: compute B Q and M Q, then the largest
    generalized singular value via the 2x2 reduction
    C = ||B Q (M Q)^+||.  M Q has full column rank here (checked)."""
    k = len(basis)
    BQ = [[sum(Brow[i] * q[i] for i in range(len(q))) for q in basis] for Brow in Brows]
    MQ = [[sum(Mrow[i] * q[i] for i in range(len(q))) for q in basis] for Mrow in Mrows]
    # Gram of M Q (k x k) and its Cholesky-free inverse via solve on each B row
    G = [[sum(MQ[r][i] * MQ[r][j] for r in range(len(MQ))) for j in range(k)] for i in range(k)]
    # whitening: C^2 = largest eigenvalue of (BQ) G^{-1} (BQ)^T  (2x2)
    Ginv_BQt = [solve(G, [BQ[j][i] for i in range(k)]) for j in (0, 1)]
    S = [[sum(BQ[a][i] * Ginv_BQt[b][i] for i in range(k)) for b in (0, 1)] for a in (0, 1)]
    lam = sym2_eigs(S[0][0], 0.5 * (S[0][1] + S[1][0]), S[1][1])[0]
    return math.sqrt(max(lam, 0.0)), G


def carrier_abs(t, x):
    """|M_t((1+ix)/2)| in Polymath's normalization, from the Stirling form of
    (1/8) s(s-1) pi^{-s/2} Gamma(s/2) times exp((t/4) Re alpha(s)^2)."""
    s = complex(0.5, x / 2.0)
    alpha = 1.0 / (2.0 * s) + 1.0 / (s - 1.0) + 0.5 * cmath_log(s / (2.0 * PI))
    # log|Gamma(s/2)| via Stirling with two correction terms
    z = s / 2.0
    lg = (z - 0.5) * cmath_log(z) - z + 0.5 * math.log(2.0 * PI) + 1.0 / (12.0 * z) - 1.0 / (360.0 * z ** 3)
    # pi^{-s/2}: |pi^{-s/2}| = pi^{-1/4}
    log_abs = math.log(abs(s * (s - 1.0)) / 16.0) - 0.25 * math.log(PI) + lg.real + (t / 4.0) * (alpha * alpha).real
    return math.exp(log_abs)


def cmath_log(z):
    return complex(math.log(abs(z)), math.atan2(z.imag, z.real))


def section_b():
    N = 6
    samples = [0.05 * k for k in range(1, 13)]  # u in (0, 0.6]
    out = {"tangent_spaces": {
               "anchored": "finite support n <= 6, delta_1 = 0, sum beta_n delta_n = 0 (dimension 4; first free node n = 3)",
               "unanchored": "finite support n <= 6, sum beta_n delta_n = 0 (dimension 5; first free node n = 2)"},
           "measurements": {
               "recurrence": "d_k = delta_{k-1} - 2 delta_k + delta_{k+1}, k = 1..7, delta_0 = delta_7 = 0",
               "reflection": "phi_delta(u_j) - phi_delta(-u_j) at u_j = 0.05 j, j = 1..12 (defect of the full-line source reflection)",
           },
           "constant": "C(t,x) = sup_{delta in V} ||B delta|| / ||M delta||, B the jet map delta -> (H_delta, d_x H_delta)(t,x)",
           "admissible_error": "eta(t,x) = |h(t,x)| / C(t,x): the measurement defect below which the physical jet at (t,x) cannot be driven to zero inside V",
           "rows": []}
    Mrec = recurrence_rows(N)
    Mref = reflection_defect_rows(N, samples)
    bases = {"anchored": tangent_basis(N, True), "unanchored": tangent_basis(N, False)}
    out["tangent_dimensions"] = {k: len(v) for k, v in bases.items()}
    for (t, x) in ((0.0, 30.0), (0.0, 44.1303), (0.25, 44.1303), (0.0, 60.0), (0.0, 70.0), (0.0, 85.0)):
        B = columns(t, x, N)
        h = [sum(B[0]), sum(B[1])]
        habs = math.hypot(h[0], h[1])
        row = {"t": t, "x": x, "jet_h": h, "|h|": habs,
               "carrier_|M_t|": carrier_abs(t, x),
               "x^{7/4} e^{-pi x/8}": x ** 1.75 * math.exp(-PI * x / 8.0),
               "x^2 |h|": x * x * habs,
               "|phi_2'(0)|/x^2": 0.039499 / (x * x)}
        for name, basis in bases.items():
            BQ = [[sum(Brow[i] * q[i] for i in range(N)) for q in basis] for Brow in B]
            Crec, _ = restricted_norm_ratio(B, Mrec, basis)
            Cref, _ = restricted_norm_ratio(B, Mref, basis)
            row[name] = {"||B|_V||": two_row_norm(BQ),
                         "C_recurrence": Crec, "eta_recurrence": habs / Crec if Crec else None,
                         "C_reflection": Cref, "eta_reflection": habs / Cref if Cref else None}
        out["rows"].append(row)
    out["comment"] = ("The constants C are nearly height-independent (algebraic in 1/x), because B is "
                      "algebraic on every finite-support direction and M is fixed; the admissible error eta "
                      "therefore decays with |h|, like x^A e^{-pi x/8}.  eta is a guarantee (no collision in V "
                      "below that defect), saturated in direction only: the worst direction is the lowest free "
                      "node, whose jet is algebraic in 1/x.  The prefactor depends on the class.  The unanchored "
                      "row is the realistic one: the recurrence rows see delta_1 through d_1 = -2 delta_1 + "
                      "delta_2 (a_0 = 1 fixed), and a change of 3e-5 in a_1 buys, under the normalization, the "
                      "change of -0.12 in a_2 that the three-square control uses (its own recurrence defect, "
                      "dominated by the third node, is about 1.4e5).  The strictly anchored class (delta_1 = 0 "
                      "exactly) is an idealization in which the first free node is n = 3; even there eta crosses "
                      "one near x = 82.  Measured relative to the carrier (divide B by |M_t|), the same numbers "
                      "read as a conditioning constant growing like x^{-A} e^{pi x/8}.")
    return out


# ---------------------------------------------------------------------------
# C. corrected attraction numbers
# ---------------------------------------------------------------------------

def section_c():
    trud = DEPNS["trudgian_S_bound"]
    T = 3.0e12
    L = math.log(2.0 * T / (4.0 * PI))
    S = trud(T)

    def pull(b, D, per_zero_factor):
        count = (D / (2.0 * PI)) * L - 2.0 * S - 2.0
        return 0.0 if count <= 0 else count * per_zero_factor * b / (D * D + 4.0 * b * b)

    def best(b, f):
        bestp, bestD, D = 0.0, None, 0.5
        while D <= 60.0:
            p = pull(b, D, f)
            if p > bestp:
                bestp, bestD = p, D
            D += 0.05
        return bestp, bestD

    def time(f, steps=1000):
        tot, hstep = 0.0, 1.0 / steps
        for k in range(steps):
            b = (k + 0.5) * hstep
            tot += hstep / (1.0 / b + best(b, f)[0])
        return tot
    out = {"T": T, "L": L, "S_bound": S,
           "pair_inequality": "g(b-c)+g(b+c) >= 4b/(d^2+4b^2), g(y)=2y/(d^2+y^2), 0<=c<=b; a conjugate pair is two counted zeros and a real zero is half a c=0 pair, so N individual zeros give at least 2bN/(d^2+4b^2)",
           "note03_as_written_factor4": {"pull_b1": best(1.0, 4.0), "time_from_b0_1": time(4.0)},
           "corrected_factor2": {"pull_b1": best(1.0, 2.0), "time_from_b0_1": time(2.0)},
           "de_Bruijn": 0.5, "published": 0.2,
           "comment": "replays Codex's audit values 0.5636 and 0.3945 independently of its script; the conclusion of Note 03 Section 5 (the law loses to first-term dominance at every height) is unchanged and slightly strengthened"}
    # algebraic identity check at random rational-looking points
    worst = 0.0
    for d in (0.0, 0.3, 1.0, 2.5):
        for b in (0.2, 1.0, 1.7):
            for c in (0.0, 0.5 * b, b):
                u, Bq, Cq = d * d, b * b, c * c
                lhs = (2 * (b - c) / (u + (b - c) ** 2) if (u + (b - c) ** 2) > 0 else 0.0) + 2 * (b + c) / (u + (b + c) ** 2)
                rhs = 4 * b / (u + 4 * Bq)
                formula = 4 * b * (Bq - Cq) * (3 * u + 3 * Bq + Cq) / (((u + Bq + Cq) ** 2 - 4 * Bq * Cq) * (u + 4 * Bq)) if ((u + Bq + Cq) ** 2 - 4 * Bq * Cq) > 0 else None
                if formula is not None:
                    worst = max(worst, abs((lhs - rhs) - formula))
    out["codex_difference_formula_max_abs_error"] = worst
    return out


# ---------------------------------------------------------------------------
# D. shrinking-window energy for the double-collision germ
# ---------------------------------------------------------------------------

def section_d():
    out = {"germ": "H = y^2 + 2s, E = H^2 + H_y^2, L_0 = 2y^2 - 4s",
           "negative_mass_of_L_0": "(16 sqrt2 / 3) s^{3/2} on |y| < sqrt(2s)",
           "window": "chi_s(y) = w(y/sqrt s), w(v) = e^{-v^2}",
           "claimed": "int chi_s E = 4 s^{3/2} int w v^2 + s^{5/2} int w (v^2+2)^2", "rows": []}
    w = lambda v: math.exp(-v * v)
    I2 = simpson(lambda v: w(v) * v * v, -12.0, 12.0, 24000)
    I4 = simpson(lambda v: w(v) * (v * v + 2.0) ** 2, -12.0, 12.0, 24000)
    for s in (1.0, 0.1, 0.01, 0.001):
        direct = simpson(lambda y: w(y / math.sqrt(s)) * ((y * y + 2 * s) ** 2 + 4 * y * y), -12.0 * math.sqrt(s), 12.0 * math.sqrt(s), 24000)
        formula = 4.0 * s ** 1.5 * I2 + s ** 2.5 * I4
        neg = simpson(lambda y: max(0.0, 4 * s - 2 * y * y), -math.sqrt(2 * s), math.sqrt(2 * s), 20000)
        out["rows"].append({"s": s, "direct_window_energy": direct, "formula": formula,
                            "negative_mass_L0": neg, "closed_form_negative_mass": 16.0 * math.sqrt(2.0) / 3.0 * s ** 1.5,
                            "ratio_negative_mass_to_window_energy": neg / direct})
    out["fixed_window_comparison"] = {
        "comment": "for a window of fixed width 1 (w(y) = e^{-y^2}, not rescaled) the energy tends to int w (y^4+4y^2) dy = O(1) as s -> 0 while the negative mass is O(s^{3/2})",
        "fixed_window_energy_s_to_0": simpson(lambda y: w(y) * (y ** 4 + 4 * y * y), -12.0, 12.0, 24000)}
    out["comment"] = ("Codex's identity holds; a window scaled with sqrt(s), the imaginary part of the "
                      "approaching pair, keeps the collision at relative order one, a fixed window dilutes "
                      "it by s^{3/2}; Note 03 Section 8 is correct for fixed windows and overstated as "
                      "written for every window, which is what the reply records.")
    return out


def rounded(obj, digits=12):
    if isinstance(obj, float):
        if obj == 0.0 or math.isnan(obj) or math.isinf(obj):
            return obj
        return float("%.*e" % (digits - 1, obj))
    if isinstance(obj, dict):
        return {k: rounded(v, digits) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [rounded(v, digits) for v in obj]
    return obj


def main():
    record = {
        "reply": "03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md",
        "model": "Claude Fable 5.1 (claude-fable-5-1), Claude Cowork, reasoning effort max",
        "date": "2026-10-16",
        "status": "floating-point diagnostics; not certified; floats rounded to 12 significant figures",
        "dependency": {"file": os.path.basename(DEP), "sha256": DEP_DIGEST,
                       "expected_sha256": DEP_SHA256, "matches": DEP_DIGEST == DEP_SHA256},
        "quadrature": "dependency composite Simpson on [0,1.8]; 36000 panels for x <= 50, 180000 panels above",
        "A_repaired_coefficient_distance": section_a(),
        "B_measurement_conditioning": section_b(),
        "C_corrected_attraction": section_c(),
        "D_shrinking_window": section_d(),
    }
    print(json.dumps(rounded(record), indent=1, sort_keys=False))


if __name__ == "__main__":
    main()
