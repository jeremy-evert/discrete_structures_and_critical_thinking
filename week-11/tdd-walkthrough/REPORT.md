# Anna report: DSCT "relations in your tests" walkthrough (Tuesday demonstration lane)

Run id 9042e7e5729a6a5788f14dcb4189ab0b · branch `anna/dsct-tdd-relations-20261027` · terminal state: **HUMAN_GATE / partial** (core verified; items below still open).
No Canvas writes, no student data (synthetic names only), no merge to main. Python 3.12 tested; code uses no 3.10+ syntax (no match, no `X | Y` types, no builtin generics) but **3.9 was not executed** (no 3.9 interpreter on April).

## Finished and verified (as of this report)
- Project `week-11/tdd-walkthrough/` with 19-tag commit ladder (`tdd-step-01..19`), `tools/ladder_check.sh` (clean-clone per-tag pytest), `tools/recover.sh`.
- Prompts `prompts/00..14`, `STEPS.md`, `reference/demos/`, `INSTRUCTOR_GUIDE.md`, `STUDENT_HANDOUT.md`, `CONCEPT_MAP.md`.
- Dry run of prompts 00–14 by an independent Sonnet agent with no access to the reference.

## Ladder output per tag (tools/ladder_check.sh, throwaway clone)
```
tdd-step-01 | 13 failed in 0.06s | RED letter_grade bins and boundaries (stub)
tdd-step-02 | 13 passed in 0.04s | GREEN letter_grade
tdd-step-03 | 15 passed in 0.05s | GREEN-from-start: 'same bin' is an equivalence relation (characterization)
tdd-step-04 | 3 failed, 15 passed in 0.06s | RED fuzzy name match: Jon ~ John ~ Jonathan
tdd-step-05 | 18 passed in 0.05s | GREEN similar_names: edit distance, threshold 0.5
tdd-step-06 | 1 failed, 20 passed in 0.06s | RED same_person must be transitive: counterexample Jon / John / Jonathan
tdd-step-07 | 23 passed in 0.06s | GREEN same_person via canonical key (a true equivalence)
tdd-step-08 | 3 failed, 23 passed in 0.06s | RED group names by chains of matches
tdd-step-09 | 26 passed in 0.06s | GREEN union-find grouping (connected components)
tdd-step-10 | 1 failed, 27 passed in 0.06s | RED is_duplicate must be symmetric
tdd-step-11 | 28 passed in 0.06s | GREEN is_duplicate: emails must be equal, so a and b are interchangeable
tdd-step-12 | 2 failed, 29 passed in 0.06s | RED order must be antisymmetric: ties on family name
tdd-step-13 | 31 passed in 0.06s | GREEN compare uses a unique key (family, given, id)
tdd-step-14 | 3 failed, 31 passed in 0.07s | RED merge_duplicates end to end
tdd-step-15 | 34 passed in 0.06s | GREEN merge_duplicates: group by key, merge each group
tdd-step-16 | 3 failed, 34 passed in 0.07s | RED dependency graph of our own code, test order leaves first
tdd-step-17 | 37 passed in 0.06s | GREEN build_graph from the AST, leaves_first by depth-first walk
tdd-step-18 | 1 failed, 38 passed in 0.07s | RED a dependency cycle must be detected
tdd-step-19 | 39 passed in 0.06s | GREEN leaves_first raises CycleError naming the loop
```
Red at every RED tag, green at every GREEN tag, final `tdd-step-19` all green (39 passed). Step 18 has one red test (the closure-antisymmetry test already passes; stated in prompt 14).

## Dry run of prompts (independent Claude, verbatim fenced blocks only)
Final live folder: 48 passed. 21 of 23 phases matched on first run; two partial.

| Prompt | Phase | Actual outcome | Match | Fix applied |
|---|---|---|---|---|
| 00 | a | replied "ready" | yes | none |
| 01 | a | `python` not found (only `python3`); digraph printed one line per pair | partial | prompts now say `python3`; digraph wording "Ben -> Ana, Cy" |
| 02 | a | witnesses Ana; (Ana,Ben); (Ana,Ben,Ana); (1,2) as expected | yes | `python3`; import wording "from seating import ..." |
| 03 | a | equivalence, partial order, partial order, neither, neither | yes | `python3` |
| 04 | a / b | 17 red NotImplementedError / 17 green, bins correct | yes / yes | none |
| 05 | a | 21 passed at once | yes | none |
| 06 | a / b | new tests red / green; Jon~John T, Jon~Jonathan F, John~Jonathan T | yes / yes | none |
| 07 | a | exactly 1 failed (transitive) with the Jon/John/Jonathan message | yes | prompt now says to use an explicit assert message |
| 08 | a | green; keys jonathan smith x3, maya smith, maria garcia | yes | none (counterexample test file left to Claude) |
| 09 | a / b | red / green; 3 groups | yes / yes | none |
| 10 | a / b | exactly 1 red (symmetric) / green; prints False False | yes / yes | none |
| 11 | a / b | 2 red (antisymmetric, shuffle) / green | yes / yes | none |
| 12 | a / b | 3 red / green; 4 merged, ids (2,3) | yes / yes | none |
| 13 | a / b | 3 red / green; graph correct; order not unique, did not end on merge_duplicates | partial | expectation loosened in prompt 13 |
| 14 | a / b | 1 red (DID NOT RAISE) / green; "dependency cycle: parse -> validate -> parse" | yes / yes | none |

**Limit:** the wording fixes above were made after the dry run and were **not re-run**. Slide-prompt verbatim dry run (REVISION 2) is for the deck: the on-slide prompts must be the fenced blocks in `prompts/`; that table belongs to the deck session's report.

## Open / not done
- Fresh-eyes plain-language read of guide and handout (REVISION 4): **not yet done**.
- Glossary completeness against the final deck: **not yet done** (deck is another session).
- Slide-number cross references in the guide: pending the deck's index.
- Thursday student workbook and facilitator page: **Ivy's lane** (REVISION 5); not built here. Reconciliation with `week-11/instructor/thursday-run-of-show.md` is Ivy's to report; this lane flags that the full path (about 96 min) exceeds one 75-minute class (guide section 5 gives a core cut).
- Python 3.9 not executed.

## Decisions for Flo / Jeremy
1. Whether the walkthrough runs Tuesday-style in one class (core cut), over two sessions, or Thursday/later week.
2. Names used in the fuzzy rule: threshold 0.5 edit-distance closeness, chosen because `difflib.SequenceMatcher` is not symmetric (it would add an unintended symmetry bug at the transitivity step).
