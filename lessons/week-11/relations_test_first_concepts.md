# Relations as tests: case first, test second, word last

**Week 11, Thursday · all names and data are made up · Python 3.9+, standard library only**

Every idea here comes in the same order: **a concrete case, then a test you can run on it, then the word.** A *relation* is just a set of pairs, so every test below takes two things: the list of `items`, and the set of `pairs` that are in the relation. Each test answers **True** or **False**. You can run a test on paper (look at the pairs) or in Python.

Check that everything on this page is correct (it runs every example and every claim, and prints a count):

```bash
python3 relations_test_first_check.py
```

It should end with `ALL CHECKS PASSED` and exit code 0. If it does not, tell us: that is our mistake, not yours.

**How to read a pair.** `Ana->Ben` means the ordered pair (Ana, Ben): Ana first, Ben second. (Ana, Ben) and (Ben, Ana) are two different pairs; a relation can contain one, both, or neither.

Each example below comes with a small data block. That block is exactly what `relations_test_first_check.py` reads, so the claim you see and the claim that is checked cannot drift apart.

---

## 0. Warm-up (10 minutes): three names, one question

**Write your answer before reading on:** *Jon looks like John. John looks like Jonathan. Must Jon look like Jonathan?* Yes, no, or it depends. (One line, on paper.)

**The case.** A messy list has Jon Smith, John Smith, Jonathan Smith, and Dee (last initial L). Our rough rule, "looks alike", says Jon and John look alike, and John and Jonathan look alike, but it does not say Jon and Jonathan look alike (as written down, they are too different). Every item also looks like itself.

```case
id: looks_alike
items: Jon John Jonathan Dee
pairs: Jon->Jon John->John Jonathan->Jonathan Dee->Dee Jon->John John->Jon John->Jonathan Jonathan->John
expect: reflexive=T symmetric=T antisymmetric=F transitive=F asymmetric=F equivalence=F partial_order=F
witness: transitive=Jon,John,Jonathan antisymmetric=Jon,John
demo: transitive=fail equivalence=fail
```

**The test (one chain).** Is `Jon->John` in? Yes. Is `John->Jonathan` in? Yes. Is `Jon->Jonathan` in? **No.** The chain Jon, John, Jonathan breaks the rule "if a goes with b and b goes with c, then a goes with c". That triple is the **witness**: the three actual items that make the answer No. So your answer to the opening question is: *it depends on the rule, and for "looks alike" the answer is no.*

**The repair: change the rule.** Instead of "looks alike", ask "has the same last initial". Jon, John and Jonathan all have last initial S; Dee has L.

```case
id: same_last_initial
items: Jon John Jonathan Dee
pairs: Jon->Jon Jon->John Jon->Jonathan John->Jon John->John John->Jonathan Jonathan->Jon Jonathan->John Jonathan->Jonathan Dee->Dee
expect: reflexive=T symmetric=T antisymmetric=F transitive=T asymmetric=F equivalence=T partial_order=F
demo: equivalence=pass
```

Try every chain: there is no a->b and b->c where a->c is missing, because "same initial" is a fact about each item, not about the pair. Same initial always splits the list into clean groups: {Jon, John, Jonathan} and {Dee}.

**A different kind of rule: "is a prerequisite for".** Three made-up courses: CS1 comes before CS2, CS2 comes before Algo. If the list records only the *direct* steps:

```case
id: prereq_direct
items: CS1 CS2 Algo
pairs: CS1->CS2 CS2->Algo
expect: reflexive=F symmetric=F antisymmetric=T transitive=F asymmetric=T equivalence=F partial_order=F
witness: transitive=CS1,CS2,Algo
```

Chain CS1, CS2, Algo: `CS1->Algo` is missing, so the list is *not* chain-closed. Now say what you really mean, "comes before **or is the same as**", and fill in every chain:

```case
id: prereq_or_equal
items: CS1 CS2 Algo
pairs: CS1->CS1 CS2->CS2 Algo->Algo CS1->CS2 CS2->Algo CS1->Algo
expect: reflexive=T symmetric=F antisymmetric=T transitive=T asymmetric=F equivalence=F partial_order=T
demo: transitive=pass
```

