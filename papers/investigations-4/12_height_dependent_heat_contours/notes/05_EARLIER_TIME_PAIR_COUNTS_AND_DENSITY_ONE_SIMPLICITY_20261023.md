# Earlier-time pair counts and RH-conditional density-one simplicity

23 October 2026, America/New_York. Prepared for **Edward Baker** with substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**, reasoning effort **ultra**. Separate same-model agents checked the finite birth balance and the projected-pair implication; no specialist review.

**Status: proved elementary finite transfer and conditional statistical consequence; no theta pair estimate or new simplicity proportion obtained.** The author identified RH implying almost-all simplicity as a worthwhile intermediate objective, separately from proving every zero simple. This note records the corresponding real-time consumer. It does not require the physical imaginary-time cap estimate of Notes 02–04.

Follow the [result index](../../../../result-summaries/README.md), [local heat geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md), [avoid index](../../../../avoid/README.md), [classification rule](../../../../avoid/01_restating_the_target.md), [control register](../../../../result-summaries/12_collision_controls_and_screening.md), and [scoped-obstruction rule](../../../../avoid/07_scoped_exclusions_read_as_universal.md). The underlying real-birth and conserved-complex-population identities are already established in [LHCT Note 05](../../11_late_heat_caps_and_charge_transport/notes/05_ZERO_COUNTS_REAL_BIRTHS_AND_RELATIVE_TOPOLOGY_20261022.md). The new work here is their explicit connection to the author's density-one statistical objective.

## 1. The target and its literature status

Write N(T) for zeta zeros up to height T counted with multiplicity, and N_s(T) for simple zeros. The target is

\[
 \mathrm{RH}\quad\Longrightarrow\quad N_s(T)/N(T)\longrightarrow1.
 \tag{1}
\]

