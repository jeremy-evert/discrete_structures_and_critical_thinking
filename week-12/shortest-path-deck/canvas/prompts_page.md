# Week 12: the Claude prompts (all six)

Each block is exactly what is on the slide. Copy the whole block into Claude. Predict the result first.

---

# Prompt 01: read the distance table

Paste the block below into Claude. `prompt-a` is the first box on the slide.

```prompt-a
Make a folder called tour_demo. Put data/distances.csv in it (I will paste it).
Write tour.py with a function read_table(path) that reads the CSV and returns a dictionary
{(from_city, to_city): distance} using whole numbers. The diagonal cells are blank, so skip them.
Do not add anything else yet.
Then add a few lines at the bottom (under an if __name__ == "__main__": block) that print
the distance from 1 to 2 and from 2 to 1. Run it and show me the output.
```

---

# Prompt 02: total length of a closed tour

Paste the block below into Claude. `prompt-a` is the first box on the slide.

```prompt-a
In tour.py add tour_length(tour, dist). tour is a list of city numbers like [1, 2, 3, 4, 5, 6].
It must add up every leg, INCLUDING the leg from the last city back to the first.
Add a second function legs(tour, dist) that returns each leg as (from_city, to_city, distance)
so I can compare it with my hand work. Keep both functions short. Do not change read_table.
```

---

# Prompt 03: check 1-2-3-4-5-6-1 against my hand total

`prompt-a` runs the check; `prompt-b` adds the tests.

```prompt-a
In tour_demo, run legs([1, 2, 3, 4, 5, 6], dist) and tour_length on the same tour.
Print the six legs and the total. I will compare them with the legs and total I added up by hand.
If they differ, do not change my numbers: tell me which leg differs and why.
```

```prompt-b
Create test_tour.py with pytest tests using read_table("data/distances.csv"):
1. the leg 1 to 2 and the leg 2 to 1 are NOT equal (the table is asymmetric);
2. tour_length([1, 2, 3, 4, 5, 6]) equals the total I give you (I will paste my hand total).
Run pytest and show me the one-line summary.
```

---

# Prompt 04: greedy, nearest unvisited city

Paste the block below into Claude. `prompt-a` is the first box on the slide.

```prompt-a
In tour.py add greedy_tour(dist, start=1). From the current city, go to the unvisited city
with the smallest distance. If two cities tie, take the lower city number. Return the tour as a list.
Run it from city 1, print the tour and tour_length. Show me each step: current city, the options
with their distances, and the one it chose, so I can check it against my hand work.
```

---

# Prompt 05: guess and check with random

Paste the block below into Claude. `prompt-a` is the first box on the slide.

```prompt-a
In tour.py add guess_tour(dist, rng, start=1): keep the start city, then pick a random city from
all six with rng.choice(); if it is already in the tour, reject it and pick again; return the tour
AND the list of every roll (rejected ones too).
Add guess_and_check(dist, k, seed): make k tours with random.Random(seed), and for each print
the rolls, the tour, its total, and the best total so far. Run it with k=5 and seed=3114 and show me the output.
```

---

# Prompt 06: brute force over itertools.permutations

`prompt-a` finds the best tour; `prompt-b` checks the count and compares with greedy.

```prompt-a
In tour.py add brute_force(dist, start=1) using itertools.permutations on the other cities, so the
start city is fixed. For each order build the tour, compute tour_length, and keep the best.
Return (best_tour, best_total, count_of_tours_tried). Run it and show me all three values.
```

```prompt-b
Add two pytest tests to test_tour.py:
1. for n = 2 to 6 (use only the first n cities of the table), the count brute_force returns equals
   math.factorial(n - 1);
2. brute_force's best total is less than or equal to the total of greedy_tour.
Run pytest and show me the one-line summary.
```
