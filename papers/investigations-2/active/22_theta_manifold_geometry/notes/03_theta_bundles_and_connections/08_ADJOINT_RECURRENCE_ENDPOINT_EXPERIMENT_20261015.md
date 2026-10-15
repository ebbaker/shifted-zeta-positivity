# Adjoint recurrence endpoint experiment and quantitative stability

15 October 2026, America/New_York. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**. Analytic derivations were checked by separate LLM agents; this is internal research review, not external refereeing or formal verification.

**Outcome.** The proposed bounded recurrence experiment produces an explicit endpoint approximation with an \(O(L^{-1/2})\) error, an exact defect-to-observation identity, and sharp \(O(1/N)\) stability for finite positive recurrence relaxations. It does **not** produce the required signed endpoint estimate. Its unresolved boundary is exactly the original physical observation; cancelling that boundary by the primitive normalization returns the observation as the remainder. The obstruction is explicit enough to give a stopping rule for this ansatz.

This carries out the experiment proposed in [the preceding strategy note](../00_research_coordination/07_RESEARCH_PATHS_AFTER_COUPLED_PRODUCT_20261015.md). The [geometric companion](../01_physical_jet_geometry/01_ARITHMETIC_BOUNDARY_TRACE_AND_SIGNED_OBSERVATION_20261015.md) interprets its boundary class and isolates a weaker signed target. The original [coefficient recurrence](05_ELLIPTIC_SHIFT_CORE_AND_PROJECTION_OBSTRUCTION_20261015.md), [complete-start cutoff](07_PARITY_STRIP_CUTOFF_AND_FULL_STARTING_FACTOR_20261015.md), and [exponential-average criterion](../02_signed_turning_control/04_EXPONENTIAL_AVERAGE_AND_SHRINKING_CHORD_TARGETS_20261015.md) remain in force.

## Physical setup and target

For \(q=e^{4u}\), write

\[
\phi_n(u)=e^u(2\pi^2n^4q^2-3\pi n^2q)e^{-\pi n^2q},
\qquad H_n(t,x)=\int_0^\infty e^{tu^2}\phi_n(u)\cos(xu)\,du.
\]

Set \(H=\sum_{n\ge1}H_n\), \(h_j=\partial_x^jH\), \(h_{j,n}=\partial_x^jH_n\), \(E=H^2+H_x^2\), and \(W=h_j\), \(S=h_{j+1}\) for \(j=0,1\). Stationarity always means the **complete** condition \(S(t,x)=0\). The exponential chord uses

\[
\mathcal A=W(t,x)^2-e^{-\delta}W(t,x)V(t,x+\delta),
\]

where only the endpoint observation \(V\) may be approximated. The desired estimate is \(\mathcal A\ge-KE-\varepsilon\sqrt E\), with \(K\) locally finite through any covered event and with the error tending to zero at the chosen scales.

The primitive endpoint weights are

\[
\beta_n=(4\pi n^2-1)e^{-\pi n^2}>0,
\qquad \sum_{n\ge1}\beta_n=\tfrac12,
\qquad m_\beta=\sum_{n\ge1}n\beta_n<\infty.
\]

The exact theta coefficient sequence obeys \(a_0=1\), \(\Delta a_n=a_{n-1}-2a_n+a_{n+1}=0\) and \(\sum\beta_na_n=1/2\). These conditions identify \(a_n=1\). Identification alone supplies no sign for a real endpoint observation.

## A. Finite local currents and their boundary

### The prescribed current and the zero-coordinate convention

Let \(F=(F_n)_{n\ge1}\) be a real or complex sequence satisfying

\[
\|F\|_{1,1}:=\sum_{n\ge1}n|F_n|<\infty.
\]

Adjoin \(F_0=0\). Define the killed averaging operator by

\[
(TF)_0=0,\qquad (TF)_n=\frac{F_{n-1}+F_{n+1}}2\quad(n\ge1).
\tag{A.1}
\]

The coordinate at zero is **reset to zero at every application** of \(T\). In particular, \(T^k\) is not unrestricted averaging on the whole integer line, and its zeroth coordinate is never computed by averaging neighboring entries. The second difference is evaluated only at positive indices:

\[
(\Delta J)_n=J_{n-1}-2J_n+J_{n+1},\qquad n\ge1.
\]

