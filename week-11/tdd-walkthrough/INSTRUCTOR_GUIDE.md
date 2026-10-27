# Instructor guide — building the duplicate-record merger live (relations in your tests)

Written for someone who does not find this natural. Follow it in order. Everything you type or paste is in a box. Numbers like **Prompt 07** are `prompts/07_*.md`; **Tag 06** is git tag `tdd-step-06`; slide references use the deck's frame titles (the deck is built by a separate session; the principle index at its end lists slide numbers).

## 0. What this session teaches, in plain words

A **relation** is a rule that says which pairs of things go together ("sits next to", "is a duplicate of", "must be built before"). Four questions sort relations: **reflexive** (is everything related to itself?), **symmetric** (if A goes with B, does B go with A?), **antisymmetric** (can A and B each come before the other while being different? it should not), **transitive** (if A~B and B~C, is A~C?). A relation that is reflexive + symmetric + transitive is an **equivalence** (it sorts things into groups: seat pods, bins, duplicates). One that is reflexive + antisymmetric + transitive is a **partial order** (things come before other things: build order, test order). Every property can be checked by a test, and every "no" comes with a **witness**: the exact pair or triple that breaks it.

The story: students merge duplicate student records. The obvious rule ("names that look alike") quietly fails transitivity, a property test proves it with Jon/John/Jonathan, and the fix is a canonical key. Then one "equals" fails symmetry, one sort fails antisymmetry, and the project's own function dependencies form a partial order whose cycle is a design smell.

## 1. Audience reality — rules for you (read twice)

Unit testing, TDD, and abstraction are hard for these students. So:
1. **Concrete before abstract.** Every idea starts with a thing they can see (seats, grade bins, two records), then the word.
2. **Why before how.** Open with the 2-minute "why test first" story (section 3). Do not start with code.
3. **Tiny steps.** One new idea per step. Each ends with a visible red or green.
4. **Same loop every step: Predict → Run → Explain.** Ask for a guess (30 seconds, hands or sticky note), run, then have a student explain the result. The expected answer is in each prompt file ("Predict first").
5. **Red is normal.** Say it out loud, repeatedly: "Red is not failure. Red means the test is awake."
6. **Jargon ledger.** The first time you say a term, say its one-line meaning from the glossary below and point to the handout.
7. If Claude's live output drifts, use the recovery move (section 2), narrate it honestly ("Claude took a different road; I'll jump to the known-good copy"), and move on.

## 2. Setup (before class, 10 minutes)

```bash
git clone git@github.com:jeremy-evert/discrete_structures_and_critical_thinking.git dsct   # or use your clone
mkdir -p ~/tdd-live && cd ~/tdd-live
python3 -m venv .venv && . .venv/bin/activate && pip install pytest
export LADDER_REPO=~/dsct          # where the clone is
python3 --version                  # must be 3.9 or newer
```
Open three things: a terminal in `~/tdd-live`, Claude (Claude Code or chat with file access) pointed at `~/tdd-live`, and `prompts/` open in an editor to copy from. Project screen: terminal on one half, Claude on the other.

**Recovery move (any step):** in `~/tdd-live` run `~/dsct/week-11/tdd-walkthrough/tools/recover.sh NN` (restores `merger/` and `tests/` to tag `tdd-step-NN`). For Prompts 01–03 copy the file from `reference/demos/` into `demos/`. To see the whole ladder passing/failing before class: `tools/ladder_check.sh`.

**Practice run:** do Prompts 00–14 once at home before class. A dry-run record (an independent Claude doing the same) is in the report.

## 3. Opening: why write a test before the code? (4 minutes, no code)

Say: "A smoke alarm. Before you cook, you press the test button. If it stays silent, you know the alarm is broken before there is a fire. A test written first is a button we press to prove our alarm can ring. If we write the code first and the test second, we cannot tell whether the test is able to fail."
Second analogy (30 seconds): "Taste the sauce *before* adding salt so you know what changed."
Ask: "When would you not trust a smoke alarm you had never heard ring?" Expected: if it never rang, I don't know if it works. Land it: **a test that has never been red might be a test that can never be red.**

Three words to teach on the spot (full list in section 9): **test** = a small program that checks one claim and says pass or fail; **red/green** = fail/pass colours pytest prints; **TDD** = write the test, see red, write the code, see green.
Name the feeling: "Red tests are normal and good. Every professional sees red many times a day."

## 4. Timeline (full path; the 75-minute cut is in section 5)

