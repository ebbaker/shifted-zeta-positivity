# Joint coefficient and source currents with complete boundaries

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**. This note records exact analytic identities and a deliberately scoped no-inverse result. It does not establish the signed theta observation estimate.

The bounded experiment recommended by [coordination note 09](../00_research_coordination/09_MANUSCRIPT_RECURRENCE_INTEGRATION_AND_NEXT_CHAT_20261015.md) can be carried out explicitly. A source integration by parts reduces each physical mode to a primitive-source remainder; the finite killed current from [recurrence note 08](08_ADJOINT_RECURRENCE_ENDPOINT_EXPERIMENT_20261015.md) then supplies a joint identity with a quantitative remainder. Both lower boundaries survive. Moreover, allowing a source divergence does **not** remove the prior finite-range obstruction when both currents use polynomial source amplitudes and finitely many real frequencies. The obstruction is an elementary source differential quotient. The [signed quotient companion](../01_physical_jet_geometry/02_SIGNED_OBSERVATION_QUOTIENT_AND_COEFFICIENT_SINGULARITIES_20261015.md) refines the sufficient signed coefficient bound but does not remove the source-norm requirements used here.

## 1. Canonical source reduction

Write

\[
\lambda_n=\pi n^2,\qquad q=e^{4u},\qquad
p_n(u)=e^u e^{-\lambda_nq},\qquad
\phi_n(u)=p_n(u)(2\lambda_n^2q^2-3\lambda_nq).
\]

Direct differentiation gives

\[
p_n''-p_n=8\phi_n,\qquad
p_n(0)=e^{-\lambda_n},\qquad
p_n'(0)=-\beta_n,
\quad \beta_n=(4\lambda_n-1)e^{-\lambda_n}.
\tag{1}
\]

For any twice differentiable source weight \(w_n\), set

\[
r_n=\phi_nw_n,\qquad
K_n=\frac{p_n'w_n-p_nw_n'}8,\qquad
g_n=\frac{p_n(w_n''-w_n)}8.
\tag{2}
\]

Then the source identity is exact:

\[
\boxed{r_n=\partial_uK_n+g_n.}
\tag{3}
\]

No integrated transform, physical zero, or unknown observation is used to choose \(K_n\). The remaining differential expression \(w_n''-w_n\) is decisive: merely obtaining (3) does not make it small or favorable in sign.

For the finite endpoint reconstruction considered in the recurrence note, let \(y=x+\delta\), \(j\in\{0,1\}\), and

\[
\begin{aligned}
w_n(u)=e^{tu^2}\bigl[&\mathbf1_{n\le N}u^j\cos(yu+j\pi/2)
-A\cos(xu)\\
&+B u\sin(xu)
-C u^{j+1}\cos(xu+(j+1)\pi/2)\bigr].
\end{aligned}
\tag{4}
\]

Here \(A,B,C\) are prescribed before the calculation; the sign of the \(B\) term reflects \(H_x=-\sum_n\int\phi_ne^{tu^2}u\sin(xu)\,du\). Its integrated total is

\[
\sum_n\int_0^\infty r_n\,du
=V_N-AH-BH_x-CS,
\quad
V_N=\sum_{n\le N}h_{j,n}(t,y),\quad S=h_{j+1}(t,x).
\tag{5}
\]

Every starting observation is complete. All weights in (4) are even functions of \(u\), so

\[
w_n'(0)=0,\qquad w_n(0)=\mathbf1_{j=0}\mathbf1_{n\le N}-A.
\tag{6}
\]

## 2. A joint finite-depth identity and its full rectangular boundary

Apply the killed averaging operator from recurrence note 08 pointwise in \(u\):

\[
(Tg)_0=0,\qquad (Tg)_n=(g_{n-1}+g_{n+1})/2,
\quad g_0=0.
\]

For a fixed depth \(L\ge1\), put

