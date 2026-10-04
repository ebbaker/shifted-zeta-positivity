# Project overview: a first fixed prime-variance exponent below one

4 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed and are not inferred.
Research planning and internal review; no new global exponent is proved.

Subsequent [preliminary work across all ten programs](PROGRAM_PREFLIGHT_ASSESSMENT_20261004.md)
now supplies concrete derivations, source gates and bounded checks. It
retains programs 01, 02 and 03 as the shortlist and targets the centered
Vaughan block covariance in program 01 for the next investigation.

The subsequent [one-sided arithmetic investigation](programs/01_signed_arithmetic_covariance/ONE_SIDED_ARITHMETIC_ATTEMPT_20261004.md)
reduces that target to a signed prime-discrepancy correlation, after
power-small density and boundary elimination. Actual smooth coefficients
defeat literal sign deletion. The required one-sided fixed-power bound
remains open; the linked note records the precise next estimate.


The best-prepared route is a genuinely signed estimate for the retained
Möbius cofactor response or the correctly centered Vaughan response. The
strongest parallel route is the Sonin source-loss program with a fixed
exponential allowance below its baseline rate. Signed prime-pair dispersion
is the main alternative arithmetic viewpoint. Several older assessments
asked for RH-scale estimates; their targets should be relaxed for this
first milestone.

The ranking measures technical readiness, specificity of the missing lemma,
and the usefulness of a bounded first investigation. It does not predict a
breakthrough. Every successful branch would establish a new constant-width
zero-free strip at all heights. No reviewed argument or available input
currently supplies that conclusion. “New program” means not developed in
the inspected notes of these two investigations, not mathematical novelty
or exhaustive literature coverage.

## The common target

Keep the manuscript's fixed normalized odd probe \(g\), supported in
\([-1/4,1/4]\), and set

\[
A=e^{-1/4},\quad B=e^{1/4},\quad w(t)=t^{-1/2}g(-\log t),\qquad
V_g(x)=\sum_n\Lambda(n)w(n/x),\qquad
\mathcal V_g(X)=\int_X^{2X}|V_g(x)|^2\,dx.
\]

The already proved equivalence is

\[
\mathcal V_g(X)=O(X^{2+\delta})
\quad\Longleftrightarrow\quad
\Re\rho\leq(1+\delta)/2\quad\text{for every nontrivial zero }\rho,
\qquad 0\leq\delta\leq1.
\]

Choose **one fixed** \(0<\kappa\leq1\), put \(\delta=1-\kappa\),
and seek \(\mathcal V_g(X)\ll X^{3-\kappa}\) for every sufficiently
large **real** \(X\). The reflected left boundary follows from the
functional equation. A tiny fixed saving counts; a saving tending to zero
does not. Constants and thresholds may depend on the fixed exponent.

There is useful endpoint flexibility: a global estimate
\(X^{3-\kappa+o(1)}\), even with logarithmic or other subpower losses,
for the prime response or a response differing by \(O(X)\) in shell norm
implies the exact endpoint \(O(X^{3-\kappa})\). Apply the equivalence
for every slightly larger exponent, intersect the closed zero strips, and
apply the converse. No uniform constants are needed. This conditional
result supersedes the older parent notes' endpoint caveat; it does not
supply a positive \(\kappa\).

By contrast, \(X^3\exp[-c(\log X)^a]\), \(0<a<1\), and
\(X^3/(\log X)^C\) retain exponent three. Known shrinking zero-free
regions, PNT/Mertens envelopes and logarithmic arithmetic savings have
already been tested. Zero-density bounds permit isolated forbidden zeros.
Finite verification extends finite variance ranges, with height-dependent
tails, but does not settle this global target. See [Initial investigation](INITIAL_DELTA_INVESTIGATION_20261004.md), [signed Mellin continuation](SIGNED_MELLIN_CONTINUATION_20261004.md),
[Type II source audit](BILINEAR_INPUT_SOURCE_AUDIT_20261004.md), and [parent baseline/exponent budget](../../investigations/sonin-critical-boundary/notes/subpower-milestones/01_baseline_and_exponent_budget_20261003.md).

## Review of the existing programs

