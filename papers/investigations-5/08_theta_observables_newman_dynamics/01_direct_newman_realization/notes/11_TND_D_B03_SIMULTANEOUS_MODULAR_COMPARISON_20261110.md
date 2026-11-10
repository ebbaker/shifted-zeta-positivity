# B03: simultaneous inversion of the complete primitive pairing

10 November 2026, America/New_York. Prepared for **Edward Baker** with
substantial OpenAI Codex LLM assistance, direct chat0008, thread
`01a1c3dc-12e9-7023-a3e1-bc27d98d94d0`. Actual backend model and reasoning
effort are unavailable in the registered source metadata.

**Status: proved in-note with proof-author local checking.** This is the
one-candidate pass authorized by [Continuation07][start], using the
10 November updated [overview][overview] and [sole register][progress].
The candidate is simultaneous Poisson inversion of the two primitive
lattice factors. Its complete formula is valid. However, the specified
finite dual-prefix method with independent absolute tail payments has
no smaller envelope than the original lattice method with the same
cutoffs. A fixed dual prefix is not an absolutely integrable substitute
on the full positive-time domain. These are scoped comparison results,
not a failure theorem for joint modular estimates. **No signed collision
margin or E09 contract is obtained.**

Classification under [avoid01][a01]: exact representation and quantitative
comparison of a specified error method, not an RH criterion or a new
collision mechanism. The relevant navigation is the [result index][results],
[theta arithmetic14][theta], [controls12][controls], [avoid index][avoid],
[premise screening02][a02], [scoped exclusions07][a07] and
[joint estimates12][a12]. The proof below preserves the complete source.

## 1. Fixed object and candidate

Use [Brainstorm06][primitive]'s definitions without renormalization:
\[
 A(r)=\sum_{n\ge1}e^{-\pi n^2r^2},\quad
 \Theta(r)=1+2A(r),\quad \psi(u)=e^uA(e^{2u}),\quad D=\partial_u^2-1.
\]
For real \(\lambda,X\), \(v\ge0\), put
\[
 g(s)=e^{-vs^2/2}\cos(Xs),\quad
 T(p,q)=\frac{e^{\lambda(p^2+q^2)}}4
 [(p-q)^2g(p+q)+(p+q)^2g(p-q)],
\]
\[
 Q=D_pD_qT,\quad f(u)=T(0,u)
 =\tfrac12u^2e^{(\lambda-v/2)u^2}\cos(Xu),\quad G=Df.
\]
At \(v=0\), A0 below means its continuous zero-variance limit. The exact
pairing is
\[
 64A_0=\iint_{[0,\infty)^2}\psi(p)\psi(q)Q(p,q)\,dp\,dq
       +\int_0^\infty\psi(u)G(u)\,du.                 \tag{1}
\]
The second term divided by 64 is
\(-H_{\lambda-v/2}''(X)/16\). It is retained throughout.

All test derivatives are fixed. In particular, with \(a=p+q,b=p-q\),
\(h(s)=s^2e^{\lambda s^2/2}\) and
\(j(s)=e^{(\lambda-v)s^2/2}\cos(Xs)\), Q is one quarter of
\[
 h(b)j^{(4)}(a)+h^{(4)}(b)j(a)-2h''(b)j''(a)
 -2h(b)j''(a)-2h''(b)j(a)+h(b)j(a)
 +(a\leftrightarrow b).                              \tag{2}
\]
The domain is \(a\ge|b|\), with Jacobian 1/2. No product-domain
replacement is made. This uses the separated test and fourth-order
operator in Brainstorm06 (8).

## 2. The combined dual formula, including axes and face

