# Full Gaussian factorial marginals and canonical pair approximation

8 November 2026, America/New_York. Prepared for **Edward Baker**, with
substantial OpenAI Codex LLM assistance. Actual recorded model and effort:
unavailable. Authenticated chat0003, thread
`01a1bbc2-ac28-71c1-8bf0-aefeb0b06ce8`, turn
`01a1bc8e-0136-7063-88d9-b1ea607e8d23`. No model change or delegation.

**Status: preliminary analytical derivations; proved in-note/manuscript,
proof-author checking only.** The accepted E02 log/source estimates are
inputs. E03/E04 remain separately pending. The new fixed assessment is E07.
The full proofs are in the current manuscript sections listed below;
this note records the selected research object, new calculations, and
continuation boundary. It supersedes Note08's prospective status, not its
dated account of the author's scope correction.

Read the [result index](../../../../../../result-summaries/README.md) and
[avoid index](../../../../../../avoid/README.md), particularly
[cluster11](../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md),
[classification01](../../../../../../avoid/01_restating_the_target.md),
[shape controls02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and
[status06](../../../../../../avoid/06_status_stronger_than_the_evidence.md).

## 1. B05 selection and the fixed E06 contract

The author requests a manuscript about generalized pair and higher
correlations obtained by marginalizing a zero configuration, potentially
using Gaussian smoothing. B05 considered its two named constructions
once each. Direct factorial convolution is selected as the base object;
an explicit center mixture and unfolding supply its statistical extension.
They are compatible levels of one construction. No canonical Gaussian or
Vandermonde ensemble is assumed.

The fixed E06 work is to derive the joint-to-marginal normalization,
soft-window interpretation, factorial self subtraction, generating
functional, smoothing flow and bias, separation projections, center
covariance, and a two-sided source-to-full-pair error estimate. These
derivations and their manuscript integration are completed here. The
covariance's canonical shape remains an identified question, not an
acquired result. Classification: exact representations and a quantitative
approximation estimate, not an RH-equivalent criterion or a favorable-value
claim. No numerical campaign was opened.

## 2. The primary hierarchy and the full joint law

For a finite labelled zero multiset z_1,...,z_N, including separate labels
for multiplicity copies, let G_e(u)=(2*pi*e^2)^(-1) exp(-|u|^2/(2e^2)).
The symmetric full probability density is

    p_N,e(u_1,...,u_N) = (1/N!) sum_sigma product_a G_e(u_a-z_sigma(a)).

Integrating N-k coordinates leaves each ordered distinct k-tuple exactly
(N-k)! times. Hence the marginal is R_k,e/(N)_k, where R_k,e is the
distinct-label Gaussian product sum. Its total mass is (N)_k and integrating
one coordinate multiplies R_(k-1),e by N-k+1.

For a compact C² window 0<=W<=1, put w_j=W(z_j) and define

    R_k,e^W(u_1,...,u_k)
       = sum_distinct j_1,...,j_k product_a w_j_a G_e(u_a-z_j_a).

These are the factorial correlation functions of independent retention
with probabilities w_j followed by independent Gaussian observation
noise. The underlying canonical configuration is fixed. The retained
count is random: the total mass is Z_k=k! e_k(w), not a generally fixed
(N)_k. Conditional on retained count m, the normalized full observation
law has marginals p_m^(k), and

    R_k,e^W = sum_(m>=k) (m)_k Pr(M=m) p_m^(k).

The densities R_k/Z_k need not be consistent marginals across k.
Reweighting an ensemble joint law by product_j W(z_j) and renormalizing
is a different operation; it changes the ensemble and partition function.

The pair is the four-real-variable function

    R_2(u,v)=r(u)r(v)-d(u,v),
    r(u)=sum_j w_j G_e(u-z_j),
    d(u,v)=sum_j w_j² G_e(u-z_j)G_e(v-z_j).

The self subtraction has **w_j²**, not w_j. At a root of multiplicity m
the surviving coincident-position coefficient is m(m-1). The primary
object does not vanish on all-real configurations: their known Gaussian
transverse factors multiply a nontrivial horizontal spacing function.

Full proofs: [Gaussian marginals](../manuscript/sections/10_gaussian_marginals.tex).
The definitions follow the standard factorial-measure convention in
Borodin, *Determinantal point processes*, §2; distinct labels accommodate
multiple roots. No determinantal structure is imported for canonical zeros.

## 3. All orders, smoothing, projections and tails

The generating functional is

    G[f] = product_j (1+w_j integral f(u)G_e(u-z_j)dA(u))
         = sum_k (1/k!) integral product_a f(u_a) R_k(u) dA^k.

If ||f||<=q and M_W=sum_j w_j, its absolute tail after order K is at most
exp(qM_W)(qM_W)^(K+1)/(K+1)!. This follows from Z_k<=M_W^k and the
exponential series, not a dynamical closure assumption.

For tau=e²/2, differentiation of the Gaussian gives
partial_tau R_k=sum_a Delta_(u_a) R_k. This auxiliary smoothing time is
distinct from Newman lambda. For F in C_b²,

    |integral F R_k - alpha_k^W(F)|
       <= (e²/2) Z_k ||sum_a Delta_(u_a)F||_infty.

Integrate P_tau F-F=int_0^tau P_t(sum Delta F)dt against alpha_k^W to
prove the inequality. It is a weak bias bound; the limiting zero measure
is atomic, so no smooth-density uniform limit is asserted.

For countable weighted configurations with finite M_W, omitting total
weight T costs at most k A_e^k M_W^(k-1)T in sup norm and
k M_W^(k-1)T in L¹, where A_e=sup G_e. Every omitted tuple has an omitted
index in one of k slots. A Gaussian physical window would therefore need
its own bound on M_W and T. Our canonical theorem uses a compact window;
the observation Gaussian does not create a source-test tail.

The common horizontal center, horizontal separation and two imaginary
marks give coordinates (c,s,a,b) with unit Jacobian. Integrating c gives
a two-mark separation density. Integrating the entire complex center
instead gives sum_(j!=k) w_jw_k G_(sqrt(2)e)(s-(z_j-z_k)), which loses
the common transverse coordinate. The difference width sqrt(2)e follows
by completing the Gaussian square. These are declared projections, not
substitutes for the full function.

## 4. Center averaging and a specific further question

Choose a probability law pi on a compact I subset [10,infinity), a window
W_X, width e_X, and positive unfolding scales l_X,b_X. Put
T_X(zeta)=X+l_X Re(zeta)+i b_X Im(zeta) and J_X=l_X b_X. The unfolded
density is J_X^k R_k,X(T_X zeta_1,...,T_X zeta_k); then average over pi.
Physical smoothing before unfolding has widths e_X/l_X and e_X/b_X in
the unfolded coordinates. This convention is stated before comparisons.

Writing tilde-r and tilde-d for the unfolded first and self intensities,

    bar-R_2(zeta,eta)-bar-r(zeta)bar-r(eta)
       = Cov_pi(tilde-r_X(zeta),tilde-r_X(eta)) - E_pi tilde-d_X(zeta,eta).

This is immediate by averaging R_2=r*r-d. It isolates the source-specific
joint information still to be estimated. A formula for covariance is
not an estimate of its value. Compact center laws include a normalized
truncated Gaussian; an untruncated law needs a separate tail payment.

The manuscript also derives the classical circular Vandermonde marginal
by finite Fourier orthogonality, yielding the sine-profile benchmark after
unfolding and the additional Gaussian difference convolution after
smoothing. This is a reference ensemble calculation, not a theta theorem.
Full derivations: [centers and marginals](../manuscript/sections/11_center_averaging.tex).

## 5. A new two-sided canonical full-pair estimate

Use the quintic cutoff P(t)=1-10t³+15t⁴-6t⁵ on (0,1), extended by 1 and
0. Set w(x)=P(2|x-X|/h-1), kappa(y)=P(|y|-1), W=w*kappa, and
theta_+(y)=P(1/2-16y), theta_-=1-theta_+. Here X>=10, 0<h<=1.

The support of theta_+W lies in the inner E02 disk centered at X+4i:

    |z-(X+4i)|² <= 1+(4+1/32)² = 17665/1024 < 625/36 = (25/6)².

Reflect for theta_-. Their values on the axis are 1/2 each. Therefore
real zeros have total weight one. Define the lower zero-free multiplier
by conjugating the upper one. The exact finite theta source is real entire,
so both disks inherit the same E02 source error delta, log error E_X,
anchor and Jensen population n_X. The total population needed is <=2n_X.

For a compact C² test psi supported in this rectangle,

    |(nu_H-nu_Hhat)(psi)|
       <= E_X/(2pi) sum_(sigma=+,-) ||Delta(theta_sigma psi)||_infty.

Proof: partition psi, use nu=(2pi)^(-1)Delta log|F| on each buffered disk,
remove the zero-free multiplier, and apply the accepted local L¹ log bound.
This neither folds out real roots nor requires a lower bound on zero spacing.

The explicit derivative costs are

    A=(2pi e²)^(-1), B=A/(sqrt(euler_number)*e), C=2A/e²,
    L=15/(4h)+30, D=24/h²+1536,
    L2=15/(2h)+30, D2=609/(8h²)+1536,
    U=D A+2L B+C,
    V=D2 A²+4L2 A B+2A C+2B².

The theta derivatives and kappa derivatives have disjoint supports;
this is why the vertical second-derivative cost is 1536 rather than
their sum plus a cross product. Applying the weak transfer to WG and
W²G_uG_v gives sup|r-rhat|<=E_X U/pi and sup|d-dhat|<=E_X V/pi.
Since r,rhat<=2n_X A, telescope their product and subtract d:

    sup_(u,v in C) |R_2,e^W(H0)-R_2,e^W(Hhat_J,U)|
       <= (E_X/pi)(4n_X A U+V).

This is the new quantitative milestone. For fixed h,X, its conservative
cost is O(E_X e^(-6)) as e decreases to zero. E_X=C_X(delta/M_X)^alpha_X,
with all constants inherited from E02 and both arithmetic/radial source
tails retained. Any fixed positive density tolerance can be met by finite
source cutoffs; no favorable correlation value or efficient runtime is
deduced. Integrating the unfolded error gives int_I J_X² E_pair(X) dpi.

The same partition expresses tilde-r_X as J_X/(2pi) times the sum of
integrals of log|F_X,sigma| against Delta(theta_sigma W_X G(T_X zeta-z)).
Its center covariance is therefore a centered product of explicit compact
log integrals. Estimating that product is the next canonical question.

Full proof and source precision choice:
[two-sided pair theorem](../manuscript/sections/12_full_pair_transfer.tex).
The higher hierarchy has exact formulas, but this canonical uniform error
theorem is established here only for k=2.

## 6. Controls, status and continuation boundary

The full hierarchy identities and Gaussian calculus hold for every
configuration satisfying their elementary hypotheses, including collision
controls. Their success on a control is required, not a defect. The
theta specialization uses the unchanged complete source and its safe anchor.
The manuscript's control table names each failed premise: Euler-factor
controls change coefficients/conductor; weighted-square and finite-tail
controls fail the unchanged complete source/reflection; reflected
super-Gaussians lack integer-square theta arithmetic; smooth-shape and
positive-primitive controls lack the full coefficient expansion; finite-prime
controls lack full reflection/all-coefficient identity; atomic and finite-
profile controls lack the full theta profile and eventual simplicity;
conditional endpoint controls fail ordinary Dirichlet-series arithmetic;
variable kernels fail the cosine oscillator/Newman equation; fractional
three-profile relaxations do not preserve an integer zero divisor.
The numerical collision certificates were not rerun: this is a premise-level
analytical screen of a generic representation and a source specialization.

**A scalar projection does not determine the full pair function.**
**Uniform approximation of that function does not determine its canonical
profile.** These are scope distinctions, not universal impossibility claims.
The earlier scalar results are preserved as supporting appendices with
their existing evidence status. The E03/E04 frozen input bytes are protected.

Next: E07, a fixed claim-level assessment of this derivation and its
manuscript proofs, with one bounded correction. After assessment, B06 can
select one center law/scale regime and compare at most two source-specific
routes to a joint covariance estimate. No new scalar-detector search or
canonical numerical campaign is the default. See
[Continuation11](../continuation-notes/11_TND_OC_AFTER_GAUSSIAN_MANUSCRIPT_AND_MODEL_CHANGE_20261108.md).
