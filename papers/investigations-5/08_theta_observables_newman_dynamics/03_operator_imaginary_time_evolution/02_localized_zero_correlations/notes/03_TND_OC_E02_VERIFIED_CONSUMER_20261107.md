# E02: verified comparison and its exact consumer

7 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Exact backend model and reasoning
effort are unavailable in the exposed session metadata. Sol6.1/ultra was
the packet's recommendation, not an observed setting. Root coordinates
three read-only scope checks at inherited settings and writes this note.

**Task:** [E] TND-OC-E02 r1. **Evidence:** written analytical assessment,
not interval arithmetic or specialist review. [Review02](../reviews/02_TND_OC_E02_CLAIM_LEVEL_ASSESSMENT_20261107.md)
owns dispositions; the [sole register](../research-progress/01_TND_OC_RESEARCH_PROGRESS_20261107.md)
owns live status. The requested checkout is write-blocked in this session;
these are staged replacements, delivered with a source-bound patch.

## 1. The one bounded correction

[Note01](01_TND_OC_REFLECTION_AND_CONFIGURATION_REDUCTION_20261107.md)
initially allowed arbitrary compact support for w but used a cover of
[X-h,X+h] in its count corollary after (11). These are different scopes.
We now specify h>0 and explicitly restrict **that count corollary** to
supp w contained in [-1,1]. No earlier identity needs this restriction.

Indeed any active real coordinate then lies in [X-h,X+h]. It is covered
by at most ceil(2h)+1 closed unit intervals whose left endpoints u obey
|u|<=|X|+h. The inherited multiplicity-count bound therefore gives

\[
 Q_w\le N_w\le
 B=A_{\rm count}(\lceil2h\rceil+1)\log(3+|X|+h).
\]

For example, a smooth window translated far from [-1,1] would place its
active coordinates near X+hL and the stated cover near X would not
cover them. This identifies the failed premise of the original corollary;
it is not a counterexample to any finite algebraic identity. Note02
already imposes the required support and needs no mathematical correction.
The absolute count constant is inherited and unevaluated.

## 2. Recalculated constants and singularity payment

For R=9/2, rho=13/3, r=25/6, B_R=R+r=26/3,

\[
 R/\rho=27/26,\qquad (\rho+r)/(\rho-r)=51.
\]

Let A=log(1/m), n=max(1,ceil(A/log(27/26))). Jensen bounds the
number k of zeros in the open rho-disk by n. After removal with R-disk
Blaschke factors, the residual h is bounded by one on D_R and is zero-free
on D_rho, with |h(0)|>=m. Applying Harnack first on a radius smaller than
rho and then taking its limit proves |h|>=exp(-51A) on D_r, even if h
has a zero on the rho-circle.

Writing q=exp(51A)t, the k>=1 sublevel cover has area at most
k*pi*B_R^2*q^(2/k). For q<1, this is bounded by
n*pi*B_R^2*q^(2/n); k=0 instead gives an empty sublevel set. For q>=1
the same displayed majorant bounds the whole disk. Thus

\[
 |\{|f|<t\}\cap D_r|
 \le n\pi B_R^2 e^{102A/n}t^{2/n},
\]
\[
 \int_{\{|f|<t\}\cap D_r}\log(t/|f|)\,dA
 \le \frac{\pi B_R^2n^2}{2}e^{102A/n}t^{2/n}.
\]

For tau=epsilon^(n/(n+2)), epsilon<=tau. The region where both
moduli exceed tau costs at most pi*r^2*epsilon/tau. On its complement
both moduli are below 2tau; the absolute log difference is bounded by
the sum of their nonnegative log deficits at 2tau. Applying the last
inequality twice gives exactly

\[
 \int_{D_r}|\log|f|-\log|g||\,dA
 \le\bigl[\pi r^2+\pi B_R^2n^2e^{102A/n}2^{2/n}\bigr]
 \epsilon^{2/(n+2)}.
\]

This handles multiple zeros without an unpaid pointwise lower modulus.
The external inputs are the checked Jensen, Harnack and smoothed Jensen
passages in [source-use02](../references/02_TND_OC_E02_SOURCE_USE_20261107.md);
the quantitative estimate above is recalculated, not imported.

## 3. Canonical normalization and complete error

