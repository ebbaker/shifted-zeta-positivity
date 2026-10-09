# Exact divisor packet cancellation in the adaptive tail

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Parallel same-model derivations and review are internal checks, not independent
specialist validation or formal proof verification.

Based on repository HEAD `480581447dcd3e93c9c2f9c22a050d9c5100ff9d`
and the working-tree [adaptive continuation](13_SHORT_FAMILY_ADAPTIVE_CONTINUATION_20261008.md).
The [strategic assessment](../../reviews/SHORT_FAMILY_PROGRAM_ASSESSMENT_20261008.md)
recommended seeking actual compensation before further absolute bounds.

There is an exact cancellation on a nonempty family of total products with
two large prime factors and a small nonunit cofactor. It holds for complex
twists, deletion zeros, and nonsquarefree cofactors. At the proposed
\(h=a=2/5,\theta=1/40\) test point, the entire packet family has arbitrarily
small full Schwartz-weighted energy. Its two opposing branches can each
exceed the target by the same coherent power as the known obstruction.

This is a local signed compensation result, obtained from finite convolution
algebra and the stated conductor comparison. It does not control the complete
tail: the essential unit-cofactor semiprimes survive. The accompanying
[product-sector barrier](16_SHORT_FAMILY_PRODUCT_BARRIER_20261008.md)
shows why their compensation must involve different total products.

## The coefficient after complete product recombination

Keep the manuscript's good ideal monoid and write

\[
 m_z(n)=\mu_K(n)\mathbf1_{Nn\le z},\qquad c_z=m_z*m_z,
 \qquad z=\sqrt{CD}.
\]

For any real \(Y>0\), define

\[
 t_{z,Y}(n)=-\sum_{\substack{d\mid n\\Nd>Y}}c_z(d).
 \tag{1}
\]

Complete multiplicativity, including every zero, gives the pointwise identity

\[
 T_{u,W}(D)=\sum_n t_{z,Y_u}(n)\lambda_u(n)W(Nn/D),
 \qquad Y_u=D^{1-\theta}/L_u.
 \tag{2}
\]

No pairwise coprimality condition has been imposed on the original factors.
On the profile, \(z<Nn\le z^2\) for sufficiently large \(D\). The
truncated inverse then also gives

\[
 t_{z,Y}(n)=\mu_K(n)+\sum_{\substack{d\mid n\\Nd\le Y}}c_z(d).
 \tag{3}
\]

The sum in (2) groups every tuple with the same total ideal \(n=abm\).
It does not estimate different total products independently.

## A pointwise divisor packet theorem

Let \(b\ne1\) be any good ideal, including a nonsquarefree one, and put
\(B=Nb\). Let \(q,r\) be distinct good prime ideals coprime to \(b\).
Write \(P^-(b)=\min_{p\mid b}Np\). Suppose

\[
 Nq,Nr\le z,\qquad BNq\le z,\qquad Nr\,P^-(b)>z,
 \tag{4}
\]
\[
 \max\{BNq,BNr\}\le Y<N(qr).
 \tag{5}
\]

Then

\[
 \boxed{t_{z,Y}(bqr)=0.}
 \tag{6}
\]

To prove this, a divisor of \(bqr\) not containing both \(q,r\) has
norm at most \(\max\{BNq,BNr\}\), and is excluded from the tail.
The surviving divisors are therefore \(qr e\), \(e\mid b\); all
of them exceed \(Y\). Furthermore (4)--(5) imply \(Y>z\), so \(q,r\)
cannot occur together in one truncated Möbius factor.

No prime dividing \(b\) can join the factor containing \(r\), because
its norm would exceed \(z\). Every divisor \(e\mid b\) can join the
factor containing \(q\), because \(N(qe)\le BNq\le z\). Consequently
the only possible ordered factor pairs are \((qe,r)\) and \((r,qe)\),
and

\[
 c_z(qre)=2\mu_K(e).
 \tag{7}
\]

For nonsquarefree \(e\), both sides are zero. Thus the same argument
allows arbitrary prime powers in \(b\), rather than silently discarding
nonsquarefree total products. Summing (7) gives