The review covered the prime-variance notes and reviews, the Sonin indexes,
and the core finite-Euler, translated-probe, selective-loss, prime-pair,
short-interval and obstruction notes/reviews. This is a targeted synthesis,
not a claim that every historical file was independently reproved. The
[internal planning review](../reviews/PROJECT_OVERVIEW_REVIEW_20261004.md) records its check scope.

| Existing program | Established result | Current implication |
| --- | --- | --- |
| Fixed-probe exponent theorem | Detects every forbidden off-critical zero; both closed-boundary directions proved | Common transfer theorem, not the missing arithmetic estimate |
| Möbius/Vaughan reductions | Large sectors discarded with quadratic or subquadratic error; exact signed retained forms and nonzero continuum | Best-prepared targets; no saving for the retained total is proved |
| Mellin/additive localization | Outer frequencies at most quadratic up to logs; explicit central Gram forms | Fixed nonzero low frequencies remain; localization is infrastructure |
| Finite Euler/Sonin identity | Exact projected boundary identity for every finite prime set; closed energy-relative formulation | No correction sign follows; active primes and support must grow together |
| Local all-source positivity | Complete tail and mixed-term certificates at \(L=1\) and \(L=6/5\) | Valid bounded-window calibration; no uniform growing-window mechanism |
| One-sided translated growth | Either eventual sign envelope at rate \(a\) excludes \(\beta>1/2+a\) | One fixed \(a<1/2\) suffices; polynomial/RH growth is stronger than needed |
| Selective dual response | Positive reference, exact positive-square split, bounded reference energy on translated sources | Retain projection/inverse metric; seek one rate below the baseline |
| Complete signed prime pairs | Full caps, diagonal/model cancellation, negative remainder \(O(X^2)\), finite signed certificates | Bound only the positive aggregate at \(X^{3-\kappa}\) |
| Short-interval reconstruction | Second- and sixth-order transfer with full endpoint accounting | Longer intervals are usable; arithmetic covariance remains open |
| Structural non-bootstrap | Countermodels preserve PNT, preparation, frame/positivity data and long finite prefixes at nonzero exponents | A contraction/descent needs an actual \(\mu/\Lambda\) ingredient |

Core Sonin records: [Sonin index](../../investigations/sonin-critical-boundary/README.md), [one-sided growth theorem](../../investigations/sonin-critical-boundary/notes/GLOBAL_GROWTH_ONE_SIDED_20261003.md), [centered dual response](../../investigations/sonin-critical-boundary/notes/selective-loss-program/03_centered_dual_energy_20261003.md), [complete response and signed pairs](../../investigations/sonin-critical-boundary/notes/selective-loss-program/04_complete_response_and_signed_pairs_20261003.md), [actual error and central projection](../../investigations/sonin-critical-boundary/notes/selective-loss-program/09_actual_error_projection_and_frequency_20261003.md),
and [structural non-bootstrap](../../investigations/sonin-critical-boundary/notes/subpower-milestones/04_structural_nonbootstrap_20261003.md). Chronology matters: the historical
'LATEST_WORK_ASSESSMENT_20261003.md' predates the first-prime resonance
theorem; its mean-only correction recommendation is superseded. Old
pair-error assessments used an RH-scale \(X^2\log X\) target and must
not be copied as obstructions to every first fixed saving.

The following shapes have proved obstructions and should be retired in
their original form:

- Mean-only or any fixed finite family of penalty functionals: two-packet
  first-prime resonance and infinite positive correction index. [resonance review](../../investigations/sonin-critical-boundary/reviews/FIRST_PRIME_RESONANCE_REVIEW_20261003.md)
- Full independently positive ambient absorption: adverse loss at least
  \(ce^{r/2}\), ruling out every fixed \(\delta<1\) in that class.
  Source-selective forms remain open. [ambient absorption obstruction](../../investigations/sonin-critical-boundary/reviews/POSITIVE_CHANNEL_ABSORPTION_REVIEW_20261003.md)
- Fixed-prime all-support comparisons, unweighted arithmetic-tail norms,
  and fixed-rank global repair of the centered reference: retained bulk
  or growing negative index defeats these proposals. [all-window obstruction audit](../../investigations/sonin-critical-boundary/reviews/ALL_WINDOW_MECHANISM_OBSTRUCTION_AUDIT_20261003.md)
