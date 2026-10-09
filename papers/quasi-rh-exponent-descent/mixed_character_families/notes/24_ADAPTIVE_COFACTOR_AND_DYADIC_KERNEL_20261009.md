# Adaptive cofactor removal and the exact dyadic signed interface

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred. Parallel audits
and finite checks are same-model internal validation, not independent
specialist review or formal proof verification.

Follow-up: [Note 25](25_SQUAREPART_REMOVAL_AND_SMOOTH_OBSTRUCTION_20261009.md) controls a large common factor of the two inverse factors with every cross term. It also disproves the unrestricted uncentered smooth target in an explicitly principal-compatible class; the selected-family target remains open. The conditional zero identities below retain their scope.

Review of the [manuscript](../mixed_character_reductions.tex) and
[continuation 23](23_SIGNED_BILINEAR_CONTINUATION_20261009.md) yields an
enlarged conditional removal, an exact dyadic coefficient interface, and
a controlled first-Poisson zero term in a sufficient smooth problem.
The remaining nonzero-frequency estimate is still open.

## 1 A larger cofactor cutoff with the same guaranteed saving

Keep every input, original selector, profile, zero, whole slot and fixed
cost condition of [note 22](22_TRUNCATED_INVERSE_BILINEAR_REMOVAL_20261009.md).
Define
\[
 \alpha_*(r)=\frac r2-\frac14,\qquad T_*=U^{\alpha_*(r)},
 \qquad M_{*,u}=-D^{-1/2}\sum_{\mathrm Nt>T_*}
 c_Z(t)\psi_u(t)P_u(D/\mathrm Nt),\quad Z=\sqrt{CD}.
\]
Here and below all variables are good ideals. On the working domain,
\(1/10\le\alpha_*<23/200\), and \(T_*\le Z\) eventually. For
\(y=\log_U\mathrm Nt\le\alpha_*\), the shorter plain exponent obeys
\[
 r-y\ge r/2+1/4\ge3/5,\qquad r-y\le r<73/100.
\]
Thus the existing reflected same-profile bound applies throughout this
larger sector; no extension to new lengths is imported.

The same absolute divisor-sum calculation gives its short square saving
\[
 \lambda_*(d,r)=d(2r-1)-(1+d)\alpha_*
              =\frac{(2r-1)(3d-1)}4.
\]
In particular, with the positive original weight
\(V_u=1_{\mathcal C_+}(u)|S_u|^4|Q_J(u)|^2\),
\[
 F_{\mathrm{sh},*}:=\sum_uV_u|M_u-M_{*,u}|^2
 \ll_\varepsilon U^{1+dr-\lambda_*+(21-6r)e_{\rm src}+\varepsilon}H^b.
                                                        \tag{1}
\]
Apply weighted Cauchy to the **full** original inverse and this short
part, exactly as in note 22. The saving for the complete difference is
\[
 \delta_*(d,r,e_{\rm src})
 =\frac{(2r-1)(3d-1)}8-(21/2+3r)e_{\rm src}.             \tag{2}
\]
For \(0<e_{\rm src}\le1/1200000\), its derivatives satisfy
\[
 \partial_d\delta_* =3(2r-1)/8>0,\qquad
 \partial_r\delta_* =(3d-1)/4-3e_{\rm src}
                         \ge1/50-3e_{\rm src}>0.
\]
The short-square saving in (1) is also increasing in both \(d\) and
\(r\). Their minima are consequently the original lower corner:
\[
 \delta_*\ge\frac1{250}-\frac{63}{5}e_{\rm src}
              \ge\frac{7979}{2000000},\qquad
 \lambda_*-(21-6r)e_{\rm src}\ge\frac{3993}{500000}.
\]
The latter is larger than the former uniformly: their difference is
\(\lambda_*/2-(21/2-9r)e_{\rm src}>0\) on this box.
Therefore
\[
 \boxed{\left|F-\sum_uV_u|M_{*,u}|^2\right|
 \ll_\varepsilon U^{1+dr-7979/2000000+\varepsilon}H^b.}  \tag{3}
\]
The reserve over \(1/700\) remains \(35853/14000000\), with all
already fixed height/profile costs deducted and the tighter source and
witness budgets still required. For every \(r>7/10\), this removes a
strictly larger combined-cofactor range. It makes no assertion that both
truncated factors are large. The new sufficient theorem is
\[
 \boxed{F_*:=\sum_uV_u|M_{*,u}|^2
       \ll_\varepsilon U^{1+dr-1/700+\varepsilon}H^b.}    \tag{4}
\]
Under (3), this is equivalent at that exponent to the full original
target. The fixed \(U^{1/10}\) formulation remains valid historically.

