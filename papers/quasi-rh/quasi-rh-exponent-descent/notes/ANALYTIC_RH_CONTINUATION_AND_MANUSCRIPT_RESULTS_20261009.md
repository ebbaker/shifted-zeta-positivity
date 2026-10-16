# Analytic continuation toward RH and results for the manuscript

9 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
The mathematical read-throughs are same-model internal checks, not independent
specialist validation. The [scoped review](../reviews/ANALYTIC_CONTINUATION_ASSESSMENT_REVIEW_20261009.md)
records the assessment and its dependencies.

The heat investigation has produced a coherent collection of reductions,
analytic comparison lemmas, effective error bounds, and obstruction theorems
that can support a manuscript. It has not produced a mechanism forcing the
Newman constant to zero. The recent collective-attraction work advances
positive-time analysis; its present gains are compatible with a positive
collision time. Improving its high-height threshold is therefore a bounded
Newman-bound task, rather than the decisive next step toward RH.

The recommended change of emphasis is to investigate the exclusion of
positive-time real collisions through the actual many-term arithmetic
collision vector. Retain collective attraction as an analytic tool and a
possible positive-time application. Keep the mixed covariance problem as the
best developed separate opportunity for a first arithmetic strip improvement;
the fixed-scale and short-family routes remain endpoint-capable conditional
alternatives with substantial unproved inputs.

## Results suitable for the manuscript

Here “include” means that a complete scoped derivation is available in the
linked notes. Imported theorems must receive attribution and their hypotheses
must remain visible. It does not mean that literature novelty has been
established. The heat results currently live in research notes; the existing
short-family and mixed-family manuscript sources do not contain this heat
package.

| Achieved result | Manuscript role | Qualification |
| --- | --- | --- |
| A positive zeta threshold forces a finite real multiple zero; exclusion of every positive-time real collision is equivalent to RH | Organizing reduction, with its compactness proof | Uniform localization is available only away from time zero; the equivalence is a reformulation, not a weaker substitute for RH. [Heat Note 1, Section 2](../newman_collisions/notes/1_NEWMAN_FLOW_AND_COLLISION_SCOUT_20261008.md) |
| An explicit positive, even, decreasing, rapidly decaying kernel has a positive threshold, despite only four nonreal time-zero zeros and arbitrarily narrow strips after scaling | Obstruction theorem explaining why generic kernel arguments cannot finish the proof | The example changes the function and preserves no zeta arithmetic. [Heat Note 1, Section 4](../newman_collisions/notes/1_NEWMAN_FLOW_AND_COLLISION_SCOUT_20261008.md) |
| Every fixed positive-half-line theta cutoff has an eventually negative collision Wronskian | Approximation obstruction and justification for retaining full modular cancellation | The defect belongs to the cutoff; it says nothing negative about the full zeta kernel. [Heat Note 2, Section 2](../newman_collisions/notes/2_ZETA_COLLISION_ARITHMETIC_20261008.md) |
| A holomorphic approximation with symmetric normalization, reflected errors, cutoff payment, and Cauchy derivative bounds | Main effective collision-exclusion interface | Polymath's value approximation is imported; derivative control is derived after bounding the whole complex disk. [Heat Note 3, Sections 1 to 5](../newman_collisions/notes/3_NORMALIZED_HEAT_COLLISION_CRITERION_20261008.md) |
| A sharp comparison of the exact attraction field with an off-zero logarithmic derivative at every probe above the maximal zero height | Strongest main-text collective-attraction proposition | Near the zero height it bounds the exact field \(E\), not the projected field \(G\). Sharpness concerns allowed pairwise geometry. [Heat Note 6, Section 2](../newman_collisions/notes/6_ANALYTIC_COLLECTIVE_ATTRACTION_AND_LANDING_20261009.md) |
| Uniform counts of all zeros give a global attraction floor and a state-dependent landing formula | Main proposition and landing corollary | The published counting error has an unprinted constant; the deduction gives no certified numerical endpoint from that constant alone. [Heat Note 6, Sections 3 and 4](../newman_collisions/notes/6_ANALYTIC_COLLECTIVE_ATTRACTION_AND_LANDING_20261009.md) |
| The effective probe \(L_{0.9}>6\), hence \(E>4\), for maximal zeros with \(x\ge10^{16}\), \(y\le0.2\), and \(t\in[0.2,0.3]\) | Worked analytic application showing that all errors can be paid without a grid | Its spatial threshold leaves the important lower sector unresolved. [Heat Note 7](../newman_collisions/notes/7_EFFECTIVE_COLLECTIVE_PROBE_AND_SPATIAL_COST_20261009.md) |
| A cutoff-crossing zero-free rectangle and a rectangle containing exactly one simple real zero at every time in \([0.2,0.3]\) | Reproducibility examples or appendix | These are local certificates, not global collision exclusion. [Heat Note 4](../newman_collisions/notes/4_CERTIFIED_COMPACT_CUTOFF_CROSSING_20261009.md), [Heat Note 5](../newman_collisions/notes/5_CERTIFIED_ZERO_BEARING_DERIVATIVE_CELL_20261009.md) |

