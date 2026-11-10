# What the signed-source search is asking for

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, direct chat0007, thread
`01a1c389-3fe9-7930-8223-c935cc1920e1`. Actual backend model and reasoning
effort are unavailable in accessible canonical capture metadata.

**Explanatory brainstorm note, requested by the author.** This explains
the established setup, the limited B03 return, and the mathematical choices
still open. It does not activate another research pass, propose a proved
new signed estimate, issue E09/E10, or change the prior evidence levels.
The author asked that this session's notes be kept in the brainstorm folder.

The [result index][results] and [avoid index][avoid] govern the account;
the relevant source clusters are [collision controls12][controls],
[local geometry13][geometry] and [theta arithmetic14][theta]. In particular,
[avoid01][a01] distinguishes an estimate from a restatement of the target,
[avoid02][a02] requires a control to test the premise actually used,
[avoid07][a07] keeps failures limited to their proved class, and
[avoid12][a12] explains why separate absolute estimates can lose the
cancellation we need. The authoritative current disposition is in the
[sole progress register][progress], [Decision04][decision] and [Note09][note09].

## 1. The unresolved work is conceptual

B03 was explicitly a brainstorm/decision task. Its last pass checked the
chosen diagnostic and established a narrow limitation of one elementary
way to estimate it. It did not discover a promising independent signed
theta inequality or exhaust the possible proof strategies.

We know what signal a nondegenerate double collision would produce. We
do not yet have a source-specific estimate that rules out that signal.
The remaining choice is the mathematical proposition and proof mechanism
to pursue. Selecting a model, a cutoff, a precision or a larger batch of
calculations cannot supply that proposition by itself.

Here “new” means additional useful information beyond the identities and
absolute bounds already available. It need not be a theorem new to the
literature, a changed physical source, or a new apparatus. An existing
theorem could be useful if its hypotheses apply and it supplies the
missing signed comparison. No such imported theorem is identified here.

## 2. What is fixed: one particular source and its Fourier observation

The canonical source is explicitly known. On the positive half-line,

\[
 \Phi(u)=e^u\sum_{n\ge1}
 \left[2(n^2\rho(u))^2-3n^2\rho(u)\right]e^{-n^2\rho(u)},
 \qquad \rho(u)=\pi e^{4u}.
 \tag{1}
\]

Every summand is positive there. The complete source also satisfies
\(\Phi(-u)=\Phi(u)\), with smooth reflection supplied by the complete
theta identity. The unit coefficients at all integer-square indices,
their exact weights, the reflection relation, and all omitted tails are
part of the fixed input. Positivity, evenness and rapid decay are only
some consequences of that input. The [operator source section][source]
gives the exact normalization and complete derivative bounds.

Write
\[
 F_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 H_\lambda(k)=\int_0^\infty F_\lambda(u)\cos(ku)du,
 \qquad \partial_\lambda H_\lambda=-H_\lambda''.
 \tag{2}
\]
The last equation follows by differentiating the integral. Primes denote
real observation derivatives. The repository normalization is
\(H_0(k)=\xi((1+ik)/2)/8\), where \(\xi\) is the completed zeta function.
Thus real \(k\) corresponds to the critical line. The local finite-class
question below is not, by itself, a proof of the global zero statement.

Although \(F_\lambda\) is positive, \(H_\lambda(k)\) is signed because
the cosine changes sign. The main question concerns the exact
cancellations in this oscillatory transform. Source positivity alone
cannot locate its zeros or prohibit them from meeting.

## 3. What the physical count realization contributes

The direct construction uses
\(\alpha=\gamma t=1/2-\lambda\) and \(h_*=H_{1/2}(0)>0\). Its
analytical signed traces obey
\[
 d_j=\frac{\alpha^j}{j!h_*}
       \int_0^\infty u^{2j}F_\lambda(u)\cos(ku)du
     =\frac{(-\alpha)^j}{j!h_*}H_\lambda^{(2j)}(k).
 \tag{3}
\]
The corresponding count probabilities replace the cosine by one and are
nonnegative. In particular \(d_0=H/h_*\) and
\(d_1=-\alpha H''/h_*\). Counts organize the same complete source
moments as direct Fourier differentiation. Products such as \(d_0d_1\)
are products of expectations, not two mutually exclusive outcomes of one
trial occurring together.

