# E16 r1: assessment of the Gaussian Laguerre and Green-strip packages

7 November 2026 UTC; 6 November 2026 America/New_York. Prepared for
**Edward Baker** with substantial OpenAI Codex assistance. Assessor explicitly
tool-selected as **gpt-6.1-sol, ultra** under the lead's E16 dispatch. This
records the selected configuration, not independent verification of the
serving backend.

**Disposition: accepted without mathematical correction within the stated
scope.** [Note24](../notes/24_TND_O_E15_GAUSSIAN_LAGUERRE_HIERARCHY_20261107.md)
pays the complete Gaussian quadratic formula, all-order hierarchy and joint
source/order remainder, every finite real multiplicity's local diagnostic,
and its variance conflict. [Note25](../notes/25_TND_O_B03_R5_COMPLETE_GREEN_STRIP_POTENTIAL_20261107.md)
pays the complete strip Green–Jensen identity, real-boundary logarithms,
product limit, exponential tails and one-defect margin. Neither note
acquires the favorable canonical signed comparison needed for exclusion.

This is one substantive internal LLM audit followed by one bounded
consistency check. The assessor shares inherited premises and the model
family with the proof work. The root's read-only Green derivation, the
lead's checks, and this assessment are not independent specialist review.
There was no subdelegation, numerical or symbolic research run, new source
acquisition, source edit, manuscript edit, transcript or shared-file edit.

## 1. Contract, freeze and assessment boundary

The exact [request30](../research-progress/handoffs/30_TND_O_E16_LOCALIZED_METRICS_ASSESSMENT_REQUEST_20261107.md)
and [inputs30](../research-progress/handoffs/30_TND_O_E16_LOCALIZED_METRICS_ASSESSMENT_INPUTS_20261107.json)
govern the audit. All **19** input byte counts and SHA-256 hashes matched
before assessment and again at return. Inputs30 itself has SHA-256
`769d11de073957a9bf9a9bb76ea6877142732149cab31c67dc3d7296d63dec14`.
The exact per-file records and this review's digest are in
[return30](../research-progress/handoffs/30_TND_O_E16_LOCALIZED_METRICS_ASSESSMENT_RETURN_20261107.json).
Hashes identify the inspected versions; they do not certify mathematics.

Root policies, [Continuation16](../notes/16_TND_O_SMOOTH_LOCALIZATION_CONTINUATION_ASTRA_SOL_ULTRA_20261106.md),
the actual broader-metric [Decision14](../brainstorm/notes/14_TND_O_B03_R5_TWO_METRIC_DECISION_20261107.md),
the live register at its frozen version, request/input/return28–29 and all
fixed mathematical dependencies in inputs30 were read. The source,
product, strip and count claims from M section 2 and Notes17–18 are the
declared inherited inputs; this assessment checks their use by the new
packages rather than claiming a new specialist audit of their literature.
Receipt13 remains abstract-level context, importing no criterion or
numerical constant. Return28's earlier status-only register change and
return29's pre-freeze wording correction retain their recorded provenance.

