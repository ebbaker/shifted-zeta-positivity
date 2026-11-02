# J-B01 coefficient representation decision and J-E01 request

1 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**.

**Decision:** select ordinary-coefficient Toeplitz determinants, using the
real multiple integral (4) below. The first transfer problem is the
third-order determinant and the curvature of the source curve
\((\Phi''/\Phi,\Phi^{(4)}/\Phi)\). This is a bounded mechanism-selection
result, not a coefficient-positivity advance. The integral identities and
conditional order-three lemma are derived here; the canonical source's
required curvature sign is **unproved**. There is no independent review or
novelty claim.

This completes the comparison requested by [Continuation04][continuation].
The [owning register][progress] holds live status. Read with the
[result index][results], especially [theta identities][theta] and
[collision controls][controls], and the [avoid index][avoid], especially
[reformulations][reformulations], [shape-only arguments][shape],
[joint estimates][joint], [scoped exclusions][scopes] and
[unchecked imports][imports].

| Next task | Type | Recommended model and reason | Dependency | Return |
| --- | --- | --- | --- | --- |
| **J-E01, request r1 in Section 7** | E | Sol; fixed integration-by-parts, determinant and derivative-algebra audit | This decision; ready | Complete normalization, one classical check, endpoint/tail feasibility of the two specified source signs |
| J-B02 | B | Astra; global source-sign mechanism remains conceptual | J-E01 supports the selected mechanism | One proof strategy or scoped obstruction for the missing global estimate |

No numerical scan, higher-order sign proof, or shared PT request is issued
by this selection. J-E01 has not been executed.

## 1. The two candidates and their normalizations

Retain the canonical source, its even extension, and physical heat time
zero:
\[
\Phi(u)=\sum_{m\ge1}(2\pi^2m^4e^{9u}-3\pi m^2e^{5u})
 e^{-\pi m^2e^{4u}},\quad
b_n=\int_0^\infty u^{2n}\Phi(u)\,du,\quad
c_n=\frac{b_n}{(2n)!},\quad\gamma_n=n!c_n.
\]
All integer parameters below are finite, although the eventual research
objective has no upper bound on them. Every fixed source derivative has
all polynomially weighted absolute integrals finite; odd derivatives at
zero vanish. These facts justify the identities below, without supplying
estimates uniform in the derivative order. The classical complete RH
criteria are recorded once in [Note03][formulations]; this note selects a
method for them.

### Direct Jensen representation

