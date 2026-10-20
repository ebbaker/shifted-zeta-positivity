# A quantitative forward neighborhood with positive Laguerre expression

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
recorded parent-session reasoning effort **ultra**, inherited by this
research subagent.

**Status: proved in-note; [separate same-model internal review][review].**
No specialist review. This is a scoped
local obstruction to BW-02 through BW-05. It gives an explicit forward
neighborhood where an ordinary double event cannot produce any of the
four proposed later witnesses. It uses the heat equation and complete
third- and fourth-derivative bounds, not all-real threshold information.
It supplies neither a theta-specific signed estimate nor an RH argument.

The [result summaries][results], especially [collision controls][controls],
and [patterns to avoid][avoid], especially [classification][a01],
[shared premises][a02], and [scoped conclusions][a07], fix that status.
The previous [same-point obstruction][initial] is strengthened to a
uniform moving-point estimate on a full spatial interval. No literature
priority is asserted for this quantitative form of local splitting.

## 1. Frozen class and derivative contract

Let H be real on the real axis, holomorphic in z on a neighborhood of
|z-a|<=r, twice continuously differentiable in real time on
[T,T+sigma], and satisfy H_t=-H_zz there. Require the differentiability
needed for the derivatives below and the exact event

\[
 H(T,a)=H_z(T,a)=0,\qquad h=H_{zz}(T,a)\in\mathbb R\setminus\{0\}.
\]

Set sigma=r^2/4, r>0. The physical H, its time variable, and its source
remain unchanged. There is no variable normalizer. Let M3,M4 be finite
complete bounds on |H_zzz| and |H_zzzz| throughout
[T,T+sigma] x {|z-a|<=r}. Real-interval bounds alone suffice for this
note's scalar theorem; the complex-disk bounds also supply [BW-02][bw02].
Define

\[
 \alpha={M_3r\over |h|},\qquad
 \beta={M_4r^2\over |h|},\qquad
 K(\alpha,\beta)=4\alpha+{3\beta\over8}
 +{3\alpha^2\over4}
 +(\alpha+\beta/8)(\alpha+\beta/4).                 \tag{1}
\]

Every exact analytic double event has some r for which K<1: on an
initial fixed neighborhood the derivative bounds are finite, and they
can be kept fixed while r shrinks. No radius uniform in event height,
time, or h is claimed.

## 2. Complete derivative remainders

For 0<=s<=sigma and |w|<=r, put q=w^2/2-s. Spatial Taylor expansion and
the heat equation give

\[
\begin{aligned}
 H(T+s,a+w)&=h q+R_0,\\
 H_z(T+s,a+w)&=h w+R_1,\\
 H_{zz}(T+s,a+w)&=h+R_2,
\end{aligned}
\]

with

\[
\begin{aligned}
 |R_0|&\le M_3(|w|^3/6+s|w|)+M_4s^2/2=:e_0,\\
 |R_1|&\le M_3(|w|^2/2+s)=:e_1,\\
 |R_2|&\le M_3|w|+M_4s=:e_2.                      \tag{2}
\end{aligned}
\]

For the first line, use

\[
 H(T+s,z)=H(T,z)-sH_{zz}(T,z)
       +\int_0^s(s-v)H_{zzzz}(T+v,z)\,dv.
\]

The other lines follow by integrating H_zt=-H_zzz and
H_zzt=-H_zzzz, respectively. Spatial Taylor integrals run along the
segment from a to a+w, inside the disk. Thus (2) has no unrecorded
fifth- or sixth-derivative demand, and includes mixed time/spatial error.

For real w=y, set R=s+y^2/2. Then |q|<=R,

\[
 e_1=M_3R,\qquad
 e_0\le(M_3|y|+M_4s/2)R.
\]

Expanding the physical Laguerre expression L=H_x^2-HH_xx *before*
paying the product errors yields

