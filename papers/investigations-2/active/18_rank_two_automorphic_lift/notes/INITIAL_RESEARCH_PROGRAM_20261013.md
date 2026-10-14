# Initial research program for the rank-two automorphic lift

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.
Status: first bounded tasks A1–A3 complete (see
[Note 1](1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md)); A4 open. No
collision exclusion, zero-free region or RH implication is claimed.

## Origin and scope

This is direction A of the
[Claude review](../../../brainstorm/reviews/REVIEW_OF_ACTIVE_LIFTED_THETA_DIRECTIONS_CLAUDE_20261013.md)
(§3). It absorbs card 09 (rank-two theta addition), and the
[recommendation note](../../CLOSE_AND_MERGE_RECOMMENDATIONS_CLAUDE_20261013.md)
proposes folding 07 (divisor transport) and 15 (adelic compatibility) into
it. It also executes the next allocation of the
[Codex first pass](../../../brainstorm/reviews/PRIORITY_RESEARCH_FIRST_PASS_CODEX_20261013.md),
which recommends "the bounded 09-to-06 calculation" once the angular gate
of 02 is not met.

The physical quadratic observations of the heat flow are pair transforms of
\(\Phi(u_1)\Phi(u_2)\). In volume and shape coordinates \(u_{1,2}=s\pm r\),
the pair source is a rectangular lattice theta function, and its Mellin
transform in the volume is the completed Eisenstein series
\(E^*(z,w)=\xi_c(2w)E(z,w)\) on the imaginary-axis geodesic
\(z=ie^{4r}\). The full modular group then acts on the lattice shape,
transverse to the physical variable, and the physical height becomes the
spectral parameter \(w=\tfrac12+\tfrac{ix}2\). The question is whether this
larger symmetry, or the Hecke operators that come with it, carries a sign
through the Newman deformation.

## Source, generator and observation

- Source: \(\Phi(u)=\sum_n(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}\),
  even and positive; \(H_t(x)=\tfrac12\int e^{tu^2+ixu}\Phi(u)\,du\).
- Generator: multiplication by \(e^{t(u_1^2+u_2^2)}=e^{2t(s^2+r^2)}\) on the
  pair.
- Observations: \(\mathscr L_0=H_x^2-HH_{xx}\) and
  \(\mathscr L_1=H_{xx}^2-H_xH_{xxx}\), with pair weights \(r^2\) and
  \(r^2(r^2-s^2)\). The stationary signs are \(\mathscr L_0\ge0\) on
  \(\{H_x=0\}\) and \(\mathscr L_1\ge0\) on \(\{H_{xx}=0\}\).

## Bounded tasks

1. **A1 (done).** Transport the physical insertions into the lift and write
   both Laguerre expressions at Newman time \(t>0\); verify against direct
   computation at \((t,x)=(0.05,8)\) and \((0.05,28.27)\).
2. **A2 (done).** Write the Hecke correspondence at 2 as an exact identity
   between the imaginary-axis geodesic and the geodesic
   \(\operatorname{Re}z=\tfrac12\), and in physical form at every Newman
   time. This is card 09's two-coset identity.
3. **A3 (done).** Control test: express the Euler-factor controls
   \(\Phi_{c,p}\) of [direction 19](../../19_euler_factor_controls/README.md)
   in the lift and determine which Hecke relations they satisfy.
4. **A4 (open, final bounded task).** Decide whether the folded cusp
   moments have any positive-definite structure: the sign of the first
   Whittaker mode for all heights, and a bound for the higher modes at
   stationary points over a height range. Compare with the
   Riemann–Siegel main-sum and remainder structure of 01.
5. **Deferred wild card W1.** The horocyclic-to-geodesic family of review
   §6. Not started; its endpoint does not satisfy RH, so it needs a new
   monotonicity before it is worth a calculation.

## Validation

Every identity has an exact algebraic part (rational arithmetic) and a
double-precision replay against direct theta quadrature. Each new identity
reports its behaviour on the three controls of
[direction 19](../../19_euler_factor_controls/notes/INITIAL_RESEARCH_PROGRAM_20261013.md).
An identity that also holds for a control with \(\Lambda>t_0\) cannot by
itself prove \(\Lambda\le t_0\).

## Stop rule

If, after A4, the stationary targets reduce to positivity of a folded cusp
moment with no positive-definite structure (no expression as
\(\langle f,f\rangle\), no positive Selberg-type transform, no
Hermite–Biehler pair) and no saving beyond the known main-term/remainder
structure, close 18 with Note 1 as its identity record.

## Literature anchors

Zagier's renormalized Rankin–Selberg method (1981) for the Hecke periods;
[Lagarias–Suzuki](https://arxiv.org/abs/math/0412039) for Hermite–Biehler
arguments on constant terms of Eisenstein series;
[Young](https://arxiv.org/abs/1306.1554) for Eisenstein series restricted
to this geodesic. Standard facts used: the Fourier–Whittaker expansion of
\(E^*\), its Hecke eigenvalues \(\lambda_w(n)=\sum_{ab=n}(a/b)^{w-1/2}\), and
\(K_\nu(X)=\tfrac12\int e^{-X\cosh v+\nu v}\,dv\).
