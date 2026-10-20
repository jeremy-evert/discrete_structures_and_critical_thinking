"""v1: the four-cell table, with every number typed in by hand.

Question: of 10,000 people screened, how many land in each cell?
Prevalence 1%, sensitivity 90%, specificity 95%.
"""

screened = 10000

have_it = 100            # 1% of 10,000
dont_have_it = 9900      # everyone else

true_pos = 90            # 90% of the 100 who have it
false_neg = 10           # the other 10
false_pos = 495          # 5% of the 9,900 who don't
true_neg = 9405          # the other 9,405

print("                 test +    test -")
print("has it        ", true_pos, "      ", false_neg)
print("does not      ", false_pos, "     ", true_neg)
print("total:", true_pos + false_neg + false_pos + true_neg)
