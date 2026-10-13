"""
stars_and_bars.py
─────────────────────────────────────────────────────────────────────────────
A story about Stars and Bars — one of the most beautiful tricks in
combinatorics. We start with a handful of cookies and two jars, and
end up with a formula that handles millions of possibilities instantly.

Press Enter at each pause to move through the story.
─────────────────────────────────────────────────────────────────────────────
"""

import math
import itertools

# ─────────────────────────────────────────────────────────────────────────────
#  DISPLAY HELPERS
# ─────────────────────────────────────────────────────────────────────────────

STAR = "★"
BAR  = "│"

def line(char="─", width=72):
    print(char * width)

def section(title):
    print()
    line("═")
    print(f"  {title}")
    line("═")
    print()

def pause():
    input("  [ Press Enter to continue ]\n")

def make_symbols(star_positions, total):
    """Build the symbol list: STAR at chosen positions, BAR everywhere else."""
    syms = [BAR] * total
    for p in star_positions:
        syms[p] = STAR
    return syms

def bins_from_symbols(symbols):
    """
    Read a symbol list left-to-right.
    Count stars between each pair of bars → one count per bin.
    """
    bins   = []
    count  = 0
    for s in symbols:
        if s == STAR:
            count += 1
        else:               # it's a BAR — end of this bin
            bins.append(count)
            count = 0
    bins.append(count)      # last bin has no bar after it, add manually
    return bins

def all_arrangements(n_bins, k_stars):
    """Return every (symbol_string, bin_counts) pair for n bins and k stars."""
    bars  = n_bins - 1
    total = k_stars + bars
    results = []
    for positions in itertools.combinations(range(total), k_stars):
        syms   = make_symbols(positions, total)
        counts = bins_from_symbols(syms)
        sym_str = " ".join(syms)
        results.append((sym_str, counts))
    return results

def show_arrangements(arrangements, bin_labels=None, indent="    "):
    """Pretty-print arrangements, optionally translating counts to labels."""
    for sym_str, counts in arrangements:
        if bin_labels:
            parts = [f"{c}×{bin_labels[i]}" for i, c in enumerate(counts) if c > 0]
            label = "  +  ".join(parts) if parts else "(all zeros)"
            print(f"{indent}{sym_str}     →   {label}")
        else:
            count_str = ", ".join(str(c) for c in counts)
            print(f"{indent}{sym_str}     →   bins: [{count_str}]")


# ─────────────────────────────────────────────────────────────────────────────
#  CHAPTER 1 — THE SIMPLEST POSSIBLE PROBLEM
# ─────────────────────────────────────────────────────────────────────────────

section("CHAPTER 1 — The Simplest Possible Problem  (2 jars, 3 cookies)")

print("""
  Imagine you have THREE identical chocolate chip cookies and TWO jars.
  Maybe one jar for eating now, one for saving for later.

  The cookies are IDENTICAL — one chip cookie looks just like another.
  The only thing that matters is HOW MANY end up in each jar.

  Question: How many ways can you split 3 cookies between 2 jars?

  Let's just list them — this is small enough to count by hand:

       Jar A     Jar B
       ──────    ──────
         3         0        (all three in Jar A)
         2         1        (two in A, one in B)
         1         2        (one in A, two in B)
         0         3        (all three in Jar B)

  Answer: 4 ways.  Easy.

  But what if we had 9 cookie flavors and 3 cookies to place?
  Or 20 flavors and 10 cookies?  Listing by hand becomes impossible.
  We need a smarter way to count — and that's what this story is about.
""")

pause()


# ─────────────────────────────────────────────────────────────────────────────
#  CHAPTER 2 — GIVE THE THINGS NAMES (symbols appear)
# ─────────────────────────────────────────────────────────────────────────────

section("CHAPTER 2 — Give the Things Names")

