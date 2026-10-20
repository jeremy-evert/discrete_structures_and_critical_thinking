"""v6: the simulation agrees with the calculation and BOTH are wrong.

What changed from v5: the real population has two groups. The test is 95%
specific for most people but only 80% specific for a subgroup (say, people
with a related condition that also triggers the test) who are 10% of those
screened.

The stated-rates calculation still says 0.1538. Reality says about 0.12.
Running the stated-rates simulation a billion times would not fix this:
more runs shrink noise, not assumption error.
"""
import random
from v3_two_conditionals import screening_table, p_c_given_pos

random.seed(10)


def simulate_two_groups(n=1000000):
    positives = 0
    positives_with_it = 0
    for _ in range(n):
        has_it = random.random() < 0.01
        in_subgroup = random.random() < 0.10
        specificity = 0.80 if in_subgroup else 0.95
        chance_positive = 0.90 if has_it else (1 - specificity)
        if random.random() < chance_positive:
            positives += 1
            positives_with_it += has_it
    return positives_with_it / positives


stated = p_c_given_pos(screening_table(0.01, 0.90, 0.95))
real = simulate_two_groups()
print("what the stated rates say:  ", round(stated, 4))
print("what the real mix produces: ", round(real, 4))
print("the table and the simulation agreed in v5. They were both answering")
print("a question about the STATED rates, not about the clinic.")
