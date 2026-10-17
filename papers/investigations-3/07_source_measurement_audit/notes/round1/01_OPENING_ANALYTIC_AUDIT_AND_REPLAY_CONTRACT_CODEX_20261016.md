# Finite source measurements and nearby double jets

16 October 2026, America/New_York. Prepared for Edward Baker with
substantial LLM assistance. Recorded model: **gpt-6.1-sol (Codex)**;
reasoning effort: **ultra**, verified from this conversation's session
metadata. Three same-model collaborators checked the analytic argument,
numerical source record and scope. These are internal LLM checks, not the
designated Claude cross-model review or specialist human review.

**17 October continuation:** the [current round plan](../../research-overview/02_ROUND_BASED_EXECUTION_PLAN_20261017.md)
supersedes this opening note's interleaved review sequence. Formal assessment
follows a round containing multiple notes. The bounded replay is now recorded
in [Note 03](03_BOUNDED_REPLAY_AND_POSITIVE_FEASIBILITY_CODEX_20261017.md);
[Note 04](04_NONDEGENERATE_FINITE_SOURCE_COLLISIONS_CODEX_20261017.md) strengthens
the double-jet construction to generic nondegenerate collisions. The body below
retains the original opening assessment and its historical next steps.

**Status: opening analytic assessment and fixed replay contract.** The
finite-support endpoint argument in [Reply 03, Sections 1–2][reply] survives
with explicit hypotheses. Its sufficient radius is not an actual distance
to a double jet. A separate argument below does establish nearby double-jet
feasibility for every fixed finite-support real perturbation space of
dimension at least two, at sufficiently large height. It preserves
coefficient positivity and exact linear normalization, but supplies no
numerical onset, nondegenerate collision, or theta sign conclusion. The
original numerical table remains floating evidence; this opening phase
has not performed its independent replay.

This begins the [initial proposal][proposal], using the
[result-summary index][results], [arithmetic bookkeeping][arithmetic] and
[patterns-to-avoid index][avoid]. Under [avoid 01][a01], the new statement
is a scoped instability result for an approximation class, not a new
RH-equivalent criterion. Its limitations follow [avoid 07][a07]; the fixed
replay and stopping rule follow [avoid 09][a09] and [avoid 10][a10].

## 1 The class and the claims under audit

Use the canonical normalization

\[
\phi_n(u)=e^u(2q_n^2-3q_n)e^{-q_n},\qquad
q_n=\pi n^2e^{4u},\qquad
\beta_n=(4\pi n^2-1)e^{-\pi n^2},\qquad \sum_{n\ge1}\beta_n=\tfrac12.
\]

Let \(V\subset\mathbb R^N\) be fixed, extend its vectors by zero outside
\(1\le n\le N\), and put

\[
f_\delta=\sum_{n=1}^N\delta_n\phi_n,\quad
g_{t,\delta}=e^{tu^2}f_\delta,\quad
B_{t,x}\delta=\binom{\int_0^\infty g_{t,\delta}\cos(xu)\,du}
{-\int_0^\infty ug_{t,\delta}\sin(xu)\,du}.
\]

The theta jet is \(h=(H,H_x)^{\mathsf T}\). The default affine source is
theta plus \(f_\delta\), with coefficients \(a_n=1+\delta_n\) for
\(n\le N\) and \(a_n=1\) beyond \(N\). Primitive normalization imposes
\(V\subset\ker\beta^{\mathsf T}\); anchoring additionally imposes
\(\delta_1=0\). Positivity means \(\delta_n\ge-1\). Heat time is in a fixed
compact interval \(I=[0,T]\). All jet and measurement norms below are
Euclidean unless expressly stated otherwise.

Exact source identification and [normalized recurrence stability][recurrence]
remain inherited results in their stated coefficient classes; neither is
being replaced by a finite numerical observation.

