# One-direction gap collisions and a uniform tail budget

17 October 2026, America/New_York. Prepared for Edward Baker with substantial
LLM assistance. Recorded model **gpt-6.1-sol (Codex)**, reasoning effort
**ultra**. Same-model analytic assistance and routine interval checks; no
new cross-model or specialist assessment. This continues [Note 01][n01]
and the [round-one Claude review][review].

**Status: proved in-note, using named published theta inputs; interval
evaluation of two fixed sufficient tail bounds.** The new analytic gain is
that one fixed direction suffices for nondegenerate collisions somewhere
inside every sufficiently high theta-zero gap at every fixed \(t>0\),
including \(t=1/4\). The original
two-direction theorem places events at every sufficiently large prescribed
abscissa; its stronger location quantifier remains distinct.

The governing context is the [result-summary index][results], [cluster
12][controls], [cluster 14][arithmetic], [avoid index][avoid], [avoid
01][a01], [02][a02] and [07][a07]. This is an approximation-class
instability theorem, not an RH criterion. No collision of theta is asserted.

## 1. Published inputs and their normalization

We use exactly \(H_t(z)=\int_0^\infty e^{tu^2}\Phi(u)\cos(zu)\,du\), with
\(H_0(z)=\xi((1+iz)/2)/8\). In [Polymath, arXiv:1904.12438v2][polymath],
Theorem 1.1 gives \(\Lambda_\theta\le0.22\); Proposition 3.1(ii) describes
the Hermite splitting at a multiple zero. Thus, at any fixed
\(t_*>\Lambda_\theta\), every theta zero is real and simple: otherwise
the splitting produces non-real zeros at a slightly earlier time still
above \(\Lambda_\theta\). In particular \(t_*=1/4\) qualifies without RH.
The source and frequency conventions agree with the paper's (3)–(4).

We also use Hadamard factorization for order-one entire functions. The
paired product is recorded in Polymath's proof of Proposition 3.1. The
theta transform has infinitely many zeros (the positive imaginary-axis
growth argument in Note 01 also applies to theta). List its positive zeros
as \(r_j\to\infty\). Evenness and order one give the locally uniform product

\[
H(x)=H(0)\prod_j(1-x^2/r_j^2),\quad H(x)=H_\theta(t_*,x).
\]

Away from its zeros,

\[
(\log|H|)''(x)
=-\sum_j\left\{(x-r_j)^{-2}+(x+r_j)^{-2}\right\}<0. \tag{1}
\]

The differentiated series converges locally because the zero sequence of
an order-one entire function has \(\sum_jr_j^{-2}<\infty\). These imported
facts are checked against the cited primary text; no effective
Riemann–Siegel estimate is imported into the following argument.

## 2. A one-direction theorem, including nondegeneracy

**Theorem.** Fix a nonzero finite vector \(v\), with any homogeneous linear
constraints already imposed, and let \(F(x)=H_{f_v}(t_*,x)\). If
\(t_*>\max(0,\Lambda_\theta)\), then, in every sufficiently high consecutive positive
theta-zero gap \((z_j,z_{j+1})\), there is a unique \(x_j\) satisfying

\[
(H/F)'(x_j)=0.
\]

For \(s_j=-H(x_j)/F(x_j)\), the frozen source \(\Phi+s_jf_v\) has a
nondegenerate double zero at \((t_*,x_j)\). Its coefficients are strictly
positive for sufficiently large \(j\), and \(s_j\to0\) faster than every
inverse power of \(x_j\). It preserves every imposed homogeneous linear
constraint. Uniqueness here concerns this one direction within each
sufficiently high gap; it does not assert a unique collision in a larger
coefficient space or across all heat times.

**Proof.** Let \(p\ge2\) be the even endpoint exponent of \(f_v\). Apply the
endpoint integrations separately to the first two physical derivatives,
with enough terms, to obtain

\[
F=ax^{-p}(1+O(x^{-2})),\quad
F'=-pa x^{-p-1}(1+O(x^{-2})),\quad
F''=p(p+1)a x^{-p-2}(1+O(x^{-2})),\quad a\ne0.
\]

