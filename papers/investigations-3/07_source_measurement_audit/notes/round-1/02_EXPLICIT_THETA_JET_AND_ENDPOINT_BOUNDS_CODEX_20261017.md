# Explicit bounds for the complete theta jet

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**, verified from this session. This is round-one research development;
formal review belongs at the end of the investigation round, following the
user's revised cadence. Routine algebra and interval checks continue during
the round.

The [opening note][opening] proved nearby-double-jet feasibility using
superalgebraic decay, leaving the rate and onset constants implicit. Here
the complete theta two-jet receives the explicit uniform bound

\[
\boxed{\|(H_t(x),H_{t,x}(x))\|_2\le\frac65e^{-\pi x/16}
\quad(0\le t\le\tfrac14,\ x\ge0).}
\tag{1}
\]

Together with explicit endpoint remainders, this gives an exponential
upper bound for the size of the constructed coefficient changes. It is an
upper bound, not a positive baseline margin or a sign criterion. The rate
is deliberately weaker than the natural carrier rate. No convexity factor
or assumed lower bound for theta occurs in (1).

This continues [Deliverable 1][proposal], with the
[result-summary index][results], [arithmetic identities][arithmetic] and
[avoid index][avoid] as context. The classification is a scoped stability
calculation, under [avoid 01][a01] and [avoid 07][a07]. The finite interval
record [ANALYTIC_BOUND_CHECKS.json][checks] checks the displayed constants
and physical normalization; the analytic arguments below supply the
contour shift and infinite sums.

## 1 A strip contour gives a complete source bound

Write \(a_n=\pi n^2\),
\(\Phi(u)=\sum_{n\ge1}e^u(2a_n^2e^{8u}-3a_ne^{4u})e^{-a_ne^{4u}}\).
The inherited theta reflection makes \(\Phi\) even. Its series is
holomorphic for \(|\operatorname{Im}u|<\pi/8\) and decays doubly
exponentially at positive real infinity in smaller closed strips.
Reflection gives the same decay at negative infinity.

For \(0<y<\pi/8\), shift the full Fourier contour to \(\mathbb R+iy\):

\[
H_t(x)=\frac12e^{-yx}\int_{\mathbb R}
 e^{t(v+iy)^2}\Phi(v+iy)e^{ixv}\,dv.
\tag{2}
\]

The vertical sides vanish by that decay, uniformly for bounded heat time.
Differentiating inserts \(i(v+iy)\). Real coefficients and reflection
make the absolute-value bounds on the two half-lines equal. Put
\(c=\cos(4y)>0\). On \(v\ge0\),

\[
|\Phi(v+iy)|\le\sum_{n\ge1}
 (2a_n^2e^{9v}+3a_ne^{5v})e^{-ca_ne^{4v}}.
\]

For \(0\le t\le T\), use \(e^{4v}\ge1+4v+8v^2\) and
\(|v+iy|\le v+y\). Define

\[
\kappa_n=8ca_n-T,\quad \lambda_{n,b}=4ca_n-b,\quad
J_j(\kappa,\lambda)=\int_0^\infty v^j e^{-\kappa v^2-\lambda v}\,dv.
\]

Whenever \(\kappa_n>0\), this proves
\(|H_t|\le K_H e^{-yx}\), \(|H_{t,x}|\le K_X e^{-yx}\), where

\[
K_H=\sum_{n\ge1}e^{-ca_n}
 [2a_n^2J_0(\kappa_n,\lambda_{n,9})+3a_nJ_0(\kappa_n,\lambda_{n,5})],
\tag{3}
\]
\[
K_X=\sum_{n\ge1}e^{-ca_n}
 [2a_n^2(J_1+yJ_0)(\kappa_n,\lambda_{n,9})
 +3a_n(J_1+yJ_0)(\kappa_n,\lambda_{n,5})].
\tag{4}
\]

Choose \(y=\pi/16\), \(T=1/4\), \(c=1/\sqrt2\). For \(n=1\), put
\(\kappa=8c\pi-T\), \(\ell=4c\pi-9<0\). Elementary majorants are

\[
J_{09}\le U_{09}:=\sqrt{\pi/\kappa}\,e^{\ell^2/(4\kappa)},\qquad
J_{19}\le(1-\ell U_{09})/(2\kappa),
\]
\[
J_{05}\le\tfrac12\sqrt{\pi/\kappa},\qquad J_{15}\le1/(2\kappa).
\]

