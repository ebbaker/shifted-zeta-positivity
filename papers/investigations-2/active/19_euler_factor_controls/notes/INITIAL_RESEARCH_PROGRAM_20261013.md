# Initial research program for the Euler-factor controls

13 October 2026. Prepared for Edward Baker with LLM assistance.
Model: Claude Opus 5.5 (configured identifier `claude-opus-5-5`; the serving
model may differ), Claude Cowork, reasoning effort **max**.
Status: first results in [Note 1](1_EXACT_FLOW_WITNESSES_AND_ASYMPTOTICS_20261013.md);
the shared protocol below is in force. No collision exclusion, zero-free
region or RH implication is claimed.

## Purpose

The [Claude review](../../../brainstorm/reviews/REVIEW_OF_ACTIVE_LIFTED_THETA_DIRECTIONS_CLAUDE_20261013.md)
(§1.3) introduced a family of sources that agree with theta in everything
except the Euler factor at one prime:
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
object. Its questions are how large \(\Lambda_{c,p}\) is, where the decisive
collision happens, and how to certify lower bounds.

## The three-controls protocol

Every new identity, inequality or certificate in the portfolio should
report its behaviour on three controls.

| Control | Definition | What it shares with theta | \(\Lambda\) | Screens out |
| --- | --- | --- | --- | --- |
| C1 shape | \(q_{T,b}(u)=e^{-Tu^2}[\phi(u)/2+\phi(u-2b)/4+\phi(u+2b)/4]\), \(\phi=e^{-\cosh u}\) ([11 Oct brainstorm](../../../../quasi-rh-exponent-descent/brainstorm/NEW_PATHS_FORWARD_BRAINSTORM_CLAUDE_20261011.md), R1) | positivity, evenness, superexponential decay, bounded zero strip | exactly \(T\) | arguments using shape, moment signs, pointwise stationary signs, radial positivity, transport certificates |
| C2 real-axis perturbation | \(\widetilde\Phi_X=s_X\Phi\{1+a_X\cos((X-d)u)+b_X\cos((X+d)u)\}\) ([angular seeds](../../02_angular_jacobi_gluing/notes/ANGULAR_GLUING_AND_RIGIDITY_REVIEW_SEEDS_20261013.md)) | positive, even, arbitrarily close to theta in relative supremum norm on \(\mathbb R\), scalar reflection | joint zero at a prescribed \((T,X)\) | arguments using real-line closeness to theta plus scalar reflection |
| C3 Euler factor | \(\Phi_{c,p}\) above | the real zeros at \(t=0\), modularity for a congruence subgroup, Euler factors and Hecke relations at all \(q\ne p\) | \(\Lambda_{c,p}>0\); numerically \(\approx4\log(1/c)/(\log p)^2\) | arguments using the Euler product at finitely many primes |

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

1. **Done.** Exact Newman-time flow of the controls; the Laguerre-witness
   criterion; a numerical table of \(\Lambda_{c,p}\) and collision points;
   the first-order expansion in \(t_m=4\log(1/c)/(\log p)^2\).
2. **Next.** Certify one witness with outward arithmetic. The natural
   target is \(\Lambda_{1/2,41}>0.2\), which is numerically true by a
   margin of \(1.2\cdot10^{-4}\) yet has a robust witness (Note 1, §2).
   The 60-digit outward evaluator of the
   [project-17 pilot](../../17_spacetime_collision_degree/numerics/check_genuine_theta_boundary_pilot.py)
   is the obvious starting point; the control needs three shifted copies
   of the same source.
3. Prove the lower half of the expansion,
   \(\Lambda_{c,p}\ge t_m-S_2t_m^2-O(t_m^3)\), with witnesses at
   \(x=\pi/a\) and explicit Taylor bounds for \(H_t\) near 0.
4. Quantify the higher pairs. Their collision times are smaller and
   decrease irregularly with height; this measures how C3 screens
   arguments that work only at large height.

## Stop rule

The folder is a tool. Keep it while other directions use the protocol.
Close the research part after task 2 if the certified witness and the
table are all that the portfolio needs.
