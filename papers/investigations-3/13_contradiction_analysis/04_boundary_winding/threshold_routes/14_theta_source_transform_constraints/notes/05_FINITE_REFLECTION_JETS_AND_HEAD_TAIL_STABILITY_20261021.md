# Finite reflection jets and quantitative head–tail cancellation

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**, checked against this chat's turn metadata.
Analytic continuation; same-assistant [self-review][review], without
independent specialist review or a novelty claim.

## 1. Result, classification and comparison

This executes a concrete part of the next action in [Note 04][n04]: keep
its actual complete tail in a signed relation with the retained head,
and use full reflection in the estimate itself. The result is a
quantitative approximation and stability theorem, **not a lower bound
for the theta jet**.

Subtracting a finite Taylor expansion of the head's vertical connector
gives an explicit approximant. Full reflection bounds the remaining
connector by the **omitted tail's** analytic norm, rather than by a
separate norm of the head. The complete physical error consists of the
existing shifted tail plus an explicit incomplete-Laplace integral.
All spectral derivatives use the same remainder.

The theorem quantifies two regimes:

- With a fixed source disk and contour, a number of reflection terms
  proportional to height suffices to recover an exponentially small
  connector error. A sharp exponential rate in the declared analytic
  disk class explains why a sublinear schedule cannot guarantee this.
- With the disk and contour approaching the source-strip boundary,
  there is a schedule with O(sqrt(x)) retained modes and O(x) reflection
  terms whose error is o(x^(7/4) exp(-pi*x/8)). This is relative to the
  explicit gamma envelope, **not relative to H or its jet norm**.

The comparator is the existing reflected-contour approximant, with the
same modes, contour and tail payment. It already removes the whole
connector exactly and needs no finite Taylor remainder. Accordingly
this result establishes a rate and robustness cost for finite reflection
data; it does not improve that evaluator's error or its cost. S01's
stronger paired-tail allowance remains available on its stated domain.

Read with the [result index][results], [arithmetic cluster][arithmetic]
and [avoid index][avoid], especially [classification][a01],
[control matching][controls], [scope][a07] and [signed cancellation][a12].
The existing [prescribed-height two-direction control][two-direction]
already treats collision construction from finitely many source tests;
that construction is not being repeated here.

## 2. The unchanged tail and its reflection relation to the head

Use the normalization of Notes 01–04:
\[
 \lambda_n=\pi n^2,\quad
 \phi_n(v)=(2\lambda_n^2e^{9v}-3\lambda_ne^{5v})
                e^{-\lambda_ne^{4v}},\quad
 S_m=\sum_{n=1}^m\phi_n,\quad R_m=\sum_{n>m}\phi_n.
 \tag{1}
\]
The full source Phi=S_m+R_m is even and holomorphic in
|Im v|<pi/8. This is the inherited modular identity, following from
[DLMF 20.7.32][dlmf] in the repository's normalization; neither the
finite head nor its tail is separately even. Write
\[
 D_m(v)=S_m(v)-S_m(-v)
       =-\{R_m(v)-R_m(-v)\}.
 \tag{2}
\]
Equation (2), at every source point in the strip, is the load-bearing
reflection input below. Matching a finite list of endpoints does not
authorize it.

This is exactly the tail from Note 04. In that note's domain it is
\[
 R_m(v)=E_m\phi_m(v)e^{-\Delta(e^{4v}-1)}
                  p_m(e^{4v}-1),
 \tag{3}
\]
with the same canonical positive measure defining p_m. We do not
optimize a different tail law for the head, the derivative, or another
height. For larger disks below, the bound |p_m|<4 need not apply:
its Laplace integral has a smaller domain than the product's analytic
continuation. We use the full series (1) to bound that continuation.
The negative lower-order monomial is retained throughout.

