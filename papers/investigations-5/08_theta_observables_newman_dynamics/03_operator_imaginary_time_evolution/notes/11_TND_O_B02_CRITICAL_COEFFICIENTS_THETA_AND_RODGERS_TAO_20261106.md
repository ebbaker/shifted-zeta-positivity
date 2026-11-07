# B02: critical-curve coefficients, theta primitives and Rodgers–Tao tools

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, actual **gpt-6-astra / max**, verified in current turn metadata; branch chat0004. **TND-O-B02 — B, author-directed coefficient reconnaissance.** [Inputs11](../research-progress/handoffs/11_TND_O_B02_COEFFICIENT_INPUTS_20261106.json); [sole register](../research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md).

The author selects manuscript (5.4)–(5.5) as a useful focus and suggests the actual theta source/primitive and Rodgers–Tao tools. We use **collision** for the current event with spatial multiplicity two; higher multiplicity is specified when relevant. This note records a coefficient dictionary, a conditional real-zero benchmark, an exact primitive transfer and the connection to existing exterior-force tools. It selects no global exclusion mechanism or numerical campaign.

**Status:** direct analytical reconnaissance with one proof-author consistency pass. Local algebra and primitive transfer are derived below; the real-zero conclusion explicitly assumes a Laguerre–Pólya collision slice. No canonical collision, new canonical coefficient bound, RH result, novelty claim or independent assessment is supplied. The source, K, encoder/readout, time convention and E01/E02 qualifications are unchanged. [Source-use06](../references/06_TND_O_B02_COEFFICIENT_SOURCE_USE_20261106.md) records literature and sibling reuse.

## 1. The coefficients worth separating

Use \(h(\tau,x)=H_{\lambda_0-\tau}(x)\), \(h_\tau=h_{xx}\). At a hypothetical interior collision, set
\[
h=h_x=0,\quad a=h_{xx}\ne0,\quad b=h_{xxx},\quad c=h_{xxxx},
\qquad s=\tau-\tau_*.
\]
Manuscript (5.4)–(5.5), p.11, are
\[
x_c(\tau_*+s)=x_*-\frac ba s+O(s^2),\qquad
v(\tau_*+s)=as+\frac12\left(c-\frac{b^2}{a}\right)s^2+O(s^3).
\tag{1}
\]
It is useful to separate the amplitude \(a\) from two ratios:
\[
\beta=\frac ba,\qquad
\gamma=\frac ca-\left(\frac ba\right)^2.
\tag{2}
\]
Then \(x_c'=-\beta\), \(v'=a\), and \(v''=a\gamma\) at the event. A constant rescaling of the field changes \(a\), but leaves \(\beta,\gamma\) unchanged. Evenness gives the same \(a,\gamma\) and the opposite \(\beta\) at the reflected event.

These ratios also have an exact meaning along any regular critical curve. With \(A(\tau)=h_{xx}(\tau,x_c(\tau))\ne0\),
\[
\frac{d}{d\tau}\log|A|
=\frac{h_{xxxx}}{h_{xx}}-\left(\frac{h_{xxx}}{h_{xx}}\right)^2
=\left.\partial_x^2\log|h_{xx}|\right|_{x=x_c(\tau)}.
\tag{3}
\]
At the event this is \(\gamma\). Thus the coefficient in (5.5) measures the change of the extremum's curvature as well as the second derivative of its value. Equation (3) is a chain-rule consequence of manuscript (5.3), not a new theta inequality. The local expansion does not supply a uniform lower bound for \(|a|\) or a uniform Taylor neighborhood.

## 2. Removing the pair reveals the surrounding field

