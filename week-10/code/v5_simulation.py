"""v5: a simulation of the same rules, compared with the calculation.

What changed from v4: instead of arithmetic on a table, we generate a million
people one at a time using random numbers.

What agreement shows: the CODE matches the table.
What it does not show: that real patients behave like these three numbers.
"""
import random
from v3_two_conditionals import screening_table, p_c_given_pos

random.seed(10)           # same seed -> same answer every run


def simulate(prevalence, sensitivity, specificity, n=1000000):
    positives = 0
    positives_with_it = 0
    for _ in range(n):
        has_it = random.random() < prevalence
        chance_positive = sensitivity if has_it else (1 - specificity)
        if random.random() < chance_positive:
            positives += 1
            positives_with_it += has_it
    return positives_with_it / positives


calc = p_c_given_pos(screening_table(0.01, 0.90, 0.95))
sim = simulate(0.01, 0.90, 0.95)
print("calculation:", round(calc, 4))
print("simulation: ", round(sim, 4))
print("difference: ", round(abs(calc - sim), 4), "(sampling noise)")