For an integer depth \(L\ge1\), prescribe the finite current

\[
\boxed{J_n^{[L]}=-\frac12\sum_{k=0}^{L-1}(T^kF)_n,\qquad
J_0^{[L]}=0.}
\tag{A.2}
\]

Each \(J_n^{[L]}\) uses only finitely many neighboring entries of \(F\); the largest displacement is \(L-1\). Since \(\Delta=2(T-I)\) on sequences with zero zeroth coordinate, telescoping gives the exact identity

\[
\boxed{\Delta J^{[L]}=F-\rho^{[L]},\qquad \rho^{[L]}=T^LF.}
\tag{A.3}
\]

The first test in this family is completely explicit:

\[
J_n^{[1]}=-\tfrac12F_n,\qquad
\rho_n^{[1]}=\tfrac12(F_{n-1}+F_{n+1}).
\tag{A.4}
\]

More generally, the scalar polynomial-current ansatz \(J_n=P(n)F_n\) gives

\[
\Delta J_n=P(n-1)F_{n-1}-2P(n)F_n+P(n+1)F_{n+1}.
\tag{A.5}
\]

In a coefficientwise matching problem with independent mode entries, matching the central coefficient to \(F_n\) forces \(P(n)=-1/2\). The neighboring terms in (A.4) remain. Formula (A.2) iterates this explicit correction rather than silently solving an unrestricted inverse problem.

For every finite \(M\ge1\), the exact boundary formulas are

\[
\sum_{n=1}^M\Delta J_n
=J_0-J_1+J_{M+1}-J_M,
\tag{A.6}
\]

\[
\sum_{n=1}^M n\Delta J_n
=J_0-(M+1)J_M+MJ_{M+1}.
\tag{A.7}
\]

The assumption \(\|F\|_{1,1}<\infty\) implies the same weighted summability for every finite iterate and for \(J^{[L]}\). Consequently \(J_M\to0\), \(MJ_M\to0\), and both upper boundary expressions tend to zero at fixed \(L\). Thus

\[
\boxed{\sum_{n\ge1}F_n=B_L(F)+R_L(F),\qquad
B_L(F):=-J_1^{[L]},\quad R_L(F):=\sum_{n\ge1}(T^LF)_n,}
\tag{A.8}
\]

and the first moment is conserved exactly:

\[
\boxed{\sum_{n\ge1}n(T^LF)_n=\sum_{n\ge1}nF_n.}
\tag{A.9}
\]

No upper boundary is discarded before this fixed-depth convergence argument.

### Explicit survival weights and a quantitative remainder

Put

\[
p_L(k)=2^{-L}\binom L{(L+k)/2},
\]

where a binomial coefficient with a nonintegral or out-of-range lower argument is zero. Reflection at the absorbing boundary gives the exact kernel

\[
(T^LF)_n=\sum_{m\ge1}\{p_L(n-m)-p_L(n+m)\}F_m.
\tag{A.10}
\]

The kernel is nonnegative. It is the transition kernel of a symmetric nearest-neighbor walk on the positive integers, killed on reaching zero. Summing (A.10) over \(n\ge1\) gives

\[
\boxed{s_L(m)=\sum_{k=1-m}^{m}p_L(k),\qquad
q_L(m)=1-s_L(m),}
\tag{A.11}
\]

\[
\boxed{R_L(F)=\sum_{m\ge1}s_L(m)F_m,\qquad
B_L(F)=\sum_{m=1}^Lq_L(m)F_m.}
\tag{A.12}
\]

Here \(s_L(m)\) is survival through time \(L\), and \(q_L(m)\) is absorption by time \(L\). In particular, \(0\le s_L,q_L\le1\), and \(q_L(m)=0\) for \(m>L\). For the first depths,

\[
B_1(F)=\tfrac12F_1,\qquad
B_2(F)=\tfrac12F_1+\tfrac14F_2,
\]

\[
B_3(F)=\tfrac58F_1+\tfrac14F_2+\tfrac18F_3.
\tag{A.13}
\]

Let

\[
c_L=2^{-L}\binom L{\lfloor L/2\rfloor}.
\]

The interval \(1-m,\ldots,m\) contains exactly \(m\) integers of the parity admitted by \(p_L\). Hence

\[
0\le s_L(m)\le\min(1,mc_L),
\]

