# Factoring the large-time field and propagating its zeros

20 November 2026. Prepared for Edward Baker with OpenAI Codex LLM assistance. The desktop chat records the model setting gpt-6.2-astra and reasoning effort max. The public archive supplies no separate per-turn configuration.

**Research question.** Can the nearly equally spaced zeros at large positive Newman time supply exact data for propagation to an earlier time? There are two constructive answers. An explicit phase gives an exact cosine product on a growing real interval. The global product over the true zeros also propagates as a convergent limit of polynomials. The distinction matters already for the mass at the origin, where the manuscript's first two Jacobi links measure exactly what a frozen cosine loses.

These are representation identities and a quantitative test of one approximation in an already all-real regime. The signed gap estimate at earlier time remains open. The project records the relevant precedents in the [result index](../../../../../../result-summaries/README.md), [heat-flow cluster](../../../../../../result-summaries/11_newman_heat_flow_reductions_and_certificates.md), [patterns index](../../../../../../avoid/README.md) and [criterion classification](../../../../../../avoid/01_restating_the_target.md).

## 1. What crystallizes

Write \(Z(T)=H(T,0)\) and \(F(T,z)=H(T,z)/Z(T)\). Let \(U\) have the **positive-half-line** probability law

\[
 d\nu_T(u)=Z(T)^{-1}e^{Tu^2}\Phi(u)\,du,\qquad u\ge0 .
\]

Then \(F(T,z)=\mathbb E_T\cos(zU)\). Its even moments \(m_{2j}\) agree with those of the manuscript's symmetric measure. Use the large solution \(L=L_T\) of \(4\pi e^{4L}=2TL+9\), and put \(\kappa=8TL-2T+36\). The earlier saddle calculation gives \(L\sim(\log T)/4\), and \(\sqrt{\kappa}(U-L)\) converges to a standard normal with convergence of each fixed moment. In particular, on bounded real \(w\)-intervals and for each fixed positive zero index \(k\),

\[
 F(T,w/L_T)\longrightarrow\cos w,\qquad
 L_T x_k(T)\longrightarrow q_k,\qquad q_k=(k-\tfrac12)\pi .
\]

The index is fixed as time increases. The sibling manuscript also treats growing spatial windows with explicit moment hypotheses. [Fixed-index saddle proof, equations (8)–(13)](../../../../../investigations-3/13_contradiction_analysis/04_boundary_winding/threshold_routes/09_expanding_contour_later_collision/brainstorm/01_CAP_AT_INFINITY_20261020.md) · [Positive-time carrier estimates](../../../../../investigations-5/01_heat_density_asymptotics/manuscript/03_positive.tex)

At any sufficiently large finite \(T\), all zeros are real. Evenness, order at most one, \(F(T,0)=1\) and inverse-square summability give the exact, locally uniformly convergent product

\[
 F(T,z)=\prod_{k\ge1}(1-b_k z^2),\qquad b_k=x_k(T)^{-2},
\]

with positive zeros counted with multiplicity. If the complete divisor were exactly the simple half-integer lattice of frequency \(\lambda\), this product would be \(\cos(\lambda z)\). Matching the curvature at zero forces \(\lambda^2=m_2=\beta_1\). This cosine is exactly the manuscript's two-site Jacobi readout \(G_2\), since \(J_2\) has eigenvalues \(\pm\sqrt{\beta_1}\) with equal weights. At fourth order the Jacobi recurrence gives \(m_4=\beta_1^2+\beta_1\beta_2\), hence

\[
 F(T,z)-\cos(\sqrt{\beta_1}\,z)
     =\frac{\beta_1\beta_2}{24}z^4+O_T(z^6),\qquad
 \beta_1\beta_2=\operatorname{Var}_T(U^2)>0 .
\]