The most useful collective-attraction statement is the following. At a simple
globally maximal nonreal zero \(z=x+iy\), put \(w=y^2\) and
\(L_\eta=-\operatorname{Im}(H_t'/H_t)(x+i\eta)\). For every \(\eta>y\),

\[
 E_t(z)\ge
 \min\!\left\{1,\frac{\eta^2-w}{4w}\right\}
 \left(\frac{L_\eta}{\eta}-\frac{2}{\eta^2-w}\right).
 \tag{1}
\]

Together with \(w'=-2-4wE_t(z)\), the nearer-probe range
\(y<\eta\le\sqrt5\,y\) gives
\(w'\le-(\eta^2-w)L_\eta/\eta\). The proof in Note 6 pays the own
conjugate exactly and compares the remaining conjugate-pair kernels.
The existing projected-field framework of
[Planat, Proposition 2.3](https://arxiv.org/html/2609.37164v2#S2.Thmproposition3)
should be acknowledged; that preprint's numerical certificates are not inputs
here. The exact near-probe extension is the candidate contribution to review for
novelty, rather than the general idea of collective attraction.

The global count deduction has the form

\[
 E_t(z)\ge\frac{n}{B^2+4w},
 \qquad
 T(w_0)=\int_0^{w_0}\frac{du}{2+4un/(B^2+4u)}<\frac{w_0}{2},
 \tag{2}
\]

with \(n,B\) explicitly defined in terms of the published counting constant.
It includes the maximum-envelope argument, switches of the maximizing root,
multiple-root events, and an epsilon start when the initial time is zero.
Those continuation details belong with the proposition.

The reflected-pair patch in Note 7 gives a gain of about \(4\cdot10^{-36}\)
over the chosen historical \(0.22\) baseline. This should appear, if at all,
as a limitation remark explaining the cost of spatial coverage. The
conditional sector endpoint near \(0.217352\) must not become a global
Newman claim: the needed control of all maximizing zeros has not been proved.
Neither number is an appropriate headline result.

A sensible heat manuscript would develop the collision reduction and generic
obstructions first, then the normalized arithmetic interface, the exact
attraction comparison, the global landing theorem, and finally the worked
examples. A paper presenting these as tools and limitations of a proposed
descent program is supported by the present record. A paper claiming descent
to zero is not.

The broader investigation also has manuscript material in the conditional
short-family extraction, exact signed mixed kernels, paid conductor sectors,
and actual coherent and deletion-mode obstructions. Those results retain
their stated family and detector hypotheses. The full short moment, central
mixed count, and new arithmetic strip improvement remain open; conditional
payoff formulas are not achieved zero-free boundaries.

## What collective attraction has accomplished and what it cannot yet do

An actual canopy \(W(t_0)\le w_0\), where \(W\) is the maximal squared
imaginary height, and a field floor valid at every maximizer give a shorter
landing duration. This is genuine analytic progress. The effective result
in Note 7 verifies the full approximation-to-field passage, while Note 6
gives global coverage without assuming that the other zeros are real.

The present field floors remain finite as \(w\downarrow0\). For a fixed
positive floor \(h\),

\[
 T_h(w)=\frac{\log(1+2hw)}{4h}
       =\frac w2-\frac h2w^2+O(w^3).
 \tag{3}
\]

The count floor has the same quadratic order of gain. At a hypothetical
ordinary double collision at \(T>0\), however,

\[
 w(t)=2(T-t)+O((T-t)^2).
 \tag{4}
\]

Thus \(t+T_h(w(t))\to T\), rather than zero. A bounded external field is
consistent with the collision normal form. Strictly better positive
endpoints, even repeatedly obtained, need not eliminate a positive limit.
Moreover, a bound on \(\Lambda\) cannot be run backward to create a new
earlier-time canopy.

The current approach is moving forward as positive-time analysis. It has
not demonstrated progress through this endpoint obstruction. A further
finite threshold improvement would strengthen an application of the tools,
but it would not supply the missing reason that a positive collision is
impossible.

One optional bounded continuation is the recorded target \(E\ge1\) for
\(x\ge X_P=6\cdot10^{10}+83951.5\), \(0<y\le1/5\), and
\(t\in[1/5,11/50]\), using an off-zero probe at \(99/100\), radius
\(1/200\), a finite head, and logarithmic integral tails. A material global
gain additionally needs a stronger lower-sector estimate, or a smaller left
envelope and a barrier continuing after \(1/5\). The published barrier ends
at that time. This task should remain optional unless a positive-time bound
is itself the desired outcome.

## Excluding positive-time collisions directly

The exact endpoint target is

\[
 H_t(x)=H_t'(x)=0
 \quad\hbox{has no solution with }t>0,\ x\in\mathbb R.
 \tag{5}
\]

Heat Note 1 proves why a positive threshold must produce a finite real
multiple root: approach the threshold from below with nonreal zeros,
use uniform positive-time localization, pass to a limit, and rule out a
simple limiting zero by conjugation and the implicit-function theorem.
The imported localization and local Hermite splitting are
[Polymath, Theorem 1.5 and Proposition 3.1](https://arxiv.org/html/1904.12438#S1.Thmtheorem5).
Together with the threshold property and
[Rodgers and Tao's nonnegativity theorem](https://arxiv.org/abs/1801.05914),
this makes (5) equivalent to RH. It is the more direct logical route to zero,
but not an easier theorem by equivalence alone.

The available normalization \(Q_t=H_t/A_t\), with \(A_t\ne0\), preserves
common zeros. A fixed-cutoff approximant \(F\) satisfies
\(|Q-F|\le\epsilon_0\) and \(|Q'-F'|\le\epsilon_1\), with both errors
proved on a complex neighborhood. Thus the natural target is a lower bound
for the genuine collision vector, or for the approximating vector large
enough to dominate those errors. It need only exclude simultaneous
vanishing, rather than force a Wronskian to be positive everywhere.

Generic transversality does not exclude a collision. At an exact double
root the heat equation already gives

\[
 \det\frac{\partial(H,H')}{\partial(x,t)}
 =(H'')^2>0.
 \tag{6}
\]

Ordinary collisions are therefore isolated transverse intersections.
Proving that they are transverse, or that every collision is double,
would still permit a positive threshold. Higher multiplicities must also
remain within the exclusion target.

### An error-paid amplitude and phase criterion

On the real axis the exact fixed-cutoff representation is

\[
 F(x)=2\operatorname{Re}\!\left(e^{i\theta(x)}P(x)\right).
 \tag{7}
\]

Where \(P\ne0\), write \(m=|P|\) and
\(\phi=\theta+\arg P\). Then
\(F=2m\cos\phi\) and \(F'=2m'\cos\phi-2m\phi'\sin\phi\).
Suppose on the region under study that

\[
 m\ge m_0>\epsilon_0/2,\qquad |m'|\le m_1,\qquad
 |\phi'|\ge\Omega>0.
\]

The explicit sufficient condition

\[
 2\Omega\sqrt{m_0^2-\epsilon_0^2/4}
 -\frac{m_1}{m_0}\epsilon_0>\epsilon_1
 \tag{8}
\]

excludes common zeros of \(Q,Q'\). Indeed, at a candidate common zero,
\(|F|\le\epsilon_0\) bounds its cosine, so
\(m|\sin\phi|\ge\sqrt{m^2-\epsilon_0^2/4}\).
The amplitude derivative term has modulus at most
\((m_1/m_0)\epsilon_0\); the phase term then exceeds the allowed
derivative error. This proves the criterion. The phase derivative is
\(\phi'=\theta'+\operatorname{Im}(P'/P)\); no choice of an absolute
phase branch enters it.

A simpler sufficient version uses \(|P|\ge p_0\),
\(|P'|\le p_1\), and \(|\theta'|\ge\omega_0>0\):

\[
 \epsilon_0<2p_0,\qquad
 2\omega_0\sqrt{p_0^2-\epsilon_0^2/4}>2p_1+\epsilon_1.
 \tag{9}
\]

At a candidate zero, the derivative of (7) has a carrier contribution
of modulus at least the left side, minus \(2p_1\).
For \(P=1\), (9) recovers Note 3's leading-pair test.
Equations (8) and (9) are conditional comparison lemmas; no new lower
bound for the actual many-term amplitude or phase speed has been proved.
Demanding \(P\ne0\) globally can be stronger than the necessary collision
statement. A useful argument may instead exploit the two candidate
collision equations together.

### The next analytic task and its stopping condition

The existing explicit tail theorem excludes real collisions for
\(t\in[\varepsilon,1/2]\), \(|x|\ge e^{64/\varepsilon}\).
Its role is localization. Decreasing the constant 64 leaves the same
shrinking-time gap.

The next attempt should retain a genuinely many-term sum and study
\(\kappa=t\log(x/(4\pi))\) in a fixed interval inside \((0,4)\),
initially one chosen interval such as \([1,2]\).
The requested output is an analytic, error-paid collision-vector estimate
uniform as \(t\downarrow0\), or a precise obstruction to a proposed signed
amplitude or phase estimate. It is not a grid of times or zeros, and proving
one such interval would still leave the other scaling regimes and low
heights to control.

An elementary asymptotic diagnostic gives a reason to require signed
arithmetic here. It concerns the approximant's coefficients only, rather
than an error-paid exclusion theorem for \(H_t\). With
\(x=4\pi e^{\kappa/t}\), the real-axis coefficient modulus near the
natural cutoff \(N\sim e^{\kappa/(2t)}\) has last-block absolute mass on
\([N/2,N]\) of order

\[
 \exp\!\left(\frac{\kappa(4-\kappa)}{16t}\right)
 \quad(0<\kappa<4).
 \tag{10}
\]

To see the exponent, use
\(\log|p_n|=-(1/2+\kappa/4)\log n+(t/4)\log^2n+o(1)\)
and \(\log n=\kappa/(2t)+O(1)\), then multiply by the block length.
The small errors in the real \(\alpha\) formula are exponentially
negligible in this scaling. The comparison is uniform on compact
\(\kappa\) intervals inside \((0,4)\). At \(\kappa=4\), fixed logarithmic blocks
below the cutoff retain a non-small mass rather than a vanishing tail.
Thus a triangle estimate treating this as a small perturbation of the
first term cannot handle the new regime.

A finite Dirichlet mollifier with constant coefficient one, whose indices
use only a fixed finite set of primes, cannot remove this obstruction by
coefficient-wise absolute estimation. In its convolution with \(P\),
coefficients at integers coprime to those primes are unchanged, and those
integers have positive density in the last block.
It may improve constants elsewhere, but crossing this obstruction requires
genuine phase cancellation or use of the joint collision conditions.
This diagnostic concerns that particular coefficient-wise absolute method,
not every possible mollifier or collision proof.

Stop an attempted proof if it only improves a large-\(\kappa\) constant,
uses kernel positivity alone, demands positivity of a fixed theta-cutoff
Wronskian, or replaces the entire signed tail by absolute values in the
regime (10). Those outputs do not address the endpoint problem.

## Other analytic approaches with a concrete repository basis

### Correlated translated probes and derivative information

Two shifted probes can retain the relative phase of the same arithmetic
terms, instead of taking independent worst cases at each point. The
[translated-probe and head-pair comparison](https://arxiv.org/html/2609.37164v2#S8)
in the recent collective-contraction preprint is a useful source of this
tool idea; its computed endpoints are not adopted here.

A bounded analytic scout would derive a joint comparison that improves
the margin in (8), or directly constrains the candidate collision vector,
on the same shrinking-time scaling family. It must retain all adverse
pair terms and physical errors. Higher derivative information may help,
but merely proving \(H''\ne0\) at a candidate double root is already
consistent with (6). This is a possible tool within the collision route,
not an established third route to zero. A new joint inequality would
justify pursuing it; another optimized numerical probe grid would not.

### Fixed-scale contraction of the actual prime variance

[Fixed-scale Note 1](../fixed_scale_descent/notes/1_FIXED_SCALE_DESCENT_CRITERION_20261008.md)
proves that a recurrence for each positive admissible exponent,

\[
 E_\delta(X)\le qE_\delta(X/b)+CX^{-\eta},
 \qquad b>1,\quad 0<q<1,\quad\eta>0,
 \tag{11}
\]

forces a strict power improvement. Applied at the attained optimal exponent,
such a theorem would rule out a positive optimum and establish the
conditional quasi-RH-to-RH implication. Constants need not be uniform as
\(\delta\downarrow0\). The attainment and prime-variance detection theorem
are inherited project inputs.

Here \(E_\delta(X)=X^{-2-\delta}\int_X^{2X}|V_g(v)|^2\,dv\)
for the inherited actual prime response. Define
\(F_X(u)=X^{-(1+\delta)/2}V_g(Xu)\), \(1\le u\le2\), and
\(D_X=F_X-F_{X/b}\). Then \(\|F_X\|^2=E_\delta(X)\), and the
exact difference is
\(2\operatorname{Re}\langle D_X,F_{X/b}\rangle+\|D_X\|^2\).

This is a genuine endpoint criterion with no known arithmetic mechanism
meeting it. [Fixed-scale Note 4](../fixed_scale_descent/notes/4_COMPLETE_FIXED_DELAY_AND_COVARIANCE_OBSTRUCTION_20261009.md)
analyzes the corresponding scalar-detector delay, retaining its complete
arithmetic domain corrections. It shows why negative covariance alone
fails: a persistent boundary mode has a squared delay defect that cancels
the apparent gain. The next acceptable estimate for either formulation must
bound the whole net energy change by a negative fixed fraction of the
smaller-scale energy plus a power remainder, including every boundary and
cross term. A logarithmic saving or an isolated negative cross term is a
stopping condition, not descent.

Retain this route as a benchmark for what a zeta-only endpoint mechanism
must accomplish. Resume substantial work only when a specific arithmetic
decomposition passes those complete-energy tests.

### Signed compensation in short families

The [short-family manuscript](../short_families/short_family_reductions.tex)
proves the extraction
\(\beta_{\rm out}=(1+a)/2+5h/12\) from its stated short moment
and detecting profile class. A hierarchy with \(a,h\to0\) can approach
\(1/2\); one fixed \(h>0\) cannot. Such a hierarchy is a new strong
arithmetic hypothesis, not a consequence of zeta-only quasi-RH.

At the displayed \(h=a=2/5\) target, the desired energy is below the
generic physical-row envelope by \(4/15\) in exponent.
The coherent cofactor packets and
[Short Note 29's deletion variance](../short_families/notes/29_DELETION_MODE_COVARIANCE_AND_FULL_RESPONSE_LEDGER_20261009.md)
show that scalar mean subtraction does not remove the obstruction.
For one prime of norm \(q\), the leading deletion coefficient
\((q-1)/q^4\) remains positive.

The bounded useful task is the exact single-prime conditional-mean contrast
with power-accurate compensation from the complete complementary response.
The required relative accuracy is \(D^{-2/15+\epsilon/2}\), up to
logarithms, in the displayed variance budget.
Its within-cell variance and remaining squarefree energy must also be paid.
Matching only a continuum leading coefficient is insufficient. This route
deserves renewed priority if an actual cross-product compensation estimate
appears; the present record supplies the obstruction and the required
precision, rather than that estimate.

### Gated mixed covariance for a first arithmetic improvement

[Mixed Note 32](../mixed_character_families/notes/32_GATED_LARGE_VALUES_AND_HIGH_RATIO_COVARIANCE_20261009.md)
reduces the first-gain task to a particular signed high-ratio two-row
covariance on the actual gate and response phases. Equal-character and
low-ratio-conductor sectors have paid conditional bounds. The remaining
aggregate retains the original inverse weights, physical zeros, and
witness profiles.

This is the strongest developed separate arithmetic target for a first
local strip improvement. Available absolute estimates, even an optimistic
square-root entry bound, miss its required scale. A useful next result
must prove a strict selected mass or count gain for the actual signed
aggregate and the needed derivative-weight family.
The current architecture has no proved iteration to the RH endpoint.
Further positive interpolation or removal of already-controlled sectors
would not close its central gap.

The integer quadratic lift remains lower priority: its exact reduction is
useful, but its available sieve has a quantified saving deficit and asks
for a wider family conclusion. Neither generic positivity nor a spectral
or zero-gap argument is currently backed by a zeta-specific invariant in
this repository. They should become active directions only when such an
invariant or signed estimate can be stated and tested.

## Recommended continuation

1. Consolidate the achieved heat propositions and obstructions into a
   manuscript outline, with the effective and computational examples in
   an appendix. Keep the modest historical endpoint in its proper role.
2. Make one bounded analytic attempt on the many-term collision vector
   in a shrinking-time scaling regime. Use (8) or a weaker criterion
   conditioned on simultaneous small value and derivative, and retain
   every normalized remainder and cutoff contribution.
3. Judge that attempt by a uniform signed estimate or a proved obstruction
   that identifies the missing arithmetic. Another smaller eventual
   cutoff, a transverse-collision lemma, or a finite cover does not meet
   this completion condition.
4. Keep collective attraction available for one optional positive-time
   application near the published barrier. Do not let repeated threshold
   optimization substitute for the endpoint mechanism.
5. In parallel arithmetic work, give the actual gated mixed covariance
   priority for a first improved strip. Promote short-family compensation
   or fixed-scale contraction only on proof-producing checkpoints, not
   on additional equivalent reformulations.

The next step toward zero is therefore a different estimate, not simply
a stronger version of the existing finite attraction floor. The achieved
tools remain useful manuscript results while that estimate is sought.
