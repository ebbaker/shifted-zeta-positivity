# B02 discussion: lobe extinction and regular event coordinates

6 November 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance, actual **gpt-6-astra / max**, verified from this turn's metadata; operator-branch chat0004. **TND-O-B02 — B, event-anatomy discussion before route selection.** [Scope10](../research-progress/handoffs/10_TND_O_B02_EVENT_DISCUSSION_SCOPE_20261106.md); [input freeze10](../research-progress/handoffs/10_TND_O_B02_EVENT_DISCUSSION_INPUTS_20261106.json); [sole register](../research-progress/01_OPERATOR_ITE_RESEARCH_PROGRESS_20261106.md).

**Discussion outcome.** A double event is the extinction of a small sign lobe under a smooth heat evolution. The moving-lobe mass obeys an exact dissipation identity, so its divergent normalized kinetic form is also its divergent *relative mass-loss rate*. The critical value divided by curvature and the squared zero gap are two regular descriptions of the same leading approach. Neither supplies additional theta information. The next conceptual question is what independently estimable fact about the complete canonical source constrains this approach on a declared region. No control route is selected.

These are faithful diagnostics and direct analytical consequences, not an RH criterion or a new canonical estimate. The [manuscript](../manuscript/README.md), §§4–9 and 11, and [Note07](07_TND_O_B02_COLLISION_ANATOMY_20261106.md) supply the inherited local geometry, integral balances and explicit source control. The elementary moving-boundary identities and their interpretation below are recorded here with **proof-author checking only**; no priority, independent assessment or formal verification is claimed. The E01/E02 accepted operator scope and Q1/Q2 remain unchanged.

## 1. What the event changes

Keep the supplied complete source and calibrated prepared channel:

\[
h(\tau,x)=H_{\lambda_0-\tau}(x),\qquad h_\tau=h_{xx},\qquad
\Psi_\tau(x)=\sqrt{2/\pi}\,h(\tau,x)\chi,
\quad K=L_0-4I.
\tag{1}
\]

Increasing imaginary time decreases Newman parameter. The source convention was rechecked in [Rodgers–Tao v5, Introduction (1)–(4)](https://arxiv.org/html/1801.05914v5#S1); [use receipt05](../references/05_TND_O_B02_EVENT_DISCUSSION_SOURCE_USE_20261106.md) records the limited primary inspection.

At an interior isolated double event let
\(h=h_x=0\), \(a=h_{xx}\ne0\), \(b=h_{xxx}\), \(c=h_{xxxx}\).
For \(s=\tau-\tau_*\), \(y=x-x_*\), the leading model is

\[
h(\tau_*+s,x_*+y)=a(y^2/2+s)+O_{\rm par}(3).
\tag{2}
\]

When \(a>0\), a negative pocket between positive neighbors fills in; the signs reverse when \(a<0\). The two real zeros leave the real axis as a conjugate pair. They are not destroyed as complex zeros. Evenness supplies a reflected event at \(-x_*\); canonical positivity rules out \(x_*=0\).

The prepared position amplitude and its first radial derivative vanish across the angular cross-section at this position, while its time derivative is nonzero. The Hilbert-space state remains nonzero, its angular channel stays fixed, and its finite operator moments remain regular. No angular transition, singular generator, or blow-up of total field energy is forced. These assertions are conditional on an event; no theta event is located here.

## 2. The lobe loses mass by an exact law

For \(\tau<\tau_*\) sufficiently close to the event, let \(r_-<r_+\) be the two simple roots and \(I_\tau=(r_-,r_+)\). Its sign \(\sigma=\operatorname{sgn}h\) is constant inside the lobe. Define

\[
L=\int_{I_\tau}|h|\,dx,\qquad
M=\int_{I_\tau}h^2\,dx,\qquad
T=\int_{I_\tau}h_x^2\,dx.
\tag{3}
\]

Here \(L\) is an absolute amplitude area, \(M\) a squared-amplitude mass, and \(T\) the local Dirichlet form. Neither \(L\) nor \(M\) is a conserved probability.

**Moving-lobe identities.** Throughout such a simple-root interval,

\[
L'=-|h_x(\tau,r_-)|-|h_x(\tau,r_+)|,
\qquad M'=-2T,
\tag{4}
\]
\[
T'=[h_xh_{xx}]_{r_-}^{r_+}-2\int_{I_\tau}h_{xx}^2\,dx.
\tag{5}
\]

For (4), Leibniz differentiation has no endpoint term because \(h=0\) at both moving endpoints. Thus \(L'=\sigma[h_x]_{r_-}^{r_+}\), with endpoint slopes pointing into and out of a lobe of sign \(\sigma\); this gives the first formula. Integration by parts gives \(M'=2\int hh_{xx}=-2\int h_x^2\). For (5), retain the moving-endpoint terms in \(T'\). Simple-root differentiation gives \(r_\pm'=-h_{xx}/h_x\). Therefore

\[
T'=2[h_xh_{xx}]_{r_-}^{r_+}-2\int h_{xx}^2
       +h_x(r_+)^2r_+'-h_x(r_-)^2r_-'
   =[h_xh_{xx}]_{r_-}^{r_+}-2\int h_{xx}^2.
\]

All differentiations occur strictly before the event, where the endpoints are smooth and simple. Limits at the collision are taken only afterward. In particular, local kinetic energy has a boundary term; its derivative must not be replaced by the full-line dissipation formula.

Because \(M>0\), an exact consequence is

\[
\frac TM=-\frac12\frac{d}{d\tau}\log M.
\tag{6}
\]

This explains the divergent local quotient without postulating an energy catastrophe. With \(\epsilon=\tau_*-\tau\), the inherited asymptotics give

\[
M\sim\frac{16\sqrt2}{15}a^2\epsilon^{5/2},\qquad
T\sim\frac{4\sqrt2}{3}a^2\epsilon^{3/2},\qquad
\frac TM\sim\frac5{4\epsilon}.
\tag{7}
\]

Both contributions vanish, while their relative loss rate diverges. Equation (6) is derived independently of (7); we do not differentiate an uncontrolled asymptotic remainder. The global mass and kinetic form remain smooth. Multiplying \(M,T\) by the common angular normalization \(2/\pi\) leaves (6) unchanged. Extension of the lobe by zero lies in the form domain \(H^1\), but generally not the operator domain \(H^2\), because the endpoint derivatives jump.

There is also a scale-free check. Let \(\delta=r_+-r_-\). Since \(\delta^2\sim8\epsilon\),

\[
L\sim\frac{|a|}{12}\delta^3,\quad
M\sim\frac{a^2}{120}\delta^5,\quad
T\sim\frac{a^2}{12}\delta^3,\quad
\delta^2\frac TM\longrightarrow10.
\tag{8}
\]

After centering at the root midpoint and rescaling the interval to \([-1,1]\), the leading amplitude is proportional to \(t^2-1\). Its normalized shape is regular. The divergence of \(T/M\) is the inverse-square spatial scale of that shrinking lobe; it does not establish a growing global high-frequency energy population.

## 3. Regular coordinates describe the same approach

Along the nondegenerate critical curve \(h_x(\tau,x_c(\tau))=0\), set
\(v=h(\tau,x_c)\), \(A=h_{xx}(\tau,x_c)\). The inherited identities and one more chain rule give

\[
x_c'=-\frac{h_{xxx}}A,\qquad v'=A,\qquad
A'=h_{xxxx}-\frac{h_{xxx}^2}{A}.
\tag{9}
\]

Thus the critical value is increasing at a nondegenerate minimum and decreasing at a nondegenerate maximum. This monotonicity is generic heat behavior. It supplies no canonical barrier against crossing zero. The critical curve can also cease to be nondegenerate when \(A=0\); its persistence over a larger region needs separate payment.

While \(A\ne0\), the amplitude-scale-invariant coordinate

\[
\rho=-\frac vA
\quad\hbox{satisfies}\quad
\rho'=-1-\rho\frac{A'}A.
\tag{10}
\]

