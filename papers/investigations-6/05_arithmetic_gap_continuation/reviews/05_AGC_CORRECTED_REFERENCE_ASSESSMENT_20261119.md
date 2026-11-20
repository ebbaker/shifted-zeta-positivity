# AGC-E13 r2: nonauthor corrected-reference assessment

19 November 2026, America/New_York. Prepared for **Edward Baker** with OpenAI
Codex LLM assistance. Reviewing helper retained the explicit dispatch
**gpt-6.1-sol / ultra**; independent actual serving-backend model/effort
attestation was unavailable.

**Accepted within the stated local analytical and source-acquisition
scope.** One complete assessment and one correction check completed.
No blocking mathematical finding remains. This accepts
[Note10](../notes/10_AGC_E13_R2_HOLOMORPHIC_CORRECTION_20261119.md)
and the mathematical integration in
[manuscript Section 9](../manuscript/sections/09_corrected_reference.tex).
It does not accept a not-yet-performed corrected numerical comparison,
acquire corrected moments, or assert a new complete gap margin.

## Scope, ownership and primary import

Inputs are [E13 r2](../research-progress/handoffs/AGC-E13-r2-request.md),
[B02 r2](../brainstorm/notes/05_AGC_B02_R2_RETAINED_CORRECTION_CONTRACT_20261119.md),
the author's [return](../research-progress/handoffs/AGC-E13-r2-return.md),
source Note06 and [Review03](03_AGC_SOURCE_ALLOWANCE_LEAD_CHECK_20261119.md),
and the accepted previous analytical and numerical interfaces.

The assessor did not author Note10 or Section 9. The assessor did author
E10 note04, E13 r1 note08 and the old numerical implementation assessment
Review04. Reuse of those premises is disclosed; this report is not an
independent review of the assessor's own earlier work. The separate
[Review02](02_AGC_CONTINUATION_ESTIMATES_ASSESSMENT_20261119.md)
owns its analytical assessment. This is a separate contributing-agent
internal review, not specialist human validation or an attested
cross-model assessment.

The [result index](../../../../result-summaries/README.md),
[patterns index](../../../../avoid/README.md),
[Controls12](../../../../result-summaries/12_collision_controls_and_screening.md),
and patterns [01](../../../../avoid/01_restating_the_target.md),
[02](../../../../avoid/02_shape_only_arguments_and_the_controls.md),
[07](../../../../avoid/07_scoped_exclusions_read_as_universal.md),
[08](../../../../avoid/08_normalization_and_constant_slips.md) and
[12](../../../../avoid/12_term_by_term_matching_and_separate_bounds.md)
govern interpretation. The milestone is a paid source-allowance gain and
changed-denominator comparison on the fixed cell, not an RH-equivalent
criterion or new canonical coverage.

