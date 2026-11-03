# Handout: a tour, a table, and a model (one page)

**Why model first?** A subway map is not the city. It keeps what matters (which stations connect) and drops the rest. A *model* is the same kind of choice: you decide what to keep. Your answer can only be as good as that choice.

**Every step, same loop:** **Predict** (write your guess) → **Run** (run the code, or do the sum or check by hand on paper) → **Explain** (say why). A wrong guess is useful: it shows you what you misunderstood.

## The situation
Six cities, numbered 1 to 6. A table gives the travel cost from each city to each other city. The table is **not symmetric**: going 1→2 can cost something different from 2→1 (think of a one-way street with a long way back).

A **tour** visits every city once and returns to the start, for example 1-2-3-4-5-6-1. Its **length** is the sum of its six legs, *including the leg from the last city back to the start*.

**The table** (row = from, column = to; the dash on the diagonal is a city to itself, so it is left blank). It is the file `data/distances.csv` that the prompts use; it is also on the slides.

| from/to | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| 1 | - | 11 | 4 | 12 | 5 | 6 |
| 2 | 9 | - | 12 | 10 | 10 | 4 |
| 3 | 12 | 11 | - | 10 | 7 | 12 |
| 4 | 10 | 9 | 9 | - | 6 | 12 |
| 5 | 12 | 3 | 6 | 8 | - | 6 |
| 6 | 10 | 9 | 2 | 11 | 13 | - |

## Three ways to look for a short tour
| Idea | What it does | What to notice |
|---|---|---|
| **Greedy** | From where you are, always go to the nearest unvisited city (ties: take the lower city number) | Fast, easy to check by hand, but can be fooled: a cheap step now can force an expensive step later. On our table greedy gives 1-3-5-2-6-4-1 with length 39, but the best tour is 1-5-2-6-3-4-1 with length 34 |
| **Guess and check** | Pick cities at random (the die has six faces, one per city; a face for a city already used is rejected and re-rolled), build a tour, keep the best so far | Never knows when it is done (an untried tour could always be better); the best-so-far (lower is better) only drops, never rises |
| **Brute force** | Try every tour, keep the best | Always right, but the number of tours explodes (see counting below) |

**Counting tours.** A tour is a loop, so where you start does not change which loop it is; we fix the start at city 1. After city 1 you choose the next of the other n−1 cities, then the next of the remaining n−2, and so on, so n cities give (n−1) × (n−2) × … × 1 = (n−1)! tours. Direction matters here, so a loop and its reverse count separately. 3 cities → 2, 4 → 6, 5 → 24, 6 → 120, 15 → 87,178,291,200. At a million tours a second, 87,178,291,200 ÷ 1,000,000 ≈ 87,000 seconds ≈ 24 hours for 15 cities. (A million a second is an assumption, not a measurement.)

## Procedure versus model (the idea of the week)
- **Procedure question:** did I follow the steps correctly? (Is every leg really an edge? Is the sum right?)
- **Model question:** did I draw the right graph? (Are edges one-way? Does the weight mean time, distance or cost?)
- A perfect procedure on the wrong model gives a confident wrong answer. AI tools do this: they answer correctly for a graph you did not mean, often without saying which graph they used.

## Course method
**Sources** (the facts you were given, such as the table) → **Rules / Assumptions** (what a vertex, edge, direction and weight mean) → **Work** → **Check** → **One-Sentence Summary** (conclusion plus its limit). Example: "Under one-way costs, the best tour is 1-5-2-6-3-4-1 with length 34; this assumes the table is correct and every city is visited exactly once."

## Self-check
I can: add a tour's legs by hand, including the return leg · say why 1→2 and 2→1 may differ · show a case where greedy is not best · say why guess-and-check can't know it is done · count tours for n cities · name one thing a graph model assumed.