\[
\boxed{|R_L(F)|\le c_L\|F\|_{1,1}
\le\sqrt{\frac2{L+1}}\,\|F\|_{1,1}.}
\tag{A.14}
\]

The final elementary bound follows, for example, from
\(\binom{2a}a/4^a\le(a+1)^{-1/2}\), proved by induction using the ratio \((2a+1)/(2a+2)\), and the corresponding odd-index ratio.

For each fixed positive integer \(m\),

\[
\frac{s_L(m)}{c_L}\longrightarrow m.
\]

Indeed each of the finitely many parity-admissible binomial probabilities in (A.11), divided by the central probability \(c_L\), tends to one; this holds on both parity subsequences. The majorant \(s_L(m)/c_L\le m\) and weighted absolute summability therefore give

\[
\boxed{\frac{R_L(F)}{c_L}\longrightarrow\sum_{m\ge1}mF_m.}
\tag{A.15}
\]

Since \(c_L\sim\sqrt{2/(\pi L)}\), the leading residual is generally of order \(L^{-1/2}\). Cancellation of the first moment improves this to \(o(L^{-1/2})\), but no stronger rate is asserted here without further moment analysis. Equations (A.8) and (A.14) show at the same time that

\[
B_L(F)\longrightarrow\sum_{n\ge1}F_n.
\tag{A.16}
\]

Thus this current has a genuinely small remainder, but its lower boundary approaches the entire original observation. The current by itself does not control the sign or size of that boundary relative to the physical energy.

### A recurrence-adapted finite endpoint observation

Write

\[
h_{j,n}(t,y)=\int_0^\infty e^{tu^2}\phi_n(u)
u^j\cos(yu+j\pi/2)\,du,
\]

where

\[
\phi_n(u)=e^u\{2\pi^2n^4e^{8u}-3\pi n^2e^{4u}\}
e^{-\pi n^2e^{4u}}.
\]

For every real \(T\), define the explicit finite constant

\[
D_j(T)=2\pi^2\int_0^\infty
u^j\exp\{Tu^2+9u-(\pi/2)e^{4u}\}\,du.
\tag{A.17}
\]

For \(t\le T\), uniformly over real \(y\),

\[
|h_{j,n}(t,y)|\le D_j(T)n^4e^{-\pi n^2/2}.
\tag{A.18}
\]

To verify this, discard the negative term in \(\phi_n\) and use
\(2n^2e^{4u}\ge n^2+e^{4u}\) for \(n\ge1,u\ge0\). In particular, the weighted sequence norms used above have source-prescribed uniform bounds.

Define the finite absorption cutoff

\[
\boxed{W^{[L]}(t,y)=\sum_{m=1}^Lq_L(m)h_{j,m}(t,y),\qquad W=h_j.}
\tag{A.19}
\]

The physical error obeys

\[
\boxed{|W(t,y)-W^{[L]}(t,y)|
\le c_LD_j(T)\sum_{m\ge1}m^5e^{-\pi m^2/2}.}
\tag{A.20}
\]

Keep the starting field \(W(t,x)\), energy \(E(t,x)=H^2+H_x^2\), and stationarity condition complete. For \(j=0,1\), \(|W(t,x)|\le\sqrt{E(t,x)}\). Therefore, with \(y=x+\delta\),

\[
\begin{aligned}
A^{[L]}_{j,\delta}(t,x)
&=W(t,x)^2-e^{-\delta}W(t,x)W^{[L]}(t,y),\\
|A_{j,\delta}-A^{[L]}_{j,\delta}|
&\le e^{-\delta}c_LD_j(T)
\left(\sum_{m\ge1}m^5e^{-\pi m^2/2}\right)\sqrt E.
\end{aligned}
\tag{A.21}
\]

This is a factor-preserving transfer estimate. The weights depend only on the endpoint index; no starting cutoff has been introduced. Its \(O(L^{-1/2})\sqrt E\) error is adequate for the fixed-length, independent-cutoff version of the collision criterion. It is also smaller than every fixed power of \(\delta_L=1/\log(L+2)\). It is not adequate for arbitrary multiplicity with the much faster choice \(\delta_L=1/L\) merely from the present bound.

The finite primitive endpoint must use the same weights:

