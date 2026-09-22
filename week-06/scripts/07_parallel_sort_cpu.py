#!/usr/bin/env python3
"""Measure a real sequential-versus-multiprocess CPU sorting path.

This is the no-compiler fallback for the Week 6 parallelism lesson.  It uses
separate Python processes (not threads) so chunk sorting can really run on
multiple CPU logical processors.  The timed parallel operation includes
dispatching chunks and the final merge: that is intentionally the cost a
caller pays, rather than a flattering but incomplete chunk-sort number.
"""

from __future__ import annotations

import argparse
import csv
import heapq
import math
import multiprocessing as mp
import random
import statistics
import time
from pathlib import Path


SIZES = (32, 256, 2_048, 16_384, 131_072, 1_048_576, 2_097_152)


def sort_chunk(chunk: list[int]) -> list[int]:
    """Worker entry point.  Kept module-level so the pool can pickle it."""
    chunk.sort()
    return chunk


def source_for(n: int) -> list[int]:
    """Deterministic source values: every backend receives the same values."""
    rng = random.Random(0xC0FFEE + n)
    return [rng.getrandbits(32) for _ in range(n)]


def repeats_for(n: int, base: int) -> int:
    """Use enough samples for tiny values without making large runs excessive."""
    if n <= 2_048:
        return max(base, 31)
    if n <= 16_384:
        return max(base, 11)
    if n <= 131_072:
        return max(base, 5)
    return base


def batch_for(n: int) -> int:
    """Keep a tiny-operation sample above timer noise, for both backends."""
    if n <= 32:
        return 3
    if n <= 256:
        return 3
    return 1


def chunks_for(source: list[int], workers: int) -> list[list[int]]:
    chunk_size = math.ceil(len(source) / workers)
    return [source[start : start + chunk_size] for start in range(0, len(source), chunk_size)]


def median_ms(samples: list[float]) -> float:
    return statistics.median(samples) * 1_000


def benchmark_sequential(source: list[int], expected: list[int], repeats: int, batch: int) -> float:
    samples: list[float] = []
    for _ in range(repeats):
        work_items = [list(source) for _ in range(batch)]  # Input preparation is outside timing.
        start = time.perf_counter()
        for work in work_items:
            work.sort()
        samples.append((time.perf_counter() - start) / batch)
        if any(work != expected for work in work_items):
            raise RuntimeError("sequential sort failed its exact-output check")
    return median_ms(samples)


def benchmark_parallel(
    source: list[int], expected: list[int], pool: mp.pool.Pool, workers: int, repeats: int, batch: int
) -> float:
    samples: list[float] = []
    for _ in range(repeats):
        # Just like the sequential list copy, forming source chunks is outside the
        # measured sort.  Sending them to workers, coordinating them, and merging
        # their answers are inside: those are real parallel-sort overheads.
        chunk_batches = [chunks_for(source, workers) for _ in range(batch)]
        start = time.perf_counter()
        results = []
        for chunks in chunk_batches:
            sorted_chunks = pool.map(sort_chunk, chunks)
            results.append(list(heapq.merge(*sorted_chunks)))
        samples.append((time.perf_counter() - start) / batch)
        if any(result != expected for result in results):
            raise RuntimeError("parallel sort failed its exact-output/multiset check")
    return median_ms(samples)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--threads", required=True, type=int)
    parser.add_argument("--repeats", default=3, type=int)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    workers = max(2, args.threads)
    base_repeats = max(1, args.repeats)
    rows: list[dict[str, object]] = []

    # Fork is available on this Linux/WSL teaching host and avoids a first-use
    # interpreter import spike.  The pool remains warm while every measured map
    # and merge still includes the parallel operation's coordination cost.
    context = mp.get_context("fork")
    with context.Pool(processes=workers) as pool:
        warm = source_for(16_384)
        warm_expected = sorted(warm)
        benchmark_sequential(warm, warm_expected, 1, 1)
        benchmark_parallel(warm, warm_expected, pool, workers, 1, 1)

        for n in SIZES:
            repeats = repeats_for(n, base_repeats)
            batch = batch_for(n)
            print(f"n={n:,} ({repeats} median samples × {batch} operations/sample) ...", flush=True)
            source = source_for(n)
            expected = sorted(source)  # Oracle is outside every timed sample.
            sequential = benchmark_sequential(source, expected, repeats, batch)
            parallel = benchmark_parallel(source, expected, pool, workers, repeats, batch)
            rows.extend(
                (
                    {"backend": "cpu_sequential", "n": n, "workers": 1, "median_ms": f"{sequential:.6f}"},
                    {"backend": "cpu_parallel", "n": n, "workers": workers, "median_ms": f"{parallel:.6f}"},
                )
            )
            print(
                f"  sequential {sequential:.3f} ms | parallel {parallel:.3f} ms "
                f"| speedup {sequential / parallel:.3f}x",
                flush=True,
            )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    with temporary.open("w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=("backend", "n", "workers", "median_ms"),
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)
    temporary.replace(args.output)
    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