- Nonnegative endpoint-profile tails in the two-template Schur construction
  on growing windows: this proposed safe complement already carries an
  RH-strength obligation. Changing a positive reference does not change the
  physical constrained infimum. [complement/dual audit](../../investigations/sonin-critical-boundary/reviews/SELECTIVE_LOSS_COMPLEMENT_AND_DUAL_REVIEW_20261003.md)

Qualitative compactness at each fixed window provides no uniform global
saving. The tested separate scalar-tail strategy forces doubly exponential
ranks; that limits this estimate class, not every certificate algorithm.

## Program map

Each subfolder has a charter with a first deliverable and failure criterion.
These are alternatives and supporting branches, not ten simultaneous claims.

| Priority | Program / status | New input to seek |
| --- | --- | --- |
| 1 | [Signed arithmetic covariance](programs/01_signed_arithmetic_covariance/README.md); reductions started | Whole signed capped energy \(X^{3-\kappa+o(1)}\), without stronger factorwise hypotheses |
| 2 | [One-sided growth and selective Sonin loss](programs/02_selective_sonin_loss/README.md); started, fixed-rate target newly emphasized | One-sided/source loss \(\mathrm{poly}(r)e^{\delta r/2}\), or selective dual energy \(\mathrm{poly}(r)e^{\delta r}\) |
| 3 | [Signed prime-pair dispersion](programs/03_signed_prime_pair_dispersion/README.md); started, reopen at weaker budget | Signed aggregate actual pair error \(X^{3-\kappa+o(1)}\), full shifts/caps/exceptions |
| 4 | [Joint short-interval and multiscale covariance](programs/04_short_interval_multiscale/README.md); reconstruction started, covariance exploratory | Joint length covariance or an arithmetic energy recursion retaining the coarse response |
| 5 | [Higher multilinear prime identities](programs/05_higher_multilinear_identities/README.md); new exploratory branch | Exact higher convolution form exposing a new signed product-level saving |
| 6 | [Arithmetic approximation below the RH norm](programs/06_arithmetic_approximation/README.md); new exploratory branch | Convergence in one \(L^p\), \(1<p<2\), or true holomorphic Hardy approximation below one |
| 7 | [Shifted Hermite–Biehler positivity](programs/07_shifted_hermite_biehler/README.md); new exploratory branch | Independent shifted-\(\xi\) dominance/positive-kernel inequality at one \(1/2<b<1\) |
| 8 | [Generalized Li positivity for one partial strip](programs/08_generalized_li_positivity/README.md); new exploratory branch | Uniform positivity of every generalized Li coefficient at one \(1<\tau<2\) |
| 9 | [Large-value and single-zero detection scout](programs/09_large_values_zero_detection/README.md); bounded source/mechanism scout | A theorem fitting the actual signed kernel or a new singleton amplification lemma |
| Support | [Finite certificates and source calibration](programs/10_finite_certificates_support/README.md); finite milestones started | Validate inequalities/constants or extend finite ranges; no global exponent follows |

### 1. Signed cofactor and centered Vaughan covariance

At \(D=X^{9/10}\), the exact divisor identity gives

\[
R_X(x)=-\sum_{k\leq\lfloor2BX/D\rfloor}
\sum_{d>D}\mu(d)\log d\,w(dk/x),\qquad
\|V_g-R_X\|_{L^2(X,2X)}\ll X^{9/10}\log X=o(X).
\]

All product caps and terminal bands remain. The limiting cutoff
\(D=X^{11/12}/(\log X)^{1/6}\) also has an \(O(X)\) norm budget.
The logarithmic adjustment matters: bare \(X^{11/12}\) gives
\(O(X\log X)\) in this bound. Mellin localization of
the complete capped polynomial, with kernel
\(J(q)=(2^{2+iq}-1)/(2+iq)\), leaves the annulus
\(X^{-1/5}<|t|\leq X^{1/12}\log X\) with \(o(X)\) norm error.
Its Gram form is positive as a quadratic form, not entrywise positive.

