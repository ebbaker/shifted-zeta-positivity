# Small-time canonical seeds and a uniform Dobner witness envelope

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.

**Status: proved in-note using the published canonical approximation
input in [Note02][budget], with separate same-model internal review.**
This acquires the seed location, a positive count and a contour-floor
envelope for every 0<tau<=1, and closes the analytical small-time transport
budget. No RH hypothesis or unproved seed assumption is used. The
published approximation constants K_1 and y_0(1) remain uninstantiated:
the result is a uniform upper envelope, not a numerical witness-height
certificate or an identification of the first nonreal zero.

This chat follows the user's Dobner-only continuation. The response and
growing-window branch is left for a separate chat. See the
[sole progress register][progress] and [Review02][review]. Read the
[result index][results], [avoid index][avoid], [classification rule][classify],
[control cluster][controls], [scope rule][scope], [known-result warning][known]
and [quantitative-gain rule][gain]. The baseline is Note02's budget with
unacquired seed data; negative-time nonreal-zero existence itself is
already known and is not counted again. No literature priority is claimed.

**27 October continuation:** [Note05](05_NARROW_SMALL_TIME_DOBNER_SEEDS_20261027.md)
acquires a narrower actual seed family and improves the final upper-envelope
exponent from tau^{-3} to tau^{-1/2}. This note's proof and inequalities
remain valid as a baseline. The [chat0001 summary](06_CHAT0001_RESEARCH_SUMMARY_20261027.md)
records the current best bound and limits. Prepared with substantial LLM
assistance, **gpt-6.1-sol, actual recorded effort ultra**.

## 1. Main result and complete explicit seed data

Use the unchanged canonical series

\[
 Z_\tau(w)=\sum_{n\ge1}e^{-\tau\log^2 n/4}n^{-w},\qquad 0<\tau\le1.
\]

Put

\[
 A=2^{17},\quad R=A/\tau,\quad M=\log2+64R^2/\tau,
 \quad N_0=\left\lceil M/\log(8/5)\right\rceil,
\]
\[
 r_j=2R+\frac{jR}{N_0}\quad(0\le j\le N_0),\qquad
 \delta=\exp\{-6M-N_0\log(16e)\}.
 \tag{S1}
\]

**Seed theorem.** At least one disk |w-8|<=r_j has a zero-free boundary
with min |Z_tau|>=delta. It contains between 1 and N_0 zeros, counted
with multiplicity. The family's simultaneous coordinate envelope is

\[
 \alpha=8-3R\le\Re w\le8+3R=:\beta,\qquad |\Im w|\le3R.
 \tag{S2}
\]

This is an analytically guaranteed good member of a specified finite
family. No index j or exact integer count has been computed. The positive
lower count and finite upper count are proved, which is enough for
existence transport. It is not a machine-selected contour certificate.
All subsequent bounds use S2, so they do not require knowing that index.

**Witness consequence.** For each fixed d>0 there is a constant C_d,
depending only on d and the fixed published K_1,y_0(1), such that for
every 0<tau<=1 the canonical H(-tau,.) has a zero z_tau with

\[
 |\Im z_\tau|\ge2d,\qquad
 R_*(\tau)\le |z_\tau|
 \le\exp\exp\{C_d\tau^{-3}\}.
 \tag{S3}
\]

The complete unsimplified bound F_tau is given in S15 below. S3 is a
sufficient upper envelope; it is not an optimal rate, lower exclusion
height, monotonicity theorem or new regime exclusion. Its gain over the
opening record is a uniform source-derived time dependence with no
unproved seed or recurrence input.

## 2. Growth and a quantitative zero-existence disk

Completing the square term by term gives, for real x,

\[
 Z_\tau(x)=\sum_{n\ge1}n^{-2}
   e^{-\tau\log^2n/4+(2-x)\log n}
 <2\exp\{((2-x)_+)^2/\tau\}.
 \tag{S4}
\]

The series and its derivatives converge normally on compact sets.
At w=8 use the probability weights proportional to
e^{-tau log^2 n/4}n^{-8}, and write mu_l for the moments of log n.
The elementary inequalities 1/2<log2<1, log n<=n and Z_tau(8)<2 give