\[
\beta_n=(4\pi n^2-1)e^{-\pi n^2},\qquad
\beta^{[L]}=\sum_{m=1}^Lq_L(m)\beta_m.
\]

Since \(\sum\beta_m=1/2\),

\[
\boxed{\tfrac12-\beta^{[L]}=R_L(\beta)>0,
\qquad R_L(\beta)\sim c_L\sum_{m\ge1}m\beta_m.}
\tag{A.22}
\]

The absorption cutoff is a concrete output of the experiment, not a sign improvement. A lower bound for \(A^{[L]}_{j,\delta}\) is still required independently.

### Exact outcome of a normalization correction

Let \(r\in\ell^1_1\) be a fixed endpoint residual sequence. In the proposed reconstruction it is

\[
r_n=\mathbf1_{n\le N}h_{j,n}(t,x+\delta)
-A H_n(t,x)-B H_{n,x}(t,x)-C h_{j+1,n}(t,x),
\tag{A.23}
\]

with coefficients fixed before this current calculation. Formula (A.18) verifies the required summability for each finite coefficient choice, uniformly on parameter sets with bounded coefficients and an upper heat-time bound. All statements below are exact for each parameter value. Asymptotic statements in \(L\) hold for a fixed sequence \(r\); they must not be imported for an \(L\)-dependent residual without additional uniform hypotheses.

Apply the current to \(F=r-\eta\beta\). Restoring the complete primitive endpoint gives

\[
\begin{aligned}
\sum_nr_n
&=B_L(r-\eta\beta)+\eta/2+R_L(r-\eta\beta)\\
&=\boxed{B_L(r)+\eta R_L(\beta)+R_L(r-\eta\beta).}
\end{aligned}
\tag{A.24}
\]

The denominator \(R_L(\beta)\) is strictly positive at every finite depth. One can therefore prescribe

\[
\eta_L=-\frac{B_L(r)}{R_L(\beta)}
\tag{A.25}
\]

and cancel the lower-boundary-plus-normalization term exactly. Nevertheless,

\[
\boxed{R_L(r-\eta_L\beta)=\sum_nr_n}
\tag{A.26}
\]

holds identically. This correction leaves the entire unknown reconstruction residual in the remainder.

More quantitatively, if \(s_r=\sum_nr_n\ne0\), (A.15)--(A.16) give

\[
c_L\eta_L\longrightarrow-
\frac{s_r}{\sum_m m\beta_m}.
\tag{A.27}
\]

Thus \(\eta_L\) has critical order \(\sqrt L\); the apparent \(L^{-1/2}\) remainder gain is lost when the size of the corrected sequence is included. No division by \(H\), \(E\), or the stationary observation was used. Even a correction whose scalar denominator is explicitly positive can merely relocate the unresolved quantity. Equations (A.24)--(A.27) are a negative result for this normalization strategy, not a prohibition on every arithmetic multiplier.

### A narrowly scoped pointwise no-inverse proposition

The following proposition concerns identities before integration in \(u\). It does not apply automatically to identities among integrated transforms at a fixed \((t,x)\).

Fix a finite set of real frequencies \(\Omega\). Let \(\mathscr A_\Omega\) be the class of functions

\[
f(u,q)=\sum_{\omega\in\Omega}P_\omega(u,q)e^{i\omega u},
\qquad q=e^{4u},
\]

where each \(P_\omega\) is a polynomial in \(u,q\). Zero terms and coincident frequencies are combined. Coefficients may depend on fixed external parameters and on the mode indices.

Choose a finite neighboring-mode range \(L\ge0\). Consider currents defined for \(n\ge0\) by

\[
J_n(u)=e^ue^{tu^2}
\sum_{\substack{m\ge1\\|m-n|\le L}}
e^{-\pi m^2q}j_{n,m}(u,q),\qquad
j_{n,m}\in\mathscr A_\Omega.
\tag{A.28}
\]

Unlike the killed-current family, this proposition need not impose \(J_0=0\); its zeroth current may contain the positive source modes \(m\le L\). The range condition itself excludes every \(m>L\) from \(J_0\).

The class includes finitely many source \(u\)-derivatives, polynomial multipliers in \(u,q,n\) or \(\pi n^2q\), and finitely many neighboring source modes, after their terms are combined. Differentiating the heat factor, a square mode, or a physical spectral phase preserves this class. The declaration excludes exponential multipliers that convert one square-mode exponent into another, unbounded mode ranges, and an additional source-divergence term.

