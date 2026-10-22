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
