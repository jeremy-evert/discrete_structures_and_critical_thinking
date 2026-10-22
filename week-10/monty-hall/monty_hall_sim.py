#!/usr/bin/env python3
"""Reproducible Monty Hall simulations using the same rules as the HTML demo."""

from __future__ import annotations

import argparse
import itertools
from dataclasses import dataclass

MASK32 = 0xFFFFFFFF


class Mulberry32:
    """The unsigned 32-bit mulberry32 generator, matching the browser version."""

    def __init__(self, seed: int) -> None:
        self.state = seed & MASK32

    def random(self) -> float:
        self.state = (self.state + 0x6D2B79F5) & MASK32
        t = self.state
        t = ((t ^ (t >> 15)) * (t | 1)) & MASK32
        t ^= (t + (((t ^ (t >> 7)) * (t | 61)) & MASK32)) & MASK32
        t &= MASK32
        t ^= t >> 14
        return (t & MASK32) / 4294967296


@dataclass(frozen=True)
class Results:
    games: int
    doors: int
    seed: int
    host_random: bool
    stay_wins: int
    switch_wins: int
    spoiled: int
    variant: str = "standard"
    open_doors: int = 1

    @property
    def counted(self) -> int:
        return self.games - self.spoiled

    @property
    def stay_rate(self) -> float:
        return self.stay_wins / self.counted if self.counted else 0.0

    @property
    def switch_rate(self) -> float:
        return self.switch_wins / self.counted if self.counted else 0.0


def simulate(games: int, seed: int, doors: int = 3, host_random: bool = False,
             variant: str = "standard", open_doors: int = 1) -> Results:
    if games < 1:
        raise ValueError("games must be at least 1")
    if doors < 3:
        raise ValueError("doors must be at least 3")
    if variant not in {"standard", "crawl"}:
        raise ValueError("variant must be standard or crawl")
    if variant == "crawl" and doors != 3:
        raise ValueError("crawl uses exactly 3 doors")
    if not 1 <= open_doors < doors - 1:
        raise ValueError("open_doors must be at least 1 and less than doors - 1")
    rng = Mulberry32(seed)
    stay_wins = switch_wins = spoiled = 0
    for _ in range(games):
        r1, r2, r3 = rng.random(), rng.random(), rng.random()
        car = int(r1 * doors)
        pick = int(r2 * doors)
        others = [door for door in range(doors) if door != pick]
        if variant == "crawl":
            opened = next(d for d in range(doors) if d != pick and d != car)
            other = next(d for d in range(doors) if d not in (pick, opened))
        elif open_doors > 1:
            goats = [d for d in range(doors) if d not in (pick, car)]
            subsets = list(itertools.combinations(goats, open_doors))
            opened_set = set(subsets[int(r3 * len(subsets))])
            remaining = [d for d in range(doors) if d != pick and d not in opened_set]
            other = remaining[int(rng.random() * len(remaining))]
        elif host_random:
            other = others[int(r3 * (doors - 1))]
            if car not in (pick, other):
                spoiled += 1
                continue
        elif car != pick:
            other = car
        else:
            other = others[int(r3 * (doors - 1))]
        stay_wins += pick == car
        switch_wins += other == car
    return Results(games, doors, seed & MASK32, host_random, stay_wins, switch_wins, spoiled, variant, open_doors)


def report(result: Results) -> str:
    mode = result.variant if result.variant != "standard" else ("random host" if result.host_random else "knowing host")
    expected = "1/2 each (conditional on not spoiled)" if result.host_random else (
        f"stay 1/{result.doors}, a specified switch target "
        f"{result.doors - 1}/({result.doors}*{result.doors - 1 - result.open_doors})" if result.open_doors > 1 else
        f"stay 1/{result.doors}, switch {result.doors - 1}/{result.doors}"
    )
    return "\n".join(
        (
            f"Mode: {mode}",
            f"Games: {result.games}  Doors: {result.doors}  Seed: {result.seed}",
            f"Counted games: {result.counted}  Spoiled: {result.spoiled}",
            f"Stay wins: {result.stay_wins} ({result.stay_rate:.6f})",
            f"Switch wins: {result.switch_wins} ({result.switch_rate:.6f})",
            f"Closed form: {expected}",
        )
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--games", type=int, default=10000)
    parser.add_argument("--seed", type=int, default=20261022)
    parser.add_argument("--doors", type=int, default=3)
    parser.add_argument("--host-random", action="store_true")
    parser.add_argument("--variant", choices=("standard", "crawl"), default="standard")
    parser.add_argument("--open", type=int, default=1, dest="open_doors", metavar="K")
    args = parser.parse_args()
    if args.games < 1 or args.doors < 3:
        parser.error("--games must be at least 1 and --doors at least 3")
    try:
        result = simulate(args.games, args.seed, args.doors, args.host_random, args.variant, args.open_doors)
    except ValueError as exc:
        parser.error(str(exc))
    print(report(result))


if __name__ == "__main__":
    main()
