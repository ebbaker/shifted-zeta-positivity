# Review reconciliation and the finite-source obstruction

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from this chat's session. Three same-model collaborators
assisted with proofs, the local interval certificate, and record hygiene.
These are routine internal checks, not a second cross-model or specialist
review. Base repository commit: `452eee43f1b32fbc7ded1e46c78b2e041bb68e8d`.

**Status: written reconciliation and bounded interval verification.** This
round follows the user's explicit request to continue in `notes/round-2/`.
It accepts the two central findings of the [Claude review][review], retains
a hypothesis omitted from that review's consolidated statement, and separates
an all-real-zero obstruction from a theorem about local heat collisions.
[Note 02][n02] supplies the additional one-dimensional collision proof.
No new height grid or support sweep is authorized or used here.

This is a scoped obstruction and corrected diagnostic, not an RH-equivalent
criterion: see [result summaries][results], [control cluster 12][controls],
[arithmetic cluster 14][arithmetic], [avoid index][avoid], and specifically
[avoid 01][a01], [02][a02] and [07][a07]. The class throughout is a fixed
finite coefficient change; it does not contain every reflected source.

## 1. What the gap lemma actually requires

Retain round one's notation. At fixed heat time let \(h=(H,H_x)^{\mathsf T}\),
let \(M\) be injective on \(V\), choose \(Q\) spanning \(V\), and take

\[
MQ=UR,\quad A(x)=B_xQR^{-1},\quad S(x)=A(x)A(x)^{\mathsf T},\quad
C=\sigma_1(A),\quad \eta=\|h\|/C,\quad r_M=\|A^\dagger h\|.
\]