The only external identity used is
\(\Theta(r)=r^{-1}\Theta(1/r)\), checked at \(z=0,\tau=ir^2\) in
[DLMF 20.7.32][dlmf], with its principal square root. Define
\[
 x=e^{-2p},\quad y=e^{-2q},\quad
 J(x)=x\Theta(x)-1=2A(1/x),\quad 0<x\le1,
\]
\[
 \widetilde T(x,y)=T(-\tfrac12\log x,-\tfrac12\log y),\quad
 \widetilde f(x)=f(-\tfrac12\log x),\quad
 \mathscr E_x=(2x\partial_x)^2-1.
\]
Direct change of variables in the already completed formula (1) gives
\[
 \boxed{A_0=\frac1{1024}\iint_{(0,1]^2}
 \frac{J(x)J(y)}{(xy)^{3/2}}
 \mathscr E_x\mathscr E_y\widetilde T\,dx\,dy
 +\frac1{256}\int_0^1\frac{J(x)}{x^{3/2}}
 \mathscr E_x\widetilde f\,dx.}                       \tag{3}
\]
Indeed \(\psi(p)dp=J(x)x^{-3/2}dx/4\) with the reversed
integration limits, and \(D_p\) pulls back to \(\mathscr E_x\).
This proves both coefficients. The arithmetic product is specifically
\[
 J(x)J(y)=xy\Theta(x)\Theta(y)-x\Theta(x)-y\Theta(y)+1.\tag{4}
\]
The two axis subtractions and the constant cannot be omitted.
The unit-sphere face is the second integral of (3); inversion has not
eliminated it. There is no new source, observation, or normalization.

These are combined integrals, not four separately integrated terms.
For \(0<x\le1\),
\[
 0<J(x)\le\frac{2e^{-\pi/x^2}}{1-e^{-3\pi/x^2}}.      \tag{5}
\]
Thus the joint expression is absolutely integrable even against the
logarithmic Gaussian growth of the test and all four transferred
derivatives. Equivalently, Brainstorm06's bound
\(\bar\psi(u)=e^{u-\pi e^{4u}}/(1-e^{-3\pi})\) dominates psi,
while Q and G have at most polynomial times Gaussian growth.
This proves the change of variables and limiting operations in (3).
The separate summands in (4) lack (5); separate integration or an
interchange with a non-absolutely convergent dual expansion is not justified.

In the sum/difference variables, (3) still has
\(a=-\frac12\log(xy), b=\frac12\log(y/x)\), hence \(a\ge|b|\).
The smaller radial domain is a coordinate transformation, not a removal
of the original infinite tail.

## 3. Literal finite dual prefixes: exact errors and a matched comparison

For an integer \(M\ge0\), let
\[
 R_M(r)=\sum_{n>M}e^{-\pi n^2r^2},\quad
 B_M(r)=\frac{e^{-\pi(M+1)^2r^2}}
                    {1-e^{-\pi(2M+3)r^2}},\quad R_M(r)\le B_M(r).
\]
The geometric bound follows by comparing successive square gaps with
\(2M+3\). The original prefix is \(A_M=A-R_M\ge0\). The literal
inverted prefix and its **exact positive error** are
\[
 C_M(r)=\frac{r^{-1}[1+2\sum_{n=1}^M e^{-\pi n^2/r^2}]-1}{2},
 \qquad E_M(r)=A(r)-C_M(r)=r^{-1}R_M(1/r)>0.           \tag{6}
\]
Unlike A_M, C_M need not be positive. Its tail envelope is
\[
 \widehat B_M(r)=\frac{e^{-\pi(M+1)^2/r^2}}
              {r[1-e^{-\pi(2M+3)/r^2}]}.
\]

**Matched-tail lemma.** For every \(r\ge1,M\ge0\),
\[
 E_M(r)\ge R_M(r),\qquad \widehat B_M(r)\ge B_M(r).  \tag{7}
\]
The inequalities are strict for \(r>1\). For each omitted n, the ratio
of the dual summand to the original summand is
\[
 r^{-1}e^{\pi n^2(r^2-r^{-2})}\ge1,
\]
because \(r^2-r^{-2}=2\sinh(2\log r)\ge4\log r\).
Summing proves the first claim. The second has the same numerator
comparison and the smaller dual denominator. Equality holds at r=1.
This compares the same M modes, not optimal algorithms or actual runtime.

