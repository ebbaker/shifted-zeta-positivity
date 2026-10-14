# Continuation and the next signed theta estimate

14 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Recorded model: **gpt-6.1-sol (Codex)**; reasoning effort: **ultra**.


The next session should use **Codex in the existing local research
checkout**. The mathematical task is a bounded, fully paid estimate for
the genuine stationary Laguerre observations, using endpoint-compensated
theta channels while retaining every arithmetic cross term. The present
manuscript establishes the reformulations and central estimates; the
collision-excluding signed estimate at unknown heights remains open.

## Read first and preserve the conventions

Read the [manuscript](../manuscript/quaternion_theta_geometry.tex), especially
Sections 2--8 for the RH criteria and coordinates and Sections 11--15 for
the theta estimates, compensation, and remaining target. The
[manuscript audit](../reviews/4_MANUSCRIPT_CONVENTION_AND_FOUNDATION_AUDIT_20261014.md)
and [build record](../manuscript/BUILD_RECORD.json) identify the checked
version. Earlier derivations remain in [Note 3](3_STANDARD_FUETER_LIFT_WITH_INDEPENDENT_TIME_20261014.md),
[Note 4](4_CAUCHY_FUETER_BOUNDARY_AND_CURRENT_REFORMULATIONS_20261014.md),
[Note 5](5_COMPLETE_THETA_CENTRAL_ESTIMATE_20261014.md), and
[Note 6](6_IMAGINARY_GLUING_STABILITY_AND_HEIGHT_OBSTRUCTION_20261014.md).

Keep Newman time t external and real, with independent quaternion
coordinates and the adopted coupled lift

\[
q=z_0+\mathbf jz_1,
\quad z_0=a+ib,\quad z_1=c+id,
\quad q=a+\mathbf ib+\mathbf jc-\mathbf kd,
\]
\[
\bar\partial_q=\tfrac12(\partial_a+\mathbf i\partial_b
                         +\mathbf j\partial_c-\mathbf k\partial_d),
\qquad
F(t,q)=H(t+\overline{z_1},z_0)+\mathbf jH_z(t+\overline{z_1},z_0).
\]

Complex coefficients are on the right of j; complex coordinate
derivatives of quaternion fields act componentwise. The constraints are
\(U_{z_0}=V\), \(\bar\partial_qF=0\), and
\(F_t=-\partial_q^2F\). The physical trace and exact endpoint are

\[
F(t,x)=H(t,x)+\mathbf jH_x(t,x),\qquad
\mathcal E=|F(t,x)|^2=H^2+H_x^2,
\]
\[
\mathrm{RH}\iff F(t,x)\ne0\quad(t>0,\ x\in\mathbb R)
\iff \mathcal F(x+\mathbf js)\ne0\quad(s>0,\ x\in\mathbb R),
\quad \mathcal F=F(0,\cdot).
\]

This equivalence uses the genuine theta threshold and uniform
positive-time localization theorems, together with the proved local
Hermite splitting. It is pointwise nonvanishing and allows time-zero
multiple roots. It makes no assertion about all quaternion arguments.
The alternative whole-plane criterion concerns
\(\tfrac12\partial_y^2|P_0F(0,x+iy)|^2\), with
\(P_0Q=(Q-\mathbf iQ\mathbf i)/2\); replacing this scalar modulus
by the full quaternion norm loses the criterion.

## Established results and their limits

The scalar normalization is
\(H(0,z)=\xi(1/2+iz/2)/8\), with \(\partial_t H=-\partial_z^2H\).
For the physical derivatives \(h_j=\partial_x^jH\), put
\(\mathscr L_j=h_{j+1}^2-h_jh_{j+2}\), j=0,1.
The two global stationary signs, and equivalently their locally bounded
loss formulations, give exact RH criteria for this genuine theta family:

\[
h_{j+1}=0\ \Longrightarrow\ \mathscr L_j\ge0,
\qquad\hbox{or}\qquad
h_{j+1}=0\ \Longrightarrow\ \mathscr L_j\ge-K_j\mathcal E,
\]

where each nonnegative \(K_j\) must remain locally bounded through
candidate joint zeros. The two sign conditions combine into
\(\mathcal E_t\ge0\) on \(H_xH_{xx}=0\). The manuscript proves
the even/odd predecessor constructions and the divergent loss
\(r/(T-t)+O(1)\) that excludes every finite collision multiplicity.

The complete-source estimate proves

