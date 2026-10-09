# Signed high-conductor continuation: support pairs and a valuation defect

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; exact serving variant and
reasoning effort are not exposed and are not inferred. Three parallel
same-model derivations and audits are internal checks, not independent
specialist validation or formal proof verification.

This continues [Note 27](27_CENTERED_AUXILIARY_CONTROL_AND_SIGNED_REMAINDER_20261009.md).
Two further sectors are controlled: small unmatched **full column support**
in the original signed square, and auxiliary conductors above the previous
cutoff in a class with a small higher-valuation defect. The remaining
signed high-conductor theorem is not proved. The exact residual below
retains the original inverse, centered coefficient, row predicates and
physical zeros.

## 1. The exact common physical kernel

Keep Note 27's original centered coefficient \(A_c(k)\), not a residual
inverse or an independently bounded positive coefficient norm. Write
\[
 X=DN^2\prod_{j\in J}P_j,\quad
 \Delta_u=X^{-1/2}\sum_k A_c(k)\psi_u(k),\quad
 D=U^r,\quad N=U^m,\quad z_J=\sum_{j\in J}\log_U P_j .
\]
The equal-product comparison scales are \(Y_1=U^{1/4}\) and
\(Y_2=U^{2m-1/4}\). For fixed permitted profile data,
\[
 \operatorname{supp}(A_c)\subset\{k:Nk\asymp X\},\qquad
 |A_c(k)|\ll_\varepsilon X^\varepsilon H^{b_c}.             \tag{1}
\]
All original annuli, inverse Möbius signs, disjoint whole prime slots,
finite ray phases and zero masks are included in \(A_c,\psi_u\).
Profile derivatives are fixed first and have a finite height degree.

For a nonnegative physical row weight \(W(u)\), put
\[
 \mathcal H_W(k,k')=\sum_u W(u)\psi_u(k)\overline{\psi_u(k')},
 \qquad E_W=\sum_uW(u)|\Delta_u|^2.
