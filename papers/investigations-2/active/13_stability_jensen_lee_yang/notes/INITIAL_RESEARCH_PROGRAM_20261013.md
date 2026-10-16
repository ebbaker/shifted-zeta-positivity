# Initial research program for stability jensen and lee yang preparation

13 October 2026. Prepared for Edward Baker with substantial LLM assistance.
Model: `gpt-6.1-sol`; reasoning effort: ultra.
Status: initialized, awaiting Claude review. No inverse spin fit, stable
symbol computation or new hyperbolicity certificate is reported here.

This project develops [brainstorm card 13](../../../brainstorm/LIFTED_THETA_SYMMETRY_SEARCH_CODEX_20261013.md).
The missing input is constructive preparation of the actual theta source
by admissible operations, rather than an assumed real-zero input.

## Actual state coefficients and heat observation

Take the complete even extension of
\[
\Phi(u)=\sum_{n\ge1}(2\pi^2n^4e^{9u}-3\pi n^2e^{5u})
e^{-\pi n^2e^{4u}},\qquad u\ge0.
\]
Then \(m_t=e^{tu^2}\Phi_e\), \(\mathscr Gm=u^2m\), and
\(H_t(x)=\frac12\int e^{ixu}m_t(u)du\), with
\(\partial_tH=-\partial_x^2H\). Let
\[
I_{2k}(t)=\int_0^\infty u^{2k}e^{tu^2}\Phi(u)du,
\quad a_k=I_{2k}/(2k)!,\quad \gamma_k=k!a_k.
\]
The entire function \(F_t(w)=H_t(i\sqrt w)=\sum a_kw^k\) is well defined
independently of the square-root branch. Its coefficient Toeplitz matrix
uses \(a_k\), while Jensen polynomials use
\(\sum_{j=0}^d\binom dj\gamma_{n+j}s^j\). Mixing these factorial
normalizations changes the target.

## Established seeds and objective

[Borcea–Branden](https://arxiv.org/abs/0809.0401v3) characterize stability
preservers; their hypotheses must be matched to both symbol and input.
[The effective xi Jensen results](https://arxiv.org/abs/1910.01227v3)
concern each fixed degree at sufficiently large coefficient shift. They
do not settle all degrees, physical-height jets, or positive-time uniformity.

Seek a source-selected stable preparation with paid complex-compact
convergence to \(H_t\), or a narrower construction proving hyperbolicity of
\[
H+2H_xs+H_{xx}s^2,\qquad H_x+2H_{xx}s+H_{xxx}s^2.
\]
Their discriminants yield the two
[physical stationary signs](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/17_enlarged_state_transport/notes/5_STATIONARY_SIGN_CRITERION_AND_THETA_TARGETS_20261010.md).
Full time and predecessor-neighborhood coverage remains necessary.

The spin alternative uses known elementary spins, positive amplitudes
\(S=\sum a_i\sigma_i\), and exponent \(\sum_{i<j}J_{ij}\sigma_i\sigma_j\)
with \(J_{ij}\ge0\). Weighting by \(e^{tS^2}\) adds exactly
\(2ta_ia_j\) to each pair coupling. An admissible limit must preserve that
law and differentiated complex-field convergence. The
[Lee–Yang theorem](https://arxiv.org/pdf/1205.6643) requires independently
admissible elementary transforms; assigning that property to the unknown
theta measure assumes the crucial input.

## First bounded task checks and stopping condition

Choose one branch before computation: one untested preparation symbol, a
small list of coefficient Toeplitz minors using fully enclosed entries, or
a fixed unequal-amplitude ferromagnetic family matched through moments
2, 4, 6 and 8. Record every source operation, parameter domain and payment.
Compare with the positive collision control and verify heat compatibility.
Do not refit spin parameters independently at each time.

Ordinary source-density PF positivity is excluded: the
[reciprocal-transform theorem](https://math.iisc.ac.in/~khare/papers/TN-note.pdf)
would make the bilateral Laplace transform zero-free on the Fourier axis,
contradicting known real zeros of the genuine source. Coefficient Toeplitz
positivity is a different, RH-strength global target. Generic Hankel moment
positivity gives neither. Do not set uncomputed high coefficients to zero;
Taylor sections can lose real-rootedness independently of the full function.

Continue only after an admissible source operation or a concrete structural
obstruction is identified. Stop if preservation assumes an already stable
theta input, or evidence consists only of finite moment agreement. The
[existing spin scout](../../../../quasi-rh/quasi-rh-exponent-descent/newman_collisions/15_lee_yang/notes/1_THETA_MOMENT_ENCLOSURE_AND_FERROMAGNETIC_SPIN_SCREEN_20261010.md)
already excludes its equal-weight families. Unequal weights remain unproved
possibilities. Real-zero location and simplicity are separate obligations;
Lee–Yang alone does not exclude repeated boundary zeros.
