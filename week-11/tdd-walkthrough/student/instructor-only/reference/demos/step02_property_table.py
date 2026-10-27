"""Step 02: ask the four yes/no questions about 'plays right after'; print a witness for every FAILS."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "tests"))
from relations import antisymmetric_failure, reflexive_failure, symmetric_failure, transitive_failure

QUEUE = ["Slow Orbit", "Paper Moons", "Glass Harbor", "Night Bus"]
PAIRS = {(QUEUE[i], QUEUE[i + 1]) for i in range(len(QUEUE) - 1)}


def plays_right_after(a, b):
    return (a, b) in PAIRS


for name, finder in [("reflexive", reflexive_failure), ("symmetric", symmetric_failure),
                     ("antisymmetric", antisymmetric_failure), ("transitive", transitive_failure)]:
    witness = finder(plays_right_after, QUEUE)
    print("{0:<14}{1}".format(name, "holds" if witness is None else "FAILS  witness: " + ", ".join(witness)))