The balanced alternative is
\[
V_g(x)=B_{U,V}(x)+c_wM_1(U)x+E_X(x),\qquad
B_{U,V}=\sum_{m>U,n>V}A_U(m)\Lambda(n)w(mn/x),
\]
where \(A_U(m)=\sum_{d\mid m,d>U}\mu(d)\),
\(M_1(U)=\sum_{d\leq U}\mu(d)/d\), and
\(c_w=\int w(t)\log t\,dt\ne0\). At \(U=V=X^{11/24}\),
\(\|E_X\|=O(X)\). Dropping the continuum is invalid. Projecting
orthogonally onto \(x\) splits the task into
\[
\|B_{U,V}-\lambda_Xx\|^2\ll X^{3-\kappa+o(1)},\qquad
|\lambda_X+c_wM_1(U)|\ll X^{-\kappa/2+o(1)}.
\]

**First investigation:** derive a complete block-Gram formula retaining
terminal blocks and scalar mismatch. Study arithmetic covariance across
logarithmic dilations/cofactor channels, or compare the two exact identities
before taking absolute values. The finite pilot motivates keeping cross
terms; it does not imply a polynomial signed/trace contraction. Individual
Möbius-log channels have higher reciprocal-zeta pole orders, so even under
RH their extra logarithms can make that contraction the wrong conjecture.

**Gate:** a new product-level arithmetic relation must defeat the generic
balanced-coefficient cubic countermodel. Balance, divisor norms or a
coefficient-only large sieve do not suffice. The audited uniform Type II
factor hypothesis already implies a stronger fixed strip through its
zero-frequency slice with full real-block uniformity. A new power Mertens
bound is itself a fixed-strip breakthrough. Preserve whole-identity signs
rather than import the goal through a separated factor. [Möbius/Vaughan reductions](MOBIUS_AND_BALANCED_VAUGHAN_REDUCTIONS_20261004.md), [signed Mellin continuation](SIGNED_MELLIN_CONTINUATION_20261004.md),
[Type II source audit](BILINEAR_INPUT_SOURCE_AUDIT_20261004.md).

### 2. One-sided growth and source-selective Sonin loss

For the autocorrelation \(\phi\) and translated source \(F_r\),
\[
Q[F_r]=q-M_g(r)+\varepsilon_g(r),\qquad
M_g(r)=\sum_n\frac{\Lambda(n)}{\sqrt n}\phi(\log n-r),
\]
with exponentially decaying \(\varepsilon_g\). The existing Landau-type
argument accepts either eventual bound
\(M_g(r)\leq C(1+r)^k e^{ar}\) or its lower counterpart and excludes
\(\beta>1/2+a\), without assuming a rightmost zero exists. Set
\(a=\delta/2<1/2\).

An independently positive source split \(Q=P-E\) only needs
\(E\ll\mathrm{poly}(r)e^{\delta r/2}\). In the centered dual construction,
\(A=\Gamma+cI\geq I\), \(A[F_r]=O(1)\), and
\(E\leq\sqrt{A[F_r]\mathscr X(r)}\); a sufficient target is
\(\mathscr X(r)\ll\mathrm{poly}(r)e^{\delta r}\).

**First investigation:** write complete selective head, mixed and residual
costs in this fixed exponential budget. Seek an arithmetic-overlap or
prime-place cross-response recurrence. The per-prime self energies have a
polynomial sum, but cross terms can be coherent; control those explicitly.
The inverse metric/projection may select a better quantity, but known
logarithmic smoothing alone gives no power. An unprojected majorant returns
the variance problem. [one-sided growth theorem](../../investigations/sonin-critical-boundary/notes/GLOBAL_GROWTH_ONE_SIDED_20261003.md), [centered dual response](../../investigations/sonin-critical-boundary/notes/selective-loss-program/03_centered_dual_energy_20261003.md), [selective-loss program](../../investigations/sonin-critical-boundary/notes/selective-loss-program/overview.md).

### 3. Signed prime-pair dispersion at the first-exponent scale

