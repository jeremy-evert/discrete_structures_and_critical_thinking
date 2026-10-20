# When Randomness Fools Us
**DSCT Week 10 · Instructor-only podcast series · October 20, 2026**

Three original, two-speaker episodes prepared from:
- Rolf Dobelli, *The Art of Thinking Clearly*, chapters 28 (base-rate neglect) and 29 (gambler's fallacy).
- Kenneth Rosen, *Discrete Mathematics and Its Applications*, 8th edition, chapter 7, especially §§7.1–7.4.
- The actual DSCT Week 10 plan at `week-10/README.md`, `week-10/instructor/tuesday-run-of-show.md`, `week-10/student/decision-gate.md`, and the historical `lessons/08-probability.md`.

## Episodes

| # | Title | Primary ideas | Estimated listening time |
|---|---|---|---|
| 01 | The Casino Has No Memory | Gambler's fallacy, independence, fair-coin streaks, replacement | 10–11 min |
| 02 | The Test That Tells the Truth but Fools You | Base rates, Bayes, screening-test four-cell tables | 10–11 min |
| 03 | Can We Trust the Numbers? | Expected value, simulation, modeling assumptions, classroom decision gate | 10–11 min |

This is original explanatory narration, **not** an audiobook reproduction of Dobelli or Rosen. It is for Jeremy's **private instructor listening library**, not student Canvas, public streaming, or student podcast publication.

## Contents

- `scripts/01_the_casino_has_no_memory.md`
- `scripts/02_the_test_that_fools_you.md`
- `scripts/03_can_we_trust_the_numbers.md`
- `manifest.json`: original source SHA-256 identities and episode metadata
- `production/render_on_maisie.sh`: staged, resumable local production and private publication with receipt checks
- `FLO_MISSION.md`: self-contained, owner-authorized Brandy → Maisie execution handoff

These source files are intentionally readable and diffable Git text; **no ZIP download or manual copying is necessary**. Do **not** commit generated MP3s, source staging copies, Audiobookshelf private runtime content, credentials or receipts that disclose private environment data to Git.

## Audio pipeline

Brandy's authorized Flo should pull the specific DSCT branch and read [FLO_MISSION.md](FLO_MISSION.md). Maisie renders using the existing Audio Foundry repository at [`tools/kokoro_dialogue.py`](https://github.com/jeremy-evert/audio_foundry/blob/main/tools/kokoro_dialogue.py) and the existing Kokoro 0.9.4 installation.

Renderer voice map: **DANA = af_sarah**, **MARCUS = af_heart**. The renderer is already responsible for normalization, MP3 encoding, decoded-audio validation, duration and source/output receipt creation. The small script here checks SHA-256 identities before render and on resume, and refuses publication collisions.

On Maisie, after Flo has established the existing checkout and interpreter paths and checked for competing jobs:

```bash
export AUDIO_FOUNDRY_CHECKOUT=/verified/existing/audio_foundry/checkout
export KOKORO_PYTHON=/verified/existing/kokoro-venv/bin/python
cd /path/to/DSCT/week-10/instructor/when-randomness-fools-us
bash production/render_on_maisie.sh render 01
```

After inspecting and spot-listening to the MP3, Flo independently verifies the live **private** Audiobookshelf mount maps to `/srv/audio-foundry/audiobooks`. Then:

```bash
export PRIVATE_AUDIOBOOKSHELF_MOUNT_VERIFIED=YES
bash production/render_on_maisie.sh publish 01
```

Scan/refresh the **private** Audiobookshelf library and confirm indexing. Repeat `render 02`, `publish 02`, then `render 03`, `publish 03`. Use `all` to verify or resume all items without replacing validated audio.

Runtime is intentionally outside Git: `/srv/audio-foundry/work/dsct-week10-20261020/`. Published location is intended to be `/srv/audio-foundry/audiobooks/Learning Foundry/DSCT Week 10 - When Randomness Fools Us/` **only after Flo verifies that folder is within the active private library mount**.

**No Android acceptance is implied by publishing.** Jeremy must actually see and test play/seek/resume on the phone, or Flo must obtain genuinely verifiable device-side evidence; do not claim it from library indexing alone.

## Mathematical cross-check

- For a fair independent coin: `P(next head | six tails) = 1/2`. Six consecutive tails have probability `1/64`.
- Hypothetical test (sensitivity 90%, specificity 90%, prevalence 1%, population 1,000): TP 9, FN 1, FP 99, TN 891; `P(condition | positive) = 9/108 ≈ 8.33%`.
- Change only prevalence to 10%: TP 90, FP 90; `P(condition | positive) = 50%`.
- Fair coin game paying $1 for heads and $0 for tails: expected gross 50 cents; at 60-cent entry cost, expected net **negative 10 cents**.

None of these examples is a claim about a real medical test, gambling venue, or observed population.

## Course-plan discrepancies to preserve, not silently change

The Tuesday run-of-show labels itself 75 minutes but its listed segments total 85. Also Week 10's README asks for a separate Show & Tell report while the grading model/Decision 029 retires separate graded Show & Tell paperwork. **For today's podcast production, do not alter course grading or existing run-of-show documents.** The current individual Decision Gate remains the ordinary Week 10 Odyssey evidence submission.

## Production state

Source scripts, manifest and production handoff: **prepared in Git**. Kokoro rendering, private Audiobookshelf publication, and actual phone playback: **not yet verified**.
