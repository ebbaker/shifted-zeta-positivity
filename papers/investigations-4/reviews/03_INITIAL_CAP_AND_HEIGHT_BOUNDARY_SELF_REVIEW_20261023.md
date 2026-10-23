# Review of the initial cap and height boundary estimates

23 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra**, effort
**max**. The reviewer is the same assistant that derived the results.
This is self-review, not separate-agent or independent specialist review.

**Assessment: accept the stated in-note scope.** [Note 11][note] gives
an exact initial real-angular cap formula, an explicit initial
multiplicity correction, canonical positive-time wall asymptotics and
a relative bound on later real creation events. Its high-height input is
the cited Polymath theorem and proof, not a new theta saddle theorem.
No estimate of the entire 0<t<T birth count or of all physical
complex-time closures is entered as complete. The maintained manuscript
has not been expanded or rebuilt for this research note.

## Mathematical checks

1. **Initial observable.** I_R is twice manuscript B(t), with density
   (H_x^2-H H_xx)/(pi(H^2+H_x^2)). The sign gives a positive contribution
   for an ordinary real zero. At an initial order-m zero its cancelled
   density has limit 1/(pi m). It counts distinct initial locations,
   with an endpoint phase, rather than initial multiplicity.

2. **Endpoint defect.** Principal arctangent jumps are pi at every
   distinct zero, including even multiplicity. The positive-time local
   heat splitting creates m real descendants. Thus I(0+)-I(0)=sum(m-1),
   with no assumption of initial simplicity. The distributional claim
   follows by integration by parts against a smooth test and bounded
   convergence of arctangent. It is not a formula for an unspecified
   three-dimensional endpoint indentation.

3. **Signs and creation weights.** Positive right-wall crossing means
   entry, so N_T=N_distinct,0+D_0+B+W and I_0=N_T-D_0-B-W+E_0.
   Births are weighted by 2 floor(m/2); event number is at most B/2.
   Using a lower bound on I_0 and on W, an upper on N_T, E_0<1/2,
   and D_0>=0 gives the upper bound (7) in the correct direction.

4. **Source verification and normalization.** [Polymath][poly],
   Theorem 1.5, was read in full, along with Proposition 9.1,
   Lemma 9.2 and the proof of Theorem 1.5(i)-(iii). Its field agrees
   with H=integral exp(tu^2) Phi(u) cos(zu) du and H_0(z)=xi(1/2+iz/2)/8.
   Counts use positive Re z, not both symmetric halves. This pays the
   coefficient (T-delta)/16 in the wall main term. R is twice zeta height.

5. **Wall asymptotic.** For t>=delta>0 and sufficiently large R, every
   root on Re z=R is real and simple. No zero can cross Re z=0 because
   the cosh integral is positive. The |Im z|<=1 strip excludes crossings
   of the auxiliary horizontal boundaries at +/-2. Hence the change of
   the *complex* count equals the real wall crossing count, with no
   creation term: complex multiplicity is conserved through collisions.
   Subtraction of the two g asymptotics yields (8). The remaining finitely
   many nonreal zeros at fixed T do not affect N_T(R)~R log R/(4 pi).

6. **Uniform barrier localization.** The headline root-location error
   O(x^(-ct)) alone is insufficient for a uniform half-integer barrier
   when delta tends to zero: multiplication by log x can destroy the
   needed phase accuracy. The proof following equation (104) explicitly
   gives O(x^(-ct)/log x). With g_x comparable to log x this gives
   |g(root,t)-integer|<=C x^(-ct), uniformly. Taking x comparable to
   exp(A/delta), with A sufficiently large, makes this smaller than 1/4
   for all t>=delta. This step is retained in the note.

7. **Barrier speed and population.** Implicit differentiation of the
   explicit g, not of a root asymptotic, gives (10) and speed magnitude
   less than pi/4. The wall moves by less than pi/8 over [delta,T],
   remains above all event thresholds and has zero crossing count.
   The finite complex population is constant and O(delta^(-1)exp(A/delta)).
   Real births consume its initially nonreal part; neither repeated
   counting of spatial events nor growth of the outer cutoff creates
   extra population. Initial or terminal real events are handled by
   one-sided regular slices. The sharper count uses K_{T^-} when the
   terminal slice is singular, because the event at T is excluded.
   For the additional all-future bound, the classical all-real property
   at t>=1/2 rules out later events by local splitting. A possible event
   at 1/2 is included through its terminal multiplicity, giving total
   later births equal to K_delta, without a simplicity assumption there.

8. **Shrinking time interval.** Substitution delta_R=A/(alpha log R)
   gives an O_alpha(R^alpha log R) bound for all positive-height events
   after delta_R and hence relative O_alpha(R^(alpha-1)). This uses
   constants uniform in delta. The interval 0<t<=delta_R remains
   unestimated. Relative progress is recorded as such; no uniform
   extension to t=0 or absolute exclusion follows.

9. **Original physical cap.** The product of the root derivatives is
   (-1)^(m(m-1)/2) Delta_P product_j U(tau,z_j). The cap formula uses
   continuous phase or d log of this complete product. The tube radii
   must share one fixed projective modulus for the common coefficient
   k. The imaginary-time faces telescope with the real-time caps of an
   event-free tube. Attaching an event core retains all other faces.
   Real-event weights floor(m/2), complex weights binom(m,2), and the
   two differently dimensional initial integrals are not identified.

## Checks and remaining work

[The check script][script] uses only the Python standard library and
passed 17 floating diagnostics. The largest reported discrepancy was
6.72e-11 or less. They cover delayed doubles and triples, initial orders
2 through 8, both entry and exit wall signs, complex root-derivative
products with a nonconstant exterior factor, and implicit barrier speed.
[The record][checks] contains the actual maximum and script SHA-256.
These are sign/algebra diagnostics, not interval certificates or theta
computations; the analytic proof and imported theorem carry the claims.

The remaining useful tasks are the early layer, lower initial-integral
bounds, explicit high-height constants, and the complete complex-time
phase estimate. Polynomial and cosine controls pass the generic
identities. The broader collision controls' failed canonical-source
premises are listed in the note; none is assigned the Polymath asymptotic
merely from shared heat flow or positivity. No manuscript or exclusion
gate is upgraded by these checks.

[note]: ../notes/11_INITIAL_CAP_FUTURE_BIRTHS_AND_HEIGHT_BOUNDARIES_20261023.md
[poly]: https://arxiv.org/html/1904.12438
[script]: ../numerics/check_initial_cap_height_20261023.py
[checks]: ../numerics/INITIAL_CAP_HEIGHT_CHECKS_20261023.json
