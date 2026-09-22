// Week 6: optional NVIDIA GPU sort benchmark.
//
// Uses CUDA Thrust. The same data is measured two ways:
//   1. gpu_sort_only   -> data is already on the GPU before timing starts.
//   2. gpu_end_to_end  -> host->GPU copy + sort + GPU->host copy.
//
// The gap between those two lines is part of the lesson.
//
// Compile:
//   nvcc -O3 -std=c++17 08_parallel_sort_gpu.cu -o parallel_sort_gpu

#include <algorithm>
#include <chrono>
#include <cstdint>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <random>
#include <string>
#include <vector>

#include <cuda_runtime.h>
#include <thrust/copy.h>
#include <thrust/device_vector.h>
#include <thrust/sort.h>

using Clock = std::chrono::steady_clock;

struct DeviceLess {
    __host__ __device__
    bool operator()(std::uint32_t a, std::uint32_t b) const {
        return a < b;
    }
};

static void cuda_check(cudaError_t status, const char* where) {
    if (status != cudaSuccess) {
        std::cerr << where << ": " << cudaGetErrorString(status) << "\n";
        std::exit(1);
    }
}

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

static double median(std::vector<double> values) {
    std::sort(values.begin(), values.end());
    return values[values.size() / 2];
}

int main(int argc, char** argv) {
    std::string output = "parallel_sort_results.csv";
    std::string metadata = "parallel_sort_hardware.txt";
    int repeats = 3;

    for (int i = 1; i < argc; ++i) {
        const std::string arg = argv[i];

        if (arg == "--output" && i + 1 < argc) {
            output = argv[++i];
        } else if (arg == "--metadata" && i + 1 < argc) {
            metadata = argv[++i];
        } else if (arg == "--repeats" && i + 1 < argc) {
            repeats = std::max(1, std::stoi(argv[++i]));
        } else {
            std::cerr
                << "Usage: " << argv[0]
                << " [--output FILE] [--metadata FILE] [--repeats N]\n";
            return 2;
        }
    }

    int device = 0;
    cudaDeviceProp props{};
    cuda_check(cudaGetDeviceProperties(&props, device), "cudaGetDeviceProperties");
    cuda_check(cudaSetDevice(device), "cudaSetDevice");

    {
        std::ofstream meta(metadata, std::ios::app);
        meta << "gpu_name=" << props.name << "\n";
        meta << "gpu_sms=" << props.multiProcessorCount << "\n";
        meta << "gpu_memory_bytes=" << props.totalGlobalMem << "\n";
    }

    std::cerr << "GPU: " << props.name << "\n";
    std::cerr << "Streaming multiprocessors: " << props.multiProcessorCount << "\n";

    std::ofstream out(output, std::ios::app);
    if (!out) {
        std::cerr << "Could not open " << output << " for append.\n";
        return 1;
    }
    out << std::fixed << std::setprecision(6);

    // Warm CUDA context and Thrust before measuring anything.
    {
        std::vector<std::uint32_t> warm_host = make_data(20000, 17);
        thrust::device_vector<std::uint32_t> warm_device(warm_host.begin(), warm_host.end());
        thrust::sort(warm_device.begin(), warm_device.end(), DeviceLess{});
        cuda_check(cudaDeviceSynchronize(), "warmup synchronize");
    }

    for (const auto n : sizes()) {
        std::cerr << "GPU n=" << n << " ...\n";

        const auto source =
            make_data(n, static_cast<std::uint32_t>(0xC0FFEEu + n));

        thrust::device_vector<std::uint32_t> device_values(n);
        std::vector<std::uint32_t> host_output(n);

        std::vector<double> sort_only_times;
        std::vector<double> end_to_end_times;

        for (int r = 0; r < repeats; ++r) {
            // --- GPU SORT ONLY ---
            // Copy happens BEFORE the timer.
            thrust::copy(source.begin(), source.end(), device_values.begin());
            cuda_check(cudaDeviceSynchronize(), "pre-sort copy synchronize");

            const auto sort_t0 = Clock::now();
            thrust::sort(device_values.begin(), device_values.end(), DeviceLess{});
            cuda_check(cudaDeviceSynchronize(), "sort synchronize");
            const auto sort_t1 = Clock::now();

            sort_only_times.push_back(
                std::chrono::duration<double, std::milli>(
                    sort_t1 - sort_t0
                ).count()
            );

            // Verify outside the timer.
            thrust::copy(
                device_values.begin(),
                device_values.end(),
                host_output.begin()
            );
            if (!std::is_sorted(host_output.begin(), host_output.end())) {
                std::cerr << "GPU sort-only result was incorrect.\n";
                return 1;
            }

            // --- END TO END ---
            // The timer includes host->device transfer, sort, and device->host transfer.
            const auto full_t0 = Clock::now();

            thrust::copy(source.begin(), source.end(), device_values.begin());
            thrust::sort(device_values.begin(), device_values.end(), DeviceLess{});
            thrust::copy(
                device_values.begin(),
                device_values.end(),
                host_output.begin()
            );
            cuda_check(cudaDeviceSynchronize(), "end-to-end synchronize");

            const auto full_t1 = Clock::now();

            end_to_end_times.push_back(
                std::chrono::duration<double, std::milli>(
                    full_t1 - full_t0
                ).count()
            );

            if (!std::is_sorted(host_output.begin(), host_output.end())) {
                std::cerr << "GPU end-to-end result was incorrect.\n";
                return 1;
            }
        }

        const double sort_only = median(sort_only_times);
        const double end_to_end = median(end_to_end_times);

        out << "gpu_sort_only," << n << ","
            << props.multiProcessorCount << "," << sort_only << ",1\n";
        out << "gpu_end_to_end," << n << ","
            << props.multiProcessorCount << "," << end_to_end << ",1\n";
        out.flush();

        std::cerr
            << "  sort-only " << sort_only << " ms"
            << " | end-to-end " << end_to_end << " ms\n";
    }

    return 0;
}
