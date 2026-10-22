#!/usr/bin/env python3
"""Small deterministic Monte Carlo models for the offline playground."""
from __future__ import annotations
import argparse, math
from monty_hall_sim import Mulberry32

def simulate(name: str, n: int, seed: int, size: int = 23):
    rng = Mulberry32(seed)
    if name == 'buffon':
        # use two independent draws: center distance in [0,t/2], angle in [0,pi/2]
        hits = 0
        for _ in range(n):
            x, a = rng.random() * .5, rng.random() * math.pi / 2
            hits += x <= .5 * math.sin(a)
        p = hits / n
        return {'measured': hits, 'true': n * (2 / math.pi), 'estimate': 2 / p if p else None, 'actual': math.pi}
    if name == 'darts':
        hits = 0
        for _ in range(n):
            x, y = rng.random(), rng.random()
            hits += x*x + y*y <= 1
        return {'measured': hits, 'true': n * math.pi / 4, 'estimate': 4 * hits / n, 'actual': math.pi}
    if name == 'birthday':
        dup = 0
        for _ in range(n):
            seen=set(); same=False
            for _ in range(size):
                d=int(rng.random()*365)
                if d in seen: same=True; break
                seen.add(d)
            dup += same
        truth=1-math.prod((365-i)/365 for i in range(size))
        return {'measured':dup/n,'true':truth,'estimate':dup/n,'actual':truth}
    if name == 'coupon':
        total=0
        for _ in range(n):
            seen=set(); draws=0
            while len(seen)<size:
                seen.add(int(rng.random()*size)); draws+=1
            total+=draws
        truth=size*sum(1/i for i in range(1,size+1))
        return {'measured':total/n,'true':truth,'estimate':total/n,'actual':truth}
    raise ValueError(name)

def prisoners(n, seed):
    """A's pardon stays 1/3; among B/C named by guard, each is 2/3."""
    rng=Mulberry32(seed); a=b=c=0
    for _ in range(n):
        pardoned=int(rng.random()*3)
        if pardoned==0: a+=1; rng.random() # guard names B/C uniformly
        elif pardoned==1: b+=1 # guard must name C
        else: c+=1 # guard must name B
    return {'A':a/n,'B':b/n,'C':c/n}

def main():
    p=argparse.ArgumentParser(); p.add_argument('simulation',choices=['buffon','darts','birthday','coupon']); p.add_argument('--runs',type=int,default=10000); p.add_argument('--seed',type=int,default=20261022); p.add_argument('--size',type=int,default=23); a=p.parse_args()
    if a.runs<1 or a.size<1:p.error('runs and size must be positive')
    print(simulate(a.simulation,a.runs,a.seed,a.size))
if __name__=='__main__':main()

def simulate_three_prisoners(games: int, seed: int):
    """Condition on guard saying B will not be freed; returns A/C pardon rates."""
    if games < 1:
        raise ValueError('games must be positive')
    rng = Mulberry32(seed)
    named_b = a_pardoned = c_pardoned = 0
    for _ in range(games):
        pardoned = int(rng.random() * 3)  # A=0, B=1, C=2
        if pardoned == 0:
            names_b = rng.random() < .5  # guard chooses uniformly between B and C
        else:
            names_b = pardoned == 2  # if C is pardoned, guard must name B
        if names_b:
            named_b += 1
            a_pardoned += pardoned == 0
            c_pardoned += pardoned == 2
    return {'observed_named_B': named_b, 'A_given_B_named': a_pardoned / named_b,
            'C_given_B_named': c_pardoned / named_b}
