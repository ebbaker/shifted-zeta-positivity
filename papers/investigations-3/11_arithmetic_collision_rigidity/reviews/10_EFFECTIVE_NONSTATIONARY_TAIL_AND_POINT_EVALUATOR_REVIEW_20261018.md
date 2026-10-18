# Review of the effective nonstationary tail and retained point evaluator

18 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. **GPT-6.1 Sol (`gpt-6.1-sol`), actual effort
ultra**. This is internal review by the contributing assistant, with
parallel same-model derivation and implementation checks. It is not
independent specialist review.

**Disposition:** no blocking mathematical defect found in the reviewed
[Note 11](../notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md)
proof chain or the scoped point-evaluation error contract. The earned
result is an effective arithmetic approximation estimate and measured
point evaluation, with the global physical margin still open.

## Proof checks

The phase derivative of each upper source monomial is
`x+2td-4*pi*n^2*sin(4d)*exp(4u)`. Its negative is strictly positive
and increases under the new explicit phase-gap condition. The amplitude
is decreasing and log-concave under the existing time/decay conditions.
The degree-nine and degree-five monomials have different constant phases
but the same phase derivative; their coefficient signs are paid in the
absolute tail bound.

The integration-by-parts identity combines the variation terms as
`-(g(u+d)^j/p)' + 2j*g(u+d)^(j-1)/p`. This proves the stated Q_j
without requiring `g(u+d)^j` to decrease and without a Cauchy derivative
loss. Both lower/upper contour polynomial factors are retained. Boundary
terms at zero are paid twice in the bound; remote boundaries vanish by
the complete-source decay. The phase coefficient has no unpaid time
term proportional to u: the imaginary part of t(u+id)^2 differentiates
to the constant 2td. Complex spectral imaginary parts enter the amplitude
and are paid by Y. Derivatives freeze the contour and cutoff.

The Gaussian tail is bounded by a first term and an integral. Its
`n^2` monotonicity needs q>=1, which is checked. The proof of the uniform
phase coefficient uses n^2>=b_*x and pays 2Td with n^2>=b_*X. Every
term of C_X, including the ceiling correction M, has the stated power and
coefficient. Monotonic log(x)/sqrt(x) substitutions are valid at X>=e^2.
The precise asymptotic exponent uses the varying sine remainder and
ceil(sqrt(b_*x)) error, rather than treating a fixed kappa<1 as a
vanishing error. This removes the older extra asymptotic condition for
this improved arithmetic estimate only.

## Interval and implementation checks

The 192-bit scalar replay verifies all sufficient conditions for the
three stated uniform examples and directly compares the Gaussian frozen
bounds with the uniform envelope at each onset, its successor and twice
the onset. The primary onset value is below 1.273826e-9 G0, supporting
the stated strict 2e-9 bound for all x>=1000, 0<=t<=1/2, |Im z|<=1
and j=0,1,2. Four actual frozen parameter choices are rejected at their
failed premise: phase gap, amplitude decay, zero shift and strip boundary.
These checks verify arithmetic; the analytic proof covers the unbounded
height range.

The 160-bit point evaluator uses exact integer ceiling selection for its
two fixed heights. Its normalized spectral factor is x^(9/4) at d and
x^(9/4)*e at d-1/x. All source modes are assembled in the integrand;
the real part supplies the exact reflected pair for real t,x. Derivative
factors are (i(u+id))^j. Quadrature pays internal rounding and the large
imaginary contour integral; an imaginary integral is not discarded as
an error estimate. Explicit tangent/concavity inequalities pay the
retained-source cutoff, and the original manuscript tail pays omitted
modes. The new IBP tail is only an additional diagnostic in these point
certificates.

Every saved component has total normalized added error below 1e-8:
less than 2.527e-12 at x=1000, 2.708e-12 for its second contour, and
3.737e-11 at x=10000. All three replayed contour enclosures intersect.
Recorded case costs are approximately 0.581 s, 0.568 s and 14.37 s,
with 10277, 10145 and 83022 callbacks. Costs include setup and all three
integrals and remain within declared case caps. They establish no
complexity law or matched performance gain; there is no whole-cell
propagation in this point contract.

The fresh 192-bit control interface replays the original source-specific
certificates and rejects all five surrounding event boxes. The genuine
Euler-factor negative-Laguerre witness separately rejects the signed gate.
The analytic premise screen names the complete reflection or unchanged
normalized theta square-source contract absent from each control class.
No theta mode-tail constants are substituted into a control source.

## Source identities and remaining scope

The reviewed artifacts have these SHA-256 identities. The checked
manuscript source-set pin remains `f6cd484647ef328047e9ac51a577b8260e899aecbfdd5026e9e238079feb823f`;
all eight source hashes still match its build record. This supplement
has not been integrated into that manuscript.

| Artifact relative to the investigation | SHA-256 |
| --- | --- |
| `notes/02_updated_research_plan/11_EFFECTIVE_NONSTATIONARY_ARITHMETIC_TAIL_20261018.md` | `a36b9c51ebd54c56a6470a7d8cbf485354a7647cb6afa39bccaa2b46b3990c40` |
| `numerics/certify_nonstationary_mode_tail.py` | `88bc7436b74a372136920f932d33ccc64ef103fddc1f6c76e6992350f2aff4f8` |
| `numerics/EFFECTIVE_NONSTATIONARY_TAIL_20261018.json` | `bdfb43f80f412657f4f18be16c6c8d3125a93cf3ccc6c34b74faec3131031b3a` |
| `numerics/bounded_near_boundary_evaluator.py` | `b7324e16ab3e586d12b3fdfc1d9475cda0e1f63b273e64f5046949607962ccdb` |
| `numerics/NEAR_BOUNDARY_POINT_EVALUATION_20261018.json` | `a2d6da749daca3712f2da7ad098f2e524f472be6b9fe535bb81372ded0b4cd0f` |
| `numerics/replay_nonstationary_controls.py` | `c8f95dbac1f84632091c314da57a2382c077d0a0c1a6738d92494f4f95681da6` |
| `numerics/NONSTATIONARY_CONTROL_REPLAY_20261018.json` | `b1ec1945b710be241796396b35ebaf439ff4d5f8a3a8188d5c03fd1f41b7b00a` |

Each computation also binds its consumed analytic source/code hashes and
actual configuration. Source-hash checks were repeated against the current
repository; the records and code identities above match. The earlier
bounded round and its failed performance gate retain their original scope.
The global finite bridge in Note 10, a uniform signed physical margin,
and an effective exterior nonvanishing consumer remain unclosed. The
new approximation theorem does not establish a Newman bound.
