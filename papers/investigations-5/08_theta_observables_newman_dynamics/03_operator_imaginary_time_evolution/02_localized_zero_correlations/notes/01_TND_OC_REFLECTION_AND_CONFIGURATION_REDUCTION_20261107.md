# Reflection reduction and the deterministic configuration hierarchy

7 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), recorded effort max**,
branch chat0001.

**Status: proved in-note by elementary finite algebra; accepted after one
bounded hypothesis correction in the separate internal [E02 assessment](../reviews/02_TND_OC_E02_CLAIM_LEVEL_ASSESSMENT_20261107.md).** This executes clause1 of
[E01 r1](../research-progress/handoffs/01_TND_OC_E01_REQUEST_20261107.md).
It supplies no signed canonical upper estimate. The source-to-observable
error comparison is [Note02](02_TND_OC_LOCAL_LOG_TRANSFER_20261107.md).
No numerical campaign or determinantal law for canonical zeros is used.

## 1. Objects and scope

Fix \(0\le\lambda\le1/2\). The complete multiset of zeros of the real
entire \(H_\lambda\) is invariant under conjugation and lies in
\(|\Im z|\le1\), as inherited in the parent
[transverse section](../../manuscript/sections/14_smooth_transverse.tex).
The strip is needed for the bounds below, not the finite reflection
identities. Count multiplicity copies separately. Fix \(h>0\). Write \(z_j=x_j+iy_j\),
\(w_j=w((x_j-X)/h)\), with \(0\le w\le1\) smooth and compactly supported.
All sums here are finite because both real and imaginary coordinates of
the contributing canonical zeros are bounded.

Put
\[
 q_\ell=\sum_j w_j y_j^\ell\delta_{x_j},\qquad
 N_w=q_0(\mathbb R),\qquad Q_w=q_2(\mathbb R).
 \tag{1}
\]
Conjugation implies \(q_{2r+1}=0\) **as a measure at each real
coordinate**, not merely after integration. The moment \(Q_w\) is the
parent's established observable; it is not introduced as a new criterion.

## 2. The quadratic marked-pair reduction

Let \(\chi\) be bounded, even and nonnegative, with \(\chi(0)=1\).
It may be smooth and compactly supported, or identically one. Define
\[
 S_2=\sum_{j\ne k}w_jw_k\chi(x_j-x_k)(y_j-y_k)^2,\qquad
 C_\chi(x)=\int\chi(x-x')\,dq_0(x').
 \tag{2}
\]
Then
\[
 \boxed{S_2=2\int C_\chi(x)\,dq_2(x)},\qquad
 0\le S_2\le2\|\chi\|_\infty N_wQ_w.
 \tag{3}
\]
For \(\chi=1\), \(S_2=2N_wQ_w\) exactly.

**Proof.** The self-pair summand is zero, so sum over every j,k.
Expand the square. The two square terms agree by the evenness of
\(\chi\), and the cross term is
\(-2\iint\chi(x-x')\,dq_1(x)dq_1(x')=0\).
The bound follows from \(C_\chi\le\|\chi\|_\infty N_w\).
No geometric diagonal is deleted after grouping multiplicities. This
proves the same statement for multiple zeros.

If \(x_0\pm id\) have multiplicity m each and weight \(w_0\), their
mutual ordered terms contribute
\[
 S_2\ge8m^2w_0^2d^2,\qquad Q_w\ge2m w_0d^2.
 \tag{4}
\]
These are lower bounds on the full statistics. Formula(3) retains their
interactions with all other zeros. For one simple pair and b real
copies, all of weight one and \(\chi=1\), it gives
\(S_2=4(b+2)d^2\), whereas \(Q_w=2d^2\). The real population increases
the pair sum without adding transverse mass.

Thus this quadratic pair statistic is a density-weighted one-point
transverse measure. General \(\chi\) can still encode longitudinal
correlations between density and transverse mass; (3) does not identify
it with a scalar function of \(N_w,Q_w\) unless \(\chi=1\).
It also does not disprove a future joint arithmetic estimate better
than the displayed absolute upper bound.

For every integer k>=1 the same argument gives
\[
 S_{2k}:=\sum_{j\ne l}w_jw_l\chi(x_j-x_l)(y_j-y_l)^{2k}
 =\sum_{r=0}^{k}{2k\choose2r}
   \iint\chi(x-x')\,dq_{2k-2r}(x)dq_{2r}(x').
 \tag{5}
\]
All odd terms vanish fibre by fibre; the even terms have positive
coefficients. A selected multiplicity-m conjugate pair contributes
\(2^{2k+1}m^2w_0^2d^{2k}\). In the unit strip,
\[
 S_{2k}\le2^{2k-2}S_2.
 \tag{6}
\]
This is an exact all-order identity and a uniform majorant for this
kernel class. It is not a universal reduction of arbitrary marked
tests, signed kernels, or configuration-dependent weights.

