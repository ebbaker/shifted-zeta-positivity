# Dobner transport with an explicit conditional witness-height budget

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6.1-sol (Codex), actual recorded effort ultra**.

**Opening status:** this note proves transport from declared seed data
and the imported approximation estimate, with explicit finite-prime
recurrence. The subsequent [small-time seed acquisition](03_SMALL_TIME_CANONICAL_SEEDS_AND_WITNESS_ENVELOPE_20261026.md)
now supplies the analytical seed data uniformly for0<tau<=1 and a
source-derived upper envelope. The [direct lattice](04_DIRECT_DOBNER_SEED_LATTICE_20261026.md)
also removes recurrence for32<=tau<=C. These continuations supersede the
opening unacquired-seed status on their respective domains. The imported
approximation constants remain uninstantiated; no numerical first-zero
location or Newman upper-bound improvement is supplied. TRD-03 remains
Partial in the [sole register][progress] for usable constants and sharper
costs, with the intermediate1<tau<32 domain still seed-parameterized here.

The [versioned source record][source] defines the imported inputs. We
rechecked [Dobner Theorem4, equations(11)-(13), Section3.1 and(35)][dobner]
on 26 October 2026. These selected passages are not a full proof audit.
Everything labeled B below is a deduction here, not a further claim of
Dobner's paper. Read the [result index][results], [avoid index][avoid],
[classification rule][classify], [control screen][controls],
[scope rule][scope] and [coupled-accounting rule][coupled]. Review is
[same-model internal review][review].

**27 October update:** the [narrow-seed continuation](05_NARROW_SMALL_TIME_DOBNER_SEEDS_20261027.md)
supplies the improved exp exp(C_d/sqrt(tau)) upper envelope with all
seed/tail/recurrence costs paid. The [chat0001 summary](06_CHAT0001_RESEARCH_SUMMARY_20261027.md)
consolidates this chat's results. The published approximation constants
remain uninstantiated. Prepared for Edward Baker with substantial LLM
assistance, **gpt-6.1-sol, actual effort ultra**.

## 1. Seed and field data

Fix 0<tau<=C and the entire absolutely convergent series

\[
 Z_\tau(w)=\sum_{n\ge1}e^{-\tau\log^2n/4}n^{-w},\qquad
 J(w)=w+\frac\tau4\operatorname{Log}(w/(2\pi)).
 \tag{B1}
\]

Let D be a closed disk with a zero-free boundary, containing at least
one zero of Z_tau, counted by a complete argument-principle count or an
analytical proof. Write alpha=min_D Re w, beta=max_D Re w,
v_-=min_D Im w, v_+=max_D Im w, V=v_+-v_- and
B=max(|alpha|,|beta|). Supply the actual contour floor
delta=min_boundaryD |Z_tau|>0. Neither a plotted minimum nor one sampled
root supplies these data.

Use Dobner's sharper estimate in canonical normalization:

\[
 \frac{\xi_{-\tau}(J(w))}{\gamma_{-\tau}(w)}
   =Z_\tau(w)+E_\tau(w),\quad
 |E_\tau(w)|\le K_C\{y^{-1/5}Z_\tau(x)
                  +e^{-y^{2/3}/(20\tau)}\},
 \tag{B2}
\]

on y>=y_0(C), |x|<=C y^{1/4}. The nonvanishing gamma factor is the
one in the [source record][source]. On an entire disk translated above
y=Y, the field allowance is strictly less than delta/3 if Y strictly
exceeds

\[
 Y_{\rm app}=\max\left\{
   (6K_C Z_\tau(\alpha)/\delta)^5,
   [20\tau\log_+(6K_C/\delta)]^{3/2}\right\}.
 \tag{B3}
\]

Here log_+(s)=max(0,log s); add a positive slack to strict gates.
Monotonicity Z_tau(x)<=Z_tau(alpha) pays the whole contour. B3 retains
the full positive series in place of the coarser exponential majorant.

For a declared off-axis margin d>0 choose Y>2pi and

\[
 Y\ge2\pi\exp\left[\frac4\tau(\tfrac12+d-\alpha)\right].
 \tag{B4}
\]

Since Re J(w)=x+(tau/4)log(|w|/(2pi)), B4 maps the entire disk into
Re s>=1/2+d. Also require Y>=y_0(C), Y>=(B/C)^4, Y>=tau/2 and Y>=1.
All these restrictions, together with B3, belong to the starting height.
The harmless Y>=tau/2 gives |J'-1|<=1/2; it also makes J injective on
the convex translated disk by integrating J'-1 along a segment.
Existence of a zero needs no inverse-map derivative estimate.

