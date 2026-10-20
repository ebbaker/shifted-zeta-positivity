# An exact one-dimensional fourth-order Schur consumer

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Authoring model **gpt-6-astra (Codex)**;
actual reasoning effort **ultra**, inherited from the parent turn.

**Status: conditional algebraic interface, proved in-note; no acquired
theta sign or fourth-order coverage gain.** The complete center and one
shared analytic residual give an exact event-conditioned coefficient
class through order four. Its signed quadratic supremum reduces to one
real parameter, after an endpoint choice and a quadratic maximization.
This retains the source center and all residual correlations. It does not
replace the source by arbitrary multiplier directions. The bounded
theta application selected in this round is subject to a first-jet screen
before this consumer is used; an empty feasible set yields no fourth-order
gain.

This is a finite coefficient optimization theorem under an independently
paid analytic error hypothesis, classified under [avoid/01][a01] as an
estimating interface rather than a reformulation of the desired sign.
Follow the [result summaries][results], [avoid index][avoid],
[collision controls][controls], [scope discipline][a07] and
[signed recombination rule][a12]. The [round contract][contract] owns
the actual domain, source acquisition and stopping decision.

## 1. Input and exact event feasibility

At a real point \(a\), let \(F=H/A=P+r\), where \(A\) is real and
nonzero on the real domain and holomorphic and nonvanishing on the
closed disk \(|z-a|\le R\). Let \(P\) and \(r\) be real-symmetric
holomorphic functions there, with
\[
 |r(z)|\le\eta,\qquad R>0,\quad\eta\ge0.
 \tag{1}
\]
An open neighborhood of the closed disk, or the corresponding limiting
boundary bound, suffices. All source, truncation, parameter, normalization
and arithmetic errors in (1) require independent payment. Write
\(p_j=P^{(j)}(a)\), \(f_j=F^{(j)}(a)\), and
\(\kappa=L+(\log A)_{xx}(a)\).

At \(H=H_x=0\), nonvanishing \(A\) makes \(f_0=f_1=0\), and the
physical target is
\[
 q:=Q_L/A^2=2f_3^2-3f_2f_4-18\kappa f_2^2.
 \tag{2}
\]
The identity preserves the signed mixed term. Its verification and source
normalizer belong to the complete fourth-order interface. If \(A=1\),
then \(\kappa=L\) and \(q=Q_L\).

If \(\eta=0\), the residual is zero; feasibility is exactly
\(p_0=p_1=0\), and (2) is evaluated at \(p_2,p_3,p_4\).
Assume henceforth \(\eta>0\), and put
\[
 g(w)=r(a+Rw)/\eta,\qquad u=-p_0/\eta.
 \tag{3}
\]
The real Schur class is the set of real-symmetric holomorphic functions
bounded by one on the unit disk. If \(|u|<1\), its first transform yields
\[
 v=-\frac{Rp_1}{\eta(1-u^2)},\qquad |v|\le1.
 \tag{4}
\]
Thus the exact necessary and sufficient event-feasibility test in this
residual information class is
\[
 \boxed{p_0^2+\eta R|p_1|\le\eta^2.}
 \tag{5}
\]
For sufficiency when \(|u|<1\), the real Schur function
\(g(w)=(u+vw)/(1+uv\,w)\) realizes both required coefficients.
When \(|u|=1\), (5) forces \(p_1=0\), and the maximum-modulus
principle forces \(g\equiv u\). If \(|u|>1\), feasibility fails.
Equality in (5) with \(|u|<1\) forces \(|v|=1\), also uniquely fixing
that Möbius residual.

This is feasibility for a paid **enclosing residual class**, not existence
of a physical theta event or a permissible theta perturbation. Conversely,
strict failure of (5), certified uniformly on a parameter cell, excludes
the actual event there. One must execute that cheaper test before optimizing
(2). A near-zero numerical first jet is not an exact event constraint.

## 2. Complete fourth-order coefficients

