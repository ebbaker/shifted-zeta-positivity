# AGC-E11: finite source allowance for the frozen physical reference

19 November 2026, America/New_York. Prepared for **Edward Baker** with
OpenAI Codex LLM assistance. The work packet explicitly requested
**gpt-6.1-sol / ultra**. That dispatch/request is distinct from actual
serving metadata: an independent backend-model or reasoning-effort
attestation was not available to this helper. One derivation and one
correction pass; no numerical campaign, zero localization, or all-real
assumption.

**Status:** proved in-note elementary finite defect bounds, with a
selected-primary-source complete value allowance attached. The imported
functions below are fully specified but **unevaluated**. No canonical
count, cleared denominator, positive discriminant margin, or transport
gain has been acquired.

This fulfills the [E11 request](../research-progress/handoffs/AGC-E11-r1-source-request.md)
under the [frozen B01 contract](../brainstorm/notes/02_AGC_B01_FIXED_CELL_COMPARISON_20261119.md).
The [result index](../../../../result-summaries/README.md), especially
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
and the [pattern index](../../../../avoid/README.md), especially
[01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md), and
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md), fix the
interpretation: this is a finite quantitative allowance, not an
RH-equivalent reformulation counted as a gain. Its useful milestone would
be a smaller complete allowance or a positive paid margin at the matched
consumer; neither is asserted here.

## 1. Fixed cell and exact finite defect

Keep the physical reference and the theta function in manuscript
[Section 5](../manuscript/sections/05_arithmetic_source.tex) unchanged:

\[
s_\pm(z)=(1\pm iz)/2,\quad
p_n(t,s)=\exp\{L_0(s)-s\log n+t(\alpha(s)-\log n)^2/4\},
\quad P_N=\sum_{n=1}^N(p_n(t,s_+)+p_n(t,s_-)).
\]

All logarithms and branches are those of that section. Let

\[
\mathcal Q=\{(t,z):t_*-U\le t\le t_*,\ |\Re z-X|\le A,
\ |\Im z|\le h\},\quad
0<U<t_*\le\tfrac12,\quad 0<h\le1,\quad d=X-A\ge200,
\]

and impose exactly

\[
N^2\le\frac{X-A}{4\pi}+\frac{t_*-U}{16},\qquad
\frac{X+A}{4\pi}+\frac{t_*}{16}<(N+1)^2.                 \tag{1}
\]

Thus the published natural cutoff equals this same integer \(N\)
throughout the cell. In particular \(N\ge3\). For each summand set

\[
a_n=\alpha-\log n,\qquad
b=\alpha'=-\frac1{2s^2}-\frac1{(s-1)^2}+\frac1{2s},\qquad
c=\alpha''=\frac1{s^3}+\frac2{(s-1)^3}-\frac1{2s^2}.
\]

Define the actual complex polynomial in these quantities by

\[
F_n(t,s)=b+t a_n^2b+\frac t2(b^2+a_nc)+\frac{t^2}{4}a_n^2b^2.
\]

Direct differentiation gives the exact identity from manuscript
[Section 6](../manuscript/sections/06_residual_transport.tex):

\[
\boxed{\mathcal R_N=P_{N,t}+P_{N,zz}
=-\frac14\sum_{n=1}^N\sum_{\nu\in\{+,-\}}
p_n(t,s_\nu(z))F_n(t,s_\nu(z)).}                           \tag{2}
\]

Here \(\partial_z^2p_n(t,s_\nu(z))=-p_{n,ss}/4\).
Equation (2), with the complex sum performed before taking its modulus,
is the sharper source object. A complete pointwise triangle allowance is

\[
|\mathcal R_N(t,z)|\le\frac14\sum_{n,\nu}|p_n(t,s_\nu)|
\left\{|b|+t|a_n|^2|b|+\frac t2(|b|^2+|a_n||c|)
+\frac{t^2}{4}|a_n|^2|b|^2\right\}.                       \tag{3}
\]