## 2. A finite coefficient budget for translation

Let a_n=exp(-tau log^2 n/4). Choose an integer N>=2 with

\[
 T_N:=\sum_{n>N}a_n n^{-\alpha}<\delta/12,
 \qquad S_N:=\sum_{2\le n\le N}a_n n^{-\alpha}\Omega(n)>0,
 \quad \vartheta=\min(1,\delta/(6S_N)).
 \tag{B5}
\]

Omega(n) is the number of prime factors with repetitions. If every
p<=N obeys dist(h log p,2pi Z)<vartheta, telescoping its prime factors
gives |exp(-ih log n)-1|<=Omega(n) vartheta. Hence uniformly on D,

\[
 |Z_\tau(w+ih)-Z_\tau(w)|
 \le \vartheta S_N+2T_N<\delta/3.
 \tag{B6}
\]

The same N pays the infinite tail; no unbounded list of prime phases
has been silently constrained. One may overestimate Omega(n) by
log n/log2 when selecting vartheta.

For an explicit analytical tail choice, impose
log N>max(0,-2alpha/tau) so the summand is decreasing beyond N. Then

\[
 T_N\le\int_{\log N}^{\infty}
          e^{-\tau v^2/4+(1-\alpha)v}\,dv
 =\frac{\sqrt\pi}{\sqrt\tau}e^{(1-\alpha)^2/\tau}
   \operatorname{erfc}\left(\frac{\sqrt\tau}2\log N
                       -\frac{1-\alpha}{\sqrt\tau}\right).
 \tag{B7}
\]

The bound tends to zero for each fixed tau. Its explicit time dependence
is retained; N is not claimed uniform as tau decreases.

## 3. Explicit relative density of the required prime phases

Let p_1,...,p_m be the primes <=N, P=product p_j, and
A_k=binom(2k,k)/4^k. Choose an integer k>=1 such that

\[
  \cos^{2k}(\vartheta/2)\le A_k^m/2.
 \tag{B8}
\]

Such k exists: the left side decays exponentially whereas
A_k>=1/(2k+1), by the largest-binomial-coefficient bound. It can be
chosen by finite search or by the sufficient explicit inequality
k vartheta^2/4 >= m log(2k+1)+log2, using
cos(vartheta/2)^{2k}<=exp(-k vartheta^2/4).

**Recurrence lemma.** Every real interval of length

\[
 L_{\rm rec}=8P^k/A_k^m
 \tag{B9}
\]

contains h with all the prime-phase distances strictly below vartheta.

Proof: F(h)=product_j cos^{2k}(h log p_j/2) is a finite exponential
polynomial. Its Fourier coefficients are nonnegative and sum to one.
Unique factorization makes its zero-frequency coefficient exactly A_k^m.
Every other frequency is log(A_1/B_1) for distinct positive integers
A_1,B_1<=P^k, so
|log(A_1/B_1)|>=|A_1-B_1|/max(A_1,B_1)>=P^{-k}. On any interval of length L,
the average of each nonconstant exponential has modulus <=2P^k/L.
Thus average F>=A_k^m-2P^k/L. With L=L_rec this is >=3A_k^m/4.
If any prime phase has distance >=vartheta from 2pi Z, its factor is
at most cos^{2k}(vartheta/2), and every other factor is <=1. Were there
no good h in the interval, average F would therefore be <=A_k^m/2,
a contradiction. The bound is elementary and deliberately conservative;
it is not a measured or optimal recurrence length.

This addresses a genuine missing upper-height cost in the opening
budget: a homogeneous Dirichlet simultaneous-approximation bound alone
would give one near return and would not justify a return above an
arbitrarily prescribed starting height with that same upper bound.

## 4. Complete constructed witness bound in z coordinates

Take h in [Y-v_-,Y-v_-+L_rec] using B9 and put
U=Y+L_rec+V. Every point of D+ih then has imaginary part in [Y,U].
On its boundary B6 and B2 together differ from the translated seed by
less than 2delta/3. Rouche gives the same positive zero count for
xi_{-tau}(J(w))/gamma_{-tau}(w). The gamma factor is holomorphic and
nonzero on the high disk; hence there is an actual xi_{-tau} zero in
J(D+ih).

Rotate only after applying J. The canonical zero is

\[
 z=-i(2J(w)-1),\quad
 \Re z=2y+\frac\tau2\operatorname{Arg}w,\quad
 \Im z=1-2x-\frac\tau2\log(|w|/(2\pi)).
 \tag{B10}
\]

It satisfies Im z<=-2d and

