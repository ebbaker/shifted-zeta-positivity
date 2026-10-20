# Local correlation tests and finite Jensen margins

20 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance, **gpt-6-astra (Codex), reasoning effort ultra**,
verified from this turn's recorded metadata. Separate same-model derivations
and [internal review][review]; no specialist review or priority claim.

**Outcome:** a localized nonnegative quadratic certificate is dominated by
its matched linear zero-counting test at the same bandwidth. For the unchanged
theta coefficients, a multiplicity-m limiting zero produces simple Jensen
roots separated at scale `d^(-1/2)`, with Laguerre margin of order `d^(1-m)`.
These are precise comparisons and approximation costs. No signed arithmetic
bound excluding an original multiple zero has been obtained.

The [program][program], [result index][results], [collision catalogue][controls]
and [avoid index][avoid] apply, especially [equivalent targets][a01],
[control premises][a02], [scoped conclusions][a07] and [gain before expansion][a20].
[Note 06][n6] supplies the full-window comparison; this note treats localized
observations and the exact theta Jensen family. The [BW09 manuscript][bw09]
retains its root-wall baseline and unmet strict-surplus requirement.

## 1. A compact observation window, retaining every zero

Assume RH. Let the distinct zero ordinates be `lambda`, with arbitrary
integer multiplicities `m_lambda`, and fix an actual zero ordinate `gamma`
of multiplicity `m>=1`. Use

\[
 K_\Delta(x)=\left(\frac{\sin\pi\Delta x}{\pi\Delta x}\right)^2,
 \qquad k_\lambda(t)=K_\Delta(t-\lambda),\qquad
 S(t)=\sum_\lambda m_\lambda k_\lambda(t).
 \tag{L1}
\]

Let `nu` be any finite nonnegative compactly supported observation measure.
This includes a usual weighted interval and any finite collection of
observations with nonnegative weights. Write `inner(f,g)=integral f g dnu`,
and assume `c=inner(k_gamma,k_gamma)>0`. Define

\[
 h_\gamma(\lambda)=\frac{\langle k_\gamma,k_\lambda\rangle}{c},
 \quad L_\gamma=\frac{\langle S,k_\gamma\rangle}{c}
              =\sum_\lambda m_\lambda h_\gamma(\lambda),
\]
\[
 C=\frac{\|S\|_\nu^2}{c},\qquad
 D=\frac1c\sum_\lambda m_\lambda\|k_\lambda\|_\nu^2,
 \qquad E=C-D.                                         \tag{L2}
\]

All sums converge. On the compact support of `nu`, the tail of `k_lambda`
is uniformly `O_Delta(lambda^(-2))`; the zero product gives
`sum m_lambda/lambda^2<infinity`. Thus `S` converges uniformly and is
bounded there. The diagonal series has a uniformly summable
`O_Delta(lambda^(-4))` tail. Nonnegativity and Tonelli justify every
quadratic expansion. No exterior root or cross term has been deleted.

The kernel `h_gamma` is nonnegative on the real axis and has value one
at `gamma`, so `m<=L_gamma`. More precisely,

\[
                    \boxed{E\ge2(L_\gamma-1).}          \tag{L3}
\]

To see this, put `b=sum_(lambda!=gamma) m_lambda h_gamma(lambda)>=0`.
Expanding (L2), isolate the central contributions:

\[
 E=m(m-1)+2mb+E_{\rm other},\qquad L_\gamma=m+b,
\]

where `E_other` consists of the other diagonal defects and unordered
cross products; each is nonnegative. Hence

\[
 E-2(L_\gamma-1)
 =(m-1)(m-2)+2(m-1)b+E_{\rm other}\ge0.                 \tag{L4}
\]

The integer multiplicity assumption is used exactly in
`(m-1)(m-2)>=0` for `m>=1`. In particular,

\[
 E\le2-\eta\quad\Longrightarrow\quad
 L_\gamma\le2-\eta/2\qquad(\eta>0).                   \tag{L5}
\]

