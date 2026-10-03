# Spatial prime reduction and a precise scalar-tail obstruction

3 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); serving variant and configured reasoning effort are not exposed and are not inferred. These are analytic derivations with an internal same-model check, not specialist refereeing. No larger-window numerical sweep was run.

A spatial reduction retains the prime shifts and all mixed blocks, and gives an effective finite-dimensional sufficient test at every fixed length. It does **not**, by itself, improve the all-window cost. The obstruction can be stated more sharply than the previous amplitude estimate: removing any finite-dimensional head, including all three source moments, leaves the full arithmetic operator norm unchanged. The centered prime discrepancy has the same essential spectral top. A separate scalar bound for archimedean energy and arithmetic norm therefore forces doubly exponential rank, even if the finite head is optimally chosen.

This is a limitation of that class of estimates. It is not a negative source for the Weil form, a complexity lower bound for every algorithm, or a proof that a signed energy-relative Schur estimate cannot succeed.

## 1. Relation to the existing spatial certificate

The [Weil-depth manuscript](../../../shifted-zeta/weil-depth/manuscript/finite_horizon_weil.tex), especially its compressed-shift lemma, fractional-integral tail lemma, and discussion of the scalar tail floor, already implements a spatial head/tail reduction through total length log 7. It certifies the full Weil form, including the pole term, with no vanishing conditions. Restricting that result to E_L removes the pole term and gives the arithmetic Q used here; the three fixed source conditions only restrict the earlier class. The [continuation note](../../../shifted-zeta/weil-depth/CONTINUATION.md) and [review of v0.3](../../../shifted-zeta/weil-depth/archive/reviews/2026-09-09_review-of-v0.3_chatgpt/FINITE_HORIZON_WEIL_V03_REVIEW_20260909.md) distinguish a cost barrier from failure of positivity.

The new material here is the finite-codimension invariance argument, its application to continuous-prime centering, an explicit lower bound on the rank required by **any separated scalar tail estimate**, and an exact formula for the null Fourier multiplier. The finite reduction below records the mixed term rather than suggesting that changing to source coordinates automatically solves the all-window problem.

## 2. Arithmetic shifts and their geometry

Write H_L=L2((-L/2,L/2)) and extend functions by zero. For a>0 define

    (S_a f)(x)=f(x-a), whenever x and x-a lie in I_L,

and zero otherwise. Put

    b_n=Lambda(n)/sqrt(n),
    W_L=sum_{log n<L} b_n (S_log n+S_log n*).

Only prime powers have nonzero b_n. The arithmetic form is

    Q_L[F]=Gamma_L[F]-<F,W_L F>,
    Gamma_L[F]=integral gamma(t)|Fhat(t)|² dt/(2pi),
    gamma(t)=Re psi(1/4+it/2)-log pi.

The three-moment space E_L is the orthogonal complement of 1,e^(x/2),e^(-x/2). Complex sources are allowed. All operators below are understood on E_L after compression when necessary.

Each S_a is nilpotent. Decomposing I_L into finite chains modulo a gives the exact symmetric-shift norm

    ||S_a+S_a*|| = 2 cos(pi/(ceil(L/a)+1)),       0<a<L.       (1)

The endpoint a=L gives zero. For example, a in [L/2,L) gives norm one. Consequently

    omega_L := ||W_L||
       <= Sigma_L := sum_{log n<L} b_n ||S_log n+S_log n*||
       <= C_L := 2 sum_{log n<L} b_n.                       (2)

The forward sum T_L=sum b_n S_log n is itself nilpotent: T_L^m=0 for m log 2>=L. Nilpotence concerns the forward operator, while Q contains T_L+T_L*. It does not make that selfadjoint sum small.

By the unconditional prime number theorem and partial summation,

    sum_{log n<L} b_n ~ 2 e^(L/2),
    C_L ~ 4 e^(L/2),
    Sigma_L ~ 2 e^(L/2).                                  (3)