Let \(s=1-u^2\), \(t=1-v^2\). Three further real Schur parameters
\(c,d,e\in[-1,1]\) parameterize exactly the remaining coefficients
through order four. Write \(g(w)=\sum_{j\ge0}b_jw^j\). Then
\[
 b_0=u,\qquad b_1=sv,
\]
\[
 b_2=s(tc-uv^2),
 \tag{6}
\]
\[
 b_3=s\{t[(1-c^2)d-vc^2]-2uvtc+u^2v^3\},
 \tag{7}
\]
\[
\begin{split}
 b_4=s\{&
 t(1-c^2)[(1-d^2)e-cd^2-2v(c+u)d]\\
 &+tv^2c^3+2uv^2tc^2-ut^2c^2+3u^2v^2tc-u^3v^4\}.
\end{split}
 \tag{8}
\]
The physical normalized derivatives are
\[
 f_j=p_j+\eta j!b_j/R^j,\qquad j=2,3,4.
 \tag{9}
\]
The factorials in (9) distinguish derivatives from Taylor coefficients.

For a direct proof, use the inverse Schur step
\[
 {\cal M}_a(h)(w)=\frac{a+wh(w)}{1+awh(w)}.
 \tag{10}
\]
Starting from the constant \(e\), apply \({\cal M}_d,{\cal M}_c,
{\cal M}_v,{\cal M}_u\) in that order. Every parameter tuple gives a
Schur function; every permitted coefficient tuple is obtained by four
Schur steps. The coefficients through degree four do not depend on the
unretained tail after \(e\). Expanding (10) gives (6)–(8).
At a boundary parameter, the corresponding transform is constant and
all deeper parameters disappear. Thus the closed cube parameterization
remains valid without dividing by \(1-c^2\) or \(1-d^2\).

In particular, for \(|v|=1\),
\[
 b_j=s(-u)^{j-1}v^j\quad(j\ge1);
 \tag{11}
\]
for \(|u|=1\), all \(b_j=0\) for \(j\ge1\). These degenerate
feasible cases must not be silently discarded by a numerical solver.

## 3. Eliminate two optimization variables exactly

For fixed \(c\), define
\[
 X=p_2+\frac{2\eta s}{R^2}(tc-uv^2),
\]
\[
 Y=p_3+\frac{6\eta s}{R^3}
       (-tvc^2-2uvtc+u^2v^3),
\qquad
 B=\frac{6\eta st(1-c^2)}{R^3},
\]
\[
 Z=p_4+\frac{24\eta s}{R^4}
   (tv^2c^3+2uv^2tc^2-ut^2c^2+3u^2v^2tc-u^3v^4),
\qquad
 E=\frac{24\eta st(1-c^2)}{R^4}.
 \tag{12}
\]
Here \(B,E\ge0\). Equations (6)–(9) become
\[
 f_2=X,\quad f_3=Y+Bd,\quad
 f_4=Z+E\{(1-d^2)e-cd^2-2v(c+u)d\}.
 \tag{13}
\]
For fixed \(c,d\), the coefficient of \(e\) in (2) is
\(-3XE(1-d^2)\). Hence its maximum is obtained at
\(e=-\operatorname{sign}(X)\); either endpoint suffices when \(X=0\)
or the coefficient vanishes. The resulting expression is
\[
 q_{\max e}=C+Dd+Jd^2,
 \tag{14}
\]
where
\[
 C=2Y^2-3XZ+3|X|E-18\kappa X^2,
\quad
 D=4YB+6XEv(c+u),
\quad
 J=2B^2+3E(Xc-|X|).
 \tag{15}
\]
This quadratic is not always convex. Assuming its maximum is always
at \(d=\pm1\) would discard valid worst cases.

For real \(J,D\), put
\[
 M(J,D)=
 \begin{cases}
 -D^2/(4J),&J<0\ \hbox{and}\ |D|\le-2J,\\
 J+|D|,&\hbox{otherwise}.
 \end{cases}
 \tag{16}
\]
This is exactly \(\max_{|d|\le1}(Jd^2+Dd)\): in the first case the
concave vertex is inside the interval, and otherwise an endpoint is
optimal. The two formulas agree at the transition.

Consequently, for fixed exact input data satisfying (5),
\[
 \boxed{U_{\rm Schur}=\max_{-1\le c\le1}
      \{C(c)+M(J(c),D(c))\}.}
 \tag{17}
\]
This is the exact maximum for the shared-disk residual information
class. It is a continuous, piecewise algebraic one-dimensional problem.
The only division in (16) is used with \(J<0\); there is no singular
division on the other branch. At \(c=\pm1\), \(B=E=0\), and (17)
reduces to the one fixed jet for that endpoint.

