# Fixed scale contraction and a strict variance improvement

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.

This note gives a sufficient condition for quasi-RH to imply RH in the
prepared-prime variance program. The iteration argument is proved below;
the required arithmetic inequality is not proved. A contraction between
successive fixed multiplicative scales would give the missing power gain.
An improved constant in a single asymptotic upper bound would not suffice.

## The normalized energy

Use the fixed real probe and prime response of the
[prime-variance manuscript](../../../prime-variance-exponents/manuscript.tex),
and write

\[
E_\delta(X)=X^{-2-\delta}\mathcal V_g(X),\qquad
\mathcal V_g(X)=\int_X^{2X}|V_g(x)|^2\,dx.
\tag{1}
\]

An admissible exponent \(\delta\in[0,1]\) means that \(E_\delta\) is
bounded for all sufficiently large real \(X\). The local fixed-exponent
theorem identifies the least admissible exponent \(\delta_*\) and says
that it is itself admissible. These are imported, internally reviewed
project results, not an independent verification of that manuscript here.

## A sufficient arithmetic inequality

Suppose, for a fixed positive admissible \(\delta\), that there are
\(b>1\), \(0<q<1\), \(\eta>0\), \(C>0\), and \(X_0>1\) such that

\[
E_\delta(X)\le qE_\delta(X/b)+CX^{-\eta}
\qquad(X\ge bX_0).
\tag{2}
\]

All parameters may depend on \(\delta\). The inequality concerns the
actual response at the smaller scale, not an arbitrary big-O constant.

**Proposition.** Put \(\kappa=\log(1/q)/\log b\). Then

\[
E_\delta(X)=
\begin{cases}
O(X^{-\min(\kappa,\eta)}),&\kappa\ne\eta,\\
O(X^{-\eta}\log X),&\kappa=\eta.
\end{cases}
\tag{3}
\]

In particular, any \(0<\sigma<\min(\delta,\kappa,\eta)\) gives the
strict improvement \(\mathcal V_g(X)=O(X^{2+\delta-\sigma})\).

**Proof.** For \(n=\lfloor\log_b(X/X_0)\rfloor\), set
\(Y=X/b^n\in[X_0,bX_0)\). Iterating (2) gives

\[
E_\delta(X)\le q^n E_\delta(Y)
+CX^{-\eta}\sum_{j=0}^{n-1}(qb^\eta)^j.
\tag{4}
\]

The initial compact interval has bounded energy because the original
prime response is continuous and locally a finite sum. Also
\(q^n=O(X^{-\kappa})\). The three cases of the geometric sum prove (3).
In the equality case, \(\log X=O(X^\epsilon)\) for any fixed
\(\epsilon>0\), which gives the stated strict improvement. This works
for all real \(X\), not only powers of \(b\). \(\square\)

**Conditional quasi-RH implication.** If (2) can be proved for every
positive admissible \(\delta<1\), then quasi-RH implies RH. Otherwise
\(0<\delta_*<1\), and applying the proposition at the attained optimum
\(\delta_*\) contradicts its minimality. No uniform choice of the
constants as \(\delta\downarrow0\) is needed.

A perturbation \(\epsilon(X)E_\delta(X)\) on the right is harmless if
\(\limsup\epsilon(X)<1-q\): it can be absorbed with a new contraction
constant below one. An unspecified \(o(1)\) error with no power rate in
place of \(CX^{-\eta}\), however, need not give a power improvement.

## An exact signed formulation for the actual primes

For \(1\le u\le2\), let

\[
F_X(u)=X^{-(1+\delta)/2}V_g(Xu),\qquad
D_X(u)=F_X(u)-F_{X/b}(u).
\tag{5}
\]

Then \(\|F_X\|_{L^2[1,2]}^2=E_\delta(X)\), and the exact identity

\[
E_\delta(X)-E_\delta(X/b)
=2\Re\langle D_X,F_{X/b}\rangle+\|D_X\|_2^2
\tag{6}
\]

shows that (2), with \(q=1-c\), is equivalent to

\[
2\Re\langle D_X,F_{X/b}\rangle+\|D_X\|_2^2
\le -c\|F_{X/b}\|_2^2+CX^{-\eta}.
\tag{7}
\]

Here the profiles are explicitly finite arithmetic sums:

\[
D_X(u)=X^{-(1+\delta)/2}
\sum_{n\ge2}\Lambda(n)
\left[w\!\left(\frac n{Xu}\right)
-b^{(1+\delta)/2}w\!\left(\frac {bn}{Xu}\right)\right].
\tag{8}
\]

Each support is retained in full; no continuum, cutoff, or prime-power
term has been removed. Formula (7) isolates the signed correlation that
would need an arithmetic estimate. Cauchy--Schwarz alone gives no negative
margin. This reformulation does not claim that (7) is easier to prove.

## Why the scale of the contraction matters

Replacing \(X/b\) by \(X^a\), \(0<a<1\), changes the iteration depth
from order \(\log X\) to order \(\log\log X\). For example,

\[
E(X)=(\log X)^{-r},\quad
q=a^r,
\qquad E(X)=qE(X^a)
\tag{9}
\]

holds exactly, yet \(E(X)\) has no fixed power decay. The analogous
factor-scale feedback in the mixed Mertens identity therefore needs an
additional power gain or a stronger form of self-improvement. See the
[arithmetic feedback note](3_ARITHMETIC_FEEDBACK_AND_RESONANCE_20261008.md).

## A mode check before attempting a proof

For the abstract pure complex mode \(V(x)=x^{(1+\delta)/2+i\gamma}\),
\(E_\delta(X)=\int_1^2u^{1+\delta}\,du>0\) is constant. Thus (2) cannot
hold with \(q<1\) and a power-decaying remainder. This is an elementary
diagnostic, not an actual-prime counterexample. It makes explicit that
the proposed estimate must exclude a persistent boundary mode.

The [spectral-edge note](2_SPECTRAL_EDGE_AND_LOG_SAVINGS_20261008.md) explains
the further obstacle when the optimal boundary is approached only at
unbounded zero height. A finite list of frequency checks is insufficient
for (2).

The next bounded task is to test candidate arithmetic decompositions
against (6)--(8), keeping the signed term and every remainder. Any argument
that replaces the cross term by its absolute value, supplies only a
logarithmic gain, or preserves each hypothetical zero mode with multiplier
one has not yet established the required contraction.
