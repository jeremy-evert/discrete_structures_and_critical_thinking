"""
monty_hall_monte_carlo.py
Monte Carlo simulation of the Monty Hall 3-door problem.

Each contestant:
  1. picks a door at random
  2. watches the host (who KNOWS where the car is) open a goat door
  3. flips a coin to decide: STAY or SWITCH
We tally four buckets: stay+win, stay+lose, switch+win, switch+lose.

Run:  python monty_hall_monte_carlo.py          (2,000 contestants, random seed)
      python monty_hall_monte_carlo.py 5000 42  (5,000 contestants, seed 42)
"""

import math
import random
import sys

import matplotlib.pyplot as plt

DOORS = [1, 2, 3]
CONFIDENCE_Z = 1.96   # 95% confidence
POWER_Z = 0.84        # 80% chance of actually detecting a real difference


def play_one_game(rng):
    """Return (strategy, won) for one contestant."""
    car_door = rng.choice(DOORS)
    first_pick = rng.choice(DOORS)

    goat_doors_host_may_open = [d for d in DOORS if d != first_pick and d != car_door]
    host_opens = rng.choice(goat_doors_host_may_open)

    strategy = rng.choice(["stay", "switch"])
    if strategy == "stay":
        final_pick = first_pick
    else:
        final_pick = next(d for d in DOORS if d != first_pick and d != host_opens)

    return strategy, final_pick == car_door


def run_show(total_contestants, rng):
    """Play the show and record running tallies after every contestant."""
    tally = {"stay_win": 0, "stay_lose": 0, "switch_win": 0, "switch_lose": 0}
    history = {key: [] for key in tally}
    for _ in range(total_contestants):
        strategy, won = play_one_game(rng)
        tally[f"{strategy}_{'win' if won else 'lose'}"] += 1
        for key in tally:
            history[key].append(tally[key])
    return tally, history


def win_rate(wins, losses):
    played = wins + losses
    return wins / played if played else float("nan")


def margin_of_error(p, n):
    return CONFIDENCE_Z * math.sqrt(p * (1 - p) / n) if n else float("nan")


def print_contestant_by_contestant(rng, count=10):
    print("First few contestants, one at a time")
    print(f"{'#':>3} {'car':>4} {'pick':>5} {'host opens':>11} {'strategy':>9} {'result':>7}")
    for i in range(1, count + 1):
        car_door = rng.choice(DOORS)
        first_pick = rng.choice(DOORS)
        host_opens = rng.choice([d for d in DOORS if d not in (first_pick, car_door)])
        strategy = rng.choice(["stay", "switch"])
        final_pick = first_pick if strategy == "stay" else \
            next(d for d in DOORS if d not in (first_pick, host_opens))
        print(f"{i:>3} {car_door:>4} {first_pick:>5} {host_opens:>11} {strategy:>9} "
              f"{'WIN' if final_pick == car_door else 'lose':>7}")
    print()


def print_how_many_do_we_need():
    print("How many contestants do we need?")
    p_switch, p_stay = 2 / 3, 1 / 3
    gap = p_switch - p_stay
    spread_of_gap = math.sqrt(p_switch * (1 - p_switch) + p_stay * (1 - p_stay))

    n_detect = (CONFIDENCE_Z * spread_of_gap / gap) ** 2
    n_reliable = ((CONFIDENCE_Z + POWER_Z) * spread_of_gap / gap) ** 2
    print(f"  Q1: Is switching better at all? (gap = 2/3 - 1/3 = {gap:.3f})")
    print(f"      95% confidence, just barely:        ~{math.ceil(n_detect)} per strategy "
          f"(~{2 * math.ceil(n_detect)} contestants)")
    print(f"      95% confidence, 80% of the time:    ~{math.ceil(n_reliable)} per strategy "
          f"(~{2 * math.ceil(n_reliable)} contestants)")

    print("  Q2: How precisely do we know the switch win rate is 2/3?")
    print(f"      {'+/- margin':>12} {'per strategy':>14} {'total contestants':>19}")
    for margin in [0.10, 0.05, 0.02, 0.01, 0.001]:
        n = math.ceil((CONFIDENCE_Z / margin) ** 2 * p_switch * (1 - p_switch))
        print(f"      {margin:>12} {n:>14,} {2 * n:>19,}")
    print()


def check_by_repeating_shows(rng, show_sizes, shows_per_size=500):
    """Run many whole shows of each size. How often does switch beat stay?"""
    switch_beats_stay = []
    for size in show_sizes:
        wins = 0
        for _ in range(shows_per_size):
            tally, _ = run_show(size, rng)
            if win_rate(tally["switch_win"], tally["switch_lose"]) > \
               win_rate(tally["stay_win"], tally["stay_lose"]):
                wins += 1
        switch_beats_stay.append(wins / shows_per_size)
    return switch_beats_stay


