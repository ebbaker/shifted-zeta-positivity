# Further bounds for the remaining signed form

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred. Three parallel
same-model derivations and audits are internal checks, not independent
specialist review or formal proof verification.

This bounds three further parts of [Note 28's exact signed form](28_SIGNED_HIGH_CONDUCTOR_SUPPORT_AND_DEFECT_20261009.md):
small primitive quotient conductors, higher-defect auxiliary rows, and
columns with a large sixth-power factor. The last bound includes the
complete cross interaction with the remaining columns. All estimates
retain the original centered inverse, physical zero masks and row
predicates. The full large-support, high-conductor correlation is still
unproved.

## 1. The form and the unchanged inputs

Write
\[
 X=DN^2P_J=U^x,\quad x=r+2m+z_J,\quad L=DP_J=U^{\ell_M},
 \quad\ell_M=r+z_J,\quad B=U^{dr-1/500}.
\]
Keep the original coefficient \(A_c(k)\), supported on \(Nk\asymp X\)
and bounded by \(U^\varepsilon H^b\). For the exact auxiliary row set
\(\mathcal R_D\) of Note 28, put \(W_D=\Omega(Nu/U)1_{\mathcal R_D}\).
The form is
\[
 \mathcal T_D=X^{-1}
 \sum_{\substack{k,k'\\Na>B,\ Nb>B}}
 A_c(k)\overline{A_c(k')}\mathcal H_{W_D}(k,k'),\qquad
 \mathcal H_W(k,k')=\sum_uW(u)\psi_u(k)\overline{\psi_u(k')}. \tag{1}
\]
Here \(a,b\) are the **full exclusive parts** of the two columns, not
ordinary gcd quotients. The row mass is \(O(U)\); the kernel is
Hermitian. Note 28 proves the absolute small-support bound
\[
 |\mathcal P_W(B)|\ll U^{1+dr-1/500+\varepsilon}H^b          \tag{2}
\]
for every bounded annular row subset used below.

The coarse box is
\[
 d\in[9/25,21/50],\quad r\in[7/10,73/100],\quad
 m\in[2/5,207/500],\quad z_J\in[0,2/45].
\]
The global premise remains \(\beta_*\le7/8\), with fresh fixed
\(0<v_{\rm ctr}\le1/5000\) and \(\delta_g=3/4+2v_{\rm ctr}\).
The native arbitrary-coefficient transfer of the sixth-order sieve is
an explicit imported input:
\[
 \Theta_6(A,C)=A+C+A^{5/6}C^{1/3}+A^{1/3}C^{5/6}.          \tag{3}
\]
The [primary theorem](https://arxiv.org/html/2610.04045v1) is for
sixth-power-free good ideals on both sides and arbitrary complex
coefficients, with the field and excluded set fixed. Every application
below meets those domains after the indicated extraction. Moving masks
stay in the vector or are removed only from a positive row square.
Neither a sharp predicate nor a signed pair cut is put into an
unproved radial Poisson formula.

## 2. An elementary count at small primitive quotient conductor

Let
\[
 f(k,k')=\prod_{\substack{\mathfrak p\ {\rm good}\\
       v_{\mathfrak p}(k)-v_{\mathfrak p}(k')\not\equiv0\pmod6}}
       \mathfrak p.
\]
Its norm is comparable, up to the fixed native factors, to the primitive
conductor of the good quotient character. It is a column quotient
conductor, distinct from the row conductor in \(\mathcal R_D\).
For \(V\ge1\),
\[
 \#\{(k,k'):Nk,Nk'\asymp X,\ Nf(k,k')\le V\}
       \ll_\varepsilon XV^{1/2+\varepsilon}.               \tag{4}
\]

**Proof.** For counting only, put \(g=(k,k')\), \(k=g d\), \(k'=g e\),
so \((d,e)=1\). Extract sixth powers:
\[
 d=d_0s^6,\qquad e=e_0t^6,
\]
where \(d_0,e_0\) are sixth-power-free and
\(\operatorname{rad}(d_0e_0)=f(k,k')\).
For fixed \(d_0,e_0,s,t\), both column norm bounds give
\[
 Ng\ll\frac{X}{\max(Nd,Ne)}
       \le\frac{X}{\sqrt{Nd_0Ne_0}(Ns\,Nt)^3}.
\]
The sum of \((Ns\,Nt)^{-3}\) over good ideals converges. At each prime
of \(f\), the positive residual valuation 1 through 5 belongs to just
one of \(d_0,e_0\); there are at most \(10^{\omega(f)}\) allocations.
Also \(Nd_0Ne_0\ge Nf\). Summing ideal counts therefore bounds the
number by
\[
 X\sum_{Nf\le V}10^{\omega(f)}(Nf)^{-1/2}
       \ll_\varepsilon XV^{1/2+\varepsilon}.
\]
Relaxing residual coprimality in this upper count is harmless.
The ordinary gcd is used to prove (4), and does not change the exclusive
parts or pair predicate of (1).

The symmetric intersection of (1) with \(Nf\le V\) is real and has
absolute value at most
\[
 U V^{1/2}U^\varepsilon H^b.
\]
Thus choose
\[
 V=B^2=U^{2dr-1/250}.                                     \tag{5}
\]
That entire part of the existing residual saves \(1/500\), with reserve
\(1/1750\) beyond \(1/700\). This is a strict extension: exclusive
columns \(p^2,q^2\) can each have norm greater than \(B\), while
\(Np\,Nq\le B^2\). Fixed ray phases and deleted-prime zeros are left in
the physical kernel. This is an application of an elementary ideal-pair
count, not a new operator theorem.

For the direct selected alternative, replace the row count by
\(U^R\) and take \(V=B_{\rm sel}^2\), where
\(B_{\rm sel}=U^{1+dr-1/500-R}\). The same bound holds subject to
the original selected-count costs; no auxiliary row estimate is
transferred to selected bins.

## 3. The complete core sieve removes the defect ceiling

Use the physical decomposition
\[
 u=a_1h w^6,\quad h=\prod_{e=2}^5a_e^e,\quad
 b=\prod_{e=2}^5a_e,\quad\mathfrak d=\prod_{e=2}^5a_e^{5-e}.
\]
The \(a_e\) are pairwise coprime squarefree good ideals; finite native
classes are retained separately. Define
\[
 \kappa=\log_U Q_{\psi_u},\quad \lambda=\log_U Nb,\quad
 \theta=\log_U Nh,\quad\eta=5\lambda-\theta,\quad
 \alpha=\kappa-\lambda,\quad \omega=\log_U Nw .
\]
The actual squarefree radius is \(Na_1\asymp U^\alpha\).
In the high-conductor domain \(\kappa>\kappa_1>1/2\), the complete
limiting feasible geometry, up to \(O(1/\log U)\) fixed-factor errors, is
\[
 0\le\lambda\le1-\kappa,\quad
 \max(0,\kappa+4\lambda-1)\le\eta\le3\lambda,\quad
 \omega=(1-\kappa-4\lambda+\eta)/6,\quad \kappa\le1.         \tag{6}
\]
In particular
\[
 \eta/3\le\lambda\le(1-\kappa+\eta)/4,\qquad
 0\le\eta\le3(1-\kappa).
\]

Freeze \(h,w\) in the original marked inverse \(M_uQ_J(u)\).
Its column length is \(L\), its square norm is
\(O(LU^\varepsilon H^b)\), and its column valuations are at most two.
The native sieve is legal at the **actual** radius \(U^\alpha\).
Counting the frozen labels gives the marked mass exponent
\[
 I=\lambda+\omega+
 \max\{\alpha,\ell_M,5\alpha/6+\ell_M/3,
                    \alpha/3+5\ell_M/6\}.
\]
Since \(\alpha\le\kappa\le1<2\ell_M\), this is exactly
\[
 I=\frac16+\frac{\kappa}{6}+\frac{5\ell_M}{6}
       +\frac{\eta+(\ell_M-2\alpha)_+
                        +3(\alpha-\ell_M)_+}{6}.           \tag{7}
\]
The low-radius positive part pays the \(L\)-term in (3).
All masks and native phases remain in the frozen vector.
The alternative original all-row marked inverse bound gives exponent
1, so \(\min(I,1)\) is also available. That alternative supplies no
new row range beyond the previous \(\kappa_1\) by itself.

Keep
\[
 \kappa_1=m+2dr/3-1/750,\qquad
 \kappa_{\rm sf}=\frac12+
 (3d/5-1/2)r-z_J/2+9m/10-3/2500 .
\]
The new gate is
\[
 \boxed{\quad\kappa>\kappa_1,\qquad
 \kappa+\frac{\eta+(\ell_M-2\alpha)_+}{10}
             \le\kappa_{\rm sf}.\quad}                     \tag{8}
\]
It implies \(\kappa\le\kappa_{\rm sf}<\ell_M\), so the upper-radius
positive part in (7) vanishes. There is **no** ceiling \(\eta\le3/20\).
The centered plain factor has square bound
\(U^{2\delta_g(\kappa-m)+\varepsilon}H^b\) throughout this gate.
The correction in (8), multiplied by \(5/3\), exactly pays the extra
mass in (7). Its nominal exponent is at most \(1+dr-1/500\).
The literal contour cost remains at most \(3/12500\), giving
\[
 E_{\mathcal G}\ll
 U^{1+dr-11/6250+\varepsilon}H^b.                          \tag{9}
\]
The reserve is \(29/87500\), with all height and fixed profile losses
charged as in Note 28. Annular and dyadic endpoint errors cost constants.

For an exact physical predicate define
\[
 F(u)=Q_{\psi_u}
 \left[N\mathfrak d\,
       \max\{1,L/(Na_1)^2\}\right]^{1/10},\qquad
 \mathcal G=\{u:\psi_u^*\ {\rm nonprincipal},\
                Q_{\psi_u}>U^{\kappa_1},\
                F(u)\le U^{\kappa_{\rm sf}}\}.              \tag{10}
\]
The logarithmic version (8) differs only by the retained fixed conductor
factors. Those factors do not consume a power reserve. This exact gate
contains the former defect sector for sufficiently large \(U\).
For \(\mathcal S=\mathcal R_D\cap\mathcal G\), its part of (1) is
\(E_{\mathcal S}-\mathcal P_{\mathcal S}(B)\). Equations (2) and (9)
therefore bound its **absolute** value with saving \(11/6250\).

One simple additional class is
\[
 3/20<\eta\le7/25,\qquad
 \kappa_1<\kappa\le\kappa_{\rm sf}-7/250 .
\]
Its actual radius stays above \(\ell_M/2\) with limiting margin \(1/900\),
and its conductor band has width at least \(5191/225000\).
The more general gate also handles low-radius blocks. For example,
at \(d=21/50,r=73/100,m=2/5,z_J=0\), the feasible type-two
geometry
\[
 \kappa=151/250,\quad\lambda=6/25,\quad
 \eta=18/25,\quad\alpha=91/250
\]
has \(\alpha<\ell_M/2\) and
\(\kappa+[\eta+(\ell_M-2\alpha)_+]/10=3381/5000
 <\kappa_{\rm sf}=2118/3125\).
This is an exponent-geometry witness, not a claim of detector-bin
population.

## 4. A native sieve bound for a large sixth-power column tail

Now let \(W\) be any nonnegative bounded annular subset of the rows
with \(Q_{\psi_u}>U^{\kappa_1}\), including the residual after (10).
Every full good column has a unique extraction
\[
 k=f t^6,\qquad f\ {\rm sixth\text{-}power\text{-}free}.
\]
For \(T\ge1\), let \(A_>(k)=A_c(k)1_{Nt>T}\), and let
\(\Delta_>\) be its normalized polynomial. Write
\[
 E_>(T)=\sum_uW(u)|\Delta_>(u)|^2,\qquad
 \zeta=(1-\kappa_1)/6 .
\]
The column extraction is of the complete centered coefficient, after
all ownership sums; it does not alter the inverse annulus or declare a
source moment for a new inverse.

In a finite native class, \(\psi_u(t^6)\) is a bounded common
presentation phase times the exact mask \(1_{(u,t)=1}\).
Weighted Cauchy over the original \(t\)-sum gives
\[
 E_>(T)\ll T^{-1}\sum_{Nt>T}(Nt)^2
 \sum_uW(u)\left|X^{-1/2}
       \sum_fA_c(ft^6)\psi_u(f)\psi_u(t^6)\right|^2,         \tag{11}
\]
since \(\sum_{Nt>T}(Nt)^{-2}\ll T^{-1}\).
No pair or row sign is removed before this positive square.

Decompose the row as \(u=v w^6\), with \(v\) sixth-power-free.
The original high-conductor gate first gives \(Nw\ll U^\zeta\),
because \(Q_{\psi_u}\ll Nv\) and \(Nv(Nw)^6\asymp U\).
For fixed \(t,w\), the columns \(f\) are sixth-power-free of norm
\(\ll X/(Nt)^6\), and
\[
 X^{-1}\sum_f|A_c(ft^6)1_{(f,w)=1}|^2
       \ll (Nt)^{-6}U^\varepsilon H^b.                    \tag{12}
\]
The mask \(1_{(v,t)=1}\) can be removed only from the positive row sum.
The frozen \(w\)-mask stays inside the coefficient vector.
Enlarge \(v\) to the permitted sixth-free ball of radius
\(O(U/(Nw)^6)\) and apply (3). Fixed presentation phases and zeros
are included once. Nonempty endpoint blocks have column radius at
least a fixed positive constant; replacing that radius by a fixed
multiple at least 1 costs only constants.

Insert (12) into (11), sum \(w\) up to \(U^\zeta\), and use
convergence of the \(w^{-6},w^{-5},w^{-2}\) ideal sums. The four
terms of (3) give
\[
 \boxed{\ E_>(T)\ll U^\varepsilon H^b
 \left[
 U T^{-4}+XU^\zeta T^{-10}
 +U^{5/6}X^{1/3}T^{-6}
 +U^{1/3}X^{5/6}T^{-9}
 \right].\ }                                             \tag{13}
\]
For example, the first term is
\(T^{-1}U\sum_{Nt>T}(Nt)^{-4}\ll UT^{-4}\);
the other \(t\)-powers are \(-10,-6,-9\) before summation
and the common \(T^{-1}\) restores those final powers.
The potentially long \(w\)-count occurs only with the column-length
term \(X\).

The same proof, using all \(Nt\ge1\) and the convergent total
\(\sum_t(Nt)^{-2}\), bounds the **whole original coefficient**:
\[
 E_W\ll U^\varepsilon H^b
 [U+XU^\zeta+U^{5/6}X^{1/3}+U^{1/3}X^{5/6}].              \tag{14}
\]
These are deductions from the stated native operator and coefficient
bound. They require neither the specialized source fourth moment nor
an inverse pointwise bound.

## 5. The entire tail interaction fits the signed-form budget

Put \(A_\le=A_c-A_>\), and use the same physical measure \(W\)
for its polynomial and both cross terms. Then exactly,
\[
 E_W-E_\le
 =2\operatorname{Re}\langle\Delta,\Delta_>\rangle_W-E_>,
\qquad
 |E_W-E_\le|\le2\sqrt{E_WE_>}+E_>.                        \tag{15}
\]
For \(T=U^\sigma\), let
\[
 \begin{aligned}
 \beta_0&=\max\{1,x+\zeta,5/6+x/3,1/3+5x/6\},\\
 \beta_>(\sigma)&=\max\{1-4\sigma,x+\zeta-10\sigma,
              5/6+x/3-6\sigma,1/3+5x/6-9\sigma\}.
 \end{aligned}
\]
The cross bound has exponent \((\beta_0+\beta_>)/2\).
At the simple choice
\[
 \boxed{\sigma=1/10},
\]
an exact multi-affine corner check of all 16 branch pairs proves
throughout the coarse box
\[
 1+dr-1/500-\frac{\beta_0+\beta_>(1/10)}2
       \ge\frac{5519}{135000}>0.0408 .                    \tag{16}
\]
The tail square itself is smaller. The limiting corner is
\(d=9/25,r=73/100,m=207/500,z_J=2/45\), with
\(\beta_0=25067/15000,\ \beta_>=4151/5400\).
Each branch-pair deficit is multi-affine in \(d,r,m,z_J\);
its minimum is attained at a box corner, so the finite corner
calculation certifies the whole displayed parameter box.

To transfer (15) to the signed form, subtract the exact pair cuts for
the full and head coefficients. Both satisfy (2), since the head
retains the pointwise coefficient bound. If the small quotient
sector (5) has also been removed, subtract its full/head difference
as well; both are bounded by (4). Consequently the complete remaining
pair sector with **at least one** \(Nt>U^{1/10}\) saves \(1/500\),
including every head/tail cross term. This argument controls the
intersection with the existing cuts rather than assuming the
pair filter preserves positivity.

There is an optional stronger cutoff. **Only when all of Note 27's
source scalar hypotheses hold**—the nonexceptional-row condition,
original prescribed slot mesh, finite ray-character coefficient
class, legal profile/height allowances and
\(2m+(9/2)z_J<1\)—one may use
\(E_W\ll U^{1+\delta_g r+\varepsilon}H^b\) for the complete
original coefficient in (15). At \(\sigma=2/25\), the exact reserve
beyond saving \(1/500\) is at least \(84727/6750000\).
The corner check includes \(v_{\rm ctr}\le1/5000\).
The larger coarse corner box is used only as a conservative arithmetic
enclosure; it does not imply those source hypotheses. Neither the
tail nor the head is inserted into the source's specialized moment.
The universal choice \(1/10\) in (16) does not need that source scope.

All complete tail-removal bounds retain the pair-cut reserve \(1/1750\).
Their finite height degrees and other fixed losses must fit within it.
The larger cross reserve in (16) does not enlarge the tighter reserve
of the elementary pair corrections.

## 6. The exact form still requiring a new correlation bound

Let
\[
 \mathcal R_*=\{u:\psi_u^*\ {\rm nonprincipal},\
 Q_{\psi_u}>U^{\kappa_1},\ F(u)>U^{\kappa_{\rm sf}}\},
 \qquad W_*=\Omega(Nu/U)1_{\mathcal R_*}.
\]
This is the exact remaining row predicate after (10); the old low and
defect sectors are included in the previous removals. Use the universal
column head
\(A_\le(k)=A_c(k)1_{Nt(k)\le U^{1/10}}\).
The surviving real signed form is
\[
 \boxed{\ \mathcal T_*=
 X^{-1}\!\!
 \sum_{\substack{k,k'\\Na>B,\ Nb>B\\
                    Nf(k,k')>B^2}}
 A_\le(k)\overline{A_\le(k')}\mathcal H_{W_*}(k,k').\ }       \tag{17}
\]
Every boundary is assigned explicitly: the head and small quotient
sector use \(\le\), the remaining quotient and row gate use \(>\).
For sufficiently large \(U\), \(\mathcal R_*\subset\mathcal R_D\).
The exact partition and (2), (4), (9), (15) prove
\[
 |\mathcal T_D-\mathcal T_*|
       \ll U^{1+dr-11/6250+\varepsilon}H^b.                 \tag{18}
\]
The controlling reserve is \(29/87500\), from the row extension;
the pair and column corrections have their own \(1/1750\) reserves.
Thus a one-sided bound
\[
 \mathcal T_*\ll U^{1+dr-1/700+\varepsilon}H^b              \tag{19}
\]
is sufficient for the full centered target, with all fixed costs paid.
It is also equivalent to the preceding finishing form up to the
controlled error. Equation (19) remains **unproved**.

The native envelope (14) bounds the whole form under its stated
inputs, but does not meet (19). Where the specialized scalar
input is legal, triangle inequality from (15) also bounds the head
energy by its former exponent \(1+\delta_g r\), and the exact signed
cuts cost smaller controlled errors. Its worst-case deficit is still
at least \(1627/7000\). The head coefficient still has Note 18's full-size square-norm
benchmark in the zero-slot prime-product prototype, since its column
sixth-power factors are units. Its diagonal pairs have been removed
from (17); this is a warning against replacing the filtered form by a
generic positive coefficient norm, not an obstruction to (19).

The direct selected route may use the small quotient bound and the
column-tail bound with its own physical row subset, retaining
\(B_{\rm sel}\) and \(V=B_{\rm sel}^2\).
The auxiliary row extension still lies below the selected high-conductor
gate and is not claimed to remove selected rows.

## 7. Verification and next obligation

The [checker](../../numerics/check_signed_form_bound.py) and its
[record](../../numerics/signed_form_bound_record_20261009.json) verify
16,191 exact finite assertions with deterministic replay.
They check the quotient/sixth-power decomposition, complete head/tail
cross terms and nested signed cuts, physical zeros, the piecewise
marked-core mass, new frontier and strict boundaries, and the rational
tail and reserve ledgers. The character kernel and ideal monoid used
in finite tests are synthetic. They do not certify native transfer,
global source inputs, ideal asymptotics, height propagation or (19).
The [review](../../reviews/MIXED_SIGNED_FORM_BOUND_REVIEW_20261009.md)
records the analytic audits and manuscript checks.

The next estimate must treat (17) jointly: both full exclusive norms
exceed \(B\), the primitive column quotient conductor exceeds \(B^2\),
both column sixth-power factors are at most \(U^{1/10}\), and the
physical row fails the complete core frontier. The centered Mellin
and common aspect derivative interfaces of Note 28 remain available,
but require a new signed aggregate estimate for this domain.
The full mixed theorem, detector coverage, new family boundary and
RH descent remain unproved.