Here is its consequence for the **specified independent absolute-tail
method**, including the face. Fix any finite U>0 and measurable
integer-valued cutoffs M(u)>=0. Write r=e^(2u),
\(\bar A(r)=e^{-\pi r^2}/(1-e^{-3\pi r^2})\),
and let \(b_D(u)=B_{M(u)}(r)\), \(b_P(u)=\widehat B_{M(u)}(r)\).
On the square \([0,U]^2\), a valid original-lattice error envelope is
\[
 \mathcal B_D=\frac1{64}\left\{
 \iint e^{p+q}[b_D(p)\bar A(e^{2q})+
                    \bar A(e^{2p})b_D(q)]|Q|\,dp\,dq
 +\int_0^U e^u b_D(u)|G(u)|\,du\right\}.             \tag{8}
\]
The analogous universally valid dual envelope is
\[
 \mathcal B_P=\frac1{64}\left\{
 \iint e^{p+q}[b_P(p)\bar A(e^{2q})+
       \bar A(e^{2p})b_P(q)+b_P(p)b_P(q)]|Q|\,dp\,dq
 +\int_0^U e^u b_P(u)|G(u)|\,du\right\}.             \tag{9}
\]
To see the mixed payment, the exact product difference is
\(AB-(A-E)(B-F)=AF+BE-EF\). Triangle bounds give (9);
positivity of the original retained prefixes permits dropping the
subtracted product in (8). If nonnegativity of both retained dual
prefixes has separately been established, the extra product in (9)
may also be dropped. Even this sharper specified envelope is at least
(8), by (7). In particular,
\[
                         \mathcal B_P\ge\mathcal B_D.\tag{10}
\]
All derivatives in these formulas are the exact Q and G of (2); no test
derivative is discarded. Both methods may use the same canonical
primitive identity and the same positive source envelope.

If the exterior is omitted, both methods must add the common complete
payment
\[
 \mathcal B_{\rm ext}(U)=\frac1{64}\left\{
 2\int_U^\infty\!\int_0^\infty\bar\psi(p)\bar\psi(q)|Q(p,q)|\,dq\,dp
 +\int_U^\infty\bar\psi(u)|G(u)|\,du\right\}.        \tag{11}
\]
Symmetry covers the union of the two exterior strips; their overlap is
harmlessly overcounted. This is a finite explicit integral envelope,
not an evaluated cutoff. Splitting (1), after its derivative transfer,
creates no new integration-by-parts boundary. A variable cutoff is used
only in an approximating weight; it is not differentiated. Numerical
evaluation and roundoff errors would be additional costs. None is used
to assert an A0 enclosure here.

Equation (10) does **not** order the signed approximants or actual
integrated errors, and it does not exclude a correlated signed tail
estimate. It orders exactly the stated absolute envelopes.

## 4. Why a fixed dual cutoff cannot cover the full domain

For each fixed M, expanding the finite sum in (6) gives
\[
 C_M(r)=-\tfrac12+\frac{2M+1}{2r}+O_M(r^{-3}),\quad
 e^u C_M(e^{2u})=-\tfrac12e^u+
                  \tfrac{2M+1}{2}e^{-u}+O_M(e^{-5u}).\tag{12}
\]
Thus this approximate primitive loses the decay of the true primitive.
On the inherited resolving class
\[
 \lambda_*\in[1/8,3/8],\quad X=k_*\in[1/2,100],\quad
 0<\varepsilon\le1/16,\quad \lambda=\lambda_*-\varepsilon,\ v=\varepsilon,
\]
we have \(\beta=\lambda-v/2\ge1/32\). In particular
\[
 G(u)=e^{\beta u^2}\bigl[2\beta^2u^4\cos(Xu)
                  -2\beta Xu^3\sin(Xu)+O(u^2)\bigr].\tag{13}
\]
On infinitely many fixed-width subintervals where \(|\cos(Xu)|\ge3/4\),
the leading term dominates. Equations (12)–(13) make the absolute face
integral divergent. Hence a fixed finite dual prefix cannot be substituted
for the full weight in the separately absolutely convergent integrals
(1) or (3). This is not a theorem against a regrouped joint regularization,
adaptive cutoff with paid errors, or a different modular decomposition.

