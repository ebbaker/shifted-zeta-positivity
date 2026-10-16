# Exact compensation between the two low/high edges

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
This is an internal derivation with finite algebra checks, not independent
specialist validation or a formal proof certificate.

This note refines the divisor packet theorem of note 15 inside the exact
logarithmic bridge of note 14. A small von Mangoldt factor can make an edge
as large as its opposing large-von-Mangoldt edge, with exact cancellation
between them. There is a positive integral formula for their common
coefficient. This identifies genuine signed compensation, and an obstruction
to estimating all selected edge pieces separately. It proves no bound for
the full adaptive tail beyond the already controlled divisor packets.

## 1. Exact endpoint conditions and the four pieces

Work in the good ideal monoid. Put
\[
 m_z(n)=\mu_K(n)\mathbf1_{Nn\le z},\qquad c_z=m_z*m_z,
 \qquad t_{z,Y}(n)=-\sum_{d\mid n,\ Nd>Y}c_z(d).
\]
Complete multiplicativity, including deletion zeros, gives
\[
 T_{u,W}(D)=\sum_n t_{z,Y_u}(n)\lambda_u(n)W(Nn/D).
\]
The logarithmic bridge, away from its explicit unit term, is
\[
 2\sum_{\substack{N(a\ell)\le z,\ Nc\le z\\N(a\ell c)>\max(1,Y)}}
 \frac{\mu_K(a)\Lambda_K(\ell)\mu_K(c)}{\log N(a\ell c)}
 \lambda_u(a\ell c)S_{u,W}(D/N(a\ell c)).                 \tag{1}
\]
Here \(\Lambda_K(p^j)=\log Np\), not \(j\log Np\). Split (1) by
\(Na\le U\) or \(Na>U\), and \(N\ell\le V\) or \(N\ell>V\).
Write LH for low \(a\), high \(\ell\), HL for high \(a\), low
\(\ell\), and retain HH and LL as well. Equality belongs to the low side.

Let \(b\ne1\) be any good ideal, put \(B=Nb\), and let \(q,r\) be
distinct good prime ideals coprime to \(b\). Suppose
\[
 Nq,Nr\le z,\quad BNq\le z,\quad NrP^-(b)>z,             \tag{2}
\]
\[
 \max\{BNq,BNr\}\le Y<N(qr),                            \tag{3}
\]
\[
 B\le\min(U,V),\qquad Nq,Nr>\max(U,V).                  \tag{4}
\]
These are sufficient conditions, including their strict and weak endpoints.
There is no omitted coprimality assumption on the individual factors in (1).
Conditions (2)--(3) imply \(Y>z\). Exactly the divisors \(d=qre\),
\(e\mid b\), occur in the original tail at total product \(n=bqr\).
The only allowable original ordered truncated factors are \((qe,r)\)
and \((r,qe)\); the free factor is \(b/e\).

## 2. The edge coefficients, including nonsquarefree cofactors

Put \(L=\log N(qr)\) and \(l_e=\log Ne\). For each divisor
\(e\mid b\), the complete contributions with convolution divisor
\(d=qre\), after factoring out the common
\(\lambda_u(bqr)W(N(bqr)/D)\), are
\[
 \mathrm{LH}_e=-\frac{2\mu_K(e)L}{L+l_e},\qquad
 \mathrm{HL}_e=-\frac{2\mu_K(e)l_e}{L+l_e},\qquad
 \mathrm{HH}_e=\mathrm{LL}_e=0.                           \tag{5}
\]

To verify this directly, \(\ell=q\) gives \((a,c)=(e,r)\), and
\(\ell=r\) gives \((a,c)=(1,qe)\). They both belong to LH by (4),
and their numerator is \(-2\mu_K(e)(\log Nq+\log Nr)\).
The other von Mangoldt factors are prime powers \(\ell\mid e\).
They occur with \((a,c)=(qe/\ell,r)\). They belong to HL because
\(Na\ge Nq>U\) and \(N\ell\le B\le V\). Their numerator is
\[
 2\sum_{\ell\mid e}\mu_K(e/\ell)\Lambda_K(\ell)
 =-2\mu_K(e)\log Ne.                                    \tag{6}
\]
This uses the exact identity \(\mu_K*\Lambda_K=-\mu_K\log N\).
For nonsquarefree \(e\), the right side of (6) vanishes; its separate
prime-power summands need not vanish and must be retained until recombination.
No HH or LL term can occur: \(\Lambda_K\) is supported on one prime
power, and (2)--(4) classify every such possibility as just described.

Define
\[
 J_b(L)=\sum_{e\mid b}\frac{\mu_K(e)}{L+\log Ne}.
\]
Summing (5), and using \(\sum_{e\mid b}\mu_K(e)=0\), proves
\[
 \boxed{\mathrm{LH}_b=-2LJ_b(L),\qquad
        \mathrm{HL}_b=+2LJ_b(L),\qquad
        \mathrm{HH}_b=\mathrm{LL}_b=0.}                  \tag{7}
\]
The complete packet is exactly zero. These identities survive arbitrary
complex physical twists and every deletion mask because the total ideal
\(bqr\) is common. They hold for every profile \(W\); zero integral is
unnecessary for this finite cancellation.

