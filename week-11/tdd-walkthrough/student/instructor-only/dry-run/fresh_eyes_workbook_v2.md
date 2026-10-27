# Fresh-eyes review: Thursday Workbook + Glossary

Reader model: first-year student, shaky on unit testing, TDD and abstract math. Only WORKBOOK.md and GLOSSARY.md were read.
"Gloss?" = does GLOSSARY.md cover it. A blanket "see the Glossary" line near the top exists (line 11), so I count a glossary entry only when the term is bolded in place or pointed to.

## Top 6 fixes (most damage first)

1. Step 03 table uses lengths 200, 204, 208 for "is within 5 seconds of". That is a near-exact Step 07 counterexample, and GLOSSARY "counterexample" repeats 200/204/208. Change both.
2. Beat 7 intro says "Test the pieces nothing else needs first". That is backwards. Leaves are pieces that need nothing else. It contradicts the glossary and the paper question below it.
3. The fast path (01, 06, 07, 08) skips Step 02 and Step 05, where reflexive, symmetric, transitive, equivalence relation and the witness finders are first defined. Step 07, Step 08 and C1 then use those words with no definition.
4. Many EXPLAIN and PREDICT questions are answered in the surrounding text (see section 3).
5. Glossary "Where you meet it" step numbers are wrong in many rows, and some glossary terms never appear in the workbook (see section 4).
6. The Step 04a edge and error-value instructions are ambiguous and contradict the prompt, which hard-codes -1 and 3601.

---

## 1. Terms or symbols not explained at or before first use

| Term / symbol | First used (where) | In GLOSSARY? | Suggested one-line definition |
|---|---|---|---|
| counterexample | Intro, line 9 ("the counterexample"); also A4 "witness finder" | Yes | An example that proves a rule wrong. Define it at the intro, or write "an example that breaks the rule". |
| "Tuesday's process" / "Tuesday's prompts" / "Step 00" | Intro; Part B preamble ("00 to 14") | No | Students absent Tuesday are lost. There is no Step 00 in this workbook. Say "you do not need Tuesday" and drop "00". |
| terminal | A4 step 1 | No | The text window where you type commands. |
| `python3 -m pytest -q`, `-q` | A3 table | No | Runs the tests. `-q` means short output. |
| `pip` | A4 step 2 | No | Python's installer for add-on tools. |
| "starter folder" | A4 step 1 | No | Say where to get it (Canvas? facilitator?). |
| program / code / file / folder / path (`playlist/track.py`) | A4 | No | Probably fine, but `a/b.py` means "file b.py inside folder a". |
| listing (vs Track vs song) | Intro quote | No | A "listing" is one Track entry in the playlist. One song can have several listings. Never defined. |
| tests/relations.py "helper" | A4 | Partly (witness finder) | A ready-made file that checks the four relation rules for you. |
| `demos/` folder | Step 01 prompt | No | Not in the A4 folder listing. Say Claude creates it. |
| matrix, diagonal, 4x4 | Step 01 | No | Matrix = grid of rows and columns. Diagonal = top-left to bottom-right squares. |
| "Standard library only" | Step 01 prompt | No | Use only what comes with Python; install nothing. |
| `sys.path`, "add tests/ to sys.path" | Step 02 prompt (and 03) | No | Tells Python where to look for files. Claude handles it; say "ignore this phrase". |
| witness | Step 02 (defined in place), but the A4 bullet "witness finder" uses it earlier | Yes | Defined at Step 02, used at A4. Move the definition up or add a forward note. |
| "holds" / "FAILS" | Step 02 prompt | No | holds = no counterexample; FAILS = counterexample found. |
| antisymmetric wording "must a and b be the same track?" | Step 02 | Yes | Very hard to read. Suggest "if both directions hold, the two ends are the same track". |
| `abs(100 - 106)` | Step 06a Stuck | No | abs = distance, ignoring minus signs. |
| `>`, `>=`, `<`, `<=`, `==` | Step 04b, 05, 06b | No | `>` greater than, `>=` greater or equal, `==` is equal to. |
| "up to but not including" | Step 04a table | No | Counts the start number but not the end number (0 yes, 180 no). |
| `pytest.mark.parametrize` | Step 04a prompt | No | A way to run one test for many values. Claude handles it. |
| "plain assert tests" | Step 04a prompt | Partly (assert) | Fine once assert is understood. |
| "edges" (of a bin) | Step 04a PREDICT | Boundary only | See ambiguities. |
| "lazy programmer" | Step 04a | No | Joke. Say "a rushed programmer". |
| "characterization test" | Step 05 | Yes (bolded and defined in place) | OK. |
| "bins" vs "labels" vs "groups" | Steps 04–05 | Yes | Three words for the same thing. |
| "tradeoff" | Step 08, 09 | No | Giving up one good thing to get another. |
| "normalize", "key" | Step 08 (bolded, defined) | Yes | OK. "stripped" in the prompt (spaces trimmed from the ends) is not explained. |
| `tuple` | Defined in A4 | Yes | OK. |
| "regex"/"punctuation" | Step 08 | No | Fine in plain English. |
| `rel` (parameter), "items" | Step 09a prompt | No | A function that says whether two items match. |
| "cluster" | Step 09a heading | Yes ("cluster / chain"), not bolded | A group of items joined by chains of matches. |
| union-find, connected components | Step 09b prompt | Yes | Claude explains it; add "you do not write it". |
| "drift" | Step 09b EXPLAIN | No | Groups slowly growing past what you meant. |
| `is_duplicate`, `b.id >= a.id` | Step 10a prompt | No | b.id >= a.id means "b was added no earlier than a". Student cannot read it. |
| tiebreaker | Step 11 (explained by analogy) | No | A second rule used when two items tie. |
| `compare` returning -1, 0, 1 | Step 11a prompt | No | -1 = first is smaller, 0 = tie, 1 = first is bigger. |
| permutations, `itertools`, `functools.cmp_to_key` | Step 11a prompt | permutations only | Claude handles it. Add "720 = every possible order of 6 things". |
| "shuffle" | Step 11a/12a | No | Means a different input order (also see the `reversed(TRACKS)` issue below). |
| "idempotent" (cleaning twice = once) | Step 12a | Not used, fine | The idea is shown but unnamed; name it or leave it. |
| graph, dict `{"X": {"Y"}}`, `set()` | Step 13a prompt | graph yes | `set()` = empty set. Say it is a table of "who needs whom". |
| "dependents first" | Step 13a prompt | No | Ambiguous (see section 2). |
| depth-first walk | Step 13b prompt | Yes | OK. |
| exception / CycleError | Step 13a | raise/ValueError | A named error type. Say so. |
| leaves | Beat 7 | "leaves first" | The tree metaphor is not explained. Say a leaf is a function that needs nothing else. |
| "design smell" | Glossary only | Yes | Never used in the workbook (see section 4). |
| TDD | Not used in the workbook text | Yes | The title says "test first". Either use or drop it. |