Choose 0<d<R<pi/8, k=m+1 and
\[
 \alpha_R=e^{-4R}\cos(4R)>0,\qquad
 q_R=\left(\frac{k+1}{k}\right)^4
                      e^{-\alpha_R\pi(2k+1)}.
 \tag{4}
\]
When q_R<1, define the explicit complete-tail bound
\[
 B_m(R)=
 \frac{2(2\lambda_k^2e^{9R}+3\lambda_ke^{5R})
                         e^{-\alpha_R\lambda_k}}{1-q_R}.
 \tag{5}
\]
Then
\[
 \boxed{\sup_{|v|\le R}|D_m(v)|\le B_m(R).}
 \tag{6}
\]
Indeed Re(e^(4v))>=alpha_R on that disk, and
\[
 |\phi_n(v)|\le(2\lambda_n^2e^{9R}+3\lambda_ne^{5R})
                        e^{-\alpha_R\lambda_n}.
\]
The successive majorant ratios are at most q_R for n>=k.
Summing the complete tail and using (2) proves (6), including its
factor two. If q_R>=1, retain finitely many extra majorant terms until
the decreasing ratio is below one; no source mode is discarded.
For simplicity the formulas below state q_R<1 as a checkable hypothesis.

## 3. An explicit signed approximant and complete error

For an integer M>=0 put p=2M+1 and
\[
 T_{m,M}(v)=2\sum_{r=0}^{M-1}
                \frac{S_m^{(2r+1)}(0)}{(2r+1)!}v^{2r+1}.
 \tag{7}
\]
The empty polynomial for M=0 is zero. Define
\[
 \begin{aligned}
 C_{m,M}(t,z)
 &=\frac i2\int_0^d e^{-ts^2-zs}T_{m,M}(is)\,ds\\
 &=\sum_{r=0}^{M-1}\frac{(-1)^{r+1}S_m^{(2r+1)}(0)}{(2r+1)!}
                  \int_0^d s^{2r+1}e^{-ts^2-zs}\,ds,\\
 A_{m,M}(t,z)&=H_{S_m}(t,z)-C_{m,M}(t,z).
 \end{aligned}
 \tag{8}
\]
Here H_(S_m) is its entire half-line integral, with every retained
source ray included. Formula (8) uses finitely many exact head
derivatives and complete finite-segment integrals. The heat exponential
is not Taylor-truncated.

Let P_m and C_m be the full paired head transform and its exact
connector from [Note 02, equations (3)–(7)][n02]. Its identities give
\[
 H_{S_m}=P_m+C_m,\qquad
 H-A_{m,M}=P_{R_m}-(C_m-C_{m,M}).
 \tag{9}
\]
Thus the approximant preserves the signed head–tail endpoint relation
before any absolute estimate. In particular the leading subtraction is
C_(m,1)=-S_m'(0) integral_0^d s exp(-t*s^2-z*s) ds. It cancels,
rather than doubles, the -S_m'(0)/x^2 term of the head.

Cauchy's coefficient bound applied to the odd function D_m gives
\[
 |D_m(is)-T_{m,M}(is)|
 \le B_m(R)\frac{(s/R)^p}{1-(s/R)^2}\quad(0\le s\le d).
 \tag{10}
\]
For |t|<=T, Re z=x>=0 and any fixed j>=0, it follows that
\[
 \begin{split}
 |\partial_z^j(C_m-C_{m,M})|&\le F_{m,M,j}(x),\\
 F_{m,M,j}(x)&=
 \frac{B_m(R)e^{Td^2}}{2R^p[1-(d/R)^2]}
                         \int_0^d s^{p+j}e^{-xs}\,ds.
 \end{split}
 \tag{11}
\]
There is no singularity at x=0: the integral is then
d^(p+j+1)/(p+j+1). For x>0 it is bounded by (p+j)!/x^(p+j+1).

For completeness, the inherited complex-time shifted-tail payment is
as follows. Set c_d=cos(4d),
\[
 \begin{gathered}
 b_d=4c_d\lambda_k-9-Y>0,\qquad 8c_d\lambda_k\ge T,\\
 q_d=\left(\frac{k+1}{k}\right)^4e^{-c_d\pi(2k+1)}<1,\\
 K_j=e^{Td^2}
 \frac{(2\lambda_k^2+3\lambda_k)e^{-c_d\lambda_k}}{1-q_d}
 \sum_{a=0}^j\binom ja\frac{d^{j-a}a!}{b_d^{a+1}}.
 \end{gathered}
 \tag{12}
\]
On |Im z|<=Y the complete approximation theorem is
\[
 \boxed{|\partial_z^j(H-A_{m,M})(t,z)|
             \le e^{-dx}K_j+F_{m,M,j}(x).}
 \tag{13}
\]
The proof of (12) uses e^(4u)>=1+4u+8u^2, pays both shifted rays,
all n>=k and all u>=0, and is recorded in Note 02. Equations
(6)–(11) pay the entire remaining vertical segment. All integrals,
series and derivatives converge normally on the stated compact
parameter sets. No acquisition, rounding or cell-propagation error is
included in (13); any implementation must add them.

