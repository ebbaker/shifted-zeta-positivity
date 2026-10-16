#!/usr/bin/env python3
"""Exact finite checks for the short-family continuation.

Standard library only; rational arithmetic and cyclotomic quotient rings.
No floating-point certification, analytic Gauss-sum theorem, asymptotic
moment estimate, prime distribution estimate, or RH statement is tested.
Output is one small JSON record on stdout. No files are written by this script.
"""
from fractions import Fraction as F
from itertools import product
import json

COUNTS = {}

def check(group, condition):
    COUNTS[group] = COUNTS.get(group, 0) + 1
    if not condition:
        raise AssertionError((group, COUNTS[group]))

# Q(zeta_6): (a,b) denotes a+b*zeta_6; zeta_6^2=zeta_6-1.
def e(a=0, b=0):
    return (F(a), F(b))

def add(x, y):
    return (x[0]+y[0], x[1]+y[1])

def neg(x):
    return (-x[0], -x[1])

def sub(x, y):
    return add(x, neg(y))

def mul(x, y):
    a,b=x; c,d=y
    return (a*c-b*d, a*d+b*c+b*d)

def conj(x):
    return (x[0]+x[1], -x[1])

def scale(x, c):
    return (x[0]*c, x[1]*c)

def norm(x):
    return x[0]*x[0]+x[0]*x[1]+x[1]*x[1]

ZERO=e(); ONE=e(1)
ROOTS=[ONE]
for _ in range(5):
    ROOTS.append(mul(ROOTS[-1],e(0,1)))

class Cyclotomic:
    """Q(zeta_6)[z]/(1+z+...+z^(p-1)), exact for tested p>3.

    Canonical elements have p-1 Q(zeta_6) coefficients. Computation first
    reduces z^p=1, then eliminates z^(p-1) using the cyclotomic relation.
    """
    def __init__(self,p):
        self.p=p
        self.zero=(ZERO,)*(p-1)
    def canonical(self, values):
        out=[ZERO]*self.p
        for k,v in enumerate(values):
            out[k%self.p]=add(out[k%self.p],v)
        top=out[-1]
        return tuple(sub(v,top) for v in out[:-1])
    def const(self,v):
        return (v,)+(ZERO,)*(self.p-2)
    def root(self,k):
        out=[ZERO]*self.p
        out[k%self.p]=ONE
        return self.canonical(out)
    def add(self,x,y):
        return tuple(add(a,b) for a,b in zip(x,y))
    def scale(self,x,c):
        return tuple(mul(a,c) for a in x)
    def mul(self,x,y):
        out=[ZERO]*self.p
        for i,a in enumerate(x):
            if a==ZERO: continue
            for j,b in enumerate(y):
                if b!=ZERO:
                    k=(i+j)%self.p
                    out[k]=add(out[k],mul(a,b))
        return self.canonical(out)
    def conjugate(self,x):
        out=[ZERO]*self.p
        for j,a in enumerate(x):
            out[-j%self.p]=add(out[-j%self.p],conj(a))
        return self.canonical(out)
    def sum(self,values):
        out=self.zero
        for v in values: out=self.add(out,v)
        return out
    def fourier(self,f):
        # Negative-sign, unnormalized finite Fourier transform.
        return [self.sum(self.mul(v,self.root(-h*x))
                         for x,v in enumerate(f)) for h in range(self.p)]

def primitive_root(p):
    for g in range(2,p):
        if len({pow(g,j,p) for j in range(p-1)})==p-1:
            return g
    raise AssertionError('no generator')

