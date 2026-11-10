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
