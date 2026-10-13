# Instructor prep: binomial coefficients and Pascal's triangle (Tuesday, Oct 13)

Private. Written for a quick read before the 12:30 class. The student-facing version is `student/pascals-triangle-and-binomials.md`.

## The one idea

Count the ordered ways, then divide by the number of orderings of each group.

`C(n,k) = P(n,k) / k!`

Everything else in the triangle is that, plus one counting argument.

## Plain-language answers to the questions students ask

**Why is `C(n,k)` = n!/(k!(n−k)!)?** Line up all n people (n! ways). Call the first k "the team" and the rest "the others". Shuffling the team among themselves (k! ways) or the others among themselves ((n−k)! ways) gives the same team. Divide both out.

**Why is `C(n,0) = 1`?** There is one way to pick nobody: the empty team. Same for `C(n,n) = 1`, everyone.

**Why does the triangle's addition rule hold?** Fix one person, Sam. A team either has Sam (`C(n−1,k−1)`) or not (`C(n−1,k)`). This is the same exhaustive-and-disjoint case split as the week's theme, so it is a good live example of "a complete case split is a claim."

**Why does row n sum to 2ⁿ?** Each person is in or out: `2·2·…·2`. Counting by group size gives `C(n,0)+…+C(n,n)`. Two counts of the same set, so they are equal.

**Why do the binomial coefficients appear in `(x+y)ⁿ`?** Expanding picks x or y from each of n factors. A term with k y's arises from choosing which k factors gave the y: `C(n,k)`.

## Traps to say out loud

- **Indexing from 0.** The top of the triangle is row 0. The first entry in a row is position 0. `C(5,2)` is row 5, position 2, which is 10. Off-by-one errors here are the most common mistake.
- **`5 × 4 = 20` for teams.** That is ordered pairs. Every team appears twice. Ask "does the formula distinguish AB from BA?"
- **Formula without a model.** Students grab `n!/(k!(n−k)!)` without saying whether order matters. Make them say it first.
- **Distinct versus identical.** Teams of named people use C. Words with repeated letters (not today) need a different divisor.

## Board script for 0:18–0:35 (about 15 minutes)

1. Write {A,B,C,D}. Ask: how many ordered pairs? (12). Ask: how many teams? Let them guess 12, 6, 8. List all six on the board. Circle the pattern: each team appeared twice in the ordered list.
2. Write `C(4,2) = P(4,2)/2! = 6`.
3. Draw the triangle to row 5 *from the rule*. Ask students to fill row 5 from row 4 themselves.
4. Point to 6 in row 4 and 10 in row 5. "These are today's two examples."
5. Do the Sam argument for `C(5,2) = C(4,1) + C(4,2) = 4 + 6 = 10`. List the 4 teams with Sam and the 6 without.
6. Pose the check: list all 10 teams from {A,B,C,D,E} and compare to 10.

## If it goes sideways

- Fall back to the list. Enumeration is the ground truth for this week, and the formula is only a shortcut.
- A student who cannot see the addition rule can see it with the list: split the 10 teams of {A..E} by whether they contain A.

## Quick self-check (answers)

- `C(6,3) = 20`. Row 6: 1 6 15 20 15 6 1.
- Committees of 3 from 6 that include Sam: `C(5,2) = 10`. Exclude: `C(5,3) = 10`. Sum 20.
- `(x+y)³ = x³ + 3x²y + 3xy² + y³`.
- Row sums: 1, 2, 4, 8, 16, 32, 64.
- Symmetry: `C(6,2) = C(6,4) = 15`.

## Optional extension (only if there is time)

The hockey stick: `C(2,2)+C(3,2)+C(4,2)+C(5,2) = 1+3+6+10 = 20 = C(6,3)`. Counting argument: committees of 3 from 6 sorted by the position of the highest-numbered member.
