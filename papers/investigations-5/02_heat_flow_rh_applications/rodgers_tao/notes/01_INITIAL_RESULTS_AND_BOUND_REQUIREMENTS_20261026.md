# Initial results and bound requirements for the Rodgers–Tao approach

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**. Parent chat 0001; thread 01a179f9-0a66-7e72-8c76-8576f688be65.

**Status: synthesis of existing results and exploratory requirements.**
The initial results here are imported theorems, earlier local calculations,
and logical distinctions established in this conversation. They are not
new RH results. The sources are the parent's
[brainstorm](../../notes/01_HEAT_FLOW_RH_APPLICATIONS_BRAINSTORM_20261026.md),
[positive-threshold analysis](../../notes/02_RODGERS_TAO_POSITIVE_THRESHOLD_20261026.md),
and [Book review](../../reviews/01_BOOK_APPLICATION_REVIEW_20261026.md).
[Input identities](INITIAL_INPUTS_20261026.json) pin the opening baseline.

## 1. What the opening discussion established

| Finding | Status and implication |
| --- | --- |
| \(\Lambda>0\) is a legitimate contradiction premise | RH means \(\Lambda\le0\) in the canonical convention. The question is the missing mathematical contradiction, not the logic of the premise. |
| The original sign argument has a distinguished endpoint | Under \(\Lambda<0\), real-root evolution reaches the zeta slice at zero time. The positive-threshold premise places that slice before the all-real regime. |
| A time shift does not restore the endpoint input | For \(G(s,z)=H(a+s,z)\), the threshold becomes \(\Lambda-a\), but the zeta slice moves to \(s=-a\). |
| A positive threshold forces a finite multiple-zero event | The existing repository proof uses exterior localization uniform near the threshold and compactness. It gives multiplicity at least two, not necessarily exactly two. |
| Forward repulsion permits an earlier collision | \(z^2-2(t-T)\) is an exact heat solution with threshold \(T\). Later simplicity alone cannot exclude its double endpoint. |
| Bulk regularity need not detect the event | A finite exceptional region can coexist with regular high zeros. An averaged estimate needs a separate implication to the suspected local collision. |
| Upper error bounds need lower margins to control zeros | A small complete field remainder does not itself bound a logarithmic derivative, prove a simple-root disk, or prevent simultaneous \(H=H_z=0\). |
| The strongest endpoint requirement is still aspirational | A bound excluding every positive-time event would settle the RH-equivalent target; specifying it is useful planning, not an achieved weaker theorem. |