\[
 t_{z,Y}(bqr)=-2\sum_{e\mid b}\mu_K(e)=0.
 \tag{8}
\]

Every tuple carries the common value
\(\lambda_u(bqr)W(N(bqr)/D)\). The cancellation therefore survives
complex character phases and deletion zeros. It is applied before squaring,
so it requires no extension of a completed row-kernel estimate.

For prime \(b=p\), the cancellation is particularly explicit:

| Branch | Ordered factors | Free factor | Total coefficient |
| --- | --- | --- | --- |
| \(e=1\) | \((q,r),(r,q)\) | \(p\) | \(-2\) |
| \(e=p\) | \((pq,r),(r,pq)\) | \(1\) | \(+2\) |

Estimating these two branches separately would destroy the exact zero.

## A growing packet family with negligible full weighted energy

Assume the same native modulus comparison as the manuscript:

\[
 1\le L_u\ll_{\nu,S}Nu.
 \tag{9}
\]

Fix

\[
 h=a=2/5,\qquad \theta=1/40,
 \qquad 0<\delta<1/40,\qquad \eta=1/40.
 \tag{10}
\]

Let \(\mathcal P_\delta(D)\) be the row-independent set of total ideals
\(n=bqr\) on the profile that have a representation satisfying

\[
 1<B\le D^{1/40-\delta},\qquad BNq\le z,
 \qquad z/7<Nr\le z,
 \qquad (b,qr)=1,
 \tag{11}
\]

with distinct good primes \(q,r\). The set contains each ideal once,
even if a representation is not unique. Define its actual projected tail

\[
 \mathcal P_{u,W}(D)=
 \sum_{n\in\mathcal P_\delta(D)}
 t_{z,Y_u}(n)\lambda_u(n)W(Nn/D).
 \tag{12}
\]

All good prime ideals have norm at least seven, because \(S\) contains
the primes above six. Hence (11) implies the last strict inequality in (4).
For every row \(Nu\le D^{h+\eta}=D^{17/40}\),

\[
 Y_u\gg D^{1-\theta-h-\eta}=D^{22/40},
 \qquad
 \max\{BNq,BNr\}\le Bz\ll D^{21/40-\delta}.
 \tag{13}
\]

Also, uniformly on the fixed annulus,

\[
 N(qr)=Nn/B\ge cD^{39/40+\delta},
 \qquad Y_u\le D^{39/40}.
 \tag{14}
\]

The positive margins in (13)--(14) dominate all fixed constants for large
\(D\). The packet theorem applies to every such row, and

\[
 \mathcal P_{u,W}(D)=0\qquad(Nu\le D^{17/40}).
 \tag{15}
\]

The farther Schwartz rows have not been omitted. Ideal counting gives the
uniform bound

\[
 |\mathcal P_{u,W}(D)|
 \ll_W\sum_{Nn\le CD}\sum_{d\mid n}|c_z(d)|
 \ll_W D\log^2(2D).
 \tag{16}
\]

Indeed the last sum is majorized by the count of all ideal triples
\(a,b,m\) with \(N(abm)\le CD\). For every fixed decay order \(A>1\),
lattice counting and the Schwartz bound give

\[
 \sum_{Nu>D^{h+\eta}}\Phi(Nu/D^h)
 \ll_{A,\Phi}D^h D^{-\eta(A-1)}.
 \tag{17}
\]

Combining (15)--(17), choosing \(A\) after the requested error power,
proves the new controlled-sector statement

\[
 \boxed{
 \frac1D\sum_{u\ne0}\Phi(Nu/D^{2/5})
       |\mathcal P_{u,W}(D)|^2=O_N(D^{-N})
 \quad\text{for every }N>0.}
 \tag{18}
\]

This holds for every fixed smooth annular \(W\); it does not require
zero integral. The only conductor input is (9). It is not a new
conductor-uniform Möbius bound. Since (18) estimates the packet as an actual
response vector, its removal from the full tail is legitimate by the
weighted triangle inequality. It does not delete its individual branches.

## The sector is nonempty and its branches can be large

Fix a good prime cofactor \(b=p\), of norm \(P\), and take a point
\(t\in(c,C)\) where \(W(t)\ne0\). Choose

