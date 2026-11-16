# Volterra degree induction and exact dyadic refinement

15 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance. Actual backend model and reasoning
effort are unavailable in the registered configurations and are not inferred.

Edward prefers to understand one route deeply before choosing further work:
Volterra first, especially induction in the recursive index, and infinite
dyadic products second. Volterra offers a scalar sequence indexed by polynomial
degree; the dyadic construction offers exact refinement of spatial masses.

This explanatory and strategic continuation of the
[methods refresher](04_METHODS_REFRESHER_20261115.md) changes no manuscript or
result status and activates no execution task. Consult the
[result index](../../../../result-summaries/README.md), especially
[cluster 18](../../../../result-summaries/18_tensor_approximation_and_coefficient_bounds.md),
and the [avoid index](../../../../avoid/README.md), especially
[pattern 03 on re-representations](../../../../avoid/03_lifts_and_re_realizations_in_new_coordinates.md).
Prospective coefficient-bound work is an **intermediate approximation target**
under [pattern 01](../../../../avoid/01_restating_the_target.md), not a new
RH-equivalent criterion. Its eventual gain would have to be a quantified
improvement to a specified norm product or scalar remainder.

## What the Volterra coefficients represent

At a fixed Newman time,
\[
 W_\lambda(u)=e^{\lambda u^2}\Phi(u),\qquad
 Z_\lambda=\int_{\mathbb R}W_\lambda(u)\,du,\qquad
 H_\lambda(z)=\frac12\int_{\mathbb R}W_\lambda(u)e^{izu}\,du.
\]
The source coordinate is \(u\), observation height is \(x=\Re z\),
and Newman time is \(\lambda\). The new index \(n\) is **polynomial
degree**, not height or a zeta-zero index.

Let \(P_n\) be the monic degree-\(n\) polynomial orthogonal to every
lower-degree polynomial under \(W_\lambda\). Start with \(u^n\) and
subtract its weighted projection onto lower degrees. Define
\[
 h_n=\int P_n^2W_\lambda\,du,\qquad
 \beta_n=\frac{h_n}{h_{n-1}}>0,\quad\beta_0=0.
\]
Multiplication by \(u\) connects only adjacent degrees:
\[
 P_{n+1}=uP_n-\beta_nP_{n-1}.
\]
Terms of degree \(j\le n-2\) vanish because
\(\langle uP_n,P_j\rangle=\langle P_n,uP_j\rangle=0\); the same-degree
term vanishes by evenness. The first examples are
\[
 P_0=1,\quad P_1=u,\quad P_2=u^2-\beta_1,\quad
 P_3=u^3-(\beta_1+\beta_2)u.
\]
Writing \(M_k=Z_\lambda^{-1}\int u^kW_\lambda\,du\) gives
\[
 \beta_1=M_2,\qquad \beta_2=\frac{M_4-M_2^2}{M_2}.
\]
The first link measures variance; the second introduces fourth-moment
information after the lower-degree contribution is removed. Later links
encode higher-degree information about the same source. They are not free
trial parameters. The full sequence and total mass encode the source in
this determinate moment setting; a finite prefix supplies finite information.