With the full signed weight
\(W_X(n,m)=\int_X^{2X}w(n/x)w(m/x)\,dx\), subtraction of the evaluated
singular-series **model** gives an actual remainder
\[
\mathcal R(X)=\mathcal V_g(X)-\beta_gX^2+o(X^2),\qquad
\mathcal R_-(X)=O(X^2).
\]
Only \(\mathcal R_+\ll X^{3-\kappa+o(1)}\) is needed. Exact partial
summation expresses it as
\(-2\sum_h\int E_{X,h}(t)\partial_tW_X(t,t+h)\,dt\), where \(E\)
is actual partial pair count minus singular-series density. Each weight
has total variation \(O(X)\); the stronger sufficient input is
\[
\sum_h\sup_t|E_{X,h}(t)|\ll X^{2-\kappa+o(1)}.
\]

A hypothetical uniform per-shift square-root error gives variance
\(X^{5/2+\varepsilon}\), already below cubic. It missed the earlier RH
goal but would help here; it is not an available theorem.

**First investigation:** an exponent table for one signed weighted
dispersion or major/minor-arc split, with full proportional shifts,
partial sums and exceptional costs. A logarithmic almost-all-shift theorem
or a singular-series mean formula alone does not supply the new input.
[complete response and signed pairs](../../investigations/sonin-critical-boundary/notes/selective-loss-program/04_complete_response_and_signed_pairs_20261003.md), [dyadic pair gate](../../investigations/sonin-critical-boundary/notes/selective-loss-program/08_dyadic_shifted_correlations_20261003.md), [actual error and central projection](../../investigations/sonin-critical-boundary/notes/selective-loss-program/09_actual_error_projection_and_frequency_20261003.md).

### 4–5. Multiscale covariance and higher convolution identities

The short-interval gate is
\(\mathcal V_g\ll X^2S(X,h)/h^2+h^4/X\). At \(h=X^{3/4}\),
\(S\ll Xh^2X^{-\kappa+o(1)}\) would suffice. Sixth-order reconstruction
uses \((V_h-20V_{h/2}+64V_{h/4})/45\) and has \(O(X)\) norm error
at \(h=X^{11/12}\); its gate has remainder \(h^{12}/X^9\).

**New covariance branch:** retain the full three-length matrix and a common
coarse response. The coefficients cancel approximation moments, not an
arbitrary slow arithmetic mode. Any energy recursion must name the actual
\(\mu/\Lambda\) relation supplying contraction; generic smoothing,
preparation or positivity cannot bootstrap the exponent. [short-interval gate](../../investigations/sonin-critical-boundary/notes/subpower-milestones/02_short_interval_transfer_and_gate_20261003.md),
[sixth-order reconstruction](HIGHER_ORDER_SHORT_INTERVAL_RECONSTRUCTION_20261004.md), [structural non-bootstrap](../../investigations/sonin-critical-boundary/notes/subpower-milestones/04_structural_nonbootstrap_20261003.md).

