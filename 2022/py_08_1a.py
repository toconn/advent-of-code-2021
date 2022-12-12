#!/usr/bin/env python3

from py_shared import *

DAY = 8
PART = 1;

# Solution ─────────────────────────────────────────────────────────────────── #

## Heights Order: [Row][Column]

def solve(lines):

	heights = to_heights(lines)
	visible = 0

	for row_index, row in enumerate(heights):
		for column_index, height in enumerate(row):
			column = [line[column_index] for line in heights]
			visible += iif(
					(all(compare_height < height for compare_height in row[:column_index]) or
					all(compare_height < height for compare_height in row[column_index + 1:]) or
					all(compare_height < height for compare_height in column[:row_index]) or
					all(compare_height < height for compare_height in column[row_index + 1:])),
					1, 0)
				
	return visible

def to_heights(lines):
	return [[int(height) for height in line] for line in lines]

# Main ─────────────────────────────────────────────────────────────────────── #

run_test(DAY, PART, solve)
run_actual(DAY, PART, solve)