A more quantitative statement concerns only **pointwise relative
primitive acquisition**. Let \(C_0=(1-e^{-3\pi})^{-1}\) and fix
\(0<\eta<1\). If \(E_M(r)\le\eta A(r)\), the first omitted dual term
and \(A(r)\le C_0e^{-\pi r^2}\) require
\[
 (M+1)^2\ge r^4-\frac{r^2}{\pi}\log(\eta C_0r).      \tag{14}
\]
Consequently \(M\ge r^2-O_\eta(\log r)\) as r grows. Conversely,
\(M=\lceil r^2\rceil\) gives
\[
 \frac{E_M(r)}{A(r)}\le
 \frac{e^{-2\pi}}{r(1-e^{-2\pi})}<\frac1{100}.        \tag{15}
\]
The original one-mode prefix already gives, for every r>=1,
\[
 \frac{R_1(r)}{A(r)}\le
 \frac{e^{-3\pi r^2}}{1-e^{-5\pi r^2}}<\frac1{1000}.  \tag{16}
\]
These coarse rational comparisons follow directly from \(\pi>3\) and
the positive exponential series. They quantify the cancellation cost
of this particular dual-prefix representation. Pointwise relative
acquisition is not necessary for every integrated signed estimate, and
(14) is not a lower bound on every algorithm for A0.

## 5. Event-scale comparison and collision controls

Keep the full [Note09][gaussian] error, with
\(b=|H_{\lambda_*}''(k_*)|>0\), \(C=I_3(3/8)\), \(D=I_4(3/8)\):
\[
 A_0=-\tfrac12b^2\varepsilon+\mathcal E,\qquad
 |\mathcal E|\le
 \tfrac{22}{3}bC\sqrt{2/\pi}\varepsilon^{3/2}
 +(2bD+\tfrac{17}{4}C^2)\varepsilon^2
 +\tfrac{11}{6}CD\sqrt{2/\pi}\varepsilon^{5/2}
 +\tfrac12D^2\varepsilon^3=:E_1.                     \tag{17}
\]
When E1<=b² epsilon/4, the hypothetical signal is at most
-b² epsilon/4. No curvature floor or common resolving radius is assumed.
The face in (1) tends to -a/16 for \(a=H_{\lambda_*}''(k_*)\),
and the bulk must tend to a/16. Inversion preserves this cancellation
exactly; (7)–(16) do not control its signed remainder. Small absolute
acquisition error alone is not an independently favorable lower bound.

The following is the analytical premise screen required by [controls12][controls].
It reuses the recorded witness evidence; no Arb certificate is rerun.