---

## 2. Ambiguous instructions and places a student could get stuck

1. **Fast path vs prerequisites.** The fast path skips Steps 02–05, but Step 07 asks for `reflexive_failure`, `symmetric_failure`, `transitive_failure`, and Step 08 and C1 say "equivalence relation". Those words are only defined in Steps 02, 03 and 05. A fast-path student reads Step 06 (nothing defined), then Step 07 with no definition of transitive or witness finder. Add a mini-definition box at Beat 2.
2. **Paper path is self-contradictory.** It says "Steps 01 to 03 and Step 07 on paper", but Step 06 (defining looks_alike) is skipped, and Step 08, the repair, is skipped. C1 ("I fixed it by") and C3 ("red at Step 07, green at Step 08") cannot be completed on paper. Also "the printed pytest screen" and "facilitator page" are unavailable to students.
3. **Starter source unknown.** "Copy the `starter` folder" says nothing about where it is. `python3 --version` check is missing for "3.9 or newer". `pytest` with no tests exits with an error code and may look like a failure; the text says it is okay (good), but add "even if it says error".
4. **Step 03 "Check: which of the five is NOT symmetric".** Three relations are not symmetric (no longer than, starts with, plays right after). Singular "the five ... which" is wrong.
5. **Step 03 table.** "Slow Orbit Remix", "Paper Moons", "Glass Harbor" have no lengths or artists shown anywhere; "title starts with the other's title" does not say which direction, and "Over" lists items the student cannot see. The ASK prompt line `<paste the table above, without my answers>` leaves unclear which table and what to delete.
6. **Step 04a: edges.** Each bin has two edges, so "edges ____ and ____" is unclear. The worked example gives only (179, 180), the upper edge, so a student has no rule for the lower edge (0 for short, which has no lower neighbour except -1). "errors: ____ and ____" duplicates the edge of short and epic. The ASK prompt hard-codes -1 and 3601, ignoring what the student wrote. "Paste your table under the sentence about lengths" does not match the placeholder `<paste your table of values>`.
7. **Step 04a Stuck:** "Test passes at Step 04a? Then the stub is not a stub; ask Claude to make it return `None` only." Fine, but say "Do not ask Claude to fix the test".
8. **Step 06a PREDICT:** "then check with Claude's tests". The tests cannot confirm True cases until Step 06b, because the stub always says False. Also "within 5" is not said to include exactly 5 until the 06b prompt ("5 apart still counts"), so the second PREDICT item is a coin flip.
9. **Step 07 edit instructions.** "Add them to the front of TRACKS" with a pasted line that shows the full TRACKS list. Does the student replace an existing `TRACKS =` line? Does the file already import Track? Say "replace the existing TRACKS line".
10. **Step 07 hint "Wait ten minutes first".** Unclear whether it means work alone, ask the facilitator, or read the chairs hint. It also conflicts with "do not ask Claude".
11. **Step 07 depends on Step 06.** `same_song` calls `looks_alike`, which needs Step 06b done. A pair skipping 06 will get ImportError. Say it.
12. **Step 09 PREDICT** needs lengths and artists of PAPER_MOONS, GLASS_HARBOR, NIGHT_BUS. The student has never been shown them; "open tests/fixtures.py" is missing.
13. **Step 09b EXPLAIN (2).** "A different Lantern Hill song of length 206" only makes sense if the student's own lengths were near 200. The student invented their own numbers, so the question is answerable only for a specific hidden answer. Say "use your own three lengths and pick a number 5 above your highest".
14. **Step 11a PREDICT** "Which two tracks have exactly the same length": the student's own Slow Orbit lengths may create ties or different pairs than the facilitator expects. Also assumes exactly one tie.
15. **Step 12a.** `reversed(TRACKS)` returns an iterator, not a list; a stub `list(tracks)` plus the test may need `list(reversed(...))`. The stub passing "twice" (tests pass with the stub) is surprising and not flagged in PREDICT.
16. **Step 13 "dependents first".** The graph is "written dependents first" but this phrase is never explained and could mean key order or arrow direction. The Beat 7 sentence "Test the pieces nothing else needs first" is the opposite of "leaves first" (see Top 6 fix 2).
17. **Step 13a/14a "Stuck?" lines missing.** Student sees red with no Stuck hint for cycle errors; `CycleError` must be imported by the test but nothing says so.
18. **A5 duplicates "Open Claude in the folder".** It appears twice (before and after the rules block); the second repeats and differs slightly (chat window workflow). Merge.
19. **Prompt jargon.** Many ASK CLAUDE prompts use words the student cannot read (parametrize, union-find, cmp_to_key). Students may think they must understand them. Add one line: "You do not have to understand the prompt's jargon, but you must check the output."
20. **Step 01 and 02 RUN/Check wording.** "mine and the computer's agree (or I know why not)" is fine. `python3 demos/step02_properties.py` may fail on import if Claude does not set `sys.path`; no Stuck hint for ImportError there (Step 05 has one).
21. **C1 summary pattern** does not say which relation to name (looks_alike) or that "the counterexample" means numbers. Suggest "…that *looks_alike* is not an equivalence relation, because it is not transitive (listing 1 at __s, 2 at __s, 3 at __s)".
22. **Two meanings of relation.** Beat 0: list of ordered pairs. Step 05 and Glossary: yes/no question. Consider a one-line bridge ("the list of pairs where the answer is yes").

