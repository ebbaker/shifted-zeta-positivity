# Using the heat-flow bounds for RH-related problems

26 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual recorded effort
max**. Thread `01a179f9-0a66-7e72-8c76-8576f688be65`, chat 0001.

**Status: opening brainstorm and application assessment.** The author
suggested following Rodgers–Tao, while retaining the alternatives of
lowering the de Bruijn–Newman upper bound and proving RH implies simple
zeros. He also asked that the investigation identify **what types of
bounds would lead to progress**, aspirationally, to inform the intermediate
estimates that are still being developed. This note therefore has two
equal purposes: explore applications of existing bounds, and work backward
from desirable applications to useful future bound specifications. All
three directions remain open. Proposed improvements below are research
targets, not consequences already proved by the Book.

The [Book review](../reviews/01_BOOK_APPLICATION_REVIEW_20261026.md) specifies
what was read; its [manifest](../reviews/BOOK_REVIEW_INPUTS_20261026.json)
identifies the working-tree inputs. Read the repository
[result index](../../../../result-summaries/README.md), especially
[heat flow](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md),
[controls](../../../../result-summaries/12_collision_controls_and_screening.md),
and [local geometry](../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
together with the [avoid index](../../../../avoid/README.md). The governing
patterns are [reformulations](../../../../avoid/01_restating_the_target.md),
[shared control premises](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scoped exclusions](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
and [unchecked imports](../../../../avoid/16_unchecked_imports_and_novelty_claims.md).

## 1. Initial judgment and the direction of the implication

Rodgers–Tao is a strong methodological starting point: it connects
analytic estimates to the dynamics and interaction energy of actual
zeros. The Book supplies richer approximations and derivative budgets
than a purely qualitative description. The missing step is a consumer
that turns those budgets into a sharper estimate for zeros, with the
necessary denominators and exterior contributions paid. It is useful to
identify that consumer's requirements now, even when the required bound
is not yet available. Section 9 records that aspirational feedback to the
approximation program; it is not necessary to wait for every regional
estimate to be finished.

Keep the canonical normalization

\[
 H(t,z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du,
 \qquad H_t=-H_{zz},\qquad H(0,z)=\xi((1+iz)/2)/8.
\]

The Newman threshold satisfies

\[
 H(t,\cdot)\text{ has only real zeros}\iff t\ge\Lambda,
 \qquad \mathrm{RH}\iff\Lambda\le0.
\]

[Rodgers–Tao](https://arxiv.org/abs/1801.05914v5) proves
\(\Lambda\ge0\). Thus RH is equivalent to \(\Lambda=0\).
Strengthening that lower bound to \(\Lambda>0\) would disprove RH.
The constructive interpretation of “strengthen the result” here is
better quantitative dynamics, effective witnesses, or an adaptation
that helps with an upper bound. It is not a stronger positive lower bound.

There are three logically different targets:

| Target | Classification |
| --- | --- |
| Prove \(\Lambda\le0\), or exclude every positive-time theta collision | RH-equivalent; state once, do not count another criterion as progress |
| Improve a specified positive bound \(\Lambda\le b\), an onset, an error, or a certified cost | Quantitative milestone, judged against an explicit baseline |
| Prove RH implies all nontrivial zeta zeros are simple | Separate open conditional target; RH alone does not presently provide the conclusion |

## 2. What the Book makes available

Here \(X\) is height in the heat coordinate, \(L=\log(X/(4\pi))\),
\(T=-t\) on the negative side, and the envelopes are positive sums of
arm moduli. The bounds are not relative to \(|H|\) at its zeros.

| Input and proof location | Retained statement | Possible use and present limit |
| --- | --- | --- |
| [Negative hierarchy](../../01_heat_density_asymptotics/book/sections/02_negative.tex), `thm:negative-fixed` | For fixed order and fixed \(0<\tau\le T\le B\), gamma-normalized field/jets/time error \(O(X^{-p-3/4})\) | Accurate analytic data on negative-time charts; fixed-endpoint constants cannot be silently made height dependent |
| Same section, `thm:negative-growing`, and recurrence Note 20 | Outer error \(e^{-L^2/4}\), with \(p=\lfloor L/2\rfloor\), on \([1,2]\), extended separately to \([1/L,2]\) | Strong tool for negative-time dynamics; excludes \(T=0\), retains roughly \(\sqrt X\) arithmetic modes and large onsets |
| [Signed crossover](../../01_heat_density_asymptotics/book/sections/03_crossover.tex), `thm:crossover` | On \(|t|L\le8\), error \(\mathcal E_o X^{-3/4}e^{t_-L^2/16}\), with spatial/time losses and residual | Covers zero time with complete arithmetic; whole-window allowance is only \(O(X^{-1/4})\), not the recurrence's exponential-in-\(L^2\) error |
| [Positive hierarchy](../../01_heat_density_asymptotics/book/sections/04_positive.tex), `thm:positive-fixed` | Every fixed \(J\) has eventual all-height envelope error \(O(t^{-J-1}\log^{-2J-3}(2+t))\), with jets/time/residual | Detailed late-time geometry; onset depends on \(J\), and its analytic range starts at \(t\ge32\) |
| Same section, `thm:compact-positive` | Fixed \([a,B]\subset[32,\infty)\): \(X^{-2J-3}+X^{-t\log2/4}\); \(P_4\) gives \(X^{-7}\) near 64 | More gamma orders alone do not remove the retained arithmetic term; no permission to insert \(t=0.2\) |
| [Physical clock](../../01_heat_density_asymptotics/book/sections/05_physical.tex) | Growing inner root block, Vandermonde comparison, pair-Laplacian comparison, and differentiated clock transport | Natural energy comparison model; not a closed evolution of that block or a near-zero-time theorem |
| [All-time construction](../../01_heat_density_asymptotics/book/sections/06_global.tex), `thm:global` | Prescribed-regulator, fixed-filter physical tuple approximated uniformly in time and height | Valuable weak-observable machinery; spatial joins are nonholomorphic and their density is not an argument-principle zero count |
| [Compression/evaluation](../../01_heat_density_asymptotics/book/sections/07_effectivity.tex) | Positive finite source with complete four-jet error; polynomial additional-accuracy cost at fixed data and query box | Supports rigorous local evaluation; no uniform practical complexity in height, small time, or regulator resolution |

**Live supplement beyond the Book's production baseline.** The Book still
lists the corrected physical transfer as open. The subsequently completed
[Ansatz Note 23](../../01_heat_density_asymptotics/ansatz/notes/23_FIXED_P4_PHYSICAL_TUPLE_20261026.md)
and [Assessment 17](../../01_heat_density_asymptotics/ansatz/reviews/17_FIXED_P4_PHYSICAL_TUPLE_ASSESSMENT_20261026.md)
record the fixed-\(P_4\) physical tuple on \([63,65]\): static rates
\(X^{-7}\), current/covariance \(X^{-7}(1+\log X)^2\), time/source
\(X^{-6}(1+\log X)^2\), and residual corrections \(X^{-7}\), at their
specified derivative orders. Status is **proved in-note from named inputs,
same-model internal assessment only**. Constants and onset remain
uninstantiated. This closes that particular transfer; small-positive-time
coverage and microscopic limits remain different tasks.

The switch at 64 is prescribed by the regulator. It is not a new Newman
threshold. Indeed all-real behavior is already known above time \(1/2\);
better estimates at time 64 need a further argument to improve an RH result.

## 3. The scales a zero-dynamics application must resolve

The zeta ordinate is \(\gamma=x/2\). The usual mean spacing in the heat
coordinate is therefore \(d_X\sim4\pi/L\), not \(2\pi/L\).
Three limits must be kept separate:

1. \(t\to+\infty\) in the Book's source-saddle clock.
2. \(X\to\infty\) with \(t>0\) fixed, or \(tL\) controlled, in
   arithmetic suppression and crossover estimates.
3. Time increments of order \(d_X^2\asymp L^{-2}\) in local gap dynamics.

The last scale follows directly from the reciprocal-gap velocity law:
rescale \(x=X+d_X u\), freezing \(X,d_X\) on a chart, and use
\(s=t/d_X^2\). The signed crossover already contains every fixed
\(t=\tau/L^2\) at sufficiently large \(X\). What it lacks is a proved
simple-root or nonvanishing margin there. The stronger negative hierarchy
stops at \(T=1/L\), before that microscopic time scale.

One useful new approximation question is whether its moving endpoint can
reach \(T\asymp L^{-2}\). This is not substitution into Note 20:
fixed transverse buffers introduce factors like \(e^{b^2/(4T)}\), now
of size \(e^{O(L^2)}\). Microscopic buffers \(b\asymp L^{-1}\) change
that payment but require a fresh proof with the resulting derivative
losses. Both possibilities deserve a bounded estimate comparison.

The Book's fixed spatial filter spans roughly \(L\) zeros at high
height. Its regulated density does not automatically become a measure
of individual spacings. A proposed shrinking filter or regulator needs
new derivative, commutator, and limit estimates. Similarly, a multiple
zero and two nearby simple zeros have nearly identical fixed-width
smoothed counting measures: for a smooth test kernel,
\(K(\cdot-a-d)+K(\cdot-a+d)-2K(\cdot-a)=O(d^2)\).
Weak density accuracy alone therefore cannot decide simplicity.

## 4. Rodgers–Tao: the leading exploratory route

Use the corrected **v5, 3 July 2021** paper. Its proof assumes
\(\Lambda<0\), studies an all-real interval \(\Lambda<t\le0\), and
forces local equilibrium incompatible with known pair-correlation
information. Section 8's corrected treatment of boundary interactions
matters here. Relevant anchors are PDF Theorem 11, equation (56), and
Propositions 26–28; the HTML numbering differs.

The Book offers two plausible points of contact. Its clock and
Vandermonde estimates can calibrate local energy comparisons in their
actual late-time domain. Its completed negative/crossover formulas can
supply more precise field data in the time regime used in the
contradiction argument. These are separate applications until an
explicit bridge is proved.

At a simple zero, differentiation of the exact heat equation gives
\(a_i'=H_{zz}(t,a_i)/H_z(t,a_i)\). For a finite block with
\(H=U\prod_i(z-a_i)\), this becomes

\[
 a_i'=2\sum_{j\ne i}\frac1{a_i-a_j}
       +2\frac{U_z}{U}(t,a_i).
\]

This elementary factorization explains the principal application
obligation: the block's exterior drift cannot be discarded. Uniformly
small position errors also need not give uniformly small derivatives
of an energy with inverse-square gap weights. A smallest-gap bound and
summation over the population must be accounted for. The Book's pair
Laplacian controls the block geometry under its premises; it does not
by itself bound its coupling to the rest of the zeros.

**Suggested first deliverable:** fix one buffered height block and a
compact time slab on which the relevant simple real roots and boundary
margins have been independently established. Compare a complete
localized energy/exterior-drift allowance obtained from the new
approximant with the allowance from the earlier canonical model, using
the same domain and information. Report a better exponent, constant,
onset, or total acquisition cost, or identify the exact term that
prevents a gain. A bounded positive-time slab already known to be real
is a legitimate methods pilot, but gives no new zero-free region.

For a later negative-time argument, all-real dynamics is conditional
on the explicit contradiction hypothesis. It must not be assumed for
the true field at negative time. Nor can that hypothesis be replaced
by RH while retaining a negative interval: RH, together with Newman
nonnegativity, gives a threshold at zero.

Possible eventual outputs include effective relaxation rates or an
explicit finite-height witness for each specified negative time.
Neither is delivered here. A proof of nonnegativity alone would reproduce
an existing theorem; novelty requires a quantitative comparison.

## 5. An upper-bound route with an exact existing consumer

The reference certificate is [Polymath, Theorem 1.2](https://arxiv.org/html/1904.12438v2):
for \(t_0,X>0\), \(0<y_0\le1\), establish (i) no zeta zeros with
\((1+y_0)/2\le\sigma\le1\), \(0\le\gamma\le X/2\);
(ii) no \(H_{t_0}\) zeros for
\(x\ge X+\sqrt{1-y_0^2}\),
\(y_0\le y\le\sqrt{1-2t_0}\); and (iii) the intermediate barrier
\(X\le x\le X+\sqrt{1-y_0^2}\),
\(\sqrt{y_0^2+2(t_0-t)}\le y\le\sqrt{1-2t}\),
\(0\le t\le t_0\). Then

\[
                         \Lambda\le t_0+y_0^2/2.
\]

This supplies an objective score for an application. The established
published benchmark \(\Lambda\le0.2\) is
[Platt–Trudgian, §3.4, Corollary 2](https://arxiv.org/html/2004.09765v1).
It is a conservative comparison baseline, **not a claim about the best
October 2026 result**. The repository's
[Gomila audit summary](../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md)
records a candidate 0.1787854 package and an unfinished full producer-row
audit. Recent conditional and other claimed improvements require their
own premise/certificate review; the [reference catalog](../references/README.md)
keeps the newly checked conditional paper explicitly conditional.

The strongest Book positive hierarchy does not cover the useful range
\(0<t_0<0.2\). Its proposed \([1/2,1]\) bridge is a useful analytic
step, but still does not reach that range. The crossover's shrinking
\(8/L\) upper endpoint cannot be used as a fixed-time exterior theorem
all the way to infinite height. A complete upper-bound application
needs a small-positive-time approximation, its full arithmetic tail,
and overlap with an established exterior theorem.

The most promising consumer may be a corrected multi-mode canonical
field. At small positive time, retaining more gamma corrections without
the relevant Dirichlet modes can spend effort on the wrong error.
Choose one candidate \((t_0,y_0,X)\) from a reproducible existing
certificate, and compare its complete margin or evaluation cost under
the old and new approximations. Reuse only source data and assumptions
that actually belong to that certificate.

For a holomorphic approximant \(F\), a contour floor \(|F|\ge m>\varepsilon_0\)
and errors \(|H-F|\le\varepsilon_0\),
\(|H'-F'|\le\varepsilon_1\) give the elementary bound

\[
 \left|\frac{H'}H-\frac{F'}F\right|
 \le\frac{\varepsilon_1}{m-\varepsilon_0}
 +\frac{|F'|\varepsilon_0}{m(m-\varepsilon_0)}.
\]

This is a useful transfer interface, not a source of the floor.
Rouché comparison similarly preserves zero counts including multiplicity.
A conjugation-invariant disk with total count one gives one real simple
zero; a disk with count two does not distinguish a double from two simple
zeros. Every lower bound must include arithmetic, analytic, evaluation,
and cell-propagation errors. The globally joined physical field cannot
be used in this holomorphic argument on its nonholomorphic joining bands.

An improved approximation is a milestone only if it improves a complete
margin, certified cost, or covered parameter. A smaller isolated remainder
need not improve the final bound: the repository's retained-Riemann–Siegel
correction audit already provides an example of this consumer mismatch.

## 6. RH implies simple zeros: retain, but connect to the existing work

The [BW-10 investigation](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/README.md)
already studies this target, including complete-root motion, endpoint
controls, and a heat-scale trace. Its proofs remain there. This new
investigation should ask whether the new Book estimates pay a previously
missing arithmetic term, rather than start the same derivations again.

Under RH the positive-time slices have simple real zeros. This does not
settle multiplicities at time zero. The exact heat solution

\[
                    F(t,z)=(z-a)^2-2t
\]

has a double at zero time and two real simple zeros for every \(t>0\).
For their gap, \(g^2=8t\). More generally, subtracting the real-root
equations for adjacent roots \(a<b\), while retaining all other roots,
gives on a simple all-real interval

\[
 \frac{d}{dt}g^2=8-4g^2\mathcal S,
 \qquad
 \mathcal S=\sum_{j\notin\{a,b\}}
        \frac1{(b-x_j)(a-x_j)},\quad g=b-a.
\]

The difference sum is convergent in the canonical setting. Every summand
is positive for adjacent roots. For an isolated double endpoint with
regular exterior data, \(g^2\sim8t\); its inverse-square interaction
has a logarithmically divergent time integral. Higher multiplicities
have their own Hermite splitting constants, so the coefficient 8 is
not an all-multiplicity rule.

These identities diagnose the required resolution. They supply no
contradiction. Integrability of every endpoint pair energy, or a positive
limiting gap for every label under RH, would already encode the desired
endpoint exclusion and is not an independently achieved intermediate
result. Late-time shrinkage or a clock approximation is compatible with
such a multiple endpoint, as the existing BW-10 work explicitly records.

A useful first comparison is narrower: identify an exact complete-theta
term in BW-10's unpaid estimate and test whether the new multi-mode
remainder actually reduces its bound below the control baseline. The
[close positive-source control](../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/10_rh_implies_simple_zeros/notes/05_CLOSE_POSITIVE_SOURCES_AND_NORMALIZED_DOUBLE_ZEROS_20261020.md)
preserves strong normalization and shape information while adding
multiple endpoints under RH; it fails ordinary Dirichlet-series
arithmetic. The decisive improvement would have to use more than the
shared information. A fixed relative source tolerance or an improved
universal leading heat profile does not provide that improvement.

## 7. Keep alternatives that can produce an informative theorem

**Effective negative-time witnesses.** [Dobner](https://arxiv.org/abs/2005.05142v2)
already obtains nonreal zeros at every negative time through a complete
heat-deformed Dirichlet series. A relevant new goal would be an explicit
search region, certified nonreal-root contour, or complexity bound as
\(t\uparrow0\), compared with that argument. Its nonlinear coordinate
map can move the relevant zeros outside fixed transverse strips; the
Book's fixed-buffer theorem does not automatically cover those contours.

**Moving-time zero geometry.** Prove an error or onset improvement for
specified positive-time zero positions or pair energies as time decreases
with height, with a complete multi-mode approximation. Benchmark against
Polymath's existing fixed-positive-time result, not against absence of
any prior real/simple high-zero theorem. A new uniformity regime can be
valuable without implying RH.

**Counts and certification.** Better complete local zero counts or lower
evaluation cost could improve barrier computations even if no new sign
mechanism emerges. Compare with the repository's
[explicit local heat-zero counts](../../../investigations-3/06_explicit_heat_zero_counts/README.md)
and existing finite certificates before selecting a benchmark. Counting
multiplicity is different from proving simplicity.

**Arithmetic cancellation.** Preserve correlated complex errors of
different modes when a concrete consumer can use them. Replacing a signed
sum by separate absolute values may erase the only possible gain.
Conversely, merely writing a signed identity supplies no estimate. This
route is worth retaining if the energy or barrier comparison identifies
exactly which cancellation is needed.

## 8. Control screen before a proposed implication

This is an analytical premise screen using the existing proved/certified
controls, not a rerun of their numerical certificates. No candidate new
theta inequality is asserted to pass it yet. The generic ratio/Rouché,
heat-flow, and weak-transfer identities apply to controls wherever their
local hypotheses hold.

| Control class | Shared information that cannot exclude it | Distinguishing premise or required test |
| --- | --- | --- |
| Euler-factor family \(\Phi_{c,p}\), all relevant primes | Positive even source, exact heat flow; genuine positive thresholds occur | Unchanged full theta coefficients/ordinary zeta factor fail. A proposed *derived inequality* must still be tested, including known witnesses contradicting any claimed \(\Lambda\le0.2\) |
| Weighted-square and finite-theta-tail controls | Square support, positive moments, finitely many reflection endpoints | Full canonical reflection/completion fails. Their local collisions cannot be mislabeled finite all-real thresholds |
| Reflected super-Gaussian control | Full even reflection, positive source and Gram information | Canonical integer-square arithmetic fails; reflection alone is not the separating premise |
| Smooth log-concave and positive-primitive controls | Strong shape, decay, positivity, and extensive asymptotic/endpoint matching | Complete theta arithmetic fails; finite asymptotic agreement alone cannot settle the sign |
| Finite-prime-compatible perturbations | Any specified finite set of prime identities and finite measurements | Complete reflection/unchanged infinite coefficients fail. Finite-prime agreement is insufficient by itself |
| Earlier \(q\), \(q_{T,a}\) counter-kernels | Positivity/evenness/heat identities and genuine positive thresholds | Canonical source fails; any generic global noncollision argument must fail at their events |
| Atomic and exact finite-profile threshold controls | Selected exact profiles, bounded moments, specified threshold events | Full theta profile/arithmetic and eventual simplicity assumptions fail; a few measurements cannot replace them |
| RH-conditional normalized endpoint controls | Arbitrary fixed source closeness, completion/tail normalization, simple positive-time zeros | Ordinary Dirichlet arithmetic fails; the endpoint consumer must distinguish these controls quantitatively |
| Polynomial/Hermite heat models | Exact heat equation and universal multiple-root splitting | Canonical theta source and arithmetic absent; they reject an inference from later simplicity alone |

Merely observing that a control is not theta is not a proof that a new
estimate rejects it. Record the exact failed hypothesis, or test the
proposed inequality on a domain containing its known event. A finite
certificate can correctly succeed on a collision-free region of a control.
These exclusions are limited to their stated information classes.

## 9. Aspirational bounds that could guide the intermediate work

A good target specification names the desired mathematical consequence,
the exact input norm and domain, the needed smallness threshold, and the
parameter whose dependence is currently missing. It can be valuable
research planning without being a theorem. In particular, a final-strength
estimate should be labeled honestly rather than rejected simply because
it would be difficult or would imply RH or simplicity.

| Desired bound | Why it would matter | Feedback to the Book program |
| --- | --- | --- |
| **Uniform small-positive-time canonical field/jets**, on specified slabs inside \(0<t<0.2\), with a complete multi-mode remainder, explicit constants, and overlap with the exterior region | Could pay a real upper-bound barrier or allow a lower \(t_0\); generic late-time precision does not pay this domain | Prioritize extension of the time range and arithmetic completion, not only more saddle orders at time 64 |
| **Near-zero microscopic comparison**, with frozen \(x=X+O(M/L)\), \(|\Im z|=O(1/L)\), \(|t|=O(L^{-2})\), and explicit dependence on block size \(M\) | Could supply local zero-dynamics data at the scale relevant to gap motion | Revisit the negative endpoint and crossover with paid narrow buffers; the present crossover already gives a baseline, so ask what extra precision a consumer needs |
| **A contour or first-jet lower margin paired with the error**, rather than only an upper remainder | Would turn excellent approximation into a certified count, simple-root disk, or velocity estimate | Expose normalized model margins and derivative floors alongside residual budgets; retain cancellations in the full mode sum |
| **Exterior unit-drift and boundary-interaction bounds for finite zero blocks**, including variation across a gap | Would make the clock/pair-Laplacian geometry usable in an actual localized dynamics argument | Estimate \(2U_z/U\) and its derivatives after removing the block; compare their contributions with the local interaction scale and retain the full zero tail |
| **A paid localized energy balance**, with explicit boundary and arithmetic errors below the amount needed by its application | Could quantify relaxation or identify precisely where a new arithmetic estimate would change the argument | Map the physical covariance/weak identities to the *same* energy functional first; a signed covariance identity is not automatically the required coercive inequality |
| **Transfer uniform at shrinking spatial resolution and regulator**, with mass retained and any changing-filter terms paid | Could expose zero counts or pair observables hidden by a fixed filter | Extend weak primitives and corrected collars to declared \(\ell,h,\eta\) families; identify the rate at which constants worsen, rather than assuming fixed-parameter estimates remain uniform |
| **An RH-conditional, theta-specific endpoint interaction estimate stronger than universal multiple-root scaling** | Would address simplicity directly; this is a final-strength aspirational target | Seek arithmetic information absent from the normalized endpoint controls; improving their shared leading heat profile cannot supply the separation |
| **Joint effective bounds in height, time, order, requested precision and consumer margins** | Would tell whether a theoretical improvement can become a finite certificate | Expose those dependencies, even if initially large; fixed-data polynomial accuracy cost alone does not answer this question |

For example, write normalized field errors on a contour as
\(|H-F|\le A e_0\), \(|H'-F'|\le A L e_1\),
and suppose the *model* has \(|F|\ge A\mu\) and
\(|F'|\le A L B_1\). The quotient estimate in Section 5 becomes

\[
 \frac1L\left|\frac{H'}H-\frac{F'}F\right|
 \le \frac{e_1}{\mu-e_0}
       +\frac{B_1e_0}{\mu(\mu-e_0)},\qquad e_0<\mu.
\]

This tells the approximation program *which ratio to improve*. An
arbitrarily impressive error exponent is unhelpful if the unknown
\(\mu\) is smaller. Conversely, a moderate remainder with a robust
floor can already be enough. The target need not always be a new power
of \(X\); it may be a better coupled margin, a wider time range, or
control of constants near zero time.

For an energy application, a useful aspirational form is a localized
balance

\[
 \mathscr F_W(t_2)+\int_{t_1}^{t_2}\mathscr D_W(t)\,dt
 \le \mathscr F_{W^+}(t_1)
       +\mathscr B_W(t_1,t_2)+\mathscr A_W(t_1,t_2),
\]

where the actual chosen energy and nonnegative dissipation must be
defined, \(W^+\) pays localization, \(\mathscr B_W\) includes all exterior
and moving-boundary contributions, and \(\mathscr A_W\) records the
source-specific approximation/arithmetic payment. This is a **design
template, not a proved inequality**. A consumer must specify how small
the last two terms need to be. No universal exponential relaxation rate
is presumed; the block size, slow modes and its actual spectral gap matter.

For endpoint simplicity, one explicit final-strength target would be an
RH-conditional majorant for
\(\mathscr E_W(t)=\sum_{i<j,\ x_i(t),x_j(t)\in W}(x_j(t)-x_i(t))^{-2}\)
in each fixed bounded window, with any tested endpoint in its interior,
that is integrable as \(t\downarrow0\), for example
\(C_W t^{-1+\delta_W}\) with \(0<\delta_W<1\). The constants would have
to be established independently of a lower time cutoff, and the coverage
would have to include every possible endpoint and multiplicity. Universal
double-root splitting instead costs \(1/t\). Thus the integrable bound
would exclude a multiple endpoint; it is a way of specifying the strength
of the missing arithmetic theorem, **not a weaker result already obtained**.
The normalized endpoint controls force us to identify a quantitative
theta input before expecting such a bound. Uniform constants over all
heights are not logically necessary if every bounded window is covered.

The feedback loop should be short: select a consumer, compute its required
error/margin/parameter dependence, compare that requirement with the
current estimates, and send the resulting target back into the parent
research priorities. For each proposed bound, label it **available**,
**plausible extension**, or **aspirational with a new arithmetic input**.
An explicit missing-bound specification can guide useful work even when
no new zero theorem is proved in this investigation's first round.

## 10. A flexible first round, with decision points

| Task | Concrete output | Continue when |
| --- | --- | --- |
| 0. Consumer requirements | Specify the domain, norm, margin and parameter dependence of one useful future bound; compare it with the available estimates | The specification explains what mathematical conclusion a successful bound would pay and can inform the intermediate-bound priorities |
| A. Rodgers–Tao interface | Match one localized energy/exterior-interaction term to a Book field/jet contract; retain the corrected boundary accounting | A complete bound or cost improves, or a specific new arithmetic estimate becomes identifiable |
| B. Small-positive certificate | Compare one existing barrier or exterior certificate with a full small-time approximation and fixed parameters | All hypotheses are covered and total margin/cost improves; otherwise record the first unavailable domain or estimate |
| C. Endpoint simplicity comparison | Crosswalk one unpaid BW-10 term to the new bounds and the normalized endpoint control | A theta-specific quantitative separation appears; shared heat profiles alone are not enough |
| D. Moving negative endpoint | Test \(T\asymp L^{-2}\) with explicit transverse-buffer and derivative payments | The completed error improves the existing crossover for a specified consumer |

Start with A, honoring the author's preference. B is the most direct route
to an objective Newman-bound score if the small-time domain can be supplied.
C remains a serious alternative, with a larger arithmetic obligation.
D is shared analytic infrastructure rather than a commitment to proving RH.
No large numerical sweep is needed before one of these comparisons defines
what its result could decide.

A useful first output can be a justified bound specification, before the
bound itself is proved. Later mathematical milestones should be short
application theorems or complete quantitative comparisons. The Book's
improved bounds make these questions worthwhile; they do not yet identify
a winning RH mechanism. Keep the general folder name and let the evolving
consumer requirements help determine both this investigation's direction
and the intermediate-bound goals.