This already is a finite explicit expression. It loses both cancellation
between the two branches and the arithmetic summands, and cancellation
inside \(F_n\). No estimate below assigns that lost cancellation a sign.

## 2. A closed uniform bound using only d, h, t_* and N

The following constants require no supremum over an unspecified function:

\[
T_0=d/2,\quad q=(1-h)/2,\quad S=(1+h)/2,\quad
T_1=2\pi(N+1)^2,\quad Q=(T_1^2+S^2)^{1/2},
\]

\[
L_n=\max\left\{\left|\log\frac{T_0}{2\pi n^2}\right|,
                    \left|\log\frac{Q}{2\pi n^2}\right|\right\},
\qquad
A_n=\frac{3}{2T_0}+\frac12\sqrt{L_n^2+\pi^2/4},
\]

\[
B=\frac1{2T_0}+\frac3{2T_0^2},\qquad
C=\frac1{2T_0^2}+\frac3{T_0^3},\qquad
K_0=\frac{\sqrt{2\pi}}{16}(T_0^2+S^2)e^{-\pi T_0/4},
\]

\[
G_n=B+t_*A_n^2B+\frac{t_*}{2}(B^2+A_nC)
                         +\frac{t_*^2}{4}A_n^2B^2.
\]

Then throughout \(\mathcal Q\),

\[
\boxed{|\mathcal R_N(t,z)|\le\mathfrak R(d,h,t_*,N)
:=\frac{K_0}{2}\sum_{n=1}^N n^{-q}
                 \exp(t_*A_n^2/4)G_n.}                    \tag{4}
\]

**Proof.** Each argument \(s_\nu=\sigma+i\tau\) has
\(q\le\sigma\le S\le1\) and
\(T_0\le T=|\tau|<T_1\), the latter upper bound following from
(1) and \(t>0\). Therefore

\[
|s_\nu|,|s_\nu-1|\ge T_0,\quad
|s_\nu|\le Q,\quad
|\arg s_\nu|\le\pi/2,
\]

and the displayed formula for \(\alpha\) gives
\(|a_n|\le A_n\), while the formulas for \(b,c\) give
\(|b|\le B\), \(|c|\le C\). To bound the actual carrier, its defining
logarithm yields, for \(\tau>0\),

\[
|\mathfrak M_0(\sigma+iT)|
=\frac{\sqrt{2\pi}}{16}|s||s-1|\pi^{-\sigma/2}
 (|s|/2)^{(\sigma-1)/2}
 e^{-(T/2)\arg(s)-\sigma/2}.
\]

The same modulus identity holds by conjugation for \(\tau<0\).
Since \(T\arg(\sigma+iT)\ge\pi T/2-\sigma\),
\(|s|/2>1\), and \(\pi^{-\sigma/2}\le1\), this is at most

\[
\frac{\sqrt{2\pi}}{16}(T^2+S^2)e^{-\pi T/4}\le K_0.
\]

The last function decreases for \(T\ge100\), because its logarithmic
derivative is at most \(2/T-\pi/4<0\). It follows that

\[
|p_n(t,s_\nu)|\le K_0 n^{-q}e^{t_*A_n^2/4}.
\]

Insert these inequalities into (3), with both branches paid, to obtain
(4). The factor \(1/2\) in (4) is \(2\times1/4\); it is not a heat
coefficient. This envelope can be very wasteful. Its small physical scale
also does not compare it with the correspondingly small contour
denominator.

## 3. Complete published value allowance, with the full remainder

