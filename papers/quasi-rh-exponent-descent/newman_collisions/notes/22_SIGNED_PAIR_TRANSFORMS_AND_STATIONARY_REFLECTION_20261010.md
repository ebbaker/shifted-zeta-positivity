# Signed pair transforms and the prescribed stationary reflection

10 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex); exact serving variant and configured reasoning effort
are not exposed and are not inferred. The derivations and cross-audits are
internal LLM work, not independent mathematical validation.

This continues the signed primitive-ratio and product priority of
[Heat Note 20](20_ANALYTIC_SCHUR_CONES_AND_DENSITY_STRENGTHENED_THRESHOLDS_20261010.md)
and [project 09 Note 6](../09_prime_phase_torus/notes/6_ANALYTIC_COMMON_FACTOR_SMOOTHING_AND_PRIMITIVE_SIGNED_FRONTIER_20261010.md).
The continuation develops a candidate-paid kernel that cancels the diagonal,
an oscillation-preserving product transform, and a coupled Möbius treatment
of the primitive frontier. It also derives the prescribed stationary
reflection below. The transformed signed main terms still require their
opposite threshold sign; no uniform collision exclusion is claimed.

## 1. The three new arithmetic targets

[Project 09 Note 7](../09_prime_phase_torus/notes/7_DIAGONAL_ANNIHILATING_PAID_KERNELS_AND_NEAR_PAIR_BOUNDS_20261010.md)
uses the two actual paid candidate coordinates to replace the old quadratic
by a complete kernel whose four ratio/product coefficients vanish on the
diagonal. Its cosine coefficients contain the factor
\((\rho_n^2-\rho_m^2)^2\). A macroscopic narrow pair band can then
be paid absolutely below the existing physical upper-budget scale. Higher
finite moments enter only the candidate-null term and its finite moment
bound; no approximation to genuine fifth or sixth derivatives is assumed.

[Project 09 Note 8](../09_prime_phase_torus/notes/8_OSCILLATION_PRESERVING_PRODUCT_POISSON_TRANSFORM_20261010.md)
keeps the product oscillation inside finite Poisson integrals. It separates
stationary modes from uniformly nonstationary modes, treating the latter by
phase-aware integration by parts. Literal cutoff and block endpoints remain
in its boundary terms. This resolves the growing absolute derivative loss
identified in Note 6; it does not estimate the sign of the retained modes.

[Project 09 Note 9](../09_prime_phase_torus/notes/9_COUPLED_MOBIUS_PRIMITIVE_FRONTIER_AND_RESONANT_SUBLATTICES_20261010.md)
expresses the exact small-common-factor frontier as a Möbius-weighted sum of
complete sublattice quadratics, keeping difference and product terms coupled.
An oscillation-preserving finite Poisson formula supplies a paid expression
for every sublattice. The true candidate constraints apply to the full sum,
not separately to each sublattice. The signed Möbius coefficients and shifted
dual weights must remain in any subsequent inequality.

These are complementary representations. Errors belong to the particular
representation used in a signed estimate; its main terms cannot be added
to those of a second complete representation as though they were disjoint.

## 2. Exact physical data for stationary reflection

Freeze the physical center, time, and natural integer cutoff. Write
\[
0<t\le1/20,\quad 1\le\kappa\le3/2,\quad
L=\kappa/t,\quad x=4\pi e^L,\quad
N=\left\lfloor\sqrt{e^L+t/16}\right\rfloor.
\]
Use the actual data of Heat Note 8 and project 09 Note 2:
\[
\begin{split}
a_r&=\tfrac12L+\tfrac14\log(1+x^{-2})-\frac1{1+x^2},\\
a_i&=\frac{3x}{1+x^2}-\tfrac12\arctan x,\\
U&=\frac{7x^2-5}{(1+x^2)^2},\qquad
V=\frac{x(x^2+5)}{(1+x^2)^2},\\
T&=\frac{x-ta_i}{2},\quad P=\frac{T}{2\pi},\quad
\sigma=\frac12+\frac t2a_r,\\
\mu&=\frac{\Re\{(a_r+ia_i)(1+t(U+iV)/2)\}}{1+tU/2}
     =a_r-\frac{ta_iV}{2(1+tU/2)}.
\end{split}
\tag{1}
\]
Here \(T\) is the large arithmetic frequency, not the heat time.
For a positive real index \(v\), define
\[
w(v)=v^{-\sigma}e^{t\log^2v/4},\qquad
q(v)=w(v)e^{i(\theta_t+T\log v)},\qquad
\rho(v)=\log v-\mu.
\tag{2}
\]
The extension to real indices is an amplitude used in an integral; it
does not replace the original integer arithmetic state. The carrier is
\[
\theta_t=-\pi+\tfrac14\arctan x+\frac x4(1-L)
-\frac x8\log(1+x^{-2})+\frac t2a_ra_i.
\tag{3}
\]

