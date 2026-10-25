# Manuscript integration instructions for GPT-6.1 Sol

24 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), actual effort max**,
verified from this chat's session metadata. Editorial handoff from chat
0006, thread `01a1704b-7af1-7931-a76c-38f570b1aeef`.

**Production request: HDA-10-MI1, revision 1.**

**Purpose.** Update the one maintained manuscript to incorporate the new
research results. This note describes the actual current TeX, the precise
insertions and replacements, the proof dependencies, and the checks needed
for a new export. It is an implementation specification, not a new
mathematical result or an independent review. The author has explicitly
chosen **GPT-6.1 Sol for manuscript production**. No new numerical research,
parameter search, onset certification or change of theorem is requested.
Ordinary manuscript production is permitted for either model by the
[root workflow][workflow]. Record Sol's actual model and effort when it
performs the work; this note does not establish those future settings.

## 1. Baseline, authority and scope

The maintained source is [manuscript/main.tex][main]. I read main.tex and
**all nine included TeX components**, including 09_local_transfer.tex,
which is included from 08_finite_time.tex rather than directly from main.
All ten TeX files match the source SHA-256 values in the existing
[build record][build-record]. That record describes the **28-page Note 23
integration**, not any subsequent analytical advance. Its SHA-256 at this
handoff is
`79c0a87d12cda8edd8ffd6c56d71e695e2445df6e8dbfcd0b1a8077649a9d5cf`.
Repository HEAD is `383aabaec68175138fdc5834108cd30e3a7c8e38`; the
post-build research is partly uncommitted, so HEAD alone is not its version.
The companion [input manifest][manifest] records the source bytes used.

The new mathematical sources are Notes **25, 26, 27, 28 and 30**.
**Author-directed scope freeze:** the author asked to leave this plan as
is and incorporate the newer positive-evolution results later. They are
therefore outside this revision, even if they now exist in the live tree. Notes 24 and 29
are continuation instructions, not additional theorems. Reviews 09--12
are same-assistant assessments of the corresponding research. They remain
such after integration. A successful Sol build is not independent
specialist mathematical review and does not complete HDA-20.

Read [AGENTS.md][agents], [LARGE_FILES.md][large], [the result index][results]
and [the avoid index][avoid], particularly [heat-flow results][geometry],
[collision controls][controls], [classification][a01], [scoped exclusions][a07],
[cancellation][a12] and [status synchronization][a19]. The gain is a set of
quantitative approximation estimates with stated domains, not an RH or
simplicity criterion. Preserve the existing failed diagnostic and all
historical evidence.

Use the live [progress register][progress] before editing. A separate
research chat is advancing the same investigation. Re-read inputs whose
hashes changed; do not overwrite another writer's progress, notes or
registry. Do not silently import an unfinished claim from a chat message.
Do not expand this revision to later mathematical notes; the author has
explicitly deferred them. A future integration revision must read their
statements, proofs and reviews before changing the scope. Preserve all unrelated worktree
changes. This handoff itself makes **no TeX changes and no new PDF claim**.

## 2. Editorial architecture and exact file responsibilities

The present paper has seven numbered sections, four appendices, and a
manual bibliography; 04_geometry_global.tex contributes two sections. Use labels, not those changing section numbers.
The integration should be organized by mathematical dependency, rather
than appending the research notes in their historical order.

Use this main input order; new files are proposals, not files already
present at the handoff:

```tex
\input{01_framework}
\input{10_global_protocol}
\input{02_negative}
\input{03_positive}
\input{07_explicit_clock}
\input{04_geometry_global}
\input{08_finite_time}
\input{11_gamma_outer_switch}
\input{12_full_gamma_saddle}
\input{14_scope_and_remaining_work}
\appendix
\input{05_appendices}
\input{06_references}
```

Keep `\input{09_local_transfer}` inside 08_finite_time.tex. Do not create
another manuscript or snapshot directory. New component numbers are file
identifiers, not a request to hard-code section numbers.

| File / existing anchor (baseline line) | Required change |
| --- | --- |
| main.tex, abstract (39--61), input sequence (64 onward) | Replace the obsolete scope summary; add the new inputs in the order above. Keep author, date and working-draft status honest. |
| 01_framework.tex, opening roadmap (11--26) | Rewrite the roadmap and source list for the final contents. Keep the exact fixed/adaptive equations and actual definition of Q. Add the static weak two-field identity after `eq:adaptiveWeak`. |
| **10_global_protocol.tex** (new), `sec:protocol` | Consolidate the fixed kernel, real source-saddle definitions and exact global regulator before either new endpoint theorem uses them. Move existing definitions with their labels; do not duplicate them. |
| 02_negative.tex, after `eq:adaptiveNegative` / end of file (139--155) | Add the Note 26 all-height adaptive evolution and covariance theorem, its finite budgets and proof. Keep the older fixed-regulator results. |
| 03_positive.tex, `eq:saddle` (54), `eq:kernel` (154) | Move those definitions to the protocol file; replace their old locations by references. Preserve the carrier theorem, fixed-regulator clock and all gates. |
| 07_explicit_clock.tex, `eq:positiveRegulator` (14), final paragraph | Move the regulator definition to the protocol file. Keep the exact finite phase and inner transport theorem. Add a forward pointer to the new static overlap theorem, without extending its transport domain. |
| 04_geometry_global.tex, `sec:global` (88), after `prop:obstruction` | Retain the fixed-regulator obstruction; add Note 25's quantitative contour and pre-switch observable tails before the xi-derivative hierarchy. Keep the hierarchy's fixed-regulator contract. |
| 08_finite_time.tex, first subsection (9--47), `prop:fixedsource` (270), closing paragraph (290--296) | Move the common protocol to 10; keep the finite-time method and failed trial. Add the distinct fixed-time/large-height positive-cutoff potential obstruction after the existing large-time obstruction. Replace the obsolete closing scope paragraph. |
| 09_local_transfer.tex | Retain the cellwise, amplitude-aware, actual-covariance and evaluation estimates, and the failed 192-cell diagnostic. No new numerical run or changed tolerance is authorized by this integration. |
| **11_gamma_outer_switch.tex** (new), `sec:gamma-outer` | Present the linearized gamma pair, compact/joint static comparison, reusable arbitrary-positive-q collar lemma, finite phase formula and resolved switch law from Notes 27--28. |
| **12_full_gamma_saddle.tex** (new), `sec:full-saddle` | Present Note 30's full saddle, all-height static theorem, full contour proof, regulator payment, inner overlap and exact residual. |
| **14_scope_and_remaining_work.tex** (new), `sec:remaining` | State the current coverage and remaining obligations once, with a short domain/error table. Use the latest accepted scope in this handoff, not historical open-task paragraphs copied from old notes. |
| 05_appendices.tex, `app:numerics` (114), `app:scope` (153), acknowledgment (204) | Keep historical numerical evidence; append an explicit provenance distinction for the new analytical results. Extend the source crosswalk, controls and preparation record. |
| 06_references.tex | Add the new mathematical notes and the actual primary sources used. This is the bibliography the PDF reads; editing references/references.bib alone has no effect on it. |

