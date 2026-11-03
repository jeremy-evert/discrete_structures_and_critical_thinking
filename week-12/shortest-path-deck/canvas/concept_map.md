# Concept map

| Concept | Real-world meaning | How you check it | Mistake it catches |
|---|---|---|---|
| Vertex | a place (city, station, person) | list them all before drawing | an omitted place |
| Edge | a permitted move between two places | every step of a path must be a listed edge | a path that uses a road that is not there |
| Direction | one-way versus two-way | compare cost 1→2 with 2→1 | treating a one-way street as two-way |
| Weight | what the move costs (minutes, km, dollars) | state the unit | mixing units, or silently changing meaning |
| Tour | visit every place once and come home | count legs: n cities, n legs | forgetting the return leg |
| Greedy | always take the nearest next place | write the options at each step | assuming "nearest" means "best overall" |
| Guess and check | random tries, keep the best | best-so-far never rises | thinking you are done when you are not |
| Brute force | try every tour | count equals (n−1)! | too slow quickly: 15 cities is about a day |
| Model vs procedure | right graph vs right steps | test each separately | a correct answer to the wrong graph |
