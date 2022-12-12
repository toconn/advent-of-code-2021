#!/usr/bin/env python3

from py_shared import *
from re import split

DAY = 4
PART = 1;

# Solution ─────────────────────────────────────────────────────────────────── #

def solve(lines):
	return [is_fully_contained(line) for line in lines].count(True)

def contains(range_1, range_2):
	return range_1[0] <= range_2[0] and range_1[1] >= range_2[1]

def is_fully_contained(line):
	range_1, range_2 = to_ranges(line)
	return contains(range_1, range_2) or contains(range_2, range_1)

def to_ranges(line):
	r1_min, r1_max, r2_min, r2_max = split('[-,]', line)
	return (int(r1_min), int(r1_max)), (int(r2_min), int(r2_max))
	

# Main ─────────────────────────────────────────────────────────────────────── #

run_test(DAY, PART, solve)
run_actual(DAY, PART, solve)