For the last relation, all delays in [L/2,L) have the exact norm one, while the total weight below L/2 is only O(e^(L/4)). Thus individual shift geometry improves the leading amplitude constant but retains its exponential dependence on L. The prime number theorem is used here only for asymptotic size, not for positivity.

## 3. Removing a finite head cannot reduce the arithmetic norm

**Proposition.** Let M be any finite-dimensional subspace of H_L and H=M-perp. Then

    sup_{f in H, ||f||=1} <f,W_L f> = omega_L,
    ||P_H W_L P_H|| = omega_L.                            (4)

In particular, (4) holds after removing the three analytic moment functions and any additional finite numerical head. The essential spectral top of W_L equals omega_L.

**Proof.** The kernel of W_L is a positive measure, so

    |<f,W_L f>| <= <|f|,W_L |f|>.

Therefore its spectral top equals its operator norm. Choose a unit f with Rayleigh quotient arbitrarily close to omega_L.

Let U_t f(x)=e^(itx)f(x). There is a sequence t_j going to infinity for which

    exp(it_j log p) -> 1

for every active prime p. This elementary simultaneous recurrence follows from pigeonholing the orbit in a finite torus; no Diophantine rate or rational-independence claim is needed. Prime-power phases then converge to one as well. Since the shift sum is finite,

    ||U_tj* W_L U_tj-W_L|| -> 0.                          (5)

For every fixed f, U_tj f converges weakly to zero: its pairing with any L2 function is the Fourier transform of an L1 product. Thus ||P_M U_tj f|| tends to zero. The normalized projections of U_tj f onto H have Rayleigh quotient tending to <f,W_L f>. This proves the lower bound in (4); the upper bound is immediate. The same weakly null sequence gives the assertion about the essential spectral top.

For the original compactly smooth source class, one can first take f compactly smooth and correct the finitely many small moments with fixed compactly smooth dual functions. Existence of such dual functions follows from the independence of the corresponding bounded functionals on the dense smooth subspace. Their correction coefficients tend to zero. Therefore the arithmetic lower-bound sequences need not rely on nonsmooth moment projections. End of proof.

This result does not combine the largest arithmetic value and the smallest archimedean energy on one source. In fact, Gamma[U_tj f] grows with log t_j for a fixed smooth f. That distinction is precisely why (4) is an obstruction to **separate scalar estimates**, not to Q itself.

## 4. The unchanged norm is exponentially large

Fix d>0, epsilon>0 and a nonnegative real g in Cc-infinity((-d/2,d/2)) with ||g||=1. For L sufficiently large set

    R=L-d-epsilon,
    f_L=(g(x-R/2)+g(x+R/2))/sqrt(2).

The two packets are disjoint and compactly supported inside I_L. Write kappa_g(u)=integral conjugate(g(x))g(x+u)dx; it is nonnegative. The cross-packet part of the arithmetic form gives the exact inequality

    omega_L >= <f_L,W_L f_L>
            >= sum_n Lambda(n)n^(-1/2) kappa_g(log n-R).    (6)

Every delay in this sum is active because R+d=L-epsilon. The prime number theorem, tested against the fixed smooth function kappa_g, gives

    e^(-R/2) sum_n Lambda(n)n^(-1/2)kappa_g(log n-R)
       -> c_g := integral e^(u/2) kappa_g(u)du
        = (integral e^(x/2)g(x)dx)(integral e^(-x/2)g(x)dx)>0.

Hence

    omega_L >= (c_g e^(-(d+epsilon)/2)+o(1))e^(L/2).        (7)

Together with (2), this proves omega_L is of order e^(L/2), up to positive constant bounds. Proposition (4) transfers this lower bound to E_L and to every finite-codimension tail in E_L. The unmodulated packet f_L in (6) need not be prepared; the recurrence-and-correction argument is the step which supplies prepared sources.

Both parity sectors retain an exponential lower bound: choose g even, use the even packet pair above, and replace its modulations by normalized cosine and sine modulations. The rapidly oscillating cross terms vanish, while the recurrent shift phases tend to one. Correct the finitely many constraints within the corresponding parity sector.