The same defect supplies the physical first jet. For a real covector
ell=(ell_0,ell_1), the connector part has the stronger joint allowance
\[
 \frac{B_m(R)e^{Td^2}}{2R^p}
 \int_0^d\frac{s^pe^{-xs}|\ell_0-\ell_1s|}{1-(s/R)^2}\,ds.
 \tag{14}
\]
This retains its common sign and parameter dependence. Independent
component bounds in (11) are optional relaxations of (14).

Every derivative is taken with m,M,d,R fixed. Later choosing these
parameters at a height or freezing them on a cell does not add their
derivatives to the physical jet. In particular A_(m,M) itself obeys
the heat equation for fixed parameters, since both terms of (8) do.

## 4. Exact order cost in a declared analytic disk class

First fix m,R,d,T. If p>=c*x with 0<c<=d, maximizing
c*log(s/R)-s on 0<s<=d gives
\[
 F_{m,M,j}(x)\le
 \frac{B_m(R)e^{Td^2}d^{j+1}}{2[1-(d/R)^2](j+1)}
                 e^{-c(1+\log(R/c))x}.
 \tag{15}
\]
For example, take R=pi/12, d=pi/16, c=pi/24 and the least odd
p>=c*x (also p>=1). The rate is
\[
 \frac\pi{24}(1+\log2)
 =d+\frac\pi{48}(2\log2-1)>d.
 \tag{16}
\]
Under the checkable mode-tail hypotheses (4),(12), M~pi*x/48
therefore makes the extra connector allowance exponentially smaller
than e^(-d*x). This is an explicit sufficient schedule.

Its linear order has a precise, limited optimality statement. Consider
the class of all odd functions analytic on a neighborhood of |v|<=R,
bounded there by a common B>0, with their Taylor coefficients through
degree p-2 known. It is a relaxation of the actual theta defect.
For t=0 let U_(p,j)(x) be the supremum of the jth connector Taylor
remainder in that class. Equation (10) is an upper bound, while the
admissible monomial D(v)=B*(v/R)^p supplies the lower bound. Hence
\[
 \frac{B}{2R^p}\int_0^d s^{p+j}e^{-xs}ds
 \le U_{p,j}(x)\le
 \frac{B}{2R^p[1-(d/R)^2]}\int_0^d s^{p+j}e^{-xs}ds.
 \tag{17}
\]
The supremum here permits any revealed lower Taylor data; the lower
example has all those data zero. It is not a lower bound conditional
on theta's particular lower Taylor coefficients.

If p/x tends to c>=0, elementary Laplace maximization gives
\[
 \lim_{x\to\infty}-\frac1x\log U_{p,j}(x)=I_{R,d}(c),\quad
 I_{R,d}(c)=
 \begin{cases}
 0,&c=0,\\
 c(1+\log(R/c)),&0<c\le d,\\
 d+c\log(R/d),&c\ge d.
 \end{cases}
 \tag{18}
\]
For c>0 the upper bound follows by maximizing the exponent, and a
small interval about its maximizer supplies the matching lower
exponential rate. The fixed factor s^j does not change the rate.
For c=0, use any fixed sufficiently small positive source interval
for the lower bound and then let its endpoints tend to zero; the
nonnegative upper rate is immediate. This also covers fixed p.

Consequently p=o(x) cannot guarantee a positive exponential rate from
this disk information alone. The threshold for rate d is the unique
c_* in (0,d) satisfying c_*(1+log(R/c_*))=d. This is a rate threshold
for the specified analytic class, not an optimal sample count for
theta, a lower bound on its actual error, or an obstruction to direct
contour evaluation. The monomial is not asserted to be a theta-tail
defect or a collision source.

## 5. A complete schedule at the gamma-envelope scale

