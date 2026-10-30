# E08 R15 assessment: actual-carrier attraction and feedback limits

29 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort
ultra**, Investigation05 **chat0037**, *Continue CTF-E08 R15 assessment*.

**Disposition: accepted without mathematical correction**, at the fixed
physical mark (T,A)=(1/4,2), conditional on the accepted R10–R13 prepared
radial/common-path and physical-vector-mass inputs. All nine obligations
of the [frozen R15 packet][packet] pass. [Note98][proof] proves
\[
 h(s)\to q_{\lambda_*}\quad\hbox{in }H^1(\mathbb R^3),\qquad
 \beta(h(s))\to\lambda_*,\qquad \alpha(s)\to\lambda_*.
\]
Here q_lambda=M exp(−lambda V)/Z(lambda), and
Q(lambda*)=||q_lambda*||2²=E0/n. The original feedback and physical-mass
premise remain essential. R14's accepted state-class entropy obstruction
is preserved.

This is a different-model internal assessment of Astra/ultra's proof,
supported by three read-only Sol contributors and parent synthesis.
Shared inherited premises remain; this is not independent specialist
review, formal verification or an interval certificate. The source proof,
issued packet, earlier accepted inputs and Sol's R5 manuscript/companion
are unchanged. [Record40][record] separates byte/transcription checks
from mathematical assessment. [Progress05][progress] owns live status.

## 1. Same path, source, preparation and accepted inputs — pass

The carrier is exactly K1*F initially, with exterior F from Note98 (7),
and evolves with the original alpha=2G_W/D_W. Notes82 and 90, accepted
through [Review46][r46], supply the same carrier's uniform H1 budget,
e and grad e decay, positive global alpha bounds, pointwise defect
delta=alpha−beta, and energy error epsilon_E. In particular the accepted
defect is all-time, rather than an asymptotic estimate that omits an
initial interval. Its denominator is paid by n>=n_*>0 and D_h>=3E0.
No new scalar path or independent feedback is introduced.

Q'/Q=2(E_lambda V−E_2lambda V)>0 follows from strict decrease of
E_lambda V, whose derivative is −Var_lambda(V)<0. Gaussian domination
justifies the derivatives for lambda>0. Thus the quoted continuous
positive Q' and unique energy-selected lambda* are available before the
attraction argument; they alone do not prove attraction.

## 2. Complete-source initial slope and every endpoint — pass

All positive theta summands remain. Their uniformly dominated derivative
series gives the positive weighted average of the logarithmic derivatives
in Note98 (9). The extra carrier factor contributes at most 1/2;
2c/(j²R²−c)<2 and pi>3 give
\[
 R(\log f)'\le4+\tfrac18\log R-\tfrac{13}{2}R^2
                  \le-\tfrac{19}{8}R^2.
\]
Consequently g(q)=f(sqrt(q)) obeys (log g)'<=−19/16. Translating this
inequality and integrating pays the tail survival ratio and conditional
excess E[q−a|q>=a]<=16/19 without truncating the theta sum.

The exact coordinate projection is
nu(y)=2pi int_max(1,|y|)^infinity R f(R)dR. Fubini gives
tau(y)=E[R²−y²|R>=max(1,y)]/2 for y>=0, with even extension.
The ceilings 35/38 inside |y|<=1 and 8/19 outside follow. The projection
plateau retains the raw sphere. Although nu' jumps at ±1, tau nu is C1
and (tau nu)'=−y nu; internal traces cancel when integration by parts
is split there. Gaussian tails pay both infinite endpoints for exp(ty).
The tilt identity E_tY=t E_t tau therefore gives
\[
 -h_r(0,r)/(rh(0,r))\in[41/152,1/2],\qquad
             41/304\le z(0,r)\le1/2.
\]
At r=0 the same dominated differentiation yields
z(0,0)=−h_rr(0,0)/(2h(0,0)). The entire prepared inner ball is included;
the raw indicator is never reapplied after convolution.

[Reference17][ref17] attributes the classical integration factor. I also
checked [Saumard v3, Section 2, (5)–(6)][stein]: these are the tail formula
and integration identity with integrability and vanishing endpoint
conditions. The selected proof derives and pays these conditions itself;
no concentration, entropy or nonlinear-convergence theorem is imported.

## 3. Finite-time regularity before division by h — pass

The seed implies h0<=A0 exp(−m0 V), with A0=M/Z(M0), and
|grad h0|<=M0 b h0. This gives the stated C0 since
sup_r r² exp(−m0 r²)=1/(e m0). With F=h²+|grad h|², the exact
differentiation gives a bound by
22alpha h²+26alpha|grad h|²<=26baralpha F. The h², gradient and
mixed contributions in Note98 (21) have the stated signs and constants.