| Control | What this candidate uses or fails; scope of the witness |
| --- | --- |
| Euler-factor sources | Generic positive-source transfer survives with its own constants. Literal unit-coefficient conductor-one theta and (6) fail. Recorded negative Laguerre witnesses at lambda=.2 also give negative sufficiently narrow Gaussian averages by continuity; no new double location is claimed. |
| Weighted-square sources | Positive square support survives. Full unit coefficients and modular inversion fail. The three-square event (.25,44.13...) is in the declared class; the four-square time .01 is outside it. Their own endpoint traces must be used. |
| Reflected super-Gaussian | Positivity, full reflection and normalized primitive boundary survive; literal theta arithmetic fails. Its exact event (.25,pi/4) is in the class. With a=16cF(pi/4)>0 and its own moments, (17) is negative at small epsilon. This explicitly rejects obtaining the sign from positive primitives or endpoint normalization alone. |
| Smooth shape / positive-primitive | Strong decay, positivity and even completed primitives can survive; the complete theta square expansion fails. Their implicit damping thresholds are not newly certified in this box. |
| Finite-source and finite-prime orbit | Selected square arithmetic may survive; the full coefficients/reflection needed for (6) fail. Their high-gap events are not asserted to lie below 100. |
| Atomic / finite-profile | Suitable moment formulas can survive, but the literal theta profile and smooth primitive domains need not. No transfer of smooth-state domains is inferred. |
| Normalized endpoint perturbations | Completion and shape can survive; ordinary theta arithmetic fails. Their time-zero doubles are outside this positive-time class. |
| Fixed amplitude / variable kernel | The exact theta product and inequalities (7), (14)–(16) can hold unchanged. The cosine/Newman test (2) fails. Thus the lattice-tail comparison itself is not collision-separating. |
| Fractional-profile relaxation | It is not the physical integer zero divisor or the literal full two-source observation (1). |

The independent canonical input is the complete unit-coefficient theta
sum and its modular identity; the reflection-only part of the identity
is not separating. Failure of this input by a control does not establish
failure of an unproved signed inequality. Equations (7)–(16) are acquisition
comparisons, not proposed separating inequalities. The reflected witness
retains the sphere cancellation yet collides; the variable-kernel control
retains the actual arithmetic yet changes the test. Both checks matter.

## 6. Decision and evidence

**Stop the tested simultaneous-inversion plus independent absolute-tail
method as a source of a new signed gain in this pass.** Its exact formula
is valid, its fixed-cutoff whole-domain substitution is invalid, and its
specified paid compact error envelopes are dominated by the original
lattice envelopes. No physical or same-information computational advantage
has been proved. Joint signed regrouping, adaptive integrated error and
other lattice mechanisms remain outside these negative conclusions.

The precise remaining gap is a source-specific estimate of the *combined*
tested lattice product and curvature face which preserves their leading
cancellation and yields a useful signed remainder. Naming that desired
bound is only restating the target. No independent inequality supplying
it emerged from this inversion; therefore plan r3 section 6 is not met.
E09/E10 remain unissued. This completes the one pass, not the investigation.

[Local check08][review] and the [small record03][record] distinguish exact
algebra from three-radius floating diagnostics. They check the change of
variables, signs, mixed errors and scope; they are by the proof author,
not a separate review or a theta positivity certificate. The manuscript,
issued inputs and earlier assessments are unchanged. Continuation and
model guidance are in [Decision/Continuation08][next].

[start]: ../brainstorm/notes/07_TND_D_PRIMITIVE_LATTICE_NEXT_SESSION_20261109.md
[primitive]: ../brainstorm/notes/06_TND_D_TWO_SOURCE_PRIMITIVE_IBP_AND_LATTICE_20261109.md
[overview]: ../research-overview/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_OVERVIEW_20261105.md
[progress]: ../research-progress/01_DIRECT_NEWMAN_REALIZATION_RESEARCH_PROGRESS_20261105.md
[gaussian]: 09_TND_D_B03_GAUSSIAN_INTERFACE_AND_SIGNED_KERNEL_SCREEN_20261109.md
[next]: ../brainstorm/notes/08_TND_D_B03_MODULAR_DECISION_AND_MODEL_CONTINUATION_20261110.md
[review]: ../reviews/08_TND_D_B03_MODULAR_LOCAL_CHECK_20261110.md
[record]: ../numerics/03_TND_D_B03_MODULAR_CHECK_20261110.json
[results]: ../../../../../result-summaries/README.md
[theta]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[dlmf]: https://dlmf.nist.gov/20.7#E32
