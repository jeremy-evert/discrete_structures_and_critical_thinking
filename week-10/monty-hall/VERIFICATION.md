# Verification record

Run on the `anna/dsct-monty-hall-20261021` branch from base `e60e221`.

## Implementation checks

- Python suite: `python3 -m unittest tests.test_monty_hall_sim` — **7 tests
  passed**.
- Headless Chromium loaded the offline HTML. Page JavaScript console errors:
  **0**. Captured requests: the local `file://.../monty_hall.html` document
  only; no external requests. A source scan for external URL schemes and
  external asset `src`/`href` references found none.
- The responsive check measured `scrollWidth` and `innerWidth` after load and
  after control interactions:

  | Viewport | `innerWidth` | `scrollWidth` | Horizontal overflow |
  | --- | ---: | ---: | --- |
  | Phone, 390 px | 390 | 390 | None |
  | Projector, 1920 px | 1920 | 1905 | None |

- Screenshots: [`phone.png`](screenshots/phone.png) at 390×844 and
  [`projector.png`](screenshots/projector.png) at 1920×1080.

## Seeded measurements

The HTML `window.MontyHall.run` and Python CLI use the same mulberry32 stream
and consume three random values per game in the same order.

| Mode | Games | Seed | Counted | Spoiled | Stay wins / rate | Switch wins / rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| Knowing host, 3 doors | 10,000 | 20261022 | 10,000 | 0 | 3,412 / 0.341200 | 6,588 / 0.658800 |
| Knowing host, 100 doors | 100,000 | 42 | 100,000 | 0 | 1,011 / 0.010110 | 98,989 / 0.989890 |
| Random host, 3 doors | 120,000 | 99 | 79,960 | 40,040 | 40,099 / 0.501488 | 39,861 / 0.498512 |

Python and JavaScript agree exactly for the shared 10,000-game run: **3,412
stay wins, 6,588 switch wins, 0 spoiled**. The 100-door switch result is
0.989890 against the closed form `99/100 = 0.99`. With the random 3-door host,
the spoiled fraction is `40,040/120,000 = 0.333667`; among valid games the two
measured rates are about 1/2 each, as predicted.

## Package 2: math deck, variants, and playground (2026-10-21)

### Implementation checks

- Deck: `latexmk -pdf -interaction=nonstopmode week-10/monty-hall/monty_hall_math.tex` — **16 pages compiled**. `grep -E 'Overfull \\hbox|^!' monty_hall_math.log` returned no matches (zero overfull boxes and zero TeX error markers). Auxiliary files were removed; source and PDF are the deliverables.
- Python: `python3 -m unittest tests.test_monty_hall_sim tests.test_monte_carlo_playground_sim` — **14 tests passed**.
- Added `--variant crawl` for three doors. Seed 1234, 90,000 games: switching won 60,104 / 90,000 = **0.667822**, against 2/3. In the defined 5-door, open-2 mode, a randomly chosen one of the two remaining doors wins with probability `(5−1)/(5(5−1−2)) = 0.4`; seed 567, 100,000 games measured **0.403490**. Existing three-draw modes remain bit-identical; extra-door mode uses draw three to choose the opened goat subset and a fourth draw to choose the remaining target.
- Three Prisoners seeded check: 300,000 trials, seed 12; conditioned on the guard naming B, A pardon rate **0.333** and C pardon rate **0.667**, as predicted. The guard chooses uniformly between B and C when A is pardoned.
- Playground seeded Python measurements, 10,000 trials, seed 20261022: Buffon crossings **6,380/10,000**, expected **6,366.20**, π estimate **3.13480** (π = 3.14159); darts hits **7,781/10,000**, expected **7,853.98**, π estimate **3.11240**; birthday n=23 shared groups **0.51530**, exact **0.50730**; coupon n=10 mean **29.205** vs `nHₙ = 29.290`; n=50 mean **224.164** vs `nHₙ = 224.960`. All five reported measurements used seed 20261022.
- JavaScript and Python were executed with the same seed and 10,000 trials under Node.js. The measurements matched exactly: Buffon 6,380 hits / π̂ 3.134796; darts 7,781 hits / π̂ 3.112400; birthdays 5,153 groups / 0.515300; coupons n=10 mean 29.204700. Birthday and coupon exact values also match. Buffon uses `sin` and can differ at floating-point boundaries. This is a deterministic function check, not browser verification.
- Browser requirement is **not verified**: `/snap/bin/chromium --headless --no-sandbox --disable-gpu --remote-debugging-port=9223 --remote-allow-origins='*' --user-data-dir=/tmp/chromium-mh-check about:blank` exited with code 46 before launch: `cannot create transient scope: DBus error ... refusing`. Therefore console errors, 390 px / 1920 px overflow, and playground screenshots were not captured in Chromium. A Firefox screenshot fallback also failed before launch because its Snap wrapper could not create `/run/user/1001/snap.firefox` on the read-only filesystem. No screenshot is claimed as browser evidence.
- Omitted: Secretary problem (explicitly bonus); not included to keep the deck and playground focused. No other requested simulation was omitted.

