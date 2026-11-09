# B10 r3: direct cell ranges pay the geometric projection width

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, OC chat0011. Recorded thread settings
`gpt-6-astra / max`; per-turn backend configuration unavailable. Root is
the sole writer; no delegation or model change.

**Disposition: complete at analytical design/conditional-contract scope.**
The E13 census is sufficiently precise for the unchanged Gaussian
projection without further centroid acquisition. The endpoint-range
construction below has geometric radius less than
\(1261/409600=0.00307861328125\). With endpoint arithmetic radii summing
to at most \(1/1000\), and the inherited complete tail \(2^{-32}\), its
final radius is **less than 0.0041, hence less than 1/200**.
This is **proved in-note, proof-author checked**. The canonical scalar
and the bounded arithmetic pass remain pending [E13 r2][request].

Read the [result index][results] and [avoid index][avoid], particularly
[local geometry13][geometry], [theta14][theta], [controls12][controls],
[classification01][a01], [premise screen02][a02], [scoped exclusions07][a07]
and [finite certification11][a11]. Classification: a finite numerical
acquisition contract with a quantitative uncertainty bound, not an
RH-equivalent criterion. The number above measures an enclosure allowance;
it is neither the value of the statistic nor new collision coverage.

## 1. What the acquired evidence actually supplies

[E13 Note21][n21], [assessment17][r17], [execution18][run] and
[Return27][census] retain the complete census despite the centroid-stage
source-call stop. The retained rectangle is
\(\mathcal R=(988,2012)+i(-3/2,3/2)\), with 388 occupied cells and one
label in each. These are complete-source winding counts, including
multiplicity; no assumption of real roots is added here.

Exact parsing of the recorded dyadic cells gives, with cells sorted by
their left real endpoint,
\[
 N=388,\qquad
 u:=\max_C|X_C|=5/32768,\qquad
 v:=\max_C|Y_C|=15/131072,
 \tag{1}
\]
\[
 \min_i(\inf X_{i+1}-\sup X_i)=5085/8192>1/2.
 \tag{2}
\]
Every imaginary interval is \([-3/32768,3/131072]\); it is retained as
an interval, never replaced by zero. The largest squared diameter is
\(625/17179869184\). [Exact record19][exact] checks these facts and
the accepted count tree against the hash-matching external trace, with
zero new canonical source calls and zero kernel evaluations.

The new useful input beyond the old count-only cap is **the actual
horizontal geometry of this certified census**. Formula (2) is a fact
about this finite artifact, not a proposed uniform zeta gap theorem or
a premise about later heat times. It implies that arbitrary points
chosen in cells i and i+k have real separation greater than k/2.

## 2. Preserve the target and enclose each ordered cell product

