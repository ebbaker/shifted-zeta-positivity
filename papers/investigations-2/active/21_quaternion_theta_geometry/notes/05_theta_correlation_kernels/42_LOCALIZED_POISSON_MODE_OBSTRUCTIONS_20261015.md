---
research_program: PR02-CORR
parent_program: PR02
secondary_programs: [ALG, PR03]
status: globally_integrable_localization_and_modewise_obstruction
---

# A globally integrable smooth Poisson localization, and its remaining sign obstruction

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6.1-sol**, reasoning effort **ultra**, verified from this conversation’s session metadata. Separate internal derivations and exact algebra replay support the claims. Internal research continuation, not formal proof verification.

This continues [Note 38](38_POISSON_PARITY_CORRELATION_AND_HEAT_OBSTRUCTION_20261015.md) and [Note 36](36_COMPLETE_THETA_CORRELATIONS_AND_SIGN_TARGETS_20261015.md). It supplies a globally integrable smooth localization of the complete parity–Poisson formula and a direct obstruction to integrating even one undamped Poisson mode at positive time. The localization gives a source-prescribed absolute error tending to zero. It does **not** prove a stronger stationary signed estimate, an energy-relative payment, or an all-\(N\) polynomial-cutoff/Gaussian-tail mechanism.

## 1. Keep the differential operator on the complete arithmetic source

Use the notation of Note 38:
\[
C=2\cosh4r,\quad f=C^{-1/2},\quad
\tau=\tanh4r,\quad a=e^{4s}/C,\quad b=e^{-4s}/C,
\]
\[
A_{p,k}(s,r)=f\,e^{-\pi(ap^2+bk^2)}
(-1)^{pk}\cos(\pi pk\tau),\qquad p,k\in\mathbb Z,
\]
\[
\Pi=\sum_{p,k}A_{p,k},\qquad
\mathcal D=(\partial_s^2-\partial_r^2)^2
-8(\partial_s^2+\partial_r^2)+16,
\]
\[
\mathcal D\Pi/4096=\Phi(s+r)\Phi(s-r).
\tag{1}
\]
The letters \(a,b\) in this section are Gaussian coefficients, not the contour displacement or energy density used elsewhere.

For \(\varepsilon>0\), define the smooth window
\[
\Omega=s^2+r^2,\qquad \chi_\varepsilon=e^{-\varepsilon\Omega^2}.
\tag{2}
\]
The window is applied **after** the source operator \(\mathcal D\). In particular, the expression is \(\chi_\varepsilon\mathcal D A_{p,k}\), not \(\mathcal D(\chi_\varepsilon A_{p,k})\). No integration by parts is used.

Let
\[
q_0=r^2,\quad q_1=r^4-s^2r^2,\quad
b_E=(1-s^2+r^2)/2,
\]
\[
W_{j,\kappa}=e^{2t\Omega}(q_j+\kappa_j b_E)\cos(2xs).
\tag{3}
\]
Here \(\kappa_j(t,x)\ge0\) is prescribed independently of the unknown energy and locally bounded on the stated parameter domain. No new nonzero coefficient rule is asserted.

Define
\[
M^\varepsilon_j=\frac1{4096}\!
\sum_{\substack{p,k\in\mathbb Z\\pk=0}}
\int_{\mathbb R^2}\chi_\varepsilon W_{j,\kappa}
\mathcal D A_{p,k}\,ds\,dr,
\]
\[
R^\varepsilon_j=\frac1{4096}\!
\sum_{\substack{p,k\in\mathbb Z\\pk\ne0}}
\int_{\mathbb R^2}\chi_\varepsilon W_{j,\kappa}
\mathcal D A_{p,k}\,ds\,dr,
\]
\[
T^\varepsilon_j=
\int_{\mathbb R^2}(1-\chi_\varepsilon)W_{j,\kappa}
\Phi(s+r)\Phi(s-r)\,ds\,dr.
\tag{4}
\]
The zero mode belongs to the axes once. Sections 2–3 prove that these are finite and that the two displayed lattice sums may be interchanged with their integrals. Consequently
\[
\boxed{\mathcal L_j+\kappa_j E
=M^\varepsilon_j+R^\varepsilon_j+T^\varepsilon_j.}
\tag{5}
\]
This is a combined localized construction: outside the window the exterior is retained as the **complete** source. It does not assign an undamped axis or mixed correlation a finite value.

