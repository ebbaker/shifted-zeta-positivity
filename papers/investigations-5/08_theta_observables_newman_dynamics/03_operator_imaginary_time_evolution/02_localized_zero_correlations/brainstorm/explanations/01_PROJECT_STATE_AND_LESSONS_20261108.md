# Current state of the theta/Newman program and what we have learned

8 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance. Exact backend model and reasoning
effort are unavailable in exposed session metadata. This is an explanation
of existing results, not a new proof, assessment, or research activation.
It focuses on the current localized-correlation branch and its shared
operator/Green context; it is not a review of every earlier RH investigation.

The project now has explicit zero-sensitive observables, complete-source
formulas, quantitative approximation errors, and several precise limitations
of proposed estimates. **The missing result is still a sufficiently small
signed estimate for the unchanged canonical theta field.** No new nonreal-zero
exclusion or proof of RH has been obtained. The recent negative results
identify information lost by particular estimating methods; they do not
exclude all localized-statistic or Green-function approaches.

The [correlation register](../../research-progress/01_TND_OC_RESEARCH_PROGRESS_20261107.md),
[Green register](../../../01_green_potential_resolvent/research-progress/01_TND_OG_GREEN_RESOLVENT_RESEARCH_PROGRESS_20261107.md),
and [parent register](../../../research-progress/02_SMOOTH_LOCALIZATION_RESEARCH_PROGRESS_20261106.md)
were read for this explanation. They own current task status.

We start with the complete theta source and its Newman deformation:

\[
 H_\lambda(z)=\int_0^\infty e^{\lambda u^2}\Phi(u)\cos(zu)\,du,
 \qquad H_0(z)=\frac18\xi\!\left(\frac12-\frac{iz}{2}\right),
 \qquad \partial_\lambda H_\lambda=-\partial_z^2H_\lambda.
\]

The two usual signs in the xi argument agree by its functional equation.
Writing \(h(\tau,z)=H_{\lambda_0-\tau}(z)\) gives ordinary forward heat
evolution \(\partial_\tau h=\partial_z^2h\). RH corresponds to all zeros
of H_0 being real. The operator realization makes this evolution precise
but takes the canonical preparation as supplied. Positivity of the source
or of a state-space norm does not itself determine the zeros of its
oscillatory amplitude. The inherited collision controls demonstrate why
that distinction matters; see the [manuscript introduction](../../../manuscript/sections/01_introduction.tex).

The parent work also established local collision diagnostics, complete
transverse-moment calculus through multiplicities, density/moment bounds,
a Gaussian derivative hierarchy, and a positive Green potential. These
results have their stated internal assessments. Their acquired upper
allowances still do not exclude one isolated nonreal pair. In particular,
a center average dilutes that pair's signal, and a local collision formula
does not automatically supply a controlled trajectory to time zero.

For the correlation branch, write a zero as \(z_j=x_j+iy_j\), counting
each multiplicity copy, and choose a smooth window
\(w_j=w((x_j-X)/h)\), with \(0\le w\le1\). The main observable is

\[
 Q_{X,h}=\sum_jw_jy_j^2\ge0.
\]

It measures transverse displacement from the real axis. A conjugate pair
\(x_0\pm id\) inside the plateau w=1 contributes exactly \(2d^2\).
Every real zero contributes zero, even if multiple. Thus the target does
not inadvertently demand simplicity in addition to realness.

One early lesson is that the simplest marked pair statistic contains less
new information than its notation suggests. With separation weight one,
conjugation cancels the odd transverse moments and gives

\[
 \sum_{j\ne k}w_jw_k(y_j-y_k)^2=2N_wQ_w,
 \qquad N_w=\sum_jw_j.
\]

For a general even separation weight chi, the corresponding expression is
\(2\int(\chi*q_0)\,dq_2\), where
\(q_0=\sum_jw_j\delta_{x_j}\) and
\(q_2=\sum_jw_jy_j^2\delta_{x_j}\). It remains a density-weighted
transverse measure; this does not reduce every possible marked correlation
or forbid a sharper joint arithmetic estimate.

The configuration product also has an exact deterministic description:

\[
 Z(\eta)=\prod_j(1+\eta w_jy_j^2),\qquad
 \log(1+\eta)Q_w\le\log Z(\eta)\le\eta Q_w,
 \quad\eta>0.
\]

The comparison uses the inherited unit strip \(|y_j|\le1\). Its coefficients
obey Newton's identities and its growing-order remainder is controlled:

\[
 Z(\eta)=\sum_ke_k\eta^k,\qquad
 0\le Z-\sum_{k=0}^Ke_k\eta^k
 \le e^{\eta Q_w}\frac{(\eta Q_w)^{K+1}}{(K+1)!}.
\]

