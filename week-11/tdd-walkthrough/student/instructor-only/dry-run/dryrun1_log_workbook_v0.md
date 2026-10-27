# DRYRUN LOG (dryrun1)

## Setup (A4/A5)
- Copied starter -> playlist-lab. `python3 -m pytest -q` gave "no tests ran in 0.00s" (matches A4; note exit code is 5 normally, not mentioned). Python here is 3.14, fine.
- A5 rules pasted conceptually. Note: rule 2 "write the test (and a stub if needed), then STOP" - fine.

## Step 1
PREDICT (written before running): short 90 / 0, 179; normal 240 / 180, 299; long 450 / 300, 599; epic 1800 / 600, 3600; errors -1 and 3601. Lazy programmer gets 180/300/600 (the starting edge, >= vs >) or 3600 (inclusive top) wrong.
ACTUAL: red, "5 failed in 0.02s" (4 label tests: `assert None == 'short'` etc; test_errors: "DID NOT RAISE <class 'ValueError'>").
Matched "You should see"? Mostly yes. Workbook says "assert None == 'short'" failures; the errors test fails differently (DID NOT RAISE), unmentioned. A student might be thrown.
Workbook alone enough? Mostly yes. Gaps: (a) "Fill in the test values" then template says "<paste your table of values>" - no format shown for how to paste; (b) "middle" vs "edges" for the first bin: a novice may not see that 0 is an edge of "short" and there is no lower neighbour (0 is one edge, -1 is the error edge); the table says "two values right at each edge" but each bin has two edges, giving 4 edge values per bin in the strictest reading (179,180 / 299,300...). Ambiguous: do I list the last value inside the bin at each end, or the pair straddling? Glossary says "values on either side of the boundary". My answer of 'edges 0 and 179' = first and last inside values; this misses straddling. Needs one worked example in the blank (e.g. short: edges 0 and 179).
(c) The pasted A5 rule 6 asks coach to say what red to expect; fine.
(d) First `assert` failing in a multi-assert test hides the others; the workbook says "one test function per label" which leads to 3 asserts per test; fine but the student can't tell which edge failed unless reading E line (Step 2 Stuck advice says "which of your edge values failed" - with one function per label and multiple asserts only the FIRST failing one is reported. Stuck advice is therefore hard to follow). Suggest "one assert per value / parametrize".
Terms used before explained: "stub" (used in Step 1 goal text; defined only in Glossary, not in-line in workbook); "plain assert tests" / "assert" (never defined in workbook text, only glossary); "raise ValueError" / "ValueError" (never explained); "Track" fine.
Minutes: 15-20 (choosing the edge numbers is the hard part, then pasting into Claude).
Change: show a worked example for one bin; define stub and assert inline in A1/A2; say "each bin has two ends: test the last value in and the first value out" explicitly; tell them what the DID NOT RAISE line means.

## Step 2
PREDICT: 180 would catch it (179 gives short either way; 180 would wrongly become "short"). Also 300 and 600 for the same reason if the same mistake were made there.
ACTUAL: green, "5 passed in 0.01s". Matched: yes.
Workbook alone enough? Yes. The "which values catch >" question is answerable only if the student understands which side of a comparison is in the bin; fine for most. 
Terms before explained: none new.
Minutes: 5. 
Change: In EXPLAIN, "what is each bin in your own words" is easy to answer by copying the table; ask for a "which side owns the edge" question instead.

