#!/usr/bin/env python3

from py_shared import *
from re import match

DAY = 7
PART = 1;

# Solution ─────────────────────────────────────────────────────────────────── #

def solve(lines):
	return total_matching_directories(iter(lines))

def is_cd_down(value):
	return match (r'\$ cd [a-zA-Z/]+', value)

def total_subdirectories(lines):

	total = 0
	size = 0

	try:

		while (line := next(lines)):

			match line.split():
				case ("$", "cd", ".."):
					break
				case ("$", "cd", name):
					subdir_size, subdir_total = total_subdirectories(lines)
					size += subdir_size
					total += subdir_total					
				case (file_size, _) if file_size.isdigit():
					size += int(line.split()[0])

	except StopIteration:
		pass

	if size <= 100_000:
		total += size

	return size, total

def total_matching_directories(lines):

	while(line := next(lines)):
		if is_cd_down(line):
			return total_subdirectories(lines)[1]
			
# Main ─────────────────────────────────────────────────────────────────────── #

# run_test(DAY, PART, solve)
run_test_and_actual(DAY, PART, solve)