## 5. A quantitative barrier for every separated scalar tail estimate

The digamma series used in the local certificate is

    gamma(t)=gamma(0)+sum_{n>=0} 2t²/[ell_n(ell_n²+t²)],
    ell_n=2n+1/2.

Its summand decreases with n. Comparing the sum with its integral, and bounding the first term by four, gives globally

    gamma(0)+(1/2)log(1+4t²)
       <= gamma(t)
       <= gamma(0)+4+(1/2)log(1+4t²).                     (8)

Let H be a codimension-N subspace of E_L and suppose a proof estimates its tail using only

    Gamma[F] >= mu_H ||F||²,
    <F,W_L F> <= omega_H ||F||².

By (4), the smallest valid omega_H is omega_L. Moreover, mu_H cannot exceed the (N+1)-st eigenvalue of the compressed Gamma operator.

To bound that eigenvalue from above, take the first m=N+4 Dirichlet sine modes on I_L. Their intersection with the three-moment space has dimension at least N+1. On that intersection, Parseval and the Dirichlet energy bound give

    integral t²|Fhat(t)|² dt/(2pi) <= (pi m/L)² ||F||².

Jensen's inequality for the concave function log, followed by (8), therefore yields

    mu_H <= gamma(0)+4+(1/2)log(1+4pi²(N+4)²/L²).          (9)

Thus a positive separated scalar conclusion mu_H-omega_H>0 is possible only if

    N+4 > (L/(2pi)) sqrt(exp(2[omega_L-gamma(0)-4])-1),      (10)

when the radicand is positive. In view of (7), the required rank is doubly exponential in L for large L.

This statement allows **any** choice of the finite head, not just Legendre polynomials. It does not assume the most negative gamma direction is also the most positive arithmetic direction. Rather, it proves that discarding their correlation and replacing both by independent scalar extrema cannot avoid the cost. A method retaining their signed correlation, a non-scalar complementary block, or source-dependent energy estimates is outside the scope of (10).

## 6. A full finite reduction retaining the mixed block

There is nevertheless a rigorous finite reduction for each L, without assuming Q>=0. Set

    kappa=1-gamma(0),
    A=Gamma|E_L+kappa I >= I,
    V=P_E W_L P_E+kappa I,
    H=A^(-1/2) V A^(-1/2).

Gamma is the closed Fourier-multiplier form on functions supported in I_L, restricted to E_L. Its lower bounded multiplier tends to infinity, so its form-domain embedding into E_L is compact: bounded form energy uniformly controls the Fourier tail, while each bounded-frequency restriction is a compact integral operator. Therefore A has compact inverse and H is compact selfadjoint. Exactly,

    Q>=0 on E_L  <=>  H<=I.                               (11)

For N>=1, let P project onto the first N eigenvectors of A, let R=I-P, and let a be a lower bound for its (N+1)-st eigenvalue. Define

    K_L=omega_L+kappa,
    d_N=a-K_L.

If d_N>0 then RQR>=d_N R. Since P commutes with A, the entire mixed block of Q is -P W_L R. Consequently the sufficient finite Schur test is

    P Q P - (1/d_N) G_N >= 0,
    G_N=P W_L R W_L P
       =P W_L²P-(P W_L P)².                              (12)

Every W in (12) means its exact E_L compression. G_N contains **all** discarded source modes; it is not a sum over only a retained buffer. Finite sums of clipped translations determine W and W² exactly. In an implementation the eigenbasis and its integrals require outward enclosures, but no arithmetic term or cross term is absent from (12).

An explicit global eigenvalue lower bound is also available without the finite-radius gamma expansion from the earlier spatial implementation. The existing fractional-integral Legendre-tail lemma, with N>=1 and H_N=sum_(k=1)^N 1/k, gives on the complement of degrees below N,

    integral log(|t|/(2pi)) |Fhat(t)|² dt/(2pi)
       >= [H_N-EulerGamma-log(pi L)] ||F||².

