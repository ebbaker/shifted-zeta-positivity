# Quasi RH prime counting and the complete growing cofactor filter obstruction

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); active reasoning effort is not exposed to this session
and is not inferred. Derivations and separate-agent audits are internal
LLM work, not independent mathematical validation.
Status: conditional analytic deduction and internal review, not independent
mathematical validation. No short-family moment or new zero-free region is
proved.

The first result below closes the untransferred growing-order range in
[Short-family Note 28](../../../short_families/notes/28_GROWING_NORM_COMPENSATED_COFACTOR_BARRIER_20261009.md) under the same quasi-RH source package that [project 17
Note 8](8_RH_STRATEGY_WITH_QUASI_RH_AND_NEXT_ANALYTIC_TARGET_20261010.md) assumes. The second applies the calculation directly to genuine
Möbius column projections at the new row length h=30/41, with the cost of
the compensating coefficients retained. It is a method obstruction only;
the complete actual Möbius response remains free to cancel the selected
filter through all its remaining columns.

## 1. A quantitative input already stated in the assumed source

The inspected primary source is
[the October 5 paper's TeX source, Corollary 1.2, label `cor:primes-ap`](https://raw.githubusercontent.com/openai/math/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex),
inspected on 10 October 2026. It states

\[
 \pi(x;q,a)=\operatorname{Li}(x)/\varphi(q)
                   +O(x^{11/12}\log x)
 \qquad(q\le x,\ (a,q)=1).
\tag{1}
\]

This paper and its consequence remain assumed here. Only the fixed
modulus q=3 is used, so no moving-character budget is imported.
For K=Q(sqrt(-3)), the exact split/inert count is

\[
 \pi_K(x)=2\pi(x;3,1)+\pi(\sqrt x;3,2)+\mathbf1_{x\ge3}.
\tag{2}
\]

Using (1) for the first term and the trivial O(sqrt(x)) bound for the
second yields

\[
 \pi_K(x)=\operatorname{Li}(x)+O(x^{11/12}\log x).
\tag{3}
\]

Removing finitely many excluded prime ideals changes (3) by O(1).
More generally the argument below uses the explicit premise
\(\pi_K(x)=\operatorname{Li}(x)+O_\eta(x^{\theta+\eta})\)
for every eta>0, with one fixed 1/2<theta<1. In this application theta=11/12.

## 2. The uniform pair error after norm compensation

Fix W in C_c^infinity((c,C)), and z=sqrt(CD). For an ideal b with
B_b=Nb<=D^beta, beta<1/2, all supported prime norms in

\[
 Q_b(D)=\sum_{Nq,Nr\le z}W(B_bNqNr/D)
\]

are at least L_b=(c/sqrt(C))D^(1/2)/B_b. Two partial summations give

\[
 Q_b(D)=\frac D{B_b}\int_c^C W(t)
    F_{\log z}(\log(C/t)+\log B_b)\,dt
  +O_{\beta,W,\eta}\left(\frac D{B_b}
                     L_b^{\theta-1}D^\eta\right),
\tag{4}
\]

with the identical complete-cutoff kernel from Note 24,

\[
 F_B(x)=\frac2{2B-x}\log\frac B{B-x}.
\]

Here the prime diagonal is still included. To check uniformity, a single
Stieltjes replacement on the supported fixed-ratio y interval costs
O((D/(B_b x))^theta D^eta). This is at most
O((D/(B_b x))L_b^(theta-1)D^eta). Summing over the remaining prime
norm x pays only its reciprocal sum. For the second replacement use
\(|G_b(x)|\ll D/(B_bx\log D)\) and
\(|G'_b(x)|\ll D/(B_bx^2\log D)\), exactly as in Note 24.
Endpoint contributions at z satisfy the same bound. Logarithms are
absorbed into eta. The sharp upper cutoffs are retained.

Let P have J distinct good prime-ideal factors of norms q_i, with NP<=D^beta,
and assume P is coprime to the fixed exclusion set S.
Multiplying (4) by the actual norm-compensating weight B_b and summing
absolutely over b|P gives error

\[
 E_{\rm PNT}
 \ll D^{(1+\theta)/2+\eta}
       \prod_{i=1}^J(1+q_i^{1-\theta})
 \le 2^J D^{1-(1/2-\beta)(1-\theta)+\eta}.
\tag{5}
\]

Distinct prime ideals in this quadratic field have at most two of any
integer norm; hence the elementary factorial bound from Note 28 gives
J=O_beta(log D/log log D), so 2^J=D^o(1). The removed prime-square
diagonal, with the same norm weights, costs

\[
 E_{\rm diag}\ll\sqrt D\prod_i(1+\sqrt{q_i})
                     \le D^{1/2+\beta/2+o(1)}.
\tag{6}
\]

Both are fixed power savings relative to D for every fixed beta<1/2.
No cancellation among the PNT errors was assumed.

For Note 28's original range beta<1/20, (5), with theta=11/12,
has exponent \(23/24+\beta/12+\eta<77/80+\eta\).
Thus the PNT gain is larger than 3/80 before eta losses. Its continuum
lower bound \(|A_{P,W}(D)|\ge D^{1-o(1)}\), already proved uniformly
for every NP<=D^beta in that note, now dominates both (5) and (6).
Consequently Note 28's actual-response lower bound extends to every
J permitted by NP<=D^beta. Its restriction
J=o(sqrt(log D)/log log D) is no longer needed under (3).
Its original weighted energy remains D^(16/15-o(1)).

## 3. Direct actual-coefficient projections at h=30/41

Here is a formulation that concerns the original response A_u of project
17 Note 8 directly, with nu=1. Set

\[
 h=30/41,\quad V=D^{5/41},\quad
 0<\beta<1/4,\quad NP\le D^\beta.
\]

For M|P let \(\mathcal B^\mu_{u,M}\) be the actual column projection
of A_u onto total ideals bqr where b|M and q,r are two distinct prime
ideals with norms at most z, neither dividing M and outside the fixed exclusion set S. Count q,r unordered.
Their coefficient is exactly mu_K(b), since mu_K(qr)=+1.
No extra factorization or adaptive cutoff is inserted.

On the physical coherent rows

\[
 \mathcal C_P=\{u=v^6:0<Nv\le V,\ (v,P)=1\},
\]

every supported pair prime has norm at least a constant times
D^(1/2-beta). This exceeds NP, since beta<1/4, and exceeds V,
since 1/2-beta>1/4>5/41. Thus the cofactor representation is unique,
all physical character factors equal one, and every mask is retained.

Use the exact coefficients from Note 28,

\[
 a_M=NM\prod_{p\mid P/M}(1-Np),\qquad
 \mathcal L^\mu_{u,P}=\sum_{M\mid P}a_M\mathcal B^\mu_{u,M}.
\]

The elementary divisor identity
\(\sum_{M\mid P:b\mid M}a_M=Nb\)
now gives the exact ordered-pair formula

\[
 \mathcal L^\mu_{u,P}
 =\frac12\sum_{b\mid P}\mu_K(b)Nb
       \sum_{q\ne r,\,Nq,Nr\le z}W(NbNqNr/D)
 \qquad(u\in\mathcal C_P).
\tag{7}
\]

The factor 1/2 distinguishes the actual mu projection from the
transformed-tail projection of Note 24, which had coefficient 2mu_K(b).

Fix a nonzero W of zero integral, and let k_0>=1 be its first nonzero
logarithmic moment, as in Notes 24 and 28. The continuum of twice (7)
is exactly Note 28's growing finite difference. Its proof applies
unchanged to every fixed beta<1/2: it only needs
\(\log NP+\log(C/c)<\vartheta\log z\) for some vartheta<1,
and J/log z -> 0. Both hold here. In particular

\[
 |A_{P,W}(D)|\gg_W
 D\frac{(J+k_0-1)!\prod_i\log q_i}{(\log z)^{J+k_0+1}}
                  =D^{1-o(1)}.
\tag{8}
\]

Equations (5)–(6), for theta=11/12 and beta<1/4, transfer (8)
to (7) for the entire norm-budget range. The worst PNT exponent is
strictly below 47/48 before eta losses. Hence

\[
 |\mathcal L^\mu_{u,P}|\ge D^{1-o(1)}
                      \quad(u\in\mathcal C_P).
\tag{9}
\]

The same uniform coprime lattice count as Note 28, now with X=V,
gives \(\#\mathcal C_P=D^{5/41-o(1)}\); the error is
O(2^J(sqrt(V)+1)), and the Euler product is at least a constant
times 1/log log D. Counting sixth-power images once changes only
a fixed factor. Therefore

\[
 \boxed{\sum_{0<Nu\le D^{30/41}}|\mathcal L^\mu_{u,P}|^2
                   \ge D^{87/41-o(1)}.}
\tag{10}
\]

This lies 16/41 above the proposed raw-moment exponent 71/41.

## 4. Pay the filter coefficients before using the obstruction

The exact cost is

\[
 C_P=\sum_{M\mid P}|a_M|=\prod_i(2q_i-1),\qquad
 NP\le C_P\le2^JNP\le D^{\beta+o(1)}.
\tag{11}
\]

Even the cost-normalized filter obeys

\[
 \boxed{\sum_{0<Nu\le D^{30/41}}
       |\mathcal L^\mu_{u,P}/C_P|^2
             \ge D^{87/41-2\beta-o(1)}.}
\tag{12}
\]

For every fixed beta<8/41 this still exceeds D^(71/41+epsilon)
for sufficiently small fixed epsilon>0. For 8/41<=beta<1/4,
(10) is still proved, but this cost-normalized comparison no longer
gives a strict obstruction. No stronger conclusion is inferred there.

The family of filters here is explicitly prescribed. The conclusion
does not cover arbitrary scale-dependent coefficients, different prime
product shapes, or the original remainder A-L/C_P. In particular,
selected-column positivity never yields a lower bound for the complete
actual moment. The appropriate new arithmetic input still has to couple
the compensating remainder with these coherent responses, keeping the
physical masks and all cross terms. The present quasi-RH input improves
the rigor and range of this diagnostic; it does not provide that coupling.

## 5. Validation and limitations

The proof retains the inherited exact coefficient and continuum identities
and replaces only their PNT-error payment. The exponents, support margins,
and normalization threshold were checked by exact rational arithmetic.
The [replay](../numerics/check_quasi_rh_cofactor_transfer.py) and
[small record](../numerics/QUASI_RH_COFACTOR_TRANSFER_RECORD_20261010.json)
retain 43 exact checks, including distinct prime ideals with equal norms.
No finite numerical experiment is claimed to verify (3), the asymptotic
uniformity, or the desired unbounded full moment. This is an internally
derived conditional extension requiring separate mathematical review.
