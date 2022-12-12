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

def is_cd_up(value):
	return value =='$ cd ..'

def is_size(value):
	return match(r'^\d+', value)

def total_subdirectories(lines):

	total = 0
	size = 0

	try:

		while (line := next(lines)):

			if is_cd_down(line):
				subdir_size, subdir_total = total_subdirectories(lines)
				size += subdir_size
				total += subdir_total

			elif is_size(line):
				size += int(line.split()[0])

			elif is_cd_up(line):
				break

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