## 2. Uniform joint-escape bound for the differentiated lattice sum

For each coordinate multiindex \(\alpha\) with \(|\alpha|\le4\), there is an effective finite constant \(c_\alpha\), independent of \(s,r,p,k\), such that, with \(Z=ap^2+bk^2\),
\[
|\partial^\alpha A_{p,k}|
\le c_\alpha f e^{-\pi Z}(1+Z)^4(1+|pk|)^4
\le c'_\alpha f e^{-\pi Z/2}(1+|pk|^4).
\tag{6}
\]
Indeed, every positive-order coordinate derivative of \(\log a,\log b,\log f\), and every derivative of \(\tau\) needed here is bounded on \(\mathbb R^2\). Gaussian differentiation introduces polynomials in \(ap^2,bk^2\), and phase differentiation introduces powers of \(pk\) of degree at most four. Absorb \((1+Z)^4\) into half of the Gaussian. This argument gives constants using only elementary derivatives; their values are not needed for the integrability claim.

For \(z>0\), the decreasing Gaussian integral comparison gives
\[
\sum_{n\in\mathbb Z}e^{-\pi zn^2/2}\le1+\sqrt{2/z}.
\tag{7}
\]
Also
\[
\sum_{n\in\mathbb Z}n^4e^{-\pi zn^2/2}
\le c_4z^{-5/2},\qquad
c_4=\frac{128}{\pi^2e^2}.
\tag{8}
\]
For (8), write \(n^4=z^{-2}(zn^2)^2\), use
\((zn^2)^2e^{-\pi zn^2/4}\le(8/(\pi e))^2\), and bound
\(\sum_{n\ne0}e^{-\pi zn^2/4}\le2/\sqrt z\).

Since \(ab=C^{-2}\), summing (6) and using (7)–(8) gives
\[
\begin{split}
\sum_{p,k}|\partial^\alpha A_{p,k}|
&\le C_\alpha\bigl[
f+2\sqrt2\cosh2s+2\sqrt C+c_4^2 C^{9/2}
\bigr]\\
&\le C'_\alpha(e^{2|s|}+e^{18|r|}).
\end{split}
\tag{9}
\]
The final crude exponential bound suffices; sharp lattice asymptotics are unnecessary.

Fix a finite heat ceiling \(T\), \(\varepsilon_0>0\), and a compact parameter set on which \(t\le T\) and \(\kappa_j\) is bounded. Equations (6)–(9) majorize the absolute values of every summand in (4) by a constant times
\[
(1+\Omega^2)
\exp[-\varepsilon_0\Omega^2+2T\Omega]
(e^{2|s|}+e^{18|r|}).
\tag{10}
\]
This is integrable on \(\mathbb R^2\). In polar coordinates, the negative quartic term dominates the positive quadratic heat term and every linear exponential in every escape direction. This explicitly includes joint escape \(s,r\to\infty\), the diagonal strips where one of \(u=s+r,v=s-r\) remains bounded, and both coordinate axes. The same proof handles any additional fixed polynomial factor.

Thus the lattice sums and integrals in (4) converge absolutely, uniformly on the specified compact parameter sets with \(\varepsilon\ge\varepsilon_0\). Local compact convergence of the original differentiated identity, followed by this global domination, proves (5). The exterior is finite by the complete-source envelope, independently of any lattice estimate.

The uniformity deliberately does not extend to \(\varepsilon=0\).

## 3. A complete-source \(O(\varepsilon)\) exterior allowance