At the collision slice write
\[
h(\tau_*,x)=(x-x_*)^2U(x),\qquad U(x_*)\ne0.
\]
Here \(U\) is the manuscript's local nonvanishing factor, renamed to avoid confusing it with a theta primitive. Define
\[
\ell=\frac{U'(x_*)}{U(x_*)},\qquad
\kappa=\left(\frac{U'}U\right)'(x_*).
\]
The Taylor coefficients give \(U_*=a/2\), \(U_*'=b/6\), \(U_*''=c/12\), hence
\[
\boxed{\beta=3\ell,\qquad \frac ca=6(\kappa+\ell^2),
\qquad \gamma=6\kappa-3\ell^2.}
\tag{4}
\]
Consequently the drift in (5.4) is \(-3\ell\), and the quadratic coefficient in (5.5) is \(a(3\kappa-3\ell^2/2)\). The same \(\kappa\) is \(B_*\) in Note07's squared-gap expansion. This is the direct connection between the two requested expansions and the surrounding-factor contribution to zero dynamics. The identities are generic; useful canonical information would be a quantitative estimate on these terms, not merely the change of variables.

### A conditional sign and its limitation

Assume, additionally, that the collision slice belongs to the real Laguerre–Pólya class, with the product representation in Csordas, Definition1.1/(1.3). This is an all-real-slice hypothesis, not a premise imposed on every possible canonical collision. Write the possible Gaussian factor as \(e^{-\alpha z^2}\), \(\alpha\ge0\), and let \(\rho_j\) be the other real zeros with multiplicities, after removing the two at \(x_*\). Logarithmic differentiation yields
\[
\kappa=-2\alpha-\sum_j\frac1{(x_* -\rho_j)^2}.
\tag{5}
\]
The sum is absolutely convergent: the product has \(\sum_{\rho_j\ne0}|\rho_j|^{-2}<\infty\), while finitely many nearby zeros are separated from \(x_*\). Linear exponential factors and the regularizing linear terms in each product factor have zero second derivative. No unsubtracted principal-value formula for \(\ell\) is asserted.

For our even field \(x_*\ne0\), and the reflected zero at \(-x_*\) also has multiplicity two. Its contribution alone gives
\[
\kappa\le-\frac1{2x_*^2},\qquad
\boxed{\gamma\le-\frac3{x_*^2}-\frac{\beta^2}{3}<0.}
\tag{6}
\]
The weaker \(\gamma\le0\) is also the classical derivative Laguerre inequality \(b^2-ac\ge0\), normalized by \(a^2\). The stronger displayed bound keeps the reflected collision's explicit contribution. This is a **conditional generic real-zero benchmark**, not a new unconditional theta estimate. For a positive-curvature collision it says \(v''<0\); for negative curvature it says \(v''>0\). In either case \(|A|\) is decreasing at the event in imaginary time. This is compatible with the critical value crossing zero.

If some exterior zeros are nonreal, the sign in (5) cannot be reused. A conjugate pair \(\alpha_0\pm i\eta\) contributes
\[
-\frac{2((x_*-\alpha_0)^2-\eta^2)}{((x_*-\alpha_0)^2+\eta^2)^2}
\]
to the second logarithmic derivative, which can have either sign. Studying a collision at the boundary of an all-real regime is therefore a different task from studying one after nonreal zeros already exist. The first is the natural setting in which to investigate the real-zero Rodgers–Tao comparison; a complete canonical application must justify its product and endpoint hypotheses.

## 3. The exact theta and primitive data

At \(\lambda_* =\lambda_0-\tau_*\), use the complete source
\(F_{\lambda_*}(u)=e^{\lambda_*u^2}\Phi(u)\), and define
\[
C_j=\int_0^\infty u^jF_{\lambda_*}(u)\cos(x_*u)\,du,
\qquad
S_j=\int_0^\infty u^jF_{\lambda_*}(u)\sin(x_*u)\,du.
\]
Then
\[
C_0=S_1=0,\qquad a=-C_2,\quad b=S_3,\quad c=C_4,
\]
\[
\beta=-\frac{S_3}{C_2},\qquad
\gamma=-\frac{C_2C_4+S_3^2}{C_2^2}.
\tag{7}
\]
These are convergent exact canonical formulas at every finite candidate parameter. The complete source bounds pay the derivatives. Source positivity does not turn the signed cosine moments \(C_2,C_4\) into a positive moment matrix. Separate absolute upper bounds on \(a,b,c\) give no ratio bound without a denominator margin. A coupled estimate for \(ac-b^2\), or an independently controlled nonvanishing exterior factor, would contain the information currently missing. We cannot assign numerical canonical event coefficients without locating or hypothesizing the event; estimates along regular critical curves are another possible formulation.

For a primitive formulation, specify the **half-line theta primitive**
\[
p(u)=e^u\sum_{n\ge1}e^{-\pi n^2e^{4u}},\quad u\ge0,
\quad p''-p=8\Phi,\quad p'(0)=-\tfrac12.
\]
These are inherited complete-theta identities, including the endpoint supplied by reflection. Put
\[
J_\lambda(x)=\int_0^\infty p(u)e^{\lambda u^2}\cos(xu)\,du.
\]
For the tests used here, the exact integration-by-parts formula is
\[
\int_0^\infty\Phi f
=\frac{f(0)}{16}+\frac{p(0)f'(0)}8
+\frac18\int_0^\infty p(f''-f).
\tag{8}
\]
Take \(f=e^{\lambda u^2}\cos(xu)\), whose \(f(0)=1\), \(f'(0)=0\). The boundary at infinity vanishes by the primitive's double-exponential decay on compact parameter sets. Direct differentiation gives
\[
\boxed{8H_\lambda(x)=\tfrac12+(2\lambda-1-x^2)J_\lambda(x)
+4\lambda xJ_\lambda'(x)-4\lambda^2J_\lambda''(x).}
\tag{9}
\]
For \(n=2,3,4\), all derivatives below being in \(x\),
\[
8H_\lambda^{(n)}=
-4\lambda^2J_\lambda^{(n+2)}+4\lambda xJ_\lambda^{(n+1)}
+(2\lambda-1-x^2+4\lambda n)J_\lambda^{(n)}
-2nxJ_\lambda^{(n-1)}-n(n-1)J_\lambda^{(n-2)}.
\tag{10}
\]
These recover \(a,b,c\) from actual primitive derivatives through order six. At \(\lambda=0\), (9) reduces to the familiar \(8H_0=1/2-(1+x^2)J_0\). At an event on that slice, \(J_0(x_*)=1/[2(1+x_*^2)]\) and \(J_0'(x_*)=-x_* /(1+x_*^2)^2\); higher derivatives still determine the coefficients. This is a consistency specialization, not an assumed event at zero.

The full signed formula, including \(1/2\), must be retained. Positivity of \(p\) alone does not sign (9) or (10); no general positivity of \(J_\lambda\) is assumed. The smooth full-line Green primitive \(G_\lambda=8(1-\partial_u^2)^{-1}F_\lambda\) is a different object. In particular \(G_\lambda\ne e^{\lambda u^2}G_0\) in general; the latter would even lose integrability for positive \(\lambda\). The primitive representation gives an exact alternative input, not a demonstrated estimating advantage.

## 4. What is reusable from Rodgers–Tao

Rodgers–Tao's v5 §4 gives real-zero dynamics and finite-block interaction identities. Their §7 renormalization subtracts the classical-spacing contribution:
\[
V(r)=r^{-2}-1+2(r-1),\qquad
\widetilde E_{jk}=d_{jk}^{-2}V(g_{jk}/d_{jk}),
\quad g_{jk}/d_{jk}>0.
\tag{11}
\]
Their localization/renormalization is relevant to estimating exterior interactions. It does not remove a colliding pair's inverse-square singularity: at fixed \(d_{jk}\ne0\), \(\widetilde E_{jk}=g_{jk}^{-2}+O(1)\) as \(g_{jk}\to0\). Their proved integrated estimates use the contradiction regime \(\Lambda<0\), all-real simple zeros above \(\Lambda\), a fixed relaxation interval and growing blocks. A quantitative bound at a specific possible positive-threshold event needs additional input. The precise checked passages and PDF/HTML numbering distinction are in [receipt06](../references/06_TND_O_B02_COEFFICIENT_SOURCE_USE_20261106.md).

Removing the local polynomial factor in (4) and subtracting the reference interaction in (11) are distinct operations. In the real-zero product class, \(-\kappa\) is an exterior inverse-square sum (plus a Gaussian term), not the colliding pair's own divergent energy or the full operator expectation.

The repository already has a particularly useful local interface: [RT Note02, §4](../../../02_heat_flow_rh_applications/rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md). If a fixed contour \(\Gamma\) encloses exactly the pair with multiplicity and has nonzero field on its boundary, then at the collision
\[
\ell=\frac1{2\pi i}\oint_\Gamma\frac{H_{\lambda_*}'(\zeta)/H_{\lambda_*}(\zeta)}{\zeta-x_*}\,d\zeta,
\quad
\kappa=\frac1{2\pi i}\oint_\Gamma\frac{H_{\lambda_*}'(\zeta)/H_{\lambda_*}(\zeta)}{(\zeta-x_*)^2}\,d\zeta.
\tag{12}
\]
The residues remove the logarithmic derivative of the enclosed quadratic; the resulting function is analytic through its internal roots. This avoids dividing by \(H(x_*)=0\), but it still requires a paid nonzero boundary margin and complete boundary source errors. The paired drift variation also cancels common translation, as RT Note02 §3 explains.

This is **reuse**, not a new contour method. [RT Note03](../../../02_heat_flow_rh_applications/rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md) and its [assessment](../../../02_heat_flow_rh_applications/rodgers_tao/reviews/02_CANONICAL_TWO_ROOT_ACQUISITION_ASSESSMENT_20261026.md) already evaluated one canonical finite pilot. There the contour upper budget was 309.53 times the same-source direct budget. That comparison concerns those upper budgets and that wide-gap pilot; it is neither a speedup measurement nor a universal failure of contours. A collision-neighborhood use must specify the new consumer and show why its information differs before repeating the pilot.

## 5. Controls and analytical checks

The admitted smooth source control from manuscript §9 has, at \(\lambda_*=1/4,x_*=\pi/4\),
\[
H=c_0Q(x)(1+\cos4x),\quad
a=16c_0Q,\quad b=48c_0Q',\quad c=96c_0Q''-256c_0Q,
\]
where \(Q(x)=\int_0^\infty e^{-u^4}\cos(xu)du\) and \(Q(x_*)>0\).
It therefore gives
\[
\beta=3Q'/Q,\qquad
\gamma=6Q''/Q-9(Q'/Q)^2-16.
\tag{13}
\]
In fact \(Q''(x_*)<0\), so \(\gamma<-16\). To see this without quadrature, let \(M_j=\int_0^\infty u^je^{-u^4}du\). Then \(M_4=M_0/4\),
\(M_2\ge1/(3e)\), \(M_0\le1+1/e\), so \(M_2/M_0\ge1/[3(e+1)]>1/12\). Since \(\cos t\ge1-t^2/2\),
\[
Q''(x_*)\le -M_2+(x_*^2/2)M_4
=-M_2+\frac{\pi^2}{128}M_0<0,
\]
using \(\pi^2<10\) and \(10/128<1/12\). Negative \(\gamma\) is thus explicitly compatible with an admitted collision, without making an all-real-zero claim for this control. Its failed canonical premise remains exact theta arithmetic. Formula (9) uses the specific canonical primitive and is not claimed unchanged for this control. The broader family/domain screen remains Note08 §5 and E02/Q2; no fresh all-family certificate is claimed.

The conditional bound (6) also agrees exactly with the local even polynomial slice \((x^2-r^2)^2\): at \(x=r\), \(\beta=3/r\), \(\gamma=-6/r^2\). This polynomial is a simple coefficient check, not a positive-source control. One analytical consistency pass checked the jet factors 2/6/12, the reflected-zero contribution, the sign reversal in time, both primitive endpoints and the product derivatives in (10)/(13). No numerical or machine-algebra research was run.

## 6. Continuation

The useful focus is now **quantitative coefficient information**, with \(a\) distinguished from \(\beta,\gamma\) and from the exterior quantities \(\ell,\kappa\). A first all-real-side collision and a generic later event have different available sign structure. A proposed bound must specify that regime, the time-height neighborhood, its lower margin, and its coupled source/tail payment. The critical-curve or exterior-factor method is not yet selected as a global collision-control route.

These statements are diagnostic and conditional benchmarks. Follow the [result index](../../../../../result-summaries/README.md), [controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), [local geometry13](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [patterns index](../../../../../avoid/README.md), [reformulations01](../../../../../avoid/01_restating_the_target.md), [scoped exclusions07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and [coupled estimates12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). A sign already forced by an assumed real-zero class is not a theta-specific discriminator.

**Next: [B] TND-O-B02 — Astra:** decide the coefficient regime and an independently estimable canonical quantity before freezing a quantitative task. [Continuation12](12_TND_O_B02_COEFFICIENT_CONTINUATION_AND_MODEL_CHANGE_20261106.md) records the narrower default. Once its domain, inputs and target are fixed, the derivation/acquisition should be an E task recommended to Sol.
