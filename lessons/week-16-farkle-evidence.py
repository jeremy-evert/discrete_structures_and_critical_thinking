#!/usr/bin/env python3
"""Thin DSCT-facing runner over the canonical shared Farkle package.

This file contains no Farkle rules, learner, or simulator. Those arrive through
the generated ``lessons/vendor/farkle_ml`` package synchronized from the shared
repository.
"""

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
VENDOR_ROOT = ROOT / "lessons" / "vendor"
PACKAGE_DIR = VENDOR_ROOT / "farkle_ml"
PROVENANCE = PACKAGE_DIR / "_SHARED_PROVENANCE.json"


def require_shared_package():
    if not PACKAGE_DIR.exists() or not PROVENANCE.exists():
        raise RuntimeError(
            "shared Farkle package is not synchronized. From a current "
            "Farkle_and_Machine_Learning checkout run:\n"
            "  python scripts/sync_consumer.py "
            "../discrete_structures_and_critical_thinking/lessons/vendor/farkle_ml --apply"
        )

    if str(VENDOR_ROOT) not in sys.path:
        sys.path.insert(0, str(VENDOR_ROOT))

    provenance = json.loads(PROVENANCE.read_text(encoding="utf-8"))
    return provenance


def print_result(result):
    print(
        f"{result.strategy_a} vs {result.strategy_b} | "
        f"games={result.games} seed={result.seed}"
    )
    print(
        f"starts A/B={result.starts_a}/{result.starts_b} | "
        f"wins A/B/ties={result.wins_a}/{result.wins_b}/{result.ties}"
    )
    print(
        f"win rate A={result.win_rate_a:.1%} | "
        f"B={result.win_rate_b:.1%} | "
        f"A-B={result.win_rate_difference_pp:+.2f} percentage points"
    )
    print(
        f"avg score A/B={result.avg_score_a:.1f}/{result.avg_score_b:.1f} | "
        f"farkle/own-turn A/B={result.farkle_rate_a:.1%}/{result.farkle_rate_b:.1%}"
    )


def run_initial(args, provenance):
    from farkle_ml.experiment import ExperimentConfig, run_experiment, save_csv, save_json

    config = ExperimentConfig(
        strategy_a=args.strategy_a,
        strategy_b=args.strategy_b,
        games=args.games,
        seed=args.seed,
        execution_context="dsct-course-runner",
    )
    result = run_experiment(config)

    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = save_json(result, out_dir / "initial_result.json")
    csv_path = save_csv([result], out_dir / "initial_result.csv")
    (out_dir / "shared_provenance.json").write_text(
        json.dumps(provenance, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print_result(result)
    print(f"saved JSON: {json_path}")
    print(f"saved CSV:  {csv_path}")


def optional_plot(results, out_dir):
    try:
        import matplotlib.pyplot as plt
    except Exception as exc:
        print(f"plot skipped: matplotlib unavailable ({type(exc).__name__})")
        return None

    seeds = [result.seed for result in results]
    differences = [result.win_rate_difference_pp for result in results]
    path = out_dir / "bundle_win_rate_difference.png"

    fig, ax = plt.subplots()
    ax.plot(seeds, differences, marker="o")
    ax.axhline(0, linewidth=1)
    ax.set_xlabel("seed")
    ax.set_ylabel("A minus B win rate (percentage points)")
    ax.set_title("Same matchup across deterministic seed samples")
    fig.tight_layout()
    fig.savefig(path)
    plt.close(fig)
    print(f"saved plot: {path}")
    return path


def run_bundle(args, provenance):
    from farkle_ml.evidence import run_seed_bundle, summarize_metric
    from farkle_ml.experiment import ExperimentConfig, save_csv, save_json

    config = ExperimentConfig(
        strategy_a=args.strategy_a,
        strategy_b=args.strategy_b,
        games=args.games,
        seed=0,
        execution_context="dsct-course-runner",
    )
    results = run_seed_bundle(config, args.bundle)
    summary = summarize_metric(results, "win_rate_difference_pp")

    out_dir = args.out_dir.resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    csv_path = save_csv(results, out_dir / f"{args.bundle}_results.csv")
    for result in results:
        save_json(result, out_dir / f"seed_{result.seed}_result.json")

    summary_path = out_dir / f"{args.bundle}_summary.json"
    summary_path.write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (out_dir / "shared_provenance.json").write_text(
        json.dumps(provenance, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(
        "seed     games  startA startB  winsA winsB ties   winA    winB    A-B pp"
    )
    for result in results:
        print(
            f"{result.seed:<8} {result.games:>5} "
            f"{result.starts_a:>7} {result.starts_b:>6} "
            f"{result.wins_a:>6} {result.wins_b:>5} {result.ties:>4} "
            f"{result.win_rate_a:>7.1%} {result.win_rate_b:>7.1%} "
            f"{result.win_rate_difference_pp:>+8.2f}"
        )

    print()
    print(
        f"A-B pp summary: mean={summary['mean']:+.2f}, "
        f"min={summary['min']:+.2f}, max={summary['max']:+.2f}, "
        f"range={summary['range']:.2f}"
    )
    print(f"saved CSV: {csv_path}")
    print(f"saved summary: {summary_path}")

    if args.plot:
        optional_plot(results, out_dir)


def build_parser():
    parser = argparse.ArgumentParser(
        description="DSCT Week 16 evidence runner over the shared Farkle package."
    )
    parser.add_argument(
        "mode",
        choices=["initial", "bundle"],
        help="run one sample or a named repeated seed bundle",
    )
    parser.add_argument("--strategy-a", default="learner:500")
    parser.add_argument("--strategy-b", default="bank_at_425")
    parser.add_argument("--games", type=int, default=100)
    parser.add_argument("--seed", type=int, default=17)
    parser.add_argument("--bundle", default="classroom_v1")
    parser.add_argument(
        "--out-dir",
        type=Path,
        default=ROOT / "artifacts" / "week16_farkle",
    )
    parser.add_argument(
        "--plot",
        action="store_true",
        help="attempt an optional matplotlib bundle plot if already installed",
    )
    return parser


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.games <= 0:
        print("games must be positive", file=sys.stderr)
        return 2

    try:
        provenance = require_shared_package()
        print(f"shared commit: {provenance.get('shared_commit', 'unknown')}")
        if args.mode == "initial":
            run_initial(args, provenance)
        else:
            run_bundle(args, provenance)
        return 0
    except Exception as exc:
        print(f"FAIL: {type(exc).__name__}: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