def main():
    total_contestants = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
    seed = int(sys.argv[2]) if len(sys.argv) > 2 else None
    rng = random.Random(seed)

    print_contestant_by_contestant(rng)
    print_how_many_do_we_need()

    tally, history = run_show(total_contestants, rng)
    stayers = tally["stay_win"] + tally["stay_lose"]
    switchers = tally["switch_win"] + tally["switch_lose"]
    stay_rate = win_rate(tally["stay_win"], tally["stay_lose"])
    switch_rate = win_rate(tally["switch_win"], tally["switch_lose"])

    print(f"Full show: {total_contestants:,} contestants (seed {seed})")
    print(f"  stay   + win : {tally['stay_win']:>6,}     stay   + lose: {tally['stay_lose']:>6,}")
    print(f"  switch + win : {tally['switch_win']:>6,}     switch + lose: {tally['switch_lose']:>6,}")
    print(f"  stay   win rate: {stay_rate:.4f} +/- {margin_of_error(stay_rate, stayers):.4f}  (theory 0.3333)")
    print(f"  switch win rate: {switch_rate:.4f} +/- {margin_of_error(switch_rate, switchers):.4f}  (theory 0.6667)")

    show_sizes = [2, 4, 6, 10, 16, 24, 32, 50, 64, 100, 150, 200]
    print("\nRepeating 500 whole shows at each size: how often does switch actually beat stay?")
    beat_rates = check_by_repeating_shows(rng, show_sizes)
    for size, rate in zip(show_sizes, beat_rates):
        print(f"  {size:>4} contestants: switch beat stay in {100 * rate:5.1f}% of shows")

    contestants = range(1, total_contestants + 1)
    figure, axes = plt.subplots(2, 2, figsize=(13, 9))

    counts_plot = axes[0][0]
    for key, label, style in [("stay_win", "stay + win", "b-"), ("stay_lose", "stay + lose", "b:"),
                              ("switch_win", "switch + win", "r-"), ("switch_lose", "switch + lose", "r:")]:
        counts_plot.plot(contestants, history[key], style, label=label)
    counts_plot.set_title("Running count of each outcome")
    counts_plot.set_xlabel("contestants so far")
    counts_plot.set_ylabel("count")
    counts_plot.legend()

    share_plot = axes[0][1]
    for key, label, style, theory in [("stay_win", "stay + win", "b-", 1 / 6),
                                      ("stay_lose", "stay + lose", "b:", 1 / 3),
                                      ("switch_win", "switch + win", "r-", 1 / 3),
                                      ("switch_lose", "switch + lose", "r:", 1 / 6)]:
        share = [c / n for c, n in zip(history[key], contestants)]
        share_plot.plot(contestants, share, style, label=f"{label} (theory {theory:.3f})")
    share_plot.set_xscale("log")
    share_plot.set_title("Share of ALL contestants in each bucket")
    share_plot.set_xlabel("contestants so far (log scale)")
    share_plot.set_ylabel("fraction of contestants")
    share_plot.legend(fontsize=8)

    rate_plot = axes[1][0]
    for strategy, color, theory in [("stay", "blue", 1 / 3), ("switch", "red", 2 / 3)]:
        rates, lows, highs, xs = [], [], [], []
        for n, w, l in zip(contestants, history[f"{strategy}_win"], history[f"{strategy}_lose"]):
            played = w + l
            if played == 0:
                continue
            p = w / played
            m = margin_of_error(p, played)
            xs.append(n); rates.append(p); lows.append(p - m); highs.append(p + m)
        rate_plot.plot(xs, rates, color=color, label=f"{strategy} win rate")
        rate_plot.fill_between(xs, lows, highs, color=color, alpha=0.15)
        rate_plot.axhline(theory, color=color, linestyle="--", linewidth=0.8)
    rate_plot.set_xscale("log")
    rate_plot.set_ylim(-0.05, 1.05)
    rate_plot.set_title("Win rate with 95% band: when do the bands stop overlapping?")
    rate_plot.set_xlabel("contestants so far (log scale)")
    rate_plot.set_ylabel("win rate")
    rate_plot.legend()

    confidence_plot = axes[1][1]
    confidence_plot.plot(show_sizes, [100 * r for r in beat_rates], "o-", color="purple")
    confidence_plot.axhline(95, color="gray", linestyle="--", label="95%")
    confidence_plot.set_title("500 repeated shows: % where switch beat stay")
    confidence_plot.set_xlabel("contestants per show")
    confidence_plot.set_ylabel("% of shows")
    confidence_plot.set_ylim(0, 105)
    confidence_plot.legend()

    figure.tight_layout()
    figure.savefig("monty_hall_monte_carlo.png", dpi=150)
    print("\nSaved graph to monty_hall_monte_carlo.png")
    plt.show()


if __name__ == "__main__":
    main()