\]
The finite exact expansion is
\[
 E_W=X^{-1}\sum_{k,k'}A_c(k)\overline{A_c(k')}\mathcal H_W(k,k').
                                                               \tag{2}
\]
The kernel is Hermitian and
\[
 |\mathcal H_W(k,k')|\le\sum_u W(u).                          \tag{3}
\]
This holds with a sharp selected-bin predicate or a sharp conductor cut
outside the column sum. It needs no radial row-Poisson theorem.
With \(W=1_{\mathcal C_+}\), the imported physical bin count gives
\(\sum W\ll U^{R+\varepsilon}H^{b_R}\), \(R=R_*+\ell\).
For a bounded smooth annular envelope, with any additional physical
conductor/class predicate, ideal/element counting gives \(\sum W\ll U\).
We use \(R\) only on the selected family.

## 2. An elementary uniform count on a fixed prime support

For a good ideal \(k\) of norm at most \(C_X X\), let
\[
 \mathcal S_k(C_X X)=
 \{c:Nc\le C_X X,\ \operatorname{supp}(c)\subseteq\operatorname{supp}(k)\}.
\]
For every \(\varepsilon>0\), uniformly in \(k\),
\[
 \#\mathcal S_k(C_X X)\ll_{\varepsilon,C_X}X^\varepsilon.
                                                               \tag{4}
\]
**Proof.** Choose fixed positive \(\sigma,\delta\). Rankin's bound gives
\[
 \#\mathcal S_k(C_X X)\le(C_X X)^\sigma
             \prod_{\mathfrak p\mid k}(1-(N\mathfrak p)^{-\sigma})^{-1}.
\]
For sufficiently large \(N\mathfrak p\),
\((1-(N\mathfrak p)^{-\sigma})^{-1}\le(N\mathfrak p)^\delta\).
There are only finitely many smaller prime ideals in the fixed field,
so their product is a constant. The entire product is at most
\(C_{\sigma,\delta}(N\operatorname{rad}k)^\delta\ll X^\delta\).
Take \(\sigma+\delta\le\varepsilon\). This proves (4) by elementary
ideal counting, without a new analytic Euler-product hypothesis.
The parameters are fixed after the requested loss, not allowed to
depend on a row or on \(X\).

## 3. A controlled signed small-unmatched-support sector

For each ordered pair \(k,k'\), make the unique **full common-support**
decomposition
\[
 k=C_1a,\qquad k'=C_2b,
\]
where \(C_1,C_2\) contain the full powers at every prime occurring in
both columns, and \(a,b\) contain the full powers at primes occurring
only in their respective column. Consequently
\[
 \operatorname{rad}(C_1)=\operatorname{rad}(C_2),\qquad
 (a,b)=1,\qquad (ab,C_1C_2)=1.                               \tag{5}
\]
This is not division by the ordinary gcd. For
\(k=p^2q,\ k'=pq^2\), the full exclusive parts are \(a=b=1\);
ordinary gcd quotients would instead be \(p,q\).

For fixed \(k\), the pairs with \(Nb\le B\) are counted by at most
\(O(B)\) choices of \(b\), and at most \(X^\varepsilon\) choices
of \(C_2\) supported on \(k\), by (4). Relaxing the required disjointness
only increases this count. There are \(O(X)\) choices of \(k\).
Reversal gives the same count for \(Na\le B\). Hence, for \(B\ge1\),
\[
 \#\{(k,k'):Nk,Nk'\asymp X,\ \min(Na,Nb)\le B\}
             \ll_\varepsilon XB X^\varepsilon.              \tag{6}
\]
Define the exact pair part of (2)
\[
 \mathcal P_W(B)=X^{-1}
 \sum_{\min(Na,Nb)\le B}
       A_c(k)\overline{A_c(k')}\mathcal H_W(k,k').
\]
The cut is symmetric, so \(\mathcal P_W(B)\) is real.
Equations (1), (3) and (6) show
\[
 |\mathcal P_W(B)|\ll_\varepsilon
       \left(\sum_uW(u)\right)B U^\varepsilon H^b.           \tag{7}
\]
Its summands can have either sign; (7) is an absolute bound for their
complete sector, not a positive enlargement of a signed expression.

For any auxiliary annular row subset use
\[
 B_{\rm all}=U^{dr-1/500}.
\]
Then
\[
 |\mathcal P_W(B_{\rm all})|
          \ll U^{1+dr-1/500+\varepsilon}H^b,                 \tag{8}
\]
with reserve \(1/1750\) over the target saving \(1/700\).
The fixed \(B=U^{1/4}\) is also sufficient on the coarse box
\(dr\ge63/250\), with the same saving \(1/500\).

For the actual selected family, its smaller physical count permits
\[
 B_{\rm sel}=U^{1+dr-1/500-R},\qquad
 |\mathcal P_{\mathcal C_+}(B_{\rm sel})|
          \ll U^{1+dr-1/500+\varepsilon}H^b.                 \tag{9}
\]
This selected cutoff is larger than the all-row cutoff by \(1-R\)
in its exponent when \(R<1\). It does not justify selected row-Poisson.
If an application uses \(R\) outside that range or has extra fixed
count/height costs, retain the literal formula and charge those costs;
the count is an imported bin input, not proved by (6).

The new sector includes **all same-radical pairs**, even when their
good sextic ratio is nonprincipal. Thus it extends beyond the already
controlled first zero frequency. It also controls one-sided small
unmatched support. It does not impose a cutoff on the inverse-variable
gcd or ratio from earlier notes, and is not identified with those
distinct selectors. Overlapping removals are combined through exact
set differences, not by adding or comparing their signs.

## 4. A legal marked inverse sieve on squarefree physical cores

We also sharpen an auxiliary conductor sector before applying the signed
pair cut. Let \(L=DP_J=U^{\ell_M}\), where
\(\ell_M=r+z_J\) is the marked inverse column-length exponent. The marked inverse has the
coefficient form
\[
 M_uQ_J(u)=L^{-1/2}\sum_k c_J(k)\psi_u(k),\qquad
 \sum_k|c_J(k)|^2\ll_\varepsilon L U^\varepsilon H^b.         \tag{10}
\]
The inverse variable is squarefree and the original slot supports are
disjoint. A prime occurs in at most one slot and once in the inverse,
so every column valuation in (10) is at most two. These columns are
sixth-power-free. This statement fails without the original disjoint
slot hypothesis; no arbitrary full plain coefficient is put into this
sieve.

Use the native arbitrary-coefficient transfer of the \(n=6\) case of
[de Faveri's Theorem 1.1](https://arxiv.org/html/2610.04045v1):
\[
 \Theta_6(A,L)=A+L+A^{5/6}L^{1/3}+A^{1/3}L^{5/6}.           \tag{11}
\]
The primary theorem was checked directly. Its arithmetic transfer to the
fixed native presentation is the explicit imported input already stated
in the manuscript. It retains reciprocity phases and physical zero masks.
The implied operator constant is uniform in the coefficient vector;
moving good-prime masks or twists are coefficients, not newly fixed
excluded primes.

First take \(u=aw^6\), with squarefree good core \(a\).
On \(Na\asymp Q_{\psi_u}\asymp U^\kappa\), there are
\(O(U^{(1-\kappa)/6})\) possible \(w\). For fixed \(w\), all
deletions \(1_{(k,w)=1}\) stay in the coefficient of (10), whose norm
cannot increase. The \(a\)-sum is a subset of the native sixth-free
operator row domain of radius \(O(U^\kappa)\). Apply (11) and sum \(w\).
For
\[
 \ell_M/2\le\kappa\le\ell_M,
\]
the dominant exponent in (11) is \(\kappa/3+5\ell_M/6\), giving
\[
 \sum_{\substack{u=aw^6\\a\ {\rm squarefree}\\
                  Q_{\psi_u}\asymp U^\kappa}}
  \Omega(Nu/U)|M_uQ_J(u)|^2
       \ll U^{1/6+\kappa/6+5\ell_M/6+\varepsilon}H^b.          \tag{12}
\]
This is a bound on actual squarefree cores after freezing \(w\);
it is not an operator theorem indexed by the conductor of an arbitrary
sixth-free physical row.

## 5. The higher-valuation defect and its actual row radius

Decompose every good physical row uniquely as
\[
 u=vw^6,\quad
 v=a_1\prod_{e=2}^5a_e^e,\quad
 h=\prod_{e=2}^5a_e^e,\quad b=\prod_{e=2}^5a_e,
                                                               \tag{13}
\]
where all \(a_e\) are squarefree and pairwise coprime. Finite unit and
bad-prime classes remain separate. No coprimality between \(w\) and
these core factors is assumed. Define
\[
 \mathfrak d(v)=\prod_{e=2}^5a_e^{5-e},\quad
 \lambda=\log_U Nb,\quad \theta=\log_U Nh,\quad
 \eta=\log_U N\mathfrak d(v)=5\lambda-\theta\ge0.             \tag{14}
\]
In particular fifth-power primes contribute zero defect. A bound
\(Nb\le U^{1/20}\) implies \(\eta\le3/20\), but the latter
is a larger, more useful class.

On a conductor band \(Q_{\psi_u}\asymp U^\kappa\), native local
identification gives \(Na_1\asymp U^\alpha\), with
\(\alpha=\kappa-\lambda\). The physical annulus imposes
\[
 \kappa+4\lambda-\eta\le1+O(1/\log U),\qquad
 \alpha\ge(5\kappa-1-\eta)/4+O(1/\log U).                    \tag{15}
\]
The actual sieve row radius is \(U^\alpha\), **not**
\(Q_{\psi_u}\) or \(Nv\).

For fixed \(h,w\) and one finite native class, multiplicativity gives
a row-independent bounded column multiplier
\(\nu_h(k)1_{(k,w)=1}\) in (10), where \(\nu_h\) incorporates
the fixed presentation once and the native character of \(h\). Keep its zeros and all finite
reciprocity phases. Enlarge the positive \(a_1\)-sum to the permitted
sixth-free row domain, apply (11), and retain the same column norm.
There are \(O(U^{\lambda+\varepsilon})\) possible \(h\) in a radical
band: each radical has at most \(4^{\omega(b)}\) allocations of
exponents 2 through 5, a subpower factor. Each such \(h\) allows
\(O(U^{(1-\kappa+\lambda-\theta)/6})\) possible \(w\).
Only nonempty physical blocks are counted; negative radius exponents
do not generate fractional row counts.

For \(\ell_M/2\le\alpha\le\ell_M\), the resulting marked inverse mass
exponent is
\[
 \lambda+\frac{1-\kappa+\lambda-\theta}{6}
 +\frac{\kappa-\lambda}{3}+\frac{5\ell_M}{6}
 =\frac16+\frac{\kappa}{6}+\frac{5\ell_M}{6}+\frac{\eta}{6}.
                                                               \tag{16}
\]
Logarithmically many norm bands cost \(U^\varepsilon\). There is no
unpaid count of all physical \(v\) at conductor radius \(U^\kappa\).
All overlaps with \(w\) are included in the frozen deletion masks.

## 6. The new controlled conductor range, with literal contour cost

Use Note 27's imported global family premise \(\beta_*\le7/8\).
Choose a fresh fixed \(0<v\le1/5000\) and set
\(\delta_g(v)=3/4+2v\). Its direct/reflected bounds, including the
literal deleted Euler factors, give for nonprincipal rows
\[
 |S_u(U^x)|^2\ll
 U^{\delta_g(v)\min(x,\kappa-x)+\varepsilon}H^b,
 \quad Q_{\psi_u}\ll U^\kappa.                              \tag{17}
\]
For \(1/2\le\kappa<2m,\ \kappa<4m-1/2\), the squared centered
plain factor is at most
\(U^{2\delta_g(v)(\kappa-m)+\varepsilon}H^b\).

Combining this with (16) gives the block exponent
\[
 \frac16+\frac{5\kappa}{3}+\frac{5(r+z_J)}6-\frac{3m}{2}
          +\frac{\eta}{6}+4v(\kappa-m).                    \tag{18}
\]
Define
\[
 \kappa_{\rm sf}=\frac12+
       \left(\frac{3d}{5}-\frac12\right)r-\frac{z_J}{2}
       +\frac{9m}{10}-\frac3{2500},\qquad
 \kappa_D=\kappa_{\rm sf}-\frac3{200}.                       \tag{19}
\]
On the coarse box from Note 27 with \(0\le z_J\le2/45\),
\[
 \frac{141583}{225000}\le\kappa_{\rm sf}\le\frac{3489}{5000},
 \qquad
 \frac{17276}{28125}\le\kappa_D\le\frac{1707}{2500},
 \qquad \kappa_{\rm sf}-m\le713/2500<3/10.                  \tag{20}
\]
Write \(\kappa_1=m+2dr/3-1/750\) for the earlier cutoff.
The gain in the new defect class is uniform:
\[
 \kappa_D-\kappa_1\ge2029/56250>0.036.                      \tag{21}
\]
For the new bands \(\kappa_1\le\kappa\le\kappa_{\rm sf}-\eta/10\)
with \(\eta\le3/20\), (15) implies
\[
 \alpha\ge101/240-O(1/\log U)>
       \tfrac12(73/100+2/45),\qquad
 \alpha\le\kappa_{\rm sf}+O(1/\log U)<7/10\le\ell_M.
                                                               \tag{22}
\]
The lower branch has room \(121/3600\), and the upper branch has room
at least \(11/5000\). The plain branches in (17) also hold uniformly.
Thus every use of the sieve exponent in (16) is legal.

At \(v=0\), the moving frontier \(\kappa\le\kappa_{\rm sf}-\eta/10\)
gives exponent at most \(1+dr-1/500\): its \(-\eta/6\)
cutoff contribution exactly pays the \(\eta/6\) mass cost. The
uniform cutoff \(\kappa_D\) is its lower endpoint at \(\eta=3/20\).
The actual contour is \(v>0\); the additional cost is at most
\[
 4v(\kappa-m)\le(6/5)v\le3/12500.
 \]
Consequently
\[
 \boxed{\sum_{\substack{u:\ \psi_u^*\ {\rm nonprincipal}\\
             Q_{\psi_u}>U^{\kappa_1},\quad N\mathfrak d(v)\le U^{3/20}\\
             Q_{\psi_u}(N\mathfrak d(v))^{1/10}\le U^{\kappa_{\rm sf}}}}
 \Omega(Nu/U)|\Delta_u|^2
       \ll U^{1+dr-11/6250+\varepsilon}H^{b_D}.}             \tag{23}
\]
Its reserve over \(1/700\) is exactly \(29/87500\).
The squarefree-core case \(\eta=0,\lambda=0\) extends through
\(Q\le U^{\kappa_{\rm sf}}\) with the same conservative saving.
The argument is conditional on the global family growth and native
sieve transfer, not on selected-bin inverse pointwise control.

Finite derivative/profile orders and the height conversion must be
charged: for \(H\le U^{\eta_{\rm ht}}\), require
\[
 b_D\eta_{\rm ht}+L_{\rm other}<29/87500.                   \tag{24}
\]
The old low-conductor sector and the pair removal have their own
reserves. Internal orders precede the permitted source height schedule;
later external tail orders do not reopen those choices. The auxiliary
global disk parameter changes constants only, whereas the printed
fixed \(v\)-cost remains a power cost. No numerical detector height
schedule is inferred from (24).

## 7. An exact reduced signed high-conductor theorem

The principal/bounded-ray layer and nonprincipal \(Q\le U^{\kappa_1}\)
sector are already controlled by Note 27, with the now smaller permitted
\(v\). Add the defect sector (23), using disjoint row subsets.
Let the remaining auxiliary row predicate be
\[
 \mathcal R_D=\{u:\psi_u^*\ {\rm nonprincipal},\
 Q_{\psi_u}>U^{\kappa_1},\
 [\,N\mathfrak d(v)>U^{3/20}\ \text{or}\ Q_{\psi_u}(N\mathfrak d(v))^{1/10}>U^{\kappa_{\rm sf}}\,]\},
                                                               \tag{25}
\]
and set \(W_D(u)=\Omega(Nu/U)1_{\mathcal R_D}(u)\).
Apply the direct signed pair removal (8) to this predicate; it is
permitted because (3) is a physical finite-sum bound. The exact remaining
real signed form is
\[
 \mathcal T_D=
 X^{-1}\sum_{\substack{k,k'\\Na>B_{\rm all},\ Nb>B_{\rm all}}}
 A_c(k)\overline{A_c(k')}\mathcal H_{W_D}(k,k').             \tag{26}
\]
The new finishing theorem would be
\[
 \boxed{\mathcal T_D\ll
             U^{1+dr-1/700+\varepsilon}H^b.}                \tag{27}
\]
It is a one-sided real signed bound, not a termwise absolute bound.
Equations (8), (23) and the earlier controlled row sectors make (27)
sufficient for the full centered smooth target, after all fixed costs
fit their respective reserves. This is an exact reduction, not a proof
of (27). The conductor and defect predicates are nonradial; this new
form does not automatically inherit a radial Poisson identity.

There is a sharper direct selected alternative:
\[
 \mathcal T_{\rm sel}=
 X^{-1}\sum_{\substack{k,k'\\Na>B_{\rm sel},\ Nb>B_{\rm sel}}}
 A_c(k)\overline{A_c(k')}\mathcal H_{\mathcal C_+}(k,k').
                                                               \tag{28}
\]
Its bound at the same exponent is equivalent to the selected centered
target up to the controlled pair error (9). Note 26 then supplies the
complete original-product comparison. The auxiliary defect estimate
is unnecessary for this direct selected route. In particular the
actual selected high gate \(Q>U^{2m-1/1000}\) lies above the new
auxiliary cutoff; (23) is not claimed to control the original selected
rows themselves.

The original complete joint transform can still be used where its
smooth-domain hypotheses apply, retaining the entire coprimality sum,
native common character, both centered columns and all masks. The
cut in (26) or (28) is not positivity-preserving and must not be
discarded or smoothed without a proved comparison. The new count
does not yield a smaller nominal joint-transform width.

The legal scalar bound for the full remaining auxiliary norm still has
exponent \(1+(3/4+2v)r\), subject to Note 27's full source coefficient,
mesh and nonexceptional hypotheses. Its worst-case deficit remains at
least \(1627/7000\). The new sectors do not improve that supremum on
the entire remaining family; they identify where additional signed
correlation is now necessary.

## 8. What equal-product centering contributes to that correlation

With identical plain profiles, put
\(h_0=\log(N/Y_1)=(m-1/4)\log U\). On initial independent Mellin
lines to the right of one, the centered triple integrand contains
\[
 \frac{L_{\rm orig}(t,\psi_u)L_{\rm orig}(w,\psi_u)}
      {L_{\rm orig}(s,\psi_u)}
       [1-e^{-h_0(t-w)}].                                  \tag{29}
\]
Here \(s\) is the independent inverse argument; all original deleted
Euler factors and profile transforms remain. On a common plain line,
exchange of \(t,w\) gives the exact symmetrized multiplier
\[
 1-\cosh(h_0(t-w)).
 \]
For \(t=\sigma+i\tau_1,\ w=\sigma+i\tau_2\), it is
\[
 1-\cos(h_0(\tau_1-\tau_2)),\quad
 0\le1-\cos(\cdot)\le
           \min(2,h_0^2(\tau_1-\tau_2)^2/2).                \tag{30}
\]
It kills the common principal double residue. It does not cancel
generic reciprocal poles in \(s\), force \(s=t=w\), or localize the
surviving correlation to a shrinking difference-frequency band.
The quadratic zero supplies a power gain only with a further proved
localization or signed frequency estimate. On different real lines
the multiplier can carry a fixed power of \(U\); the bound by two
cannot be reused there.

There is a common-measure physical coefficient version. Let
\(A_q(k)\) be the original marked coefficient with plain scales
\((Ne^{-q},Ne^q)\). Then \(A_q=A_{-q}\) and
\[
 A_c(k)=A_0(k)-A_{h_0}(k)
       =-\int_0^{h_0}(h_0-q)A_q''(k)\,dq.                 \tag{31}
\]
For \(\mathcal DB(x)=xB'(x)\), the full pair derivative is
\[
 (\mathcal D^2B)(x_1)B(x_2)
 -2(\mathcal DB)(x_1)(\mathcal DB)(x_2)
 +B(x_1)(\mathcal D^2B)(x_2).                               \tag{32}
\]
The inverse Möbius coefficient, slots and all their ownership stay
unchanged. The product length and physical kernel are independent of
\(q\). Substituting (31) into (26) or (28) retains both integrals
and all their cross terms under the **same** pair cut. Its measure
cost is only \(O(\log^4 U)\) in the squared form, but (31) supplies
no fixed power saving. Separately bounding the three terms in (32)
would discard their cancellation.

For unequal ordered profiles the linear multiplier (29) remains exact;
evenness and (30)–(32) need explicit exchange symmetry. Prime extraction
preserves the relative scale ratios in both rectangles, but an unequal
individual child need not have that symmetry. The Note 18 prime-product
benchmark still has a full-size centered coefficient norm. Neither the
Möbius sign nor (30) repairs a proof reduced to that separately positive
norm.

## 9. Verification and status

The [checker](../../numerics/check_signed_high_sectors.py) and
[record](../../numerics/signed_high_sectors_record_20261009.json)
verify 7,021 exact finite assertions, with deterministic replay.
They test the full centered pair expansion, full common-support
decomposition versus gcd quotients, symmetric selected cuts and physical
zeros, the inverse-column sixth-free condition, and rational sieve,
defect, contour and reserve ledgers. They do not prove the native transfer,
source analytic inputs, ideal asymptotics, smooth Poisson, derivative
propagation or the unbounded correlation (27) or (28).

The completed results are (7)–(9), the legal marked-core bound (16),
the higher-valuation sector (23), and the exact residual (26)–(28).
The next analytic task is to bound that real signed form with its
large unmatched supports, rather than re-estimate the removed
same-support or low-defect conductor sectors. The difference-frequency
and derivative representations are interfaces for that task, not a
claimed estimate.

See the [review](../../reviews/MIXED_SIGNED_HIGH_CONDUCTOR_REVIEW_20261009.md)
for the audits and manuscript checks. The full mixed fourth theorem,
operational detector coverage, new family boundary and descent from
zeta-only quasi-RH to RH remain unproved.
