# The live plain divisor: exact splitting and the unchanged width obstruction

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

**Status.** This note proves a coefficient identity and a positive
Cauchy/reindexing inequality on the squarefree, mutually coprime core. It
does not prove the mixed moment. Every use of the complete smooth-family
Poisson initialization below is **conditional on resolving the selector
feasibility gate**, analyzed in the [selector note](SELECTOR_FEASIBILITY_20261008.md)
and required by the [continuation](CONTINUATION_20261008.md). In
particular, a formal calculation in that enlarged family does not give a
formula for the sharply restricted physical rows.

The new bookkeeping point is that the live plain divisor can be moved
into the canonical averaged label after a Cauchy step. Its energy cost is
its length, not twice its length: the label and divisor reindex together.
This removes that particular residual coefficient in the separated
positive child, but leaves the first canonical width margin negative
throughout the requested box. Near the endpoint where essentially all
plain length is live, even a hypothetical baseline estimate for that
larger canonical support would leave a macroscopic Cauchy cost.

## 1. Inputs and distinct meanings of the labels

Use the actual profiles, physical prime lists, finite ray factor, zero
extensions and normalization of the [manuscript](../manuscript.tex).
Write

\[
 D=U^r,\qquad N=U^m,\qquad P_i=U^{w_i},\qquad
 z=\sum_iw_i,\qquad L=r+m+z.
\]

The actual squarefree-core coefficient, with the fixed ray factor
\(\nu(v)\) removed, is \(\mu_F(v)h(v)\), where

\[
 h(v)=\sum_{kP\mid v}\mu_F(k)\mu_F(P)
 A\left(\frac{\mathrm Nv}{\mathrm Nk\,\mathrm NP\,D}\right)
 B(\mathrm Nk/N)
 \prod_i a_i(p_i)W_i(\mathrm Np_i/P_i),\qquad P=\prod_i p_i.
 \tag{1}
\]

Every divisor in (1) is outside the fixed excluded set. Each \(p_i\)
belongs to its original list. The factorization means that \(k,P\), and
\(v/(kP)\) are pairwise coprime; here this is equivalent to their product
being squarefree with no repeated prime. No profile in (1) is replaced by
an arbitrary arithmetic coefficient.

We checked the September 30 source itself, Lemma 17.2 and equations
(17.69), (17.72)--(17.85), in the cached PDF with SHA-256
`8fe93046f8cf5ef1ba5969c89addc02d76311adc4ee907509ff9cd96f7ec99e7`.
The source is the [September 30 companion preprint](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf).
Its analytic assertions remain assumed rather than independently proved.

Rename the source's transformed label \(f\) as \(g\), and rename its
transformed row \(k\) as \(y\). Specifically, if \(C\) is the initial
column gcd, \(a\mid C\) is the source's Poisson mask divisor \(d'\),
and \(s\) is its subsequent coprimality-inclusion divisor, put

\[
 t=C/a,\qquad g=as,\qquad y=ah',\qquad v=Csn=tgn.
 \tag{2}
\]

