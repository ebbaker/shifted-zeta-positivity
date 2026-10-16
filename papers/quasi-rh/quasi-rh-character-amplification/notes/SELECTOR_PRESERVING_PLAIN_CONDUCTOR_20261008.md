# A selector-preserving reduction by the conductor of the plain ratio

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

**Status.** This note proves an additional controlled sector of the actual
mixed moment using the existing marked inverse input and elementary ideal
pair counting. It preserves the exceptional-row selector. It removes pairs
whose **plain-variable ratio** has small conductor even when their total
column ratio has large conductor. It also increases the removable total
ratio-conductor range using the existing coarse row-count input. The
remaining mixed estimate is still open; this is neither a new zero-free
boundary nor an obstruction to that estimate.

Use the [manuscript](../manuscript.tex) setting, actual coefficients,
profiles, zero extensions, height uniformity and three stated inputs.
The external source assumptions are unchanged. This follows the
[selector-feasibility note](SELECTOR_FEASIBILITY_20261008.md), which leaves
the complete-family enlargement unjustified, and supplies a reduction
that does not require that enlargement.

## 1. Two different ratio conductors

Keep the original tuple \(\tau=(d,k,(p_i))\), total column
\(n(\tau)=dk\prod_i p_i\), and coefficient \(b(\tau)\) from the
manuscript. In particular,

\[
 X=DN\prod_iP_i,
 \qquad M_r(u)S_m(u)Q_I(u)
 =X^{-1/2}\sum_\tau b(\tau)\chi_{n(\tau)}(u)^{s_\chi}.
\]

For the plain ideals alone define

\[
\begin{split}
 e_p^{\rm pl}(k,k')&=(v_p(k)-v_p(k'))\bmod6\in\{0,\ldots,5\},\\
 c_{\rm pl}(k,k')&=\prod_{e_p^{\rm pl}\ne0}p^{e_p^{\rm pl}},
 \qquad f_{\rm pl}(k,k')=\operatorname{rad}(c_{\rm pl}),\\
 E_{\rm pl}(k,k')&=\prod_{\substack{p\mid kk'\\e_p^{\rm pl}=0}}p.
\end{split}
\tag{1}
\]

The same local proof as for the total columns gives the exact identity