In particular \(F\) has no zeros at sufficiently large positive height,
and direct division, without differentiating an unspecified remainder,
gives

\[
(\log|F|)''=F''/F-(F'/F)^2=p/x^2+O(x^{-4})>0. \tag{2}
\]

Put \(R=H/F\). On a high gap \(R\ne0\), vanishes at its endpoints, and
by (1)–(2),

\[
(\log|R|)''<0.
\]

Its logarithmic derivative tends to \(+\infty\) at the left endpoint and
to \(-\infty\) at the right endpoint, since the zeros of \(H\) are simple
and \(F\) is nonzero. Hence it has exactly one zero \(x_j\). At that point

\[
R'(x_j)=0,\qquad R''(x_j)/R(x_j)=(\log|R|)''(x_j)<0.
\]

Thus \(R''(x_j)\ne0\) and \(s_j\ne0\). Set \(G=H+s_jF\), keeping \(s_j\)
constant when differentiating. From \(H=RF\),

\[
G(x_j)=G'(x_j)=0,\qquad G''(x_j)=F(x_j)R''(x_j)\ne0. \tag{3}
\]

The heat equation then gives the local real/non-real splitting proved in
round-one Note 04. Finally \(H(x)=O_K(x^{-K})\) for every \(K\), whereas
\(|F(x)|\ge |a|x^{-p}/2\) eventually. Therefore \(s_j=O_K(x_j^{-K})\) for
every \(K\); all \(1+s_jv_n>0\) eventually. Linear constraints remain exact
because the perturbation is a scalar multiple of \(v\). ∎

This proves the one-dimensional local-collision assertion that does not
follow merely from the non-reality proposition. This elementary proof
uses \(t_*>\Lambda_\theta\); §2a removes that restriction by a different
published input. Neither proof requires sampling additional high gaps.
In an interval ending at \(1/4\), the non-real side of its endpoint
collision lies at times just below \(1/4\).

For a one-dimensional measurement space \(V=\mathbb Rv\), with \(Mv\ne0\),
the theorem also gives exact saturation of the sufficient radius at \(x_j\):

\[
r_M=|s_j|\|Mv\|=\frac{\|h\|\|Mv\|}{\|Bv\|}=\eta. \tag{4}
\]

If \(Mv=0\), this nonzero perturbation is exactly invisible to \(M\).
For an ambient higher-dimensional \(V\), the constructed collision gives
an upper bound for its optimum, not equality in (4) for the ambient map.

## 2a. Extension to every fixed positive heat time

**Theorem.** The one-direction theorem of §2 holds for every fixed
\(t_*>0\). Its sufficiently large gap cutoff may depend on \(t_*\) and
the direction. No uniform cutoff as \(t_*\downarrow0\), numerical onset,
or conclusion at \(t_*=0\) is asserted.

**Proof.** For \(0<t_*\le1/2\), [Polymath][polymath] Theorem 1.5(i) states that all
zeros with sufficiently large positive real part are real; part (ii)
gives one zero in each sufficiently high model disk. Its §9 proof uses
winding number one and the argument principle, so the zero count includes
multiplicity: these zeros are simple. Combined with (i), the high real
zeros exhaust the high zeros and form an unbounded sequence. The same
paper recalls the global strip \(|\operatorname{Im}z|\le1\); evenness
provides the corresponding negative-real-part cutoff. Consequently all
nonreal zeros lie in a compact rectangle and are finite in number. For
\(t_*>1/2\), its bound \(\Lambda_\theta\le0.22\), together with the
multiple-zero Hermite splitting, gives real and simple zeros everywhere.
The imaginary-axis growth argument supplies infinitely many zeros in
this case as well.

Fix the time and let \(\mathcal E\) be the finite multiset of nonreal
zeros in the upper half-plane, each included with its multiplicity.
Write \(\rho=\alpha+i\beta\) in this multiset. Hadamard factorization,
order one, and real symmetry give, for real \(x\) away from real zeros,

\[
(\log|H|)''(x)
=-\sum_{r\in\mathcal Z_{\mathbb R}}\frac1{(x-r)^2}
 -2\sum_{\rho\in\mathcal E}
   \frac{(x-\alpha)^2-\beta^2}
        {((x-\alpha)^2+\beta^2)^2},
\]

where the real-zero multiset also includes multiplicities. The infinite
sum converges locally away from its zeros because order one gives
\(\sum_{r\ne0}|r|^{-2}<\infty\); there is no quadratic exponential
factor. For
\(x>\max_{\rho\in\mathcal E}(\alpha+|\beta|)\), every term in the finite
sum is negative. The real-zero terms are negative as well, so
\((\log|H|)''<0\) eventually. If \(\mathcal E\) is empty, the same
conclusion follows from the real-zero sum alone.

For the chosen finite direction, the separately justified endpoint
derivative expansions still give
\((\log|F|)''=p/x^2+O(x^{-4})>0\). Thus \(\log|H/F|\) is strictly
concave in every sufficiently high consecutive real-zero gap. Its
logarithmic derivative runs from \(+\infty\) to \(-\infty\), since those
endpoints are simple. Exactly one critical point follows, with nonzero
ratio and nonzero second derivative. The remaining proof in §2 applies
unchanged: \(s_j=-H/F\) produces a frozen nondegenerate double zero,
\(s_j\) decreases faster than every inverse power, coefficients are
eventually strictly positive, and imposed homogeneous constraints remain
exact. Positive-time local splitting follows by taking a sufficiently
small neighborhood of the fixed positive time. ∎

This strengthens the earlier \(t_*>\Lambda_\theta\) version by using
Polymath's eventual-real-zero theorem. It does not assume RH or import
real-rootedness of the entire theta transform at small positive times.


**Measurement corollary on any positive heat interval.** Let \(T>0\),
let \(V\ne\{0\}\) be a fixed finite coefficient space preserving its imposed
homogeneous constraints, and fix a finite linear measurement \(M\).
Choose any \(v\in V\setminus\{0\}\) and \(0<t_*<T\). The theorem gives
positive normalized sources with nondegenerate events at that time and
unbounded heights, with \(\|M(s_jv)\|\to0\). Their local real/non-real
splittings can be kept inside \((0,T)\). Therefore no positive absolute
measurement tolerance excludes all such collisions on the unbounded height
domain, even when \(\dim V=1\). Injectivity is unnecessary for this
obstruction. This supplies a separate proof of the dimension-one extension
suggested in review §4(a); non-real zeros at all times alone did not supply it.
The prescribed-abscissa construction remains a two-direction statement.


## 3. A fixed tiny change removes all high real zeros

Take the already declared normalized direction

\[
A=e_2-(\beta_2/\beta_1)e_1,\qquad
\beta_n=(4\pi n^2-1)e^{-\pi n^2}.
\]

Round-one Notes 02 and 05 supply, uniformly for \(0\le t\le1/4\),

\[
|H_\theta(t,x)|\le K e^{-\kappa x},\quad K=6/5,\quad\kappa=\pi/16,
\]

\[
H_A(t,x)=a/x^2+R_A(t,x),\quad |R_A(t,x)|\le E_A/x^4,
\]

with \(a=0.0395122594985\ldots>0\) and \(E_A<745.331444\). Whenever

\[
|s|(a/x^2-E_A/x^4)>K e^{-\kappa x}, \tag{5}
\]

the fixed source \(\Phi+sf_A\), for either sign of \(s\ne0\), has no real
zero at that height. For \(a/x^2-E_A/x^4>0\), the ratio of the two sides
has logarithmic derivative

\[
\kappa-2/x+\frac{2E_A}{x^3(a-E_A/x^2)}>\kappa-2/x.
\]

It therefore suffices to check (5) once at \(X>2/\kappa\), with positive
tail lower bound. The [producer][tail-code] recomputes the fixed directional
budget from its exact formulas, validates its producer binding, then uses
Arb for the following two predetermined cases:

| Absolute error units | Multiplier \(s\) in magnitude | Sufficient \(X\) | Lower bound / theta upper bound at \(X\) |
| --- | --- | --- | --- |
| Coefficient multiplier | \(10^{-16}\) | 264 | (>1.12069) |
| Original raw recurrence Euclidean norm | \(10^{-16}/\|M_{\rm rec}A\|_2\) | 269 | (>1.19200) |

Here \(\|M_{\rm rec}A\|_2=2.450051\ldots\), computed from the exact
zero-padded second-difference rows; the [record][tail-record] carries the
full ball. The changed coefficients remain strictly positive and exactly
normalized. Both conclusions hold for every \(x\ge X\) and every
\(0\le t\le1/4\), with the same fixed coefficients for each row. These
are sufficient tail-domination bounds, not the first loss of real zeros.
No finite value for \(\eta\) at \(x=140\) is inferred. The review's floating
illustration near 145 remains its own diagnostic, and is not rerun here.

## 4. What the error scale says analytically

More generally, suppose one fixed direction has endpoint exponent \(p\),
leading magnitude \(|a|>0\), a uniform remainder \(E x^{-p-2}\), and the
complete source has the envelope \(Ke^{-\kappa x}\) on a declared heat
interval. For \(x\ge\sqrt{2E/|a|}\), a sufficient condition is

\[
\kappa x-p\log x> L,\qquad L=\log\frac{2K}{|sa|}. \tag{6}
\]

As \(|s|\to0\), one may choose a sufficient threshold

\[
X_s=\kappa^{-1}\{L+p\log L+C\},\qquad C>-p\log\kappa,
\tag{7}
\]

once \(L\) is large enough that this also exceeds the fixed endpoint and
monotonicity onsets. Substitution gives

\[
\kappa X_s-p\log X_s-L=C+p\log\kappa+o(1)>0.
\]

Thus the scale of this **sufficient envelope bound** is

\[
\kappa^{-1}\log(1/|s|)
+(p/\kappa)\log\log(1/|s|)+O(1).
\]

This is an analytic consequence of named estimates, not a fitted law or
an asymptotic for an actual last zero. The half-rate envelope governs
\(\kappa\); it does not establish the optimal carrier rate or make 269 an
optimal threshold. With a fixed measurement norm \(\|M(sv)\|=|s|\|Mv\|\),
changing from multiplier to measurement units shifts \(L\) by a fixed
constant. No support growth or adaptive design is covered.

## 5. Controls and the round boundary

Weighted-square controls and these finite theta-tail changes share the
endpoint obstruction; neither preserves full reflection. Euler-factor,
reflected super-Gaussian and smooth/primitive controls are screened by the
different membership qualifications stated in Note 01 and cluster 12.
The published inputs concern unperturbed theta: global real-rootedness
above \(\Lambda_\theta\), and eventual real/simple zeros at each positive
time. They are not assumptions of real-rootedness for a control and supply
no conclusion about theta's zeros at \(t=0\).

The bounded reconciliation now has a written answer: prescribed-point
distances need their location qualifier; every nonzero nonnegative finite
change has non-real zeros at all times; one direction already creates
nondegenerate nearby collisions in high gaps at each fixed \(t>0\); and the two
sufficient tail heights reproduce without a grid. New computation needs
a separate consumer, such as an estimate for a reflected or
infinite-dimensional class. The work is ready for an accumulated round-two
assessment; no external review is commissioned here.

[n01]: 01_REVIEW_RECONCILIATION_AND_ENDPOINT_NONREALITY_CODEX_20261017.md
[review]: ../../reviews/01_ROUND_ONE_CROSS_MODEL_REVIEW_CLAUDE_20261017.md
[tail-code]: ../../numerics/round-2/no_real_tail_certificate.py
[tail-record]: ../../numerics/round-2/NO_REAL_TAIL_CERTIFICATE.json
[polymath]: https://arxiv.org/html/1904.12438v2
[results]: ../../../../../result-summaries/README.md
[controls]: ../../../../../result-summaries/12_collision_controls_and_screening.md
[arithmetic]: ../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../../avoid/README.md
[a01]: ../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../avoid/07_scoped_exclusions_read_as_universal.md