After normalizing the polynomials, multiplication by \(u\) becomes the
Jacobi matrix \(J(\lambda)\), with link \(\sqrt{\beta_n}\) between
sites \(n-1\) and \(n\). The Fourier field is recovered by
\[
 H_\lambda(x)=\frac{Z_\lambda}{2}
 \langle e_0,e^{ixJ(\lambda)}e_0\rangle.
\]
This is an oscillatory return amplitude at the first site of the degree
chain. Positive links do not make this amplitude positive. The
source-variable polynomials have real, interlacing roots, but these are
roots of \(P_n(u)\), not of \(H_\lambda(z)\). The standard
[orthogonal-polynomial zero theorem](https://dlmf.nist.gov/18.2#vi)
therefore does not prove the desired Fourier-field zero statement.

**Paper pointers:** [Volterra manuscript](../../03_volterra_coefficient_dynamics/manuscript/main.tex),
eq:recurrence and eq:twochains.

## Two different recursions

The three-term recurrence constructs \(P_{n+1}\) once its coefficient is
known. The Volterra equation describes how the coefficients change with
Newman time.

Since \(\partial_\lambda W_\lambda=u^2W_\lambda\), differentiation gives
\[
 \partial_\lambda\log h_n=\beta_n+\beta_{n+1}.
\]
Terms containing \(\partial_\lambda P_n\) vanish by orthogonality. The
right side follows by taking the squared norm of \(uP_n\). Subtracting
adjacent identities yields
\[
 \partial_\lambda\beta_n
 =\beta_n(\beta_{n+1}-\beta_{n-1}).
\]
Increasing \(\lambda\) relatively increases the source weight at large
\(|u|\). The equation describes how that redistribution changes successive
norm ratios, through interactions with neighboring coefficients. For the
reversed clock \(\tau=1/2-\lambda\), the sign reverses.

This locality does not by itself give a forward calculation in degree:
\[
 \beta_{n+1}=\beta_{n-1}+\partial_\lambda\log\beta_n.
\]
The next degree requires time-derivative information, not merely a value
or upper bound at one time. Evolution of a finite coefficient prefix
likewise needs the next coefficient at its boundary. Exact functions and
their required derivatives would permit formal recursive reconstruction;
supplying them already requires substantial source information.

**Paper pointers:** eq:hflow, eq:volterra, eq:monicvariation. The entrywise
Lax identity eq:lax does not supply the missing boundary information or
an infinite-dimensional well-posedness theorem.

## Where induction could do useful work

An existing example is the norm product:
\[
 h_{n+1}=\beta_{n+1}h_n,\qquad
 \beta_{n+1}\le B_n
 \quad\Longrightarrow\quad
 \frac{h_N}{h_0}\le\prod_{j=0}^{N-1}B_j.
\]
The manuscript gives \(B_n=\operatorname{arcosh}^2(2n+12)/16\), uniformly
over its time interval, by a confinement and integration-by-parts argument.
The product feeds into a scalar quadrature remainder. A sharper relation
that can be propagated in degree could improve this specific consumer.

For a more structural example, put \(V_\lambda=-\log W_\lambda\).
For a smooth positive weight with the required integrable tails,
integration by parts gives the classical identity
\[
 \int V_\lambda'(u)P_n(u)P_{n-1}(u)W_\lambda(u)\,du
 =n h_{n-1}. \tag{S}
\]
Integrate \((P_nP_{n-1}W_\lambda)'\): the boundary terms vanish,
\(P_n'=nP_{n-1}\) plus lower degrees, and \(P_{n-1}'\) has degree
below \(n\). Orthogonality proves (S). This is an explanatory derivation,
not a new theta estimate.

The identity shows where a particular source enters. For
\(W(u)=e^{-u^2/(2\sigma^2)}\), the logarithmic derivative is
\(V'(u)=u/\sigma^2\), giving \(\beta_n=n\sigma^2\). For the classical
quartic weight \(W(u)=e^{-u^4+t u^2}\), the same method gives
\[
 n=4\beta_n(\beta_{n-1}+\beta_n+\beta_{n+1})-2t\beta_n.
\]
Its log-weight derivative is cubic, so only a fixed number of neighboring
coefficients enter. This is a closed nonlinear relation in degree; it
does not make positivity or stable forward computation automatic. See
Van Assche, [*Orthogonal polynomials, Toda lattices and Painlevé equations*,
§3, equation (3.1)](https://arxiv.org/html/2202.11017v1), already catalogued
in the branch's references.

For theta, \(V_\lambda'=-\Phi'/\Phi-2\lambda u\) involves the complete
infinite theta sum. The manuscript has not reduced (S) to a closed finite
relation of this kind. Instead it bounds a diagonal integration-by-parts
identity using the score and Jensen's inequality. The next conceptual
question is whether the complete source supplies relations or inequalities
that carry a useful inductive invariant from degree \(n\) to \(n+1\),
possibly retaining neighboring coefficients jointly.

The closure test must be explicit: list the information assumed through
degree \(n\), identify each new derivative, integral or coefficient at
the next step, and show that the same assumptions control it. An
uncontrolled source integral or future coefficient means the induction
has not closed. A claimed improvement must reach a specified scalar
remainder rather than stop at a reformulation of the zero problem.

**Paper pointers:** eq:confinement, lem:general, thm:theta, eq:product.

## Dyadic products as conditional mass

At level \(L\), divide the real line into cells
\(I_{L,j}=[j2^{-L},(j+1)2^{-L})\) and assign exact masses
\[
 m_{L,j}=\int_{I_{L,j}}W_\lambda(u)\,du.
\]
Children's masses add to their parent's mass. Their conditional fractions are
\[
 p_\epsilon(j)=\frac{m_{L+1,2j+\epsilon}}{m_{L,j}},
 \qquad p_0(j)+p_1(j)=1.
\]
Prepare cell amplitude \(\sqrt{m_{L,j}}\) and refine by
\[
 |j\rangle\longmapsto
 \sqrt{p_0(j)}|j0\rangle+\sqrt{p_1(j)}|j1\rangle.
\]
Multiplying by the parent's amplitude gives the exact child amplitudes.
The square roots make squared amplitudes equal masses, preserving squared
norm \(Z_\lambda\). Division by \(\sqrt{Z_\lambda}\) would normalize
the state to norm one.

For an illustrative unit mass, take a first split \(0.6/0.4\). Split
the left child conditionally as \(0.7/0.3\) and the right child as
\(0.2/0.8\). These are toy values, not theta computations.

| Binary path | Conditional product | Mass |
| --- | --- | --- |
| 00 | \(0.6\times0.7\) | 0.42 |
| 01 | \(0.6\times0.3\) | 0.18 |
| 10 | \(0.4\times0.2\) | 0.08 |
| 11 | \(0.4\times0.8\) | 0.32 |

The second split depends on the first bit. The source is generally a
correlated binary state. Each branch mass is its root mass times the
product of all conditional fractions on that branch.

The entire line has a root label \(a\in\mathbb Z\), one for each unit
interval. Within it, digits locate \(u=a+\sum_{k\ge1}2^{-k}b_k\).
The recursive index \(L\) measures spatial resolution \(2^{-L}\),
whereas Volterra's \(n\) measures polynomial degree.

**Paper pointer:** [Dyadic manuscript](../../04_exact_infinite_tensor_products/manuscript/main.tex),
eq:mass-isometry.

## The infinite product and the meaning of exactness

Let \(f_L=P_hW_\lambda\) be the cell-average density; on a cell of
width \(h=2^{-L}\), it equals \(m_{L,j}/h\). The cell-vector embedding
maps the prepared state to \(\sqrt{f_L}\) in the common space
\(L^2(\mathbb R,du)\). An unresolved reference bit splits amplitude
equally and leaves the old step function unchanged. The source correction
on a child multiplies amplitude by \(\sqrt{2p_\epsilon}\).

On each unit interval define \(R_k=f_k/f_{k-1}\). Then
\[
 f_L=f_0\prod_{k=1}^L R_k,\qquad
 \sqrt{f_L}=\sqrt{f_0}\prod_{k=1}^L\sqrt{R_k}.
\]
This telescoping identity is the source product. Each factor can depend
on the entire first \(k\) bits. For a smooth positive source, fine
neighboring children have nearly equal density, so \(R_k\) tends to
one locally. The paper proves multiplication-product convergence on each
fixed bounded interval and weighted state convergence
\(\sqrt{f_L}\to\sqrt{W_\lambda}\) on the whole line. It does not
turn the local product bound into a global operator-norm estimate.

The observation has a separate product:
\[
 e^{izu}=e^{iza}\prod_{k\ge1}e^{iz2^{-k}b_k}.
\]
The phase factors act on individual bits even though the source state is
correlated. Their expectation in the limiting state gives
\[
 \frac12\langle\sqrt{W_\lambda},
 e^{izu}\sqrt{W_\lambda}\rangle=H_\lambda(z).
\]

At finite resolution, exact integration of the phase across each
unresolved cell gives the Fourier transform of the cell-average density:
\[
 A_L(\lambda,z)=\frac12\operatorname{sinc}(zh/2)
       \sum_jm_{L,j}e^{izc_{L,j}},
 \qquad \operatorname{sinc}(w)=\sin(w)/w,\quad\operatorname{sinc}(0)=1.
\]
The sinc factor is the phase average over a uniformly filled cell; the
original theta density need not be uniform within that cell.
In general \(A_L\ne H_\lambda\) at finite \(L\); the theorem controls
the difference and gives the exact field in the limit. At a finite level
the full-line sum still has infinitely many cells, until a spatial tail
is also truncated.

Exactness specifies the limiting object and the identities preserved at
each refinement. It does not make cell-mass acquisition free or bound
the complexity of dependence on earlier bits. Finite-level time evolution
also requires information within each cell:
\[
 \partial_\tau m_{L,j}(1/2-\tau)
 =-\int_{I_{L,j}}u^2W_{1/2-\tau}(u)\,du.
\]
The right side is not determined by the cell mass alone. Induction in
resolution naturally proves conservation of mass and approximation
bounds; Fourier cancellation and efficient contraction require further
estimates.

**Paper pointers:** eq:telescopes, eq:state-limit, eq:phase-product,
eq:sinc, eq:readout, and §Time and arithmetic in the finite readout.

## Controls and scope

The [control catalog](../../../../result-summaries/12_collision_controls_and_screening.md)
and [pattern 02](../../../../avoid/02_shape_only_arguments_and_the_controls.md)
were applied as an analytical premise screen. The existing
[VCD integration table](../../03_volterra_coefficient_dynamics/notes/02_VCD_ANALYTICAL_MANUSCRIPT_INTEGRATION_20261114.md)
records the detailed checks; existing interval certificates were not rerun.

The polynomial recurrence, Volterra evolution and identity (S) hold for
broad classes of regular positive even weights; they do not distinguish
theta from colliding sources. The dyadic construction likewise applies
to many positive densities. In particular, the positive three- and
four-square collision controls pass the paper's actual coefficient
envelope. They lack complete canonical equal coefficients and full
reflection, but the envelope does not exploit those missing properties
strongly enough to reject them.

The remaining catalog controls have these relevant premise limits:

- Atomic sources lack the positive full-line density needed for
  \(V=-\log W\); compact triangular extensions also lack global strict
  positivity. Their degree recurrences still make sense up to available
  degree. These density failures do not exclude all recurrences or all
  conditional-mass constructions.
- The reflected super-Gaussian fails exponential confinement at large
  \(|u|\). Smooth shape and positive-primitive controls lack the complete
  theta summand formula; their weaker coefficient bounds were not tested
  in the source screen.
- Euler-factor translates lack the unchanged summand score. The actual
  envelope failure in the source screen is specifically
  \(c=1/2,p=23,\lambda=0\); other primes are not covered.
- Finite-prime square perturbations lack full canonical reflection even
  when positivity and score bounds persist. RH-conditional endpoint
  controls lack ordinary Dirichlet arithmetic and retain their RH
  hypothesis; their coefficient comparison is untested.
- Fixed-source varied-observation controls retain source coefficients but
  fail the literal cosine/Newman observation. Actual-profile positive
  measure relaxations do not supply the same full-line theta density and
  physical Fourier readout.

This screens explanatory identities and the inherited envelope, not an
unspecified future theta relation. Such a relation must name the
additional premise that the relevant collision controls fail. These
limitations follow [pattern 07](../../../../avoid/07_scoped_exclusions_read_as_universal.md);
they are not impossibility results for coefficient induction or dyadic
methods.

## Suggested order of study

Volterra is the better first focus for the proposed induction strategy:
one scalar sequence, a local time law and an identified norm-product
consumer. Examine the complete theta logarithmic derivative and
orthogonality identities to see what can actually be carried from one
degree to the next. Distinguish the existing confinement estimate from
a stronger joint coefficient statement.

Dyadic products are a useful second focus for exact multiscale
representation. The next structural issue is whether the conditional
fractions admit controlled compression or cancellation estimates across
levels. Exact mass refinement leaves these questions open. This order
reflects the requested proof style, not evidence that either route is
presently close to a theorem about zeta zeros.

## Session capture

The registered history remains protected by its integrity checks. A
prior reply now has structured moderation metadata unsupported by the
strict paginated exporter; the earlier 36 ms creation-time mismatch also
remains unresolved. Neither check was relaxed in this discussion.

The native thread reader separately returned public user and assistant
messages, including both preceding completed final replies. An explicitly
[unregistered native public excerpt](../../chat-histories/unregistered_native_public_export_0003_20261115.json)
preserves that returned text and provenance under the shared recorder
lock. It excludes tool traffic and private reasoning, does not replace
the original registry or timestamps, and cannot include this turn's
unsent final reply. Canonical automatic final capture remains blocked.

