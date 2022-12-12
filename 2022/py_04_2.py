#!/usr/bin/env python3

from py_shared import *
from re import split

DAY = 4
PART = 2;

# Solution ─────────────────────────────────────────────────────────────────── #

def solve(lines):
	return [has_overlap(line) for line in lines].count(True)

def has_overlap(line):
	range_1, range_2 = to_ranges(line)
	return max(range_1[0], range_2[0]) <= min(range_1[1], range_2[1])

def to_ranges(line):
	r1_min, r1_max, r2_min, r2_max = split('[-,]', line)
	return (int(r1_min), int(r1_max)), (int(r2_min), int(r2_max))
	

# Main ─────────────────────────────────────────────────────────────────────── #

run_test(DAY, PART, solve)
run_actual(DAY, PART, solve)
