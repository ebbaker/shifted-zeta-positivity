# Square support plus complete reflection is rigid

15 October 2026. Prepared for Edward Baker with substantial LLM assistance. Recorded coordinating model **gpt-6-astra**, reasoning effort **ultra**, verified from the current session. This is an elementary analytic derivation and a scope check for the arithmetic relaxation; no literature-novelty or theta-sign claim is made. The proof was independently checked by the connection-bridge collaborator.

The square-support experiment admits positive weighted sources with a positive-time collision. That obstruction does not extend to the intersection of square support and the complete theta reflection identity. Under a mild coefficient-growth assumption, that intersection contains only scalar multiples of the ordinary theta series. Correct primitive normalization fixes the scalar. This identifies a missing relation; it does not establish positivity of the associated physical transform.

## 1. Precise class

Let `(a_n)_(n in Z)` be an even sequence of complex numbers of at most polynomial growth. Define, for `q>0`,

\[
 F_a(q)=\sum_{n\in\mathbb Z}a_n e^{-\pi n^2q}.
\]

The series and each fixed derivative converge locally uniformly on `Re(q)>0`. Suppose

\[
 \boxed{F_a(q)=q^{-1/2}F_a(1/q)\quad(q>0).}
 \tag{1}
\]

Then every coefficient equals `a_0`:

\[
 \boxed{a_n=a_0\quad(n\in\mathbb Z).}
 \tag{2}
\]

Positivity of the coefficients is unnecessary for this rigidity statement. Evenness and polynomial growth are explicit hypotheses. The latter makes the weighted integer comb a tempered distribution; a broader growth class would require a different argument.