(Ordinary English "is a prerequisite for" does not pair a course with itself, which is why we say "before or equal" when we want that property.) This rule is the opposite of "same initial": it has a direction.

The tests are taken one at a time below, each with the same shape: **case, test, word, one that passes, one that fails, one plain sentence.**

---

## How the tests are written

Each test below is one line of Python over `items` and `pairs`. You will see it right after its case, **before** its word. When you meet the word, you also meet the function name; every function is in `relations_test_first_check.py`, takes `(items, pairs)`, and returns True or False.

---

## 1. Does everything match itself?

**The case.** Three people. Rule one: "has the same birthday month as". Ana and Ben were both born in March; Cy in July. Rule two: "sits next to", in a row of seats Ana, Ben, Cy.

**The test.** For every item `a`, is `(a, a)` in the set?

```python
all((a, a) in pairs for a in items)
```

```case
id: same_month
items: Ana Ben Cy
pairs: Ana->Ana Ben->Ben Cy->Cy Ana->Ben Ben->Ana
expect: reflexive=T symmetric=T antisymmetric=F transitive=T asymmetric=F equivalence=T partial_order=F
demo: reflexive=pass symmetric=pass
```

```case
id: next_to
items: Ana Ben Cy
pairs: Ana->Ben Ben->Ana Ben->Cy Cy->Ben
expect: reflexive=F symmetric=T antisymmetric=F transitive=F asymmetric=F equivalence=F partial_order=F
witness: reflexive=Ana transitive=Ana,Ben,Cy antisymmetric=Ana,Ben asymmetric=Ana,Ben
demo: reflexive=fail symmetric=pass asymmetric=fail
```

**Passes (same_month).** Check each item: `Ana->Ana` in, `Ben->Ben` in, `Cy->Cy` in. All three present: **True**.
**Fails (next_to).** Check each item: `Ana->Ana`? Not in the set (no seat is next to itself). **False.** Witness: Ana.

**The word:** this is called **reflexive** (`is_reflexive` in the checker).
**In plain language:** *every item is paired with itself.*

---

## 2. If it goes one way, does it go back?

**The case.** "Sits next to" again, and a second rule, "has sent a message to". Ana sent a message to Ben, Ben sent one to Cy, Cy sent one back to Ben. Nobody wrote to Ana.

**The test.** For every pair `(a, b)` in the set, is `(b, a)` also in the set?

```python
all((b, a) in pairs for (a, b) in pairs)
```

**Passes (next_to).** The pairs are `Ana->Ben`, `Ben->Ana`, `Ben->Cy`, `Cy->Ben`. Take each one and flip it: `Ben->Ana` in, `Ana->Ben` in, `Cy->Ben` in, `Ben->Cy` in. **True.**

```case
id: messaged
items: Ana Ben Cy
pairs: Ana->Ben Ben->Cy Cy->Ben
expect: reflexive=F symmetric=F antisymmetric=F transitive=F asymmetric=F equivalence=F partial_order=F
witness: symmetric=Ana,Ben transitive=Ana,Ben,Cy antisymmetric=Ben,Cy
demo: symmetric=fail
```

**Fails (messaged).** Take `Ana->Ben` and flip it: `Ben->Ana`? Not in the set. **False.** Witness: the pair Ana, Ben.

**The word:** this is called **symmetric** (`is_symmetric`).
**In plain language:** *whenever a is paired with b, b is paired with a too.*

---

## 3. Can two different things each come "before" the other?

**The case.** "Is at most as old as". Ana is 19, Ben is 20, Cy is 21. Every person is at most as old as themselves, and Ana is at most as old as Ben, and so on up the line. Now change the case: Dee is also 19, same as Ana.

**The test.** Look at each pair `(a, b)` that also has `(b, a)` in the set. Are `a` and `b` the same item?

```python
all(a == b for (a, b) in pairs if (b, a) in pairs)
```

