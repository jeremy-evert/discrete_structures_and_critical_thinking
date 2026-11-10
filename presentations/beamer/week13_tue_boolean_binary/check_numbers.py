"""Recomputes every number and truth table claimed in the deck. Exit nonzero on mismatch."""
from itertools import product
D="0123456789ABCDEF"
def b(n,base):
    s=""
    while True:
        s=D[n%base]+s; n//=base
        if n==0: return s
def val(s,base): return int(s,base)
assert b(7+1,8)=="10" and b(0o77+1,8)=="100" and b(0o27+0o15,8)=="44"
assert b(9+7,16)=="10" and b(0xA+5,16)=="F" and b(0xF+1,16)=="10" and b(0xFF+1,16)=="100" and b(0x3B+0x1C,16)=="57"
assert b(3+1,4)=="10" and b(3+3,4)=="12" and b(16,4)=="100"
for x,y,s,p in [("11","1","100","11"),("101","11","1000","1111"),("1011","110","10001","1000010"),("111","101","1100","100011"),("1111","1","10000","1111"),("11","10","101","110"),("110","101","1011","11110")]:
    assert b(val(x,2)+val(y,2),2)==s,(x,y,s)
    assert b(val(x,2)*val(y,2),2)==p,(x,y,p)
assert 23*14==322 and b(val("101",2)*val("11",2),2)=="1111" and b(13+7,2)=="10100"
# half adder: 2C+S == A+B ; full adder: 2Cout+S == A+B+Cin, with the stated formulas
for a,c in product((0,1),repeat=2):
    assert 2*(a&c)+(a^c)==a+c
for a,c,ci in product((0,1),repeat=3):
    s=a^c^ci; co=(a&c)|(ci&(a^c))
    assert 2*co+s==a+c+ci
    assert ((a&c)&(ci&(a^c)))==0   # the two carries never both fire
# 4-bit ripple example 0111+0101 -> 1100, and wrap on 1111+0001
def ripple(x,y,n=4):
    c=0; out=0
    for i in range(n):
        a=(x>>i)&1; d=(y>>i)&1
        out|=(a^d^c)<<i; c=(a&d)|(c&(a^d))
    return out,c
assert ripple(0b0111,0b0101)==(0b1100,0) and ripple(0b1111,0b0001)==(0,1)
print("all deck numbers check out")

# ---- delay model and carry-lookahead (added for the 8-bit / 16-bit slides) ----
import random
# carry into bit i (i>=1) ready at 2i+1; sum bit i one XOR later
assert [2*(n-1)+1+1 for n in (4,8,16,32,64)]==[8,16,32,64,128]
def cla16(x,y):
    P=[((x>>i)^(y>>i))&1 for i in range(16)]; G=[((x>>i)&(y>>i))&1 for i in range(16)]
    c=[0]*17
    for blk in range(4):
        b=4*blk; cin=c[b]
        # flat two-level carries inside the block, each written only from G, P and the block carry-in
        c[b+1]=G[b]|(P[b]&cin)
        c[b+2]=G[b+1]|(P[b+1]&G[b])|(P[b+1]&P[b]&cin)
        c[b+3]=G[b+2]|(P[b+2]&G[b+1])|(P[b+2]&P[b+1]&G[b])|(P[b+2]&P[b+1]&P[b]&cin)
        c[b+4]=G[b+3]|(P[b+3]&G[b+2])|(P[b+3]&P[b+2]&G[b+1])|(P[b+3]&P[b+2]&P[b+1]&G[b])|(P[b+3]&P[b+2]&P[b+1]&P[b]&cin)
    # 16-bit block-level lookahead: c4,c8,c12,c16 straight from block G*, P* and c0
    Gs=[G[b+3]|(P[b+3]&G[b+2])|(P[b+3]&P[b+2]&G[b+1])|(P[b+3]&P[b+2]&P[b+1]&G[b]) for b in (0,4,8,12)]
    Ps=[P[b]&P[b+1]&P[b+2]&P[b+3] for b in (0,4,8,12)]
    c4=Gs[0]|(Ps[0]&0); c8=Gs[1]|(Ps[1]&Gs[0])|(Ps[1]&Ps[0]&0)
    c12=Gs[2]|(Ps[2]&Gs[1])|(Ps[2]&Ps[1]&Gs[0]); c16=Gs[3]|(Ps[3]&Gs[2])|(Ps[3]&Ps[2]&Gs[1])|(Ps[3]&Ps[2]&Ps[1]&Gs[0])
    assert (c[4],c[8],c[12],c[16])==(c4,c8,c12,c16)
    s=sum((P[i]^c[i])<<i for i in range(16))
    return s,c[16]
