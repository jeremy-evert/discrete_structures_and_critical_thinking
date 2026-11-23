# Prompt 320 — Ship DSCT while Jeremy + Chaz rebuild Week 1

## Mission

Keep moving **already-authoritative DSCT** into real SWOSU Canvas course **74035** while Jeremy teaches and Jeremy + Chaz redesign the Week 1 teaching voice.

The goal is student-useful shipped work, not architectural perfection.

## Writer boundary

Jeremy + Chaz own Week 1 narrative and presentation work during this shift.

**Read if useful. Do not edit:**

- `planning/week-01-source-map.md`
- `week-01/instructor/**`
- `week-01/student/**`
- any new Week 1 presentation/Beamer source
- `semester_kickoff_week/**`

If a production problem appears to require changing that lane, report the seam and keep moving elsewhere.

## Known starting point — verify it yourself

Last known production state:

- Week 1 is published and student-usable.
- Week 2 is published but incomplete because some remaining page creates hit a content-specific CloudFront/WAF 403.
- A trivial Canvas probe succeeded during the same period, so this was not proven to be a blanket outage.
- Week 3 has substantial accepted source around the container/LaTeX skill ladder.
- Weeks 4–14 have a resolved spine, but a spine is not permission to invent lessons.

Begin with current Git truth plus a **read-only live inventory of course 74035**. Do not operate from this paragraph alone.

## Order of work

### 1. Confirm the floor

Verify Week 1 remains GREEN and inventory the exact live Week 2 delta.

Do not rewrite Week 1 while verifying it.

### 2. Give Week 2 one bounded attack

Do not hammer production with retries.

Dispatch bounded Golems to isolate the WAF/content seam using source, rendered HTML, diffs between successful and failing objects, and local/offline tests.

We are looking for a legitimate source/rendering/request defect or harmless equivalent representation. **Do not bypass or evade institutional security controls.**

If evidence supports a small repair:

1. dispatch implementation;
2. test it;
3. independently review it;
4. run the vetted production dry-run against exactly 74035;
5. require zero deletes and an explainable delta;
6. reconcile through the normal reviewed production path;
7. independently read back Canvas.

Production remains a single-writer Foreman responsibility. Golems do not get production-write authority.

### 3. If Week 2 does not fall quickly, MOVE

A stubborn yellow does not own the shift.

Evaluate Week 3 from its existing accepted artifacts and reports. If the source is sufficient, write a bounded implementation prompt, dispatch the compiler/deployment work, test, review, dry-run, ship, and read back.

If Week 3 is not actually ready, record exactly what source is missing and move to the next real authored unit.

For later weeks, distinguish:

- `SOURCE READY`
- `STRUCTURE ONLY`
- `NOT AUTHORED`

Ship the first. Do not fabricate the other two.

## Foreman rules

- Good enough and teachable beats immaculate and absent.
- Named yellows are acceptable. Silent defects are not.
- One logical change per commit; push durable evidence.
- Isolate Golem branches/worktrees and receipts so worker exhaust cannot contaminate another repo.
- Project truth lands in this repo first; JTT gets a thin status pointer after outcomes are verified.
- Do not ask Jeremy to relay worker messages, monitor shells, supervise retries, or decide implementation trivia.
- Stop only for a real pedagogy/policy conflict, destructive authority boundary, credential/physical action, safety approval gate, or materially conflicting source truth.

## Success

Best case: Week 2 reaches full production, Week 3 advances, and later authored material keeps moving.

Acceptable case: Week 2 remains a precisely named yellow while another legitimate student-useful unit ships.

**Metric: accepted student-useful work per unit of attention.**

Jeremy teaches. Chaz + Jeremy rebuild Week 1. Cleo runs the machinery.

Clipboard up. Keep shipping. 🍪
