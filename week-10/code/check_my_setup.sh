#!/bin/sh
# Run this first. It should print "ready" and nothing alarming.
python3 --version || { echo "python3 not found"; exit 1; }
python3 test_screening.py && echo ready
