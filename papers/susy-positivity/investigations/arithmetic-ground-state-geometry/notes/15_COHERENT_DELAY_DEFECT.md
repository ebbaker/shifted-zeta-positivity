# Coherent delay defects: an exact signed-pole control and its contact cost

13 September 2026. This note couples the calibrated quartic cap of
[note 10](10_REFLECTED_BOUNDARY_PAIRING.md) coherently to the closed
massive residual source of [note 11](11_CLOSED_ARITHMETIC_SOURCE.md).
One two-component defect produces **both signed pole terms exactly**
after finite-interval compression. Its positive gluing necessarily adds
a positive contact. A second calculation produces an exact prime atom,
with a contact cost and a shifted massive kernel.

For the larger class of bounded raw translation injections with a finite
delay alphabet, preserving the gamma continuous kernel and the specified
pole kernel forces the contact contribution to be nonnegative. This
includes square-summably many massive channels and arbitrary fixed cap
vectors. It rejects this concrete coupling class, not coherent sources,
bounded perturbations in general, or interacting physical theories.

The construction below specifies a positive auxiliary Hilbert model and
its adjoint before matching coefficients. The matching does not derive
the defect amplitude or the delay from an independent arithmetic law.
No full Weil norm identity is claimed.

## 1. A normalized cap and a bounded coherent perturbation

At the homogeneous quartic endpoint, put

\[
f_0=(Z^4+W^4+Z^2W^2)/16,\qquad s_0=Z^2+W^2,
\qquad \lambda=256\pi^2/3.
\]

The actual cutoff-and-heat cap construction in note 10 gives the
normalized physical vacuum

\[
\chi=\lambda^{-1/2}h_{f_0}(s_0),\qquad \|\chi\|=1.
\tag{1}
\]

This normalization is evaluated; it is not a choice from an unknown
source Gram matrix. Tensor the residual output space with the quartic
physical Hilbert space and use the isometric source
\(\mathcal A^\chi F=\mathcal AF\otimes\chi\). In a mode with
\(a=2k+1/2\), abbreviate

\[
\alpha=\sqrt{2/a},\quad R_a=(a^2-\partial_x^2)^{-1},\quad
(\mathcal A^\chi F)_k=
\alpha\begin{pmatrix}(I-a^2R_a)F\\a\partial_xR_aF\end{pmatrix}
\otimes\chi.
\tag{2}
\]

The two components use an ordinary positive Euclidean norm. Their
constant orthogonal rotations below are unitary rotations of these
residual channels. A new geometric interpretation as physical fermions
is not required for their Hilbert adjoints and has not been derived.

For any explicitly specified bounded map \(\mathcal B\) from whole-line
\(L^2\) to this output, define

\[
\mathcal S_L=(\mathcal A^\chi+\mathcal B)E_L,
\qquad \operatorname{Dom}\mathcal S_L=\mathcal D_{\log,L}.
\tag{3}
\]

Bounded perturbation of the closed source proves that (3) is closed,
has the same graph topology and compactly supported smooth core, and
has the exact maximal adjoint

\[
\mathcal S_L^*=(\mathcal A_L^\chi)^*+E_L^*\mathcal B^*,
\qquad \operatorname{Dom}\mathcal S_L^*
=\operatorname{Dom}(\mathcal A_L^\chi)^*.
\tag{4}
\]

In particular the interval distributional-adjoint qualification of
note 11 is retained. The positive block Hamiltonian obtained from the
closed self-adjoint supercharge
\(\left(\begin{smallmatrix}0&\mathcal S_L^*\\
\mathcal S_L&0\end{smallmatrix}\right)\) has source-sector block
\(\mathcal S_L^*\mathcal S_L\). Its positivity is an ordinary Hilbert
norm statement. It does not assume positivity of a prescribed
arithmetic operator.

## 2. A remote two-channel defect produces the signed poles

Let \(U_dF(x)=F(x-d)\). Fix a mode \(a\), a distance \(D>0\), and a
real coupling \(t\). Specify the defect in that mode by

\[
\boxed{\quad
(\mathcal B_{D,t}F)_k
=-t\begin{pmatrix}(U_D+U_{-D})F\\ (U_D-U_{-D})F\end{pmatrix}
\otimes\chi,
\qquad (\mathcal B_{D,t}F)_j=0\ (j\ne k).
\quad}
\tag{5}
\]

Equivalently its two translated inputs occupy the orthogonal vectors
\((1,1)/\sqrt2\) and \((1,-1)/\sqrt2\). Direct use of
\(U_d^*=U_{-d}\) gives

\[
\mathcal B_{D,t}^*\mathcal B_{D,t}=4t^2I.
\tag{6}
\]

