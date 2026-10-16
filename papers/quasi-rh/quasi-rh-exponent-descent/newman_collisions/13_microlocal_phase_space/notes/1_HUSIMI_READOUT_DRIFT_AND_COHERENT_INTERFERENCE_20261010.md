# Husimi readout drift and coherent interference

10 October 2026. Prepared with substantial LLM assistance. Model: GPT-6
(Codex); the exact serving variant and configured reasoning effort are not
available in this session and are not inferred. The checks recorded here
are internal, not independent mathematical review.

This is the initial scout for program 13 in [Heat Note 14](../../notes/14_DIMENSIONAL_REDUCTION_AND_SUPERSYMMETRIC_HEAT_PROGRAM_20261010.md).
The new calculation is the full Gaussian-smoothed phase-space generator
and its exact reconstructed jet observations, including drift, zeroth-order
terms, and smoothing amplification. A finite doubled density matrix then
isolates both phase-difference and reflected phase-sum interference. The
genuine adjacent packet rules out a diagonal-energy nonvanishing claim in
this representation as well.

## 1. Genuine Wigner state and exact reduction

For real time define
\[
 \psi_t(u)=e^{tu^2/2}\sqrt{\Phi_e(u)},\qquad
 \partial_t\psi_t=(u^2/2)\psi_t.
\]
The positive smooth theta kernel and its super-exponential tails imply
\(\psi_t\in\mathcal S(\mathbb R)\), together with all finite time
derivatives on compact time intervals. For example its logarithmic
derivatives grow at most exponentially in \(|u|\), which is dominated by
the theta tail. It lies in every multiplication domain used here.

With the explicit convention
\[
 W_t(u,p)=\frac1{2\pi}\int e^{-ips}
 \psi_t(u+s/2)\overline{\psi_t(u-s/2)}\,ds,
\tag{1}
\]
the real-valued Wigner function is Schwartz and obeys
\[
 \int W_t(u,p)\,dp=|\psi_t(u)|^2=m_t(u),
 \qquad \partial_tW_t=u^2W_t-\tfrac14\partial_p^2W_t.
\tag{2}
\]
Indeed \(\partial_t\) of the integrand multiplies it by
\(((u+s/2)^2+(u-s/2)^2)/2=u^2+s^2/4\); Fourier transformation in \(s\)
turns the latter term into \(-\partial_p^2/4\). The genuine readout is
\[
 H_t(z)=\tfrac12\int e^{izu}W_t(u,p)\,du\,dp.
\tag{3}
\]
Integrating the \(p\)-derivative in (2) gives zero boundary flux and
\(\partial_tH_t=-\partial_z^2H_t\). The sign is retained in the lift.
Wigner positivity is not assumed.

## 2. Positive Husimi state and its entire generator

Fix \(a>0\), set \(b=1/(16a)\), and define
\[
 \mathcal H_t=e^{a\partial_u^2+b\partial_p^2}W_t.
\tag{4}
\]
Here \(a,b\) are Gaussian convolution heat parameters, so the variances
are \(2a,2b\). They are not Newman time. For the normalized Gaussian
\(g(u)=(\pi\sigma^2)^{-1/4}e^{-u^2/(2\sigma^2)}\),
\(\sigma^2=4a\), its Wigner density is
\(\pi^{-1}e^{-u^2/\sigma^2-\sigma^2p^2}\). Formula (4) is convolution
with precisely this density. Direct expansion of the Gaussian overlap gives
\[
 \mathcal H_t(u,p)=\frac1{2\pi}
 |\langle\psi_t,e^{ip(\cdot-u/2)}g(\cdot-u)\rangle|^2\ge0.
\tag{5}
\]
The irrelevant phase in this coherent-state convention does not affect its
modulus. Integration of (5) over phase space returns \(\|\psi_t\|_2^2\).
Thus this is a genuinely positive state, without claiming positive evolution
on arbitrary nonnegative functions.

