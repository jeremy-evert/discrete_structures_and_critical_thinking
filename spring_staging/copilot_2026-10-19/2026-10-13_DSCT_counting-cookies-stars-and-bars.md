**Counting Cookies**

Permutations, Combinations, Repetition, and Stars & Bars

*DSCT — Discrete Structures and Critical Thinking \| Week 09 \| October 13, 2026 \| Dr. Jeremy Evert, SWOSU*

1\. What We Set Out to Do

This session started with a simple whiteboard question — choose 2 letters from {A, B, C, D} — and grew into a full map of the four counting patterns, a narrated Python program that counts cookie batches from the class lineup, and a seven-chapter story that builds Stars and Bars from first principles.

The guiding idea throughout: **see it small, count it by hand, then let the formula describe what you already understand.**

2\. Choosing 2 from {A, B, C, D}: Why 12 and Why 6?

Permutations: 12

Picture two labeled seats. The first seat has 4 options. Once one letter is used, the second seat has 3 options. The counting principle says multiply:

P(4,2) = 4 × 3 = 12

Order matters here: A in seat 1 with B in seat 2 is a different outcome from B in seat 1 with A in seat 2.

Combinations: 6

On the whiteboard, every pair showed up twice — once in each order — and the duplicates were crossed out:

| **Keep (unique group)** | **Crossed out (same group, other order)** |
|-------------------------|-------------------------------------------|
| AB                      | BA                                        |
| AC                      | CA                                        |
| AD                      | DA                                        |
| BC                      | CB                                        |
| BD                      | DB                                        |
| CD                      | DC                                        |

C(4,2) = P(4,2) / 2! = 12 / 2 = 6

> **Core intuition:** Permutations — order matters (AB ≠ BA). Combinations — order does not matter (AB = BA). A combination count is a permutation count with the duplicate orderings removed.

3\. Why Divide by 2! and Not Just 2?

The divisor answers one question: **how many ways can the chosen group rearrange itself?** Every unique group gets counted that many times in the permutation list, so that is exactly what we divide out.

- 2 chosen items rearrange in 2! = 2 × 1 = 2 ways (AB, BA).

- 3 chosen items rearrange in 3! = 3 × 2 × 1 = 6 ways.

- k chosen items rearrange in k! ways.

For k = 2, “divide by 2” and “divide by 2!” happen to give the same number. Writing 2! reveals the pattern that keeps working as k grows.

4\. Extending to 3: Choosing 3 from {A, B, C, D}

Three labeled slots give 4 × 3 × 2 = 24 ordered arrangements. Each group of three letters, such as {A, B, C}, appears in 3! = 6 orders:

|     |     |     |
|-----|-----|-----|
| ABC | BAC | CAB |
| ACB | BCA | CBA |

C(4,3) = 24 / 3! = 24 / 6 = 4

The four unique groups are ABC, ABD, ACD, and BCD — exactly the four boxed entries on the second whiteboard.

> **Whiteboard label check:** The second whiteboard reads “Per = Comb / 3!”, with 4×3×2 = 24 labeled “Comb.” The labels are swapped. 24 is the permutation count, and the correct relationship is **Comb = Perm / 3!**, so 24 / 6 = 4 combinations. The arithmetic on the board is right; only the names need to trade places.

The general pattern

| **Choosing k items** | **Divide by** | **Because**               |
|----------------------|---------------|---------------------------|
| 2                    | 2! = 2        | 2 items rearrange 2 ways  |
| 3                    | 3! = 6        | 3 items rearrange 6 ways  |
| 4                    | 4! = 24       | 4 items rearrange 24 ways |

C(n,k) = n! / ( k! (n − k)! )

The n!/(n−k)! part is the shorthand for the slot-by-slot product (like 4 × 3 × 2). The k! below it removes the duplicate orderings.

5\. The Cookie Lineup and the Four Counting Patterns

Each student contributed a favorite cookie, giving n = 9 varieties. We count batches of k = 3 cookies.

| **Student** | **Cookie**                   |
|-------------|------------------------------|
| Student 1      | Peanut Butter                |
| Student 2      | Raspberry White Chocolate    |
| Student 7   | Chocolate Chip               |
| Student 3       | Macadamia Nut                |
| Student 4        | Sugar Cookie                 |
| Student 5       | Snickerdoodle                |
| Student 6     | Peanut Butter Chocolate Chip |
| Student 8   | S'mores Cookie               |
| Jeremy      | Twix Ice Cream Cookie        |