A compact proof may refer back to a previously stated lemma in the paper.
It must still show the argument's decisive estimates. Do not replace the
new main results by a paragraph saying that details are in the notes.
Long finite constants can be moved to an additional appendix within
05_appendices.tex if needed, with explicit references from the theorem.
Preserve the complete-source and regulator steps in the main argument.

## 3. Common definitions and notation: make these changes first

### 3.1 Move the kernel and global protocol, without changing them

Create `10_global_protocol.tex` with
`\section{A common regulator and spatial averaging protocol}\label{sec:protocol}`.
Move the compact kernel display `eq:kernel` from 03_positive.tex, including
its normalization, C3 regularity and **bounded weak derivatives through
order four**. State that all new endpoint/outer results use fixed positive
ell,h and a fixed spatial convolution K. General fixed space-time filters
in Section `sec:framework` remain a separate exact framework; the new
theorems are not automatically time-averaged evolution theorems.

Move `eq:saddle` from 03 and `eq:positiveRegulator` from 07 here. In the
latter, write the exponent of M_0 explicitly as
`t L^2+9L-pi exp(4L)` so this definition does not depend on the later
source exponent `q_t(u)`. Keep the labels intact. Keep `p=pi/L` as the
lattice-spacing definition in 07, or explicitly recall it there after
the move. Retain L'=2L/kappa and the displayed kappa' formula where
used in the differentiated clock proof.

Move the entire first subsection of 08 (`One regulator for both
endpoints`) here, including the saddle-existence check at 64, the flat
switch construction, the exact identity with epsilon_+ from 128, and the
negative comparison with eta C_T. Preserve `eq:globalRegulator` exactly.
Add the useful notation from Note 25 OH12 / Note 28 JT1:

\[
\epsilon_g(t,x)=E_0(t)e^{-\beta(t)x^2/2},\qquad
\beta(t)=\begin{cases}0&t\le64,\\ \chi(t)/\kappa(t)&t>64,\end{cases}
\]

with E_0=epsilon_b for t<=64 and
`E_0=epsilon_b^(1-chi)(M_0/kappa)^chi` above 64. Explain that 32, 64 and
128 appearing later have different roles: an analytical time floor, and
two chosen regulator switch points. None is a certified asymptotic onset.
The regulator is smooth at each finite point but has no positive spatial
floor over an unbounded height tail once t>64.

Replace the removed subsection in 08 by a short reference to this common
protocol and its positive floor on a **compact full buffer**. The later
source/interpolation definitions and comparisons remain in 08.

### 3.2 Keep these symbols distinct

| Symbol in the integrated paper | Meaning and precaution |
| --- | --- |
| H, s=(1+iz)/2 | Canonical complete field; H(0,z)=xi(s)/8 and H_t=-H_zz. Height is x, not y. |
| q=epsilon_g^2, r=log q | Regulator quantities; distinct from the source exponent q_t(u). |
| M_0 | Real source-saddle mass in the inner model and regulator. |
| mathcal M(w) | Exact gamma factor `w(w-1) pi^(-w/2) Gamma(w/2)/16`; neither M_0 nor Polymath's Stirling model. |
| alpha(w) | mathcal M'/mathcal M. Earlier alpha=mu'/mu is local to the inner proof; name this explicitly or rename the inner drift alpha_in. |
| P_lin(t,z) | The gamma pair called P in Notes 27--28. Use P_lin to avoid confusion with the existing finite lattice P(p,x). |
| P_*(t,z) | The different, full-saddle field of Note 30. Do not substitute it into the previously proved switch-center formula without a new estimate. |
| mathfrak p_t(w) | Suggested name for Note 30's complex saddle p_t(w), avoiding confusion with lattice spacing p=pi/L. Rename consistently in every derivative and residual. |
| A_X, mathcal A, Theta, omega | Amplitude and phase of the specified model; mark lin or * when both occur in one section. |
| B_2^Phi | Suggested name for the complete-source second derivative constant, to distinguish it from the composition bounds B_m in Note 26 and the saddle determinant B. |
| mathcal E_* | Exact heat residual `(partial_t+partial_zz)P_*`; distinct from the density R and from a bound on an error. |

Use common observable notation `S_F=log(|F|^2+q)`,
`w_F=q/(|F|^2+q)`, `U_F=K*S_F`, `W_F=K*w_F`,
`rho_F=q|F_z|^2/[pi(|F|^2+q)^2]`, `R_F=K*rho_F`.
Every comparison uses the **same physical q** on its two fields.
Keep physical potential offsets; no arbitrary harmonic correction or
mass normalization is allowed. A carrier normalization inside a proof
must not silently change q.

### 3.3 Add the static weak identity in the framework

After `eq:adaptiveWeak`, add a lemma with proposed label
`lem:holomorphic-weak-density`, from Note 28 JT17 (also Note 30 FS24):

\[
4\pi\langle\rho_F,\psi\rangle
=\int S_F\Delta\psi+2\int w_F\nabla r\cdot\nabla\psi
 +\int\{w_F\Delta r+w_F(1-w_F)|\nabla r|^2\}\psi.
\]

It holds for any holomorphic F on the full test buffer; it needs no heat
equation. Derive it from the already proved spatial curvature identity.
This is why it can be used for P_lin and P_* although their heat residuals
are nonzero. Keep the existing adaptive potential/current equations for
H and exact heat fields. Do not apply them unchanged to a residual-bearing
model; deriving and integrating its full evolution comparison is outside
this revision.

## 4. Negative endpoint: expand 02_negative.tex

Preserve `thm:negative`, `eq:Eminus`, `cor:negative`, and the fixed-region
covariance expansion. Their fixed-epsilon errors and scales are valid
under their own hypotheses. The new global adaptive theorem does not
replace O(T^-3) in the fixed-regulator density theorem by O(T^-2).
They measure different regularizations and domains.

After the current crossover subsection, add
`\subsection{All-height comparison of the adaptive evolution}` and
`\subsection{Cancellation in the actual filtered covariance}`.
Use proposed labels `thm:negative-evolution`, `lem:negative-spatial-jets`
and `prop:negative-covariance`.

State the contract before the estimates: t=-T, fixed eta>0,
0<=A_0<A, all real x, |y|<=A_0 sqrt(T), fixed ell,h, and
`T>=max(1,(h/(A-A_0))^2)`. Supply the full |y|<=A sqrt(T) convex buffer.
Time derivatives are at fixed physical coordinates, not along the
expanding boundary. Use the **exact**
`epsilon_g(-T)=eta C(1+T^2)^(-1/4)`, with
`r_t=T/(1+T^2)`, for both H and the existing Gaussian G_T.