For the original-index Fourier integral, the phase is
\[
\Phi_k(v)=T\log v-2\pi kv.
\]
When \(k>0\), its unique stationary point is \(v_k=P/k\),
with negative second derivative and
\[
\Phi_k(v_k)=T\log(P/k)-T,\qquad
|\Phi_k''(v_k)|=T/v_k^2.
\tag{4}
\]
The usual interior leading stationary coefficient therefore has amplitude
\(w(P/k)\sqrt P/k\) and phase
\(T\log(P/k)-T-\pi/4\). This normalization is the negative-curvature
case of [NIST stationary phase](https://dlmf.nist.gov/2.3#iv).
Only its coefficient is studied here. A leading coefficient alone is not
a uniform approximation when a saddle meets an endpoint; the exact
integrals and uniform boundary terms in the companion notes are retained.

## 3. The quadratic heat weight reflects into the prescribed family

For any positive \(P,k\), the amplitude identity is exact:
\[
\frac{\sqrt P}{k}w(P/k)
=C_{\rm sd}\, k^{-\sigma^*}e^{t\log^2k/4},
\qquad
\sigma^*=1-\sigma+\frac t2\log P,
\quad C_{\rm sd}=P^{1/2-\sigma}e^{t\log^2P/4}.
\tag{5}
\]
Put
\[
\delta_\sigma=\sigma-\left(\frac12+\frac t4\log P\right).
\]
Then \(\sigma^*=\sigma-2\delta_\sigma\), and (5) becomes
\[
\frac{\sqrt P}{k}w(P/k)
=w(k)\exp\{\delta_\sigma(2\log k-\log P)\}.
\tag{6}
\]
In particular, if \(\delta_\sigma=0\), the heat weight is exactly
invariant in this stationary amplitude. This equality uses the prescribed
quadratic logarithmic heat factor, not an arbitrary positive coefficient.

For the actual data, uniformly in the stated sector as \(t\downarrow0\),
\[
\delta_\sigma=O(t x^{-2}+t^2x^{-1}).
\tag{7}
\]
Indeed \(\log P=L+\log(1-ta_i/x)\), so
\[
\delta_\sigma=\frac t2
\left[a_r-\frac L2-\frac12\log(1-ta_i/x)\right].
\]
The exact rational formulas in (1) give
\(a_r-L/2=O(x^{-2})\) and \(a_i=O(1)\), proving (7).
On a fixed macroscopic dual interval
\(c_1\sqrt P\le k\le c_2\sqrt P\), the exponent in (6) is
\(O(\delta_\sigma)\), since
\(2\log k-\log P=2\log(k/\sqrt P)\) is bounded. The separate
prefactor and power must be combined before estimating them; estimating
them separately introduces a needless logarithmic factor.

## 4. The actual center and carrier reflect as well

Define
\[
\Delta_\mu=\log P-2\mu,\qquad
\Theta=2\theta_t+T\log P-T-\pi/4.
\tag{8}
\]
Then exactly
\[
\rho(P/k)=-\rho(k)+\Delta_\mu,
\]
and the actual physical mismatches satisfy
\[
\Delta_\mu=O(x^{-2}),\qquad \Theta+2\pi=O(x^{-1}).
\tag{9}
\]
The constants are uniform for \(0<t\le1/20\) at sufficiently large
\(x\); in particular they are uniform along the shrinking sector.

For the first bound, put \(z=ta_i/x\). Formula (1) gives
\[
\Delta_\mu=\log(1-z)-2(a_r-L/2)
+z\frac{xV}{1+tU/2}.
\tag{10}
\]
Here \(xV=1+O(x^{-2})\), \(U=O(x^{-2})\), and
\(\log(1-z)+z=O(z^2)\). Consequently
\[
\Delta_\mu=O(x^{-2}+t^2x^{-2}+tx^{-3})=O(x^{-2}).
\]
The nominal terms of order \(t/x\) cancel because the center includes
the actual frequency derivative.

For the phase, let \(T_0=x/2\), \(\delta=T-T_0=-ta_i/2\),
and \(F(u)=u\log(u/(2\pi))-u\). Its exact Taylor formula gives
\[
F(T)-F(T_0)=\delta L+
\delta^2\int_0^1\frac{1-v}{T_0+v\delta}\,dv.
\]
Substituting (3) into (8), with \(F(T_0)=T_0(L-1)\), yields
\[
\begin{split}
\Theta+2\pi={}&\tfrac12\arctan x-\frac\pi4
-\frac x4\log(1+x^{-2})+ta_i(a_r-L/2)\\
&+\delta^2\int_0^1\frac{1-v}{T_0+v\delta}\,dv.
\end{split}
\tag{11}
\]
The right side is \(O(x^{-1}+tx^{-2}+t^2x^{-1})\), proving (9).
The terms of order \(tL\) cancel exactly; discarding the heat correction
in either the carrier or frequency would lose this cancellation.

## 5. Static coefficient reflection and its paid mismatch

The leading carried stationary datum for a fixed logarithmic degree j is
\[
\begin{split}
B_j(k)={}&e^{i\theta_t}\frac{\sqrt P}{k}w(P/k)
\rho(P/k)^j e^{i\{T\log(P/k)-T-\pi/4\}}\\
={}&e^{i\Theta}e^{\delta_\sigma(2\log k-\log P)}
\overline{q(k)}\{-\rho(k)+\Delta_\mu\}^j.
\end{split}
\tag{12}
\]
This is an exact algebraic identity for the leading coefficient defined
on the first line. On any fixed macroscopic dual interval as above,
\(\rho(k)\) is bounded, and (7), (9) give
\[
\left|B_j(k)-(-1)^j\overline{q(k)}\rho(k)^j\right|
\le C_j x^{-1}w(k).
\tag{13}
\]
Since \(\sqrt P/N\to1\), a macroscopic dual interval contains
\(O(N)\) integer indices and has weights \(O(w_N)\). Summing
(13) therefore costs \(O_j(Nw_N/x)\).

The exact limiting algebra is the antilinear map
\[
M_j\longmapsto(-1)^j\overline{M_j}.
\tag{14}
\]
It fixes every even cosine moment and every odd sine moment. Hence
\[
X_2\mapsto X_2,\quad Y_3\mapsto Y_3,\quad X_4\mapsto X_4,
\]
and the density-strengthened threshold quadratic
\[
2Y_3^2+3X_2X_4-\Gamma_{\rm count}X_2^2
\tag{15}
\]
is invariant under (14), for either normalizer coefficient. It also fixes
\(X_0,Y_1\), while \(X_1\) changes sign. The drift-containing
candidate \(Z_1=Y_1+\epsilon X_1\) thus becomes
\(Z_1-2\epsilon X_1\); its small physical drift must be paid.

For any fixed finite moment quadratic with matrix scale \(\mathfrak M\),
the coefficient mismatch on a macroscopic dual interval is at most
\[
O\!\left(\mathfrak M\frac{(Nw_N)^2}{x}\right)
=O\!\left(\mathfrak M N^{-1-\kappa/4}\right),
\tag{16}
\]
by bilinearity, the moment envelope \(O(Nw_N)\), and (13).
The physical \(\epsilon=O(t/x)\) costs a smaller term of the same
type. The bound vanishes below the displayed physical upper-budget scale
for \(\mathfrak M=O(L)\). This is a coefficient comparison on the
stated macroscopic interval, not a global stationary-phase error theorem.

## 6. Why reflection alone does not supply the sign

The stationary image of an original interval \([A,B]\) is the dual
interval \([P/B,P/A]\). In particular, the original macroscopic block
roughly \([N/2,N]\) maps roughly to \([N,2N]\), rather than to
the same natural cutoff. Poisson endpoint transition factors also remain
in the integrals. For a q-sublattice the weight, center, and carrier acquire
additional q-dependent shifts, as derived in project 09 Note 9.

Thus (12)–(14) cannot identify the transformed finite sum with the original
finite sum on the same index set. Even if an auxiliary reflected data set
is compared on matching ranges, (15) reproduces its threshold quadratic;
it does not turn it into a negative square. This is a scoped limitation of
using the leading stationary reflection alone. It does not prohibit a
signed inequality using the actual coupled stationary terms, boundary
coefficients, or candidate constraints across the complete transformed sum.

## 7. Remaining signed theorem

The analytical remainder obligations now have explicit mechanisms that
preserve product oscillation and primitive coupling. The next theorem must
bound the complete retained resonant contribution together with its boundary
terms and paid candidate-null terms. A negative margin must exceed the
appropriate transformation remainder and recomputed physical payment.

The diagonal cancellation allows a narrow macroscopic pair band to be paid
separately; the remaining separated pairs still retain both ratio and
product channels. The Möbius coefficients and q-dependent reflected data
cannot be replaced by independent positive moment envelopes or independently
enforced candidate equations. Higher multiplicities, small-curvature
candidates, complementary parameters, and the small-time endpoint remain
obligations of the eventual uniform exclusion argument.