Keep [Note19 (4)–(6)][n19] and [Note20 (3)–(4)][n20] exactly:
\[
 P_{1000}=\sum_{j\ne k}K(z_j,z_k),\quad
 K(z,w)=c_G I_T(m)g(d)b_+(y)b_-(y'),
 \tag{3}
\]
where \(T=1000,\ell=h=1,\epsilon=1/4\),
\[
 c_G=32\sqrt2/51<1,\quad m=(x+x')/2,\quad d=x-x',
 \quad g(d)=e^{-25d^2/36},\quad
 b_\pm(y)=e^{-(8/17)(y\mp1/2)^2},
\]
\[
 I_T(m)=\frac{\sqrt\pi}{2T}
 [\operatorname{erf}(2T-m)-\operatorname{erf}(T-m)].
 \tag{4}
\]
The center is still uniform on \([1000,2000]\). Both edges, both ordered
imaginary marks, the original observation blur and all labels remain.

For an unordered pair C<E, form exact rational intervals
\[
 M=[(x_C^-+x_E^-)/2,(x_C^++x_E^+)/2]=[m_-,m_+],
 \quad D=[x_E^--x_C^+,x_E^+-x_C^-]=[d_-,d_+].
\]
Here \(d_->0\). Define the following **ideal real endpoints**, before
floating or ball evaluation:
\[
 \begin{split}
 A_-&=\frac{\sqrt\pi}{2T}
  [\operatorname{erf}(2T-m_+)-\operatorname{erf}(T-m_-)],\\
 A_+&=\frac{\sqrt\pi}{2T}
  [\operatorname{erf}(2T-m_-)-\operatorname{erf}(T-m_+)],\\
 I_-&=\max(0,A_-),\qquad I_+=\min(2/T,A_+),\\
 G_-&=e^{-25d_+^2/36},\qquad G_+=e^{-25d_-^2/36}.
 \end{split} \tag{5}
\]
Monotonicity of erf encloses I on all of M; the clipping uses the
proved bounds \(0\le I_T\le\sqrt\pi/T<2/T\). The natural dependency
loss from using the two erf terms separately is explicitly paid below.

For each mark sign, let \(s_{C,\pm}^-\) and \(s_{C,\pm}^+\) be the
minimum and maximum of \((y\mp1/2)^2\) on \(Y_C\). These extrema are
exact rational numbers, using distance to the interval and its endpoints.
Set
\[
 B_{C,\pm}^-=e^{-(8/17)s_{C,\pm}^+},\qquad
 B_{C,\pm}^+=e^{-(8/17)s_{C,\pm}^-},
\]
\[
 H_{CE}^{\pm}=B_{C,+}^{\pm}B_{E,-}^{\pm}
                  +B_{E,+}^{\pm}B_{C,-}^{\pm}.
 \tag{6}
\]
The same superscript denotes lower or upper endpoints throughout (6).
It is a sum of the two ordered products, not twice one of them.
For the present singleton census define
\[
 L_* =c_G\sum_{C<E}I_-G_-H_{CE}^-,\qquad
 U_* =c_G\sum_{C<E}I_+G_+H_{CE}^+.
 \tag{7}
\]
All factors are nonnegative. Interval inclusion term by term proves
\(P_{1000}^{\mathcal R}\in[L_*,U_*]\). Discarding dependencies between
M, D and the marks only enlarges this enclosure. Every one of the
75,078 unordered pairs is evaluated; no small pair is dropped.

**Factorial self rule.** For general integer counts, cross-cell terms
have coefficient \(n_Cn_E\), and same-cell terms have coefficient
\(n_C(n_C-1)\) multiplying an enclosure of **K on C×C**. A diagonal
range \(K(z,z)\) alone would not cover two distinct points in one cell.
Only for a point cell or known coincident labels may that term reduce
to the diagonal D. In this frozen census \(n_C=1\), so the same-cell
coefficient is exactly zero. No uncertain raw sum is subtracted from
another uncertain self sum, and no distinct-label contribution is lost.

## 3. Gaussian decay pays the range width

For C=i and E=i+k put \(q_k=e^{-k^2/16}\). The exact ranges in (5)–(6)
satisfy
\[
 \operatorname{wid}I\le 2u/T,\qquad \sup I\le2/T,
 \quad \sup G\le q_k,\quad \operatorname{wid}G\le4u q_k,
 \tag{8}
\]
and \(\sup B\le1,\operatorname{wid}B\le v\).

To prove the first bound, each erf endpoint difference changes at
speed at most \(2/\sqrt\pi\), so the width of the unclipped I interval
is at most \(2(m_+-m_-)/T\le2u/T\). Clipping cannot increase width.
For \(a=25/36\),
\[
 |g'(d)|=2\sqrt a\,(\sqrt a|d|e^{-ad^2/2})e^{-ad^2/2}
       \le2e^{-d^2/4},\qquad g(d)\le e^{-d^2/4}.
\]
Here \(\sup_{t\ge0}t e^{-t^2/2}=e^{-1/2}<1\), \(a<1\) and
\(a/2>1/4\). Use \(d\ge k/2\) and \(|D|\le2u\) to obtain (8).
Finally \(\sup|b_\pm'|=\sqrt{16/(17e)}<1\) gives the mark width.

For nonnegative intervals, product width is bounded by telescoping
one factor at a time against the upper bounds of all other factors.
Thus the ideal interval for **one ordered contribution** has width
at most
\[
 \frac{2u}{T}q_k+\frac2T(4u q_k)
       +\frac2T q_k(2v)
 =\frac{10u+4v}{T}q_k.
 \tag{9}
\]
There are \(2(N-k)\) ordered pairs at index separation k. No statistical
independence is used. As the Gaussian is decreasing on the positive
axis,
\[
 \sum_{k=1}^{\infty}e^{-k^2/16}
 <\int_0^\infty e^{-t^2/16}\,dt=2\sqrt\pi<4.
\]
Consequently
\[
 U_*-L_*<\frac{8N(10u+4v)}{T},\qquad
 \boxed{\frac{U_*-L_*}{2}<\frac{4N(10u+4v)}{T}
       =\frac{1261}{409600}.}
 \tag{10}
\]
The old count-only Lipschitz allowance in Note20 is an upper bound,
not a lower bound forbidding this improvement. Equation (10) uses
the observed ordered spacing and Gaussian decay to sum local
uncertainty. It is specific to these singleton separated cells. A
large multi-label cell or a smaller separation must not inherit (10).

## 4. A separately testable arithmetic gate

Evaluate the two real expressions \(L_*,U_*\) in (7) as **point
expressions in outward ball arithmetic**, including all scalar erf/exp
evaluations, \(\pi\), square roots, products and sums. Exact dyadic
input conversion has zero initial error. Rational constants such as
8/17 must themselves be enclosed outward. Max/min in (5) are monotone
maps of point-enclosing balls: apply them to the exact lower and upper
endpoints, never choose a branch from the midpoint when its sign is
unresolved. Retain intermediate uncertainty until both endpoint
expressions have been enclosed.

Let their final balls be \(\mathcal L,\mathcal U\), with radii r_L,r_U.
Require finite balls and
\[
 r_L+r_U\le1/1000. \tag{11}
\]
Set \(a=\inf\mathcal L,b=\sup\mathcal U\) using exact dyadic outward
endpoints. Require \(a\le b\). Then
\[
 \frac{b-a}{2}\le\frac{U_*-L_*}{2}+r_L+r_U.
\]
This follows because each outward endpoint is within at most twice
its ball radius of the enclosed exact point. It does not assume either
point is the ball midpoint.

The canonical tail from Note20 (11), checked in E13 P2, is unchanged:
\(0\le P_{1000}-P_{1000}^{\mathcal R}<t\), \(t=2^{-32}\).
Use the conservative interval \([a-t,b+t]\). Its exact radius obeys
\[
 R_{\rm final}<\frac{1261}{409600}+\frac1{1000}+2^{-32}
              <\frac{41}{10000}<\frac1{200}. \tag{12}
\]
The executor must also test the actual final dyadic radius strictly
against 1/200. A printed rounded decimal or comparison of midpoints
does not pass either gate. Serialize the endpoint balls and final
endpoints exactly; reparse them and repeat the inequalities.

| Contribution | Payment |
| --- | --- |
| Locations anywhere in the certified cells | (10), below 0.003079 in radius |
| Endpoint-expression arithmetic | Measured r_L+r_U ≤ 0.001 |
| All labels outside the complete rectangle | Inherited 2^-32 |
| Centroid replacement or moment quadrature | None; no centroid is used |
| Marks, center edges, blur, small pairs | Included in the exact target and every pair range |

Higher precision can reduce (11); it cannot reduce the fixed geometric
part. The endpoint functions are continuous, including max/min, so
the point arithmetic converges in arbitrary precision. This gives a
viable method, not a guarantee that a particular library meets the
finite precision and elapsed-time caps.

## 5. Evidence import and bounded execution

The census is imported at **E13's recorded certificate scope**. The
return, execution record, source code, proof assessment and external
trace must match the frozen digests in [Inputs29][inputs]. Reconcile
trace leaves with the returned dyadic cells, the outer 388 count and
the accepted count tree. Every coordinate, count, split and gap check
uses exact arithmetic. [Checker19][check] performs that source-free
structural check and six malformed-census rejection controls.

**A hash is identity evidence, not a new winding proof.** The trace's
decimal source-ball displays are inspection data; they are not a
standalone exact arithmetic certificate. E13's outward execution and
review remain the load-bearing source premise. Neither this note nor
the new checker independently recomputes it. A reader needing fresh
source certification must replay the separately bounded E13 source
acquisition; that is outside the zero-new-source-call r2 pass. Missing
or mismatched evidence fails closed, with no replacement by a list of
approximate real zeros. The external trace exists and both hashes
matched during this turn's inspection.

[E13 r2][request] freezes (5)–(12), all 388 cells and all 75,078 pair
products, precision 128/256/512, one worker, zero new source or centroid
calls, at most 1,400,000 exp/erf calls in total, and a cumulative
600-second evaluator ceiling. The canonical endpoint formula needs
452,020 exp/erf calls per full precision pass before caching savings.
These are declared work counts, not measured runtime savings. One
bounded implementation repair must fit the same cumulative limits.
Return a certified projection or the first exact failed gate.

## 6. Collision controls and scope

The [controls12][controls] inventory was applied analytically at premise
level; its original numerical collision certificates were not rerun.

| Control class | Premise absent for the canonical application; surviving statement |
| --- | --- |
| Euler-factor | Unmodified complete theta/zeta source fails. Its own paid divisor still obeys interval inclusion. |
| Weighted-square, finite-tail, finite-prime orbit | Full normalized reflection or complete unit coefficients fail. The canonical count, strip and tail are not transferred. |
| Reflected super-Gaussian, smooth shape, positive primitive | Complete arithmetic theta expansion fails; smooth positive kernels alone do not supply the census. |
| Atomic and finite-profile threshold | Complete theta growth/profile fails. Their collisions are compatible with the factorial rule. |
| RH-conditional theta-close endpoint | Ordinary Dirichlet-series arithmetic fails. It does not acquire this frozen source census. |
| Variable observation kernel | Literal cosine/Newman equation fails. Snapshot inclusion does not use that equation and need not reject the control. |
| Fractional-profile relaxation | Integer labelled-divisor realizability fails; fractional masses are not winding multiplicities. |

Local analytical controls are also explicit. A double zero at any
complex a contributes \(2K(a,a)\); a cell enclosing two distinct zeros
uses K on C×C, not the diagonal. For unequal imaginary marks,
\(K(z,w)/K(w,z)=\exp[(16/17)(y-y')]\), so replacing the two orders
by twice one fails this control. For a real or imaginary split
\(a\pm\delta\) in a common cell, interval inclusion still holds,
whereas the singleton/separation hypotheses of (10) do not. Empty and
singleton divisors have zero factorial sum. These statements check
the proposed mechanism against collisions without asserting their
canonical occurrence or exclusion. E13 r2 adds numerical containment
and rejection tests for these fixed cases before using the census.

**Next: [E] TND-OC-E13 r2 — GPT-6.1 Sol**, with author-selected effort.
The conceptual choice is resolved; the remaining work is proof checking,
fixed endpoint arithmetic and a bounded execution record. A failed
evidence gate, unresolved proof clause or exhausted arithmetic/work
gate returns to B10 r4 only for a named new decision. No automatic
budget enlargement. [Review18][review] is same-assistant checking;
no specialist or independent acceptance is claimed. No manuscript
milestone, investigation closure, root-summary promotion or sibling
status change occurs here. [Continuation25][continuation] carries the
manual model handoff and [Progress02][progress] owns live status.

[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[geometry]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a11]: ../../../../../../avoid/11_certifying_the_known_and_tests_that_cannot_fail.md
[n19]: 19_TND_OC_B10_R1_GAUSSIAN_CONTRACTION_AND_MISSING_ESTIMATE_20261109.md
[n20]: 20_TND_OC_B10_R2_CONTOUR_CENTROIDS_AND_GAUSSIAN_ESTIMATE_20261109.md
[n21]: 21_TND_OC_E13_R1_GAUSSIAN_PROJECTION_EXECUTION_20261109.md
[r17]: ../reviews/17_TND_OC_E13_R1_PROOF_AND_IMPLEMENTATION_CHECK_20261109.md
[run]: ../numerics/18_TND_OC_E13_R1_EXECUTION_20261109.json
[census]: ../research-progress/handoffs/27_TND_OC_E13_R1_RETURN_20261109.json
[exact]: ../numerics/19_TND_OC_B10_R3_EXACT_GEOMETRY_20261109.json
[check]: ../numerics/check_b10_r3_cell_geometry.py
[review]: ../reviews/18_TND_OC_B10_R3_CELL_RANGE_SELF_CHECK_20261109.md
[request]: ../research-progress/handoffs/29_TND_OC_E13_R2_CELL_RANGE_EVALUATOR_REQUEST_20261109.md
[inputs]: ../research-progress/handoffs/29_TND_OC_E13_R2_INPUTS_20261109.json
[continuation]: ../continuation-notes/25_TND_OC_AFTER_B10_R3_AND_MODEL_CHANGE_20261109.md
[progress]: ../research-progress/02_TND_OC_MARGINAL_PRIORITIES_RESEARCH_PROGRESS_20261108.md
