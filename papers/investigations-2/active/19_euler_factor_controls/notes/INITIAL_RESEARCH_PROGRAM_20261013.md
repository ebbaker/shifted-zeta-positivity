# Initial research program for the Euler-factor controls

**Status update, 14 October 2026:** the fixed outward witness is now
[certified in Note 2](2_CERTIFIED_EULER_FACTOR_WITNESS_20261014.md), proving
`Lambda_(1/2,41)>0.2`. Prepared for Edward Baker with LLM assistance by
`gpt-6-astra`, effort **ultra**. The dated plans and numerical claims below
retain their original scope; the local expansion remains formal and no
tracked collision is identified with the global constant.

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.

**Correction, 13 October 2026.** Prepared for Edward Baker with LLM
assistance by `gpt-6-astra` (Codex), reasoning effort **ultra**. Original
Claude provenance above is retained. This revision distinguishes tracked
collision times from the global Newman constant and corrects the witness
margin; it introduces no new numerical certificate.

Status: first results in [Note 1](1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md);
the shared protocol below is in force. No collision exclusion, zero-free
region or RH implication is claimed.

## Purpose

The [Claude review](../../../brainstorm/reviews/REVIEW_OF_ACTIVE_LIFTED_THETA_DIRECTIONS_CLAUDE_20261013.md)
(§1.3) introduced a family sharing theta's positivity, evenness, real zeros
at time zero and local Euler-factor relations away from one prime:
\[
\Phi_{c,p}(u)=\Phi(u)+\tfrac c2\bigl[\Phi(u+a)+\Phi(u-a)\bigr],\qquad
a=\tfrac12\log p,\quad 0<c<1 .
\]
Each is positive, even and superexponentially decaying. Its transform at
\(t=0\) is \(H_0(x)(1+c\cos ax)\), so it has exactly the real zeros of
\(H_0\), and it has non-real zeros at \(|\operatorname{Im}x|=\delta=2\operatorname{arccosh}(1/c)/\log p\).
Its Dirichlet series is \(\zeta(s)Q_p(p^{-s})\) with
\(Q_p(X)=1+(2\sqrt p/c)X+pX^2\). It is modular for a congruence subgroup,
keeps every Euler factor and Hecke relation at primes \(q\ne p\), and has
\(\Lambda_{c,p}>0\).

This folder makes the family a shared screening tool and studies it as an
object. Write \(T_0(c,p)\) for the tracked lowest-pair collision time.
The computations estimate \(T_0\); identifying it with the global Newman
constant \(\Lambda_{c,p}\) would require all remaining zeros to be real
by that time. The immediate task is a certified negative Laguerre witness
at a specified time, which proves a lower bound without that global
identification.

## The three-controls protocol

Every new identity, inequality or certificate in the portfolio should
report its behaviour on three controls. A screen applies only when the
control satisfies every hypothesis used by the proposed argument; a
shared identity does not rule out a method with an additional genuine
theta hypothesis that excludes the control.

| Control | Definition | What it shares with theta | \(\Lambda\) | Screens out |
| --- | --- | --- | --- | --- |
| C1 shape | \(q_{T,b}(u)=e^{-Tu^2}[\phi(u)/2+\phi(u-2b)/4+\phi(u+2b)/4]\), \(\phi=e^{-\cosh u}\) ([11 Oct brainstorm](../../../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md), R1) | positivity, evenness, superexponential decay, bounded zero strip | exactly \(T\) | arguments using shape, moment signs, pointwise stationary signs, radial positivity, transport certificates |
| C2 real-axis perturbation | \(\widetilde\Phi_X=s_X\Phi\{1+a_X\cos((X-d)u)+b_X\cos((X+d)u)\}\) ([angular seeds](../../02_angular_jacobi_gluing/notes/ANGULAR_GLUING_AND_RIGIDITY_REVIEW_SEEDS_20261013.md)) | positive, even, arbitrarily close to theta in relative supremum norm on \(\mathbb R\), scalar reflection | joint zero at a prescribed \((T,X)\) | arguments using real-line closeness to theta plus scalar reflection |
| C3 Euler factor | \(\Phi_{c,p}\) above | the real zeros at \(t=0\), modularity for a congruence subgroup, Euler factors and Hecke relations at all \(q\ne p\) | \(\Lambda_{c,p}>0\); numerically \(T_0\approx4\log(1/c)/(\log p)^2\) | arguments using the Euler product at finitely many primes |

