# RSCT research state and obstacles

11 November 2026, America/New_York. Discussion prepared for **Edward Baker** with substantial OpenAI Codex LLM assistance, chat0004, actual title “Review RSCT research status.” Actual backend model and reasoning effort are unavailable in the recorded session configuration (`model_configurations: []`); no settings are inferred.

**Status: explanatory synthesis of existing results, not a new proof, independent assessment, or activation of B01 r10.** The investigation has acquired controlled local expressions and several precise failures of proposed estimating classes. It has acquired no favorable canonical signed bound or new collision-exclusion region. B01 r9 remains complete and E01 remains reserved, not executable, as recorded in the [sole register](../../research-progress/01_RSCT_RESEARCH_PROGRESS_20261111.md) and [continuation](../../notes/01_RSCT_CONTINUATION_AND_PROMPT_20261111.md).

Interpretation follows the [result index](../../../../../result-summaries/README.md), specifically [heat-flow cluster11](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md) and [collision controls12](../../../../../result-summaries/12_collision_controls_and_screening.md), and the [avoid index](../../../../../avoid/README.md), especially [endpoint reformulations01](../../../../../avoid/01_restating_the_target.md), [shared premises02](../../../../../avoid/02_shape_only_arguments_and_the_controls.md), [scoped exclusions07](../../../../../avoid/07_scoped_exclusions_read_as_universal.md), and [separate bounds12](../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md). This discussion introduces no new proposed criterion or estimating mechanism. The inherited endpoint reformulation is stated once; the substantive progress is the quantitative approximation and the scoped obstructions below.

## The inherited reduction and the desired contradiction

The canonical field and physical clock are
\[
H_T(z)=\int_0^\infty e^{Tu^2}\Phi(u)\cos(zu)\,du,
\qquad \partial_T H_T=-\partial_z^2H_T,
\qquad H_0(z)=\tfrac18\xi((1+iz)/2).
\]
Here \(\Phi\) is the complete canonical theta source. The threshold property is that every zero of \(H_T\) is real precisely for \(T\ge\Lambda\). The [collision manuscript](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex), `prop:finitecollision`, already proves that \(\Lambda>0\) forces a finite real multiple zero at time \(T=\Lambda\). Thus the proposed contradiction concerns
\[
0<T\le\tfrac12,\quad a>0,\quad H_T(a)=H_T'(a)=0,
\quad m\ge2,\quad \text{every zero of }H_T\text{ real}.
\]
Evenness forces an equal-multiplicity event at \(-a\). The ultimate exclusion is an RH-strength endpoint problem; rewriting its conditions is not an independently weaker theorem. Fixed-positive-time eventual simplicity and finite attainment are inherited. The upper bound on a possible exceptional height deteriorates like \(e^{C/T}\) as \(T\downarrow0\).

