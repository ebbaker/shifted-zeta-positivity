# Review of root motion and differentiated saddle estimates

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**. This is a **same-assistant self-review**, not
an independent, cross-model, specialist or formal analytic review.
Repository checkpoint: `8cc883d2e022710975ab71a0da8591a5ad963d39`, with
the existing working-tree manuscript integration retained.

The manuscript and new program provide a consistent starting point for
this investigation. [Note 19][n19] now supplies the complete-root
remainders requested by HMC-01. [Note 20][n20] proves the proposed
fixed-label velocity asymptotics, with explicit sufficient error bounds.
These conclusions do not exclude a multiple zero; the additional signed
theta estimate and the moving geometric trace estimate remain open.

The [result index][results], [heat geometry][geometry], [control register][controls]
and [avoid index][avoid] govern the scope, particularly [reformulations][a01],
[shared premises][a02], [same-model review][a05] and [scoped conclusions][a07].

## 1. Manuscript and program assessment

I read the canonical [BW10 manuscript][manuscript], both new HMC files,
the root-continuation argument in Note 01, BW09's complete saddle proof,
the two 21 October discussion notes, and the relevant prior review and
control material. The review of the approximation part is a dependency
and scope review, including a bounded reread of Note 16 Section 11 and
Review 18. It is not a new verification of every estimate in Notes 15–18.

The manuscript correctly retains squared multiplicities in its
approximation infimum and in its heat-profile costs. Its fixed-taper
scaled-tail theorem and normalized complete-tail theorem remain
substantial internal analytic premises. The finite replay and repeated
same-model reviews do not independently validate them. Neither is used
in Notes 19–20, whose dependencies are the original source, its paired
product, and the explicitly bounded saddle law.

The HMC program correctly distinguishes a finite root cap, source-contour
exhaustion and ordinate exhaustion. Its proposed differentiated
asymptotics require a new argument: a location error tending to zero
cannot be differentiated on that basis alone. Note 20 supplies the
missing argument. The root-cap phase is still exactly pi for an
adjacent pair. A gap tending to zero at infinite time does not produce
a finite positive-time collision or a regular terminal physical jet.

The higher-dimensional representations summarized in Brainstorm 03
retain signed information, but this round has not established their
moving-domain trace bound. No new conclusion about all quaternionic or
octonionic contour methods is warranted. The next task is the specific
HMC-04 transport and trace estimate, with the original physical jet.

## 2. Uniform root tail and endpoint enclosure

RM1–RM4 were checked from the positive source rather than an assumed
zero-count asymptotic. The small source interval gives a time-uniform
positive normalization floor. The gamma bound is elementary and safely
overestimates the source. Jensen counts **both signs**, and the
Stieltjes tail therefore has no missing factor two. It yields
\(\mathcal B_T(R)=2C_T(\log R+2)/R\).

At an individual root, the mirror term is \(1/x_i\), not \(2/x_i\).
The remaining positive/negative pairs give
\(4x_i/(x_i^2-x_j^2)\). The gap sum is absolutely convergent,
whereas the center uses symmetric pairs. For \(R>2A\), the two tail
allowances are \(8g\mathcal B_T(R)\) and
\((8/3)A\mathcal B_T(R)\). Cutoff sums may jump as membership changes;
the note does not differentiate them.

The finite root-block cancellation was checked directly. Each internal
unordered pair contributes eight to the derivative of the sum of
squares, giving \(2K(2K-1)\), with a nonpositive complete exterior
contribution. This supplies the enclosure from one initial finite block,
or from the declared event height and rank. The resulting width bound
\(g^2\le4A^2(1-e^{-2t/A^2})\) uses the two mirror roots and is
strictly below \(8t\). Its constant depends on the chosen time horizon,
event height and root rank; it is not a uniform maximum-gap theorem.

## 3. Deflation and higher multiplicity

