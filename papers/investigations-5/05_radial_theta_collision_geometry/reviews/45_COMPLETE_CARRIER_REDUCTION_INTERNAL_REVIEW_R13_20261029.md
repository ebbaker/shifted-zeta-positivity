# Complete carrier reduction: internal review of R13

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort ultra**,
Investigation05 **chat0033**. Same-model contributing audit with shared
R10–R12 premises and parent synthesis; **not independent or specialist
review**. The parent has synthesized the issued notes; fixed E08 assessment remains pending.

**Disposition: pass at the stated fixed-mark scope.** The checked
[complete-balance transfer][n89] pays finite absolute differences of the
entire production and exact dissipation. The checked [feedback and
candidate note][n90] pays the scalar-ratio defect, its weak equation
forcing, and convergence with finite variation of the carrier's squared
L2 norm. Its unique smooth radial stationary candidate is correctly
separated from unproved stationary convergence. These are quantitative
auxiliary-flow results on the already admitted physical mark, obtained
by the equally informed direct method.

This review read the complete final Note89 and Note90 drafts in the R13
temporary directory, their contributing drafts, the frozen intake, and
the relevant accepted formulas in [Notes67][n67], [82][n82], [83][n83]
and [Review43][r43]. The radial-square coefficients were checked against
[Note42][n42]. No manuscript or repository file was edited by this
contributor. No numerical evidence or new source acquisition is used.

## 1. Exact common-path decomposition and balance — pass

The same original \(\alpha(s)\) drives actual, carrier and error
fields. The identities

\[
 W=ah+e,\quad J_2=a_2h+e_2,\quad Z=Z_c+Z_e,
 \qquad
 Z_c=\omega[a\mathcal A_T h-\tau h],
\]

