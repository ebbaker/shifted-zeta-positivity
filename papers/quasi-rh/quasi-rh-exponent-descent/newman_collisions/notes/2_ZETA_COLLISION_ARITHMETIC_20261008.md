# Zeta collision arithmetic: exact theta identities and the finite-cutoff obstruction

8 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: GPT-6 (Codex), inherited configuration; the exact serving variant and
configured reasoning effort are not exposed to this agent and are not inferred.
Parallel same-model review is an internal check, not independent validation.

Status: elementary exact identities, an arithmetic-truncation obstruction, and
a conditional finite-certificate theorem. No new sign estimate for the full
zeta heat flow, new zero-free region, or proof of RH is asserted. The small
numerical record is floating-point reconnaissance, not interval certification.

The useful new distinction is that **every fixed finite theta cutoff has an
eventually negative collision Wronskian**, at every finite heat time. The exact
modular cancellation of odd endpoint derivatives is lost by that cutoff.
This makes positivity of a truncated theta Wronskian an unsuitable all-height
target, even if all its omitted terms have positive Fourier weight. The
finite-certificate theorem below pays those omissions as errors and remains
valid on prescribed compact rectangles.

## 1. Exact arithmetic quantities

Use the same normalization as the [parent bridge](../../../prime-variance-exponents/notes/QUASI_RH_NEWMAN_BRIDGE_20261008.md):

\[
 H_t(x)=\int_0^\infty e^{tu^2}\Phi(u)\cos(xu)\,du,
 \qquad H_0(x)=\tfrac18\xi(\tfrac12+ix/2),
\]
\[
 \Phi(u)=\sum_{n\ge1}\phi_n(u),\qquad
 \phi_n(u)=(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})e^{-\pi n^2e^{4u}}.
 \tag{1}
\]

