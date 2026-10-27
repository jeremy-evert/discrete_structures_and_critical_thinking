# DRYRUN LOG (student pair, struggling, naive)

## Part A
Read A1-A6, GLOSSARY. Pasted rules (A5) as coach context. Setup: copied starter -> playlist-lab; `python3 -m pytest -q` -> "no tests ran in 0.00s" (matches A4).
Part A notes:
- A4 says "install pytest if you need to" - fine. pytest.ini sets pythonpath so imports work.
- A4 lists "a function / stub / assert / raise / tuple / witness finder" but A2 "Red/Green" and A3 say "Run python3 -m pytest -q" before A4 explains how. Fine.
- A5 coach rule 2 "STOP" good. Rule 3 forbids editing relations.py/track.py but NOT tests/fixtures.py -> fine since student edits it in Step 07 (but coach should not edit fixtures.py in Steps 01/06; nothing forbids it).
- "Paper path" and "fast path" both in A4/Part B intro: the fast path is announced only in line 99, AFTER Part A. A pair reading top-to-bottom does not know which steps to skip (02-05) until Part B. Minor.
- The workbook says "Steps 01, 06, 07, 08" but 06 = 06a+06b. Not stated outright.
- Term "relation", "ordered pair", "reflexive/symmetric/transitive" first defined in Step 02/Beat 0, but A4 mentions "witness finder ... transitive_failure" before; the Glossary rescues it.

## Step 01
PREDICT (written before running):
 pairs: (Slow Orbit, Paper Moons), (Paper Moons, Glass Harbor), (Glass Harbor, Night Bus)
 matrix rows: SO: 0 1 0 0 | PM: 0 0 1 0 | GH: 0 0 0 1 | NB: 0 0 0 0
 arrows: SO->PM->GH->NB. Flipped over diagonal: not the same (1s move from above to below diagonal).
EXPLAIN (student): not symmetric - if A plays right before B, B does not play right before A.
Actual run of demo: 3 pairs, matrix with three 1s just above the diagonal, 3 arrows. pytest -q: "no tests ran". Matched: yes.
 Workbook alone enough: yes. Prompt text sufficient for coach: yes (output exactly as expected; ambiguity: "demos/" dir already exists, fine).
 Nits: Step 01 uses "relation", "ordered pair" explained right above - good. "matrix", "diagonal" not in GLOSSARY ("above the diagonal" is used in the You-should-see line; a struggling student may not know diagonal). "Draw four dots" fine. Step 01 lists "the very next track" - fine.
 Minutes: 8 (paper 5, run 3). Fix: add one picture/example row of matrix and define "diagonal" (top-left to bottom-right).

## Step 06a
PREDICT (before running):
 Zed 100 vs Zed 104: True. Zed 100 vs 105: True (within 5 includes 5). 100 vs 106: False.
 zed 100 vs ZED 101: True. different artists both 100s: False.
ACTUAL: "3 failed, 2 passed". FAILED: test_same_artist_4_apart, test_exactly_5_apart, test_capitals_in_artist. Passing: 6_apart, different_artists.
Matched workbook ("red, only some fail; the expect-False ones pass"): yes. My predictions: all 5 right.
Workbook alone enough: mostly yes. Gaps:
 - PREDICT block says "check with Claude's tests" but the pair has no way to map my 5 prediction lines to the 5 test names (output shows test names, not my wording). Suggest numbering.
 - Prompt gives no seconds for the pair; a coach picks its own numbers (I chose 100/104/105/106). Student predicts with Zed 100s etc. but the prompt doesn't say "use my numbers from PREDICT". Coach could pick different numbers, making student predictions not comparable. Fix: put "Zed 100 vs 104..." into the prompt.
 - Prompt does not say where Track lives (from playlist.track import Track). Coach can find it in the folder; ok.
 - "within 5 seconds" is introduced in the opening line; "Zed 100s" the 's' shorthand unexplained (seconds). Minor.
 - Student does not know how to read the failure text; "Reading pytest output" in A5 helps.
