#!/usr/bin/env python3

from py_shared import *

DAY = 3;
PART = 1;

# Solution ─────────────────────────────────────────────────────────────────── #

SCORE = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def solve(lines):
	return sum([score_duplicate(line) for line in lines])

def score_duplicate(line):

	split = len(line)//2
	first, second = line[:split], line[split:]

	for letter in first:
		if letter in second:
			return SCORE.find(letter)

	print ("  Not found", line, first, second)
	nl()

# Main ─────────────────────────────────────────────────────────────────────── #

run_test(DAY, PART, solve)
run_actual(DAY, PART, solve)