print(f"""
  Here's the key move. Instead of drawing a table, we represent
  each split using only two symbols:

       {STAR}  =  one cookie  (a "star")
       {BAR}  =  a wall between jars  (a "bar")

  The rule:
       Stars to the LEFT of the bar  →  those cookies go into Jar A.
       Stars to the RIGHT of the bar →  those cookies go into Jar B.
       The bar itself is not a cookie — it is just a divider.

  Let's re-write our 4 splits using symbols:

       Jar A=3, Jar B=0     ★ ★ ★ │        (all stars left of the wall)
       Jar A=2, Jar B=1     ★ ★ │ ★        (two left, one right)
       Jar A=1, Jar B=2     ★ │ ★ ★        (one left, two right)
       Jar A=0, Jar B=3     │ ★ ★ ★        (all stars right of the wall)

  Look at what we built: every split is an arrangement of
  3 stars and 1 bar in a row of 4 positions.

  Counting splits is EXACTLY THE SAME as asking:
       "Which 3 of the 4 positions get a star?"

  That's a combination problem we already know how to solve:

       C(4, 3)  =  4! / (3! × 1!)  =  4   ✓

  Let's verify with Python — generating every possible arrangement:
""")

arr_2_3 = all_arrangements(2, 3)
show_arrangements(arr_2_3, indent="       ")
print(f"\n  Python count: {len(arr_2_3)}  ✓  Same as our table.\n")

pause()


# ─────────────────────────────────────────────────────────────────────────────
#  CHAPTER 3 — WHY EXACTLY (n-1) BARS?
# ─────────────────────────────────────────────────────────────────────────────

section("CHAPTER 3 — Why Exactly (n-1) Bars?")

print(f"""
  With 2 jars we needed 1 bar.  What about 3 jars?  9 jars?

  Think of the jars like rooms in a row, and bars like the walls
  between them.  Draw it out:

       2 jars:    [ Jar A  {BAR}  Jar B ]                       → 1 wall
       3 jars:    [ Jar A  {BAR}  Jar B  {BAR}  Jar C ]              → 2 walls
       4 jars:    [ Jar A  {BAR}  Jar B  {BAR}  Jar C  {BAR}  Jar D ]     → 3 walls
       n jars:    [ Jar 1  {BAR}  Jar 2  {BAR}  . . .  {BAR}  Jar n ]     → n-1 walls

  You always need ONE FEWER wall than you have rooms.
  (A hotel with 10 rooms has 9 interior walls between them.)

  So the TOTAL number of symbols in our string is always:

       Total symbols  =  k stars  +  (n - 1) bars
                      =  k + n - 1

  For our 2-jar, 3-cookie example:
       Total = 3 + (2 - 1) = 3 + 1 = 4 symbols   ✓

  For 3 jars and 2 cookies:
       Total = 2 + (3 - 1) = 2 + 2 = 4 symbols
  (same total, different breakdown — different answer, as we'll see)
""")

pause()


# ─────────────────────────────────────────────────────────────────────────────
#  CHAPTER 4 — THREE JARS (things get richer)
# ─────────────────────────────────────────────────────────────────────────────

section("CHAPTER 4 — Three Jars  (n=3 bins, k=2 cookies)")

print(f"""
  Let's try 3 jars and 2 cookies.

  We have:  k=2 stars,  n=3 jars → 2 bars
  Total symbols: 2 + 2 = 4

  Question: which 2 of the 4 positions get a star?
       C(4, 2) = 4! / (2! × 2!) = 6

  Let's list all 6 and translate them:
""")

arr_3_2 = all_arrangements(3, 2)
show_arrangements(arr_3_2, bin_labels=["Jar A", "Jar B", "Jar C"], indent="       ")

print(f"""
  Total: {len(arr_3_2)} arrangements   ✓

  Notice what opened up compared to the 2-jar problem:
  Now we can have splits like (1,1,0) and (0,1,1) — one cookie
  in each of two different jars — which simply wasn't possible
  when we only had 2 jars.

  More jars = more possible splits = bigger answer.
  The formula keeps track of all of that automatically.
""")