Thus the declared quadratic exclusion always supplies a linear one-point
exclusion using its matched kernel. Any benefit over the original Fejér
kernel is already a benefit of this different nonnegative linear kernel;
it is not an additional consequence of squaring the observations.

## 2. Arithmetic bandwidth and absolute errors

In Note 02's Fourier convention, direct convolution gives

\[
 \widehat h_\gamma(v)=
 \frac{(1-|v|/\Delta)_+}{\Delta c}
       \int k_\gamma(t)e^{-2\pi i vt}\,d\nu(t).         \tag{L6}
\]

Thus `h_gamma` has bandwidth `Delta`, despite the arbitrary compact
observation weight. It is entire, decays quadratically on each fixed
horizontal strip, and is admissible in the same Guinand–Weil formula.
Its exact full-zero mass is

\[
 \begin{aligned}
 L_\gamma={}&h_\gamma(i/2)+h_\gamma(-i/2)\\
 &+\frac1{2\pi}\int_{\mathbb R}h_\gamma(u)
                [\Re\psi(1/4+iu/2)-\log\pi]\,du\\
 &-\frac1\pi\sum_{n\le e^{2\pi\Delta}}
             \frac{\Lambda(n)}{\sqrt n}
             \Re\widehat h_\gamma(\log n/(2\pi)).
 \end{aligned}                                         \tag{L7}
\]

Both pole terms, the gamma term, signed coefficients, and every exterior
zero are retained. No ordinary Euler series is used in the critical strip.

By contrast the diagonal in (L2) is the full-zero sum for

\[
 d(\lambda)=c^{-1}\int K_\Delta(t-\lambda)^2\,d\nu(t),
 \qquad
 \widehat d(v)=c^{-1}\widehat{K_\Delta^2}(v)
                       \int e^{-2\pi i vt}\,d\nu(t).   \tag{L8}
\]

Its Fourier support is contained in `[-2Delta,2Delta]`. A direct exact
explicit-formula payment can therefore reach primes `n<=exp(4 pi Delta)`,
the square of (L7)'s horizon. Special cancellation or a separate lower
bound for `D` could avoid that payment; it must be proved. The signed
prime-pair expansion of `C` does not itself supply the diagonal subtraction.

There are two precise error comparisons. First, if a computation proves
`C<=C_hat+eps_C` and `D>=D_hat-eps_D`, then (L3) transfers the complete
bound, without new zero data, to

\[
 L_\gamma\le1+\tfrac12(C_{\rm hat}-D_{\rm hat}
                                      +\epsilon_C+\epsilon_D).   \tag{L9}
\]

The errors must be smaller than the actual strict slack, not merely
smaller than a nominal two-unit threshold. Second, for the distinct norm
consumer, suppose a real-valued approximation `S_hat` satisfies
`||S-S_hat||_nu<=eps`. Then

\[
 m\le L_\gamma\le
 U_{\rm lin}:=\frac{\langle\widehat S,k_\gamma\rangle}{c}
                         +\frac\epsilon{\sqrt c}
 \le \frac{\|\widehat S\|_\nu+\epsilon}{\sqrt c}
 =:U_{\rm norm}.                                      \tag{L10}
\]

The last inequality is Cauchy–Schwarz. The same weighted-L2 residual ball
therefore makes the matched linear upper bound no worse than the norm
upper bound. These are exact information comparisons; they do not assert
that every independently implemented arithmetic estimate of (L7) will have
less computation or a smaller numerical error. The normalization `c` is
explicit, and any uncertainty in it must also be propagated.

## 3. The untruncated matched kernel is larger than the original Fejér kernel

For a finite zero projection `I`, take Lebesgue observation measure on the
whole line. Then `c=2/(3 Delta)` and the matched kernel is Note 06's
autocorrelation `R(2 pi Delta(lambda-gamma))`. For every real `z`,

