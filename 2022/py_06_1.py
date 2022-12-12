#!/usr/bin/env python3

from py_shared import *

DAY = 6
PART = 1;

# Solution ─────────────────────────────────────────────────────────────────── #

def solve(data):

	index = 0
	letters = [letter for letter in data[0]]

	for index in range(4, len(letters)):

		check = letters[index - 4: index]
		if len(set(check)) == 4:
			return index

	assert False

# Main ─────────────────────────────────────────────────────────────────────── #

# run_test(DAY, PART, solve)
run_test_and_actual(DAY, PART, solve)
