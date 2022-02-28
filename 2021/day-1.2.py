#!/usr/bin/env python3

from data import *
from shared import *

# data = DAY_1_TEST
data = DAY_1_ACTUAL

last = sum(data[0:3])
count = 0

for i in range (1, len(data) - 2):
	next = sum(data[i : i + 3])
	if next > last:
		count += 1

	last = next

print (count)
