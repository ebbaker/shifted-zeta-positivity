# Complex-strip carriers and sharper logarithmic derivatives

18 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6-astra (Codex)**, reasoning effort
**ultra**, verified from the current turn metadata. Separate same-model
agents checked the strip and Schwarz arguments; this is internal LLM
review, not independent specialist review.

**Status: proved in-note, conditional only on the elementary estimates
already proved in manuscript Section 3.** The carrier payment improves
from 117 E to E/64. The relative two-prime remainder has sharper first and
second derivatives, and a uniform complex-strip bound. These are auxiliary
estimates, not a theta collision exclusion or a bound on the Newman constant.

The [manuscript](../manuscript/positive_arithmetic_packets/main.tex) fixes all
normalizations. This note does not change its sources or build record.
Read the [result summaries](../../../../result-summaries/README.md), especially
[collision controls](../../../../result-summaries/12_collision_controls_and_screening.md),
and [patterns to avoid](../../../../avoid/README.md), especially
[target restatements](../../../../avoid/01_restating_the_target.md) and
[separated bounds](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).

## 1. A positive packet maps a large strip into the right half-plane

Write
\[
 H_n(t,z)=\int_0^\infty g_n(u)\cos(zu)\,du,\qquad
 g_n(u)=e^{tu^2}\phi_n(u).
\]
Throughout the main statements, \(0\le t\le1/2\). Fix an integer \(m\ge2\)
and a bounded, nonnegative coefficient sequence \((c_n)_{n\ge m}\) which
is not identically zero. Put
\[
 V(t,z)=\sum_{n\ge m}c_nH_n(t,z).
\]
Then
\[
 \boxed{\Re V(t,x+iy)>0\quad(x\in\mathbb R,\ |y|\le\pi m^2).} \tag{1}
\]

