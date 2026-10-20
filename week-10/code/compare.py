"""Show exactly what changed between two versions:  python3 compare.py v2 v3

Only the differences are shown. Lines starting with + were added,
lines starting with - were removed. That is the whole lesson.
"""
import difflib
import glob
import sys

if len(sys.argv) != 3:
    sys.exit("usage: python3 compare.py v2 v3")
a, b = (glob.glob(p + "_*.py")[0] for p in sys.argv[1:])
old, new = open(a).read().splitlines(), open(b).read().splitlines()
for line in difflib.unified_diff(old, new, a, b, lineterm="", n=2):
    print(line)