Retain **lambda=0, X>=10, 0<h<=1** and Note02's fixed windows/cutoffs.
For c=X+4i and s=1/2-iz/2, the R-disk has
Re s in [1/4,19/4]. The multiplier
D=16*pi^(s/2)/(s^2*Gamma(s/2)) is holomorphic and zero-free on a
neighborhood of the closed disk, and F=D H_0=((s-1)/s) zeta(s).
Fractional-part continuation gives |F|<=2X+25=M_X-1;
the safe anchor obeys |F(c)|>=c_0=(3/5)zeta(5)/zeta(5/2).

For a holomorphic approximation with complete-disk absolute error
delta<=min(1,c_0/2), both F/M_X and Fhat/M_X satisfy the lemma with
m_X=c_0/(2M_X) and epsilon=delta/M_X. In particular the approximant's
upper bound is (M_X-1)+delta<=M_X and its anchor is at least c_0/2.

For Note02's finite arithmetic source integrated on [0,U], independently
recalculated tails and conversion give

\[
 \delta\le\mathcal B_X\,[5C_2(J)I_b+B_0 I_b^{>U}],\quad b=17/2,
\]
\[
 I_b^{>U}=\tfrac14\pi^{-19/8}\Gamma(35/8,\pi e^{4U}),\qquad
 C_2(J)\le\frac{(J+1)^4e^{-\pi((J+1)^2-1)}}
 {1-16e^{-\pi(2J+3)}}.
\]

The gamma change of variables has power v^(27/8), hence parameter
35/8. From the reciprocal-gamma product,
|1/Gamma(w)|<=|w| exp(gamma Re w+pi^2|w|^2/12).
Putting w=s/2 gives the prefactor 8/|s|<=32 and exponent
pi^2(361+4(X+9/2)^2)/768 in Note02(32). No full-line conversion
or fixed-height-independent cost is substituted.

For either compact C^(1,1) test phi_Q=2a or
phi_eta=2log(1+eta*a), its value and first normal derivative vanish at
y=0. Therefore its weak Laplacian has no line atom. Its support lies
strictly in D(c,r), since 17<625/36. Mollification within that buffer
and local logarithmic integrability justify the zero-measure formula.
Conjugation supplies the factor two; real multiple zeros contribute zero.
Approximate zeros in the 1<y<2 collar keep their actual cutoff weights.

The exact accepted output is

\[
 |Q_{X,h}-\widehat Q|\le E_Q,\quad
 |\log Z_{X,h}(\eta)-\widehat L_\eta|\le E_\eta,
\]
\[
 E_\varphi=\frac{\|\Delta\varphi\|_\infty}{2\pi}
 C_X(\delta/M_X)^{2/(n_X+2)}.
\]

Note02(35)--(36) makes this at most e/2 for every prescribed e>0.
All limits and cutoffs are selected **after** X,h,e,eta and any defect
d are declared. The case eta=0 is exact without those costs.

## 4. The exact next consumer, and its first unpaid premise

For a plateau pair with |y|>=d>0, the true statistics obey
Q>=2d^2 and log Z>=2log(1+eta*d^2). The accepted implication is

\[
 \widehat Q+E_Q<2d^2\quad\text{or}\quad
 \widehat L_\eta+E_\eta<2\log(1+\eta d^2)
 \quad\Longrightarrow\quad\text{no such pair in that plateau}.
\]

**First unpaid downstream premise:** an independent canonical upper
estimate on Qhat or Lhat below its remaining margin. There is no unpaid
clause inside E02's comparison theorem after the support correction.
A future evaluated statistic must also carry quadrature/rounding error
in this strict inequality. The exact finite-source logarithmic area
integral has not been certified numerically.

The pair/product identities and this approximation theorem remain
compatible with the [collision controls](../../../../../../result-summaries/12_collision_controls_and_screening.md).
Their canonical source/normalization premise failures are itemized in
Note01 section5; missing canonical identity alone does not prove a
favorable sign. All-window exact vanishing is the already identified
RH reformulation, not a new numerical target. Keep the
[result index](../../../../../../result-summaries/README.md),
[avoid index](../../../../../../avoid/README.md),
[shared-premise warning](../../../../../../avoid/05_same_model_reviews_and_shared_premises.md)
and [scope rule](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md).

**Next: [B] TND-OC-B02 — Astra.** Select one source-sensitive signed
comparison for the finite log statistic, or record a precisely scoped
failure. There is no ready task whose contract is merely to prove the
unknown statistic small. No new mechanism or numerical campaign was
started in E02; parent and Green registers are unchanged.
