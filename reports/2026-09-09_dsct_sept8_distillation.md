# DSCT Sept. 8 (Week 4) lecture distillation — Logic, Claims & Proof / King Octopus

Prepared 2026-09-09 by Flo from evidence Jeremy captured on Maise.

## Evidence and scope

- Teams transcript: `Fall 2026 Discrete Structures (COMSC-2043-1420).vtt`
  (~127 KB, 870 caption cues, ~78 min). Flattened readable copy kept off-Git
  in the working scratchpad as `dsct_sept8_class_flat.txt`.
- Companion `.docx` of the same meeting and two `.mp4` recordings
  (2026-09-08 class, plus a 2026-09-03 recording) — raw media, stays
  outside Git per the standing DSCT rule.
- `jeremy_DSCT_notes_Sept_8th.md` — a Copilot chat log about finishing the
  King Octopus LaTeX write-up (not classroom dialogue). Substance extracted
  below; the HTML-slurping the file complains about is a chat-renderer
  artifact, not a content problem.

Raw media/VTT and the Copilot log are **not** committed. Student first names
in the transcript are not carried into this file — participants are "a
student" / "students."

## Instructor digest

Week 4 is the first formal-topic week: turning ordinary claims into precise
logical language, telling a valid argument apart from a merely true
conclusion, and backing a conclusion with a proof or a counterexample.
Monday was Labor Day, so this was the week's first meeting.

Jeremy ran the whole 78 minutes on one worked artifact — **King Octopus and
His Servants** (Puzzle Prime): servants have 6, 7, or 8 legs; 7-legged
servants always lie, 6- and 8-legged always tell the truth; four servants
claim the group has 28 / 27 / 26 / 25 legs total; which told the truth?

The session moved through four deliberately different *modes of reasoning*
on the same problem:

1. **By hand, informal.** Students got the answer fast. Two lines of student
   reasoning were surfaced and named:
   - all four claims differ ⇒ at most one is true ⇒ ≥3 are lying ⇒ ≥3 have
     7 legs ⇒ 21 + (6 or 8) = 27 or 29; 29 isn't offered, so 27, i.e.
     legs (7,6,7,7), **Servant 2 truthful**.
   - a parity argument: even+even is even, 7 flips parity; 25 and 27 are
     odd and impossible, 26 and 28 are the only claimable truths, which
     combined with "exactly one true" also lands on 27.
2. **A precise mathematical model.** Translate "we together have N legs"
   into an exact statement (= N, not ≈ N, not ≥ N); make the group
   referenced by "we" explicit; state the lie/truth rule as a predicate.
3. **A written proof with logical bounds.** "At least one servant tells the
   truth" (rule out all-lying: that would make claim 1 true, contradiction)
   AND "at most one tells the truth" (the four claims are distinct) ⇒
   exactly one. Verification truth-table: F, T, F, F. No counterexample
   needed because the claim is true and a witness was found.
4. **Brute force / exhaustive search.** 3 choices per servant, 4 servants ⇒
   3^4 = 81 assignments; check all, exactly one satisfies every rule. Used
   to teach that code proves facts *about the model it was given*, nothing
   more. Doubled as a live exponent drill (3^0=1 as the multiplicative
   identity, 3^1..3^4).

Thursday (Sept 10) is Show & Tell: students bring **their own** logic puzzle
(river-crossing was suggested) and run the same five-heading process, not
just re-explain King Octopus. Cadence reminder given: even Thursdays =
Show & Tell, odd Thursdays = paired reasoning (with a human or an LLM).

## Teaching moves worth keeping

- **One artifact, four reasoning modes.** The puzzle is disposable; the
  point is that a claim can be reached informally, modeled, proved, and
  checked, and these are different skills.