| Min | Prompt | Say / do | Ask the room | Expected answer | Properties / relation types shown |
|---|---|---|---|---|---|
| 4 | — | Section 3 | smoke alarm question | an untested alarm is untrustworthy | — |
| 2 | 00 | Paste Prompt 00. "These are the rules for our robot helper." | — | Claude says "ready" | — |
| 4 | 01 | Paste. Show pairs, matrix, arrows. "Same facts, three pictures." | How many pairs? Same flipped over the diagonal? | 8; yes | symmetric (visible in matrix) |
| 6 | 02 | Paste. Read each property aloud with the seat example. | Is anyone next to themselves? | No → reflexive fails, witness Ana | all four; witnesses |
| 5 | 03 | Paste. Read the verdict column. | Which row is "neither"? | sits-next-to and `<` | **equivalence** (birthday month), **partial order** (divides, ≤) |
| 8 | 04 | Prompt 04A red; ask; run; then 04B green. Stress "stub only, no code yet". | Why must it fail first? | proves the test can fail | partition into bins, boundaries |
| 4 | 05 | Paste. "Passed at once is OK here." | Why is this one allowed to pass first time? | it records a fact about finished code | reflexive, symmetric, transitive of "same bin" → equivalence |
| 7 | 06 | A red, B green. At the end point at Jon~Jonathan False. | Will Jon and Jonathan match? | surprise: no | (setup) |
| 6 | 07 | Paste. Leave it red on purpose. | Three names where A~B, B~C, but not A~C? | Jon, John, Jonathan | **transitive** fails; witness |
| 6 | 08 | Paste. "Do not edit the tests." | Will the unchanged tests pass? | yes: equal keys are an equivalence | equivalence by construction; tradeoff: nickname table |
| 6 | 09 | A red, B green. | Which two get grouped but were never similar? | Jon and Jonathan | equivalence by chains; over-merge tradeoff |
| 7 | 10 | A red, B green. | Which direction says duplicate? | (1,2) yes, (2,1) no | reflexive holds, **symmetric** fails |
| 7 | 11 | A red, B green. | What does a comparator returning 0 for different people mean? | each is "at or before" the other | **antisymmetric** fails; partial/total order |
| 6 | 12 | A red, B green. | How many merged records from 5? | 4 | classes of the equivalence become merged records |
| 8 | 13 | A red, B green. | Which function do we test first? | one that needs nothing (`_split`) | **partial order** (depends-on), leaves first |
| 6 | 14 | A red, B green. | Which first, if parse needs validate and validate needs parse? | neither | cycle breaks antisymmetry → design smell |
| 4 | — | Self-check list (section 8). | — | — | — |

Total about 96 minutes. Do not try all of it in one 75-minute class.

## 5. The 75-minute cut (recommended Tuesday) and what to hold back

**Core path, ~65 minutes + wrap:** why 4 · 00 (2) · 01 (4) · 02 (6) · 03 (5) · 04 (8) · 06 (7) · 07 (6) · 08 (6) · 10 (7) · 13A/B read-only walk of the printed order (6) · wrap (4). Skip 05, 09, 11, 12, 14 live; they stay as take-home prompts or a later class. This still shows: bins (equivalence), a transitivity failure with a witness, the fix, a symmetry failure, and a partial order.
Say the cut out loud so students know the rest exists. **Decision for Jeremy:** whether this runs Tuesday-style in one session, over two sessions, or Thursday 10-29 or a later week, and how it relates to the existing Tuesday/Thursday run-of-shows (see report).

## 6. Step-by-step detail

For each prompt: open `prompts/NN_*.md`; follow Predict → Run → Explain.

- **00 Rules.** Paste the block. If Claude starts coding, stop it: "Wait. Only reply 'ready'."
- **01 Seating.** After the run, say: "This is a relation: a list of pairs. The matrix and the arrows say the same thing three ways." Point to row Ben: 1s under Ana and Cy only. *Common slip:* Claude lists 4 pairs; ask for both directions.
- **02 Properties.** Read the output line by line with the seating chart behind you. "Reflexive: is a seat next to itself? Witness: Ana." "Antisymmetric: Ana-Ben and Ben-Ana both exist, so the answer is 'fails', witness Ana, Ben." Then divides: "1 divides 2, 2 does not divide 1; symmetric fails, witness 1, 2."
- **03 Classify.** "Four yes/no answers decide the kind." Walk row 5 (`<`): fails reflexive, so *neither*. Students often expect "partial order" — let them argue.
- **04 Bins.** A: paste, let Claude write the stub and tests, run → all red. Ask why before writing code. B: green; read the bins. "101 scores, five groups; one test per group plus the edges."
- **05 Same bin.** Introduces `tests/relations.py` (four helper checkers that return a witness or None). "Reflexive: each score is in its own bin. Symmetric: A same bin as B means B same bin as A. Transitive: A with B and B with C means A with C. Equivalence."
- **06 Fuzzy.** A red, B green. Before running the print: "Will Jon and Jonathan match?" Most say yes. It prints False.
- **07 Transitivity.** The pivotal moment. Leave it red. Read the failure message aloud: `'Jon Smith' ~ 'John Smith' and 'John Smith' ~ 'Jonathan Smith' but 'Jon Smith' !~ 'Jonathan Smith'`. "That is a witness. The test did not just say no, it showed us the exact three names."
- **08 Fix.** "Instead of asking 'are these two close?' we turn each name into a standard spelling, and compare spellings. Same spelling = same group. Groups cannot fail transitivity." Tradeoff to state: it only knows nicknames in our table.
- **09 Chains.** Alternative when you have no table. Tradeoff: a chain can join people who never matched directly.
- **10 Symmetric equals.** Show that the same two records disagree depending on order. Fix: emails must be equal.
- **11 Sort.** "A sort must give one answer however the list started out." The shuffle test proves it.
- **12 Merge.** All earlier ideas in one function.
- **13 Depends-on.** "Which function needs which?" The code reads itself with `ast`. Test the functions nothing else needs first.
- **14 Cycle.** "No first thing to test." The error names the loop.

