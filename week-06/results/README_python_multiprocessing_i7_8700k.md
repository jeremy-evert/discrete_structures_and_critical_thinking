# Alternate Week 6 parallel-sort evidence: Python multiprocessing, i7-8700K

A second, independent measurement kept apart from `parallel_sort_results.csv`
(GNU/OpenMP on a different CPU). The hosts and algorithms differ, so the two
datasets are not combined or compared directly.

- Script: `../scripts/07_parallel_sort_cpu.py` (chunk sort in worker processes, then merge)
- Results: `python_multiprocessing_i7_8700k_results.csv`
- Hardware/method: `python_multiprocessing_i7_8700k_hardware.txt` (12 logical threads, no CUDA)
- Regenerate: `python3 week-06/scripts/07_parallel_sort_cpu.py --output <csv> --threads 12`