For f=exp(−26baralpha s)F, Kato gives a subsolution
w=(f−C0)_+. The inherited H1 estimate makes w uniformly L1 on a finite
time window. For a radial cutoff chi_R, integration gives errors bounded by
\[
 C R^{-2}\int_0^t\!\|w\|_1ds+
 C\bar\alpha\int_0^t\!\int_{R\le|X|\le2R}w\,dXds,
\]
after discarding −alpha int d w chi_R<=0. Both errors vanish; hence
w=0. This explicitly verifies the whole-space payment in (22).

Xi_c=h_r/b+c h is bounded on every finite window: outside the ball use
b>=r and (22); on its closure use inherited local classical regularity
and the smooth origin extension. Only local h_rr is used there. Neither
a global higher-derivative bound nor bounded logarithmic quotient has
been assumed.

## 4. Exact commutation and whole-space sign comparison — pass

An independent derivation, with p=h_r/b and a=2/r+alpha b, gives
\[
 p_s=p_{rr}+(2b'/b+a)p_r+
       (d'/b+2\alpha b'+\alpha d)p+\alpha(d'/b)h.
\]
Adding c h yields exactly Note98 (23), including source
−(alpha−c)(2cb'−d'/b)h. It is nonpositive at c=m and nonnegative
at c=Lambda, with the required initial signs.

Since b'/b=1/r−2r/[(1+r²)(2+r²)], the singular drift is 4/r plus
a smooth radial vector drift of at most linear growth. Even smooth
profiles lift to the R5 radial comparison equation at the origin.
The bounded potential and drift admit the quadratic infinity barrier
epsilon exp(Ks)(1+r²). After the usual time exponential removes the
potential's upper bound, positive maxima are localized and the local
sign principle applies. Sending epsilon to zero proves both comparisons.
This establishes m<=z<=Lambda without a prior global division estimate.
R5 is solely a comparison device; the physical PDE, mass and energy
integrals remain in R3.

## 5. Exact slope equation, confinement and beta average — pass

Logarithmic differentiation gives Note98 (26), with reaction
(alpha−z)(2b'z−d'/b). Direct differentiation of b and d gives
b' in [7/8,2] and gamma=−d'/b in [0,5], including smooth even
origin extensions. The proved slope band yields
mV<=K_s<=Lambda V and the normalized Gaussian confinement (27).
It pays polynomial h/h² moments and weighted first derivatives uniformly.

In physical dimension three, integration of div(vh²) has no origin
flux and zero infinite flux. Thus
\[
 D_h=2\int zb^2h^2,\qquad
 \beta=\frac{\int z^2b^2h^2}{\int zb^2h^2}.
\]
The denominator is strictly positive. Beta is therefore a positive
weighted average of the actual spatial slope, rather than a separately
chosen number or unproved spatial-extremum value.

## 6. Ordered envelopes and actual-defect convolution — pass

For k=7m/4 and K=4Lambda+5, the reaction multiplier lies in [k,K].
The scalar ODEs (29) are exactly the maximum/minimum over that multiplier.
Each preserves [m,Lambda], and their order is invariant at contact.
Freezing the actual bounded z in the spatial drift turns comparison of
the differences into the already paid bounded linear comparison, with
uniformly Lipschitz reaction. Spatial extrema need not be attained.

Subtracting gives the exact width identity
\[
 w'=-kw+(K-k)\operatorname{dist}(\alpha,[\ell,u])
                     \le-kw+(K-k)|\alpha-\beta|.
\]
The initial width is 1/2−41/304=111/304. The resulting convolution
in (32) is all-time; B>=a_*s and the accepted d1,d2 bound give (33),
including the resonance s exp(−ks). Every term tends to zero.
The transport term from the exact coefficient defect vanishes on the
spatially constant barriers. No delta derivative or arbitrary
dual-Lipschitz-forcing stability theorem is needed or asserted.

## 7. Quantitative H1 approximation and energy selection — pass

For c(s)=beta(h(s)), |z−c|<=Omega gives
|K_s−cV|<=Omega V. Both exponents are at least mV; their normalizations
are at least Z(Lambda). Subtraction of the normalized exponentials therefore
gives exactly the explicit P and |h−q_c|<=Omega P in (34).
The identity
\[
 \nabla h-\nabla q_c=-(z-c)vh-cv(h-q_c)
\]
pays the extra gradient cost and C_H in (36). Every displayed weighted
integral is finite by V>=r²/2 and |v|<=2r. No Fisher hypothesis,
higher derivative or compactness-to-stationarity argument is hidden here.

The difference-of-squares bound gives
|Q(c)−Q(lambda*)|<=epsilon_E+2B2||P||2 Omega=mathcal E.
Since c stays in [m,Lambda], compactness of this scalar interval and
strict monotonicity first put lambda* in the interval and force c→lambda*.
Then q_*=min Q'>0 and finite L_H=sup||partial_lambda q_lambda||H1
give both quantitative estimates in (38). Gaussian domination pays L_H
and its gradient term. This is an actual-profile estimate followed by
energy selection; stationary uniqueness alone is never used as attraction.

## 8. Original feedback's spatial derivatives and denominator — pass

The inherited error decay and (38) yield
\[
 \|W-aq_{\lambda_*}\|_{H^1}
 \le\sqrt n\|h-q_{\lambda_*}\|_{H^1}
       +\sqrt{L_\Sigma+T_\Sigma}e^{-B/4}\to0.
\]
Consequently G_W→n||grad q_lambda*||2². Since d is bounded,
D_W→n int d q_lambda*²>0. Integrating div(vq_lambda*²) gives
2||grad q_lambda*||2²=lambda* int d q_lambda*², so the genuine
original quotient tends to lambda*. This independently checks (39).
It uses H1 convergence, not L2 alone. No temporal alpha' limit is claimed.

## 9. Matched direct comparison, controls and preserved scope — pass

The equally informed direct method receives the complete source,
preparation, physical margin, original coefficient path and inherited
error/energy data and can reproduce every step. There is no
primitive-specific advantage, smaller complete-production allowance,
favorable carrier production sign or physical-margin removal.

The [control register][controls] is applied individually:

| Control family | Failed or conditional premise of this application |
| --- | --- |
| Positive weighted-square source | Positive coefficients with the same summands/preparation inherit the seed; at an admitted double event vector mass mu=0, so n>0 and its global feedback/selection inputs fail. Registered high-frequency events are outside the fixed A=2 mark. |
| Euler-factor | Modified source gets no unchanged-theta seed automatically; a negative Laguerre witness alone is not a double event. Any actual double event loses positive vector mass. |
| Reflected super-Gaussian and smooth shape/positive primitive | Positivity, reflection or primitive endpoints alone do not supply this quantitative theta preparation seed or vector-mass premise. No universal impossibility is inferred. |
| Finite-prime and RH-conditional source | Their source restrictions, parameter domains and conditionality remain; the original theta seed/margin is not transferred without proof. |
| Atomic/profile | Original preparation, smooth path, derivative and moment payments must be checked for that control; they are not inherited merely from positive mass. |
| Fixed theta amplitude, variable observation | Literal cosine/Newman observation and its physical-mass argument are absent. |

The genuine residual, raw/prepared mismatch, centered primitive endpoints,
full source C0/C1, combined sphere cancellation and entire inner ball
remain. Note98 changes none of them. R14 excludes a universal entropy
sign on its stated exact mass–energy state class; that class does not
impose the common slope premise proved here. Its counterexamples are
not actual-orbit realizations, and no assertion that every individual
counterexample violates every finite slope band is needed.

This is an auxiliary-flow milestone under [avoid01][a01], not an
RH-equivalent criterion or new theta collision exclusion. Read the
[result index][results] and [avoid index][avoid], especially
[shared premises][a05], [scoped conclusions][a07], [imports][a16] and
[parallel writers][a17]. All nine checks complete E08 R15. No E07
execution gap remains in this proof, and no integration is assigned.
The [research return][return] and [continuation][next] record the next
decision and preserve both chats' actual identities.

[packet]: ../research-progress/handoffs/CTF-E08_RADIAL_LOG_SLOPE_ATTRACTION_ASSESSMENT_R15_20261029.md
[proof]: ../notes/98_RADIAL_LOG_SLOPE_ATTRACTION_B02_R15_20261029.md
[r46]: 46_COMPLETE_CARRIER_REDUCTION_E08_R13_ASSESSMENT_20261029.md
[ref17]: ../references/17_STEIN_KERNEL_PREPARATION_IDENTITY_SCOPE_20261029.md
[stein]: https://arxiv.org/html/1804.03926v3#S2
[record]: ../numerics/40_RADIAL_LOG_SLOPE_ATTRACTION_R15_E08_ASSESSMENT_RECORD_20261029.json
[progress]: ../research-progress/05_CONSERVATIVE_THETA_FLOW_ESTIMATES_RESEARCH_PROGRESS_20261029.md
[return]: ../notes/CTF_E08_R15_RADIAL_ATTRACTION_RESEARCH_RETURN_20261029.md
[next]: ../notes/CTF_E08_R15_ASSESSMENT_AND_MODEL_CONTINUATION_20261029.md
[results]: ../../../../result-summaries/README.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../avoid/README.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a05]: ../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a16]: ../../../../avoid/16_unchecked_imports_and_novelty_claims.md
[a17]: ../../../../avoid/17_parallel_writers_and_broken_registries.md
