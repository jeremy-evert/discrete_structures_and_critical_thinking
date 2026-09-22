// Week 6: CPU sequential vs parallel sort benchmark.
//
// Sequential path: std::sort
// Parallel path: GNU libstdc++ parallel multiway mergesort using OpenMP.
//
// Compile:
//   g++ -O3 -std=c++17 -fopenmp 07_parallel_sort_cpu.cpp -o parallel_sort_cpu
//
// This deliberately times sorting only. Input generation and vector copying happen
// outside the timer so we can discuss algorithm/runtime overhead separately.

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

template <typename F>
static double median_ms(
    const std::vector<std::uint32_t>& source,
    int repeats,
    F sorter
) {
    std::vector<double> times;
    times.reserve(repeats);

    for (int r = 0; r < repeats; ++r) {
        auto work = source;  // outside timer

        const auto t0 = Clock::now();
        sorter(work);
        const auto t1 = Clock::now();

        if (!std::is_sorted(work.begin(), work.end())) {
            throw std::runtime_error("sort produced incorrect output");
        }

        times.push_back(
            std::chrono::duration<double, std::milli>(t1 - t0).count()
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

    out << "backend,n,workers,median_ms\n";
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

        const double sequential = median_ms(
            source,
            repeats,
            [](auto& work) {
                std::sort(work.begin(), work.end());
            }
        );

        const double parallel = median_ms(
            source,
            repeats,
            [threads](auto& work) {
                __gnu_parallel::sort(
                    work.begin(),
                    work.end(),
                    std::less<std::uint32_t>(),
                    __gnu_parallel::multiway_mergesort_tag(threads)
                );
            }
        );

        out << "cpu_sequential," << n << ",1," << sequential << "\n";
        out << "cpu_parallel," << n << "," << threads << "," << parallel << "\n";
        out.flush();

        std::cerr
            << "  sequential " << sequential << " ms"
            << " | parallel " << parallel << " ms"
            << " | speedup " << (sequential / parallel) << "x\n";
    }

    std::cerr << "Wrote " << output << "\n";
    return 0;
}