The first bound extends the shifted Gaussian integral to the whole line;
the second uses \(2\kappa J_1+\ell J_0=1\). For \(n\ge2\), both
\(\lambda_{n,9},\lambda_{n,5}\ge2ca_n\), so discard the Gaussian and use
\(J_0\le1/(2ca_n)\), \(J_1\le1/(4c^2a_n^2)\).
With \(a_2=4\pi\), geometric ratio bounds give

\[
S_a=\frac{a_2e^{-ca_2}}{1-(9/4)e^{-5c\pi}},\qquad
S_0=\frac{e^{-ca_2}}{1-e^{-5c\pi}},
\]

and contributions from \(n\ge2\) at most

\[
K_{H,\mathrm{tail}}\le S_a/c+3S_0/(2c),\quad
K_{X,\mathrm{tail}}\le
 [1/(2c^2)+3/(4c^2a_2)]S_0+yK_{H,\mathrm{tail}}.
\]

Adding the first-node majorants, outward-rounded evaluation gives upper
expressions below \(1.125808767\), \(0.314420277\), and
\(\sqrt{K_H^2+K_X^2}<1.168890710<6/5\). This proves (1). These loose
constants are complete-source bounds, not measurements of cancellation.

## 2 Explicit endpoint and determinant remainders

For a finite-source direction let \(g=e^{tu^2}f\), whose first nonzero odd
endpoint has order \(p-1\), \(p\) even. Put
\(a=(-1)^{p/2}g^{(p-1)}(0)\). Define uniform constants on \([0,T]\),

\[
E_p=\sup_t\{|g^{(p+1)}(0)|+\|g^{(p+2)}\|_1\},\quad
F_p=\sup_t\{(p+2)|g^{(p+1)}(0)|+\|(ug)^{(p+3)}\|_1\}.
\]

The opening integration-by-parts identities give, for every \(x>0\),

\[
|H_f-ax^{-p}|\le E_p x^{-p-2},\qquad
|H_{f,x}+pa x^{-p-1}|\le F_p x^{-p-3}.
\tag{5}
\]

The sine remainder is treated separately, using
\((ug)^{(p+2)}(0)=(p+2)g^{(p+1)}(0)\).

These constants have a finite constructive majorant. For each node set
\(q=a_ne^{4u}\), start \(P_0=2q^2-3q\), and iterate

\[
P_{k+1}=\partial_uP_k+4q\partial_qP_k+(2tu+1-4q)P_k.
\]

Then \(g_n^{(k)}=e^{tu^2+u-q}P_k(u,q;t)\). Bound the polynomial
coefficients uniformly on \([0,T]\). For every monomial and
\(c_n=1-T/(8a_n)>0\),

\[
\int_0^\infty e^{tu^2+u-q}u^j q^k\,du
\le\frac{j!}{4\sqrt{a_n}}c_n^{-k-1/2}
 \Gamma(k+\tfrac12,c_na_n).
\tag{6}
\]

Indeed \(tu^2\le Tq/(8a_n)\), \(u^j\le j!e^u\), and the substitution
\(q=a_ne^{4u}\) gives (6). Start instead from \(uP_0\) to bound the
derivatives of \(ug\), and sum absolute coefficient contributions for
the fixed directions. Thus no unspecified regularity norm is needed to
evaluate \(E_p,F_p\).

Take two directions from the opening construction with exponents
\(p<r\), leading coefficients \(a,b\), and remainder constants
\(E_A,F_A,E_B,F_B\). For \(D=(B\delta_A\ B\delta_B)\), put

\[
L=(r-p)|ab|,\quad
K_2=|a|F_B+r|b|E_A+|b|F_A+p|a|E_B,\quad
K_4=E_AF_B+E_BF_A.
\]

Expanding the determinant proves

\[
|\det D-(p-r)abx^{-p-r-1}|
\le K_2x^{-p-r-3}+K_4x^{-p-r-5}.
\tag{7}
\]

Consequently \(|\det D|\ge(L/2)x^{-p-r-1}\) whenever

\[
x\ge1,\qquad x^2\ge\frac{K_2+\sqrt{K_2^2+2LK_4}}L.
\tag{8}
\]

