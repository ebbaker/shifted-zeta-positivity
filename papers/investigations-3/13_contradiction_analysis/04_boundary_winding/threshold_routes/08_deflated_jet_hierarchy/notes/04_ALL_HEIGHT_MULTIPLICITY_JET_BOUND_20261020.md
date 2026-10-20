# BW-08: an all-height deflated bound at every finite multiplicity

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Model **gpt-6-astra (Codex)**; actual effort
**ultra**, verified from the parent turn metadata.

**Status: restricted analytic result, proved in-note; [separate same-model
internal review][review], with no specialist review.** For every hypothetical all-real theta slice at
T>=0 with an exact m-fold zero a>0, m>=2, define h_j=∂_x^jH(T,a),

\[
S_m=\frac{h_{m+1}^2}{(m+1)^2h_m^2}
       -\frac{2h_{m+2}}{(m+1)(m+2)h_m},\qquad b=\max\{a,20m\}.
\]

Then the following explicit bound strengthens the mirror-only bound at
**every positive height and every finite multiplicity**:

\[
\boxed{S_m>L_m(a):=\frac{m}{4a^2}
 +\frac1{4b}\log\frac{b+1}{4\pi}
 -\frac{2m}{a^2+b^2}
 >\frac{m}{4a^2}+\frac1{40b}.}                         \tag{1}
\]

For m=2 this feeds the original physical critical-value pair of BW-01,
with the finite-time payment already proved in [Note 03][old]. For m>2
it gives a restriction on the unchanged H's jets, and feeds a
differentiated-field pair in [BW-07][reduction]. The latter pair is not
the physical jet (H,H_x). No multiple event is excluded. This is a
quantitative necessary-condition milestone, not an RH criterion,
new theta region, improved Newman bound, or speed claim.

The classification and screening follow [result summaries][results],
[local laws][laws], [collision controls][controls], and [patterns to
avoid][avoid], especially [restatements][a01], [control premises][a02]
and [scoped conclusions][a07]. The all-multiplicity index is inherited;
it is not proved anew here. No literature priority is claimed.

## 1. Contract and exact comparison

Use the complete positive theta source, physical time and normalization
in [BW-01 Contract 02][source]. The event height and time are unknown
parameters. No finite set of modes is assigned the event cancellations.
Only the all-real slice is needed; minimality of T as a threshold is not
used. Order one, evenness and H(T,0)>0 give the paired canonical product
used in Note 03. These classical inputs and the source normalization are
also stated in [Polymath, sections 1 and 3][polymath].

Deflate all m factors at +a, setting g(z)=H(T,z)/(z-a)^m. Direct Taylor
division gives

\[
-(\log|g|)''(a)=S_m
 =\frac{m}{4a^2}
  +\sum_{\rho>0,\rho\ne a}m_\rho
     \left(\frac1{(a-\rho)^2}+\frac1{(a+\rho)^2}\right).       \tag{2}
\]

The mirror contribution is m/(4a²), not m/(2a²). For any b>=a,

\[
\frac1{(a-\rho)^2}+\frac1{(a+\rho)^2}
 \ge\frac2{a^2+\rho^2}\ge\frac2{b^2+\rho^2}.
\]

Write D_T(b)=∂_b log H(T,ib). Its product sum is
D_T(b)/b=Σ_{ρ>0}2m_ρ/(ρ²+b²). Removing precisely the m roots at
the positive representative a from this sum proves

\[
S_m\ge\frac{m}{4a^2}+\frac{D_T(b)}b-\frac{2m}{a^2+b^2}.
                                                               \tag{3}
\]

All summands converge and are nonnegative; no conditional subtraction
of divergent sums occurs. For (z²-a²)^m, (3) is an equality for every
b>=a. Extra real root pairs make the first comparison strict.

Note 03 proves, from the full source and the time-zero xi identity,

\[
D_T(b)>\tfrac14\log((b+1)/(4\pi))\quad(T\ge0,\ b\ge5).       \tag{4}
\]