The class in (17) includes \(f_2=0\). It is a valid enclosure of ordinary
double events, which require \(f_2\ne0\). If there exists at least one
feasible jet with nonzero \(f_2\), removing the zero-curvature slice
does not change the supremum: for \(st>0\), \(X(c)\) is nonconstant
affine, so the possible isolated excluded value of \(c\) is a limit of
admissible values; for \(st=0\), \(X\) is fixed. If the sole possible
\(X\) is zero, the ordinary-double class is empty. A quantitative
floor \(|f_2|\ge m>0\) changes the class and must be independently paid.

For interval source inputs over a domain \(D\), (17) alone is not a
uniform numerical certificate. Retain the dependence of \(p_j,\eta,R,
\kappa\) on the actual \((T,a)\), or outwardly enclose every resulting
parameter on a complete closed cover. Cells straddling the branch
conditions in (16) can use the unsimplified quadratic (14), or certified
branch subdivision. A solver's sampled maximum is insufficient. No
particular subdivision or runtime is prescribed by this theorem.

## 4. Strongest comparator from given independent component intervals

Suppose the same paid information gives component intervals
\(f_j\in[\ell_j,u_j]\), \(j=2,3,4\), and a fixed \(\kappa\).
These can be the direct Cauchy intervals
\(p_j\pm\eta j!/R^j\), exact coordinate projections of the constrained
class, or stronger source-informed intervals; name which were acquired.
The strongest bound that treats these three intervals independently is
\[
 U_{\rm box}=2\max\{\ell_3^2,u_3^2\}
 +\max_{x\in[\ell_2,u_2]}
       \{-18\kappa x^2-3x\,v(x)\},
 \quad
 v(x)=
 \begin{cases}\ell_4,&x\ge0,\\u_4,&x\le0.\end{cases}
 \tag{18}
\]
The two choices coincide in contribution at zero. Split the \(x\)
interval at zero. On each nonempty part, evaluate its endpoints and,
when \(\kappa>0\), the vertex \(x=-v/(12\kappa)\) if that vertex
lies in the part. For \(\kappa\le0\), endpoints suffice. Thus (18)
is exact for the declared independent-box information class, retaining
the negative square term even when the sign of \(f_2\) varies.

If \(\kappa\) is independently enclosed by
\([\kappa_-,\kappa_+]\), use \(\kappa_-\); the expression decreases
with \(\kappa\). This loses any coupling between the normalizer and
jets and should not be presented as a fully coupled optimum.

When the same joint Schur class is contained in the declared box,
\(U_{\rm Schur}\le U_{\rm box}\). Strict inequality is **not**
automatic: zero residual or a degenerate event class may make them
equal. More generally, the strongest applicable complete-source
reference can beat both. Report
\(G_Q=U_{\rm base}-U_{\rm new}\) against that reference, with one
normalization and the same \(L\). If the first-jet test already excludes
every event, report “event class empty; \(G_Q\) not applicable,” rather
than manufacture a fourth-order margin by assigning a number to
the supremum of the empty set.

## 5. A complete algebraic fixture with a scoped strict gain

One explicit fixture checks the endpoint/vertex machinery and shows what
it does **without claiming theta input**. Set \(P=0,\eta=R=1,A=1\)
and \(L>0\). Then \(u=v=0\), \(f_2=2c\),
\(f_3=6(1-c^2)d\), and
\(f_4=24(1-c^2)[(1-d^2)e-cd^2]\).
In (15), \(D=0\) and
\(J=72(1-x^2)(1-x)^2\ge0\), where \(x=|c|\).
Consequently the \(d\) maximum is at \(|d|=1\), giving
\[
 U_{\rm Schur}=
 \max_{0\le x\le1}\{72(1-x^4)-72Lx^2\}=72.
 \tag{19}
\]
The maximum is attained at
\(c=0,\ |d|=1\). Even after \(f_2=0\) is omitted, the supremum
remains \(72\), by taking \(c\to0\).

Independent Cauchy intervals are
\(f_2\in[-2,2],f_3\in[-6,6],f_4\in[-24,24]\).
Their exact bound from (18) is
\[
 U_{\rm box}=72+\max_{0\le x\le2}(72x-18Lx^2)
 =72+
 \begin{cases}
 144-72L,&0<L\le1,\\
 72/L,&L\ge1.
 \end{cases}
 \tag{20}
\]
This gives a strictly positive matched reduction, but the best shared
Schur bound remains positive. The fixture is an exact synthetic
information-class check, with \(P=0\); it is **not** a fourth-order
arithmetic gain, a theta source estimate, or a counterexample heat flow.