\[
 R(z)=\frac{6(z-\sin z)}{z^3}
 \ge\frac{2(1-\cos z)}{z^2},                           \tag{L11}
\]

with equality only at `z=0` after removable extension. Indeed their
difference is `2[z(2+cos z)-3 sin z]/z^3`. For `0<z<=3<pi`, the
bracket has derivative
`2 sin(z/2)[2 sin(z/2)-z cos(z/2)]>0`, since `tan u>u` for `0<u<pi/2`.
For `z>=3`, the bracket is at least `z-3`, with strictness at `z=3`
from the first case. Evenness completes the proof.

Consequently, at each actual zero in that same finite projection,

\[
 \boxed{S_{I,\Delta}(\gamma)
       \le L_{I,R}(\gamma)
       \le1+\mathcal E_{I,\Delta}/2.}                 \tag{L12}
\]

The full-window quadratic excess can therefore never pass its threshold
when the direct Fejér mass on the same projected zero data fails.
This comparison concerns `S_I`, not the full arithmetic `S`. Replacing it
by full `S` requires the same independently paid exterior contribution;
`S>=S_I` is the wrong direction for omitting that cost. Section 1's compact
window formulation already includes every zero and avoids this projection.

For arbitrary compact windows, (L11) must not be asserted for the matched
kernel. A concrete paired-observation example makes the distinction clear.
Put equal observation masses at `gamma +/- a`, `a=3/(2 Delta)`. The
matched kernel at `gamma+v` is
`[K_Delta(a-v)+K_Delta(a+v)]/[2K_Delta(a)]`. Its second derivative at
zero is `-2 pi^2 Delta^2+(8/3)Delta^2`, strictly less than
`K_Delta''(0)=-(2/3)pi^2 Delta^2`. It is therefore smaller than the
original Fejér kernel for sufficiently small nonzero `v`. This permits
linear-kernel optimization; it does not create a quadratic advantage,
because (L3) still holds with the exact matched kernel.

## 4. Signed observation forms and the contour obligation

A positive-semidefinite matrix on finitely many observations need not have
nonnegative cross inner products between different root profiles. Then
`E_other>=0` and `b>=0` used above can both fail. For example take the two
observation points `gamma,lambda`, let `q=K_Delta(gamma-lambda)<1`, and
choose a real vector `v` with
`v dot (1,q)=1`, `v dot (q,1)=-r`, `r>0`. The rank-one matrix `vv^T`
is positive semidefinite. For a central double and the other simple root,
its normalized diagonal-subtracted form is
`(2-r)^2-(2+r^2)=2-4r<2`. Thus PSD alone does not make that signed excess
a valid multiplicity certificate. This is a finite algebraic check of the
discarded cross term, not a zeta-arithmetic or positive-source control.
Actual noncentral signed contributions must be estimated and retained.

The root-wall identity cancels the tangential phase exactly, and under RH
retains the baseline `(m-1)pi`; it provides no sign for these missing
correlated terms. Event conditions identify the central integer `m`,
already fully used in (L4), but impose no further estimate here on the
unchanged signed prime data. No strict cap surplus or original multiple-zero
exclusion follows. The useful result is the exact local comparison
(L3), its bandwidth/error bookkeeping, and the scoped disposition of this
quadratic-consumer class.

## 5. Keep the coefficient normalization and the limiting parameter fixed

Use the existing entire squared-variable function

\[
 f(z)=\xi(1/2+\sqrt z)=\sum_{k\ge0}b_kz^k,
 \qquad b_k=\frac{\gamma_k}{k!}
 =\frac{8\,4^k}{(2k)!}\int_0^\infty u^{2k}\Phi(u)du>0. \tag{J1}
\]

The square-root notation means its single-valued entire power series. A zero of xi at `1/2+i gamma`, gamma>0, corresponds to a zero `r=-gamma^2` of f with the same multiplicity. Define

