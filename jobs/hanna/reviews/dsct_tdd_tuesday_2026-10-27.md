# Sandy the Skeptic — DSCT TDD Tuesday demo review

- **review_id:** `sandy-sol-hanna-20261027T1150CDT`
- **role:** Sol / adversarial review (Sandy the Skeptic)
- **review date:** 2026-10-27
- **bounded_scope:** review the Tuesday TDD demo core for simplicity, clarity, excitement, and live reliability; inspect only the DSCT walkthrough inputs; write this receipt only. No Canvas, student data, merge, or changes to Anna/Flo branches.
- **terminal_state:** `COMPLETE` for the 12:30 class verdict at 12:15 PM CDT. The deck report labels this a first-usable, partial package with another update due at 4:00 PM; the conditional Thursday final-package pass remains a follow-up after that update lands.

## Input refs

- Work order: `foreman_interface/jobs/tasks/hanna_review_dsct_tdd_tuesday_demo_2026-10-27.md` (run-bound SHA-256 supplied by dispatcher: `52633dce76ae711235dd287cd28ba4d6dcc2eb1fb835eda4d16808945d602795`).
- Review rule: `foreman_interface/spells/sol.md` (Sandy the Skeptic / Sol adversarial review).
- Anna core: `origin/anna/dsct-tdd-relations-20261027` at `4d1b0c69bc02a227661693fd030bca31f6eb4db3c`.
- Ladder: `tdd-step-01` through `tdd-step-19` are present; `tools/ladder_check.sh` checked every tag.
- Deck: `origin/anna/dsct-tdd-deck-20261027` at `1c2affc4547313f0776ee4f96f764cc04f8f9bd2` (arrived after the 12:00 snapshot; fetched at 12:12 CDT). `deck/REPORT.md` calls this the first-usable partial deck and says a final update is due at 4:00 PM. This is a separate deck branch; its prompts were compared against the prompt files from the core branch above.
- Comparison materials: `week-11/tdd-walkthrough/STEPS.md`, `prompts/00`–`prompts/14`, `INSTRUCTOR_GUIDE.md`, `STUDENT_HANDOUT.md`, `CONCEPT_MAP.md`, and `REPORT.md` at the Anna core tip.

## Checks attempted

1. Read the stated review lens, criteria, scope, and Sol receipt requirements in the assigned work file and `spells/sol.md`.
2. `git ls-remote https://github.com/jeremy-evert/discrete_structures_and_critical_thinking.git 'refs/heads/anna/dsct-tdd-relations-20261027' 'refs/heads/anna/dsct-tdd-deck-20261027' 'refs/tags/tdd-step-*'` — Anna core and all 19 tags present; deck branch absent. Repeated at 11:50 and 12:00 CDT. SSH `git fetch origin` was attempted first but failed before connecting: `Bad owner or permissions on /etc/ssh/ssh_config.d/30-libvirt-ssh-proxy.conf`; read-only HTTPS ref checks were used instead.
3. Fresh clone of the Anna relations branch under `worktrees/hanna-dsct-tdd-review-20261027`; initial status clean. `week-11/tdd-walkthrough/tools/ladder_check.sh` — all 19 tag outcomes matched their intended red/green status, ending with `tdd-step-19 | 39 passed`.
4. `python3 -m pytest -q week-11/tdd-walkthrough/tests` — `39 passed in 0.16s` on Python 3.12.
5. `make task-check` — unavailable: `make: *** No rule to make target 'task-check'. Stop.`
6. `make check` — unavailable: `make: *** No rule to make target 'check'. Stop.`
7. Blind live rehearsal: a sparse fresh clone exposed only `week-11/tdd-walkthrough/prompts/`; Codex executed the prompt blocks 00 through 14 in order, without access to the reference demos or completed implementation. Runtime was Python 3.9.25. Prompt 00 returned `ready`. Prompts 01–03 produced the requested examples/verdicts. For 04–14, observed phase results were: 04a 12 failed / 04b 12 passed; 05 13 passed; 06a 5 failed / 06b 18 passed; 07 one transitivity failure; 08 22 passed; 09a 3 failed / 09b 25 passed; 10a one symmetry failure / 10b 27 passed; 11a 2 failed / 11b 30 passed; 12a 3 failed / 12b 33 passed; 13a one test-collection error / 13b 36 passed; 14a one cycle failure / 14b 38 passed. Final suite: `38 passed in 0.14s`. Details of the consequential mismatch are in REPAIR-1 below.
8. `find week-11/tdd-walkthrough -maxdepth 2 -type d -name deck -o -type f -name '*.pdf'` — no output. No deck source existed to build, render, or compare against the prompt files.
9. Follow-up after the deck tip arrived: `./check_prompts.sh /mnt/brandy_nvme/jevert/git/worktrees/hanna-dsct-tdd-review-20261027/week-11/tdd-walkthrough/prompts` from the deck branch — passed: 23 prompt boxes, 38 index rows over 5 index frames, 57 content slides, and all 40 watched glossary terms present.
10. `./check_glossary.py` — passed (40 watched terms).
11. `./build.sh` first failed because the machine's default TeX font cache was read-only. With `TEXMFVAR=/tmp/hanna-dsct-texmfvar-20261027`, it passed: two PDFs emitted; `overfull/error lines: slides=0 notes=0`.
12. `pdfinfo` — both slide and notes PDFs have 62 pages. `pdftoppm -png -r 36` rendered all pages of both PDFs (124 PNG pages total). Visually inspected representative title/opening, counterexample, plan, and dependency-order pages and the opening notes page. The rebuilt PDFs and generated artifacts were restored/left uncommitted; the deck review worktree is clean.