The heat-convolution commutator is
\[
 e^{a\partial_u^2}(u f)=(u+2a\partial_u)e^{a\partial_u^2}f.
\]
Using it twice, with the derivative of \(u\) retained, gives the exact
generator
\[
 \partial_t\mathcal H_t=
 \left(u^2+4au\partial_u+2a+4a^2\partial_u^2
             -\tfrac14\partial_p^2\right)\mathcal H_t.
\tag{6}
\]
The positive \(u\)-diffusion term does not remove negative \(p\)-diffusion.
The cross term \(4au\partial_u\) and contact term \(2a\) are mandatory.
This calculation can be done on Schwartz functions by convolution and
integration by parts; an unbounded inverse smoothing operator on arbitrary
data is not needed or asserted. The genuine trajectory remains in the
image of (4).

If widths move, additional terms are
\(a'(t)\partial_u^2+b'(t)\partial_p^2\). Keeping fixed widths avoids
those terms; replacing widths later requires them and the moving readout
term below.

## 3. Exact smoothed observations and derivative drift

Set
\[
 F_t^a(z)=\tfrac12\int e^{izu}\mathcal H_t(u,p)\,du\,dp.
\]
Its marginal is the Gaussian convolution of \(m_t\), hence
\[
 F_t^a(z)=e^{-az^2}H_t(z),\qquad H_t(z)=e^{az^2}F_t^a(z).
\tag{7}
\]
Both sides extend entirely in \(z\); all spatial derivatives hold time and
the fixed width constant. The true first derivative is
\[
 H_t'=e^{ax^2}\bigl((F_t^a)'+2axF_t^a\bigr).
\tag{8}
\]
Consequently positivity of (5) still observes a cosine transform, and
common vanishing of \(H,H'\) is exactly common vanishing of \(F^a,(F^a)'\).
The smoothing introduces no exclusion.