This is a valid hierarchy, but writing it down does not make Q small.
No probability law or determinantal process for canonical zeros is assumed.
These identities and their limits are in
[Note01](../../notes/01_TND_OC_REFLECTION_AND_CONFIGURATION_REDUCTION_20261107.md),
accepted after a bounded support correction in E02.

The strongest positive result in this branch is a quantitative bridge
from the complete field to these nonholomorphic zero statistics. Set

\[
 s=\frac12-\frac{iz}{2},\qquad
 F(z)=\frac{s-1}{s}\zeta(s)=D(z)H_0(z).
\]

Here D is nonvanishing on the chosen disk, so it changes no local zeros.
At time zero, for X>=10 and 0<h<=1, a complete-disk field error delta,
with the specified anchor and normalization, gives

\[
 \int_{D(X+4i,25/6)}
   |\log|F|-\log|\widehat F||\,dA
 \le C_X\left(\frac{\delta}{M_X}\right)^{\alpha_X},
 \qquad M_X=2X+26,\quad
 \alpha_X=\frac2{n_X+2},\quad n_X=O(\log X).
\]

The important point is that this handles the logarithmic singularities at
zeros, including multiple zeros, rather than assuming a positive modulus
throughout the region. The full theta arithmetic and radial tails and the
normalizing multiplier have explicit payments. The exponent deteriorates
with height, so this is not a practical-cost or height-uniform-exponent claim.

The zero-measure identity

\[
 S_\varphi(F)=\sum_jm_j\varphi(z_j)
 =\frac1{2\pi}\int\log|F|\Delta\varphi\,dA
\]

then gives, for the accepted compact tests representing Q and log Z,

\[
 |Q-\widehat Q|\le E_Q,\qquad
 |\log Z-\widehat L_\eta|\le E_\eta,
 \qquad
 E_\varphi=\frac{\|\Delta\varphi\|_\infty}{2\pi}
 C_X\left(\frac{\delta}{M_X}\right)^{\alpha_X}.
\]

These results are internally accepted in E02; the precise proof and
conditions are [Note02](../../notes/02_TND_OC_LOCAL_LOG_TRANSFER_20261107.md)
and [consumer Note03](../../notes/03_TND_OC_E02_VERIFIED_CONSUMER_20261107.md).
The finite-source integrals have not been certified by numerical quadrature;
an evaluator would also owe integration and rounding error.

The missing arithmetic step is now explicit. A plateau pair with
transverse size at least d is excluded if one can prove

\[
 \widehat Q+E_Q<2d^2
 \quad\text{or}\quad
 \widehat L_\eta+E_\eta<2\log(1+\eta d^2).
\]

We can drive the comparison error down for a declared finite window and
positive budget. We have not shown the remaining finite-source value to
be sufficiently small. Accurate acquisition and a favorable value are
separate mathematical achievements. A fixed positive error cannot resolve
every d approaching zero.

B02 examined two ways of filling this gap. First, split the Laplacian
into positive and negative parts of equal mass b, and normalize them to
probability measures mu+ and mu-. For a normalized holomorphic field f,
define

\[
 A_\pm=\int|f|^2d\mu_\pm,\qquad
 J_\pm=\log A_\pm-\int\log|f|^2d\mu_\pm\ge0.
\]

The exact expression is

\[
 S_\varphi(f)=\frac b{4\pi}
   \left[\log\frac{A_+}{A_-}+J_--J_+\right],
 \qquad
 A_+-A_-=\frac4b\int\varphi|f'|^2dA.
\]

For nonconstant f the quadratic term has a positive sign. Even a zero-free
nonconstant field needs a compensating negative difference of Jensen gaps
to produce its true statistic zero. Separate quadratic estimates therefore
discard potentially decisive cancellation. We still lack the source-specific
estimate for the coupled gap difference. The identity alone is not a gain
toward the sign, and B02 does not exclude all coupled moment methods.

Second, B02 proved a sharp local obstruction to a harmonic logarithmic
baseline. If F has a zero of multiplicity m at a, then

\[
 \inf_{v\ \mathrm{harmonic}}
 \int_{D(a,\ell)}|\log|F|-v|\,dA
 \ge\frac{\pi\log2}{2}\,m\ell^2.
\]

A compact nonnegative radial dual test proves the inequality without a
zero-separation hypothesis, and a monomial attains equality in this local
class. In the E02 geometry, a real zero at X has a surrounding disk of
radius approaching 1/6. Consequently the **harmonic-baseline plus full-disk
absolute-error method** must pay

\[
 E_Q\ge\frac{m\log2}{36},\qquad
 E_\eta\ge\frac{\eta m\log2}{36}.
\]

