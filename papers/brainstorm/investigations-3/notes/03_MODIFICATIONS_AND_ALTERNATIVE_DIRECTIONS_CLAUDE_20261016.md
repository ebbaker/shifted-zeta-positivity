# Modifications to the proposed directions, and alternatives

16 October 2026, America/New_York. Prepared for Edward Baker with LLM
assistance. Model: Claude Fable 5.1 (`claude-fable-5-1`), Claude Cowork,
reasoning effort max; the serving model may differ from the configured
identifier. This is a brainstorm, not a result: every statement below is
either a proposal, a reading of the repository, a literature check made
today, or a labelled floating-point computation. Nothing here is proved
about zeta, and nothing selects a research program.

Written at Edward's request as the additional brainstorm that the
[folder index](../README.md) anticipates, after reading the
[initial six-direction note](01_PATHS_FORWARD_AFTER_INVESTIGATIONS_2_CODEX_20261016.md),
the [follow-up after the results audit](02_ADDITIONS_AFTER_RESULTS_AUDIT_CODEX_20261016.md),
the [coverage review](../reviews/01_RESULT_SUMMARY_COVERAGE_INVESTIGATIONS_21_22_CODEX_20261016.md),
the [recorded conversation](../chat-histories/README.md),
[Review 19](../../../investigations-2/active/22_theta_manifold_geometry/reviews/19_PATHS_FORWARD_AFTER_THE_SECOND_ROUND_CLAUDE_20261015.md)
and [Review 20](../../../investigations-2/active/22_theta_manifold_geometry/reviews/20_ADDITIONAL_PATHS_FORWARD_ASSESSMENT_CODEX_20261016.md),
the [result summaries](../../../../result-summaries/README.md) and the
[patterns to avoid](../../../../avoid/README.md). The computations cited
below are in
[`numerics/check_brainstorm_modifications_claude_20261016.py`](../numerics/check_brainstorm_modifications_claude_20261016.py)
with their [record](../numerics/CHECK_BRAINSTORM_MODIFICATIONS_CLAUDE_20261016.json);
they are standard-library floating point, not certificates.

## 0. Summary

Codex asked for an opinion on which of its four starting structures
supports a new intermediate estimate, what arithmetic that estimate would
use, and which control separates it from the generic case. My answer, in
one paragraph: none of the four, as stated, supports an intermediate
estimate, and for three of them the reason can be made quantitative in a
page. Source-space rigidity (Section 2) meets an exponentially small
tolerance in the height; the Jensen compatibility question (Section 3) is
answered in the literature up to degree about \(10^{20}\) and is
RH-strength beyond; collective prime interactions (Section 4) look for a
term the explicit formula does not contain; cancellation/localization
(Section 8) is insensitive to collisions by construction, because an
impending collision carries negative mass \(O(s^{3/2})\) in a window of
energy \(O(1)\). The surrounding-zeros direction (Section 5) has a sharp
form, the attraction law, whose numbers are computed below and lose to
first-term dominance at every height. The canonical-system direction
(Section 6) is the transfer side the program already closed. The modular
direction (Section 7) has two definite calculations, both of which I
expect to end it.

What I would keep from the brainstorm is its question, "what mechanism
would be worth discovering", and I would answer it with the one place
where all of these directions converge once they are pushed to the scale
at which collisions are decided: the physical field at height \(x\) is a
beyond-all-orders remainder of size \(e^{-\pi x/8}\), its arithmetic
enters through the theta function at its natural boundary, and the only
known tool for that remainder is the Riemann–Siegel expansion and its heat
deformation. That is Review 19's lane (1) and Review 20's outer theorem,
reached from a different side. Section 9 proposes alternatives: a
coefficient-space experiment that settles the rigidity direction in a
week, a family (conductor) route to de Bruijn–Newman bounds that is a
theorem with a number and not RH-equivalent, and an explicit local zero
count for the heat-deformed function that every certificate method and
the attraction law both need. Section 10 gives the shortlist I would
bring to the discussion.

## 1. Three facts the directions keep running into

