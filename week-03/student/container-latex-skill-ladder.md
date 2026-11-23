# Week 3 — running your reasoning in a container

> **Week 3 Question: How do you know an experiment is repeatable?**
>
> If the code stays the same, what else can change?
>
> This week you will run a tiny experiment, preserve evidence about its
> environment, compare observations, and decide exactly how much confidence
> that evidence deserves. Along the way, you will meet containers. You are
> not learning containers for their own sake. We use one because it lets us
> deliberately control part of an experiment while leaving other parts of
> the machine/environment outside that boundary.

## Start here: the shared Commons lesson

Before Step 1 below, work through the shared Computing Commons module —
`computing_commons/curriculum/containers-and-repeatable-environments.md`
(deck: `computing_commons/slides/week3_containers/week3_containers.pdf`). It
teaches the concept once: repeatability vs. reproducibility, image vs.
container, pinned digest identity, bind mounts, and what a container does
and does not control. This page is DSCT's application of that shared
concept, not a second copy of it.

Your disciplinary question for this week is:

> **What claim can the evidence justify?**

You will use the container skill below to reason about evidence,
uncertainty, what was controlled versus what was recorded, failure and
recovery, and the bounded claim your receipt can actually carry — not to
memorize container syntax.

## Worked example: claim, evidence, assumptions, check, confidence

Before you run anything yourself, read
[`lectures/ai_reasoning_latex_from_data/`](../../lectures/ai_reasoning_latex_from_data/README.md)
(compiled report: `final/build/main.pdf`, 3 pages). It is a full worked
example of this week's disciplinary question, built on a real local-model
GPU concurrency benchmark rather than a toy dataset.

The report tests one claim — "more concurrency raises throughput, and a
bigger GPU is faster" — against 24 measured observations (4
hardware/parallel-setting series x 6 batch sizes) and finds the honest
version is narrower than the tempting one: throughput only rises while
genuine parallel generation is available, then flattens near the
configured parallel limit. "Bigger GPU = faster" does not survive as a
universal claim.

Read it for the reasoning shape, not the GPU trivia:

- **Claim** — stated before the data, falsifiable;
- **Evidence** — a generated table and figure, not hand-picked numbers;
- **Assumptions** — named explicitly (comparable token counts, placement
  read from the recorded setting, not measured directly);
- **Check** — an overlap-factor calculation (aggregate rate ÷ per-request
  rate) that tests whether requests were actually running concurrently,
  not just tests whether the exit code was clean;
- **Confidence** — a bounded decision ("medium-high confidence" on the
  narrow claim, explicitly *not* on the universal one).

It also works two DSCT moves directly: an ordering relation (does
"larger batch size implies higher throughput" stay true once you condition
on the parallel limit — it does not, once the ceiling is reached) and a
product-rule count (4 series x 6 sizes = 24 observations). The steps under
`lectures/ai_reasoning_latex_from_data/steps/01`–`07` show the same report
built up one reasoning move at a time, if you want to see how each piece
gets added rather than reading only the finished version.

This pairs directly with the container lesson: a `RESULT: PASS` line or a
clean benchmark run is not itself proof of anything. In both cases, the
evidence has to be inspected and the claim has to be no bigger than what
the evidence actually supports.

---

Week 3 is where your Pair Reasoning artifacts (checkers, counterexample
generators, proof write-ups) start needing a real toolchain, starting with a
small typeset `.tex` claim/proof. You will run that toolchain inside a
container rather than installing it yourself.

## The deal

You are handed a working environment. You do not build it. Your job is not
to memorize container syntax; your job is to be able to:

1. get the known-good environment running,
2. understand enough of what is happening to inspect it,
3. notice when something is wrong,
4. recover from a bounded failure, and
5. verify the result with evidence rather than trusting a clean exit.

This is the same doctrine as the rest of the course: **Love AI more. Trust AI
less.** An AI assistant may help you read an error, explain a command, or
propose a fix. It has not fixed anything until you have run it and checked
the result yourself.

## What is supplied

- A **pinned image**: `week-03/container/IMAGE_CONTRACT.md` records exactly
  which image, which recipe, which digest. You are not asked to trust "the
  latest version of some image" — you are told precisely which one, and that
  identity does not silently change under you.
- A **wrapper script**: `week-03/container/run-latex.sh`. It runs your `.tex`
  source through the pinned image and produces a PDF.
- A **starter source**: `week-03/container/fixture/week3-claim.tex`.

## Step 1 — Run

From the repository root:

```bash
cp week-03/container/fixture/week3-claim.tex /path/to/your/work/
cd /path/to/your/work
/path/to/repo/week-03/container/run-latex.sh week3-claim.tex
```

A successful run prints `RESULT: PASS` and the path to the generated PDF.

## Step 2 — Inspect

