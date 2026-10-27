"""Step 01: a relation is a list of ordered pairs; show it as pairs, a matrix and arrows."""
QUEUE = ["Slow Orbit", "Paper Moons", "Glass Harbor", "Night Bus"]

# "plays right after": (a, b) is in the relation when b is the very next track after a.
PAIRS = [(QUEUE[i], QUEUE[i + 1]) for i in range(len(QUEUE) - 1)]

print("Ordered pairs (a, b) = 'b plays right after a':")
for a, b in PAIRS:
    print("  ({0}, {1})".format(a, b))

print("\nMatrix (row = first, column = second, 1 = in the relation):")
print(" " * 16 + "".join("{0:>4}".format(i + 1) for i in range(len(QUEUE))))
for i, a in enumerate(QUEUE):
    row = "".join("{0:>4}".format(1 if (a, b) in PAIRS else 0) for b in QUEUE)
    print("{0:>2} {1:<13}{2}".format(i + 1, a, row))

print("\nArrows (digraph):")
for a, b in PAIRS:
    print("  {0} -> {1}".format(a, b))