That method cannot pass the strict consumer when
\(d^2\le m\log2/72\). The cost arises from a real zero that the target
observable ignores. This is an allowance floor, not a lower bound on
actual transverse mass, and it does not assert a real zero in every
window. All-real approximants containing real zeros, weighted errors
that exploit vanishing at y=0, and direct signed remainders remain outside
the stopped class. The original finite theta approximant is allowed to
have zeros and is unaffected by this zero-free-reference obstruction.
See [Note04](../../notes/04_TND_OC_B02_SIGNED_JENSEN_AND_HARMONIC_DISTANCE_20261107.md).
Its status is **proved in-note, proof-author self-check only**; E03's
separate assessment is still pending.

The Green sibling provides complementary information. Its internally
assessed positive potential is

\[
 J^{\rm G}_\lambda(X)=\sum_{y_j>0}
 \operatorname{atanh}\!\left(
 \frac{\sin(\pi y_j/8)}{\cosh(\pi(X-x_j)/8)}\right).
\]

It equals a complete logarithmic boundary average minus the value at the
safe interior point. One nonreal zero with y>=d and |x-X|<=r forces a
positive margin at least \(\sin(\pi/8)d/\cosh(\pi r/8)\). The exact
identity and complete tails are available; a favorable signed upper bound
is not. The latest Green E02 assessment accepts a complementary obstruction:
for fixed 0<theta<1/2 and short Dirichlet polynomials with a1=1, |an|<=1
and length N<=(T/2)^theta, one polynomial throughout the padded interval
I_T, its actual normalized boundary residual obeys

\[
 \liminf_{T\to\infty}\inf_A\frac1{|I_T|}
   \int_{I_T}\epsilon_A(X)^2\,dX
 \ge\frac{1/(2\theta)-11/12}{\zeta(5/2)^4}>0.
\]

Here \(\epsilon_A^2=\int|F_A/F_A(X+4i)-1|^2d\mu_X\),
\(F_A=((s-1)/s)\zeta(s)A(s)\), and mu_X is the two-boundary strip
probability measure. This limits that sufficient quadratic certificate;
it gives no positive lower bound for the actual Green potential and does
not cover arbitrary longer or center-adaptive polynomials. The
[latest Green handoff](../../../01_green_potential_resolvent/continuation-notes/04_TND_OG_E02_RESULTS_AND_MODEL_CHANGE_20261107.md)
records its bounded additive source correction and assessment status.

The recurring lesson across the branches is that source positivity,
accurate reconstruction and good bulk averages can coexist with an
unresolved local signed comparison. For example, averaging one pair over
centers of interval length T gives only

\[
 \frac1T\int_I Q_{X,h}^{\rm pair}\,dX
 =\frac{2d^2h}{T}\int w,
\]

when I contains the complete window profile. That h/T loss cannot be
discarded to infer an estimate at every center. Likewise the HDA hierarchy's
assessed negative-Newman-time estimates have not been extended to time zero.
The [result index](../../../../../../../result-summaries/README.md),
[collision controls](../../../../../../../result-summaries/12_collision_controls_and_screening.md),
[avoid index](../../../../../../../avoid/README.md), and the specific
[separate-bound](../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
and [scope](../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
rules explain these limits. None of the internal LLM assessments constitutes
independent specialist validation.

The default next task in this branch is **[E] TND-OC-E03 — Sol / ultra**,
a bounded assessment of Note04's existing proof, constants and scope.
Only after that does B03 ask whether retaining real-zero structure or the
test's vanishing permits an estimate from additional canonical
information. That route has not been selected; there is no ready task
whose content is merely to prove the remaining signed quantity small.
The [model-change continuation](../../continuation-notes/04_TND_OC_AFTER_B02_AND_MODEL_CHANGE_20261107.md)
contains the frozen assessment request and input hashes.

Chat capture was checked again on 8 November. **Full automatic capture of
this conversation is still not working.** The recorder's compatibility
repair now supports the verified paginated SQLite format as well as legacy
JSONL. Nevertheless the exact current thread has neither an available
legacy source nor matching paginated metadata; the app's supported thread
reader also fails. Repository writes work. This check establishes missing
source access, not a new hook-trust or filesystem-permission diagnosis.

The earlier completed B02 final reply and this turn's completed public
messages are preserved in the explicitly
[unregistered partial exchange](../../chat-histories/UNREGISTERED_PARTIAL_TND_OC_B02_PUBLIC_TEXT_20261107.md).
The unsent summary reply is not prewritten into a transcript. Existing
registered histories are preserved. No native title, turn id, completion
event or hook activation is fabricated; exact-turn capture cannot be
verified without those genuine source records.