\[
M_2-\tfrac{25}{2}M_4>1/120000,
\qquad |F(t,x)|>1/120000\quad(0\le t\le1,\ |x|\le8),
\]

with the entire theta sum and integration tail paid. On \(|x|\le5\),
\(H_{xx}<-1/120000\), the first stationary set contains only zero,
and \(\mathscr L_0(t,0)>1/5000000\). This is a bounded central
diagnostic; it does not address arbitrary collision heights.

The full angular imaginary-gluing defect at one theta scale controls
all four physical jets absolutely, with constants bounded by
\((1/2,1/8,1/12,1/12)\). A defect at most 1/30000 preserves a
central norm gap of 1/240000 in the declared half-line observation
class. Arbitrarily small positive defects can nevertheless permit
remote joint zeros in that class. Those controls fail exact gluing and
smooth modular reflection. Thus an absolute defect tolerance cannot
give the all-height conclusion.

Cauchy--Fueter reconstruction, spherical moments, and conserved currents
retain the signed physical observation. Substituting the complete theta
source reproduces the original paired kernel. Its separate fixed-index
diagonals have negative algebraic Laguerre tails; cancellation between
indices is essential. Subharmonic norms, reciprocal arguments, or
quaternion zero nondegeneracy do not supply the required sign.

The 26-page manuscript compiled successfully and was visually checked.
All 58 coordinate algebra checks, 14 polynomial boundary cases, 17
central constant checks, and 22 gluing checks passed. These are internal
checks, with analytic proofs in the manuscript. The work is in the
working tree; no commit, tag, or manuscript snapshot was created.

## The next bounded construction

Use the initial target rectangle

\[
R=[1/100,1/20]\times[8,40],\qquad
R^+=[1/200,3/50]\times[7,41].
\]

Certify the two stationary observations on \(R^+\), whose interior
contains predecessor neighborhoods for every candidate collision in R.
Evenness transfers the result to reflected negative heights. These are
proposed test domains, not certified regions or a cover of every possible
positive threshold collision. They extend the current central diagnostic
and overlap it near x=8.

Start with two odd endpoint cancellations (K=2):

\[
\beta_0(u)=(u+u^3)e^{-u^2},\qquad
\beta_1(u)=\tfrac16u^3e^{-u^2},
\]
\[
g_{n,t}=e^{tu^2}\phi_n,
\quad b_n=\phi_n'(0),\quad e_n=\phi_n^{(3)}(0),
\quad
\widetilde g_{n,t}
=g_{n,t}-b_n\beta_0-(e_n+6tb_n)\beta_1.
\]

The beta functions have the required first/third derivative Kronecker
jets, and the complete theta sum cancels both subtractions. Define
\(\widetilde H_n=\int_0^\infty\widetilde g_{n,t}(u)\cos(xu)\,du\),
\(P_N=\sum_{n\le N}\widetilde H_n\),
\(p_k=\partial_x^kP_N\), and \(r_k=h_k-p_k\).
Start with N=3 and use manuscript equations (14.3)--(14.4) to pay every
omitted index and the source-integration tail. Its threshold
\(\pi(N+1)^2\ge8K+9\) is satisfied. Obtain rigorous bounds
\(|r_k|\le\varepsilon_k\), k=0,1,2,3, on every retained cell.
Interval or Taylor enclosures must also pay quadrature and rounding errors.

Split the finite observation exactly into diagonal and cross terms:

\[
\mathscr L_j(P_N)=D_j^N+X_j^N,
\]
\[
D_j^N=\sum_{n\le N}(a_{n,j+1}^2-a_{n,j}a_{n,j+2}),
\quad a_{n,k}=\partial_x^k\widetilde H_n,
\]
\[
X_j^N=\sum_{n<m\le N}
\left(2a_{n,j+1}a_{m,j+1}
-a_{n,j}a_{m,j+2}-a_{m,j}a_{n,j+2}\right).
\]

Do not presume a sign for either part. On the genuine stationary set
\(h_{j+1}=0\), one has \(p_{j+1}=-r_{j+1}\), giving the exact identity

\[
\mathscr L_j(H)=D_j^N+X_j^N-r_{j+1}^2
-p_jr_{j+2}-p_{j+2}r_j-r_jr_{j+2}.
\]

The first concrete sufficient target, for both j=0,1, is therefore

