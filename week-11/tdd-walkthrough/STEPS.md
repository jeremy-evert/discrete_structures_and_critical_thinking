# STEPS — the agreed step list (Tuesday demonstration; Thursday students repeat on a parallel problem)

Every step runs the same 3-beat loop: **Predict** (30 seconds, write a guess), **Run** (paste the prompt, run pytest), **Explain** (say why it came out that way). Red tests are normal and good.
Prompts are in `prompts/NN_slug.md`; the text inside the fenced ` ```prompt-a ` / ` ```prompt-b ` blocks is the exact paste (A = red or only prompt, B = green). Recovery tags are `tdd-step-NN` (`tools/recover.sh NN`).
Fallback reference demos: `reference/demos/*.py` (prompts 01–03).

| Prompt | Step name | Concept shown (plain words first) | Principle tag | Outcome you should see | Ladder tags |
|---|---|---|---|---|---|
| 00 | Session rules | Work in tiny test-first steps | — | Claude replies "ready" | — |
| 01 | Seating relation | A relation is a list of pairs; matrix; digraph | — (concept) | 8 pairs, symmetric matrix, arrows | demo |
| 02 | Property checker | Four yes/no questions, each with a witness | witness/counterexample | table of holds/FAILS with witnesses | demo |
| 03 | Classify relations | Equivalence vs partial order vs neither | equivalence vs partial order | verdict column: equiv, order, order, neither, neither | demo |
| 04 | letter_grade bins | Same-bin scores behave alike; test each bin and each edge | equivalence partitioning, boundaries | A red (NotImplemented) then green; bins printed | 01 red, 02 green |
| 05 | Same bin is an equivalence | Reflexive, symmetric, transitive checked by code; reusable `relations.py` | R/S/T property tests | passes first run (a recorded fact) | 03 green |
| 06 | Fuzzy name match | First rule for "same person": names that look alike | partitioning | red, then green; Jon~Jonathan prints False | 04 red, 05 green |
| 07 | Transitivity counterexample | The fuzzy rule is not transitive: Jon/John/Jonathan | transitive test, witness | exactly 1 red with the three names | 06 red |
| 08 | Canonical key fix | Normalize to a key; equal keys are an equivalence | partitioning, witness (kept) | all green; keys printed | 07 green |
| 09 | Group by chains | Union-find alternative and its over-merge tradeoff | partitioning, witness | red, then green; 3 groups | 08 red, 09 green |
| 10 | Symmetric equals | A one-sided "equals" caught by a swap test | reflexive + symmetric tests, witness | 1 red (symmetric), then green | 10 red, 11 green |
| 11 | Antisymmetric sort | Comparator returning 0 for different items | antisymmetric test, witness | 2 red, then green | 12 red, 13 green |
| 12 | merge_duplicates | Everything combines; classes become merged records | partitioning | 3 red, then green; 4 merged records | 14 red, 15 green |
| 13 | Dependency order | "Depends on" is a partial order; test leaves first | partial-order test ordering | 3 red, then green; order printed | 16 red, 17 green |
| 14 | Cycle smell | A cycle breaks antisymmetry; no leaf to test first | antisymmetric test, order, witness | cycle test red, then green; message printed | 18 red, 19 green |

Bridge to Thursday: Tuesday = prompts 00–14 by Jeremy. Thursday = the same loop on a parallel problem (Ivy's student workbook).