C2 and C3 are dual. C2 multiplies the *source* by cosines, which adds
shifted copies of \(H\) along the real \(x\)-axis. C3 multiplies the
*transform* by a cosine, which adds shifted copies of \(\Phi\) along the real
\(u\)-axis; at Newman time these become copies of \(H_t\) at complex
spectral shifts \(x\pm2ita\).

**Report format.** For a proposed relation \(R\), state whether \(R\)
holds for C1, for C2, and for C3 at which primes \(p\). If \(R\) holds for a
control with \(\Lambda>t_0\), then \(R\) alone cannot prove \(\Lambda\le
t_0\). An exact identity that every control also satisfies is a rewriting,
not a constraint.

**Applied so far.**

| Relation | C1 | C2 | C3 |
| --- | --- | --- | --- |
| 02 elliptic transport (uses the full integer lattice law) | no lattice structure | no lattice structure | lattice law fails at the theta scale (review §1.3, item 5) |
| 18 Theorems 1–2 (cusp formula) | no Eisenstein lift | no Eisenstein lift | same kernel with translated test functions (18, Prop. 4a) |
| 18 Theorem 3 (Hecke at 2) | no Dirichlet expansion | no Dirichlet expansion | holds for every \(p\ne2\) |
| 17 winding count | holds | holds | holds |

None of these relations carries a sign. The winding count holds for every
heat solution, so it screens nothing.

## Bounded tasks

1. **Recorded.** Exact Newman-time flow of the controls; the
   Laguerre-witness criterion; a numerical table of \(T_0(c,p)\) and
   collision points; a formal local expansion in
   \(t_m=4\log(1/c)/(\log p)^2\). The table and expansion are not
   certificates for the global constant \(\Lambda_{c,p}\).
2. **Next.** Certify one witness with outward arithmetic. The natural
   target is \(\Lambda_{1/2,41}>0.2\), suggested by
   \(T_0(1/2,41)-0.2\approx1.17\cdot10^{-4}\) and a negative numerical
   witness (Note 1, §2). Certify the raw negative margin: the normalized
   ratio diverges near an isolated simple-pair collision while the raw
   margin tends to zero.
   The 60-digit outward evaluator of the
   [project-17 pilot](../../../inactive/17_spacetime_collision_degree/numerics/check_genuine_theta_boundary_pilot.py)
   is the obvious starting point; the control needs three shifted copies
   of the same source.
3. Prove the lower half of the expansion,
   \(\Lambda_{c,p}\ge t_m-S_2t_m^2-O(t_m^3)\), with witnesses at
   \(x=\pi/a\) and explicit Taylor bounds for \(H_t\) near 0.
4. Quantify the higher pairs if needed for a proposed large-height
   argument. The sampled \(k=1,2\) collision times are smaller than
   \(T_0\) and vary nonmonotonically; no claim has been established for
   all higher pairs or any pre-existing off-line zeros of \(H_0\).

## Stop rule

The folder is a tool. Keep it while other directions use the protocol.
Close the research part after task 2 if the certified witness and the
numerical \(T_0\) table are all that the portfolio needs. Pursue tasks 3–4
only when a named use of the screen requires them. The
[legacy-key guide](../numerics/README.md#legacy-labels-and-what-the-record-establishes)
explains the unchanged historical checker and JSON labels.
