#!/usr/bin/env python3

from py_shared import *
from dataclasses import dataclass
from re import match

DAY = 7
PART = 2;

TOTAL_SIZE = 70_000_000
FREE_SIZE = 30_000_000

# Types ────────────────────────────────────────────────────────────────────── #

@dataclass
class Directory:
	name: str
	size: int = 0

# Solution ─────────────────────────────────────────────────────────────────── #

def solve(lines):
	directories = directories_with_sizes(iter(lines))
	return find_best_match(directories)

def delete_min_size(directories):
	size_used = directories[-1].size
	remaining = TOTAL_SIZE - size_used
	target = FREE_SIZE - remaining
	return target

def find_best_match(directories):
	
	target = delete_min_size(directories)
	match = None

	for directory in directories:
		if directory.size > target:
			if match is None or match.size > directory.size:
				match = directory

	# print(f'final  {match.name:>12}  size {match.size:>12,}')

	return match.size

def get_next(items):
	value = next(items)
	print (value)
	return value

def directory_name(line):
	return line.split()[2]

def subdirectory_with_sizes(lines, name):

	directory = Directory(name)
	directories = []

	try:

		while (line := next(lines)):

			if is_cd_down(line):
				subdirectories, dir_size = subdirectory_with_sizes(lines, directory_name(line))
				directories.extend(subdirectories)
				directory.size += dir_size

			elif is_size(line):
				directory.size += int(line.split()[0])

			elif is_cd_up(line):
				break

	except StopIteration:
		pass

	directories.append(directory)

	return directories, directory.size

def directories_with_sizes(lines):

	while(line := next(lines)):
		if is_cd_down(line):
			return subdirectory_with_sizes(lines, directory_name(line))[0]

	assert False

def is_cd_down(value):
	return match (r'\$ cd [a-zA-Z/]+', value)

def is_cd_up(value):
	return value =='$ cd ..'

def is_size(value):
	return match(r'^\d+', value)


# Main ─────────────────────────────────────────────────────────────────────── #

# run_test(DAY, PART, solve)
run_test_and_actual(DAY, PART, solve)