Let
\[
w_t(u)=e^{tu^2}\Phi(u),\qquad
\mathsf M_\ell(t)=\int_{\mathbb R}|u|^\ell w_t(u)\,du.
\]
All these moments are finite and locally uniform in \(t\), since the complete positive-half-line envelope is
\(\Phi(u)\le4\pi^2e^{9u-\pi e^{4u}}\) for \(u\ge0\).

Define the complete two-source moments
\[
\mu_k(t)=\int_{\mathbb R^2}\Omega^k
e^{2t\Omega}\Phi(s+r)\Phi(s-r)\,ds\,dr.
\]
The independent coordinate change \(u=s+r,v=s-r\), with
\(ds\,dr=du\,dv/2\), gives the exact formula
\[
\mu_k(t)=2^{-k-1}
\sum_{\ell=0}^k {k\choose\ell}
\mathsf M_{2\ell}(t)\mathsf M_{2k-2\ell}(t).
\tag{11}
\]
Use
\[
0\le1-\chi_\varepsilon\le\varepsilon\Omega^2,\qquad
|q_j|\le\Omega^{j+1}\ (j=0,1),\qquad
|b_E|\le(1+\Omega)/2.
\]
Then
\[
\boxed{
|T^\varepsilon_j|
\le\varepsilon\left[
\mu_{j+3}(t)+\frac{\kappa_j(t,x)}2
\{\mu_2(t)+\mu_3(t)\}
\right].}
\tag{12}
\]
Only complete-source moments through order eight occur. This estimate has no omitted mixed interactions and is locally uniform through any covered parameter collision, provided the prescribed \(\kappa_j\) is.

Equation (12) is an absolute allowance. Its right side is not a multiple of \(E\), and it need not vanish when \(E=0\). Hence it does not prove the desired signed inequality near a possible collision. Optimizing the absolute allowance over \(\varepsilon\) does not supply the missing signed energy factor. An energy-dependent selection can be made only after the required uniform signed family has been proved; it cannot substitute for that proof.

## 4. Even one undamped Poisson mode is not heat integrable

Fix \(p,k\) and a finite \(S\), and let \(r\to+\infty\), uniformly for \(|s|\le S\). Put \(z=e^{-4r}\) and \(A=e^{4s}p^2+e^{-4s}k^2\). Then
\[
C=z^{-1}+z,\quad
f=z^{1/2}(1+z^2)^{-1/2},\quad
\tau=(1-z^2)/(1+z^2).
\]
Because \(pk\in\mathbb Z\),
\[
(-1)^{pk}\cos(\pi pk\tau)
=\cos(\pi pk(\tau-1))=1+O_{p,k}(z^4).
\]
Therefore
\[
A_{p,k}=z^{1/2}
\left[1-\pi A z+
\left(\frac{\pi^2 A^2}2-\frac12\right)z^2
+O_{p,k,S}(z^3)\right].
\tag{13}
\]
The expansion may be differentiated through order four with the same order of remainder on the fixed \(s\)-strip.

For a separated term \(e^{\lambda s-ar}\), the symbol of \(\mathcal D\) is
\[
\lambda^4-(2a^2+8)\lambda^2+(a^2-4)^2.
\tag{14}
\]
It vanishes for \((a,\lambda)=(2,0),(6,\pm4),(10,\pm8)\). Thus \(\mathcal D\) kills the \(z^{1/2}\), \(z^{3/2}\), and the \(e^{\pm8s}z^{5/2}\) terms in (13). The constant-in-\(s\) part of the \(z^{5/2}\) coefficient is
\(\pi^2p^2k^2-1/2\); its symbol is \(9216\). Hence
\[
\boxed{
\frac{\mathcal D A_{p,k}(s,r)}{4096}
=\left(\frac94\pi^2p^2k^2-\frac98\right)e^{-10r}
+O_{p,k,S}(e^{-14r}).}
\tag{15}
\]
The coefficient is negative on every axis mode \(pk=0\), and positive on every mixed mode \(pk\ne0\). It is never zero. Thus for every fixed \(t>0,s\) and each mode,
\[
\int^\infty e^{2tr^2}|\mathcal D A_{p,k}(s,r)|\,dr=\infty.
\tag{16}
\]
Polynomial Laguerre weights do not repair it. Individual undamped mode integration therefore fails even if the full axis/mixed split is abandoned. Cancellation must occur before the window is removed.