\[
 \chi_k(u)^{s_\chi}\overline{\chi_{k'}(u)^{s_\chi}}
 =\chi_{c_{\rm pl}(k,k')}(u)^{s_\chi}
   1_{(u,E_{\rm pl}(k,k'))=1}.
 \tag{2}
\]

Here \(f_{\rm pl}\) is the moving primitive conductor of this plain
ratio character at the good primes. It is not the primitive conductor
\(Q_{\psi_u}\) of the physical row, nor the total-column ratio
conductor \(f(n(\tau),n(\tau'))\). There is no general divisibility
relation between the two ratio conductors: the inverse and physical
prime variables can introduce, or cancel modulo six, local exponents.

If a phase cancels, its zero remains. For example, \(k=p^6,k'=1\)
has \(f_{\rm pl}=1\) and \(E_{\rm pl}=p\), giving
\(1_{p\nmid u}\), not the constant one. Likewise equal valuations
of a prime in both plain ideals contribute to \(E_{\rm pl}\).

## 2. A weighted plain-pair theorem

Fix all separating parameters. Let \(w(u)\ge0\) be any summable
weight on physical element rows and put \(\mathcal A=\sum_u w(u)\).
This is a statement about a nonnegative weight of controlled total
mass; no estimate is asserted for arbitrary weights without such a
mass bound. Define

\[
 \mathcal K_w^{\rm pl}(k,k')
 =\sum_u w(u)\chi_{c_{\rm pl}(k,k')}(u)^{s_\chi}
             1_{(u,E_{\rm pl}(k,k'))=1},
\]

and retain the actual plain coefficient
\(a(k)=\nu(k)B(\mathrm Nk/N)\), with its original fixed zeros.
For \(V\ge1\),

\[
 \frac1N\sum_{\substack{k,k'\\\mathrm Nf_{\rm pl}(k,k')\le V}}
 |a(k)a(k')\mathcal K_w^{\rm pl}(k,k')|
 \ll_\epsilon \mathcal A\,V^{1/2+\epsilon}N^\epsilon.
 \tag{3}
\]

The same estimate holds after any additional restriction on the plain
pair, including \(k\ne k'\). In (3), absolute values are taken after
all inverse/prime variables, if present in \(w\), have already been
assembled into a nonnegative weight. It is not an absolute bound for
the individual expanded inverse/prime tuples.

**Proof.** Zero-extended characters have modulus at most one, so
\(|\mathcal K_w^{\rm pl}(k,k')|\le\mathcal A\), with every mask
retained in the identity before this inequality. The profiles restrict
\(\mathrm Nk,\mathrm Nk'\) to fixed annuli at scale \(N\), and
their coefficients are bounded by the permitted seminorm and height
constants. The manuscript's elementary ideal-pair lemma, with its
column scale replaced by \(N\), gives

\[
 \#\{(k,k'):\mathrm Nk,\mathrm Nk'\ll N,
                    \ \mathrm Nf_{\rm pl}(k,k')\le V\}
 \ll_\epsilon N V^{1/2+\epsilon}.
\]

For completeness, write \(k=gA,k'=gB,(A,B)=1\), then
\(A=a_0a^6,B=b_0b^6\), with \(a_0,b_0\) sixth-power-free.
The ratio radical is \(\operatorname{rad}(a_0b_0)\). For each
allocation of its primes to the two sides and exponents \(1,\ldots,5\),
counting \(g\) costs at most
\(N/(\sqrt{\mathrm N(a_0b_0)}(\mathrm N(ab))^3)\).
The \(a,b\) sums converge, and summing the at most
\(10^{\omega(f_{\rm pl})}\) allocations gives the displayed bound.
Combining this with the kernel bound proves (3). Additional pair
restrictions decrease its positive majorant. No complete row kernel,
Poisson transformation, or arbitrary-coefficient inverse theorem is
used. \(\square\)

As a genuine partial-moment corollary, let \(\mathcal K\) be any
subcollection of the original plain support such that
\(\mathrm Nf_{\rm pl}(k,k')\le V\) for every pair in
\(\mathcal K\). Keeping the original coefficients on this
subcollection, put
\(S_{\mathcal K}(u)=N^{-1/2}\sum_{k\in\mathcal K}a(k)
\chi_k(u)^{s_\chi}\). Then

\[
 \sum_u w(u)|S_{\mathcal K}(u)|^2
 \ll_\epsilon \mathcal A V^{1/2+\epsilon}N^\epsilon.
 \tag{4}
\]

This corollary imposes an explicit condition on the subcollection; it
does not claim that the full annular plain support has that property.

## 3. Applying the theorem while preserving the selected rows

Take exactly

\[
 w(u)=1_{u\in\mathcal C_+}|M_r(u)Q_I(u)|^2.
 \tag{5}
\]

All inverse coefficients, prime lists, physical prime weights and
character masks remain inside this weight. The existing marked inverse
input bounds its mass by

\[
 \mathcal A\le\sum_{0<\mathrm Nu\le C_0U}|M_r(u)Q_I(u)|^2
 \ll_\epsilon U^{1+\epsilon}\mathcal H^{A_0}.
 \tag{6}
\]

The only enlargement in (6) is of a nonnegative inverse norm, already
authorized by that input. The weighted ratio kernel in (3) is still
the kernel on \(\mathcal C_+\); no smooth complete-row kernel has
been substituted for it. More generally, (3)--(6) remain valid with
\(1_{\mathcal C_+}\) replaced by any weight between zero and one
on the original physical row ball.

Let \(P_{\rm low}(V)\) be the exact signed contribution from
\(\mathrm Nf_{\rm pl}(k,k')\le V\) when only the plain factor is
expanded over \(\mathcal C_+\), including the whole plain diagonal:

\[
 P_{\rm low}(V)=\frac1N
 \sum_{\substack{k,k'\\\mathrm Nf_{\rm pl}(k,k')\le V}}
 a(k)\overline{a(k')}
 \mathcal K_w^{\rm pl}(k,k').
 \tag{7}
\]

The result is

\[
 |P_{\rm low}(V)|
 \ll_\epsilon U^{1+\epsilon}V^{1/2+\epsilon}\mathcal H^{A_0}.
 \tag{8}
\]

Set

\[
 \eta=\frac1{5000},\qquad\gamma=\frac1{6250},\qquad
 K=1+\delta m-\eta,\qquad
 v_{\rm pl}=2\delta m-\frac9{12500},\qquad V_{\rm pl}=U^{v_{\rm pl}}.
 \tag{9}
\]

Since \(2(\eta+\gamma)=9/12500\),

\[
 1+v_{\rm pl}/2=K-\gamma,
 \qquad
 \frac{3231}{12500}\le v_{\rm pl}\le\frac{5241}{12500}
 \tag{10}
\]

on the entire manuscript rectangle. Thus \(V_{\rm pl}>1\), and
(8) bounds the whole low-plain-conductor contribution by
\(O_\epsilon(U^{K-\gamma+\epsilon}\mathcal H^{A_0})\).
The freely chosen small losses include \(V_{\rm pl}^{\epsilon}\)
because its exponent lies in a fixed bounded range.

This sector includes genuinely off-diagonal plain pairs. For example,
\(k=ga,k'=gb\), with distinct coprime fixed good ideals \(a,b\),
has bounded plain-ratio conductor when \(g\) grows. If \(a,b\)
have equal norm, the two ideals occupy the same norm annulus. Choosing
different inverse columns can make the total ratio conductor large.
Such examples explain the additional sector being removed; no lower
bound or asymptotic for its contribution is assumed.

There is also unused room in the previous total-conductor cutoff. Write
\(R_0(\delta)=9/8-23\delta/20\) for the manuscript's assumed row-count
exponent, and set

\[
 \tau_0(\delta,m)=2\delta\left(m+\frac{23}{20}\right)
                   -\frac14-\frac9{12500},
 \qquad V_{\rm tot}=U^{\tau_0(\delta,m)}.
 \tag{10a}
\]

Then

\[
 R_0(\delta)+\frac{\tau_0(\delta,m)}2=K-\gamma,
 \qquad
 \frac{2614}{3125}\le\tau_0\le\frac{14191}{12500}.
 \tag{10b}
\]

Both extrema follow from monotonicity in \(\delta,m\). In particular,
\(\tau_0\ge0.83648>4/5\). The existing elementary total-column
pair count therefore bounds every tuple sector with total ratio
conductor at most \(V_{\rm tot}\) by
\(O_\epsilon(U^{K-\gamma+\epsilon}\mathcal H^{A_0})\), retaining
any further tuple restrictions. This uses only the existing coarse
count, not the sharper application-specific exponent \(R^*\). The
upper endpoint exceeding one is harmless: the column-pair conductor
is not bounded by the original physical row scale.

## 4. Intersection subtraction and the new remaining sum

A total-conductor cutoff cannot be inserted inside (5) while claiming
that its inverse/prime expansion is still positive. The passage to the
original \(T_{\rm large}\) therefore requires an explicit subtraction.

For this comparison only, let \(A_{\rm pl}(V)\) denote (7) with
the further restriction \(k\ne k'\). Bound (8) still holds for it
by (3). Thus \(P_{\rm low}(V)\) is \(A_{\rm pl}(V)\) plus the
previously controlled whole plain diagonal.

Let \(I(V)\) be the fully expanded tuple contribution on
\(\mathcal C_+\) with

\[
 k\ne k',\qquad\mathrm Nf_{\rm pl}(k,k')\le V,
 \qquad\mathrm Nf(n(\tau),n(\tau'))\le V_{\rm tot}.
\]

Its coefficients and its total-ratio kernel are exactly those of the
manuscript. Its elementary absolute total-column estimate gives

\[
 |I(V)|\ll_\epsilon
 U^{K-\gamma+\epsilon}\mathcal H^{A_0},
 \tag{11}
\]

uniformly in \(V\), by (10b), since the additional plain-pair
restriction can only decrease that positive tuple majorant. Therefore
the tuple sector having total ratio conductor greater than
\(V_{\rm tot}\) and \(\mathrm Nf_{\rm pl}\le V\) is
**exactly** \(A_{\rm pl}(V)-I(V)\). This identity is what permits
(8) to remove that sector from the retained total-conductor sum.
The extra annulus \(U^{4/5}<\mathrm Nf\le V_{\rm tot}\) of the
original \(T_{\rm large}\) is itself bounded by the same elementary
total-column estimate (10b).

Define the new exact remaining sum

\[
\begin{split}
 T_{\rm joint}=\frac1X
 \sum_{\substack{\tau,\tau'\\k\ne k'\\
       \mathrm Nf(n(\tau),n(\tau'))>V_{\rm tot}\\
       \mathrm Nf_{\rm pl}(k,k')>V_{\rm pl}}}
 b(\tau)\overline{b(\tau')}
 \mathcal K_{\mathcal C_+}
       \bigl(c(n(\tau),n(\tau'));E(n(\tau),n(\tau'))\bigr).
\end{split}
\tag{12}
\]

The strengthened reduction is

\[
 \sum_{u\in\mathcal C}|M_r(u)S_m(u)Q_I(u)|^2
 =\operatorname{Re}T_{\rm joint}
  +O_\epsilon\!\left(U^{K-1/6250+\epsilon}\mathcal H^{A_0}\right).
 \tag{13}
\]

Here is a direct proof that needs no overlap subtraction. First remove
\(\mathcal C_-\), whose positive contribution already has the
\(K-\gamma\) bound. On \(\mathcal C_+\), expand only the plain
factor and remove the entire \(P_{\rm low}(V_{\rm pl})\), bounded
by (8)--(10). Expand the remaining high-plain-conductor contribution
in all inverse and physical prime variables, and remove its
total-conductor part \(\mathrm Nf\le V_{\rm tot}\) by the
existing absolute tuple majorant and (10b). This leaves exactly (12).
Since \(V_{\rm pl}\ge1\), its plain-conductor condition already
implies \(k\ne k'\). These three controlled terms establish (13)
with the same error scale. The preceding intersection subtraction is
needed only when comparing to the old \(T_{\rm large}\); it also
explains why a conductor-truncated inverse norm was never positively
majorized.
One may instead choose any total cutoff \(U^\tau\) with
\(4/5\le\tau\le\tau_0\); all these conclusions remain valid.
In particular, retaining the old total cutoff \(U^{4/5}\) while
adding only the plain-conductor restriction is a special case.

Every pair region in (7), (11), and (12) is invariant under swapping
the two indices. The coefficients and kernels become complex
conjugates under that swap, including their zero masks. Consequently
the complete signed sums are real. They need not be nonnegative.
Equation (13), with positivity only for its left side, bounds the
negative part of \(T_{\rm joint}\) by the smaller error.

It follows that proving

\[
 \operatorname{Re}T_{\rm joint}
 \le C_\epsilon U^{1+\delta m-1/5000+\epsilon}\mathcal H^{A_0}
 \tag{14}
\]

is sufficient for the desired mixed input, and equivalent to it at
this scale under the existing assumptions. A modulus bound for the
**whole** remaining sum also suffices. No sum of the absolute values
of its individual tuple contributions is asserted.

## 5. Uniformity and what remains open

These identities use fixed permitted separating parameters and the
actual coefficient arrays. Their constants depend on the allowed
annuli, seminorms, arithmetic data, bounded slot count and strict marked
inverse margins. The pair count is independent of heights; the profile
and inverse-moment bounds have the same fixed polynomial height costs
as before. The required derivative profiles are handled by the same
fixed-parameter argument followed by the source's positive-norm
Sobolev procedure. Assigning unrelated profiles inside a rowwise
expansion would not yield (7).

The new bound applies with the sharp selector and all original masks.
It covers the complete inverse/prime cross terms associated with
small plain-ratio conductor and, via the explicit intersection
subtraction, a new sector of the previously retained large-total-
conductor sum. It does not estimate the remaining sector in which
both conductors are large. In particular, it supplies no uniform
\(1/5000\) saving for the complete mixed moment.

The current conditional candidate \(7/8-1/24000\) and the unproved
target \(7/8-1/20000\) remain distinct.
