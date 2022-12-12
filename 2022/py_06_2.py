#!/usr/bin/env python3

from py_shared import *

DAY = 6
PART = 2;

# Solution ─────────────────────────────────────────────────────────────────── #

MARKER_LENGTH = 14

def solve(data):

	index = 0
	letters = [letter for letter in data[0]]

	for index in range(MARKER_LENGTH, len(letters)):

		check = letters[index - MARKER_LENGTH: index]
		if len(set(check)) == MARKER_LENGTH:
			return index

	assert False

# Main ─────────────────────────────────────────────────────────────────────── #

# run_test(DAY, PART, solve)
run_test_and_actual(DAY, PART, solve)
