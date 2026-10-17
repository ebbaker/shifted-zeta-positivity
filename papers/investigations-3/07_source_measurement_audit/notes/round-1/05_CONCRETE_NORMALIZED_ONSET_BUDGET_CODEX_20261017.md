# A concrete normalized onset budget

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from this session. Same-model collaborators developed
the finite interval calculation and its interpretation. These are research
contributions within round one, not a formal round assessment.

**The fixed direction pair gives a usable explicit sufficient threshold.**
For every \(0\le t\le1/4\) and \(x\ge3915\), there is a perturbation of
only the first three theta coefficients, preserving the primitive
normalization and the theta tail, such that

\[
H_a(t,x)=H_{a,x}(t,x)=0,\qquad
\|a-\mathbf1\|_\infty<4\times10^{-307},\qquad a_n>\tfrac12.
\tag{1}
\]

The norm is over the changed coefficients; all coefficients beyond the
third remain exactly one. The source is chosen for the selected \((t,x)\)
and then held fixed. The first coefficient is not pinned exactly.
At each fixed \(0<t\le1/4\), [Note 04][nondegenerate] makes these genuine
nondegenerate heat collisions outside a discrete exceptional set above
3915. Nondegeneracy at 3915 itself is not asserted.

This resolves the next analytic decision in the
[round execution plan][plan]. The threshold is sufficient and conservative,
obtained from the [Note 02][bounds] determinant remainder. It is not a
measured or minimal onset, and does not verify the earlier extrapolation
near 140. Its gain is an explicit instance of the scoped finite-source
instability, not a theta sign result.

The [result-summary index][results], [control screen][controls] and
[avoid index][avoid] supply the inherited context. The classification is a
quantitative obstruction for a specified relaxed class, under
[avoid 07][a07]. The fixed calculation follows [avoid 09][a09] and
[avoid 10][a10]; its numerical threshold is judged by the resulting bound,
not by assertion counts or precision.

## 1 The fixed directions and exact constraints

Write \(\beta_n=(4\pi n^2-1)e^{-\pi n^2}\), and let
\(\ell_0(v)=f_v'(0)\), \(\ell_1(v)=f_v'''(0)\), with the physical
modes of the preceding notes. Before calculation, fix

\[
v_2=e_2-\frac{\beta_2}{\beta_1}e_1,\quad
v_3=e_3-\frac{\beta_3}{\beta_1}e_1,\quad
A=v_2,\quad B=v_3-\rho v_2,\quad
\rho=\frac{\ell_0(v_3)}{\ell_0(v_2)}.
\tag{2}
\]

These definitions give the exact identities
\(\beta\cdot A=\beta\cdot B=\ell_0(B)=0\). The last is algebraic,
not inferred from an interval residual containing zero. The two directions
span the normalized three-coordinate tangent space. Their approximate
values are

\[
A=(-0.000343729316632,1,0),\qquad
B=(6.01196952451\times10^{-10},-2.09194443031\times10^{-6},1).
\]

The interval calculation excludes zero for

\[
a=-\ell_0(A)\approx0.0395122594985,\qquad
b=\ell_1(B)\approx-0.000692611224986.
\]

Thus the endpoint exponents are \(p=2\), \(r=4\). The leading coefficients
are independent of heat time: multiplication by \(e^{tu^2}\) preserves
the first odd endpoint of \(A\), and
\(g_B'''(0)=f_B'''(0)+6t f_B'(0)=f_B'''(0)\).

## 2 A single analytic budget evaluation

The fixed calculation uses \(T=1/4\), these two directions, and the
polynomial derivative and incomplete-gamma majorants of Note 02. It
evaluates no physical integrals at new heights. The preregistered rule is

\[
X=\max(1,\lceil\operatorname{upper}(X_D)\rceil)+1,
\tag{3}
\]

followed by one evaluation of the coefficient bound at that height.
There is no height grid or support search. The execution limit was two
minutes and 512 MiB; the 320-bit Arb calculation took about 0.01 seconds
and 26 MiB in the recorded environment.

The [code][code] and [small interval record][record] retain the exact
polynomial recurrence, parameters, component bounds and source hash.
The resulting uniform remainder majorants are

| Constant | Conservative upper bound |
| --- | --- |
| \(E_A\) | 745.331444 |
| \(F_A\) | 58615.351716 |
| \(E_B\) | 68.219941 |
| \(F_B\) | 9373.876742 |

For reproducibility, every derivative is represented by an integer
polynomial in \(u,q,t\) multiplying \(e^{tu^2+u-q}\). Endpoint
coefficients are summed by their powers of \(t\); their absolute values
are bounded on \([0,1/4]\). The integral terms use the monomial majorant
of Note 02, equation (6), with upper incomplete gamma evaluated outward.
The cancellation in (2) is retained as an exact defining identity.

## 3 The threshold and a short outward certificate