Point-of-use primary check on 19 November 2026: Polymath,
[*Effective approximation of heat flow evolution of the Riemann xi
function, and a new upper bound for the de Bruijn–Newman constant*,
arXiv:1904.12438v2](https://arxiv.org/html/1904.12438v2), Theorem 1.3,
Propositions 6.1 and 6.3, and Corollaries 6.4–6.5; specifically (5),
(44), (59), (68), and (70)–(74). Selected passages only, not a full-paper
audit or certificate replay. The existing
[reference record](../references/README.md) owns the bibliographic and
external-PDF provenance. No new PDF is stored.

For \(z=x+iy\), set \(\eta=|y|\), \(T=x/2\),
\(\sigma_-=(1-\eta)/2\), \(\sigma_+=(1+\eta)/2\), and
\(w_\pm=\sigma_\pm+iT\). Use

\[
T'=T+\pi t/8,\quad a_{\rm RS}=\sqrt{T'/(2\pi)},\quad
\epsilon_n(t,w)=
\exp\left(\frac{(t^2/8)|\alpha(w)-\log n|^2+t/4+1/6}
                 {T-3.33}\right)-1,
\]

\[
\delta_\sigma(t,T)=
\left(\frac{0.397\,9^\sigma}{a_{\rm RS}-0.865}
                    +\frac5{3(T-6)}\right)
                         \exp\left(\frac{3.49}{T-4}\right).
\]

A fully specified physical allowance at the original center \(P_N\) is

