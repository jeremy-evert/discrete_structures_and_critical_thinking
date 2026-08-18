# Report 319 — DSCT Week 1/2 production launch (course 74035)

## Why

Jeremy teaches DSCT in-person shortly after this session; Week 1 needed to
be live on real production SWOSU Canvas, not just validated on the internal
Savnac sandbox (course 4, self-hosted at `192.168.122.172:3000` — not
student-visible).

## What was built

`course_foundry/production_deploy.py` (previously CS1-only "by design") was
extended in Prompt 107 to also support DSCT, targeting real production
course **74035**, reusing the existing `savnac_deploy._build_dsct` builder.
This required a follow-on fix: `dsct_savnac_desired_course`'s own guard
(`course_foundry/dsct_desired_course.py`) hard-refused any `course_id` other
than the Savnac sandbox id (4) — a deliberate safety rail, but one that
didn't yet know about the real production target. Widened it to an explicit
allowlist (`_DSCT_ALLOWED_COURSE_IDS = {4, 74035}`) rather than removing the
guard, so it still refuses anything else. 17/17 DSCT-related tests green
after, 27/27 across `test_production_deploy.py` + `test_savnac_deploy.py`.

## What happened live

1. Dry-run against 74035: `29 create / 0 update / 0 delete` (first-ever
   push to this course id for DSCT-owned content).
2. Live push: succeeded for Week 1 in full (8/8 items) and Week 2 partially
   (7/19 items), then failed with a Canvas API `403` whose body is a raw
   CloudFront error page ("Request blocked... too much traffic"), not
   Canvas's own JSON rate-limit response — an edge/WAF-level block, not an
   application-level one.
3. Confirmed the same known defect already found on CS1 today: Canvas's
   module-create endpoint ignores `module[published]=true` — both new DSCT
   modules were live but unpublished. Fixed directly via a plain
   `PUT .../modules/:id {module[published]: true}` for each (this specific
   write path was never blocked — see below), confirmed `published=true` on
   read-back for both modules.
4. Retried the remaining Week 2 page creates three times with increasing
   backoff (90s, then 240s); all three failed identically. Diagnosed rather
   than blindly retried further:
   - A trivial throwaway probe page (`create_page` with a two-word body)
     succeeded and was cleaned up immediately — so this is **not** a
     blanket write block or a simple rate limit on the endpoint.
   - Creating the actual next missing page (`Aider as the Coding Client`,
     2141 chars, discusses Aider/Ollama/PowerShell/loopback API content)
     failed with the identical CloudFront block.
   - Conclusion: something about the *content* of the remaining Week 2
     pages (all covering the local AI lab setup — Aider, Ollama, PowerShell,
     `127.0.0.1` API calls) is tripping a CloudFront WAF rule on
     `swosu.instructure.com`, not a source/compiler defect and not
     (apparently) a pure rate limit, since a trivial page went through
     cleanly at the same moment.

## Current live state (confirmed by direct read-back)

- `DSCT Week 1 — Reasoning Odyssey`: **published, 8/8 items** — complete.
- `DSCT Week 2 — Build the Lab, Then Make Results Reproducible`:
  **published, 7/19 items** — partial. Missing: `Aider as the Coding
  Client`, `Localhost, APIs, and Local vs. Cloud`, `Run the Readiness
  Check`, `First Local AI Interaction`, `Troubleshoot with Evidence`,
  `DSCT Extension: Analyze Claims, Evidence, and Limits`, `Assignment:
  Local AI Lab Readiness Check`, `Tuesday activity: A claim about a
  prepared AI lab`, `Thursday activity: Container boundaries and
  repeatability`, `Week 2 Evidence Portfolio rubric`, `Week 2 Evidence
  Portfolio — 40 points`, `Windows classroom workflow reference`.

## Why this isn't blocking today

DSCT meets Tuesday/Thursday; today's class (Tuesday) is Week 1 content,
which is fully live and published. Week 2 doesn't start until next
Tuesday/Thursday. This is a real, disclosed yellow — not silently dropped —
but not a today-class blocker.

## Next unit (not done here)

Re-attempt the 12 missing Week 2 items once the WAF condition is
understood or clears (try again after a longer cooldown, or investigate
which specific content pattern triggers it — possibly the loopback
`127.0.0.1` API-call examples or specific PowerShell syntax; bisecting one
page at a time would identify it precisely, at the cost of more live
requests against a service that's already shown edge-level pushback
today). Zero assignment-group weighting remains an intentionally accepted
gap for this partial slice (`partial_weight_note` in `savnac_deploy.py`),
not a new defect.

## Evidence

This session's transcript; live read-backs shown above; `course_foundry`
`f61f176`/`a49b658` (Prompts 106/107).
