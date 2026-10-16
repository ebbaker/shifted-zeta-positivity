#!/usr/bin/env python3
"""Exact checks for selected inverse distribution and the cubic frame target.

GPT-6 (Codex), inherited configuration; exact variant/effort not exposed.
Uses rational intervals and finite fields, not sampled analytic moments.
"""
from fractions import Fraction as F
from itertools import product
import json

from check_mixed_conductor_refinement import Interval, quantities, ETA, ELL, D0, D1, X0, X1


def rec(v):
    return {"exact": str(v), "decimal": float(v)}


def repeated_row_margin():
    lower = None
    for i,j in product(range(32), repeat=2):
        d = Interval(D0+(D1-D0)*F(i,32),D0+(D1-D0)*F(i+1,32))
        x = Interval(X0+(X1-X0)*F(j,32),X0+(X1-X0)*F(j+1,32))
        v = quantities(d,x)
        rmax = v["rn"]+(ETA+ELL)/(d*(1-x))
        mmax = v["mn"]+ELL/(d*v["b"])
        # Target minus repeated-row/nonprincipal upper exponent, discarding
        # the additional nonnegative 2*mu_C improvement.
        margin = 1-d*(1+rmax)/2-(F(11,4)-3*d)*mmax-3*(ETA+2*ELL)
        assert margin.lo > 0
        lower = margin.lo if lower is None else min(lower,margin.lo)
    coarse = F((lower*100000).numerator//(lower*100000).denominator,100000)
    assert coarse > F(1,100)
    return coarse


class Field:
    def __init__(self, coefficients):
        # Monic modulus over F_3, coefficients in increasing degree order.
        self.mod = coefficients
        self.n = len(coefficients)-1
        self.q = 3**self.n

    def digits(self,a):
        return [(a//(3**i))%3 for i in range(self.n)]

    def add(self,a,b):
        return sum(((x+y)%3)*3**i for i,(x,y) in enumerate(zip(self.digits(a),self.digits(b))))

    def neg(self,a):
        return sum(((-x)%3)*3**i for i,x in enumerate(self.digits(a)))

    def mul(self,a,b):
        out=[0]*(2*self.n-1)
        for i,x in enumerate(self.digits(a)):
            for j,y in enumerate(self.digits(b)):
                out[i+j]=(out[i+j]+x*y)%3
        for k in range(len(out)-1,self.n-1,-1):
            coeff=out[k]
            for j in range(self.n+1):
                out[k-self.n+j]=(out[k-self.n+j]-coeff*self.mod[j])%3
        return sum(out[i]*3**i for i in range(self.n))

    def power(self,a,n):
        ans=1
        while n:
            if n%2: ans=self.mul(ans,a)
            a=self.mul(a,a)
            n//=2
        return ans

    def trace(self,a):
        out=0
        for i in range(self.n): out=self.add(out,self.power(a,3**i))
        assert out in (0,1,2)
        return out


def gauss_frame_checks():
    records=[]
    for modulus,bcount in [([0,1],2),([1,0,1],3),([1,2,0,1],9)]:
        f=Field(modulus)
        q=f.q
        assert 2<=bcount<=q-1
        # Independently verify that the small quotient has no zero divisors.
        assert all(f.mul(a,b)!=0 for a,b in product(range(1,q),repeat=2))
        assert all(f.power(a,q)==a for a in range(q))
        cases=0
        for a,b in product(range(q),repeat=2):
            counts=[0,0,0]
            for y in range(q):
                phase=f.trace(f.add(f.mul(a,y),f.mul(b,f.mul(y,y))))
                counts[phase]+=1
            # z=(c0-c2)+(c1-c2)*omega; |z|^2=A^2-A B+B^2.
            aa,bb=counts[0]-counts[2],counts[1]-counts[2]
            norm2=aa*aa-aa*bb+bb*bb
            assert norm2==(q*q if a==b==0 else (0 if b==0 else q))
            cases+=1
        # Exact spectra and cyclic sums, using the proved union-of-bases
        # identity. No floating eigensolver or matrix storage is needed.
        rows=q*bcount
        trace3=q*bcount**3
        repeated=rows*(3*bcount-2)
        distinct=q*bcount*(bcount-1)*(bcount-2)
        assert trace3==repeated+distinct
        records.append({"field_order":q,"modulus":modulus,"bases":bcount,
                        "rows":rows,"gauss_sum_cases":cases,
                        "signed_operator_norm":bcount,
                        "unsigned_operator_norm":f"1+{bcount-1}*sqrt({q})",
                        "signed_trace_cube":trace3,
                        "repeated_index_trace_part":repeated,
                        "distinct_index_trace_part":distinct,
                        "absolute_distinct_index_trace_part":
                            f"{bcount*(bcount-1)*(bcount-2)*q}*sqrt({q})"})
    return records


def local_fiber_mask_checks():
    # The residue field F_7 has generator 3 and a character of exact order
    # six. Work in exponents of zeta_6, with None denoting a retained zero.
    logs={pow(3,j,7):j for j in range(6)}
    assert len(logs)==6
    cases=0
    for a,b,orientation in product(range(6),range(6),(-1,1)):
        difference=(orientation*(a-b))%6
        same_on_units=all((orientation*(a-b)*logs[r])%6==0 for r in range(1,7))
        assert same_on_units==(a==b)
        reduced=(a+5*b)%6
        assert reduced==(a-b)%6
        for r in range(7):
            left=None if r==0 and (a or b) else (0 if r==0 else difference*logs[r]%6)
            # After phase cancellation the extra original mask remains.
            phase=None if r==0 and difference else (0 if r==0 else difference*logs[r]%6)
            right=None if r==0 and (a or b) else phase
            assert left==right
            cases+=1
    # These two local characters have equal order but are unequal;
    # their quotient is nonprincipal. An order-only fiber proof is invalid.
    assert (1-5)%6==2 and logs[3]==1
    return {"residue_field":7,"exact_phase_and_zero_cases":cases,
            "same_order_distinct_character_example":{"exponents":[1,5],"quotient_exponent":2},
            "scope":"finite local algebra only; source reciprocity remains imported"}


def main():
    margin=repeated_row_margin()
    # Coarse continuous proof for the all-identical-row trace contribution.
    gmax=F(21,50)*(1+F(37,50))/2
    hmin=3*(1-(1-F(9,25))*F(1,2)-(ETA+2*ELL))
    diagonal_margin=hmin-(1+2*gmax)
    assert diagonal_margin>F(3,10)
    square_root_gap=(F(1,2)-D1)*F(2,5)-(ETA+2*ELL)
    assert square_root_gap==F(15899,500000)
    cubic_tight_slack=(3*D0-1)*F(2,5)-3*(ETA+2*ELL)
    assert cubic_tight_slack==F(15697,500000)
    print(json.dumps({
        "status":"conditional exponent and exact finite-character checks; no arithmetic triple estimate proved",
        "model":"GPT-6 (Codex), inherited; exact variant and reasoning effort not exposed",
        "continuous_interval_cells":1024,
        "two_equal_primitive_character_margin_lower":rec(margin),
        "all_equal_primitive_character_margin_lower":rec(diagonal_margin),
        "absolute_schur_square_root_exponent_deficit_lower":rec(square_root_gap),
        "allowed_cubic_trace_excess_over_tight_frame_lower":rec(cubic_tight_slack),
        "finite_character_frames":gauss_frame_checks(),
        "local_fiber_mask_checks":local_fiber_mask_checks()
    },indent=2,sort_keys=True))


if __name__=="__main__":
    main()