On the real axis the complete reflected RS representation has \(H_T=2\Re U_T\). A multiple zero with \(U_T\ne0\) forces \(\Im(U_T'/U_T)=0\); if \(U_T=0\), that phase is undefined. Neither the representation nor global all-realness alone supplies strict rotation of this particular arithmetic arm. [Note03](../../notes/03_RSCT_B01_REFLECTED_POISSON_TEST_20261111.md) retains both alternatives.

The more useful geometric observation is, for \(y>0\),
\[
Q(a,y)=-y\Im\frac{H_T'(a+iy)}{H_T(a+iy)}
=\sum_r\frac{y^2}{(a-r)^2+y^2}
=m k(a,y)+y^2 S(a,y),
\]
\[
k(a,y)=1+\frac{y^2}{4a^2+y^2},\qquad
S(a,y)=\sum_{r\ne\pm a}\frac1{(a-r)^2+y^2}>0.
\]
Zeros are counted with multiplicity and all copies at both event roots are removed from \(S\). The remaining canonical zero population makes \(S\) strictly positive. Consequently the denominator-free quantity
\[
\mathcal B(a,y)=2k|H_T(a+iy)|^2+
y\Im\bigl(H_T'(a+iy)\overline{H_T(a+iy)}\bigr)
=\bigl[(2-m)k-y^2S\bigr]|H_T(a+iy)|^2<0
\]
at the assumed event. An independently acquired opposing arithmetic sign would contradict it. The identity supplies the geometric side, not that missing sign.

## Quantitative progress and its limits

R2's complete signed logarithmic difference at imaginary offsets 4, 6, and 8 has magnitude less than \(13/72\), after uninstantiated high-height gates. A multiple all-real event then needs a noncentral contribution less than \(-1/36\). That is permitted because the associated zero kernel changes sign. R3's stronger finite matrix gives
\[
m\le\frac6{13}L+O(1),\qquad L=\log(a/(4\pi)).
\]
The bound grows with height; indeed its exact matrix passes every fixed proposed multiplicity eventually. It cannot exclude an ordinary double event there. These are the scopes of [Note04](../../notes/04_RSCT_B01_R2_SIGNED_THREE_HEIGHT_ESTIMATE_20261111.md) and [Note05](../../notes/05_RSCT_B01_R3_EVENT_SUBTRACTED_PICK_TEST_20261111.md), not realizations of an actual zero configuration.

R4 changes the observation scale to
\[
T=c/L,\quad c\in[1/2,1],\quad z=a+w/L,
\quad N=\lfloor e^{L/2}\rfloor.
\]
With the explicitly retained nonvanishing carrier \(A(T,z)\), it obtains
\[
f_a(w):=H_T(a+w/L)/A(T,a+w/L)
=q_a(w)+O_R(a^{-3/4}),
\]
\[
q_a(w)=\sum_{n\le N}d_n\cos(\phi_n+\lambda_n w)+K_a(w),
\quad
d_n=n^{-1/2}\exp\!\left\{\frac{c}{4L}[(\log n)^2-L\log n]\right\},
\]
\[
\lambda_n=\tfrac14-\frac{\log n}{2L},\qquad
\phi_n=\Theta(T,a)-\nu\log n,\qquad \nu=a/2+\pi T/8.
\]
Both reflected arms, every cutoff mode, heat weights and the full specified correction \(K_a\) remain. The holomorphic bound on a larger fixed scaled disk pays derivatives; R9 explicitly extends payment through order four. Under an event,
\[
f_a(w)=q_a(w)-q_a(0)-wq_a'(0)+O_R(a^{-3/4}|w|^2).
\]
At \(y=\beta/L\), fixed \(\beta>0\), the normalized form
\[
D_a(g)=\mathfrak d_a|g(i\beta)|^2+
\beta\Im\bigl(g'(i\beta)\overline{g(i\beta)}\bigr),
\quad
\mathfrak d_a=2k+\frac\beta L\Im\frac{A_z}{A}
=2+O_\beta(a^{-2}L^{-2})
\]
equals \(\mathcal B/|A|^2\) when \(g=f_a\). Its complete approximation error is \(o(1)\), without dividing by the possibly small field. The favorable sign of the actual correlated expression remains unproved. See [Note06 §§2–5](../../notes/06_RSCT_B01_R4_MICROSCOPIC_EVENT_EXPANSION_20261111.md).

Absolute values do not recover it. For each fixed order \(j\), the positive coefficient moments obey
\[
\sum_{n\le N}d_n\lambda_n^j
\sim\frac{2j!}{L^j}e^{(1/4-c/16)L}.
\]
After subtracting the two event equations, the specified termwise value allowance at \(i\beta\) is still asymptotic to
\(2\beta^2 e^{(1/4-c/16)L}/L^2\), which grows. This is the size of an upper allowance, not a lower bound on the actual field or approximation error. Known population and local-scaling work is credited in Note06; its extension here is the full fixed-order coefficient and this event-subtracted consumer.

## What the phase tests establish

The later passes test whether selected arithmetic constraints suffice for a nonnegative lower bound on \(D_a\). Each retains the stated local event equations and complete correction.

| Estimating class | Recorded result and boundary |
| --- | --- |
| R5 independent coefficient disks | Negative feasible value. Exact magnitudes and common phases fail. |
| R6 every exact coefficient magnitude, independently free phases | Negative feasible value. A necessary multiplicative phase identity fails. |
| R7 all unit-phase multiplicative identities and any fixed finite actual-prime calibration | Negative feasible value. Same-height phase agreement fails at another prime. |
| R8 actual phases through a specified growing prime cutoff | Negative feasible value. A moving prime outside the cutoff still disagrees with the actual height. |
| R9 that calibrated class plus the forced-mirror fourth-jet condition | One complete point has both the strict mirror sign and negative Poisson value. Global all-realness and physical realization remain unproved. |

For R8–R9 the paid range is
\[
Y=\gamma L^2(\log L)^2,\qquad 0<\gamma<9/256\text{ fixed}.
\]
Every prime through \(Y\), and every retained integer with only such prime factors, has its actual phase. Yet the construction gives
\[
q_*(0)=q_*'(0)=0,\qquad
D_a(q_*)\le-\kappa_\beta\frac{e^{(1/2-c/8)L}}{L^8}<0.
\]
The sufficient coefficient \(9/256\) is not a sharp success/failure threshold. The number of constrained primes grows, but \(Y\) is still much smaller than the complete cutoff \(N\). Matching every fixed prime eventually is not uniform agreement with the whole growing arithmetic population.

R9 adds the inherited necessary inequality, with physical derivatives \(H_j=H_T^{(j)}(a)\),
\[
2H_3^2-3H_2H_4\ge9H_2^2/a^2.
\]
It comes from deflating two event roots at \(a\) and retaining the mirror pair. R9 pays its normalized four-derivative error and constructs a single calibrated point with \(q_*''(0)<0<q_*''''(0)\), strictly positive normalized mirror margin, and the negative \(D_a\) above. Passing this necessary inequality does not imply the global all-real property. It is also vacuous for multiplicity at least four; the higher-multiplicity hierarchy needs other jets. The original condition and generic polynomial compatibility belong to the collision manuscript, not R9. [Note11](../../notes/11_RSCT_B01_R9_MIRROR_JET_COMPATIBILITY_20261111.md) and [Review09](../../reviews/09_RSCT_B01_R9_SAME_ASSISTANT_CHECK_20261111.md) supply the precise simultaneous construction and scope.

## The remaining obstacles

1. **Actual arithmetic correlations.** A multiplicative unit function can choose prime phases separately. Canonical phases must all satisfy \(\omega(p)=p^{-i\nu}\) at the same \(\nu=a/2+\pi T/8\), with that same height determining weights, cutoff, carrier and correction. R9 explicitly fails this at a moving prime. Realizing some phases at a different height would change the other data. The weighted coefficients themselves are not multiplicative: \(d_{mn}/(d_md_n)=\exp[c\log m\log n/(2L)]\) when \(mn\le N\).
2. **Full event information.** Two vanishing derivatives and one necessary fourth-jet inequality are weaker than a globally all-real canonical field. A stronger global or deflated-derivative condition remains outside the exclusions, but no tractable favorable method is established. R9 proves nothing about every finite collection of jet conditions.
3. **Exceptional-event control.** A positive average or a good typical-height estimate can coexist with one exceptional collision. Auxiliary integration over free prime phases is neither an actual-height average nor control of a particular threshold event.
4. **Coverage and uniformity.** The recent quantitative work treats sufficiently large \(a\) and \(c=T\log(a/(4\pi))\in[1/2,1]\). No premise puts an unknown threshold in that band. Bounded heights, other \(c\), arbitrarily small positive \(T\), and arbitrary physical multiplicity remain part of the goal. Constants/onsets are not numerically instantiated; a vanishing absolute error alone does not determine the sign of a smaller quantity.

The interpretation is that the selected estimating classes discard information that matters for this proposed sign argument. It is not a universal obstruction to RS methods, all global all-real arguments, or every finite-jet method. There is no quantitative measure here of proximity to a proof of RH.

The analytical control screen is inherited from [Note11 §5](../../notes/11_RSCT_B01_R9_MIRROR_JET_COMPATIBILITY_20261111.md), without a numerical rerun: the new phase point fails the actual same-height orbit and has no established global all-realness; quartic thresholds fail theta arithmetic and infinite population; atomic/finite-profile/continuous compact-source thresholds fail complete theta coefficients, profile growth and eventual threshold simplicity; Euler/translated sources alter canonical coefficients; weighted-square/finite-tail/finite-prime-orbit sources fail the complete source and/or reflection and their local events do not supply an all-real time; reflected/smooth/primitive controls fail theta square-series arithmetic; the RH-conditional endpoint retains its conditional premise and fails ordinary Dirichlet arithmetic; variable-readout/counter-kernel families alter the cosine readout, source or physical generator; relaxed zero/profile populations do not identify the exact full canonical field. No premise failure is converted into a universal no-go statement.

R2–R6 retain **proved in-note from named inherited approximation inputs; same-assistant checking only**. R7–R9 retain **proved in-note from named classical and inherited approximation inputs; same-assistant checking only**. This discussion is not an independent proof audit. Fresh targeted primary inspection checked [Polymath v2](https://arxiv.org/html/1904.12438v2), introduction (1)–(4) and Theorem 1.5(i)–(ii), for the normalization, threshold framework and time-dependent exterior scale; existing reference ownership and reading copies remain in [the catalog](../../references/README.md).

The session's public chat is registered in [chat-histories](../../chat-histories/README.md). [Its registry](../../chat-histories/index.json) owns current capture metadata. Final-reply capture must be verified after the real reply completes; queueing its bounded worker alone is not evidence of that final capture.