The ideals \(t,a,s,n\) are squarefree and pairwise coprime on nonzero
support. The element \(h'\) need not be coprime to every one of them:
the source retains the precise zero conditions rather than asserting
such coprimality. The character in the child is
\(\chi_n(y)\chi_n(g)^4\), with fixed puncture \(1_{(n,t)=1}\).
There is no inverse/physical-prime overlap in this core, so the source's
earlier overlap ideal \(j\) equals one.

The transformed label \(g\) is **not** the primitive conductor of a
physical row, and is **not** the column-ratio conductor in the remaining
target. Before formal coprimality extension, the latter conductor in this
squarefree sector is the product of the two coprime quotient columns.
After the extension used to obtain (2), that formal product cannot be
called the conductor of a newly introduced noncoprime pair.

## 2. Exact coefficient with every slot assigned

For each physical slot choose its unique location among \(t,a,s,n\).
Let \(J_t,J_a,J_s,J_n\) be the resulting partition of the slot set and
write

\[
 P_x=\prod_{i\in J_x}p_i\quad(x=t,a,s,n),\qquad
 P_0=P_tP_aP_s,\qquad P=P_0P_n.
\]

The assignments mean \(P_t\mid t\), \(P_a\mid a\), \(P_s\mid s\),
and \(P_n\mid n\), with the original list and individual coefficient
on each slot. This is a disjoint exact partition on the squarefree core,
so no priority convention or multiplicity factor is being hidden.

The original plain divisor splits uniquely as

\[
 k=k_0k_1,\qquad k_0\mid tg/P_0,\qquad k_1\mid n/P_n.
 \tag{3}
\]

Consequently the exact substitution in (1) is

\[
\begin{split}
 h(tgn)={}&\sum_{J_t\sqcup J_a\sqcup J_s\sqcup J_n=I}
 \sum_{\substack{p_i\in\mathcal P_i\\
                 P_t\mid t,\ P_a\mid a,\ P_s\mid s,\ P_n\mid n}}
 \sum_{\substack{k_0\mid tg/P_0\\k_1\mid n/P_n}}
 \mu_F(k_0)\mu_F(k_1)\mu_F(P_0)\mu_F(P_n)\\
 &\quad\times
 A\left(\frac{\mathrm Nt\,\mathrm Ng\,\mathrm Nn}
 {\mathrm Nk_0\,\mathrm Nk_1\,\mathrm NP_0\,\mathrm NP_n\,D}\right)
 B\left(\frac{\mathrm Nk_0\,\mathrm Nk_1}{N}\right)
 \prod_i a_i(p_i)W_i(\mathrm Np_i/P_i).
\end{split}
\tag{4}
\]

In particular, the Möbius sign of the live plain divisor \(k_1\) is
still present. The signs \(\mu_F(a)\mu_F(s)\) from the source's
outer mask expansion are separate signs and must also remain. They do
not cancel \(\mu_F(k_1)\) by a formal convolution argument.

The source's outer zero conditions here include \((s,C)=1\) and
\((s,h')=1\). Its row ball, fixed ray coefficient, dyad cutoffs and
Fourier phases stay outer. On the inner side,
\(1_{(n,t)=1}\chi_n(y)\chi_n(g)^4\) retains the exclusions at
\(C,s\) and the numerator zeros at \(a,h'\). Equation (4) makes no
change to these factors. In particular, it does not replace a
zero-extended character by a unit-valued phase at an excluded prime.

The product condition in \(B\) is essential. Replacing it by independent
unrestricted conditions on \(k_0,k_1\) changes the coefficient. Smooth
Mellin/Fourier separation may be applied to a single common compact
profile in independent normalized coordinates, before the arithmetic
variables are evaluated. It then restores the displayed coupling under
inversion. A profile or Fourier measure chosen separately after fixing
the current label or row would not have the required uniformity.

## 3. Support and the endpoint stratum

Let \(B_C,\theta,v_s\) denote the source's dyadic centers for
\(C,a,s\), and set

\[
 \beta=B_C-\theta,\qquad V=\theta+v_s,\qquad
 R=L-B_C-v_s=L-\beta-V.
\]

Thus \(t,g,n\) have norm exponents \(\beta,V,R\), respectively.
All displays of exact exponent centers below have the source's harmless
annular tolerances; nonempty negative-center windows are clipped as in
its (17.74). These small losses are not sources of a fixed saving.

Put

\[
 \lambda=\log_U\mathrm Nk_1,\qquad
 z_n=\sum_{i\in J_n}w_i,\qquad z_0=z-z_n.
\]

The coupled plain cutoff gives
\(\log_U\mathrm Nk_0=m-\lambda+O(1/\log U)\). The two inverse
factors reconstructed from (4) are

\[
 d_0=tg/(k_0P_0),\qquad d_1=n/(k_1P_n),
\]

with centers

\[
 r_0=\beta+V-m+\lambda-z_0,\qquad
 r_1=R-\lambda-z_n,\qquad r_0+r_1=r.
 \tag{5}
\]

Each is nonnegative up to the bounded endpoint tolerance. In particular,

\[
 \max\{0,m+z_0-\beta-V\}\le\lambda
 \le\min\{m,R-z_n\}
 \tag{6}
\]

at exponent scale. This support restriction is real; it is not a new
conductor bound.

When \(\lambda\approx m\), \(k_0\) has bounded or very short norm,
and the residual ideal still contains almost all of the plain factor.
For example, the formal sector \(C=a=s=t=g=1\), if nonempty for the
chosen supports, has \(k_0=1\), \(R=L\), and all physical slots in
\(n\). It retains exactly the original free annular divisor
\(k_1\) in \(h(n)\). This is an allowed support test, not an assertion
that the sector has a main term or dominates the moment.

The first dual row ball comes from the full original columns, whose
length is \(L\). In the notation above the source's formal centers are

\[
 M=2L-1-2\beta,\qquad F=R+V=L-\beta,
 \qquad \kappa=1-2L+\beta.
 \tag{7}
\]

Splitting the divisor in (3) leaves (7) unchanged. In particular,
\(\lambda\approx m\) does not give the inverse-only row width.
For the example just given and \(z=(1-r)/2-\rho\), the row center is
\(r+2m-2\rho\), not \(r-2\rho\).

## 4. Moving the live divisor into the averaged label

There is an exact useful identity beyond a scalar divisor bound. Write
\(q=k_1\), \(n=qe\), and

\[
 A_*(n)=\overline{\alpha(n)}\gamma_2(n)\nu_*(n)
\]

for the source's canonical coefficient after its fixed ray expansion.
On squarefree coprime arguments, its equation (17.72), specialized to
the unit values of the other two arguments, gives

\[
 A_*(qe)=A_*(q)A_*(e)\chi_e(q)^4.
\]

Therefore the live-divisor summand satisfies

\[
\begin{split}
 &\mu_F(q)A_*(qe)1_{(qe,t)=1}
       \chi_{qe}(y)\chi_{qe}(g)^4\\
 &\quad=\mu_F(q)A_*(q)1_{(q,t)=1}
       \chi_q(y)\chi_q(g)^4
       A_*(e)1_{(e,t)=1}\chi_e(y)\chi_e(gq)^4.
\end{split}
\tag{8}
\]

Here \((q,g)=1\), so the new label
\(\widetilde g=gq\) is squarefree. The zero extension in
\(\chi_e(\widetilde g)^4\) enforces \((e,gq)=1\); the fixed
puncture at \(t\) is unchanged. The scalar
\(\chi_q(y)\) retains its original numerator zeros. No additional
moving puncture is discarded. Since the plain ideal is coprime to all
physical slots, all residual slot primes lie in \(e\), keeping their
original lists and individual coefficient products.

In (4) the inverse profile after this substitution is

\[
 A\left(\frac{\mathrm Nt\,\mathrm Ng\,\mathrm Ne}
 {\mathrm Nk_0\,\mathrm NP_0\,\mathrm NP_n\,D}\right),
 \qquad B(\mathrm Nk_0\,\mathrm Nq/N)
\]

for the plain profile. Their coupling to outer scales must still be
separated by one common smooth measure. After this separation the inner
polynomial in \(e\), at each fixed mode, has the canonical coefficient
class with label \(\widetilde g\), fixed puncture \(t\), and the
remaining physical prime marks. Its centers are

\[
 \widetilde R=R-\lambda,\qquad
 \widetilde V=V+\lambda,\qquad
 \widetilde F=F,\qquad \widetilde M=M.
 \tag{9}
\]

Here is the explicit polynomial that makes this independence precise.
For one fixed Fourier mode \(\xi\), with harmless endpoint clipping
understood, set \(z_e=\mathrm Ne/U^{R-\lambda}\) and

\[
\begin{split}
 R_{\widetilde g,\xi}(y)
  &=\sum_{e\ {\rm sf}}A_*(e)1_{(e,t)=1}
    \chi_e(y)\chi_e(\widetilde g)^4
    d_\xi(e)\,\omega_e(z_e)z_e^{i\xi_e},\\
 d_\xi(e)
  &=\sum_{\substack{p_i\in\mathcal P_i\ (i\in J_n)\\p_i\mid e}}
    \prod_{i\in J_n}\mu_F(p_i)a_i(p_i)
       W_i(\mathrm Np_i/P_i)(\mathrm Np_i/P_i)^{i\xi_i}.
\end{split}
\tag{9a}
\]

On the conjugated side the corresponding conjugations and Fourier signs
are understood. The cutoff \(\omega_e\) has a fixed full annular
support enclosing every quotient of the current \(n\)-window by the
chosen \(q\)-window. Neither it nor \(d_\xi\) depends on the actual
\(q,g,y\); the dependence on \(q\) left inside (9a) is precisely
the label \(\widetilde g=gq\).

To obtain (9a), choose the common joint compact profile using independent
normalized coordinates for \(C,a,s,h'\), and on each side for
\(q,e,k_0\) and every physical slot prime, before evaluating any of
those ideals. For example these latter coordinates are
\(x_q=\mathrm Nq/U^\lambda\),
\(x_e=\mathrm Ne/U^{R-\lambda}\),
\(x_0=\mathrm Nk_0/U^{m-\lambda}\) and
\(x_i=\mathrm Np_i/P_i\). The inverse and plain factors in this
profile are exactly
\(A(x_Cx_sx_e/(x_0\prod_i x_i))\) and \(B(x_0x_q)\).
The old column windows involve \(x_Cx_sx_qx_e\); the full Poisson
kernel and its normalized real roots also stay in the common joint
profile, as in the source's (17.75)--(17.76). Larger fixed cutoffs make
that profile compact in the independent coordinates. Retain the
individual \(W_i\) and fresh \(\omega_e\) outside inversion. Fourier
inversion then puts only pure norm powers on their coefficients, as
displayed in (9a), and puts the other coordinates' modes in the outer
weight. The Fourier measure is common to the full current row and label
sum; it is not chosen after \(q\) or \(g\) is known. Divisibility,
coprimality and the source's arithmetic outer masks stay outside this
smooth separation.

This is a transfer of arithmetic structure after an explicit Cauchy
loss. It is not an application of Lemma 17.2 to \(h(tgn)\).

For clarity, the relevant Cauchy calculation can be stated independently
of any analytic moment theorem. Suppose a separated branch, for fixed
\(t\), has the form

\[
 Q_g(y)=\sum_{\substack{\mathrm Nq\asymp U^\lambda\\(q,g)=1}}
          c(q,g,y)R_{gq}(y),\qquad |c(q,g,y)|\ll U^\epsilon,
 \tag{10}
\]

where \(g,q\) are squarefree and the polynomial \(R_{gq}\) depends
on \(q\) only through its displayed label. Bounded row phases and
zero masks are permitted in \(c\). For divisor weights of fixed order,
ideal counting and Cauchy give

\[
 \sum_g d_F(g)^C\sum_y|Q_g(y)|^2
 \ll U^{\lambda+\epsilon}
 \sum_{\widetilde g\ {m sf}}d_F(\widetilde g)^{C'}
       \sum_y|R_{\widetilde g}(y)|^2.
 \tag{11}
\]

The row domain is the same on both sides. The label window on the right
encloses the product of the two original windows. Indeed, Cauchy first
costs at most \(O(U^\lambda)\) for the number of possible \(q\).
The subsequent sum over \((g,q)\) has at most \(d_F(\widetilde g)\)
preimages of a fixed \(\widetilde g=gq\). It must not be charged
another \(U^\lambda\) independent count.

The choices of \(k_0\mid tg/P_0\) and of the bounded number of
assigned physical primes enter the source fibre with at most a fixed
divisor power. After reindexing, they divide \(t\widetilde g\),
so that their multiplicity is bounded by a fixed product of divisor
powers in \(t\) and \(\widetilde g\). As in the source's (17.80),
this changes divisor weights and freely chosen small losses; it does
not remove the explicit Cauchy cost in (11). The common Fourier density
is integrated once, with the needed seminorm and height bounds. Only a
fixed number of additional smooth coordinates is used. Derivative
orders must be chosen before any application height cutoff, just as in
the source; no uniformity for an arithmetic row selector follows.

Equations (8)--(11) are a proved partial structural reduction. They do
not assert a bound for the right side of (11) on the present support.

## 5. Width and cost table

Ignoring only the freely chosen small window tolerances, the canonical
puncture has exponent \(\beta\) and the surviving mark has cap
\(z_n\). Equations (7) and (9) give the actual formal margins

\[
 \widetilde F-\widetilde M-\beta-z_n=1-L-z_n,
 \qquad
 4\widetilde F-3\widetilde M-6z_n=3-2L+2\beta-6z_n.
 \tag{12}
\]

The first is independent of \(\lambda\). Even if every physical
prime has been assigned outside the residual column,

\[
 1-L-z_n\le1-r-m\le-3/50.
 \tag{13}
\]

Thus the first hypothesis of Lemma 17.2 fails by a fixed amount on
every branch of this attempted application. Its prohibition on a
residual divisor coefficient cannot be bypassed by a scalar bound;
even after (8)--(11) remove that coefficient, the genuine support
still lies outside its width conditions.

In the no-assigned-slot endpoint \(\beta=0,z_n=z\), (12) recovers
the audited margins

\[
 2\rho-m,\qquad 2r-1-2m+8\rho
 \quad\text{when }z=(1-r)/2-\rho.
\]

The following table is per separated Cauchy side. Put
\(\eta_*=1/5000\). A hypothetical canonical baseline bound on the
larger support would be \(H\ll U^{2F+\epsilon}\) for its
unnormalized squared norm. This is precisely the estimate that the
available lemma does not furnish here.

| Live plain length | Residual / label lengths after (8) | Proposed treatment and genuine cost | Status against \(K=1+\delta m-\eta_*\) |
| --- | --- | --- | --- |
| Exact \(k_1=1\) | \(R,V\) | Put \(k_0\) in the outer divisor fibre and separate the profiles; no live-divisor Cauchy cost. | Canonical coefficient class can be recovered, but (13) still forbids the available theorem. |
| \(0\le\lambda\le\delta m-\eta_*\), subject to (6) | \(R-\lambda,V+\lambda\) | Apply (11), costing \(U^\lambda\) in energy. | A new baseline estimate on this support would fit the target, apart from strictly reserved small losses. No such estimate is supplied. |
| \(\delta m-\eta_*<\lambda<m\), subject to (6) | \(R-\lambda,V+\lambda\) | The same reindexing and same cost. | Even a new baseline estimate would require an additional energy saving \(\lambda-\delta m+\eta_*\). |
| \(\lambda\approx m\) | \(R-m,V+m\); \(k_0\) bounded or short | Almost all the plain factor enters the averaged label; row width remains \(M\). | Additional saving approaches \((1-\delta)m+\eta_*\), on top of solving the width problem. |

The cost statement follows from the source normalization identity

\[
 \kappa+\beta+2F=1.
\]

Thus a hypothetical baseline child bound together with (11) gives
exponent \(1+\lambda\), not \(1\). For unequal side strata
\(\lambda_1,\lambda_2\), the source's weighted Cauchy geometric mean
gives exponent \(1+(\lambda_1+\lambda_2)/2\). There is no basis for
assuming that only a favorable diagonal choice of strata occurs.

At the live endpoint the required additional cost reduction is bounded
on the full parameter rectangle by

\[
 \frac{209}{1000}
 \le (1-\delta)m+\frac1{5000}
 \le\frac{1601}{5000}.
 \tag{14}
\]

These are exact endpoint evaluations, using monotonicity in \(m\) and
\(\delta\). The lower endpoint is
\((1-21/50)(9/25)+1/5000\). The cost is much larger than the sought
\(1/5000\) gain. Neither (12) nor (14) is a lower bound on the actual
mixed moment: they diagnose this particular transfer and Cauchy route.

Dyadic decomposition of \(\mathrm Nk_1\) uses \(O(\log U)\)
strata. Finite slot assignments, divisor fibres and logarithmic stratum
sums are absorbed into chosen positive losses with uniform profile
bounds. They do not absorb any fixed power in (11) or repair (13).

## 6. Consequence for the continuation

The calculation does not authorize a complete-family enlargement, and
its identities do not preserve a sharp exceptional-row selector through
Poisson summation. That is the independent first gate. In particular,
neither a principal physical row nor a sixth-power physical row should
be confused with the label \(g\) or with a principal column pair.

Even conditional on that first gate, the endpoint test rules out closing
the continuation by a formal plain-divisor split followed by the old
canonical lemma. The split can recover its coefficient class after a
controlled Cauchy step, but cannot recover its admissible support. A
useful new estimate would have to exploit the signed \(q\)-sum before
that Cauchy loss, or control a genuinely broader mixed/label family on
the retained support, while also addressing the physical row selector.

No new saving, complete mixed theorem, or zero-free boundary is claimed.
The current conditional candidate remains \(7/8-1/24000\), and the
proposed \(7/8-1/20000\) still requires the unproved uniform input
specified in the manuscript.

The reproducible [selector and divisor checker](../numerics/check_selector_feasibility.py)
checks the rational endpoint bounds, unchanged \(F\), width identities
and normalization used here. Such checks establish the displayed
arithmetic identities and costs; they do not prove an analytic saving.