\[
\begin{split}
\mathcal V_N(t,x,\eta)={}&
\sum_{n=1}^N\sum_{\nu\in\{-,+\}}
      |p_n(t,w_\nu)|\,\epsilon_n(t,w_\nu)\\
&+e^{t\pi^2/64}|\mathfrak M_0(iT')|
             \{1+\delta_{\sigma_-}(t,T)+\delta_{\sigma_+}(t,T)\}.
\end{split}
\]

\[
\boxed{|H_t(z)-P_N(t,z)|\le\mathcal V_N(t,x,|y|).}             \tag{5}
\]

This is the unnormalized complete Corollary 6.5 budget. The first row
pays the exact-term replacements; the second pays the **entire omitted
RS remainder**, including the leading correction. It is the complete
unnormalized version of
\(|\mathcal B_t|(e_A+e_B+e_{C,0})\), not the retained-correction budget
\(|\mathcal B_t|(e_A+e_B+e_C)\). The source's \(s_+,s_-\) names in
Corollary 6.4 are opposite to the manuscript's names; the explicit
arguments \(w_\pm\) and their conjugates above remove that ambiguity.

Its domain is exactly \(0<t\le1/2\), \(x\ge200\),
\(0\le\eta\le1\), with \(N=\lfloor a_{\rm RS}\rfloor\).
Conjugation gives the lower half of the cell. No clock-regime height
condition is added. All denominators above are positive on this domain.
The cell condition (1) makes (5) available at the initial slice and both
lateral boundaries of every horizontal heat problem in B01.

An exact alternative keeps
\(\sum_{n,\nu}(r_n-p_n)\) and both exact RS remainders together before
taking a modulus. That retains additional cancellation but requires
enclosures of those exact integrals. Equation (5) acquires a complete
triangle allowance without acquiring such a coupled enclosure. No
correction-aware holomorphic reference or its defect is supplied here.

## 4. Acquired inequalities and remaining acquisition gates

| Object | Acquired here | Still unacquired |
| --- | --- | --- |
| Physical reference defect | Exact finite expression (2), pointwise (3), closed uniform (4) | Certified values or complex-sum enclosures on a chosen cell; any gain from its phases |
| Canonical value error | Selected-source inequality (5), including full RS remainder and its domain | Numerical/interval values of the imported functions \(\epsilon_n,\delta_\sigma,\mathcal V_N\), and rigorous all-cell suprema if those are used |
| Heat data | (5) can bound \(E(0,x+iy)\) at \(t=t_*\) and the two lateral values \(E(u,X\pm A+iy)\) | Accepted E10 heat weights and analytical or interval enclosures of their data integrals (or evaluated suprema), giving the error on every point of the contour |
| Reference contour | Explicit holomorphic \(P_N\) on the right half-plane | One fixed \(\Gamma:|z-X|=r\), \(r<\min(A,h)\), a proved count \(\#_\Gamma P_N=2\), and \(m_P(u)=\inf_\Gamma|P_N|>0\) uniformly in time |
| Transfer to \(H\) | Rouché applies if a paid \(\varepsilon(u)<m_P(u)\); then \(\inf_\Gamma|H|\ge m_P-\varepsilon\) | That strict inequality, all-time count/clearance, and the full discriminant allowance from the accepted E10 consumer |
| Positive gap and gain | No such claim | A real, positive paid lower bound for \(D_H(u)\) on **every** time slice, and comparison with a direct calculation given identical information |

These are separate payments. For example, (4) gives
\(\sup_\Gamma|\mathcal R_N/P_N|\le\mathfrak R/m_P\) only after the
floor \(m_P\) is acquired. A symbolic upper bound is not a successful
positive margin. The selected-source theorem and the elementary
inequalities have been acquired as formulas; their unevaluated functions
must not be reported as measured source data.

## 5. Cutoff width and circle geometry: restrictions, not an impossibility

Eliminating \(X\) from (1) gives the necessary and sufficient condition
for a nonempty interval of admissible centers, before \(X-A\ge200\)
is imposed:

\[
2A<4\pi(2N+1)-\pi U/4.                                    \tag{6}
\]

The actual placement must still satisfy

\[
4\pi N^2+A-\pi(t_*-U)/4\le X
 <4\pi(N+1)^2-A-\pi t_*/4.
\]

Thus a prescribed cell can fail by straddling a cutoff jump, but its
allowable width does not collapse at high \(N\). A fixed-\(N\) reference
remains analytic across such a jump; what fails there is the immediate
use of this natural-cutoff budget without paying the extra finite terms.
B01 has deliberately frozen a cell that avoids that issue.

The circle is more restrictive in a different direction:
\(r<\min(A,h)\le1\). Any two distinct real zeros it encloses must have
separation less than \(2r<2\). This excludes that circle for a particular
pair too wide to fit, and proves no statement about where canonical
pairs occur. A count of two alone also permits a conjugate nonreal pair;
positive discriminant still has to be established. These are restrictions
of the frozen source domain and circular consumer, not a theorem that
canonical continuation or other contours are impossible.

## 6. Collision-control screen and scope

| Control from Controls12 | Shared generic ingredient | Premise unavailable for importing (5) unchanged |
| --- | --- | --- |
| Euler-factor controls | Heat evolution, positivity/evenness of source | The unchanged complete theta source and its canonical RS coefficient formula; the source modification changes the exact value error to this \(P_N\) |
| Weighted-square controls | Integer-square support and local heat identities | All theta weights and full normalized reflection; support alone does not supply (5) |
| Reflected super-Gaussian control | Reflection, positive source/Gram data | The exact integer-square theta expansion underlying the RS estimate |
| Smooth positive-primitive controls | Strong shape/primitive/asymptotic properties | The complete arithmetic square expansion, rather than its shared asymptotics |
| Finite-prime orbit controls | Any fixed selected-prime identities and finite measurements | Unchanged complete coefficients and full reflection |

These are failures of premises of the source import, not assertions that
each numerical inequality must fail on every collision-free box. Generic
heat and contour formulas continue to apply to the controls with their
own data. In particular \(H=P=z^2-2(t-T)\) has \(E=\mathcal R=0\)
and still merges: the reference's positive all-time discriminant margin
fails. Source fidelity and a small defect therefore do not replace the
gap payment. No negative conclusion here extends beyond the stated
fixed-cell, natural-cutoff, circular and triangle-estimate classes.

## 7. Correction-pass record

The single correction pass checked the physical factor \(-1/4\), both
branches in (4), the carrier's exponential scale, the two source naming
conventions, the full \(+1\) remainder payment in (5), and the strict
endpoint in (6). It also kept the source's \(\sigma\in[0,1]\),
\(T\ge100\) remainder hypotheses and the closed-cell cutoff conditions.
The initial derivation did not require a mathematical correction; wording
was tightened to separate available symbolic formulas from all missing
positive-margin data. This is a same-assistant check, not independent
review.
