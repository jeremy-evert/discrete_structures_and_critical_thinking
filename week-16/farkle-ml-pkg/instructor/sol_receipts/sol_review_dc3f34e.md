# Sol adversarial review — DSCT Week 16 Farkle ML package, pass 2

- `review_id`: `sol-dsct-w16-dc3f34e-20261103-pass2`
- `role`: Sol / adversarial review (Sandy the Skeptic)
- `verdict`: `REPAIR`
- `terminal_state`: `COMPLETE`

## Input refs

- Delivered result: commit `dc3f34e324ec85ba4615b0524c088b3f6c5e2cad`, branch `ivy/dsct-w16-farkle-ml-20261103`, package `week-16/farkle-ml-pkg/`.
- Accepted criteria: `<worktree>`, especially `Student-facing contents`, `Design rules`, and `Acceptance test` (lines 36-53).
- Approved plan: sibling scratch artifact `terra_plan.md`; Tectonic and the AI-failure-mode fallback are coordinator-approved substitutions.
- Literal worker inputs: sibling scratch artifacts `luna1_prompt.md`, `luna2_prompt.md`, `luna3_prompt.md`, and repair dispatch `luna4_prompt.md`.
- Prior Sol receipt: sibling scratch artifact `sol_review_096874e.md`, verdict `REPAIR`, findings F1-F7.
- Claims inspected but not trusted as proof: all `LUNA_RECEIPT*` files and `instructor/REPORT.md` at the delivered commit.
- Cross-scope baseline: `ee18526`.

## Bounded scope

Read-only review of the exact delivered commit. I created the execution tree with:

```sh
git -C <worktree> \
  archive dc3f34e324ec85ba4615b0524c088b3f6c5e2cad \
  week-16 lessons assignments planning | tar -x -C <scratch>
```

All builds, mutations, rasterization, and temporary ZIP work occurred in the scratch copy. I did not write to the reviewed worktree, contact Canvas, use student data, or use the network. Tectonic used the installed local font/cache state.

## Verdict summary

The executable/build/publication mechanics survived: clean-archive pytest passed, both negative controls failed, two deck builds were stable at 18/18 pages with zero real diagnostics, prompts matched, the manifest was safe, the ZIP was prompt-only, byte copies matched, and the fallback arithmetic recomputed correctly.

The package is nevertheless not acceptable yet. The repaired handout publishes two model sentences that reverse the seed-17 result; it exposes the bundle's signs and extrema before asking students to predict; its numeric-threshold rule conflicts with the published deck/prompt; first-use jargon remains; and the required coordinator report omits its promised tip and makes a false clean-grep claim. These are bounded repairs, so the verdict is `REPAIR`, not `BLOCK`.

## Prior F1-F7 disposition

| Prior finding | Pass-2 result | Evidence |
|---|---|---|
| F1 alternate-metric evidence absent | **Fixed by authorized reframing.** | `student/handout.md:77-81` and `student/thursday_activity.md:51-61` explicitly say no extra numbers are supplied, make the step reasoning-only, define candidate metrics, and give a sample answer. |
| F2 `instructor/REPORT.md` absent | **Partially fixed; remains REPAIR.** | The file exists, but `REPORT.md:5` promises a tip on the final line and supplies none; `dc3f34e...` does not occur in the report. See S2-F5. |
| F3 incomplete first-use vocabulary | **Partially fixed; remains REPAIR.** | The glossary is alphabetized and the named repair terms were mostly added, but `fallback fixture`, `benchmark`, and strategy-state jargon still fail first-use/plain-language review. See S2-F4. |
| F4 receipt route not reachable | **Logged, by design.** | Student pages name the assignment without inventing a URL (`handout.md:85`, `thursday_activity.md:105`); `REPORT.md:27` records the publisher/route question for Anna. |
| F5 strategies unexplained | **Fixed.** | `handout.md:54-55` and `thursday_activity.md:26-27` explain both strategies. The statements agree with `lessons/vendor/farkle_ml/strategies.py:13-24,99-112` and `learner.py:12-44,145-150`. |
| F6 package hostname grep failed | **Regressed; remains REPAIR.** | Older receipts were sanitized and validator fragments were split, but new `REPORT.md:18` contains `maise`; the literal package scan is nonempty. See S2-F6. |
| F7 prompts page H1 exception | **Logged, by design.** | `REPORT.md:22` records the exact-concatenation/H1 exception, and the validator reports it explicitly. Exact concatenation still holds. |

## Findings

### S2-F1 — HIGH — repaired model sentences reverse the actual seed-17 result

**Violated invariant:** Student-facing conclusions must agree with the supplied evidence; the fallback arithmetic and interpretation must not be invented or reversed.

**Evidence:**