## Step 3
PREDICT (before running): green, because it only records what the function already does (characterization test). Why: the labels are fixed groups so "same label" can't break.
ACTUAL: green, "9 passed in 0.01s". Matched: yes.
Workbook alone enough? Mostly. Struggles: 
- The coach must import from tests/relations.py; prompt says only "from tests/relations.py". `from tests.relations import ...` worked here (tests/ has no __init__.py; works because pytest.ini sets pythonpath=.). A coach could equally write `from relations import` or `from .relations`. The workbook never says how to import; `.relations` would FAIL (no package). Risk of an import error that a novice cannot fix; the "Stuck? Import error?" hint only blames the working directory, not the import style.
- "reflexive_failure(rel, items)" signature is never shown in the workbook; the coach has to open relations.py (allowed to read, not edit). Student can't predict what a "failure finder" is until the docstring is read. The text 'A finder returns None' is given AFTER the run.
- Student has to understand why "exactly four bins" (assert len(set)==4) is meaningful - fine.
- "equivalence relation" introduced with 3 new adjectives in one paragraph: reflexive/symmetric/transitive each in one parenthetical. Heavy for a first-year who finds abstraction hard. Glossary's picture for reflexive "Everyone sits at their own table" ok.
Terms before explained: "failure finder"/"finder" (A4 says "helper that hunts for counterexamples" but "counterexample" is only defined at Step 6); "counterexample" used in A4 before definition; "characterization test" defined in-line (ok); "sorts everything into groups with no overlap" (ok).
Minutes: 15 (the three properties are new; reading Claude's test).
Change: Show, inline, the signature `transitive_failure(rel, items)` and 'returns a tuple or None'; define counterexample in A4 or earlier; give import line explicitly in the prompt: `from tests.relations import ...`. Move the "None is good" sentence ahead of RUN.

## Step 4
PREDICT (before running): Zed100 vs Zed104: True. 100 vs 105: True (<=5). 100 vs 106: False. zed 100 vs ZED 101: True. different artists both 100: False.
ACTUAL: red with passes: "3 failed, 11 passed in 0.02s" (3 expect-True tests fail; 2 expect-False tests pass; plus the 9 old ones pass).
Matched: yes, matches "only some tests fail". But the summary shows 11 passed, which includes 9 from earlier steps - workbook doesn't explain that the old tests keep running, so a novice may be puzzled by "11 passed" when only 2 tests "should" pass.
Workbook alone enough? Yes.
Prompt template issue: it doesn't say what titles/ids to give the tracks; a coach invents them (harmless). It also doesn't say whether the stub should import Track (not needed). It says "Build the Tracks inline with Track(id, title, artist, seconds)" - good.
Terms before explained: "looks alike" ok. None new.
Minutes: 10.
Change: Say "the count includes tests from earlier steps; look at the names in FAILED lines".

## Step 5
PREDICT: green. The rule: same artist (lowercase compare) and abs difference <= 5.
ACTUAL: green, "14 passed in 0.01s". Matched: yes.
PREDICT answers wrong? None; least sure about "exactly 5" - the template said "5 apart still counts", so it is given away.
Workbook alone enough? Yes. 
Terms: none new. Minutes: 5.
Change: EXPLAIN asks "which predictions were wrong" - fine, but template for Step 5 states the answer; ok since it's a green step.

## Step 6
PREDICT (my witness, invented before running): Listing 1: 150 s, Listing 2: 155 s, Listing 3: 160 s.
Check by hand: gap 1->2 = 5 (<=5 yes), gap 2->3 = 5 (<=5 yes), gap 1->3 = 10 (>5 yes). Missing arrow: between 1 and 3.
(Note: GLOSSARY.md "counterexample" row contains "200 s, 204 s, 208 s with a gap of 5" - this leaks a near-complete answer to a student who reads the glossary beside the workbook, and "gap of 5" is wrong/confusing since 204-200=4. Also the Stuck hint gives 100,104,108.)
Expect: one failure, transitive test only.
ACTUAL: red, "1 failed, 16 passed in 0.02s". Failed test: test_same_song_is_transitive; message "id 1 = 150 s, id 2 = 155 s, id 3 = 160 s". Same three I picked. Reflexive/symmetric passed.
Matched: yes.
Workbook alone enough? Mostly yes, with these problems:
- The coach prompt asks the assert message to print ids and seconds. A coach has to write code that builds a message from the failure BEFORE the assert (as I did, with an early return when None). Typical coach would write `assert result is None, f"{result}"` - fine, but the pytest output also dumps the full Track reprs, so output is long. Not an error.
- A student must do the fixtures edit by hand: the instruction "following the pattern of PAPER_MOONS" is clear. But the starter's TRACKS list in fixtures.py has to be edited (replace the line); the snippet shows the full TRACKS line, OK. Unclear whether to leave the `# Ids 1, 2 and 3 are saved` comment.
- Big conceptual leap: Step 6 PREDICT asks for numbers satisfying a 3-way constraint; "gap" and "looks alike" under "within 5" must be re-derived by the student. Many first-years will pick 100,104,108 from the Stuck hint; it IS easy to find. The glossary leak (200/204/208) means few will really invent.
- Titles in listings differ but looks_alike ignores titles - not stated; students may wonder whether titles matter. Not explained.
- The "Draw it" instruction asks for arrows "each way" - 4 arrows + a missing pair; fine.
- EXPLAIN is a heavy, multi-part prompt: fill a sentence AND explain in plain words why a pairwise rule can't be trusted to sort into groups. Hard for target audience; no sample answer.
- The one-failure expectation depends on iteration order of the finder; workbook says it "names three ids" - fine.
Terms before explained: "pairwise"/"a single rule that only compares two things at a time" - ok in plain words; "witness" defined here, but "witness" appears in A4 ("hunts for counterexamples") and in glossary. "gap" used without definition (only implied abs difference).
Minutes: 25-30 for a struggling pair (inventing numbers, editing fixtures, reading the failure).
Change: Remove the 200/204/208 from the Glossary; show the pytest failure sample once; give a sentence frame example from a different domain; state explicitly that titles are ignored by looks_alike (that's why differing titles are fine).

## Step 7
PREDICT: key for "Slow Orbit (Remastered)" / "Lantern Hill" = ("lantern hill", "slow orbit"). For "slow orbit" / "LANTERN HILL" = ("lantern hill", "slow orbit"). Equal? Yes. (Order artist-first is guessed from the sentence "the artist and the title" and the glossary example; not explicitly stated for the tuple.)
ACTUAL: green, "19 passed in 0.02s". Matched: yes.
Workbook alone enough? Yes, but:
- Prompt template ambiguity: "artist lowercase and stripped" vs the prose "artist and title ... punctuation removed": does punctuation removal apply to the artist too ("Moss & Marrow" -> "moss  marrow")? Prompt says only title; prose is ambiguous. Result still correct either way for the tests.
- Template doesn't name the fixtures (SLOW_ORBIT_1...) - coach must read tests/fixtures.py; the student's own constant names are given in Step 6, so ok, but if the student renamed them it breaks.
- Template (b) says "the three Slow Orbit tracks have the same song_key and Paper Moons does not" - ok.
- Tuple key order and the exact key (e.g. ("lantern hill","slow orbit")) isn't asserted by any test; PREDICT is only checked by the "Stuck?" suggestion of printing. A student who guessed wrong would never find out unless stuck. Suggest a test that asserts the exact key for the Remastered one.
- Regex: coach needs `re`; "(...) removed" if unbalanced parentheses or nested - no tests. Fine.
- Big hidden jump: the glossary explains "key" but 'equal keys cannot fail to chain' is asserted, not shown. Student EXPLAIN is a one-liner; fair.
- Step 7 is the biggest step for a novice: 2 new functions + 2 tests + modifying same_song. Core ends here.
Terms before explained: "tuple" (never explained; glossary has no entry); "regex"/"punctuation removal" fine; "collapse".
Minutes: 20.
Change: add tuple to glossary with example; add one test pinning the exact key; split into 7a (song_key) 7b (same_song+tests).

## Step 8
PREDICT: 4 groups: {1,2,3}, {4}, {5}, {6}. (Glass Harbor and Night Bus both 351 s but different artists.)
ACTUAL: red, "1 failed, 21 passed in 0.02s". Only the Slow Orbit cluster test failed. Matched "red (the Slow Orbit cluster test fails)": yes. Note: "every track in exactly one cluster" and "others alone" pass with the stub, which the workbook doesn't say (Step 8 only mentions the failing one). EXPLAIN asks "why exactly one cluster per track" - that test passes already, so the student can't see it fail.
Workbook alone enough? Yes.
Template issue: "items" may be hashable Track (frozen dataclass => hashable) - fine. The prompt gives no hint how tests identify a cluster; coach had to invent helper functions. Fine.
Terms before explained: "cluster" used in Step 8 heading; glossary defines "cluster / chain"; the Beat 3 intro uses "group", "chains of matches" in everyday language. OK.
Minutes: 10.
Change: Say which tests pass on the stub (like in Steps 4, 14).

## Step 9
PREDICT: green. 
ACTUAL: green, "22 passed in 0.02s". Matched: yes.
Workbook alone enough? Code yes; the EXPLAIN is hard. "This clustering used looks_alike, the rule that failed to chain. Why does clustering by chains still give clean groups?" A struggling student needs the idea "the cluster itself is DEFINED as 'connected by a chain', and that relation chains by construction (friend of a friend is in)". The only hint is "Re-read the friend-of-a-friend picture". It's also a conceptual tension with Step 6-7 (we said looks_alike is bad for grouping; now it's fine?) that the workbook never resolves: the clusters can merge songs that don't look alike directly (e.g. 150 and 200 chained through many 5-gaps, drift). Real gap: nothing warns about "chaining drift" risk of this clustering, which is the other side of the lesson.
Prompt behavior: "if rel(a, b) is True put them in the same cluster" - I also checked rel(b,a), a small deviation from the literal text (harmless).
Prompt asks the coach to "Explain union-find in two sentences" - which I put in a docstring; a real coach would say it in chat. Fine.
Terms before explained: "union-find", "connected components" (only explained by Claude on request, not in glossary), "depth-first" later.
Minutes: 10 (mostly reading Claude's code, which a novice can't follow; the workbook doesn't ask them to).
Change: Add glossary rows for union-find / connected components; add an extra EXPLAIN hint: "If 1~2 and 2~3, can 1 and 3 land in different clusters?".

## Step 10
PREDICT: is_duplicate(1,2): True (same song, 2 >= 1). is_duplicate(2,1): False (1 >= 2 is false). Symmetric?: No.
ACTUAL: red, "1 failed, 23 passed in 0.03s". Message: "is_duplicate(1, 2) is True but is_duplicate(2, 1) is False". Matched: yes, exactly.
Workbook alone enough? Yes. 
Note: the Everyday picture says "Is the sibling of" (symmetric) - but also Glossary lists it. Note Step 10 PREDICT asks "is_duplicate(1,2)" using ids 1,2, which are the student's own numbers (fine). The word "symmetric" was defined in Step 3 and again here; ok. The step relies on Step 7 having been done (same_song with keys); if the pair stopped at Step 6 (or never finished 7), is_duplicate(1,2)... would still be True/True (looks_alike). Not stated as a prerequisite; steps 8+ are "if time allows" but each builds on song_key/same_song from step 7.
Minutes: 10.
Change: state prerequisites for 8-19 (needs steps 1-7 files).

## Step 11
PREDICT: green after making is_duplicate just same_song(a, b) (no id comparison).
ACTUAL: green, "24 passed in 0.01s". Matched: yes.
Workbook alone enough? Yes. EXPLAIN "why is 'which one do I keep?' a different question" - answerable from the Step 11 prompt text itself, which gives it away ("Which copy to KEEP is a separate question").
Prompt issue: "Fix is_duplicate so swapping a and b can never change the answer" - a coach could do many things (e.g. abs, sorted, or drop the id test). Mine dropped the id test. Another coach could make it `same_song(a,b) and a.id != b.id`, which breaks REFLEXIVE (the test would then go red on reflexive). The prompt has no hint to keep reflexive; acceptable, since tests catch it.
Minutes: 5.
Change: none critical.

## Step 12
PREDICT: ids 5 and 6 (Glass Harbor and Night Bus, both 351 s).
ACTUAL: red, "2 failed, 25 passed in 0.03s": antisymmetric and "one answer" failed; transitive passed. Matched: yes. Prediction (5, 6) correct.
Workbook alone enough? Yes, but heavy for a novice:
- The prompt uses itertools.permutations and functools.cmp_to_key; neither is explained; "every shuffle" means 720 orderings (6 tracks) - never said. Student's confusion likely at "sorting gives exactly one answer".
- "compare returning -1, 0 or 1" and "cmp_to_key" are concepts nobody introduced. "at_or_before" fine.
- Prompt says "test antisymmetric_failure is None" but antisymmetric_failure is described in relations.py only; workbook A4 mentions the file but never lists the four finders.
- The EXPLAIN "Why does sorting give different results depending on how the list started?" has the ids 5/6 as the answer: tie -> sort is "stable", leaves original order. "stable sort" never explained.
- Photo-finish picture is good.
Terms before explained: "tiebreaker" (in picture text, ok), "shuffle", "permutations", "cmp_to_key", "comparator".
Minutes: 15.
Change: Explain in one line that sorted() keeps ties in their starting order; say 6 tracks => 720 shuffles; list the four finders in A4.

## Step 13
PREDICT: green; id is unique so no two different tracks tie.
ACTUAL: green, "27 passed in 0.02s". Matched: yes. Workbook alone enough: yes. EXPLAIN "Why does adding id fix it?" answerable (id unique).
Minutes: 5. Change: none.

## Step 14
PREDICT: clean_playlist(TRACKS) returns ids [1, 4, 5, 6]. On its own result: the same, [1, 4, 5, 6].
ACTUAL: red, "2 failed, 30 passed in 0.04s" (earliest-listing test and shuffled test fail; no-dups, empty, twice pass with stub). Matched exactly: yes.
Workbook alone enough? Yes. 
Template note: "shuffled input" - a coach has to choose how to shuffle; I used random.Random(7). A coach using plain random.shuffle would make a flaky test (could shuffle to identical order); prompt doesn't say deterministic or "reverse". Wrong-thing risk: moderate.
Also unclear whether clean_playlist returns Track objects or ids; PREDICT says "list the ids" while tests compare Tracks - minor.
Minutes: 10.
Change: say "use a fixed shuffle such as reversed()".

## Step 15
PREDICT: green.
ACTUAL: green, "32 passed in 0.02s". Matched: yes. 
Workbook alone enough? Yes. EXPLAIN "which earlier step made this easy" -> Step 7 (song_key). Answerable.
Minutes: 5.

## Step 16
(Paper step) PREDICT: test first (leaves): song_key, looks_alike, cluster_by_chain, compare, length_label; then same_song; then is_duplicate and clean_playlist.
ACTUAL: red, "1 failed, 33 passed in 0.04s" (only "comes after what it needs" fails; "exactly once" passes with the stub). Matched "red": yes.
Workbook alone enough? Yes. 
Issues: the EXPLAIN "Compare Claude's order with your paper answer" - at red, Claude produced no order (stub just returns the dict order), so there is nothing to compare at Step 16; the comparison only makes sense after Step 17. Workbook error/ambiguity.
Also the paper question says arrows "from each function to what it needs" and "which would you test first" - fine, but there's no check/answer for the paper answer anywhere (unlike code), a struggling student can't self-verify.
Prompt note: the "dependents first" phrase is explained only by the "X needs Y" gloss; "graph" and dict-of-sets never explained (no glossary entry for graph). "exception" (CycleError) never explained.
Minutes: 15-20 (paper dependency drawing is new).
Change: move compare-with-paper to Step 17; add "graph" and "exception" to glossary; give a one-line sample answer for the paper question after the fold.

## Step 17
PREDICT: green. 
ACTUAL: green, "34 passed in 0.03s". Matched: yes. Workbook alone enough: yes. No EXPLAIN at Step 17 (fine). 
Template note: "Mark each function as seen so it is added once" - a coach that marks seen at START of the visit (as I did) makes Step 18 red for the "wrong" reason (no error) which is what the workbook expects; one that marks at END would infinite-loop (RecursionError) on Step 18's cyclic input, giving a different red. Prompt doesn't pin this down.
Also: prompt doesn't say recursion vs. stack; fine.
Terms before explained: "depth-first walk" (not in glossary), "recursion".
Minutes: 5-10 (novice just runs; can't read the code).

## Step 18
PREDICT: for {"a":{"b"},"b":{"a"}} there is no right order (each needs the other first). It should raise an error rather than return something.
ACTUAL: red, "2 failed, 34 passed in 0.04s" ("DID NOT RAISE" both). Matched: yes ("no error raised yet").
Workbook alone enough: yes. PREDICT question ("Is there a right answer?") fine.
Note: the message check "a -> b -> c -> a" depends on the traversal starting at "a" and iterating deterministically; with sets of one element and dict order it works, but a coach using unsorted multi-element sets might get e.g. "b -> c -> a -> b" if started elsewhere. Prompt gives only this one example, so correct only if traversal starts at "a" (dict order). Not stated.
Minutes: 8.

## Step 19
PREDICT: green after tracking the current path (a "visiting" list) and raising CycleError with " -> ".join(path + [name]).
ACTUAL: green, "36 passed in 0.02s". Matched: yes.
Workbook alone enough: yes for the run. EXPLAIN "What does a cycle in a needs order tell you about the design?" answerable from the picture (key in room).
Minutes: 8.
Change: Step 19 prompt is one dense line unlike earlier ones; it also says "Make all tests pass" which could tempt a coach to edit earlier tests; fine.

## Part C (read, not completed in detail)
- C1 pattern: "I showed that ____ is / is not an equivalence relation, because ____ (counterexample: ____), and I fixed it by ____." My answer: "I showed that 'looks alike (same artist, lengths within 5 s)' is not an equivalence relation, because it is not transitive (counterexample: 150 s, 155 s, 160 s), and I fixed it by comparing normalized keys (artist + title lowercased, without brackets/punctuation)."
- C2 honesty log table has no example row; a novice won't know "what Claude proposed" granularity. A6 promises "mark it in the log at the end" - ok.
- C3 says "paste the red output at Step 6 and the green output at Step 7" - a student who didn't save terminal output has to re-create the red state; not warned in Step 6/7. Also Step 7 says "Core done? jump to Part C", but Part C is placed after Step 19, which could confuse about page ordering.
- C4 checklist: fine.

## Cross-cutting findings
1. Nothing in the workbook says how to run Claude in the folder or what to do when Claude does more than the step (A5 rule 1 helps, but no "if Claude wrote ahead, say STOP" recovery).
2. The workbook never says tests accumulate: each pytest run includes every earlier test; the "N passed" counts jump. 
3. Python 3.9: my code is compatible; the workbook gives no guidance for what happens if the student's Claude uses 3.10+ features (match, X | Y).
4. Step prompts rely on the coach reading existing files (fixtures names, relations signatures); A5 never says "read the files in the folder first".
5. Pytest exit code / `-q` output reading: the "Stuck?" hint of Step 1 helps; no sample output screenshot in text for the student (facilitator-provided only).
6. The 'Paper path' promises hand-check tables "at each step", but the steps do not contain those tables (only Step 16 has paper work, plus Step 6 hand checks). Promise unmet.
7. Hand-check of EXPLAIN prompts: the EXPLAIN boxes are many (about 17). For a struggling pair, Steps 6, 7, 9, 12 EXPLAINs are the hard ones; no model answers or self-check.
8. The term "relation" is defined as "a yes/no question about two things", yet `rel(a, b)` appears in code before the student sees how it maps; ok.
9. Glossary rows for "antisymmetric" says "photo finish with a tie breaks this" fine; "partial order" is introduced in Beat 5 but never actually tested in the workbook (Step 12/13 test antisymmetric and transitive, never reflexive/partial order name used); fine.
10. Glossary "counterexample" row leaks numbers (200,204,208), "gap of 5" is inaccurate (gap is 4 between neighbors, 8 total).

## TOP 10 FIXES (ranked)
1. Remove the leaked numbers from GLOSSARY ("200 s, 204 s, 208 s") and the Step 6 Stuck hint (100,104,108), or move the hint behind an explicit "only after 10 minutes" gate: the core learning (invent the witness) is otherwise skippable.
2. Step 1: add a worked example for one bin's test values (e.g. short: middle 90; edges 0 and 179 / and the straddling pair 179,180) and define "edge" as "last value in the bin and first value of the next". State how to paste the table into the prompt.
3. Define stub, assert, ValueError/exception, tuple, graph, union-find/connected components, depth-first, permutations/cmp_to_key where first used (or add to glossary). These are the terms a novice hits cold.
4. In Step 3 (and A4), show the finder signature `transitive_failure(rel, items) -> tuple or None` and give the exact import line `from tests.relations import ...` in the prompt; the current text leaves the coach to guess (a relative import `.relations` would fail with a confusing error).
5. Explain that each pytest run includes all earlier tests, so counts like "11 passed" in Step 4 or "30 passed" at Step 14 are normal; tell them to read the FAILED lines, not the totals.
6. Step 1/2: multi-assert tests only report the first failing edge; either ask for one assert per value (or parametrize) so the "which edge failed?" Stuck advice in Step 2 is actually usable.
7. Step 7: add a test pinning the exact key (e.g. song_key(SLOW_ORBIT_2) == ("lantern hill","slow orbit")) so the PREDICT is checked by the machine, not only by "Stuck?" printing; split the step in two (song_key; then same_song+tests). Clarify whether punctuation is stripped from the artist.
8. Step 9: resolve the conceptual puzzle (why is clustering with looks_alike fine?). Add a hint question and mention the "drift" risk (chains of 5-second gaps can merge songs 50 seconds apart). Add model answers/self-check for hard EXPLAINs (Steps 6, 7, 9, 12).
9. Step 12-13 and 14: pin down deterministic choices in prompts (fixed shuffle such as reversed(); say 720 permutations for 6 tracks; explain that sorted() keeps tied items in starting order). Step 16: remove "Compare Claude's order" (no order exists at red) and move it to Step 17; give an answer for the paper dependency question.
10. State prerequisites for Steps 8-19 (they need song_key, fixtures from Steps 1-7), keep a "save the red output" reminder at Steps 6/7 for the C3 evidence sheet, and add either the promised "by hand" tables for the Paper path or drop that promise.

## UNEXPLAINED TERMS (used before or without explanation in the workbook text)
- "stub" (Step 1 Goal prompt; glossary only)
- "assert" / "plain assert tests" (Step 1 prompt; glossary only)
- "ValueError" / "raise" / "exception" / "CycleError"
- "counterexample" (used in A4 before its Step 6 definition)
- "failure finder" / "finder" (Step 3 "a finder returns None")
- "tuple" (Step 7 "returns a tuple"; Step 3 finder returns "a tuple")
- "gap" (Step 6 check by hand)
- "regex"/"punctuation removed", "collapsed" (Step 7 prompt)
- "union-find", "connected components" (Step 9)
- "permutations", "cmp_to_key", "shuffle", "stable"/"tied order" (Step 12)
- "unique sort key", "tiebreaker" (Step 13; tiebreaker explained in picture, "unique sort key" not)
- "graph", "dependents first", "depth-first walk", "seen", "path" (Steps 16-19)
- "fixtures" is defined in A4 but pytest's other sense isn't needed; ok.
- "idempotent" is never used (good) but "cleaning twice gives the same answer" is not named or explained as to why it matters.
- "playlist-lab folder" / "Open Claude in the folder": no instruction on how.

## Time estimate overall (honest guess for a struggling pair)
Core (Steps 1-7): roughly 100-120 minutes. Steps 8-19: another 60-80 minutes. Total about 3 hours; core alone likely overruns a 75-90 minute class.