Strictness follows from the positive continuous density on the half-line. This excludes that exact global lattice at every finite all-real anchor. [Jacobi recurrence](../../manuscript/sections/source.tex) · [Manuscript product argument](../../manuscript/sections/hierarchy.tex) · [Polymath, introduction and Theorem 1.1](https://arxiv.org/pdf/1904.12438v2#page=2) · [Cosine product, DLMF 4.22.2](https://dlmf.nist.gov/4.22.E2)

## 2. An exact factorization with the lattice in the phase

Set \(a=\mathbb E_T U\), \(\sigma^2=\operatorname{Var}_T U\), and form a transform of the fluctuations around the positive saddle,

\[
 C_T(z)=\mathbb E_T e^{iz(U-a)} .
\]

For real \(x\) on an interval around zero where \(C_T\ne0\), take its continuous argument starting at zero. Define \(A_T(x)=|C_T(x)|\) and \(\Theta_T(x)=a x+\arg C_T(x)\). Taking the real part of \(e^{iax}C_T(x)\) gives

\[
 \boxed{\displaystyle
 F(T,x)=A_T(x)\cos\Theta_T(x)
       =A_T(x)\prod_{k\ge1}\left(1-\frac{\Theta_T(x)^2}{q_k^2}\right).}
\]

All inputs come from the specified theta density. The factors require no prior zero locations. A concrete interval is \(|x|\le1/\sigma\). Centering and \(|e^{iy}-1-iy|\le y^2/2\) give \(|C_T(x)-1|\le x^2\sigma^2/2\), hence \(A_T\ge1/2\) there. Also \(|C_T'(x)|\le\sigma\), so

\[
 |\Theta_T'(x)-a|\le 2\sigma .
\]

The saddle gives \(a\sim L_T\) and \(\sigma\sim\kappa^{-1/2}\). Thus the interval grows and the phase is strictly increasing there for all sufficiently large \(T\). Each positive \(q_k\) in its phase range labels exactly one simple zero by \(\Theta_T(x_k)=q_k\).

For complex \(z\) the global identity is \(2F(T,z)=e^{iaz}C_T(z)+e^{-iaz}C_T(-z)\). On a simply connected symmetric neighborhood of zero where both transforms are nonzero, set \(K(z)=\log C_T(z)\) with \(K(0)=0\). Then \(A=\exp((K(z)+K(-z))/2)\) and \(\Theta=az+(K(z)-K(-z))/(2i)\) give the same holomorphic factorization. A sufficient disk test of radius \(R\) is \(R^2\mathbb E_T[(U-a)^2e^{R|U-a|}]/2<1\). Near zero, writing \(\gamma_j\) for the cumulants of the half-line law,

\[
 \log A=-\sigma^2z^2/2+\gamma_4z^4/24+\cdots,\qquad
 \Theta=az-\gamma_3z^3/6+\gamma_5z^5/120+\cdots .
\]

The variance controls the leading amplitude correction. The third central moment gives the first possible correction to the linear phase. The exact formula keeps every term. The cumulant series converges within its logarithm disk.

### The first displacement from the two-site lattice

Write \(\epsilon=\sigma/a\) and \(d=\beta_2/\beta_1\). For fixed \(k\), the saddle gives \(x_k=O_k(1/a)\) and \(\mathbb E_T|U-a|^j=O_j(\sigma^j)\) for \(j=3,4\). Centering in the sine integral gives
\(|\Im C_T(x_k)|\le |x_k|^3\mathbb E_T|U-a|^3/6=O_k(\epsilon^3)\).
The real part is at least \(1/2\), so \(a x_k=q_k+O_k(\epsilon^3)\).
Also \(\sqrt{\beta_1}/a=\sqrt{1+\epsilon^2}\). Expanding the variance of \(U^2=a^2+2a(U-a)+(U-a)^2\) gives \(d=\operatorname{Var}(U^2)/(a^2+\sigma^2)^2=4\epsilon^2+O(\epsilon^3)\). Consequently

\[
 \sqrt{\beta_1}\,x_k(T)=q_k(1+d/8)+O_k(d^{3/2}),\qquad
 \frac{D_{F,k}(T)}{D_{2,k}(T)}=1+d/4+O_k(d^{3/2}).
\]

Here \(D_{F,k}=(x_{k+1}-x_k)^2/4\) and \(D_{2,k}=\pi^2/(4\beta_1)\). The second formula follows by subtracting the two fixed-index expansions and squaring. Thus the true squared half-gap exceeds the two-site value for each fixed \(k\) and sufficiently large \(T\). This is a large-time asymptotic for degree two. The manuscript's degree-24 result concerns a different degree and time interval. [Degree-24 calculation in §8](../../manuscript/sections/evidence.tex)

### An approximation in \(T\) and \(k\) alone

The large saddle has the explicit form

\[
 L=-\frac14 W_{-1}\!\left(-\frac{8\pi}{T}e^{-18/T}\right)-\frac{9}{2T}.
\]

For each fixed \(k\), the first shift from \(q_k/L\) can also be evaluated without theta moments. With \(\kappa=8TL-2T+36\),

\[
 x_k(T)=\frac{q_k}{\,L-2(\kappa+2T)/\kappa^2\,}
            +O_k\!\left(\frac{1}{L^2\kappa^{3/2}}\right).
\]

To see the shift, put \(v=U-L\) and use the complete prefactor \(b(u)\) in \(e^{Tu^2}\Phi(u)=2\pi^2 e^{Tu^2+9u-\pi e^{4u}}b(u)\). The sibling manuscript's integrated source derivative gives

\[
 \kappa(a-L)=-\tfrac{\kappa+2T}{4}\mathbb E_T(e^{4v}-1-4v)
              +\mathbb E_T[b'(U)/b(U)]+\Phi(0)/Z(T).
\]

Its moment estimates give \(\mathbb E_T v^2=\kappa^{-1}+O(\kappa^{-3/2})\) and \(\mathbb E_T(|v|^3e^{4|v|})=O(\kappa^{-3/2})\). The explicit prefactor has \(b\) bounded below and \(b'(u)=O(e^{-4u})\). Indeed its first square mode has that derivative bound, and differentiating the higher modes preserves their doubly exponential decay. Thus the middle expectation is \(O(e^{-4L}\mathbb E_T e^{4|v|})=O(\kappa^{-1})\). The endpoint term decays faster than any power of \(\kappa^{-1}\). Taylor expansion of the exponential now gives \(a=L-2(\kappa+2T)/\kappa^2+O(\kappa^{-3/2})\). Substitution into \(a x_k=q_k+O_k((\sigma/a)^3)\) proves the stated approximation. Its leading term is \(q_k/L\sim4q_k/\log T\). [Lambert formula and complete prefactor](../../../../../investigations-5/01_heat_density_asymptotics/manuscript/03_positive.tex) · [Integrated derivative and variance estimates](../../../../../investigations-5/01_heat_density_asymptotics/manuscript/07_explicit_clock.tex) · [Weighted moment bounds](../../../../../investigations-5/01_heat_density_asymptotics/manuscript/05_appendices.tex) · [Lambert \(W\) branches, DLMF §4.13](https://dlmf.nist.gov/4.13)

### An exact integral for the individual zero

Put \(q=q_k\), \(r=1/2\), \(f(w)=F(T,w/L)\), and take the counterclockwise circle \(\Gamma_k=\{|w-q|=r\}\). For each fixed \(k\) and sufficiently large \(T\),

\[
 \boxed{\displaystyle x_k(T)=\frac1L\left(q-\frac{1}{2\pi i}
              \oint_{\Gamma_k}\log\frac{f(w)}{\cos w}\,dw\right).}
\]

The principal logarithm on the circle suffices. The contour and every input on its right are specified before locating any zero. To check the hypotheses at a given \(T\), put \(v=U-L\), \(B=q+r\) and

\[
 \eta=\frac{e^r}{\sin r}\left\{\frac{B\,|a-L|}{L}
     +\frac{B^2}{2L^2}\mathbb E_T\!\left[v^2 e^{r|v|/L}\right]\right\}.
\]

Taylor expansion of \(\cos(w+wv/L)\) with integral remainder gives \(|f(w)-\cos w|\le\eta\sin r\) for \(|w|\le B,\ |\Im w|\le r\). On each circle about \(q_j,\ 1\le j\le k\), of radius \(r\), one has \(|\cos w|\ge\sin r\). This follows from \(|\sin(h+iy)|^2=\sin^2 h+\sinh^2 y\) with \(h^2+y^2=r^2\). If \(\eta<1\), Rouché gives one zero in each disk. It is simple and real by conjugation. Between these disks on \([0,B]\), \(|\cos w|\ge\sin r\) excludes intervening real zeros. The moment bounds above give \(\eta=O_k(1/(\kappa L))\), so the test holds eventually. A double of any of the §5 controls inside one of these disks would violate the strict contour comparison there.

The argument principle expresses \(Lx_k-q\) as \((2\pi i)^{-1}\oint w(f'/f+\tan w)\,dw\). Integration by parts gives the boxed formula. Expanding the logarithm through order \(m\) costs at most \(r\eta^{m+1}/[L(m+1)(1-\eta)]\). Equivalently put \(D(w)=(w-q)(1-f(w)/\cos w)\), with its removable value at \(q\). Taking residues term by term gives the convergent expression

\[
 Lx_k=q+\sum_{n\ge1}\frac1{n!}
       \left.\frac{d^{n-1}}{dw^{n-1}}D(w)^n\right|_{w=q}.
\]

Every derivative uses source integrals at the known real lattice point. The first correction to \(q\) is \((-1)^{k-1}f(q)\). The full formula is exact at finite time inside the stated range. [Manuscript's logarithmic contour comparison](../../manuscript/sections/signed.tex) · [Classical inverse-series formula, DLMF §1.10(vii)](https://dlmf.nist.gov/1.10.vii)

## 3. The true factors can also be recovered from Jacobi data

At an all-real anchor, each reciprocal square in the global product admits a convergent expression in the source moments. Define

\[
 p_n=-n[v^n]\log\!\left(\sum_{j\ge0}
          \frac{(-1)^jm_{2j}}{(2j)!}\,v^j\right)=\sum_{k\ge1}b_k^n .
\]

The equality follows by taking the logarithm of the product near zero. The first \(N-1\) power sums use only data seen exactly by the \(N\)-site Gaussian quadrature. In decreasing order, put \(s_n^{(k)}=p_n-\sum_{j<k}b_j^n\). Then

\[
 b_k=\lim_{n\to\infty}\frac{s_{n+1}^{(k)}}{s_n^{(k)}} .
\]

The ratio is an average of the remaining \(b_j\) with weights proportional to \(b_j^n\). For a separated factor its relative deficit from \(b_k\) is at most
\((b_{k+1}/b_k)^{n-1}\sum_{j>k} b_j/b_k\), by bounding each term of the tail. The base tends to \(((2k-1)/(2k+1))^2\) for fixed \(k\), in particular \(1/9\) for the first factor. This makes the global product explicit as successive limits. High orders require more moments, and subtracting previously recovered factors can lose numerical precision. [Gaussian exactness in §2](../../manuscript/sections/source.tex)

One can remove all earlier zeros from the inputs at a single all-real time \(T\). From the same power sums define \(E_{0,n}=1\) and

\[
 E_{j,n}=\frac1j\sum_{\ell=1}^{j}(-1)^{\ell-1}p_{\ell n}E_{j-\ell,n}.
 \qquad
 \boxed{\displaystyle x_k(T)=\lim_{n\to\infty}
       \left(\frac{E_{k-1,n}}{E_{k,n}}\right)^{1/(2n)}.}
\]

Indeed \(E_{j,n}\) is the coefficient of \(s^j\) in \(\prod_i(1+s b_i^n)\), as follows by logarithmic differentiation. It sums \((b_{i_1}\cdots b_{i_j})^n\) over increasing index tuples. The largest such product before raising to the \(n\)-th power is \(b_1\cdots b_j\). The products are summable for \(n=1\), so \(E_{j,n}^{1/n}\to b_1\cdots b_j\) by bounding the sum between the largest term and \((b_1\cdots b_j)^{n-1}E_{j,1}\). The formula follows including multiplicities. For example \(x_1=\lim p_n^{-1/(2n)}\) and \(x_2=\lim(2p_n/(p_n^2-p_{2n}))^{1/(2n)}\). Each finite approximation uses normalized source moments through order \(2kn\).

## 4. What propagates to earlier time

For \(s>0\) write \(P_s f(z)=\mathbb E f(z+\sqrt{2s}\,G)\), \(G\) standard normal. The sign \(\partial_t H=-\partial_z^2 H\) gives

\[
 H(T-s,z)=P_s H(T,\cdot)(z)
         =Z(T)\mathbb E_T[e^{-sU^2}\cos(zU)] .
\]

The complete zero product really can be used in this formula. With \(B_m(z)=\prod_{k\le m}(1-b_kz^2)\),

\[
 \frac{H(T-s,z)}{Z(T)}
    =\lim_{m\to\infty}\sum_{\ell=0}^{m}
        \frac{s^\ell}{\ell!}\,\partial_z^{2\ell} B_m(z) .
\]

Indeed \(|B_m(w)|\le F(T,i|w|)\). The order-one growth bound \(\log \max_{|w|\le r}|F(T,w)|=O_T(1+r\log(2+r))\) makes this majorant integrable against the translated Gaussian, locally uniformly in \(z\). Dominated convergence and the finite heat formula for polynomials give the result. Propagate each whole partial product. A window of the phase alone supplies only part of the Gaussian integral. [Parent manuscript, growth and Gaussian propagation](../../../manuscript/sections/01_source.tex)

For the explicit phase representation, one complex term propagates by the exact identity

\[
 \big(P_s(e^{ia\,\cdot}C_T)\big)(z)
    =e^{-sa^2+iaz}(P_s C_T)(z+2isa).
\]

Inserting \(C_T\) gives the source multiplier \(e^{-s(U-a)^2-2sa(U-a)}\) inside its centered expectation. The other term follows by reflection. Thus a descent of length \(s\) tests the fluctuations at an imaginary displacement \(2sa\). This specifies information to control for propagation beyond a real phase interval.

### A quantitative test at the origin

Give the lattice approximation its exact initial mass and curvature, \(Z(T)\cos(\sqrt{\beta_1(T)}z)\). After a backward step \(s\) its predicted mass is \(Z(T)e^{-s\beta_1(T)}\). Differentiating the theta integral gives \((\log Z)'=\beta_1\) and \((\log Z)''=\beta_1\beta_2\). Taylor's formula with integral remainder gives the exact loss

\[
 \boxed{\displaystyle
 \log\frac{Z(T-s)}{Z(T)e^{-s\beta_1(T)}}
   =\int_0^s(s-r)\,\beta_1(T-r)\beta_2(T-r)\,dr>0 .}
\]

The large-time scale follows from four saddle moments. For \(V=\sqrt{\kappa}(U-L)\), expand \(U^2=L^2+2LV/\sqrt\kappa+V^2/\kappa\). Since \(\operatorname{Var}V\to1\) and its first four moments stay bounded,

\[
 \beta_1(T)\beta_2(T)=\operatorname{Var}_T(U^2)
   \sim 4L_T^2/\kappa_T\sim L_T/(2T).
\]

For \(0<s=o(T)\) this equivalent holds uniformly with the same leading value throughout \([T-s,T]\), since \(v/T\to1\) there and \(L_v\sim(\log v)/4\). The log mass ratio is therefore asymptotic to \(s^2 L_T/(4T)\). At \(s=2\sqrt{T/L_T}\) the actual mass divided by the propagated cosine mass tends to \(e\). For a return all the way to time zero the exact integral becomes \(\int_0^T v\beta_1(v)\beta_2(v)\,dv\sim T\log(T)/8\).

There is a separate failure visible in the zeros even if one renormalizes the mass at every step. Gaussian convolution multiplies a single cosine by a scalar. Its first positive zero stays at \(\pi/(2\sqrt{\beta_1(T)})\to0\) during the entire descent, whereas \(H(0,0)>0\) gives the true time-zero field a fixed zero-free neighborhood of the origin. These conclusions concern propagation of a single frozen frequency.

## 5. Collision controls and the remaining gap question

The phase estimate has a direct screen at an actual double zero \(x_*\) of a positive cosine source with \(a>0\). There \(e^{iax_*}C_T(x_*)\) is purely imaginary. Differentiating its real part at the double gives \(a|C_T(x_*)|\le |C_T'(x_*)|\le\sigma\). Together with \(\Re C_T(x_*)\ge1-x_*^2\sigma^2/2\), this gives

\[
 x_*^2\sigma^2/2+\sigma/a\ \ge\ 1 .
\]

Thus each genuine double in the positive cosine-source controls fails the strict inequality in the opposite direction. The Euler-factor controls change the coefficients. Weighted-square, finite-tail and finite-prime controls lose the complete normalized theta source. Reflected super-Gaussian and smooth positive-primitive controls lack the canonical square expansion. Atomic and finite-profile controls change the support or full profile, and the RH-conditional endpoint construction changes ordinary Dirichlet arithmetic. Their generic phase and heat identities still apply to their own data. The changed-observation controls fail the literal cosine hypothesis. [Collision families](../../../../../../result-summaries/12_collision_controls_and_screening.md) · [Branch control table](../../research-overview/01_AGC_JH_RESEARCH_OVERVIEW_20261119.md) · [Shape-only arguments](../../../../../../avoid/02_shape_only_arguments_and_the_controls.md) · [Scoped exclusions](../../../../../../avoid/07_scoped_exclusions_read_as_universal.md)

For an explicit transport check take \(H_c(t,x)=e^t\cos x+c\), \(c>1\). All its zeros are real and simple at \(t>\log c\). The difference between its normalized field and \(\cos x\) is \(c(1-\cos x)/(e^t+c)\), exponentially small uniformly on the real axis. Every \(c\) therefore gives the same late profile through every power of \(1/t\). At \(t=\log c\) it has a double zero at \(\pi\). The half-line source at that time assigns equal mass to 0 and 1, so \(a=\sigma=1/2\) and its centered transform vanishes at \(\pi\). This atomic example tests recovery from the limiting shape. The fourth-moment test and the mass-loss asymptotic above use the canonical theta source itself.

For the manuscript's counted pair the remaining task is to control the transported field relative to its boundary values on the same two-zero contour. A useful estimate from the centered transform would bound its Gaussian transport, including the spatial complement, sharply enough to keep that contour clear and preserve the signed gap margin. [Signed contour formula](../../manuscript/sections/signed.tex) · [Outstanding challenges](../../manuscript/sections/challenges.tex)
