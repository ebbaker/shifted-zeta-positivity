# Nondegenerate collisions in the finite source class

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from the session. This is an analytic continuation
within the current investigation round. Formal review is deferred to the
round boundary; no new numerical campaign is used.

The nearby double jets of [Note 01][opening] can be made nondegenerate.
For every fixed heat time \(t_*>0\), sufficiently large observation heights
outside a discrete exceptional set give a genuine local heat collision
after the constructed coefficients have been frozen. Exact linear
constraints and positivity of the resulting coefficients are retained.
This strengthens the scoped instability statement; it does not assert a
collision of theta or preservation of full source reflection.

This addresses the next analytic question in the
[round execution plan][plan]. Its context is the
[result-summary index][results], [collision controls][controls] and
[avoid index][avoid], especially [scoped exclusions][a07] and
[normalization and endpoints][a08]. The statement is an obstruction for a
fixed relaxed coefficient class, not an RH-equivalent reformulation.

## 1 Precise statement

Let \(V\subset\mathbb R^N\) be a fixed finite-support perturbation space
of dimension at least two. Any homogeneous exact constraints, such as
\(\beta\cdot\delta=0\) and \(\delta_1=0\), are already built into \(V\).
The reference source has theta coefficients one at every positive node.
Fix \(t_*>0\).

There are \(X\) and a discrete set \(Z\subset(X,\infty)\) such that for
each \(x_*\in(X,\infty)\setminus Z\) one can choose
\(\delta(x_*)\in V\), with all resulting coefficients positive and the
theta tail fixed, for which the frozen source satisfies

\[
H_a(t_*,x_*)=H_{a,x}(t_*,x_*)=0,\qquad
H_{a,xx}(t_*,x_*)\ne0.
\tag{1}
\]

The coefficient changes tend to zero faster than every inverse power of
\(x_*\). For \(0<t_*\le1/4\), [Note 02][bounds] gives the exponential
upper budget there. Every fixed finite linear measurement of these
changes tends to zero as well. The exceptional set is for each fixed
time; no uniform bound on its cardinality or spacing is asserted.

## 2 Curvature cannot vanish identically

Choose the two directions \(\delta_A,\delta_B\) from Note 01 with distinct
leading endpoint exponents \(p<r\), and write at the fixed time

\[
F(x)=H_{\delta_A}(t_*,x),\quad G(x)=H_{\delta_B}(t_*,x),\quad
H(x)=H_\theta(t_*,x),\quad
D(x)=\begin{pmatrix}F&G\\F'&G'\end{pmatrix}.
\]

For all sufficiently large \(x\), the determinant expansion makes \(D\)
invertible. Define the analytic coefficient choice

\[
\binom{c_A(x)}{c_B(x)}=-D(x)^{-1}\binom{H(x)}{H'(x)}.
\]

The curvature of the source frozen at that observation point is

\[
\mathcal K(x)=H''(x)-(F''(x),G''(x))D(x)^{-1}
\binom{H(x)}{H'(x)}.
\tag{2}
\]

This is a real analytic function on the half-line of invertibility. It
is not the second derivative of the identically vanishing expression
obtained by allowing the coefficients to vary with \(x\): freezing the
source is essential.

Suppose \(\mathcal K\) vanished identically there. Put
\((A(x),B(x))=(F'',G'')D^{-1}\). Then \(F,G,H\) would all solve

\[
Y''=A(x)Y+B(x)Y'.
\tag{3}
\]

The Wronskian of \(F,G\) is nonzero, so uniqueness for this second-order
linear ODE implies \(H=\lambda F+\mu G\) with constant coefficients on
the connected half-line. But

\[
F(x)=a x^{-p}(1+O(x^{-2})),\quad
G(x)=b x^{-r}(1+O(x^{-2})),\quad a,b\ne0,
\]

whereas \(H\) decays faster than every power. Multiplying first by
\(x^p\) and then by \(x^r\) forces \(\lambda=\mu=0\). This would make
the entire function \(H(t_*,\cdot)\) identically zero, contradicting
\(H(t_*,0)>0\). Therefore \(\mathcal K\) is not identically zero.
Its zeros form a discrete set on that half-line.

Outside this set, the opening construction gives (1). Its coefficient
changes tend to zero, so after increasing \(X\) they preserve strict
positivity. All prescribed linear constraints are preserved because the
change remains in \(V\). If theta itself has a double jet at a selected
point, a zero perturbation is possible; nonzero perturbations are not
claimed at every point. This qualification does not affect arbitrarily
large admissible choices.

## 3 The heat event with coefficients held fixed

At any selected point satisfying (1), set \(s=t-t_*\), \(y=x-x_*\),
and \(k=H_{a,xx}(t_*,x_*)\ne0\). The frozen source obeys
\(\partial_tH_a=-\partial_x^2H_a\), hence its local expansion begins

\[
H_a(t_*+s,x_*+y)=\frac{k}{2}(y^2-2s)
 +O(|y|^3+|s|\,|y|+s^2).
\tag{4}
\]

The implicit function theorem gives a real analytic critical curve
\(y_c(s)\) from \(H_{a,x}=0\), with critical value
\(A(s)=-ks+O(s^2)\). Taylor expansion about that curve factors
\(H_a-A(s)=(y-y_c(s))^2U(s,y)\), where \(U(0,0)=k/2\).
The analytic change of coordinate
\(z=(y-y_c(s))\sqrt{2U(s,y)/k}\) is locally invertible and real on real
arguments. Hence the zero equation is \(z^2=2s+O(s^2)\): two real simple
zeros for small \(s>0\), and a nonreal conjugate pair for small \(s<0\).
Since \(t_*>0\), those earlier nonreal zeros occur at positive
heat time as well. Thus (1) describes an actual nondegenerate local heat
collision, not just an undecided small jet. No global Newman constant for
the perturbed kernel is needed for this local statement.

## 4 What is excluded and what remains open

For this fixed finite-support relaxed class with at least two tangent
directions, no fixed positive absolute measurement radius around theta
can exclude every positive-time heat collision on an unbounded height
domain. The proof constructs a different nearby source after choosing
each event; it does not construct one source colliding at every large
height. There is no numerical onset or finite-box exclusion in this note.

The [control screen][controls] still applies by class. The constructed
sources have the fixed theta tail and positive coefficients but fail full
source reflection when the perturbation is nonzero. Canonical zero-tail
square controls and reflected or Euler-factor controls have the separate
memberships recorded in Note 01. Exact normalized reflection, growing
measurement designs, relative error models and independently bounded
comparison-source margins are outside this exclusion.

The remaining quantitative question is whether one explicit direction
pair makes the endpoint and positivity onset budget in Note 02 useful.
That is a bounded analytic calculation, not a reason for a larger numerical
grid. The accumulated notes remain in the same round until its questions
and limitations are ready for a joint assessment.

[opening]: 01_OPENING_ANALYTIC_AUDIT_AND_REPLAY_CONTRACT_CODEX_20261016.md
[bounds]: 02_EXPLICIT_THETA_JET_AND_ENDPOINT_BOUNDS_CODEX_20261017.md
[plan]: ../../research-overview/02_ROUND_BASED_EXECUTION_PLAN_20261017.md
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a08]: ../../../../../avoid/08_normalization_and_constant_slips.md
