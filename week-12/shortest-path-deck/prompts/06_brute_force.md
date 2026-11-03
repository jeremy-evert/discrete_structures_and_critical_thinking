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