Its proof retains the complete Euler-series tail, uses positivity to
show ∂_TD_T(b)>=0, and uses the [DLMF digamma integral][digamma]. It is
reused, not recomputed from an incomplete theta sum. Unlike the earlier
choice b=a, choosing b=max(a,20m) makes (4) useful at every a>0.

To check the final strict inequality in (1), b>=20m>=40. Already for
b>=20, π<22/7 and log x>=2(x-1)/(x+1) imply

\[
\log((b+1)/(4\pi))>118/235>1/2.
\]

Also 2m/(a²+b²)<=2m/b²<=1/(10b). The increment in (1) is therefore
greater than 1/(8b)-1/(10b)=1/(40b). This is a uniform formula in
a and m, not a uniform event radius or a bounded multiplicity theorem.

At b=a with a>=5, (3)-(4) instead read
S_m>log((a+1)/(4π))/(4a)-3m/(4a²), improving the mirror when
a log((a+1)/(4π))>4m. Equation (1) avoids that height restriction.
It is an explicit admissible choice, not a claim of optimizing b.

## 2. Named consumers and complete error payment

For these finite-time consumers assume T>0, so their rectangles may be
chosen with δ<T. The necessary bound (1) itself also holds at T=0.

For m=2 set C=6L_2(a), or use the stronger
C=(h_3/h_2)²/3+6L_2(a). With the rectangle, critical curve and K of
Note 03, replace its old coefficient ℓ(a) by L_2(a). All its derivative
orders and geometry remain unchanged. In particular

\[
0<s\le\min\{\delta,3C/(2K)\}
 \implies \frac{H(T+s,c(T+s))+H(T-s,c(T-s))}{h_2}
 \le-\frac C2s^2<0.                                         \tag{5}
\]

The K=0 cap is omitted. The full physical first-jet winding is still -1
near the assumed double event. A more negative pair is not zero winding.

For general m let G=∂_x^{m-2}H. Its normalized critical-value curve has

\[
v_G''(T)=\frac{h_{m+2}}{h_m}
             -\left(\frac{h_{m+1}}{h_m}\right)^2
 =-\frac{m}{2(m+1)}\left(\frac{h_{m+1}}{h_m}\right)^2
  -\frac{(m+1)(m+2)}2S_m.                                   \tag{6}
\]

Thus C_m=(m+1)(m+2)L_m(a)/2 is a positive lower curvature
coefficient. The proof of (5) applies to G with bounds B_{m+1},...,B_{m+4},
normalizer h_m, and b_m=|h_m|/2. Explicitly require

\[
B_{m+1}\rho+B_{m+2}\delta\le |h_m|/2,\quad
B_{m+1}\delta<b_m\rho,
\]
\[
K_m=\frac1{|h_m|}\left(B_{m+4}
 +\frac{3B_{m+1}B_{m+3}}{b_m}
 +\frac{3B_{m+1}^2B_{m+2}}{b_m^2}
 +\frac{B_{m+1}^4}{b_m^3}\right).
\]

There is an event-dependent positive δ<T,ρ<a satisfying these
conditions. The resulting G-pair is at most -C_m s²/2 for
0<s<=min(δ,3C_m/(2K_m)). This uses **m+4** spatial derivatives;
the old order-six allowance cannot be reused when m>2. The [BW-07
audit][reduction] explains which source and threshold facts G preserves.
It supplies no rule identifying G's winding with H's winding.

For any finite B=T+δ, the exact complete moments
M_j(B)=∫₀∞e^{Bu²}Φ(u)u^jdu bound these derivatives and are finite.
This analytic proof has no numerical truncation, quadrature, cutoff or
parameter error. A numerical realization must acquire these moments and
jets with its own exhaustive errors. No such acquisition is reported.

For clarity, if a complete jet enclosure gives |h_j-f_j|<=e_j for
j=m,m+1,m+2, and a certified fixed rational L<=L_m(a), L>0, then

\[
Q_L=(m+2)h_{m+1}^2-2(m+1)h_mh_{m+2}
       -(m+1)^2(m+2)Lh_m^2>0,                               \tag{7}
\]

and the complete elementary product allowance for |Q_L-Qhat_L| is