## 3. The full product and its genuinely controlled order expansion

Let \(a_j=w_jy_j^2\in[0,1]\), and for \(\eta\ge0\) set
\[
 Z(\eta)=\prod_j(1+\eta a_j)
       =\sum_{k=0}^{n_{\rm loc}}e_k\eta^k,\qquad
 p_r=\sum_j a_j^r,\quad p_1=Q_w.
 \tag{7}
\]
The product includes every multiplicity copy. Real copies have factor
one. In particular the simple selected pair contributes
\(2\log(1+\eta w_0d^2)\) to \(\log Z\).

Differentiating the finite product near zero gives
\[
 k e_k=\sum_{r=1}^{k}(-1)^{r-1}p_r e_{k-r},\qquad e_0=1.
 \tag{8}
\]
Indeed \(Z'/Z=\sum_j a_j/(1+\eta a_j)\), and comparison of Taylor
coefficients proves (8). Its first terms are
\(e_1=p_1\), \(e_2=(p_1^2-p_2)/2\),
\(e_3=(p_1^3-3p_1p_2+2p_3)/6\).
These are Newton's identities for a deterministic multiset, not
probabilistic cumulant estimates.

Concavity of \(t\mapsto\log(1+\eta t)\) on [0,1] gives the exact bounds
\[
 \boxed{\log(1+\eta)Q_w\le\log Z(\eta)\le\eta Q_w.}
 \tag{9}
\]
For \(\eta>0\), the product logarithm and \(Q_w\) consequently vanish
together. This is comparability at fixed response strength, not an
independently small upper value.

There is no hidden every-fixed-order remainder. Positivity gives
\[
 0\le e_k\le\frac{Q_w^k}{k!},\qquad
 0\le Z-\sum_{k=0}^{K}e_k\eta^k
 \le e^{\eta Q_w}\frac{(\eta Q_w)^{K+1}}{(K+1)!}.
 \tag{10}
\]
The first inequality expands \(Q_w^k\) and discards repeated-index
terms; the second uses \((K+1+l)!\ge(K+1)!l!\).
For a known upper bound \(Q_w\le B\), put \(t=\eta B\).
For \(0<\varepsilon\le1\), any integer \(k=K+1\) satisfying
\[
 k\ge\max\{1,2et,(t+\log(1/\varepsilon))/\log2\}
 \tag{11}
\]
pays the tail by \(\varepsilon\), using \(k!\ge(k/e)^k\).
If t=0 the tail is identically zero.

For this count allowance assume additionally \(\operatorname{supp}w\subset[-1,1]\),
as in Note02 and the parent window convention. The earlier finite algebra
continues to hold for an arbitrary compactly supported w.
For the inherited unit-count constant \(A_{\rm count}\) in the parent
[transverse section](../../manuscript/sections/14_smooth_transverse.tex),
a cover by at most \(\lceil2h\rceil+1\) unit intervals gives the
explicit usable choice
\[
 B=A_{\rm count}(\lceil2h\rceil+1)\log(3+|X|+h)\ge N_w\ge Q_w.
\]
That inherited absolute constant has not been numerically evaluated.
For fixed h this is \(O_h(\log(2+|X|))\), so fixed \(\eta\) permits
\(K=O_h(\log(2+|X|)+\log(1/\varepsilon))\).
This is a sufficient representation-order bound. It neither evaluates
the coefficients nor supplies a small moment.

Alternatively, for complex \(\eta\) with
\(q=|\eta|\max_j a_j<1\), the branch of \(\log Z\) at zero satisfies
\[
 \left|\log Z-\sum_{r=1}^{K}
        \frac{(-1)^{r-1}\eta^r p_r}{r}\right|
 \le\frac{|\eta|^{K+1}p_{K+1}}{(K+1)(1-q)}.
 \tag{12}
\]
The all-zero-mark case is understood separately. This records the
actual logarithmic generating radius rather than assuming one.

Borodin's [§2, (2.4)](https://arxiv.org/pdf/0911.1153v1) is a different
statement: an expectation for a determinantal process with the required
operator hypotheses. Equations(7)–(12) need no expectation. Applying
that Fredholm formula to canonical zeros would require additional
identification and transfer results. See [source-use01](../references/01_TND_OC_OPENING_SOURCE_USE_20261107.md).

## 4. What averaging costs

For a single simple pair at \(x_0\pm id\), its contributions to \(Q_w\),
its mutual part of \(S_2\), and its part of \(\log Z\), averaged over
a center interval I of length T containing the complete window profile,
are respectively
\[
 \frac{2d^2h}{T}\int w,\qquad
 \frac{8d^2h}{T}\int w^2,\qquad
 \frac{2h}{T}\int\log(1+\eta d^2w(v))\,dv.
 \tag{13}
\]
Other nonnegative terms can increase the totals. Equations(13) follow
by \(v=(x_0-X)/h\); they retain the h/T dilution. The first response is
quadratic in d, including near a collision. None of these comparisons
turns a center-averaged asymptotic into an all-center exclusion.

## 5. Source interface, inherited hierarchy, and control screen

The distributional identity
\(\nu=(2\pi)^{-1}\Delta\log|H|\) sends a compact planar test to an
integral of \(\log|H|\Delta\varphi\). The test \(w(x)y^2\) is
nonholomorphic. A contour integral against a holomorphic test is not
an evaluation of it; Rouché's zero count alone is likewise insufficient.
Note02 supplies an area-logarithm comparison with all singularity costs.

The HDA recurrence's fluctuation order groups gamma-carrier corrections,
whereas (8) groups zero marks. HDA's assessed bound at \(T=-\lambda>0\),
including \(T\ge1/\log(X/(4\pi))\), does not cover \(\lambda=0\).
The field error must also be converted to a logarithmic error.
[Decision02](../brainstorm/notes/02_TND_OC_B01_SELECTION_20261107.md)
therefore selects direct time-zero acquisition, not an unproved HDA
time extension. Parent Notes28–29's finite-Euler residual obstruction
remains a statement about that quadratic certificate, not these moments.

This analytical control screen uses the
[canonical control catalog](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [positive-construction controls](../../../../../../result-summaries/04_positive_constructions_and_scoped_obstructions.md).
No old numerical certificate was rerun.

| Control family | What survives here / premise not supplied |
| --- | --- |
| Euler-factor family, for every admissible prime and coefficient | Conjugation and the identities hold on each finite window. Literal canonical theta coefficients and conductor do not survive. No algebraic identity excludes its nonreal zeros. |
| Weighted squares, finite source/tail modifications | Real transforms retain conjugation; the full normalized theta reflection/arithmetic identity is absent. A finite set of endpoint constraints does not restore it. |
| Reflected super-Gaussian, smooth shape and positive-primitive controls | Reflection and the same diagnostics survive; the unchanged theta square expansion/gamma-zeta identity does not. |
| Finite-prime orbit controls | Selected prime identities may survive; full source reflection and unchanged coefficients are not jointly supplied. |
| Atomic fixed-event and finite-profile controls, including their continuous extensions | Positive source and selected measurements do not supply the full theta profile/arithmetic or its eventual-simple-tail premises. |
| RH-conditional normalized endpoint controls | The stated ordinary Dirichlet-series arithmetic fails; a real double zero contributes zero to these transverse tests, as intended. |
| Counter-kernels \(q,q_{T,a}\), smooth-density and two-channel constructions | Their retained positivity/heat or realization properties do not identify the literal canonical field. Apply the finite algebra only when its conjugation/local-finiteness hypotheses hold. |
| Variable-observation-kernel controls | Fixing source amplitude does not impose the literal cosine readout or Newman equation; the canonical identification is absent. |

The generic algebra and generic logarithm lemma can hold for controls:
they are not exclusion premises. In any window containing an actual
nonreal pair, its positive signal prevents a true upper estimate below
that signal. Merely naming the absent canonical identity would not prove
such an estimate for theta.

Under [avoid01](../../../../../../avoid/01_restating_the_target.md),
all-window \(Q_w=0\) at time zero is the real-zero/RH reformulation
without an added simplicity demand. It is not supported by finite checks.
Equations(3), (5) and (8) are representation results; (10)–(12) are
explicit order-error estimates. Carry the
[result index](../../../../../../result-summaries/README.md),
[avoid index](../../../../../../avoid/README.md), and the specific
[control](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md)
and [scope](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
rules. General marked kernels and independent arithmetic estimates
remain outside the limited reductions proved here.

**E02 correction, 7 November 2026:** positive window width and the support
hypothesis for the count allowance are now explicit. No identity, remainder,
source, observable or numerical constant changed. Original frozen bytes
remain identified by E02 inputs02; see [Note03](03_TND_OC_E02_VERIFIED_CONSUMER_20261107.md).
Prepared for Edward Baker with substantial OpenAI Codex assistance; exact
backend model/effort unavailable in the exposed session metadata.