The representation and evenness of the **full** kernel follow from the theta
functional equation; see [Polymath, equations (1)–(4)](https://arxiv.org/html/1904.12438#S1).
For \(u\ge0\), every \(\phi_n(u)>0\). Absolute convergence, including after
any finite number of parameter derivatives, justifies the manipulations
below on compact parameter sets. The bounds in Section 3 also verify this.

Put \(w_t(u)=e^{tu^2}\Phi(u)\) on \([0,\infty)\). Two collision quantities are

\[
 C_t(x)=H_t(x)^2+H'_t(x)^2,
 \qquad W_t(x)=H'_t(x)^2-H_t(x)H''_t(x).
 \tag{2}
\]

For real \(t,x\), \(C_t(x)>0\) is **equivalent** to no simultaneous zero of
\(H_t,H'_t\). The inequality \(W_t(x)>0\) is sufficient at that point, but
is not a pointwise equivalent condition: a noncolliding point can have a
negative Wronskian. Away from zeros,

\[
 W_t=-H_t^2(\log |H_t|)'',
\]

and the exact arithmetic double integral is

\[
 W_t(x)=\frac14\int_0^\infty\!\int_0^\infty w_t(u)w_t(v)
 \left((u+v)^2\cos(x(u-v))+(u-v)^2\cos(x(u+v))\right)du\,dv.
 \tag{3}
\]

Indeed, symmetrize \(-H_tH_t''\), then apply the product-to-sum identities to
\(H_t'^2\) and the cosine product. Substitution of (1) gives an absolutely
convergent double sum over the actual squared-integer lattice \((n^2,m^2)\).
The coefficients of that lattice sum are positive; its cosines have both
signs. No termwise positivity claim follows.

There is also a single-integral Dirichlet-polynomial representation. Put
\(\ell_n(v)=\log(v/(\pi n^2))\). The substitution
\(v=\pi n^2 e^{4u}\) gives exactly

\[
 H_t(x)=\frac{\pi^{-1/4}}4\int_\pi^\infty
 (2v-3)v^{1/4}e^{-v}
 \sum_{n\le\sqrt{v/\pi}}n^{-1/2}
 e^{t\ell_n(v)^2/16}\cos(x\ell_n(v)/4)\,dv.
 \tag{4}
\]

For \(H_t^{(j)}\), multiply each summand by \((\ell_n(v)/4)^j\)
and replace its cosine by
\(\cos(x\ell_n(v)/4+j\pi/2)\). Formula (4) is an exact finite sum at
each integration point, with an infinite outer integral. It is not an Euler
product for \(H_t\). Applying a family estimate would require a new theorem
for these weights and for the outer integral and its errors.

At time zero an alternative exact summand is

\[
 H_0(x)=\frac{\pi^{-1/4}}4\operatorname{Re}
 \sum_{n\ge1}n^{-1/2}(\pi n^2)^{-ix/4}
 \left[2\Gamma(9/4+ix/4,\pi n^2)
       -3\Gamma(5/4+ix/4,\pi n^2)\right].
 \tag{5}
\]

This is obtained directly from (4), not by evolving an unjustified infinite
Dirichlet series. Equation (4), or its differentiated version, keeps the
heat weight at positive time.

## 2. Why a fixed theta cutoff necessarily fails at large height

Define

\[
 \Phi_N=\sum_{n=1}^N\phi_n,\qquad
 H_{t,N}(x)=\int_0^\infty e^{tu^2}\Phi_N(u)\cos(xu)\,du,
 \quad N\ge1.
\]

These are genuine finite arithmetic approximants, but \(\Phi_N\) is not even
as an analytic function of \(u\). With \(a_n=\pi n^2\), direct differentiation
gives

\[
 \phi'_n(0)=-a_n(8a_n^2-30a_n+15)e^{-a_n}.
\]

The full evenness identity \(\Phi'(0)=0\) implies

\[
 A_N:=\Phi_N'(0)
 =\sum_{n>N}a_n(8a_n^2-30a_n+15)e^{-a_n}>0.
 \tag{6}
\]

The positivity is strict: \(n>N\ge1\) implies \(a_n\ge4\pi\), beyond the
larger root \((15+\sqrt{105})/8\) of the quadratic. Termwise differentiation
at zero is justified by Gaussian convergence. Approximate values are
\(A_1=0.0394987653\), \(A_2=8.26527958\times10^{-8}\), and
\(A_3=1.39172586\times10^{-16}\).

### Proposition 1: the cutoff Wronskian is eventually negative

For every fixed \(N\ge1\), uniformly for \(t\) in a compact real interval,

\[
 \begin{aligned}
 H_{t,N}(x)&=-A_Nx^{-2}+O_{N,t}(x^{-4}),\\
 H'_{t,N}(x)&=2A_Nx^{-3}+O_{N,t}(x^{-5}),\\
 H''_{t,N}(x)&=-6A_Nx^{-4}+O_{N,t}(x^{-6}),
 \end{aligned}
\]
\[
 W_{t,N}(x)=-2A_N^2x^{-6}+O_{N,t}(x^{-8})<0
 \quad\text{for sufficiently large }|x|.
 \tag{7}
\]

**Proof.** Let \(f(u)=e^{tu^2}\Phi_N(u)\). All its derivatives are integrable
on \([0,\infty)\), uniformly on compact time intervals, and \(f'(0)=A_N\)
because the heat multiplier has zero derivative at zero. Repeated integration
by parts gives
\(\int_0^\infty f(u)\cos(xu)du=-f'(0)/x^2+f'''(0)/x^4+O(x^{-6})\).
Apply the same integration-by-parts argument separately to
\(-u f(u)\sin(xu)\) and \(-u^2f(u)\cos(xu)\); do not differentiate an
uncontrolled asymptotic remainder. Their leading coefficients are
\(2f'(0)\) and \(-6f'(0)\). Substitution proves (7). \(\square\)

The full theta kernel cancels **all** odd endpoint derivatives, including
after multiplication by \(e^{tu^2}\). At the first derivative, the omitted
lattice tail supplies exactly \(-A_N\). Thus the algebraic term in (7) is
an arithmetic truncation defect, not an approximation to a sign change of
the full zeta Wronskian.

In fact the cutoff cannot have all its zeros real at any finite time. It is
a real entire function of order at most one: its defining integral gives
\(\log\max_{|z|\le r}|H_{t,N}(z)|=O_{N,t}(r\log(r+2))\).
A real entire function of order less than two with all zeros real satisfies
the Laguerre inequality \(F'^2-FF''\ge0\) on the real axis, by its
Hadamard product (or the sum of reciprocal squared distances away from its
zeros). Equation (7) contradicts that necessary inequality. This is a
failure of these approximants, not of the original heat flow or of the
strip theorem: an initial bounded zero strip is not available for them.

Naively restoring evenness also has a cost. For finite \(N\),
\(\Phi_N(-u)\sim-3\pi(\sum_{n\le N}n^2)e^{-5u}\) as \(u\to\infty\).
The symmetrization \((\Phi_N(u)+\Phi_N(-u))/2\) therefore cannot be
multiplied by \(e^{tu^2}\) and integrated absolutely for any \(t>0\).
An even replacement must also retain heat integrability; finite analytic
symmetrization alone does not do that.

## 3. Uniform finite-approximation errors

Here \(0\le t\le\tau\le1/2\), \(U>0\), and

\[
 P_{j,N,U}(t,x)=\int_0^U u^j e^{tu^2}\Phi_N(u)
                   \cos(xu+j\pi/2)\,du.
\]

The bounds are uniform over **all real** \(x\); they are absolute errors,
not relative errors near the exponentially small zeta heat transform.

Let \(m=N+1\), and define

\[
 B_N=e^{-\pi m^2}
 \left(m^4+\frac{m^3}{2\pi}+\frac{3m}{4\pi^2}
                         +\frac{3}{8\pi^3m}\right).
\]

Monotonicity of \(v^4e^{-\pi v^2}\) for \(v\ge1\), comparison with its
integral, two integrations by parts, and the Gaussian tail inequality give
\(\sum_{n>N}n^4e^{-\pi n^2}\le B_N\). Hence the omitted lattice terms on
\([0,U]\) contribute at most

\[
 E^{\mathrm{lat}}_j
 =2\pi^2e^{\tau U^2+9U}\frac{U^{j+1}}{j+1}B_N.
 \tag{8}
\]

For the spatial tail, note that

\[
 \Phi(u)\le4\pi^2e^{9u-\pi e^{4u}},\qquad u\ge0.
 \tag{9}
\]

For example,
\(\sum_{n\ge1}n^4e^{-\pi(n^2-1)}
 \le(1-16e^{-3\pi})^{-1}<2\), using
\(n^4\le16^{n-1}\) and \(n^2-1\ge3(n-1)\).
Set

\[
 d_j=4\pi e^{4U}-2\tau U-9-j/U.
\]

If \(d_j>0\), concavity of
\(j\log u+\tau u^2+9u-\pi e^{4u}\) on \([U,\infty)\) gives

\[
 E^{\mathrm{sp}}_j
 =\frac{4\pi^2U^j e^{\tau U^2+9U-\pi e^{4U}}}{d_j},
 \qquad
 |H_t^{(j)}(x)-P_{j,N,U}(t,x)|
 \le E_j:=E^{\mathrm{lat}}_j+E^{\mathrm{sp}}_j.
 \tag{10}
\]

Indeed the logarithmic derivative is \(-d_j\) at \(U\), and its second
derivative is
\(-j/u^2+2\tau-16\pi e^{4u}<0\). Its tangent majorant integrates to
(10). Take larger \(U\) if the denominator condition fails.

If certified quadrature gives
\(|P_{j,N,U}-a_j|\le q_j\), put \(e_j=E_j+q_j\). Then

\[
 \left|W_t-(a_1^2-a_0a_2)\right|
 \le2|a_1|e_1+e_1^2+|a_0|e_2+|a_2|e_0+e_0e_2.
 \tag{11}
\]

Thus even the scalar Wronskian can be rigorously checked on a prescribed
region if its errors and region coverage are supplied. A negative cutoff
Wronskian with an error bar crossing zero says nothing about the full sign.

## 4. A finite conditional certificate with actual rectangle coverage

Let \(R=[t_-,t_+]\times[x_-,x_+]\), with
\(0\le t_-\le t_+\le1/2\). Obtain finite certified upper bounds

\[
 M_j\ge\int_0^\infty u^j e^{t_+u^2}\Phi(u)\,du,
 \qquad j=1,2,3,
\]

using positive quadrature and (8)–(10), for example. Partition \(R\) into
finitely many closed cells. A cell with center \((t_c,x_c)\), time
half-width \(b\), and spatial half-width \(a\) is certified collision-free
if, for certified center approximations \(a_0,a_1\) and total center errors
\(e_0,e_1\), either

\[
 |a_0|>e_0+aM_1+bM_2
 \quad\text{or}\quad
 |a_1|>e_1+aM_2+bM_3.
 \tag{12}
\]

### Proposition 2: finite-certificate theorem

If every cell passes (12), then \(H_t\) and \(H'_t\) have no common real
zero anywhere in \(R\). Conversely, if they have no common zero on that
compact rectangle, a sufficiently fine partition and sufficiently accurate
certified quadrature and truncations produce such a finite certificate.

**Proof.** The identities \(\partial_tH=-H''\) and
\(\partial_tH'=-H'''\), together with the moment bounds, give the two
Lipschitz errors in (12). Each accepted cell has a nonvanishing component.
For the converse, continuity and compactness give a positive minimum of
\(\sqrt{H^2+H'^2}\). One component at every center has magnitude at least
that minimum divided by \(\sqrt2\). Refine the mesh and numerical errors
below that common margin. The analytic integral has convergent validated
quadrature schemes, and (8)–(10) tend to zero with suitable \(N,U\).
\(\square\)

This is an effective characterization of compact collision exclusion, not a
uniform arithmetic lower bound on the collision vector. No rectangle is
claimed certified by the accompanying floating-point script.

## 5. The remaining height issue and the next research task

The [Newman scout](1_NEWMAN_FLOW_AND_COLLISION_SCOUT_20261008.md) proves that a
positive zeta threshold forces a finite real collision. Its compactness
argument uses the positive-time cutoff from
[Polymath, Theorem 1.5(i)](https://arxiv.org/html/1904.12438#S1.Thmtheorem5),
which grows like \(\exp(C/t)\). For a hypothesized threshold at least
\(\varepsilon>0\), a sufficiently large rectangle can contain its collision;
an explicit certificate needs an effective numerical height cutoff as well.
No fixed rectangle covers every possible positive threshold as
\(\varepsilon\downarrow0\).

There is a second practical cost. Formula (10) gives errors independent of
\(x\), while the natural archimedean envelope of \(H_t\) decays on the scale
\(\exp(-\pi |x|/8+o(|x|))\). This is an envelope comparison, **not a lower
bound** on \(H_t\) or the collision vector. To make these crude absolute
errors small compared with that scale, one needs roughly
\(N^2\gtrsim |x|/8\), \(e^{4U}\gtrsim |x|/8\), and increasing quadrature
precision. Near joint small values the required margin could be much worse.
The finite-cutoff obstruction explains why omitted arithmetic tails cannot
be dropped merely because they are absolutely tiny.

A useful next task is therefore a **derivative-aware normalized effective
heat approximation**, with all complex-neighborhood errors included.
Polymath's effective Riemann–Siegel representation supplies a starting point;
its approximation changes when its integer cutoff changes. One must not
differentiate a pointwise error estimate or a jumping cutoff as though it
were an analytic remainder.

Concretely, if \(B\) is a locally nonzero analytic normalizing factor and
\(Q=H_t/B\), then

\[
 H_t=H'_t=0\quad\Longleftrightarrow\quad Q=Q'=0,
\]
\[
 \frac{W_t}{B^2}=Q'^2-QQ''-(\log B)''Q^2.
 \tag{13}
\]

If \(B,F\) are holomorphic on a neighborhood of the closed radius-\(r\)
disk about a real point, \(B\) is nonzero throughout that neighborhood,
and \(|Q-F|\le\eta\) on the bounding circle, Cauchy's estimate gives
\(|Q'-F'|\le\eta/r\) at its center. Thus
\(|F|>\eta\) or \(|F'|>\eta/r\) excludes a collision there. The missing
input is a certified analytic-neighborhood approximation, with a valid
branch and cutoff handling and bounds on both sides of the real axis; the
published scalar approximation is not silently promoted to that input.
Time and spatial coverage still require cell bounds such as (12), and an
all-positive-time theorem would still require an additional arithmetic
nonvanishing estimate.

The theta identities retain zeta's specific squared-integer coefficients and
the cancellation among their endpoint jets. **Vanishing of odd endpoint jets
itself does not distinguish zeta from the general-kernel counterexample:**
that example is also even and smooth, so its odd jets vanish too. The result
here diagnoses what a finite theta cutoff destroys; it supplies no new
sign-forcing invariant that the positive-threshold example violates. In
particular, it does not prove that theta modularity alone forces (2) or (3)
positive. Character amplification could contribute only after a representation
theorem links its actual weighted family estimates to (4) or to a certified
normalized approximation. The present result changes the approximation task;
it does not supply the missing RH-strength arithmetic estimate.

## 6. Small reproducible reconnaissance

Run

```sh
python3 papers/quasi-rh-exponent-descent/numerics/zeta_collision_arithmetic_check.py
```

The [script](../../numerics/zeta_collision_arithmetic_check.py) uses only the
Python standard library and writes a small JSON record to stdout. The saved
[record](../../numerics/zeta_collision_arithmetic_record_20261008.json) records
panel doubling, center values, and floating evaluations of the analytic error
formulas. Simpson quadrature roundoff and discretization are **not enclosed**.

At \(t=1/4\), \(N=6\), the sampled Wronskians at \(x=28,30,40\) are
positive. At \(N=1,x=80,160\), and \(N=2,x=240\), the sampled truncated
Wronskians are negative, in agreement with Proposition 1. These are isolated
sample observations only. The proof of eventual negativity is analytic;
the samples neither prove a full-flow sign nor certify a rectangle.

All three deliverables are small source/record files and produce no large
derived data, in accordance with the repository's `LARGE_FILES.md`.
