# Choosing without order: C(n, k) and Pascal's triangle

**Week 9, Tuesday.** One idea does most of the work today: when order does not matter, count the ordered ways, then divide out the repeats. Pascal's triangle is that idea written as a table, and it is a built-in way to check yourself.

## 1. Ordered versus unordered

A *selection* of k things from n is **ordered** if AB and BA are different outcomes and **unordered** if they are the same.

- Ordered: `P(n, k) = n × (n−1) × … × (n−k+1) = n! / (n−k)!`
- Unordered: `C(n, k) = P(n, k) / k! = n! / (k! (n−k)!)` (read "n choose k")

Why divide by `k!`: every unordered group shows up `k!` times in the ordered count, once for each way to line its members up.

**Team example.** Two-person teams from {A, B, C, D}: `P(4,2) = 4 × 3 = 12` ordered pairs; each team appears `2! = 2` times (AB and BA); so `C(4,2) = 12 / 2 = 6`.

## 2. Pascal's triangle

Row *n* lists `C(n, 0), C(n, 1), …, C(n, n)`. Start counting rows and positions at **0**.

```
n=0                1
n=1              1   1
n=2            1   2   1
n=3          1   3   3   1
n=4        1   4   6   4   1
n=5      1   5  10  10   5   1
n=6    1   6  15  20  15   6   1
```

Each inside number is the sum of the two above it. Look up today's examples:

- `C(4, 2) = 6`: row 4, position 2. That is the team example.
- `C(5, 2) = 10`: row 5, position 2. That is question 2 on the activity. The proposed answer `5 × 4 = 20` counted every team twice.

## 3. Why the sum rule works (a counting argument, not a pattern)

Claim: `C(n, k) = C(n−1, k−1) + C(n−1, k)`.

Choose a team of k from n people. Single out one person, Sam. Every team falls into exactly one of two cases:

1. **Sam is on the team.** Pick the other `k−1` members from the remaining `n−1` people: `C(n−1, k−1)` ways.
2. **Sam is not on the team.** Pick all `k` members from the remaining `n−1`: `C(n−1, k)` ways.

The cases are **exhaustive** (Sam is either in or out) and **disjoint** (no team is both). That is exactly the discipline for this week: complete case split, nothing counted twice.

## 4. Three facts you can now explain

- **Symmetry: `C(n, k) = C(n, n−k)`.** Choosing who is on the team is the same as choosing who is left off. Row 5 reads 1 5 10 10 5 1 forwards and backwards.
- **Row sums: row n adds to `2ⁿ`.** Each of n people is in or out of a group (2 choices each, product rule), so there are `2ⁿ` groups of any size. Adding up groups of size 0, 1, …, n gives the same total. Check row 4: 1+4+6+4+1 = 16 = 2⁴.
- **Binomial expansion.** `(x + y)ⁿ` multiplies n copies of `(x + y)`. To get `x^(n−k) y^k`, choose which k of the n factors contribute a `y`: `C(n, k)` ways. So `(x + y)⁴ = x⁴ + 4x³y + 6x²y² + 4xy³ + y⁴`, and the coefficients are row 4.

## 5. Check habit for your Decision Gate

When you get a counting answer:

1. Say whether order matters, in one sentence.
2. State your cases and say why they are exhaustive and disjoint.
3. Check a small instance (n = 4 or 5) by listing every outcome, or against a row of the triangle.
4. If the list and the formula disagree, find which outcome the formula counted twice or missed.

## Practice (answers at the bottom)

1. From 6 students, how many 3-person committees?
2. How many 3-person committees from 6 students include Sam? Exclude Sam? Do they add to your answer to 1?
3. Expand `(x + y)³`.
4. Why does row 6 add up to 64?

<details><summary>Answers</summary>

1. `C(6,3) = 20`.
2. Include Sam: `C(5,2) = 10`. Exclude Sam: `C(5,3) = 10`. They add to 20, matching question 1.
3. `x³ + 3x²y + 3xy² + y³`.
4. Each of 6 people is in or out: `2⁶ = 64`. (1+6+15+20+15+6+1 = 64.)

</details>