- `student/handout.md:109` says: `A had the higher observed win rate in seed 17`.
- `student/handout.md:110` again says: `A had the higher observed win rate in this one row`.
- The same page's table at `student/handout.md:73` gives A = 3 wins and B = 7 wins, or 30% versus 70%.
- Independent `csv.DictReader` recomputation from `week-16/fallback/quick_v1_results.csv` produced `seed=17 wins=3/7 rates=30.0%/70.0% A-B=-40pp`.
- `canvas/handout.md` is byte-identical, so the error is on the manifest-published surface.

**Observed versus expected:** The examples declare A ahead where B is ahead. The expected limited observation is that **B** had the higher observed win rate for seed 17 under the fixed setup.

**Why independent:** The result was recomputed directly from the fallback CSV without importing `evidence_summary.py` or trusting any receipt/validator.

**Smallest repair:** Change both model sentences to B (and keep the limited scope), then re-copy the handout to Canvas and rerun the byte/manifest/numerical checks.

### S2-F2 — HIGH — Tuesday reveals the repeated-bundle answer before students declare the rule and prediction

**Violated invariant:** The accepted design is predict/check/explain with the decision rule and prediction written before repeated evidence; the repair specifically intended the full bundle for Thursday.

**Evidence:**

- `student/handout.md:28`, in the definitions before the activity, gives the actual bundle signs: `-, +, +`.
- `student/handout.md:30`, still before the activity, gives the actual extrema and range: `60 - (-40) = 100` and calls it the calculation for `the table below`.
- The request to write a rule and prediction does not occur until `student/handout.md:59-63`.
- The table below at `student/handout.md:71-73` contains only seed 17, so the +60 value is not from that table.
- The literal three-row-table check passes—only one row is displayed Tuesday—but the outcome that Thursday asks students to discover has already been disclosed.

**Observed versus expected:** A student reading top-to-bottom knows the ordering flips and knows the bundle range before making the supposedly pre-evidence prediction. The expected Tuesday page may define `sign` and `range`, but must use neutral/non-bundle examples or defer the actual bundle values.

**Comparison-set conflict:** `luna4_prompt.md:9` asked for the actual sign list and range calculation, while `luna4_prompt.md:15(a)` and the accepted design require Tuesday to withhold repeated evidence. The output followed the literal vocabulary example but breaks the higher-level learning sequence. This needs a bounded Foreman choice, not silent acceptance.

**Smallest repair:** Use unrelated example numbers to define sign/range, or move the actual `-,+,+` and `60-(-40)=100` work to Thursday. Correct `for the table below` regardless.

### S2-F3 — MEDIUM — the numeric-threshold rule contradicts the published deck and Prompt 01

**Violated invariant:** Students must receive one coherent, checkable procedure.

**Evidence:**

- `student/handout.md:29` says a decision rule **must include a number threshold**.
- `student/thursday_activity.md:18` tells students whose Tuesday rule had no numeric threshold to create one and mark it `LATE`.
- The published deck's worked rule at `deck/part1.tex:51` uses `more wins ... in every tested seed row` and refuses on reversal/tie, but gives no numeric threshold.
- Prompt 01 at `prompts/01_claim_and_rule.md:9-19` asks for a decision rule, metric, denominator, and scope, but never asks for a numeric threshold.
- The slide is manifest-published, and the prompt is both manifest-published and in the prompt ZIP.

**Observed versus expected:** A student can follow the official Tuesday worked rule/prompt exactly and be told Thursday that the rule was incomplete and must be labeled late.

**Why independent:** This is a direct cross-artifact comparison; `check_prompts.sh` can prove equality while still missing semantic contradiction.

**Smallest repair:** Either add a numeric threshold consistently to the deck and Prompt 01 (then rebuild/recheck all prompt artifacts) or change the handout/Thursday rule to accept a predeclared numeric threshold **or another explicit test**. The repair dispatch favors the first choice.

### S2-F4 — MEDIUM — first-use/plain-language vocabulary remains incomplete

**Violated invariant:** Contract design rules and the prior F3 repair require every technical term to be defined in plain language at first use.

**Evidence:**

- `student/handout.md:13` first uses `validated fallback fixture` and `benchmark`; `fallback fixture` is not defined until line 37, and `benchmark` has no glossary heading or inline definition.
- `student/handout.md:54` and `student/thursday_activity.md:26` use `turn-score buckets` and `dice remaining` to explain the learner, but do not explain what a bucket is; the glossary has no `turn-score bucket` entry.
- `canvas/validate_manifest.py:289-309` checks only that curated terms appearing in pages have glossary headings. It does not check first-use order or inline explanations, so `VALIDATION OK` is not evidence for the first-use requirement.

**Observed versus expected:** A first-year reader is told to understand the fallback's provenance and learner state through terms the page has not yet explained. The expected result is a short definition on first use (for example, a bucket groups nearby turn scores) and either a definition or removal of `benchmark`.