**New multilinear branch:** use a finite higher convolution identity to
distribute Möbius factors over more scales. Heath–Brown's primary
[Sieve identities and gaps between primes](https://www.numdam.org/item/AST_1982__94__61_0.pdf),
Lemma 1 and its coefficient expansion, supplies the identity framework.
First derive one complete form on the product band, account for all
continuum moments/discarded terms, and prove quadratic equivalence to
\(V_g\). Then audit a signed product-level dispersion theorem. More factors
alone provide no oscillation; termwise absolute estimates may reproduce
cubic energy. This branch is worthwhile if it exposes an arithmetic
relation inaccessible to the current Type II form.

### 6. Arithmetic approximation in a weaker norm

Fix \(1<p<2\), \(b=1/p\), and prepared fractional-part functions
\[
\rho_\theta(x)=\{\theta/x\}-\theta\{1/x\},\qquad0<\theta<1.
\]
Approximate \(1\) by their finite linear combinations in \(L^p(0,1)\).
Beurling's criterion gives zero-freeness for \(\beta>1/p\), hence
\(\delta=2/p-1<1\); its general-\(p\) formulation is recorded in
[Delaunay–Fricain–Mosaki–Robert](https://arxiv.org/pdf/1101.1199),
introduction pp. 1–2. The sufficient direction is also elementary:
the Mellin functional at a zero with \(\beta>1/p\) is continuous by
Hölder, vanishes on every prepared function, and is nonzero on \(1\).

**First investigation:** a coefficient construction at \(p\) just above
one, with the complete small-\(x\) tail. For example \(p=200/199\)
targets \(\delta=0.99\). Any proved norm convergence, even logarithmic,
suffices here. This is a different criterion from a logarithmic saving
of cubic variance. Finite norm minimization does not prove convergence,
and an integer-only dictionary for \(p<2\) needs its own justification.

A separate proposed sufficient target fixes \(1/2<b<1\), chooses
Dirichlet polynomials \(P_N\) with \(P_N(1)=0\), and proves
\[
F_N(s)=\frac{1-\zeta(s)P_N(s)}s\in H^2(\Re s>b),\qquad
\|F_N\|_{H^2}\longrightarrow0.
\]
The constraint cancels the pole at one. At a forbidden zero,
\(F_N(\rho)=1/\rho\), contradicting continuous point evaluation.
Each fixed finite prepared polynomial already gives unconditional
\(H^2\) membership for \(b>1/2\): elementary zeta growth gives
\(F_N(\sigma+it)\ll_{b,P_N}|t|^{-b}\), uniformly for
\(b\leq\sigma\leq2\), and the far-right half-plane is elementary.
The new obligation is norm convergence, with the polynomial-dependent
tail costs controlled as \(N\) grows. A meromorphic boundary-line integral
alone is inadequate. No convergence theorem is claimed. The prior
[weighted-energy note](../../investigations/sonin-critical-boundary/notes/selective-loss-program/07_weighted_energy_abscissa_20261003.md) documents the physical/meromorphic-line trap.

### 7. Shifted Hermite–Biehler / positive-kernel program

For \(b=(1+\delta)/2\in(1/2,1)\), put \(E_b(z)=\xi(b-iz)\).
Prove directly
\[
|E_b^\#(z)|<|E_b(z)|\quad(\Im z>0),\qquad
E_b^\#(z)=\overline{E_b(\bar z)}=\xi(b+iz).
\]
A forbidden zero maps to \(z=-\gamma+i(\beta-b)\).
[Lagarias](https://arxiv.org/pdf/math/0601653), Lemma 2.1,
establishes the natural dominance unconditionally for \(b\geq1\)
and under RH for \(b>1/2\).

**First investigation:** derive the shifted theta/Euler representation
or kernel
\[
K_b(z,w)=
\frac{E_b(z)\overline{E_b(w)}-E_b^\#(z)\overline{E_b^\#(w)}}
{2\pi i(\bar w-z)}
\]
and find an independent strict diagonal positivity mechanism slightly
below one. Scalar theta-density positivity does not prove positivity of
this oscillatory kernel. Semidefiniteness alone may hide common nonreal
factors; strictness or independent exclusion is needed.

Boundary zeros produce real zeros of \(E_b\), allowed by our target but
excluded by some HB definitions; use dominance directly. At \(b=1/2\)
symmetry gives \(E_b^\#=E_b\). Varying the Euler exponent in the current
critical-phase Sonin identity does not derive the new shifted phase.
Assuming quotient analyticity or using a product comparison under the
desired strip would be circular.

### 8. Generalized Li positivity and a signed Laguerre prime family

Set \(\tau=1+\delta\in(1,2)\). [Freitas](https://arxiv.org/pdf/math/0507368),
Theorem 1 and Lemma 3.1, gives
\[
\alpha_n(\tau)=\frac1{(n-1)!}
\left.\frac{d^n}{ds^n}\{s^{n-1}\log\xi(s)\}\right|_{s=\tau}
=\frac1\tau\sum_\rho\left[1-\left(\frac\rho{\rho-\tau}\right)^n\right].
\]
Nonnegativity for **every** \(n\geq1\), at one common \(\tau<2\),
is equivalent to no \(\beta>\tau/2\), allowing the boundary. The zero
sum includes multiplicity and symmetric summation. Positivity at
\(\tau=2\) is unconditional; finite-index continuity provides no
uniform deformation interval.

**New concrete arithmetic family:** differentiating the absolutely
convergent log-zeta series at \(\tau>1\) gives the prime contribution
\[
\alpha_n^{\rm prime}(\tau)=
-\sum_{k\geq2}\Lambda(k)k^{-\tau}L_{n-1}^{(1)}(\tau\log k),
\quad
L_{n-1}^{(1)}(u)=
\sum_{j=0}^{n-1}\binom n{j+1}\frac{(-u)^j}{j!}.
\]
This formula is an elementary planning derivation, not a claim that the
source proves an arithmetic domination estimate.

**First investigation:** derive exact elementary/gamma terms and prime
tails, then seek an \(n\)-uniform signed lower bound at one \(\tau\)
just below two. Very high forbidden zeros may require enormous indices.
Absolute prime estimates can destroy Laguerre cancellation. Finite
positivity remains diagnostic. These known criteria specify what must
be proved; they are not independent proof mechanisms by themselves.

### 9. Large-value geometry and singleton zero detection

[Guth–Maynard, v2](https://arxiv.org/pdf/2405.20552v2) provides new large-value
tools and the density bound
\(N(\sigma,T)\leq T^{30(1-\sigma)/13+o(1)}\), which permits isolated
forbidden zeros. Near values \(N^{3/4}\), Theorem 1.1 improves classical
bounds for \(N<T^{10/11}\); Proposition 12.1 gives a further estimate
for \(T^{5/6}\leq N\leq T\). The often quoted \(5/6\) threshold is not
the full improving range. Our current central cap
\(T\asymp X^{1/12}\log X\), with lengths about \(X\) or \(X^{1/2}\),
is far outside even \(N\leq T\), so the direct import still misses.

**First investigation:** match one exact primary theorem to the actual
coefficients, lengths, kernel and frequency range. Regrouping or shorter
physical windows need complete low-frequency and remainder budgets.
Alternatively trace what a hypothetical single zero forces in a detector;
a new amplification lemma would have to produce more large values than
the theorem permits, rather than one exceptional point. No such lemma is
currently supplied. The mismatch limits this import, not all possible
uses of the geometric method.

Classical zero-free-region optimization belongs first in a bounded barrier
audit; compare [Mossinghoff–Trudgian–Yang](https://arxiv.org/pdf/2212.06867).
Retain the height-growing gamma/background term. Changing its
constant does not give a constant strip. A proposed positive trigonometric
combination would need a new height-uniform background estimate, not merely
another coefficient optimization.

## Recommended sequence and working conventions

Start programs 1 and 2 in parallel with bounded exact preflights; use
program 3 as the main alternative. Program 4 should proceed when a
specific source benefits from the longer reconstruction or supplies an
arithmetic cross-length relation. Permit one exploratory scout among
5–9, requiring an explicit new inequality and source/range audit before
large numerical work.

The additive central projection, physical fitted error, and physical
weighted energy remain interfaces in program 1/6. Four trends
\(1,t,\sqrt t,\log t\) are exactly removable, but trend removal plus
PNT supplies no power. Prefer the exact projected norm to a stronger raw
norm unless a source naturally controls the latter. Descent beyond a first
strip is deferred until a specific new arithmetic ingredient is identified.

Every proposed lemma should state all-real-\(X\) scope, one fixed power,
exact signs/caps, low frequencies, continuum terms, exceptional costs,
boundary/multiplicity behavior, and the arithmetic property defeating
known countermodels. Do not upgrade logarithmic parameters to powers,
discard terminal bands, or infer contraction from finite ratios.

Continue dated notes in the linked 'notes/programs/01_...' through
'10_...' subfolders. Put corresponding reviews in
'reviews/<same-program-name>/' and numerical sources/small records in
'numerics/<same-program-name>/' when those artifacts exist. Link parent
Sonin material rather than copying it. Include model/effort and LLM
assistance honestly; distinguish reductions, conditional inputs, heuristics,
failed mechanisms, diagnostics and certificates. Follow LARGE_FILES.md;
no third-party papers or large regenerable arrays are added.

Keep one editable manuscript, no new snapshot folders. A notable later
milestone may receive a concise DRAFT_HISTOR.md entry pointing to its
commit/tag and note/review. This overview organizes future work; it
changes no manuscript or compilation record and proves no new exponent.