The [result index](../../../../../result-summaries/README.md),
[controls12](../../../../../result-summaries/12_collision_controls_and_screening.md),
[patterns index](../../../../../avoid/README.md),
[target classification01](../../../../../avoid/01_restating_the_target.md),
[control rule02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[shared-premise rule05](../../../../../avoid/05_same_model_reviews_and_shared_premises.md),
[scope07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md) and
[normalization08](../../../../../avoid/08_normalization_and_constant_slips.md)
set the evidentiary boundary. No new all-window or real-rootedness criterion
is proposed here.

## 2. Note24: accepted Gaussian hierarchy and collision diagnostic

**Transform, variance and signed energy identity, equations (2)–(9).**
With the stated half Fourier transform, symmetrizing the quadratic
multiplier gives exactly
\[
 \frac18(-pq)^n(p-q)^2.
\]
The characteristic function of the normalized Gaussian supplies
\(e^{iX(p+q)-v(p+q)^2/2}\), where \(v\) is variance. Opposite simultaneous
reflection removes the imaginary part. The four quadrants give the
\(1/4\) half-line formula, with the stated \((-1)^n\) on the same-sign
term and no such sign on the opposite-sign term. Substitution of the full
positive theta sum therefore gives the complete signed formula (8).

Integration by parts gives
\(A_0=2\int wH_x^2-\tfrac12\int w''H^2\). Expanding
\(\int|(H\sqrt w)'|^2\) then gives exactly
\[
 A_0=2E_w-Z/(2v)=Z_\lambda+\tfrac12Z_{XX}
\]
at fixed variance. Thus the threshold is \(E_w\ge Z/(4v)\), which is
stronger than ordinary positivity of kinetic energy. The reuse of M
section 4 is correctly identified; the local formula makes no new generic
energy exclusion.

**All-order hierarchy and its two time directions, equations (10)–(14).**
The direct identities
\((L_f)_\lambda=(f'')^2+ff''''-2f'f'''\) and
\((L_f)''=(f'')^2-ff''''\) imply the stated minus spatial sign and the
\(+2A_{n+1}\) term. Gaussian variance differentiation gives the second
identity and hence the general schedule coefficient \(v'/2-1\).

The factorial allowance (12), including its \(1/4\) constant, is valid
for every \(n\). After absorbing
\(|pq|^n\le n!\epsilon^{-n}e^{\epsilon(p^2+q^2)/2}\), the remaining
nonnegative \((p-q)^2\) integral equals \(2M_0M_2\) by evenness; taking
the phase modulus has not invalidated that cancellation. It also proves
the pointwise defect bound. Source moments are finite at the shifted
time \(L+\epsilon/2\); their dependence on \(\epsilon\) is retained.

On \(v_0+2h>0\), the exact kernel ratio is \(e^{-2hpq}\). Its exponential
series gives (13) for positive and negative \(h\), with integrable absolute
majorant \(e^{|h|(p^2+q^2)}\). No backward hierarchy is inferred from a
finite differential truncation. The binomial tail in (14) is correct for
\(|h|\le D\), \(\epsilon>2D\), \(r=2D/\epsilon<q_*<1\).
In particular the factors \(n!\epsilon^{-n}(1-q_*)^{-n-1}\) remain costs
in a growing-order limit, and neither variance endpoint needs a uniform
positive lower bound for this absolute estimate.

**Complete theta index, radial line and joint remainder, equations
(15)–(22).** The reflected finite source is used only inside integrals;
its missing endpoint smoothness is neither denied nor used. It satisfies
\(0\le\Phi_{N,U}\le\Phi\). The positive source difference gives (16),
including its possible harmless double counting of index and radial tails.
For consecutive index terms the ratio is bounded by
\(16e^{-\pi(2N+3)}<1\), proving (17). The substitution
\(s=\pi e^{4|p|}\) gives exactly the factor \(2/4^{j+1}\) in (18).
For \(j=0,2\), the two logarithm inequalities in the proof of (19) give
the stated threshold, \(c_0=1\), \(c_2=(8/e)^2\), and
\(2^{5/2}\Gamma(5/2,R_U/2)/\sqrt\pi\) factor. No omitted
order-dependent constant is present.

The product difference is positive and even in each variable, so its
\((p-q)^2\) integral is twice
\(M_0M_2-M_0^{N,U}M_2^{N,U}\). This proves the \(1/4\) prefactor in
\(\mathcal T_\epsilon\) as defined in (20), without an unpaid cross term. Summing
the coefficient errors gives \((1-r)^{-n-1}\), while the order tail
retains \((r/q_*)^{K+1}(1-q_*)^{-n-1}\). Thus (22) correctly controls
joint \(n,K,N,U\), every real center, and every positive endpoint
variance. It supplies convergence and an explicit absolute allowance;
it does not supply favorable sign or inexpensive acquisition.

**Every finite real multiplicity, equations (23)–(29).** For
\(g=\partial_x^{m-2}H_{\lambda_*-t}(x_*+y)\), the heat equation and
the global bounds \(C=M_{m+1}(L)/2\), \(D=M_{m+2}(L)/2\) give all three
rows of (25) on the full real line. In particular, the first time
remainder is \(Dt^2/2\), not \(Dt\). Expanding \((g_y)^2-gg_{yy}\)
from these rows gives the five error groups printed after (26):
\[
\begin{split}
 &bCt^{3/2}(4|z|+5|z|^3/3)
 +bDt^2(3/2+z^2/2)\\
 &\quad+C^2t^2(1+2z^2+5z^4/12)
 +CDt^{5/2}(3|z|/2+|z|^3/6)+D^2t^3/2.
\end{split}
\]
Taking the declared Gaussian moments verifies every coefficient in (26).
The leading term is therefore
\(a_m^2t(\kappa/2-1)\) for all finite \(m\ge2\), not merely doubles
and triples. Equation (5) exposes factorial multiplicity dependence of
the global derivative constants. The criterion (27) follows with the
printed strict negative margin for positive sufficiently small \(t\).

The local alternative also pays its exterior. Spatial Cauchy radii
\(R/2\) on \(|y|\le R/2\) give exactly (28). The identity
\(E[y^2\mathbf1_{|y|>r_0}]=\kappa t[P(z_0)+2z_0\varphi(z_0)]\)
gives (29), including both its polynomial leading-term tail and its
global defect allowance \(G\). The canonical bounds on \(B\) and \(G\)
are available from the complete source and (12). Local entire
continuation alone is not substituted for global Gaussian integrability.

For a real nonzero scalar rescaling of the field, \(A_n\) and
\(|a_m|^2\) both scale quadratically; the relative costs remain
\(C/|a_m|\), \(D/|a_m|\) and their products. No positive uniform lower
bound for \(|a_m|\), uniform event radius, height-uniform resolution
time or bound on the finite multiplicity is acquired. The direct field
observable is smooth at fixed positive variance; its resolving limit is
separately shrinking.

**Controls, variance conflict and unpaid comparison, equations
(30)–(36).** The quadratic and cubic defects and their Gaussian moments
are exact. The cubic's first defect stays positive while its derivative
defect resolves \(v<c/3\); both exact heat families reproduce the
coefficient \(a_m^2(\kappa/2-1)\). The resolving schedule has
\(v'=-\kappa\), hence spatial coefficient \(-(1+\kappa/2)\).
Cancellation requires \(v'=2\). Substituting
\(t=t_0-h\), \(v=\kappa t_0+2h\) gives exactly
\(h_{\rm exit}=(2-\kappa)t_0/4\); reverse traversal loses positive
variance at \(s=\kappa t_0/2\). No positive cancellation characteristic
reaches the event inside the resolving cone. Conditional forward
propagation of infinitely many initial nonnegative signs does not
provide those signs or preserve resolution.

The sufficient comparison (36) is correctly conditional: its lower bound
must hold at a resolving \(t\) with
\(E_\kappa<(1-\kappa/2-c)|a_m|^2t\). This would contradict (1).
Neither that signed quadratic-source estimate nor its normalized margin
is proved. An absolute allowance divided by \(|a_m|^2t\) need not be
small; this is a limitation of that allowance rather than a lower bound
on the true acquisition cost or a universal obstruction.

M section 10's exact colliding source shares positivity, reflection,
super-Gaussian decay, the heat/quadratic identities and finite moments
with its own constants. It fails the literal canonical theta expansion.
It is not assigned a canonical global strip, the canonical numerical
constants, or any other unproved premise. The weighted-square controls
likewise are not assigned full reflection; other controls retain only
the equations and bounds they actually satisfy. This is the correct
scope of the screen, not an exclusion of all localized metrics.

## 3. Note25: accepted complete Green-strip potential

**Strip normalization and finite factors, equations (1)–(5).** With
\(-\Delta G_B=2\pi\delta\), the displayed logarithmic reflected-distance
ratio has positive Green sign and singularity \(-\log|z-\zeta|\).
At \(B=8\), observation height 4, both Poisson kernels reduce to
\(K(t)=[16\cosh(\pi t/8)]^{-1}\), each of mass \(1/2\). The Green value
reduces to
\(\operatorname{atanh}[\sin(\pi y/8)/\cosh(\pi d/8)]\).

The harmonic correction is **\(\log|z-\zeta|+G_B(z,\zeta)\)**. Thus the
boundary average minus the interior logarithm is \(+G_B\). The
pre-freeze wording repair recorded in return29 is correctly incorporated;
there is no residual sign correction. Linear factors have only
logarithmic horizontal growth, so their vertical-side harmonic measures
vanish on strip exhaustion. Exterior zeros give zero. Boundary zeros
give locally integrable logarithms and no interior half-weight atom,
including at arbitrary finite real multiplicity.

The inherited even product is exact, with the constant \(H_\lambda(0)\)
and no surviving linear or quadratic exponential factor. Applying the
finite-factor identity to complete opposite pairs then cancels constants
because the two boundary masses add to one. This supplies the claimed
finite identity before the infinite limit; it is not a finite-source
surrogate for the canonical entire field.

**Uniform origin radius and complete logarithmic limit, equations
(6)–(8).** Positivity at the origin and the complete-source derivative
bound give \(m_0>0\), finite positive \(D_0\), and the zero-free radius
\(r_*\). The segment estimate is valid for complex \(z\) in that disk.
Compact time dependence also bounds \(C_0\). These constants are uniform
in the entire declared time interval.

The proof of (8) bounds the sum of absolute factor logarithms, which is
the needed stronger convergence statement. A near representative costs
at most \(4\log(3Q)+4+2|\log r_*|\) on a unit interval. The two negative
distance logs each integrate to at most 2, even for a zero on that
boundary and with multiplicity. There are at most
\(CQ\log(2Q+2)\) near representatives: this uses **half** the full
origin-centered count at radius \(2Q\), not half a horizontal count.
For far representatives, \(|z^2/\zeta^2|\le1/4\) gives the factor
\(4/3\), and partial summation with half the full count gives the
printed \((2/3)CQ\{\log(2Q+2)+1\}\). For \(Q\ge12\), these costs are
covered by the deliberately coarse
\(C_*=C_0+20C(1+|\log r_*|)\).

Consequently the product logarithms converge absolutely in local
\(L^1\), and their polynomial unit-interval majorant is summable against
the exponential Poisson weight. It gives absolute weighted \(L^1\)
convergence as well. The interior product converges at \(X+4i\), where
the common zero strip ensures nonvanishing. This justifies the complete
sum/integral passage in (3). In particular, no silent outer or harmonic
term remains after passing from the exact product.

**Both quantitative tails and the defect margin, equations (9)–(14).**
For the boundary tail, \(K\le e^{-ak}/8\), two horizontal intervals per
shell and two boundaries give the prefactor \(C_*/2\). The choice
\(S=|X|+13+\lfloor R\rfloor\) covers both interval locations. The
polynomial-logarithmic shell estimate and
\(\sum q_0^j(1+j)^3=(1+4q_0+q_0^2)/(1-q_0)^4\) give exactly (9).
Its displayed height factor is essential in joint limits.

For zeros, \(\sin(ay)\le ay\), \(\operatorname{sech}(ad)\le2e^{-a|d|}\)
and \(\operatorname{atanh}q\le q/(1-q^2)\) give
\(K_G=2a/\cos^2a\). Each of the two unit shells is bounded by the
inherited **full** horizontal count from Note18, with
\(\log(Q_X+k)\) and \(Q_X=3+|X|\). Using the stated logarithm
inequalities gives every term of (11), including the factor 2 and
\((n+1)^{-1}\). This proves the complete upper-zero sum converges and
gives the time-uniform \(O_A(\log(3+|X|))\) bound. The boundary-integral
tail and zero-statistic tail are distinct payments.

Concavity of \(\sin(ay)\) on \([0,1]\) and
\(\operatorname{atanh}q\ge q\) give exactly the positive one-defect lower
margin \(\sin(a)d/\cosh(ar)\) in (13). Positivity and scalar invariance
of \(J\) follow with the declared normalization. A nonzero complex
scalar adds \(\log|c|\) with total boundary mass one and subtracts it
at the observation point. No nonreal-zero exclusion follows from
positivity or the coarse count bound. The safe-line lower estimate (14)
follows by integrating \(\Re(H'/H)\), and its separate source upper
bound remains too coarse for the defect margin.

**Collisions and the remaining signed logarithmic comparison.**
Uniform tails on compact center ranges and continuity of finite root
multisets give continuity of \(J\) through collisions. Extending an upper
contribution by zero at height zero is continuous, so no root labeling or
boundary atom is required. At a real double event its height is of
square-root size in reverse time; the Green kernel has a nonzero linear
height coefficient. The stated square-root limitation is therefore
correct. The local real-double and small imaginary-pair factor checks
count zero and one upper contribution respectively. They give neither
general monotonicity nor the earlier transverse moment's Lipschitz law.

The exact unpaid input is a signed comparison of the two complete
boundary log averages with the interior log modulus, below the declared
one-defect margin. The note correctly does not insert a finite-source
approximation into a logarithm near a real zero from an absolute
\(H\)-tail alone. The acquired complete-product integrability proves
the identity and tails; it does not prove that missing relative margin.

## 4. Bounded consistency check and usable disposition

One bounded analytical check rederived the transform and Gaussian
factors, heat signs, characteristic exponential and binomial factors;
the index ratio, radial substitution and incomplete-gamma constants;
all five Taylor-error groups and their Gaussian moments; local Cauchy
and exterior-tail payments; quadratic/cubic controls and cone exit;
and the strip Green sign, two boundary masses, full versus representative
counts, logarithmic factor bound, two shell tails and defect margin.
It found **no mathematical correction**. No source version was changed.
Documentation checks verify the allocated output links and JSON records;
they carry no mathematical evidence beyond the written audit.

The accepted objects remain distinct: Note24 is a signed Gaussian
quadratic form indexed by field derivative order; Note25 is a positive
one-point nonreal-zero Green potential. Neither is the earlier Gaussian
Gram or pair-correlation statistic. All-window vanishing at the zeta
slice is not promoted into progress toward RH. The accepted 46-page E14
manuscript is unchanged; these two exact new packages remain research
notes with this internal assessment.

The actual successor is the lead-owned B04/B05 comparison of their
different unpaid signed-source and signed-boundary requirements, using
their actual margins and costs. This assessment makes that comparison
ready; it does not declare either further proof route ready solely from
the representations or positivity. Continuation remains authorized under
Note16 without a new permission boundary.
