#!/usr/bin/env python3

from day_3_data import *
from shared import *
from dataclasses import dataclass

def parse(data):
	return data.splitlines()

def product(items):
	value = 1
	for item in items:
		value *= item
	return value


TREE = '#'


@dataclass
class Slope:
	right: int
	down: int


def width(data):
	return len(data[0])

def has_tree(data, x, y):
	x_relative = x % width(data)
	return data[y][x_relative] == TREE

def get_count(slope):

	count = 0
	x = 0

	for y in range(slope.down, len(data), slope.down):

		x += slope.right
		if has_tree(data, x, y):
			count += 1

	return count

def get_counts(slopes):
	return [get_count(slope) for slope in slopes]

# Data ########################

data = parse(DATA_TEST)
data = parse(DATA_ACTUAL)



# Part 1 ######################

slope_1 = Slope(3, 1)
count = get_count(slope_1)
print (count)
nl()


# Part 2 ######################

slopes = (
		Slope (1, 1),
		Slope (3, 1),
		Slope (5, 1),
		Slope (7, 1),
		Slope (1, 2))

counts = get_counts(slopes)
print ('counts', counts)
print ('product', product(counts))
nl()