\[
\begin{aligned}
E={}&(m+2)(2|f_{m+1}|e_{m+1}+e_{m+1}^2)\\
 &+2(m+1)(|f_m|e_{m+2}+|f_{m+2}|e_m+e_me_{m+2})\\
 &+(m+1)^2(m+2)|L|(2|f_m|e_m+e_m^2).
\end{aligned}
\]

An opposing upper enclosure Qhat_L+E<=0 would exclude that event.
It has not been obtained. This interface is not evidence for its sign.
Event uncertainties add M_{j+2}(B)ΔT+M_{j+1}(B)Δa to e_j.
For a∈[a_-,a_+], a_->0, choose a fixed b>=max(a_+,20m); a safe L is
m/(4a_+²)+log((b+1)/(4π))/(4b)-2m/(a_-²+b²), rounded downward.
If it is not positive, subdivide or decline this positive-C consumer.

## 3. Controls, coefficient checks and scope

The [exact checker][checker] differentiates finite polynomial coefficients
and independently computes the root sums. It checks multiplicities
2,3,4,6, negative normalization, b=a and b>a, the subtracted m-root
term, and (6) via the finite heat series. These checks audit formulas;
the all-m proof is (2)-(6), not the list of examples. Outward rational
enclosures use the Machin/logarithm routines of Note 03. The [receipt][record]
contains coefficient values at hypothetical parameters and source hashes.
It reports no acquired theta jet or event.

| Hypothetical (a,m) | Mirror bound | Outward interval for L_m(a) |
| --- | --- | --- |
| (1,2) | 0.5 | [0.504892485397391, 0.504892485397392] |
| (20,2) | 0.00125 | [0.006640923873343, 0.006640923873344] |
| (20,10) | 0.00625 | [0.009220301321411, 0.009220301321412] |

For (20,2), the prior coefficient was in
[0.002668727384426,0.002668727384427]. This is an improvement in a
necessary coefficient, not a measured exclusion margin.

The pure polynomial (z²-a²)^m has exactly the mirror S_m and fails
the D floor at the selected b. Polynomials with extra nearby real roots
can pass the selected D floor and still collide. This distinguishes
the scalar necessary bound from exclusion, not just the literal source
identity from a different source.

Euler-factor controls also pass (4), because their time-zero imaginary
logarithmic derivative exceeds theta's by a positive term; their own
positive source propagates it. Hence the proof of (1) applies at any of
their all-real finite-multiplicity events satisfying the stated product
premises. It does not eliminate that control family. No location or
multiplicity is asserted for an uncomputed control event.

The q and q_(T,a) controls lack the unchanged xi identity; their order
and product hypotheses must be checked before (3) is used. Weighted-square
and finite-prime controls lack the complete unchanged source and are
not assigned all-real threshold slices. Reflected and positive-primitive
controls lack the exact xi identity. Failing an identity does not imply
failing its derived bound. These are analytical premise screens using
each control's own source, not new computations of their events.

This completes the selected all-height/multiplicity necessary-bound task.
The original double-event pair now has no a>=20 restriction. Higher
multiplicity has a paid differentiated-field consumer, while direct
physical winding exclusion, all heights' theta acquisition and an
opposing arithmetic sign remain open. Further coefficient tables alone
would not advance those tasks.

[old]: 03_IMAGINARY_AXIS_JET_BOUND_20261019.md
[reduction]: ../../07_multiplicity_reduction/notes/02_DIFFERENTIATED_THRESHOLD_TRANSFER_20261020.md
[source]: ../../01_local_double_winding/notes/02_PAIRED_FACE_CONTRACT_20261019.md
[checker]: ../numerics/check_all_height_multiplicity.py
[record]: ../numerics/ALL_HEIGHT_MULTIPLICITY_CONTROLS_20261020.json
[results]: ../../../../../../../result-summaries/README.md
[laws]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[polymath]: https://arxiv.org/html/1904.12438v2#S3
[digamma]: https://dlmf.nist.gov/5.9.E13

[review]: ../reviews/02_ALL_HEIGHT_MULTIPLICITY_REVIEW_20261020.md