---

## 3. Answer leaks (things students are supposed to work out)

Strongest first.

1. **Step 07 counterexample numbers:** Step 03 table "is within 5 seconds of: the lengths 200, 204, 208"; GLOSSARY "counterexample" row "200 s, 204 s, 208 s with a gap of 5". The glossary row is also misleading: the real gap between the ends is 8, not 5. Replace with a different example in both places.
2. **Step 07 structure via chairs:** Beat 2 gives 4-foot spacing, within 5, ends 8 feet apart. Step 07 Stuck repeats the recipe. Also GLOSSARY transitive row links "sits near" to Step 6. This is OK as a hint but defeats "do not ask Claude for these numbers". Keep the chairs, but change the spacing (for example "within 3 feet, chairs 2 feet apart") so it is not copyable.
3. **Step 05:** "This test is **green from the start**" appears immediately before "PREDICT. Will it be green or red?" and the heading says "GREEN from the start". The whole prediction is given away.
4. **Step 08 PREDICT:** the 08 ASK prompt contains `song_key(SLOW_ORBIT_2) == ("lantern hill", "slow orbit")` exactly, and states they have the same key. Also the 08 intro: "Equal keys cannot fail to chain, because 'equal' always chains" gives away the EXPLAIN sentence (and the closing line of 08 EXPLAIN).
5. **Step 04a:** the ASK prompt hard-codes -1 and 3601 (the "errors: ____ and ____" blank), and the worked example gives short's middle and edge values (90, 179, 180). The worked example is meant, but the error values are an unintended leak. 04b PREDICT then gives the 180 edge. The "lazy programmer" question is answered in 04b ("`>` where it should use `>=` on the edge at 180") and 06b Stuck ("`<=` not `<`").
6. **EXPLAIN answers printed in the RUN notes:** 04a ("the stub returns nothing, so every test notices"), 06a ("The ones that expect False already pass because the stub always says False"), 12a RUN ("the 'no duplicates', 'empty' and 'twice' tests already pass with the stub"), 13a EXPLAIN contains the paper answer ("the functions that use nothing else ... come first"), 01 EXPLAIN restates the PREDICT answer ("not the same flipped"), 02 EXPLAIN reveals that antisymmetric holds ("even though the relation is not symmetric").
7. **Step 06a Stuck:** "abs(100 - 106) is 6. Over 5, so not alike" answers one PREDICT item. The 06b prompt also says "5 apart still counts", which answers another.
8. **Step 09a prompt** lists the expected clusters (three Slow Orbit tracks together; the others alone), answering the PREDICT.
9. **Step 10a:** the prompt contains `b.id >= a.id` and the RUN note says `is_duplicate(1, 2)` True and `is_duplicate(2, 1)` False, which is the PREDICT answer. The intro also says careless wording "is directional".
10. **Step 11b:** the prompt gives the full sort key `(seconds, artist, title, id)`, and the Everyday picture gives the bib-number idea, answering "Why does adding `id` fix it?".
11. **Step 12:** the 12a prompt lists "cleaning twice gives the same answer as cleaning once" and "reversed(TRACKS)", answering the second PREDICT. 12b prompt names `song_key`, answering "Which earlier step made this easy?".
12. **Beat 7 paper question** is answered by the sentence immediately before it ("Test the pieces nothing else needs first ... leaves first"), and again in 13a EXPLAIN (see 6).
13. **Step 03 RUN:** gives all five verdicts. This is after the PREDICT table, so acceptable, but the table "Verdict (you)" column is visible in the same page.
14. **Step 02 RUN:** "three FAILS lines ... and one 'holds' (antisymmetric)" is after PREDICT, so acceptable; flag only because there is no "cover this until you have written your answers" instruction anywhere. Suggest a standing line in A3: "Do not read the 'You should see' lines until your PREDICT is written."
15. **Step 14a PREDICT** ("Is there a right answer?") is answered by the Beat 7 picture ("A 'needs' order has no cycles").
16. **Step 09b hint** "chaining means a match joins the group even if the ends are far apart" gives away EXPLAIN (1). Acceptable as a hint if labelled, but currently it sits inside the question.