\[
 \mu_1\le\sum_{n\ge2}n^{-7}\le\frac1{96},\quad
 \mu_2\le\frac{\mu_3}{\log2},\quad
 \mu_3>\frac{(3/4)2^{-8}(1/2)^3}{2}=\frac3{16384}.
 \tag{S5}
\]

Here the n=2 damping exceeds 3/4 for tau<=1, by e^{-v}>=1-v and
tau log^2 2/4<1/4. Thus the third logarithmic derivative satisfies

\[
 |(\log Z_\tau)'''(8)|
 =\mu_3-3\mu_2\mu_1+2\mu_1^3
 >\frac{45}{262144}>2^{-13}.
 \tag{S6}
\]

If Z_tau were zero-free in |w-8|<R, choose its analytic logarithm ell
there. By S4 its real part is bounded by M_R=log2+R^2/tau, while
ell(8)=log Z_tau(8)>=0. The positive harmonic function
M_R-Re ell has mean M_R-ell(8) on centered circles. Its third Fourier
coefficient gives the elementary Caratheodory estimate

\[
 |\ell'''(8)|\le12(M_R-\ell(8))/R^3\le12M_R/R^3.
 \tag{S7}
\]

One may first use a smaller circle and take its radius up to R; no
zero-free boundary at radius R is assumed. For R=A/tau the last side
is <=13/A<2^{-13}. This contradicts S6, proving a zero strictly inside R.
The coefficient argument proves the inequality used here, rather than
importing a qualitative factorization result with an unspecified radius.

## 3. Count, a finite circle family, and its complete floor

Set f(z)=Z_tau(8+z). Equation S4 gives log |f|<=M on |z|<=8R.
Since f(0)>=1, Jensen's formula implies that at most N_0 zeros lie
within |z|<=5R: each contributes at least log(8/5). Taking outer
circle radii up to 8R through zero-free radii handles any boundary zeros.

Choose L_out in [4R,5R] meeting no zero modulus. For all m<=N_0 zeros
a_l inside it, form the finite disk Blaschke product

\[
 B(z)=\prod_{\ell=1}^{m}
       \frac{L_{\rm out}(z-a_\ell)}{L_{\rm out}^2-\bar a_\ell z}.
\]

Then g=f/B is analytic and zero-free on the closed outer disk. On its
boundary |B|=1, so the maximum principle gives |g|<=e^M. Moreover
log |g(0)|>=0 because |B(0)|<=1. Harnack's inequality for
M-log |g|, or directly the positive Poisson kernel, gives on |z|<=3R

\[
 \log|g(z)|\ge M-7(M-\log|g(0)|)\ge-6M.
 \tag{S8}
\]

The factor 7 pays (L_out+3R)/(L_out-3R) with L_out>=4R.
For u in [2,3], put v_l=|a_l|/R and define the auxiliary monic
polynomial p(u)=product_l(u-v_l). On every circle |z|=Ru,

\[
 \left|\frac{L_{\rm out}(z-a_\ell)}
                   {L_{\rm out}^2-\bar a_\ell z}\right|
 \ge\frac{|z-a_\ell|}{L_{\rm out}+|z|}
 \ge\frac{|u-v_\ell|}{8}.
 \tag{S9}
\]

To find a completely paid radius in the finite grid, augment p to the
monic degree N_0 polynomial p_tilde(u)=p(u)(u-2)^{N_0-m}. On [2,3]
one has |p_tilde|<=|p|. Its N_0-th forward difference with step 1/N_0
is exactly N_0!/N_0^{N_0}. The sum of the absolute binomial weights is
2^{N_0}, so some u_j=2+j/N_0 satisfies

\[
 |\widetilde p(u_j)|\ge
   \frac{N_0!}{2^{N_0}N_0^{N_0}}\ge(2e)^{-N_0}.
 \tag{S9a}
\]

The factorial inequality follows by integrating log x from1 to N_0.
Thus |B(z)|>=8^{-m}|p(u_j)|>=(16e)^{-N_0} on the complete circle,
and S8 supplies delta in S1. This use of an auxiliary polynomial is
only a finite-difference bound; it makes no change to f or its zeros.
Every candidate radius is at least 2R and hence contains the zero
proved inside R. The count is positive and at most N_0. This proves
the seed theorem for the full series without a numerical wall sample.