| Inherited claim | Opening disposition |
| --- | --- |
| Every nonzero finite-support perturbation has a first nonzero odd endpoint | Valid; finite Vandermonde argument below |
| The cosine transform has an algebraic endpoint expansion | Valid with derivative integrability and remainder stated below |
| A lower bound for the optimal constant determines its full growth | Does not follow from that lower bound alone; a fixed-space asymptotic is available below |
| \(\eta=\|h\|/C\) is the actual collision distance or necessary measurement precision | Incorrect inference; it is a sufficient exclusion radius |
| Carrier size bounds the complete two-jet by the same displayed power | Not established as written; arithmetic factors, derivative factors and uniformity must be supplied |
| A negative equality minimizer proves positive infeasibility | Valid only when the equality solution is unique and rank is established, or with a separate infeasibility witness |
| The printed weighted distance is the weighted optimum | Incorrect; the code evaluates a weighted distance at a Euclidean minimizer |
| Sixteen-digit measurements fail near \(x=140\) | Extrapolation with unspecified error units; excluded from this phase's conclusions |

## 2 Endpoint asymptotics with a remainder

For a nonzero vector supported on distinct nodes \(n_1,\ldots,n_s\),

\[
f_\delta(-u)=e^{-u}\sum_{k\ge1}
 \frac{(-1)^k(2k+1)\pi^k}{(k-1)!}e^{-4ku}
 \sum_n\delta_n n^{2k}.
\]

If \(f_\delta\) were even, its double-exponential decay at positive
infinity would force every coefficient in this convergent power series
to vanish. The equations for \(k=1,\ldots,s\) form a Vandermonde matrix
times the invertible diagonal matrix with entries \(n_i^2\), so
\(\delta=0\), a contradiction. Each finite sum is entire in \(u\);
therefore a nonzero odd part has some nonzero odd derivative at zero.
This is the finite-support statement, consistent with the broader
[reflection-rigidity result][rigidity].

All derivatives of \(g=g_{t,\delta}\), and of \(ug\), vanish at positive
infinity and belong to \(L^1(0,\infty)\). Their norms are uniformly bounded
for \(t\in I\) and \(\delta\) in a bounded subset of fixed \(V\).
For \(x>0\), repeated integration by parts gives the exact formula

\[
\int_0^\infty g(u)\cos(xu)\,du
=\sum_{j=0}^{m-1}\frac{(-1)^{j+1}g^{(2j+1)}(0)}{x^{2j+2}}
 +\frac{(-1)^m}{x^{2m}}\int_0^\infty g^{(2m)}(u)\cos(xu)\,du.
\tag{1}
\]

In particular, the remainder is at most
\(x^{-2m}\|g^{(2m)}\|_1\). Extra integrations give the stronger orders
used next. The first odd nonzero endpoint is unchanged by multiplication
by \(e^{tu^2}\), because that factor is even and equals one at zero.

For nonzero \(V\), choose the **least** \(q\ge0\) for which
\(\ell_q(\delta)=f_\delta^{(2q+1)}(0)\) is not identically zero on \(V\).
Set \(p=2q+2\) and \(a(\delta)=(-1)^{q+1}\ell_q(\delta)\). Then, in
operator norm on fixed \(V\), uniformly over \(t\in I\),

\[
B_{t,x}\delta=
\binom{a(\delta)x^{-p}+O_I(\|\delta\|x^{-p-2})}
{-p\,a(\delta)x^{-p-1}+O_I(\|\delta\|x^{-p-3})}.
\tag{2}
\]

The derivative expansion does not come from differentiating an
uncontrolled asymptotic remainder. Apply integration by parts separately
to \(-\int ug\sin(xu)\,du\), using
\((ug)^{(2j)}(0)=2j\,g^{(2j-1)}(0)\); the same integrability bounds give
the second remainder in (2).

For a fixed injective measurement \(M:V\to\mathbb R^m\), define

\[
C(t,x)=\sup_{\delta\ne0}\frac{\|B_{t,x}\delta\|}{\|M\delta\|},\qquad
A_M=\sup_{\delta\ne0}\frac{|\ell_q(\delta)|}{\|M\delta\|}>0.
\]

Finite-dimensional norm equivalence and (2) give the sharper statement

\[
C(t,x)=A_M x^{-p}\bigl(1+O_I(x^{-2})\bigr).
\tag{3}
\]

The constants and the onset depend on the fixed space and measurement.
This does not cover growing supports, height-dependent measurements or
unbounded heat time. For a noninjective \(M\), finite \(C\) exists exactly
when \(\ker(M|_V)\subseteq\ker(B_{t,x}|_V)\).

## 3 Actual distance and a stronger scoped instability