Immediately before a double event, \(\rho>0\), and
\(\rho=\epsilon+O(\epsilon^2)\), \(\rho'(\tau_*)=-1\).
It is a local coordinate with a remaining-time asymptotic, not a source-independent prediction of the event time or a global clock.

For comparison, factor \(h=(x-r_-)(x-r_+)G\) locally, with \(G\ne0\), and write
\(q=\delta^2\), \(g=G_x/G\),
\(B(\tau)=\int_0^1g_x(\tau,r_-+t\delta)\,dt\).
The inherited exact equation is

\[
q'=-8-4qB,\qquad q/8=\epsilon+O(\epsilon^2).
\tag{11}
\]

Hence \(\rho\) and \(q/8\) agree to leading order; their higher corrections differ. They are useful coordinate choices, not two independent source constraints. The critical point is generally not the root midpoint: their event velocities are \(-b/a\) and \(-2b/(3a)\).

An instructive limitation is immediate. A bound \(|B|\le C\) yields
\(q'\le-8+4Cq\). If \(C>0\) and \(0<q\le1/C\), this is at most \(-4\); for \(C=0\), the rate is exactly \(-8\). A bounded regular correction therefore does not create a repulsive barrier arbitrarily close to a separated double collision. This does not exclude using quantitative bounds on \(B\), together with earlier gap data and a finite time budget, to control entry into that region. The bound and cluster assumptions must persist for any integrated conclusion. No all-height estimate is obtained.

## 4. What the positive source is doing

At the event, the positive momentum source has three signed observations:

\[
\int F_{\lambda_*}(u)\cos(x_*u)\,du=0,\qquad
\int uF_{\lambda_*}(u)\sin(x_*u)\,du=0,
\quad
\int u^2F_{\lambda_*}(u)\cos(x_*u)\,du=-a\ne0.
\tag{12}
\]

All integrals here are over \([0,\infty)\). The first two impose cancellation and stationarity. The third determines how the cancellation is crossed as damping changes. At equal positive/negative cosine-sector masses \(A_+=A_-=A_0\), let \(B_\pm\) be their linear-source mean \(u^2\). Then \(a=-A_0(B_+-B_-)\). For an upward crossing, the negative cosine sector has larger mean \(u^2\) and decays faster under \(e^{-\tau u^2}\).

The spatial heat-average account says the same event has equal opposing Gaussian-weighted masses and centroids at an earlier time, with unequal variances. Those are descriptions of the balance, not contradictions to positivity. They use signed position amplitudes; the positive momentum source and the spectral energy measure \(|F|^2du\) are different objects. In particular, no covariance identity may silently interchange \(F\) and \(|F|^2\).

The joint event also has a nonsingular Jacobian:
\(D_{(\tau,x)}(h,h_x)=\bigl(\begin{smallmatrix}a&0\\b&a\end{smallmatrix}\bigr)\).
Its determinant \(a^2>0\) explains persistence under small admissible source perturbations. Two equations in spacetime do not make an interior double event a fragile coincidence. This local stability changes neither the canonical source nor its arithmetic: generic source perturbations leave that class. It provides no evidence of a nearby theta event.

## 5. Controls and the information still missing

The explicit control in manuscript §9 is

\[
\Phi_{\rm c}(u)=c_0e^{-u^2/4}
\{e^{-u^4}+\tfrac12e^{-(u-4)^4}+\tfrac12e^{-(u+4)^4}\}.
\]

At \(\lambda_*=1/4,x_*=\pi/4\), it has \(H=c_0Q(x)(1+\cos4x)\), \(Q(x_*)>0\), \(a=16c_0Q(x_*)>0\). With \(\lambda_0=1/2\) the event is interior, at \(\tau_*=1/4\). Its complete source moments and power domains were paid by E01/E02. It satisfies every new identity (4)–(11) on its local simple-root lobe and their displayed limits. The failed canonical premise is its exact unit-weight theta arithmetic, not positivity, smoothness or operator regularity. No equation here uses that failed premise.

For the broader [control register](../../../../../result-summaries/12_collision_controls_and_screening.md), retain E02's Q2 rather than inventing new domain certificates:

| Control class | Failed premise or scope boundary relevant here |
| --- | --- |
| Euler-factor densities | Unchanged canonical coefficients; generic density heat evolution remains applicable |
| Weighted squares and finite-prime controls | Complete unit weights and/or full reflection; only members with the paid moment domains enter this encoder |
| Reflected, smooth-shape and positive-primitive densities | Exact canonical arithmetic; the explicit reflected witness above is fully admitted |
| Atomic controls | The ambient L²-density encoder; no new measure-valued realization is claimed |
| Continuous compact profiles and conditional endpoint controls | Canonical coefficients/full source profile, or ordinary Dirichlet-series arithmetic; inherited existence/domain qualifications remain |
| Fixed amplitude with changed kernel | The literal Fourier/cosine observation and Newman equation; not an event of this fixed readout |

These are premise distinctions, not proof that a proposed quantitative theta estimate rejects any control. No such estimate is proposed here. The quadratic model \(h=a(y^2/2+s)\) checks the moving-boundary constants analytically, but is only a local model; the displayed source is the actual admissible witness.

## 6. Consequence for the discussion

The useful distinction is between **the universal terminal shape** and **why the canonical orbit can or cannot reach it on a specified time-height region**. A generic smoothness or energy-monotonicity argument cannot distinguish the admitted witness. A source-sensitive estimate still might; the present discussion has not supplied one.

Before choosing a route, identify which information is actually available from the complete theta source: a coupled critical-value/curvature estimate, a quantitative contribution of the surrounding factor with initial gap data, or a controlled signed interference estimate. These are alternative descriptions to discuss, not three activated research campaigns. An eventual comparison should specify the region, independent inputs, actual error and the same-information scalar baseline before adding a new criterion. Merely naming the source's arithmetic is not an estimate.

This pass keeps the event interior, isolated and double. Higher multiplicities use the inherited finite heat-polynomial analysis; a global claim also needs endpoint and height control, and cannot assume a first finite-height collision. No source-specific bound, canonical event, global exclusion, computational advantage or new manuscript milestone is claimed.

One analytical consistency pass checked endpoint signs and moving-boundary terms in (4)–(5), the exact quadratic model's constants in (7)–(8), the chain rule in (9)–(10), the time orientation in (11)–(12), and the control's admissibility. No numerical campaign or machine-algebra verification was run. This remains same-author checking.

Follow the [result index](../../../../../result-summaries/README.md), [local geometry cluster](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [patterns index](../../../../../avoid/README.md), [target classification](../../../../../avoid/01_restating_the_target.md), [re-realization boundary](../../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md) and [scoped exclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md). The account is a diagnostic clarification within B02, not a quantitative milestone toward RH.

**Next: [B] TND-O-B02 — Astra.** Continue the discussion about which independently estimable canonical-source information could constrain entry into this local event geometry. [Continuation09](09_TND_O_B02_DISCUSSION_CONTINUATION_AND_MODEL_CHANGE_20261106.md) records the open decision and model handoff. No route or successor E contract is selected.