\[
X_j^N\ge-D_j^N+\varepsilon_{j+1}^2
+|p_j|\varepsilon_{j+2}+|p_{j+2}|\varepsilon_j
+\varepsilon_j\varepsilon_{j+2}
\quad\hbox{where }h_{j+1}=0.
\]

Cover the padded rectangle by rigorous cells. Exclude cells only when a
certified enclosure excludes stationarity; isolate regular stationary
branches when the required derivative is separated from zero. Retain
degenerate or unresolved cells explicitly. Use the full stationary
constraint above, rather than replacing it by truncated stationarity.
Increase N when the paid tail is limiting; subdivide or change the signed
decomposition when cancellation is limiting. No tabulated zero locations
or sampled signs decide a certificate.

If a sign estimate is unavailable, a bounded-loss alternative must prove
\(\mathscr L_j+K_j\mathcal E\ge0\) directly with an explicit finite
nonnegative coefficient. An uncontrolled quotient by the unproved norm
would be circular. Compensated finite channels generally fail the heat
equation; any use of ambient Fueter boundary reproduction on them must
retain the Borel--Pompeiu residual. Apply the exact heat collision theorem
to the complete source.

## Controls and completion criteria

Test claims based only on regularity or heat against shifted polynomial
controls, with a=24 and T=1/40 inside the proposed rectangle:

\[
Q_2(t,x)=(x-a)^2-2(t-T),\qquad
Q_3(t,x)=(x-a)^3-6(t-T)(x-a).
\]

They have double and triple collisions, respectively; on their relevant
predecessor branches the negative Laguerre-to-energy ratio is
\(1/(T-t)\). A successful genuine-theta estimate must identify the
source property these controls lack. Reuse the existing Euler and
approximate-gluing controls only within their declared source classes.

The deliverable is a derivation note with one genuinely signed cross-term
estimate on the declared domain, reproducible rigorous error payments,
and an internal review recording all unresolved cells and hypotheses.
If only absolute jet accuracy, source uniqueness, or sampled positivity
is obtained, record that narrower outcome and the remaining signed
remainder. A bounded success is not an all-height RH theorem.

## Session choice and repository continuity

My recommendation is Codex for this next pass: the task combines exact
repository conventions, source-integral derivation, reproducible rigorous
checks, saved notes and reviews, and research-history maintenance. Codex's
documented local workflow supports inspecting files, editing, and running
installed tools ([official documentation](https://learn.chatgpt.com/docs/cli)).
This is a workflow recommendation, not a claim that one interface has
greater mathematical ability. A subsequent ChatGPT session can provide
an independent conceptual critique supplied with the manuscript and this
note.

Use `/Users/ebbaker/Documents/shifted-zeta-positivity` as the existing local
checkout. Investigation 21 currently contains untracked working files and
there are other uncommitted repository changes. A new checkout from the
current Git commit would omit this uncommitted work. Read repository
`AGENTS.md`, `tools/CHAT_HISTORY.md`, and `LARGE_FILES.md`; save research in
`notes/`, rigorous calculations in `numerics/`, and assessments in
`reviews/`. Maintain one stable manuscript and the concise root history.

The founding [chat archive](../chat-histories/0007_2026-10-14T18-39-36Z_explain-rh-criteria-in-quaternionism.json)
now lives in this investigation, preserving its original identity,
number 7, filename, creation time, first-capture provenance, and all
earlier public messages. The [relocation record](../CHAT_HISTORY_RELOCATION_20261014.json)
documents the byte-preserving move. Future refreshes and investigation 21
conversations belong in this [history folder](../chat-histories/README.md).
Use the shared refresh tool at the beginning and end of replies, including
its bounded exact-turn final capture; do not hand-edit registered histories.

## Suggested next-session prompt

> Continue investigation 21 from
> `notes/7_CONTINUATION_AND_NEXT_SIGNED_ESTIMATE_20261014.md` in the existing
> local shifted-zeta-positivity checkout. Read the manuscript and its
> convention/foundation audit. Preserve the independent-time standard
> Fueter lift. Develop the K=2 endpoint-compensated four-jet bounds on the
> declared padded rectangle, then seek the stated signed cross-term
> estimate on both genuine stationary sets. Pay every index, integration,
> rounding and approximation remainder; retain unresolved cells and test
> general implications on the shifted double/triple collision controls.
> Save the derivation, reproducible rigorous checks, and an internal review
> in investigation 21. Record this new conversation in its chat-histories
> using the repository workflow. Report the precise bounded claim achieved
> and the remaining all-height obligation.