The same explicit estimates can approach the physical strip boundary.
Let r_0=pi/8 and fix 0<a<b and kappa>0. For sufficiently large x set
\[
 R=r_0-a\frac{\log x}{x},\quad
 d=r_0-b\frac{\log x}{x},\quad
 k=\lceil\sqrt{\kappa x}\rceil,\quad m=k-1,
 \tag{19}
\]
and take the least odd p>=R*x, with M=(p-1)/2. These choices are
made for evaluating the frozen-parameter errors (13).
All admissibility conditions in (4),(12) hold eventually. In fact
\[
 \begin{aligned}
 \alpha_R&\sim4e^{-\pi/2}a\frac{\log x}{x},\\
 1-q_R&\sim8\pi e^{-\pi/2}a\sqrt\kappa
                              \frac{\log x}{\sqrt x},\\
 B_m(R)&=O\!\left(
 \frac{x^{5/2-4\pi e^{-\pi/2}a\kappa}}{\log x}\right).
 \end{aligned}
 \tag{20}
\]
The ceiling in k changes alpha_R*pi*k^2 only by o(1).
For p+j+1>d*x, the elementary inequality
1-s/d<=-log(s/d) gives
\[
 \int_0^d s^{p+j}e^{-xs}ds
 \le\frac{d^{p+j+1}e^{-dx}}{p+j+1-dx}.
 \tag{21}
\]
Since p>=R*x and log(d/R)<=d/R-1,
(d/R)^p exp(-d*x)<=exp(-R*x). Moreover
1-(d/R)^2 is asymptotic to 2(b-a)log(x)/(r_0*x), and
p+j+1-d*x is asymptotic to (b-a)log(x). Substitution in (11) yields
\[
 F_{m,M,j}(x)=O\!\left(e^{-\pi x/8}
 \frac{x^{7/2+a(1-4\pi e^{-\pi/2}\kappa)}}{(\log x)^3}\right).
 \tag{22}
\]
For every fixed j and bounded T,Y, the same calculation for (12)
is the inherited shifted-tail asymptotic
\[
 e^{-dx}K_j=O\!\left(e^{-\pi x/8}
 \frac{x^{5/2+b(1-4\pi\kappa)}}{(\log x)^2}\right).
 \tag{23}
\]
The factor exp(T*d^2) is bounded and does not change either exponent.

It follows, for example whenever
\[
 \frac74+a(1-4\pi e^{-\pi/2}\kappa)<0,\qquad
 \frac34+b(1-4\pi\kappa)<0,
 \tag{24}
\]
that the complete allowance (13), divided by
G_0(x)=x^(7/4)exp(-pi*x/8), tends to zero. Equality in either
condition also suffices because of the logarithmic denominators.
One entirely analytic choice is a=4, b=8, kappa=2. Indeed
3<pi<4 and e^2<9 imply 8*pi*exp(-pi/2)>8/3, making the first
exponent less than -59/12; the second is less than -733/4.

This schedule uses m=O(sqrt(x)) and M~pi*x/16. It supplies a uniform
asymptotic for the complex-time and bounded-imaginary-height domains
already stated, with each fixed derivative order. An explicit onset
is not claimed; formulas (4)–(13) remain the finite-parameter tests.
No lower bound for G_0/|H|, evaluation precision or runtime follows.

## 6. Accuracy of the finite reflection data

Write a_r=S_m^(2r+1)(0)/(2r+1)!. If the coefficient used in (8)
has absolute error at most epsilon_r, its jth derivative adds at most
\[
 e^{Td^2}\sum_{r=0}^{M-1}\epsilon_r
                 \int_0^d s^{2r+1+j}e^{-xs}ds
 \le e^{Td^2}\sum_{r=0}^{M-1}
           \epsilon_r\frac{(2r+1+j)!}{x^{2r+2+j}}
 \quad(x>0).
 \tag{25}
\]
Use the finite integral at x=0. In particular a fixed uncertainty in
the first coefficient creates a worst-case inverse-square payment
for the value, even if M grows. Controlling that individual payment
by C*exp(-d*x) requires its allowance to be O(x^2*exp(-d*x)).
This is a robustness statement about an independently bounded error;
correlated errors can cancel and are not assigned that lower bound.

Thus increasing the endpoint count without also paying their accuracy
does not restore exponential control. The signed finite sum in (8)
may be badly conditioned; this note does not assert a stable algorithm.