**1.1 The scale of the physical field.** With the repository's source
\(\Phi(u)=\sum_{n\ge1}\phi_n(u)\),
\(\phi_n(u)=e^{u}(2\pi^2n^4e^{8u}-3\pi n^2e^{4u})e^{-\pi n^2e^{4u}}\), and
\(H(t,x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du\), the complete even
source is analytic in the strip \(|\operatorname{Im}u|<\pi/8\) and no
wider: \(\operatorname{Re}e^{4u}>0\) is exactly that strip, and on its
boundary \(e^{-\pi n^2e^{4u}}=e^{-i\pi n^2e^{4\operatorname{Re}u}}\) is
the theta function on the real axis, its natural boundary. So
\(|H(t,x)|\) decays like \(e^{-\pi x/8}\) times powers, which matches
\(|\xi(\tfrac12+iT)|\) of size \(T^{7/4}e^{-\pi T/4}|\zeta(\tfrac12+iT)|\)
at \(T=x/2\). At the
height of the three-square control, \(x=44.13\), the field is
\(H(0,x)\approx9.7\cdot10^{-7}\) and \(H(\tfrac14,x)\approx1.0\cdot10^{-6}\);
at \(x=60\) it is \(1.9\cdot10^{-9}\) (record, sections A and B). Each
half-line term, by contrast, has an algebraic tail: the even extension of
a single \(\phi_n\) has a corner at \(u=0\), so
\[
\int_0^\infty\phi_n(u)\cos(xu)\,du=-\frac{\phi_n'(0)}{x^2}+\frac{\phi_n'''(0)}{x^4}-\cdots,
\]
and at \(x=44.13\) the first two terms are \(-1.06\cdot10^{-5}\) and
\(+1.16\cdot10^{-5}\), ten times the field they sum to. The tails cancel
because \(\phi_1'(0)=0.039499=-\phi_2'(0)\) to six digits (the third
term supplies the next \(8\cdot10^{-8}\)) and \(\Phi'(0)=0\) exactly
(reflection). The physical field is what is left
after every algebraic order cancels; it is governed by the strip width,
that is, by theta at its natural boundary. This is the content of 21 Note
56's control, which matches every algebraic primitive coefficient and
still collides, stated as a scale.

**1.2 Where the arithmetic of the primes sits.** By the scaling
\(\phi_n(u)=n^{-1/2}\phi_1(u+\tfrac12\log n)\), the \(n\)-th square term
is the first one translated by \(\tfrac12\log n\) and weighted by
\(n^{-1/2}\); its full-line transform is the Dirichlet term
\(n^{-1/2-ix/2}\) times the \(n=1\) transform, and the heat weight turns
the translation into the complex shift \(x\mapsto x+it\log n\) with the
factor \(e^{(t/4)\log^2n}\) (the same law as 22 §12's dilations and
Investigation 19's exact flow). On the half-line \(u\ge0\), however, every
term with \(n\ge2\) is doubly-exponentially small
(\(\phi_2(0)\approx9.7\cdot10^{-4}\), \(\phi_3(0)\approx8\cdot10^{-10}\)),
and the terms are not separately heat-integrable on the full line
(\(\phi_n(u)\sim-3\pi n^2e^{5u}\) as \(u\to-\infty\), against
\(e^{tu^2}\)). So there are two coefficient pictures and neither is the
one the brainstorm needs: the full-line comb carries the Dirichlet
coefficients but does not admit the heat flow termwise; the half-line comb
admits the flow but carries the arithmetic only in its endpoint jets and
in doubly-exponentially small corrections. The controls of Investigation
22 live in the second picture, which is why their weights look as they do:
the three-square control has raw weights
\((a_1,a_2,a_3)=(1,\,0.879,\,5.77\cdot10^4)\), the third compensating the
\(e^{-9\pi}\) suppression of \(\phi_3\) at the endpoint.

**1.3 The explicit formula is linear in the primes.** Weil's form is
\(\int(f\star\tilde f)\,d\mu\) with
\(\mu=(\text{archimedean})-\sum_n\Lambda(n)n^{-1/2}(\delta_{\log n}+\delta_{-\log n})\).
Only prime powers appear, singly; \(\Lambda(6)=0\). No term in any
explicit formula couples two primes. Interactions between primes arise
only when the test function is itself built from prime translates, and
then they are sampled values of \(\mu\) near \(\log(p/q)\): the Gram entry
of two prime translates with a bump of half-width \(\varepsilon\) is the
archimedean value minus \(\sum_n\Lambda(n)n^{-1/2}\) over prime powers
\(n\) with \(|\log(nq/p)|\le2\varepsilon\), that is, over primes \(p\)
within a factor \(e^{2\varepsilon}\) of a prime-power multiple of \(q\).
That is a prime-correlation statistic of Hardy–Littlewood type, which is
the object behind Montgomery's pair-correlation conjecture at
\(\alpha\ge1\), not an input available to a proof.

## 2. Direction 1, source-space rigidity, and the sharpened measurement question

**What is proposed.** Quantitative rigidity: if a weighted square source
nearly satisfies reflection on an interval, how closely are its
coefficients determined, which perturbations are invisible, and how do
they affect collisions. Note 02 §2 sharpens this to the conditioning of
finite reflection or elliptic measurements against the weighted recurrence
defects and the affine slope.

**Assessment.** The exact statement is settled and should be anchored in
the literature: 22 Note 05/02 (integer-square support plus Fourier
self-duality forces constant coefficients) is the conductor-one,
degree-one case of the classification of the extended Selberg class in
degree \(\le1\) by Kaczorowski and Perelli (Acta Math. 182, 1999; I did
not re-read the paper today and the project should, under
[avoid 16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md),
before citing it). The quantitative statement is where the direction
fails, for the reason in 1.1. In the half-line picture a defect \(\delta\)
in the first reflection endpoint \(\Phi'(0)\) produces a field tail
\(-\delta/x^2\), which exceeds the physical field as soon as
\(|\delta|>|H(x)|x^2\): the tolerance is \(0.079\) at \(x=30\),
\(1.9\cdot10^{-3}\) at \(x=44\), \(6.8\cdot10^{-6}\) at \(x=60\), and
decreases like \(x^2e^{-\pi x/8}\) (record, section B). Each higher
endpoint has the same exponential tolerance at the next order in
\(1/x^2\). So any stability modulus "on a prescribed finite spectral
domain \([0,X]\)" is of size \(e^{-\pi X/8}\), and is honest only in that
form. In the elliptic picture the conditioning is the same number in
different clothing: recovering \(a_n\) from \(\Theta_a(\cdot,\tau)\) on a
period divides by \(e^{-\pi n^2\operatorname{Im}\tau}\), so a measurement
of accuracy \(\eta\) resolves coefficients to index
\(\sqrt{\log(1/\eta)/(\pi\operatorname{Im}\tau)}\), and good conditioning
requires \(\operatorname{Im}\tau\to0\), which is the natural boundary
again. The three-square control is the exhibit: its half-line source is
within \(7\cdot10^{-5}\) of theta's in sup norm, seventy times the field
it collides against at \(x=44.13\) (record, section B). "Source-level
closeness" is not a measure in which collisions are decided, and no
finite set of Gaussian-type measurements can be.

**Modification.** Drop the quantitative-rigidity question and keep two
things: the exact theorem, cited against Kaczorowski–Perelli, and the
coefficient-space experiment of Section 9.1, which asks the direction's
real question (which coefficient changes create collisions) in the one
picture where the answer is \(O(1)\) and computable.

**Kill criterion** for anything that survives: a proposed stability
estimate must beat \(x^2e^{-\pi x/8}\) at every height it claims to cover,
or state that it does not.

## 3. Direction 2, constructive stable approximation, and the Jensen compatibility question

**What is proposed.** Build admissible models whose transforms have real
zeros by construction and converge to theta's; in the sharpened form, ask
at each degree whether the actual theta moment \(\gamma_d\) lies in the
interval of integration constants that keeps the Appell sequence
\(R_d=f(D)x^d\), \(R_d'=dR_{d-1}\), hyperbolic, and look for an inequality
explaining the margin.

**Assessment.** The sharpened question has a literature answer that I
checked today by web fetch of the arXiv text (to be verified against the
journal version before any citation): Griffin, Ono, Rolen, Thorner, Tripp
and Wagner, *Jensen polynomials for the Riemann xi function*
(arXiv:1910.01227), prove that \(J^{d,n}\) is hyperbolic for all
\(n\ge ce^{d/2}\) (Theorem 1.1), that if the zeros of \(\xi^{(m)}\) up to
height \(T\) lie on the line and \(d\le\lfloor T\rfloor/2\) then
\(J^{d,n}\) is hyperbolic for all \(n\ge m\) (Theorem 1.2), and hence,
from Platt's verification to \(3.06\cdot10^{10}\), that \(J^{d,n}\) is
hyperbolic for all \(d\le9.36\cdot10^{20}\) and \(n\ge0\) (Corollary 1.3);
Chasse had \(d\le2\cdot10^{17}\). Theorem 1.2 says what the "margin" at
finite degree is: the zeros up to height \(2d\). So the next theta
coefficient is admitted, with a margin that is a restatement of verified
zeros, up to degree \(10^{20}\), and uniformity in \(d\) beyond that is
Pólya's criterion, RH itself. The repository's own
[Note 01/07](../../../investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/07_REAL_PROJECTIVE_JETS_AND_JENSEN_HEAT_SURFACES_20261015.md)
already records that a uniform auxiliary-heat threshold is RH-equivalent;
the compatibility interval is the same fact at auxiliary time zero.

The unsharpened direction has two known kinds of "preservation theorem
that does substantive work". One is the multiplier-sequence kind
(Pólya–Schur, Lee–Yang, Borcea–Brändén): an operation preserves
hyperbolicity because the operation is itself generated by a
Laguerre–Pólya function, and it can only pass hyperbolicity along, never
create it; applied to theta it needs theta's hyperbolicity as input, which
is what
[Investigation 13's program](../../../investigations-2/active/13_stability_jensen_lee_yang/notes/INITIAL_RESEARCH_PROGRAM_20261013.md)
and the spin scout found. The other is the intersection-theoretic kind:
Weil's proof for curves is the Hodge index theorem on the square of the
curve, a positivity that bounds the prime side by the geometric side, and
its number-field analogue is the Connes–Consani archimedean positivity
that the program's bulk-realization line (summary 04, overview) was going
to build on. A constructive direction has to say which of the two it
means. If the first, it should stop; if the second, it is the paused bulk
program under a new name and should be reopened only with the specific new
input that the exclusion map asked for.

**Modification.** Replace the direction by a one-page classification of
proposed constructions into these two kinds, with Theorem 1.2 of the paper
above cited as the reason the finite-degree question is closed.

## 4. Direction 3, collective prime interactions

**What is proposed.** Mixed responses to adding two primes in the Sonin
metric, accumulated over structured groups, in search of a cancellation
invisible when each prime is bounded separately.

**Assessment.** By 1.3 there is no two-prime term to find in the explicit
formula; the mixed response in the compressed metric is a property of the
projection \(M^{-1}\), which is what Note 01 means by "generic operator
algebra will not provide that sign", and the program's own \(2\times2\)
control shows either sign generically (summary 07). Where prime pairs do
enter, through prepared sources, the entry is the von Mangoldt mass near
\(\log(p/q)\), a Hardy–Littlewood-type statistic. The averaged version of
that statistic is Montgomery's pair correlation, which under RH is
equivalent (Goldston–Montgomery) to the variance of primes in short
intervals; the project's own
[fixed-exponent equivalence](../../../../result-summaries/09_prime_variance_exponents.md)
is the diagonal of that correspondence. The "cancellation that disappears
when each prime is bounded separately" is, in the only place it exists,
the off-diagonal Hardy–Littlewood terms, and bounding them with a power
saving is a statement of Hardy–Littlewood type, independent of RH in both
directions as far as is known.

**Modification.** Before any computation, write down the statistic the
direction would need, in the form "the von Mangoldt measure within
\(\varepsilon\) of \(\log(p/q)\), summed with the prepared weights, is at
most the archimedean diagonal", and run the three model tests of the
11 October brainstorm (random multiplicative model; the control kernel;
restriction to the coherent rows). My prediction is that the statement
either fails on the random model or restates the single-probe
equivalence. If it does neither, it is a research question in prime
correlations worth stating on its own, and still not a route.

**Kill criterion.** The statistic is implied by the conclusion on the
rows where \(p/q\) is a prime power (the R3 trap), or no finite set of
primes gives it a sign (the fixed-place obstruction, Prop. 9.3 of the
Sonin manuscript, already says \(K>B\) for dilated sources at every
fixed \(S\)).

## 5. Direction 4, the surrounding zero configuration, and the attraction law

**What is proposed.** Isolate a close pair, separate its universal
interaction from the regularized field of the other zeros, and find a
compulsory signature of an impending collision beyond its neighbourhood.

**Assessment.** The separation Codex asks for is exact and short. With
\(H_t=-H_{xx}\), the zeros obey
\(\dot z_j=2\sum_{k\ne j}(z_j-z_k)^{-1}\) (the dynamics used by
Csordas–Smith–Varga and by Polymath: differentiating \(H(t,z_j(t))=0\)
gives \(\dot z_j=H_{xx}/H_x\) at \(z_j\), and writing \(H=(x-z_j)G\)
gives \(H_{xx}/H_x=2G'/G=2\sum_{k\ne j}(z_j-z_k)^{-1}\) there). For a complex zero
\(z=a+ib\) and another zero \(z_k=a_k+ib_k\) at horizontal distance
\(d_k\), the contribution of \(z_k\) and \(\bar z_k\) to \(\dot b\) is
\[
-\frac{2(b-b_k)}{d_k^2+(b-b_k)^2}-\frac{2(b+b_k)}{d_k^2+(b+b_k)^2},
\]
the conjugate of \(z\) itself giving \(-1/b\). Three consequences.
(i) For the zero of largest imaginary part every term is \(\le0\), so
\(\dot b\le-1/b\) and \(b(t)^2\le b_0^2-2t\): this is de Bruijn's
\(\Lambda\le b_0^2/2\) read off the dynamics, modulo the supremum over
infinitely many zeros that de Bruijn's own argument handles. (ii) A
lower zero can be pushed up by a higher one (take \(d_k=0\),
\(b_k>b\)), so nothing is forced on an individual zero; only the top
of the configuration is monotone. (iii) The "signature" on the real
zeros is a gap: a real zero at distance \(d\) is pushed away from
\(a\) at speed \(4d/(d^2+b^2)\), at most \(2/b\), so over the collision
time \(b^2/2\) the gap grows by about \(b\), which at the current
heights is about \(2b\) mean spacings. For \(b<\tfrac12\) this is less
than one spacing and is invisible to any average statistic, and gaps
of several spacings occur anyway. At time zero the configuration is a
complex pair with a gap, and the only thing that detects it is the
count of zeros on the line against the count in the strip, which is RH
verification. Codex's worry that a rare collision is compatible with
every available statistic is correct, and it is the whole story.

The sharp form of the direction is the attraction law: the surrounding
zeros accelerate the collision, and the question is whether their known
density improves de Bruijn's bound. For the top zero, each lower zero
and its conjugate contribute at least \(4b/(d_k^2+4b^2)\) (checked on a
grid in the record, equality at \(b_k=b\)), and the number of zeros within
horizontal distance \(D\) at height \(x=2T\) is at least
\((D/2\pi)L-2S_{\max}-2\), \(L=\log(x/4\pi)\), with
\(|S(T)|\le0.111\log T+0.275\log\log T+2.450\) (Trudgian, arXiv:1208.5846,
Theorem 1, fetched today). At \(T=3\cdot10^{12}\): \(L=26.9\),
\(S_{\max}=6.56\), the pull at \(b=1\) is at least \(1.13\) (window
\(D\approx7.6\)), comparable to the universal \(1/b\), and the
integrated collision time from \(b_0=1\) is \(0.332\), against de
Bruijn's \(0.5\) and the published \(0.2\). With the heuristic full
density, as if every zero near the pair were counted exactly, the pull
is \(L/2=13.4\) and the time \(0.060\); the difference is the
\(S(T)\) uncertainty, which is about thirteen zeros, while the pull is
carried by the zeros within one or two units of \(x\), that is, within
a few spacings. At \(T=10^{50}\) the law gives \(0.133\) against
first-term dominance's \(4.5/L=0.040\); the law decays like
\(\log L/L\), dominance like \(1/L\) (record, section C). So the
attraction law is a genuinely different lever, it reproduces de Bruijn
and improves it, and it loses to the Polymath mechanism at every height
unless the local count is known at the scale of a few spacings, which is
verification-strength information. It has one further gap, which is
also the one reusable thing in this direction: the count above is for
\(\xi\) at time zero, and the law needs the zeros of \(H_t\) for
\(0<t<\Lambda\), for which no explicit Riemann–von Mangoldt formula with
an \(S_t(T)\) bound is in the literature as far as I know (Section 9.3).

**Modification.** Record the attraction law and its numbers as the
direction's result, and close it. The Euler-factor controls are a
laboratory for the law, since all their zeros are known and their
\(\Lambda_{c,p}\) is certified above \(0.2\); predicting \(\Lambda_{c,p}\)
from the law would validate it as a tool, with no application to zeta.

## 6. Direction 5, canonical systems through their breakdown

**What is proposed.** Derive the \(\omega\)-evolution of the positive
objects on the safe side and classify the first failure as the shift
moves to the line.

**Assessment.** The safe side has no failure and the failure point is
known: the \(\omega\)-string is Stieltjes for \(\omega\ge\tfrac12\)
unconditionally, and the all-pass dichotomy of summary 05 says
\(\|V_{\omega,L}\|\le1\) for all \(L\) exactly when no zero is further
than \(\omega\) from the line. So the first breakdown is at
\(\omega_*=\sup_\rho|\operatorname{Re}\rho-\tfrac12|\), which is zero if
and only if RH, and an evolution law that "controls the first failure"
computes \(\omega_*\). The shift-energy identity
\(I-V^*V=2\int_0^\omega V_s^*Q_sV_s\,ds\) shows what the evolution is: the
contraction at \(\omega\) is the integrated positivity of the shifted
forms below \(\omega\), so the evolution supplies no input that the
positivity does not. This is the transfer side that the Loewner closure
and summary 05 ("the contraction margin carries essentially no arithmetic
information") already closed, and the breakdown signature of an off-line
zero is Paper 3's defect-depth law. The one open item there, uniform
detection of every defect, is a question about finite certificates, not a
mechanism.

**Modification.** Close, with the pointer. If the \(\omega\)-family is to
be revisited, it should be as the inverse-spectral object to publish
(Paper 2), not as a dynamical program.

## 7. Direction 6, the modular deformation, and the transverse question

**What is proposed.** Find a global evolution on the modular or Jacobi
space whose restriction to the physical path is Newman's, describe its
compatibility defect, and compute the variation at \(t=0\) including cusp
behaviour; in the sharpened form, keep the elliptic base variable in a
product of theta jets before restricting.

**Assessment.** Review 19 located the geometry: the Newman weight
\(e^{tu^2}\), \(u=\tfrac14\log y\), is \(e^{t\,d(iy,i)^2/16}\) along the
geodesic \(\operatorname{Re}\tau=0\). Four further facts settle the
questions Note 01 asks, and I would record them and move on.

1. *A canonical \(\Gamma\)-invariant extension exists.* On the geodesic
   with \(y\ge1\), \(\log y\) is also \(\log y_\Gamma(\tau)\), the
   invariant height \(y_\Gamma=\max_\gamma\operatorname{Im}\gamma\tau\).
   So \(m_t(\tau)=\exp(t(\log y_\Gamma(\tau))^2/16)\) is \(\Gamma\)-invariant,
   continuous, restricts to Newman's weight, and is the natural choice
   (it is the Siegel-set coordinate). Its compatibility defect is a
   crease: \(\log y_\Gamma=\log\operatorname{Im}\tau+2\max(0,-\log|\tau|)\)
   near the arc \(|\tau|=1\), so \(m_t\) is Lipschitz but not \(C^1\)
   across the \(\Gamma\)-orbit of the arc, with the jump in normal
   derivative proportional to \(\log\operatorname{Im}\tau\), which
   vanishes exactly at \(\tau=i\): the completion is smooth precisely
   where the physical geodesic crosses the arc. It adds nothing to the
   trace, which it was built from.
2. *No automorphic object restricts to the weight.* Any \(\Gamma\)-invariant
   eigenfunction, Eisenstein series or finite combination has at most
   polynomial growth \(y^\sigma\) along the cusp, while
   \(e^{t(\log y)^2/16}=y^{(t/16)\log y}\) is super-polynomial for every
   \(t>0\). The Poincaré-series completion
   \(\sum_{\gamma\in\Gamma_i\backslash\Gamma}e^{t\,d(\tau,\gamma i)^2/16}\)
   diverges for every \(t>0\), since the orbit count grows like
   \(e^{R}\) against terms \(e^{tR^2/16}\); the incomplete Eisenstein
   series with \(g_t(y)=e^{t(\log y)^2/16}\mathbf 1_{y\ge1}\) is a finite
   sum, but its Rankin–Selberg unfolding against any form of moderate
   growth with a nonzero constant term diverges, because
   \(\int_1^\infty g_t(y)y^{w-2}dy\) does, and against cusp forms it
   vanishes identically, as every incomplete Eisenstein series does. This
   is the cusp behaviour Note 01 proposed to compute: the deformation is
   incompatible with moderate growth, and only the functional equation,
   the stabilizer of the geodesic, survives, as Review 19 said.
3. *The flow is the heat flow in the spectral parameter.* Since
   \(\xi(s)=4\int_{\mathbb R}\Phi_e(u)e^{(2s-1)u}du\), one has
   \(H_t=\tfrac18\,e^{(t/4)\partial_s^2}\xi\) at \(s=\tfrac12+ix/2\); in the
   exponent \(w=(2s-1)/4\) of \(y=e^{4u}\) the operator is
   \(e^{(t/16)\partial_w^2}\). The corresponding operator on an Eisenstein
   series \(E(\tau,w)\) acts termwise as \(y^w\mapsto y^we^{(t/16)\log^2y}\),
   which is item 2's divergence, and on the constant term
   \(y^w+\varphi(w)y^{1-w}\) it flows the scattering matrix
   \(\varphi(w)=\xi^*(2w-1)/\xi^*(2w)\), a ratio, not \(\xi\).
   The variation at \(t=0\) is \(\tfrac14\partial_s^2\xi\), the heat
   equation itself; in the Eisenstein picture it is the second derivative
   in the spectral parameter, which is a known object and carries no
   constraint on \(\xi\) beyond the functional equation.
4. *The transverse question has a scale.* Note 02 §4 asks whether the
   full elliptic multiplier and the transverse commutators give an
   estimate on the collective expression that pairs square indices
   through their differences. By 1.1 that estimate would have to act at
   the \(e^{-\pi x/8}\) scale after every algebraic order cancels, and the
   elliptic multiplier under \(z\mapsto z+\tau\) is equivalent, after
   reindexing, to the coefficient recurrence \(a_{n+1}=a_n\) (Note 05/02
   §3), which is the identification of the source. The sharpened
   direction therefore asks the elliptic variable to do what Section 2
   shows the coefficients cannot do quantitatively.

**Modification.** Write items 1–3 as a short note, with the crease and the
divergence as the recorded compatibility defects, and close the direction
unless someone exhibits a \(\Gamma\)-invariant object of super-polynomial
cusp growth with an independent reason to exist. The one object this
analysis leaves on the table is the spectral heat flow of the scattering
matrix, which I would not pursue (its zeros and poles are both zeros of
\(\xi\)), but which is at least a definite thing.

## 8. The added direction, cancellation and localization of proved positivity

**What is proposed.** Use the proved centered averages, the sharp
translated bound \(\int\chi\mathcal L_j\ge-c_*a^2\int\chi h_j^2\) with
\(\chi=\operatorname{sech}(a(x-x_0))\), \(c_*=(3-2\sqrt2)/2\), the disk
identity, and the positive primitive \(J\) with
\(8H=\tfrac12+(2t-x^2-1)J+4txJ_x-4t^2J_{xx}\), to control a potentially
negative local region from a positive average, with some arithmetic
constraint improving the relation.

**Assessment.** Two scale facts decide this. First, the local collision
law: at time-to-event \(s\) the \(m=2\) germ is \(H=x^2+2s\), so
\(\mathcal L_0=2x^2-4s\) is negative only on \(|x|<\sqrt{2s}\), with
total negative mass of order \(s^{3/2}\), inside a window whose energy
\(\int\chi E\) is of order one. The averaged inequalities hold for the
general class, so they are satisfied by the colliding controls and they
are insensitive to a collision by construction: the negative mass of an
impending collision is invisible against the window energy at every
\(s>0\). No localization of an average, however sharp, can reach a
pointwise sign at a point where \(E\to0\); the controls say so, and the
scale says why. Second, the primitive. Equation (5) of 21 Note 52 gives
\(J=\tfrac1{2x^2}-\tfrac{1+6t}{2x^4}+O(x^{-6})\), with every coefficient
shared by the primitive-compatible control of Note 56; so \(8H\), which
is \(\tfrac12-(x^2+1)J\) at \(t=0\), is the beyond-all-orders remainder of
an asymptotic series in \(1/x^2\). The remainder beyond all orders of
such a series is governed by the complex singularities of the integrand,
here the strip boundary \(|\operatorname{Im}u|=\pi/8\) where \(\psi\)
meets theta's natural boundary; computing it is Siegel's derivation of the
Riemann–Siegel formula from the theta function near the real axis. A
"source-derived representation that estimates this difference while
preserving the cancellations" is the heat-deformed Riemann–Siegel
expansion, which Polymath used and which the repository's corrected
interface (summary 11) already sharpened by three to five orders of
magnitude. So this direction, pursued to the scale at which it would have
to work, is the effective outer theorem of Review 19 §1 and Review 20,
and the right place for its energy is there.

**Modification.** Reassign the averaged inequalities to the role they can
play: as boundary and wall estimates inside finite certificates (the
moving-wall flux and winding certificates of summary 13 bound boundary
contributions, and an unconditional averaged sign reduces the number of
enclosures), and fold the primitive remainder into the outer-theorem
lane, where the question becomes whether the resurgent structure of the
Riemann–Siegel series (Berry–Keating's late-term/early-term relation,
to be checked before import) sharpens the explicit remainder at complex
time. That question has a number attached and a kill criterion: it
either lowers the effective threshold \(\theta\) below Polymath's \(4.5\)
at a computable \(X_*\), or it does not.

## 9. Alternative directions

Each is stated so that it can fail, with a first bounded test and a kill
criterion. None claims a route to RH.

### 9.1 Coefficient-space collision distance (one week; settles Direction 1)

*Idea.* Ask Direction 1's question in the picture where the answer is
\(O(1)\): in the half-line comb class, with weights \((a_n)\) and
\(a_0=1\), define the collision distance
\(\sigma(t,x;N)=\min\{\|a-\mathbf 1\|_2:\ H_a(t,x)=\partial_xH_a(t,x)=0,\ a_n=1\text{ for }n>N\}\),
the minimal Euclidean change of the first \(N\) weights that creates a
collision at \((t,x)\); it is the minimum-norm solution of a \(2\times N\)
linear system with the term transforms as columns, and
\(\min_x\sigma(t,x;N)\) is the distance from theta to the collision
variety in that class. By 1.2 the columns for \(n\ge3\) are
doubly-exponentially small on the half-line, so the distance is carried
by the endpoint jets, and the three-square control's \(a_3=5.77\cdot10^4\)
is what it costs to use the third node. The experiment is to compute
\(\sigma\) on a grid of \((t,x)\) for \(N\le6\), for theta and for the
four controls of Reply 18 §3 (where the all-ones vector is replaced by the
control's weights), and to see whether theta's distance has any structure
that the controls' lack.

*Why it survives the rules.* It is exact linear algebra with a labelled
output, it uses the complete coefficients, and it is screened by
construction, since the controls are points of the variety.

*Kill criterion.* Theta's distance function is, up to scale, the
normalized energy \(|(H,H_x)|\) divided by the column norms, with no
structure beyond the field's own zeros (my prediction, in which case
Direction 1 is closed with a record); or it shows a feature at the
endpoint jets that the controls fail, in which case that feature is the
"additional coefficient coupling" Note 05/01 §6 asks for and should be
named.

### 9.2 A family route: conductor as height for de Bruijn–Newman bounds

*Idea.* For a primitive Dirichlet character of conductor \(q\), the
heat-deformed completed \(L\)-function \(H_{t,\chi}\) has the same
structure as \(H_t\), and in the first-term dominance condition the
conductor enters with the height, roughly through \(\log(qx/4\pi)\): a
large conductor puts the outer region at low height. The published
contract \(\Lambda\le t_0+y_0^2/2\) (verification, barrier, exterior
exclusion; Review 20) would then apply to characters whose low-lying
zeros are verified, and, more interestingly, to *almost all* characters
modulo \(q\): a complex zero of \(H_{t,\chi}\) at time \(t\) with
imaginary part \(b\) descends, by de Bruijn's strip argument applied to
the configuration's top, from a zero of \(L(s,\chi)\) with
\(\operatorname{Re}s\ge\tfrac12+\sqrt{t/2}\), that is, at \(t=0.2\), from
\(\operatorname{Re}s\ge0.816\), where family zero-density theorems
(Montgomery's large-sieve density estimate and its successors) are
strong. The target statement is "\(\Lambda_\chi\le t_0+y_0^2/2\) for all
but \(O(q^{1-\delta})\) characters modulo \(q\), for \(q\ge q_0(t_0)\)":
a theorem with a number, not RH-equivalent, and the first "almost all"
statement about de Bruijn–Newman constants that I know of. Dobner
(arXiv:2005.05142, fetched today) proved \(\Lambda_F\ge0\) for the whole
extended Selberg class without zero information, so the lower-bound side
of the family picture exists; the upper-bound side does not.

*What it needs.* (a) An effective outer theorem with explicit conductor
dependence, a rerun of Polymath's Section 8 analysis with \(q\), standard
and laborious; (b) a replacement for the per-character barrier, which is
the crux: either a mean-value argument showing the barrier segment is
zero-free for all but few \(\chi\), or a velocity bound on zeros that
keeps zeros above the exterior height from entering the box during
\([0,t_0]\), which needs control of \(H'_{t,\chi}/H_{t,\chi}\) along a
curve; (c) the family density estimate at \(\sigma=\tfrac12+\sqrt{t_0/2}\)
up to the exterior height, which is available. The strip-descent step in
(b)–(c) must be done for the top of the configuration, by item (i) of
Section 5, not zero by zero.

*First bounded test.* Write the dominance condition with the conductor
and tabulate, for \(t_0\in\{0.2,0.3\}\), the exterior height
\(X(t_0,q)\) and the height to which GRH is verified for all characters
modulo \(q\) in Platt's computations; find the range of \(q\), if any, in
which verification already covers the box. If that range is empty for
every \(t_0<\tfrac12\), the per-character version is dead and only the
almost-all version remains; then attempt (b) for one modulus.

*Kill criterion.* (b) cannot be done by mean values without a per-character
computation, and the velocity bound requires zero information above the
exterior height; or the exterior height with conductor is not lower than
without it (then the conductor does not trade for height and the idea is
empty).

### 9.3 An explicit local zero count for the heat-deformed function

*Idea.* Every certificate method in the repository (windings, wall
fluxes, barriers, the attraction law) needs, and none has, an explicit
formula \(N_t(T)=\frac T{2\pi}\log\frac T{2\pi e}+\frac78+S_t(T)+O(1/T)\)
for the zeros of \(H_t\) in the strip, uniformly for \(0\le t\le\tfrac12\),
with an explicit bound on \(S_t(T)\) of the Trudgian type. Ki, Kim and
Lee's proof that \(\Lambda<\tfrac12\) presumably contains the asymptotic;
the explicit version would be new as far as I know and is unconditional
analytic number theory of exactly the kind the program's Investigation 21
machinery (the complete coefficient sum, the carrier-to-phase error) was
built for. Its uses: it turns the attraction law of Section 5 into a
theorem (weaker than dominance, but a theorem with a different
mechanism), it provides the interior count that winding certificates
currently obtain by enclosure, and it is a prerequisite for 9.2(b).

*First bounded test.* Derive \(N_t(T)\) from the argument principle on the
rectangle using Polymath's bounds on \(H_t\) on vertical lines in the
outer region, and see whether the resulting \(S_t\) constant is within a
factor of two of Trudgian's at \(t=0\); if the outer-region hypothesis
\(tL\ge\theta\) is needed for the bound to hold at all, record that the
count is only available where dominance already gives reality, and stop.

*Kill criterion.* The one just stated.

### 9.4 Two calculations to record and close the modular direction

Items 1–3 of Section 7 are a day's work each to write properly: the
invariant-height completion with its crease, and the divergence of every
moderate-growth completion with the spectral-parameter form of the flow.
The deliverable is a closure note in the sense of the Loewner template
(closed with proofs rather than with an expectation), which the repository
has found more valuable than another lift. Kill criterion: none; it is
hygiene.

### 9.5 The outer theorem, with the beyond-all-orders remainder as its organizing principle

This is not new: it is Review 19's lane (1), Review 20's "structural
redesign problem", and Codex's own first choice, the sharp finite-sum
inequality from the Newman audit. What Section 8 adds is the reason the
brainstorm's most natural analytic direction lands here, and one concrete
question for it: whether the resurgent structure of the Riemann–Siegel
expansion gives an explicit remainder at complex time that is sharper
than the convex-dyadic and carrier-phase budgets (21 Notes 39 and 58, 22
outer Note 01), which still need \(L\) in the tens of millions where \(27\)
is required. The kill criterion is the one Review 16 set: if
\(X_*(0.15)\) exceeds \(10^{13}\) or the constants cannot be evaluated,
the lane belongs to verification height alone.

### 9.6 Regardless of the choice

The controls paper (Review 19 §3, Review 20's "concise controls
exposition"), with the screening theorem and the four-family table; and
the fixed-exponent equivalence of summary 09 as a standalone note, as the
11 October brainstorm recommended. Both are publishable negatives and
neither depends on the discussion.

## 10. The shortlist I would bring to the discussion

In order: 9.1 (one week, decisive for Direction 1, cheap); 9.5 with
Codex's finite-sum feasibility note as its first step (the only lane
whose output is a theorem with a number about zeta); 9.2 (the one new
non-RH-equivalent target, with its crux named); 9.3 (reusable, feeds two
of the others); 9.4 and 9.6 as hygiene. I would remove source-space
rigidity, constructive approximation, collective prime interactions and
cancellation/localization from the shortlist, for the reasons in
Sections 2, 3, 4 and 8, and keep the surrounding-zeros and canonical-system
directions closed with their records.

Two process remarks for the narrowing. First, two of the six directions
were settled today by literature checks of less than an hour
(Kaczorowski–Perelli for the exact rigidity;
Griffin–Ono–Rolen–Thorner–Tripp–Wagner for the Jensen compatibility),
which is
[avoid 16](../../../../avoid/16_unchecked_imports_and_novelty_claims.md)
in its positive form: a check before development, not after. I would make
that check a required line of any direction that enters the shortlist.
Second, Codex's three questions for this note (which structure supports an
estimate, what arithmetic it uses, which control separates it) are the
right gate, and I would add the one that decided most of the above: at
what scale does the estimate have to work, and is that scale
\(e^{-\pi x/8}\).

## Provenance and scope

Repository sources: the three brainstorm files and the chat archive in
this folder; Reviews 16–20 and Notes 01/07, 03/08, 05/01, 05/02 of
Investigation 22; Notes 47, 51, 52, 56 of Investigation 21; the Sonin
place-addition note and manuscript summary; the stability program of
Investigation 13; result summaries 03, 04, 05, 07, 09, 11, 12, 13, 14, 16;
the 11 October brainstorm. Literature statements were checked today by
web fetch of arXiv:1910.01227 (Jensen polynomials), arXiv:2005.05142
(Dobner), arXiv:1208.5846 (Trudgian) and the bibliographic reference to
Kaczorowski–Perelli I in Soundararajan's strong-multiplicity-one paper;
none was read in full, and each should be re-read before it is imported
into a manuscript. The Berry–Keating resurgence remark and the Ki–Kim–Lee
attribution are from memory and are flagged as such. The numerical
statements are floating-point computations in the companion script, with
composite Simpson quadrature on \([0,1.8]\), accurate to about
\(10^{-12}\) absolute at the heights used; they support remarks and prove
nothing. The attraction-law bound is heuristic in one named respect (the
time-zero count is applied at positive time). No file outside this folder
was modified; this note, its numerics and the index entries were added,
and nothing was committed.