There is no contradiction with Note 38's positive \(+(9/8)e^{-10r}\) tail for the summed axis sector. The fixed-mode asymptotic is not uniform in the indices as \(r\to\infty\); an infinite number of modes contribute on the changing lattice scale. Interchanging that asymptotic with the axis sum would be invalid.

The obstruction also applies to every nonempty centered finite rectangular lattice packet. For integers \(P,K\ge0\), summing (15) over \(|p|\le P,|k|\le K\) gives leading coefficient
\[
\boxed{\frac98(2P+1)(2K+1)
\left\{\frac{2\pi^2P(P+1)K(K+1)}9-1\right\}.}
\tag{16a}
\]
Here \(\sum_{p=-P}^Pp^2=P(P+1)(2P+1)/3\). The coefficient is negative if \(P=0\) or \(K=0\). If both are at least one, it is positive since \(P(P+1)K(K+1)\ge4\) and \(\pi^2>9\). Thus no finite centered rectangle has a zero leading tail, and every such unwindowed packet has divergent positive-time absolute heat integral. A finite lattice rectangle cannot itself replace the window's complete exterior.

### Finite diagonal compensation after the zero-mode addback

The simple compensated primitive \(\Pi_{\rm ax}+f\) also retains an
infinite ladder of exponential tails in joint escape. Put
\(u=s+r\), \(v=s-r\), and let \(u\to+\infty\) with \(v\) in a fixed
compact interval. Since
\[
C=e^{2(u-v)}(1+e^{-4u+4v}),
\]
its exact theta formula gives, for every fixed integer \(K\ge0\),
\[
\Pi_{\rm ax}+f=e^{u+v}+\sum_{n=0}^K e^{-(4n+1)u}F_n(v)
+O_K(e^{-(4K+5)u}),\qquad
F_n(v)=\frac{e^{-v}}{n!}\Theta^{(n)}(e^{-4v}). \tag{16b}
\]
The omitted second-theta corrections are superexponentially small and
absorbed in the remainder. All derivatives through order four obey the
same uniform expansion, by analytic Taylor expansion on a compact
positive theta-argument interval. Here \(F_0=P(v)\).

