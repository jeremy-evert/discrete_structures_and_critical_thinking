# Tuesday Oct 13: teaching plan for counting, binomials and Pascal's triangle

Author: Flo (Claude Code, Brandy). Companion to `tuesday-run-of-show.md` (timing is unchanged) and `binomial-and-pascal-prep.md` (instructor explanations). Student page: `../student/pascals-triangle-and-binomials.md`.

## Why this lesson

Last week a gap showed up in combinatorics, binomial coefficients and Pascal's triangle. This plan puts that content inside the existing Tuesday-only week. It does not add a meeting, an artifact or a due date. Thursday Oct 15 is Fall Break.

## The three things a student should leave able to do

1. Say, before touching a formula, whether order matters, and count with `P(n,k)` or `C(n,k)` accordingly.
2. Justify a case split as **exhaustive and disjoint** (the Sam argument for `C(n,k) = C(n-1,k-1) + C(n-1,k)`).
3. Check a counting answer against a small enumeration or a row of Pascal's triangle.

## How it fits the run-of-show

| Time | Existing move | What this plan adds |
|---|---|---|
| 0:00 to 0:08 | AI Fluency: formula-first answer that mixes ordered and unordered | Use `5 x 4 = 20` for teams as the specimen answer. Students name the error. |
| 0:08 to 0:18 | A complete case split is a claim needing evidence | Introduce Sam in or out as the claim. Ask: how do we know no team is in both? |
| 0:18 to 0:35 | Four-student team example, enumerate | Build rows 0 to 5 of the triangle from the addition rule; point to the 6 in row 4 and the 10 in row 5. |
| 0:35 to 0:52 | Product-rule and team problems | Add: a student predicts a row-5 entry, then lists it to check. |
| 0:52 to 1:07 | Pair exchange | Unchanged. Prompt: "Could two descriptions name the same outcome?" |
| 1:07 to 1:20 | Assemble Decision Gate | Add the check habit from the student page (section 5). |
| 1:20 to 1:25 | Fall Break exit | Unchanged. |

## Exit check (one question, on paper, ungraded)

"From 5 students, how many 3-person teams? Say whether order matters, give your count, and show a check." Expected: 10, unordered, row 5 position 3 (equals `C(5,2)` by symmetry).

## Evidence to keep

Students' Decision Gate artifact (already specified in `student/decision-gate.md`). Nothing new is collected.

## Not in scope

Multisets and stars-and-bars, inclusion-exclusion, and the Fall Break week have no new content here. They belong to later weeks or the existing lesson stub.