Two yes/no decisions produce four different questions: **Does order matter?** and **Are repeats allowed?**

Case 1 — Order does not matter, no repeats (Combination)

Story: a plain cookie box with one of each flavor. Once the lid closes, the order you dropped them in is gone.

- Slot by slot: 9 × 8 × 7 = 504 ordered picks.

- Each batch like {PB, Choc, Sugar} was counted 3! = 6 times.

- 504 ÷ 6 = **84** unique batches.

C(9,3) = 9! / (3! · 6!) = 362,880 / (6 · 720) = 84

Case 2 — Order matters, no repeats (Permutation)

Story: the box has FRONT, MIDDLE, and BACK compartments. Which cookie sits where makes it a different batch.

- Keep all orderings — no dividing: 9 × 8 × 7 = **504**.

P(9,3) = 9! / 6! = 504

- Key link to Case 1: Permutations = Combinations × k!, so 504 = 84 × 6.

Case 3 — Order does not matter, repeats allowed (Combination with repetition)

Story: plain box again, but we baked plenty of every flavor. Three Peanut Butter cookies is a legal batch.

C(n + k − 1, k) = C(11, 3) = 165

This formula comes from Stars and Bars, developed in Section 7.

Case 4 — Order matters, repeats allowed (Permutation with repetition)

Story: labeled compartments and unlimited supply. Every slot independently has 9 choices.

n^k = 9 × 9 × 9 = 9³ = 729

Summary map (n = 9, k = 3)

|                       | **No repeats** | **Repeats allowed**          |
|-----------------------|----------------|------------------------------|
| Order does NOT matter | C(9,3) = 84    | C(11,3) = 165 (Stars & Bars) |
| Order DOES matter     | P(9,3) = 504   | 9³ = 729                     |

Python's itertools library has one generator for each cell:

| **Case**                    | **itertools function**                    |
|-----------------------------|-------------------------------------------|
| Combination                 | combinations(cookies, k)                  |
| Permutation                 | permutations(cookies, k)                  |
| Combination with repetition | combinations_with_replacement(cookies, k) |
| Permutation with repetition | product(cookies, repeat=k)                |

6\. Other Ways to Bake This Potato

- **Circular arrangements:** If k cookies are placed around a round tray where rotations look the same, each arrangement is counted k times by rotation, so the count is P(n,k) / k. For n = 9, k = 3: 504 / 3 = 168.

- **Derangements:** How many ways can items be rearranged so that none lands in its original spot? (The classic hat-check problem.)

- **Multinomial counting:** When some items are identical (for example, 2 PB and 1 Sugar to be ordered), divide by the factorial of each repeated group: 3! / (2! · 1!) = 3 orderings.

> **Correction:** In class the circular formula was given as (n−1)!/(n−k)!. That is only right when every item is used (k = n). The general version for choosing k of n is P(n,k)/k = n! / (k · (n−k)!).

7\. Stars and Bars from First Principles

The stars_and_bars.py program tells this as a seven-chapter story, pausing between chapters so the class can talk through each step.

Chapter 1 — Two jars, three identical cookies

List them by hand: (3,0), (2,1), (1,2), (0,3). Four ways. Easy — but listing will not scale to 9 flavors.

Chapter 2 — Give the things names

Let ★ be a cookie and │ be a wall between jars. Stars left of the wall go in Jar A; stars to the right go in Jar B.

A=3, B=0 ★ ★ ★ │

A=2, B=1 ★ ★ │ ★

A=1, B=2 ★ │ ★ ★

A=0, B=3 │ ★ ★ ★

Every split is a row of 4 symbols with 3 stars. Counting splits is the same as asking which 3 of 4 positions hold a star: C(4,3) = 4.

Chapter 3 — Why exactly n − 1 bars?

Jars are rooms in a row; bars are the interior walls. A hallway of 10 rooms has 9 walls between them. So the symbol row always has k stars + (n − 1) bars = **k + n − 1** positions.

Chapter 4 — Three jars, two cookies

2 stars + 2 bars = 4 positions, so C(4,2) = 6 arrangements, including new splits like one cookie in Jar A and one in Jar C.