## 4. Infinite-tail, prime-phase and recurrence payments

All quantities in this section are explicit upper envelopes. Put

\[
 W=2\exp\{((2-\alpha)_+)^2/\tau\},\qquad E=-\log\delta,
\]
\[
 D=1+\frac{8(2-\alpha)_+}{\tau}
        +\sqrt{\frac{8\log(12/\delta)}{\tau}},
 \quad Q=\lceil e^D\rceil,\quad
 \overline S=\frac{\log Q}{\log2}W,\quad
 \vartheta=\min(1,\delta/(6\overline S)).
 \tag{S10}
\]

Here Q is an integer coefficient cutoff, distinct from the zero-count
bound N_0. For log n>log Q, completing a partial square gives

\[
 e^{-\tau\log^2n/4}n^{-\alpha}
 \le n^{-2}e^{-\tau\log^2n/8},\quad
 T_Q< e^{-\tau\log^2Q/8}<\delta/12.
 \tag{S11}
\]

The first inequality uses log Q>8(2-alpha)_+/tau. Summing n^{-2}
over n>Q costs at most 1/Q<1. Also the finite prime-factor weighted
sum is <=overline S. As in Note02 B6, prime phase distances below
vartheta therefore imply |Z_tau(w+ih)-Z_tau(w)|<delta/3 throughout
Re w>=alpha.

Let p_1,...,p_m be the primes <=Q, P=product p_l and
A_k=binom(2k,k)/4^k. A closed degree choice paying B8 is

\[
 T=64(m+1)/\vartheta^2,\quad k=\lceil T\log T\rceil,
 \qquad L_{\rm rec}=8P^k/A_k^m.
 \tag{S12}
\]

Indeed T>=128, k<=2T log T and 2k+1<=5T log T<=T^2. Thus
k vartheta^2/4>=16(m+1)log T>=m log(2k+1)+log2.
Together with A_k>=1/(2k+1) and
cos(vartheta/2)^{2k}<=exp(-k vartheta^2/4), this proves B8.
The positive-Fourier-coefficient proof in Note02 B9 then provides a
good shift in every interval of length L_rec. It uses the lower bound
|log(A_1/B_1)|>=P^{-k} for its nonzero rational frequencies.

## 5. Approximation, map and actual canonical radius bound

Use the fixed C=1 version of Dobner's approximation from Note02.
Its constants K_1 and y_0(1) depend on the completed canonical function,
not on tau. Set B_*=8+3R, retain a fixed d>0, and choose

\[
 Y=1+\max\left\{2\pi,y_0(1),B_*^4,\tau/2,
 (6K_1W/\delta)^5,
 [20\tau\log_+(6K_1/\delta)]^{3/2},
 2\pi e^{4(1/2+d-\alpha)/\tau}\right\},
\]
\[
 U=Y+6R+L_{\rm rec}.
 \tag{S13}
\]

Choose one good seed circle and a good shift in
[Y+3R,Y+3R+L_rec]. The entire translated disk lies at heights [Y,U]
and |Re w|<=B_*. The two approximation terms sum to less than delta/3,
and translation costs less than delta/3. Rouche transfers the positive
seed count to xi_{-tau}(J(w))/gamma_{-tau}(w). Its gamma factor is
nonzero on this high disk. The map J(w)=w+(tau/4)Log(w/(2pi)) is
injective there, since |J'-1|<=1/2 on the convex upper region. Thus an
actual completed-function zero maps to a canonical zero via

\[
 z=-i(2J(w)-1),\quad
 \Re z=2\Im w+\frac\tau2\operatorname{Arg}w,\quad
 \Im z=1-2\Re w-\frac\tau2\log(|w|/(2\pi))\le-2d.
 \tag{S14}
\]

In particular the entirely paid unsimplified envelope is

\[
 R_*(\tau)\le F_\tau:=( (2U+\tau\pi/2)^2+
  [1+2B_*+(\tau/2)\log(\sqrt{B_*^2+U^2}/(2\pi))]^2 )^{1/2}.
 \tag{S15}
\]