---

## 4. Glossary completeness

### Bolded workbook terms missing from GLOSSARY.md
- **Track** (A4)
- **function** (A4)
- **Import lines** (A4)
- **look alike** (Step 06a; the glossary has no `looks_alike` entry)
- **PREDICT / RUN / EXPLAIN** (A3 table; bolded, not in glossary)
- **pass / fail** (A1, bolded in table headers only; fine, covered by "test")
- **partition** appears in the glossary only inside the "bin" row (acceptable)
- Not bolded but used and absent: listing, matrix, diagonal, tiebreaker, tradeoff, drift, exception/CycleError, `None`, `sys.path`, idempotent.

### Bolded terms present
test, unit test, pytest, red, green, stub, assert, tuple, raise, witness finder, relation, ordered pair, reflexive, symmetric, antisymmetric, transitive, witness, equivalence relation, partial order, bin, boundary, fixtures, characterization test, counterexample, normalize, key, cycle, AI proposed / we checked it.

### Glossary entries that never appear in the workbook text
property (only "property table" in the Paper path), property test, canonical key, design smell, TDD, graph (only inside a prompt), permutations and depth-first walk (only inside prompts, never bolded). Either use them in the workbook or remove them to avoid confusion.

### Wrong or stale step references in the glossary ("Where you meet it")
- assert "Step 1", stub "Step 1", boundary "Step 1": no Step 1 exists (Steps are 01, 04a ...).
- relation "Step 3" (it is Beat 0 / Step 05); property "Steps 3, 6, 10, 12".
- witness "Step 6", counterexample "Step 6": defined at Step 07.
- transitive "Step 6" (first at Step 02).
- antisymmetric "Step 12": the tie example is Step 11.
- partial order "Steps 12, 16": no Step 16.
- cycle "Step 18": no Step 18; it is Beat 7 / Step 14.
- normalize and key "Step 7": it is Step 08.
- characterization test "Step 3": it is Step 05.
- design smell "Step 14": the term is not used there.
- equivalence relation "Steps 3, 7": defined in Step 03 (and 05); Step 07 does not define it.
These look like leftovers from a longer Tuesday numbering. Renumber to match this workbook.

### Content issues in glossary
- counterexample example "200 s, 204 s, 208 s with a gap of 5" is a leak and also wrong (the ends are 8 apart).
- relation is "a yes/no question about two things", while Beat 0 defines it as a list of pairs.
- partial order mentions "some pairs may not be comparable at all" (not taught in the workbook). Fine, but this is a new idea for first-years.
- The glossary note "Words are in the order you meet them" is false (cycle, depends on, TDD, etc. out of order).