pause()


# ─────────────────────────────────────────────────────────────────────────────
#  CHAPTER 5 — THE FORMULA LOCKS IN
# ─────────────────────────────────────────────────────────────────────────────

section("CHAPTER 5 — The Formula Locks In")

print("""
  Every time we chose stars and bars, we were asking the same question:

       "Which k positions out of (k + n - 1) total get a star?"

  That's a combination.  The formula is:

       ┌─────────────────────────────────────────────────────────┐
       │                                                         │
       │           ⎛  k + n - 1  ⎞        (k + n - 1)!         │
       │   Ways  = ⎜             ⎟  =   ─────────────────       │
       │           ⎝      k      ⎠          k! × (n-1)!         │
       │                                                         │
       └─────────────────────────────────────────────────────────┘

  Let's watch it grow as we scale n and k up:
""")

print(f"  {'n bins':>8}  {'k stars':>8}  {'total syms':>11}  {'formula':>12}  {'answer':>8}")
line()

cases = [
    (2, 1, "smallest possible"),
    (2, 2, ""),
    (2, 3, "our jar story"),
    (3, 2, "three jars"),
    (3, 3, ""),
    (4, 3, ""),
    (9, 3, "← our cookie problem"),
    (9, 10, "← bigger batch"),
]

for n, k, note in cases:
    total   = k + n - 1
    count   = math.comb(total, k)
    formula = f"C({total},{k})"
    tag     = f"   {note}" if note else ""
    print(f"  {n:>8}  {k:>8}  {total:>11}  {formula:>12}  {count:>8,}{tag}")

print(f"""
  See how quickly the numbers grow?
  The formula handles all of it — no tables, no listing, just math.
""")

pause()


# ─────────────────────────────────────────────────────────────────────────────
#  CHAPTER 6 — BACK TO THE COOKIE BAKERY  (n=9, k=3)
# ─────────────────────────────────────────────────────────────────────────────

section("CHAPTER 6 — Back to the Cookie Bakery  (n=9 flavors, k=3 per batch)")

cookies = [
    "Peanut Butter",
    "Raspberry White Choc",
    "Chocolate Chip",
    "Macadamia Nut",
    "Sugar Cookie",
    "Snickerdoodle",
    "PB Choc Chip",
    "S'mores Cookie",
    "Twix Ice Cream",
]

n_cookies = len(cookies)
k_batch   = 3
bars      = n_cookies - 1
total_sym = k_batch + bars

print(f"""
  Now we swap "jars" for "cookie flavor bins":

       Bin 1:  Peanut Butter
       Bin 2:  Raspberry White Choc
       Bin 3:  Chocolate Chip
       Bin 4:  Macadamia Nut
       Bin 5:  Sugar Cookie
       Bin 6:  Snickerdoodle
       Bin 7:  PB Choc Chip
       Bin 8:  S'mores Cookie
       Bin 9:  Twix Ice Cream

  Each ★ represents one cookie slot landing in a flavor bin.
  The │ bars separate the bins from each other.

  Our star-bar string has:
       {k_batch} stars  +  {bars} bars  =  {total_sym} symbols total

  An example string for the batch  "1 PB + 2 Choc Chip":

       ★ │ │ ★ ★ │ │ │ │ │ │
       ^       ^ ^
      PB  Rasp  Choc  Mac  Sugar  Sndl  PBChoc  Smores  Twix

  Reading it: 1 star before bar 1 → 1 PB cookie
              0 stars before bar 2 → 0 Raspberry
              2 stars before bar 3 → 2 Chocolate Chip
              0 stars in all remaining bins → all others empty

  The formula:  C({total_sym}, {k_batch}) = {math.comb(total_sym, k_batch)}  unique batches
""")

pause()

print("  Here are some real arrangements translated into cookie batches:\n")

all_batches = all_arrangements(n_cookies, k_batch)