For \(h\ne0\), \(C>0\), the triangle inequality proves only

\[
\|M\delta\|<\eta:=\frac{\|h\|}{C}
\quad\Longrightarrow\quad h+B\delta\ne0.
\]

Let \(Q\) be a basis matrix for \(V\), take a thin QR factorization
\(MQ=UR\), and set \(A=BQR^{-1}\). Then \(C=\sigma_{\max}(A)\).
The actual unconstrained measurement distance is

\[
r_M=\inf_{B\delta=-h}\|M\delta\|
=\begin{cases}\|A^\dagger h\|,&h\in\operatorname{ran}A,\\
\infty,&h\notin\operatorname{ran}A.
\end{cases}
\tag{4}
\]

Thus \(\eta\le r_M\), with equality requiring the appropriate singular
direction. Adding \(\delta_n\ge-1\) can increase this distance or remove
feasibility. A small \(\eta\) alone does neither calculation.

**Scoped analytic deduction.** If \(\dim V\ge2\), there nevertheless are
positive theta-tail sources with exactly vanishing double jet at every
sufficiently large prescribed \((t,x)\), uniformly for \(t\in I\), whose
coefficient changes tend to zero faster than every power of \(x^{-1}\).
Any exact linear constraints already built into \(V\) remain satisfied.

To prove this, choose \(\delta_A\in V\) with \(a(\delta_A)\ne0\), using
the least \(q\) above. Choose a nonzero
\(\delta_B\in\ker(\ell_q|_V)\). Its first nonzero odd endpoint exists and
has a strictly later order, say \(r-1\), where \(r>p\) is even. Put
\(a=a(\delta_A)\ne0\) and let \(b\ne0\) be its analogous signed leading
coefficient for \(\delta_B\). Formula (2), applied separately, yields

\[
\det\bigl(B_{t,x}\delta_A\ \ B_{t,x}\delta_B\bigr)
=(p-r)ab\,x^{-p-r-1}\bigl(1+O_I(x^{-2})\bigr).
\tag{5}
\]

Consequently this two-column matrix \(D_{t,x}\) is invertible for all
sufficiently large \(x\), and
\(\|D_{t,x}^{-1}\|=O_I(x^{r+1})\). Complete theta's even source and all
its derivatives decay at both ends; \(e^{tu^2}\Phi(u)\) is uniformly
Schwartz for \(t\in I\). Its Fourier transform and first derivative
therefore obey \(\|h(t,x)\|=O_{I,K}(x^{-K})\) for every \(K\), directly
by integration by parts. This uses no RH or unquantified convexity bound.
Set

\[
\binom{c_A}{c_B}=-D_{t,x}^{-1}h(t,x),\qquad
\delta(t,x)=c_A\delta_A+c_B\delta_B.
\tag{6}
\]

Then \(h+B\delta=0\), and \(\|\delta(t,x)\|=O_{I,K}(x^{-K})\) for every
\(K\). Eventually \(\|\delta\|_\infty<1/2\), so all coefficients remain
strictly positive. For every fixed finite linear measurement,
\(\|M\delta\|\) also tends to zero faster than every power. This proves
actual nearby feasibility separately from the radius argument.
When \(h(t,x)=0\), the construction returns \(\delta=0\); it does not
claim a nonzero perturbation at every point.

This excludes a fixed positive absolute measurement tolerance that would
guarantee nonvanishing double jets over the entire unbounded spectral
domain for this relaxed class. In particular it applies to the dimension
five and dimension four tangent spaces in Reply 03. It gives no explicit
height, no exponential rate for the distance, and no corresponding
statement for a one-dimensional space or a fixed finite height box.
The constructed source depends on the selected observation point and is
then held fixed; differentiating (6) as if its coefficients varied with
the observation would change the problem. A vanishing double jet is a
zero of multiplicity at least two; a nondegenerate heat collision needs
the additional check \(H_{a,xx}\ne0\).

Nonzero perturbations here fail complete source reflection. Exact theta
identities, zero measurement error for an injective map, growing designs,
and directional finite-box certificates are outside this exclusion.
Conversely, a comparison source with independently established jet margin
\(m\) still gives a valid transfer when \(C\|M\delta\|<m\); this audit
does not assume that such a margin is unavailable in every other class.

