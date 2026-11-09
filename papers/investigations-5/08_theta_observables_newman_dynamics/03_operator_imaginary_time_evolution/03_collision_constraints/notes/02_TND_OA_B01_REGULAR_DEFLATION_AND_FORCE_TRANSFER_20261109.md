# Regular deflation and a complete source force transfer

9 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex assistance, OA chat0002. The actual model identifier
and reasoning effort are unavailable in the local chat registry.
**TND-OA-B01 — B, first bounded research cycle.**

**Status: proved in-note, with proof-author analytical self-check only.**
This note gives a conditional, finite-domain acquisition and confinement
estimate. It obtains no canonical numerical force, denominator floor,
improved lifetime, or Newman bound. Its new use here of classical divided
differences removes an artificial small-gap loss in a direct source
comparator. It does not remove conditioning by the deflated field.
The [decision](../brainstorm/notes/01_TND_OA_B01_DECISION_20261109.md)
and [E01 request](../research-progress/handoffs/02_TND_OA_E01_REGULAR_DEFLATION_ASSESSMENT_REQUEST_20261109.md)
record the next boundary.

Read the [result index](../../../../../../result-summaries/README.md),
especially [controls12](../../../../../../result-summaries/12_collision_controls_and_screening.md)
and [geometry13](../../../../../../result-summaries/13_local_heat_flow_geometry_and_rh_equivalent_criteria.md),
and the [avoid index](../../../../../../avoid/README.md), especially
[classification01](../../../../../../avoid/01_restating_the_target.md),
[premise02](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[scope07](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)
and [coupled estimates12](../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md).
The identities below are diagnostics; the error estimates are conditional
intermediate estimates; the final strict test is a finite-domain sufficient
test, not a claimed RH-equivalent advance.

## 1. Fixed domain and the two acquisition candidates

Keep
\[
h(\tau,z)=H_{\lambda_s-\tau}(z),\qquad h_\tau=h_{zz},\qquad
0<\Delta\le\lambda_s\le\tfrac12.
\]
Thus the proposed time slab is
\(\lambda\in[\lambda_s-\Delta,\lambda_s]\). Choose finite parameters
\(X>R+D>0,\ R,D>0\), and the parameter box
\[
\mathcal K=\{0\le\tau\le\Delta,\quad |c-X|\le R,\quad
0\le d\le D,\quad -1\le v\le1\}.
\tag{1}
\]
The prospective real pair is \(a=c-d,\ b=c+d\); an evaluation point on
its segment is \(x=c+dv\). At time zero the actual field must have two
specified distinct simple real roots with these coordinates. No global
all-real-zero hypothesis is made. A collision in this class is a local
double event; the nonvanishing condition below excludes higher
multiplicity at a terminal coalescence.

Candidate one, terminal event jets, gives the inherited
\[
B_*=\frac{h_{xxxx}}{6h_{xx}}-\frac{h_{xxx}^2}{9h_{xx}^2}.
\]
An event-only bound does not control the preceding slab. Separate source
moment bounds do not lower-bound its denominator. Primitive transfer
through order six changes neither fact; parent [Note11 §§2–3](../../notes/11_TND_O_B02_CRITICAL_COEFFICIENTS_THETA_AND_RODGERS_TAO_20261106.md)
already contains that transfer.

Candidate two, exterior force, uses
\[
h=(z-a)(z-b)U,\quad g=U_z/U,\quad
B=\tfrac12\int_{-1}^1 g_z(\tau,c+dv)\,dv,\qquad
q'= -8-4qB,\quad q=4d^2.
\tag{2}
\]
Parent [Note07 §4](../../notes/07_TND_O_B02_COLLISION_ANATOMY_20261106.md)
proves (2). The focused clarification is whether vanishing root slopes
force one to obtain \(U\) from a complex contour. They do not: the same
complete source has a direct, regular deflation. This selects an
acquisition method inside candidate two, not a third mechanism.

## 2. Deflate at the actual nodes without dividing by the gap

For a \(C^4\) real function \(f\) on the relevant interval, set
\[
\mathscr D_{a,b}f(x)=f[a,b,x]
=\int_0^1\int_0^{1-s}
f''((1-s-t)a+tb+sx)\,dt\,ds.
\tag{3}
\]
For distinct nodes this is the ordinary second divided difference;
the integral defines all repeated-node cases. For example, integrating
first in \(t\) and then in \(s\) gives
\[
\frac1{b-a}\left\{\frac{f(x)-f(b)}{x-b}
                       -\frac{f(x)-f(a)}{x-a}\right\},
\]
which is (3). Continuity supplies the coincident limits. This is the
classical Genocchi–Hermite formula; see de Boor, §9, (52), printed p.64,
in the [source-use record](../references/01_TND_OA_B01_SOURCE_USE_20261109.md).
No novelty is claimed for this interpolation formula.

If \(f(a)=f(b)=0\), then
\(\mathscr D_{a,b}f(x)=f(x)/((x-a)(x-b))\). At \(a=b\) this conclusion
requires \(f(a)=f'(a)=0\); it is not true at an arbitrary repeated node.
The latter distinction matters when a parameter box includes hypothetical
nodes that are not roots.

Choose a fixed sign \(\sigma\in\{1,-1\}\), and put
\[
U_j=\partial_x^j\mathscr D_{a,b}(\sigma h)(x),\qquad j=0,1,2,
\]
where these derivatives hold \(a,b,\tau\) fixed. Differentiating (3)
gives the weight \(s^j\). Its total mass is
\[
\int_0^1s^j(1-s)\,ds=\frac1{(j+1)(j+2)}.
\tag{4}
\]
At an actual pair, \(U_0\) is the signed deflated factor, and
\[
g=\frac{U_1}{U_0},\qquad
g_z=\frac{U_2}{U_0}-\left(\frac{U_1}{U_0}\right)^2.
\tag{5}
\]
At a double event \(a=b=x\), the three values are respectively
\(\sigma h_{xx}/2,\sigma h_{xxx}/6,\sigma h_{xxxx}/12\).
Equation (5) therefore recovers \(B_*\) with the correct factors.

For any real \(C^4\) approximation \(P(\tau,x)\), define
\(V_j=\partial_x^j\mathscr D_{a,b}(\sigma P)(x)\) at the **same nodes**.
Neither \(P(a)=P(b)=0\) nor matching model roots is required. Indeed,
\[
\mathscr D_{a,b}P(x)
=\frac{P(x)-L_{a,b}P(x)}{(x-a)(x-b)}
\]
with its linear interpolant subtracted. Directly dividing \(P(x)\) by
the true quadratic instead would be wrong. The model need not solve
the heat equation; all dynamics in this note use the actual \(h\).

If
\[
\sup_{\tau,\ y\in[X-R-D,X+R+D]}
|\partial_y^k(h-P)|\le\epsilon_k,\qquad k=2,3,4,
\]
then, uniformly on (1),
\[
|U_j-V_j|\le e_j:=
\frac{\epsilon_{j+2}}{(j+1)(j+2)}
\quad(j=0,1,2).
\tag{6}
\]
In particular the constants are \(1/2,1/6,1/12\), and contain no inverse
power of \(b-a\). This is a derivative-error statement. Small value
error \(\epsilon_0\) alone does not imply (6).

## 3. A signed force transfer with its conditioning retained

Suppose uniform, independently established model bounds on (1) give
\[
V_0\ge m>e_0,\qquad |V_1|\le M_1,\qquad |V_2|\le M_2.
\tag{7}
\]
The fixed sign makes the floor positive. Define
\[
\begin{split}
A&=\frac{M_1+e_1}{m-e_0},\\
K&=\frac{M_2+e_2}{m-e_0}+A^2,\\
\alpha&=\frac{e_1+M_1e_0/m}{m-e_0},\\
\kappa&=\frac{e_2+M_2e_0/m}{m-e_0}
  +\alpha\left(\frac{M_1+e_1}{m-e_0}+\frac{M_1}{m}\right).
\end{split}
\tag{8}
\]
Then \(|g|\le A,\ |g_z|\le K\), and
\[
\left|g_z-
 \left\{\frac{V_2}{V_0}-\left(\frac{V_1}{V_0}\right)^2\right\}
\right|\le\kappa.
\tag{9}
\]
Proof: subtract the second-derivative quotients to get the first term
of \(\kappa\). Subtract the first-derivative quotients to get \(\alpha\);
multiply by the upper bound for the sum of their absolute values to
bound the difference of their squares. All divisions use (7).

Consequently, an acquired bound
\[
b_P\ \ge\
\sup_{\tau,c,d}\frac12\int_{-1}^1
\left\{\frac{V_2}{V_0}-\left(\frac{V_1}{V_0}\right)^2\right\}\,dv
\tag{10}
\]
gives \(B\le b:=b_P+\kappa\) at the actual pair. Retain the signed
integral in (10), including its negative square, before adding errors.
The unknown zero locations have been replaced by a declared compact
parameter box, not by assumed model roots.

The quantities \(m,M_1,M_2,b_P\) have not been obtained for a canonical
box. Absolute source moments upper-bound derivatives but cannot
supply \(m\) or a favorable \(b_P\). There is no gap singularity in
(8), but \(m-e_0\) can be arbitrarily small. Multiplying both the field
and its model by a nonzero constant rescales \(m,M_j,e_j\) together
and leaves \(A,K,\kappa,b\) unchanged.

## 4. Complete theta truncation errors for this method

Here a concrete source acquisition replaces an unspecified residual.
Write
\[
\Phi_n(u)=(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
                       e^{-\pi n^2e^{4u}},\qquad u\ge0.
\]
Every \(\Phi_n\) is positive on this half-line. For integer \(N\ge1\)
and \(W\ge1\), take the exact finite-integral model
\[
P(\tau,x)=\sum_{n=1}^N\int_0^W
 e^{(\lambda_s-\tau)u^2}\Phi_n(u)\cos(xu)\,du .
\tag{11}
\]
This model is a computational approximation; the target remains the
complete canonical source. No assertion about the zeros or heat
threshold of the truncated source is used.

Set \(L=\lambda_s,\ M=N+1\),
\[
r_M=(1+1/M)^4e^{-\pi(2M+1)},\quad
C_\Phi=\frac{2\pi^2}{1-16e^{-3\pi}},
\]
\[
A_k(N,W,L)=
\frac{2\pi^2M^4}{1-r_M}
e^{LW^2-\pi M^2}\frac{W^{k+1}}{k+1},
\]
\[
d_k(W,L)=4\pi e^{4W}-2LW-9-k/W,\qquad
T_k(W,L)=
\frac{C_\Phi W^k e^{LW^2+9W-\pi e^{4W}}}{d_k(W,L)}.
\tag{12}
\]
For \(0\le k\le6,\ 0\le L\le1/2,\ W\ge1\), \(d_k>0\), and
\[
\epsilon_k=A_k(N,W,L)+T_k(W,L)
\tag{13}
\]
bounds the complete derivative error, uniformly for every real \(x\)
and the whole time slab.

For completeness, the proof pays two disjoint omitted regions. On
\([0,W]\), the ratio between successive terms \(n^4e^{-\pi n^2e^{4u}}\)
is at most \(r_M\) for \(n\ge M\). Moreover
\(e^{9u-\pi M^2e^{4u}}\le e^{-\pi M^2}\), since its logarithmic
derivative is negative. Multiplication by \(e^{LW^2}\) and integration
of \(u^k\) gives \(A_k\). On \(u>W\), sum all theta indices using
\(\Phi(u)\le C_\Phi e^{9u-\pi e^{4u}}\). The logarithm of
\(u^ke^{Lu^2+9u-\pi e^{4u}}\) has derivative \(-d_k\) at \(W\),
and second derivative
\(-k/u^2+2L-16\pi e^{4u}<0\). Its tangent exponential integrates to
\(T_k\). These are real-axis derivative bounds, not unmodified
complex-contour bounds.

For a discretized approximation, add certified derivative quadrature
and rounding errors to \(\epsilon_k\). Point sampling is not such a
certificate. The finite integrals (11) alone require no claim about a
quadrature implementation. One possible total-moment bound, useful for
mesh allowances, is
\[
\overline M_k(L)=\frac{C_\Phi e^{L-\pi}}{k+1}+T_k(1,L),
\quad
\int_0^\infty u^ke^{Lu^2}\Phi(u)\,du\le\overline M_k(L)
\quad(0\le k\le6).
\tag{14}
\]
The same split at one proves it. These coarse positive bounds pay
errors; they do not preserve the oscillatory sign needed in (10).

In (3) write \(\xi=c+d(-1+s+2t+sv)\). For \(j=0,1,2\), parameter
variation of \(U_j\) has the explicit allowances
\[
\begin{split}
|\partial_cU_j|,\ |\partial_dU_j|
 &\le \overline M_{j+3}/((j+1)(j+2)),\\
|\partial_vU_j|&\le D\overline M_{j+3}/((j+2)(j+3)),\\
|\partial_\tau U_j|&\le \overline M_{j+4}/((j+1)(j+2)).
\end{split}
\tag{15}
\]
They also hold for (11), whose positive measure is a submeasure of the
complete source bound. Here \(|-1+s+2t+sv|\le1\). For a parameter cell,
sum these bounds times its coordinate radii. No velocity of an
individual root is used for time interpolation. A future computation
must additionally enclose the retained integral and the rational
expression (10) on complete cells.

## 5. Pay confinement before concluding survival

This step prevents the circular assumption that an isolated pair has
already survived the requested interval. Suppose (6)–(10) hold on the
entire parameter box before following the roots. At time zero let
\[
|c(0)-X|\le R_0<R,\qquad
0<Q_-\le q(0)\le Q_+<4D^2.
\]
The following three **strict** inequalities suffice:
\[
R_0+2A\Delta<R,\qquad
Q_+e^{4K\Delta}<4D^2,\qquad
\eta:=Q_- -8E_b(\Delta)>0,
\tag{16}
\]
where
\[
E_b(t)=\int_0^t e^{4bs}\,ds
=\begin{cases}(e^{4bt}-1)/(4b),&b\ne0,\\t,&b=0.\end{cases}
\]
Then the specified real pair remains distinct and simple throughout
\([0,\Delta]\), inside the box, with
\[
q(\tau)\ge e^{-4b\tau}\{Q_- -8E_b(\tau)\}>0.
\tag{17}
\]

To prove this, continue the two simple real roots only until the first
collision or exit from the box. On that interval the local root law
gives \(c'=-g(a)-g(b)\), hence \(|c'|\le2A\).
Also \(q'\le4Kq\), after dropping the negative constant in (2),
so \(q\le Q_+e^{4K\tau}\). The first two inequalities in (16)
prevent a parameter-boundary exit. Since \(B\le b\) and \(q\ge0\),
the lower differential inequality \(q'\ge-8-4bq\) proves (17);
the third inequality prevents the pair's own collision. At either
root, \(|h_z|=2d\,U_0\ge2d(m-e_0)>0\), so a collision with an
additional root is also impossible before a stopping event. Compactness,
analyticity and these positive margins extend the branches beyond any
putative earlier stopping time. Reality follows from uniqueness and
conjugation symmetry.

This is an alternative to acquiring a separate fixed complex isolation
contour for this specific real-pair theorem. Its price is the stronger
uniform floor (7) over the whole declared parameter box. It does not
certify a complete complex zero inventory. If (7) or a confinement
margin fails, that is failure of this sufficient implementation, not
evidence of an actual theta collision.

## 6. Equally informed comparisons and analytical controls

The preceding estimate must be compared with the best same-source
direct calculation, including divided differences themselves. Raw
quotients \(h_{xx}(r)/h_x(r)\) are not the only direct comparator.
The inherited [RT Note02 §4](../../../../02_heat_flow_rh_applications/rodgers_tao/notes/02_CORRECTED_PROPAGATION_AND_CONTOUR_FORCE_TRANSFER_20261026.md)
already has an internal-gap-independent contour transfer; its boundary
floor and distance are different conditioning costs from (7).
[RT Note03 §§4–5](../../../../02_heat_flow_rh_applications/rodgers_tao/notes/03_CANONICAL_TWO_ROOT_MARGINS_AND_FORCE_BUDGET_20261026.md)
found its *model curvature allowance*, rather than its tiny source
error, dominated the unfavorable 309.53 budget ratio.
Neither a smaller truncation error nor a regular direct formula proves
that the signed curvature value will improve.

For any actual canonical application, compare (16) with complete-source
sign or critical-value bounds on the same time/height domain as well
as the contour route. For example, a certified regular minimum obeys
\(v'=h_{xx}\); \(v(0)+M_{xx}\Delta<0\), together with the requisite
spatial boundary and critical-curve controls, is a direct competitor.
No universal ranking or runtime advantage is proved here.

Three exact local checks are informative:

1. For \(h=z^2+2(\tau-T)\), \(U_0=1,U_1=U_2=0\). Thus
   \(A=K=b=0,\ q(0)=8T\); (16) permits exactly \(\Delta<T\)
   and fails at its collision horizon by equality.
2. For \(h=z^2+\alpha z^3+2\tau+6\alpha\tau z\), which also solves
   the heat equation, \(U_0=1+\alpha(a+b+x),U_1=\alpha,U_2=0\).
   On a positive-floor box,
   \(B=-\alpha^2/((1+3\alpha c)^2-\alpha^2d^2)\).
   Its event at \((0,0)\) has \(B_*=-\alpha^2\). Negative exterior
   curvature remains compatible with collision.
3. At the quadruple event of
   \(h=z^4+12\tau z^2+12\tau^2\), \(U_0=0\) at the repeated
   zero. Condition (7) fails. This theorem makes no claim for that
   higher-multiplicity class.

These heat polynomials are algebraic checks, not positive theta-source
controls. The required [control inventory](../../../../../../result-summaries/12_collision_controls_and_screening.md)
has the following analytical premise screen; prior numerical
certificates are not rerun.

| Recorded control | Premise it fails in the canonical acquisition (11)–(14) |
| --- | --- |
| Euler-factor | Unchanged unit coefficients/completion; its additional translated source must be included in its own error payment |
| Weighted-square | Complete unit weights and full normalized reflection; finite endpoints and square support do not justify the canonical tails |
| Reflected super-Gaussian | Complete integer-square expansion; reflection does not justify (12) |
| Smooth shape, earlier counter-kernels and positive-primitive controls | Exact theta amplitude/arithmetic; positivity and endpoint matching do not justify the retained signed model or its canonical remainder |
| Finite-source and finite-prime orbit controls | Full theta coefficients/reflection; their time-dependent high-gap witnesses do not identify a fixed canonical box |
| Fixed-event and exact finite-profile threshold controls | Unchanged theta coefficients, full profile and eventual simplicity; finite profiles do not establish (7) or (10) |
| RH-conditional normalized endpoint control | Ordinary Dirichlet-series arithmetic; escaping time-zero doubles are not witnesses inside an arbitrary fixed compact box |
| Fixed-amplitude variable-kernel controls | Literal cosine and the physical heat equation |
| Actual-profile measure relaxations | A complete integer divisor of the canonical field; not an actual solution to which the root continuation proof applies |

The **generic** transfer (3)–(10) and survival theorem also apply to
controls with their own valid source data. They are not supposed to
distinguish theta. If a control has a nondegenerate double event at
\(T\le\Delta\), retains the denominator and confinement premises, and
has a valid \(B\le b\), its exact identity gives
\[
q(0)=8\int_0^T \exp\!\left(4\int_0^s B(t)\,dt\right)ds
\le8E_b(T)\le8E_b(\Delta).
\]
Thus its strict gap premise necessarily fails. Where a recorded witness
does not meet this local event class, no particular failing numerical
margin is invented. Failure of the literal canonical identity alone is
not evidence that a future derived signed estimate separates a control.

## 7. What the first cycle establishes and leaves open

The measurable analytical improvement is the transfer
\((\epsilon_2,\epsilon_3,\epsilon_4)\mapsto(e_0,e_1,e_2)\) with exact
constants \(1/2,1/6,1/12\), a force error (8) without inverse gap
loss, explicit complete theta remainders (12), and a noncircular
confinement/survival package (16). These are conditional results,
with proof-author checking only.

The favorable canonical input is still the jointly acquired
\((m,M_1,M_2,b_P,Q_-,Q_+,R_0)\) on a useful specified box.
No tuple has been selected or measured. In particular this note does
not claim a positive canonical \(\eta\), a coverage gain, or a new
arithmetic sign theorem. Its explicit next E task is assessment of this
fixed analytic method; selecting a consequential canonical box remains
a later B decision, not permission for an open numerical search.
