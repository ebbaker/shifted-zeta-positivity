# Removing the diagonal and the large transformed cofactor

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Same-model analysis and cross-review are internal checks, not independent
specialist validation.

**Correction and continuation, 8 October 2026.** Two missing conjugations
in the definitions of the Gauss coefficient and transformed profile have
been repaired below, following a rendered-PDF and TeX-source check. The
[source audit and exact core involution](SHORT_FAMILY_CORE_INVOLUTION_20261008.md)
record the error and its scope. The prior absolute bounds survive, while
the exact identity requires the corrected definitions. The
[latest continuation](SHORT_FAMILY_CONTINUATION_20261008.md) also removes
a larger overlap sector and identifies an actual prime-column obstruction.

## Outcome and verification scope

The small-cofactor obstruction in the
[short-family refinement](SHORT_FAMILY_DESCENT_REFINEMENT_20261008.md)
can be sharpened in two ways.

First, the source's proposed positive dual estimate cannot simply be
extended to its long-dual-row range: an allowed test isolating the unit
ideal gives an explicit counterexample with the actual source coefficients.
Second, after removing the **entire original column diagonal**, a second
Poisson summation proves rapid decay for a substantial complementary
sector. It keeps the actual coupled smooth kernel and every zero mask.

For \(H=D^h\), \(0<h<1\), and a fixed small buffer \(\eta>0\), the
remaining new signed estimate can be restricted to

\[
Nb<D^{1-h+\eta},\qquad
(Nf)^2N(m_1,m_2)<H D^{2\eta},\qquad m_1\ne m_2.
\tag{1}
\]

In particular \(Nf<D^{h/2+\eta}\). At \(h=2/3\), both displayed
cofactor exponents are \(1/3\), before their explicit buffers. The
positive dual bound is replaced by a signed quadratic form with its
diagonal removed; the new estimate for (1) remains open.