## 4 Carrier bounds and the numerical evidence

Reply 03's carrier logarithm includes the necessary heat correction
\(t\log^2(x/4\pi)/16\). A carrier is not the complete two-jet. The
displayed bound for \(h\) leaves an arithmetic factor unquantified and
does not budget its derivative. No numerical exclusion radius or finite
threshold follows from it as written. Sections 2–3 above avoid that import.

There is also a literal carrier mismatch in the recorded solver.
[Polymath, equations (6), (9), (10)][polymath] define \(M_0\) by the
uncorrected Stirling expression and \(M_t=e^{t\alpha^2/4}M_0\).
The solver's `carrier_abs` adds
\(\operatorname{Re}(1/(12z)-1/(360z^3))\), \(z=s/2\). Its labelled
\(|M_t|\) column is therefore a modified gamma approximation. This
changes the diagnostic column, not the separately calculated jet matrix.

Source inspection of the [solver][solver] and [record][record] gives:

- `min_norm` solves equalities and checks coefficient signs afterward
  (lines 107–139, 222–237). Negative answers do not establish positive
  infeasibility for underdetermined cases. Its numerical rank cutoff is
  \(10^{-13}\); outputs labelled singular are not exact rank results.
- The weighted value is \(\sum_{n\le N}\beta_n|\delta_n|\) at the
  Euclidean minimizer (lines 234–235), not its own minimum.
- In the zero-tail variant, \(a_n-1=-1\) for every \(n>N\). Full raw
  \(\ell^2\) distance to theta is infinite; the printed finite value is
  only a distance in the first \(N\) coordinates. Full weighted
  \(\ell^1\) distance adds \(\sum_{n>N}\beta_n\).
- The complete baseline is approximated by six source columns, with
  Simpson quadrature and an integrand cutoff. Their errors are not
  bounded in the record. This matters for a jet obtained by cancellation.
  The norm calculation also uses normal equations (lines 316–330).
- Anchoring \(a_1\) determines a relation for \(a_2\) and higher nodes;
  it does not force \(a_2=1\). More rows than unknowns do not by themselves
  establish inconsistency. Both shortcuts appear in the solver's wording.

These are source-level findings; no new numerical values are asserted.

## 5 The bounded independent replay contract

Freeze the following inputs before implementation. The purpose is to
assess the recorded finite values and feasible classes, not estimate an
asymptotic onset from a fitted height law.

| Component | Fixed cases |
| --- | --- |
| Conditioning observations | \((0,30),(0,44.1303),(1/4,44.1303),(0,60),(0,70),(0,85)\) |
| Conditioning support and constraints | \(N=6\); \(\beta\cdot\delta=0\), separately with \(\delta_1=0\); dimensions five and four |
| Recurrence measurements | \(d_k=\delta_{k-1}-2\delta_k+\delta_{k+1}\), \(k=1,\ldots,7\); every coefficient outside \(1,\ldots,6\) is zero |
| Reflection measurements | \(f_\delta(j/20)-f_\delta(-j/20)\), \(j=1,\ldots,12\) |
| Equality and positive-feasibility cases | Only \((1/4,44.1303),(0,60)\); \(N=2,3,4,6\); theta or zero tail; anchor off or on |
| Error units | Absolute Euclidean errors in the raw rows; entrywise tolerance \(\varepsilon\) implies aggregate \(\sqrt7\varepsilon\) or \(\sqrt{12}\varepsilon\) |

The zero-tail class is affine, with
\(\sum_{n\le N}\beta_n\delta_n=\sum_{n>N}\beta_n\), rather than the
homogeneous theta-tail tangent constraint. Do not set the omitted tail
to zero in the normalization or complete theta jet.

Reimplement evaluation and linear algebra without importing Claude's
solver. Compare 80- and 120-decimal-digit calculations once, use thin QR
and singular values, and bound the coefficient tail, integral tail and
quadrature error separately. Check all five time-zero baseline jets
against \(H_0(x)=\xi((1+ix)/2)/8\) and its physical derivative. Record
normalization residuals and uncertainty propagated through the solve.
Precision agreement alone remains diagnostic.

