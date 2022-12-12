#!/usr/bin/env python3

from py_shared import *

DAY = 8
PART = 2;

# Solution ─────────────────────────────────────────────────────────────────── #

## Heights Order: [Row][Column]

def solve(lines):

	heights = to_heights(lines)
	rows, columns = len(lines), len(lines[0])
	
	max_score = 0
	
	for row in range(1, rows - 1):
		for column in range(1, columns - 1):
			score = tree_score(heights, column, row, heights[row][column])
			max_score = max(max_score, score)

	return max_score

def score_line(height, trees):
	for i in range(len(trees) - 1):
		if height <= trees[i]:
			return i + 1
	return len(trees)

def to_heights(lines):
	return [[int(height) for height in line] for line in lines]

def tree_score(heights, column, row, height):
	row_trees = heights[row]
	column_trees = [line[column] for line in heights]

	print('r', row_trees[:column], height, row_trees[column + 1:], ':', score_line(height, row_trees[:column][::-1]), score_line(height, row_trees[column + 1:]))
	print('c', column_trees[:row], height, column_trees[row + 1:], ':', score_line(height, column_trees[:row][::-1]), score_line(height, column_trees[row + 1:]))
	nl()

	return (
		score_line(height, row_trees[:column][::-1]) *
		score_line(height, row_trees[column + 1:]) *
		score_line(height, column_trees[:row][::-1]) *
		score_line(height, column_trees[row + 1:]))

# Main ─────────────────────────────────────────────────────────────────────── #

run_test(DAY, PART, solve)
run_actual(DAY, PART, solve)