\[
 \left|\mathcal L-h^2R\right|
 \le 2|hy|e_1+e_1^2+|hq|e_2+|h|e_0+e_0e_2.     \tag{3}
\]

With A=M3/|h| and B=M4/|h|, division by h^2 R, for R>0, bounds
the right side by

\[
 4A|y|+\tfrac32Bs+A^2R
       +(A|y|+Bs/2)(A|y|+Bs).
\]

The inequalities |y|<=r, s<=r^2/4 and R<=3r^2/4 give (1).

**Forward scalar theorem.** If K(alpha,beta)<1, then throughout
0<s<=r^2/4, |y|<=r,

\[
 \boxed{\quad
 \mathcal L(T+s,a+y)\ge
 [1-K(\alpha,\beta)]h^2(s+y^2/2)>0.
 \quad}                                                        \tag{4}
\]

The estimate also holds at s=0 and is strict there when y!=0.
At the original event equality is required. In particular, this closes
the attempted negative-Laguerre witness for *all moving points inside
this certified forward neighborhood*, not just the fixed point a.

A convenient sufficient contract is

\[
 \alpha\le1/16,\qquad\beta\le1/4.                    \tag{5}
\]

Then K<=367/1024 and the right side of (4) is at least
(657/1024)h^2(s+y^2/2), hence greater than h^2(s+y^2/2)/2.
These rational constants are not asserted optimal.

## 3. A radius from the unchanged complete theta source