\[
 2Y\le\Re z\le2U+\tau\pi/2,
 \quad |\Im z|\le W_\perp
 :=1+2B+\frac\tau2\log\frac{\sqrt{B^2+U^2}}{2\pi}.
 \tag{B11}
\]

In particular, with R_* defined by complex radius as in the overview,

\[
 R_*(\tau)\le
  \sqrt{(2U+\tau\pi/2)^2+W_\perp^2}.
 \tag{B12}
\]

Every input is displayed: seed count/location/floor, finite-tail cutoff,
prime tolerance, recurrence length, approximation constants and map
displacement. These data may depend badly on tau. The theorem gives an
upper bound for one constructed witness. It gives no lower bound
excluding closer zeros and no asymptotic or identification of the first
witness. Derivative estimates for further physical consumers would need
their own buffered contour margins; none are needed to infer existence.

## 5. Comparison with the Book: pay the actual overlap

Let X=Re z, L=log(X/(4pi)), and keep both tau L and tau L^2. In the
upper half-plane the image transverse coordinate is exactly B10. For
fixed tau>0 and bounded seed x it tends to minus infinity as y grows.
Therefore arbitrarily large translated seed disks do not remain inside
any one fixed transverse strip of the [Book canonical atlas][book].
The large recurrence allowance in B9 can push the guaranteed witness
beyond a candidate fixed-strip overlap.

An actual comparison must first check |Im z|<=B_0 on the complete
mapped contour, the Book's time/height gates and analytic buffers, and
the conversion between |gamma_{-tau}|/8 and its outer field envelope.
Equality of leading carriers or a field estimate on another strip does
not pay that conversion. For the joint band |t|L<=8 the Book supplies
X^{-3/4}exp(tau L^2/16) in its outer norm. This is <=X^{-1/4} there.
B2 has the different explicit allowance y^{-1/5}Z_tau(alpha), with
Z_tau(alpha)>=1. Thus the published D2 allowance by itself is no
automatic improvement over that Book allowance, even before a rigorously
paid envelope conversion. No replacement of the Book estimate is
claimed. Its negative hierarchy likewise keeps its own lower-time gate
and transverse domains.

The gain here is an explicit conditional zero-transport budget. Improving
the field error alone may leave U essentially unchanged if the seed
floor or recurrence dominates. Compare max(Y_app,Y_map,Y_domain) and
the added L_rec with the same seed data before claiming a height gain.

## 6. Classification, controls and the next bounded question

This is a quantitative existence construction shared by all three
canonical hypotheses. It does not discriminate among them. The
nonnegativity theorem is an inherited input, not counted again.

The heat-polynomial controls lack B1's completed Dirichlet-series
representation. Positive atomic, reflected, shape/primitive and
theta-close multiple-endpoint controls do not supply the unchanged
ordinary theta coefficients; the exact preservation lists remain those
in [the control cluster][controls]. Euler-factor examples require their
own coefficients and completion in B1/B2, rather than this zeta-specific
formula; qualifying extended-Selberg examples can still admit analogous
negative-time transport and positive thresholds. Weighted-square and
finite-tail controls lack the all-real heat interval needed for an RH
population interpretation. Finite-prime/profile controls preserve only
their selected data, not B1's full fixed source. The all-multiple
coarse-count control passes coarse response/count information and is
not excluded by this existence argument. Missing exact theta arithmetic
is not an already proved favorable inequality in any case.

For A at positive T, the actual base source is e^{Tu^2}Phi. Formally
replacing the damping in B1 by e^{+T log^2 n/4} makes its terms fail to
tend to zero in every fixed right half-plane. This screens that direct
ordinary-series time shift only. It does not rule out a different
functional approximation to the shifted canonical source.

**Next bounded task:** obtain a certified or analytical seed disk with a
quantitative count/floor/location for a declared negative-time family,
then compare its B3/B5/B9 payments before making a small-time law. State
the interval, success quantity and resource cap before numerical work.
No research numerics, new PDF acquisition or numerical constant
evaluation was performed for this note.

[progress]: ../research-progress/01_THREE_REGIME_DYNAMICS_RESEARCH_PROGRESS_20261026.md
[source]: ../references/01_DOBNER_FUNCTIONAL_APPROXIMATION_20261026.md
[dobner]: https://arxiv.org/html/2005.05142v2
[book]: ../../01_heat_density_asymptotics/book/sections/01_canonical.tex
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[classify]: ../../../../avoid/01_restating_the_target.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[scope]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[coupled]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[review]: ../reviews/01_OPENING_RESPONSE_AND_BUDGET_REVIEW_20261026.md