Let
\(K_D^2=(|a|+E_A)^2+(p|a|+F_A)^2+(|b|+E_B)^2+(r|b|+F_B)^2\).
Then \(\|D^{-1}\|_2\le(2K_D/L)x^{r+1}\). With coefficient matrix
\(P=(\delta_A\ \delta_B)\), the constructed change obeys

\[
\boxed{\|\delta(t,x)\|_\infty
\le\frac{12K_D\|P\|_{2\to\infty}}{5L}
 x^{r+1}e^{-\pi x/16}.}
\tag{9}
\]

For fixed directions, (6)–(9) supply a computable positivity test. Once
\(x\ge16(r+1)/\pi\), the last height factor decreases. An evaluated
onset would require selecting and evaluating the direction constants;
this note asserts no numerical onset. The source is fixed after the
observation point is selected. The conclusion remains exact double-jet
feasibility, without a nondegeneracy claim.

## 3 The published carrier and its derivative

Use [Polymath equations (6), (9), (10)][polymath], with the uncorrected
Stirling carrier. For \(s=(1+ix)/2\), write \(\alpha(s)=A+iB\), where

\[
A=\tfrac14\log(1+x^2)-\tfrac12\log(4\pi)-\frac1{1+x^2},\qquad
B=\tfrac12\arctan x-\frac{3x}{1+x^2}.
\]

Direct evaluation gives the exact modulus

\[
\Gamma_t(x):=|M_t(s)|=
\frac{\pi^{1/4}}{32e^{1/4}}(1+x^2)^{7/8}
\exp\{-\tfrac x4\arctan x+\tfrac t4(A^2-B^2)\}.
\tag{10}
\]

It follows uniformly for bounded nonnegative \(t\) that

\[
\Gamma_t(x)=\frac{\pi^{1/4}}{32}e^{-t\pi^2/64}x^{7/4}
e^{-\pi x/8+(t/16)\log^2(x/(4\pi))}(1+O_T(x^{-1})).
\tag{11}
\]

The physical derivative is

\[
\partial_xM_t(s(x))=\frac i2[\alpha+\tfrac t2\alpha\alpha']M_t,
\quad \alpha'=-\frac1{2s^2}-\frac1{(s-1)^2}+\frac1{2s}.
\]

Its logarithmic factor cannot be silently dropped from a two-jet budget.
For the opening fixed-space constant \(C=A_Mx^{-p}(1+O(x^{-2}))\),

\[
\frac C{\Gamma_t}=
\frac{32A_M}{\pi^{1/4}}e^{t\pi^2/64}x^{-p-7/4}
e^{\pi x/8-(t/16)\log^2(x/(4\pi))}(1+O_T(x^{-1})).
\tag{12}
\]

This is a relative operator asymptotic, not a bound for \(h/\Gamma_t\).
Equation (1) independently supplies a weaker explicit bound for the
complete jet. No unquantified arithmetic factor is inserted into (12).

## 4 Scope and continuation

The [control screen][controls] retains the opening distinctions: normalized
zero-tail square controls occupy a different affine tail class; reflected
super-Gaussians lack the supplied integer-square representation; Euler-factor
controls lack membership in fixed \(V\). Nonzero theta-tail perturbations
constructed here fail full source reflection. Estimate (1) uses the complete
theta reflection and does not imply noncollision, so reflected controls do
not contradict it. No new control grid is introduced.

The [bounded numerical continuation][replay] uses complete integral tails
and distinguishes sufficient radii from actual distances. These are further
notes in the same investigation round; their accumulation does not require
a separate review after each note. A uniform finite-domain exclusion or a
sharp numerical onset would be a separate estimate, not a consequence of
the six recorded observations.

[opening]: 01_OPENING_ANALYTIC_AUDIT_AND_REPLAY_CONTRACT_CODEX_20261016.md
[proposal]: ../../research-overview/01_INITIAL_RESEARCH_PROPOSAL_20261016.md
[replay]: 03_BOUNDED_REPLAY_AND_POSITIVE_FEASIBILITY_CODEX_20261017.md
[checks]: ../../numerics/round1/ANALYTIC_BOUND_CHECKS.json
[results]: ../../../../../result-summaries/README.md
[arithmetic]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[polymath]: https://arxiv.org/html/1904.12438v2#S1
