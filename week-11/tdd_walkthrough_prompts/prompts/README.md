# Classroom prompts

Run order is `00` to `14`; one file per step. Open the file, paste the fenced `prompt-a` block into Claude, run what it asks, then (if there is one) paste `prompt-b`. Each file carries: why, what you should see, a Predict-first question with its expected answer, a common mistake, and the recovery move. The step table with principle tags is `../STEPS.md`.

Loop for every step: **Predict** (ask the room, 30 s) → **Run** (paste, run pytest) → **Explain** (why red/green).

Recovery when Claude's live output drifts: from your live folder run `LADDER_REPO=<DSCT clone> tools/recover.sh NN` (restores `merger/` and `tests/` to `tdd-step-NN`), or for steps 01–03 copy the file from `reference/demos/`.