Does the prompt let the coach produce the right thing? Yes, mostly; 5 tests produced. Risk noted above.
EXPLAIN (student): stub always returns False so tests expecting False pass by accident - passing doesn't mean the code works.
Minutes: 10.  Fix: put the 5 cases with numbers in the prompt; add a "tests that pass at red prove nothing" sentence (EXPLAIN covers it).

## Step 06b
PREDICT: none asked; I expect green, 5 passed.
ACTUAL: "5 passed". Matched ("green"): yes. Workbook alone enough: yes. Coach prompt sufficient: yes.
 Gaps: "Stuck?" mentions `<=` vs `<`: good. EXPLAIN asks "which PREDICT answers were wrong" -> none; ok.
 Honest note: no explanation of how to hand pasted code to a student who does not use Claude Code (A5 covers).
 Minutes: 5.

## Step 07
PREDICT (my own witness, written before running):
 Listing 1: 200 s, Listing 2: 205 s, Listing 3: 210 s.
 gaps: 1->2 = 5 (<=5 yes), 2->3 = 5 (<=5 yes), 1->3 = 10 (>5 yes).
 Missing arrow: between 1 and 3 (both directions).
 (Glossary peek tempted me: it lists "200 s, 204 s, 208 s with a gap of 5" - see notes.)
ACTUAL: "1 failed, 7 passed" (7 = 5 looks_alike + reflexive + symmetric). FAILED: tests/test_transitivity.py::test_transitive. Message: "not transitive: id 1 = 200s, id 2 = 205s, id 3 = 210s". Matched workbook: yes, and pytest found exactly my triple.
Workbook alone enough: yes with caveats:
 - tests/fixtures.py comment says the ids are "saved ... in Step 6" but the workbook says Step 07 (starter file mismatch; starter text, not workbook).
 - "add them to the front of TRACKS" plus pasted snippet is clear. Student must also DELETE the old comment/TRACKS line (the snippet replaces TRACKS; not said "replace the existing TRACKS line"). A struggling pair could end up with two TRACKS definitions (second wins, harmless if after; if snippet pasted above old TRACKS, old overrides -> tests pass vacuously and Step 07 shows no failure). RANK HIGH: say "replace the existing TRACKS line".
 - Glossary entry "counterexample ... 200 s, 204 s, 208 s with a gap of 5" gives away an answer in Step 07 and is wrong (200->208 is 8, not 5; 4+4 steps). Also Step 03 table uses lengths 200,204,208 for "within 5 seconds of". So pairs who peek will copy. Also Step 06a numbers Zed 100/104/105/106 are fine.
 - Step 07 PREDICT checklist asks for 'gap 1->3 (>5?)' good.
 - Mixed up: seconds could duplicate length of Paper Moons (204) or Glass Harbor/Night Bus (351) -> ties matter in Step 11a. Warn students to avoid 204 and 351, or the Step 11a PREDICT ("which two tracks have exactly the same length") has several answers. E.g. if a pair chose 204 for listing 2, then 2 and 4 tie as well.
 - "Wait ten minutes first" in Stuck is good pedagogy but a coach on a rule is fine.
 - Coach prompt: how to import fixtures from a test was not stated; coach used `from fixtures import TRACKS` (works because pytest adds tests/ to sys.path). Prompt mentions "TRACKS from tests/fixtures.py" - ok. It worked for me; A4 only promises imports for relations. Slight risk the coach writes `from tests.fixtures` (also works with pythonpath=.).
 - Prompt said "make the assert message print ids and seconds" - coach can do it. Right thing produced: yes.
 - Prompt says "add same_song(a, b) ... returns looks_alike" fine.
Minutes: 15 (invent numbers 5-10 with the chairs, paste, run).
Fix: "replace the existing TRACKS line (delete the old one)"; remove spoiler from Glossary; tell students to avoid 204/351.

