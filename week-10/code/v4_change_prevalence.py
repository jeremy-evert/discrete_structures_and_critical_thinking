"""v4: v3 plus a loop that changes ONE input.

What changed from v3: a for-loop over prevalence. The test did not get any
better or worse. Only who is being screened changed.

PREDICT FIRST: before you run this, write down P(C | +) at 20% prevalence.
"""
from v3_two_conditionals import screening_table, p_c_given_pos

for prevalence in (0.001, 0.01, 0.05, 0.20, 0.50):
    t = screening_table(prevalence, 0.90, 0.95)
    print("prevalence", format(prevalence, ".1%"), "-> P(C | +) =",
          round(p_c_given_pos(t), 3))