★ ★ │ │ → 2 in A

★ │ ★ │ → 1 in A, 1 in B

★ │ │ ★ → 1 in A, 1 in C

│ ★ ★ │ → 2 in B

│ ★ │ ★ → 1 in B, 1 in C

│ │ ★ ★ → 2 in C

Chapter 5 — The formula locks in

Ways = C(k + n − 1, k) = (k + n − 1)! / ( k! (n − 1)! )

| **n bins** | **k stars** | **Positions** | **Formula** | **Answer** |
|------------|-------------|---------------|-------------|------------|
| 2          | 3           | 4             | C(4,3)      | 4          |
| 3          | 2           | 4             | C(4,2)      | 6          |
| 4          | 3           | 6             | C(6,3)      | 20         |
| 9          | 3           | 11            | C(11,3)     | 165        |
| 9          | 10          | 18            | C(18,10)    | 43,758     |

Chapter 6 — Back to the bakery

The jars become nine flavor bins (Student 1's PB through Jeremy's Twix). Three stars and eight bars make 11 positions. The batch “1 Peanut Butter + 2 Chocolate Chip” is:

★ │ │ ★ ★ │ │ │ │ │ │

bin 1 (PB) has 1 star, bin 2 (Raspberry) has 0, bin 3 (Choc Chip) has 2, all others 0

Choosing which 3 of 11 positions are stars gives C(11,3) = 165 batches — matching Case 3.

Chapter 7 — The big picture

Each step below is a perfect one-to-one translation; nothing is added or lost:

1.  A batch of k cookies with repeats allowed, order ignored

2.  is a distribution of k cookies into n flavor bins,

3.  is an arrangement of k stars and n − 1 bars,

4.  is a choice of k positions out of k + n − 1,

5.  which is C(k + n − 1, k).

Compare Case 1, C(9,3) = 84, with Case 3, C(11,3) = 165. The pool grew from 9 to 9 + 3 − 1 = 11. Those extra k − 1 = 2 positions are exactly the room the repeated choices need.

> **Correction:** The stars_and_bars.py summary text says Stars and Bars fills the “bottom-left cell” of the 2×2 table. In the table as printed, it is the **top-right** cell (order does not matter, repeats allowed).

8\. The Code Artifacts

| **File**           | **Purpose**                                                                                                                                                                         |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| cookie_counting.py | Narrated walk through all four cases for the cookie lineup, with Press Enter pauses, slot-by-slot derivations, sample batches, and a summary table. Change k at the top to explore. |
| stars_and_bars.py  | Seven-chapter Stars and Bars story, from two jars to 165 cookie batches, with generated star-bar strings translated into real batches.                                              |

Run from PowerShell in the week folder:

cd C:\Users\<you>\git\discrete_structures_and_critical_thinking\week-09

python .\cookie_counting.py

python .\stars_and_bars.py

Core helper that turns a star-bar string into bin counts:

def bins_from_symbols(symbols):

bins, count = \[\], 0

for s in symbols:

if s == STAR:

count += 1

else: \# a BAR ends the current bin

bins.append(count)

count = 0

bins.append(count) \# last bin has no bar after it

return bins

Small polish items for the next commit: the first cookie_counting.py printed “batchs” (fixed in the narrated version), and the bin-label caret line in Chapter 6 of stars_and_bars.py does not align under the stars.

9\. Prediction and Discussion Prompts

1.  Before running: predict all four counts for n = 4, k = 2. Then set the values in cookie_counting.py and check.

2.  Why does Case 4 always produce the largest count?

3.  For k = 1, why do all four cases give the same answer?

4.  Pick an arrangement of ★ and │ for n = 9, k = 3 and translate it into a cookie batch. Trade with a neighbor and translate theirs back.

5.  Is there any star-bar row that corresponds to two different batches? Why does the answer matter for the formula being correct?

6.  Using the whiteboard, explain in one sentence why the divisor is k! and not just k.

10\. Key Takeaways

- Count slots first with the multiplication principle; formulas come second.

- Dividing by k! removes the orderings of a chosen group that the slot count treated as different.

- Permutation = Combination × k!.

- Repeats allowed + order ignored → Stars and Bars → C(n + k − 1, k).

- Repeats allowed + order matters → n^k, the least restricted case.
