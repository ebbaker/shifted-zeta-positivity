# E08 assessment of the joint source interface

8 November 2026, America/New_York. Prepared for **Edward Baker**, with
substantial OpenAI Codex LLM assistance, authenticated chat0007, thread
01a1bd52-6850-7b02-a292-10c8c1d4b525, turn
01a1bd52-7c36-7db2-81b9-0512fc129c38. The captured model configurations
are empty; actual backend model and reasoning effort are unavailable.
Root writes; three read-only helpers at inherited settings checked claims
1–4, 5–6 and 7–8. This is internal LLM assessment with shared premises,
not specialist or verified different-model review.

**Result: all eight E08 claims accepted unchanged.** One analytical pass
completed; no correction pass was needed. All 28 frozen inputs15 match.
[Review09](../reviews/09_TND_OC_E08_CLAIM_LEVEL_ASSESSMENT_20261108.md)
owns the assessment; the [sole register](../research-progress/01_TND_OC_RESEARCH_PROGRESS_20261107.md)
owns live status. [Note11](11_TND_OC_B06_CENTER_LAW_AND_JOINT_SOURCE_DECISION_20261108.md)
remains byte-identical to the assessed source.

Read the [result index](../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../avoid/README.md), particularly
[cluster11](../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
[classification01](../../../../../../avoid/01_restating_the_target.md),
[shape02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [separate-bounds12](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
Classification: quantitative approximation and a scoped obstruction for
harmonic replacements; no RH-equivalent criterion. Acceptance concerns
the displayed errors, not a canonical moment value.

## 1. Common normalization and Fourier error

For every fixed finite T>=10 and X in [T,2T], the outer-disk exact bound
2X+25 is at most 4T+25. Adding delta<=1 gives the common normalization
mathsf M=4T+26. The exact anchor c_0 becomes at least c_0/2 for the
approximant. Both normalized fields therefore have the common a_*, n
and alpha of Note11 (3), with at most m=2n active labels. This counts
multiplicities and retains real labels with partition weights summing
to one. The support buffer is 625/36-17665/1024>0.

J_T G_(epsilon_T)(ell_T zeta-xi)=G_tau(zeta-xi/ell_T).
Thus R=m/(2pi tau^2) and D=m/(4pi^2 tau^4). Fixed T supplies positive
epsilon_T and the width floor h_min=1. Neither a height-uniform cutoff
nor a limiting density follows.

For complex A=A_X(k), B=A_X(q), bilinear covariance satisfies

\[
 |\mathbb E[(A-\mathbb EA)(B-\mathbb EB)]|
 \le\sqrt{(\mathbb E|A|^2-|\mathbb EA|^2)
           (\mathbb E|B|^2-|\mathbb EB|^2)}\le m^2.
\]

No conjugation belongs in the Fourier identity itself. The self transform
uses B_X(k+q), with W_X^2. Each planar Gaussian has frequency integral
2pi/tau^2 and disk-exterior fraction exp(-s). The complement of the
product of two frequency disks has fraction 2exp(-s)-exp(-2s).
Multiplication by (m^2+m)/(2pi)^4 gives Note11 (6) exactly.

The common-center phase in (7) depends on k_x+q_x, and the transverse
phases keep both marks. A difference-only projection cannot determine
this general transform. The finite translation screen is confined to
arbitrary finite configurations, not another canonical zero set.
The H-coordinate x=2 gamma requires BGST's height T/2 and log(T/2).
The selected-source recheck is recorded in
[reference07](../references/07_TND_OC_E08_SOURCE_SCOPE_RECHECK_20261108.md).

## 2. Two separate boundary comparisons and harmonic scope

For restriction and renormalization, decompose the original center law
as (1-p)pi_core+p pi_edge with p=2/T. A quantity in [0,L] changes
by at most pL. Use L=R, R^2 and D for intensity, raw product and self.
The product of means costs at most 2pR^2, by telescoping factors in
[0,R]. Their sum is p(3R^2+D).

For deletion of labels outside [T,2T] with the original center law,
the original and truncated intensities agree off the edge strips.
On the strips the truncated intensity, raw product and self term are
between zero and their originals. This gives the same separate bound.
Combining both operations would require a separate comparison; (8) does
not silently pay two operations. Keeping the exact declared interval
and labels adds zero boundary error.

Each source test is compact C^2 inside its disk. If h is harmonic on
a neighborhood of that full closed disk, distributional integration
by parts gives integral h Delta(phi)=integral phi Delta(h)=0.
The contracted random variable is identically zero pathwise, so all
contracted covariance cross terms vanish without assuming a pointwise
log-field covariance exists. This concerns only the stated harmonic
replacement class; contours and estimates retaining the nonharmonic
residual are outside the exclusion.

## 3. Squared modulus, endpoints and polynomial tail

Put t=|f|^2 in [0,1]. E02 gives
A{t<u}<=Lambda u^(1/n). For u>=1 the majorant exceeds the whole disk
area, since Lambda=n pi(26/3)^2 exp(102a_*/n)>=pi r^2.
The layer-cake identity, including the upper endpoint, is

\[
 \int e^{-at}\,dA
 =a\int_0^\infty e^{-au}\operatorname{area}\{t<u\}\,du
 \le\Lambda\Gamma(1+1/n)a^{-1/n}\le\Lambda a^{-1/n}.
\]

The final inequality is Jensen concavity of x^(1/n) under the unit
exponential law. Nonnegative-series Tonelli and (1-t)^a<=exp(-at)
then give Lambda/2 times sum_(a>M) a^(-1-1/n), at most
n Lambda M^(-1/n)/2. The nonzero anchor excludes an identically zero
field; its isolated zeros have area zero. Local log integrability is
already paid by the same sublevel estimate, with multiplicity allowed.

For P=P_M and holomorphic f,

\[
 \Delta P(|f|^2)=4|f'|^2(tP'(t))'
              =2M|f'|^2(1-t)^{M-1}.
\]

This is a polynomial identity and extends across zeros and t=1.
The approximation retains nonharmonic information.

## 4. Products, signed self term and moment precision

Two disks, each of area pi r^2, give summed kernel L1 bounds
kappa=J_T r^2 U and nu=J_T^2 r^2 V, including every disk-sign pair.
Their supremum bounds with the log-tail give precisely d_M and e_M
in Note11. No positivity of the polynomial intensity is needed:
|r_X^(M)|<=R+d_M. A raw product or product of averaged means therefore
changes by at most 2R d_M+d_M^2. Paying both gives
4R d_M+2d_M^2+e_M; the direct full pair pays only one product.

Each polynomial log contraction carries a minus one-half coefficient.
Their covariance carries +1/(4ab); subtraction of the self contraction
carries +1/(2a). The latter kernel is signed and retains W^2.
All moments in (14) share the same X. Replacing them by independently
centered products would erase the needed information.

Projection of real estimated means onto [0,1] cannot increase their
error. Products of clipped and true means then differ by at most
2delta_1. The double kernel contraction costs
kappa^2 H_M^2(delta_2+2delta_1)/4, and the self mean costs
nu H_M delta_1/2. For direct full pairs the product-of-means cost is
absent. A polynomial surrogate need not be nonnegative or itself the
factorial density of a point-process law.

## 5. Both complete source tails and the three shares

Let a=J_T E U/pi and R=2nJ_T A_e. Both exact and finite-source
intensities are in [0,R]. The averaged raw product costs 2Ra;
the product of averaged means costs another 2Ra. The self cost is
J_T^2 E V/pi. Their sum is (18), with coefficient 8nA_eU+V.
The direct full pair needs only the first product payment.

The arithmetic term 5C_2(J_c)I_(17/2) and the radial term
B_source I_(17/2)^(>U_c) both remain. The explicit enlarged-disk
multiplier is increasing for positive X, so mathcal B_(2T) covers
the whole center interval; reflection gives the other disk. A useful
explicit reading of step 1 is

\[
 \delta_* =\min\left(1,c_0/2,\mathsf M
 \left[\frac{e\pi}{3J_T^2 C(a_*,n)(8nA_eU+V)}\right]^{1/\alpha}\right).
\]

Choose each tail inside (17)'s brackets at most
delta_*/(2 mathcal B_(2T)). Their separate decay gives finite cutoffs
for fixed T and e. This spells out the existing budget, without
changing its method or estimating the canonical value.

For step 2 let A=4Rg+v>0 and x=M^(-1/n). The declared M implies
x<=x_*, hence Ax<=e/6 and 2g^2x^2<=e/6. For step 3 set both moment
errors equal to d. Equation (16) is then
d[(3/4)kappa^2 H_M^2+(1/2)nu H_M], and the stated d makes it at
most e/3. Together the three shares give e. The direct full-pair
formula has smaller errors and is covered by the same budget.

## 6. Controls and exact consumer

The analytical control screen in Note11 section 7 passes: the generic
identities and error bounds remain valid for controls meeting their
hypotheses. The distinguishing canonical premises fail as follows:
Euler-factor controls change coefficients/conductor; weighted-square,
finite-tail and finite-prime-orbit controls lack full normalized reflection
or all-coefficient identity; reflected super-Gaussian, smooth-shape and
positive-primitive controls lack the complete theta arithmetic; atomic
threshold/exact finite profiles lack that profile and the stated eventual
simplicity; the RH-conditional theta-close endpoint lacks ordinary
Dirichlet-series arithmetic; variable kernels fail the literal cosine
oscillator/Newman equation; fractional relaxations lack integer
zero-divisor realizability. These are premise checks, not new collision
certificate runs or favorable theta estimates.

**E08 accepts the finite accuracy interface and scoped stop unchanged.**
It acquires no moment array, canonical full-pair value, limiting profile,
practical runtime, higher-order transfer, RH gain or Newman dynamics.
Step 3 of Note11 section 6 remains unpaid. B07 requires a named arithmetic
joint estimate or certified evaluator with explicit uniform errors and
a finite work budget; a stronger directly contracted estimate may qualify
with its own proof and complete errors. E03/E04 remain separately pending.
The manuscript and all frozen sources remain unchanged; no manuscript
milestone or investigation closure is declared.
