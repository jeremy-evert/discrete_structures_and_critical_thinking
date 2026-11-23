"""v3: v2 plus the two probabilities that get confused.

What changed from v2: two new functions. They read DIFFERENT parts of the
same table. Same four numbers, two different denominators.
"""


def screening_table(prevalence, sensitivity, specificity, n=10000):
    have_it = n * prevalence
    dont = n - have_it
    return {
        "true_pos": have_it * sensitivity,
        "false_neg": have_it * (1 - sensitivity),
        "false_pos": dont * (1 - specificity),
        "true_neg": dont * specificity,
    }


def show(table):
    print("                 test +    test -")
    print("has it        ", round(table["true_pos"]), "      ", round(table["false_neg"]))
    print("does not      ", round(table["false_pos"]), "     ", round(table["true_neg"]))
    total = sum(table.values())
    assert round(total) == 10000, "cells must total the number screened"
    print("total:", round(total))


def p_pos_given_c(t):
    """P(+ | C): of the people who HAVE it, the share who test positive.
    Denominator = the 'has it' row."""
    return t["true_pos"] / (t["true_pos"] + t["false_neg"])


def p_c_given_pos(t):
    """P(C | +): of the people who TEST positive, the share who HAVE it.
    Denominator = the 'test +' column."""
    return t["true_pos"] / (t["true_pos"] + t["false_pos"])


if __name__ == "__main__":
    t = screening_table(0.01, 0.90, 0.95)
    show(t)
    print()
    print("P(+ | C) =", round(p_pos_given_c(t), 4), "  <- the test's sensitivity")
    print("P(C | +) =", round(p_c_given_pos(t), 4), "  <- what a patient actually wants")