Suppose \(z<z'\) are consecutive simple real zeros of \(H\), and on the
closed gap \(A\) has rank two, a simple largest singular value, and a top
left singular vector that is **never vertical**. Then some \(x_*\in(z,z')\)
satisfies \(r_M(x_*)=\eta(x_*)\).

Indeed, choose its continuous unit top vector \(u_1\) with first component
positive. With \(u_2\perp u_1\),

\[
r_M^2-\eta^2=(u_2\cdot h)^2(\sigma_2^{-2}-\sigma_1^{-2}). \tag{1}
\]

At a simple zero of \(H\),

\[
s(x):=\det(u_1,h)/\|h\|
=\operatorname{sign}(H_x(x))u_{1,1}(x).
\]

The endpoint signs are opposite, and \(h\ne0\) throughout the closed gap.
The intermediate value theorem proves the claim. This accepts review §3,
including its nonvertical hypothesis. Under simple spectrum an equivalent
pointwise way to exclude a vertical top vector is

\[
S_{12}\ne0\quad\hbox{or}\quad S_{11}>S_{22}. \tag{2}
\]

The review's consolidated §7(b) omits this condition. Rank two and simple
top singular value alone do not imply its conclusion. For a derivative
compatible abstract example, put

\[
H(x)=\sin x,\quad h=(\sin x,\cos x)^{\mathsf T},\quad
A(x)=\begin{pmatrix}\cos2x&\sin2x\\-2\sin2x&2\cos2x\end{pmatrix},
\quad M=I.
\]

On the zero gap \((0,\pi)\), \(S=\operatorname{diag}(1,4)\), so the top
direction is vertical and simple, but

\[
r_M^2-\eta^2=\tfrac34\sin^2x>0.
\]

The two rows of each column are a function and its derivative. This
counterexample addresses the abstract jet lemma; it is not claimed to be
a theta-source example. No hypothesis of source parity occurs in that lemma.

## 2. One actual theta alignment is now interval-certified

The [local certificate][gap-record] and [producer][gap-code] verify one
preregistered bracket at \(t=1/4\), in the normalized unanchored \(N=6\)
theta-tail class, with the original seven raw recurrence rows:

\[
44.1060084240845<x_*<44.1060084240847. \tag{3}
\]

Set \(P=Q((MQ)^{\mathsf T}MQ)^{-1}Q^{\mathsf T}\), \(S=BPB^{\mathsf T}\),
and \(F(x)=\det(h,Sh)\). Outward-rounded endpoint evaluations give opposite
strict signs of \(F\). Across the whole bracket the computation verifies
rank two, simple top eigenvalue \(\lambda_+\), and

\[
h^{\mathsf T}Sh-\tfrac12\operatorname{tr}(S)\|h\|^2>0.
\]

Consequently at an exact root of \(F\), \(h\) belongs to the top, rather
than the bottom, eigenspace. The exact minimum-measurement coefficient
change there is

\[
\delta_*=-PB^{\mathsf T}h/\lambda_+.
\]

Normalization holds identically because \(\beta^{\mathsf T}Q=0\). The
interval checks establish, with deliberately coarser outward bounds here,

\[
0.12169448523265<r_M(x_*)=\eta(x_*)<0.12169448523268,
\quad \min_{n\le6}(1+\delta_{*,n})>0.88128,
\]

\[
-2.55237822\cdot10^{-7}<H_{a,xx}(1/4,x_*)
<-2.55237814\cdot10^{-7}. \tag{4}
\]

The coefficients selected at the root are then held fixed. By round-one
Note 04's local heat argument, (4) is a nondegenerate positive-time heat
collision. The code uses scaled Acb quadrature, explicit integral and
coefficient tails, and Taylor bounds across one bracket; it extends the
round-one evaluation method and is not a code-independent cross-model
check. It does not certify the two adjacent theta zeros or uniqueness of
this \(N=6\) alignment. Existence follows directly from this local bracket.

Thus the large ratios \(r_M/\eta\) and the 32 feasibility classifications
in round-one Note 03 are facts **at the prescribed abscissae**. They do not
give the distance to a double jet somewhere in a surrounding region. The
historical tables remain correct. The review's other floating alignment
cases remain labelled floating; this round does not promote all 24 to
interval certificates.

## 3. Every nonzero finite change has non-real zeros at every heat time

**Proposition.** Let \(\Psi\ge0\) on \([0,\infty\)), \(\Psi\not\equiv0\), be
either \(\Phi+f\) with \(f=\sum_{n\le N}c_n\phi_n\ne0\), or a nonzero
finite sum \(f\) itself. Then, for every real \(t\),

\[
H_\Psi(t,z)=\int_0^\infty e^{tu^2}\Psi(u)\cos(zu)\,du
\]

has finitely many real zeros and infinitely many non-real zeros.

**Proof.** Round-one finite endpoint separation gives a least nonzero odd
endpoint of the finite sum, of order (p-1) with \(p\ge2\) even. Multiplying
by \(e^{tu^2}\) preserves it. Repeated integration by parts, for each fixed
real \(t\), gives

\[
H_\Psi(t,x)=a x^{-p}(1+O_t(x^{-2})),\quad a\ne0. \tag{5}
\]

When theta is present, its contribution is Schwartz and hence smaller
than every inverse power. The leading \(a=(-1)^{p/2}f^{(p-1)}(0)\) is
independent of heat time. Thus (5) has a fixed nonzero sign for large
\(|x|\). Its nonzero entire extension has finitely many real zeros.

For completeness, the entire function cannot have only finitely many
zeros in total. Write \(a_n\) for the full coefficient sequence. Its least
nonzero index \(n_0\) exists, and its mode dominates at positive infinity.
Nonnegativity forces \(a_{n_0}>0\). For suitable constants \(c,C,U>0\),

\[
\Psi(u)\ge c e^{9u-\lambda_{n_0}e^{4u}}\ (u\ge U),\qquad
|\Psi(u)|\le C e^{9u-ce^{4u}}\ (u\ge0). \tag{6}
\]

These bounds follow by comparing later modes to the first one; the tail
coefficients are either all one or all zero. Let \(M_t(r)\) be the maximum
modulus on \(|z|=r\). Absorbing \(|t|u^2+9u\) into half the exponential
decay in the upper bound, then substituting \(v=ce^{4u}/2\), gives

\[
\log M_t(r)\le\tfrac r4\log r+O_t(r).
\]

For the lower bound use positivity, \(\cosh(yu)\ge e^{yu}/2\), and integrate
on \([u_y-1,u_y]\), where \(u_y=\tfrac14\log(y/(4\lambda_{n_0}))\).
For large \(y\), this interval lies beyond \(U\); (6) gives

\[
\log H_\Psi(t,iy)\ge\tfrac y4\log y-O_t(y).
\]

The function therefore has order one and infinite type. Hadamard
factorization says an order-one entire function with finitely many zeros
is a polynomial times \(e^{az+b}\), which has finite type. Hence the
total zero set is infinite, and only finitely many zeros are real. ∎

This supplies the review's missing detailed growth argument. It also
applies to the finite weighted-square controls, regardless of how many
initial odd endpoints have been cancelled.

If the notation \(\Lambda_{\rm ext}=+\infty\) is used, define it here as

\[
\Lambda_{\rm ext}(\Psi)
=\inf\{t\in\mathbb R:H_\Psi(t,\cdot)\text{ has only real zeros}\},
\qquad\inf\varnothing=+\infty.
\]

There is no all-real time for these sources. Their even half-line
extensions are not smooth at their first uncancelled odd endpoint; this
notation does not invoke a general de Bruijn–Newman theorem for an
admissible smooth even kernel. The assertion about their zero sets is
independent of that terminology.

## 4. Scope of the measurement consequence and disposition

For any nonzero fixed finite-dimensional \(V\), any fixed linear map \(M\)
and any tolerance \(\epsilon>0\), choose \(v\in V\setminus\{0\}\) and a
sufficiently small nonzero scalar \(s\). Then all \(1+sv_n>0\) and

\[
\|M(sv)\|<\epsilon.
\]

Yet the positive theta-tail source \(\Phi+sf_v\) has non-real zeros at
every real heat time, by the proposition. Thus no positive absolute
tolerance distinguishes theta from this non-real-zero class, even in
dimension one. This conclusion alone is not a proof of a local collision
in a prescribed heat interval. [Note 02][n02] proves that additional
statement at every fixed positive time, including \(t=1/4\);
round one's arbitrary-\(T>0\), prescribed-height
construction still needs two directions.

| Review item | Disposition in this continuation |
| --- | --- |
| §3 gap lemma | Accepted with the nonvertical top-vector condition retained; shortened §7(b) corrected by (1)–(2) and the counterexample |
| §4 non-reality proposition | Accepted with the full proof above and explicit meaning of extended \(\Lambda\) |
| R1 pointwise wording | Round-one Note 03 qualified explicitly; local certificate (3)–(4) supplies the companion regional statement |
| R2 dimension one | All-real-zero obstruction proved above; local collision extension proved separately in Note 02 |
| R3 bracket and \(x\approx140\) | Three-square root lies inside its inherited bracket; endpoint replay differs. No verified threshold for \(\eta\) at 140. The new tail certificate gives sufficient heights 264/269, not first-loss heights |
| R4 replay hygiene | Stable mathematical-content hashes and portable peak-memory units added; two bounded replays agree with historical mathematical records |
| R5 no round two / close project | Superseded as workflow by the user's explicit round-two request; no other portfolio project is closed |

The round-one manuscript remains the dated source/PDF reviewed by Claude;
its readme flags the corrections and new results here. No PDF deletion or
new manuscript snapshot is part of this continuation. The coefficient
minimum at an endpoint need not describe the source at the interior
three-square root, and neither represents a theta collision.

The control screen is by membership: weighted-square sources are included
in the proposition’s finite-sum branch but fail full reflection; Euler-factor sources are not finite coefficient
changes; reflected super-Gaussian and smooth/positive-primitive controls
lack a supplied membership in this fixed square class. No argument here
excludes reflected or infinite-dimensional approximation methods. This
answers the scoped audit without a new numerical campaign.

[review]: ../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md
[n02]: 02_ONE_DIRECTION_GAP_COLLISIONS_AND_TAIL_BUDGET_CODEX_20261017.md
[gap-record]: ../../numerics/round-2/GAP_ALIGNMENT_CERTIFICATE.json
[gap-code]: ../../numerics/round-2/certify_gap_alignment.py
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[arithmetic]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