The conditional physical realization and its supplied loading/access
remain useful established work within their assessed scope. They do not
add an arithmetic constraint merely by writing the moments as counts.
Any estimating advantage needs a comparison against scalar analysis
allowed the same source data and correlations. Additional post-count
measurement access is not being assumed. See the [count section][count].

**Normalization clarification requested later in this chat, 9 November
2026.** The fixed quantity
\[
 h_*=H_{1/2}(0)=\int_0^\infty e^{u^2/2}\Phi(u)du>0
\]
is the initial half-line source mass. The full-line mass is \(2h_*\).
The choice \(k=0\) removes the oscillation because \(\cos(0u)=1\);
it gives the mass needed to normalize the source density. It does not
restrict the later observation to \(k=0\). The choice \(\lambda=1/2\)
comes from the initial slice selected for this realization,
\(\lambda(t)=1/2-\gamma t\), rather than from any necessity in the
definition of a normalization. In an analogous construction starting at
\(\lambda_0\), the fixed reference would be \(H_{\lambda_0}(0)\),
with attenuation toward \(\lambda\le\lambda_0\).

There are two normalizations to distinguish. The source-coordinate
conditional density at the current parameter is
\(F_\lambda(u)/(2H_\lambda(0))\) on the full real line. Its cosine
expectation is \(C(t,k)=H_\lambda(k)/H_\lambda(0)\), so
\(C(t,0)=1\). The no-count success probability and absolute contrast are
\[
 p_t=\frac{H_\lambda(0)}{h_*},\qquad
 d_0(t,k)=p_tC(t,k)=\frac{H_\lambda(k)}{h_*}.
\]
Thus \(d_0(t,0)=p_t\), which is generally below one after filtering.
The fixed reference keeps this success-frequency scale visible instead
of normalizing it away. Multiplication by \(h_*>0\) changes neither
zeros nor signs; likewise \(A_0/h_*^2\) and \(A_0\) have the same sign.
The star in \(h_*\) labels the initial reference and should not be
confused with the hypothetical event label in \(\lambda_*\). These
identities are the normalization in the [observation section][observation];
this clarification changes no construction or research status.

## 4. Why this particular signed quantity was chosen