The entire reduced equation from (6) is
\[
 \partial_tF_t^a=-(\partial_x+2ax)^2F_t^a
 =-(F_t^a)''-4ax(F_t^a)'-(2a+4a^2x^2)F_t^a.
\tag{9}
\]
For a moving width, (9) has the additional term \(-a'(t)x^2F_t^a\).
In particular using a time-dependent width to improve the numerical scale
does not remove the moving observation term.

To print the fourth-jet dictionary, let \(p_k=e^{-ax^2}\partial_x^ke^{ax^2}\):
\[
 p_0=1,\quad p_1=2ax,\quad p_2=2a+4a^2x^2,
\]
\[
 p_3=12a^2x+8a^3x^3,\qquad
 p_4=12a^2+48a^3x^2+16a^4x^4.
\]
Then
\[
 H^{(j)}=e^{ax^2}\sum_{k=0}^j{j\choose k}p_{j-k}(F^a)^{(k)}.
\tag{10}
\]
At a collision, this simplifies to
\[
 H''=e^{ax^2}(F^a)'',\quad
 H'''=e^{ax^2}\bigl((F^a)'''+6ax(F^a)''\bigr),
\]
\[
 H^{(4)}=e^{ax^2}\bigl((F^a)^{(4)}+8ax(F^a)'''
                 +(12a+24a^2x^2)(F^a)''\bigr).
\tag{11}
\]
These terms must be kept in any threshold-jet test; ordinary derivatives
of a positive Husimi marginal are not the genuine unsmoothed jets.

For the manuscript normalizer, use
\(A_t^a=A_te^{-ax^2}\), so the genuine normalized function is
\(Q_t=F_t^a/A_t^a=H_t/A_t\). Its logarithmic spatial derivative is
\(b^a=b-2ax\). The joint observation therefore reads
\[
 \left(\frac{e^{ax^2}F_t^a}{2A_t},
 \frac{2e^{ax^2}}{LA_t}
  ((F_t^a)'+(2ax-b)F_t^a)\right).
\tag{12}
\]
Every higher normalized jet follows by differentiating
\(e^{ax^2}/A_t\), rather than discarding normalizer drift. The expression
\(2q_3^2-3q_2q_4-\gamma q_2^2\),
\(\gamma=18\partial_x^2\log A_t+9/x^2\), in Note 13 is unchanged when
the correctly reconstructed \(q_j=Q_t^{(j)}\) are used. Treating
\(A_t^a\) as the old normalizer while reusing its old \(\gamma\) would
be a different, unjustified formula.

## 4. Exact doubled arithmetic density matrix

For a fixed genuine finite cutoff, put \(q_n=w_ne^{i\phi_n}\),
\(\alpha_n=(\log w_n)'\), and \(\beta_n=\phi_n'\). Define
\[
 v=(q_1,\ldots,q_N,\overline q_1,\ldots,\overline q_N)^\top,
 \qquad D=vv^*,
\]
and the row observations
\[
 l_0=(1,\ldots,1;1,\ldots,1),\qquad
 l_1=(\alpha_n+i\beta_n;\alpha_n-i\beta_n)_{n\le N}.
\]
The actual approximant and derivative are exactly
\[
 F_{t,N}=l_0v,\qquad F_{t,N}'=l_1v,
 \quad |\mathcal V_N|^2=
 \tfrac14l_0Dl_0^*+\tfrac4{L^2}l_1Dl_1^*.
\tag{13}
\]
All quantities are evaluated at one shared height, and \(\alpha_n\)
retains the amplitude drift. The higher derivative row is obtained from
\(q_n^{(j)}=T_{n,j}q_n\),
\(T_{n,0}=1\), \(T_{n,j+1}=T_{n,j}'+(\alpha_n+i\beta_n)T_{n,j}\),
with the conjugate row in the second half. This supplies the complete
fixed-time fourth-jet test, without freezing the coefficients during
differentiation.

The upper-left block of \(D\) has entries
\(w_nw_me^{i(\phi_n-\phi_m)}\). The upper-right block has
\(w_nw_me^{i(\phi_n+\phi_m)}\). Thus both phase differences and reflected
phase sums are present. Keeping only a density matrix for \(q\), or
dropping the off-diagonal blocks, loses some terms in the actual real pair.

The rank-one matrix \(D\) is positive, but the observations (13) can vanish.
In particular the manuscript's genuine adjacent packet at
\(x=4\pi M^2\), \(t=\kappa/(2\log M)\) has diagonal pair energy
asymptotic to \(2\cos^2(\pi/8)w_M^2\), while its coherent energy is
\(O(w_M^2/M^2)\). Therefore no positive lower bound by a fixed fraction of
the retained diagonal can hold for every such genuine packet. The complete
twist and positive-kernel controls separately rule out twist-uniform and
generic-transform positivity implications. None is an actual theta heat
collision.

## 5. Error scale and continuation

For a spectral cutoff, the explicit theta tail payment in the kinetic scout,
\[
 E_j(U)=\frac{32U^j e^{TU^2+10U-\pi e^{4U}}}
 {4\pi e^{4U}-2TU-10-j/U}
 \quad(T=1/20,U\ge1,j\le6),
\]
applies directly to the genuine readout (3) on \(|\Im z|\le1\).
Exact smoothing of the cutoff state changes the scalar error by the factor
\(e^{-az^2}\), which reconstruction cancels exactly. In contrast, an
arbitrary numerical Husimi readout error \(\varepsilon\) gives an error
\(e^{ax^2}\varepsilon\) in \(H_t(x)\). Its derivative errors use all
factors in (10), and division by \(A_t\) adds the complete product payment.
The collision margin from Note 13 is exponentially small in \(1/t\);
fixed-width damping at \(x=4\pi e^{\kappa/t}\) is vastly smaller still.
A phase-space approximation described merely as \(o(1)\) cannot support
that margin. No phase-space truncation with a certified large-height margin
is claimed in this scout.

The strongest next bounded task is an interference-sensitive inequality
for a composite-complete genuine arithmetic block, using all entries in
(13), and with a measured remainder on recombination. A Husimi mass bound,
ordinary uncertainty bound, or diagonal truncation alone stops at the
obstructions above. The continuous formulas organize exact observations
and their errors; they supply no new collision exclusion or RH conclusion.

For primary-source discussion of Wigner and Husimi observables and the limits
of coarse phase-space descriptions, see Trushechkin,
[Semiclassical evolution of quantum wave packets on the torus beyond the Ehrenfest time](https://arxiv.org/abs/1607.07572).
Its free quantum evolution is different from Newman heat. Equations (1)–(13)
are derived here with the conventions printed above.