Include the Gaussian current in Note 26 NE4, not merely its density,
and define its covariance from its actual potential as in NE5.
State the following absolute comparison table as one theorem:

| Observable difference | Uniform error | Source |
| --- | --- | --- |
| R_H-R_G | O(T^-2) | NE10--NE12 |
| J_H-J_G | O(T^-5/2) | NE10--NE12 |
| (R_H)_t-(R_G)_t | O(T^-3) | NE11--NE12 |
| U_H-U_G, W_H-W_G | O(T^-1) | NE13 |
| (U_H)_t-(U_G)_t | O(T^-2) | NE13 |
| K*(B_H-B_G) | O(T^-2) | NE14 |
| K*(S_epsilon,H-S_epsilon,G) | O(T^-3) | NE14 |
| K*Delta(B_H-B_G) | O(T^-3) | NE18a--NE18b |
| Q_H-Q_G | O(T^-3) | NE19--NE21 |
| Delta(Q_H-Q_G) | O(T^-4) | NE22--NE23 |

Here B denotes the adaptive potential forcing, not the composition
constant or saddle determinant. Use the manuscript's existing
`mathcal B_epsilon` and `mathcal S_epsilon` names in the final table.
Spatial curvature corrections vanish exactly at these negative times.
The first three natural upper scales are T^-1, T^-3/2 and T^-2;
scaled errors improve each by T^-1, without a pointwise relative claim
at zeros of a reference observable.

The proof must contain the following, in this order:

1. Extend the existing B_2 source remainder to **jets j=0,...,4**, with
   d_j,P_j from NE6--NE7. Define u_j=P_j/e and v_j=d_j/e only as algebraic
   bounds; H/e is not an exact heat field. Display the finite density,
   current, time and potential budgets NE10--NE14.
2. Include the finite composition constants C_m and partition formulas
   NE15--NE18, including the fifth scalar derivative needed for the
   difference of fourth spatial derivatives. These give
   `D^m S=O(T^(-m/2))` and
   `D^m(S-S_G)=O(T^(-m/2-1))`, m=1,...,4. Include NE18a--b for the
   differentiated forcing, rather than sacrificing that rate by moving
   every derivative to the kernel.
3. Display the two-point covariance identity NE19 and its Lipschitz
   bound with sigma_K^2. Derive the exact finite error bounds
   `4 sigma_K^2 B_2 D_2` and
   `16 sigma_K^2 B_3 D_3+8 sigma_K^2(B_4 D_2+B_2 D_4)`.
   Use NE22 for the differentiated covariance before estimating it.
   Separate bounds on squared first gradients lose the claimed power.
4. Conclude with the exact Gaussian adaptive equations NE24, all required
   spatial derivatives/traces on the full buffer, and the physical
   additive normalization. No moving-domain transport formula is implied.

This is a direct comparison with an actual field/covariance, not an
autonomous closure in R. It gives no zero-count statement for the
zero-free Gaussian and no earlier-time collision exclusion.

## 5. Outer tails and two different compact-source obstructions

### 5.1 Add quantitative tails to 04_geometry_global.tex

After `prop:obstruction` and its scope paragraph, add a subsection
`Quantitative tails before the spatial regulator switch` with
`lem:contour-jets` and `thm:preswitch-tail`.

Import Note 25 OH2--OH3: for a **fixed compact** I=[t_a,t_b], bounded
transverse full buffer and 0<a<=pi/16,
`|partial_z^j H|<=A_j(I,Y,a) exp(-a|x|)`.
Give A_j explicitly, in the text or an immediately referenced appendix.
Its field statement holds on any fixed compact time interval. The
observable theorem uses t_b<=64, where a uniform-in-height regulator
floor exists. Do not claim constants uniform as t_b tends to infinity.

The contour proof must retain even analytic reflection, all theta modes,
the full Fourier contour, both vertical ends and the differentiated
weights. A half-line shift that drops its endpoint does not prove OH3.

For the fixed kernel put E=exp(-a max(|x|-ell,0)). Display the regulated
background `(R,J,U,W,Q)=(0,0,r,1,0)` and the finite allowances OH6--OH9:
linear observables, their directly computed time derivatives and the
forcing/source errors are O(E^2); Q and Delta Q are O(E^4), with the
kernel-derivative coefficient in OH9. Retain the actual covariance
comparison and the full support margins. Give OH11 as one explicit
example of a tail threshold for a prescribed density error.

Call this a regulated measurement background. Do not assign a zero
measure to the identically zero reference field or infer absence of high
zeros. Keep the old fixed-epsilon obstruction, whose scope is different.
Keep the xi-derivative hierarchy that follows, with its original fixed
positive regulator assumptions and separate evaluation cost.

### 5.2 Add the large-height potential obstruction to 08_finite_time.tex

The existing `prop:fixedsource` concerns **t tending to infinity at a
fixed spatial buffer**. Keep it. Immediately after its scope paragraph,
add `prop:cutoff-potential`, entitled, for example,
`Positive-cutoff obstruction at fixed positive time`.

State precisely Note 25 OH13--OH17: fix t>64, a finite continuous
piecewise-linear source on [0,U_s] with f(U_s)>0, extend it by zero, and
observe at a fixed y_*>h with the whole off-axis buffer. Then

\[
H_f(t,z)=e^{tU_s^2}f(U_s)\frac{\sin(U_s z)}z+O(|z|^{-2}),\qquad
U_f(t,x,y_*)-U_H(t,x,y_*)\ge2ax-2\log x-O(1)\longrightarrow+\infty.
\]

Give the explicit B_f remainder and the full OH17 inequality, including
horizontal and transverse margins. The proof pays every cell derivative
jump and both end derivatives, uses the off-axis sinh lower bound, then
compares the physical logarithms against the complete-source contour
upper bound. This is a failure of the representation for **absolute
source-anchored potential**, not just a failed numerical allowance.

After the proposition, explicitly retain its exclusions from scope:
no density-only impossibility, no assertion at y=0, no result for a
smooth zero-endpoint taper, moving cutoff or arbitrary noncompact model.
It does not contradict compact-buffer finite-time approximability.
A constant or arbitrary harmonic correction cannot be introduced to
change the physical potential contract. The new noncompact gamma models
are outside the excluded class.

## 6. Linear gamma model, uniform transfer and switch: new file 11

Use `sec:gamma-outer` and the subsections below. These results remain
useful even after the stronger full saddle is presented: they provide a
simple finite phase density and the explicit regulator-layer law. The
old exponential joint threshold is **not** the final paper's current
spatial limitation.

