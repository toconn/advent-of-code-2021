#!/usr/bin/env python3

from py_shared import *

DAY = 3;
PART = 1;

# Solution ─────────────────────────────────────────────────────────────────── #

def solve(lines):
	return sum([score_duplicate(line) for line in lines])

def score(letter):
	return ord(letter) - (96 if letter > 'Z' else 38)

def score_duplicate(line):

	split = len(line)//2
	first, second = line[:split], line[split:]

	for letter in first:
		if second.find(letter) >= 0:
			return score(letter)

	print ('  Not found', line, first, second)
	nl()

# Main ─────────────────────────────────────────────────────────────────────── #

run_test(DAY, PART, solve)
run_actual(DAY, PART, solve)
