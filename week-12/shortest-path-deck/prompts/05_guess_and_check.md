# Prompt 05: guess and check with random

Paste the block below into Claude. `prompt-a` is the first box on the slide.

```prompt-a
In tour.py add guess_tour(dist, rng, start=1): keep the start city, then pick a random city from
all six with rng.choice(); if it is already in the tour, reject it and pick again; return the tour
AND the list of every roll (rejected ones too).
Add guess_and_check(dist, k, seed): make k tours with random.Random(seed), and for each print
the rolls, the tour, its total, and the best total so far. Run it with k=5 and seed=3114 and show me the output.
```