**Proposition.** Suppose

\[
F_n(u)=e^ue^{tu^2}e^{-\pi n^2q}f_n(u,q),
\qquad f_n\in\mathscr A_\Omega,
\]

and

\[
\Delta_nJ_n(u)=F_n(u)
\quad\text{for every }n\ge1\text{ and every }u>0.
\tag{A.29}
\]

Then \(f_m\equiv0\) for every \(m>L\).

**Proof.** Distinct functions \(e^{-\pi m^2e^{4u}}\) are independent over \(\mathscr A_\Omega\). To see this, take the least mode with a nonzero coefficient in a finite putative relation and divide by its double-exponential factor. Every later mode is super-exponentially smaller as \(u\to\infty\). A nonzero finite exponential polynomial
\(\sum P_\omega(u,e^{4u})e^{i\omega u}\)
cannot have that decay: its largest \(e^{4du}\) degree and largest polynomial \(u\) degree leave a nonzero finite trigonometric polynomial, which has a nonzero mean square and hence a sequence of nonvanishing values at arbitrarily large \(u\). This contradicts the required super-exponential smallness. Iterating proves independence.

For a fixed \(n\), (A.29) contains only finitely many modes, so this independence extracts the coefficient of each global mode \(m\):

\[
\Delta_nj_{n,m}=\mathbf1_{n=m}f_m.
\]

For fixed \(m\), the sequence \(j_{n,m}\) has finite support in \(n\), contained in \(|n-m|\le L\). Formula (A.7) therefore gives, exactly,

\[
\sum_{n\ge1}n\Delta_nj_{n,m}=j_{0,m}.
\]

If \(m>L\), its right side is zero, whereas the extracted target contributes \(mf_m\). Thus \(f_m=0\), as claimed. \(\square\)

For the endpoint reconstruction in (A.23), take \(x\ge0\), \(\delta>0\), and \(N>L\). At \(m=L+1\le N\), its pointwise source residual contains frequency \(x+\delta\), distinct from the starting frequencies \(\pm x\). Its endpoint term cannot be canceled by any scalar \(A,B,C\). The proposition therefore excludes an exact pointwise identity of the form (A.29) in this declared class. Exceptional frequency coincidences, such as \(x+\delta=-x\), are outside that stated application.

The range obstruction is sharp as an algebraic statement. If a target is supported on \(1\le m\le L\), the finite inverse

\[
J_n(u)=\sum_{m=n+1}^L(m-n)F_m(u)
\]

does satisfy \(\Delta J=F\), but its lower boundary is
\(J_0-J_1=\sum_{m=1}^LF_m\). Enlarging the current until it contains the complete finite endpoint can therefore solve the index algebra while leaving the desired observation unchanged at the boundary.

This proposition does not rule out cancellation after source integration, a joint identity containing \(\partial_uK_n\) with its complete endpoints, nonlocal index currents, or one-sided bilocal estimates. A primitive endpoint correction is a boundary functional and must be restored explicitly; it cannot be treated as an unexplained pointwise interior cancellation.

### Interpretation

For this chosen current, the relevant geometry is the discrete half-line with an absorbing boundary. The affine harmonic direction \(n\) explains the conserved first moment and the leading survival remainder. It is the same elementary affine direction that appears in the projected recurrence's ramp ambiguity. Normalizing the source removes the input ramp but does not estimate the signed output boundary. This interpretation is not a claim of a new general source geometry or a replacement for the prior complete-source identities.

## B. Normalized recurrence defects and physical observations

Put

\[
\beta_n=(4\pi n^2-1)e^{-\pi n^2},\qquad
\sum_{n\ge1}\beta_n=\tfrac12,
\quad m_\beta=\sum_{n\ge1}n\beta_n\ge\tfrac12.
\]

For a coefficient sequence with \(a_0=1\), define the recurrence and endpoint defects

\[
d_k=a_{k-1}-2a_k+a_{k+1},\qquad
e=\sum_{n\ge1}\beta_na_n-\tfrac12.
\]

Assume \(\sum\beta_n|a_n|<\infty\). Polynomial growth is sufficient but unnecessary. Positive normalized sequences automatically satisfy this assumption. They need not give a smooth source density at zero, so their physical observations should be defined through the absolutely convergent mode transforms below.