```case
id: at_most_as_old
items: Ana Ben Cy
pairs: Ana->Ana Ben->Ben Cy->Cy Ana->Ben Ana->Cy Ben->Cy
expect: reflexive=T symmetric=F antisymmetric=T transitive=T asymmetric=F equivalence=F partial_order=T
witness: symmetric=Ana,Ben asymmetric=Ana,Ana
demo: antisymmetric=pass partial_order=pass
```

```case
id: tie_ages
items: Ana Dee Cy
pairs: Ana->Ana Dee->Dee Cy->Cy Ana->Dee Dee->Ana Ana->Cy Dee->Cy
expect: reflexive=T symmetric=F antisymmetric=F transitive=T asymmetric=F equivalence=F partial_order=F
witness: symmetric=Ana,Cy antisymmetric=Ana,Dee
demo: antisymmetric=fail partial_order=fail
```

**Passes (at_most_as_old).** Which pairs have their flip in the set? Only the self-pairs `Ana->Ana`, `Ben->Ben`, `Cy->Cy`, and each has `a == b`. `Ana->Ben` has no flip (`Ben->Ana` is missing), so it is not checked. **True.**
**Fails (tie_ages).** `Ana->Dee` has its flip `Dee->Ana` in the set, and Ana is not Dee. **False.** Witness: Ana, Dee (the two 19-year-olds).

**The word:** this is called **antisymmetric** (`is_antisymmetric`).
**In plain language:** *if a goes with b and b goes with a, then a and b must be the same item, so a tie between two different items is not allowed.*

**Careful: antisymmetric is not "the opposite of symmetric".** A relation can be both. Two people paired only with themselves:

```case
id: only_self
items: Ana Ben
pairs: Ana->Ana Ben->Ben
expect: reflexive=T symmetric=T antisymmetric=T transitive=T asymmetric=F equivalence=T partial_order=T
```

Every pair's flip is in the set (symmetric: True) and every pair with a flip has `a == b` (antisymmetric: True).

---

## 4. Do chains close up?

**The case.** You already saw it in the warm-up. Jon looks like John, John looks like Jonathan, does Jon look like Jonathan? And: CS1 comes before CS2, CS2 comes before Algo, so does CS1 come before Algo?

**The test.** For every pair of pairs that chain, `(a, b)` and `(b, d)` both in the set, is the shortcut `(a, d)` in the set?

```python
all((a, d) in pairs for (a, b) in pairs for (c, d) in pairs if b == c)
```

(The `if b == c` just means "the second item of the first pair is the first item of the second pair".)

**Passes (prereq_or_equal).** Pairs `CS1->CS2` and `CS2->Algo` chain: is `CS1->Algo` in the set? Yes. (The self-pairs also chain: `CS1->CS1` then `CS1->CS2` needs `CS1->CS2`: in. All other chains are checked the same way.) **True.**
**Fails (looks_alike).** `Jon->John` and `John->Jonathan` chain: is `Jon->Jonathan` in the set? No. **False.** Witness: Jon, John, Jonathan.

**The word:** this is called **transitive** (`is_transitive`).
**In plain language:** *if a goes with b and b goes with c, then a goes with c.*

---

## 5. Only if there is time: can a pair point at itself, or both ways?

**The case.** "Is an ancestor of": Ana is Ben's parent, Ben is Cy's parent, so Ana is Cy's grandparent and ancestor too. Nobody is their own ancestor ("I am not my own grandpa"), and no two people are each other's ancestors.

**The test.** For every pair `(a, b)` in the set, is `(b, a)` **not** in the set? (Including `a == b`: for `(a, a)` the flip is itself.)

```python
all((b, a) not in pairs for (a, b) in pairs)
```

```case
id: ancestor_of
items: Ana Ben Cy
pairs: Ana->Ben Ben->Cy Ana->Cy
expect: reflexive=F symmetric=F antisymmetric=T transitive=T asymmetric=T equivalence=F partial_order=F
witness: reflexive=Ana symmetric=Ana,Ben
demo: asymmetric=pass
```