\[
J_n^{[L]}=-\frac12\sum_{k=0}^{L-1}(T^kg)_n,
\qquad J_0^{[L]}=0,\qquad \varrho_n^{[L]}=(T^Lg)_n.
\tag{7}
\]

The requested joint identity is therefore

\[
\boxed{r_n=\Delta_nJ_n^{[L]}+\partial_uK_n+\varrho_n^{[L]}.}
\tag{8}
\]

For arbitrary finite \(M\ge1\) and \(U>0\), summation and integration give exactly

\[
\begin{aligned}
\sum_{n=1}^M\int_0^U r_n\,du
={}&\int_0^U\left[J_0^{[L]}-J_1^{[L]}
+J_{M+1}^{[L]}-J_M^{[L]}\right]du\\
&+\sum_{n=1}^M\left[K_n(U)-K_n(0)\right]
+\sum_{n=1}^M\int_0^U\varrho_n^{[L]}\,du.
\end{aligned}
\tag{9}
\]

Thus the finite coefficient upper boundary, source upper boundary, and both lower boundaries are present before any limit. In particular,

\[
-K_n(0)=\frac{\beta_nw_n(0)+e^{-\lambda_n}w_n'(0)}8.
\tag{10}
\]

For the physical weights (4), fixed-depth limits in (9) are justified locally uniformly on parameter sets with bounded \(A,B,C,x,\delta\) and \(t\) in a compact real interval \([t_-,T]\). The lower bound on \(t\) is relevant because \(w_n''\) contains explicit powers of \(t\); an upper bound alone is insufficient for this source-derivative estimate. Every positive-time finite-height event has a neighborhood of the stated type. For some finite \(C,d\) on each such set,

\[
|g_n(u)|\le C(1+u)^d
\exp\{Tu^2+u-(\pi/2)e^{4u}\}\,e^{-\pi n^2/2},
\tag{11}
\]

using \(2n^2e^{4u}\ge n^2+e^{4u}\). Corresponding estimates with additional polynomial factors bound \(K_n\) and its source upper boundary. Hence

\[
\mathcal M(g):=\sum_{n\ge1}n\int_0^\infty|g_n(u)|\,du<\infty,
\tag{12}
\]

the upper source flux vanishes, and the coefficient upper flux vanishes at every fixed depth. Uniformity through a hypothetical event requires the stated local bounds on the prescribed coefficients; this calculation supplies no bound for coefficients defined by division by a vanishing physical jet.

Let

\[
G_n=\int_0^\infty g_n(u)\,du,
\quad B_L(G)=\sum_{n=1}^Lq_L(n)G_n,
\quad R_L(G)=\sum_{n\ge1}s_L(n)G_n,
\tag{13}
\]

where \(q_L\) and \(s_L\) are the absorption and survival weights of the recurrence experiment. Passing to the full rectangle yields

\[
\boxed{V_N=AH+BH_x+CS+B_{\rm src}+B_L(G)+R_L(G),}
\tag{14}
\]

with complete source boundary

\[
\boxed{
B_{\rm src}
=\frac{\mathbf1_{j=0}}8\sum_{n\le N}\beta_n-\frac A{16}
=\frac{\mathbf1_{j=0}-A}{16}
-\frac{\mathbf1_{j=0}}8\sum_{n>N}\beta_n.
}
\tag{15}
\]

The primitive tail in the second expression is essential. For a complete endpoint it disappears; for a weighted endpoint, replace the indicator by those same weights in (4) and (15). Formula (15) is not obtained by replacing the finite endpoint normalization by \(1/2\).

The remainder estimate is

\[
\boxed{|R_L(G)|\le c_L\mathcal M(g)
\le\sqrt{\frac2{L+1}}\,\mathcal M(g),
\qquad c_L=2^{-L}\binom L{\lfloor L/2\rfloor}.}
\tag{16}
\]

This follows from \(s_L(n)\le nc_L\); integrating the absolute source remainder is also bounded by its right-hand side. As in the previous experiment, the estimate is sufficient for a factor-preserving mixed error after multiplication by the complete starting factor \(|W|\le\sqrt E\). It remains an approximation result.

Explicitly, define \(\widehat V_{N,L}=AH+BH_x+CS+B_{\rm src}+B_L(G)\), retain \(W=h_j(t,x)\), \(E=H^2+H_x^2\), and complete stationarity \(S=0\). Then

\[
\left|\{W^2-e^{-\delta}WV_N\}
-\{W^2-e^{-\delta}W\widehat V_{N,L}\}\right|
\le e^{-\delta}c_L\mathcal M(g)\sqrt E.
\tag{16a}
\]

A certified complete-to-finite endpoint error \(|V-V_N|\le\varepsilon_N\) adds exactly \(e^{-\delta}\varepsilon_N\sqrt E\). No finite starting factor is used.

## 3. What the two lower boundaries contain

The source boundary can be removed by a legitimate source-prescribed choice,

\[
A=2\mathbf1_{j=0}\sum_{n\le N}\beta_n,
\tag{17}
\]

which is bounded and does not use an unknown real observation. For a complete endpoint this is simply \(A=1\) on branch zero and \(A=0\) on branch one. It removes only the source lower boundary.

More generally, an endpoint multiplier \(d_n\) in place of \(\mathbf1_{n\le N}\) gives

\[
B_{\rm src}=\frac{\mathbf1_{j=0}\sum_nd_n\beta_n-A/2}{8},
\quad A=2\mathbf1_{j=0}\sum_nd_n\beta_n.
\tag{17a}
\]

For fixed bounded endpoint weights, these are still source-prescribed bounded coefficients. In particular, choosing this \(A\) and \(B=C=0\) gives a fully explicit physical joint family with zero source lower flux and the error (16a); its unresolved term is \(B_L(G)\).

The total arithmetic trace is

\[
B_{\partial}^{[L]}=B_{\rm src}+B_L(G).
\tag{18}
\]

Its exact relation to the original residual is

\[
\boxed{
B_{\partial}^{[L]}+R_L(G)
=V_N-AH-BH_x-CS.
}
\tag{19}
\]

In particular, at fixed physical parameters,

\[
B_{\partial}^{[L]}\longrightarrow V_N-AH-BH_x-CS.
\tag{20}
\]

Thus the joint current carries the same unresolved observation in its coefficient lower boundary after the source primitive has been removed. The two fluxes cannot be treated independently and then discarded. The identity supplies neither the sign of
\((W/\sqrt E)B_{\partial}^{[L]}\) nor the radial order of its positive part.

For orientation, at \(t=0\) with \(w_n(u)=\cos(yu)\), the residual is

\[
g_n(u)=-\frac{1+y^2}{8}p_n(u)\cos(yu),
\qquad
H(0,y)=\frac1{16}-\frac{1+y^2}{8}\sum_n\int_0^\infty p_n(u)\cos(yu)\,du.
\tag{21}
\]

The source reduction has removed powers of \(q\), while retaining a real oscillatory observation. This example illustrates why lower polynomial degree is not a signed estimate.

## 4. The source polynomial quotient

Fix real \(t,\omega\), a positive \(\lambda\), and let \(P(u,q)\) be a polynomial. Differentiating
\(e^{u+tu^2-\lambda q+i\omega u}P(u,q)\), with \(q=e^{4u}\), induces the operator

\[
\mathcal L_{\lambda,t,\omega}
=\partial_u+4q\partial_q+1+2tu+i\omega-4\lambda q.
\tag{22}
\]

**Polynomial-source lemma.** If \(a(u)\) is a nonzero polynomial, there is no polynomial \(P(u,q)\) such that

\[
\mathcal L_{\lambda,t,\omega}P
=(2\lambda^2q^2-3\lambda q)a(u).
\tag{23}
\]

**Proof.** The highest \(q\)-degree in the left side is one more than that of any nonzero \(P\), because \(-4\lambda q\) is the sole degree-raising term. Thus a solution must have degree one in \(q\). Matching its two positive powers forces

\[
P=-\frac\lambda2a\,q+\frac{(1-2tu-i\omega)a-a'}8.
\tag{24}
\]

Define \(D=\partial_u+2tu+i\omega\). The remaining constant coefficient is \((1-D^2)a/8\). Hence a solution exists only if

\[
D^2a-a
=a''+2(2tu+i\omega)a'
+\bigl[(2tu+i\omega)^2+2t-1\bigr]a=0.
\tag{25}
\]

If \(t\ne0\), the highest-degree term is \(4t^2u^2a\), and cannot vanish. If \(t=0\), the leading coefficient is \(-\left(1+\omega^2\right)\) times the leading coefficient of \(a\), also nonzero because \(\omega\) is real. This proves the claim. \(\square\)

For \(w=e^{tu^2+i\omega u}a(u)\), condition (25) is exactly \(w''=w\). This identifies the exceptional primitive anchor: when complex frequencies are admitted, \(t=0\), \(\omega=\pm i\), and constant \(a\) yield \(w=e^{\mp u}\), and their sum gives \(\cosh u\). The normalized imaginary anchor therefore lies in the source-primitive class, whereas no nonzero polynomial-amplitude real-frequency physical mode does. This algebraic distinction is not a claim about all possible nonpolynomial primitives.

## 5. Joint finite-range no-inverse theorem

The declared class below allows the source divergence excluded from the earlier proposition. It remains a pointwise theorem before source integration.

Fix finite ranges \(L_J,L_K\ge0\), a finite set \(\Omega\subset\mathbb R\), and real \(t\). Let

\[
J_n=e^{u+tu^2}\sum_{\substack{m\ge1\\|m-n|\le L_J}}
e^{-\lambda_mq}\sum_{\omega\in\Omega}P_{n,m,\omega}(u,q)e^{i\omega u},
\tag{26}
\]

for \(n\ge0\), and

\[
K_n=e^{u+tu^2}\sum_{\substack{m\ge1\\|m-n|\le L_K}}
e^{-\lambda_mq}\sum_{\omega\in\Omega}Q_{n,m,\omega}(u,q)e^{i\omega u},
\tag{27}
\]

for \(n\ge1\), with polynomial amplitudes \(P,Q\). Coefficients may depend on fixed external parameters and on the mode indices. Let the target be

\[
F_n=e^{u+tu^2-\lambda_nq}(2\lambda_n^2q^2-3\lambda_nq)
\sum_{\omega\in\Omega}a_{n,\omega}(u)e^{i\omega u},
\tag{28}
\]

where each \(a_{n,\omega}\) is a polynomial in \(u\).

**Theorem.** If

\[
F_n=\Delta_nJ_n+\partial_uK_n
\quad(n\ge1,\ u>0),
\tag{29}
\]

then \(a_{m,\omega}\equiv0\) for every \(m>L_J\) and every \(\omega\in\Omega\).

**Proof.** We first recall why finite square modes can be separated in this class. In a finite putative relation, divide by the least nonzero square-mode exponential. All later modes are super-exponentially small as \(u\to\infty\). A nonzero coefficient
\(\sum_\omega R_\omega(u,e^{4u})e^{i\omega u}\) cannot have that decay: take its largest \(q\)-degree and then its largest \(u\)-degree at that \(q\)-degree. Dividing by those leading growth factors leaves a nonzero finite trigonometric polynomial plus a term tending to zero. The trigonometric polynomial has positive limiting mean square and therefore has a sequence of values bounded away from zero at arbitrarily large \(u\). This contradicts super-exponential decay. Iteration separates every square mode. The same leading-degree argument separates frequencies and powers of \(q\) within each finite polynomial identity.

At each fixed index \(n\), equation (29) has only finitely many square modes, so this independence extracts a global mode \(m\) and frequency \(\omega\):

\[
\mathbf1_{n=m}(2\lambda_m^2q^2-3\lambda_mq)a_{m,\omega}
=\Delta_nP_{n,m,\omega}
+\mathcal L_{\lambda_m,t,\omega}Q_{n,m,\omega}.
\tag{30}
\]

For fixed \(m\), both coefficient sequences have finite support in \(n\), with their respective ranges. Multiply by \(n\) and sum over \(n\ge1\). The discrete first-moment boundary formula gives

\[
m(2\lambda_m^2q^2-3\lambda_mq)a_{m,\omega}
=P_{0,m,\omega}
+\mathcal L_{\lambda_m,t,\omega}
\left(\sum_{n\ge1}nQ_{n,m,\omega}\right).
\tag{31}
\]

If \(m>L_J\), the index-range restriction makes \(P_{0,m,\omega}=0\). The parenthesized expression is a polynomial, being a finite sum. The polynomial-source lemma then forces \(ma_{m,\omega}=0\). \(\square\)

For the endpoint reconstruction (4), take \(x\ge0\), \(\delta>0\), and \(N>L_J\). The mode \(m=L_J+1\le N\) has the nonzero endpoint frequency \(x+\delta\), distinct from all starting frequencies \(\pm x\). Its amplitude is a nonzero constant multiple of \(u^j\). Thus (29) cannot hold in the declared class for any scalar choices of \(A,B,C\), even after source divergences with any fixed finite range \(L_K\) are admitted.

The result does not assert that no joint identity exists. Equation (8) supplies one with a controlled residual. Nor does the theorem exclude nonpolynomial source primitives, nonlocal coefficient currents, identities only after source integration, direct signed estimates, bilocal identities, or source identities with complex auxiliary frequencies outside the declared real-frequency class. Allowing the coefficient range to contain the entire finite target can also solve the index algebra, with the complete target reappearing at its lower boundary as before.

There is also an elementary diagnostic for an unrestricted source inverse. Whenever the integral exists,

\[
\widetilde K_n(u)=-\int_u^\infty r_n(v)\,dv
\]

has \(\partial_u\widetilde K_n=r_n\), but its lower trace is
\(-\sum_n\widetilde K_n(0)=\sum_n\int_0^\infty r_n\,du\), exactly the unknown observation. Existence of a nonpolynomial primitive by itself therefore supplies no signed gain either; this diagnostic does not exclude independently controlled nonpolynomial constructions.

## 6. Consequence for the next research decision

This bounded experiment has a clear stopping rule. Enlarging finite polynomial neighboring-mode currents and adding polynomial source derivatives cannot produce an exact residual-free reconstruction of an endpoint mode beyond the coefficient boundary range. The hybrid identity gives a valid approximation and makes every endpoint explicit, but its lower coefficient trace converges to the same unresolved physical residual.

The useful next step must therefore provide additional information: an independently proved one-sided estimate for the trace in (18), or a mechanism outside the declared class with an independently controlled boundary. A new representation alone is insufficient. The fixed-length order of choices, complete stationarity, both physical branches, local boundedness through every covered positive-time finite-height event, and the full stationary starting factor remain unchanged.

The source-independence argument, the polynomial obstruction, and the local uniform bounds are analytic derivations. Finite exact checks of the source reduction and rectangular bookkeeping are distinct from those proofs and supply no theta sign theorem.

## Verification record

The [exact checker](../../numerics/check_joint_source_current.py) passes **3,803 overlapping rational assertions**, recorded in its [receipt](../../numerics/JOINT_SOURCE_CURRENT_CHECKS_20261015.json). The [review](../../reviews/10_JOINT_SOURCE_CURRENT_AND_SIGNED_QUOTIENT_REVIEW_20261015.md) distinguishes those finite algebra checks from the analytic proofs and the unresolved theta sign.