## Findings

### REPAIR-1 — Dependency-order slide overstates which function must appear last

- **Locator/evidence:** deck slide 54/notes page 54 says the output “ends with `merge_duplicates`.” Core `prompts/13_dependency_order.md:27` says the order is not unique and explicitly says not to expect it to end with `merge_duplicates`. The blind rehearsal happened to end at `merge_duplicates`, confirming that this output is possible but not guaranteed.
- **Criterion violated:** Jeremy should be able to trust the “what you should see” cue and explain valid model variation without inventing a rule.
- **Smallest bounded repair:** change the slide and notes cue to say dependencies must precede callers; multiple valid orders exist, so do not require `merge_duplicates` to be last.

### REPAIR-2 — Prompt 13A can turn the expected three red tests into a collection error

- **Locator/evidence:** `week-11/tdd-walkthrough/STEPS.md:22` says Prompt 13 produces “3 red, then green.” In the blind rehearsal, the plausible test setup put `GRAPH = build_graph(names, records, pipeline)` at module scope (`tests/test_dependencies.py:8`) while the requested stub raises `NotImplementedError`. `pytest` therefore stopped during collection with one error instead of collecting and reporting the three expected failing tests. Prompt 13B then implemented the graph and the suite passed (`36 passed`).
- **Criterion violated:** the red/green outcome should match the step expectation, and a plausible Claude deviation should not leave Jeremy unsure whether the step is working.
- **Smallest bounded repair:** add a clear prompt instruction/test pattern that defers `build_graph(...)` until inside a test, or explicitly label the collection error as an expected red variant and teach the recovery action (`tools/recover.sh 16`). Then rerun the blind prompt 13A/B pair and update the step table to the observed supported outcome.

### REPAIR-3 — The opening hook arrives after the requested first three minutes

- **Locator/evidence:** `INSTRUCTOR_GUIDE.md:39-46` allocates four minutes to the smoke-alarm opening; the timeline starts it at minute 4 (`INSTRUCTOR_GUIDE.md:52`).
- **Criterion violated:** the review asks for a hook in the first three minutes. This opens with an analogy, but delays the concrete surprise that the brief identifies as the strongest hook.
- **Smallest bounded repair:** start in minute 1 with the Jon/John/Jonathan prediction (“If Jon matches John and John matches Jonathan, must Jon match Jonathan?”), then use the failing test as the reveal. Keep the smoke-alarm analogy as the short TDD explanation after the hook.

### POLISH-1 — Step 13 asks beginners to absorb several abstractions in one live step

- **Locator/evidence:** `prompts/13_dependency_order.md:8-24` combines AST parsing, call-graph extraction, graph traversal, dependency ordering, and transitive closure; `INSTRUCTOR_GUIDE.md:94` introduces reading code with `ast`.
- **Criterion at risk:** one new idea per step and first-year readable code. The step's purpose is “what can I test first?”, but the AST implementation can eclipse that concept.
- **Smallest improvement:** make a five-function dependency sketch visible first and ask which node has no prerequisites; keep the AST implementation as an optional extension.

## Dullest five steps, ranked, with sharper replacements

These are step-level judgments with their related slides cited; the slides are present but detailed rather than animated.

1. **Prompt 13 — Dependency order (slides 35, 53–54):** abstract AST + graph machinery makes the student watch code inspect code. Replace the opener with a five-card “who waits for whom?” ordering puzzle; reveal the code graph only after students find the first callable piece.
2. **Prompt 05 — Same-bin checkers (slides 27, 40):** a large checker implementation passes immediately and offers little visible tension. Replace the opening with “Which score flips grade at 90?”; show 89/90, then name the equivalence property after the boundary prediction.
3. **Prompt 11 — Antisymmetric sort (slides 33, 49–50):** comparator and `cmp_to_key` risk turning the story into Python API detail. Put Jon/John cards in both input orders and show the family-name-only sort preserve each order; ask whether the code actually chose between them.
4. **Prompt 12 — Merge pipeline (slides 34, 51–52):** “put it together” is a broad label. Give students five sample record cards and ask which records survive and which IDs combine before showing the merge output.
5. **Prompt 14 — Cycle smell (slides 36, 55–56):** cycle detection and closure vocabulary are less vivid than the no-first-step result. Have students physically order three dependency cards where each waits on the next; ask them to find the first card, then reveal the cycle error.