Reopened [Polymath v2](https://arxiv.org/html/1904.12438v2), (7), (52),
(53), (68), Corollaries 6.4/6.5 and (59). Its definitions, correction
prefactors, retained-error budget and unchanged source domain match the
frozen contract. This is a selected-import check, not a full-paper proof
audit.

## Source phase, branches and conjugation

Substitution of $s=iT$ into the actual principal carrier logarithm gives
the exponential phase
$T\log(T/(2\pi))/2-T/2-\pi/4$. The polynomial factor remains
$(iT)(iT-1)=-T(T+i)$. Multiplication by the source's $U(T)$ and the
additional $e^{i\pi/8}$ therefore gives precisely

\[
\mathfrak M_0(iT)U(T)e^{i\pi/8}
=-\frac{\sqrt\pi}{8}e^{-\pi T/4}\sqrt T(T+i).
\]

The minus sign, square-root factor and factor $1/8$ are correct.
The source correction's extra factor two and $(-1)^N$ produce the
$(-1)^{N+1}\sqrt\pi/4$ in $J_N$. At $T'=x/2+kt$,
$e^{k^2t-\pi T'/4-iky}=e^{-kz-k^2t}$. Hence the published value
correction is $J_N(t,z)A_N(T')$, whereas its holomorphic lift is
$J_N(t,z)A_N(T'+iy/2)$. Only the lift is differentiated.

The fixed rectangle gives $\Re w>7004$, $|w|<7007$ and
$|\Im w|\le1/2$. The two displayed rational comparisons with
$157/50<\pi<22/7$ imply
$1669/50<\Re\sqrt{w/(2\pi)}<3341/100$.
The identity for the imaginary part then gives

\[
9/50<\Re p<6/25,\qquad |\Im p|<1/400,\qquad |p|<1/4.
\]

The principal square root stays in its positive-half-plane branch.
The cosine identity bounds its denominator away from zero; in particular
$|2\cos(\pi p)|>7/5$. The strict bounds on the compact rectangle
provide a common open analytic neighborhood. No assertion about remote
poles or their removability is needed.

Conjugating $p(w)$ respects the principal root on this patch. The sharp
terms exchange under conjugation, so $A_N$ and then $Q_N$ have the
physical conjugation symmetry. The lower-half-plane value inequality is
therefore supplied by conjugation; no unsupported source-domain extension
is introduced.

## Explicit derivative constants

The exponential and hyperbolic-cosine estimates on the stated $p$ patch
are valid. The three explicit rational numerator expressions in Note10
are respectively below $5/2$, $7/4$, $15/2$; the denominator derivatives
are below $5$ and $20$. From $n=dC$,

\[
|C|<25/14<9/5,\quad
|C'|<215/28<8,\quad
|C''|<1235/14<90.
\]

These quotient-rule overpayments are correct and hold for the sharp
function and its derivatives on the same symmetric patch.

The exact root derivatives give the stated
$|p'|<1/200$, $|p''|<1/2800000$,
$|(\sqrt w)'|<1/166$ and
$|(\sqrt w)''|<1/2300000$.
For $A_N=\sqrt w\,B$, the author's $B'$ retains both coefficient
derivatives and both $p'$ terms; $B''$ retains the two first-derivative
terms, $p''$ and $(p')^2$ on both branches. The rational $b_0,b_1,b_2$
therefore bound the full products and chains. Their substitution gives

\[
|A_N|<1060000,\qquad |A_N'|<24000,\qquad |A_N''|<1400
\]

on the **entire** frozen rectangle. No derivative was estimated at
sampled points, and no numerical evaluation was used in this assessment.

## Complete defect, mismatch and source allowance

The identities $J_t=-k^2J$, $J_z=-kJ$,
$w_t=k$, $w_z=1/2$ give

\[
(C_{\rm hol})_t=J(-k^2A+kA'),\qquad
(C_{\rm hol})_{zz}=J(k^2A-kA'+A''/4).
\]

The $A$ and $A'$ terms cancel exactly. Thus
$R_Q=R_N-JA''/4$ has the correct sign and coefficient, and backward
time gives $(H-Q)_u=(H-Q)_{zz}+R_Q$.
The triangle payment $|R_Q|\le|R_N|+350|J|$ includes the full
new defect. The old constant scale obeys $\mathcal S|J|<1$ by the
stated elementary exponential estimate, so the added scaled triangle
payment is below $350$. This does not assert favorable cancellation
with $R_N$ or a smaller heat allowance.

The vertical path stays in the same analytic patch, and $J(t,z)$ is a
common factor in its two endpoint values. The mismatch is therefore at
most $12000|J||y|$, with no omitted derivative of $J$. The exact
leading payment satisfies

\[
L/|J|=\tfrac12\sqrt{T'}\sqrt{T'^2+1}
>\tfrac12(83)(7004).
\]

Consequently the rational checks
$24000\cdot24<83\cdot7004$ and
$2\cdot1060000<4\cdot83\cdot7004$ prove

\[
\mathcal M<|y|L/24\quad(y\ne0),\qquad
\mathcal M=0\quad(y=0),\qquad |C_{\rm hol}|<4L.
\]

The contour subcase $|y|\le9/10$ gives $\mathcal M<3L/80$.
Both source term sums and the entire retained remainder are present in
$V_Q=V_P-L+\mathcal M$. Saving more than $23L/24$ on the rectangle
and $77L/80$ on the contour follows, including $y=0$. These fractions
refer to the omitted-leading payment, not to the complete source error
or a final gap bound.

## Changed denominator, counts and complete-margin scope

At a contour point, put $q_P=V_P/|P|$ and $v=L/|P|>0$. Since
$L\le V_P$, the acquired $q_P\le q_0<23/96$ gives
$1-4v>0$. The note correctly obtains

\[
\frac{V_Q}{|Q|}
\le\frac{q_P-(23/24)v}{1-4v}<q_P.
\]

The last inequality is exactly $4q_P<23/24$; multiplying by the
positive denominator preserves its direction. The numerator is
nonnegative because $q_P\ge v$. Also $|C_{\rm hol}/P|<4q_0<1$,
so Rouché transfers count two from the already certified $P$ to $Q$,
and $m_Q\ge(1-4q_0)m_P$.

The old accepted interval record has $q_0=166454/10^6<1/6$ on
every contour slice. It therefore supplies these count and clearance
consequences, including $m_Q>m_P/3$, without a new numerical run.
This is a proved consequence of the existing certificate. It does not
pretend to be a direct new interval evaluation of $Q$. The relative
comparison is confined to the contour, where the denominator/ratio was
acquired; only the absolute source comparison is asserted on the full
rectangle. Continuity on the compact cleared contour-time set justifies
uniform strict relative improvement, without supplying an evaluated
numerical decrement.

The note correctly requires new enclosures of $c_Q,D_Q$ and complete
alias/arithmetic uncertainties before applying the common endpoint
allowance. Its concrete full-margin comparison
$\underline D_Q-B_Q>\underline D_P-B_P$ is kept separate from
the source gain. A time/heat calculation must also pay the actual
$R_Q$, initial and both lateral $H-Q$ data. Direct evaluation of
the same $Q$ receives identical information and may use the same refined
estimator. No representation or cost advantage is inferred.

The source gain and count transfer therefore satisfy the analytical
milestone. They do **not** establish a stronger corrected all-time
discriminant margin, new coverage or a Newman bound.

## Controls and integration correction check

The quadratic $H=Q=(z-X)^2-2(t-T)$ still has zero approximation
error/defect and a discriminant reaching zero. The strict complete gap
margin fails there. The theta-specific retained budget is not assigned
unchanged to Euler-factor, weighted-square, finite-prime, finite-profile,
reflected or primitive controls. Their failed source-identification
premise is distinguished from an actual quantitative rejection.
The lack of an all-real anchor in the documented finite-source class,
the hypothesis and escaping-location scope of RH-conditional controls,
and the physical-forcing failure of changed observation kernels are
retained. Generic local identities remain valid with each control's own
data. No universal exclusion of corrected references follows.

The correction check read the lead's final Section 9 integration after
it was aligned to Note10's simpler root/chain constants. The explicit
$U$ definition, numerator/denominator derivative payments, full product
rules, local branch bounds, phase sign, defect, vertical mismatch and
changed-denominator comparison all agree with the accepted source note.
The compressed proof is mathematically consistent, including its
equivalent convention $A_N=(\sqrt w/2)B$ with the doubled bracket.
No additional mathematical correction was required. No assessed source
or manuscript file was edited by this assessor.

One complete analytical assessment and one integration correction check
were used. No numerical run, precision change, parameter search or
coverage campaign was performed. A separately frozen E12 r2 may evaluate
the corrected source/contour inputs after this acceptance; its code,
record and complete-margin conclusions require their own assessment.