\[
 J_d(X)=\sum_{k=0}^d\binom dk\gamma_kX^k,
 \qquad P_d(z)=J_d(z/d)
      =\sum_{k\ge0}q_{d,k}b_kz^k,
\]
\[
 q_{d,k}=(d)_k/d^k\quad(k\le d),\qquad q_{d,k}=0\quad(k>d). \tag{J2}
\]

Under RH, f has a genus-zero product with infinitely many negative zeros, counted with multiplicity. The [existing strict-Jensen proof][inv22] proves that every J_d has d distinct negative roots by factoring off d positive operators `1+aD` from that product. Its argument expressly permits repeated factors of f. Hence strict Jensen hyperbolicity is already a consequence of RH **without** simple zeta zeros.

The missing question is a quantitative margin that survives `d->infinity`. The following calculation uses the actual moments (J1), not modified coefficients.

## 6. An explicit compact error bound from the positive theta moments

Let `theta=R d/dR` and
`B_4(R)=R^4 f^(4)(R)+4R^3 f'''(R)+2R^2 f''(R)`.
For every d>=1 and R>0,

\[
 \boxed{\sup_{|z|\le R}
 \left|P_d(z)-f(z)+\frac{z^2}{2d}f''(z)\right|
 \le\frac{B_4(R)}{8d^2}.}                              \tag{J3}
\]

Indeed for k<=d put `A=k(k-1)/(2d)`. Expansion of the product in (J2) gives
`0<=q_(d,k)-1+A<=A^2/2`; the upper bound follows, for example, from the second-order Taylor remainder of `product_(j=0)^(k-1)(1-t j/d)` on 0<=t<=1. For k>d,
`|q_(d,k)-1+A|=A-1<=A^2/2`, since A>=1.
Thus the bound `k^2(k-1)^2/(8d^2)` applies for every k. Sum against the positive coefficients `b_k R^k`; `sum k(k-1)b_kz^k=z^2 f''(z)` and `sum k^2(k-1)^2b_kR^k=B_4(R)`.

For derivatives of orders j=1,2, the same coefficient proof gives

\[
 \sup_{|z|\le R}|\partial_z^j(P_d-f+z^2f''/(2d))|
 \le\frac{B_4^{(j)}(R)}{8d^2}.                         \tag{J4}
\]

All constants are finite complete-source moments. These are useful approximation bounds, but they are upper error estimates; they supply no positive lower bound for the limiting first jet at a zero.

For a hypothetical exact double zero r, (J3)–(J4) immediately give