def finite_gauss_checks():
    records=[]
    for p in (7,13,19):
        ring=Cyclotomic(p)
        g=primitive_root(p)
        log={pow(g,j,p):j for j in range(p-1)}
        profile=[e(F(x*x+1,p),F((-1)**x*(x+2),p+1)) for x in range(p)]
        f=[ring.const(v) for v in profile]
        ff=ring.fourier(f)
        fff=ring.fourier(ff)
        for x in range(p):
            check('double_fourier',fff[x]==ring.scale(f[-x%p],e(p)))
        character_records=[]
        for k in range(1,6):
            chi=[ZERO]+[ROOTS[(k*log[x])%6] for x in range(1,p)]
            bar=[conj(v) for v in chi]
            check('zero_extension',chi[0]==ZERO and bar[0]==ZERO)
            check('character_nonprincipal',sum((v[0] for v in chi),F(0))==0
                  and sum((v[1] for v in chi),F(0))==0)
            for x in range(p):
                for y in range(p):
                    check('character_multiplicativity',mul(chi[x],chi[y])==chi[x*y%p])
            tau=ring.sum(ring.scale(ring.root(x),chi[x]) for x in range(p))
            bartau=ring.sum(ring.scale(ring.root(x),bar[x]) for x in range(p))
            check('gauss_product',ring.mul(tau,bartau)==ring.const(scale(chi[p-1],p)))
            check('gauss_absolute_square',ring.mul(tau,ring.conjugate(tau))==ring.const(e(p)))
            chi_f=ZERO
            for x in range(p): chi_f=add(chi_f,mul(chi[x],profile[x]))
            lhs=ring.const(scale(chi_f,p))
            dual=ring.sum(ring.scale(ff[h],bar[h]) for h in range(p))
            rhs=ring.mul(tau,dual)
            check('weighted_gauss_fourier',lhs==rhs)
            # Forgetting the character conjugation is detected for nonreal chi.
            wrong=ring.mul(tau,ring.sum(ring.scale(ff[h],chi[h]) for h in range(p)))
            if k!=3:
                check('wrong_character_orientation_detected',wrong!=lhs)
            # A complex profile cannot silently be replaced by its conjugate.
            wrong_profile=ZERO
            for x in range(p):
                wrong_profile=add(wrong_profile,mul(chi[x],conj(profile[x])))
            check('wrong_profile_conjugation_detected',wrong_profile!=chi_f)
            character_records.append({'power':k,'order':6//__import__('math').gcd(k,6)})
        records.append({'prime':p,'generator':g,'characters':character_records,
                        'profile':'(x^2+1)/p + (-1)^x(x+2)/(p+1) * zeta_6'})
    return records

def rational_exponent_checks():
    examples=[]
    for h,a in ((F(8,9),F(0)),(F(4,5),F(0)),(F(2,3),F(0)),
                (F(1,4),F(0)),(F(1,2),F(1,8))):
        beta=(1+a)/2+F(5,12)*h
        for d in (2,3,6):
            hd=F(d,6)*h; ad=a+h-hd
            check('inherited_floor',(1+ad)/2+F(d-1,2*d)*hd==beta)
            check('inherited_recurrence',1-hd/d==1-h/6)
        check('useful_target',beta<F(7,8))
        check('useful_target_gap',h+a<F(9,10)<1)
        check('useful_target_identity',h+a==F(6,5)*(a+F(5,6)*h)-a/5)
        prime_core=1+h/6
        prime_gap=prime_core-h-a
        check('coherent_prime_core_exponent',prime_gap==1-a-F(5,6)*h)
        check('coherent_prime_core_exponent',prime_gap==2*(1-beta))
        check('coherent_prime_core_target_gap',prime_gap>F(1,4))
        check('coherent_prime_core_diagonal_gap',prime_core>h)
        check('coherent_prime_core_masks',h/6<1)
        examples.append({'h':str(h),'a':str(a),'beta':str(beta),
                         'prime_core_exponent':str(prime_core),
                         'prime_core_minus_target':str(prime_gap),
                         'prime_core_minus_diagonal':str(prime_core-h),
                         'g_cutoff_at_b_f_zero':str((1-a)/2)})
    # Independently assemble weight, counts, and a sqrt-conductor bound.
    tested=0
    for h,a,b,f,g in product((F(1,4),F(2,3),F(8,9)),
                             (F(0),F(1,8)),
                             (F(0),F(1,8),F(1,4)),
                             (F(0),F(1,8),F(1,4)),
                             (F(0),F(1,4),F(1,2))):
        x=1-b-f
        if g>x: continue
        # Original weight H B /D^2; counts B,F,X^2/G; kernel sqrt(Q)=X/G.
        assembled=(h+b-2)+b+f+(2*x-g)+(x-g)
        compact=h+1-b-2*f-2*g
        check('new_block_budget',assembled==compact)
        check('controlled_sector',(compact<=h+a)==(b+2*f+2*g>=1-a))
        tested+=1
    return {'examples':examples,'block_parameter_cases':tested,
            'budget':'H*B/D^2 * B * F * (X^2/G) * (X/G) = H*D/(B*F^2*G^2)',
            'support':'X=D/(BF), G<=X',
            'controlled_sector_without_epsilon_buffers':'b+2f+2g >= 1-a',
            'all_beating_7_over_8_targets':'a+h < 9/10 < 1 for a>=0',
            'coherent_prime_core':'D*H^(1/6)/log(D)^2 - O(H/log(D))',
            'coherent_prime_core_target_gap':'1-a-5h/6 = 2(1-beta_out) > 1/4 when beta_out<7/8',
            'separate_prime_sector_bound_requires':'a+5h/6 >= 1',
            'coherent_prime_core_scope':'Only exponent arithmetic is checked; the prime-counting, row-counting, and exact involution arguments are proof inputs.'}

def generic_sieve_exponent_checks():
    # This grid checks exact consequences of the four proposed sieve terms;
    # the analytic sieve estimate itself is a separate proof input.
    heights=sorted({F(k,d) for d in range(1,33) for k in range(1,d+1)})
    samples=[]
    for h in heights:
        terms=(h,1+h/6,F(5,6)*h+F(1,3),h/3+F(5,6))
        dominant=1+h/6
        gaps=(1-F(5,6)*h,F(2,3)*(1-h),(1-h)/6)
        for other,gap in zip((terms[0],terms[2],terms[3]),gaps):
            check('generic_sieve_gap_identity',dominant-other==gap)
            check('generic_sieve_dominance',gap>=0)
        check('generic_sieve_maximum',max(terms)==dominant)
        check('generic_sieve_boundary',(terms[2]==dominant)==(h==1))
        check('generic_sieve_boundary',(terms[3]==dominant)==(h==1))
        a_gen=1-F(5,6)*h
        check('generic_sieve_normalization',h+a_gen==dominant)
        check('generic_sieve_floor',(1+a_gen)/2+F(5,12)*h==1)
        if h in (F(1,4),F(2,3),F(4,5),F(8,9),F(1)):
            samples.append({'h':str(h),'term_exponents':[str(v) for v in terms],
                            'a_gen':str(a_gen),'beta_gen':'1'})
    useful=[]
    for h,a in ((F(8,9),F(0)),(F(4,5),F(0)),(F(2,3),F(0)),
                (F(1,4),F(0)),(F(1,2),F(1,8))):
        beta=(1+a)/2+F(5,12)*h
        a_gen=1-F(5,6)*h
        saving=a_gen-a
        check('generic_sieve_useful_gap',saving==1-a-F(5,6)*h)
        check('generic_sieve_useful_gap',saving==2*(1-beta))
        check('generic_sieve_useful_gap',saving>F(1,4))
        useful.append({'h':str(h),'a':str(a),'beta':str(beta),
                       'required_improvement_over_generic_loss':str(saving)})
    return {'term_order':['H','D H^(1/6)','H^(5/6) D^(1/3)','H^(1/3) D^(5/6)'],
            'grid':'all distinct k/d with 1<=k<=d<=32',
            'grid_count':len(heights),'samples':samples,'useful_examples':useful,
            'dominance_identities':['1+h/6-h = 1-5h/6',
                                   '1+h/6-(5h/6+1/3) = 2(1-h)/3',
                                   '1+h/6-(h/3+5/6) = (1-h)/6'],
            'conclusion':'For 0<h<=1 the generic normalized exponent is 1+h/6; a_gen=1-5h/6 gives beta_gen=1.',
            'scope':'Finite rational checks of exponent arithmetic; no analytic sieve estimate is certified.'}

def weighted_replication_checks():
    # Rational Gaussian complex weights, separately from the cyclotomic ring.
    pool=[(F(0),F(0)),(F(1),F(0)),(F(0),F(1)),
          (F(1,2),F(-1,3)),(F(-1),F(2))]
    def abs2(z): return z[0]*z[0]+z[1]*z[1]
    vectors=0
    for size in range(1,5):
        for weights in product(pool,repeat=size):
            total=(sum((z[0] for z in weights),F(0)),sum((z[1] for z in weights),F(0)))
            energy=sum((abs2(z) for z in weights),F(0))
            gap=size*energy-abs2(total)
            pair=sum((abs2((weights[i][0]-weights[j][0],weights[i][1]-weights[j][1]))
                      for i in range(size) for j in range(i+1,size)),F(0))
            check('weighted_count_identity',gap==pair)
            check('weighted_count_bound',gap>=0)
            check('weighted_count_equality',(gap==0)==all(z==weights[0] for z in weights))
            vectors+=1
    return {'vectors':vectors,'maximum_rows':4,
            'identity':'R sum|w|^2 - |sum w|^2 = sum_(i<j)|w_i-w_j|^2',
            'consequence':'effective replication <= R; equality only for equal weights'}

def phase_and_profile_checks():
    # omega=zeta_6-1, n=-2-3omega=1-3zeta_6, Nn=7.
    n=e(1,-3)
    phase_square=scale(mul(n,n),F(1,7))
    check('eisenstein_witness',norm(n)==7)
    check('eisenstein_witness',phase_square==e(F(-8,7),F(3,7)))
    check('eisenstein_witness',phase_square!=ONE)
    check('eisenstein_witness',norm(phase_square)==1)
    # Multiplying alpha by its conjugate gives 1; alpha by itself does not.
    check('eisenstein_witness',scale(mul(n,conj(n)),F(1,7))==ONE)
    D=F(49); H=F(11); sqrt_q=F(294)
    W1=e(F(2,3),F(4,5)); W2=e(F(-3,7),F(5,11))
    W01=scale(conj(W1),F(1,2)); W02=scale(conj(W2),F(1,3))
    lhs=scale(mul(W01,conj(W02)),H/(D*D)*sqrt_q/H)
    rhs=scale(mul(conj(W1),W2),1/D)
    check('complex_profile_normalization',lhs==rhs)
    check('complex_profile_orientation',rhs!=scale(mul(W1,conj(W2)),1/D))
    return {'norm':7,'n':'-2-3 omega',
            'alpha_square':'(-5+3 omega)/7 != 1',
            'alpha_conjugate_alpha':'1',
            'profile_identity':'(H/D^2)(sqrt(q)/H) W0(x1) conjugate(W0(x2)) = conjugate(W1) W2 /D',
            'profile_parameters':{'D':'49','H':'11','x1':'4','x2':'9','sqrt_q':'294'}}

def main():
    exponent=rational_exponent_checks()
    generic_sieve=generic_sieve_exponent_checks()
    weights=weighted_replication_checks()
    phase=phase_and_profile_checks()
    gauss=finite_gauss_checks()
    print(json.dumps({'status':'all exact finite checks passed',
        'scope':'Rational exponent bookkeeping, weight-count identity, Eisenstein phase witness, and finite cyclic Gauss/Fourier identities only. No asymptotic estimate or number-field analytic theorem is certified.',
        'arithmetic':'fractions.Fraction; Q(zeta_6)[z]/Phi_p(z); no floating point',
        'check_count':sum(COUNTS.values()),'checks_by_group':COUNTS,
        'exponents':exponent,'generic_sieve_exponents':generic_sieve,
        'weighted_replication':weights,
        'phase_and_complex_profile':phase,'finite_gauss_fourier':gauss},indent=2))

if __name__=='__main__': main()
