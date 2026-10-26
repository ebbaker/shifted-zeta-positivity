# Rodgers–Tao with a positive-threshold contradiction hypothesis

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**. Chat 0001, thread 01a179f9-0a66-7e72-8c76-8576f688be65.

**Status: explanatory analysis and aspirational bound specification.**
This answers the author's question: why not assume \(\Lambda>0\), rather
than \(\Lambda<0\), and seek a contradiction? It continues
[Brainstorm 01](01_HEAT_FLOW_RH_APPLICATIONS_BRAINSTORM_20261026.md) and is
tracked in the [current summary](../summary/CURRENT_SUMMARY.md).
No new upper bound, collision exclusion, or independent literature-proof
verification is claimed.

## 1. A legitimate strategy, with a different missing step

There is no logical objection to the proposed contradiction assumption.
In the canonical convention

\[
 \partial_t H(t,z)=-\partial_z^2H(t,z),\qquad
 H(0,z)=\tfrac18\xi((1+iz)/2),
\]

the all-real times are exactly \([\Lambda,\infty)\), and RH is equivalent
to \(\Lambda\le0\). The positive-threshold assumption is precisely the
failure of RH. The question is whether the Rodgers–Tao machinery gives a
contradiction there, and what the new bounds would need to add.

Our reading of [Rodgers–Tao v5](https://arxiv.org/abs/1801.05914v5) is:
under \(\Lambda<0\), an all-real evolution ending at zero forces almost
all normalized gaps there toward one. Section 9 contradicts this using
zeta spacing results under RH, which their premise already implies.
Their estimates work away from the lower endpoint; corrected Section 8
pays the boundary interactions. PDF anchors: Theorem 11 / equation (56),
Propositions 26–28, and equation (93). HTML numbering differs.

The following diagnosis is our analysis of changing that premise.

| Assumption | Where real-root dynamics is available | Endpoint available for comparison |
| --- | --- | --- |
| \(\Lambda<0\) | A fixed all-real interval before \(0\), staying above \(\Lambda\) | The original zeta slice at \(0\), with its arithmetic spacing information |
| \(\Lambda>0\) | Only above \(\Lambda>0\); slices below the threshold have some nonreal zeros | A positive-time heat deformation, with no reason to inherit the time-zero spacing obstruction |

In the first case, zero time is an interior time of the all-real regime,
after a positive duration of evolution. At height \(X\), with mean heat
coordinate spacing \(d_X\sim4\pi/\log(X/(4\pi))\), a fixed duration is
many local interaction times \(d_X^2\). This explains the relaxation
picture; the actual proof must still control all its terms.

In the second case, the known zeta slice lies before the interval of
ordered real zeros. The complex-root equation can still be written away
from multiplicities, but real ordering and the positive real-gap energy
arguments do not carry over unchanged. The RH-dependent spacing input
used in the first contradiction is also unavailable under this premise.
This does not forbid a new complex-zero argument; it identifies a
different task.

## 2. Neither a time shift nor reversing relaxation fixes this

Shift by a real \(a\):

\[
 G(s,z)=H(a+s,z),\qquad
 G(0,z)=\int_0^\infty e^{a u^2}\Phi(u)\cos(zu)\,du.
\]

Its threshold is \(\Lambda-a\). Taking \(a=\Lambda\) puts the threshold
at zero, with no preceding all-real interval. Taking \(a>\Lambda\)
creates a negative threshold for \(G\), but the slice \(G(0,\cdot)\) is
\(H(a,\cdot)\), not the zeta slice. The original zeta slice has shifted
to \(s=-a\), still below the new threshold when \(\Lambda>0\).
The heat factor changes the source, so the required zeta spacing
information is not preserved by this translation.

Indeed, [Polymath, Theorem 1.5](https://arxiv.org/html/1904.12438v2)
already gives real, simple, asymptotically regularly spaced high zeros
for each \(0<t\le1/2\), beyond a height of exponential order in \(1/t\).
That conclusion does not assume RH. Positive-time regularity is
therefore compatible with the hypothesis we want to contradict.

A forward energy-dissipation estimate also has an orientation.
Schematically, \(E(t_2)\le E(t_1)+\text{payments}\), for \(t_2>t_1\),
does not upper-bound earlier energy from a later upper bound. Such
information can coexist with energy that diverges at the lower endpoint
and rapidly decreases afterward. A bound on every interval
\([T+\varepsilon,t_2]\), whose constant diverges as
\(\varepsilon\downarrow0\), gives no endpoint exclusion.

Thus better late-time clock accuracy alone would not supply the missing
contradiction. A new estimate must address the initial exceptional
configuration or propagate information toward it with a paid bound.

## 3. A positive threshold is a finite collision problem

The repository already proves the relevant reduction from named
Polymath inputs in
[the collision manuscript](../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/newman_collision_reductions.tex),
Proposition “A positive threshold entails a finite collision”
and Corollary “Exact endpoint target.”

Here is the compactness argument to keep its scope visible. Suppose
\(\Lambda=T>0\) and choose \(t_n<T\) increasing to \(T\), with a nonreal
zero \(z_n\) at each time. For \(t_n\ge T/2\), a uniform exterior theorem
confines nonreal zeros to a fixed finite height range; a strip bound
confines their imaginary parts. After taking a subsequence,
\(z_n\to x_*\), where \(H(T,x_*)=0\) and \(x_*\) is real. If that zero
were simple, the implicit-function theorem and conjugation would give a
unique real zero nearby for real times on both sides of \(T\), contrary
to the chosen \(z_n\). Consequently

\[
                    H(T,x_*)=H_z(T,x_*)=0.
\]

The argument gives multiplicity **at least two**, not necessarily
exactly two. Uniform localization in a neighborhood of \(T\) is
essential: separate finite exceptional sets at separate times would
not establish compactness.

For this canonical family, excluding all positive-time real common
zeros of \(H,H_z\) is the existing RH-equivalent endpoint target.
We use that reduction once; a new name or representation for the
target is not an improvement.

A collision at one finite height, however large that height is, can
escape an asymptotic statement about almost all zeros as height tends
to infinity. This is the additional reason a stronger bulk relaxation
theorem need not settle the positive-threshold question. An averaged
argument remains possible, but it needs an explicit implication from
the average to this particular local event.

## 4. The local heat model shows the missing strength

For any \(T>0\), the even real polynomial

\[
                    F(t,z)=z^2-2(t-T)
\]

solves \(\partial_tF=-F_{zz}\). Its zeros are nonreal for \(t<T\),
double at \(t=T\), and real and simple for every \(t>T\). Writing
\(s=t-T>0\), their gap satisfies

\[
             g^2=8s,\qquad g^{-2}=\frac1{8s}.
\]

There is nothing inconsistent about a positive threshold for the heat
equation itself. This model does not have theta's source or arithmetic;
it only checks what follows from the shared local heat mechanism.
The repository's genuine positive-kernel controls provide the stronger
source-level screen below.

More generally, Polymath Proposition 3.1(ii) supplies Hermite splitting
at a multiplicity-\(m\) event. Its local roots have the form
\(x_*+\sqrt{2s}\lambda_j+O(s)\), with distinct real Hermite roots
\(\lambda_j\). For the cluster's inverse-square pair energy, direct
substitution gives

\[
 E_{\rm cluster}(T+s)=\frac{c_m+o(1)}s,\qquad
 c_m=\frac12\sum_{i<j}(\lambda_j-\lambda_i)^{-2}>0.
\]

Here \(c_2=1/8\). The higher-multiplicity constants need not equal
that value. The logarithmic divergence of the time integral is a
feature of a hypothetical event, not an independently forbidden
behavior.

The existing
[BW-10 program](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/README.md)
studies the analogous endpoint at \(T=0\) under RH. Import its complete
root-motion and control lessons, while keeping the two questions distinct.

## 5. Useful specifications for new bounds

These are application requirements, not proved inequalities or claims
of a new criterion. Their value is to direct the intermediate work.

### A. A fixed positive slab: an incremental target

Choose \(b>0\) below an established upper bound \(B\le1/2\).
An exterior estimate uniform for \(b\le t\le B\) confines any candidate
collision to \(|x|\le R_b\); existing asymptotics give a theoretical
cutoff of shape \(R_b=\exp(C/b)\), after enlarging the absolute constant.
Practical use needs an instantiated constant and all required margins.

On that finite slab, let \(F\) approximate the canonical field, with
pointwise complete errors
\(|H-F|\le\varepsilon_0\) and
\(|H_z-F_z|\le\varepsilon_1\). For a declared positive length
\(\ell\), the elementary vector triangle inequality shows that

\[
 \sqrt{|F|^2+\ell^2|F_z|^2}
   >\sqrt{\varepsilon_0^2+\ell^2\varepsilon_1^2}
\]

excludes a common zero of \(H,H_z\) at the point. Positive amplitude
normalization can be applied to both sides. Covering every point of
the closed slab, together with its exterior, excludes a threshold in
\([b,B]\), and hence implies \(\Lambda<b\). This is sufficient for
the weaker reported milestone \(\Lambda\le b\).

For a real application, all source, arithmetic, truncation, evaluation,
and interpolation errors must be included. Sampling points is not
coverage. No common-zero assumption may be hidden in the margin.
Compare against the existing direct/barrier certificates on the same
data before expecting an energy method to be more efficient.

**Feedback to the bounds:** small-positive-time coverage, a complete
multimode remainder, lower first-jet margins, and lower exterior onsets
are immediately relevant. A fixed \(b\) is a genuine finite target;
passing to \(b\downarrow0\) requires additional uniform estimates,
not an extrapolation from several successful slabs.

### B. A threshold-centered energy target: aspirational

Under the hypothetical \(T=\Lambda>0\), take a bounded window \(W\)
with a suspected event in its interior and no endpoint zero on its
boundary. For sufficiently small \(s>0\), define

\[
 E_W(T+s)=
 \sum_{\substack{i<j\\x_i(T+s),x_j(T+s)\in W}}
          (x_j(T+s)-x_i(T+s))^{-2}.
\]

A bound implying

\[
                  sE_W(T+s)\longrightarrow0
                  \quad(s\downarrow0)
\]

would contradict the displayed cluster asymptotic at that event.
An integrable majorant \(C_{W,T}s^{-1+\delta}\), \(0<\delta<1\),
would be a stronger example. The constants must be independent of an
artificial lower cutoff and of an assumed minimum gap. Every candidate
height and multiplicity must eventually be covered; constants need not
be uniform over all heights merely to exclude each finite event.

This is a **final-strength target**, not a weaker result proved here.
To make it a viable research program, first identify an arithmetic term
that could yield the improved endpoint rate. Even a precise reason
the current error loses that rate would inform the next estimates.

For a finite block, the exact simple-root identity is

\[
 H=U\prod_j(z-a_j),\qquad
 a_i'=2\sum_{j\ne i}(a_i-a_j)^{-1}+2U_z(t,a_i)/U(t,a_i).
\]

Accordingly, a proposed localized energy estimate must pay the exterior
unit, moving boundaries, singular gap weights, and the full arithmetic
remainder. The Book's physical covariance or pair Laplacian must first
be matched to the actual energy being bounded. A useful bound cannot
be obtained by discarding the exterior drift or by assuming all gaps
are already bounded away from zero.

The leading heat profile is universal. The desired improvement must
use information that a matching colliding source fails, potentially
complete arithmetic cancellation or a quantitative normalized margin.
The present note identifies no such new successful theta estimate.

## 6. Control screen and what remains open

This is an analytic use of the existing controls, not a rerun of their
numerical certificates. The full inventory remains in Brainstorm 01 §8
and [result cluster 12](../../../../result-summaries/12_collision_controls_and_screening.md).

| Control | Consequence for this proposal / missing theta premise |
| --- | --- |
| Polynomial and Hermite flows | Exact heat evolution and forward real-root repulsion allow an earlier collision. Canonical positive theta source and arithmetic are absent. |
| \(q,q_{T,a}\) positive-kernel families | Positive even rapidly decaying sources can have genuine positive thresholds. The canonical theta completion is absent. |
| Euler-factor families, for all relevant primes | Retain positive sources and explicit arithmetic structure but modify the ordinary zeta coefficients. A universal claimed upper bound must also confront their certified witnesses. |
| Weighted-square and finite-tail families | Square support and some endpoint identities do not exclude local collisions; full canonical reflection/completion fails. Their events must not be called finite all-real thresholds. |
| Reflected and smooth/primitive families | Strong symmetry, shape, positivity, or asymptotic matching does not provide the needed exclusion; full theta arithmetic fails. |
| Finite-prime and finite-profile families | Preserve their declared finite constraints but fail the complete coefficient/reflection or full-profile requirements; finite observations cannot be silently promoted to those requirements. |
| Normalized RH-conditional endpoint families | Later real simple zeros and arbitrary fixed source closeness still allow a multiple zero at time zero; ordinary Dirichlet arithmetic fails. This specifically screens the simplicity alternative. |

The sub-\(1/s\) endpoint energy target necessarily fails on any control
with the displayed finite-multiplicity splitting at its event. A
first-jet certificate cannot pass at a common zero if its error bounds
are valid. Either can correctly hold on a region of a control that
contains no collision. These observations check the logical interfaces;
they do not establish a theta-specific lower margin or improved rate.

Follow the [result index](../../../../result-summaries/README.md),
especially [11](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
and [13](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and the [avoid index](../../../../avoid/README.md), particularly
[reformulations](../../../../avoid/01_restating_the_target.md),
[shared premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope](../../../../avoid/07_scoped_exclusions_read_as_universal.md), and
[checked imports](../../../../avoid/16_unchecked_imports_and_novelty_claims.md).
This analysis rules out the direct reuse of the same endpoint
contradiction; it is not an impossibility result for positive-threshold
methods.

**Recommended next piece of work:** compare one complete local
energy/exterior estimate with a direct first-jet certificate on a fixed
positive slab. State what additional arithmetic estimate would improve
its margin, onset, or endpoint dependence. This keeps Rodgers–Tao as
the methodological lead and gives the intermediate-bound program a
concrete consumer, while retaining upper-bound and simplicity alternatives.

Source inspection was targeted: corrected Rodgers–Tao introduction and
§§8–9, Polymath Theorem 1.5 and Proposition 3.1, and the repository's
existing finite-collision proof. The reference catalog records the
versions and retained PDF provenance. Local algebra and logical scope
were checked by this same assistant; no independent specialist review
or research numerical experiment was performed.