## 7. Controls, comparison and disposition

The following is analytic premise screening using the registered
controls and their inherited review status, not a fresh numerical replay.

| Control | Relation to the theorem |
| --- | --- |
| Finite-prime or finite weighted-square controls matching the first M endpoints | They can reproduce the finite endpoint tests, and their own tails can have positive Laplace laws. They fail the full relation (2) and unchanged complete coefficients. For a general source A, the identity acquires its full connector C_A; a finite endpoint match does not set it to zero. |
| Euler-factor translated sources | Full even reflection can hold, so the connector algebra applies. The canonical square tail (1) and its constant (5) do not transfer. Their own paid approximation could still be valid at a collision. |
| Reflected super-Gaussian control | Full reflection and contour shifting hold at its exact double event. It lacks the canonical square-tail law. Exponential approximation of a field is compatible with a double zero. |
| Smooth-shape and positive-primitive controls | Real reflection alone does not supply the stated complex disk and complete canonical bounds. No extra complex continuation is assumed. |
| Polynomial, atomic, compact-profile, smooth-density and two-channel controls | They do not supply the analytic source with the unchanged square expansion and this connector-tail payment. |
| Close positive-source endpoint controls | They fail unchanged ordinary Dirichlet/square arithmetic. Their fixed-tolerance limitation is consistent with (25). |

For a noncanonical analytic source A=S_m+R, the exact replacement
for (9) is
\[
 H_A-A_{m,M}=P_R-(C_m-C_{m,M})+C_A.
 \tag{26}
\]
The term C_A and the replacement for (6) are genuine obligations.
A fixed finite-prime control can have an algebraically small connector
after its matched endpoints; it need not obey (13). This is where
complete reflection enters the estimate, beyond a formal representation.
Conversely the theorem is an upper error estimate, so it is not
supposed to reject every colliding source that has its own version.

For the same canonical head and contour, A_(m,M)-P_m=C_m-C_(m,M).
The direct P_m comparator pays K_j exp(-d*x) and no Taylor term.
Whenever [S01][s01] supplies a better complete P_(R_m) allowance,
it can replace that term on both sides, leaving the additional
nonnegative finite-connector payment unchanged. There is no demonstrated
advantage over S01 or the direct retained evaluator.

**Disposition.** The finite-reflection stability task is complete in its
declared norms: it has an explicit complete bound, a sharp class-level
rate, a gamma-scale schedule and an accuracy payment. It is useful
analytic control of the head–tail cancellation. It does not supply the
still-missing signed retained-core inequality or a BW-11–13 nonvanishing
margin. HMC-05 remains open and HMC-06 remains gated.

The next sign task should work with the exact shifted head P_m and the
same tail law, rather than recomputing this connector hierarchy. At a
putative double event it must estimate the signed interaction in
(P_m,P_(m,x))=-(P_(R_m),P_(R_m,x)), using unchanged height-dependent
arithmetic and conditioning on both equations. A further tail allowance
alone will not accomplish that. A useful next result would be a bound
on a higher-jet signed combination under those two matching conditions;
no such bound or numerical sign pilot is asserted here.

[n02]: 02_FULL_REFLECTION_ADJOINT_AND_CONNECTOR_AUDIT_20261021.md
[n04]: 04_CANONICAL_TAIL_LAPLACE_CONSTRAINT_AND_COUPLED_ENCLOSURE_20261021.md
[review]: ../reviews/05_FINITE_REFLECTION_STABILITY_SELF_REVIEW_20261021.md
[results]: ../../../../../../../result-summaries/README.md
[arithmetic]: ../../../../../../../result-summaries/14_theta_identities_and_arithmetic_bookkeeping.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a12]: ../../../../../../../avoid/12_term_by_term_matching_and_separate_bounds.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[two-direction]: ../../../../../07_source_measurement_audit/notes/round-1/01_OPENING_ANALYTIC_AUDIT_AND_REPLAY_CONTRACT_CODEX_20261016.md
[s01]: ../../../../../11_arithmetic_collision_rigidity/symmetries/01_modular_self_duality/notes/01_PAIRED_ENDPOINT_REMAINDER_AND_BOUNDED_COMPARISON_20261018.md
[dlmf]: https://dlmf.nist.gov/20.7.E32