The actual source is the
[October 5 paper](https://github.com/openai/math/blob/main/preprints/The-Quasi-Riemann-Hypothesis-October-5-2026/paper2.pdf),
local PDF SHA-256
f919b57829b178c8e60e7c17b018cf773e7907cf642ef5a3347d8a826e8dbf18.
Sections 4.1--4.4, Proposition 5.1, and the induction step were inspected.
The finite Gauss/reciprocity identities of Lemma 4.1 and the existing
dual moment remain imported inputs. No theta-transform proof or Lean
verification was replayed. The second-Poisson estimate below uses the
standard primitive finite-character Gauss identity and Schwartz decay,
not a new arithmetic mean square.

## 1. The actual smooth moment and its full diagonal

Retain the notation, fixed character \(\nu\), excluded primes \(S\),
and smooth annular profile \(W\) from the preceding note. Thus

\[
A_u(D)=\sum_{(n,S)=1}\mu_K(n)\nu(n)\chi_n(u)W(Nn/D).
\tag{2}
\]

Choose a fixed nonnegative radial Schwartz function
\(\Phi(Nu/H)\), at least one on \(Nu/H\le1\), whose radial Fourier
transform \(\widehat\Phi\) is smooth and compactly supported, as in
the source. Define the normalized smoothed moment

\[
\mathfrak M(D,H)=D^{-1}\sum_{u\in\mathcal O}
\Phi(Nu/H)|A_u(D)|^2.
\tag{3}
\]

For sufficiently large \(D\), the unit column is outside the annular
support of \(W(Nn/D)\); consequently its zero-row convention causes
no issue. The nonnegative weight makes (3) an upper bound, after
multiplication by \(D\), for the original \(0<Nu\le H\) moment.

Remove \(n_1=n_2\) in the expansion **before** taking Poisson sums.
Its entire contribution is

\[
\mathfrak D(D,H)=D^{-1}\sum_n
\mu_K(n)^2|\nu(n)W(Nn/D)|^2
\sum_u\Phi(Nu/H)\mathbf1_{(u,n)=1}
\ll_{\nu,S,W,\Phi} H.
\tag{4}
\]

This uses ideal counting and lattice counting, since \(H\ge1\).
It includes all Fourier frequencies of that diagonal, not only the
zero-frequency term \(Z\) of the source. Nothing in (4) presumes
Möbius cancellation.

The remaining original pairs have \(n_1\ne n_2\). In the source's
variables \(n_j=gz_j\), followed by \(z_j=vm_j\), this is exactly
\(m_1\ne m_2\). The changes of variables preserve that exclusion.
The primitive ratio character in the first Poisson sum is then
nonprincipal, so its zero frequency vanishes.

## 2. Exact transformed form after removing the diagonal

Write \(W_0(t)=t^{-1/2}\overline{W(t)}\). The source's Lemma 4.1 converts the
Möbius coefficients, on squarefree ideals, to

\[
a_\xi(n)=\overline{\alpha(n)}\gamma_2(n)\xi(n),\qquad |a_\xi(n)|=1,
\tag{5}
\]

for a finite fixed collection of ray characters \(\xi\). Its explicit
functions and Gauss normalization are retained, rather than replaced
by arbitrary divisor-bounded coefficients.

Repeating only the finite algebra of Section 4.4, with \(m_1\ne m_2\)
retained, gives

\[
\mathfrak M-\mathfrak D=\sum_\xi c_\xi\,\mathfrak S_\xi^\circ,
\tag{6}
\]
\[
\begin{split}
\mathfrak S_\xi^\circ={H\over D^2}
\sum_{\substack{b,f\ {\rm squarefree}\\(b,f)=1}}^*
 \mu_K(f)Nb
\sum_{\substack{m_1,m_2\ {\rm squarefree}\\
 (m_1m_2,b)=1,\ m_1\ne m_2}}^*
&a_\xi(m_1)\overline{a_\xi(m_2)}
 \chi_{m_1}(f)^4\overline{\chi_{m_2}(f)^4}\\
{}\times W_0(N(bfm_1)/D)
 \overline{W_0(N(bfm_2)/D)}
&\,\mathcal K_f(m_1,m_2).
\end{split}
\tag{7}
\]

Every starred ideal is prime to \(S\) and has its fixed primary
generator. The finite coefficients \(c_\xi\) depend only on the
original fixed arithmetic data. Their convention is explicitly
\[
\overline{\nu(t)}G_{\rm ray}(t^{-1})=\sum_\xi c_\xi\xi(t),
\]
where \(G_{\rm ray}\) is the fixed ray-group function in source Lemma 4.1.
The **complete** dual-row kernel is

\[
\mathcal K_f(m_1,m_2)=
\sum_{k\in\mathcal O\setminus\{0\}}
\chi_{m_1}(k)\overline{\chi_{m_2}(k)}
\widehat\Phi\!\left({H Nk\over (Nf)^2Nm_1Nm_2}\right).
\tag{8}
\]

The factors at \(f\) retain their zeros: they enforce
\((m_1m_2,f)=1\). There is no extra artificial truncation of \(k\)
in (8); finiteness comes from the original support of
\(\widehat\Phi\). The \(b\)-mask is retained separately.

The source bijection is \(b=g/e,\ f=ev,\ k=eh\), with inverse
\(e=(f,k),\ v=f/e,\ g=be,\ h=k/e\). It does not require a new
coprimality between \(m_1,m_2\). Unlike the deep moment theorem,
these Poisson and algebraic identities do not require \(H>D\):
Lemma 4.2 assumes only \(H>0\). Here all sums at the finite-algebra
stage are finite, and the Schwartz lattice sums converge absolutely.
Thus (6)--(8) may be used for \(H=D^h\), subject to the stated
finite Gauss/reciprocity source inputs.

## 3. Why the old positive target cannot hold in general here

The source's positive dual mean square is

\[
\mathcal E(R,X,F;\xi,V)=\frac1{XF}
\sum_{F\le Nf<2F}^{*}
\sum_{0<Nk\le R}
\left|\sum_n^* a_\xi(n)\chi_n(k)\chi_n(f)^4V(Nn/X)\right|^2.
\tag{9}
\]

Take \(X=1\) and a fixed smooth profile \(V\), supported in
\((1/2,3/2)\), with \(V(1)=1\). The only contributing integral ideal
is the unit ideal. Since \(a_\xi(1)=1\), (9) becomes exactly

\[
\mathcal E(R,1,F;\xi,V)
=F^{-1}\#\{f:\ F\le Nf<2F,\ f\ {\rm squarefree},\ (f,S)=1\}
\ \#\{k:\ 0<Nk\le R\}\asymp R.
\tag{10}
\]

The lower counts use the positive density of squarefree ideals outside
fixed \(S\) and elementary lattice counting. These are the actual
coefficients; no Möbius-sign-canceling column weight was added.

At \(b=1,\ F=D,\ H=D^h\), the source range is

\[
R\asymp D^{2-h},\qquad \Sigma=XF=D.
\tag{11}
\]

For any fixed \(h<1\), (10) contradicts a uniform
\(\mathcal E\ll D^\varepsilon\Sigma\) estimate for
\(\varepsilon<1-h\). This is a coefficient-level obstruction to
extending that **positive** theorem to the needed long-row range.
It is not a lower bound against the desired original Möbius moment.
The offending unit contribution disappears from (7), because its
column diagonal has already been removed.

## 4. A second Poisson sum controls large \(f\) and large common factors

Fix \(m_1\ne m_2\) in (7), and set

\[
\mathfrak g=(m_1,m_2),\quad G=N\mathfrak g,\qquad
\mathfrak c=m_1m_2/\mathfrak g^2,\quad
Q=N\mathfrak c={Nm_1Nm_2\over G^2}.
\tag{12}
\]

The primitive ratio character \(\psi_{\mathfrak c}\) has local
exponent \(+1\) at primes of \(m_1/\mathfrak g\) and \(-1\) at
primes of \(m_2/\mathfrak g\). These primes are outside \(S\), where
the sextic residue characters have exact order six. Thus its conductor
is exactly \(\mathfrak c\), it is nonprincipal, and
\((\mathfrak c,\mathfrak g)=1\). The exact zero convention is

\[
\chi_{m_1}(k)\overline{\chi_{m_2}(k)}
=\psi_{\mathfrak c}(k)\mathbf1_{(k,\mathfrak g)=1}.
\tag{13}
\]

Cancellation of phases on the shared primes does not erase this mask.
Put

\[
R_{12}={(Nf)^2Nm_1Nm_2\over H},\qquad
Z={(Nf)^2G\over H}.
\tag{14}
\]

Apply the masked Poisson formula, source Lemma 4.2, to (8), with
weight \(\widehat\Phi\), primitive character \(\psi_{\mathfrak c}\),
and excluded ideal \(\mathfrak g\). The Fourier transform of
\(\widehat\Phi\), denoted \(\widetilde\Phi\), is a fixed radial
Schwartz function. All nonzero frequencies for a divisor
\(d\mid\mathfrak g\) have the scale

\[
t_d={R_{12}\over Nd\,Q}
={(Nf)^2G^2\over H\,Nd}\ge {(Nf)^2G\over H}=Z.
\tag{15}
\]

There is no zero-frequency term, since \(\psi_{\mathfrak c}\) is
nonprincipal. Its normalized Gauss sum has absolute value one.
For every \(A>1\) and \(t\ge1\), lattice counting and Schwartz decay
give

\[
\sum_{\ell\in\mathcal O\setminus\{0\}}
|\widetilde\Phi(tN\ell)|\ll_{\Phi,A}t^{-A}.
\tag{16}
\]

Consequently, for \(Z\ge1\),

\[
\boxed{\quad
|\mathcal K_f(m_1,m_2)|
\ll_{\Phi,A}
\tau(\mathfrak g)\,{R_{12}\over\sqrt Q}\,Z^{-A}.
\quad}
\tag{17}
\]

Indeed each divisor has Poisson prefactor
\(R_{12}/(Nd\sqrt Q)\), and \(Nd\ge1\), so summing (16)
proves (17). This intentionally crude bound suffices. It retains the
complete \(k\)-sum and all shared-prime masks. It does not rely on
positivity or cancellation in \(f\).

The useful sector is

\[
(Nf)^2G\ge H D^{2\eta},
\tag{18}
\]

where \(\eta>0\) is fixed. For any requested \(L>0\), the contribution
of (18) to (7) is \(O(D^{-L})\), after choosing \(A\) sufficiently
large in terms of \(L,\eta\) and paying fixed seminorms of \(\Phi,W\).

Here is an explicit total-cost check. In blocks \(Nb\asymp B\),
\(Nf\asymp F\), the physical support forces

\[
Nm_j\asymp X={D\over BF},\qquad
R_{12}\asymp {D^2\over HB^2}.
\tag{19}
\]

There are \(O(B)\) ideals \(b\), \(O(F)\) ideals \(f\), and
\(O(X^2)\) pairs. The weight outside the kernel is \(O(HB/D^2)\).
Use \(Q^{-1/2}\le1\), \(\tau(\mathfrak g)\ll_\epsilon D^\epsilon\),
and \(Z^{-A}\le D^{-2\eta A}\). The resulting block bound is

\[
\ll D^\epsilon {HB^2FX^2\over D^2}
{D^2\over HB^2}D^{-2\eta A}
=D^\epsilon {D^2\over B^2F}D^{-2\eta A}
\ll D^{2+\epsilon-2\eta A}.
\tag{20}
\]

The finitely many dyadic blocks cost only logarithms. When \(X\) is
bounded below by a fixed positive constant but less than one, replace
its count by \(O(1)\); (20) changes only by a fixed support constant.
This proves the asserted rapid decay.

Since \(G\ge1\), the entire sector \(Nf\ge H^{1/2}D^\eta\)
is controlled. The stronger form (18) also controls smaller \(f\)
when the two columns share sufficiently large factors.

## 5. Combining with the source's valid large-\(b\) range

Fix \(0<\eta<h/10\) and first treat the complete blocks

\[
Nb\ge D^{1-h+\eta}.
\tag{21}
\]

For these blocks the existing dual parameters satisfy

\[
{R\over\Sigma}\ll {D\over HB}\ll D^{-\eta}.
\tag{22}
\]

After absorbing fixed support constants, the source's Proposition 5.1
applies with \(\kappa=\eta/2\), with its original actual coefficients.
The \(b\)-mask removal in Lemma 4.4 preserves \(\Sigma=XF\).
The smooth-kernel argument from Section 4.4 therefore bounds the
**whole** quadratic block by \(O(H D^\varepsilon)\). The column
diagonal reintroduced in that positive-norm bound has the elementary
block cost

\[
{HB^2FX\over D^2}\,{D^2\over HB^2}
=FX={D\over B}\ll H D^{-\eta},
\tag{23}
\]

so its subtraction does not spoil the estimate for (7). Polynomial
length bounds and fixed seminorm hypotheses are the ones in the source;
bounded nonempty column lengths can also be handled by direct counting.
Partial boundary blocks are bounded by the same positive enlargement
and ideal counts.

The order matters: use the imported positive moment on complete
large-\(b\) blocks **before** restricting pairs by (18). After that,
on the remaining small-\(b\) blocks use (17) to remove the pairs in
(18). No sharp pair selector is ever inserted into the positive
moment theorem. The selector in (18) is independent of \(k\), so it
preserves the complete row sum needed by the second Poisson argument.

Thus the actual short-family problem reduces to the form (7) restricted
exactly by (1), including its original masks, coupled physical profiles,
all nonzero dual rows, fixed \(a_\xi\), and the signed coefficient
\(\mu_K(f)\). Call it \(\mathfrak S_{\xi,\rm rem}\). The proved
reduction is

\[
\mathfrak M(D,D^h)
=O(D^{h+\varepsilon})+
\sum_\xi c_\xi\,\mathfrak S_{\xi,\rm rem}
 +O(D^{-L}).
\tag{24}
\]

The \(O(D^{h+\varepsilon})\) term uses the imported valid-range
dual theorem. The diagonal and the large-\(f\)/large-common-factor
bound use only the elementary and Poisson arguments above.

## 6. The new sufficient input and its possible continuation

A sufficient new input, for one fixed \(h\) and \(a\ge0\), is

\[
\operatorname{Re}\sum_\xi c_\xi\,\mathfrak S_{\xi,\rm rem}
\ll_{\nu,S,W,h,a,\eta,\varepsilon}D^{h+a+\varepsilon}
\quad\text{for every }\varepsilon>0,
\tag{25}
\]

on all sufficiently large real \(D\), with the allowed fixed-profile
seminorm control if a uniform profile theorem is asserted. A bound on
the whole modulus also suffices. The sum is real after restoring the
conjugate terms; positivity is not asserted for individual pieces.
Equation (24) then yields the original full-family moment
\((M)_{h,a}\), and the preceding note gives the fixed-character
exponent

\[
\beta_{\rm out}={1+a\over2}+{5h\over12}.
\tag{26}
\]

For the lossless case, the following are exact exponents before buffers:

| \(h\) | Remaining \(b\) exponent | Remaining \(f\) exponent | Conditional \(\beta_{\rm out}\) |
| --- | --- | --- | --- |
| \(8/9\) | \(1/9\) | \(4/9\) | \(47/54=7/8-1/216\) |
| \(4/5\) | \(1/5\) | \(2/5\) | \(5/6\) |
| \(2/3\) | \(1/3\) | \(1/3\) | \(7/9\) |
| \(1/4\) | \(3/4\) | \(1/8\) | \(29/48\) |

The \(h=8/9\) case gives the narrowest \(b\) range among these first
improvement targets. At \(h=2/3\), the residual has two cofactor ranges
at exponent \(1/3\), together with the sharper common-factor selector
in (1). These are reductions of the obligation, not estimates of it.

For a program approaching \(1/2\), the argument permits each fixed
\(h>0\), choosing its buffer first. In the residual,

\[
Nb<D^{1-h+\eta},\quad Nf<D^{h/2+\eta},\quad
Nm_j\gg D^{h/2-2\eta}.
\tag{27}
\]

As \(h\to0\), the \(f\) range becomes shorter while the \(b\) range
grows; the row/column difficulty has not vanished. Constants and
derivative orders may deteriorate with \(h\). A proof of (25) for a
sequence \(h\to0,a\to0\) would supply the strong new arithmetic input
needed for the endpoint; it is not provided by zeta-only quasi-RH.

The next concrete analytic task is a diagonal-subtracted estimate for
(7) on (1), especially its \(b=f=1\) part. It must retain the
Gauss-sum coefficient \(a_\xi\) and actual signs. An extension of
\(\mathcal E\ll\Sigma D^\varepsilon\) without subtracting the
diagonal is ruled out by (10), even before arbitrary coefficients or
unbounded heights enter.

## Finite verification

[check_short_family_small_cofactor.py](../../numerics/check_short_family_small_cofactor.py)
checks the exact local sextic ratio and shared-prime masks, vanishing
of complete nonprincipal finite-character sums, and the rational
exponents in (15), (20), (23), and (26). Its small record is
[short_family_small_cofactor_check.json](../../numerics/short_family_small_cofactor_check.json).
The finite residue-field tests check coefficient identities, not the
two-dimensional analytic Poisson theorem or the missing estimate (25).
The [scoped same-model review](../../reviews/SHORT_FAMILY_SMALL_COFACTOR_REVIEW_20261008.md)
checked full diagonal removal, shared-prime masks, block budgets, and
the order of the sector reductions. Its original source-normalization
acceptance missed the two conjugations corrected above; the
[follow-up review](../../reviews/SHORT_FAMILY_CORE_AND_OVERLAP_REVIEW_20261008.md)
checks the repaired conventions. No new zero-free region is certified.
