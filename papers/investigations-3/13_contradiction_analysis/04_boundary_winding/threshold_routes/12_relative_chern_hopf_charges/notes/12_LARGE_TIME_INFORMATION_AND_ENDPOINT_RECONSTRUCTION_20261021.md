# Large time information and endpoint reconstruction

21 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**, verified from the active turn metadata. **Status: exact identities and consequences of the cited in-note asymptotics; separate same-model internal review.** No endpoint exclusion, independent specialist validation, or impossibility theorem is claimed. See [Review 11][review].

This note checks whether the infinite heat-time limit can constrain the missing endpoint sign. It complements [the fixed-time signed calculation][n11], [the source-response manuscript][source], and [the progress register][progress]. Read the [result index][results] and [avoid index][avoid], especially [target reformulation][a01], [matched controls][controls], [coupled estimates][a12], and [scoped conclusions][a07]. The quantitative gain is an explicit reconstruction-conditioning calculation; an invariant equal to the endpoint target is classified as such.

## 1. The actual fixed-label theorem

[BW10 Note 20][bw20], DS2–DS4 and DS13–DS15, proves for each fixed adjacent positive rank k that
\[
 g_k(t)\sim\pi/L_t,\qquad
 g_k'(t)=-\pi L_t'/L_t^2+O_k((L_t\kappa_t^{5/4})^{-1}),
\]
where
\[
4\pi e^{4L_t}=2tL_t+9,\quad
L_t\sim\tfrac14\log t,\quad \kappa_t\sim8tL_t.
\]
The late-time identification of each fixed finite set of roots is unconditional. RH connects those ranks to positive-time walls continued from a hypothetical endpoint. No uniformity in growing ranks or event heights is supplied. [Review 19][bwreview] retains the same-assistant review limitation.

For \(\Delta=g_k^2\), therefore,
\[
\Delta(t)\sim\pi^2/L_t^2,\qquad L_t^2\Delta(t)\longrightarrow\pi^2,
\qquad\Delta'(t)\longrightarrow0.
\tag{1}
\]
A double-born pair can open as \(\sqrt{8t}\), remain separated at every finite positive time, and eventually shrink to zero. This is explicitly compatible with Note 20, Section 5. Neither limiting gap in (1) identifies its initial value. The unscaled roots approach zero while the source normalization grows; this supplies no regular terminal physical jet.

## 2. Exact gap transport and its amplification