Let \(L,K_2,K_4,K_D,P\) have the meanings in Note 02. The following
short decimal constants are strictly outward relative to the computed
expressions:

\[
L>5.47332689\times10^{-5},\quad
K_2<418.436649,\quad K_4<10985380.865,
\]
\[
K_D<59364.960794,\qquad \|P\|_{2\to\infty}<1.000000000003.
\tag{4}
\]

The determinant formula gives \(X_D<3913.596554\), so (3) selects
\(X=3915\). At this point its relative remainder is below
\(0.499640973<1/2\). Both positive terms in that remainder decrease with
\(x\), establishing the determinant lower bound over the whole subsequent
half-line, uniformly in heat time.

The coefficient estimate is

\[
\|\delta(t,x)\|_\infty
\le C_*x^5e^{-\pi x/16},\qquad
C_*<2.603095134\times10^9.
\tag{5}
\]

The height factor decreases for \(x\ge80/\pi<25.465\). Using either the
full interval values or the outward constants (4) at 3915 proves
\(\|\delta\|_\infty<4\times10^{-307}\), uniformly for every later
height. The tighter recorded expression is about
\(3.414363786\times10^{-307}\). Positivity is therefore automatic;
normalization and the tail are preserved exactly by (2).

The large threshold is driven by the coarse determinant remainder,
not the positivity inequality. Refining the inverse norm would improve
an already tiny coefficient bound without addressing that leading cost.
This calculation supplies no reason to tune further heights or fit an
onset law.

## 4 Consequences for the declared measurements

The two original measurement designs remain in their raw absolute units.
For a change supported on nodes 1–3, with \(d=\|\delta\|_\infty\), the
seven recurrence rows obey

\[
\|M_{\rm rec}\delta\|_2\le\sqrt{35}\,d.
\]

Indeed their possible magnitudes are bounded by \((3d,4d,3d,d,0,0,0)\).
For the twelve reflection samples, an explicit coefficient-to-measurement
bound is

\[
K_{\rm ref}=
\left\{\sum_{j=1}^{12}
 \left(\sum_{n=1}^3|\phi_n(j/20)-\phi_n(-j/20)|\right)^2\right\}^{1/2}
<1.916.
\]

Consequently the constructed double jets satisfy the conservative bounds

\[
\|M_{\rm rec}\delta\|_2<2.4\times10^{-306},\qquad
\|M_{\rm ref}\delta\|_2<7.7\times10^{-307}
\quad(x\ge3915).
\tag{6}
\]

These are upper bounds from an explicit feasible construction, unlike the
sufficient exclusion radius \(\eta=\|h\|/C\). In particular they bound
the corresponding positivity-constrained feasible distance from above in
this unanchored theta-tail class. They are not optimal distances.

At any fixed positive time in the domain, Note 04 supplies nondegenerate
collisions at all heights above the threshold outside its discrete
exceptional set. Thus every nonempty open height interval above 3915
contains an admissible collision source obeying these bounds. This is
an existence conclusion from the analytic construction, not a newly
integrated collision witness at a selected abscissa.

## 5 Decision and remaining scope

**Decision: retain the budget as an explicit quantified instability of
the normalized, unanchored, three-coordinate theta-tail class.** It is
useful because it replaces the earlier unspecified high-height threshold
by a proved sufficient number. It does not locate the first event,
justify the extrapolation near 140, certify a finite box around the six
replay observations, or establish the same numerical threshold after
pinning \(a_1\) exactly. Finite infeasibility at \(x=60\) and eventual
feasibility above this bound have compatible quantifiers.

The [control screen][controls] retains the preceding distinctions. The
new sources have strictly positive coefficients and the fixed theta tail,
but any nonzero change fails full source reflection. The canonical
zero-tail square controls therefore belong to a different affine tail
class; reflected super-Gaussian and Euler-factor controls do not supply
membership in this finite square-coefficient space. This is not an
exclusion of exact theta identification, growing designs or independent
comparison-source margins.

The next step within the same round is the claim-by-claim disposition of
the original argument using the repaired analytic statements and validated
finite record. No additional numerical campaign is needed for that step.
Round review remains deferred until the accumulated investigation is ready.

[opening]: 01_OPENING_ANALYTIC_AUDIT_AND_REPLAY_CONTRACT_CODEX_20261016.md
[bounds]: 02_EXPLICIT_THETA_JET_AND_ENDPOINT_BOUNDS_CODEX_20261017.md
[nondegenerate]: 04_NONDEGENERATE_FINITE_SOURCE_COLLISIONS_CODEX_20261017.md
[plan]: ../../research-overview/02_ROUND_BASED_EXECUTION_PLAN_20261017.md
[code]: ../../numerics/round-1/concrete_onset_budget.py
[record]: ../../numerics/round-1/CONCRETE_ONSET_BUDGET.json
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a09]: ../../../../../avoid/09_round_floors_and_fitted_laws.md
[a10]: ../../../../../avoid/10_numerics_ahead_of_the_question.md
