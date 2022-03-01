#!/usr/bin/env python3

from day_1_data import *
from shared import *


def parse(data):
	return [int(item) for item in data.splitlines()]

def find_pair(data):
	length = len(data)
	for i in range(length - 1):
		for j in range(i, length):
			if data[i] + data[j] == 2020:
				return data[i], data[j]
	return 0, 0

def find_triple(data):
	length = len(data)
	for i in range(length - 2):
		for j in range(i, length - 1):
			for k in range(j, length):
				if data[i] + data[j] + data[k] == 2020:
					return data[i], data[j], data[k]
	return 0, 0, 0


# data = parse(DATA_TEST)
data = parse(DATA_ACTUAL)

item_1_1, item_1_2 = find_pair(data)
item_2_1, item_2_2, item_2_3 = find_triple(data)

print (item_1_1, item_1_2, item_1_1 + item_1_2, item_1_1 * item_1_2)
nl()
print (item_2_1, item_2_2, item_2_3, item_2_1 + item_2_2 + item_2_3, item_2_1 * item_2_2 * item_2_3)
nl()