Use exactly the [predecessor's][predecessor] physical convention

\[
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
\quad
 \Phi(u)=\sum_{n\ge1}
 (2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
\]

At the hypothetical theta event, define the finite positive quantities

\[
 C_j(T)=\int_0^\infty
 u^j e^{(T+1/4)u^2}\Phi(u)\cosh u\,du,\qquad j=3,4. \tag{6}
\]

Absolute convergence follows directly from the double-exponential
decay. On any disk of radius r<=1 and any 0<=s<=r^2/4,
|sin((a+w)u)| and |cos((a+w)u)| are at most cosh u; hence Cj are
complete complex derivative bounds. The explicit event-dependent choice

\[
 r_*=\min\left\{1,{|h|\over16C_3(T)},
                   \sqrt{{|h|\over4C_4(T)}}\right\}>0,
 \qquad\sigma_*=r_*^2/4                                  \tag{7}
\]

satisfies (5). The center a need not be known numerically. Formula (7)
does not compute a theta event or a uniform event-free region; it is a
conditional quantitative consequence of the hypothetical exact event.
It uses the original source only as a complete absolute envelope. It
does not exploit arithmetic cancellation, and the corresponding own-source
envelope works for other sufficiently decaying kernels.

There is no truncation in (6). If numerical moment estimates are later
used, replace Cj by proved upper bounds including every source tail and
quadrature error, and replace |h| by a strictly positive proved lower
bound. Without those bounds (7) is an analytic formula, not a numerical
certificate. An uncertain event center or residual H,Hx must be paid
separately; this theorem assumes exact cancellation and is not an interval
test for whether a hypothetical box contains an event. In particular a
nonzero absolute residual at the center cannot be ignored as s tends to
zero.

## 4. Consumers and exact controls

The same contract supplies three further conclusions, with proofs in
their own route notes:

* [BW-02][bw02]: exactly two zeros in |z-a|<r at every 0<s<=sigma,
  both real and simple; no off-real contour wholly in this disk can have
  a positive zero count.
* [BW-03][bw03]: no real multiple event in the forward rectangle; at a
  real zero |Hx|>=sqrt(657/1024)|h| sqrt(s) under (5).
* [BW-04][bw04]: zero physical winding on every bounded Jordan region
  whose closure lies inside 0<s<=sigma, |y|<=r. It follows from a
  nonzero jet throughout the enclosed region, not just on its boundary.

The [exact rational checker][checker] and [receipt][receipt] verify the
constants and the following own-polynomial controls. They do not certify
an actual theta event or imply an arithmetic gain.

| Control | Exact outcome and scope |
| --- | --- |
| h(y^2/2-s), h=1 and h=-1 | M3=M4=0, K=0; (4) is equality. Two real simple forward roots, two imaginary backward roots. Backward time is outside the contract. |
| Even threshold quartic from the predecessor, T=1/4,a=1,r=1/64 | h=8, M3=24(1+r), M4=24. Contract (5) passes. Positive threshold and all-real forward evolution coexist with every conclusion. |
| Negative of that quartic | Same margins and zero locations; L is unchanged. No hidden positive-h normalization. |
| Same quartic at r=1/8 | The scalar K test fails. The proof reports no scalar bound at that radius, although the actual function has nonnegative L. Failure of a sufficient bound is not a negative witness. The separate complex zero-count test still passes. |
| Flow from y^2(1+y^2)/2 at T, r=1/16 | h=1, M3=12r, M4=12; (5) passes. At s=r^2/4 there are also two imaginary zeros outside the disk. Thus a local conclusion does not establish global real-rootedness or a threshold. |
| Cubic Hermite event y^3-6sy at (0,0) | h=0, excluded. No all-multiplicity conclusion is inferred. |
| Original double event s=0,y=0 | Strict positivity and a wholly-later domain test refuse this boundary case. |

The remaining required [control screens][controls] are analytic premise
screens, not invented numerical runs:

| Family | Shared and missing premises |
| --- | --- |
| Positive-kernel q and q_(T,a) | At a proved exact double event with finite local derivative envelopes, all hypotheses here are shared. No theta-only premise occurs in (1)-(5); their canonical coefficients differ. |
| Euler-factor controls | Same heat law and usable own-source moments; the unchanged theta source is absent. At an exact double event this theorem applies with their own h,M3,M4. A lower bound on their threshold alone is not a supplied double-event location. |
| Weighted-square and finite-prime controls | Certified/analytic local double events admit the same local estimates. Full normalized reflection or the unchanged complete coefficients fail. Their local event times are not promoted to finite all-real thresholds. |
| Reflected smooth / positive-primitive controls | Reflection and auxiliary positivity add no needed hypothesis to this local theorem. At their established double events use their own envelopes. The complete normalized theta square expansion is absent; no numerical damping/event parameter is invented. |
| Smooth-density / two-channel positive constructions | Auxiliary positivity alone does not provide an exact physical double event with the required complete derivative data. No threshold claim for these families is made here. |

## 5. What this closes and what remains

The completed task is a quantitative obstruction, with the explicit
number in (4), to obtaining any later witness *inside the certified
forward neighborhood from local double-event data*. It remains valid
without global real-rootedness and therefore cannot distinguish theta
from the threshold controls. It is not an RH-equivalent reformulation.

Any successful BW-02--BW-05 implication must use new arithmetic information
to force a physical witness beyond this local exclusion, or contradict
some necessary premise of the hypothetical event itself. No such signed
arithmetic implication is proved here. In particular, choosing a later
time outside (7), reducing h, or increasing a numerical search domain
does not itself provide a witness. Higher multiplicities, unbounded
event heights, and a uniform radius remain untreated.

[initial]: 01_INITIAL_RESEARCH_NOTE_20261019.md
[bw02]: ../../02_later_nonreal_zeros/notes/02_COMPLETE_DISK_EXCLUSION_20261020.md
[bw03]: ../../03_later_real_collisions/notes/02_FORWARD_COLLISION_EXCLUSION_20261020.md
[bw04]: ../../04_later_negative_winding/notes/02_FORWARD_ZERO_WINDING_20261020.md
[checker]: ../numerics/check_forward_neighborhood_controls.py
[receipt]: ../numerics/FORWARD_NEIGHBORHOOD_CONTROLS_20261020.json
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[predecessor]: ../../../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex

[review]: ../reviews/01_FORWARD_NEIGHBORHOOD_REVIEW_20261020.md