### 6.1 Exact source identity and linear model

State `H=(pi t)^(-1/2) int_R exp(-v^2/t) xi(s+v)/8 dv`, t>0,
and define

\[
\mathcal M(w)=\frac{w(w-1)}{16}\pi^{-w/2}\Gamma(w/2),\quad
\alpha=(\log\mathcal M)',\quad
\mathcal G_t(w)=\mathcal M(w)e^{t\alpha(w)^2/4},\quad
P_{\rm lin}=\mathcal G_t(s)+\mathcal G_t(1-s).
\]

Proposed labels: `eq:xi-heat-convolution`, `eq:gamma-linear` and
`prop:linear-field-budget`. Preserve the factor 1/16 and variance t/2.
Explain the factor's relation to xi/8. Cite Polymath (35) for the exact
identity; do not import its 0<t<=1/2 high-zero theorem at t>64.

Give the compact error GO7 and the time-dependent budget JT10--JT11,
relative to `|G_t(s)|+|G_t(1-s)|`, **not |P_lin|**. The four payments in
JT11 must be visible: local gamma expansion with its exp(t) loss, the
complete arithmetic tail, the bounded middle/lower tail, and the infinite
right Gaussian tail. Keep both reflected arms. The compact estimate has
constants depending on its fixed interval. On `32<=t<=log X/4`, the
paid bound is `O(X^(-3/4)(1+log^4 X))`; on fixed [32,T] it is
`O_T((1+log^2 X)/X)`. Neither formula has a numerically supplied onset.

### 6.2 Phase and an arbitrary-regulator collar lemma

Use GO17--GO22 / JT12 to construct the nonvanishing carrier and phase,
`P_lin=2 mathcal A cos Theta`, with real phase on the real axis,
`omega=theta_x=(1/4)log(X/(4pi))+O(t log X/X)` on the joint range.
Retain a holomorphic full buffer, bounded carrier logarithmic derivative,
small phase curvature, all actual simple roots, O(omega) collar counts,
root shifts O(error/omega), and physical exterior/interior floors.
A small absolute field estimate alone is not this geometry.

Then state and prove `lem:uniform-q-collar` from JT13--JT16. In the
phase-scaled disk, compare u B(u) and (u-e_0) C(u) with their bounded
zero-free units, for **any positive function Q(u)**. Replace the unit
first; translate the root while holding Q fixed. Include the two
integrable derivative bounds `2|e_0|/|u-se_0|` and
`|e_0|/(2|u-se_0|)`. Account for omega^-2 area and O(omega) disks.
This yields the L1 bound for S and w, uniformly in the regulator.
It is a simple-root lemma, not a new multiple-event theorem.

Apply `lem:holomorphic-weak-density` with the two retained spatial
regulator corrections. For beta X bounded, its coefficients are bounded.
For beta X large, separately pay each field's bias relative to its own
zero measure with the actual collars; copy JT19--JT21's regulator
estimates. Do not use an unbounded weak-test constant and assert uniformity.

State `thm:linear-static` with JT4--JT5 and the spatial U,W jet corollary
JT18a through order four. The proof transfers bounded weak derivatives
of K onto the L1 difference. This static statement alone says nothing
about unfiltered gradient products or time derivatives.

### 6.3 Retain the exact finite phase result

State `cor:outer-finite-phase` on each compact I strictly inside (64,infinity).
Set p_out=pi/omega and v_out=theta/omega. Reuse the **existing** exact
periodization `P(p,x)` from `eq:finiteP` as `P(p_out,v_out)`; no need to
print a second copy of its five coefficients. The density model is
`k_h(y)P(p_out,v_out)`, with absolute error
`O_I((1+log^2 X)/X)` from GO31. The phase-free consequence GO32 has the
additional error O((log X)^-4). The weaker generic periodization bound
in the old fixed-regulator section is not a reason to change this sharper
finite-polynomial rate.

Mention the t>=128 portion of the JT4 joint range where the same resolved
phase argument applies. Do not use the zero-lattice formula throughout
the unresolved regulator layer. Keep x<0 by the actual symmetries.

### 6.4 The two-layer law and its exact center

Add `thm:regulator-layer` for JT22--JT24 and `cor:switch-scaling` for
JT26--JT33. These are distinct accuracy statements from the vanishing
static error above. With **linear-model** A_X and omega, set

\[
b=\log(\epsilon_g/A_X),\quad d=b_+/\omega,\quad
R_{\rm layer}=\frac{\omega}{2\pi}
 \{k_h(y-d)+k_h(y+d)\}.
\]

Its absolute error is O(1), uniformly on the declared joint range or a
fixed compact [32,T], not O(X^-3/4 log^4 X). Dividing by log X gives
O(1/log X). The potential comparison with
`2 log|mathcal A|+2 max(b,omega|v|)` in JT25 is the proof; retain the
harmonic carrier, the adaptive corrections and the horizontal average.
The off-axis layers are regularized density, **not nonreal zeros**.

Define t_c(X) by the exact known-model equation
`epsilon_g(t_c,X)=|G_(t_c)((1+iX)/2)|` in its specified small right
neighborhood of 64. Include

\[
t_c-64=\frac{64}{\log X+c_0+O(1/\log X)},\qquad
c_0=\log\frac{4e}{\pi\kappa(64)},\qquad
 t_X(\tau)=t_c-\frac{128\tau}{\pi X\log X},
\]
\[
\frac{R_H(t_X(\tau),X,y)}{\log X}
 =\frac{k_h(y-\tau_+)+k_h(y+\tau_+)}{8\pi}
   +O(1/\log X).
\]

The second statement is uniform for bounded tau,y with the stated strip.
Include the directly computed b_t, beta'/beta and b_tt allowances in
JT28--JT31, which pay the Taylor error. **Do not replace the exact t_c
in t_X by 64+64/log X or a short inverse-log series**: its omitted error
is much larger than the layer width 1/(X log X). Do not change A_X to
the full-saddle amplitude inside this center definition. That would need
a separate recentering argument.

Derive GO33's fixed-time normalized jump as a consequence/remark, with
no discontinuity of H at finite height. It is a nonuniform limit created
by the chosen regulator, not a forbidden interpolation or an RH statement.

Close with the exact linear-model heat residual JT34--JT36. Label it
`eq:linear-heat-residual`, retain all coefficients, and say explicitly
that P_lin is not an exact heat solution. Explain that its proved joint
range X>=exp(4t) does not overlap the polynomial inner window; **the next
section removes that restriction using a different model**. Do not leave
this historical limitation as the paper's final scope statement.

## 7. Full saddle and actual static overlap: new file 12

Use `sec:full-saddle`. Lead with the quantitative improvement, then prove
it. This is Note 30 FS1--FS34, not a new extension of Note 28's theorem.

