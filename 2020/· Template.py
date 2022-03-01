#!/usr/bin/env python3

from day_x_data import *
from shared import *
from dataclasses import dataclass


def parse(data):
	return data.splitlines()

def product(items):
	value = 1
	for item in items:
		value *= item
	return value


# Data ########################

data = parse(DATA_TEST)
# data = parse(DATA_ACTUAL)


# Part 1 ######################



# Part 2 ######################


