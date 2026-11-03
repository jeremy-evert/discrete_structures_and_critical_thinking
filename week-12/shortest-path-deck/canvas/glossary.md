# Glossary (plain language)

- **Graph**: places and the connections between them, written down. Not a chart with axes.
- **Vertex** (plural vertices): one place in the graph. Here, a city.
- **Edge**: one connection between two places.
- **Directed**: each edge goes one way only, and 1→2 and 2→1 are two separate edges. In our table both exist, but with different costs (that is what *asymmetric* means below).
- **Weighted**: each edge has a number on it (a cost).
- **Weight**: that number. Say what it measures (minutes, distance, dollars).
- **Asymmetric**: the cost from A to B differs from the cost from B to A.
- **Leg**: one edge used in a trip, such as 3→4.
- **Tour**: a trip that visits every city once and returns to the start.
- **Length (of a tour)**: the sum of all its legs, including the return leg.
- **Greedy**: at each step take the cheapest option you can see right now.
- **Tie**: two options with equal cost. We break ties by taking the lower city number.
- **Guess and check**: build a random answer, measure it, keep the best so far.
- **Random generator (rng)**: code that produces unpredictable-looking picks, such as which city comes next.
- **Seed**: a starting number for the random generator. The same seed gives the same "random" picks every time, so your output can match your neighbor's.
- **Brute force**: try every possibility.
- **Factorial** (written n!): n × (n−1) × … × 1. So 4! = 24. A tour of n cities has (n−1)! orders when the start is fixed.
- **Permutation**: one ordering of a list. The cities 2, 3, 4 can be ordered 6 ways.
- **Diagonal**: the cells of the table where row and column are the same city (1 to 1, 2 to 2). They are blank because you do not travel from a city to itself.
- **Traversal**: visiting vertices by following edges, for example walking a path or a tour.
- **Model**: the choices about what to keep from a real situation (what is a vertex, what is an edge, what is a weight).
- **Procedure**: the steps you follow on a model.
- **Assumption**: something you chose to treat as true. Write it down.
- **Test (pytest)**: a small program that checks one claim and says pass or fail.
- **Counterexample**: one case that shows a claim is false (a case where greedy is not best).
- **CSV**: a plain text table, values separated by commas. Open it in any text editor; each line is one row.

## Words that appear in the Claude prompts
- **Dictionary**: a Python collection that looks things up by a key. Here the key is a pair (from_city, to_city) and the value is the distance.
- **Tuple**: a fixed group of values, such as (1, 2, 11) = from 1, to 2, distance 11.
- **dist**: the name the prompts use for that dictionary.
- **k**: how many random tours to try.
- **itertools.permutations**: a Python tool that lists every ordering of some items.
- **`if __name__ == "__main__":`**: the lines under it run only when you run the file directly, not when another file imports it. Claude writes it for you.
- **Roll**: one random pick of a city number, including picks that are rejected.
- **Evidence / assumption / inference**: evidence is what you observed or computed; an assumption is something you chose to treat as true; an inference is a conclusion you drew from them.
