#!/usr/bin/env python3

from py_shared import *

DAY = 8
PART = 1;

# Solution ─────────────────────────────────────────────────────────────────── #

## Heights Order: [Row][Column]

def solve(lines):

	heights = to_heights(lines)
	rows, columns = len(lines), len(lines[0])
	
	visible = 0
	
	for row in range(1, rows - 1):
		for column in range(1, columns - 1):
			if is_visible_in_row(heights, column, row) or is_visible_in_column(heights, column, row):
				visible += 1

	total = visible + (rows * 2) + (columns * 2) - 4
	return total

def is_visible(height, position, trees):
	return max(trees[:position]) < height or max(trees[position + 1:]) < height

def is_visible_in_column(heights, column, row):
	trees = [line[column] for line in heights]
	return is_visible(heights[row][column], row, trees)

def is_visible_in_row(heights, column, row):
	return is_visible(heights[row][column], column, heights[row])

def to_heights(lines):
	return [[int(height) for height in line] for line in lines]

# Main ─────────────────────────────────────────────────────────────────────── #

run_test(DAY, PART, solve)
run_actual(DAY, PART, solve)