Define
\[
 L_H(k)=(H'(k))^2-H(k)H''(k),\qquad
 A_0(\lambda,X,v)=\int_\mathbb R w_v(k-X)L_H(k)dk,
 \tag{4}
\]
where \(w_v\) is a normalized Gaussian of variance \(v>0\). In counts,
\[
 A_0/h_*^2=\int w_v[(d_0')^2+\alpha^{-1}d_0d_1].
 \tag{5}
\]
The positive square in this expression competes with a signed neighboring
count product. Separate positivity of the count probabilities does not
determine their competition.

Suppose hypothetically that
\(H_{\lambda_*}(k_*)=H_{\lambda_*}'(k_*)=0\),
\(a=H_{\lambda_*}''(k_*)\ne0\). Put
\(\varepsilon=\lambda_*-\lambda>0\), so that \(\varepsilon\) increases
in the forward physical heat direction. The leading local field is
\[
 H_{\lambda_*-\varepsilon}(k_*+y)
 \simeq a(y^2/2+\varepsilon).
 \tag{6}
\]
For the leading quadratic \(q(y)=a(y^2/2+\varepsilon)\),
\(L_q=a^2(y^2/2-\varepsilon)\). The Gaussian moment identity
\(\int w_v(y)y^2dy=v\) evaluates its integral exactly:
\[
 A_0(q;0,v)=a^2(v/2-\varepsilon).
 \tag{7}
\]
Choosing \(v=\varepsilon\) makes the leading signal negative:
\(-a^2\varepsilon/2\). The [operator theorem][operator] and Note09 turn
this explanation into a full-source estimate with an explicit error,
including the Gaussian exterior. It is not justified by the quadratic
approximation alone.

This explains the shrinking window: a fixed positive variance eventually
becomes too broad compared with an arbitrarily recent event. It also
explains the curvature cost: a small \(|a|\) gives a small signal.
We have no uniform positive lower bound on that unknown curvature.

**Exact averaging versus field approximation, clarification requested
9 November 2026.** The earlier wording “replaces y-squared by its mean”
was liable to suggest a pointwise or mean-field approximation. The step
in (7) is exact integration of a polynomial. It does not replace
\(\mathbb E[f(Y^2)]\) by \(f(\mathbb E[Y^2])\) for a nonlinear \(f\),
nor does it discard correlations in the products defining \(L_H\).
For example, \(Y\sim N(0,v)\) has
\(\mathbb E[Y^4]=3v^2\), whereas \((\mathbb E[Y^2])^2=v^2\).
In fact \(\operatorname{Var}(Y^2)=2v^2\); no small relative fluctuation
of \(Y^2\) is being assumed. Form the entire signed expression first,
then integrate it.

The actual approximation is the use of the leading quadratic for the
full field, and it needs a separate remainder estimate. Writing exactly
\(g(y)=H_{\lambda_*-\varepsilon}(k_*+y)=q(y)+R(y)\), expansion gives
\[
 (g')^2-gg''
 =a^2(y^2/2-\varepsilon)
 +2ayR'+(R')^2-qR''-aR-RR''.
\]
Thus the error is the Gaussian integral of every term after the leading
quadratic defect; none is assumed to vanish. The inherited proof uses
global third- and fourth-derivative bounds \(C,D\) on the real line and
the relevant time slab to give
\[
 \begin{aligned}
 |R|&\le C(|y|^3/6+\varepsilon|y|)+D\varepsilon^2/2,\\
 |R'|&\le C(y^2/2+\varepsilon),\qquad
 |R''|\le C|y|+D\varepsilon.
 \end{aligned}
\]
Integration of those bounds includes the whole Gaussian tail. With
\(v=\varepsilon\), it yields exactly
\(A_0=-a^2\varepsilon/2+\mathcal E\), with the explicit bound
\(E_1(\varepsilon;|a|,C,D)\) in [Note09][note09] (3), of order
\(\varepsilon^{3/2}\) at each fixed nondegenerate event. The negative
conclusion requires \(E_1\le a^2\varepsilon/4\); choosing
\(v=\varepsilon\) alone is not sufficient at an arbitrary finite time.
Small \(|a|\) can require a much smaller resolving scale, and no uniform
scale over unknown events is supplied.

The complete source-coordinate formula (9) is exact independently of
this local expansion. Its Gaussian factor follows directly from
\[
 \int_\mathbb R w_v(k-X)e^{ik(p+q)}dk
 =e^{iX(p+q)-v(p+q)^2/2}.
\]
Gaussian smoothing can still hide a narrow signal when its variance is
too large. That is a limitation of the selected observable and resolution
scale, distinct from an error in computing its Gaussian moments. These
clarifications preserve the existing theorem and its proof-author/internal
assessment qualifications; they add no new source-sign estimate.

The last pass declared double events in
\(\lambda_*\in[1/8,3/8]\), \(k_*\in[1/2,100]\), with
\(0<\varepsilon\le1/16\), and further required the explicit error to
be small enough relative to \(a^2\varepsilon\). These were boundaries
for the analytical test, not a numerical exclusion certificate or an
optimized range. Higher multiplicities and endpoints require additional
work; level zero is not a universal test for every nonreal zero pattern.

## 5. The desired conclusion versus an independent premise

Let \(b=|a|\). Once the full local error is at most
\(b^2\varepsilon/4\), the hypothetical event forces
\[
 A_0(\lambda_*-\varepsilon,k_*,\varepsilon)
 \le-\tfrac14b^2\varepsilon.
 \tag{8}
\]
An independently proved lower bound strictly above this value would
exclude the covered event. For example a lower bound
\(A_0\ge-b^2\varepsilon/8\), with all errors already included, would
contradict (8). This example states the desired quantitative consequence;
it is not a candidate theorem that has been proved or independently
motivated. No new global equivalent criterion is being proposed.

“Independent” means the estimate must be established from permitted
source information without assuming that the same collisions are absent,
that the relevant zeros are all real, or that this diagnostic already has
the wanted sign. It does not mean statistical independence, a second
physical system, or merely a separate model checking the work.

The missing reasoning must have the form:

1. A definite property of the complete theta source is proved or cited
   with applicable hypotheses.
2. That property bounds an actual signed correlation after every omitted
   contribution has been included or bounded.
3. The resulting error and signed margin improve a declared estimate or
   contradict the permitted event signal.

The first item is where a mathematical strategy must be selected.
Writing the third item's desired bound again in different notation does
not supply the first item. Exact arithmetic identity identifies the
function; it does not automatically estimate its oscillatory integral.

A successful next task need not exclude a collision outright. A weaker
intermediate lemma can qualify if it demonstrably improves a specified
signed enclosure, error comparison or other useful estimate against the
same-information baseline. The consumer and the improvement must be
identified; an exact identity with no additional estimate is not that gain.

## 6. Where the sign is located in source coordinates

**Notation clarification requested in this chat, 9 November 2026:**
\(F_\lambda(u)=e^{\lambda u^2}\Phi(u)\) is the unnormalized, reweighted
theta source; \(\Phi\) is the fixed canonical source and \(F_0=\Phi\).
For real \(\lambda\), it remains positive and even. Its argument is a
source coordinate such as \(u,p,q\), whereas \(H_\lambda(k)\) is its
cosine transform in the observation parameter \(k\). In the double
integral below,
\[
 F_\lambda(p)F_\lambda(q)
 =e^{\lambda(p^2+q^2)}\Phi(p)\Phi(q).
\]
There is no division by \(h_*\) hidden in this definition. The normalized
full-line source density would instead be
\(F_\lambda(u)/(2H_\lambda(0))\), since
\(\int_\mathbb R F_\lambda(u)du=2H_\lambda(0)\).

The same diagnostic has the complete source formula
\[
 A_0=\frac18\int_{\mathbb R^2}(p-q)^2F_\lambda(p)F_\lambda(q)
       e^{-v(p+q)^2/2}\cos(X(p+q))\,dp\,dq.
 \tag{9}
\]
Every factor apart from the cosine is nonnegative. The cosine has both
signs, and its weighted cancellation is precisely what must be controlled.
Folding the full line by reflection yields the paired half-line kernel
in Note09; both reflected terms and the complete theta double sum remain.
The folding identity alone does not eliminate the negative regions.

Two examples of a *type* of future input are useful for understanding the
decision, without selecting or launching either:

- A source relation might quantitatively pair a specified group of
  negative contributions with positive contributions. The actual proposal
  would have to name that pairing and prove a comparison of the complete
  theta weights, including any Jacobian and remainder. A drawing of a
  symmetric pairing or a new name for the total integral is insufficient.
- A finite calculation might bound a specified signed combination while
  keeping the terms correlated and enclosing every omitted index and
  radial tail. Its accepted output would be the resulting finite signed
  interval or a demonstrated cost gain. Merely acquiring more positive
  moments or obtaining a smaller absolute error does not give that value.

Both examples lie inside the existing signed-estimate question. Neither
is a promising candidate established by B03, and neither opens a new task
here. There is currently no particular weight-pairing lemma or favorable
finite signed value ready to hand to an executor.

## 7. What the last B03 pass ruled out

For the particular folded kernel, separate its positive and negative
contributions as \(A_0=\mathcal P-\mathcal N\), with both nonnegative.
Note09 exhibits an explicit rectangle where that kernel is negative and
uses positivity of the complete canonical source to show
\(\mathcal N\ge\mu>0\) uniformly on its declared compact parameter box.
The floor is deliberately crude and extremely small; it is not a practical
collision cutoff.

If the only retained information about \(\mathcal P\) is
\(\mathcal P\ge0\), even knowing \(\mathcal N\) exactly gives only
\(A_0\ge-\mathcal N\). Its loss divided by the event signal grows at
least as \(\mu/(b^2\varepsilon)\) as \(\varepsilon\downarrow0\).
That specific estimate cannot resolve the vanishing signal close enough
to an event. It can lose cancellation between two individually substantial
quantities even when their difference is tiny.

This is a limitation of that way of bounding the integral. It says
nothing negative about the actual sign of theta's \(A_0\), does not show
that every finite \(\varepsilon\) fails, and does not test every possible
arithmetic pairing or signed correlation. The record's phrase “B03
complete” means its bounded decision pass ended with this disposition,
not that the search for an independent signed mechanism was exhausted.

The secondary Green option was checked only against its entry condition:
the accepted count remainder is the same scalar omitted source kernel,
so substituting its existing absolute error into the known acquisition
theorem gives no new matched gain by itself. No newly correlated Green
remainder was constructed. This is likewise a missing-input conclusion,
not a general failure theorem for Green acquisition.

## 8. Why the counterexamples and error scales matter

The repository has smooth positive even sources with actual collisions.
The direct reflected control, for example, has
\(H^*_{1/4}(k)=cF(k)(1+\cos4k)\), and hence a nondegenerate double
at \(k=\pi/4\), with its positive curvature checked in the
[control proof][control-proof]. It obeys the generic heat/count identities
and the local Gaussian signal law. It fails the complete canonical theta
expansion. Other families fail different premises; the [control register][controls]
and Note09 section 4 state the precise distinctions and location limits.

An argument using only shared positivity and smoothness would wrongly
exclude that control. Conversely, observing that the control is not
theta is not enough: the proposed **quantitative bound** must actually
use a property the control fails. This is why identifying the source and
deriving a signed consequence are separate research steps.

Accuracy must also scale with the signal. If an approximant has uniform
value/first-derivative errors \(\eta_0,\eta_1\), and
\(|H|\le M_0, |H'|\le M_1\), the checked transfer is
\[
 |A_0(H)-A_0(\widehat H)|\le
 2\eta_1(2M_1+\eta_1)+\frac{\eta_0}{v}(2M_0+\eta_0).
 \tag{10}
\]
With \(v=\varepsilon\), the value error is amplified by
\(1/\varepsilon\). At a fixed nonzero curvature, making this allowance
negligible compared with \(b^2\varepsilon\) requires appropriately small
errors, for example \(\eta_0=o(b^2\varepsilon^2/M_0)\) and
\(\eta_1=o(b^2\varepsilon/M_1)\). Thus “more accurate” is not enough
without a stated scale and consumer. The complete finite inequality,
rather than just these order labels, decides an application.

## 9. Where the decision making resides

| Decision | What is already settled | What the next conceptual proposal must supply |
| --- | --- | --- |
| Scientific input | Complete canonical theta source and literal cosine are fixed | Name the particular source relation that yields additional signed information |
| Signed object and grouping | Gaussian level-zero diagnostic is the current double-event choice | Specify which terms must remain coupled and how their cancellation will be estimated |
| Consequence and domain | Local double-event signal, with a bounded initial class | State an actual finite margin/gain and its domain, or explicitly justify changing the target |
| Proof or computation | Existing complete moments, tails and interface errors are available | A definite analytical proof route or finite calculation with adequate error and curvature dependence |
| Controls and comparison | Known colliding sources and identical scalar baseline must be respected | Show the used bound distinguishes relevant controls and adds something beyond that baseline |

In the project workflow, these are B-stage mathematical decisions. E09
begins only when their result is a fixed claim with a method, inputs,
errors and completion test. E10 would then assess the returned claim.
The user need not invent the missing lemma: selecting and evaluating it
is the research work. The author's choices concern the desired scope,
acceptable kind of progress and amount of further exploration.

For a later conceptual continuation, the useful request is: **identify
one concrete source relation capable of controlling a specified signed
correlation, explain why it is expected to hold, and test its quantitative
consequence against the controls and the same-information direct method.**
It should be allowed to return a precise rejection. “Find something new”
by itself is too vague to be an execution specification.

The current pass remains closed at its bounded scope; this explanatory
note does not silently reset that scope. [Continuation10][continuation]
records model routing and the requirement to make a changed premise or
method explicit before dependent work. None of the present explanation
changes the proof-author checking status of Note09 or supplies independent
specialist review.

[results]: ../../../../../../result-summaries/README.md
[avoid]: ../../../../../../avoid/README.md
[controls]: ../../../../../../result-summaries/12_collision_controls_and_screening.md
[geometry]: ../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[theta]: ../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[a01]: ../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[progress]: ../../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md
[decision]: 04_TND_D_B03_R3_SIGNED_PREMISE_DECISION_20261109.md
[note09]: ../../notes/09_TND_D_B03_GAUSSIAN_INTERFACE_AND_SIGNED_KERNEL_SCREEN_20261109.md
[source]: ../../../03_operator_imaginary_time_evolution/manuscript/sections/02_source.tex
[count]: ../../manuscript/sections/05_count_calculus.tex
[observation]: ../../manuscript/sections/04_observation.tex
[operator]: ../../../03_operator_imaginary_time_evolution/manuscript/sections/16_gaussian_laguerre.tex
[control-proof]: ../../manuscript/sections/07_control.tex
[continuation]: ../../notes/10_TND_D_AFTER_B03_CONTINUATION_AND_MODEL_CHANGE_20261109.md
