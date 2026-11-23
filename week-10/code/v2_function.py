"""v2: same table, but the typed-in numbers become a function.

What changed from v1: the four cells are now COMPUTED from three inputs
(prevalence, sensitivity, specificity), so we can ask "what if?" later.
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


if __name__ == "__main__":
    show(screening_table(0.01, 0.90, 0.95))