For \(b=p\), (7) reads particularly simply:
\[
 \mathrm{LH}_p=-\frac{2\log Np}{\log N(pqr)},\qquad
 \mathrm{HL}_p=+\frac{2\log Np}{\log N(pqr)}.              \tag{8}
\]
The formal unit-cofactor case has \(J_1(L)=1/L\), LH coefficient \(-2\),
and HL coefficient zero. The general pre-cancellation HL formula is
\(2LJ_b(L)-2\sum_{e\mid b}\mu_K(e)\). Thus (7) must not be extended
to \(b=1\): the surviving semiprime obstruction is still present.

## 3. A positive integral and its quantitative size

Let \(k=\omega(b)\ge1\), \(w_p=\log Np\), and
\(R_b=\sum_{p\mid b}w_p=\log N\operatorname{rad}(b)\). Finite
expansion and \(1/x=\int_0^\infty e^{-xt}\,dt\) give
\[
 \boxed{J_b(L)=\int_0^\infty e^{-Lt}
                  \prod_{p\mid b}(1-e^{-w_pt})\,dt>0.}  \tag{9}
\]
Using \(xe^{-x}\le1-e^{-x}\le x\), for \(x\ge0\), yields
\[
 \frac{k!\prod_{p\mid b}w_p}{(L+R_b)^{k+1}}
 \le J_b(L)\le
 \frac{k!\prod_{p\mid b}w_p}{L^{k+1}}.                   \tag{10}
\]
For fixed nonunit \(b\), rescale \(t=s/L\) in (9) and apply dominated
convergence to obtain
\[
 J_b(L)\sim\frac{k!\prod_{p\mid b}w_p}{L^{k+1}},\qquad
 |\mathrm{LH}_b|=|\mathrm{HL}_b|
 \sim\frac{2k!\prod_{p\mid b}w_p}{L^k}.                \tag{11}
\]
This is a positive kernel for one already canceled packet; it supplies no
positive sign for the sum of different total products or different packets.
In particular, (9) alone does not establish a renewal contraction.

## 4. Consequences at the proposed small-theta test point

For the lower-bound illustration only, take the trivial fixed twist
\(\nu=1\), and take \(h=a=2/5\), \(\theta=1/40\), and \(U=V=D^{1/50}\).
For fixed \(b\ne1\), choose narrow prime windows
\(q\asymp z/B\), \(r\asymp z\) satisfying (2) and with \(bqr\)
in a nonzero phase-consistent part of the profile. Conditions (4) hold
eventually. On all significant rows \(Nu\le D^{17/40}\),
\(Y_u\gg D^{11/20}\), while \(Bz\asymp D^{1/2}\), and
\(N(qr)\asymp D\), whereas \(Y_u\le D^{39/40}\). Thus (3)
holds uniformly for large \(D\). The complete packet remains pointwise
zero on those rows, just as in note 15.

Using the same fixed-window prime-ideal counting input as notes 15--16,
there are \(\asymp D/\log^2D\) such pairs. On coherent rows
\(u=v^6\) with the fixed cofactor and prime windows coprime to \(v\),
the relevant physical phases are one. A nonzero smooth complex profile has
a narrow interval on which one fixed rotation of it has positive real part.
Equations (10)--(11) then give each selected edge-packet amplitude
\(\gg_{b,W,\Phi} D/\log^{k+2}D\). The same coherent-row count
\(\asymp H^{1/6}\) gives selected edge-packet energy
\[
 \frac1D\sum_u\Phi(Nu/H)|\mathrm{selected\ LH\ packet}_u|^2
 \gg_{b,W,\Phi}\frac{D H^{1/6}}{\log^{2k+4}D},                   \tag{12}
\]
and the identical estimate for HL. For \(H=D^{2/5}\), this is
\(D^{16/15}/\log^{2k+4}D\), above the desired \(D^{4/5+\epsilon}\)
budget. For prime \(b\), the denominator is \(\log^6D\).

Statement (12) concerns an explicitly selected common-total-product packet
inside an edge. Other total products can cancel that packet within the full
edge, so (12) is not a lower bound for the full LH edge, the full HL edge,
or the full tail. It does rule out a proof that uniformly charges every
such selected edge piece to the target budget before retaining its opposing
edge. The full packet in (12) has energy zero on the significant rows.

## 5. What remains unresolved

The two edges are not automatically cheap merely because one factor is
small: (7)--(12) make their necessary coupling explicit. The HH sector,
the edge terms outside these packets, and compensation across the surviving
unit-cofactor semiprimes remain unbounded. The integer source
`papers/prime-variance-exponents/notes/programs/01_signed_arithmetic_covariance/ARITHMETIC_CLOSURE_ATTEMPT_20261004.md`,
lines 162--176, likewise presents Selberg or renewal as an available place
to test a new argument, while explicitly recording no proved contraction.
The finite positive formula (9) is not that missing contraction.

The accompanying `check_short_family_edge_compensation.py` verifies the complete
triple expansion, all four classifications, and (5)--(7) with exact formal
logarithms for squarefree and nonsquarefree cofactors. It also checks finite
rational evaluations of (10) and the first nonzero finite-difference moment.
It does not certify analytic prime-ideal counting or the full tail estimate.

See the [logarithmic bridge](14_SHORT_FAMILY_IDEAL_MIXED_DISCREPANCY_20261008.md),
[divisor packets](15_SHORT_FAMILY_DIVISOR_PACKET_CANCELLATION_20261008.md),
[checker](../../numerics/check_short_family_edge_compensation.py),
[record](../../numerics/short_family_edge_compensation_record_20261008.json),
and [scoped review](../../reviews/SHORT_FAMILY_SQUAREFREE_AND_COFACTOR_REVIEW_20261008.md).
