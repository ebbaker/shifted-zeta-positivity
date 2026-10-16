"""
The compressed transfer V_{omega,L} by GAUSS-JACOBI quadrature for the exact weight of
the spike, at arbitrary precision.  Unregistered (mpmath).  Successor to
contraction_margin.py, which used the substitution tau = u^{1/omega} and a tanh-sinh rule;
that rule's noise floor (about 6e-12 in lambda_min(D) at 1/h = 16) is above the signal at
omega <= 0.01 and its two smallest-omega rows are superseded by this programme.

THE SINGULARITY IS IN THE WEIGHT.  kG(tau) = (2 pi^om/Gamma(om)) (2 sinh tau)^{om-1} e^{tau/2}
is tau^{om-1} G(tau) with G(tau) = (2 pi^om/Gamma(om)) ((2 sinh tau)/tau)^{om-1} e^{tau/2}
analytic on |tau| < pi, and the two exponential smoothings are
J_c(tau) = int_0^tau e^{c(tau-u)} kG(u) du = tau^om Psi_c(tau) with
Psi_c(tau) = int_0^1 v^{om-1} e^{c tau (1-v)} G(tau v) dv, so the single-atom kernel is

    kappa_om(tau) = tau^{om-1} Gh(tau),   Gh = G - 4 om tau (b Psi_{-b} + a Psi_a),

with Gh analytic on |tau| < pi.  Every integral against tau^{om-1} -- the outer integral over
each atom's whole support and the inner integral of each smoothing -- is then a Gauss-Jacobi
rule for the weight x^{om-1} on [0,1] (Golub-Welsch on the closed-form monic Jacobi
recurrence, alpha = 0, beta = om - 1), which converges geometrically because the integrand is
analytic in a neighbourhood of the interval.  Nothing forms tau by subtraction and nothing
underflows, so the same code runs in double precision (see ../check_contraction_margin.py).

REPORTED.  ||V_N||, lambda_min(D_N) with D_N = I - V_N^T V_N, the ratio lambda_min(D_N)/(2 om)
to m_L^(N) = lambda_min(Q_{0,L}) in the same basis (weil_sine_basis.py of the Wilson-lines
exploratory folder, closed form, no quadrature), the first-order law on e_1, the mass
int_0^L k_om, the nested defect when Nbig > N, and the cumulative Cayley coordinate
Z = (I-V)(I+V)^{-1}, P = (2/om) Re Z with the exact congruence D = (om/2)(I+V*) P (I+V).

Usage:  python3 contraction_margin_gj.py omega L N [nq] [dps] [Nbig]
  e.g.  python3 contraction_margin_gj.py 0.01 log3 24 40 40      (L = log 3 exactly; atoms log n < L)
        python3 contraction_margin_gj.py 0.1  log3 24 40 40 64   (nested defect in 64 modes)
Nothing here is a positivity certificate.
"""
import sys, os, json, time
import mpmath as mp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '../../../wilson-lines/numerics/exploratory'))


def gauss_jacobi_unit(om, n):
    """nodes/weights for int_0^1 x^(om-1) f(x) dx  (total mass 1/om), at the current dps."""
    al, be = mp.mpf(0), om - 1
    T = mp.zeros(n, n)
    for k in range(n):
        d = 2*k + al + be
        T[k, k] = (be*be - al*al)/(d*(d + 2))
        if k >= 1:
            T[k, k-1] = T[k-1, k] = mp.sqrt(4*k*(k + al)*(k + be)*(k + al + be)
                                            / (d*d*(d + 1)*(d - 1)))
    E, EV = mp.eigsy(T)
    mu0 = mp.mpf(2)**om/om
    nodes = [(1 + E[i])/2 for i in range(n)]
    wts = [mu0*EV[0, i]**2*mp.mpf(2)**(-om) for i in range(n)]
    order = sorted(range(n), key=lambda i: nodes[i])
    return [nodes[i] for i in order], [wts[i] for i in order]


def comb_weight(m, om):
    v = mp.mpf(m)**(om - mp.mpf(1)/2)
    q, r = 2, m
    while q*q <= r:
        if r % q == 0:
            v *= 1 - mp.mpf(q)**(-2*om)
            while r % q == 0:
                r //= q
        q += 1
    if r > 1:
        v *= 1 - mp.mpf(r)**(-2*om)
    return v


def kernel_nodes(om, L, nq):
    """(t, weight, Gh(tau)) over every atom's whole support, one Gauss-Jacobi rule each."""
    a, b = mp.mpf(1)/2 - om, mp.mpf(1)/2 + om
    pref = 2*mp.pi**om/mp.gamma(om)
    xv, wv = gauss_jacobi_unit(om, nq)

    def G(tau):
        return pref*(2*mp.sinh(tau)/tau if tau > 0 else mp.mpf(2))**(om - 1)*mp.e**(tau/2)

    def Gh(tau):
        g = G(tau)
        if tau <= 0:
            return g
        s1 = mp.fsum(w*mp.e**(-b*tau*(1 - v))*G(tau*v) for v, w in zip(xv, wv))
        s2 = mp.fsum(w*mp.e**(a*tau*(1 - v))*G(tau*v) for v, w in zip(xv, wv))
        return g - 4*om*tau*(b*s1 + a*s2)

    atoms, n = [], 1
    while mp.log(n) < L:
        atoms.append(n)
        n += 1
    nodes = []
    for m in atoms:
        ln, T = mp.log(m), L - mp.log(m)
        pre = comb_weight(m, om)*T**om
        for xi, wi in zip(xv, wv):
            tau = T*xi
            nodes.append((ln + tau, pre*wi, Gh(tau)))
    return atoms, nodes