# Show a curated mix: multi-flavor batches
print("  ── Multi-flavor batches (the interesting ones) ──\n")
shown = 0
for sym_str, counts in all_batches:
    n_flavors_used = sum(1 for c in counts if c > 0)
    if n_flavors_used >= 2 and shown < 5:
        parts = [f"{c}×{cookies[i]}" for i, c in enumerate(counts) if c > 0]
        print(f"       {sym_str}")
        print(f"           →  {'  +  '.join(parts)}\n")
        shown += 1

# Show all "triple of one flavor" batches
print("  ── All-one-flavor batches (repeats really do count here!) ──\n")
triple_shown = 0
for sym_str, counts in all_batches:
    n_flavors_used = sum(1 for c in counts if c > 0)
    if n_flavors_used == 1 and triple_shown < 4:
        parts = [f"{c}×{cookies[i]}" for i, c in enumerate(counts) if c > 0]
        print(f"       {sym_str}")
        print(f"           →  {'  +  '.join(parts)}\n")
        triple_shown += 1
print(f"       ... plus {n_cookies - triple_shown} more triple-of-one-flavor batches (one per person)\n")

pause()


# ─────────────────────────────────────────────────────────────────────────────
#  CHAPTER 7 — THE BIG PICTURE
# ─────────────────────────────────────────────────────────────────────────────

section("CHAPTER 7 — The Big Picture")

c1 = math.comb(9, 3)
c2 = math.perm(9, 3)
c3 = math.comb(11, 3)
c4 = 9**3

print(f"""
  Stars and Bars answers one specific question:

       "How many ways can I choose k items from n types
        when ORDER does not matter and REPEATS are allowed?"

  And the answer is always:

       C(n + k - 1, k)

  Here's why the translation works — step by step:

       A batch of cookies with repeats
           ↕  is the same thing as
       A distribution of k cookies into n flavor bins
           ↕  is the same thing as
       An arrangement of k stars and (n-1) bars
           ↕  is the same thing as
       A choice of k positions out of (k + n - 1) total
           ↕  is the same thing as
       C(k + n - 1, k)

  Each arrow is a perfect one-to-one translation.  Nothing is added,
  nothing is lost.  That's why the formula works — it's not a trick,
  it's a restatement of the same problem in a language we already know.

  ─────────────────────────────────────────────────────────────────────
  WHERE STARS AND BARS FITS IN OUR FOUR-CASE MAP  (n=9, k=3):
  ─────────────────────────────────────────────────────────────────────

  ┌──────────────────────────┬──────────────┬──────────────┐
  │                          │  No Repeats  │  Repeats OK  │
  ├──────────────────────────┼──────────────┼──────────────┤
  │  Order does NOT matter   │  C(9,3)={c1:>4} │  C(11,3)={c3:>3} │
  │  (Combination)           │              │  ← Stars & Bars  │
  ├──────────────────────────┼──────────────┼──────────────┤
  │  Order DOES matter       │  P(9,3)={c2:>4} │  9³   ={c4:>4} │
  │  (Permutation)           │              │              │
  └──────────────────────────┴──────────────┴──────────────┘

  Stars and Bars is what fills in that bottom-left cell.
  Without it, Case 3 has no clean formula.
  With it, all four cases are covered and the picture is complete.

  ─────────────────────────────────────────────────────────────────────
  ONE LAST THING TO NOTICE:
  ─────────────────────────────────────────────────────────────────────

  Compare Case 1 and Case 3:

       Case 1 — no repeats:   C(9, 3)     = {c1}   batches
       Case 3 — repeats OK:   C(11, 3)    = {c3}   batches

  The only difference in the formula is  n=9  becomes  n+k-1=11.
  Those 2 extra positions in the "choose from" pool are exactly
  the room the repeated choices need.  Beautiful, right?

  That's Stars and Bars.  🌟
""")

line()
print("  Thanks for counting with us.  🍪\n")
line()