The usual theta reflection formula is recorded in [DLMF 20.7.32](https://dlmf.nist.gov/20.7.E32). The converse within the stated coefficient class is proved directly below, rather than inferred from that formula or from a dimension count for modular forms.

## 2. Gaussian uniqueness for even tempered distributions

Use the Fourier convention `hat f(xi)=int f(x)exp(-2*pi*i*x*xi)dx`. Put

\[
 \mu=\sum_{n\in\mathbb Z}a_n\delta_n,\qquad
 \nu=\mu-\widehat\mu.
\]

Both distributions are tempered and even. The Fourier transform of `g_q(x)=exp(-pi*q*x²)` is `q^(-1/2)g_(1/q)`. Thus (1) implies

\[
 \langle\nu,g_q\rangle=0\quad(q>0).
 \tag{3}
\]

Differentiating at `q=1` in the Schwartz topology gives

\[
 \langle\nu,x^{2k}e^{-\pi x^2}\rangle=0\quad(k\ge0).
\]

Odd Gaussian moments vanish by evenness. The function

\[
 G(z)=\langle\nu,e^{-\pi x^2+zx}\rangle
\]

is entire: on every compact set of `z`, the test function and all its `z` derivatives are Schwartz functions with uniform bounds for each Schwartz seminorm. Every derivative of `G` at zero vanishes, hence `G` is identically zero.

On `z=-2*pi*i*xi`, this is the Fourier transform of `e^(-pi*x²)nu`. Fourier injectivity gives `e^(-pi*x²)nu=0`. Local division by the nowhere-zero Gaussian, using compactly supported smooth tests, gives `nu=0`. Therefore

\[
 \mu=\widehat\mu.
 \tag{4}
\]

No unproved completeness of a finite moment list is being used. The argument requires all Gaussian moments, obtained from the functional identity on an open interval of positive `q`.

## 3. Integer support forces constant weights

The Fourier transform of an integer-supported comb is a period-one distribution:

\[
 \widehat\mu(\xi)=\sum_{n\in\mathbb Z}a_n e^{-2\pi i n\xi},
 \qquad \widehat\mu(\xi+1)=\widehat\mu(\xi).
\]

The Fourier series is interpreted distributionally, with polynomial coefficient growth sufficient for convergence in that sense. By (4), `mu` is also period one. Testing against smooth functions supported near individual integers shows `a_(n+1)=a_n` for every integer `n`, proving (2).

There is a second direct discriminator when the elliptic variable is retained. For

\[
 \Theta_a(z,\tau)=\sum_n a_n e^{\pi i n^2\tau+2\pi i nz},
\]

elliptic translation `z -> z+tau` with the standard theta multiplier is equivalent, after reindexing, to the same recurrence `a_(n+1)=a_n`. Period two in `tau` and the Jacobi heat equation hold for arbitrary fixed coefficients and do not impose this recurrence. The standard quasi-periodicity convention appears in [DLMF 20.2](https://dlmf.nist.gov/20.2); our `z` has period one, so it corresponds to DLMF's elliptic argument divided by `pi`.

## 4. Physical source evenness and the primitive endpoint recover reflection

Set `a_0=1`, let `q=e^(4u)`, and define on the whole real `u` axis

\[
 \psi_a(u)=e^u\sum_{n\ge1}a_n e^{-\pi n^2e^{4u}},\qquad
 P_a(u)=e^u+2\psi_a(u)=e^uF_a(e^{4u}),
\]
\[
 \Phi_a(u)=\frac{\psi_a''(u)-\psi_a(u)}8
          =\frac{P_a''(u)-P_a(u)}{16}.
 \tag{5}
\]

These functions are real analytic along the whole real axis by local uniform convergence. If

\[
 \Phi_a(-u)=\Phi_a(u),\qquad \psi_a'(0)=-\frac12,
 \tag{6}
\]

then `R(u)=P_a(u)-P_a(-u)` satisfies `R''-R=0`, `R(0)=0`, and

\[
 R'(0)=2P_a'(0)=2[1+2\psi_a'(0)]=0.
\]

Hence `R=0`, which is precisely (1), and the rigidity theorem gives `a_n=1` for every `n`.

For reference, without either assumption in (6), the exact defect identity is

\[
 \boxed{R(u)=2P_a'(0)\sinh u
 +16\int_0^u\sinh(u-v)[\Phi_a(v)-\Phi_a(-v)]\,dv.}
 \tag{7}
\]

The oriented integral also gives the formula for negative `u`. This retains the homogeneous endpoint contribution explicitly. Source evenness alone leaves a homogeneous freedom because the differential source operator annihilates the `n=0` term. The primitive normalization removes that freedom.

Equivalently, all odd source derivatives at zero, together with the primitive endpoint, force (6): real analyticity makes the odd part vanish near zero and then on the connected real axis. A finite number of endpoint constraints does not supply that identity.

## 5. Scope of the weighted collision obstruction

For positive weights, the physical half-line source is

\[
 \Phi_a(u)=\sum_{n\ge1}a_n e^u
 [2\pi^2n^4e^{8u}-3\pi n^2e^{4u}]e^{-\pi n^2e^{4u}}.
\]

It is positive for `u>=0`. Its cosine transform is even in the spectral variable `x`, regardless of whether the source is even in `u`. These two evenness statements must not be confused.

Moreover

\[
 \psi_a'(0)=\sum_{n\ge1}a_n(1-4\pi n^2)e^{-\pi n^2}<0.
\]

A common positive rescaling can enforce `psi_a'(0)=-1/2` without changing collisions or square-support inequalities. Thus retaining the one primitive boundary constant does not repair the relaxation. The weighted collision control still fails the complete source reflection hierarchy.

For a nonzero finite set of nonnegative weights, failure of source evenness is also immediate without computing an endpoint derivative. As `u -> -infinity`,

\[
 \Phi_a(u)=-3\pi e^{5u}\sum_{n\ge1}a_n n^2+O(e^{9u}),
\]

which is negative for sufficiently negative `u`, while `Phi_a(u)>0` for `u>=0`. Its even extension from the half-line is a different function. The certified three-mode control retains the first odd source derivative and fails at the third.

The [square-support collision control](01_SQUARE_SUPPORT_ENDPOINT_COLLISION_OBSTRUCTION_20261015.md) therefore rejects certificates using only square-support localizers, positivity, period two and Jacobi heat, even if the primitive endpoint is normalized. It does not reject a certificate using full modular reflection or elliptic quasi-periodicity. Conversely, uniqueness of the input under these stronger relations is not a positive signed representation of its transform.

## 6. Implication for the next certificate

Adding more support-gap localizers cannot remove a control that passes every such localizer. The next finite relaxation must also couple coefficients across the lattice, or encode a quantified part of reflection with its complete boundary terms. It must then show that this additional relation improves the actual chord or stationary signed observation. Merely forcing a finite model to resemble theta, or paying its error by an absolute source norm, supplies no uniform control near small physical energy.

The accompanying [exact checker](../../numerics/check_weighted_reflection_algebra.py) verifies the source differentiation polynomials and the endpoint recurrences with rational arithmetic. It checks finite identities only; the tempered-distribution uniqueness and reflection arguments are the analytic proofs above.