### 7.1 Model, branch and main statement

For t>=32, X=|x|, write
`mathcal R=2+t+X`, `mathcal L=log mathcal R`,
`N_*=1+X+t mathcal L`, `e_*=t^(3/2)/N_*^2`.
Use distinct N_* and e_* names here so they are not confused with the
finite number of source modes or an earlier regulator floor. Specify the
full fixed holomorphic and averaging buffer from FS1--FS2.

Define the large branch and its determinant exactly:

\[
\mathfrak p_t(w)=w+\frac t2\alpha(\mathfrak p_t(w)),\quad
v_* =\mathfrak p_t(w)-w,\quad
B=1-\frac t2\alpha'(\mathfrak p_t(w)),
\]
\[
\mathcal S_t(w)=\frac{\mathcal M(\mathfrak p_t(w))e^{-v_*^2/t}}{\sqrt B},
\qquad P_*(t,z)=\mathcal S_t(s)+\mathcal S_t(1-s).
\]

The square root is near 1. Prove existence and uniqueness **in the FS9
rectangle**, with reflection for negative imaginary parts and holomorphic
extension on overlapping buffered domains. Do not assert uniqueness among
all meromorphic saddle solutions or an entire global model. Include the
fixed sector, positive imaginary-increment check, and contraction ratio
O(1/log mathcal R). Suggested label: `lem:full-saddle-branch`.

State `thm:full-saddle-static` with C,R_* depending only on fixed widths,
transverse buffer and regulator parameter, independent of t,x:

\[
|R_H-R_{P_*}|+\sum_{|\gamma|\le4}
\bigl(|\partial^\gamma(U_H-U_{P_*})|
      +|\partial^\gamma(W_H-W_{P_*})|\bigr)
\le C\frac{t^{3/2}}{(1+X+t\log(2+t+X))^2}
\]

for t>=32, 2+t+X>=R_*, |y|<=Y. Gamma is **spatial** here. Pair it with
the holomorphic field bound FS7 relative to the sum of the two carrier
amplitudes. The formula still requires a uniquely specified implicit
special-function saddle and a fixed spatial average; do not call it a
finite elementary closed formula or a density-only autonomous model.

### 7.2 Proof that must survive condensation

Retain the following chain, using named lemmas rather than one large
unexplained asymptotic argument:

1. **Field estimate before regulator transfer.** Split the exact
   convolution at real parts 2 and -1. Reflect one arm. Shift each arm
   to its complex saddle while paying both finite connectors and the
   vanishing right faces; no singularity is crossed. Preserve the bounded
   middle and the full Dirichlet-series tail.
2. **Exact saddle cancellation.** Display FS14,
   `exp(-B u^2/t+E_p(u))`, with FS13's cubic remainder and a separate
   Gaussian majorant on the whole allowed half-line. The quadratic
   determinant B^(-1/2) is essential. Integrating the cubic remainder
   yields t^(3/2)/N_*^2 without the earlier exp(t) loss. Do not use a local
   Taylor expansion at arbitrary u without its global majorant.
3. **Remaining pieces.** Show FS16--FS19's horizontal-left,
   connector/middle and arithmetic estimates, then the three-part FS20
   budget before absorbing it. The fact that t log2/8>2 for t>=32 pays
   the arithmetic absorption; it is not a known zero threshold.
4. **Collars and static potential.** Differentiate the actual implicit
   formula FS21--FS22. The bounded logarithmic carrier derivative uses
   cancellation. Obtain all simple real roots on the enlarged strip,
   including edge collars. Apply the already proved arbitrary-q lemma
   to get FS23 and spatial U,W jets.
5. **Density with the common physical regulator.** Split beta X at a
   sufficiently large fixed B_0, not necessarily Note 28's pi. In the
   bounded regime use the weak identity. In the other regime use the
   independent field theorem at x=0 and the earlier complete-source mass
   bound to prove A_0 comparable to M_0 (FS26). Then pay the amplitude
   variation and Gaussian regulator by FS27--FS28. The mass comparison
   belongs **after** the field proof; it cannot define or fit P_*.
   Cover the remaining compact time interval separately. Bound both
   models' regularization biases and their zero displacement.

For a self-contained mass anchor, explicitly state the consequence of
Note 12 (3)--(6), `H(t,0)/M_0=1+O(kappa^-1/4)`, and obtain it from the
existing appendix's complete-source normalization estimate. Do not refer
to the measured value H(t,0) as an input to the new model.

### 7.3 Corollaries and retained residual

Add `cor:full-saddle-limits` with all three quantitative regimes:

- uniformly over all real x at sufficiently large t:
  O(t^-1/2 log^-2(2+t));
- uniformly over t>=32 at sufficiently large X:
  O(X^-1/2 log^-3/2(2+X));
- on each fixed [32,T]: O_T(X^-2).

They apply to static density and the stated U,W spatial jets. Include
FS30's elementary rescaling argument. Onsets are eventual and not
numerically instantiated; a large-time result includes small x because
t itself then meets the domain condition.

Add `cor:inner-static-overlap` with FS31. Both models use exactly the
same q at sufficiently large time. On the original buffered inner window,

\[
\|R_{P_*}-R_L\|\le C\kappa^{-1/2}
   +Ct^{-1/2}\log^{-2}(2+t)=O(\kappa^{-1/2}).
\]

Give the nonempty eventual overlap `2X_*<=|x|<=X_in(t)/2`, with all inner
source/carrier gates retained. The triangle inequality through the same
physical density proves matching; no termwise equality of unrelated
expansions or fitted phase is needed. This closes the **static positive
spatial gap**, not the finite-time transition.

Finally display FS21, FS32 and the exact residual FS33:

