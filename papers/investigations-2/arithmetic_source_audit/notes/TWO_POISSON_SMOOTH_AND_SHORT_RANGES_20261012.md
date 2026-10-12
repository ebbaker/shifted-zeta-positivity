# Two Poisson smooth norms and short ranges

12 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited session configuration. The serving variant
and configured reasoning effort are not exposed and are not inferred.
Internal LLM-assisted mathematical review; not independent specialist
validation or formal verification.

## Source and finding

Pinned source: the [5 October 2026 manuscript](https://github.com/openai/math/blob/fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/build/paper2.tex), `paper2.tex`, at
openai/math revision `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`,
SHA-256 `d9a8f15aa770cf883d0eabd2b775fad694ce20b44cba7928f5c0c9a6d8750d4d`.
Physical source lines are used below.

Scope: the full smooth and positivity passage in `prop:transfer`,
especially lines 2230–2683, the exclusion-removal comparison at lines
962–991, and the smooth/Mellin/recombination appendix, lines 3490–3650.
The arithmetic two-Poisson identities are retained as exact inputs
whose masks and domain consequences are checked here. The classical
lattice Poisson theorem, primitive Gauss-sum identity, and reciprocity
are imports; the estimates below are independent bookkeeping and
smooth-norm deductions from those inputs.

**Finding:** no unresolved gap was found in this part of the full
transfer. The two zero-frequency contributions are bounded without a
lower bound \(Y\ge1\). The original row masks remain in force until
positive enlargement. Every divisor-shifted child has column and
auxiliary scales at least one. Smooth separation preserves fixed
support intervals and gives exactly the derivative recurrence
\(m\mapsto4m+12\).

This does not by itself prove the arithmetic regrouping identities,
completed theta mean square, or final theorem. Those are separate
obligations. In particular, the nonempty-child lower bound relies on
the exact preimage cancellation producing \(f'\mid k'\); it would not
follow by taking absolute values before that regrouping.

## First Poisson masks finite rows and the first diagonal

The primitive row character after extracting the common squarefree
column \(C\) is \(\chi_{u_1}\overline{\chi_{u_2}}\), of conductor
\(u_1u_2\), and the common factor supplies \((k,C)=1\)
(lines 2274–2279). Its zero Fourier frequency is confined to
\(u_1=u_2=1\). The complete diagonal is bounded by

\[
|Z_1|\ll \frac{\mathcal H}{LF}
\sum_f^*\sum_C^*|W(N(C)/L)|^2
\ll_I\mathcal H\|W\|_\infty^2
\le\Sigma\|W\|_\infty^2.
\]

The auxiliary \(f\)-count is \(O(F)\); the supported column
\(C\)-count is \(O_I(L)\). Original masks can only reduce this
quantity. No squarefree Möbius cancellation is being used for this
diagonal.

After the paired Gauss conversion and Möbius expansion, the source
retains \((f,Ct)=1\), \((h,t)=1\), and \((C,t)=1\)
(lines 2293–2312). The coefficient

\[
p_y(n)=\mu(n)\xi_1(n)\mathbf1_{(n,t)=1}
\overline{\chi_n(y)}\chi_n(C)^4\chi_n(d)
\]

retains \((n,t)=1\) explicitly, while its zero-extended characters
supply the remaining column zeros. There is no remaining condition
that the two independent column indices be coprime.

For fixed \(C,d,t\), the row map is \(y=h f^2\). For each nonzero
\(y\), its multiplicity is bounded by the number of squarefree ideal
divisors \(f\) with \(f^2\mid(y)\). Primary generators make \(h\)
unique once \(f\) is specified, so units cause no further multiplicity.
The image lies in

\[
0<N(y)\le
\frac{4C_\Phi v^2L^2F^2N(d)}{\mathcal H N(C)^2}
\le Y_{C,d}
=\frac{c_I\Sigma LFN(d)}{\mathcal H N(C)^2},
\]

using \(\Sigma\ge LF\) and \(c_I\ge4C_\Phi v^2\)
(lines 2330–2338). All such image norms are bounded by a fixed
power of \(D\), so the divisor multiplicity costs an arbitrarily
small power \(D^\eta\). The inequality \(\Phi\ge1\) on \([0,1]\)
then dominates the finite mapped-row mean square by the positive form
\(\mathcal Q_{\xi_1}(U)\).

If \(Y_{C,d}<1\), there are no nonzero mapped rows in this part of
the argument. The positive dominating form still includes \(y=0\);
this inclusion is legitimate. A point \(y=0\) in the original row
sum is not the same as the zero Fourier frequency introduced by the
second Poisson calculation.

## Smooth separation at the first stage

The first coupled kernel, lines 2318–2323, is supported in
\(I^2=[u,v]^2\) and satisfies

\[
\|\mathscr K_h\|_{C^q(I^2)}
\ll_{I,\Phi,q}\|W\|_{C^q(I)}^2.
\]

All its arguments remain away from zero. The Fourier parameter
\(\mathcal H N(h)N(C)^2/(L^2N(d))\) is uniformly bounded on
the displayed original frequency range. Thus the chain rule introduces
only constants depending on the fixed support and cutoff, rather than
powers of moving scales.

The smooth-mean-square lemma is applied to the **finite** row set
\((C,d,t,f,h)\). The signs \(\mu(d)\mu(t)\) have magnitude at most
one, and the row weights \(w_{C,d}\) are nonnegative. Both column
families have the same common-test bound supplied by the positive
form. The lemma's logarithmic Fourier coefficient bound is pointwise
and common over all those rows; it does not replace a common test by an
arbitrary independent test in each row.

The hypothesis
\(\mathcal Q_{\xi_1}(U)\le M\|U\|_{C^j(I_*)}^2\), where
\(I_*=[u/2,2v]\), therefore gives a cost of \(2j+4\)
derivatives of the first kernel. The fixed box \(I\) is strictly
inside \(I_*\), so its common Mellin tests can be cut off smoothly
without changing the expression. Hence

\[
\mathcal A(W)\ll D^{\varepsilon_0}(\Sigma+M)
\|W\|_{C^{2j+4}(I)}^2.
\]

The infinite \(y\)-sum in \(\mathcal Q\) is only the positive
dominating form, not the row set to which this finite-row smooth
lemma is directly applied.

## Second Poisson for every positive Y

The second Poisson identity is stated for arbitrary \(\ell,Y>0\),
lines 2353–2422. For fixed \(\ell\), the input column sum is finite;
its coefficients as functions of \(y\) are bounded. Thus the original
\(y\)-sum converges absolutely by the Schwartz decay of
\(\Phi(N(y)/Y)\), even when \(Y<1\).

The compact Fourier support gives a finite output frequency range:

\[
N(h)\le\frac{C_\Phi b^2\ell^2N(e)}{YN(g)^2},
\]

where \([a,b]=I_*\). For fixed positive \(Y\), this is finite
regardless of its size; no assumption \(Y\ge1\) is used.
The second zero-frequency term is exactly

\[
Z_2=Y\widehat\Phi(0)
\sum_{(g,Ct)=1}^* |U(N(g)/\ell)|^2
\prod_{p\mid g}(1-N(p)^{-1}),
\]

and therefore

\[
|Z_2|\ll_{I_*,\Phi}Y\ell\|U\|_\infty^2.
\]

If \(b\ell<1\), the column and diagonal sums are empty. Otherwise
\(\ell\ge1/b\), and ideal counting \(O_{I_*}(\ell)\)
proves the displayed bound. In the actual positive form, the outer
domain already imposes \(\ell\ge1/(2v)\).
Thus this bound remains valid for short column scales and small \(Y\).

One must not bound the entire lattice row sum by \(O(Y)\) when
\(Y<1\): its \(y=0\) term can have size one. The source only uses
the \(Y\ell\) bound for the zero **Fourier** term and keeps every
nonzero Fourier frequency. This is the correct distinction.

## Retaining the domain through regrouping

The second identity retains \((g,Ct)=1\), \((w,gCth)=1\)
and the residual coefficient mask. Set

\[
r=tg/e,\qquad f'=Cew,\qquad k'=deh.
\]

Then \(r,f'\) are disjoint squarefree ideals, and the column
coefficient is precisely

\[
a_{\xi'}(n)\mathbf1_{(n,r)=1}
\chi_n(k')\chi_n(f')^4.
\]

The scale and exterior coefficient simplify to

\[
X'_0=\frac{L}{N(r)N(f')},\qquad
w_{C,d}\frac{Y_{C,d}N(g)}{N(e)\ell}
=\frac{c_I\Sigma N(r)}{L^2}.
\]

The coupled Fourier parameter becomes

\[
\frac{Y_{C,d}N(h)N(g)^2}{N(e)\ell^2}
=\frac{c_I\Sigma F N(k')N(r)^2}{\mathcal H L}.
\]

These expressions depend only on the regrouped indices; their moving
preimages have the same weight and kernel. The original support
restriction \(N(gw)\le2v\ell\) becomes
\(N(r)N(f')\le2vL\). Any preimage satisfying a nonzero common
kernel also has \(N(Ct)\le N(r)N(f')\le2vL\), so the outer
positive-form domain does not remove a nonzero preimage. This is why
the source defines \(\mathcal Q\) with the full outer domain
(lines 2253–2261), rather than imposing an inherited first-Poisson
Fourier-support restriction on that domain.

The frequency bound becomes

\[
0<N(k')\le
\frac{4C_\Phi v^2}{c_I}
\frac{\mathcal HL}{\Sigma F N(r)^2}
\le\frac{\mathcal HL}{\Sigma F N(r)^2}.
\]

The exact preimage cancellation gives \(f'\mid k'\), with all
nonzero frequencies retained. This cancellation must be performed
before taking absolute values (lines 2550–2582). A separate arithmetic
audit checks the local cancellation itself; its support consequences
are essential here.

## Every divisor-shifted child is admitted

In a dyadic block \(R\le N(r)<2R\),
\(F'\le N(f')<2F'\), define

\[
X'=\frac{L}{RF'},\qquad
\Sigma'=\frac{L}{R},\qquad
\mathcal H'=\frac{\mathcal HL}{\Sigma F R^2}.
\]

Only \(r\)'s for which an original nonzero term exists are retained.
For each such \(r\),

\[
F'\le N(f')\le N(k')
\le\frac{\mathcal HL}{\Sigma F N(r)^2}.
\]

Consequently \(\mathcal H'\ge1\). For every divisor \(j\mid r\),

\[
\frac{X'}{N(j)}
\ge\frac{\Sigma F N(r)^2}{\mathcal H R N(j)}
\ge\frac{\Sigma F}{\mathcal H}\ge1,
\]

because \(N(r)\ge R\), \(N(j)\le N(r)\), and
\(\mathcal H\le\Sigma\) (lines 2590–2601).

**The retained set of \(r\)'s is fixed before enlarging the
\(f',k'\)-ranges.** The source states this explicitly at lines
2623–2625. Enlarging \(r\) first would invalidate this lower bound;
no such enlargement occurs.

Exclusion removal changes only

\[
(X',F')\longmapsto(X'/N(j),F'N(j)),\qquad j\mid r.
\]

It preserves \(\mathcal H'\) and \(\Sigma'\); the new column scale
is at least one by the preceding argument, and the new auxiliary
scale is at least one. The common test function is unchanged:
substituting \(n=jm\) gives
\(V(N(m)/(X'/N(j)))\), so no divisor-dependent derivative cost
is introduced.

All three transfer inequalities are preserved:

\[
\frac{\mathcal H'}{\Sigma'}=
\frac{\mathcal H}{\Sigma FR}\le\frac{\mathcal H}{\Sigma},
\qquad
\Sigma'\le L,\qquad
\mathcal H'\le\frac{\mathcal HL}{\Sigma F}.
\]

Since each child scale is at least one, \(\Sigma'\le L\) also
bounds its individual column and auxiliary scales by \(D^{C_0}\).
Moreover \(\mathcal H'\le L/F\le D^{C_0}\). Hence all
divisor factors and the ambient small-power constants remain uniform.

If the supremum defining \(S_m\) is empty, there can be no retained
nonzero block. The second form consists only of its bounded
zero-frequency contribution. This covers the corresponding short-range
case without an inadmissible child.

The supremum is finite before any recursive energy estimate is applied.
For every admitted normalized test, ideal and row counting give
\(\mathcal E(\mathcal H',X'',F'')\ll_{I'}\mathcal H'X''\),
so \(\mathcal E/\Sigma'\ll_{I'}\mathcal H'/F''\le\mathcal H\).
Here all scales are at least one, and
\(\mathcal H'\le\mathcal HL/(\Sigma F)\le\mathcal H\).
Thus the finite constant required by the first-transfer hypothesis
is supplied without a recursive assumption about operator norms.

## Rescaled support and the second smooth step

The ratio of common and individual column scales is

\[
s=\frac{X'}{X'_0}
=\frac{N(r)N(f')}{RF'}\in[1,4).
\]

The old column kernel is supported in \(I_*^2=[u/2,2v]^2\).
After the substitution \(x_{\rm old}=s x_{\rm new}\),
its support is contained in

\[
[u/8,2v]^2\subset\operatorname{int}([u/16,4v]^2).
\]

Thus the common child test interval is exactly
\(I'=[u/16,4v]\). To apply the smooth lemma formally, use the
kernel box \([u/8,2v]\) as its smaller interval and \(I'\)
as its larger test interval.

For retained nonzero kernels the original Fourier parameter is
at most \(4C_\Phi v^2\). All old and rescaled column arguments
lie in fixed intervals away from zero, and \(1\le s<4\).
The chain rule therefore gives

\[
\sup_{r,f',k'}
\|\mathcal K_{r,f',k'}\|_{C^{2m+4}(I'^2)}
\ll_{I,\Phi,m}\|U\|_{C^{2m+4}(I_*)}^2.
\]

Alternatively, compact support and Schwartz derivative bounds for
\(\widehat\Phi\) give the same uniform bound for all Fourier
parameters, including zero kernels. There is no power of \(Y^{-1}\)
or of a divisor in this norm.

For each retained \(r\), exclusion removal and the supremum \(S_m\)
give the common-test mean-square bound

\[
\sum_{f',k'}\left|
\sum_n^*a_{\xi'}(n)\mathbf1_{(n,r)=1}
\chi_n(k')\chi_n(f')^4V(N(n)/X')
\right|^2
\ll D^\delta(\Sigma')^2S_m\|V\|_{C^m(I')}^2.
\]

The two factors of \(\Sigma'\) are correct: one reverses energy
normalization, and one comes from the target in \(S_m\).
The restriction \(f'\mid k'\) and the original masks may now be
dropped inside this nonnegative common-test bound, while retained
\(r\) stays fixed.

There are \(O(R)\) retained ideals \(r\), and their exterior
factor \(N(r)\tau_{\rm div}(r)\) costs at most \(R D^\delta\).
The smooth lemma with row index \((r,f',k')\) therefore bounds a
dyadic block by

\[
D^{2\delta}\frac{\Sigma R}{L^2}
R(\Sigma')^2 S_m\|U\|_{C^{2m+4}(I_*)}^2
=D^{2\delta}\Sigma S_m\|U\|_{C^{2m+4}(I_*)}^2.
\]

The exact cancellation of dyadic lengths is
\((\Sigma R/L^2)R(L/R)^2=\Sigma\).

## Second diagonal and all summation losses

The total second zero-frequency contribution uses the exact identity

\[
w_{C,d}Y_{C,d}\ell
=\frac{c_I\Sigma}{N(C)^2N(t)}.
\]

Summing \(d\mid C\), dropping harmless coprimality restrictions,
and using ideal counting gives

\[
|\mathcal Z|
\ll\Sigma\|U\|_\infty^2
\left(\sum_C\frac{\tau_{\rm div}(C)}{N(C)^2}\right)
\left(\sum_{N(t)\le2vL}\frac1{N(t)}\right)
\ll D^\delta\Sigma\|U\|_\infty^2.
\]

The first ideal series converges; the second is
\(O_I(\log(2+L))\). This deduction uses only \(Y_{C,d}>0\),
as the source explicitly notes at lines 2653–2665.

Every nonzero regrouped term has \(N(r),N(f')\le2vL\),
so there are \(O_{I,C_0}((\log(2D))^2)\) dyadic blocks.
The remaining finite ray-character sum has fixed size.
Taking \(\delta=\varepsilon_0/4\), the displayed block loss
\(D^{2\delta}\), logarithmic block count, and diagonal
logarithm fit within \(D^{\varepsilon_0}\).
The divisor exponents are chosen relative to the fixed polynomial
range before these estimates are applied.

No infinite Fourier-row or dyadic-block summation is silently replaced
by an unbounded supremum. In the actual parameter ranges,
\(Y_{C,d}\gg_I F N(d)/L\gg_I D^{-C_0}\), since
\(\mathcal H\le\Sigma\) and \(N(C)\le2vL\).
The second Fourier frequencies are consequently bounded by a fixed
power of \(D\), even when \(Y_{C,d}<1\). The input \(y\)-sum
remains infinite but absolutely convergent by Schwartz decay and is
handled by the exact Poisson identity.

## Derivative recurrence and conclusion

The second-transfer lemma gives the common-test norm order
\(j=2m+4\). Substituting it into the first-transfer lemma gives

\[
2j+4=2(2m+4)+4=4m+12.
\]

Taking the two lemmas with losses \(D^{\varepsilon/4}\)
gives an overall loss at most \(D^{\varepsilon/2}\), within
the proposition's stated \(D^\varepsilon\) budget
(lines 2672–2682). Therefore the inspected smooth and positivity
steps return the precise energy class with

\[
\mathcal A(W)\ll
D^\varepsilon\Sigma(1+S_m)\|W\|_{C^{4m+12}(I)}^2.
\]

Support expansion is fixed and explicit, masks are retained until
permitted positive enlargement, and all children satisfy the three
scale inequalities. The recurrence itself is a finite derivative
calculation; its use in canonical induction and termination is
reviewed separately.

The [arithmetic ledger](TWO_POISSON_ARITHMETIC_LEDGER_20261012.md) checks the paired conversions and full signed preimage count. The [return and termination note](TWO_POISSON_RETURN_AND_TERMINATION_20261012.md) checks every cube range and the finite canonical induction. The [combined review](../reviews/TWO_POISSON_TRANSFER_REVIEW_20261012.md) records the proposition scope and next obligation.
