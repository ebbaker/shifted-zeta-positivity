# Correlated holomorphic payments and complete candidate coverage

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6.1-sol (Codex), reasoning effort ultra, verified from this
chat's recorded configuration. Mathematical derivations, arithmetic
replays and agent cross-readings are internal checks, not independent
mathematical review.

This continues [Heat Note 17](17_TWO_PRIORITY_CONTINUATION_AND_COMPLETE_CURRENT_GEOMETRY_20261010.md).
The bounded holomorphic remainder couples its value and derivative errors.
Keeping that coupling gives a strictly stronger collision-candidate test
and a sharp improvement of the complete-current payment. A second Schur
step also couples the second derivative error to the first two measured
errors. These improvements use the existing full approximation payment;
the missing uniform signed arithmetic margin remains a separate input.

## 1. The holomorphic error has a curved first-jet body

Fix a genuine parameter point in
\[
1\le\kappa=tL\le2,\qquad 0<t\le1/20,\qquad
L=\log(x/(4\pi)),\qquad R=1/L.
\]
Freeze time and the natural integer cutoff at this center. Set
\[
E(z)=Q_t(z)-F_{t,N}(z),\qquad
\eta=5\exp\{-tL^2/16-L/4\}>0.
\tag{1}
\]
[Heat Note 8, Proposition 1](8_SIGNED_SHRINKING_COLLISION_VECTOR_AND_PHASE_OBSTRUCTION_20261009.md)
supplies the holomorphic bound \(|E(z)|\le\eta\) on the full disk
\(|z-x|\le R\). This includes normalizer conversion, analytic
reflection and all possible changes of the natural cutoff on that disk.
The analytic approximant on the disk is \(S(z)+S^\#(z)\).
The real-axis expression \(2\Re S\) is used only for its central real
jets. The imported approximation remains
[Polymath, Theorem 1.3](https://arxiv.org/html/1904.12438v2#S1.Thmtheorem3).

Define the disk map
\[
g(\zeta)=E(x+R\zeta)/\eta,\qquad
a=g(0)=E(x)/\eta,\qquad b=g'(0)=E'(x)/(L\eta).
\]
Real symmetry makes \(a,b\) real. The Schwarz lemma applied to
\((g-a)/(1-ag)\) gives
\[
\boxed{a^2+|b|\le1.}
\tag{2}
\]
For \(|a|<1\), the transformed map vanishes at zero and has derivative
\(b/(1-a^2)\), whose modulus is at most one. If \(|a|=1\), the
maximum principle makes \(g\) constant, so \(b=0\). The
non-strict disk-bound case follows by applying the argument to
\(g/(1+\epsilon)\) and taking \(\epsilon\downarrow0\).
This is the central derivative form of Schwarz–Pick; see
[Broder, Section 2](https://arxiv.org/html/2110.04989#S2).
The elementary proof above supplies the particular consequence used here.

The exact feasible set of these real first jets, using only this local
bounded-disk information, is
\[
\mathcal C=\{(a,b)\in\mathbb R^2:a^2+|b|\le1\}.
\tag{3}
\]
Indeed, for \(|a|<1\), let \(\lambda=b/(1-a^2)\) and take
\[
g(\zeta)=\frac{a+\lambda\zeta}{1+a\lambda\zeta}.
\tag{4}
\]
Its denominator has no zero on the closed unit disk and
\[
|1+a\lambda\zeta|^2-|a+\lambda\zeta|^2
=(1-a^2)(1-\lambda^2|\zeta|^2)\ge0.
\]
The endpoint cases use \(g\equiv\pm1\). These are local analytic
error realizations, not assertions about errors of the genuine heat
approximation or prescribed arithmetic states.

At a genuine heat collision, \(Q_t=Q_t'=0\), hence
\[
\boxed{\left(\frac{F_{t,N}}\eta\right)^2+
\frac{|F_{t,N}'|}{L\eta}\le1.}
\tag{5}
\]
Writing \(S=u+iv\), this reads
\[
\left(\frac{2u}\eta\right)^2+
\frac{2|u'|}{L\eta}\le1.
\tag{6}
\]
It implies both earlier rectangular candidate tolerances, and excludes
some states that satisfy them. For example, the scaled real pair
\((F/\eta,F'/(L\eta))=(3/4,3/4)\) lies in their square but violates
(5). Thus a certified lower bound greater than one for the left side of
(5) excludes a genuine collision, retaining both coordinates together.

Two norm corollaries keep the manuscript's distinct derivative scales:
\[
\|(F,F'/L)\|\le\eta,\qquad
\left\|(F/2,2F'/L)\right\|^2\le4\eta^2
\quad\text{at a collision}.
\tag{6a}
\]
For the first, \(a^2+b^2\le a^2+(1-a^2)^2\le1\). For the
second, maximize \(a^2/4+4b^2\) under (2); the maximum is four,
at \((a,b)=(0,\pm1)\). The latter improves Heat Note 8's
\(17\eta^2/4\) joint tolerance. The former also yields the general
paid bound \(\|(Q_t,Q_t'/L)\|\ge(\|(F,F'/L)\|-\eta)_+\),
while the exact distance below retains more information.

## 2. The exact support and the stronger complete-current test

For any real \(A,B\), the support of (3) is
\[
h_{\mathcal C}(A,B)=
\begin{cases}
|B|+A^2/(4|B|),& B\ne0,\ |A|\le2|B|,\\
|A|,& |A|\ge2|B|\text{ or }B=0.
\end{cases}
\tag{7}
\]
The formulas agree at their common boundary. Maximize
\(|A|s+|B|(1-s^2)\) for \(0\le s\le1\): its maximizing point
is \(s=|A|/(2|B|)\) in the first case and \(s=1\) otherwise.
This also proves all degenerate cases directly.

Use the complete state, including its full complement and cross terms:
\[
\mathcal J=-\Im(S'\overline S)=u'v-uv',\quad
O=(u,u'/L),\quad V=(v,v'/L),\quad
\xi=(-v'/L,v),\quad j=\mathcal J/L.
\]
Then \(\xi\cdot O=j\), and the true normalized pair satisfies
\[
q=(Q_t,Q_t'/L)=2O+\eta z,\qquad z\in\mathcal C.
\tag{8}
\]
The sign of the error is immaterial since \(\mathcal C\) is centrally
symmetric. When \(V\ne0\), Cauchy–Schwarz therefore gives
\[
\boxed{\|q\|\ge
\frac{\bigl(2|\mathcal J|/L-
\eta h_{\mathcal C}(-v'/L,v)\bigr)_+}
{\sqrt{v^2+(v'/L)^2}}.}
\tag{9}
\]
Consequently a sufficient complete-current exclusion is
\[
|\mathcal J|>\frac\eta2\mathcal H_L(v,v'),\qquad
\mathcal H_L(v,v')=
\begin{cases}
L|v|+(v')^2/(4L|v|),&v\ne0,\ |v'|\le2L|v|,\\
|v'|,&|v'|\ge2L|v|\text{ or }v=0.
\end{cases}
\tag{10}
\]
If \(V=0\), consistency gives \(\mathcal J=0\), so this current
information gives no lower bound. No division by \(S\) occurs.

Bound (9) is sharp given only \((\mathcal J,V)\) and the bounded
holomorphic error jets. To attain a positive excess, select a support
point \(z_*\in\mathcal C\) in direction \(\operatorname{sgn}(j)\xi\)
and put
\[
2O=\eta z_*+
\operatorname{sgn}(j)
\frac{2|j|-\eta h_{\mathcal C}(\xi)}{\|\xi\|^2}\xi.
\]
An error with jets \(-\eta z_*\) is realizable by (4), and the
remaining real pair attains (9). If the excess is nonpositive, scale
the support point until \(\xi\cdot(\eta z)=2j\), then take
\(2O=\eta z\). The paired error yields \(q=0\).
These sharpness constructions belong to the enlarged local analytic
class; they do not generate heat-function collisions.

The earlier square test used \(L|v|+|v'|\). The new support is strictly
smaller whenever both coefficients are nonzero. With
\(r_*=(\sqrt5-1)/2\), the inclusions
\[
r_*[-1,1]^2\subset\mathcal C\subset[-1,1]^2
\]
give
\[
r_*(L|v|+|v'|)\le\mathcal H_L(v,v')
\le L|v|+|v'|.
\tag{11}
\]
The first constant is attained in support directions with
\(|v'|/(L|v|)=\sqrt5-1\). This quantifies the improvement: it
changes constants and candidate geometry, with no change of the
shrinking-sector exponential error scale.

If the full actual real pair is available, it carries more information
than the current compression. Its sharp local analytic-error bound is
\[
\|q\|\ge\operatorname{dist}(2O,\eta\mathcal C)
=\max_{\|\xi\|\le1}
\{2\xi\cdot O-\eta h_{\mathcal C}(\xi)\}.
\tag{12}
\]
The maximum includes \(\xi=0\). Equality is the standard supporting
hyperplane argument for the closest point of a closed convex set.
Equation (9) selects one such direction from the complete current;
it is not the sharpest bound when all of \(O\) is retained.

## 3. The second error jet is correlated as well

Write
\[
g(\zeta)=a+b\zeta+c\zeta^2+O(\zeta^3),\qquad
c=E''(x)/(2L^2\eta),\qquad D=1-a^2.
\]
For \(|a|<1\), the Schur transform
\[
h(\zeta)=\frac{g(\zeta)-a}{\zeta(1-ag(\zeta))}
\]
is a disk map with
\[
h(0)=b/D,\qquad h'(0)=c/D+ab^2/D^2.
\]
Applying the same derivative argument to \(h\) gives
\[
\boxed{\left|c+\frac{ab^2}{D}\right|
\le D-\frac{b^2}{D}.}
\tag{13}
\]
This retains the actual signed center of the allowed second-error
interval. At \(|a|=1\), all positive-order jets vanish and no division
by \(D\) is made. If \(|b|=D\), the second error is forced to
\(c=-ab^2/D\).

Every real triple satisfying (2) and (13) is locally realizable: put
\(\lambda=b/D\), select \(|\nu|\le1\), and compose
\[
h(\zeta)=\frac{\lambda+\nu\zeta}{1+\lambda\nu\zeta},\qquad
g(\zeta)=\frac{a+\zeta h(\zeta)}{1+a\zeta h(\zeta)}.
\]
Its second coefficient is
\(c=D\{(1-\lambda^2)\nu-a\lambda^2\}\). Constant and extremal
cases are handled separately: if \(|\lambda|=1\), take
\(h\equiv\lambda\), avoiding the removable boundary singularity
of the uncanceled fraction; if \(D=0\), take \(g\equiv a\).

At a collision, the measured finite lower jets fix
\(a=-F/\eta\) and \(b=-F'/(L\eta)\). Equation (13) then bounds
\(Q_t''-F''\) conditionally. Subsequent Schur steps can correlate
the third and fourth error jets. A negative threshold expression still
requires its signed arithmetic implication; replacing independent
Cauchy errors by their feasible Schur body does not provide that sign.

For project 09, its exact physical lower jets are
\(F/2=X_0\) and \(F'/2=A X_0-c_{\rm orb}Z_1\), where
\(A=-d\mu\) and \(c_{\rm orb}>0\) is the physical frequency
coefficient. Thus its stronger paid candidate set is
\[
\left(\frac{2X_0}\eta\right)^2+
\frac{2|A X_0-c_{\rm orb}Z_1|}{L\eta}\le1.
\tag{14}
\]
Here \(c_{\rm orb}\) is distinguished from the second error coefficient
\(c\). This retains amplitude drift and both lower tolerances. Any
dual payment optimized on this smaller set must still pay all raw-jet
residuals and the normalizer term in the threshold test.

## 4. A stronger payment on the retained complete rectangle

The unchanged [project 13 Note 3 certificate](../13_microlocal_phase_space/numerics/COMPLETE_CURRENT_RECTANGLE_CERTIFICATE_20261010.json)
encloses the full \(22066\)-term state on
\[
t_0\le t\le t_0+8\cdot10^{-6},\qquad
x_0+0.3\le x\le x_0+0.4,
\quad t_0=(2\log22066)^{-1},\quad x_0=4\pi22066^2.
\]
Its bounds give \(v>1.1208\), \(|v'|<3.447\), \(L>20\), so
the first branch of (10) applies throughout. Exact rational operations
on its retained decimal endpoints prove
\[
\frac\eta2\mathcal H_L(v,v')<0.135671,
\quad \mathcal J-\frac\eta2\mathcal H_L(v,v')>5.10786,
\quad \|(Q_t,Q_t'/L)\|>0.36.
\tag{15}
\]
The earlier square current payment was less than \(0.151649\), with
gap greater than \(5.09188\). The rectangle's direct paid derivative
already gives the stronger joint floor \(0.5\); (15) tests the new
correlated payment without extending that old certificate's domain.

The [exact checker](../../numerics/check_correlated_holomorphic_payments.py)
checks the support extremizers, boundary cases, disk-map identity,
current distance and attaining compatible quadratures, second Schur
coefficients, and the rational application (15). Its
[small record](../../numerics/CORRELATED_HOLOMORPHIC_PAYMENT_RECORD_20261010.json)
has 163340 passing assertions and binds its own source and the unchanged
old certificate. A mismatched certificate fails before its intervals are
used. Hashes identify files; rational inequalities establish the signs.

## 5. Complete coverage and the remaining arithmetic input

The companion [project 13 Note 4](../13_microlocal_phase_space/notes/4_CANDIDATE_CURRENT_ATLAS_AND_THIRTEEN_SIMPLE_ZERO_BRANCHES_20261010.md)
builds an atlas using the complete prescribed sum, physical spatial and
time transport, and the full holomorphic payment. The candidate set is
first narrowed by the value condition. On all remaining strips, paid
derivative and complete-current tests exclude joint zeros. Coverage is
verified for the full stated closed rectangle, including shared strip
boundaries; a finite sample of heights would not imply this conclusion.
Its exact domain, finite zero count, arithmetic bounds and replay are
recorded in that project note and certificate.

The certified exact domain is
\[
\mathcal R_8=[(2\log22066)^{-1},1/20]
\times[4\pi22066^2,4\pi22066^2+8].
\tag{16}
\]
All \(22066\) genuine cutoff terms are retained. The complete closed
atlas has 46 adjacent height strips: 29 exclude zeros by the paid value
test, and the 17 strips surviving that screen each pass both the paid
physical derivative and complete-current tests. On those 17 strips the
rectangular current gap exceeds \(0.11934\); on the entire rectangle
\[
\|(Q_t,Q_t'/L)\|>0.03728.
\tag{17}
\]
Thirteen disjoint bands have opposite endpoint signs and a uniform
nonzero derivative sign throughout each band. Consequently there are
exactly thirteen simple genuine heat zeros at every allowed time,
forming thirteen smooth branches, and no joint \((H_t,H_t')\) zero
anywhere on \(\mathcal R_8\). This reaches the exact time endpoint
\(1/20\); it does not extend toward zero time. The full value and
derivative payments are below \(0.009642\) and \(0.192864\).
The atlas uses the original rectangular payments for its proof, and
reports the correlated candidate test as an additional checked quantity.

The companion [project 09 Note 4](../09_prime_phase_torus/notes/4_PRESCRIBED_HEAT_WEIGHT_COVARIANCE_AND_SIGNED_HIERARCHY_20261010.md)
uses the prescribed quadratic log-weight shape to expose a signed
covariance term in a Gaussian tilt transformation. Its required signed
estimate and the costs of taking absolute values are recorded there.

Concretely, the exact prescribed weight is the mean of a Gaussian
coefficient tilt at the same physical phases. Its five-moment covariance
has the rank-one expansion
\[
\mathcal C_t=\sum_{k\ge1}\frac{(t/2)^k}{k!}
V^{[k]}(V^{[k]})^T,
\quad V^{[k]}=(X_k,Y_{k+1}+\epsilon X_{k+1},
X_{k+2},Y_{k+3},X_{k+4})^T.
\tag{18}
\]
The dual quadratic of the mean is its Gaussian averaged dual quadratic
minus \(\operatorname{tr}(\mathbb Q\mathcal C_t)\). For zero dual
parameters the leading covariance term is
\(t(2Y_4^2+3X_3X_5-\Gamma X_3^2)/2\). The complete contraction
keeps all four sine/cosine ratio/product channels. Its sign remains open.
The specified absolute coefficient/feature envelope has uniform size
\(\Theta(t e^{2\mathfrak a/t})\) on \(\kappa\in[1,3/2]\),
with \(\mathfrak a=\kappa(4-\kappa)/16\); that diverging payment
quantifies the loss of absolute recombination for this Gaussian method.
It is not a lower bound for the signed covariance, and a larger separately
proved negative margin could still dominate it. Conditioning the mean
lower coordinates does not condition every auxiliary tilted state.

[The shared review](../../reviews/HEAT_CORRELATED_PAYMENT_AND_CANDIDATE_ATLAS_REVIEW_20261010.md)
records internal derivation audits, fresh arithmetic replays and their
scope. [The shared check record](../../reviews/HEAT_CORRELATED_PAYMENT_AND_CANDIDATE_ATLAS_CHECK_RECORD_20261010.json)
binds the source files and retained outputs.

The next uniform target can now use the stronger actual candidate set
(5), the sharper complete-current support (10), or successive Schur
constraints on the complete threshold jets. Each still requires a
signed estimate for the genuine common orbit and its prescribed weights.
The finite atlas and correlated error theorem do not give an exclusion
uniform as \(t\downarrow0\), cover all positive threshold parameters,
or eliminate higher multiplicities. The RH and global Newman questions
remain open. The stable manuscript is preserved, and all new artifacts
follow [LARGE_FILES.md](../../../../LARGE_FILES.md).