**Passes (ancestor_of).** Flip `Ana->Ben`: `Ben->Ana` not in. Flip `Ben->Cy`: `Cy->Ben` not in. Flip `Ana->Cy`: `Cy->Ana` not in. **True.**
**Fails (next_to).** Flip `Ana->Ben`: `Ben->Ana` is in. **False.** (A pair paired with itself, like `Ana->Ana`, also fails, because its flip is itself.)

**The word:** this is called **asymmetric** (`is_asymmetric`).
**In plain language:** *no pair ever points both ways, and nothing points at itself.* (This is "antisymmetric, and also nothing is paired with itself". The checker proves that statement on all 512 relations over 3 items.)

---

## 6. Named goal: a rule with a direction ("comes before or is equal to")

**The case.** Four numbers, 1, 2, 3, 6, and the rule "divides": 2 divides 6, 3 divides 6, 1 divides everything, every number divides itself. Notice 2 and 3: neither divides the other. Nothing says every two items have to be comparable.

```case
id: divides
items: 1 2 3 6
pairs: 1->1 1->2 1->3 1->6 2->2 2->6 3->3 3->6 6->6
expect: reflexive=T symmetric=F antisymmetric=T transitive=T asymmetric=F equivalence=F partial_order=T
witness: symmetric=1,2 asymmetric=1,1
demo: partial_order=pass
```

**The test.** Run three tests: `is_reflexive`, `is_antisymmetric`, `is_transitive`. All **True**? Then:

```python
is_reflexive(items, pairs) and is_antisymmetric(items, pairs) and is_transitive(items, pairs)
```

**Passes (divides).** Reflexive: all four self-pairs are in. Antisymmetric: no pair has its flip except the self-pairs. Transitive: for example `1->2` then `2->6` needs `1->6`: in. **True.**
**Fails (a loop of prerequisites).** If CS1 needs CS2, CS2 needs Algo, and Algo needs CS1, then once every chain is filled in, everything is paired with everything:

```case
id: cycle
items: CS1 CS2 Algo
pairs: CS1->CS1 CS1->CS2 CS1->Algo CS2->CS1 CS2->CS2 CS2->Algo Algo->CS1 Algo->CS2 Algo->Algo
expect: reflexive=T symmetric=T antisymmetric=F transitive=T asymmetric=F equivalence=T partial_order=F
witness: antisymmetric=CS1,CS2
demo: partial_order=fail
```

`CS1->CS2` has its flip `CS2->CS1`, and CS1 is not CS2: antisymmetric is **False**, so the partial-order test is **False**. (A loop means there is no first thing to do.)

**The word:** a relation that passes this test is a **partial order** (`is_partial_order`).
**In plain language:** *a way of saying "comes before or is the same as", where nothing can come before itself through a loop, and some pairs may not be comparable at all.*

The other named kind: a relation where the reflexive, symmetric and transitive tests are all True together (like "same last initial") is an **equivalence relation** (`is_equivalence`; `same_last_initial`, `same_month`): it sorts the items into groups.

---

## Quick reference

| Word | The test (True or False) | Passes | Fails | In plain language |
|---|---|---|---|---|
| reflexive | every `(a, a)` is in the set | same_month | next_to (Ana) | everything pairs with itself |
| symmetric | every pair's flip is in the set | next_to | messaged (Ana, Ben) | if it goes one way, it goes back |
| antisymmetric | any pair with its flip has `a == b` | at_most_as_old | tie_ages (Ana, Dee) | no tie between two different things |
| transitive | every chain's shortcut is in the set | prereq_or_equal | looks_alike (Jon, John, Jonathan) | chains close up |
| asymmetric (if time) | no pair's flip is in the set | ancestor_of | next_to | nothing points both ways or at itself |
| partial order (goal) | reflexive and antisymmetric and transitive | divides | cycle (CS1, CS2) | "before or equal", with some pairs unrelated |
| equivalence | reflexive and symmetric and transitive | same_last_initial | looks_alike | groups of things that count as the same |

**Use it Thursday.** For any rule you are given: write out its pairs, ask the questions in this order (reflexive, symmetric, antisymmetric, transitive), and for every **False** write the witness: the actual pair or triple that breaks it.