\[
 \beta\in(\max\{t/C,1/7\},1),\qquad
 \alpha=t/(C\beta)<1.
\]

Take the same sufficiently narrow prime windows
\(Nq\asymp\alpha z/P\), \(Nr\asymp\beta z\) in both branches.
Their centers satisfy \(PNq<z\), \(Nr>z/7\), and
\(PNqNr=tD\). Shrinking the windows preserves these strict inequalities
and puts all products in a neighborhood where
\(\Re(e^{-i\arg W(t)}W)\) has a positive lower bound. The fixed-field
prime ideal theorem supplies \(\asymp D/\log^2D\) pairs in these
windows. This imported counting input is needed only for the branch-size
illustration, not for the exact theorem or (18).

For \(\nu=1\), consider coherent rows \(u=v^6\) with \(Nv\le H^{1/6}\)
and \((v,p)=1\). The primes \(q,r\asymp D^{1/2}\) cannot divide
these small \(v\), and there are \(\asymp H^{1/6}\) distinct such
physical rows. Both branch amplitudes therefore have size
\(\gg_{W,p} D/\log^2D\) on these rows. Each separately has normalized
weighted energy

\[
 \gg_{W,p,\Phi} DH^{1/6}/\log^4D
 =D^{16/15}/\log^4D\qquad(H=D^{2/5}),
 \tag{19}
\]

which exceeds the proposed \(D^{4/5+\varepsilon}\) budget by \(4/15\)
in power. Their recombined contribution is exactly zero. For complex or
sign-changing \(W\), the same common narrow-window selector is essential
to this illustration; no lower bound for an unrestricted branch sum is
asserted.

## What remains after this cancellation

The same divisor sum equals one at \(b=1\). For balanced semiprimes
\(n=qr\) with \(Nq,Nr\le z\le Y_u<Nn\),

\[
 t_{z,Y_u}(qr)=-2.
 \tag{20}
\]

Thus the packet theorem cannot cancel the original \(m=1\) semiprime
obstruction. All decompositions of the same total semiprime have already
been included in (20); its compensation must cross total ideals. The
negligible packet sector does not imply a power estimate on that residual.

The [ideal mixed-discrepancy bridge](14_SHORT_FAMILY_IDEAL_MIXED_DISCREPANCY_20261008.md)
retains an explicit von Mangoldt discrepancy, principal density, both edges,
and the adaptive selector for the remaining tail. It supplies the next
interface for a signed arithmetic estimate, rather than allowing independent
estimates of the oversized branches. The full tail moment, any stronger
zero-free boundary, and descent to RH remain open.

## Finite verification

The [standalone checker](../../numerics/check_short_family_divisor_packets.py)
prints deterministic JSON and writes no files. Its
[small record](../../numerics/short_family_divisor_packet_record_20261008.json)
contains 3,982 exact assertions. The tests cover productwise closure, complete
tuple recombination, arbitrary and nonsquarefree cofactors, distinct equal-norm
prime symbols, complex phases, deletion zeros, strict cutoff boundaries, and
the rational exponents in (10)--(18).

The checker also computes actual local sextic residue symbols at split
Eisenstein primes through their two maps \(\omega\mapsto r\bmod p\),
where \(r^2+r+1=0\). It verifies multiplicativity and sixth-power deletion
masks, then replays a packet with prime norms \(13,19,241\),
\(D=32768,z=256\), and the exact cutoff test
\((Nd\cdot7)^{40}>32768^{39}\). Here seven is a good-radical proxy;
the computation does not assert that it equals the primitive combined
conductor. This finite example checks the local packet lemma, rather than membership in
the asymptotic growing-cofactor range. The packet has norm \(59,527\), while balanced semiprime and
prime-square witnesses survive the same cutoff.

These finite checks do not prove native reciprocity, the conductor comparison,
Poisson summation, prime ideal asymptotics, or any unbounded signed estimate.
The full Schwartz conclusion follows from the proof above, not from the
finite record.

The [scoped review](../../reviews/SHORT_FAMILY_SIGNED_PACKET_REVIEW_20261008.md)
records the separate same-model audit and the reproducibility checks.
