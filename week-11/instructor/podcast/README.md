# Relations, Order, and Structure

One original two-voice instructor listening script for DSCT Week 11, beginning October 26, 2026. Dana and Maria are the speakers; the package uses the established renderer voices `af_sarah` and `af_heart`. This is instructor preparation material, not a student-facing assignment or publication.

## Sources and credit

The narration follows the DSCT Week 11 README, Tuesday and Thursday instructor run-of-show documents, Tuesday activity, Odyssey Checkpoint 2, and the Fall 2026 semester spine. It draws on the course's historical `Relations` lesson for topic continuity. The course materials are credited as the source of the week's goals and examples. The narration is original explanatory wording and does not reproduce passages from course texts.

## Contents

- `scripts/01_relations_order_and_structure.md` — source script
- `manifest.json` — source SHA-256, speaker map, word count, and estimated duration
- `production/render_on_maisie.sh` — single-episode render and private library handoff for Flo or Anna

Keep the script and manifest in Git. Do not add rendered audio, staging copies, runtime receipts, or Audiobookshelf content to Git.

## How Flo or Anna renders it

On Maisie, use the existing Audio Foundry checkout and Kokoro environment. Verify their paths, then from this directory run:

```bash
export AUDIO_FOUNDRY_CHECKOUT=/verified/existing/audio_foundry/checkout
export KOKORO_PYTHON=/verified/existing/kokoro-venv/bin/python
bash production/render_on_maisie.sh render 01
```

Inspect and spot-listen to the rendered file. Before using `publish 01`, independently verify that the live Audiobookshelf mount is the private instructor library, then set `PRIVATE_AUDIOBOOKSHELF_MOUNT_VERIFIED=YES`. The script refuses publication without that explicit check and refuses to overwrite a different existing file. Library refresh and device playback checks remain separate. Generated files and receipts stay under the configured Audio Foundry runtime, outside this repository.

## Claims and source checks

- The divisibility classification is for the explicit domain containing one, two, three, and six, with ordinary positive-integer divisibility. It is reflexive, antisymmetric, and transitive, but not symmetric; the two and six pair is the counterexample.
- The script describes matrices as row-first and column-second representations and digraph arrows as ordered pairs. Check that those conventions match the notation used in class.
- The checkpoint description follows `week-11/student/odyssey-checkpoint-2.md`, including that it replaces the ordinary Decision Gate and is the only Odyssey submission this week.
- The Tuesday run-of-show heading says seventy-five minutes, while its listed segments run through minute eighty-five. The intended meeting length is unresolved in the source and should be checked before using the pacing table.

## Production state

Source script, manifest, and render handoff are prepared in Git. Rendering, private Audiobookshelf publication, and device playback are not verified.