### Revision follow-up (2026-10-21)

- Updated the deck to 18 frames (including title), added an explicit Bayes-denominator path diagram, a seeded measured-vs-model bar chart, and a secretary-problem derivation. Speaker notes are present throughout. Recompiled with `latexmk -pdf -interaction=nonstopmode monty_hall_math.tex`: **18 pages**, zero TeX error markers, and `grep -E 'Overfull \\hbox|^!' monty_hall_math.log` returned no matches.
- Added the secretary problem to both playgrounds: n=100, skip `floor(100/e)=36`; its finite-n success probability is `sum(36/(100(j−1)))` for j=37…100 = **0.371015**, tending to `1/e = 0.367879`. Seed 20261022, 10,000 runs: Python and JavaScript both report **3,763/10,000 = 0.376300**.
- The playground now auto-runs its default seed on page load and whenever a tab is selected. Hot dogs render as bun-colored rounded capsules with sausage centers; crossings are gold. Each simulation displays its measured result alongside its model value, and derivation text uses numbered steps.
- `python3 -m unittest tests.test_monty_hall_sim tests.test_monte_carlo_playground_sim` — **15 tests passed**.
- Node v22.23.3 deterministic function check (10,000 runs, seed 20261022): Buffon **6,380** crossings; darts **7,781** hits; birthdays **5,153** groups at n=23; coupon collector mean **29.204700** draws at n=10; secretary **3,763** wins at n=100. Python agrees exactly on the shared mulberry32 stream, including secretary. Buffon retains the documented small possibility of a floating-point trigonometry boundary difference.
- Browser checks remain assigned to Anna. This run did not verify Chromium console output, responsive widths, or new playground screenshots. Existing phone/projector captures are for `monty_hall.html` only.

### Final polish (2026-10-21)

- Reworked the Monty Fall, Monty Crawl, Three Prisoners, open-$k$, Buffon,
  darts/birthdays, and coupon-collector derivations into concise claims followed
  by staged equations. The Monty Fall frame includes the three car-location
  branches and random-host outcomes; Three Prisoners has a conditional-path
  table. The deck has **18 logical frames**. Overlay reveals produce **44 PDF
  pages**.
- Buffon's canvas now draws at most 120 smaller hot dogs, with deterministic
  positions spread over the full width. Gold marks crossings. The displayed
  measured and expected counts still use all $N$ simulated trials.
- Recompiled with `latexmk -pdf -interaction=nonstopmode monty_hall_math.tex`:
  44 pages, zero TeX error markers, and `grep -E 'Overfull \\hbox|^!'
  monty_hall_math.log` returned no matches. Updated source and PDF are present.
- `python3 -m unittest tests.test_monty_hall_sim
  tests.test_monte_carlo_playground_sim` — **15 tests passed**. Node.js 22
  function checks at 10,000 runs and seed 20261022 agreed with Python:
  Buffon 6,380; darts 7,781; birthdays 5,153; coupon mean 29.204700; secretary
  3,763. Browser measurements remain Anna's reported checks: `monty_hall.html`
  had 0 console errors and widths 390/390 and 1905/1920; the playground had 0
  errors after her canvas fix and widths 390/390 and 1905/1920. This run did not
  independently launch a browser.