## Simplicity and clarity read

- Steps 01–03 provide a concrete progression from pairs to properties to classifications, but Step 01's stated outcome is only “8 pairs, symmetric matrix, arrows” (`STEPS.md:10`); it lacks an explicit pass/fail cue. Add a visible check label (“check passed: 8 directed pairs; matrix mirrors across diagonal”) so Jeremy can point to a result without inventing one.
- The topic sequence is understandable in the guide, but several steps introduce terms rapidly: Step 01 has relation/pairs/matrix/digraph; Step 02 has four properties plus witnesses; Step 13 stacks AST, graph, DFS, dependency and closure. The glossary helps after the fact; present one term at a time with the concrete artifact first.
- Excitement is strongest at Prompt 07's transitivity counterexample and Prompt 10's order-dependent duplicate result. Keep those as the payoff beats. The guide's 75-minute cut does keep the transitivity failure and a symmetry failure, but the deck alignment cannot be checked.
- The blind rehearsal confirms prompts 01–14 can grow a working implementation without the reference. Aside from the Prompt 13A mismatch, all final phase outcomes matched their textual expectations. Prompt-box parity against the pushed core prompt files passed for all 23 boxes. The dependency slide's claimed final function remains a misleading cue even though this particular rehearsal ended with `merge_duplicates`.

## Verdict

**Finding severity:** BLOCK: none. REPAIR: the dependency-order cue, Prompt 13A red-state behavior, and opening-hook timing (REPAIR-1 through REPAIR-3). POLISH: make Step 13 more concrete before introducing the AST (POLISH-1).

**12:30 teaching verdict: REPAIR.** Teach the 75-minute cut with the dependency-order section as a read-only walk, explicitly say valid dependency orders can vary, and avoid requiring `merge_duplicates` to be last. Keep Prompt 13A read-only or be ready to recover if it produces a collection error.

**Primary verdict: REPAIR** for teaching at 12:30. The deck is now available, all 23 prompt boxes match the core prompt files, the glossary and index checks pass, both 62-page PDFs compile with zero overfull/error log lines, and all 124 pages render. Before using the dependency-order slides, change the claim that `merge_duplicates` must be last; that contradicts the source prompt. The recommended 75-minute cut treats this dependency-order segment as a read-only walk, so Jeremy can teach it safely by describing only the ordering rule and noting that valid orders can vary. The blind rehearsal also found a collection-error variant in Prompt 13A; keep that out of the live run or use the recovery tag if a red state surprises the class. The opening hook reaches slide 3, but the guide allocates four minutes to it, so tighten the timeline if “within three minutes” is required.

**Plain-language summary for Jeremy:** The slides and notes have now landed and the checks pass: all 23 Claude prompt boxes match the source prompts, both 62-page PDFs compile and render, and the walkthrough reaches 38 passing tests after the intended red/green sequence. The Jon/John/Jonathan surprise is clear. I recommend teaching the 75-minute cut with the dependency-order slide as a read-only diagram, but do not tell students that `merge_duplicates` must be last; several orders are valid. Prompt 13A can also show a collection error instead of three red tests, so keep that step read-only or recover to its known-good tag if the output drifts.

## Reproduction limits and next action

- The deck review was against the separate deck tip `1c2affc` and source prompts at project tip `4d1b0c6`; the branches were not merged. The 62-page notes PDF provides one notes page per slide; no in-room usability test with Jeremy was possible.
- The blind run exercised prompts 00–14 using Codex; it was not a live classroom run with Jeremy, and no Canvas or student-facing system was touched.
- **Next action:** for today's class, say that any valid dependency order is acceptable; do not require `merge_duplicates` to appear last. After the final deck update is published, run the conditional Thursday pass on the guide, handout, concept map, and final deck; fix slide/notes 54 and revise Prompt 13A guidance/recovery before Thursday.

## Repository process receipt

- **AGENTS.md:** read the shared `/mnt/brandy_nvme/jevert/git/AGENTS.md` and DSCT `AGENTS.md`; neither was changed.
- **Diff check:** `git diff --cached --check` passed before publication.
- **Validation:** the tag ladder and fresh-clone pytest results are recorded above; no other tests were run.
- **Make checks:** `make task-check` unavailable with the exact error above; `make check` unavailable with the exact error above.
- **Publication:** receipt published to `hanna/dsct-tdd-review-20261027`; initial published commit `e657806de84a5a10db03e56094a5e6f105d81cda`; process addendum commit `db42b19d6196209a172f7a6078b2eea7afb04776`.
- **Final worktree status after publication:** `git status --short --branch` reported only `## hanna/dsct-tdd-review-20261027` (clean).