## Step 08
PREDICT (before running): song_key(SLOW_ORBIT_2) = ("lantern hill", "slow orbit"); song_key(SLOW_ORBIT_3) = ("lantern hill", "slow orbit"); Equal: yes.
ACTUAL: "10 passed". Matched: yes. Workbook alone enough: yes. Coach prompt sufficient: yes.
 Notes: regex "(...)" removal and punctuation removal is spelled out; prompt is tight and the coach can't go wrong. The sentence "Punctuation is removed from the title only" is a patch-looking sentence added at the end of the prompt, fine.
 "Hold on": when same_song flips to keys, the old test_transitive in the same file turns green - workbook does not tell students that the red test from Step 07 is the SAME test that turns green. Worth one sentence (the payoff moment).
 Terms: "normalize", "key" defined; "tuple" glossary; "canonical key" in glossary says Step 08 but is never used in Step 08 text. "Equal keys cannot fail to chain, because 'equal' always chains" - abstract; a struggling student gets lost. Suggest the picture: same table number.
 "Core done?" jump to Part C: fine.
 Minutes: 12.

## Step 09a
PREDICT: 4 groups: {1,2,3}, {4}, {5}, {6}.
ACTUAL: "1 failed, 12 passed". FAILED: test_grouping.py::test_slow_orbit_one_cluster. Matched: yes ("Slow Orbit cluster test fails"); prediction right.
Workbook alone enough: yes. Prompt: coach produced right thing; ambiguity: "stub returns each item in its own list" explicit - good. Does not say what the cluster list order must be; tests I wrote used sorted ids (coach's choice). Fine.
 Terms before explained: "cluster" (Glossary "cluster / chain" yes), "stub" ok. EXPLAIN "Why must it be exactly one cluster per track" - hard to answer for a beginner; "partition: no overlap, nothing left out" appears in Glossary, not at the step. Add a hint.
 Minutes: 8.

## Step 09b
PREDICT: green (13 passed); union-find: "each item starts as its own boss; when two match, one boss adopts the other".
ACTUAL: "13 passed". Matched: yes. Workbook alone enough: yes. Prompt: right thing produced.
 EXPLAIN (1): "Why does clustering by chains still give clean groups?" Student answer: because a chain match joins the group, so we never need the ends to match. Hint helps. (2) 206 lands in the Slow Orbit cluster (1 away from 205, 4 from 210), not wanted - it is a different song. I could answer ONLY because the hint/ numbers are in my head; the workbook's (2) uses 206 and the student's own numbers may differ (e.g. 200/204/208 -> still within 5). OK for typical choices but if student chose widely spread numbers (200, 205, 210) it still works. Fine.
 Gaps: "union-find" is unexplained in text; the prompt asks the coach to explain it in two sentences (OK). The coach's code is ~15 lines: the student cannot verify it; they only check the groups. Acceptable but "we checked it" = test pass only. The test checks only the TRACKS data; no test for chain joining independent of looks_alike. Fine.
 Minutes: 10 (reading union-find explanation is slow for strugglers).

## Step 10a
PREDICT: is_duplicate(1,2) True (same song, 2 >= 1). is_duplicate(2,1) False (1 >= 2 is false). Symmetric?: No.
ACTUAL: "1 failed, 14 passed". FAILED: test_duplicates.py::test_symmetric ("is_duplicate(1, 2) is True but is_duplicate(2, 1) is False"). Matched: yes; prediction right.
Workbook alone enough: yes. Prompt right thing: yes.
 Gap: the PREDICT asks "is_duplicate(1, 2)" with ids; a student must know id 1 and 2 are the Slow Orbit tracks (they know from Step 07). Fine. Also is_duplicate is given in the prompt as code (b.id >= a.id): a coach could "correct" it - rule 3 says do not change tests, nothing says "do not fix this rule" except the prompt's last sentence. OK.
 Minutes: 6.

## Step 10b
PREDICT: green, 15 passed. Fix = drop the b.id >= a.id part.
ACTUAL: "15 passed". Matched: yes. Workbook alone enough: yes. Prompt: ok (coach could write several valid fixes).
 EXPLAIN "why is which-one-to-keep different from are-these-duplicates": answer: duplicate is a yes/no about a pair, symmetric; keep is a choice that needs an order. Workbook foreshadows "handled later" - good.
 Minutes: 5.

## Step 11a
PREDICT: Glass Harbor (id 5) and Night Bus (id 6), both 351s.
ACTUAL: "2 failed, 16 passed". FAILED: test_antisymmetric ("tracks 5 and 6 are different..."), test_sort_gives_one_answer ("2 different orders"). Matched: yes (red on antisymmetric and one answer); ids 5 and 6 = my prediction.
Workbook alone enough: yes, but: 
 - Hidden dependency: prediction is only 5 and 6 if the student's Step 07 lengths avoid 204 and 351 (and each other). If a pair picked 204 for a Slow Orbit, 2-4 also tie and "which two" has 2 answers. Antisymmetric_failure returns the FIRST pair it finds (could be 2 and 4 rather than 5 and 6) -> "Did the two ids match" would fail confusingly.
 - Terms before explained: "permutations"/"itertools"/"cmp_to_key" in the prompt - coach handles; Glossary has permutations. 'one answer' phrasing ("sorting every shuffle gives exactly one answer") is not explained in student language. Antisymmetric defined in Beat 5 intro - good.
 - Prompt for coach: 'message names the two different tracks' clear. Right thing produced.
 Minutes: 12 (PREDICT 2 min; understanding "two orders" is the hard part).

## Step 11b
PREDICT: green, 18 passed. Adding id makes each track's key unique so nothing ties.
ACTUAL: "18 passed". Matched: yes. Workbook alone enough: yes. Prompt: ok.
 EXPLAIN why id fixes it: because ids are unique, no two different tracks can be equal in the key, so 0 only for the same track.
 Gap: prompt says "compare may return 0 only for the very same track" fine. The key tuple order puts seconds first: fine.
 Minutes: 6.

## Step 12a
PREDICT: clean_playlist(TRACKS) -> ids [1, 4, 5, 6]. On its own result: the same, [1, 4, 5, 6].
ACTUAL: "2 failed, 21 passed". FAILED: test_earliest_of_each_song_in_id_order, test_reversed_input_same_result. Passing with stub: no_duplicates, empty, twice. Matched workbook: yes. Predictions right.
Workbook alone enough: yes. Prompt: right thing produced.
 Ambiguity: "the reversed input (reversed(TRACKS)) gives the same result" - reversed() returns an iterator, coach must wrap in list; the clean_playlist must accept any iterable (stub uses list(tracks) so iterator works). Fine. Also "same result" - same ids or equal Track lists? Equal anyway (frozen dataclass).
 Gap: the PREDICT 'on its own result' leaves a learner not grasping idempotence word; the workbook never names it ("cleaning twice gives same answer as once" - plain, good).
 EXPLAIN: tests that already pass with a stub (no dups, empty, twice) are weak - they only guard against breaking things (like characterization tests); they cannot prove the function works.
 Minutes: 8.

## Step 12b
PREDICT: green, 23 passed. Use dict key->earliest track.
ACTUAL: "23 passed". Matched: yes. Workbook alone enough: yes. Prompt: yes.
 EXPLAIN: Step 12b easy because song_key (Step 08) already turns each listing into one key; grouping by key is a dictionary lookup.
 Minutes: 5.

## Step 13a
PAPER (before anything): arrows: clean_playlist->song_key, is_duplicate->same_song, same_song->song_key. Test first: song_key, looks_alike, cluster_by_chain, compare, length_label (they need nothing).
 Then same_song, then is_duplicate and clean_playlist.
ACTUAL: "1 failed, 24 passed". FAILED: test_needs_come_first. test_each_function_once PASSES with the stub (list(graph) lists each once).
Matched workbook "red": yes, but workbook does not say one of the two tests passes already (unlike 12a which lists passing ones). Mild confusion.
Workbook alone enough: mostly.
 Gaps/ambiguities:
 - "Step 13" is the first time the graph's meaning ("X needs Y" = X uses Y) appears; prompt explains. 'graph', 'dependents first', 'leaves' (a tree word) - 'leaves first' is explained in Glossary only vaguely ("pieces that need nothing"). Glossary 'depends on' present.
 - The Step 13a graph lists length_label, but the fast-path pair never created lengths.py (skipped 04). Not a test failure (strings), but "Steps 09-14 need files from 06-08 only" is true; fine. A pair confused: "where is length_label?" - one clause would help.
 - The paper answer is given in the EXPLAIN line of 13a (spoiler, so the "Do this on paper first" question gets answered before they try). Minor.
 - EXPLAIN "Why does test order matter for finding bugs?" - student: if you test same_song before song_key and it fails you don't know which one is broken.
 Prompt text lets coach produce right thing: yes.
 Minutes: 12 (paper arrows, graph reading).

## Step 13b
PREDICT: green, 25 passed. Order will start with song_key (first leaf reached from dict order is clean_playlist -> song_key).
ACTUAL: "25 passed". Matched: yes. Order printed (coach's debug): song_key, clean_playlist, same_song, is_duplicate, looks_alike, cluster_by_chain, compare, length_label.
 FINDING: this is a valid order but does NOT match the workbook's stated paper answer ("the five leaves first, same_song next, is_duplicate and clean_playlist last"). EXPLAIN says "Compare Claude's order with your paper answer" - a struggling pair will think one is wrong. Workbook should say: "many orders are right; the test only checks that every function comes after what it needs. clean_playlist right after song_key is fine."
 Prompt: 'depth-first walk' etc. produces right thing. Minutes: 8.

## Step 14a
PREDICT: for {"a":{"b"},"b":{"a"}}: no right order exists (a needs b, b needs a). So it should be an error, not an order.
ACTUAL: "2 failed, 25 passed". FAILED: test_cycles.py::test_two_cycle_raises, test_three_cycle_message_names_loop (both "DID NOT RAISE"). Matched: yes. Prediction right.
Workbook alone enough: yes. Prompt right thing: yes. Note: test file uses pytest.raises (new idea, never introduced; coach tests it fine; A4 explains "raise" only). Minutes: 6.

## Step 14b
PREDICT: green, 27 passed; coach keeps a "current path" list, and if a function is already on the path it raises with the loop printed.
ACTUAL: "27 passed". Matched: yes. Workbook alone enough: yes. Prompt right thing: yes ("Track the current path" is enough). Gap: message format "a -> b -> c -> a" is in 14a prompt only; 14b prompt says "naming the loop" - coach relies on the existing test, fine since tests are in the folder.
 EXPLAIN: a cycle means two pieces each need the other, so there is no first thing to test; the design should change (split or move a shared piece out).
 Minutes: 8. Final state: `python3 -m pytest -q` -> 27 passed.

## Part C
C1 (student): "I showed that 'within 5 seconds, same artist' is not an equivalence relation, because it is not transitive (the counterexample: 200 s, 205 s, 210 s: 1~2 and 2~3 but 1 is 10 s from 3), and I fixed it by comparing a normalized key (lowercase artist and title with brackets and punctuation removed) so equal keys always chain."
C2 honesty log (sample): Step 06b | Claude wrote looks_alike | ran 5 tests, hand-checked 105 case | agreed. Step 08 | song_key | printed keys vs my PREDICT | agreed. Step 09b | union-find | checked groups on paper, tests; could not read the code | agreed (tests only). Step 13b | leaves_first | compared order to paper | DID NOT match the stated paper order but valid.
C3: last step finished 14b; counterexample as C1; wrong prediction: (honest) none wrong in this dry run - a real pair would likely miss 06a "exactly 5". Change next time: use key rather than closeness.
Part C notes: C2 table is empty with one blank row, fine. C3 asks to "paste red output at Step 07" - student must save it BEFORE going on (the red is gone after 08, since the same test goes green). Not said. Wait: the 07 red test is gone at Step 08. Add "copy it now". C1 pattern needs the word "is / is not" - ok; the pattern uses "equivalence relation" which a pair that skipped Steps 02-03 meets only in Step 08 text and glossary (Step 08 does not use the term "equivalence relation" apart from title; Step 05 defines it, but 05 is skipped on the fast path!). Rank high: fast path pair never sees a definition of reflexive/symmetric/transitive/equivalence in the flow (defined in 02/03/05 which are skipped; only Glossary and the 'chairs' picture in Beat 2 intro). Step 07 text says "claim this rule always chains" - the word "transitive" is used in Step 07 prompt and Part C without being defined in the fast path.

## TOP FIXES (ranked)
1. Fast-path pair skips Steps 02/03/05 where "transitive", "equivalence relation", "reflexive", "symmetric" are defined; Step 06-08 and C1 use them. Add a 3-line definition box at the top of Beat 2 (chairs picture is there but doesn't name transitive) and in C1.
2. Step 07: say "REPLACE the existing TRACKS line" (otherwise old TRACKS may override and test goes green vacuously); fix starter comment ("Step 6" -> "Step 7"); tell pairs to avoid 204 and 351 (collides with Paper Moons / Glass Harbor/Night Bus, breaks Step 11a prediction).
3. Glossary counterexample row spoils Step 07 answer (200/204/208) and says "gap of 5" which is wrong (ends 8 apart). Also Step 03's table uses the same numbers. Replace with different numbers or a non-playlist example.
4. Step 06a: the prompt must contain the PREDICT numbers (Zed 100 vs 104 etc.); otherwise coach invents numbers and the pair cannot compare to predictions. Number the five cases so predictions map to test names.
5. Step 13b: the stated "paper answer" order is not what a correct depth-first walk produces; add "any order where every function comes after what it needs is right".
6. Step 07/08: say "the red transitive test from 07 is the same test that goes green in 08"; and tell pairs to save the red output now (C3 asks for it, but it is gone after 08).
7. Mention at the start that fast path = 01, 06a, 06b, 07, 08 (currently only at line 99, after Part A) and what to do for steps with passing tests under a stub (13a does not list which test passes).
8. Glossary step references are for Tuesday numbering ("Step 1", "Step 3", "Step 6") and do not match the workbook's steps; characterization test says Step 3 but is Step 05. "diagonal", "matrix", "gap", "cluster", "pytest.raises" missing/unclear.
9. 12a says "duplicate and shuffle tests" but the test is the reversed input; harmonize wording.

## UNEXPLAINED TERMS
- "diagonal" ("sit just above the diagonal", Step 01), "matrix" (only in Step 01 text)
- "transitive", "equivalence relation", "reflexive", "symmetric" before Step 06-08 on the fast path (defined only in skipped Steps 02/03/05; "transitive" used in Step 07 prompt/PREDICT-free text, C1 and C4 "equivalence")
- "chains" / "chain" ("this rule always chains", Step 07) - only the chairs picture
- "canonical key" (Glossary points to Step 08 but not used there)
- "union-find" (prompt asks coach to explain; Glossary says do not write it)
- "pytest.raises", "cmp_to_key", "itertools.permutations", "parametrize" appear in prompts (coach-side) but not in glossary except permutations
- "idempotent"-like idea ("cleaning twice") fine; "leaves first" / "leaf" (tree word) vague
- "drift" (Step 09b) only in italic aside
- "gap" (used as the difference in seconds in Step 07) never defined, fine in context
- "dependents first" (Step 13a prompt)
- "partition" mentioned in 04 and Glossary only

## TIME ESTIMATE (struggling real pair)
Part A read + setup: ~15 min. Fast path 01+06a+06b+07+08: 8+10+5+15+12 = 50 min -> about 65 min with Part A, plus Part C ~10 min = ~75 min (over a typical 50-min class; Step 07 and the Step 01 paper work are the sinks; realistic fast path alone: 65-75 min).
Extended steps 09a-14b: 8+10+6+5+12+6+8+5+12+8+6+8 = ~94 min.
Full run (fast path + extended + Part C): ~3 hours.