[BW10 Note 19][bw19], RM6, retains the complete exterior interaction:
\[
\Delta'=8+A\Delta,\qquad A=-4S_{\rm ext}.
\]
Fix \(t_0>0\) and define \(\mu(T)=\exp(-\int_{t_0}^T A)\). Since \(\Delta>0\),
\[
\mu(T)=\frac{\Delta(t_0)}{\Delta(T)}
 \exp\left(8\int_{t_0}^T\frac{ds}{\Delta(s)}\right).
\tag{2}
\]
Indeed, \(A=(\log\Delta)'-8/\Delta\), whose integral gives (2). By (1),
\(\Delta(s)^{-1}\sim(\log s)^2/(16\pi^2)\). Comparison above any sufficiently large fixed lower limit, followed by
\[
\int^T(\log s)^2ds=T((\log T)^2-2\log T+2)+O(1),
\]
proves
\[
\log\mu(T)\sim\frac{T(\log T)^2}{2\pi^2},\qquad
\mu(T)^{-1}=\exp\left[-\left(\frac1{2\pi^2}+o(1)\right)T(\log T)^2\right].
\tag{3}
\]
The logarithm of the prefactor in (2) is only \(O(\log\log T)\). Equation (3) is a logarithmic asymptotic, not a ratio asymptotic against the exponential of its displayed leading term; omitted exponent terms can diverge.

For an isolated exact double, RM16 gives
\(\Delta(t)=8t-16S_0t^2+O(t^3)\), hence \(A(t)=-4S_0+O(t)\). Thus
\[
\mu_0(T)=e^{-\int_0^{t_0}A}\mu(T)
\tag{4}
\]
extends (3) to an integrating factor normalized at zero. This uses a positive finite factor, **not** the invalid substitution \(\Delta(0)/\Delta(T)\) into (2). For a selected pair in a higher birth, RM17 instead contains singular exterior terms; this extension does not apply.

## 3. Terminal and coefficient errors

The exact reconstruction is
\[
\Delta(t_0)=\mu(T)\Delta(T)-8\int_{t_0}^T\mu(s)ds.
\tag{5}
\]
Even with exact A, a separately bounded terminal squared-gap error \(\varepsilon_T\) gives the initial-error bound \(\mu(T)\varepsilon_T\). A vanishing guaranteed initial-error bound therefore requires \(\varepsilon_T=o(\mu(T)^{-1})\) in this separate-bound model. A gap error ε first produces a squared-gap error at most 2gε+ε². The existing algebraic saddle remainder does not meet that requirement.

Coefficient uncertainty has an exact, nonlinear-error identity. Given differentiable approximations \(\widehat\Delta,\widehat A\), set
\[
r=\widehat\Delta'-8-\widehat A\widehat\Delta,\qquad e=\Delta-\widehat\Delta.
\]
Then
\[
e(t_0)=\mu(T)e(T)-\int_{t_0}^T\mu\big[(A-\widehat A)\widehat\Delta-r\big]ds,
\tag{6}
\]
by integrating \(e'=Ae+(A-\widehat A)\widehat\Delta-r\). Consequently
\[
|e(t_0)|\le\mu(T)|e(T)|+
\int_{t_0}^T\mu\bigl(|A-\widehat A|\,|\widehat\Delta|+|r|\bigr)ds.
\tag{7}
\]
A concrete first variation also exposes coefficient sensitivity. Perturb A to A+ε while holding the terminal value fixed. Differentiating at ε=0 gives initial variation
\[
-\int_{t_0}^T\mu(s)\Delta(s)ds
\sim-\frac{\mu(T)\Delta(T)^2}{8}
\sim-\frac{\pi^4\mu(T)}{8L_T^4}.
\]
For the middle equivalence, the derivative of \(\mu\Delta^2/8\) is \(\mu\Delta(1+\Delta'/8)\); (1) and l’Hôpital’s rule apply, since the denominator tends to infinity. This is scalar sensitivity, not an assertion that the perturbed coefficient is realized by another theta field.

These are conditioning statements for separately bounded scalar data. They do not exclude correlated source identities that control the cancellation directly.

## 4. A scalar all-orders control

For \(\Delta'=8-4t\Delta\), the solutions with \(\Delta(0)=C\ge0\) are
\[
\Delta_C(t)=e^{-2t^2}\left(C+8\int_0^t e^{2s^2}ds\right).
\tag{8}
\]
They are positive for \(t>0\), tend to zero, and eventually decrease. Endpoint Laplace expansion, or substitution with successive remainder bounds in this linear equation, gives
\[
\Delta_C(t)\sim\frac2t+\frac1{2t^3}+\frac3{8t^5}+\frac{15}{32t^7}+\cdots.
\]
For completeness, substituting w=4t(t−s) in (8)'s particular solution gives
\[
\Delta_0(t)=\frac2t\int_0^{4t^2}e^{-w+w^2/(8t^2)}dw.
\]
On \(0\le w\le2t^2\), expand the second exponential to any fixed order N. Its integrated remainder is bounded by a constant times \(t^{-2N-2}\), since the combined exponential is at most \(e^{-3w/4}\). The remaining interval contributes at most \(2t^2e^{-3t^2/2}\). Extending each coefficient integral to infinity costs only an exponential tail. Thus the coefficient of \(2t^{-2n-1}\) is \((2n)!/(8^n n!)=(2n-1)!!/4^n\), with remainder \(O(t^{-2N-3})\) after multiplying by 2/t.

All C have the same expansion to every algebraic order, while their exact difference is \((C_1-C_2)e^{-2t^2}\). Thus C=0 and C>0 retain different endpoint information beyond all these orders. This is a **scalar ODE information control**, not a claimed heat-function or theta realization.

The closer source controls have their own scope: BW10 Note 20 explains that the positive normalized endpoint controls preserve a leading tail permitting qualitative saddle concentration and shrinkage, while retaining endpoint doubles. They fail ordinary Dirichlet-series arithmetic; no identical numerical allowances or full asymptotic expansion are assigned to them.

## 5. Exact full-field reconstruction remains available

The scalar conditioning above is not universal inverse-heat instability. For real x and T>0, the complete heat field satisfies the Gaussian identity
\[
H(0,x)=\frac1{\sqrt{4\pi T}}\int_{\mathbb R}
 e^{-(x-y)^2/(4T)}H(T,y)dy.
\tag{9}
\]
Insert \(H(T,y)=\int_0^\infty\Phi(u)e^{Tu^2}\cos(yu)du\). Fubini is justified because the Gaussian has mass one and \(\int\Phi e^{Tu^2}<\infty\). Its Fourier transform sends \(\cos(yu)\) to \(e^{-Tu^2}\cos(xu)\), proving (9). The same argument applies to fixed spatial derivatives using their finite complete moments.

Gaussian convolution contracts absolute supremum error: a uniform absolute error \(\varepsilon\) in the entire real field H(T,·) produces at most \(\varepsilon\) in (9). Therefore (3) cannot be promoted to a prohibition on all terminal-field methods. The distinction is that the moving-saddle approximation supplies normalized, restricted-scale information, not an equally accurate absolute approximation on the entire real line.

A finite spatial approximation requires an additional tail payment. Truncating (9) to \(|y-x|\le Y\), the bound \(|H(T,y)|\le H(T,0)\) gives
\[
|\mathrm{tail}|\le H(T,0)\operatorname{erfc}(Y/(2\sqrt T)).
\]
This is a sufficient envelope bound, not a necessary accuracy or acquisition lower bound; oscillatory cancellation may improve it. The fixed-label saddle estimates concern bounded scaled coordinates, hence physical positions of order \(1/L_T\). Their existing domain and error contract do not cover the entire Gaussian integral. This spatial-coverage obligation is separate from the small normalization needed below.

This loss can be stated exactly in source variables. Define the probability law
\[
d\nu_T(u)=\Phi(u)e^{Tu^2}du/H(T,0).
\]
Then
\[
\frac{e^{-Tu^2}d\nu_T(u)}{\mathbb E_{\nu_T}e^{-TU^2}}
 =\frac{\Phi(u)du}{H(0,0)},\qquad
\mathbb E_{\nu_T}e^{-TU^2}=\frac{H(0,0)}{H(T,0)}.
\tag{10}
\]
Thus exact reweighting recovers the original source; a leading Gaussian limit about its moving saddle does not control this small denominator relatively.

Note 20's complete saddle normalization gives
\[
\log H(T,0)=q_T(L_T)-\tfrac12\log\kappa_T+O(1),
\quad q_T(L_T)=TL_T^2-\tfrac12TL_T+9L_T-\tfrac94.
\]
The stationary equation gives the second equality; the normalized density integral in DS8–DS10 tends to \(\sqrt{2\pi}\), proving the first. Hence
\[
\log H(T,0)\sim\tfrac1{16}T(\log T)^2.
\tag{11}
\]
The weight in (10) has exponentially small expectation on this logarithmic scale. Recovering it requires information outside the leading saddle approximation. For example, a uniform normalized-field error \(\varepsilon_T\) in H(T,·)/H(T,0), with exact normalization, gives the sufficient absolute error bound \(H(T,0)\varepsilon_T\) in (9). Coupled oscillatory estimates may improve that bound.

## 6. A precise usefulness gate

The renormalized scalar invariant
\[
\mathcal C(T)=\mu_0(T)\Delta(T)-8\int_0^T\mu_0(s)ds=\Delta(0)
\tag{12}
\]
preserves the desired information exactly. Its identity alone is a target reformulation. For any differentiable reference d, with \(r_d=d'-8-Ad\), the equivalent comparison is
\[
\Delta(0)=d(0)+\mu_0(T)(\Delta(T)-d(T))+
\int_0^T\mu_0(s)r_d(s)ds.
\tag{13}
\]
A useful infinite-time continuation must independently bound this coupled difference with a strict sign and paid errors, or derive an endpoint signed estimate from the complete Gaussian/source reconstruction. Merely computing more algebraic terms, bounding A absolutely, or imposing the known limit (1) does not meet that gate.

The fixed-time canonical signed response remains the immediate priority. The infinite-time calculation identifies a concrete possible research target: a signed connection coefficient or complete reweighting estimate that survives the loss of leading-profile information. Exact source asymptotics and new coupled identities remain possible. ECE-02 and the height/multiplicity exclusion obligations retain their open statuses.


## 7. Recommended first investigation: a finite matching time

Follow-up, 21 October 2026, for Edward Baker with substantial LLM
assistance; recorded **gpt-6-astra, effort ultra**. This is a research
priority with elementary transfer/error identities, not an endpoint sign
result. Two separate same-model agents checked the identities and the
screen below; [Review 11][review] records their scope.

The most promising first test is to transport the existing endpoint
response to a **finite** time T, estimate its signed residual there, and
compare against Note 11 on the same proper two-root window. Taking an
infinite limit is justified only if this comparison produces useful bounds
that persist as T grows. This is an assessment of the available routes,
not a claim that a successful estimate exists.

Write K_T(z,y)=(4 pi T)^(-1/2) exp(-(z-y)^2/(4T)), and keep F, L_F,
B_F and Q_F from Note 11 at time zero. For the complete residual E,
Gaussian transfer gives
\[
 E(0,z)=\int_{\mathbb R}K_T(z,y)E(T,y)dy.
\]
Set
\[
 \ell_T(y)=L_F(K_T(\cdot,y)),\qquad
 b_T(y,v)=B_F(K_T(\cdot,y),K_T(\cdot,v)).
\]
Then the same signed response S=L_F(E(0))+Q_F(E(0)) is
\[
 S=\int\ell_T(y)E(T,y)dy+
       \iint b_T(y,v)E(T,y)E(T,v)dydv.                 \tag{14}
\]
The contour is compact, and the complete real residual and its fixed
spatial derivatives are bounded for each finite T by source moments.
Gaussian decay, including the bounded imaginary displacement of the
contour, therefore justifies the exchanges. Approximate fields below
must satisfy the corresponding integrability assumptions.

For an approximation P_T to the residual, write r_T=E(T)-P_T and
p_0(z)=integral K_T(z,y)P_T(y)dy. The exact response error is
\[
\begin{split}
 S-L_F(p_0)-Q_F(p_0)
 ={}&\int[\ell_T(y)+2B_F(p_0,K_T(\cdot,y))]r_T(y)dy\\
 &+\iint b_T(y,v)r_T(y)r_T(v)dydv.                    \tag{15}
\end{split}
\]
**Equation (15) is the proposed estimating target:** retain the mixed
term and the residual quadratic term together, and use the unchanged
canonical coefficients and full-source identities to bound their sign.
Its identity is not itself a gain. The actual E(0)/F wall ratio and the
cubic response remainder remain those of Note 11.

A complete error budget is available without demanding uniform accuracy
on the entire real line. For real a, set
\[
 d\gamma_{T,a}(y)=K_T(a,y)dy,\qquad
 \eta_T(a)^2=\int|r_T(y)|^2d\gamma_{T,a}(y).
\]
For e_0=E(0)-p_0, Gaussian orthogonality and Cauchy--Schwarz give
\[
 |e_0(a)|^2+2T|e_0'(a)|^2\le\eta_T(a)^2,\qquad
 |e_0(z)|\le e^{|z-a|^2/(4T)}\eta_T(a).                \tag{16}
\]
For the first inequality use the orthonormal Gaussian functions 1 and
(y-a)/sqrt(2T); differentiation of K_T supplies the second coefficient.
For the second, the squared L2(gamma) norm of
K_T(z,y)/K_T(a,y) is exp(|z-a|^2/(2T)). In particular, the complete
contour error is at most exp(R^2/(4T)) eta_T(a). Tails outside a finite
integration interval must be included in eta, not dropped. These norm
estimates are fallback error payments; a gain in (15) may require
estimating its signed integrals more sharply.

There is a decisive screen against a free gain from time evolution.
If P_T is the exact evolution of a fixed residual approximation, then
p_0 is independent of T. Its reconstructed value is exactly that same
endpoint approximation. Moreover, r_T satisfies r_T,t=-r_T,yy, and
\[
 \frac{d}{dT}\eta_T(a)^2
   =2\int K_T(a,y)|\partial_y r_T(y)|^2dy\ge0.         \tag{17}
\]
Differentiate the Gaussian integral, use partial_T K_T=partial_y^2 K_T,
and integrate twice by parts. The product rule cancels the r_T,yy terms.
All steps are justified for a fixed theta source residual by complete
heat-weighted moments on compact T intervals and Gaussian decay. This
monotonicity does not apply to arbitrary approximations with a nonzero
heat defect. Nor does it imply monotonicity of the full contour allowance
exp(R^2/(4T)) eta_T, whose first factor decreases.

For an explicit check, r_T(y)=exp(Tu^2)cos(uy) reconstructs exactly
cos(uz), while
\[
 \eta_T(a)^2=\tfrac12\{e^{2Tu^2}+e^{-2Tu^2}\cos(2ua)\},
\]
whose derivative is u^2(e^{2Tu^2}-e^{-2Tu^2}cos(2ua))>=0.
Thus the scalar source control obeys both reconstruction and (17).
The collision sources in the [control register][controls] likewise obey
the generic transfer identities on their admissible finite time intervals.
No collision is excluded by those identities. Euler-factor sources change
the arithmetic; weighted-square and finite-prime controls lack full
normalized reflection; reflected and primitive-compatible sources lack
canonical square coefficients. The close normalized endpoint controls
fail ordinary Dirichlet-series arithmetic. A new inequality must exploit
such a distinction quantitatively on a domain containing the control's
event; positivity, Gaussian smoothing and leading concentration do not
supply that distinction.

The first deliverable should be a **matched analytic error comparison**:
choose one parameterized proper two-root window, retain the complete
canonical tail, and estimate (15) with explicit spatial-tail and source
payments. Compare its signed enclosure against Note 11 using the same
reference and residual data. A strictly improved enclosure with stated
parameter dependence is an estimating gain; a positive full lower bound
would additionally exclude an endpoint double in that window. A known
separated-pair example alone is only a transfer check, not new exclusion
evidence. Failure to improve this comparison is a reason to keep the
fixed-time source estimate primary, not an impossibility result for all
large-time arguments. Only after a useful finite-T gain should one seek
uniformity as T grows, and then separately address height and multiplicity.

[bw19]: ../../10_rh_implies_simple_zeros/notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[bw20]: ../../10_rh_implies_simple_zeros/notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[bwreview]: ../../10_rh_implies_simple_zeros/reviews/19_ROOT_MOTION_AND_DIFFERENTIATED_SADDLE_REVIEW_20261021.md
[source]: ../manuscript/source.tex
[n11]: ../notes/11_CANONICAL_QUADRATIC_RESPONSE_AND_HEAD_TAIL_CANCELLATION_20261021.md
[progress]: ../research-progress/02_ENDPOINT_CHARGE_EXCLUSION_PROGRESS_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[review]: ../reviews/11_SIGNED_RESPONSE_AND_INFINITY_TRANSFER_REVIEW_20261021.md