The unwanted delays \(\pm2D\) cancel between the two output components.
If \((g_j,h_j)_j\) denotes the output after contraction with \(\chi\),
the defect adjoint is explicitly

\[
\mathcal B_{D,t}^*(g,h)
=-t(U_D+U_{-D})g_k+t(U_D-U_{-D})h_k.
\tag{7}
\]

Write \(V_D=U_D+U_{-D}\) and \(J_D=U_D-U_{-D}\). The real cross term
is the bounded self-adjoint operator

\[
\begin{aligned}
\mathcal C_{a,D,t}
&=(\mathcal A^\chi)^*\mathcal B_{D,t}
  +\mathcal B_{D,t}^*\mathcal A^\chi\\
&=-2\alpha tV_D+2\alpha t a^2R_aV_D
  +2\alpha at\partial_xR_aJ_D.
\end{aligned}
\tag{8}
\]

Only the bounded mode (2) participates in this cross term, so (8)
has no infinite-adjoint domain ambiguity. Its Fourier multiplier is

\[
-4\alpha t\,
\frac{\tau^2\cos(D\tau)-a\tau\sin(D\tau)}{a^2+\tau^2}.
\tag{9}
\]

The massive Green function and its derivative are

\[
r_a(x)=\frac{e^{-a|x|}}{2a},\qquad
r_a'(x)=-\frac12\operatorname{sgn}(x)e^{-a|x|}.
\tag{10}
\]

Suppose now \(D\geq L\). For inputs supported in \(I_L\), the atomic
term \(E_L^*V_DE_L\) vanishes. At every difference \(|z|<L\),

\[
(R_aV_D)(z)=a^{-1}e^{-aD}\cosh(az),\qquad
(\partial_xR_aJ_D)(z)=e^{-aD}\cosh(az).
\]

Thus the **whole** compressed cross kernel is

\[
\boxed{\quad
\bigl(E_L^*\mathcal C_{a,D,t}E_L\bigr)(x,y)
=4\alpha at e^{-aD}\cosh(a(x-y)).
\quad}
\tag{11}
\]

Both residual components matter: dropping the second one loses half
the interior coefficient and the cancellation in (6).

Take the existing lowest gamma mode, \(a_0=1/2\), so \(\alpha_0=2\).
After deriving (11), choosing

\[
t=\frac12e^{D/2}
\tag{12}
\]

matches its coefficient to the fixed arithmetic pole coefficient. With
\(c_L(x)=\cosh(x/2)\) and \(s_L(x)=\sinh(x/2)\), the exact positive
gluing is

\[
\boxed{\quad
\|\mathcal S_Lf\|^2
=\|\mathcal A_Lf\|^2
+2|\langle c_L,f\rangle|^2-2|\langle s_L,f\rangle|^2
+e^D\|f\|^2,\qquad D\geq L.
\quad}
\tag{13}
\]

This follows from
\(2\cosh((x-y)/2)=2c_L(x)c_L(y)-2s_L(x)s_L(y)\).
The negative odd pole occurs through interference inside one positive
norm. It was not appended as a separate negative-norm state. Equation
(13) extends from smooth inputs to all of \(\mathcal D_{\log,L}\)
by the common core, or directly because its correction is bounded.
The corresponding source-sector operator is strictly positive:
its negative pole eigenvalue is \(L-2\sinh(L/2)\), so

\[
\mathcal S_L^*\mathcal S_L
\geq\bigl(e^D+L-2\sinh(L/2)\bigr)I>0\qquad(D\geq L).
\tag{13a}
\]

Together with the compact logarithmic embedding from note 11, this
also makes its inverse a well-defined compact operator.

This realizes the pole signs, but it gives the contact \(+e^D\) rather
than
\(w_0=-\gamma_E-\pi/2-3\log2-\log\pi<0\).
It also supplies no active prime atoms. A fixed \(D\) works for all
\(L\leq D\) with the same source, but choosing \(D=L\) as support grows
changes the source and is not a support-compatible all-length theory.

## 3. The contact cost is optimal for this remote pair

Keep only the translations \(\pm D\) in one mode, but allow arbitrary
constant cap vectors in each component. Let
\(r_\pm,s_\pm\) be their overlaps with \(\chi\); orthogonal cap
components can only increase their squared norms. In the interior
\(|x-y|<D\), the cross kernel is

\[
-\frac{\alpha a}{2}e^{-aD}
\left[Xe^{a(x-y)}+\overline X e^{-a(x-y)}\right],
\quad X=r_++\overline r_-+s_+-\overline s_-.
\tag{14}
\]

To obtain \(\kappa\cosh(a(x-y))\) with real \(\kappa\), one needs
\(X=-\kappa e^{aD}/(\alpha a)\). The coefficient of the identity
in the defect norm is therefore bounded below by

