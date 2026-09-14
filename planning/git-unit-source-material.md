# Source material for a future DSCT Git unit

**Status: raw source material, not a lesson plan.** Jeremy is planning to add
Git to DSCT (2026-09-14). This is candidate material mined from two real,
already-taught lectures — not invented, not summarized by an LLM guessing at
what a good analogy would be. Direct quotes/paraphrases below are pulled from
real transcripts of Jeremy's own teaching. Use, cut, or ignore freely; nothing
here is committed to a week or a shape yet.

## Sources

- **CS1, 2026-09-11** (course 74029, Week 4's dedicated Git/GitHub lecture) —
  `/mnt/ironwolf-scratch/video_mechanics/protected_raw/teams/2026-09-11_cs1_62f62fa2/out/transcript.txt`
  on april (protected; not committed anywhere, quoted only, per the privacy
  boundary in `video_mechanics/README.md`/`AGENTS.md`). Already published to
  Canvas as lecture notes/digest — see
  `video_mechanics/reports/2026-09-12_cs1_week4_sept11_publish.md`.
- **CS2, 2026-09-14** (course 74031, today's Monday class — GitHub setup was
  a secondary thread inside a broader session, not the day's dedicated
  topic) — `.../protected_raw/teams/2026-09-14/incoming/out/transcript.txt`
  on april. Not yet published anywhere; transcribed today as part of
  checking whether today's recordings had anything usable.

## Reusable analogies/framing, already proven live in front of students

- **Commit = a labeled thumb drive.** "You're just pulling out your digital
  thumb drive and you're writing on the side of it what you're doing... git
  commit is this point in time... that commit message stays there for all
  of time." (CS2) Same idea in CS1: "that commit message that says, yay
  verily, this is what the universe looked like at this time. And you label
  that universe [with a name]. That's what your commit is saying — we have
  a saved checkpoint."
- **Push/pull direction, kept dead simple.** "Push away from the laptop,
  pull towards the laptop." (CS2) — one sentence, no diagram needed.
- **Clone happens once, then forget it.** "Clone my repo. That happens once.
  It happens at the beginning of the conversation. And that's it. After
  that, you can effectively erase that from your memory." (CS2) — directly
  answers the most common student confusion (re-cloning every session).
- **Git vs. GitHub, disentangled.** "Git and GitHub and repositories and
  commits and pushes are all separate things... That part that's on your
  computer is called Git. It's free open source software... GitHub — there's
  lots of hubs on the internet where you can go and find lots of interesting
  files." (CS1) Also CS2: "GitHub is a service... GitHub is owned by
  Microsoft... so they have a seat at the table." Both lectures independently
  reach for the same core distinction — worth keeping as the spine of a DSCT
  explanation.
- **Repository vs. folder.** "Repository and the folder are very similar
  ideas, but they don't mean the same thing... it keeps track of every
  comma." (CS1) — a real discrete-structures hook: a repo is a folder *plus*
  a tracked history graph, which is exactly the kind of "what does this
  representation add/hide" framing Week 5's relations material already used
  for Fibonacci and for domain/codomain/range.
- **Durability, played for a laugh but structurally correct.** "Wrapped in
  18 inches of steel reinforced concrete. Life as we know it will cease to
  exist before your files disappear... It will never cease to exist unless
  you manually go in and delete it." (CS1) — a concrete, memorable claim
  students can test/question rather than just accept.
- **Permission/consent framing for the SSH key step**, which is normally the
  single most confusing setup step: "You are manually giving written
  permission for GitHub to use that public key. This is your expressed
  written consent... you pull the private key from your computer, you give
  it to their server." (CS2) — turns a scary-looking cryptographic step into
  a plain-language consent transaction.
- **A cross-course vocabulary echo, likely unplanned but useful:** CS1's
  example commit message was literally "coding Odyssey Gate 4" — DSCT
  already uses "Odyssey Checkpoint" as its own recurring vocabulary (Weeks 7,
  11, 14). A DSCT git unit could lean into that overlap on purpose instead
  of treating it as a coincidence.

## What's thin or missing from both sources (a DSCT unit would need to add)

- Neither lecture connects git/commits to anything discrete-structures-native
  (relations, sets, sequences, graphs) — both are pure CS1/CS2-style
  procedural walkthroughs (how to click buttons / type commands), not a
  representation-and-reasoning framing. **A DSCT-native hook is not yet
  in this material** — e.g., a commit history *is* a sequence, a branch
  merge *is* a specific kind of graph operation, `git log --graph` *is* a
  directed graph a student could actually draw. That reframe is DSCT's own
  job to add, not something to extract from CS1/CS2.
- Neither lecture covers branching/merging in real depth (CS2's mention is a
  single aside: "I also want to do a branch, I want to do a merge" — no
  worked example). If a DSCT unit wants to use "what did a merge collapse
  or preserve?" as a representations question (very on-theme for Week 5's
  "what did this representation hide?" hook), that worked example still
  needs to be built from scratch.

## Not done here

No lesson plan, no Canvas page, no week placement. This file only answers
"what do we already have on tape that's worth reusing" — Jeremy decides
if/when/where a DSCT Git unit actually lands.