For integers \(d,n\ge0\), factorial duplication gives the exact identity
\[
J_\gamma^{d,n}(X)=\frac{n!}{(2n)!}
 \int_0^\infty u^{2n}\Phi(u)
 {}_1F_1\!\left(-d;n+\tfrac12;-\frac{Xu^2}{4}\right)du.
\tag{1}
\]
Here the hypergeometric function is a finite polynomial: its coefficient
of \(X^j\) is
\(\binom dj u^{2j}/[4^j(n+1/2)_j]\). Thus there is no infinite-series
interchange or convergence issue in (1), for any complex \(X\).
Equivalently its kernel is
\(d!L_d^{(n-1/2)}(-Xu^2/4)/(n+1/2)_d\), by
[DLMF 18.5.12](https://dlmf.nist.gov/18.5.E12).

For \(d\ge1\), each positive dilation \(u>0\) has negative real
polynomial zeros: \(n-1/2>-1\), so the Laguerre orthogonality and zero
theorems apply ([DLMF 18.3](https://dlmf.nist.gov/18.3),
[18.2(vi)](https://dlmf.nist.gov/18.2#vi)).
Positive integration does not preserve this property. Already at
\(d=2,n=0\), the kernel is \(1+u^2X+u^4X^2/12\). Replacing the source
measure by \(9\delta_1/10+\delta_4/10\) gives
\[
1+\tfrac52X+\tfrac{53}{24}X^2,
\qquad\operatorname{disc}=-\tfrac{31}{12}<0.
\tag{2}
\]
This exact example excludes **positive averaging alone**, not the
canonical theta source or a theta-specific Jensen argument. The scaled
Laguerre kernels do not come with a common interlacing over the full
half-line. A successful use of (1) needs additional information about the
integrated coefficients or root separation. Jacobi identities can
generate source derivatives, but do not immediately supply that
information.

### Coefficient determinant representation

For \(r\ge1,k\ge0\), put
\(D_{r,k}=\det[c_{k+j-i}]_{i,j=0}^{r-1}\), with \(c_\ell=0\) for
\(\ell<0\). Katkova's Lemma 1 gives, for \(F(w)=\sum c_nw^n\) and
\(\rho>0\),
\[
D_{r,k}=\frac{\rho^{-kr}}{r!(2\pi)^r}
\int_{[-\pi,\pi]^r}\prod_{j=1}^r
 [e^{-ik\theta_j}F(\rho e^{i\theta_j})]
 \prod_{a<b}4\sin^2\!\frac{\theta_a-\theta_b}{2}\,d\boldsymbol\theta.
\tag{3}
\]
The real part of the **whole product** is sign-bearing; the sine square
does not make the integral nonnegative. Rather than estimating its
complex phases in this pilot, use the following real-source identity.

Define
\[
\Delta_r(\mathbf u)=\det[\Phi^{(2i)}(u_j)]_{{i=0,\ldots,r-1}\atop{j=1,\ldots,r}},
\qquad V(\mathbf u^2)=\prod_{a<b}(u_b^2-u_a^2).
\]
Then
\[
\boxed{D_{r,k}=\frac{1}{\prod_{j=0}^{r-1}(2k+2j)!}
\int_{0<u_1<\cdots<u_r}
 \Big(\prod_{j=1}^r u_j^{2k}\Big)V(\mathbf u^2)
 \Delta_r(\mathbf u)\,d\mathbf u.}
\tag{4}
\]
All factors outside \(\Delta_r\) are positive in the ordered interior.
This exposes a different source determinant from either a raw moment
Hankel matrix or \([S^{(i+j)}(x)]\), where \(S(x)=\Phi(\sqrt x)\).
No sign theorem for either of those matrices transfers automatically.

**Derivation, including small indices.** For integers \(i,m\ge0\),
\[
\int_0^\infty\frac{u^{2m}}{(2m)!}\Phi^{(2i)}(u)\,du=c_{m-i}.
\tag{5}
\]
If \(m\ge i\), integrate by parts \(2i\) times. Every endpoint vanishes
and the result is the defining normalized moment. If \(m<i\), the only
possible lower endpoint is \(-\Phi^{(2i-2m-1)}(0)=0\), and the differentiated
polynomial is zero. This proves precisely the negative-index convention,
not an analytic continuation of a factorial. Without source evenness that
endpoint must be retained.

Apply the continuous determinant-composition formula to (5), with
\(m=k+j\). The determinant of monomials is
\((\prod u_j^{2k})V(\mathbf u^2)\). Its product with \(\Delta_r\) is
symmetric, so restriction from the full orthant to the ordered chamber
cancels the composition formula's \(1/r!\). Absolute convergence follows
by expanding the two finite determinants into products of weighted
derivative integrals. In particular (4) includes \(k<r-1\), and
\(D_{r,0}=c_0^r\) is the triangular boundary check.

## 2. The first concrete sign problem

Set, with derivatives in \(u\),
\[
R(u)=\frac{\Phi''(u)}{\Phi(u)},\qquad
T(u)=\frac{\Phi^{(4)}(u)}{\Phi(u)},\qquad
C(u)=R'(u)T''(u)-T'(u)R''(u).
\tag{6}
\]
The order-three integrand is
\[
\Delta_3(\mathbf u)=\prod_{j=1}^3\Phi(u_j)
 \det\begin{pmatrix}1&1&1\\R(u_1)&R(u_2)&R(u_3)\\T(u_1)&T(u_2)&T(u_3)\end{pmatrix}.
\tag{7}
\]
**Conditional transfer lemma.** For a positive smooth source satisfying
the convergence and endpoint assumptions of (5), the hypotheses
\[
R'(u)>0,\qquad C(u)\ge0\quad(u>0)
\tag{8}
\]
imply \(\Delta_3\ge0\) and hence \(D_{3,k}\ge0\) for every integer
\(k\ge0\). Strict convexity on an interval gives strict positivity of
these integrals.

Indeed \(d^2T/dR^2=C/(R')^3\). For ordered nodes, the determinant in (7)
equals
\[
(R_2-R_1)(R_3-R_1)
\left[\frac{T_3-T_1}{R_3-R_1}-\frac{T_2-T_1}{R_2-R_1}\right],
\]
which is nonnegative for a convex graph. This proves the conditional
lemma; it does **not** prove (8) for theta.

Equation (8) is the **first unpaid estimate**. It is stronger than
nonnegativity of the weighted integral in (4), and source log-concavity
does not establish it. Its appeal is that a determinant at three source
points has a sufficient condition involving derivatives at just one
point, where the Jacobi system operates. A negative value of either
quantity would reject this particular monotone-convex-graph mechanism,
while leaving (4), integrated cancellation, and the coefficient route
available.

For the regular endpoint calculation use \(x=u^2\),
\(\widehat R(x)=R(\sqrt x)\), \(\widehat T(x)=T(\sqrt x)\). Then
\[
R'=2u\widehat R',\quad
C=8u^3(\widehat R'\widehat T''-\widehat T'\widehat R'').
\tag{9}
\]
The factors vanishing at zero must not be mistaken for failed strict
positivity on \(u>0\).

## 3. Where exact theta information enters

Use [Note02][closure]'s Jacobi state \(Z=(a,U,\chi)\), vector field
\(\mathcal D\), and \(B(L)=e^{L/4}\theta_3(e^L)\), with \(L=4u\):
\[
Q_0=U+\tfrac32(a^2-1),\qquad
Q_{j+1}=\mathcal DQ_j+\tfrac a4Q_j,\qquad
\Phi^{(j)}(u)=\frac{4^jB(4u)}8Q_j(Z(4u)).
\tag{10}
\]
In particular
\[
R=16\frac{Q_2}{Q_0},\qquad T=256\frac{Q_4}{Q_0},\qquad
\Delta_r=\frac{4^{r(r-1)}}{8^r}\prod_j B(4u_j)
 \det[Q_{2i}(Z(4u_j))]_{i,j}.
\tag{11}
\]
Here \(Q_0>0\) on the canonical orbit. Thus (8) becomes two rational
sign questions along that orbit, with denominators whose positivity is
known. On \(u>0\), derivatives through \(\Phi^{(6)}\) suffice; removable
endpoint limits in (9) require derivatives through \(\Phi^{(8)}(0)\).
Mixed terms in \(C\) must be formed before bounding them.

The theta-specific premise is the **canonical** orbit with
\(a(0)=\chi(0)=0\), \(U(0)=\Gamma(1/4)^8/(64\pi^4)\), together with
the canonical normalization of \(B\) and the reconstruction (10).
The ODE and reconstruction agree with
[Planat–Solé (5.10)–(5.12)](https://arxiv.org/html/2608.19160v1#S5.SS1).
Their second-concavity theorem and certificates are not inputs to (8).
Source identification by the initial value problem supplies no curvature
bound by itself.

Primitive positivity also leaves a signed operation. With
\(a_n=\int_0^\infty p(u)u^{2n}/(2n)!\,du\) and \(a_{-1}=0\), the
boundary-preserving identity in Note02 gives
\[
c_n=\frac{\mathbf1_{n=0}}{16}+\frac{a_{n-1}-a_n}{8}.
\tag{12}
\]
The first term is essential at \(n=0\); positivity of \(a_n\) does not
sign determinants of their differences. Therefore the first pilot uses
(10) inside (7), not a claim that positive primitive moments suffice.

## 4. Classical baseline and actual possible payoff

The mandatory low-order check is the classical Turán transfer. Write
\(T_k^{\gamma}=\gamma_k^2-\gamma_{k-1}\gamma_{k+1}\). For \(k\ge1\),
\[
D_{2,k}=\frac{1}{(k!)^2}
\left[T_k^{\gamma}+\frac{\gamma_{k-1}\gamma_{k+1}}{k+1}\right]>0.
\tag{13}
\]
For theta, \(T_k^{\gamma}>0\) follows from the signed double-integral
identity of Csordas–Varga, Proposition 2.2 and Theorem 2.4, specialized
to \(f=1\), heat parameter zero. The exact moment factor is
\((2k-1)/(2k+1)\); [Note02, (11)][closure] records the identity.
The source input is their Theorem 2.1, strict concavity of
\(\log\Phi(\sqrt x)\) for \(x>0\). Equation (13) checks the distinction
between ordinary and exponential coefficients; it does not prove
\(R'>0\).

| Established or reported comparison | Quantifiers relevant here |
| --- | --- |
| [Katkova, Theorem 1](https://arxiv.org/html/math/0505174v1) | The ordinary coefficient sequence is already PF44, so an order-three coefficient conclusion is known. Her coefficients equal \(8\,4^n c_n\), a positive geometric rescaling preserving minor signs. |
| Katkova, Theorem 2 | For each fixed order, eventual multiple positivity; the index cutoff depends on order. |
| [Griffin–Ono–Rolen–Zagier, Theorems 1–2](https://arxiv.org/html/1902.07321v1) | Each fixed degree is eventually hyperbolic; their stated small-degree theorem covers \(d\le8\), all shifts. |
| [Griffin et al., Theorems 1.1–1.2](https://arxiv.org/html/1910.01227v3) | \(n\ge c e^{d/2}\); separately, verified zeros to height \(T\) imply finite-degree coverage \(d\le\lfloor T\rfloor^2\). Neither treats arbitrarily large degree at fixed small shift. |
| July 2026 coefficient-tail preprint, as catalogued in [Source04][sources04] | Reports \(k\ge10^{18}r^3\); proof/certificates remain unaudited and are not used here. |

The rationale for order three is to test a **transfer mechanism** whose
source conditions can be explicitly derived and falsified. It is not a
new finite-order positivity target. A useful later advance must supply
order dependence, a new applicable transfer, or a precise obstruction.
Neither (8) nor success for \(r=3\) gives an induction in \(r\).
Small \(k\) with increasing \(r\) remains entirely open in this plan.
No theorem reducing weak consecutive-minor positivity to all minors is
invoked; any such later reduction needs its own verified hypotheses.

## 5. Control screen for the actual claims

The generic claims proved here are identities (1), (4), (5), (12) in
their declared classes, and the finite-order implication (8) to (7) to
\(D_{3,k}\ge0\). They are not RH-sufficient estimates. In particular a
positive-time collision does not refute time-zero order-three positivity.
The [registered controls][controls] give the following premise audit:

| Control | What it says about this proposed use |
| --- | --- |
| Euler-factor source | Positive/even decay permits the generic transfer. Its shifted source and changed arithmetic factor fail the complete canonical reconstruction (10). No failure of (8) is asserted without testing it. |
| Weighted-square sources, including finite-prime perturbations | Changed square weights fail the complete canonical source. Finitely many matched reflection endpoints do not justify all the odd-derivative cancellations in (5); unmatched endpoints must be retained for the corresponding orders. |
| Reflected super-Gaussian source | Full evenness permits (5), but the non-theta source fails the complete canonical reconstruction. Its collision does not require failure of this finite-order conclusion. |
| Smooth shape and positive-primitive sources | Their positive primitive and matched endpoints do not provide (8). Their changed source fails the complete canonical reconstruction; (12) alone does not distinguish them. |
| [Note03's concavity diagnostic][formulations] | Already defeats the broad inference from the stated scalar source-concavity data to real Fourier zeros, within the respective Gaussian/admissible scopes recorded there. It does not settle the derivative-ratio curvature in (8). |

This is an analytical premise screen, not a numerical rerun of collision
certificates. The canonical initial-value/reconstruction condition
distinguishes the proposed theta application, but its quantitative link
to (8) remains unpaid. A valid order-three transfer may accept colliding
controls. Rejecting every control is a requirement for an applicable
global exclusion claim, not for this finite-order lemma.

## 6. Decision and evidence limits

Choose the Toeplitz family because (4) places the unresolved sign in
source derivatives that the available Jacobi algebra explicitly
generates. The first candidate implication is completely specified by
(6)–(8). Direct Jensen averaging has the concrete failure (2), with no
equally specific root-preservation mechanism selected in this round.
This is a priority decision between these two approaches, not an
exclusion of direct Jensen methods.

The comparison has produced an exact representation, a scoped failure
of naive averaging, and a checkable conditional transfer. It has not
established a new sign or improved any known coefficient range.
The next work should determine whether the proposed source conditions
even survive their elementary endpoint and tail tests before attempting
a global proof.

## 7. Frozen execution request J-E01 r1

**Parent:** J-B01. **Type:** E. **Recommendation:** Sol, because the
source, formulas, algebra and stopping test are fixed. Issued 1 November
2026 for Edward Baker by gpt-6-astra / max. The actual executor records
its own model and effort. This request is issued, not dispatched.

**Inputs.** This note r1; [Note02][closure]; [Note03][formulations];
[Continuation04][continuation]; the [Jensen overview][overview]; and the
primary passages listed in Section 8. Repository HEAD at selection was
`c97b376dcbf81f05ea3a4f7d360da168af4a1345`; these investigation files
include uncommitted working-tree inputs. Their SHA-256 versions are:

| Input | SHA-256 |
| --- | --- |
| Note02 | `2408408ef63968525b48ec82b6b8aa3f82892e238ddd9daf32acf960009ed505` |
| Note03 | `c5715d555194f7099f6b823e6701d8c4138e702062716ec30ed469a96c513223` |
| Continuation04 | `d839d7df19fe8310afbd0a3902c68c6df2eff569f0b89d9bca6df56bda1b0a0b` |
| Jensen overview before this decision's navigation update | `48060ee21830b3ab8c2237329efab19e490e24a63c35bcacd50eff77664f2d41` |

**Fixed work, in order.**

1. Audit (4)–(5) for every finite \(r\ge1,k\ge0\), including the endpoint
   with \(m<i\), absolute convergence and the ordered-chamber constant.
   Check \(k=0\) directly. Do not assume a consecutive-to-all-minors
   theorem.
2. Reproduce the one classical baseline (13) from the cited
   Csordas–Varga specialization, with factorials and \(k=1\) retained.
   This is validation only. A Gaussian source may be used as an
   additional elementary normalization check, not as theta evidence.
3. Audit the conditional convex-graph lemma and (9)–(11). Generate only
   \(Q_0,\ldots,Q_8\), as needed. Express \(R'\) and \(C\), or their
   regularized versions in (9), with complete signed numerators and
   positive denominators on the canonical orbit.
4. Perform **two analytical feasibility tests**, not a global scan:
   obtain the leading endpoint values/terms in (9) from the canonical
   initial data, using at most the eighth source derivative; obtain the
   leading signs as \(u\to\infty\) from the first theta summand with a
   justified differentiated remainder. Record positive, negative, or
   unresolved outcomes. An asymptotic positive sign is not an explicit
   global cutoff or a compact-interval proof.

**Permitted routine choices and limits.** Exact polynomial/rational
algebra, Taylor series and equivalent variable choices preserving (6)
are allowed. A single outward-rounded enclosure of the endpoint theta
constant may use 128 bits and one refinement to 256 bits, with its source
and tail error recorded. If unresolved, report it; do not launch a
parameter sweep. No evaluation grid, coefficient campaign, \(r>3\) sign
test, new heat flow, or source replacement belongs to r1.

**Outputs and completion.** Save one derivation/feasibility return in
`01_jensen/notes/`, with any algebra code and small execution record in
`01_jensen/numerics/`. Retain all failed cases. Completion is a verified
representation and baseline plus the two bounded feasibility outcomes,
or a precise failed identity/premise. It does not require a proof of
(8). Update only this route's owning register and relevant navigation;
preserve other writers' changes. Record hashes of actual inputs and code.

**Return triggers.** A failed required source sign in (8), insufficient endpoint
order, or need for a different representation/curvature mechanism returns
to **[B] J-B01 — Astra** with the scoped failure. If the identity and
necessary tests support the fixed mechanism, return the still-unproved
global (8) to **[B] J-B02 — Astra**. Passing both end tests does not
authorize an automatic full-half-line certificate. No shared conceptual
tool is currently a prerequisite; a later PT request must name its
specific consumer and estimate.

**Pasteable request.**

> Complete [E] J-E01 r1 in Investigation07's Jensen route. Read the owning
> register and Section 7 of Note01. Audit the real derivative-determinant
> representation, reproduce the classical order-two normalization, and
> derive the specified endpoint/tail tests for R' and C. Keep the complete
> source, all boundary terms, the Q8 limit and the finite work limits.
> Save the return and stop; do not begin a global sign proof or widen the
> numerical scope.

## 8. Primary-source inspection in this round

Existing entries, versions and PDF receipts in the [shared catalog][catalog]
are retained. This round rechecked:

- Katkova `math/0505174v1`: coefficient scaling (4), Theorems 1–2,
  Lemma 1 (12), determinant composition, and the **strict** Theorem D.
  No full asymptotic proof audit.
- Griffin–Ono–Rolen–Zagier `1902.07321v1`: introduction and Theorems 1–2;
  Griffin et al. `1910.01227v3`: Theorems 1.1–1.2 and coefficient convention.
- Csordas–Varga (1988): printed pp. 177–181, visually inspected from the
  existing reading copy; Theorem 2.1, admissible multiplier (2.11),
  Proposition 2.2 and Theorem 2.4. The specialization is \(f=1,\lambda=0\).
- Planat–Solé `2608.19160v1`: only the exact orbit/reconstruction
  (5.10)–(5.12) used here; second-concavity certificates not rerun.
- DLMF 18.5.12, Table 18.3.1 and 18.2(vi): finite Laguerre/hypergeometric
  normalization, the parameter range and the orthogonal-polynomial zeros.

[continuation]: ../../notes/04_CONTINUATION_FIRST_COEFFICIENT_INVESTIGATION_20261101.md
[closure]: ../../notes/02_CNV_DETERMINANT_TRANSFER_AND_THETA_DIFFERENTIAL_CLOSURE_20261101.md
[formulations]: ../../notes/03_RH_FORMULATIONS_AND_RESEARCH_DIRECTION_20261101.md
[sources04]: ../../references/04_RH_FORMULATION_SOURCES_20261101.md
[catalog]: ../../references/sources.json
[overview]: ../research-overview/01_JENSEN_RESEARCH_OVERVIEW_20261101.md
[progress]: ../research-progress/01_JENSEN_RESEARCH_PROGRESS_20261101.md
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[reformulations]: ../../../../../avoid/01_restating_the_target.md
[shape]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[scopes]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[joint]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[imports]: ../../../../../avoid/16_unchecked_imports_and_novelty_claims.md