Its uninstantiated constants are precisely the imported K_1,y_0(1).
The seed, tail, recurrence and coordinate costs have been supplied.
This constructs an upper witness bound; it does not exclude lower zeros.

## 6. Simplifying the complete cost and comparing regimes

Let V_tau=tau^{-3}. All constants below are independent of
0<tau<=1. From S1, M, N_0 and E are O(V_tau).
Equations S10-S12 imply

\[
 \log W=O(V_\tau),\quad \log Q=O(V_\tau),\quad
 \log(1/\vartheta)=O(V_\tau),\quad
 \log k=O(V_\tau),\quad
 \log P\le Q\log Q\le e^{O(V_\tau)}.
\]

Since log(1/A_k)<=log(2k+1), it follows that
log L_rec<=exp(O(V_tau)). In contrast log Y=O_d(V_tau), including
the map and the fixed imported onsets. Thus U and F_tau are bounded by
exp exp(C_d V_tau), proving S3. The double exponential comes from the
fully paid recurrence bound in this construction; it is not a lower
bound on true recurrence or zero height. A better field error alone
would not remove that supplied worst-case recurrence payment.

Under regime C, the inherited compact-stability argument gives
R_*(tau)->infinity, now with the upper envelope S3. Under A or B, an
off-axis time-zero zero or a multiple endpoint supplies a compact witness
and hence R_*=O(1) near zero. S3 also holds there; it cannot distinguish
the regimes or prove a lower escape rate. The mapped witness may leave
every fixed transverse strip. No fixed-strip Book comparison, original
physical-regulator estimate, derivative tuple or covariance closure is
deduced from S15.

## 7. Control screen, limits and bounded next task

The acquired coefficient/growth/cumulant estimates serve a negative-time
existence upper bound, so colliding controls are allowed rather than
contradicted. The analytical screen reuses the [recorded controls][controls]:

| Control family | Actual premise and disposition |
| --- | --- |
| Hermite/quadratic, positive atomic and reflected/shape/primitive sources | Do not supply this canonical ordinary series; the local heat laws alone cannot supply S4-S6. Their negative-time zeros are compatible with the conclusion. |
| Theta-close endpoint, finite-prime and finite-profile controls | Fail unchanged full ordinary coefficients; selected local data do not prove S4-S6 for their whole function. Passing analogous bounds would still be compatible with multiple endpoints. |
| Euler-factor controls | Have changed coefficients/completion. Some qualifying positive-coefficient series can satisfy analogous growth/cumulant bounds and negative-time transport despite positive thresholds; the proof makes no contrary claim. |
| Weighted-square and finite-tail controls | Lack the global all-real interval for an RH population interpretation and do not supply B1's ordinary series. This proof uses no such population interpretation. |
| All-multiple coarse-count control | May pass coarse response/wall bounds and retain every multiplicity; those bounds are not an exclusion premise of this construction. |

Only the new quantitative seed/transport range is counted as progress.
No favorable simplicity inequality, numerical certification, Newman upper
bound, source change, manuscript snapshot or Git commit is asserted.

**Next bounded task:** improve the actual small-time seed family before
spending effort on the field error. Compare the S1 radius/floor and S12
recurrence with a source-derived seed in a narrower strip, paying its
complete positive count and floor. Alternatively instantiate K_1,y_0(1)
to make S15 a numerical bound on a declared finite interval. Do not launch
a survey without a finite protocol. [Note04][lattice] records a separate
direct seed lattice for tau>=32 where recurrence can be removed entirely;
its two-term argument does not extend to tau->0.

[budget]: 02_DOBNER_COMPLETE_CONDITIONAL_BUDGET_20261026.md
[lattice]: 04_DIRECT_DOBNER_SEED_LATTICE_20261026.md
[progress]: ../research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md
[review]: ../reviews/02_DOBNER_CANONICAL_SEED_ACQUISITION_REVIEW_20261026.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[classify]: ../../../../avoid/01_restating_the_target.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[known]: ../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[gain]: ../../../../avoid/20_volume_without_a_gain.md