**Proof.** With \(a=\pi n^2e^{4u}\), Section 3 gives
\[
 -4a<g_n'/g_n\le-3a,\qquad g_n''/g_n\ge7a^2.
\]
The lower logarithmic-derivative inequality follows directly from
\(g_n'/g_n=2tu+9-4a+12/(2a-3)\).
For real \(y\), set \(k_y(u)=g_n(u)\cosh(yu)\). Since
\(0\le y\tanh(yu)\le|y|\),
\[
 k_y'/k_y\le-3a+|y|<0,
 \qquad
 \frac{k_y''}{k_y}
 \ge7a^2-8a|y|+y^2=(a-|y|)(7a-|y|).
\]
For \(|y|\le\pi m^2\le\pi n^2\), the last expression is strictly
positive when \(u>0\). All derivatives decay at infinity. For \(x\ne0\),
\[
 \Re H_n(t,x+iy)
 =\int_0^\infty k_y(u)\cos(xu)\,du
 =\frac1{x^2}\int_0^\infty k_y''(u)(1-\cos(xu))\,du>0.
\]
At \(x=0\) the defining integral is positive. Bounded coefficients justify
summation, and at least one summand is positive. This proves (1), including
the boundary of the strip. In particular \(V\) has no zero in this strip.

The packets \(A_{\mathcal P}\), \(C=\sum_{n\ge2}H_n\), and
\(R_{\mathcal P}\) all satisfy this theorem with their respective starting
indices. The proof depends on positive higher-mode coefficients, not on
primality or on full modular reflection.

## 2. Strip geometry gives a sharp universal derivative budget

For real \(x\), let \(\beta=(\log V)_x\). Then
\[
 \boxed{\beta^2+|\beta_x|\le\frac1{4m^4}.} \tag{2}
\]
Here "sharp" refers to the general positive-real-part strip class, not a
claim that a theta packet attains equality.

**Proof.** Set \(L=\pi m^2\), \(K=4L/\pi=4m^2\), and, for a fixed real
point \(x\),
\[
 F(\zeta)=\frac{V(t,x+K\operatorname{artanh}\zeta)}{V(t,x)},\qquad
 q(\zeta)=\frac{F(\zeta)-1}{F(\zeta)+1}.
\]
The disk maps into \(|\Im z|<L\); (1) implies \(|q|<1\), and \(q(0)=0\).
Write \(q=a_1\zeta+a_2\zeta^2+\cdots\). All coefficients here are real
by conjugation symmetry. Schwarz's lemma makes \(q(\zeta)/\zeta\) a disk
map; applying the disk automorphism taking its value \(a_1\) to zero and
Schwarz's lemma again gives \(|a_2|\le1-a_1^2\). The constant unimodular
case follows by continuity or directly. Since the second derivative of
\(\operatorname{artanh}\) vanishes at zero,
\[
 K\beta=2a_1,\qquad K^2\beta_x=4a_2.
\]
Consequently \(\beta^2+|\beta_x|\le4/K^2=1/(4m^4)\).

For the usual carrier \(A=A_{\mathcal P}\) with \(2\in\mathcal P\),
\[
 |\alpha|\le\frac18,\qquad
 \alpha^2+|\alpha_x|\le\frac1{64},\qquad \alpha=A_x/A. \tag{3}
\]
Thus the manuscript's exact identity, with \(h=H/A\), becomes
\[
 \mathcal L_0=A^2(h_x^2-hh_{xx})-\alpha_xH^2,
 \qquad |\alpha_xH^2|\le\frac{H^2}{64}\le\frac E{64}. \tag{4}
\]
Its drift equation \(h_t=-h_{xx}-2\alpha h_x\) also has \(|2\alpha|\le1/4\).
The signed first term in (4) remains uncontrolled. Merely lowering its
bounded carrier payment does not remove the collision singularity.

## 3. Stronger real-axis remainder derivatives

Let \(R=R_{\mathcal P}\) start at index \(m\), \(r=R/A>0\), and
\(d_m=1/8+1/(2m^2)\). Then
\[
 \boxed{|r_x|\le d_mr,\qquad |r_{xx}|\le d_m^2r.} \tag{5}
\]
Indeed, set \(p=(\log R)_x\), \(q=(\log A)_x\). Formula (2) gives
\(p^2+|p_x|\le1/(4m^4)\) and \(q^2+|q_x|\le1/64\). Hence
\[
 r_x/r=p-q,
 \quad
 |r_{xx}|/r\le|p_x|+|q_x|+(p-q)^2
 \le\frac1{4m^4}+\frac1{64}-2pq\le d_m^2.
\]
For \(\mathcal P=\{2,3\}\), \(m=5\), \(d_5=29/200\). Combining (5)
with the existing \(r\le\rho_5<7.3\,10^{-25}\) gives
\[
 |r_x|<1.0585\,10^{-25},\qquad
 |r_{xx}|<1.534825\,10^{-26}. \tag{6}
\]
Using the certified enclosure of \(\rho_5\) directly improves these to
\(1.051432\,10^{-25}\) and \(1.524576\,10^{-26}\), respectively.

## 4. An explicit relative error throughout the classical zero strip

On \(|y|\le1\), the proof above gives \(k_y''/k_y\ge6a^2\).
For the \(n=2\) mode and \(0\le u\le1/64\), the manuscript's local
bound \(g_2>\phi_2(0)/3\) therefore gives \(k_y''\ge288\phi_2(0)\).
The same sinc inequality used there proves
\[
 \Re A(t,x+iy)\ge\frac{\kappa_s}{4096+x^2},\qquad
 \kappa_s=\frac34\phi_2(0)=\frac67\kappa. \tag{7}
\]

Use the manuscript's \(S_m,Q_m\), and define
\[
 I_m=\frac{S_m}{4\pi m^2-10},\qquad
 \rho_{s,m}=\frac{4097I_m+2Q_m+S_m}{\kappa_s}. \tag{8}
\]
Then
\[
 \boxed{|R(t,z)/A(t,z)|\le\rho_{s,m}\quad(|\Im z|\le1).} \tag{9}
\]
To verify this, write \(g=e^{tu^2}\sum_{n\in R}\phi_n\), \(q=-g'(0)\),
\(s=g(0)\). The source majorant gives \(\int ge^u\le I_m\), hence
\(|R(z)|\le I_m\). Twice integrating by parts gives, for \(z\ne0\),
\[
 z^2R(z)=q-\int_0^\infty g''(u)\cos(zu)\,du.
\]
Here \(g''>0\), \(q\le Q_m\), \(s\le S_m\), and
\(\int g''e^u=q+s+\int ge^u\). It follows that
\[
 |z|^2|R(z)|\le2Q_m+S_m+I_m.
\]
Since \(x^2\le|z|^2\), combine this with the absolute bound and (7).
The point \(z=0\) follows from the absolute bound alone.

For \(m=5\), exact rational interval evaluation gives
\[
 \rho_{s,5}<8.474\,10^{-25}<8.5\,10^{-25}. \tag{10}
\]
Thus \(h=H/A=Z+r\), \(Z=1+H_1/A\), is holomorphic throughout the
classical strip. If a closed Jordan contour and its interior lie there
and \(|Z|>\rho_{s,m}\) on its boundary, Rouché's theorem transfers the
zero count of \(Z\) to \(H/A\), hence to \(H\). This is a usable error
contract, not an established boundary margin. Computing \(Z\) still
requires resolving its cancellation. The contour must have a separately
certified count, including multiplicities.

## 5. Scope, checks and a nonpriority extension

The [rational checker](../numerics/certify_strip_carriers.py) replays all
original table checks and certifies (6), (10), and the constants used in
the [continuation plan](06_CANCELLATION_PRESERVING_APPROXIMATION_AND_NEWMAN_ROADMAP_CODEX_20261018.md).
Its [record](../numerics/STRIP_CARRIER_CHECKS_20261018.json) distinguishes
scalar arithmetic from analytic proof. It reuses the original interval
implementation and is not an independent implementation.

The strip and logarithmic-derivative bounds (1)–(5) hold for bounded
positive higher-mode coefficients. Thus the manuscript's finite-prime
collision controls inherit the same exact logarithmic-derivative constants.
The absolute numerical tolerances (6) additionally use the original
relative-amplitude bound; for coefficients in [1-eta,1+eta], multiply
those tolerances by (1+eta)/(1-eta). Their failed premise is
complete source reflection, not (1)–(6). Reflected smooth controls fail the
specified integer-square source expansion; Euler-factor controls fail its
unchanged normalized theta coefficients. No collision exclusion follows
from the improved carrier estimates alone.

The original real bounds and this note also extend to \(0\le t\le24\):
use \(2tu\le48u\) and \(a\ge12(1+4u)>48u+9+4/7\) to keep
\(g'/g\le-3a\), while the tail majorant still has \(24<8\lambda_2\).
This larger-time extension has no apparent priority for improving
\(\Lambda\), whose useful regime is already below \(1/2\).

The [round review](../reviews/04_MANUSCRIPT_AUDIT_AND_STRENGTHENING_REVIEW_CODEX_20261018.md)
records proof coverage and remaining gaps.
