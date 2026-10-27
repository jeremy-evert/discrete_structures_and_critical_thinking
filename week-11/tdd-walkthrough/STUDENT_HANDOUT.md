# Handout — Relations in your tests (one page)

**Why test first?** A smoke alarm has a test button: you press it *before* the fire. A test written first is the button. If it has never been red, you don't know it can ring.
**Every step, same loop:** **Predict** (write your guess) → **Run** (see red or green) → **Explain** (say why). Red is normal and good.

**Four questions about any rule that pairs things** (example: "sits next to"):
1. **Reflexive**: is everything paired with itself? (Is a seat next to itself? No.)
2. **Symmetric**: if A goes with B, does B go with A? (Yes: neighbours.)
3. **Antisymmetric**: if A↔B both ways, must A and B be the same? (No: Ana↔Ben, different.)
4. **Transitive**: A~B and B~C, so A~C? (No: Ana-Ben, Ben-Cy, but Ana is not next to Cy.)
For every **no**, find a **witness**: the exact pair or triple that breaks it.

| Kind | Needs | Real-world picture |
|---|---|---|
| **Equivalence** | reflexive + symmetric + transitive | groups: same grade bin, same person, same birthday month |
| **Partial order** | reflexive + antisymmetric + transitive | "comes before": build order, test order, divides |

**Our project: merging duplicate records.** Jon Smith, John Smith, Jonathan Smith. "Looks alike" says Jon~John and John~Jonathan but **not** Jon~Jonathan: **not transitive** (witness: those three). Fix: turn every name into a **canonical key** (one standard spelling) and compare keys: equal keys always form an equivalence.

**Glossary:** *test* checks one claim, pass or fail · *assert* "this must be true" · *red/green* fail/pass · *TDD* test first, see red, code, see green · *stub* placeholder · *fixture* fixed sample data · *relation* which pairs go together · *ordered pair* (A,B)≠(B,A) · *equivalence* groups · *partial order* what comes before what · *partition/bin* inputs that behave the same · *boundary* edge of a bin (59|60) · *property test* checks a rule over many items · *witness/counterexample* the pair or triple that breaks a rule · *canonical key* standard spelling · *design smell* sign that the structure should change · *dependency* a function another function needs.

**Concept map**
| Concept | Real-world meaning | Test form | Bug it catches |
|---|---|---|---|
| Bins & boundaries | scores that get the same grade | one test per bin + both sides of each edge | off-by-one at 59/60, 89/90, 100/101 |
| Reflexive | a thing matches itself | `reflexive_failure` returns None | a rule that excludes identical items |
| Symmetric | A matches B ⇒ B matches A | swap the arguments | one-sided "equals" (missing email as wildcard) |
| Antisymmetric | no two different items each "before" the other | `antisymmetric_failure` returns None | comparator returning 0 for different records |
| Transitive | match chains agree | `transitive_failure` returns None | fuzzy "looks alike" (Jon/John/Jonathan) |
| Partial order | depends-on / comes-before | test leaves first; closure is antisymmetric | dependency cycle (no first thing to test) |
| Witness | proof for a "no" | the failing test prints it | vague "it's broken" |

**Self-check:** I can say why red comes first · draw a relation as pairs · ask the four questions and give a witness · tell equivalence from partial order · explain why Jon/John/Jonathan breaks transitivity.