\[
\begin{aligned}
\gamma_{\mathcal B}
&\geq |r_+|^2+|r_-|^2+|s_+|^2+|s_-|^2\\
&\geq\frac{|X|^2}{4}
=\frac{\kappa^2e^{2aD}}{8a}.
\end{aligned}
\tag{15}
\]

For \(a=1/2\) and \(\kappa=2\), this is \(e^D\). The source (5),
(12) attains it, since its four overlaps are
\((-t,-t,-t,+t)\), and the two translated channel vectors are
orthogonal. Thus the positive contact in (13) is not removed by
rephasing these caps, changing their constant overlaps, or rotating
the two residual components. The optimization in (15) concerns this
two-shift ansatz only.

## 4. A local prime atom carries a shifted massive kernel

There is a second simple coherent control. In a mode \(a\), let
\(c>0\), \(d>0\), and set

\[
(\mathcal B_{d,c}F)_k
=-\frac c\alpha\begin{pmatrix}U_dF\\0\end{pmatrix}\otimes\chi.
\tag{16}
\]

Its exact whole-line defect operator is

\[
\boxed{\quad
(\mathcal A^\chi+\mathcal B_{d,c})^*
(\mathcal A^\chi+\mathcal B_{d,c})
-(\mathcal A^\chi)^*\mathcal A^\chi
=\frac{ac^2}{2}I-c(U_d+U_{-d})
+ca^2R_a(U_d+U_{-d}).
\quad}
\tag{17}
\]

The equality is initially an identity of forms, with a bounded
right-hand side. The final term has the explicit continuous kernel

\[
\frac{ca}{2}
\left(e^{-a|x-y-d|}+e^{-a|x-y+d|}\right).
\tag{18}
\]

For \(d=m\log p<L\), choosing \(c=(\log p)p^{-m/2}\) gives exactly
the desired prime-translation coefficient. It simultaneously adds
the positive contact \(ac^2/2\) and changes the continuous gamma
kernel by (18). The sign of that continuous kernel pointwise does
not imply positivity of its translation-invariant operator.

Assigning finitely many prime injections to distinct massive modes
avoids their mutual cross terms but retains every term (18). Placing
several in one output creates the additional autocorrelation delays
\(d_i-d_j\) in \(\mathcal B^*\mathcal B\). These are explicit costs
of the chosen construction, not exclusions of more general defects.

## 5. A finite raw delay alphabet cannot repair the negative contact

Here is a precise extension that does not assume a finite number of
massive modes. Let \(\mathcal V\) be any fixed positive cap Hilbert
space with \(\chi\in\mathcal V\), \(\|\chi\|=1\). Let
\(\mathscr D\subset\mathbb R\) be a finite delay alphabet, with repeated
delays merged. In every mode and component specify constant vectors
\(z_{k,\epsilon,d}\in\mathcal V\), and put

\[
(\mathcal BF)_{k,\epsilon}
=\sum_{d\in\mathscr D}U_dF\otimes z_{k,\epsilon,d},
\qquad
\sum_{k,\epsilon}
\left(\sum_{d\in\mathscr D}\|z_{k,\epsilon,d}\|\right)^2<\infty.
\tag{19}
\]

This condition proves boundedness of \(\mathcal B\). With a finite
alphabet it is equivalent to square summability of all the vectors.
It allows infinitely many participating massive channels; their
truncations converge in operator norm. The operator
\(\mathcal B^*\mathcal B\) is a finite translation polynomial, with
its coefficient at zero exactly

\[
\gamma_{\mathcal B}
=\sum_{k,\epsilon,d}\|z_{k,\epsilon,d}\|^2\geq0.
\tag{20}
\]

**Proposition.** Suppose, for one \(L>0\), the gluing of (19) has
the original gamma continuous kernel, the specified pole kernel
\(2\cosh((x-y)/2)\), and otherwise only finitely many contact or
translation atoms. Then its contact coefficient is exactly (20).
Consequently it cannot equal the complete arithmetic pairing, whose
contact coefficient is \(w_0<0\).

This includes arbitrary finite constant cap mixing and constant
unitary rotations of residual components. It does not include
frequency-dependent filters, resolvent insertions in \(\mathcal B\),
infinitely many distinct delays with an accumulation point, a
modification of the bulk resolvents, or a physical constraint that
changes the source.

**Proof.** Only the cap overlaps
\(u_{k,d}=\langle\chi,z_{k,1,d}\rangle\) and
\(w_{k,d}=\langle\chi,z_{k,2,d}\rangle\) occur in the cross term.
Extend them by zero off \(\mathscr D\), and use the finite symmetric
alphabet \(\mathscr D\cup(-\mathscr D)\). Define