Using the lower side of (8), gamma(t)>=gamma(0)+log(2|t|), and min-max therefore gives

    a >= b_N := max(1, H_N-EulerGamma+1+log(4/L)).           (13)

This is valid for every L. It supplies an effective, though expensive, rank bound for (12). Alternatively a direct operator-norm approximation has

    ||H-PHP|| <= K_L [2/sqrt(b_N)+1/b_N].                  (14)

Indeed the mixed block is bounded by K_L/sqrt(b_N), because A>=I, and the complementary block by K_L/b_N. Equations (13)-(14) imply convergence and provide a finite reduction to any chosen absolute accuracy. They do not promise that the resulting finite inequality is true: a genuine negative direction would be retained by sufficiently accurate approximation.

The use of b_N in the scalar complementary floor of (12) is still subject to (10). The useful all-window improvement must replace that scalar arithmetic loss by a bound tied to A on the same source directions. Merely naming the compact Birman-Schwinger operator or rearranging a finite Schur matrix does not do this.

## 7. Continuous-prime centering and the exact null multiplier

Let J_L be the restriction of the convolution kernel e^(-|u|/2), whose Fourier multiplier is

    j(t)=1/(t²+1/4).

Let C_L^cont have kernel e^(|x-y|/2) on I_L. Pole neutrality gives the exact compressed identity

    P_E C_L^cont P_E = -P_E J_L P_E.

Thus the signed centered discrepancy is

    E_L=P_E(W_L-C_L^cont)P_E
       =P_E(W_L+J_L)P_E.                                (15)

J_L is positive, compact, and has norm at most four. Since finite moment compression and J_L are compact perturbations, (4) implies

    sup essential-spectrum(E_L)=omega_L,
    sup spectrum(E_L)>=omega_L.                          (16)

Consequently an absolute estimate E_L[F]<=poly(L)||F||² on the stated source space is false for large L. The proposed centered strategy must retain an archimedean-energy term or another direction-sensitive control. Centering still identifies the correct signed discrepancy and may be useful in such a bound; (16) rules out only its interpretation as a small bare L2 remainder.

There is an exact multiplier expression for the null-form freedom. Set

    r_cont,L(t)=2 integral_0^L e^(u/2)cos(tu)du.

Direct integration gives

    j(t)+r_cont,L(t)
       = e^(L/2)[cos(Lt)+2t sin(Lt)]/(t²+1/4).             (17)

The inverse kernel on |u|<L is e^(-|u|/2)+e^(|u|/2)=2cosh(u/2), whose compression to E_L is zero. Thus any fixed real multiple of (17) can be added to a Fourier multiplier representing Q on E_L. Zero mean similarly permits the null multiplier 2sin(Lt)/t, with its continuous value at zero.

This freedom can change the quality of a pointwise positive-part majorant at a finite window. It cannot change the source operator, the essential arithmetic norm, or (10). For fixed L and a fixed coefficient, (17) decays as O(e^(L/2)/|t|); it does not remove the nondecaying prime phases from a large-frequency absolute-amplitude estimate. No optimization of this freedom has been claimed here.

## 8. Remaining useful theorem

The extension experiment shows that retaining signed frequency contributions can change a failed sufficient test into a successful local one. The spatial analysis now rules out a proposed shortcut: the bad arithmetic norm cannot be removed by more moments, a larger finite head, nilpotence alone, or the compact continuous-prime term.

A sufficient next analytic result would control the **joint** complementary operator, for example

    R_N A^(-1/2) V A^(-1/2) R_N <= theta_L R_N,
    theta_L<1,

with a computable mixed-block enclosure and rank/error bounds better than the independent arithmetic norm in (10). Such an estimate need not make theta_L or the final Q gap uniform in L. It must be proved on an unbounded sequence of windows, or accompanied by a continuation argument whose accepted lengths do not accumulate. The formulas in this note isolate that obligation; they do not establish it.