def transfer_matrix(L, N, nodes):
    """V_jk = int_0^L k_om(t) S_jk(t) dt, S the closed-form one-sided sine autocorrelation."""
    al = mp.pi/L
    cache = []
    for (t, w, g) in nodes:
        cache.append((t, w*g,
                      [mp.mpf(0)] + [mp.sin(j*al*t) for j in range(1, N + 1)],
                      [mp.mpf(0)] + [mp.cos(j*al*t) for j in range(1, N + 1)]))
    V = mp.zeros(N, N)
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            sg = 1 if (j + k) % 2 == 0 else -1
            acc = []
            for (t, c, sn, cs) in cache:
                if j == k:
                    s = ((L - t)*cs[k] + sn[k]/(k*al))/L
                else:
                    s = ((sg*sn[k] - sn[j])/((j - k)*al) + (sg*sn[k] + sn[j])/((j + k)*al))/L
                acc.append(c*s)
            V[j-1, k-1] = mp.fsum(acc)
    return V


def main():
    om = mp.mpf(sys.argv[1])
    Ls, N = sys.argv[2], int(sys.argv[3])
    nq = int(sys.argv[4]) if len(sys.argv) > 4 else 40
    dps = int(sys.argv[5]) if len(sys.argv) > 5 else 40
    Nbig = int(sys.argv[6]) if len(sys.argv) > 6 else N
    mp.mp.dps = dps
    om = mp.mpf(sys.argv[1])
    L = mp.log(int(Ls[3:])) if Ls.startswith('log') else mp.mpf(Ls)
    t0 = time.time()

    atoms, nodes = kernel_nodes(om, L, nq)
    mass = mp.fsum(w*g for (_, w, g) in nodes)
    Vbig = transfer_matrix(L, Nbig, nodes)
    t_assemble = time.time() - t0
    V = Vbig[0:N, 0:N]
    I = mp.eye(N)
    VtV = V.T*V
    ev = mp.eigsy(VtV, eigvals_only=True)
    lam = min(1 - x for x in ev)

    Z = (I - V)*mp.inverse(I + V)
    P = (Z + Z.T)/om
    lamP = min(mp.eigsy(P, eigvals_only=True))
    R = (I - VtV) - (om/2)*(I + V.T)*P*(I + V)
    congruence = max(abs(R[i, j]) for i in range(N) for j in range(N))

    import weil_sine_basis as wsb
    W = wsb.WeilForm(L, N)
    comb = wsb.prime_comb(L)
    Me, _ = W.matrix(comb, 0)
    Mo, _ = W.matrix(comb, 1)
    mL_e = min(mp.eigsy(Me, eigvals_only=True))
    mL_o = min(mp.eigsy(Mo, eigvals_only=True))
    mL = min(mL_e, mL_o)
    f = mp.zeros(N, 1); f[0] = 1
    Vf = V*f
    first_order = (1 - mp.fsum(Vf[i]**2 for i in range(N)))/(2*om)

    nested = None
    if Nbig > N:
        evn = mp.eigsy((Vbig.T*Vbig)[0:N, 0:N], eigvals_only=True)
        ln_ = min(1 - x for x in evn)
        nested = {"Nbig": Nbig, "lambda_min_nested_D": mp.nstr(ln_, 14),
                  "lambda_min_nested_D_over_2omega": mp.nstr(ln_/(2*om), 14),
                  "ratio_to_mL": mp.nstr(ln_/(2*om)/mL, 12)}

    out = {
        "programme": "contraction_margin_gj.py", "quadrature": "Gauss-Jacobi (weight tau^(omega-1))",
        "omega": mp.nstr(om, 10), "L": Ls, "N": N, "Nbig": Nbig, "nodes_per_atom": nq, "dps": dps,
        "atoms": atoms, "mass_on_0_L": mp.nstr(mass, 20),
        "one_minus_norm_V": mp.nstr(1 - mp.sqrt(max(ev)), 14),
        "lambda_min_D": mp.nstr(lam, 14),
        "lambda_min_D_over_2omega": mp.nstr(lam/(2*om), 14),
        "m_L_even_block_same_basis": mp.nstr(mL_e, 14),
        "m_L_odd_block_same_basis": mp.nstr(mL_o, 14),
        "ratio_lamD_over_2om_to_mL": mp.nstr(lam/(2*om)/mL, 12),
        "first_order_check_e1": {"(1-||Ve1||^2)/(2omega)": mp.nstr(first_order, 14),
                                 "Q[e1]": mp.nstr(Me[0, 0], 14),
                                 "ratio": mp.nstr(first_order/Me[0, 0], 12)},
        "cayley": {"lambda_min_P": mp.nstr(lamP, 14),
                   "ratio_to_mL": mp.nstr(lamP/mL, 12),
                   "P_minus_D_over_2omega_relative": mp.nstr((lamP - lam/(2*om))/mL, 8),
                   "congruence_residual_max": mp.nstr(congruence, 4)},
        "nested_defect": nested,
        "assemble_time_s": round(t_assemble, 1), "total_time_s": round(time.time() - t0, 1),
    }
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