for _ in range(20000):
    x,y=random.randrange(65536),random.randrange(65536)
    s,co=cla16(x,y); assert s+(co<<16)==x+y,(x,y)
assert cla16(0xFFFF,1)==(0,1) and cla16(0x00FF,1)==(0x0100,0)
assert ripple(0b11111111,1,8)==(0,1)
# delay counts for the CLA slide: P,G t=1; block P* t=2, G* t=3; c4..c16 t=5; inner carries t=7; sums t=8
assert (1+1, 1+2, 3+2, 5+2, 7+1)==(2,3,5,7,8)
print("delay model and 16-bit carry-lookahead check out")

assert 67+58==125 and 58+27==85 and 999+1==1000
print('decimal slide sums check out')

# ---- handout examples (shown both in binary and in decimal) ----
for x,y,s in [("11","1","100"),("1011","110","10001"),("10110111","01101101","100100100")]:
    assert int(x,2)+int(y,2)==int(s,2)
assert (int("10110111",2),int("01101101",2),int("100100100",2))==(183,109,292)
assert 292==256+32+4 and 183==128+32+16+4+2+1 and 109==64+32+8+4+1
for x,y,p in [("101","11","1111"),("110","101","11110")]:
    assert int(x,2)*int(y,2)==int(p,2)
assert 23*14==322==92+230
print("handout examples check out")

# ---- multiplier: 1-bit = AND; 2-bit = 4 ANDs + 2 half adders; n-bit array multiplier counts ----
for a_,b_ in product((0,1),repeat=2): assert a_*b_==(a_&b_)
def ha(x,y): return x^y, x&y
def mul2(a1,a0,b1,b0):
    p0=a0&b0
    p1,c=ha(a1&b0, a0&b1)
    p2,p3=ha(a1&b1, c)
    return p3,p2,p1,p0
for a_ in range(4):
    for b_ in range(4):
        p3,p2,p1,p0=mul2(a_>>1,a_&1,b_>>1,b_&1)
        assert 8*p3+4*p2+2*p1+p0==a_*b_
assert int("1011",2)*int("1101",2)==143==int("10001111",2)==128+8+4+2+1 and int("1011",2)==11 and int("1101",2)==13
assert int("11",2)*int("11",2)==9==int("1001",2) and int("011",2)+int("110",2)==9
def array_mult(a,b,n):
    """Ripple-array multiplier built only from AND gates, half adders and full adders. Returns (product, #and, #HA, #FA)."""
    A=[(a>>j)&1 for j in range(n)]; B=[(b>>i)&1 for i in range(n)]
    nha=nfa=0; P=[0]*(2*n)
    P[0]=A[0]&B[0]
    upper=[A[j]&B[0] for j in range(1,n)]+[0]       # row 0 bits above weight 0, plus a constant 0 on top
    for i in range(1,n):
        s=[0]*n; c=0
        for j in range(n):
            pp=A[j]&B[i]; y=upper[j]
            if j==0:
                s[j],c=ha(pp,y); nha+=1
            elif j==n-1 and i==1:                       # nothing above row 0 here, so only pp and the carry meet: half adder
                s[j],c=ha(pp,c); nha+=1
            else:
                s[j]=pp^y^c; c=(pp&y)|(c&(pp^y)); nfa+=1
        P[i]=s[0]; upper=s[1:]+[c]
    for j in range(n): P[n+j]=upper[j]
    return sum(bit<<k for k,bit in enumerate(P)), n*n, nha, nfa
for n in (2,3,4,8):
    for a_ in range(2**n if n<=4 else 0):
        for b_ in range(2**n):
            p,ands,h,f=array_mult(a_,b_,n); assert p==a_*b_,(n,a_,b_,p)
    import random
    for _ in range(3000):
        a_,b_=random.randrange(2**n),random.randrange(2**n); assert array_mult(a_,b_,n)[0]==a_*b_
    _,ands,h,f=array_mult(1,1,n); assert (ands,h,f)==(n*n,n,n*(n-2)),(n,ands,h,f)
assert [array_mult(1,1,n)[1:] for n in (2,4,8)]==[(4,2,0),(16,4,8),(64,8,48)]
print("multiplier: 1-bit AND, 2-bit (4 AND + 2 HA), and array multiplier counts check out")
