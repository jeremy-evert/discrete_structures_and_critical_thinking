# Concept map

| Concept | Real-world meaning | Test form | Bug it catches |
|---|---|---|---|
| Bins & boundaries | scores that get the same grade | one test per bin + both sides of each edge | off-by-one at 59/60, 89/90, 100/101 |
| Reflexive | a thing matches itself | `reflexive_failure` returns None | a rule that excludes identical items |
| Symmetric | A matches B ⇒ B matches A | swap the arguments | one-sided "equals" (missing email as wildcard) |
| Antisymmetric | no two different items each "before" the other | `antisymmetric_failure` returns None | comparator returning 0 for different records |
| Transitive | match chains agree | `transitive_failure` returns None | fuzzy "looks alike" (Jon/John/Jonathan) |
| Partial order | depends-on / comes-before | test leaves first; closure is antisymmetric | dependency cycle (no first thing to test) |
| Witness | proof for a "no" | the failing test prints it | vague "it's broken" |
