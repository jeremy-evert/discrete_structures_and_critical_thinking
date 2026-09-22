7e65eaa0-d4ea-4192-94d1-67862a212607.png
6abcc47f-b569-43ed-b2bd-868fb8be8e2f.png
Pasted text(20260922-171638).txt
Document

a0a129b3-3be8-48b6-b2c4-cd70f0acda6f.png
next. what do we do and what should I say?
👍

Yep, just use python3 on this machine:

python3 02_recursive_fibonacci_60_second_race.py

Then the iterative one:

python3 03_iterative_fibonacci_timing.py

No need to install anything. python is just not aliased here.

okay. is there a bubble sort script?  can we bubble sort like 10 100 1000 or 10000 numbers and graph that?
👍

Yep. I just added a measured Bubble Sort script that does exactly that.

Pull it:

git pull --ff-only

Run:

python3 scripts/04_bubble_sort_timing.py

It Bubble Sorts:

10
100
1,000
10,000

using reverse-sorted input, so Bubble Sort gets its worst-case workout. It prints:

    comparisons

    swaps

    actual elapsed time

    how much slower each 10× increase became

It also generates:

websites/04b_bubble_sort_measured.html

Open that with:

explorer.exe "$(wslpath -w websites/04b_bubble_sort_measured.html)"

What to ask before running it

    “If I make the list 10 times bigger, should it take 10 times longer?”

Let them guess.

Then run it.

The theoretical expectation is that Bubble Sort’s worst-case work grows roughly with n², so a 10× increase in n trends toward about 100× the work.

That should make a very nice bridge from the Big O graph into actual measured pain.

evertj@STF259-CZYC704:~/git/discrete_structures_and_critical_thinking/week-06/scripts$ ls
00_recursive_fibonacci_simple.py          08_parallel_sort_gpu.cu
01_recursive_fibonacci_trace.py           09_build_parallelism_webpage.py
02_recursive_fibonacci_60_second_race.py  10_run_parallelism_showdown.sh
03_iterative_fibonacci_timing.py          11_hanna_parallelism_showdown.sh
04_bubble_sort_timing.py                  12_collect_gpu_parallelism_showdown.sh
07_parallel_sort_cpu.cpp                  __pycache__
evertj@STF259-CZYC704:~/git/discrete_structures_and_critical_thinking/week-06/scripts$ python3 04_bubble_sort_timing.py
BUBBLE SORT: WATCH QUADRATIC WORK GROW
============================================================================
Reverse-sorted input gives Bubble Sort its worst-case workout.

n=    10 | comparisons=          45 | swaps=          45 | time=  0.000006 s
n=   100 | comparisons=       4,950 | swaps=       4,950 | time=  0.000406 s
n= 1,000 | comparisons=     499,500 | swaps=     499,500 | time=  0.044936 s
n=10,000 | comparisons=  49,995,000 | swaps=  49,995,000 | time=  4.851436 s

TIME GROWTH
----------------------------------------------------------------------------
    10 ->    100:    65.99x measured time
   100 ->  1,000:   110.55x measured time
 1,000 -> 10,000:   107.96x measured time

============================================================================
GRAPH WRITTEN TO:
/home/evertj/git/discrete_structures_and_critical_thinking/week-06/websites/04b_bubble_sort_measured.html

STUDENT QUESTION:
When n grows by 10x, why does the work trend toward roughly 100x?
evertj@STF259-CZYC704:~/git/discrete_structures_and_critical_thinking/week-06/scripts$ python3 04_bubble_sort_timing.py
BUBBLE SORT: WATCH QUADRATIC WORK GROW
============================================================================
Reverse-sorted input gives Bubble Sort its worst-case workout.

n=    10 | comparisons=          45 | swaps=          45 | time=  0.000006 s
n=   100 | comparisons=       4,950 | swaps=       4,950 | time=  0.000400 s
n= 1,000 | comparisons=     499,500 | swaps=     499,500 | time=  0.044306 s
n=10,000 | comparisons=  49,995,000 | swaps=  49,995,000 | time=  4.835711 s

TIME GROWTH
----------------------------------------------------------------------------
    10 ->    100:    66.19x measured time
   100 ->  1,000:   110.89x measured time
 1,000 -> 10,000:   109.14x measured time

============================================================================
GRAPH WRITTEN TO:
/home/evertj/git/discrete_structures_and_critical_thinking/week-06/websites/04b_bubble_sort_measured.html

STUDENT QUESTION:
When n grows by 10x, why does the work trend toward roughly 100x?
evertj@STF259-CZYC704:~/git/discrete_structures_and_critical_thinking/week-06/scripts$

make it bigger so we can see htop spin up
👍

Done. I bumped it to:

10
100
1,000
10,000
20,000
30,000

Pull the change:

git pull --ff-only

Then in one terminal:

htop

and in the other:

python3 04_bubble_sort_timing.py

Based on your current 10,000 ≈ 4.8 seconds, rough expectations are:

    20,000 around 20 seconds

    30,000 around 40–45 seconds

The fun part is what htop should show: one core working very hard while the others mostly lounge around.

That gives you a perfect line for class:

    “Look at all these processors, and Bubble Sort is basically making one poor core do the whole job.”

Then we can pivot directly into:

    “What if we let more cores help?”
