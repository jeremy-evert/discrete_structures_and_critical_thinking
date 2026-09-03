# Discrete Structures — Sept. 3 recap: GPU data reasoning + container setup

## Big idea

A clean exit code is not proof of anything. Whether it's a benchmark table or a script that just ran, the evidence has to be inspected before you trust the claim it seems to support.

## Remember

1. "Cold start" vs. "warm start" isn't about temperature — it's about whether the GPU already has a job queued up when the next one arrives. A warmed-up pipeline finishes work faster than the same hardware starting cold.
2. A small, non-random sample of machines (six of them, sitting in one building) can't support a claim about GPU families in general — that's sampling bias, the same failure mode as the WWII "armor the bullet holes" story: you only get to reason about the evidence you actually have, not the evidence you wish you had.
3. An observation ("the newest GPU wasn't the fastest") is not yet a claim. Turn it into a *modest* claim — one no bigger than what the data actually supports — before you trust it.
4. Ask: **what would it take to convince a skeptic?** That question is the throughline of this course.
5. Podman/WSL2 setup verification hit a real wall live in class — Ubuntu wouldn't finish launching on the instructor's own machine. That's the correct response to an administrative/platform wall: stop, file a help desk ticket, don't burn the class period fighting a Windows service you don't have permission to restart.
6. LaTeX builds in two passes: the first pass writes supporting files (like a table of contents), and it doesn't show up correctly until the *second* pass reads that file back in. One pass with no visible change is not a failure — it's how the tool works.
7. `.gitignore` should exclude build byproducts (`main.pdf` and friends) — track the source you wrote, not the file the tool regenerates every time.

## What happened when the AI assistant got it wrong, live

Live in class, the assistant was asked to find a folder — and searched from *inside* that same folder, so it reported the folder didn't exist. That's the same mistake as using your phone as a flashlight to go look for your phone. The fix wasn't magic: recognize the mismatch, correct the assistant, move on. That's the actual skill — not typing the first prompt, but noticing when the answer doesn't match reality and knowing what to check.

## Recovery path

If your own Podman/WSL2 setup is still stuck: this is a known, shared problem this week, not something you broke. Save your exact error text, note where it hangs, and bring that evidence to next class — "it didn't work" is not evidence; "it hung after typing `wsl --distribution Ubuntu-22.04` with no prompt for 90 seconds" is.

## Exact next action

Look at the GPU Showdown table again on your own. Write down one observation and turn it into a modest, falsifiable claim — one sentence, no bigger than what the six-machine sample can actually support. Next class moves into discrete mathematics and critical thinking content directly.
