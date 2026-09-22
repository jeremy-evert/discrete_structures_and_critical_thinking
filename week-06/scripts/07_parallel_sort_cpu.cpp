// Week 6: CPU sequential vs parallel sort benchmark.
//
// Sequential path: std::sort
// Parallel path: GNU libstdc++ parallel multiway mergesort using OpenMP.
//
// Compile:
//   g++ -O3 -std=c++17 -fopenmp 07_parallel_sort_cpu.cpp -o parallel_sort_cpu
//
// This deliberately times sorting only. Input generation and vector copying happen
// outside the timer so we can discuss algorithm/runtime overhead separately. Tiny
// inputs are batched into one timed sample; the reported value is milliseconds per
// sort, which avoids teaching from a single clock-tick-sized measurement.

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <parallel/algorithm>
#include <parallel/tags.h>
#include <random>
#include <stdexcept>
#include <string>
#include <thread>
#include <vector>
#include <omp.h>

using Clock = std::chrono::steady_clock;

static std::vector<std::size_t> sizes() {
    return {10, 100, 1000, 10000, 100000, 1000000, 5000000, 10000000};
}

static std::vector<std::uint32_t> make_data(std::size_t n, std::uint32_t seed) {
    std::mt19937 rng(seed);
    std::uniform_int_distribution<std::uint32_t> dist;
    std::vector<std::uint32_t> values(n);
    for (auto &v : values) v = dist(rng);
    return values;
}

static int repeats_for(std::size_t n, int base) {
    if (n <= 1000) return std::max(base, 51);
    if (n <= 10000) return std::max(base, 11);
    return base;
}

static int sorts_per_timed_sample(std::size_t n) {
    if (n <= 10) return 10000;
    if (n <= 100) return 1000;
    if (n <= 1000) return 100;
    if (n <= 10000) return 10;
    return 1;
}

template <typename F>
static double median_ms(
    const std::vector<std::uint32_t>& source,
    const std::vector<std::uint32_t>& expected,
    int repeats,
    int sorts_per_sample,
    F sorter
) {
    std::vector<double> times;
    times.reserve(repeats);

    for (int r = 0; r < repeats; ++r) {
        // Source-vector preparation is deliberately outside the timed region.
        std::vector<std::vector<std::uint32_t>> work(
            static_cast<std::size_t>(sorts_per_sample), source
        );

        const auto t0 = Clock::now();
        for (auto& item : work) sorter(item);
        const auto t1 = Clock::now();

        for (const auto& item : work) {
            // Equality to a separately sorted reference confirms both ordering
            // and preservation of the complete input multiset.
            if (item != expected) {
                throw std::runtime_error("sort produced incorrect output");
            }
        }

        times.push_back(
            std::chrono::duration<double, std::milli>(t1 - t0).count() /
            static_cast<double>(sorts_per_sample)
        );
    }

    std::sort(times.begin(), times.end());
    return times[times.size() / 2];
}

int main(int argc, char** argv) {
    std::string output = "parallel_sort_results.csv";
    int threads = std::min(16, std::max(2, omp_get_max_threads()));
    int base_repeats = 3;

    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];

        if (arg == "--output" && i + 1 < argc) {
            output = argv[++i];
        } else if (arg == "--threads" && i + 1 < argc) {
            threads = std::max(2, std::stoi(argv[++i]));
        } else if (arg == "--repeats" && i + 1 < argc) {
            base_repeats = std::max(1, std::stoi(argv[++i]));
        } else {
            std::cerr
                << "Usage: " << argv[0]
                << " [--output FILE] [--threads N] [--repeats N]\n";
            return 2;
        }
    }

    std::ofstream out(output);
    if (!out) {
        std::cerr << "Could not open " << output << " for writing.\n";
        return 1;
    }

    out << "backend,n,workers,median_ms,timed_sorts\n";
    out << std::fixed << std::setprecision(6);

    std::cerr << "CPU hardware threads reported: "
              << std::thread::hardware_concurrency() << "\n";
    std::cerr << "OpenMP max threads: " << omp_get_max_threads() << "\n";
    std::cerr << "Parallel workers requested: " << threads << "\n";

    // Warm both code paths before collecting measurements.
    auto warm = make_data(20000, 7);
    auto warm_seq = warm;
    std::sort(warm_seq.begin(), warm_seq.end());

    auto warm_par = warm;
    __gnu_parallel::sort(
        warm_par.begin(),
        warm_par.end(),
        std::less<std::uint32_t>(),
        __gnu_parallel::multiway_mergesort_tag(threads)
    );

    for (const auto n : sizes()) {
        const int repeats = repeats_for(n, base_repeats);
        std::cerr << "n=" << n << " (" << repeats << " repeats) ...\n";

        const auto source =
            make_data(n, static_cast<std::uint32_t>(0xC0FFEEu + n));
        auto expected = source;
        std::sort(expected.begin(), expected.end());
        const int sorts_per_sample = sorts_per_timed_sample(n);

        const double sequential = median_ms(
            source,
            expected,
            repeats,
            sorts_per_sample,
            [](auto& work) {
                std::sort(work.begin(), work.end());
            }
        );

        const double parallel = median_ms(
            source,
            expected,
            repeats,
            sorts_per_sample,
            [threads](auto& work) {
                __gnu_parallel::sort(
                    work.begin(),
                    work.end(),
                    std::less<std::uint32_t>(),
                    __gnu_parallel::multiway_mergesort_tag(threads)
                );
            }
        );

        out << "cpu_sequential," << n << ",1," << sequential << ","
            << sorts_per_sample << "\n";
        out << "cpu_parallel," << n << "," << threads << "," << parallel
            << "," << sorts_per_sample << "\n";
        out.flush();

        std::cerr
            << "  sequential " << sequential << " ms"
            << " | parallel " << parallel << " ms"
            << " | speedup " << (sequential / parallel) << "x"
            << " | timed sorts/sample " << sorts_per_sample << "\n";
    }

    std::cerr << "Wrote " << output << "\n";
    return 0;
}