with \(\tau=(2a_1,a_1+2a_2)\), preserve the complete residual
relation. Each triple obeys
\(F'+\mathcal D_s=\mathcal P_s\) with its **instantaneous** field
energy in the radial identity. The carrier and centered energies are
not assumed conserved; their feedback is not recomputed. No derivative
of the coefficient is needed. The exact production includes full
\(C_0,C_1\), the weight potential, gradient production, second-jet
energy and the whole radial remainder through the exact dissipation.

## 2. Spatial form domain and absolute coefficient bound — pass

Note89 explicitly freezes the actual coefficient and proves its
diagonal estimate for arbitrary radial spatial triples with
\(w\in H^2\), \(z,j\in L^2\). No solution, conserved-energy,
feedback or canonical-residual restriction is imposed on the test
triple. This is sufficient for polarization and avoids a nonlinear
solution-set assumption.

The bound
\(\|\omega C_0w\|_2\le A_2\sqrt N+A_1\sqrt G+A_0\sqrt E\)
retains the full Hessian term. Whole-space
\(\|D^2w\|_2^2=\|\Delta w\|_2^2\) is the required derivative
payment. Direct checking gives
\(2|\nabla\log\omega|^2\le8\),
\(h_\omega\le265/24\), \(d\le6\). Every entry in the stated
maximum \(C_P\) follows from the corresponding coefficient of
\(N,G,E,Y,Q\) by \(2\sqrt{xy}\le x+y\). This is an absolute
spatial-form estimate, with no extra diffusion absorption.

## 3. Production polarization and window summation — pass

For \(V=N+E+F\), the checked estimate
\(|\mathcal P_s(X)|\le C_PV(X)\) implies
\(|p_s(X,Y)|\le C_P\sqrt{V(X)V(Y)}\) by symmetric polarization
and rescaling. The vector space and coefficient remain fixed in this
argument. Using \(X_c=X_a-X_e\) gives

\[
 |\delta P|\le2C_P\sqrt{V(X_a)V(X_e)}+C_PV(X_e).
\]

R11 supplies the actual unit-window integral \(V_A\); R12 supplies
the centered tail \(V_e e^{-B(t)/2}\). Cauchy–Schwarz on each
\([t+k,t+k+1]\), then \(B(t+k)\ge B(t)+a_*k\), yields exactly

\[
 \int_t^\infty|\delta P|
 \le2C_PS_*\sqrt{V_AV_e}\,e^{-B(t)/4}
        +C_PV_e e^{-B(t)/2},\qquad
 S_*=(1-e^{-a_*/4})^{-1}.
\]

The initial window is included. In particular the \(C_0\) pairing is
paid without a pointwise uniform \(H^2\) bound on either actual or
carrier fields. No circular use of the conclusion pays an input.

## 4. Exact dissipation and the two-versus-one \(N\) cost — pass

The exact balance contains \(2N\), whereas the retained R11/R12
inequalities contain \(N\) after absorption. The resulting exact
budgets are \(2Q_A\) for each actual unit window and
\(2\Lambda e^{-B(t)/2}\) for the centered tail. The representation
of \(\mathscr H_{\rm rad}\) as squared linear features has the
correct nonnegative weights

\[
 g_v(q)=\frac{11+5q}{(1+q)^2},\qquad
 p_v(q)=\frac{q(203+59q+69q^2+21q^3)}{4(1+q)^4}.
\]

Cauchy–Schwarz for the entire feature vector therefore proves

\[
 \int_t^\infty|\delta D|
 \le4S_*\sqrt{Q_A\Lambda}\,e^{-B(t)/4}
                   +2\Lambda e^{-B(t)/2}.
\]

This includes every gradient, second-derivative and radial term. The
carrier's finite-window second-derivative cost follows by subtraction;
it is not an independently assumed regularity budget.

## 5. Preparation, sphere cancellation and the meaning of finite totals — pass

The whole-space estimates retain the inner ball and the combined sphere
cancellation. Neither raw carrier nor raw centered mismatch is reset
to zero. In particular the inherited centered raw mismatch is
\(-a\mathcal A_T h^{\rm raw}+\tau h^{\rm raw}\), and primitive
centered endpoint factors \(\delta_{j0}-a_j\) remain present. The
new comparison requires no separate unpaid boundary estimate.

Both differences are formed at each finite time and then integrated.
The conclusion is not finite total dissipation of actual or carrier
fields, and it does not subtract two divergent total integrals. The
decaying energy difference obeys

\[
 \delta F'+\delta D=\delta P,
 \qquad \int_t^\infty(\delta P-\delta D)=-\delta F(t).
\]

This gives finite variation of \(\delta F\), without a sign or
convergence claim for either full weighted energy. No improvement to
the inherited uniform \(F_*\) allowance is established.

## 6. Feedback denominator, exact signs and all-time constants — pass

The physical floor gives \(n=|a|^2\ge n_*=(70/73)^2\), and carrier
domination gives \(D_h\ge3E_h\ge3E_0\). Thus the correct denominator
is \(nD_h\ge3n_*E_0\). No individual signed jet mass is assumed
nonzero. The exact identity is

\[
 \alpha-\alpha_h
 =\frac{2\Delta G-\alpha\Delta D}{nD_h},\qquad
 \Delta G=2\langle\nabla W,\nabla e\rangle-G_e,\quad
 \Delta D=2\langle dW,e\rangle-\int d|e|^2.
\]

The minus signs follow from \(ah=W-e\). The constants in Note90,

\[
 d_1=\frac{4\sqrt{KE_0T_\Sigma}
                  +12\bar\alpha\sqrt{E_0L_\Sigma}}{3n_*E_0},
 \qquad d_2=\frac{2T_\Sigma+6\bar\alpha L_\Sigma}{3n_*E_0},
\]

correctly prove the defect bound for every time, with no late-time
threshold. The factors \(4\) and \(2\) in its \(\alpha\)-weighted
tail are exact integrations of the displayed exponentials. The
unweighted tail costs \(a_*^{-1}\). A limiting difference of accumulated
coefficients does not establish convergence of their derivatives.

## 7. Unbounded drift and the actual forced scalar equation — pass

The inherited moment bound is
\(\bar R=\max(R_0,3M/a_*)\); its initial \(R_0\) includes the
unit-Gaussian preparation cost \(6M\). Since \(|v|\le2|X|\),
\(\int|v|h\le2\sqrt{M\bar R}\). This pays the forcing against
compactly supported smooth tests with gradient bounded by one.
The exact identity

\[
 h_s=\Delta h+\alpha_h(h)\operatorname{div}(vh)
              +(\alpha-\alpha_h(h))\operatorname{div}(vh)
\]

is therefore accompanied by a finite tail in the stated dual-Lipschitz
seminorm. It describes the original carrier and introduces no second
evolution. It supplies neither an \(L^2\) forcing estimate nor nonlinear
shadowing in a stronger topology. Those distinctions are explicit.

## 8. Scalar norm limit and finite variation — pass

The derivative \(E_h'=(\alpha-\alpha_h)D_h\), together with
\(D_h\le6M^2D\), gives the stated finite-variation tail. The exact
relation
\(E_0-nE_h=2\langle W,e\rangle-\|e\|_2^2\) independently
identifies the limit and its rate:

\[
 \left|E_h-\frac{E_0}{n}\right|
 \le\frac{2\sqrt{E_0L_\Sigma}}n e^{-B/4}
                         +\frac{L_\Sigma}n e^{-B/2}.
\]

This is convergence of the scalar squared norm. The audit finds no
justification for upgrading it to profile convergence, gradient-norm
convergence, or a limit of \(\alpha\); Note90 makes no such upgrade.

## 9. Unique stationary candidate and the exact dynamical gap — pass, bounded class

For the displayed potential \(\mathcal V=r^2/2+\tfrac12\log(1+r^2)\),
radial zero flux classifies nonzero nonnegative smooth radial equilibria
in the stated integration domain as
\(h_\lambda=M e^{-\lambda\mathcal V}/Z(\lambda)\), \(\lambda>0\).
The origin removes the integration constant; Gaussian decay justifies
the feedback identity \(\alpha_{h_\lambda}=\lambda\).

The derivative
\(\frac d{d\lambda}\log Q
=2(\mathbb E_\lambda\mathcal V-\mathbb E_{2\lambda}\mathcal V)>0\)
and the Gaussian bounds
\(M^2(\lambda/(8\pi))^{3/2}\le Q\le M^2(\lambda/\pi)^{3/2}\)
are correct. They prove that exactly one candidate has squared norm
\(E_0/n\), with the stated bracket
\(\pi(E_0/\mu^2)^{2/3}\le\lambda_*\le8\pi(E_0/\mu^2)^{2/3}\).

R12 compares fields on one coefficient path; the stationary candidate
uses a different, constant path. The paid difference
\(\alpha-\alpha_h\) does not pay \(\alpha_h-\lambda_*\).
The conditional entropy identity in Note90 has the correct sign and
is explicitly restricted to profiles for which its entropy/Fisher
terms and integrations are justified. Its remaining feedback term has
no established favorable sign. This is an identified missing stability
estimate, not a no-go theorem. [Reference16][ref16] attributes the
classical frozen Gibbs form; no nonlinear convergence theorem or
literature novelty is imported.

## 10. Control screen, equally informed comparison and continuation — pass

This is an auxiliary quantitative milestone under [avoid/01][a01].
The equally informed direct comparator has every paid premise and
obtains the same complete transfer. There is no primitive-specific
gain, new source domain, sign theorem or new noncollision criterion.
The [result index][results], [pattern index][avoid] and
[collision register][controls] remain controlling, with [avoid/02][a02]
and [avoid/07][a07] fixing the premise and scope discipline.

At an admitted double event the vector mass is zero, failing the
positive physical floor that supplied global \(K\) and \(n_*\).
Weighted-square controls can pass the low-mark bound and collide at
other frequencies; that does not contradict this fixed-mark transfer.
Fixed-theta polynomial observation controls fail literal cosine in the
upstream mass payment. Primitive normalization and positivity do not
repair that failed premise. Finite-prime, reflected, shape and
RH-conditional controls retain their own admission and conditional
domains; an admitted double event again lacks the positive-mass floor.
A negative Laguerre witness is not automatically a double event. Atomic
examples must first meet the smooth source/preparation admission
hypotheses. No new event location or quantitative source ratio is
asserted.

The declared R13 comparison is complete at proved-in-note scope,
with the fixed E08 assessment still pending. A subsequent
stationary task would need a separately recorded stability/attraction
consumer suited to the actual state-dependent scalar field and the paid
forcing topology. The present candidate uniqueness does not supply
that theorem, and its absence is not mathematical impossibility.

[n42]: ../notes/42_RADIAL_DRIFT_PRODUCTION_IMPROVEMENT_B02_R4_20261029.md
[n67]: ../notes/67_UNIFORM_FEEDBACK_DIRECT_COMPARISON_B02_R10_20261029.md
[n82]: ../notes/82_COMMON_CARRIER_SYNCHRONIZATION_R12_20261029.md
[n83]: ../notes/83_FINITE_CENTERED_PRODUCTION_CORRECTION_R12_20261029.md
[n89]: ../notes/89_COMPLETE_CARRIER_PRODUCTION_TRANSFER_R13_20261029.md
[n90]: ../notes/90_CARRIER_FEEDBACK_DEFECT_AND_STATIONARY_CANDIDATE_R13_20261029.md
[r43]: 43_COMMON_CARRIER_AND_PRODUCTION_E08_R12_ASSESSMENT_20261029.md
[ref16]: ../references/16_FIXED_DRIFT_GIBBS_AND_FEEDBACK_SCOPE_20261029.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a02]: ../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
