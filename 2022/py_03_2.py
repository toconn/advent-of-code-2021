#!/usr/bin/env python3

from py_shared import *

DAY = 3;
PART = 2;

# Solution ─────────────────────────────────────────────────────────────────── #

SCORE = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solve(lines):
	return sum([score(duplicates(first, second, third)) for first, second, third in every_3_lines(lines)])

def every_3_lines(lines):
	for i in range(0, len(lines), 3):
		yield lines[i], lines[i+1], lines[i+2]

def duplicates(first, second, third):
	return set(first) & set(second) & set(third)

def score(match_set):
	letter = next(iter(match_set))
	return SCORE.find(letter)

# Main ─────────────────────────────────────────────────────────────────────── #

# run_test(DAY, PART, solve)
run_test_and_actual(DAY, PART, solve)
