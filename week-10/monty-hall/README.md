# Monty Hall: three doors, one good question

An offline classroom activity for Week 10, Probability, Uncertainty & Evidence.
Open [`monty_hall.html`](monty_hall.html) in a browser; it needs no server,
account, internet connection, or extra software. The page includes a playable
round, the nine first-pick/car-location cases, a seeded Monte Carlo simulation,
the 3–100-door extension, and an optional random-host comparison.

The matching standard-library Python simulation is
[`monty_hall_sim.py`](monty_hall_sim.py):

```sh
python3 monty_hall_sim.py --games 10000 --seed 20261022
python3 monty_hall_sim.py --games 100000 --seed 42 --doors 100
python3 monty_hall_sim.py --games 120000 --seed 99 --host-random
```

The tests use only Python's standard library:

```sh
python3 -m unittest tests.test_monty_hall_sim
```

## Five-minute class script

1. **Predict first (about a minute).** Before opening the page, ask: “You pick
   one of three doors. The host knows where the car is and opens a goat door.
   Stay or switch?” Have students commit to a prediction and say what they
   think the host's reveal tells them.
2. **Play a few rounds (about a minute).** Open the page, pick a door, and ask
   students to advise “stay” or “switch” before revealing the car. Try to
   notice individual wins separately from the strategy scores.
3. **Pause at the split (about a minute).** Show the 1/3 first-pick chance and
   2/3 chance that the first pick was a goat. Ask where the original 2/3 goes
   after a knowing host removes a goat, then use the nine-case table to check.
4. **Check by simulation (about a minute).** Run 10 games first so the class
   sees a noisy result. Then run 10,000 with the displayed seed. Compare both
   strategies side by side and point out that a simulation checks the model's
   prediction; it does not replace the case count or guarantee that a small
   run lands close.
5. **Change the host rule (about a minute).** Turn on “Host opens a door at
   random.” Ask what happens when the car is exposed. Those rounds are marked
   spoiled and excluded. Among the remaining rounds, staying and switching
   each win about half the time. The follow-up is: *what did the host's
   knowledge change about the games we get to observe?*

## Why the random-host answer changes

With `n` doors, a random retained door keeps a round valid if it is the first
pick or the car. Each event has probability `1/n`, so `2/n` of all rounds are
counted and `1 - 2/n` are spoiled. The car is behind the first pick in `1/n` of
all rounds, and behind the other retained door in another `1/n`; conditional
on a round being valid, those two outcomes are equally likely. Thus each
strategy wins half of the counted rounds for every `n >= 3`. A knowing host
never spoils a round, and switching wins whenever the first pick was wrong,
with probability `(n - 1)/n`.

The puzzle is named for the host of *Let's Make a Deal*. Marilyn vos Savant's
1990 *Parade* column made it widely known.

## Evidence

Browser, Python/JavaScript agreement, and measurement details are recorded in
[`VERIFICATION.md`](VERIFICATION.md). Phone and projector captures are in
[`screenshots/`](screenshots/).

## Math deck and additional simulations

The 16-slide derivation deck is [`monty_hall_math.pdf`](monty_hall_math.pdf),
with editable LaTeX source in [`monty_hall_math.tex`](monty_hall_math.tex).

[`monte_carlo_playground.html`](monte_carlo_playground.html) is a single-file,
offline page with Buffon's hot dogs, darts for π, birthdays, and coupon
collection. Choose a tab, seed, and run count. The related standard-library
models are in [`monte_carlo_playground_sim.py`](monte_carlo_playground_sim.py).
The browser exposes deterministic functions as `window.MonteCarlo.buffon`,
`.darts`, `.birthday`, and `.coupon`.

The original simulation also accepts `--variant crawl` for the three-door
leftmost eligible reveal rule and `--open K` with `--doors N` for a knowing host
who opens K goats. For example:

```sh
python3 week-10/monty-hall/monty_hall_sim.py --games 100000 --seed 17 --variant crawl
python3 week-10/monty-hall/monty_hall_sim.py --games 100000 --seed 17 --doors 5 --open 2
python3 -m unittest tests.test_monty_hall_sim tests.test_monte_carlo_playground_sim
```

Seeded results, formula checks, and browser verification status are in
[`VERIFICATION.md`](VERIFICATION.md).

## Files added or maintained in this package

- `monty_hall.html` — interactive three-door activity.
- `monty_hall_sim.py` — standard-library Monty Hall and variant simulator.
- `monte_carlo_playground.html` — offline five-tab simulation playground (Buffon, darts, birthdays, coupons, secretary).
- `monte_carlo_playground_sim.py` — matching deterministic Python models.
- `monty_hall_math.tex` and `monty_hall_math.pdf` — editable 18-frame Madrid deck and compiled slides.
- `VERIFICATION.md` — test commands, reproducible measurements, and verification limits.
- `../../tests/test_monty_hall_sim.py` and `../../tests/test_monte_carlo_playground_sim.py` — standard-library tests.
- `screenshots/phone.png` and `screenshots/projector.png` — earlier captures of the Monty Hall activity; playground browser captures are pending Anna's browser check.

Run all project tests with `python3 -m unittest tests.test_monty_hall_sim tests.test_monte_carlo_playground_sim`.
