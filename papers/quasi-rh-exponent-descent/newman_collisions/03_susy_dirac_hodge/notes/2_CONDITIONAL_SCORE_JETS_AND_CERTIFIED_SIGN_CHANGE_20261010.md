# Conditional score jets and a certified theta residual sign change

10 October 2026. Model: GPT-6 (Codex); exact serving variant and configured
reasoning effort unavailable. Derivations, replay and review are internal
LLM work, not independent mathematical validation.

This continues [Note 1](1_MOVING_THETA_GROUND_STATE_WARD_RESIDUAL_AND_GAP_LIMIT_20261010.md)
and priority 4 in [Heat Note 15](../../notes/15_SIXTEEN_PROGRAM_INITIAL_RESULTS_AND_FIVE_PRIORITIES_20261010.md).
The new actual-theta result is a uniform, outward-enclosed sign change of
the optimally fitted Gaussian score residual for \(0\le t\le1/20\).
The collision-conditioned jet dictionary then isolates the uncontrolled
signed residual moment that prevents the proposed sign closure.

## 1. State, reduction, and insertion domain

Retain exactly the genuine full even theta kernel, including all terms,
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}}\quad(u\ge0).
\]
Put \(Z_t=H_t(0)\), \(\rho_t=e^{tu^2}\Phi_e/(2Z_t)\),
\(C_t(x)=H_t(x)/Z_t\), \(W_t=-\log\rho_t\).
Thus \(H_0=\xi(1/2+ix/2)/8\), and
\[
\dot\rho_t=(u^2-\mu_2)\rho_t,\quad
\dot Z_t=\mu_2Z_t,\quad
\dot C_t=-C_t''-\mu_2C_t,\quad
\partial_t(Z_tC_t)=-\partial_x^2(Z_tC_t).
\tag{1}
\]
This retains the normalization and Newman sign from Note 1.
The score and all polynomial insertions used below are integrable with
their derivatives: \(W_t'\) grows like \(e^{4|u|}\), while theta decay
dominates that growth and every fixed Gaussian, exponential, and
polynomial factor. Every full-line integration by parts has zero boundary
term. The normalized even state, not an independently twisted state, is
used throughout the enclosed theta calculation.
For the generic positive controls compared in Section 5, require
\[
\int_{\mathbb R}e^{T u^2+Y|u|}|\phi^{(j)}(u)|\,du<\infty
\quad(T,Y\ge0,\ j\ge0)
\]
for every fixed weight, together with finiteness of the score norms
actually used. Unspecified super-exponential decay alone would not
ensure positive-time Gaussian heat integrability. The theta kernel
and the explicit control in Program 06 Note 2 meet these conditions.

At fixed time choose
\[
\beta_t=1/\mu_2(t),\qquad R_t(u)=W_t'(u)-\beta_tu,
\qquad C_j=\partial_x^jC_t(x).
\]
The choice minimizes \(\mathbb E(W_t'-\beta u)^2\), since
\(\mathbb E[uW_t']=1\). Its defect is
\[
D_0=\mathbb E R_t^2=\mathbb E W_t'^2-1/\mu_2(t)>0.
\tag{2}
\]
Beta is held fixed under every spatial derivative.

## 2. A real signed residual hierarchy through the sixth jet

Define real observations
\[
r_j(x)=i^{j-1}\mathbb E[u^jR_t(u)e^{ixu}]
=\mathbb E[u^jR_t(u)\cos(xu+(j-1)\pi/2)].
\]
Parity makes the right side real. Differentiation gives \(r_j'=r_{j+1}\).
Integrating \((u^j\rho_te^{ixu})'\) yields the exact hierarchy
\[
\boxed{r_j=jC_{j-1}+xC_j+\beta_t C_{j+1},}
\qquad 0\le j\le5,
\tag{3}
\]
with the negative-index term omitted. This is an inserted score
identity, not a new differential equation imposed on theta.

At a genuine collision \(C_0=C_1=0\), the complete list needed through
sixth order is
\[
r_0=0,\quad r_1=\beta C_2,\quad
r_2=xC_2+\beta C_3,\quad
r_3=3C_2+xC_3+\beta C_4,
\]
\[
r_4=4C_3+xC_4+\beta C_5,\quad
r_5=5C_4+xC_5+\beta C_6.
\tag{4}
\]
In particular the conditional residual does not vanish beyond its
zeroth insertion. The map \((C_2,\ldots,C_6)\mapsto(r_1,\ldots,r_5)\)
is triangular with determinant \(\beta^5>0\). Formal assignment of its
five residual moments supplies five arbitrary higher jets; this does
not assert their realization by a positive kernel. Ward algebra alone
places no sign restriction on them.

At a collision the normalized all-real-threshold expression from Note 13
equals
\[
\mathscr L(q)=(Z_t/A_t)^2\,T_C,\quad
T_C=2C_3^2-3C_2C_4-9C_2^2/x^2.
\]
Eliminating \(C_2,C_3,C_4\) using (4) gives a concrete residual target:
\[
\boxed{\beta^4T_C=
2\beta^2r_2^2-\beta x r_1r_2-3\beta^2r_1r_3
+(9\beta-x^2-9\beta^2/x^2)r_1^2.}
\tag{5}
\]
For an ordinary double zero, \(r_1\ne0\). The coefficient of \(r_3\)
in (5) is then nonzero. A bound on \(D_0\), or the identity \(r_0=0\),
does not constrain the sign of this mixed residual insertion.
At exact multiplicity three the fourth-jet test remains automatically
positive; higher deflation still requires the fifth/sixth jet data in (4).

## 3. Actual theta does not have a one-sign Gaussian-score residual

The checker encloses the score at two short positive intervals, using
theta terms \(n=1,2,3\), an explicit positive omitted-tail bound,
42-digit outward Decimal arithmetic, and the existing source-bound
time-zero moment enclosure from Program 15.

Let \(m_2,m_4\) be those time-zero enclosed moments. Since
\(\dot\mu_2=\operatorname{Var}(u^2)\le\mu_4\),
\[
\mu_2(t)\ge m_2,\qquad
\mu_2(t)\le m_2+\tfrac1{20}(e^{1/5}m_4+5\cdot10^{-37})
\quad(0\le t\le1/20).
\tag{6}
\]
For \(u\le2\), \(e^{tu^2}\le e^{1/5}\); the weighted omitted fourth
moment above two is below \(10^{-39}\), and \(Z_0>0.002\), so its
normalized contribution is below \(5\cdot10^{-37}\).
The latter mass lower bound follows directly from the enclosed theta
kernel on \([0,0.01]\).
These estimates give the conservative uniform beta range
\[
86.39010<\beta_t<86.56254.
\tag{7}
\]
The actual time-dependent score is exactly
\(W_t'=-\Phi_e'/\Phi_e-2tu\). The resulting outward enclosures imply
\[
\boxed{R_t(u)<-0.72\quad(0.1\le u\le0.1001),}
\]
\[
\boxed{R_t(u)>4.18\quad(0.3\le u\le0.301),}
\qquad 0\le t\le1/20.
\tag{8}
\]
This rules out a one-sign residual argument for the genuine theta
state across the entire stated time interval, rather than merely showing
that theta is non-Gaussian.

For transparency, set \(E_m(u)=\sum_{n\ge4}n^m e^{-\pi n^2e^{4u}}\).
The omitted pointwise derivative terms are paid using
\[
E_m(u)\le
\frac{4^m e^{-16\pi e^{4u}}}
{1-(5/4)^m e^{-9\pi e^{4u}}},
\quad m=2,4,6,
\tag{9}
\]
because \(n^m\le4^m(5/4)^{m(n-4)}\) and
\(n^2\ge16+9(n-4)\). The denominators are strictly positive on the
stated intervals. The omitted kernel tail is bounded by
\(2\pi^2e^{9u}E_4+3\pi e^{5u}E_2\); the omitted slope magnitude by
\(30\pi^2e^{9u}E_4+15\pi e^{5u}E_2+8\pi^3e^{13u}E_6\).
The finite slope uses exactly
\[
\phi_n'=(30c^2e^{9u}-15ce^{5u}-8c^3e^{13u})e^{-ce^{4u}},
\quad c=\pi n^2.
\]
All signs in the quotient interval are retained. The calculation is
not a quadrature-resolution comparison.

There is also a genuine quantitative defect bound. On the positive
interval in (8) the checker obtains \(\Phi>0.0071135\).
The full-theta Gaussian envelope gives
\(Z_t\le2\pi^2e^{-\pi}\sqrt{\pi/(8\pi-t)}<1\) for this time range:
\(3<\pi<22/7\), \(e^3>20\), and \(8\pi-t>\pi\) suffice.
For \(u\ge0\), drop the negative part of each summand and use
\(n^4\le16^{n-1}\), \(n^2-1\ge3(n-1)\), giving
\(\sum n^4e^{-\pi(n^2-1)e^{4u}}<2\).
Then \(e^{4u}\ge1+4u+8u^2\) yields
\(\Phi(u)\le4\pi^2e^{-\pi}e^{-(4\pi-9)u-8\pi u^2}\).
Dropping its additional negative linear exponent and integrating the
Gaussian proves the displayed \(Z_t\) bound.
The symmetric pair of intervals therefore pays
\[
\boxed{D_0>0.00012\quad(0\le t\le1/20).}
\tag{10}
\]
The source record's unrounded lower endpoint is approximately
0.0001243385854. This lower bound controls a bulk defect, not its
oscillatory projection. Indeed \(\mathbb E[uR_t]=0\) by the optimal
beta choice, and (4) sets its zeroth oscillatory projection to zero
at a candidate. The actual sign change makes those distinctions concrete.

The tail budget used in (6) follows from
\(\Phi(u)\le4\pi^2e^{-\pi}e^{-(4\pi-9)u-8\pi u^2}\) and
\(u^4\le100e^{u^2}\).
For \(t\le0.05\), elementary bounds \(4\pi-9>3\),
\(8\pi-1.05>22.95\), \(4\pi^2e^{-\pi}<2\) give an omitted
integral at most \((200/94.8)e^{-97.8}<10^{-39}\).
No unrecorded infinite theta tail is ignored.

## 4. Quantitative limitation of residual-to-jet recovery

Cauchy--Schwarz gives only \(|r_j|\le\sqrt{D_{2j}}\), where
\[
D_{2k}=\mathbb E[u^{2k}R_t^2]
=\mathbb E[u^{2k}W_t'']
+2k(2k-1)\mu_{2k-2}
-2\beta(2k+1)\mu_{2k}+\beta^2\mu_{2k+2}.
\tag{11}
\]
Negative-index terms are omitted. This follows from two polynomial Ward
insertions, and is valid through \(D_{10}\) needed by \(r_5\).
It supplies absolute bounds, with no sign for \(r_1r_3\) in (5).

There is an explicit high-height error amplification. If measured
\(r_1,r_2,r_3\) have errors \(\sigma_1,\sigma_2,\sigma_3\), with
beta exact, reconstruction using (4) gives
\[
\delta C_2\le\sigma_1/\beta,\qquad
\delta C_3\le\sigma_2/\beta+|x|\sigma_1/\beta^2,
\]
\[
\delta C_4\le\sigma_3/\beta+|x|\sigma_2/\beta^2
+(3/\beta^2+x^2/\beta^3)\sigma_1.
\tag{12}
\]
Thus this recovery pays an \(x^2\) amplification of the first inserted
residual error. A bulk defect estimate cannot be silently used as a
precision estimate at \(x=4\pi e^{\kappa/t}\).
In a directly measured jet scheme, errors instead propagate through (3)
as \(j\epsilon_{j-1}+|x|\epsilon_j+\beta\epsilon_{j+1}\).
If beta is enclosed rather than exact, also pay its interval width
times the measured \(C_{j+1}\), with the corresponding product error.

For any approximate \(C_2,C_3,C_4\) with errors \(\delta_j\), the
complete raw conditional sign payment is
\[
\Delta_C=4|v_3|\delta_3+2\delta_3^2+
3(|v_2|\delta_4+|v_4|\delta_2+\delta_2\delta_4)
+\frac9{x^2}(2|v_2|\delta_2+\delta_2^2).
\tag{13}
\]
Only \(T_C(v)<-\Delta_C\), conditional on an actual all-real-threshold
collision, would contradict necessity. When using the finite arithmetic
sum, retain the manuscript normalizer and its full
\(j!L^j\eta_N\) payments. The norm bound (10) has not produced (13)'s
opposite sign.

## 5. Cross-feed to theta lattice and scoped result

[Program 06 Note 2](../../06_theta_lattice/notes/2_GREEN_KERNEL_ENDPOINT_EQUIVALENCE_AND_CONDITIONAL_JETS_20261010.md)
shows that the affine theta endpoint hierarchy is shared by a normalized
positive-kernel double-zero control. Its score has the same integration-
by-parts hierarchy (3)--(4). These two Ward systems therefore do not
supply independent generic positivity constraints when combined.
The lattice coefficient dictionary or another genuine arithmetic
selection theorem must enter beyond the common identities.

The continuation establishes a true uniform theta score sign change,
a quantified Gaussian-score defect, the complete conditional residual
target, and its precise uncontrolled mixed insertion and error
amplification. It establishes no paid opposite threshold sign, genuine
collision exclusion, or endpoint coverage.

Replay [the checker](../numerics/check_conditional_score.py); the
[record](../numerics/conditional_score_record_20261010.json) binds its
source and imported moment record. Decimal semantics used by the
enclosure are documented in the primary
[Python Decimal reference](https://docs.python.org/3/library/decimal.html).
This is trusted standard-library interval arithmetic with analytic
tail proofs, not formal proof-assistant certification.
Files follow [LARGE_FILES.md](../../../../../LARGE_FILES.md).
