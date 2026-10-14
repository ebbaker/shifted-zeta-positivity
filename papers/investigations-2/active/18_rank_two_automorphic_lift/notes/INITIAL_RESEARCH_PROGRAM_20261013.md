# Initial research program for the rank-two automorphic lift

**Status update, 14 October 2026:** the
[bounded matched A4 pilot](2_MATCHED_STATIONARY_SIGNED_MODE_PILOT_20261014.md)
is complete and stopped without a new sign or matched saving. The exact
identities, completed tail bounds and the original stopping/reopening
conditions are preserved; see the [current disposition](../README.md).
Prepared for Edward Baker with LLM assistance by `gpt-6-astra`, effort **ultra**.

**Allocation update, 13 October 2026.** Prepared for Edward Baker with
substantial LLM assistance by `gpt-6-astra` (Codex), effort **ultra**.
The current origin and A4 gate below incorporate the accepted consolidation;
the original Claude provenance and completed identities are retained.

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.
Status: first bounded tasks A1–A3 complete (see
[Note 1](1_CUSP_FORMULA_HECKE_AND_CONTROLS_20261013.md)); A4 open. No
collision exclusion, zero-free region or RH implication is claimed.

## Origin and scope

This is direction A of the
[Claude review](../../../brainstorm/reviews/REVIEW_OF_ACTIVE_LIFTED_THETA_DIRECTIONS_CLAUDE_20261013.md)
(§3). Following the accepted consolidation, 07 and 15 are organized
under this program, with their unfinished cutoff and compatibility tasks
preserved. [09's completed reduction](../../../inactive/09_rank_two_theta_addition/README.md)
is an input shared with [06](../../06_paired_kernel_factorization/README.md);
its folded endpoint ledger and negative sector results remain distinct
from this program's raw-source Hecke identity.

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
   time. This is the raw-source Hecke form of the parity relation; the
   separate folded 09-to-06 reduction and its endpoints remain preserved.
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

A4 must declare its time-height domain and comparator, retain the actual
stationary constraints, and account for both Laguerre targets and every
higher-mode, endpoint and tail payment. A favorable first mode alone is
insufficient. A new complete signed estimate, justified positive structure,
or demonstrated saving can support continuation. If A4 yields only another
representation or the known main-term/remainder structure, stop with Note 1
as the identity record. W1 remains deferred.

## Literature anchors

Zagier's renormalized Rankin–Selberg method (1981) for the Hecke periods;
[Lagarias–Suzuki](https://arxiv.org/abs/math/0412039) for Hermite–Biehler
arguments on constant terms of Eisenstein series;
[Young](https://arxiv.org/abs/1306.1554) for Eisenstein series restricted
to this geodesic. Standard facts used: the Fourier–Whittaker expansion of
\(E^*\), its Hecke eigenvalues \(\lambda_w(n)=\sum_{ab=n}(a/b)^{w-1/2}\), and
\(K_\nu(X)=\tfrac12\int e^{-X\cosh v+\nu v}\,dv\).
