#!/usr/bin/env python3

from py_shared import *

DAY = 7
PART = 1;

# Solution ─────────────────────────────────────────────────────────────────── #

def solve(lines):

	return sum([sum(sizes) for sizes in sizes_by_directory(lines) if sum(sizes) <= 100_000])

def sizes_by_directory(lines):

	batch = []
	for line in lines:

		if line[0].isdigit():
			batch.append(int(line.split()[0]))

		elif len(batch) > 0:
			yield batch
			batch = []

	if len(batch) > 0:
		yield batch

# Main ─────────────────────────────────────────────────────────────────────── #

run_test(DAY, PART, solve)
# run_test_and_actual(DAY, PART, solve)