### Complete physical bounds

Let \(f_n=\partial_x^jH_n(t,x)\), for any fixed nonnegative integer \(j\). The source modes satisfy

\[
\frac{\phi_n(u)}{\beta_n}
\le\frac{2\pi^2}{4\pi-1}n^2
e^{9u-\pi n^2(e^{4u}-1)}.
\]

For finite \(T\), set

\[
M_j(T)=\sup_{u\ge0}u^j
\exp\{Tu^2+9u-\tfrac\pi2(e^{4u}-1)\}<\infty,
\quad C_j(T)=\frac{\pi M_j(T)}{4\pi-1}.
\]

Since \(e^{4u}-1\ge4u\) and \(n^2-1/2\ge n^2/2\), integration of \(n^2e^{-2\pi n^2u}\) proves

\[
|f_n|\le C_j(T)\beta_n\qquad(t\le T,\ x\in\mathbb R).
\tag{B.1}
\]

Thus all weighted physical mode sums converge absolutely. Fixed finite combinations of jets or real endpoint evaluations satisfy the same statement with the corresponding sum of constants. Coefficients that are locally bounded in the physical parameters preserve local boundedness.

The endpoint has an exact transform meaning. For \(p_n=e^u e^{-\pi n^2e^{4u}}\), one has \(p_n''-p_n=8\phi_n\), \(p_n'(0)=-\beta_n\). Integration against \(\cosh u\) gives

\[
\boxed{\beta_n=8\int_0^\infty\phi_n(u)\cosh u\,du.}
\tag{B.2}
\]

Accordingly the normalized primitive endpoint is \(H_a(0,i)=1/16\). It is one exact affine anchor, not the desired real stationary estimate.

### Discrete Green formula and normalized dual

For any mode test satisfying \(|f_n|\le C\beta_n\), define

\[
F_\theta=\sum f_n,\quad m_f=\sum nf_n,\quad
G_f(k)=\sum_{n>k}(n-k)f_n,
\quad G_\beta(k)=\sum_{n>k}(n-k)\beta_n.
\]

Use distinct notation for the first moment \(m_\beta=G_\beta(0)\) and the tail Green weights \(G_\beta(k)\). Set

\[
\eta_f=\frac{m_f}{m_\beta},\qquad
D_k(f)=G_f(k)-\eta_fG_\beta(k).
\tag{B.3}
\]

Then the exact normalized defect-to-observation identity is

\[
\boxed{F_a-F_\theta
=\eta_f e+\sum_{k\ge1}D_k(f)d_k,\qquad
F_a=\sum_{n\ge1}a_nf_n.}
\tag{B.4}
\]

To prove it, write \(b=a_1-1\). The elementary finite-index recurrence solution is

\[
a_n=1+nb+\sum_{k<n}(n-k)d_k.
\]

Equivalently, as a formal generating-function identity,

\[
A(z)=\frac1{1-z}+\frac{bz}{(1-z)^2}
+\frac{z\sum_{k\ge1}d_kz^k}{(1-z)^2}.
\]

Summing the finite-index formula first against \(\beta_n\) and then against \(f_n\) gives
\(e=bm_\beta+\sum G_\beta(k)d_k\) and
\(F_a-F_\theta=bm_f+\sum G_f(k)d_k\). Eliminating \(b\) proves (B.4).

All exchanges are justified under the stated weighted assumption. Indeed \(\beta_{n+1}/\beta_n<1/2\), so

\[
G_\beta(k)\le4\beta_{k+1},\qquad
\sum_{k\ge1}G_\beta(k)|d_k|<\infty.
\]

The last conclusion follows by expanding \(d_k\) into its three neighboring coefficients and using monotonicity of \(\beta_n\).

### Quantitative content and the boundary obstruction

The coefficients in (B.3) require no division by \(H\), \(E\), or stationarity:

\[
|\eta_f|\le C,\qquad
|D_k(f)|\le2C G_\beta(k)\le8C\beta_{k+1}.
\]

Consequently

\[
\boxed{|F_a-F_\theta|
\le C\left(|e|+2\sum_{k\ge1}G_\beta(k)|d_k|\right).}
\tag{B.5}
\]

For physical jets this is uniform for real \(x\) and \(t\le T\). The dual weights decay at Gaussian rate. A *uniform Gaussian remainder after truncating the defect sum* additionally requires a uniform bound on the defects: polynomially bounded defects suffice, while arbitrary normalized positive sequences supply convergence but no common Gaussian tail rate.

The same construction displays the exact lower boundary that prevents (B.4) from becoming a sign theorem. Let \(\Delta D_k=D_{k-1}-2D_k+D_{k+1}\). Then

\[
\Delta D_k=f_k-\eta_f\beta_k,\qquad
D_0=0,\qquad D_1=-F_\theta+\eta_f/2.
\tag{B.6}
\]

Discrete summation by parts therefore reads

\[
F_a=\eta_f(\tfrac12+e)-D_1
+\sum_{k\ge1}D_k(f)d_k.
\]

The endpoint anchor removes the affine slope, but the unknown theta observation remains exactly in \(D_1\). Choosing the automatic Green inverse has merely moved that observation to the lower boundary. Requiring both \(D_0=D_1=0\) would impose the extra identity \(F_\theta=\eta_f/2\), which is not implied by the recurrence. For an endpoint reconstruction residual, it is precisely an additional physical estimate that must be proved.

Thus (B.4)–(B.5) give constructive quantitative stability and a diagnostic for candidate arithmetic currents. They do not yield a favorable sign at theta, where \(d=e=0\). Any useful new current must bound or cancel the boundary by an independent source argument, and must preserve complete stationarity and the starting factor through every subsequent remainder.

## C. Finite recurrence hierarchy: sharp stability and a slope anchor

In this section \(L=N+1\) denotes the affine-prefix cutoff, independently of the current depth used in Part A.

Let \(\beta_n=(4\pi n^2-1)e^{-\pi n^2}\), with \(\sum_{n\ge1}\beta_n=1/2\), and define

\[
R_L=\sum_{n>L}\beta_n,\qquad
m_L=\sum_{n=1}^{L}n\beta_n,\qquad
m_\beta=\sum_{n\ge1}n\beta_n.
\]

Suppose \(a_0=1\), \(a_n\ge0\), \(\sum\beta_na_n=1/2\), and
\(a_{k-1}-2a_k+a_{k+1}=0\) for \(1\le k\le N\). Put \(L=N+1\).

### Uniform upper bound

The recurrence gives \(a_n=1+bn\) for \(0\le n\le L\), where \(b=a_1-1\). Positivity and normalization imply

\[
-\frac1L\le b\le\frac{R_L}{m_L},\qquad
T_a:=\sum_{n>L}\beta_na_n=R_L-bm_L\ge0.
\]

Consequently

\[
\begin{aligned}
\sum_{n\ge1}\beta_n|a_n-1|
&\le |b|m_L+T_a+R_L\\
&=2R_L+(|b|-b)m_L\\
&\le 2R_L+\frac{2m_L}{L}
\le 2R_L+\frac{2m_\beta}{L}.
\end{aligned}
\tag{C.1}
\]

For any mode observation satisfying \(|f_n|\le C\beta_n\), the complete sums therefore obey

\[
\boxed{|F_a-F_\theta|\le
2C\left(R_L+\frac{m_L}{L}\right).}
\tag{C.2}
\]

The physical-mode bound in the recurrence-defect derivation makes this uniform in real spectral coordinate and heat times bounded above, for each fixed spatial jet. No polynomial-growth assumption on \(a_n\) is needed.

### Sharp weighted distance

Choose \(M>L\). Set \(a_n=(1-n/L)_+\) except at \(n=M\), and set

\[
a_M=\frac{R_L+m_L/L}{\beta_M}.
\]

This nonnegative, finitely supported sequence has \(a_0=1\), satisfies all the prescribed recurrences, and has exactly the required endpoint normalization. For sufficiently large \(M\), one has \(a_M\ge1\), and a direct calculation gives

\[
\sum\beta_n|a_n-1|
=2R_L+\frac{2m_L}{L}-2\beta_M.
\tag{C.3}
\]

Thus the sharper bound in (C.1) is the exact supremum over this relaxation.

### The algebraic loss occurs in an actual physical observation

At \(t=x=0\), put

\[
p_n(u)=e^u e^{-\pi n^2e^{4u}},\qquad
P_n=\int_0^\infty p_n(u)\,du>0.
\]

The exact primitive integration by parts gives

\[
H_n(0,0)=\frac{\beta_n-P_n}{8},\qquad
\frac{P_n}{\beta_n}\le\frac1{(4\pi n^2-1)^2}\longrightarrow0.
\]

For the preceding ramp/spike family, as \(M\to\infty\), the physical deviation therefore tends to

\[
\boxed{H_a(0,0)-H_\theta(0,0)\longrightarrow
\frac{\sum_{n\le L}nP_n+L\sum_{n>L}P_n}{8L}.}
\tag{C.4}
\]

This limit is positive and is at least \(P_1/(8L)\). For each \(L\), a sufficiently large finite \(M\) yields a deviation at least \(P_1/(16L)\). Moreover the numerator tends to \(\sum_{n\ge1}nP_n>0\), so the limit in (C.4) has exact order \(1/L\). Hence no uniformly smaller order, in particular no Gaussian rate, follows from the finite projected recurrence, positivity, and the endpoint alone. These are admissible finite weighted controls; no collision is asserted.

### Adding the missing slope anchor

If \(a_1=1\) is also imposed, then \(b=0\), so \(a_n=1\) for \(1\le n\le L\) and \(T_a=R_L\). Equations (C.1)–(C.2) improve to

\[
\sum\beta_n|a_n-1|\le2R_L,\qquad
\boxed{|F_a-F_\theta|\le2CR_L.}
\]

Since \(R_L=O((L+1)^2e^{-\pi(L+1)^2})\), this is Gaussian control, with the first omitted coefficient at \(n=L+1=N+2\).

These are quantitative stability results for a relaxed coefficient family. Even Gaussian absolute transform closeness does not become an error of order \(o(\sqrt E)\) near an unknown event without an additional argument.

## What the experiment closes and leaves open

The finite current gives a controlled approximation and the normalized dual gives a controlled response to coefficient defects. At the exact theta sequence the defects vanish, so the latter identity reduces to equality with the unknown theta observation. Neither calculation supplies its favorable sign.

The finite-range source obstruction is deliberately narrow. It does not exclude an identity involving a source-variable divergence,

\[
r_n(u)=\Delta_nJ_n(u)+\partial_uK_n(u)+\rho_n(u),
\]

or a one-sided bilocal estimate after integration. Such a calculation must retain the complete \(n=0\) and \(u=0\) fluxes, all finite-cutoff corrections, and the full stationary starting factor. Earlier complete-source work already included source divergence and primitive endpoints. Merely adding that notation is therefore not a new mechanism. A useful extension must establish a new signed estimate for the complete resulting trace.

The geometric companion gives a precise weaker target. If a source-prescribed reconstruction is

\[
V=AH+BH_x+CS+B_{\partial}+R,
\quad |R|\le\varepsilon,
\quad \rho=\sqrt E,
\]

seek on full stationary starts

\[
\frac{W}{\rho}B_{\partial}\le C_0\rho+\varepsilon_0.
\]

With locally bounded \(A,B,C_0\), this implies
\(WV\le(|A|+|B|+C_0)E+(\varepsilon+\varepsilon_0)\sqrt E\).
It allows large boundary traces whose pairing with the starting jet has the favorable sign. Absolute endpoint reconstruction is stronger than necessary. This estimate remains open.

## Verification and scope

The standard-library [exact checker](../../numerics/check_adjoint_recurrence_boundary.py) passes **6,892 rational assertions**; its [receipt](../../numerics/ADJOINT_RECURRENCE_BOUNDARY_CHECKS_20261015.json) records the script hash and scope. It compares random-walk distributions against the independent binomial reflection formula, checks the local current and both boundary moments, demonstrates the normalization cancellation identity, checks the normalized defect formula, and tests the finite hierarchy with rational surrogate weights. The surrogate weights are explicitly not the actual theta coefficients. The analytic bounds, sharp asymptotics, and pointwise finite-source obstruction are proved in this note, not by the assertion count.

The [review](../../reviews/08_ADJOINT_RECURRENCE_AND_GEOMETRIC_REVIEW_20261015.md) records independent audits and the distinction between constructive estimates and the unresolved theta sign. No new collision exclusion, global positivity theorem, or RH conclusion is claimed. The manuscript is unchanged.