\[
(\partial_t+\partial_{zz})P_*=
-\sum_{w=s,1-s}\mathcal S_t(w)
 \left\{\frac{t\alpha'''(\mathfrak p_t(w))}{16B^3}
 +\frac{5t^2[\alpha''(\mathfrak p_t(w))]^2}{64B^4}\right\},
\]

with its carrier-relative bound O(t/N_*^3). Use label
`eq:full-saddle-residual`. Preserve the sign, 16 and 5/64 coefficients,
and evaluate B separately at each branch. The residual is nonzero.
Static estimates must not be differentiated to create transport claims.
Later positive evolution results are expressly deferred by the author.

## 8. Frozen scope: later positive evolution belongs to a later revision

During preparation, a separate research chat was developing positive-time
current, time-derivative and covariance estimates. The author then
instructed: **“Leave it as is, we will incorporate the new results later.”**
This handoff is therefore frozen at the completed source set in Section 1:
Notes 25--28 and 30, with Reviews 09--12. It contains no theorem from that
ongoing positive-evolution work and makes no claim to assess it.

For this manuscript integration, the positive all-height **static**
comparison and static inner overlap are included; the later positive
all-height **evolution** comparison is deferred. Do not add
13_positive_evolution.tex, insert an announced rate from another chat, or
rewrite the conclusion around a source outside the manifest. Keep the
nonzero exact residuals and the explicit static/evolution distinction.

The manuscript should identify its coverage as “results through Note 30”
so its remaining-work statements describe the integrated source scope.
If later notes have closed a listed obligation, the current project
README/progress must distinguish “proved subsequently, not integrated in
this version” from a globally open research problem. Preserve the live
research ledger's newer statuses; never roll them back to this frozen
manuscript scope. That reconciliation is documentation, not permission to
incorporate the deferred mathematical results.

A future manuscript revision can add the later result after reading its
saved proof and review and specifying its domains, residual corrections,
source dependencies and limits. That work is not part of HDA-10-MI1 r1.

## 9. Abstract, introduction and conclusion: replace claims, not only append sections

Keep the current title, **Averaged densities for the theta heat flow:
explicit asymptotics and finite-time approximation**, unless the author
asks to change it. It still describes the integrated work. Keep Edward
Baker in the author field (`Drafted for Edward Baker` is the existing
form), and preserve a candid working-draft/review qualifier.

The abstract must now contain these concrete gains, in this order:

1. The same canonical unnormalized field and exact adaptive-regulator
   identities, with actual covariance retained.
2. Negative all-height Gaussian comparison including current, time
   derivatives and covariance, not just static density.
3. The existing explicit inner phase/current formula and its original
   O(kappa^-1/2), O(L kappa^-7/6) rates and growing-window domain.
4. The noncompact gamma construction, the improved full-saddle static
   all-height rate O(t^-1/2 log^-2 t), and actual static inner overlap.
5. The regulator-layer resolution, and the source-local finite-time
   construction with the scoped positive-cutoff obstruction.
6. The transition/assembly, positive-evolution, autonomous-closure, onset
   and review limitations of the **integrated source scope**, explicitly
   identified as through Note 30. Later project research is deferred under
   Section 8 and must not be silently imported.

For this version through Note 30, the following is a complete replacement
abstract:

> We develop quantitative approximations to the unnormalized regularized
> zero density of the canonical theta heat flow under one smooth
> time- and height-dependent regulator. Its potential forcing, spatial
> curvature correction, current source and actual filtered covariance are
> retained. At negative time, a Gaussian field approximates density,
> current, their required time terms and the physical potential uniformly
> over real height; covariance and covariance-Laplacian errors are
> O(T^-3) and O(T^-4). An explicit finite Bernoulli formula retains the
> positive inner clock phase and gives density error O(kappa^-1/2) and
> current/time error O(L kappa^-7/6) on buffered windows of size
> kappa^(1/3). A noncompact full gamma-saddle field gives static density
> and averaged-potential spatial-jet error
> O(t^(3/2)/(1+|x|+t log(2+t+|x|))^2), yielding an all-height positive
> endpoint and static overlap with the inner clock. A separate gamma
> approximation resolves the chosen regulator's thin time/height switch
> layer. Complete-source finite-time fields retain direct observable
> comparison bounds, while a fixed positive source cutoff is excluded
> from an off-axis all-height potential contract. Positive endpoint
> evolution and all-time transition assembly are not established by the
> results consolidated in this version. No autonomous density closure is
> asserted. Onsets are eventual, numerical support remains diagnostic,
> and no earlier-time simplicity conclusion is drawn.

Convert this prose and its mathematical expressions to normal LaTeX;
do not paste Markdown syntax into the TeX. The final abstract should
remain a coherent paragraph, not a task ledger or catalogue of note IDs.
State the through-Note-30 coverage in the introduction and source
crosswalk, and retain the version-specific limitation in the abstract.

In 01_framework.tex replace the two roadmap paragraphs and the incomplete
source list. Explain the distinction between fixed-regulator preliminaries,
the common adaptive measurement, the inner differentiated clock, the
static full saddle, and the finite-time problem. Include Note 23 in the
source list (the present opening list omits it although the manuscript
already uses it), then the actual newly integrated mathematical notes.
Avoid claiming that every result uses the same domain or regulator as the
older fixed-epsilon theorems.

The following exact stale statements must be removed or qualified in the
**current** manuscript and current README; they remain valid historical
statements in their dated notes:

| Existing wording / location | Required disposition |
| --- | --- |
| main.tex abstract: `an outer-height positive-time profile ... remain open` | Replace by the proved static gamma profile/full-saddle coverage, with its quantified domains. |
| 08_finite_time.tex final paragraph: `a positive outer-height model` is a remaining task | Replace by the remaining finite-transition/evolution obligations appropriate to Section 8. |
| manuscript/README.md: `positive outer heights ... remain open` | Update after a successful new build to identify the incorporated result and current limitations. |
| manuscript/README.md and continuation summaries: `missing inner overlap` | Mark this as the pre-Note-30 state; current static inner overlap is FS31. |
| Any current summary that gives X>=exp(4t) as the final outer threshold | Attribute it specifically to P_lin/JT4 and point to P_*'s stronger domain. |
| Any current claim that positive potential spatial comparison is absent | Replace by JT18a/FS6; this is distinct from potential time comparison and actual covariance. |
| Any claim that an exact heat residual of zero is enough for approximation | Keep the two fixed-source counterexamples and require the direct source error. |

Create `14_scope_and_remaining_work.tex` with a concise coverage table.
Include negative all-height evolution; compact pre-switch tails; inner
phase/transport; linear-model compact/joint static and switch results;
full-saddle joint static, all-height late-time and overlap; finite-slab
source comparisons. Positive evolution beyond these sources is deferred. Each row
needs its domain, target observable, error and theorem reference.

The closing paragraph must distinguish **same-time spatial overlap** from
**overlap through finite heat times**. A regulator smoothly defined for
all t is not an all-time approximation theorem. The failed 192-cell trial
remains failed. A future splice must pay the actual cutoff/time-derivative
and heat-residual terms; do not build a blend during this production task.
Respect the source-version distinction in Section 8; HDA-17 acceptance,
HDA-18 assembly and HDA-20 independent specialist review do not follow
from typesetting the new results. Keep the absence of an autonomous
covariance closure and of any RH/earlier-simplicity conclusion explicit.

## 10. Source crosswalk, bibliography, controls and acknowledgment

### 10.1 Source crosswalk

Extend `app:scope` with this mapping. It should be a short text/table,
not another copy of the proofs.

| Source | Distinct material that must appear in the manuscript |
| --- | --- |
| [Note 25][n25], OH2--OH11 | Complete contour jets; pre-switch physical tails including actual covariance, sources and traces; explicit tail threshold. |
| Note 25, OH13--OH17 | Positive-cutoff asymptotic and scoped fixed-time off-axis potential obstruction. |
| [Note 26][n26], NE1--NE24 | Exact-regulator negative endpoint, direct time budgets, composition jets, covariance cancellation, forcing/traces. |
| [Note 27][n27], GO4--GO26 | Canonical convolution, exact gamma pair, carrier-relative error, physical collars and regulator bias. |
| Note 27, GO27--GO33 | Finite phase formula, continuum error, fixed-time nonuniform switch limit. |
| [Note 28][n28], JT10--JT21 and JT18a | Time-dependent linear-pair budget, arbitrary-positive-q lemma, static potential jets and two regulator regimes. |
| Note 28, JT22--JT33 | Two-layer shape, exact implicit center, width and rescaled switch law. |
| Note 28, JT34--JT36 | Exact nonzero linear-pair heat residual; its range is a historical sufficient bound. |
| [Note 30][n30], FS3--FS20 | Implicit full saddle, branch and determinant; both deformed arms/connectors, middle, all arithmetic modes and joint field error. |
| Note 30, FS21--FS31 | Actual collars, mass-anchored adaptive transfer, static spatial jets, both uniform limits and inner overlap. |
| Note 30, FS32--FS34 | Direct implicit derivatives and exact nonzero full-saddle heat residual. |

Notes 24/29 remain continuation history. This integration note is an
editorial specification. None of those three is a source for a new theorem.
Preserve the new source's numbering in the crosswalk, but let LaTeX assign
its own equation numbers. Use semantic labels rather than manual `\tag`
values copied from Markdown research notes.

### 10.2 Bibliography and primary-source scope

Add manual `\bibitem{n25}`, `n26`, `n27`, `n28`, `n30` to 06_references.tex, using their exact titles and
`\repo{notes/<filename>}{Repository source}` links. Reviews belong in the
provenance paragraph/crosswalk, not as proof substitutes. If the PDF links
them, add explicit entries or direct repo links with the correct review
status. The bibliography uses `thebibliography`, **not BibTeX**; do not
assume the separate reference catalog is being compiled.

Carry metadata from [the reference catalog][refs] and
[references.bib][bib] for the primary inputs:

- `polymath2019heat`: version-pinned Polymath paper, exact normalization
  and Section 4 equation (35). State its 0<t<=1/2 high-zero theorem's
  scope when explaining why it is not the theorem used here.
- `DLMFGammaOuter2026`: DLMF 5.11.1, 5.11.2, 5.11.9 and the complex
  remainder discussion in 5.11(ii). The note supplies Cauchy derivatives
  on a fixed sector; do not treat a real-axis asymptotic as a derivative
  estimate without that step.
- `DLMFZetaOuter2026`: DLMF 25.2.1 and 25.2.8, for the full Dirichlet
  tail and middle-strip polynomial allowance.
- Retain the existing Bernoulli `dlmf24` entry and earlier complex-analysis
  citations where their lemmas are used.

Use normal external links for the primary online references and existing
local provenance for any third-party reading copy. No new PDF download,
full-paper-review claim or bibliography-driven theorem extension is part
of this task. The exact gamma factor and the new regulator/collar estimates
are derived in the notes; they are not attributed wholesale to Polymath.

The catalog's `BakerHeatDensityDraft2026` title is stale relative even to
the present main.tex title. Correct that bibliographic metadata to the
actual retained manuscript title when synchronizing the new build; keep
its historical preparation attribution and add the revision attribution
without rewriting what model did the earlier mathematics.

### 10.3 Controls and provenance

Retain the existing collision-control discussion and add the new
source-specific premises from Notes 25--30. In particular:

- Gaussian/source-Taylor and generic rational-map comparisons can also
  hold for smooth colliding sources with their own constants.
- The contour application uses canonical even reflection and the complete
  coefficient envelope. Atoms and heat polynomials lack that source;
  changed-source controls do not inherit its constants.
- The gamma application uses the unchanged xi completion/reflection and
  the ordinary **full** Dirichlet series. State which premise each
  existing control family lacks; do not claim that a generic collar or
  covariance inequality excludes them.
- A simple-root collar argument is local to the proved regime. It does
  not exclude multiple events elsewhere. Generic finite-field stability
  remains valid through multiple events under its positive floor.
- The two regularized layers do not represent complex zeros. Static or
  late-time agreement does not give early-time simplicity or RH.

Do not rerun the control numerics. Their role here is the analytical
premise screen already recorded in the sources.

In `app:numerics`, keep the four existing diagnostic paragraphs, including
every failed case and lack of interval coverage. Add one short sentence
that the new mathematical sources, Notes 25--28 and 30, were derived
analytically and add no numerical onset certificate. Manuscript compilation,
link checks and visual inspection are production checks, not numerics
supporting these theorems.

Revise the acknowledgment to distinguish the historical Astra derivations
and checks from this future Sol integration and production work. Preserve
Edward Baker, substantial LLM assistance, actual recorded models/efforts
and dates. Do not relabel the existing same-assistant research reviews as
independent merely because another model typeset the manuscript. Do not
claim Sol performed a mathematical audit unless a separate audit with
its real scope was actually done.

## 11. Production work, status synchronization and acceptance

### 11.1 Implementation order and writable scope

Implement in this order: protocol/notation moves; framework weak lemma;
negative theorem; contour/cutoff additions; linear gamma/switch section;
full saddle; final abstract and
scope; crosswalk/references; production checks. This prevents conclusions
from being rewritten before the supporting statements exist.

The requested files are the maintained manuscript components and README,
the new components named here, a refreshed small build record, a concise
integration/production note or review, and the existing investigation
status/index/history documents that must describe the resulting artifact.
Source research notes and existing numerical evidence should not be
rewritten to conceal an inconsistency. If a mathematical ambiguity blocks
faithful transcription, record its exact source equation and impact and
return that analytical issue to Astra. Complete unaffected production work.
Do not invent a missing proof, change a coefficient, expand a domain or
silently weaken/strengthen the target to make the build look complete.

No new numerical evaluator, data run, plot campaign, precision sweep,
certified onset, manuscript snapshot, commit, push, release or publication
is requested by this handoff. Source editing and local PDF production are
the intended concrete task. Keep current raw transcript registration and
chat capture in their existing unique homes.

### 11.2 Build and inspect the real final artifact

Use the existing build script from the repository root:

```sh
python3 -B papers/investigations-5/01_heat_density_asymptotics/manuscript/build.py
```

It writes the reading copy to the ignored
`output/pdf/heat_density_asymptotics/heat_density_asymptotics.pdf` and
auxiliaries to that directory's `.build/`. It fails on LaTeX warnings and
prints PDF bytes/hash; **it does not update BUILD_RECORD_20261024.json**.
Do not leave generated PDFs/auxiliaries beside the TeX or commit them.
The built-in LaTeX compiler is a fallback for source diagnostics; a
successful editor compile alone is not proof that the shared export and
its record were refreshed.

The final validation should establish:

1. One definition for every moved label; all new inputs included; no
   missing or duplicate labels, unresolved citations/references, warning
   lines, unreviewed box overflows or literal question-mark references.
2. Every theorem's domain and observable exactly match the frozen source;
   correct 1/8 and 1/16 normalizations, t=-T sign, covariance definition,
   full buffers, common q, and retained heat/adaptive terms. Check the
   finite phase's rate and the switch's **different** O(1) absolute rate.
3. The complete source-to-theorem crosswalk above has no unplaced result.
   Historical limitations are attributed to their old model, not repeated
   as current facts. Read the abstract and closing scope after all edits.
4. Local PDF links resolve at the detected checkout root; internal
   destinations and primary URLs are correct. Preserve the build
   driver's checkout-root mechanism rather than adding more machine paths.
5. Render every page of the new PDF and inspect page contact sheets;
   inspect new long displays, proof breaks, tables, bibliography and
   hyperlink text at readable page size. Repair clipping, overlap,
   missing symbols and awkward display breaks. Report only inspections
   actually performed; do not copy the old 28-page visual-review claim.
6. Inspect the final diff and file sizes. New tracked text/records stay
   below the repository limit; generated PDFs stay ignored. No evidence,
   unrelated changes or chat identity has been discarded.

A PDF production skill may be used for the render-and-inspect step.
Numerical checks of theorem formulas are not a substitute for faithful
source comparison and are not requested here.

### 11.3 Record and synchronize only after the new build exists

Refresh the build record with the **actual** new source list/hashes,
script hash, export path/hash/bytes/pages, time, actual model/effort,
commands, warning results, citation/link checks, visual review and current
limitations. Include every new TeX file. Preserve the old export's hash
and page count as previous-export provenance, rather than presenting it
as the new result. If using the same dated record, retain that historical
information; if the actual production date changes, use a correctly dated
new record and update the current pointer. Do not invent an unavailable
page count or compiler/visual result.

Update together, while preserving the author-directed source freeze in
Section 8 and all newer research statuses in the live ledger:

- manuscript/README.md: replace 28 pages with the verified new count,
  describe integrated notes and the actual new build, and remove the
  accumulated `not yet integrated` paragraphs for sources now included;
  retain that qualifier for any later source deferred under Section 8;
- investigation README.md and research-overview: link the new artifact
  and distinguish this manuscript's frozen coverage from subsequent
  research, preserving each source's actual limitations;
- the **existing sole progress register**: complete only the HDA-10
  production follow-up whose source scope was actually integrated; do not
  infer completion of research tasks from document production;
- DRAFT_HISTORY.md: one concise date/investigation/source-or-commit
  milestone with why it matters and links to this specification and the
  integration/production assessment. No new snapshot folder;
- references/README.md and references.bib as needed for the actual
  bibliography and preparation metadata;
- result-summaries/13 and avoid/12 or avoid/19 only if a current pointer or
  description needs synchronization. Preserve the source status words and
  historical entries; this is integration, not a new mathematical gain;
- reviews/README.md if a production review is added, explicitly separated
  from independent mathematical review.

Refresh the Sol chat's own history at the start/end under the standing
capture workflow. Do not reuse this chat's thread ID or create a second
registration for it. Record the handoff in the appropriate production
note/progress entry; do not hand-edit any generated history JSON.

### 11.4 Definition of done and return to the author

The task is complete when the maintained TeX and exported PDF contain
every accepted mathematical item in this specification, with its proof
and scope intact, all production checks have their recorded actual outcome,
and the current documentation agrees with the new source/build. If a
source issue prevents a theorem's integration, name that exact issue and
its omitted consequence; do not call the full task complete.

Return the main source, PDF, build record and integration assessment links,
the actual new page count, a short list of the substantive additions,
and any unresolved analytical issue. Recommend the next real research
task from the live ledger. This handoff recommends **Sol 6.1 for manuscript
integration**, by the author's explicit choice; it is a production task,
not a fabricated numerical assignment. The next mathematical task remains
**Analytical — Astra** unless a later accepted analysis produces a bounded
numerical question. No numerical packet has been issued by this note.

## 12. Prompt the author can give Sol

> Follow the repository instructions and
> `/Users/ebbaker/Documents/shifted-zeta-positivity/GPT_RESEARCH_MODEL_WORKFLOW.md`.
> Read
> `/Users/ebbaker/Documents/shifted-zeta-positivity/papers/investigations-5/01_heat_density_asymptotics/notes/MANUSCRIPT_INTEGRATION_FOR_SOL_20261024.md`
> and its input manifest, then implement HDA-10-MI1 revision 1 using the
> live progress register. The author has frozen this integration at Notes
> 25--28 and 30; leave later positive-evolution results for a future revision. Read the actual source notes
> and their reviews; preserve all domains, constants, physical normalization
> and residual terms. Update the maintained TeX, build and visually inspect
> the shared PDF, refresh the build record and related status documents,
> and record the production work and chat history. This is manuscript
> production; do not start new numerical research or silently change a
> mathematical statement. Record any analytical discrepancy for Astra.
> Finish with links to the manuscript, PDF, build record and integration
> assessment, and recommend the next model/task.

[agents]: ../../../../AGENTS.md
[workflow]: ../../../../GPT_RESEARCH_MODEL_WORKFLOW.md
[large]: ../../../../LARGE_FILES.md
[results]: ../../../../result-summaries/README.md
[avoid]: ../../../../avoid/README.md
[geometry]: ../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md
[controls]: ../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../avoid/01_restating_the_target.md
[a07]: ../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[a19]: ../../../../avoid/19_status_files_that_lag_the_findings.md
[main]: ../manuscript/main.tex
[build-record]: ../manuscript/BUILD_RECORD_20261024.json
[progress]: ../research-progress/01_AVERAGED_DENSITY_RESEARCH_PROGRESS_20261024.md
[manifest]: MANUSCRIPT_INTEGRATION_INPUTS_20261024.json
[refs]: ../references/README.md
[bib]: ../references/references.bib
[n25]: 25_OUTER_CONTOUR_BOUNDS_AND_CUTOFF_OBSTRUCTION_20261024.md
[n26]: 26_NEGATIVE_ENDPOINT_EVOLUTION_AND_COVARIANCE_20261024.md
[n27]: 27_COMPACT_TIME_GAMMA_OUTER_DENSITY_20261024.md
[n28]: 28_JOINT_OUTER_REGULATOR_TRANSFER_AND_SWITCH_LAYER_20261024.md
[n30]: 30_FULL_GAMMA_SADDLE_AND_INNER_OVERLAP_20261024.md