## 2 Literal dyadic cover, including its cross terms

For \(A,B,L\) powers of two at least one, let \(\gamma=(A,B,L)\) and
\[
 R_{\gamma,u}=-D^{-1/2}
 \sum_{\substack{A\le\mathrm Na<2A,\ B\le\mathrm Nb<2B,
                         \ L\le\mathrm Nl<2L\\
             \mathrm Na,\mathrm Nb\le Z,\ \mathrm N(ab)>T_*}}
 \mu_F(a)\mu_F(b)\psi_u(abl)A_0(\mathrm N(abl)/D).       \tag{5}
\]
Only squarefree \(a,b\) contribute; they can share a prime. The quotient
\(l\) has no power-free restriction. Empty blocks are discarded. The
half-open intervals assign each tuple once, including every endpoint.
Nonempty blocks satisfy
\[
 A,B\le Z,\quad AB>T_*/4,\quad ABL\le CD,\quad 8ABL>cD.
\]
These are necessary outer bounds; they do **not** replace the literal
cuts or profile in (5). There are \(O((1+\log U)^3)\) blocks and exactly
\[
 M_* =\sum_\gamma R_\gamma,\qquad
 F_* =\sum_{\gamma,\gamma'}\sum_uV_u
                      R_{\gamma,u}\overline{R_{\gamma',u}}.             \tag{6}
\]
Both \(A=1\) and \(L=1\) are retained. In particular a balanced
two-factor estimate is only a subcase. Cauchy gives
\(F_*\le\#\Gamma\sum_\gamma\sum_uV_u|R_{\gamma,u}|^2\);
uniform target-sized block norms would suffice with logarithmic losses.
Such bounds are stronger than (4). Equation (6) retains the potentially
useful cancellation between different blocks.

## 3 The signed squarefree core and exact prime-extraction closure

Whenever \(c_Z(t)\ne0\), uniquely write \(t=g^2h\), with \(g,h\)
squarefree and coprime. Then
\[
 c_Z(g^2h)=\mu_F(h)\sum_{a_0b_0=h}
              1_{\mathrm Na_0,\mathrm Nb_0\le Z/\mathrm Ng}.            \tag{7}
\]
Indeed \(a=g a_0,b=g b_0\); the two Möbius factors have product
\(\mu_F(h)\). The count is nonnegative but generally nonmultiplicative.
There is still a physical square factor \(\psi_u(g)^2\), with its
zeros. Neither \(g\) nor \(h\) can be deleted from the annulus or cut.

For possibly unequal caps define
\[
 h_{Z_a,Z_b,T}(n)=\sum_{\substack{abl=n\\
                 \mathrm Na\le Z_a,\ \mathrm Nb\le Z_b,\ \mathrm N(ab)>T}}
                          \mu_F(a)\mu_F(b).                           \tag{8}
\]
It is row independent and \(|h(n)|\le d_{3,F}(n)\). The inverse is
\(-D^{-1/2}\sum_n h_{Z,Z,T_*}(n)\psi_u(n)A_0(\mathrm Nn/D)\).
For a prime \(p\), \(P=\mathrm Np\), and \(p\nmid n_0\), its exact
extraction identity is
\[
 h_{Z_a,Z_b,T}(p^kn_0)=
 \sum_{\substack{e_a,e_b\in\{0,1\}\\e_a+e_b\le k}}
 (-1)^{e_a+e_b}
 h_{Z_a/P^{e_a},\,Z_b/P^{e_b},\,T/P^{e_a+e_b}}(n_0).    \tag{9}
\]
The quotient carries \(k-e_a-e_b\) powers. A cap below one gives an
empty branch. The strict threshold and inclusive caps remain literal.
For dyadic coefficients the same branch also rescales their factor
intervals; (9) is stated for the unsliced coefficient. Iterating it
handles any finite prime set without replacing its signed branches by
independent positive estimates.

This class is not squarefree in its full output. If \(1\le T<P\le Z\) and
\(p^2\) lies in the original annulus, then \(h_{Z,Z,T}(p^2)=-1\):
the large tuples \((p,1,p),(1,p,p),(p,p,1)\) have weights \(-1,-1,+1\).
The short tuple \((1,1,p^2)\) completes cancellation with the original
\(\mu_F(p^2)=0\). This coefficient example is not a lower bound for
the selected moment.

## 4 Full marked coefficient and the first zero term

Put \(P_J=\prod_{j\in J}P_j\) and \(X=DN^2P_J\). Expanding the
complete polynomial gives
\[
 M_{*,u}S_u^2Q_J(u)=-X^{-1/2}\sum_k\mathscr A_*(k)\psi_u(k),          \tag{10}
\]
where
\[
 \mathscr A_*(k)=
 \sum_{abl v_1v_2\prod_jp_j=k}
 \mu_F(a)\mu_F(b)1_{\mathrm Na,\mathrm Nb\le Z}
 1_{\mathrm N(ab)>T_*}A_0(\mathrm N(abl)/D)
 B(\mathrm Nv_1/N)B(\mathrm Nv_2/N)
 \prod_j a_j(p_j)W_j(\mathrm Np_j/P_j).                 \tag{11}
\]
All original good-ideal and live-slot exclusions remain. This is a finite,
row-independent coefficient, supported in \(\mathrm Nk\asymp X\),
with \(|\mathscr A_*(k)|\ll_\varepsilon X^\varepsilon\) for fixed
bounded profile/slot data. Its negative sign is common to the whole
polynomial and cancels on forming the norm. These statements also hold
for each dyadic block.

For exact extraction in (11), set the valuations of \(a,b\) to
\(e_a,e_b\in\{0,1\}\), those of \(l,v_1,v_2\) to
\(e_l,f_1,f_2\ge0\), and keep any live-slot ownership separately.
Every residual factor is \(p\)-free. The caps and threshold are those
in (9); the inverse annulus rescales to \(D/P^{e_a+e_b+e_l}\),
and the two plain annuli to \(N/P^{f_1},N/P^{f_2}\).
The coefficient sign is \((-1)^{e_a+e_b}\). The native row factor is
the actual \(\psi_u(p)\) to the total extracted power, including slot
ownership. Under the formal residual product normalization \((X/P^k)^{-1/2}\)
the scalar is \(P^{-k/2}\) for total extracted power \(k\).
If a frozen slot is removed while the child uses its nominal remaining
slot scales, retain that slot's actual \(P_j^{-1/2}\) scalar; its
normalizer is not obtained by replacing \(P_j\) with \(P\).
No division by a
character is allowed; a positive extracted power keeps its physical zero.
An eligible prime outside live slot windows has no slot ownership.

Thus the finite common-support and joint-kernel algebra of
[note 21](21_SIGNED_JOINT_TRANSFORM_20261009.md) extends to this literal
coefficient, retaining its masks, caps, profiles, and common pair kernel.
This is an **algebraic** coefficient extension. It does not establish the
source reflection, centered comparison, recursive child estimates, or
seminorm/height propagation for this five-variable marked class.

There is one controlled analytic component in a sufficient positive smooth
row envelope. Assume the imported native first row-Poisson formula applies
to (10), with a fixed admissible envelope of row mass \(O(U)\).
Its zero frequency is nonzero only when the good sextic ratio is principal.
In a fixed common presentation this forces equal sixth-power-free cores:
\(k=v a_1^6,k'=v b_1^6\). Ideal counting gives
\[
 \#\{(k,k'): \mathrm Nk,\mathrm Nk'\le C_X X,
                     \text{equal sixth-power-free core}\}
 \ll X^{1/3}\sum_{\mathrm Nv\le C_X X}(\mathrm Nv)^{-1/3}\ll X.
\]
Finite ray/unit multiplicities and divisor allocations cost at most
\(X^\varepsilon\). The local zero means have modulus at most one,
and the central square normalizer is \(X^{-1}\). The first zero term
therefore has bound \(O_\varepsilon(U^{1+\varepsilon}H^b)\), with
reserve \(dr-1/700\ge877/3500\) against (4). This is conditional on
the specified smooth Poisson input; it is not Poisson on the sharp bin.
It is also distinct from the artificial **second** zero diagonal canceled
by the complete coprimality projector in note 21.
An all-row positive envelope can add auxiliary principal rows. The
original nonprincipal-bin bounds cannot be applied on those rows; the
full smooth moment remains a stronger sufficient problem.

The residual unit/unit **second** zero also admits an aggregate bound.
Use raw allocated coefficients, the unchanged whole-product square
normalizer \(X^{-1}\), and the source's scalar of bounded modulus in
the frozen labels (printed p. 161, (18.21)). Frozen profile and slot
weights stay inside the raw coefficients. For \(r_c=1,a=b=1\), put
\(\lambda=H_{\rm row}T_{\rm freq}/\mathrm Ne_c\). The scale times
Fourier weight is \(X^{-1}\lambda\widehat w_\lambda(0)\).
Since \(w_\lambda(x)=\omega(x)\widehat\Phi_1(\lambda x)\) on a fixed
annulus, boundedness for \(\lambda\le1\) and Schwartz decay for
\(\lambda\ge1\) give \(\sup_{\lambda>0}|\lambda\widehat
w_\lambda(0)|<\infty\). The full common columns have equal sextic
cores when \(r_c=1\), so their outer pair count is \(O(X)\).
Divisor-bounded raw coefficients, masks, allocations and retained dyads
give a total unit-exception contribution
\(O_\varepsilon(U^\varepsilon H^b)\). This is an outer-label bound,
not pointwise disappearance. Any child normalizers require restoring
their corresponding outer norm factors before this calculation.

## 5 What to estimate next

The remaining task is a bound for the full nonzero-frequency signed
aggregate of (11), or its dyadic pair coefficients from (6), in a
sufficient smooth row problem. Use the complete coprimality combination
and its frequency-divisor support before any absolute label sum. The
literal prime branches (9) and their rescaled profiles give the algebraic
child interface; their signed estimates, exceptional comparisons and
derivative/height uniformity still require proof. The joint width ledger
remains unchanged. The source's separately positive diagonal estimate
still does not supply the missing power gain.

The elementary block estimate illustrates the gap. Ideal counting and
the fixed three-factor divisor bound give \(|R_{\gamma,u}|^2\ll
D U^\varepsilon\). The original selected fourth mass then gives only
\(\sum_uV_u|R_{\gamma,u}|^2\ll U^{1+r+\varepsilon}H^b\), with
exponent deficit \((1-d)r+1/700\ge713/1750\). The dyadic cover alone
does not improve this estimate. A sharp quotient dyad also changes the
plain profile; any use of the reflected bound there needs a permissible
smooth decomposition and its derivative allowance proved first.

This session completes the exact dyadic partition requested in note 23,
its algebraic marked extension, the adaptive enlargement and the smooth
first-zero count. It does not prove (4), complete operational/bin coverage,
native-family boundary reuse, a new zero-free strip, or RH descent.

The [checker](../../numerics/check_mixed_dyadic_cofactor.py) and
[record](../../numerics/mixed_dyadic_cofactor_record_20261009.json) retain
finite exact evidence; the [review](../../reviews/MIXED_ADAPTIVE_DYADIC_REVIEW_20261009.md)
records its scope and manuscript verification. Third-party analytic
inputs retain their status and source links in Notes 16, 21 and 22.