## 6. Paid bounded application and the remaining source request

The selected bounded acquisition uses physical \(A=1\), \(R=1/2\),
and the domain
\[
 D_*=[99999/10^6,100001/10^6]\times
     [29999999/10^6,30000001/10^6].
 \tag{21}
\]
The [round contract][contract] and Project 11's complete fourth-order
source record supply the exact center polynomial and shared analytic
residual. This lies inside previously covered finite territory. The
fresh 192/256-bit direct-source enclosure gives, conservatively,
\[
 |H(T,a)|>9.07289607819\,10^{-5}\quad((T,a)\in D_*).
 \tag{22}
\]
The real-contour center has shared disk residual
\(\eta<9.473581\,10^{-30}\), and the paid interval lower bound on the
left side minus right side of (5) is greater than
\(8.2317443245\,10^{-9}\).
Thus even \(H=0\) is impossible throughout this small box, and the
Schur event class is empty. The strongest applicable direct reference
already excludes the event. No optimizer is run on this empty class;
\(U_{\rm base},U_{\rm new},G_Q,d_Q,\delta_Q\) for an event-conditioned
fourth-order comparison are **not applicable**. These figures validate
the source interface and the early rejection path; they supply neither
new coverage nor a fourth-order arithmetic gain. The consumer in
Sections 1–4 remains available for a future nonempty information class.

For the unresolved UAR sector, the present theorem names the missing
producer precisely: a single, coherent, cutoff-frozen fourth-order
center \(P(T,z)\), together with a proved uniform **value** bound for
the complete residual \(H/A-P\) on the common complex disk used by
(1), and a paid enclosure of \((\log A)_{xx}\). A complete value
bound on that disk would already imply every needed residual derivative
by Cauchy; no separate fourth-derivative source theorem is logically
required. But a bound for the rotating residual *increment*, an
endpoint expression, or a real-axis value does not supply (1).
The widened UAR saddle disk is a promising analytic ingredient, not
a verified complete fourth-order input here. The retained finite and
edge terms, source tails, gamma/heat correction, normalizer, cutoff
overlap, and parameter variation still need assembly on one domain.

In particular, direct first-order time propagation of physical \(h_4\)
uses \(h_6\), because \(\partial_t h_4=-h_6\). A normalized residual
does not inherit the unmodified heat equation. New cutoff transitions
cannot be absorbed by differentiating a floor function. These are
specific acquisition obligations, not evidence that a source-specific
fourth-order bound is impossible.

## 7. Controls and disposition

The exact Schur parameterization is source-neutral. Every control
admitted by its own complete analytic disk allowance and exact event
data must remain feasible, so it cannot falsely exclude that event.
The positive continuous and atomic threshold controls retain their
positive \(Q_L\) when their own center and errors enclose their exact
jets. Theta's error allowance must not be assigned to them.
Euler-factor, weighted-square and finite-prime controls do not retain
unchanged theta coefficients; reflected and positive-primitive controls
do not identify the theta square expansion. Polynomial event fixtures
test the algebra and acceptance semantics without inheriting any theta
source budget. Free arithmetic phases are not used here.

The [exact rational fixture checker][checker] compares (6)–(8) with
nested Möbius expansions, checks the endpoint elimination, the quadratic
vertex branch, boundary parameters and the comparator. It tests the
finite algebra, not the source residual bound. Its small
[execution record][record] contains the retained check counts and source
hash. No numerical theta optimizer, theta sign, new region, manuscript
snapshot or global obstruction is claimed by this note.

[results]: ../../../../../result-summaries/README.md
[avoid]: ../../../../../avoid/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[contract]: 04_FOURTH_ORDER_SOURCE_CONTRACT_20261020.md
[checker]: ../numerics/check_event_conditioned_schur.py
[record]: ../numerics/EVENT_CONDITIONED_SCHUR_CHECKS_20261020.json

The [round assessment](../../04_boundary_winding/reviews/03_FOURTH_ORDER_AND_ACTUAL_PROFILE_ROUND_REVIEW_20261020.md) records separate same-model review and fresh exact-checker replays. Recursive and expanded formulas are distinct algebraic checks within the same implementation; no independent theta implementation is claimed.