This would be a substantial advance over the RH-alone proportion 19/27 established by [Bui–Heath-Brown](https://arxiv.org/abs/1302.5018), which is still the RH-conditional benchmark reported in [Lamzouri's September 2026 introduction](https://arxiv.org/html/2609.02882). This is a literature-based assessment, not a claim that this note proves (1). Standard full PCC under RH implies almost-all simplicity, as [Montgomery's original paper, p.184](https://websites.umich.edu/~hlm/paircor1.pdf), explicitly states. It does not eliminate every exceptional multiple zero.

The distinction matters: an error tending to zero in a normalized population can prove (1). Excluding every double instead requires a bound below the contribution of one exceptional pair, of order 1/N.

## 2. A finite count transfer across an earlier real time

Let a<0. Suppose H is a real-type holomorphic solution of H_t=−H_zz near [a,0] times the closure of a bounded conjugation-invariant spatial domain U. Assume no spatial slice is identically zero and H is nonzero on the spatial boundary throughout this interval. Let N be its conserved number of roots in U, counted with multiplicity. Write N_nr(t) for the number of nonreal roots, with the same convention.

At an isolated real event of spatial order m, the local heat/Hermite law has m mod 2 real roots just before, and m real roots just after. At the event itself its real root is counted m times. Complex events off the real axis preserve the nonreal count. Therefore

\[
 N_{\rm nr}(a)-N_{\rm nr}(0)
 =\sum_{\substack{a<t\le0,\ x\in U\cap\mathbb R\\H(t,x)=H_z(t,x)=0}}
       2\lfloor m(t,x)/2\rfloor .
 \tag{2}
\]

The upper endpoint is included; the lower endpoint is excluded. A real multiple root at a already contributes its full multiplicity there and splits into the same number of real roots immediately afterward, so it introduces no missing endpoint correction. The local heat law isolates multiple events; compactness and the zero-free spatial wall make the finite count legitimate. This argument does not require a nonzero first jet at t=0.

Suppose all endpoint roots are real, as supplied by RH for the canonical field. Define their nonsimple multiplicity mass and multiplicity excess by

\[
 M_0=\sum_{m(0,x)\ge2}m(0,x),\qquad
 D_0=\sum_x(m(0,x)-1).
\]

Since m<=3 floor(m/2) for m>=2, while m−1<=2 floor(m/2), (2) gives

\[
 \boxed{M_0\le\tfrac32N_{\rm nr}(a),\qquad
 D_0\le N_{\rm nr}(a).}
 \tag{3}
\]

The number of multiple endpoint sites is at most N_nr(a)/2. For a growing sequence of complete populations covering all but o(N(T)) endpoint labels, an independently proved N_nr(a)=o(N) therefore implies (1). Different bands may have different a, provided each population is completely tracked and the total omitted-root and wall-crossing costs are controlled at the root-count level. They are not silently discarded.

## 3. Which earlier-time pair statistic suffices

Include **all** N earlier roots z_j(a), including nonreal roots and repeated labels. For a positive unfolding density nu, define

\[
 \mu_N=\frac1N\sum_{i\ne j}
 \delta_{\nu(\Re z_i(a)-\Re z_j(a))}.
 \tag{4}
\]

Off diagonal means different labels, not different projected locations. Every nonreal label has a distinct conjugate label with exactly the same real projection. If a conjugate pair of locations has multiplicity r at each, it contributes 2r² ordered pairs at zero and 2r nonreal labels. Consequently

\[
 \frac{N_{\rm nr}(a)}N\le\mu_N(\{0\}),\qquad
 \boxed{\frac{M_0}N\le\tfrac32\mu_N(\{0\}).}
 \tag{5}
\]

Thus vague convergence of these complete projected-pair measures to any locally finite measure without an atom at zero implies density-one simplicity at the endpoint. Continuous nonnegative tents, or compact-set Portmanteau, justify the zero-atom bound. PCC only for the real-root subset at a does not control omitted nonreal roots. Tests supported away from zero also lose the relevant witness.

For a finite inequality use f_delta(s)=(1−|s|/delta)_+ and suppose

\[
 \int f_\delta\,d\mu_N
 \le\int f_\delta(s)R_2(s)\,ds+e_N(\delta),
 \qquad R_2(s)=1-\left(\frac{\sin\pi s}{\pi s}\right)^2.
 \tag{6}
\]

The triangular Fourier representation of sinc squared and 1−cos v<=v²/2 imply R2(s)<=pi²s²/3. Also integral f_delta(s)s² ds=delta³/6. Therefore

\[
 \boxed{\frac{M_0}N\le
       \frac{\pi^2\delta^3}{12}+\frac32e_N(\delta).}
 \tag{7}
\]

For each fixed delta, an error tending to zero as N grows is enough: take the population limit first, then delta down to zero. Neither a shrinking-test rate nor full PCC is needed. The weaker condition

\[
 \lim_{\delta\downarrow0}\limsup_N\int f_\delta\,d\mu_N=0
 \tag{8}
\]

already suffices. It is an upper bound near zero, distinct from the positive inverse-square lower bound in [Note 04](04_PAIR_STATISTICS_AS_A_ONE_SIDED_CONTOUR_INPUT_20261023.md). A sparse set can defeat an every-zero conclusion while remaining fully acceptable for (1).

## 4. Classification, controls and missing estimates

Unrestricted existence of a sequence a_N approaching zero with N_nr(a_N)=o(N) is a reformulation of density-one simplicity under the finite endpoint-reality contracts. Indeed (3) proves one direction. Conversely, for each finite population choose a sufficiently near zero that there are no intermediate events; then N_nr(a)=sum_endpoint 2 floor(m/2)<=M_0. Choosing such a after knowing the endpoint multiplicities does not constitute progress. A prescribed, source-derived height scale and an independently proved bound such as (6) would constitute additional information. The stronger projected nonconcentration condition is not claimed equivalent to simplicity.

The exact double H=z²−2t has N_nr(a)=2 and M_0=2. The cubic H=z³−6tz has N_nr(a)=2 and M_0=3, proving the 3/2 in (3) sharp. At negative time their conjugate pairs contribute the zero atom required by (5); the cubic also has additional coincident projections, so it does not establish sharpness of (7). No generic smoothing estimate can erase these witnesses. A finite number of such controls is compatible with density-one simplicity in a growing population; the aim is to bound their density, not to reject each individual event.

The broader Euler-factor, reflected, weighted-square, positive-primitive and normalized endpoint controls in the linked register obey the same finite identities. No new statistical estimate is asserted for them or for theta. Their recorded failures of unchanged theta arithmetic, reflection or complete coefficients cannot substitute for proving (6). In particular close positive-source controls exclude a shape-only inference, not a future arithmetic density bound.

An o(N) set of omitted roots need not change a normalized pair statistic by o(1), because one omitted root can form many pairs. Account for omitted endpoint labels after the count transfer, or independently estimate their pair-statistic contribution. Under a height-dependent contour, each population and real-time track must be specified; sampling roots at unrelated times and calling the result one heat slice is not justified.

No statement here asserts that backward Gaussian smoothing produces (6), keeps almost every root real, or improves an existing RH-conditional simplicity proportion. The next independent input is a near-zero pair upper bound at a prescribed earlier time, with complete populations and coverage. [Note 06](06_PAIR_MATRIX_SPECTRUM_AND_ENDPOINT_MULTIPLICITY_20261023.md) connects this objective to the previously studied pair-matrix eigenvalues.