## 7. Where each property and relation type appears

| Idea | Prompt(s) | Tag(s) | What students see |
|---|---|---|---|
| Reflexive | 02, 05, 07, 10 | 03, 06, 10 | a record/score related to itself |
| Symmetric | 02, 05, 07, **10** | 10 red → 11 green | `is_duplicate(1,2)` ≠ `is_duplicate(2,1)` |
| Antisymmetric | 02, **11**, 14 | 12 red → 13 green, 18 | different records each "at or before" the other |
| Transitive | 02, 05, **07**, 08, 09 | 06 red → 07 green | Jon ~ John ~ Jonathan, Jon ≁ Jonathan |
| Equivalence relation | 03, 05, 08, 09, 12 | 03, 07, 09, 15 | bins, canonical key, groups, merged records |
| Partial order | 03, 11, 13, 14 | 12, 13, 16, 17, 19 | sort order, depends-on, test leaves first |
| Witness / counterexample | 02, 07, 08, 10, 11, 14 | 06, 10, 12, 18 | a printed pair or triple |
| Partitioning / boundaries | 04, 05, 06 | 01–03 | 59/60, 69/70, 89/90, 100/101 |

## 8. Self-check list (end of class, and for the reader of this guide)

Tick each when you can say it in your own words:
- [ ] I can explain why a test is written before the code (smoke-alarm button).
- [ ] I can say what red and green mean and why red first is good.
- [ ] I can draw a relation as pairs, a matrix, and arrows.
- [ ] I can ask the four property questions of any relation and give a witness for each "no".
- [ ] I can tell an equivalence from a partial order using the three-property rule.
- [ ] I can name the three names that break transitivity, and why a canonical key fixes it.
- [ ] I can explain why `is_duplicate(a, b)` must equal `is_duplicate(b, a)`.
- [ ] I can say why a comparator returning 0 for different records is a bug.
- [ ] I can explain why a dependency cycle means there is no first thing to test.
- [ ] I know the recovery move and when to use it.

## 9. Glossary (plain words; same list in the handout)

| Term | Plain meaning |
|---|---|
| test / unit test | a small program that checks one claim about one small piece of code and reports pass or fail |
| assert | a line in a test that says "this must be true"; if it is false, the test fails |
| pytest | the program that runs our tests and prints red (fail) or green (pass) |
| red / green | a failing test / a passing test |
| TDD | write the test, watch it fail, then write the code, watch it pass |
| stub | a placeholder function that does nothing useful yet (here: raises NotImplementedError) |
| fixture | fixed sample data used by many tests (our list of names and records) |
| relation | a rule saying which pairs of things go together; stored as pairs |
| ordered pair | (A, B) where order matters; (A, B) is not (B, A) |
| reflexive | everything is related to itself |
| symmetric | if A is related to B then B is related to A |
| antisymmetric | if A and B are each related to the other, they must be the same thing |
| transitive | if A~B and B~C then A~C |
| equivalence relation | reflexive + symmetric + transitive; sorts things into groups |
| partial order | reflexive + antisymmetric + transitive; says what comes before what |
| partition / bin | a way of splitting inputs into groups that behave the same (here: grade bins) |
| boundary | the edge of a bin (59 vs 60), where mistakes hide |
| property test | a test that checks a rule over many items instead of one example |
| witness / counterexample | the exact pair or triple that shows a property fails |
| canonical key | a standard spelling of a name; two names are the same person when their keys are equal |
| union-find / connected components | grouping things that are linked by any chain of matches |
| design smell | a sign in the structure (like a dependency loop) that something should be redesigned |
| dependency | a function another function calls and needs |

## 10. If things go wrong

| Problem | Move |
|---|---|
| Claude writes code in a red step | "Delete that code. Stub only. Show me the red." |
| Claude edits a test to make it pass | "Undo. Do not edit the tests." Then redo the green step. |
| Output differs from expected | `tools/recover.sh NN` for the last tag, narrate it, continue |
| pytest not found / import error | `pip install pytest`; check `pytest.ini` has `pythonpath = .` |
| Out of time | stop after Prompt 08 or 10; Section 5 lists what to hold back |