\[
 P_d(r)=-\frac{r^2f''(r)}{2d}+O_r(d^{-2}),
 \qquad P_d'(r)=O_r(d^{-1}),\quad P_d''(r)=f''(r)+O_r(d^{-1}),
\]
\[
 \boxed{(P_d'(r))^2-P_d(r)P_d''(r)
       =\frac{r^2f''(r)^2}{2d}+O_r(d^{-2})>0.}         \tag{J5}
\]

The strict finite Laguerre sign therefore occurs on the double hypothesis itself, with a margin tending to zero at rate 1/d. The two nearby Jensen roots satisfy

\[
                    r\pm\frac{|r|}{\sqrt d}+O_r(d^{-1}),\tag{J6}
\]

so their separation is `2|r|/sqrt(d)+O_r(d^-1)`. Formula (J6) follows either directly by rescaling (J3) around r or as the m=2 case below.

## 7. Every multiplicity has a local Hermite cluster, with a complete error argument

Let f have a real zero r!=0 of exact multiplicity m, and set
`c_m=f^(m)(r)/m!`. This part only needs an entire real f; positivity is used to express its error norm by f(R) in our theta case. Let the probabilists' Hermite polynomial be

\[
 \operatorname{He}_m(y)=m!\sum_{j=0}^{\lfloor m/2\rfloor}
                \frac{(-1)^j y^{m-2j}}{2^j j!(m-2j)!}.
\]

Then locally uniformly for complex y,

\[
 \boxed{\frac{d^{m/2}}{c_mr^m}
          P_d(r+r y/\sqrt d)
       =\operatorname{He}_m(y)+O_{f,r,m}(d^{-1/2}).}    \tag{J7}
\]

The statement includes corresponding derivatives on compact y-disks by Cauchy's estimate. Here is a finite expansion proof with a controlled remainder.

For j>=0 define the polynomial `E_j(k)=e_j(0,1,...,k-1)` on nonnegative integers, with E_0=1. The recurrence
`E_j(k+1)-E_j(k)=k E_(j-1)(k)` shows that E_j is a polynomial of degree 2j with leading coefficient `1/(2^j j!)`. For every fixed integer J>=0,

\[
 P_d(z)=\sum_{j=0}^J\frac{(-1)^j}{d^j}E_j(z\partial_z)f(z)
          +\mathcal R_{d,J}(z),
 \qquad
 \sup_{|z|\le R}|\mathcal R_{d,J}(z)|
 \le\frac{2\,\theta^{2J+2}f(R)}{d^{J+1}}.              \tag{J8}
\]

For k<=d, the Taylor remainder of `product(1-t l/d)` is bounded by
`e_(J+1)(0,...,k-1)/d^(J+1)<=k^(2J+2)/[2^(J+1)(J+1)!d^(J+1)]`.
For k>d, q_(d,k)=0 and the absolute sum of the first J+1 terms is at most
`sum_(j=0)^J k^(2j)/(2^j j! d^j)`.
Each summand is bounded by `k^(2J+2)/d^(J+1)` times `1/(2^j j!)`, since k^2>d. Their constants sum to at most sqrt(e)<2. This proves (J8) after summing the positive theta coefficients; for a general entire f replace them by their absolute values.

In `E_j(z partial_z)`, the highest derivative term is
`z^(2j) f^(2j)/(2^j j!)`; all others have derivative order at most 2j-1. Take J=floor(m/2), put `z=r+r y/sqrt(d)`, and use the order-m Taylor zero of f. The highest terms all have order d^(-m/2) and sum to the displayed Hermite polynomial. Every lower-derivative term and the remainder in (J8) is `O(d^(-(m+1)/2))`. This proves (J7), including odd m.

The roots h_1<...<h_m of He_m are simple and real. Rouché's theorem on disjoint small disks around them, followed by conjugation, therefore gives **m distinct real** roots of P_d near r for large d:

\[
                r+\frac{r h_j}{\sqrt d}+O_{f,r,m}(d^{-1}),
                \qquad1\le j\le m.                    \tag{J9}
\]

Each disk contains one root counted with multiplicity, which proves its simplicity. The signs of r reverse their ordering when r<0. Their minimum local separation is
`|r|min_j(h_(j+1)-h_j)/sqrt(d)+O(d^-1)` for m>=2.

There is also an explicit positive Laguerre-margin rate. Write
`L_1(p;x)=p'(x)^2-p(x)p''(x)` and

\[
 A_m=\operatorname{He}_m'(0)^2
             -\operatorname{He}_m(0)\operatorname{He}_m''(0)>0.
\]

The Hermite differential equation gives
`A_m=m[(m-1)!!]^2` for even m and
`A_m=m^2[(m-2)!!]^2` for odd m (with `(-1)!!=1`).
From (J7) and its first two derivatives,

\[
 \boxed{L_1(P_d;r)=c_m^2r^{2m-2}d^{1-m}
                   [A_m+O_{f,r,m}(d^{-1/2})].}         \tag{J10}
\]

For m=2, the sharper first-order expansion (J3) gives (J5)'s smaller error. All multiplicity classes are retained. Neither (J7) nor (J10) is an RH-equivalent criterion: they describe what Jensen approximation itself does if a multiple zero exists.

## 8. What the imported moment results do and do not address

The two limiting parameters must not be confused. [Griffin–Ono–Rolen–Zagier, Theorems1 and3](https://arxiv.org/pdf/1902.07321) prove eventual hyperbolicity as the **coefficient shift** n tends to infinity with degree d fixed, via a Hermite limit. The effective follow-up [Griffin et al., Theorem1.1](https://arxiv.org/pdf/1910.01227) gives hyperbolicity for n>=c exp(d/2). This is not the unshifted large-degree limit (J2) used to recover a fixed zero of f.

The normalizations have been checked: GORZ equation(1) expands
`(4w^2-1)Lambda(1/2+w)=8xi(1/2+w)`, so its gamma(n) is eight times
our gamma_n. Its Jensen roots and normalized Turán ratios are unchanged.
The effective follow-up's equation(1.1) expands xi itself and agrees
exactly with our gamma_n.

The latter paper's Theorem2.1 also quantifies the actual coefficients' Turán slack:
with `Delta(M)^2=(1/2)(1-gamma_(M-2)gamma_M/gamma_(M-1)^2)`, it proves
`Delta(M)~1/sqrt(2M)`.
Thus the normalized adjacent-coefficient Turán margin itself tends to zero like 1/M. These are useful exact-theta asymptotics; they do not give a lower bound for `L_1(f;r)` at every negative zero. No simplicity assumption is smuggled into either cited theorem.

For comparison, under RH the genus-zero product gives, away from its zeros,

\[
 L_1(f;x)=f(x)^2\sum_j\frac{m_j}{(x-r_j)^2}>0.
\]

At a zero it equals f'(x)^2. Thus a claimed strictly positive all-real limiting Laguerre inequality would already assert simplicity; plain nonnegativity does not. This is the distinction recorded in [Csordas, §4](https://arxiv.org/pdf/1309.0055), especially Remark4.8. The source/moment Turán inequalities and finite Jensen strictness must not be substituted for that missing limiting estimate.

The physical theta heat regularization has the same type of loss: at an exact double event, `H(t,a)=-t h_2+O(t^2)`, `H_x(t,a)=O(t)`, and `H_xx(t,a)=h_2+O(t)`, so its strict positive-time Laguerre margin is `t h_2^2+O(t^2)`. This is already part of the local heat framework. Jensen degree and physical heat time are different parameters; (J3) identifies only the local effective scale `r^2/(2d)` in the squared-variable approximation.

**Disposition.** The new quantified information is (J3)–(J10): finite Jensen strictness at a putative multiple theta zero survives with root spacing d^(-1/2) and margin d^(1-m), then collapses at the endpoint. The existing RH strictness theorem therefore cannot be upgraded by continuity alone. The exact theta moments have supplied approximation-error constants but no signed estimate or uniform lower margin beating this cost. That narrower attempt stops here; no further coefficient-shift scan, auxiliary heat criterion, or source control is proposed.


[review]: ../reviews/07_LOCAL_CORRELATION_AND_JENSEN_MARGIN_REVIEW_20261020.md
[program]: ../research-overview/01_RH_TO_SIMPLICITY_PROGRAM_20261020.md
[n6]: 06_SIGNED_CORRELATION_RESOLUTION_AND_MOBIUS_ENERGY_20261020.md
[bw09]: ../../09_expanding_contour_later_collision/manuscript/main.tex
[results]: ../../../../../../../result-summaries/README.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
[avoid]: ../../../../../../../avoid/README.md
[a01]: ../../../../../../../avoid/01_restating_the_target.md
[a02]: ../../../../../../../avoid/02_shape_only_arguments_and_the_controls.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[a20]: ../../../../../../../avoid/20_volume_without_a_gain.md
[inv22]: ../../../../../../../papers/investigations-2/active/22_theta_manifold_geometry/notes/01_physical_jet_geometry/05_JENSEN_HYPERELLIPTIC_TOPOLOGY_20261015.md