In these independent coordinates,
\[
\mathcal D/4096=(\partial_u^2-1)(\partial_v^2-1)/256.
\]
It kills \(e^{u+v}\) and \(e^{-u}F_0(v)\). For every \(n\ge1\),
\[
(F_n''-F_n)(0)=\frac{24\Theta^{(n+1)}(1)+16\Theta^{(n+2)}(1)}{n!}
=\frac{(-1)^n}{n!}\sum_{\ell\ne0}
(\pi\ell^2)^{n+1}(16\pi\ell^2-24)e^{-\pi\ell^2}\ne0. \tag{16c}
\]
All terms in the sum after its common sign are positive. The derivative
identity follows directly from
\((\partial_v^2-1)[e^{-v}g(e^{-4v})]
=e^{-v}(24y g'(y)+16y^2g''(y))\), \(y=e^{-4v}\).

Consequently subtracting the exact profiles \(n=1,\ldots,K\) from
\(\Pi_{\rm ax}+f\) leaves, after \(\mathcal D/4096\), the leading term
\[
\frac{(4K+5)^2-1}{256}e^{-(4K+5)u}
(F_{K+1}''-F_{K+1})(v), \tag{16d}
\]
with a nonzero coefficient on an open \(v\)-interval about zero and a
smaller differentiated remainder. The heat is exactly
\(e^{t(u^2+v^2)}\), so the absolute integral along this diagonal tube
diverges for every \(t>0\). This rejects every fixed-order subtraction
in this specified modular Taylor class. It does not reject arbitrary
compensation formulas that perform an exact resummation or localization.

## 5. The smooth cutoff's raw sector cost becomes enormous

This subsection concerns a raw **absolute sector budget**, not the signed value of \(M^\varepsilon_j\). Fix \(t>0\), \(\kappa_j\ge0\), and define
\[
\mathcal A^\varepsilon_j=
\int_{\mathbb R^2}\chi_\varepsilon e^{2t\Omega}
|q_j+\kappa_jb_E|
\left|\frac{\mathcal D\Pi_{\rm ax}}{4096}\right|\,ds\,dr.
\tag{17}
\]
By Note 38, on any fixed strip \(|s|\le s_0\), the last factor is at least \(c e^{-10r}\) for all sufficiently large \(r\). On that strip and at large \(r\), \(b_E\ge0\) and
\(q_j+\kappa_jb_E\ge c_jr^{2j+2}\).

Let \(R=\sqrt{t/\varepsilon}\) and restrict the integral to
\(|s|\le s_0,\ R\le r\le R+1\). Complete the square:
\[
2t\Omega-\varepsilon\Omega^2
=t^2/\varepsilon-\varepsilon(\Omega-t/\varepsilon)^2.
\]
On this strip the final square contributes only a bounded loss as \(\varepsilon\downarrow0\). Consequently
\[
\boxed{
\mathcal A^\varepsilon_j\ge
c\, (t/\varepsilon)^{j+1}
\exp\!\left[\frac{t^2}{\varepsilon}
-10\sqrt{\frac t\varepsilon}-C\right]}
\tag{18}
\]
for all sufficiently small \(\varepsilon\), with constants depending on the fixed \(t,s_0,j\). The same conclusion applies if an absolute budget also retains \(|\cos2xs|\), after shrinking the fixed \(s\)-strip so that \(|\cos2xs|\ge1/2\); on compact \(x\)-sets the strip can be chosen uniformly.

For example, choosing \(\varepsilon_N=e^{-cN^2}\) makes (12) Gaussian-small in \(N\), while (18) makes this raw absolute axis budget grow at least like
\[
\exp[t^2e^{cN^2}-O(e^{cN^2/2})].
\]
It cannot be paid by a fixed polynomial in \(N\). The example does not rule out a genuinely signed cancellation mechanism; it rejects the inference that smooth integrability plus a small complete exterior alone supplies the accepted all-\(N\) coefficient rule.

### An expanding box has a milder, but still superpolynomial, absolute cost

The same issue appears in Note 38's compact-box construction. Let
\(R_N=S_N=\tfrac12\log N\), with \(N\) sufficiently large. Its complete
exterior allowance has the Gaussian factor
\(\exp[-(\pi/2)e^{4R_N}]=\exp[-\pi N^2/2]\), with the polynomial
source moments in Note 38 retained. Define the raw box-axis absolute budget
\[
\mathcal A_{j,N}^{\rm box}=
\int_{[-R_N,R_N]^2}e^{2t\Omega}
|q_j+\kappa_jb_E|\,|\cos(2xs)|
\left|\mathcal D\Pi_{\rm ax}/4096\right|\,ds\,dr.
\]
Fix any finite \(x\) and \(t>0\). Choose \(s_0>0\) with
\(|\cos(2xs)|\ge1/2\) on \(|s|\le s_0\). On this strip and
\(r\in[R_N-1/R_N,R_N]\), the uniform axis asymptotic from Note 38
is at least \(c e^{-10r}\), while \(b_E\ge0\) and
\(q_j\ge c_j R_N^{2j+2}\) for all sufficiently large \(N\).
The strip has radial width \(1/R_N\), and
\(2tr^2-10r\ge2tR_N^2-10R_N-4t\). Thus
\[
\boxed{\mathcal A_{j,N}^{\rm box}\ge
c R_N^{2j+1}\exp(2tR_N^2-10R_N)
=c' (\log N)^{2j+1}
\exp\{(t/2)(\log N)^2-5\log N\}.} \tag{19}
\]
The constants can depend on the fixed parameters, and the last formula
absorbs the fixed powers of two. At each fixed positive time this exceeds
\(C(t,x)N^p\) for every fixed finite \(p\) and finite \(C(t,x)\) as
\(N\to\infty\). Consequently separate absolute box-sector allowances
cannot yield the adopted polynomial-cutoff transfer.

This lower bound concerns the absolute budget, not the signed box integral.
It does not reject a mechanism preserving cancellation between sectors.
Moreover, a future **signed** all-cutoff bound with an \(E\) factor and
cost \(N^p\exp\{a(\log N)^2\}\) would still exclude finite analytic
collisions by the conditional [subpower transfer in Note 44](../02_signed_cusp_control/44_SUBPOWER_CUTOFF_TRANSFER_AND_ANALYTIC_RIGIDITY_20261015.md).
The absolute budgets above have no such \(E\) factor. Their growth alone
is therefore a restriction on a particular proof strategy, not a general
impossibility theorem for collision exclusion.

## 6. What this continuation resolves and what remains open

The positive-time integrability defect can be repaired by an explicitly declared localization **before** unbounded mode integration. Equations (2), (4), (9) and (12) give a global two-coordinate construction with joint-escape control and a complete exterior allowance. Neither coordinate is constrained or replaced by the reciprocal slice \(s=0\). Every heat factor and source differential factor remains present. There are no boundary terms because neither integration by parts nor discontinuous truncation is used; moving the window inside \(\mathcal D\) would require its full commutator.

The missing theorem is still a signed estimate, for instance
\[
R^\varepsilon_j+T^\varepsilon_j\ge-M^\varepsilon_j
\quad\text{on the full stationary set }S_j=\{h_{j+1}=0\},
\qquad j=0,1,
\]
with one source-prescribed coefficient rule locally bounded through covered collisions. Equation (5) is equivalent to that target and does not establish it. The frozen zero rule \(\kappa_0=\kappa_1=0\) remains a diagnostic target, not a proved lower bound.

The window introduces no statement about the original hybrid staircase \(n\le Ne^{-2y}\), its endpoints, contour displacement, full stationary sets, or all-\(N\) predecessor-neighborhood coverage. In particular, a smooth-window calculation cannot be renamed a validation of that staircase. The principal collision-exclusion estimate and the previously established sign domains are unchanged.


## 7. Exact algebra checks and replay

The [checker](../../numerics/check_poisson_mode_cutoff_obstructions.py) independently forms the truncated generating series in \(z\), \(e^{4s}\), and \(\pi\), applies the exact differential symbol, and checks (15) in 49 fixed-mode cases. It separately sums 49 centered lattice rectangles and checks their leading coefficients, strict rational sign bounds, cutoff scaling, and the diagonal-profile differential symbol. The [receipt](../../numerics/POISSON_MODE_CUTOFF_OBSTRUCTIONS_20261015.json) records **260 exact rational assertions**. A separate internal execution produced the same receipt bytes. These finite algebra checks support normalizations; the analytic remainder and integrability arguments above establish the unbounded conclusions.

Replay using the Python standard library:

    python3 papers/investigations-2/active/21_quaternion_theta_geometry/numerics/check_poisson_mode_cutoff_obstructions.py --output /tmp/inv21-poisson-mode-replay.json

[Review 28](../../reviews/28_LOCALIZED_POISSON_AND_EFFECTIVE_BUDGET_REVIEW_20261015.md) records the independent internal checks. No full stationary pilot of a new arithmetic mechanism was run: the signed estimate needed to define such a mechanism is still absent.