**Smallest repair:** Reorder the fallback definition before its first use, replace/define `benchmark`, and explain or simplify the learner-state wording on both pages. Extend the checker only if it can test order/inline definitions honestly; do not claim the current heading-presence check proves first-use compliance.

### S2-F5 — MEDIUM — required REPORT tip/evidence chain is incomplete and self-contradictory

**Violated invariant:** Contract acceptance line 52 requires `REPORT.md` with real results, judgment calls, tip SHA, unfinished work, and terminal state.

**Evidence:**

- `instructor/REPORT.md:5` says `Tip: see the final line.` The final line is a process lesson, not a Git SHA.
- `rg -n 'dc3f34e|Tip:|Terminal state|FINAL|VERDICT' instructor/REPORT.md` finds the terminal state and the broken `Tip:` reference, but not the delivered SHA.
- `instructor/REPORT.md:3` says the second Sol result is recorded in `Sol below`; no Sol section or verdict exists in the file.
- Read-only Git establishes the actual reviewed commit as `dc3f34e324ec85ba4615b0524c088b3f6c5e2cad` with parent `096874e...`.

**Observed versus expected:** The required tip/readback reference is absent, and the report claims a review section that does not exist. The expected report must identify exactly what tree its claims cover and accurately state that pass 2 was pending at commit time, or point to the durable external Sol receipt after completion.

**Smallest repair:** Replace the broken promises with an auditable commit/tree reference and an accurate link/path to this pass-2 receipt. Because a committed file cannot trivially self-contain its own final commit SHA, name the reviewed content commit/tree explicitly and have the coordinator's final external receipt record the branch tip.

### S2-F6 — MEDIUM — literal hostname cleanliness and REPORT's clean-grep claim are false

**Violated invariant:** Package-wide grep must contain no real fleet host names; report claims must match actual results.

**Evidence:**

```sh
rg -n -i 'april|maise|brandy|morgan|september|<worktree> \
  week-16/farkle-ml-pkg
```

returns:

```text
week-16/farkle-ml-pkg/instructor/REPORT.md:18: ... pdflatex absent on maise ...
```

Yet `instructor/REPORT.md:15` says `Package-wide grep for fleet host names and absolute paths: clean.` A separate real-host scan also finds the literal campus Canvas fragment `swosu.instructure` in `canvas/validate_manifest.py:124`; the validator was instructed to detect that string, but it remains a literal package-wide hostname fixture.

**Observed versus expected:** The requested grep is nonempty and the report says it is empty. The expected result is either neutral fake fixtures/phrasing or an explicitly accepted, narrowly documented fixture exception; a false `clean` claim is not acceptable.

**Smallest repair:** Replace the fleet host with `<build-host>` or a tool-only statement. Construct the Canvas-host fixture without embedding the production hostname, as was done for fleet fragments, or log a deliberate exception. Rerun and quote the exact final scan.

### S2-F7 — LOW — repair's Predict/Check/Explain wording is not consistent across the published package

**Violated invariant:** Literal repair input `luna4_prompt.md:15(i)` says to use `Predict, Check, Explain` consistently and leave no `predict-run-explain` wording.

**Evidence:** Student pages use `Predict, Check, Explain` (`handout.md:39-45`, `recap_outline.md:9`), but `deck/part1.tex:63` and generated `deck/index_rows.tex:9` still say `PREDICT -- RUN -- EXPLAIN`; the published PDF shows that text on slides 8 and 17.

**Comparison-set conflict:** The older contract says `predict-run-explain`, while the later repair dispatch says no such wording. This is a real source-of-truth conflict, not enough to block the package, but the coordinator report does not log it and the output is not internally consistent.

**Smallest repair:** Foreman chooses the canonical phrase, records why, and makes the student pages, deck, recap, and contract-derived report consistent.

## Attacks/checks attempted and results

### Clean execution and negative controls

```sh
(cd week-16/farkle-ml-pkg/code && pytest -q)
```

Result: `5 passed`, exit 0.

Two independent disposable copies of `code/` were mutated:

1. `win_rate_a = wins_a / (games + 1)` instead of `/ games`.
2. `sign_flip_detected = False` instead of checking both signs.

Results:

- Wrong denominator: exit 1, two failures (`test_fallback_bundle_rates_range_and_sign_flip` and tie-rate check).
- Dropped sign flip: exit 1, one failure at `test_fallback_bundle_rates_range_and_sign_flip`.

The tests are discriminating for both named defects.

### Deck builds and prompts

```sh
(cd week-16/farkle-ml-pkg/deck && ./build.sh)
(cd week-16/farkle-ml-pkg/deck && ./build.sh)
(cd week-16/farkle-ml-pkg/deck && ./check_prompts.sh)
```