For the primary sources and detailed arguments, retain
[Rodgers–Tao v5](https://arxiv.org/abs/1801.05914v5), the
[Polymath record](../../references/README.md), and parent Note 02.
The canonical sign is \(\partial_tH=-H_{zz}\), and
\(H(0,z)=\xi((1+iz)/2)/8\). Height in the heat coordinate is twice
the zeta ordinate.

## 2. Keep three different energy objects distinct

For an isolated finite cluster at \(T\), let

\[
 E_{\rm pair}(T+s)=\sum_{i<j}(x_j(T+s)-x_i(T+s))^{-2}.
\]

At multiplicity \(m\ge2\), Hermite splitting gives
\(E_{\rm pair}(T+s)=(c_m+o(1))/s\), with \(c_m>0\) and \(c_2=1/8\).
This is the endpoint diagnostic used in parent Note 02.

Rodgers–Tao instead use, among their localized objects, the renormalized
interaction from PDF §7, equations (62)–(63):

\[
 V(r)=r^{-2}-1+2(r-1)\quad(r>0),\qquad
 \widetilde E_{jk}=
 \frac{1}{(\xi_k-\xi_j)^2}
 V\!\left(\frac{x_k-x_j}{\xi_k-\xi_j}\right).
\]

Here \(\xi_j\) are their classical reference locations, not the entire
function \(\xi(s)\). Their block sum counts ordered pairs \(j\ne k\);
our \(E_{\rm pair}\) counts each pair once. Reference positions,
weights, cutoffs, and this factor of two must be retained.

At a fixed finite collision with nonzero reference gaps, the subtracted
constant and linear terms in this formula stay bounded. Consequently
renormalization alone does not remove the inverse-square singularity.
This is an elementary reading of the displayed formula, not a new
estimate for the canonical field.

The Book's physical covariance and pair-Laplacian quantities form a
third set of objects. Their comparison with the chosen energy must be
proved; they are not interchangeable by notation. Nor may a formal
infinite Hamiltonian identity be differentiated without paying its
convergence and boundary terms.

## 3. The available field input has advanced

After the opening brainstorm,
[Ansatz Note 26](../../../01_heat_density_asymptotics/ansatz/notes/26_RETAINED_ARITHMETIC_MOVING_POSITIVE_BAND_20261026.md)
and [Assessment 20](../../../01_heat_density_asymptotics/ansatz/reviews/20_RETAINED_ARITHMETIC_MOVING_BAND_ASSESSMENT_20261026.md)
report a complete retained-arithmetic comparison on
\(4/L\le t\le1\), \(L=\log(X/(4\pi))\), together with the existing
signed-window overlap. The same finite model covers \(0\le t\le1\)
at sufficiently large height.

To avoid confusing the source note's logarithmic symbol with the Newman
constant, write \(\mathcal L_X=1+\log X\) and
\(\epsilon_X=\mathcal L_X^2X^{-3/4}\). Its stated field contract is

\[
 |\partial_z^j(H-F_N)|\le C_j E_o\mathcal L_X^j\epsilon_X
 \quad(0\le j\le3),\qquad
 |\partial_t(H-F_N)|\le C_tE_o\mathcal L_X^2\epsilon_X.
\]

It also bounds the actual residual and its first spatial derivative.
The model retains \(O(\sqrt X)\) modes with its cutoff frozen on each
analytic chart. Constants and onsets depend on the fixed buffers and
remain uninstantiated.

Preserve the source status: **proved in-note from named inputs;
same-model internal assessment only**. We inspected the theorem, union,
scope, and assessment, not independently every proof step.
This updates the earlier application inventory: the reported
high-height positive-time field-domain gap has closed at this allowance.
It does not provide a root margin, a finite-height collision exclusion,
uniform shrinking-resolution transfer, or a practical evaluator cost.
The stronger negative recurrence rate still has its separate endpoint.

## 4. What the new bounds would have to buy

The first application question is how the complete error compares with
the denominator or margin required by an actual zero observable.
For a finite block,

\[
 H=U\prod_j(z-a_j),\qquad
 a_i'=2\sum_{j\ne i}(a_i-a_j)^{-1}+D(t,a_i),\qquad
 D=2U_z/U.
\]

A gap involves the difference \(D(t,a_i)-D(t,a_j)\). A common
translation cancels, so a bound on this variation may be more useful
than separate absolute drift bounds. Whether it yields a quantitative
gain with the available data remains to be determined.

For threshold work the target strength is qualitatively different:
an estimate forcing \(sE_W(T+s)\to0\) would contradict a finite
multiple-zero event in the interior of \(W\). Its constants must not
hide dependence on a lower time cutoff or a minimum gap. No such
theta estimate is established. A better forward relaxation estimate
away from \(T\) does not automatically give it.

For a fixed upper-bound milestone, a complete first-jet margin on a
finite positive-time slab, combined with a uniform exterior theorem,
is a concrete alternative consumer. The domain, onset, complete error,
and baseline certificate must be fixed before claiming a gain.

These observations motivate the
[research overview](../research-overview/01_RODGERS_TAO_RESEARCH_OVERVIEW_20261026.md):
first identify the actual energy and its dependencies, then derive the
bound requirements, then compare them with available approximations.

## 5. Control screen and scope

The full screen is inherited from parent Brainstorm §8 and Note 02 §6.
Polynomial/Hermite flows lack the theta source; positive-kernel
\(q,q_{T,a}\) controls lack canonical theta completion; Euler-factor
controls modify the ordinary coefficients; weighted-square and finite-tail
controls lack full canonical reflection/completion; reflected and
smooth/primitive controls lack the full arithmetic data; finite-prime
and finite-profile controls lack the corresponding complete identities.
Normalized RH-conditional endpoint controls fail ordinary Dirichlet
arithmetic. Their events test the claimed inference at its actual domain.

The generic local identities apply to controls where their hypotheses
hold. A proposed theta inequality must show which quantitative premise
fails at a control's event; merely naming theta is insufficient.
The controls limit those shared-premise arguments, not all future
positive-threshold methods. No numerical control certificates were rerun.

Read the [result index](../../../../../result-summaries/README.md),
[heat-flow reductions](../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[controls](../../../../../result-summaries/12_collision_controls_and_screening.md),
[local geometry](../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and [avoid index](../../../../../avoid/README.md), especially
[reformulations](../../../../../avoid/01_restating_the_target.md),
[shared premises](../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
and [scoped conclusions](../../../../../avoid/07_scoped_exclusions_read_as_universal.md).
No independent specialist review is claimed for this synthesis.