Before you trust the result, look at what the wrapper printed. Every run
shows you, in plain text:

- `IMAGE:` — which image ran your source, and (per `IMAGE_CONTRACT.md`) that
  it is a pinned image, not a floating `:latest` tag;
- `HOST_SOURCE_DIR:` — the folder on your machine that was made visible
  inside the container;
- `CONTAINER_WORK_DIR:` — where that folder appears inside the container
  (`/work`);
- `SOURCE:` / `EXPECTED_PDF:` — which file went in, and where the result
  should land;
- `RESULT:` — pass or fail, in plain text, not just an exit code.

You do not need to memorize the underlying `podman run` invocation. You do
need to be able to point at each of the facts above and say what it means.

## Step 3 — Explain

In your own words (this is what a Tuesday reasoning-check or Show & Tell may
ask for), you should be able to say something like: *"My `.tex` file lives
on my machine. The wrapper hands a copy of my work folder to a container
that already has TeX Live and `latexmk` installed. The container compiles my
file and writes the PDF back into that same folder, so I see it without
having to reach into the container."* You do not need to explain rootless
namespaces, SELinux relabeling, or `latexmk`'s dependency-tracking rules —
those are exactly the kind of detail the wrapper is allowed to hide.

## Step 4 — Perturb, Diagnose, Recover, Verify

You will encounter (or be handed) at least one bounded failure. The general
loop is always the same:

1. **Read the `REASON:` line.** The wrapper always tells you what it thinks
   went wrong before you go looking.
2. **Decide what kind of problem it is.** Is it a *path/mount* problem (the
   wrapper can't find your file, or it's not where you expected), a
   *container/runtime* problem (the image reference is wrong, or the runtime
   itself failed before compilation even started), or a *LaTeX content*
   problem (the toolchain ran but your source has an error)? The wrapper's
   message is written to help you tell these apart — a runtime failure says
   so explicitly and points you at the `IMAGE:`/`RUNTIME:` lines instead of a
   log file.
3. **Propose a fix.** You may ask an AI assistant to help interpret the
   error or suggest a repair. That suggestion is a **proposal**, not a
   result.
4. **Execute and rerun.** Apply the fix yourself and rerun the wrapper.
5. **Verify with evidence**, not a clean exit code alone. At minimum: open
   or extract text from the resulting PDF and confirm it actually reflects
   your source, or (for a repaired path/runtime issue) confirm the PDF now
   exists where you expected it. A `RESULT: PASS` line is a necessary
   condition, not sufficient proof by itself.

### Failure types you should be able to recognize

| Symptom | Likely category | What to check |
| --- | --- | --- |
| `source not found: ...` | wrong working directory / wrong path | Are you in the folder you think you're in? Does the file exist there under that exact name? |
| `image not known` / runtime error before any `pdflatex` output | container/runtime invocation problem | Check the `IMAGE:`/`RUNTIME:` lines — did you override `DSCT_WEEK3_IMAGE` to something that doesn't exist? |
| `Undefined control sequence` / `Fatal error occurred, no output PDF file produced!` | LaTeX source error | This is your `.tex` file, not the container. Read the line number the log gives you. |
| `RESULT: PASS` but the PDF doesn't show your edit | false success | Did you edit the file the wrapper actually compiled? Check `SOURCE:`/`HOST_SOURCE_DIR:` again. |

## Step 5 — Extend later

Later in the course (not required for your first Week 3 success), you may
inspect or modify the image recipe itself
(`week-03/container/Containerfile`) or build your own image. That is a
deeper skill layered on top of this one — you do not need it to get your
first working, verified artifact.

## Minimum vocabulary you should leave with

- **Image vs. running container** — the image is the frozen template; a
  container is a disposable running instance of it. Deleting a container
  after a run (which the wrapper does automatically) does not delete the
  image.
- **Pinned identity vs. floating tag** — a digest always refers to exactly
  one image; a tag like `:latest` can point at different images over time.
- **Host path vs. container path** — your file lives at some path on your
  machine; the same file appears at a different path (`/work/...`) inside
  the container. Confusing the two is the single most common recovery-only
  mistake.
- **Source vs. generated output** — you edit the `.tex`; the PDF, `.log`,
  `.aux`, and `.fls` files are regenerated every run and are not something
  you hand-edit.
- **Current working directory** — relative paths are evaluated from wherever
  you ran the command, not from "the repository" in the abstract.
- **Bind-mounted work vs. disposable container state** — anything written to
  your mounted work folder survives after the container exits; anything
  written only inside the container's own filesystem does not.
- **Success vs. error** — a nonzero exit or a `RESULT: FAIL` line means
  something specific went wrong; read it before rerunning blindly.
- **Rerun after repair** — the whole point of the loop above is that you can
  fix the one thing that was wrong and rerun without starting over.