Both builds exited 0 and reported:

```text
slides pages: 18
notes pages: 18
overfull/error lines: slides=0 notes=0
```

Independent `pdfinfo` read 18 slide and 18 notes pages after each build. Narrow log search for `Overfull`, TeX `!`, or actual `error:` diagnostics returned no matches. (`infwarerr` is a harmless TeX package name and was excluded from the diagnostic expression.)

`check_prompts.sh` exited 0 with four prompt boxes. Independently, each fenced prompt block byte-matched its generated `deck/prompts_txt/NN_a.txt`, and each `\promptbox{NN}{a}` include occurred exactly once in deck sources. Raster review of slides 7, 13, and 14 found no clipping/overlap.

### Manifest, copies, ZIP, and reachability

`python3 canvas/validate_manifest.py` exited 0 with `VALIDATION OK`.

Independent checks, not using validator conclusions, established:

- Seven unique page titles and all declared sources exist.
- Reachable paths are the seven `canvas/*.md` pages, `deck/farkle_ml_slides.pdf`, and `prompts/` only.
- No `instructor`, `code`, notes PDF, `REPORT`, `LUNA_RECEIPT`, `JUDGMENT_CALLS`, guide, or run-of-show path is manifest-reachable.
- The slide PDF has `0 embedded files`; the package has no symlinks.
- Student/Canvas byte matches hold for handout, concept map, glossary, Thursday activity, and recap.
- `canvas/prompts.md` equals the sorted byte concatenation of the four prompt files.
- A fresh temporary ZIP contains only the four prompt Markdown files at ZIP root.

### Independent numerical recomputation

Using only `csv.DictReader` and integer arithmetic on `week-16/fallback/quick_v1_results.csv`:

```text
seed=17   wins=3/7 rates=30.0%/70.0% A-B=-40pp starts=5/5
seed=6262 wins=6/4 rates=60.0%/40.0% A-B=+20pp starts=5/5
seed=2026 wins=8/2 rates=80.0%/20.0% A-B=+60pp starts=5/5
min=-40 max=+60 range=100 sign_flip=True
```

The evidence numbers in the slide tables, Tuesday table, Thursday table, and recap agree with this recomputation. The exception is interpretive rather than numeric: S2-F1 labels A as the higher-rate strategy for seed 17 despite the correct displayed numbers.

### Other required invariants

- No unqualified winner is declared as the package conclusion. Winner/best language is a rule, refusal, warning, or quoted AI claim to audit. The wrong seed-17 leader in S2-F1 still requires repair.
- No `student/decision-gate.md` exists. No student-facing Decision Gate text was invented. The special receipt distinction is confined to instructor/report material and student pages say there is no other Week 16 form.
- Recap count is exactly Tuesday=5 and Thursday=5.
- The glossary has 71 H2 entries and is alphabetized case-insensitively.
- The Tuesday handout contains only the seed-17 table row, but S2-F2 records the earlier leakage of the bundle's signs/extrema.
- Secret/key/token/email/nine-digit-ID scans returned no matches. Manual student-page reading found no student names or protected student information.
- `git diff --quiet ee18526 dc3f34e -- lessons/vendor` exited 0.
- `git diff --quiet ee18526 dc3f34e -- assignments/week-16-farkle-evidence-receipt.md` exited 0.
- `git diff --stat ee18526 dc3f34e -- . ':(exclude)week-16/farkle-ml-pkg/**'` and the matching name-status command produced no output.

## Reproduction limits

- Canvas/publisher execution was not attempted, as forbidden. Reachability conclusions are based on the manifest, resolved local paths, ZIP construction, and PDF attachment inspection.
- No roster or protected student dataset was accessed. The no-student-name conclusion is based on the supplied package text and identifier scans, not a roster comparison.
- Tectonic reused the installed local cache; no cold-cache or alternate-TeX-host test was attempted.
- Visual review sampled three high-density/prompt slides; full PDF text was extracted and searched, but every slide was not raster-inspected at full zoom.

## Next action

Return the slice to Flo for one bounded repair round:

1. Correct the two seed-17 model sentences.
2. Remove actual bundle signs/extrema from the pre-prediction Tuesday section.
3. Make the numeric-threshold procedure coherent across deck, Prompt 01, handout, and Thursday.
4. Define/simplify remaining first-use jargon.
5. Repair `REPORT.md` metadata and false claims; sanitize hostname fixtures.
6. Resolve and record the Predict/Check/Explain versus Predict/Run/Explain source-of-truth conflict.

Then rerun the same clean-archive test/build/manifest suite, both negative controls, numerical/readability checks, and a fresh Sol pass. Do not promote or publish this commit from this review.

VERDICT: REPAIR input_refs=dc3f34e324ec85ba4615b0524c088b3f6c5e2cad