Report \(C\), \(\eta\) and the actual equality distance as separate
quantities. Use bounded active-set calculations for nonnegative
feasibility; an infeasibility claim needs a checked separating witness,
and an optimum claim needs the corresponding optimality conditions.
Optimize weighted \(\ell^1\) separately or label it as a value at the
Euclidean minimizer. Do not reinterpret a rank cutoff as exact singularity.

Execution limit for this replay: the listed cases only, one precision
comparison, at most 30 minutes wall time and 1 GiB additional memory.
Stop a case as unresolved if its error budget or conditioning cannot be
resolved within that limit. No height grid, increasing-support sweep or
\(x=140\) test is included in this contract. Small code and records go
in `numerics/` under [LARGE_FILES.md][large].

## 6 Controls and the next decision

Apply [summary 12][controls] and [avoid 02][a02] by actual class membership:

| Control | Eligible class and missing premise |
| --- | --- |
| Three-square collision at \(t=1/4\), \(44.1303<x_*<44.1304\) | Its normalized zero-tail source belongs to the corresponding affine square class, but fails full reflection; it is not a finite-support perturbation with theta tail |
| Four-square collision at \(t=1/100\), \(83.5323729<x_*<83.5323730\) | Same zero-tail qualification; even after two odd endpoint constraints it fails full reflection. Its time and collision bracket are outside the six listed observation points |
| Reflected super-Gaussian control | Full reflection retained; integer-square coefficient representation is not supplied, so membership in \(V\) cannot be assumed |
| Euler-factor controls | Shifted arithmetic source family; not established members of the fixed finite square perturbation space |
| Smooth and positive-primitive controls | Test shape or auxiliary positivity premises; do not supply the theta square-coefficient constraints |

A bracket endpoint such as \(x=44.1303\) is not the exact certified
collision. The opening replay compares the existing solver there; a
positive control collision is inherited from its own certificate, not
proved by a nearby small residual. No new control run is needed here.

The next gate is Claude's repair/review of the original proposition and
the two analytic deductions above, including the least-endpoint choice
and the determinant remainder. The independent numerical replay then
uses Section 5, followed by Claude's review and at most one reconciliation
round.
Record the accepted scoped obstruction, corrected diagnostic or unresolved
claim without closing the other structural projects. The quantitative
onset remains an explicit missing input; this phase supplies no reason to
expand the numerical campaign.

## Source identities

The source audit used repository HEAD
`688b2db797ff4c99f481ace5f3a186979fa07ef3`. At inspection the reply, solver
and floating record had SHA-256 digests, respectively:

```text
0871fb3829301bd2f03c262d8d9839cd0ba4306b9cc48e3e3f7dcdc13000db68
b5d9d9c5c45ae329bc6f8094b2c9dec5af76945bc57b41b06adbad5dd1307e7a
3a9e555cafa456a5dbac601625c083577a1ecf95c12c329f55fac278f3b13a1d
```

These identify the inspected source bytes, not mathematical validity.
The public conversation retains [formal replay identity 28][chat] under
the local standing instruction; it is not re-registered in this project's
history folder.

[proposal]: ../../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md
[reply]: ../../../../brainstorm/investigations-3/reviews/03_REPLY_TO_CODEX_RESPONSE_CLAUDE_20261016.md
[solver]: ../../../../brainstorm/investigations-3/numerics/check_codex_response_reply_claude_20261016.py
[record]: ../../../../brainstorm/investigations-3/numerics/CHECK_CODEX_RESPONSE_REPLY_CLAUDE_20261016.json
[rigidity]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/05_control_families/02_WEIGHTED_COMB_REFLECTION_RIGIDITY_20261015.md
[recurrence]: ../../../../investigations-2/active/22_theta_manifold_geometry/notes/03_theta_bundles_and_connections/08_ADJOINT_RECURRENCE_ENDPOINT_EXPERIMENT_20261015.md
[results]: ../../../../../result-summaries/README.md
[arithmetic]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a09]: ../../../../../avoid/09_round_floors_and_fitted_laws.md
[a10]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
[large]: ../../../../../LARGE_FILES.md
[polymath]: https://arxiv.org/html/1904.12438v2#S1
[chat]: ../../../../investigations-2/formal_replay_crosswalk/chat-histories/0028_2026-10-17T03-47-38Z_audit-source-measurement.json