\[
\sigma_{k,d}=u_{k,d}+\overline{u_{k,-d}},\qquad
\theta_{k,d}=\overline{w_{k,-d}}-w_{k,d}.
\tag{21}
\]

In one mode, the cross operator is

\[
\alpha_k\sum_d\sigma_{k,d}U_d
-\alpha_ka_k^2R_{a_k}\sum_d\sigma_{k,d}U_d
+\alpha_ka_k\partial_xR_{a_k}\sum_d\theta_{k,d}U_d.
\tag{22}
\]

Away from the finitely many centers \(d\), its continuous kernel is

\[
-\sum_{k,d}\frac{\alpha_ka_k}{2}
\left[\sigma_{k,d}+\theta_{k,d}\operatorname{sgn}(z-d)\right]
e^{-a_k|z-d|},\qquad z=x-y.
\tag{23}
\]

The series and all its derivatives converge uniformly on compact
sets disjoint from the centers: square summability in (19), followed
by the exponential distance factor, dominates every polynomial in
\(a_k\). This is the actual cross-form kernel there, obtained by
truncating the bounded source and using Cauchy–Schwarz on smooth
inputs. No infinite whole-line adjoint sum is assumed to be bounded.
Equality of the compressed forms determines this difference kernel
throughout \((-L,L)\), since every such difference is attained by
interior points of \(I_L\).

On an open cell between consecutive centers, (23) has an absolutely
convergent expansion

\[
\sum_{k\geq0}\left(A_ke^{-a_kz}+B_ke^{a_kz}\right).
\tag{24}
\]

Set \(\zeta=e^{z/2}\). Since \(a_k=2k+1/2\), this is a Laurent
series with the distinct integer powers
\(\zeta^{-(4k+1)}\) and \(\zeta^{4k+1}\). It converges on the full
complex annulus determined by that cell. The assumed pole kernel
is \(\zeta+\zeta^{-1}\). Equality on a real interval forces equality
of Laurent coefficients by the identity theorem and uniqueness of
Laurent series. Extra atomic centers from the proposed target or
\(\mathcal B^*\mathcal B\) merely subdivide these cells.

For any center \(d\in(-L,L)\), compare the coefficients on its two
sides. The target Laurent coefficients are unchanged. The changes
in the two coefficients for mode \(k\) are nonzero scalar multiples
of \(\sigma_{k,d}+\theta_{k,d}\) and
\(\sigma_{k,d}-\theta_{k,d}\), respectively. Hence

\[
\sigma_{k,d}=\theta_{k,d}=0
\quad\text{for every }k\text{ and every }d\in(-L,L).
\tag{25}
\]

Their cross contributions, including the atoms in (22), therefore
vanish individually. Remaining centers lie outside the open
difference interval. Their series is smooth on every compact subset
of \((-L,L)\), so it contributes no contact distribution there.
Thus the only contact is the zero-delay coefficient of
\(\mathcal B^*\mathcal B\), namely (20). This proves the proposition.
The same argument with zero in place of the pole kernel shows that
preserving the gamma continuous kernel alone forces the entire
compressed cross term to vanish. ∎

The proposition does not infer a universal obstruction from a finite
mode calculation. Its square-summable extension is explicit, and its
finite-alphabet hypothesis is essential to the cell argument.

## 6. What the control establishes

The construction (5)–(13) realizes an infinite-state, cap-normalized,
closed positive source whose gluing contains the exact even and odd
arithmetic pole terms. It retains the original gamma kernel and
exhibits how a negative finite-rank contribution can occur through
ordinary positive-Hilbert-space interference. Its remaining contact
is positive and has an exact optimum within the two-shift model.

The prime control (16)–(18) identifies the corresponding unwanted
massive return kernel. The proposition proves that adding more raw
shifts from a fixed finite alphabet, even over square-summably many
of the massive channels, cannot supply the missing negative contact
while keeping the continuous part exact. A next construction must
change a stated hypothesis, for example by a derived resolvent
coupling or boundary constraint; choosing a target square root or an
equivalent assumed positive block would not do so.

All operator and kernel formulas in this note are direct calculations
from the sources in notes 10–11. The Laurent-series argument is an
analytical proof, not a numerical positivity test. The cap's Hodge
construction and evaluated norm are the inherited analytical inputs
from note 10.

The [exact delay-algebra program](../numerics/check_coherent_delay.py)
and its [retained record](../numerics/records/coherent-delay.json) replay
the two-channel cancellation, cross-term signs, pole coefficient,
contact optimum, and prime numerator in rational Laurent algebra.
They do not certify source domains or the infinite-channel proposition.
