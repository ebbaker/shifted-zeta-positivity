# BW-13 nodal-period self-review

21 October 2026, America/New_York. Prepared for **Edward Baker** with
substantial LLM assistance. Actual recorded model **gpt-6-astra (Codex)**,
reasoning effort **max**.

**Same-assistant self-review of [Note 01][note].** This is not a separate
agent, independent review, cross-model review, or specialist assessment.

## Assessment

The local fixed-boundary calculation is internally consistent. It supplies
an explicit finite time/disk contract, pays transport and source errors,
and identifies the first correction with an existing four-jet quantity.
It does not supply an opposing theta inequality or a numerical theta
certificate. The scope of the stopped comparison is the first coefficient
calculated from the same event four-jet; finite non-asymptotic periods and
different source information remain open.

The written proof carries these conclusions. The seven rational controls
and fourteen floating contour rows are transcription and convention checks,
not independent proof or interval certification.

## Checks made

1. **Normalization and sign.** The source agrees with BW10's manuscript
   and satisfies \(H_t=-H_{zz}\). The vanishing cycle is the negative
   lifted counterclockwise boundary. For \(H=x^2-2\tau\) this gives
   \(P=2\pi i\tau\) and \(Q=-2\pi i\), matching proposal C4.
   The constant normalizer is \(\sqrt{h_2/2}\), with either branch
   allowed. For a general germ \(P'=-Q\) is false and is not used.

2. **Regular finite family.** The explicit radius choices imply the
   boundary relative change is at most \(1/2\). Rouché therefore preserves
   the two-zero count. A separate stationary-point argument is essential:
   boundary regularity alone would not exclude additional interior
   critical times. Note 01 supplies it through
   \(|H_{zz}-2A|\le|A|/2\) and
   \(|v(\tau)+2A\tau|\le|A||\tau|/2\).
   Thus every nonzero time in the stated disk has two simple branches.

3. **Moving endpoints and outer boundary.** The closed-lift transport
   term is an exact parameter derivative with zero total integral.
   The first open-cut endpoint term vanishes because \(w=0\), but
   higher open-cut derivatives cannot be taken by discarding divergent
   endpoints. Those derivatives are taken on the regular fixed contour.
   The outer boundary is retained as the observable itself.

4. **Residue coefficient.** With \(h=Ax^2+Bx^3+Cx^4+\cdots\), the residue
   in \(P''\) is \(3C/(2\sqrt A)-15B^2/(8A^{3/2})\).
   Dividing the Taylor term \(P''\tau^2/2\) by \(2\pi i\sqrt A\)
   gives \(15B^2/(16A^2)-3C/(4A)\).
   Substituting \(A=h_2/2,B=h_3/6,C=h_4/24\) gives the stated
   \((5h_3^2-3h_2h_4)/(48h_2^2)\). The factorial 2 in the
   time Taylor coefficient is included. Formula (19)'s residue degree
   proves the stated spatial \(2n\)-jet dependence.

5. **Complete remainder.** Three time derivatives of \(\sqrt H\)
   require spatial derivatives through order six. The \(M_6\),
   \(M_2M_4\), and \(M_2^3\) terms have the correct respective boundary
   denominators \(m^{1/2},m^{3/2},m^{5/2}\). Multiplying the contour
   length, dividing by \(3!\), and normalizing yields exactly \(C_3\).
   It is uniform on the stated finite disk and can be very conservative.

6. **Source tails.** For \(u\ge0\) every summand in (3) is positive.
   The ratio bound uses
   \(((n+1)/n)^4e^{-\pi(2n+1)e^{4u}}
      \le16e^{-\pi(2N+3)}\) for \(n\ge N+1\).
   The outer-tail log second derivative is
   \(-j/u^2+2B-16\pi e^{4u}\le0\), proving the exponential integral
   bound when the stated \(\lambda_j\) is positive. The finite index
   and outer tails cover disjoint omitted pieces; quadrature/rounding
   is still a separate payment. No numerical source truncation is
   presumed to satisfy the event equations.

7. **Control strength and limits.** The even control
   \((z^2-a^2)^2\) has two double endpoints and four simple real roots
   for every positive heat time, with positive correction
   \(3/(4a^2)\). This is an exact counterexample to exclusion from that
   correction's positivity plus the stated polynomial properties.
   It does not have the unchanged theta source. The inherited
   BW-08 floor is a necessary condition, not an established
   contradiction. Finite-source controls are not assigned all-real
   time slices. The cubic's two nonreal-time events remain separate
   from its one physical event.

8. **Comparison scope.** The exact admissible-image equality uses
   precisely the same event four-jet information on both sides.
   Formula (18) includes uncertain normalization.
   Formula (13) assumes exact normalization and explicitly says so.
   Nothing proved here compares all possible interval implementations,
   computation costs, multi-cycle observations, or correlated source
   estimates. In particular, the bounds do not justify closing BW-13.

## Reproducibility and remaining limitations

Run from this investigation:

    python3 numerics/check_nodal_period.py \
      --output /tmp/NODAL_PERIOD_CHECK_20261021.json

The script uses only the standard library. Its [receipt][receipt] keeps
exact fractions separate from floating diagnostics and identifies the
script by SHA-256. The floating contour values are not rounded outward;
a second grid comparison is not a rigorous quadrature error estimate.
The moment-tail bounds are analytically proved in the note but have not
been exercised in a theta acquisition.

No change to the BW10 manuscript, HMC-05, or HMC-06 follows. A future
theta pilot needs a specified bounded observation, a source estimate
outside the same-four-jet class, and a matched direct comparator.
Higher multiplicity and height exhaustion remain gated.

This review applies the [result index][results] and [avoid index][avoid],
especially [same-model review limits][a05], [normalization][a08],
[control matching][controls] and [scoped exclusions][a07].

[note]: ../notes/01_NODAL_PERIOD_VARIATION_AND_FOUR_JET_COMPARISON_20261021.md
[receipt]: ../numerics/NODAL_PERIOD_CHECK_20261021.json
[results]: ../../../../../../../result-summaries/README.md
[avoid]: ../../../../../../../avoid/README.md
[a05]: ../../../../../../../avoid/05_same_model_reviews_and_shared_premises.md
[a08]: ../../../../../../../avoid/08_normalization_and_constant_slips.md
[a07]: ../../../../../../../avoid/07_scoped_exclusions_read_as_universal.md
[controls]: ../../../../../../../result-summaries/12_collision_controls_and_screening.md
