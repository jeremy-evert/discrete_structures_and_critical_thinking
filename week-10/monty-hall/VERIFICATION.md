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