The identity for \(H=PD\) retains \(P_t+2\), both first-spatial
cross terms, and the two endpoint velocities. After substituting the
gap equation its coefficient is
\(-2c'(z-c)+g^2S_{\rm ext}\). Endpoint cancellation was checked
against the direct ratios \(H_{zz}/H_z\).

At an isolated exact double, the symmetric two-root factor and its
deflated unit are analytic in heat time. The coefficient
\(-16S_0\) in \(g^2=8t-16S_0t^2+O(t^3)\) follows from the
gap equation. For a pair inside a larger Hermite cluster, the deflated
factor still vanishes at the original event and the other cluster roots
give an order \(1/t\) exterior interaction. The note correctly keeps
these terms and does not reuse the double-isolation argument.

The normalization and classical local laws were checked against
[Polymath, Proposition 3.1](https://arxiv.org/html/1904.12438v2#S3).
[Rodgers–Tao's Theorem 4.16](https://arxiv.org/html/1801.05914#S4)
has the negative-time range stated in the program; the positive-time
proof here is supplied directly.

## 4. Differentiated saddle and all tails

DS5 differentiates the full source law including its normalization.
The linear observable term in the covariance is
\(-2z\sin z\operatorname{Var}(U-L)\); the moving scale contributes
\(+2z\sin z/\kappa\). **Dropping the moving-scale term loses a
cancellation at the full leading velocity scale.** DS6 bounds the
remaining cubic, quartic and mean errors explicitly.

The finite allowances DS7–DS10 were checked region by region:

- On \(|w|\le\kappa^{1/12}\), the cubic exponential remainder is
  at most \((4e/3)\kappa^{-1/4}\), and the complete higher-mode
  theta contribution is bounded by its stated geometric series.
- On the near-left and right regions, the Gaussian upper bound uses
  \(c=1/(4e)\); the finite condition on \(t/\kappa\) pays the
  positive quadratic term.
- The entire far-left region has an endpoint maximum and a separate
  exponentially small mass with its full moment power retained.
- The normalization lower bound is imposed before division. The signed
  first moment and the second moment are both controlled, so the
  variance bound includes the squared mean.

These give \(\widehat{\mathcal D}_Z=O_Z(\kappa^{-5/4})\).
The spatial root neighborhoods retain signs and a strictly positive
derivative floor; zero exclusion between them identifies the ranks.
Implicit differentiation then gives DS14 and the sufficient test DS15.
The error in each physical velocity is smaller than
\(L'/L^2=2/(\kappa L)\). No theta data or numerical onset estimate
is needed for the analytic conclusion.

## 5. Controls and actual verification

The finite exact-rational replay checks quadratic/cubic and even
multi-root slices, Hermite heat polynomials of degrees 2–8, the root-block
constant, endpoint removability, atomic Taylor coefficients and the
covariance decomposition. It passed; the [record][replay] identifies
the script and arithmetic. These finite identities do not test the
infinite-tail theorem or the asymptotic quantifiers.

The controls respond to different premises. Atomic and polynomial models
lack the theta saddle. Weighted-square and finite-prime controls are not
assigned an all-real heat slice. Euler and close-source endpoint controls
retain generic motion estimates; the latter's unchanged leading tail
also permits qualitative late-time shrinkage with source-specific
allowances. Their ordinary Dirichlet arithmetic fails. No one control
is assigned the union of another control's preserved properties.

The lesson is constructive: covariance cancellation supplies a velocity
estimate, but it does not distinguish an original multiple zero from a
nearby source's multiple endpoint. HMC-05 therefore remains open.

## 6. Status and next bounded step

HMC-01 is complete for the declared positive compact intervals.
HMC-02 is complete for fixed finite labels, including explicit finite
error inequalities; a numerical onset and uniformity in growing labels
are not supplied. HMC-03 has an explicit finite-interval width result;
turning-time and sharper maximum-gap estimates remain possible work.
HMC-07 has this round's self-review, not a final review of the whole program.

Next, fix one bounded product tube around the moving cap and compare
the complete signed Stokes flux to the planar physical observation.
The calculation must retain all faces, the tube thickness, moving
endpoints and the physical denominator \(H^2+H_x^2\). Source moment
bounds can pay a specified trace error; they must not be presented as
an arithmetic sign gain merely because they reconstruct the known cap
budget. No new endpoint exclusion or changed BW09 status is recorded.

[n19]: ../notes/19_COMPLETE_ROOT_MOTION_AND_FINITE_TIME_BOUNDS_20261021.md
[n20]: ../notes/20_DIFFERENTIATED_SADDLE_AND_EVENTUAL_GAP_SHRINKAGE_20261021.md
[manuscript]: ../manuscript/main.tex
[replay]: ../numerics/HMC_EXACT_ALGEBRA_REPLAY_20261021.json
[results]: ../../../../../../../result-summaries/README.md
[geometry]: ../../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