- **"These little monsters are trying to kill you."** Running bit about
  LLMs all session — used every time the model was confidently wrong
  (identified a CPU-cooler photo as "a fan" then as "a CPU"; asserted the
  `.tex` source "is probably being ignored by git" when it plainly wasn't).
  The praise-on-success / "dopamine" framing was named explicitly as the
  manipulation to watch for.
- **Change one thing, then check.** "Is one added package enough to brick
  the code? Damn right it is" — deliberate habit of making a single change
  and rebuilding before the next.
- **Naming is reasoning.** Long riff on why `decision-gate-template.tex` is
  a bad name for a King-Octopus write-up, and why
  `king_octopus_bruteforce_version_2.py` is "evil, hateful, and useless" —
  version-numbered filenames are what source control is for; "understanding
  where your cheese is still matters."
- **The cake analogy for source vs. output.** git tracks the `.tex`
  (the recipe), not the `.pdf` (the cake you can always re-bake) — used to
  explain why `git status` only showed the PDF and why that's correct.
- **Divide the labor with the machine.** Explicit list: brains on the
  interesting questions (how many servants have an even leg count; a
  hypothetical King Octopus with 4 servants) and on hearing a classmate's
  framing; *not* on LaTeX syntax, compiler-message archaeology, or "knowing
  how to Google something."
- **AI-fluency check, live.** Prompt: "AI can make an invalid argument
  sound compelling — true, or does it not go far enough?" Landed on:
  *anyone* can; this is old (rhetoric, moral argument throughout history);
  the AI lens is new but the failure mode isn't. Cliché offered: "a clever
  person knows half of what they hear is wrong; a wise person can tell
  which half."
- **Here-strings / here-docs as a danger signal.** "When you see this, run
  like hell. Never blindly copy-paste this off the internet" — said
  immediately after doing exactly that, on purpose, and naming it.
- Tooling aside: abandoned Microsoft Whiteboard mid-search for **Lucid**
  whiteboard because it's already integrated in Canvas; retired Zoom in
  favor of Teams (old recordings now under Teams → Microsoft Education →
  Meetings).

## De-identified friction points

- Whiteboard tool churn ate the first ~6 minutes (Microsoft Whiteboard UI
  had changed; found the pen/stroke controls only after hunting).
- LLM confidently wrong twice on camera (the CPU-cooler photo; the
  "git is ignoring your .tex" claim) — both turned into teaching beats
  rather than derailments.
- A copy-pasted `version_2.py` created purely to demonstrate why that's the
  wrong move; the session ended mid-"Check Your Answer" section with "we
  are out of time," leaving that part to finish off-camera into the video.

## King Octopus artifact — status and cleanup debt

The write-up now lives in the **public** `computing_commons` repo
(`fun_with_LaTeX/`, pushed 2026-09-09 as `0fdf017`). It is a genuinely nice
self-contained evidence package: problem statement, explicit model,
human-readable proof, direct verification, exhaustive 81-case search,
printed Python source, and embedded `.py` / `.html` / `.txt` artifacts. All
three reasoning paths agree: legs (7,6,7,7), total 27, Servant 2 truthful.

Per the Copilot log, the PDF is **"working draft, nearly shipped"** — these
were flagged and are still open:

1. `mimetype=text/x-python` on the `\textattachfile` calls throws an
   `attachfile2` warning twice; the attachment works, the MIME line should
   just be removed.
2. The five-line brute-force summary is one long line — **overfull hbox,
   runs off the right edge of page 5**; needs real newlines inside the
   verbatim block.
3. The "Included Computational Artifacts" section appears **twice** —
   icon-only on ~page 6, readable filenames on pages 13–14. Keep the
   readable one, delete the earlier.
4. Stale generator name: footer/source still say
   `king_octopus_bruteforce_version_3.py`; should be
   `king_octopus_bruteforce_report_generator.py`.
5. Verify the embedded attachments open in a real desktop PDF reader before
   calling it done.

Also: the push carried intermediate cruft into a public repo —
`king_octopus_writeup.before_cleanup.tex`,
`king_octopus_writeup.before_source_repair.tex`,
`king_octopus_bruteforce_report_generator.before_cleanup.py`, and
`king_octopus_bruteforce_version_2.py` (the deliberately-bad-named file from
the lesson). Worth deciding whether the evolution is part of the lesson or
should be pruned before this is pointed at as the polished student example.

## Canvas follow-up (recommend, not yet done)

Jeremy told the class the King Octopus decision-gate template is in the
**public** `computing_commons` repo and to pull it from there. Earlier today
the DSCT Week 3/4 Canvas overview pages had raw repo chrome and an SSH
clone URL (`git@github.com:jeremy-evert/computing_commons.git`) pasted in;
those were stripped as unusable/leaky. The *intent* behind them is
legitimate — so DSCT Week 4 should carry a **clean** student path to the
template: either an `https://github.com/jeremy-evert/computing_commons`
link (public, allowed) pointed at `fun_with_LaTeX/`, or — cleaner — the
`.tex` template uploaded to Canvas Files and linked there. Flagging for
Jeremy's pick.

## Student-facing recap

`lecture-recaps/2026-09-08-week4-king-octopus-logic-claims-proof.md` — the
concise, de-identified "here's what we did and the method" version for
students who missed the room.
